from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1310.bin",                # FileName
        "t1310",                    # MapName
        "t1310",                    # Location
        0x00BD,                     # MapIndex
        "ed7161",
        0x00002000,                 # Flags
        ("t1310", "t1310_1", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 189, 0, 12, 0, 13],
    )

    BuildStringList((
        "t1310",                  # 0
        "塞茜尔",                 # 1
        "莉夏",                   # 2
        "艾莉",                   # 3
        "缇欧",                   # 4
        "芙兰",                   # 5
        "蔡特",                   # 6
        "琪雅",                   # 7
        "修利",                   # 8
        "伊莉娅",                 # 9
        "兰迪",                   # 10
        "诺艾尔",                 # 11
        "瓦吉",                   # 12
        "球",                     # 13
        "梅尔卡瓦",               # 14
        "梅尔卡瓦",               # 15
        "猎兵",                   # 16
        "猎兵",                   # 17
        "猎兵",                   # 18
        "猎兵",                   # 19
        "猎兵",                   # 20
        "猎兵",                   # 21
        "军犬",                   # 22
        "军犬",                   # 23
        "军犬",                   # 24
        "军犬",                   # 25
        "伊丽莎白",               # 26
        "塔帕",                   # 27
        "救生员韦伯",             # 28
        "企鹅",                   # 29
        "企鹅",                   # 30
        "企鹅",                   # 31
        "企鹅",                   # 32
        "企鹅",                   # 33
        "企鹅",                   # 34
        "SE控制",                 # 35
        "bt1310",                 # 36
        "bt1310",                 # 37
        "bt1310",                 # 38
        "bt1320",                 # 39
        "翠雀酒店方向",           # 40
    ))

    ATBonus("ATBonus_7C4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_884", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_888", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_88C", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_890", 2, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_894", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_898", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_89C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_864", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_868", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_86C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_870", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_874", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_878", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_87C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_880", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_8E4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8EC", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F0", 2, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F8", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8FC", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_900", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 2, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C8", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 2, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E0", 0, 0, 180)

    # monster count: 0

    # event battle count: 4

    BattleInfo(
        "BattleInfo_904", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1310", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42001.dat", "ms41902.dat", "ms41902.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", 0, 0, "MonsterBattlePostion_884", "MonsterBattlePostion_864", "ed7540", "ed7453", "ATBonus_7C4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9D0", 0x004A, 255, 6, 45, 3, 3, 30, 0, "bt1320", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42001.dat", "ms41902.dat", "ms41902.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", "ms82002.dat", 0, "MonsterBattlePostion_8E4", "MonsterBattlePostion_864", "ed7540", "ed7453", "ATBonus_7C4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_948", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt1310", 0x00000000, 100, 0, 0, 0,
        (
            ("ms87100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8A4", "MonsterBattlePostion_864", "ed7451", "ed7453", "ATBonus_7C4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_98C", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt1310", 0x00000000, 100, 0, 0, 0,
        (
            ("ms87000.dat", "ms87100.dat", "ms87200.dat", "ms87300.dat", "ms87400.dat", "ms87500.dat", 0, 0, "MonsterBattlePostion_8C4", "MonsterBattlePostion_864", "ed7452", "ed7453", "ATBonus_7C4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch15700.itc",                   # 00
        "chr/ch15600.itc",                   # 01
        "apl/ch51330.itc",                   # 02
        "chr/ch15900.itc",                   # 03
        "apl/ch51329.itc",                   # 04
        "chr/ch16100.itc",                   # 05
        "apl/ch51328.itc",                   # 06
        "apl/ch51316.itc",                   # 07
        "chr/ch15300.itc",                   # 08
        "chr/ch15500.itc",                   # 09
        "chr/ch15400.itc",                   # 0A
        "apl/ch51706.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
        "chr/ch39100.itc",                   # 11
        "chr/ch24800.itc",                   # 12
        "chr/ch23602.itc",                   # 13
        "chr/ch02708.itc",                   # 14
        "apl/ch51338.itc",                   # 15
        "apl/ch51317.itc",                   # 16
        "apl/ch51332.itc",                   # 17
        "apl/ch51347.itc",                   # 18
        "chr/ch00000.itc",                   # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "apl/ch51343.itc",                   # 1C
        "apl/ch51351.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   255, 255, 0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   255, 255, 0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   20,  0,   255, 255, 0,   27,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   29,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(54880,   -2000,   -37700,  0,    385,  0x0, 0,   17,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(-9270,   -1500,   8449,    90,   257,  0x0, 0,   18,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(31920,   -4309,   42560,   90,   261,  0x0, 0,   19,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 33,  -12.380000114440918,   0.0,                   -2.5,                  126.5625,              [0.4000000059604645,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.1111111119389534,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.952000141143799,     -0.0,                  0.5,                   1.0])
    DeclEvent(0x0000, 0, 34,  8.600000381469727,     0.07000000029802322,   -5.0,                  156.25,                [0.4000000059604645,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.440000295639038,    -0.007000000216066837, 1.0,                   1.0])
    DeclEvent(0x0000, 0, 35,  8.949999809265137,     46.0,                  -5.0,                  87.890625,             [0.4000000059604645,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.13333332538604736,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.5799999237060547,   -6.133333206176758,    1.0,                   1.0])
    DeclEvent(0x0000, 0, 37,  26.0,                  -16.0,                 -6.0,                  2304.0,                [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.25,                 1.3333333730697632,    1.2000000476837158,    1.0])

    DeclActor(27000,   -6010,   38000,   1200,    27000,   -4010,   38000,   0x007C, 0,  56, 0x0000)
    DeclActor(-8450,   -1500,   8340,    2000,    -9270,   0,       8450,    0x007E, 0,  14, 0x0000)
    DeclActor(14680,   -6000,   9990,    1200,    14280,   -4500,   9990,    0x007C, 0,  32, 0x0000)
    DeclActor(48500,   -7110,   -16940,  1200,    48500,   -6110,   -16940,  0x007C, 0,  47, 0x0000)
    DeclActor(54330,   -7270,   -2840,   1200,    54330,   -6270,   -2840,   0x007C, 0,  48, 0x0000)
    DeclActor(67070,   -7480,   17930,   1000,    67070,   -6480,   17930,   0x007C, 0,  49, 0x0000)
    DeclActor(39320,   -6780,   26760,   1000,    39320,   -5780,   26760,   0x007C, 0,  50, 0x0000)
    DeclActor(50260,   -7210,   49470,   800,     50260,   -6210,   49470,   0x007C, 0,  51, 0x0000)

    PlaceName(-50.0, 0.0, 0.0, 0x0000, 0x0000, "翠雀酒店方向")

    ChipFrameInfo(3088, 0)                                       # 0

    ScpFunction((
        "Function_0_C10",          # 00, 0
        "Function_1_CC0",          # 01, 1
        "Function_2_D13",          # 02, 2
        "Function_3_D3E",          # 03, 3
        "Function_4_D69",          # 04, 4
        "Function_5_D94",          # 05, 5
        "Function_6_DBF",          # 06, 6
        "Function_7_DDF",          # 07, 7
        "Function_8_DFF",          # 08, 8
        "Function_9_E1F",          # 09, 9
        "Function_10_E3F",         # 0A, 10
        "Function_11_ED1",         # 0B, 11
        "Function_12_EEA",         # 0C, 12
        "Function_13_12D7",        # 0D, 13
        "Function_14_15E5",        # 0E, 14
        "Function_15_15E9",        # 0F, 15
        "Function_16_16CF",        # 10, 16
        "Function_17_1AB1",        # 11, 17
        "Function_18_1D3C",        # 12, 18
        "Function_19_1EFF",        # 13, 19
        "Function_20_20E2",        # 14, 20
        "Function_21_21C8",        # 15, 21
        "Function_22_22E9",        # 16, 22
        "Function_23_23E7",        # 17, 23
        "Function_24_2790",        # 18, 24
        "Function_25_2B0F",        # 19, 25
        "Function_26_2D46",        # 1A, 26
        "Function_27_2EB2",        # 1B, 27
        "Function_28_2F12",        # 1C, 28
        "Function_29_317A",        # 1D, 29
        "Function_30_3608",        # 1E, 30
        "Function_31_36F4",        # 1F, 31
        "Function_32_3A5B",        # 20, 32
        "Function_33_3BB1",        # 21, 33
        "Function_34_3C2E",        # 22, 34
        "Function_35_3C7E",        # 23, 35
        "Function_36_3CCE",        # 24, 36
        "Function_37_3D1D",        # 25, 37
        "Function_38_4EEF",        # 26, 38
        "Function_39_602A",        # 27, 39
        "Function_40_65EA",        # 28, 40
        "Function_41_70E7",        # 29, 41
        "Function_42_88E7",        # 2A, 42
        "Function_43_88FF",        # 2B, 43
        "Function_44_92F9",        # 2C, 44
        "Function_45_ACCF",        # 2D, 45
        "Function_46_AD5A",        # 2E, 46
        "Function_47_B517",        # 2F, 47
        "Function_48_B5A3",        # 30, 48
        "Function_49_B629",        # 31, 49
        "Function_50_B6DC",        # 32, 50
        "Function_51_B77E",        # 33, 51
        "Function_52_B833",        # 34, 52
        "Function_53_BAC6",        # 35, 53
        "Function_54_CA39",        # 36, 54
        "Function_55_CB56",        # 37, 55
        "Function_56_D185",        # 38, 56
        "Function_57_D4B2",        # 39, 57
        "Function_58_10E05",       # 3A, 58
        "Function_59_10E94",       # 3B, 59
        "Function_60_10EAC",       # 3C, 60
        "Function_61_10ED7",       # 3D, 61
        "Function_62_10F02",       # 3E, 62
        "Function_63_10F2D",       # 3F, 63
        "Function_64_10F58",       # 40, 64
        "Function_65_10F83",       # 41, 65
        "Function_66_10FAE",       # 42, 66
        "Function_67_10FD9",       # 43, 67
        "Function_68_11004",       # 44, 68
        "Function_69_1102F",       # 45, 69
        "Function_70_11046",       # 46, 70
        "Function_71_1105B",       # 47, 71
        "Function_72_11070",       # 48, 72
        "Function_73_11085",       # 49, 73
        "Function_74_11165",       # 4A, 74
        "Function_75_11248",       # 4B, 75
        "Function_76_11328",       # 4C, 76
        "Function_77_1140B",       # 4D, 77
        "Function_78_1146F",       # 4E, 78
        "Function_79_114FF",       # 4F, 79
        "Function_80_1158F",       # 50, 80
        "Function_81_116B8",       # 51, 81
        "Function_82_12455",       # 52, 82
        "Function_83_12474",       # 53, 83
        "Function_84_124D4",       # 54, 84
        "Function_85_1250B",       # 55, 85
        "Function_86_12585",       # 56, 86
        "Function_87_125AA",       # 57, 87
        "Function_88_1260F",       # 58, 88
        "Function_89_1262B",       # 59, 89
        "Function_90_1271C",       # 5A, 90
        "Function_91_1283B",       # 5B, 91
        "Function_92_12862",       # 5C, 92
        "Function_93_12889",       # 5D, 93
        "Function_94_128A8",       # 5E, 94
        "Function_95_128C7",       # 5F, 95
        "Function_96_128FF",       # 60, 96
        "Function_97_12937",       # 61, 97
        "Function_98_1296F",       # 62, 98
        "Function_99_12989",       # 63, 99
        "Function_100_12CB6",      # 64, 100
        "Function_101_12D50",      # 65, 101
        "Function_102_13362",      # 66, 102
        "Function_103_134B2",      # 67, 103
        "Function_104_13569",      # 68, 104
        "Function_105_13579",      # 69, 105
        "Function_106_13589",      # 6A, 106
        "Function_107_13804",      # 6B, 107
        "Function_108_1389E",      # 6C, 108
        "Function_109_13A56",      # 6D, 109
        "Function_110_13B59",      # 6E, 110
        "Function_111_15203",      # 6F, 111
        "Function_112_15231",      # 70, 112
        "Function_113_15320",      # 71, 113
        "Function_114_15CA9",      # 72, 114
        "Function_115_15CBC",      # 73, 115
        "Function_116_15CCF",      # 74, 116
        "Function_117_15CE2",      # 75, 117
        "Function_118_15CF5",      # 76, 118
        "Function_119_15D08",      # 77, 119
        "Function_120_15D48",      # 78, 120
        "Function_121_15D88",      # 79, 121
        "Function_122_15DC8",      # 7A, 122
        "Function_123_15E08",      # 7B, 123
        "Function_124_15E48",      # 7C, 124
        "Function_125_15E72",      # 7D, 125
        "Function_126_15E8B",      # 7E, 126
    ))


    def Function_0_C10(): pass

    label("Function_0_C10")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_C48"),
        (1, "loc_C54"),
        (2, "loc_C60"),
        (3, "loc_C6C"),
        (4, "loc_C78"),
        (5, "loc_C84"),
        (6, "loc_C90"),
        (SWITCH_DEFAULT, "loc_C9C"),
    )


    label("loc_C48")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C54")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C60")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C6C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C78")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C84")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C90")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_C9C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_CA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CBF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CA8")

    label("loc_CBF")

    Return()

    # Function_0_C10 end

    def Function_1_CC0(): pass

    label("Function_1_CC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D12")
    OP_95(0xFE, 45340, -7050, -19380, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 42650, -7010, 17060, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    Jump("Function_1_CC0")

    label("loc_D12")

    Return()

    # Function_1_CC0 end

    def Function_2_D13(): pass

    label("Function_2_D13")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3D")
    OP_94(0xFE, 0x514, 0x13D8, 0xFFFFF650, 0x4254, 0x3E8)
    Sleep(300)
    Jump("Function_2_D13")

    label("loc_D3D")

    Return()

    # Function_2_D13 end

    def Function_3_D3E(): pass

    label("Function_3_D3E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D68")
    OP_94(0xFE, 0x64C8, 0x995C, 0xAB9A, 0x49AC, 0x7D0)
    Sleep(300)
    Jump("Function_3_D3E")

    label("loc_D68")

    Return()

    # Function_3_D3E end

    def Function_4_D69(): pass

    label("Function_4_D69")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D93")
    OP_94(0xFE, 0xD16A, 0xFFFFE908, 0xEA60, 0x1EC8, 0x7D0)
    Sleep(300)
    Jump("Function_4_D69")

    label("loc_D93")

    Return()

    # Function_4_D69 end

    def Function_5_D94(): pass

    label("Function_5_D94")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DBE")
    OP_94(0xFE, 0xDEA8, 0xFFFFA600, 0xF618, 0xFFFFC158, 0x7D0)
    Sleep(300)
    Jump("Function_5_D94")

    label("loc_DBE")

    Return()

    # Function_5_D94 end

    def Function_6_DBF(): pass

    label("Function_6_DBF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DDE")
    SetChrFlags(0xFE, 0x8000)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1)
    Jump("Function_6_DBF")

    label("loc_DDE")

    Return()

    # Function_6_DBF end

    def Function_7_DDF(): pass

    label("Function_7_DDF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DFE")
    SetChrFlags(0xFE, 0x8000)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1)
    Jump("Function_7_DDF")

    label("loc_DFE")

    Return()

    # Function_7_DDF end

    def Function_8_DFF(): pass

    label("Function_8_DFF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E1E")
    SetChrFlags(0xFE, 0x8000)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1)
    Jump("Function_8_DFF")

    label("loc_E1E")

    Return()

    # Function_8_DFF end

    def Function_9_E1F(): pass

    label("Function_9_E1F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E3E")
    SetChrFlags(0xFE, 0x8000)
    TurnDirection(0xFE, 0x14, 500)
    Sleep(1)
    Jump("Function_9_E1F")

    label("loc_E3E")

    Return()

    # Function_9_E1F end

    def Function_10_E3F(): pass

    label("Function_10_E3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ED0")
    SetChrFlags(0x14, 0x8000)
    OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFB30C, 0x7D0, 0x3E8)
    SetChrSubChip(0x13, 0x0)
    SetChrSubChip(0x11, 0x1)
    OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFB9B0, 0xBB8, 0x3E8)
    SetChrSubChip(0x11, 0x0)
    SetChrSubChip(0x12, 0x1)
    OP_9D(0xFE, 0x5FB4, 0xFFFFEA84, 0xFFFFD058, 0x7D0, 0x3E8)
    SetChrSubChip(0x12, 0x0)
    SetChrSubChip(0x10, 0x1)
    OP_9D(0xFE, 0x6B6C, 0xFFFFED40, 0xFFFFCD38, 0xBB8, 0x3E8)
    SetChrSubChip(0x10, 0x0)
    SetChrSubChip(0x13, 0x1)
    Jump("Function_10_E3F")

    label("loc_ED0")

    Return()

    # Function_10_E3F end

    def Function_11_ED1(): pass

    label("Function_11_ED1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EE9")
    SetChrFlags(0xFE, 0x8000)
    Sleep(1)
    Jump("Function_11_ED1")

    label("loc_EE9")

    Return()

    # Function_11_ED1 end

    def Function_12_EEA(): pass

    label("Function_12_EEA")

    SetChrChipByIndex(0x23, 0x13)
    SetChrSubChip(0x23, 0x0)
    EndChrThread(0x23, 0x0)
    SetChrBattleFlags(0x23, 0x4)
    BeginChrThread(0x23, 0, 0, 11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_F1D")
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    EndChrThread(0x23, 0x0)
    Jump("loc_1247")

    label("loc_F1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_F2B")
    Jump("loc_1247")

    label("loc_F2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1247")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 18200, -5650, 23100, 90)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x8, 18200, -5650, 20700, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 18200, -5650, 18200, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1078")
    SetChrPos(0x11, 24500, -6000, -20000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x20)
    BeginChrThread(0x11, 0, 0, 6)
    SetChrPos(0x12, 27500, -6000, -18000, 0)
    SetChrChipByIndex(0x12, 0x15)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x20)
    BeginChrThread(0x12, 0, 0, 7)
    SetChrPos(0x10, 24500, -6000, -12000, 180)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x20)
    BeginChrThread(0x10, 0, 0, 8)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrChipByIndex(0x13, 0x1C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x20)
    BeginChrThread(0x13, 0, 0, 9)
    SetChrPos(0x14, 26000, -3000, -16000, 0)
    BeginChrThread(0x14, 0, 0, 10)
    Jump("loc_10D7")

    label("loc_1078")

    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrPos(0x14, 25950, -6000, -13400, 0)

    label("loc_10D7")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_113E")
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrChipByIndex(0xC, 0x16)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    Jump("loc_1176")

    label("loc_113E")

    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)

    label("loc_1176")

    SetChrFlags(0xD, 0x10)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_END)), "loc_11C7")
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_1231")

    label("loc_11C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_END)), "loc_1203")
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    Jump("loc_1231")

    label("loc_1203")

    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_1231")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 55710, -2000, -36910, 45)

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_125B")
    ClearScenarioFlags(0x22, 0)
    Event(0, 80)
    Jump("loc_1292")

    label("loc_125B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_126F")
    ClearScenarioFlags(0x22, 1)
    Event(0, 81)
    Jump("loc_1292")

    label("loc_126F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1283")
    ClearScenarioFlags(0x22, 2)
    Event(0, 108)
    Jump("loc_1292")

    label("loc_1283")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1292")
    ClearScenarioFlags(0x22, 3)
    Event(0, 109)

    label("loc_1292")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12A3")
    Event(0, 57)

    label("loc_12A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_12D6")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D6")
    SetChrPos(0x0, 27000, -6010, 38000, 135)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_12D6")

    Return()

    # Function_12_EEA end

    def Function_13_12D7(): pass

    label("Function_13_12D7")

    Sound(136, 1, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_12F7")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x2, 0)
    Jump("loc_1309")

    label("loc_12F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_1309")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_131C")
    OP_1B(0x0, 0x0, 0x65)

    label("loc_131C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1329")
    OP_65(0x1, 0x1)

    label("loc_1329")

    MiniGame(0x2F, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_135F")
    SetMapObjFlags(0x0, 0x4)
    OP_65(0x0, 0x1)

    label("loc_135F")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13C7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138F")
    OP_66(0x3, 0x1)

    label("loc_138F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_139D")
    OP_66(0x4, 0x1)

    label("loc_139D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AB")
    OP_66(0x5, 0x1)

    label("loc_13AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B9")
    OP_66(0x6, 0x1)

    label("loc_13B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13C7")
    OP_66(0x7, 0x1)

    label("loc_13C7")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13EE")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_13EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1406")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_1406")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1423")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1434")
    Call(0, 100)

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1445")
    Call(0, 107)

    label("loc_1445")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_148A")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    Jump("loc_14CA")

    label("loc_148A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_14CA")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)

    label("loc_14CA")

    SetMapObjFlags(0xA, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14E8")
    ClearMapObjFlags(0xA, 0x4)
    OP_70(0xA, 0x0)

    label("loc_14E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_END)), "loc_14F5")
    OP_70(0xA, 0x2)

    label("loc_14F5")

    OP_52(0x14, 0x24, (scpexpr(EXPR_PUSH_LONG, 0x90), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15E4")
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    SetChrPos(0x11, 24500, -6000, -20000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x20)
    BeginChrThread(0x11, 0, 0, 6)
    SetChrPos(0x12, 27500, -6000, -18000, 0)
    SetChrChipByIndex(0x12, 0x15)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x20)
    BeginChrThread(0x12, 0, 0, 7)
    SetChrPos(0x10, 24500, -6000, -12000, 180)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x20)
    BeginChrThread(0x10, 0, 0, 8)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrChipByIndex(0x13, 0x1C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x20)
    BeginChrThread(0x13, 0, 0, 9)
    SetChrPos(0x14, 26000, -3000, -16000, 0)
    BeginChrThread(0x14, 0, 0, 10)

    label("loc_15E4")

    Return()

    # Function_13_12D7 end

    def Function_14_15E5(): pass

    label("Function_14_15E5")

    Call(0, 15)
    Return()

    # Function_14_15E5 end

    def Function_15_15E9(): pass

    label("Function_15_15E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 3)), scpexpr(EXPR_END)), "loc_15F6")
    Call(0, 55)
    Return()

    label("loc_15F6")

    TalkBegin(0x22)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1607")
    Jump("loc_16CB")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_16CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1687")

    #C0001
    ChrTalk(
        0x22,
        (
            "你们就是今天包下\x01",
            "湖水浴场的客人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x22,
        (
            "啧，真让人羡慕。\x01",
            "我也想和那样的美女们\x01",
            "一起游玩戏水啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16CB")

    label("loc_1687")


    #C0003
    ChrTalk(
        0x22,
        (
            "哦，现在正在准备\x01",
            "店内的商品。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x22,
        (
            "不好意思，\x01",
            "可以稍后再来吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CB")

    TalkEnd(0x22)
    Return()

    # Function_15_15E9 end

    def Function_16_16CF(): pass

    label("Function_16_16CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1835")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17BE")

    #C0005
    ChrTalk(
        0xFE,
        (
            "『纯白之石』是一种\x01",
            "偶尔能在这一带发现的\x01",
            "雪白色的漂亮石头。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "据说『纯白天堂』的沙滩中\x01",
            "埋藏着不少这种石头，\x01",
            "多半是和沙子一起运来的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "如果你想找的话，\x01",
            "不要局限在水边，\x01",
            "也可以在沙滩上找找看。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1830")

    label("loc_17BE")


    #C0008
    ChrTalk(
        0xFE,
        (
            "据说『纯白天堂』的沙滩中\x01",
            "埋藏着不少\x01",
            "纯白之石。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "如果你想找的话，\x01",
            "不要局限在水边，\x01",
            "也可以在沙滩上找找看。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1830")

    Jump("loc_1AAD")

    label("loc_1835")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1954")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E1")

    #C0010
    ChrTalk(
        0xFE,
        (
            "话说回来，真没想到划破泳装的犯人\x01",
            "竟然是那种魔兽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "我本以为肯定是\x01",
            "某个变态狂……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "算啦，能把事情解决就比什么都好。\x01",
            "真是感谢你们。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_194F")

    label("loc_18E1")


    #C0013
    ChrTalk(
        0xFE,
        (
            "话说回来，真没想到划破泳装的犯人\x01",
            "竟然是那种魔兽啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "算啦，能把事情解决就比什么都好。\x01",
            "真是感谢你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194F")

    Jump("loc_1AAD")

    label("loc_1954")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A2E")

    #C0015
    ChrTalk(
        0xFE,
        (
            "为了防止这个湖水浴场中\x01",
            "发生危险的事情，\x01",
            "我负责在这里监视。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "岸边这一带的水还算浅，\x01",
            "但如果游到离岸太远的地方，\x01",
            "小孩子的脚就够不到湖底了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "在游泳的时候一定要注意，\x01",
            "不要游得太远。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1AAD")

    label("loc_1A2E")


    #C0018
    ChrTalk(
        0xFE,
        (
            "岸边这一带的水还算浅，\x01",
            "但如果游到离岸太远的地方，\x01",
            "小孩子的脚就够不到湖底了。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "在游泳的时候一定要注意，\x01",
            "不要游得太远。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AAD")

    TalkEnd(0xFE)
    Return()

    # Function_16_16CF end

    def Function_17_1AB1(): pass

    label("Function_17_1AB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD8")
    TalkEnd(0xFE)
    Call(0, 52)
    Return()

    label("loc_1AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B65")

    #C0020
    ChrTalk(
        0xA,
        (
            "#12613F真是的，\x01",
            "竟然突然钻到\x01",
            "这种地方来……\x02\x03",

            "#12611F做事情的时候，\x01",
            "多考虑一下\x01",
            "比较好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#12506F真、真丢脸啊……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1B89")

    label("loc_1B65")


    #C0022
    ChrTalk(
        0xA,
        (
            "#12613F呼，罗伊德\x01",
            "可真是的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B89")

    Jump("loc_1D38")

    label("loc_1B8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA4")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD6")

    #C0023
    ChrTalk(
        0xA,
        (
            "#12600F虽然很感谢你\x01",
            "帮我涂防晒霜……\x02\x03",

            "#12613F但让身为同事的你\x01",
            "来涂，终究还是\x01",
            "有点不好意思呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#12512F哈、哈哈，\x01",
            "老实说，我也很不好意思。\x02\x03",

            "#12503F（话虽如此……咕。）\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        (
            "#12612F……怎么了……罗伊德？\x01",
            "请不要那么目不转睛地\x01",
            "盯着……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0026
    ChrTalk(
        0x101,
        "#12511F抱、抱歉。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D38")

    label("loc_1CD6")


    #C0027
    ChrTalk(
        0xA,
        (
            "#12613F让身为同事的你帮我涂，\x01",
            "有点不好意思呢。\x02\x03",

            "#12611F算了，总比让兰迪之类的人\x01",
            "给我涂要好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D38")

    TalkEnd(0xFE)
    Return()

    # Function_17_1AB1 end

    def Function_18_1D3C(): pass

    label("Function_18_1D3C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1DD9")

    #C0028
    ChrTalk(
        0x8,
        (
            "#13305F啊，罗伊德，你和小琪雅她们\x01",
            "正在找什么东西吗？\x02\x03",

            "#13303F纯白之石……？\x01",
            "唔……没在这附近见到过呢。\x01",
            "不好意思哦，帮不上你的忙。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EFB")

    label("loc_1DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEF")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E9E")

    #C0029
    ChrTalk(
        0x8,
        (
            "#13304F呵呵，感觉好舒服。\x01",
            "谢谢啦，罗伊德。\x02\x03",

            "#13309F……啊，对了。\x01",
            "作为回报，我也帮你\x01",
            "涂些防晒霜吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#12512F不、不用了！\x01",
            "塞茜尔姐姐还是好好躺着吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1EFB")

    label("loc_1E9E")


    #C0031
    ChrTalk(
        0x8,
        (
            "#13304F感觉真舒服，\x01",
            "这样下去好像就要睡着了。\x02\x03",

            "#13309F呵呵，要是有什么事，就把我叫醒吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFB")

    TalkEnd(0xFE)
    Return()

    # Function_18_1D3C end

    def Function_19_1EFF(): pass

    label("Function_19_1EFF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F81")

    #C0032
    ChrTalk(
        0x9,
        (
            "#13505F又白又圆的漂亮石头……？\x01",
            "没见过呢。\x02\x03",

            "#13503F这个沙滩本身就很白很漂亮，\x01",
            "想找白色的石头恐怕很难。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20DE")

    label("loc_1F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F97")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1F97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_206C")

    #C0033
    ChrTalk(
        0x9,
        "#13508F呼……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#12505F……莉夏？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#13505F啊，没什么，不好意思。\x01",
            "只是在想些心事而已。\x02\x03",

            "#13504F那个……罗伊德警官，\x01",
            "刚才真是谢谢了。\x02\x03",

            "#13502F呵呵，这样一来，\x01",
            "就不用担心被太阳\x01",
            "晒黑了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_20DE")

    label("loc_206C")


    #C0036
    ChrTalk(
        0x9,
        (
            "#13504F这样一来，\x01",
            "就不用担心被太阳\x01",
            "晒黑了。\x02\x03",

            "#13502F伊莉娅小姐和修利\x01",
            "好像也玩得很开心……\x01",
            "呵呵，真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20DE")

    TalkEnd(0xFE)
    Return()

    # Function_19_1EFF end

    def Function_20_20E2(): pass

    label("Function_20_20E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_213E")

    #C0037
    ChrTalk(
        0x11,
        (
            "#12805F嗯？在找白色的石头？\x02\x03",

            "#12803F真遗憾，我在这一带没见到过。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C4")

    label("loc_213E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214D")
    Jump("loc_21C4")

    label("loc_214D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215F")
    Call(0, 21)
    Jump("loc_21C4")

    label("loc_215F")


    #C0038
    ChrTalk(
        0x11,
        (
            "#12800F本想冲冲浪，\x01",
            "但这里好像没有\x01",
            "冲浪板出租。\x02\x03",

            "#12806F白白错失了在女士们面前\x01",
            "耍帅的好机会啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21C4")

    TalkEnd(0xFE)
    Return()

    # Function_20_20E2 end

    def Function_21_21C8(): pass

    label("Function_21_21C8")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0039
    ChrTalk(
        0x12,
        (
            "#13002F稍微休息一下，\x01",
            "然后去玩些别的吧。\x02\x03",

            "#13004F唔……在海边还有\x01",
            "什么可以玩的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x11,
        (
            "#12800F是啊，沙滩必玩的东西\x01",
            "好像都已经玩过了……\x02\x03",

            "#12806F本来还想尽情\x01",
            "搭讪一番呢，但既然是包场，\x01",
            "也就没机会认识到漂亮的姐姐了～\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x12,
        "#13006F前辈还是老样子啊……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_21_21C8 end

    def Function_22_22E9(): pass

    label("Function_22_22E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2362")

    #C0042
    ChrTalk(
        0x12,
        (
            "#13000F如果想找什么东西的话，\x01",
            "不妨尝试一下\x01",
            "转换思路。\x02\x03",

            "#13003F说不定能在某些\x01",
            "意外之处找到呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_23E3")

    label("loc_2362")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2371")
    Jump("loc_23E3")

    label("loc_2371")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2383")
    Call(0, 21)
    Jump("loc_23E3")

    label("loc_2383")


    #C0043
    ChrTalk(
        0x12,
        (
            "#13003F唔……在海边还有\x01",
            "什么可以玩的呢……\x02\x03",

            "#13000F要是有什么适合多人\x01",
            "一起玩的游戏就好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23E3")

    TalkEnd(0xFE)
    Return()

    # Function_22_22E9 end

    def Function_23_23E7(): pass

    label("Function_23_23E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2592")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F4")

    #C0044
    ChrTalk(
        0x13,
        (
            "#12900F纯白之石吗……\x01",
            "我也听说过，那种石头的材质\x01",
            "好像和『纯白天堂』的沙粒相同。\x02\x03",

            "#12904F经过漫长岁月的洗礼，\x01",
            "大部分纯白之石都会化为沙粒，\x01",
            "但似乎也有少部分维持着原形。\x02\x03",

            "#12902F呵呵，如果发现了大块的石头，\x01",
            "可以说是相当幸运的事呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_258D")

    label("loc_24F4")


    #C0045
    ChrTalk(
        0x13,
        (
            "#12904F经过漫长岁月的洗礼，\x01",
            "大部分纯白之石都会化为沙粒，\x01",
            "但似乎也有少部分维持着原形。\x02\x03",

            "#12902F呵呵，如果发现了大块的石头，\x01",
            "可以说是相当幸运的事呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_258D")

    Jump("loc_278C")

    label("loc_2592")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A1")
    Jump("loc_278C")

    label("loc_25A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_271A")

    #C0046
    ChrTalk(
        0x13,
        (
            "#12906F哎呀呀，玩不习惯的游戏\x01",
            "真是好累啊。\x02\x03",

            "#12900F我一向都不太擅长\x01",
            "那种体育类的活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#12503F可是……你好像\x01",
            "连一口粗气都没喘呢……\x02\x03",

            "#12502F而且对规则\x01",
            "也了解得很详细，\x01",
            "其实你根本就是很擅长吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x13,
        (
            "#12904F呵呵，怎么会，\x01",
            "我可是在都市里长大的孩子哦。\x02\x03",

            "#12900F沙滩排球的规则，\x01",
            "我只是在看杂志打发时间的\x01",
            "时候记住的。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#12503F（那可真是很厉害呢……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_278C")

    label("loc_271A")


    #C0050
    ChrTalk(
        0x13,
        (
            "#12906F哎呀呀，玩不习惯的游戏\x01",
            "真是好累啊。\x02\x03",

            "#12909F呵呵，不然我也加入艾莉她们，\x01",
            "在躺椅上优雅地休息一下好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_278C")

    TalkEnd(0xFE)
    Return()

    # Function_23_23E7 end

    def Function_24_2790(): pass

    label("Function_24_2790")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_28E9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2866")

    #C0051
    ChrTalk(
        0x10,
        (
            "#13400F小琪雅好像正在\x01",
            "和修利一起玩吧？\x02\x03",

            "#13404F呵呵，修利那孩子\x01",
            "没有同龄的朋友，\x01",
            "被小琪雅粘着可能会有些不习惯吧。\x02\x03",

            "#13402F今天也许能看到她与平时不同的一面。\x01",
            "呵呵，很期待啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_28E4")

    label("loc_2866")


    #C0052
    ChrTalk(
        0x10,
        (
            "#13404F修利没有同龄的朋友，\x01",
            "被小琪雅粘着可能会有些不习惯吧。\x02\x03",

            "#13402F今天也许能看到她与平时不同的一面。\x01",
            "呵呵，很期待啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E4")

    Jump("loc_2B0B")

    label("loc_28E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F8")
    Jump("loc_2B0B")

    label("loc_28F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A94")

    #C0053
    ChrTalk(
        0x10,
        (
            "#13409F呀，偶尔参加一些\x01",
            "这样的体育运动也不错呢。\x02\x03",

            "#13402F而且还能欣赏到\x01",
            "穿泳装的女孩们……\x01",
            "这一趟真是来对了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0054
    ChrTalk(
        0x101,
        (
            "#12512F伊莉娅小姐……\x01",
            "其实你就是个披着演员外皮的\x01",
            "怪叔叔吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x10,
        (
            "#13406F哎呀，好失礼。\x02\x03",

            "#13402F哼哼，警察弟弟，\x01",
            "你不是也一直在死盯着\x01",
            "塞茜尔和莉夏她们吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#12511F我、我拒绝回答。\x02\x03",

            "#12506F（说起来，感觉还是伊莉娅小姐的\x01",
            "　泳装最惹眼呢……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2B0B")

    label("loc_2A94")


    #C0057
    ChrTalk(
        0x10,
        (
            "#13404F仔细想想，除了练习之外，\x01",
            "好像已经很久没有\x01",
            "这样活动过身体了～\x02\x03",

            "#13402F嗯嗯，接受邀请\x01",
            "果然是很正确的决定啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B0B")

    TalkEnd(0xFE)
    Return()

    # Function_24_2790 end

    def Function_25_2B0F(): pass

    label("Function_25_2B0F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B9E")

    #C0058
    ChrTalk(
        0xB,
        (
            "#12705F纯白之石……\x01",
            "这沙滩上还有那种东西吗？\x02\x03",

            "#12703F我在堆建沙堡的地基时\x01",
            "用过这附近的沙子，\x01",
            "但并没见过那种东西呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D42")

    label("loc_2B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BB4")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_2BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CDB")

    #C0059
    ChrTalk(
        0xB,
        (
            "#12703F用沙子竟能造出这样的东西，\x01",
            "我原本还一直半信半疑……\x02\x03",

            "#12702F但现在我却觉得，\x01",
            "只要有沙子，无论什么都可以做出来。\x02\x03",

            "#12704F呵呵，\x01",
            "不然再给蔡特\x01",
            "造个沙窝好了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0060
    ChrTalk(
        0x101,
        (
            "#12506F（再怎么说，\x01",
            "  蔡特也不会喜欢沙子做的窝吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xD,
        "#01203F咕呜呜……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_2D42")

    label("loc_2CDB")


    #C0062
    ChrTalk(
        0xB,
        (
            "#12704F现在我觉得，\x01",
            "只要有沙子，无论什么都可以做出来。\x02\x03",

            "#12702F呵呵，\x01",
            "不然再给蔡特\x01",
            "造个沙窝好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D42")

    TalkEnd(0xFE)
    Return()

    # Function_25_2B0F end

    def Function_26_2D46(): pass

    label("Function_26_2D46")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DA5")

    #C0063
    ChrTalk(
        0xC,
        (
            "#13105F哎，你在找什么～？\x02\x03",

            "#13103F纯白之石……？\x01",
            "唔……没听说过呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EAE")

    label("loc_2DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DBB")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_2DBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E68")

    #C0064
    ChrTalk(
        0xC,
        (
            "#13109F呀～真的建起了\x01",
            "漂亮的城堡呢～！\x02\x03",

            "#13106F要是带着相机，\x01",
            "就能把它给拍下来了……\x01",
            "哎，真遗憾啊～\x02\x03",

            "#13101F至少把它永久留存在\x01",
            "我心中的感光回路里吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_2EAE")

    label("loc_2E68")


    #C0065
    ChrTalk(
        0xC,
        (
            "#13101F回去之前，要把这城堡的样子\x01",
            "牢牢留存在心中的感光回路里～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EAE")

    TalkEnd(0xFE)
    Return()

    # Function_26_2D46 end

    def Function_27_2EB2(): pass

    label("Function_27_2EB2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2EDD")

    #C0066
    ChrTalk(
        0xD,
        "#01200F……嗷？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F0E")

    label("loc_2EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EF3")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_2EF3")


    #C0067
    ChrTalk(
        0xD,
        "#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()

    label("loc_2F0E")

    TalkEnd(0xFE)
    Return()

    # Function_27_2EB2 end

    def Function_28_2F12(): pass

    label("Function_28_2F12")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F85")

    #C0068
    ChrTalk(
        0xE,
        (
            "#13210F啊，罗伊德，\x01",
            "你已经找到\x01",
            "『纯白之石』了吗？\x02\x03",

            "#13209F嘿嘿嘿，大块的\x01",
            "在什么地方呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3176")

    label("loc_2F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F9B")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_2F9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 0)), scpexpr(EXPR_END)), "loc_3128")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30AA")

    #C0069
    ChrTalk(
        0xE,
        (
            "#13210F这块纯白之石\x01",
            "真是好大啊！\x02\x03",

            "#13209F这也许会是我米修拉姆之行\x01",
            "中的最美好回忆呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#12509F哈哈，我们才刚来没多久，\x01",
            "说这话也太早了吧。\x02\x03",

            "#12504F不过，看你那么开心，\x01",
            "我也很高兴呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xE,
        (
            "#13209F嘿嘿，谢谢了，罗伊德，\x01",
            "我会好好珍惜的！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_3123")

    label("loc_30AA")


    #C0072
    ChrTalk(
        0xE,
        (
            "#13202F嘿嘿，这也许会是我米修拉姆之行\x01",
            "中的最美好回忆呢。\x02\x03",

            "#13209F谢谢，罗伊德。\x01",
            "我会好好珍惜\x01",
            "这块『纯白之石』的！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3123")

    Jump("loc_3176")

    label("loc_3128")


    #C0073
    ChrTalk(
        0xE,
        (
            "#13209F寻找纯白之石\x01",
            "真是开心呢。\x02\x03",

            "#13204F嘿嘿，一会也拿去\x01",
            "给蔡特看看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3176")

    TalkEnd(0xFE)
    Return()

    # Function_28_2F12 end

    def Function_29_317A(): pass

    label("Function_29_317A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31B6")
    Call(0, 30)
    Jump("loc_33DE")

    label("loc_31B6")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",                  # 0
            "要求出示纯白之石\x01",      # 1
            "放弃\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3222")
    Call(0, 30)
    Jump("loc_33DE")

    label("loc_3222")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33CF")

    #C0074
    ChrTalk(
        0xF,
        (
            "#13605F唔……\x01",
            "你好像已经找到\x01",
            "『纯白之石』了啊。\x02\x03",

            "#13600F现在就要和\x01",
            "我们的『纯白之石』\x01",
            "比较大小吗？\x02",
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
        1,
        (
            "比较\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_337D")

    #C0075
    ChrTalk(
        0x101,
        "#12504F嗯，立刻开始吧。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xF,
        (
            "#13605F哼，真是自信满满啊。\x02\x03",

            "#13604F那我这就把小鬼头叫来。\x01",
            "哼哼，待会输掉之后可别哭哦～\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    Call(0, 53)
    Return()

    label("loc_337D")


    #C0077
    ChrTalk(
        0x101,
        "#12500F啊，再等我一下吧。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xF,
        (
            "#13606F啧，什么嘛，\x01",
            "是男人的话就爽快些。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33DE")

    label("loc_33CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_33DE")

    label("loc_33DE")

    Jump("loc_3604")

    label("loc_33E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33F9")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_33F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 2)), scpexpr(EXPR_END)), "loc_3587")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_353F")

    #C0079
    ChrTalk(
        0xF,
        (
            "#13600F啊，那、那个……\x01",
            "刚才真是谢啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#12500F你是指纯白之石的事吗？\x01",
            "不用放在心上啦。\x02\x03",

            "#12509F哈哈，回去以后也拿给\x01",
            "彩虹剧团的各位看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xF)

    #C0081
    ChrTalk(
        0xF,
        (
            "#13611F笨、笨蛋……\x01",
            "谁会做那么\x01",
            "幼稚的事情！\x02\x03",

            "#13606F有没有常识啊，真是的……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#12506F（这个年纪的女孩真是别扭啊……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3582")

    label("loc_353F")


    #C0083
    ChrTalk(
        0xF,
        (
            "#13603F谢谢你送我\x01",
            "纯白之石啦。\x02\x03",

            "#13608F……哼、哼，仅此而已。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3582")

    Jump("loc_3604")

    label("loc_3587")


    #C0084
    ChrTalk(
        0xF,
        (
            "#13603F找石头虽然也很有趣……\x01",
            "但难得来到沙滩，\x01",
            "还是想下水游泳啊。\x02\x03",

            "#13602F机会难得，我想把游泳技术\x01",
            "练得比莉夏姐更好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3604")

    TalkEnd(0xFE)
    Return()

    # Function_29_317A end

    def Function_30_3608(): pass

    label("Function_30_3608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_369B")

    #C0085
    ChrTalk(
        0xF,
        (
            "#13600F如果找到了『纯白之石』，\x01",
            "就来和我说。\x02\x03",

            "我们到时候来比较大小，\x01",
            "谁的最大就算赢。\x02\x03",

            "#13604F哼，反正我是不会\x01",
            "输给你们的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_36F3")

    label("loc_369B")


    #C0086
    ChrTalk(
        0xF,
        (
            "#13600F一会咱们来比谁的\x01",
            "『纯白之石』最大吧。\x02\x03",

            "#13604F哼，反正我是不会\x01",
            "输给你们的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36F3")

    Return()

    # Function_30_3608 end

    def Function_31_36F4(): pass

    label("Function_31_36F4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3705")
    Jump("loc_3A57")

    label("loc_3705")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_3A57")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A4B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3763")

    #C0087
    ChrTalk(
        0x101,
        (
            "#12500F哎，这只黑猫……\x01",
            "好像曾在哪里见过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "喵～\x02",
    )

    CloseMessageWindow()
    Jump("loc_376D")

    label("loc_3763")


    #C0089
    ChrTalk(
        0xFE,
        "喵～\x02",
    )

    CloseMessageWindow()

    label("loc_376D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('猫食', 0x0)"), scpexpr(EXPR_END)), "loc_395A")

    #C0090
    ChrTalk(
        0x101,
        (
            "#12505F……莫非是\x01",
            "肚子饿了吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "交出『猫食』\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3946")

    #C0091
    ChrTalk(
        0x101,
        "#12500F来，吃吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '猫食'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "交出了。\x02",
        )
    )

    Sound(17, 0, 100, 0)
    CloseMessageWindow()
    FadeToBright(300, 0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Sound(953, 0, 100, 0)

    #C0093
    ChrTalk(
        0xFE,
        "喵呜呜～⊥\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "（狼吞虎咽）……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#12509F哈哈，有那么饿吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0xFE,
        "喵噢⊥\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0097
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝６卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝６卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0098
    ChrTalk(
        0x101,
        (
            "#12505F哎……要把这本书给我吗？\x02\x03",

            "#12500F哈哈，谢谢啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 5)
    SubItemNumber('猫食', 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3955")

    label("loc_3946")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3955")

    label("loc_3955")

    Jump("loc_3A43")

    label("loc_395A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39DF")

    #C0099
    ChrTalk(
        0x101,
        (
            "#12505F……莫非是\x01",
            "肚子饿了吗？\x02\x03",

            "#12503F要是带着『猫食』\x01",
            "就可以喂你了……\x02\x03",

            "#12512F但真不巧，我现在没有，\x01",
            "抱歉啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A35")

    label("loc_39DF")


    #C0100
    ChrTalk(
        0x101,
        (
            "#12503F要是带着『猫食』\x01",
            "就可以喂你了……\x02\x03",

            "#12512F但真不巧，我现在没有，\x01",
            "抱歉啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A35")


    #C0101
    ChrTalk(
        0xFE,
        "喵噢……\x02",
    )

    CloseMessageWindow()

    label("loc_3A43")

    SetScenarioFlags(0x1, 6)
    Jump("loc_3A57")

    label("loc_3A4B")


    #C0102
    ChrTalk(
        0xFE,
        "喵噢⊥\x02",
    )

    CloseMessageWindow()

    label("loc_3A57")

    TalkEnd(0xFE)
    Return()

    # Function_31_36F4 end

    def Function_32_3A5B(): pass

    label("Function_32_3A5B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            "　　 在湖水浴场游玩时的注意事项\x01",
            "——————————————————\x01",
            "·请在下水之前务必做好准备运动。\x01",
            "·请不要身着便装下水。\x01",
            "  （服务台提供租借泳装服务）\x01",
            "·请听从救生员的指挥。\x01",
            "——————————————————\x01",
            "  请遵守规章制度，祝您游玩愉快。\x01",
            "  　　　　　　　──米修拉姆事业部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_32_3A5B end

    def Function_33_3BB1(): pass

    label("Function_33_3BB1")

    EventBegin(0x1)

    #C0104
    ChrTalk(
        0x101,
        (
            "#12500F哦……\x01",
            "往这边走就离开湖水浴场了。\x02\x03",

            "玛丽亚贝尔小姐\x01",
            "特意为我们包了场，\x01",
            "还是继续在这里玩吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -10330, -2000, -920, 90)
    EventEnd(0x4)
    Return()

    # Function_33_3BB1 end

    def Function_34_3C2E(): pass

    label("Function_34_3C2E")

    EventBegin(0x1)

    #C0105
    ChrTalk(
        0x101,
        (
            "#12500F『纯白之石』应该在\x01",
            "水边的某处。\x01",
            "再找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11580, -5080, -120, 90)
    EventEnd(0x4)
    Return()

    # Function_34_3C2E end

    def Function_35_3C7E(): pass

    label("Function_35_3C7E")

    EventBegin(0x1)

    #C0106
    ChrTalk(
        0x101,
        (
            "#12500F『纯白之石』应该在\x01",
            "水边的某处。\x01",
            "再找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11210, -4940, 46030, 90)
    EventEnd(0x4)
    Return()

    # Function_35_3C7E end

    def Function_36_3CCE(): pass

    label("Function_36_3CCE")

    EventBegin(0x1)

    #C0107
    ChrTalk(
        0x101,
        (
            "#12500F哦……找石头的时候\x01",
            "可不能妨碍他们打排球啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 32500, -6000, -13500, 90)
    EventEnd(0x5)
    Return()

    # Function_36_3CCE end

    def Function_37_3D1D(): pass

    label("Function_37_3D1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D2F")
    Call(0, 36)
    Return()

    label("loc_3D2F")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch51311.itc", 0x1E)
    LoadChrToIndex("apl/ch51312.itc", 0x1F)
    LoadChrToIndex("apl/ch51313.itc", 0x20)
    LoadChrToIndex("apl/ch51314.itc", 0x21)
    LoadChrToIndex("apl/ch51315.itc", 0x22)
    LoadChrToIndex("apl/ch51331.itc", 0x23)
    LoadChrToIndex("apl/ch51333.itc", 0x25)
    LoadChrToIndex("apl/ch51334.itc", 0x26)
    LoadChrToIndex("apl/ch51335.itc", 0x27)
    LoadChrToIndex("apl/ch51336.itc", 0x28)
    LoadChrToIndex("apl/ch51337.itc", 0x29)
    LoadChrToIndex("apl/ch51339.itc", 0x2B)
    LoadChrToIndex("apl/ch51340.itc", 0x2C)
    LoadChrToIndex("apl/ch51341.itc", 0x2D)
    LoadChrToIndex("apl/ch51342.itc", 0x2E)
    LoadChrToIndex("apl/ch51344.itc", 0x30)
    LoadChrToIndex("apl/ch51345.itc", 0x31)
    LoadChrToIndex("apl/ch51346.itc", 0x32)
    LoadChrToIndex("apl/ch51348.itc", 0x34)
    LoadChrToIndex("apl/ch51349.itc", 0x35)
    LoadChrToIndex("apl/ch51350.itc", 0x36)
    LoadEffect(0x0, "event\\ev13001.eff")
    EndChrThread(0x11, 0xFF)
    EndChrThread(0x12, 0xFF)
    EndChrThread(0x10, 0xFF)
    EndChrThread(0x13, 0xFF)
    EndChrThread(0x14, 0xFF)
    ClearChrFlags(0x11, 0x20)
    ClearChrFlags(0x12, 0x20)
    ClearChrFlags(0x10, 0x20)
    ClearChrFlags(0x13, 0x20)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x101, 31000, -6000, -14500, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4301")
    Call(1, 1)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)

    #C0108
    ChrTalk(
        0x10,
        "#13400F#11P──好¤\x02",
    )

    CloseMessageWindow()

    def lambda_3E87():
        TurnDirection(0x13, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_3E87)
    Sleep(50)

    def lambda_3E97():
        TurnDirection(0x11, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_3E97)
    Sleep(50)

    def lambda_3EA7():
        TurnDirection(0x12, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_3EA7)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    #C0109
    ChrTalk(
        0x11,
        "#12809F#5P唔唔，果然厉害啊……！！\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x12,
        "#13006F#6P完全没看到球……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x10, 500)

    #C0111
    ChrTalk(
        0x13,
        (
            "#12902F#12P呵呵，使出了全身能量\x01",
            "的超级扣杀呢。\x02\x03",

            "#12904F真不愧是\x01",
            "伊莉娅·普拉提耶啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x13, 500)

    #C0112
    ChrTalk(
        0x10,
        "#13409F#5P呵呵，过奖了¤\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(28000, -4800, -15000, 0)
    MoveCamera(260, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    OP_0D()

    #C0113
    ChrTalk(
        0x101,
        "#12505F#6P好、好厉害……！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_403B():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_403B)
    Sleep(50)

    def lambda_404B():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_404B)
    Sleep(50)

    def lambda_405B():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_405B)
    Sleep(50)

    def lambda_406B():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_406B)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    #C0114
    ChrTalk(
        0x10,
        (
            "#13400F#11P啊，警察弟弟，你看到了吗？\x02\x03",

            "#13409F呵呵，我的必杀技\x01",
            "很强吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12512F#6P是、是的……\x01",
            "真是太厉害了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x11,
        (
            "#12802F#5P嗯，伊莉娅小姐的确很恐怖呢。\x02\x03",

            "#12804F连我的大力扣杀\x01",
            "都能轻易接下。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x12,
        (
            "#13000F#5P瓦吉的托球也很精妙，正好传到了\x01",
            "最佳位置，让伊莉娅小姐扣杀成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x13,
        (
            "#12900F#11P呵呵，那只是运气好罢了。\x01",
            "话说回来，你们的配合\x01",
            "也非常默契呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#12504F#6P哎呀……老实说，\x01",
            "大家的实力都太强了，\x01",
            "让我简直连话都说不出来了。\x02\x03",

            "#12500F以这种阵容，就算参加比赛，\x01",
            "也会立刻夺得冠军吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10,
        (
            "#13404F#11P呵呵，现实可没有\x01",
            "那么简单，\x01",
            "不过这主意倒是不坏呢。\x02\x03",

            "#13409F对了，警察弟弟也来参加下一场比赛如何？\x01",
            "一起打沙滩排球吧¤\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15D, 2)
    Jump("loc_4405")

    label("loc_4301")

    SetChrPos(0x10, 24500, -6000, -15000, 90)
    SetChrPos(0x11, 24500, -6000, -17000, 90)
    SetChrPos(0x12, 27500, -6000, -19000, 45)
    SetChrPos(0x13, 27500, -6000, -13000, 90)
    SetChrPos(0x14, 23500, -6000, -14000, 0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    OP_68(28000, -4800, -15000, 0)
    MoveCamera(260, 20, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0121
    ChrTalk(
        0x10,
        (
            "#13400F#11P机会难得，\x01",
            "警察弟弟也来参加下一场比赛如何？\x02\x03",

            "#13409F一起打沙滩排球吧¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4405")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "参加沙滩排球\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D86")

    #C0122
    ChrTalk(
        0x101,
        (
            "#12500F#6P那就恭敬不如从命了，\x01",
            "让我也加入吧。\x02\x03",

            "#12506F话虽如此，但我并不是很了解\x01",
            "沙滩排球的规则呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x12,
        (
            "#13000F基本规则和普通排球一样。\x02\x03",

            "#13004F至于不同之处，\x01",
            "大致来说也就是二人一组，\x01",
            "还有沙滩场地了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x13,
        (
            "#12900F另外，在正式比赛中要得到\x01",
            "２１分才算是取胜一场……\x02\x03",

            "但这次为了轻松些，\x01",
            "就改为每局１２分制了。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#12500F#6P嗯，原来如此……\x01",
            "那应该没什么问题了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x11,
        (
            "#12802F#5P好啦，闲话少说，\x01",
            "我们赶快来分组吧。\x02\x03",

            "#12806F既然罗伊德加入了，那就只能\x01",
            "分出一个人去当裁判啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#12505F#6P啊，这样啊……\x01",
            "我好像打扰到你们了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x10,
        (
            "#13409F#11P啊哈哈，不会啦。\x02\x03",

            "#13400F那……警察弟弟，\x01",
            "你想和谁组成一队呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#12500F#6P这个嘛，嗯……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0130
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要和谁组队呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "兰迪\x01",        # 0
            "诺艾尔\x01",      # 1
            "瓦吉\x01",        # 2
            "伊莉娅\x01",      # 3
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
        (0, "loc_4762"),
        (1, "loc_48DD"),
        (2, "loc_4A69"),
        (3, "loc_4BE6"),
        (SWITCH_DEFAULT, "loc_4D67"),
    )


    label("loc_4762")


    #C0131
    ChrTalk(
        0x101,
        "#12500F#6P兰迪，请多指教了。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x11,
        "#12800F#5P没问题，看我的吧！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x12,
        (
            "#13004F#5P好，再来决定另外\x01",
            "一组的成员和裁判吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x13,
        (
            "#12900F嗯，公平起见，\x01",
            "不如用猜拳来决定吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x10,
        (
            "#13409F#11P呵呵，好啊，\x01",
            "那就赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    #A0136
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "根据猜拳的结果，\x01",
            "由伊莉娅来担任裁判……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0137
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德&兰迪队\x01",
            "与瓦吉&诺艾尔队\x01",
            "的比赛拉开了帷幕。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0138
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "接下来──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 3)
    Call(1, 9)
    Jump("loc_4D67")

    label("loc_48DD")


    #C0139
    ChrTalk(
        0x101,
        "#12500F#6P诺艾尔，请多指教了。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x12,
        (
            "#13000F#5P明白了！\x01",
            "一起加油吧，罗伊德警官！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x13,
        (
            "#12904F好，再来决定另\x01",
            "一组的成员与裁判吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x10,
        (
            "#13400F#11P嗯，为了公平，\x01",
            "不然就用猜拳来决定如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x11,
        (
            "#12809F#5P说的也对，\x01",
            "那就赶快开始吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    #A0144
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "根据猜拳的结果，\x01",
            "由兰迪来担任裁判……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0145
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德&诺艾尔队\x01",
            "与伊莉娅&瓦吉队\x01",
            "的比赛拉开了帷幕。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "接下来──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 4)
    Call(1, 24)
    Jump("loc_4D67")

    label("loc_4A69")


    #C0147
    ChrTalk(
        0x101,
        "#12500F#6P瓦吉，请多指教了。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x13,
        "#12900F呵呵，没问题。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x10,
        (
            "#13404F#11P好，再来决定另\x01",
            "一组的成员和裁判吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x11,
        (
            "#12800F#5P嗯，公平起见，\x01",
            "不如就用猜拳来决定吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x12,
        (
            "#13009F#5P有道理，赶快决定，\x01",
            "然后开始比赛吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "根据猜拳的结果，\x01",
            "由诺艾尔来担任裁判……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0153
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德&瓦吉队\x01",
            "与伊莉娅&兰迪队\x01",
            "的比赛拉开了帷幕。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0154
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "接下来──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 5)
    Call(1, 49)
    Jump("loc_4D67")

    label("loc_4BE6")


    #C0155
    ChrTalk(
        0x101,
        "#12500F#6P伊莉娅小姐，请多指教了。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x10,
        "#13400F#11POK，请多指教！\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x11,
        (
            "#12804F#5P好，再来决定另\x01",
            "一组的成员和裁判吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x12,
        (
            "#13000F#5P嗯，公平起见，\x01",
            "还是用猜拳来决定比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x13,
        (
            "#12902F呵呵，是啊，\x01",
            "那就赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "根据猜拳的结果，\x01",
            "由瓦吉来担任裁判……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0161
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德&伊莉娅队\x01",
            "与兰迪&诺艾尔队\x01",
            "的比赛拉开了帷幕。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "接下来──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 6)
    Call(1, 69)
    Jump("loc_4D67")

    label("loc_4D67")

    Call(0, 38)
    Call(0, 39)
    Call(0, 45)
    SetChrPos(0x0, 20000, -6000, -15000, 0)
    Jump("loc_4ED4")

    label("loc_4D86")


    #C0163
    ChrTalk(
        0x101,
        "#12500F#6P那个……还是稍后再说吧……\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x10,
        (
            "#13405F#11P啊，这样啊？\x01",
            "算啦，那就不勉强你了。\x02\x03",

            "#13400F如果想加入了，\x01",
            "随时都可以过来哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4EC3")
    SetChrPos(0x11, 24500, -6000, -20000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x20)
    BeginChrThread(0x11, 0, 0, 6)
    SetChrPos(0x12, 27500, -6000, -18000, 0)
    SetChrChipByIndex(0x12, 0x15)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x20)
    BeginChrThread(0x12, 0, 0, 7)
    SetChrPos(0x10, 24500, -6000, -12000, 180)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x20)
    BeginChrThread(0x10, 0, 0, 8)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrChipByIndex(0x13, 0x1C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x20)
    BeginChrThread(0x13, 0, 0, 9)
    SetChrPos(0x14, 26000, -3000, -16000, 0)
    BeginChrThread(0x14, 0, 0, 10)

    label("loc_4EC3")

    SetChrPos(0x0, 32500, -6000, -13500, 90)

    label("loc_4ED4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4EEC")
    Call(0, 54)

    label("loc_4EEC")

    EventEnd(0x5)
    Return()

    # Function_37_3D1D end

    def Function_38_4EEF(): pass

    label("Function_38_4EEF")

    OP_68(26000, -4700, -16000, 0)
    MoveCamera(330, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x14, 0x8)
    SetChrPos(0x14, 29100, -6000, -11900, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_521F")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x11, 27000, -6000, -18000, 0)
    SetChrPos(0x12, 25000, -6000, -14000, 180)
    SetChrPos(0x13, 27000, -6000, -14000, 180)
    SetChrPos(0x10, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0165
    ChrTalk(
        0x11,
        (
            "#12809F#6P哈哈，真是一场\x01",
            "很精彩的比赛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x13,
        "#12902F呵呵，的确不坏呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0167
    ChrTalk(
        0x10,
        (
            "#13401F#5P唔～你们好狡猾！\x01",
            "只顾着自己开心。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_50AA():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_50AA)
    Sleep(50)

    def lambda_50BA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_50BA)
    Sleep(50)

    def lambda_50CA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_50CA)
    Sleep(50)

    def lambda_50DA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_50DA)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    #C0168
    ChrTalk(
        0x12,
        "#13005F#11P哎……？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x10,
        (
            "#13406F#5P那么有趣的比赛，\x01",
            "光在一旁看着，果然还是无法满足啊！\x02\x03",

            "#13409F这次让我加入，\x01",
            "再来比一场吧！！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#12500F#6P哈哈，那我们就来\x01",
            "重新分组吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x11,
        (
            "#12809F#12P哈哈，好啊。\x02\x03",

            "#12800F那……罗伊德，\x01",
            "你来选择下一场比赛\x01",
            "的搭档吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0172
    ChrTalk(
        0x101,
        "#12500F#5P啊，这个嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B12")

    label("loc_521F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_54FA")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x12, 27000, -6000, -18000, 0)
    SetChrPos(0x10, 25000, -6000, -14000, 180)
    SetChrPos(0x13, 27000, -6000, -14000, 180)
    SetChrPos(0x11, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0173
    ChrTalk(
        0x12,
        "#13009F#6P呼～真是场激烈的比赛啊！\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x10,
        "#13409F#11P嗯嗯，出了不少汗呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x11, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0175
    ChrTalk(
        0x11,
        (
            "#12806F#5P唔……罗伊德加入之后，\x01",
            "比赛好像明显变得激烈了呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5380():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5380)
    Sleep(50)

    def lambda_5390():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5390)
    Sleep(50)

    def lambda_53A0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_53A0)
    Sleep(50)

    def lambda_53B0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_53B0)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    #C0176
    ChrTalk(
        0x13,
        "#12905F#12P嗯？你想说什么吗？\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x11,
        (
            "#12803F#5P嗯……那个，\x01",
            "只有我在一边看着，\x01",
            "未免有点不公平吧？\x02\x03",

            "#12800F这次让我也加入，\x01",
            "再来一场比赛吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#12500F#6P嗯，那我们就来\x01",
            "重新分组吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x12,
        (
            "#13009F#12P嗯，好啊。\x02\x03",

            "#13000F罗伊德警官，\x01",
            "你来选择下一场比赛\x01",
            "的搭档吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0180
    ChrTalk(
        0x101,
        "#12500F#5P啊，这个嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B12")

    label("loc_54FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_57C4")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x13, 27000, -6000, -18000, 0)
    SetChrPos(0x10, 25000, -6000, -14000, 180)
    SetChrPos(0x11, 27000, -6000, -14000, 180)
    SetChrPos(0x12, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0181
    ChrTalk(
        0x13,
        "#12902F#6P呵呵，很有趣嘛。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x11,
        "#12809F#11P嗯，真是场精彩的比赛呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x13, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0183
    ChrTalk(
        0x12,
        (
            "#13001F#5P……那个……各位！\x01",
            "如果可以，能不能再比一场呢！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5654():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5654)
    Sleep(50)

    def lambda_5664():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5664)
    Sleep(50)

    def lambda_5674():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5674)
    Sleep(50)

    def lambda_5684():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5684)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x13, 2)

    #C0184
    ChrTalk(
        0x10,
        "#13405F#11P哎……？\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x12,
        (
            "#13006F#5P看了你们刚才的比赛之后，\x01",
            "我实在是忍耐不住了……\x02\x03",

            "#13002F这次请一定让我加入！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#12500F#6P嗯，那我们就来\x01",
            "重新分组吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x13,
        "#12904F#12P呵呵，我没意见。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x13,
        (
            "#12902F#12P那好，罗伊德，\x01",
            "你来选择下一场比赛\x01",
            "的搭档吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0189
    ChrTalk(
        0x101,
        "#12500F#5P啊，这个嘛……\x02",
    )

    CloseMessageWindow()
    Jump("loc_5B12")

    label("loc_57C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_5B12")
    SetChrPos(0x101, 25000, -6000, -18000, 0)
    SetChrPos(0x10, 27000, -6000, -18000, 0)
    SetChrPos(0x11, 25000, -6000, -14000, 180)
    SetChrPos(0x12, 27000, -6000, -14000, 180)
    SetChrPos(0x13, 21300, -6000, -16000, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0190
    ChrTalk(
        0x10,
        "#13409F#6P呀～真是让人热血沸腾啊！\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x12,
        "#13009F#11P是啊，真是太有意思了！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x10, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x12, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0192
    ChrTalk(
        0x13,
        (
            "#12900F#5P呵呵，那比赛就\x01",
            "到此结束吧？\x02\x03",

            "#12904F我的嗓子好像有点干了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0193
    ChrTalk(
        0x101,
        (
            "#12504F#12P别啊……机会难得，\x01",
            "再来一场怎么样？\x02\x03",

            "#12500F这次让瓦吉加入。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5981():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5981)
    Sleep(50)

    def lambda_5991():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5991)
    Sleep(50)

    def lambda_59A1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_59A1)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)

    #C0194
    ChrTalk(
        0x11,
        (
            "#12800F#11P哦哦，这主意不错啊。\x01",
            "瓦吉当了一阵子裁判，大概也有些无聊了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0195
    ChrTalk(
        0x13,
        (
            "#12906F#5P这倒没有，\x01",
            "其实我完全无所谓的……\x02\x03",

            "#12900F……呵呵，算了。\x01",
            "既然你们这么有兴致，\x01",
            "我就继续奉陪吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x10,
        (
            "#13409F#12P呵呵，那就这么定了。\x02\x03",

            "#13400F好，警察弟弟，\x01",
            "你来选择下一场比赛\x01",
            "的搭档吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0197
    ChrTalk(
        0x101,
        (
            "#12500F#6P嗯，好的。\x01",
            "那么……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B12")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要和谁组队呢？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "兰迪")
    MenuCmd(1, 0, "诺艾尔")
    MenuCmd(1, 0, "瓦吉")
    MenuCmd(1, 0, "伊莉娅")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_5B78")
    MenuCmd(3, 0, 0x0)

    label("loc_5B78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_5B85")
    MenuCmd(3, 0, 0x1)

    label("loc_5B85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_5B92")
    MenuCmd(3, 0, 0x2)

    label("loc_5B92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_5B9F")
    MenuCmd(3, 0, 0x3)

    label("loc_5B9F")

    MenuCmd(2, 0, -1, 85, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5BE4"),
        (1, "loc_5CF0"),
        (2, "loc_5E0F"),
        (3, "loc_5F15"),
        (SWITCH_DEFAULT, "loc_6029"),
    )


    label("loc_5BE4")

    TurnDirection(0x101, 0x11, 500)

    #C0199
    ChrTalk(
        0x101,
        (
            "#12500F#6P#N嗯……那这次就和兰迪组队吧。\x01",
            "兰迪，请多指教哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x11, 0x101, 500)

    #C0200
    ChrTalk(
        0x11,
        "#12809F#5P#N没问题，看我的吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "再次猜拳之后，\x01",
            "由伊莉娅来担任\x01",
            "第二场比赛的裁判……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德&兰迪队\x01",
            "与瓦吉&诺艾尔队\x01",
            "开始了新一场比赛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 9)
    Jump("loc_6029")

    label("loc_5CF0")

    TurnDirection(0x101, 0x12, 500)

    #C0203
    ChrTalk(
        0x101,
        (
            "#12500F#6P#N嗯……那这次就和诺艾尔组队吧。\x01",
            "诺艾尔，请多指教哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x12, 0x101, 500)

    #C0204
    ChrTalk(
        0x12,
        (
            "#13009F#5P#N明白了！\x01",
            "一起加油吧，罗伊德警官！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "再次猜拳之后，\x01",
            "由兰迪来担任\x01",
            "第二场比赛的裁判……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德&诺艾尔队\x01",
            "与伊莉娅&瓦吉队\x01",
            "开始了新一场比赛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 24)
    Jump("loc_6029")

    label("loc_5E0F")

    TurnDirection(0x101, 0x13, 500)

    #C0207
    ChrTalk(
        0x101,
        (
            "#12500F#6P#N嗯……那这次就和瓦吉组队吧。\x01",
            "瓦吉，请多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x13, 0x101, 500)

    #C0208
    ChrTalk(
        0x13,
        "#12902F#5P#N呵呵，放心吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "再次猜拳之后，\x01",
            "由诺艾尔来担任\x01",
            "第二场比赛的裁判……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德&瓦吉队\x01",
            "与伊莉娅&兰迪队\x01",
            "开始了新一场比赛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 49)
    Jump("loc_6029")

    label("loc_5F15")

    TurnDirection(0x101, 0x10, 500)

    #C0211
    ChrTalk(
        0x101,
        (
            "#12500F#6P#N嗯……那这次就和伊莉娅小姐组队吧。\x01",
            "伊莉娅小姐，请多指教。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x10, 0x101, 500)

    #C0212
    ChrTalk(
        0x10,
        "#13409F#5P#NOK，请多指教哦！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(500, 0, -1)
    OP_0D()
    SetChrName("")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "再次猜拳之后，\x01",
            "由瓦吉来担任\x01",
            "第二场比赛的裁判……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0214
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德&伊莉娅队\x01",
            "与兰迪&诺艾尔队\x01",
            "开始了新一场比赛。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 69)
    Jump("loc_6029")

    label("loc_6029")

    Return()

    # Function_38_4EEF end

    def Function_39_602A(): pass

    label("Function_39_602A")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x101, 20000, -6000, -15000, 180)
    SetChrPos(0x11, 20600, -6000, -17000, 0)
    SetChrPos(0x10, 19400, -6000, -17000, 0)
    SetChrPos(0x13, 20600, -6000, -18000, 0)
    SetChrPos(0x12, 19400, -6000, -18000, 0)
    SetChrPos(0x14, 26000, -6000, -16000, 0)
    ClearChrFlags(0x14, 0x8)
    OP_68(20000, -5000, -16000, 0)
    MoveCamera(305, 30, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0215
    ChrTalk(
        0x10,
        (
            "#6P#13409F……哈哈，玩得真开心呢。\x02\x03",

            "#13400F多亏有警察弟弟加入，\x01",
            "分组方式也丰富了很多。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#12500F哈哈，不过连续比赛两场，\x01",
            "还真是有些吃不消呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x11,
        (
            "#6P#12803F嗯，而且……\x02\x03",

            "#12809F没能看到期待的场面，\x01",
            "真是遗憾至极啊。\x02\x03",

            "#12806F本来还指望\x01",
            "诺艾尔能\x01",
            "爆些看点出来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x10,
        "#6P#13405F啊啊，对啊！！\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x13,
        (
            "#6P#12904F呵呵，结果却不知不觉\x01",
            "就专注在沙滩排球上了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x12, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0220
    ChrTalk(
        0x12,
        (
            "#6P#13006F前、前辈，还有瓦吉……\x01",
            "你们在说什么呢，真是的。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#12512F伊莉娅小姐的过激反应\x01",
            "倒真让我有些在意……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0222
    ChrTalk(
        0x101,
        (
            "#12500F啊，对了，\x01",
            "大家渴吗？\x02\x03",

            "如果有需要，我就去小卖部\x01",
            "买些冷饮回来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        (
            "#6P#13400F哦，警察弟弟好体贴啊。\x01",
            "嗯～要什么好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x11,
        (
            "#6P#12800F我听说米修拉姆\x01",
            "好像发售了一种\x01",
            "新型饮品呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x12,
        (
            "#6P#13000F哦哦，我也\x01",
            "听说过。\x02\x03",

            "#13004F好像是一种\x01",
            "叫做『铃铛可乐』，\x01",
            "口感很清爽的饮料。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x13,
        (
            "#6P#12902F呵呵，听起来\x01",
            "似乎不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#12500F那大家都喝\x01",
            "『铃铛可乐』，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x10,
        (
            "#6P#13400F嗯，麻烦你啦。\x02\x03",

            "#13404F不过现在还不是很渴，\x01",
            "也不用那么着急\x01",
            "去买。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#12500F哈哈，知道了，\x01",
            "那我稍后再带过来。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2B)
    OP_D7(0x2C)
    OP_D7(0x2D)
    OP_D7(0x2E)
    OP_D7(0x30)
    OP_D7(0x31)
    OP_D7(0x32)
    OP_D7(0x34)
    OP_D7(0x35)
    OP_D7(0x36)
    SetScenarioFlags(0x15E, 0)
    ModifyEventFlags(0, 3, 0x80)
    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrChipByIndex(0x13, 0xA)
    SetChrSubChip(0x13, 0x0)
    SetChrPos(0x14, 25950, -6000, -13400, 0)
    BeginChrThread(0x11, 0, 0, 0)
    BeginChrThread(0x12, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)
    BeginChrThread(0x13, 0, 0, 0)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    Return()

    # Function_39_602A end

    def Function_40_65EA(): pass

    label("Function_40_65EA")

    EventBegin(0x0)
    Fade(500)
    OP_68(19000, -4700, 20700, 0)
    MoveCamera(319, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 20500, -6000, 20700, 270)
    SetChrSubChip(0x9, 0x2)
    SetChrSubChip(0xA, 0x1)
    SetMapObjFlags(0x1, 0x1000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6F71")

    #C0230
    ChrTalk(
        0x8,
        "#5P#13302F啊，这不是罗伊德吗。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        "#11P#13502F呵呵，玩累了吧。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#12P#12504F塞茜尔姐姐，你们在做日光浴吗？\x02\x03",

            "#12500F还没下水，好像就已经\x01",
            "很开心了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "#5P#13304F嗯，光是在这里安静休息一下，\x01",
            "就已经非常享受了。\x02\x03",

            "#13309F而且还能和\x01",
            "艾莉、莉夏聊聊天。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        (
            "#12602F啊哈哈，我们虽然\x01",
            "也很开心……\x01",
            "但有件事情比较伤脑筋呢。\x02\x03",

            "#12606F塞茜尔小姐从刚才开始\x01",
            "就一直问些『和罗伊德的感情如何』\x01",
            "之类的问题。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x9,
        (
            "#11P#13509F嗯、嗯……\x01",
            "的确是有些吃惊呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0236
    ChrTalk(
        0x101,
        "#12P#12506F那、那个，塞茜尔姐姐……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "#5P#13309F呵呵，因为好在意嘛。\x02\x03",

            "身为姐姐，自然要随时关注\x01",
            "弟弟的交友关系。\x02\x03",

            "#13301F谁会成为你将来的新娘呢？\x01",
            "现在就要彻底确定！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#12P#12506F不、不要了，\x01",
            "那种事情还是算了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "#11P#13500F（嗯～真不愧是\x01",
            "  伊莉娅小姐的童年好友呢……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0240
    ChrTalk(
        0x8,
        (
            "#5P#13302F对了，罗伊德，\x01",
            "机会难得，你也\x01",
            "一起来做日光浴吧？\x02\x03",

            "#13309F还有空的躺椅，\x01",
            "我们正好可以聊一聊。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#12P#12512F不、不必了……\x01",
            "再怎么说，加入你们这里\x01",
            "也太不好意思了……\x02\x03",

            "#12500F这次就容我谢绝吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        "#5P#13305F哎，这样啊？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        (
            "#12600F呵呵，都已经来了，\x01",
            "还有什么好害羞的。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x9,
        (
            "#11P#13503F嗯，是啊，\x01",
            "我也有好多话想和你聊呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#12P#12502F哈哈，你们有此好意，\x01",
            "我心领就是了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0246
    ChrTalk(
        0x8,
        (
            "#5P#13303F嗯……既然如此……\x02\x03",

            "#13309F作为补偿，\x01",
            "你来帮我们涂\x01",
            "防晒霜如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0247
    ChrTalk(
        0x101,
        "#12P#12505F哎……………………\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0xC8, 0xBB8, 0x1F4)

    #C0248
    ChrTalk(
        0x101,
        "#12P#12511F#4S哎哎哎哎哎哎哎哎！？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xA,
        "#12605F等、等一下啊，塞茜尔小姐！\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        "#11P#13506F这、这终究有些……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#5P#13302F呵呵，这不是很好嘛，\x01",
            "反正我完全不介意哦～\x02\x03",

            "#13304F艾莉和莉夏之前不是\x01",
            "也说过，想尽量避免\x01",
            "被太阳晒黑吗？\x02\x03",

            "#13309F而且艾莉刚刚才说过\x01",
            "『都已经来了，还有什么好害羞的』，\x01",
            "这可是你自己的话哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        "#12605F那、那个……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0253
    ChrTalk(
        0xA,
        (
            "#12607F我、我知道了！\x02\x03",

            "#12613F那……\x01",
            "罗伊德，麻烦你啦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    #C0254
    ChrTalk(
        0x101,
        "#12P#12505F艾、艾莉……？\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "#12611F反、反正其他人都在\x01",
            "专心游玩吧？\x02\x03",

            "#12606F而且我确实说过\x01",
            "想防晒……\x02\x03",

            "#12613F与其让兰迪之类的人帮我涂，\x01",
            "让你来涂总要好一些。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0256
    ChrTalk(
        0x9,
        (
            "#11P#13503F说、说起来……\x02\x03",

            "#13506F我在酒店的房间里倒是\x01",
            "给伊莉娅小姐涂过防晒霜……\x02\x03",

            "#13502F那个……如果是罗伊德警官帮我涂，\x01",
            "倒也不会十分抵触。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    #C0257
    ChrTalk(
        0x101,
        "#12P#12511F连、连莉夏也……！？\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "#5P#13304F呵呵，好啦，罗伊德，\x01",
            "姐姐和两位可爱女孩\x01",
            "都已经开口请求你了。\x02\x03",

            "#13302F你会给我们涂防晒霜吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    SetScenarioFlags(0x15D, 0)
    Jump("loc_6FA7")

    label("loc_6F71")


    #C0259
    ChrTalk(
        0x8,
        (
            "#5P#13302F啊，罗伊德，\x01",
            "可以给我们涂\x01",
            "防晒霜了吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FA7")

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
            "给塞茜尔等人涂防晒霜\x01",      # 0
            "放弃\x01",                      # 1
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
        (0, "loc_7011"),
        (1, "loc_7019"),
        (SWITCH_DEFAULT, "loc_70E6"),
    )


    label("loc_7011")

    Call(0, 41)
    Jump("loc_70E6")

    label("loc_7019")


    #C0260
    ChrTalk(
        0x101,
        (
            "#12P#12511F那、那个，请稍等一下，\x01",
            "心理准备还没……！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "#5P#13302F啊……呵呵，真没办法。\x01",
            "那就稍后再说吧。\x02\x03",

            "#13304F不过要快点哦，\x01",
            "再这么下去，我们就要被晒黑了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 21500, -6000, 20700, 90)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    ClearMapObjFlags(0x1, 0x1000)
    EventEnd(0x5)
    Jump("loc_70E6")

    label("loc_70E6")

    Return()

    # Function_40_65EA end

    def Function_41_70E7(): pass

    label("Function_41_70E7")

    EventBegin(0x0)

    #C0262
    ChrTalk(
        0x101,
        (
            "#12P#12501F知、知道了……\x01",
            "我会小心涂的！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        "#12611F小心是指……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        (
            "#11P#13509F啊哈哈……\x01",
            "你好像有点紧张呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "#5P#13300F呵呵，那就赶快\x01",
            "帮我们涂吧。\x02\x03",

            "#13303F首先要给谁涂呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        "#12P#12506F这、这个……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0267
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K先给谁涂防晒霜呢？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "从艾莉开始涂\x01",        # 0
            "从塞茜尔开始涂\x01",      # 1
            "从莉夏开始涂\x01",        # 2
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
        (0, "loc_725E"),
        (1, "loc_779B"),
        (2, "loc_7D82"),
        (SWITCH_DEFAULT, "loc_83BE"),
    )


    label("loc_725E")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xA, 500)

    #C0268
    ChrTalk(
        0x101,
        (
            "#12P#12500F那就……\x01",
            "先给艾莉涂吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "#12612F我、我吗！？\x02\x03",

            "#12613F……可、可以是可以……\x01",
            "但是不要碰一些奇怪的地方哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        "#12P#12503F我、我会小心的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51321.itc", 0x1E)
    LoadChrToIndex("apl/ch51320.itc", 0x1F)
    LoadChrToIndex("apl/ch51319.itc", 0x20)
    LoadChrToIndex("apl/ch51318.itc", 0x21)
    OP_68(18400, -3700, 18300, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 18150, -5850, 18900, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0xA, 18400, -5900, 18300, 0)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_70(0x1, 0x2)
    SetChrSubChip(0x8, 0x2)
    OP_68(18400, -4700, 18300, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0271
    ChrTalk(
        0x101,
        (
            "#11P#12501F那、那就失礼了……\x02\x03",

            "#12503F（伸手摸）\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x64, 0xBB8, 0x12C)

    def lambda_7425():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_7425)

    #C0272
    ChrTalk(
        0xA,
        "#6P#12615F#4S……呀！！\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        "#11P#12505F抱、抱歉！没事吧？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "#6P#12613F嗯、嗯……\x01",
            "只是太凉了，稍微吃了一惊。\x02\x03",

            "#12602F已经没事了，请继续吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#11P#12503F是、是吗，那就……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13500, 9000)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    #C0276
    ChrTalk(
        0x101,
        (
            "#11P#12506F（呼，对心脏的刺激\x01",
            "  比想象中还要强啊……）\x02\x03",

            "#12508F（话说回来，\x01",
            "  艾莉真是很美呢……）\x02\x03",

            "#12503F（肌肤洁白如雪，\x01",
            "  银灰色的秀发\x01",
            "  就像在闪耀着光芒……）\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    #C0277
    ChrTalk(
        0xA,
        (
            "#6P#12612F……等、等一下，\x01",
            "请不要突然沉默啊。\x02\x03",

            "#12611F难道说……你正在想象一些\x01",
            "奇怪的事情吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x101,
        (
            "#11P#12511F绝、绝对没有！\x02\x03",

            "#12503F（要是处理不善，恐怕就真的要被\x01",
            "　玛丽亚贝尔小姐沉入湖底了……！！）\x02\x03",

            "#12501F（……总之什么都别再想了，\x01",
            "  必须要努力进入『无』的境界……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_4C(0x101, 0xFF)
    OP_63(0x9, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0279
    ChrTalk(
        0x9,
        (
            "#11P#N#13506F罗伊德警官的脸……\x01",
            "好像突然变得像\x01",
            "东街的地藏一样呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0280
    ChrTalk(
        0x8,
        (
            "#11P#13309F呵呵，罗伊德，\x01",
            "给艾莉涂完之后，\x01",
            "就该轮到我们了哦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_83BE")

    label("loc_779B")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0281
    ChrTalk(
        0x101,
        (
            "#12P#12500F那就……\x01",
            "先给塞茜尔姐姐涂吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "#5P#13309F呵呵，好的，\x01",
            "那就拜托啦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51321.itc", 0x1E)
    LoadChrToIndex("apl/ch51320.itc", 0x1F)
    LoadChrToIndex("apl/ch51319.itc", 0x20)
    LoadChrToIndex("apl/ch51318.itc", 0x21)
    OP_68(18400, -3700, 20800, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 18150, -5850, 21400, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x8, 18400, -5900, 20800, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x20)
    OP_70(0x1, 0x3)
    OP_68(18400, -4700, 20800, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    #C0283
    ChrTalk(
        0x101,
        "#11P#12500F……这样可以吗？塞茜尔姐姐。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "#6P#13304F嗯，就是这种感觉，\x01",
            "不过还要涂得更均匀广阔。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        "#11P#12500F嗯，知道啦。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#6P#13304F……呵呵，不知为何，\x01",
            "此情此景让我回想起了过去的往事呢。\x02\x03",

            "#13302F在罗伊德小时候，\x01",
            "我经常给他洗澡擦背呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0287
    ChrTalk(
        0x101,
        (
            "#11P#12511F哇啊啊啊，塞、塞茜尔姐姐！！\x01",
            "在大家面前不要说这些啊！！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_63(0x8, 0xFFFFFE0C, 1700, 0x2, 0x7, 0x50, 0x1)

    def lambda_7A3E():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_7A3E)

    #C0288
    ChrTalk(
        0x8,
        (
            "#6P#13306F呀！\x02\x03",

            "#13309F……呵呵，罗伊德真是的，\x01",
            "不可以乱碰奇怪的地方哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0289
    ChrTalk(
        0x101,
        "#11P#12511F哇，对、对不起！！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    SetCameraDistance(13500, 9000)
    Sleep(2000)

    #C0290
    ChrTalk(
        0x101,
        (
            "#11P#12506F（啊啊，真是的……\x01",
            "  塞茜尔姐姐未免也太没防备了吧！？）\x02\x03",

            "#12508F（而、而且，露出肌肤之后，\x01",
            "  视觉杀伤力实在是惊人……）\x02\x03",

            "#12506F（……呃！不行不行！\x01",
            "  怎么能对塞茜尔姐姐有这种想法！）\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    #C0291
    ChrTalk(
        0x8,
        (
            "#6P#13305F罗伊德，你怎么了？\x01",
            "从刚才开始，就一直\x01",
            "在同一个地方涂个不停……\x02\x03",

            "#13308F……难道是我太胖了吗？\x02\x03",

            "#13306F护士长和患者们\x01",
            "经常送我一些点心，\x01",
            "我总会忍不住吃掉……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#11P#12512F哪、哪里哪里，\x01",
            "完全没有那种事啦！！\x01",
            "塞茜尔姐姐的身材很棒，根本不用担心……\x02\x03",

            "#12506F……啊啊！不、不对！！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        "#6P#13309F呵呵，谢谢哦，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xA,
        (
            "#6P#12611F（唔……\x01",
            "  他们的关系一直这么暧昧呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "#11P#13509F（啊哈哈……\x01",
            "  和之前听说的一样呢。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_83BE")

    label("loc_7D82")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    #C0296
    ChrTalk(
        0x101,
        (
            "#12P#12500F那么……\x01",
            "莉夏，先从你开始涂吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        (
            "#11P#13505F好、好的！\x02\x03",

            "#13503F那个……礼仪不周之处，\x01",
            "还请多多包涵。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0298
    ChrTalk(
        0x101,
        "#12P#12506F……这、这话好像应该由我来说吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("apl/ch51321.itc", 0x1E)
    LoadChrToIndex("apl/ch51320.itc", 0x1F)
    LoadChrToIndex("apl/ch51319.itc", 0x20)
    LoadChrToIndex("apl/ch51318.itc", 0x21)
    OP_68(18400, -3700, 23200, 0)
    MoveCamera(315, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 18150, -5850, 23800, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x9, 18400, -5900, 23200, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x20)
    OP_70(0x1, 0x4)
    SetChrSubChip(0x8, 0x1)
    OP_68(18400, -4700, 23200, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    #C0299
    ChrTalk(
        0x101,
        "#11P#12502F嗯嗯……涂、涂得可以吗？\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "#6P#13503F啊，嗯，\x01",
            "没问题，就是这种感觉。\x02\x03",

            "#13506F呼，真是多谢了。\x01",
            "因为要在彩虹剧团的舞台上演出，\x01",
            "所以绝对不能晒黑。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#11P#12500F啊，是吗？\x02\x03",

            "#12505F哎，不过……\x01",
            "你不是帮伊莉娅小姐\x01",
            "涂了防晒霜吗？\x02\x03",

            "#12511F涂完以后，只要让她再来\x01",
            "给你涂不就——呃，哦哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x9,
        (
            "#6P#13509F嗯……那个……啊哈哈，\x01",
            "正如你所想。\x02\x03",

            "#13506F如果穿着这种毫无防备的装扮，\x01",
            "暴露在伊莉娅小姐的面前，\x01",
            "还不知道会有什么下场呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetCameraDistance(13500, 9000)

    #C0303
    ChrTalk(
        0x101,
        (
            "#11P#12512F（也就是说，和大叔心的伊莉娅小姐相比，\x01",
            "  反而是我更加安全吗……\x01",
            "  这理由也让人心情复杂呢。）\x02\x03",

            "#12501F（……话说回来，\x01",
            "  虽然从表面上很难看出，\x01",
            "  但莉夏似乎经受过相当程度的锻炼呢。）\x02\x03",

            "#12508F（既保持着如此匀称的身材，\x01",
            "  又能锻炼出那么惊人的身体能力……\x01",
            "  这大概也是她的才能吧。）\x02\x03",

            "#12503F（而且，更重要的是……\x01",
            "  这种身高就能拥有如此尺寸，\x01",
            "  就算称之为凶器恐怕也不为过……）\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    #C0304
    ChrTalk(
        0x9,
        "#6P#13505F罗、罗伊德警官？那个，你的视线……\x02",
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0305
    ChrTalk(
        0x101,
        (
            "#11P#12511F哇，抱、抱歉！\x02\x03",

            "#12512F不、不是……那个，\x01",
            "我只是在想……你果然努力锻炼过啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xA,
        (
            "#6P#N#12611F呼……男人\x01",
            "全都是这样子吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0307
    ChrTalk(
        0x8,
        (
            "#13309F呵呵，罗伊德，\x01",
            "给莉夏涂完之后，\x01",
            "就该轮到我们了哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_83BE")

    label("loc_83BE")

    EndChrThread(0x101, 0xFF)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 20300, -6000, 17500, 315)
    SetChrPos(0x9, 18400, -5900, 23000, 0)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrFlags(0x9, 0x20)
    SetChrPos(0x8, 18400, -5900, 20600, 0)
    SetChrChipByIndex(0x8, 0x20)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x20)
    SetChrPos(0xA, 18400, -5900, 18100, 0)
    SetChrChipByIndex(0xA, 0x21)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x20)
    OP_70(0x1, 0x6)
    Sleep(2000)
    OP_68(18400, -5000, 24100, 0)
    MoveCamera(315, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    OP_68(18400, -5000, 18200, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(19000, -5000, 20000, 0)
    MoveCamera(319, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0308
    ChrTalk(
        0x101,
        (
            "#6P#12506F（仔、仔细一看，\x01",
            "  还真是惊人的画面啊……）\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "#5P#13304F呼～谢谢啦，罗伊德，\x01",
            "感觉完全舒缓下来了。\x02\x03",

            "#13309F呵呵呵，这样下去好像就要睡着了。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xA,
        (
            "#1P#12606F塞、塞茜尔小姐，\x01",
            "穿成这样子睡觉，\x01",
            "实在是有些危险……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x9,
        (
            "#2P#13509F啊哈哈……\x01",
            "确实是过于随意了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        "#13304F呵呵，因为感觉很舒服嘛。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0313
    ChrTalk(
        0x101,
        (
            "#6P#12500F那我去买些饮料回来，\x01",
            "让大家提提神吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xA,
        "#1P#12605F啊，可以吗？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#6P#12503F（从某种意义上说，我刚刚经历过\x01",
            "  有如梦幻般的体验……）\x02\x03",

            "#12512F（如果连这点事情都不主动去做，\x01",
            "  女神恐怕都会降下天罚的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x9,
        "#2P#13505F……罗伊德警官？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#6P#12512F啊、啊啊，没什么。\x02\x03",

            "#12500F那无酒精的鸡尾酒\x01",
            "可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#5P#13302F嗯，麻烦你了。\x02\x03",

            "#13309F不用太着急，\x01",
            "你也多玩一会吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#6P#12500F好的，谢谢，\x01",
            "那就稍后见啦。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    SetScenarioFlags(0x15D, 1)
    Call(0, 45)
    SetChrPos(0x9, 18200, -5650, 23100, 90)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x9, 0x20)
    SetChrPos(0x8, 18200, -5650, 20700, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x8, 0x2)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x8, 0x20)
    SetChrPos(0xA, 18200, -5650, 18200, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xA, 0x20)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    ClearMapObjFlags(0x1, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_88D3")
    Call(0, 54)
    EventEnd(0x5)
    Jump("loc_88E6")

    label("loc_88D3")

    SetChrPos(0x0, 21500, -6000, 20700, 90)
    EventEnd(0x5)

    label("loc_88E6")

    Return()

    # Function_41_70E7 end

    def Function_42_88E7(): pass

    label("Function_42_88E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88FE")
    OP_A0(0xFE, 500, 0x0, 0x3)
    Jump("Function_42_88E7")

    label("loc_88FE")

    Return()

    # Function_42_88E7 end

    def Function_43_88FF(): pass

    label("Function_43_88FF")

    EventBegin(0x0)
    Fade(500)
    OP_68(32000, -4750, 6750, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13250, 0)
    SetCameraDistance(12750, 2500)
    SetChrPos(0x101, 30690, -6000, 8050, 135)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E42")

    #C0320
    ChrTalk(
        0xC,
        "#6P#13101F（堆积）……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        "#12P#12701F（拍打）……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0322
    ChrTalk(
        0x101,
        "#11P#12505F（怎、怎么回事，精神好集中啊……）\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xD,
        "#01200F……咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8AB9")
    Jump("loc_8B03")

    label("loc_8AB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8AD9")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B03")

    label("loc_8AD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8AF9")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8B03")

    label("loc_8AF9")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8B03")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8BB9")
    Jump("loc_8C03")

    label("loc_8BB9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8BD9")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C03")

    label("loc_8BD9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BF9")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8C03")

    label("loc_8BF9")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8C03")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0324
    ChrTalk(
        0xB,
        "#12P#12705F……啊，是罗伊德前辈。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        "#6P#13100F有什么事吗～？\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#11P#12512F哈哈，好像打搅到你们了啊。\x02\x03",

            "#12500F这个……我只是有点好奇，\x01",
            "想看看你们这么认真在做些什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xC,
        (
            "#6P#13100F不不，没什么啦。\x02\x03",

            "#13109F只是在建造\x01",
            "沙之城堡而已～\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        (
            "#12P#12700F也就是『堆沙堡』啦。\x02\x03",

            "#12706F不过一直都堆不好……\x01",
            "之前堆了好几次，每次都会塌掉。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        "#11P#12503F嗯～看起来好像很难呢。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "#6P#13100F对了，机会难得，\x01",
            "罗伊德警官也来帮忙如何～？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        "#11P#12505F哎……我吗？\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xB,
        (
            "#12P#12702F嗯，是啊，如果有你加入，\x01",
            "或许能取得一些进展呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 1)
    Jump("loc_90BE")

    label("loc_8E42")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8ED3")
    Jump("loc_8F1D")

    label("loc_8ED3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8EF3")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F1D")

    label("loc_8EF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8F13")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_8F1D")

    label("loc_8F13")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8F1D")

    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xB, 0x10)
    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 0)
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FD3")
    Jump("loc_901D")

    label("loc_8FD3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_8FF3")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_901D")

    label("loc_8FF3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9013")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_901D")

    label("loc_9013")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_901D")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0333
    ChrTalk(
        0xC,
        (
            "#6P#13100F啊，罗伊德警官，\x01",
            "要帮我们堆\x01",
            "沙之城堡吗～？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        (
            "#12P#12702F请务必帮忙，如果有你加入，\x01",
            "或许能取得一些进展呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_90BE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "帮忙堆沙堡\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_91FE")

    #C0335
    ChrTalk(
        0x101,
        (
            "#11P#12500F嗯，知道啦。\x01",
            "如不嫌弃，我就来帮些忙吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xC,
        (
            "#6P#13109F不愧是罗伊德警官！\x01",
            "谢谢～！\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#11P#12502F哈哈，话虽如此，\x01",
            "但我之前也从没堆过呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xB,
        (
            "#12P#12702F没关系，大家都差不多。\x02\x03",

            "#12704F那就请赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 44)
    Call(0, 45)
    Jump("loc_92CD")

    label("loc_91FE")


    #C0339
    ChrTalk(
        0x101,
        "#11P#12512F唔……现在有点不方便……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xC,
        "#6P#13106F哎，这样啊……\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xB,
        (
            "#12P#12702F算了，等你有兴趣的时候\x01",
            "再来找我们吧。\x02\x03",

            "#12704F在那之前，我先和芙兰小姐\x01",
            "一起努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xD,
        "#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)

    label("loc_92CD")

    SetChrPos(0x0, 29920, -6000, 8910, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_92F6")
    Call(0, 54)

    label("loc_92F6")

    EventEnd(0x5)
    Return()

    # Function_43_88FF end

    def Function_44_92F9(): pass

    label("Function_44_92F9")

    LoadChrToIndex("chr/ch15200.itc", 0x1E)
    SetChrChipByIndex(0xB, 0x1E)
    SetChrSubChip(0xB, 0x0)
    ClearChrBattleFlags(0xB, 0x4)
    SetChrChipByIndex(0xC, 0x1)
    SetChrSubChip(0xC, 0x0)
    ClearChrBattleFlags(0xC, 0x4)
    OP_70(0xA, 0x1)
    FadeToBright(1000, 0)
    OP_0D()

    #C0343
    ChrTalk(
        0xC,
        "#6P#13100F……呼，已经算是基本完成了呢～\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xB,
        "#12P#12700F嗯，距离完成只差一步——\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    Sound(1023, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    OP_70(0xA, 0x3)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0345
    ChrTalk(
        0xD,
        "#01203F……嗷。\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xB,
        "#12P#12706F……果然很难呢。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#11P#12500F唔……\x01",
            "或许是沙子的\x01",
            "强度有问题吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xC,
        (
            "#6P#13105F强度吗……\x02\x03",

            "#13106F可我们已经把沙子和水一起放在桶里搅拌，\x01",
            "建造了很坚固的地基啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#11P#12500F但在堆积过程中，\x01",
            "沙子还是会渐渐变干的。\x02\x03",

            "#12504F我以前好像听说过，\x01",
            "应该在堆积的同时补充水分。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xB,
        (
            "#12P#12705F原来如此……\x01",
            "似乎很有道理。\x02\x03",

            "#12702F那么，每次应该补充\x01",
            "多少水分才合适呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        "#11P#12503F嗯，这个嘛……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0352
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要补充多少水量？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "适中的\x01",      # 0
            "稍多的\x01",      # 1
            "稍少的\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9720")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0353
    ChrTalk(
        0x101,
        (
            "#11P#12500F应该稍微补充些水……\x01",
            "只要让沙子保持湿润就没问题了。\x02\x03",

            "#12504F如果水分过多，\x01",
            "反而有可能使强度降低。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xC,
        (
            "#6P#13100F听你这么一说，\x01",
            "好像的确如此呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xB,
        (
            "#12P#12702F那就按照罗伊德前辈\x01",
            "说的试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9827")

    label("loc_9720")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9787")

    #C0356
    ChrTalk(
        0x101,
        (
            "#11P#12500F还是应该\x01",
            "尽量补充\x01",
            "适中的水量吧？\x02\x03",

            "#12504F我觉得这样才能\x01",
            "提升强度。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_97D5")

    label("loc_9787")


    #C0357
    ChrTalk(
        0x101,
        (
            "#11P#12500F应该补充\x01",
            "稍多一些的水量吧？\x02\x03",

            "#12504F我觉得这样才能\x01",
            "提升强度。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_97D5")


    #C0358
    ChrTalk(
        0xC,
        "#6P#13105F是这样吗～？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xB,
        (
            "#12P#12700F好吧，就按照罗伊德前辈\x01",
            "说的试试看吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9827")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9979")
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0360
    ChrTalk(
        0xB,
        "#12P#12702F已经临近完成了呢。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xC,
        (
            "#6P#13109F嗯嗯，多亏有罗伊德警官\x01",
            "的指点。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        "#11P#12502F哈哈，多谢夸奖。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0363
    ChrTalk(
        0xB,
        (
            "#12P#12702F呵呵……终于要到\x01",
            "最后一步啦。\x02\x03",

            "接下来要给主城的部分\x01",
            "做一些细微修饰……\x01",
            "可以请罗伊德前辈来完成吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AF1")

    label("loc_9979")


    #C0364
    ChrTalk(
        0xB,
        "#12P#12700F都已经很接近完成了呢，结果还是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0365
    ChrTalk(
        0xC,
        "#6P#13105F不、不知为何，看起来似乎不太坚固呢～\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#11P#12506F（唔、唔……\x01",
            "  水大概还是放多了吧……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0367
    ChrTalk(
        0xB,
        (
            "#12P#12703F算了，目前看来，\x01",
            "似乎也不会塌掉……\x01",
            "赶快开始最后的工序吧。\x02\x03",

            "#12702F接下来要给主城的部分\x01",
            "做一些细微修饰……\x01",
            "可以请罗伊德前辈来完成吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AF1")


    #C0368
    ChrTalk(
        0x101,
        (
            "#11P#12500F嗯，明白了，\x01",
            "交给我吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0369
    ChrTalk(
        0xC,
        (
            "#6P#13100F一切都交给罗伊德警官了！\x01",
            "拜托啦～！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0370
    ChrTalk(
        0x101,
        (
            "#11P#12506F（突、突然增加了\x01",
            "  不少心理压力呢……\x01",
            "  算啦，也只能试试看了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#11P#12501F（嗯……虽然凭借水的作用\x01",
            "  而增强了坚固性，\x01",
            "  但素材毕竟只是沙子……）\x02\x03",

            "#12503F（最重要的恐怕就是\x01",
            "  速度与力道的控制。\x01",
            "  ……要怎样完成呢？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要如何控制速度与力道？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "缓慢／轻柔\x01",      # 0
            "缓慢／强劲\x01",      # 1
            "迅速／轻柔\x01",      # 2
            "迅速／强劲\x01",      # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9D13"),
        (1, "loc_9D5C"),
        (2, "loc_9DA5"),
        (3, "loc_9DF8"),
        (SWITCH_DEFAULT, "loc_9E41"),
    )


    label("loc_9D13")


    #C0373
    ChrTalk(
        0x101,
        (
            "#11P#12500F（好……就用缓慢又细腻的手法\x01",
            "  来完成修饰工作吧！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E41")

    label("loc_9D5C")


    #C0374
    ChrTalk(
        0x101,
        (
            "#11P#12500F（好……就用缓慢又强劲的手法\x01",
            "  来完成修饰工作吧！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E41")

    label("loc_9DA5")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0375
    ChrTalk(
        0x101,
        (
            "#11P#12500F（好……就用迅速又细腻的手法\x01",
            "  来完成修饰工作吧！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E41")

    label("loc_9DF8")


    #C0376
    ChrTalk(
        0x101,
        (
            "#11P#12500F（好……就用迅速又强劲的手法\x01",
            "  来完成修饰工作吧！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9E41")

    label("loc_9E41")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9E5F")
    Jump("loc_A1B7")

    label("loc_9E5F")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    Sound(1023, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    OP_70(0xA, 0x3)
    OP_0D()

    #C0377
    ChrTalk(
        0x101,
        "#11P#12511F#4S啊。#3S\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xB,
        "#12P#12705F啊……\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xC,
        (
            "#6P#13100F啊……啊哈哈，\x01",
            "失败了呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xB, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0380
    ChrTalk(
        0x101,
        (
            "#11P#12505F哎，这个，该怎么说呢……\x02\x03",

            "#12506F……真对不起。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0381
    ChrTalk(
        0xB,
        (
            "#12P#12703F……算啦，这也没办法。\x02\x03",

            "#12700F总之，我们就从零开始，\x01",
            "重新再建一个吧。\x02\x03",

            "罗伊德前辈，请你\x01",
            "协助我和芙兰小姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#11P#12512F知、知道了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0383
    ChrTalk(
        0xC,
        (
            "#6P#13109F罗伊德警官，\x01",
            "请不要沮丧哦～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0F5")

    #C0384
    ChrTalk(
        0x101,
        (
            "#11P#12506F（水量应该掌握得\x01",
            "  正合适啊……）\x02\x03",

            "（呼……真是没面子。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B7")

    label("loc_A0F5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A15B")

    #C0385
    ChrTalk(
        0x101,
        (
            "#11P#12506F（速度与力道应该控制得\x01",
            "  没有问题啊……）\x02\x03",

            "（呼……真是没面子。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A1B7")

    label("loc_A15B")


    #C0386
    ChrTalk(
        0x101,
        (
            "#11P#12506F（看来水量的掌握，\x01",
            "  还有速度和力道都有问题啊……）\x02\x03",

            "（呼……真是没面子。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A1B7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x2)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0387
    ChrTalk(
        0x101,
        "#11P#12500F呼……这样就行了吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0388
    ChrTalk(
        0xC,
        (
            "#6P#13100F终于……\x01",
            "终于完成了啊～！！\x02\x03",

            "#13109F哇～！太棒了太棒了～！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A344")
    OP_2C(0xA5, 0x1)
    TurnDirection(0xB, 0x101, 500)

    #C0389
    ChrTalk(
        0xB,
        (
            "#12P#12704F……真让人感慨。\x01",
            "罗伊德前辈，辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        (
            "#11P#12502F哈哈……没什么，\x01",
            "多亏你们二位的努力。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0391
    ChrTalk(
        0xC,
        (
            "#6P#13109F哪里哪里，全靠罗伊德警官才能成功～！\x01",
            "真是太感谢了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A3FA")

    label("loc_A344")

    TurnDirection(0xB, 0x101, 500)

    #C0392
    ChrTalk(
        0xB,
        (
            "#12P#12702F……总之，真是太好了。\x01",
            "虽然在完成之前经历过种种挫折。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#11P#12506F那、那个……真是抱歉。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0394
    ChrTalk(
        0xC,
        (
            "#6P#13109F啊哈哈，不用在意啦～\x01",
            "最后终于还是成功了嘛！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A3FA")

    TurnDirection(0xB, 0xD, 500)

    #C0395
    ChrTalk(
        0xB,
        (
            "#12P#12702F#5P蔡特也辛苦了。\x02\x03",

            "#12704F在搭建终期，还特地帮我们\x01",
            "运送不够的沙子和水。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xD,
        "#01200F咕呜呜……嗷。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    #C0397
    ChrTalk(
        0x101,
        "#11P#12500F#5P哈哈，真不愧是蔡特啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    #C0398
    ChrTalk(
        0x101,
        (
            "#11P#12505F对了，说起来……\x01",
            "这座城堡有名字了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0xC, 0x5A, 0x1F4)
    OP_93(0xB, 0xB4, 0x1F4)

    #C0399
    ChrTalk(
        0xC,
        "#6P#13105F名字吗……？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        (
            "#11P#12500F嗯，如此辛苦才建成，\x01",
            "如果起个名字，\x01",
            "应该能留下很好的回忆吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xB,
        (
            "#12P#12703F有道理呢。\x01",
            "嗯，那么……\x02\x03",

            "#12700F就叫『咪西城堡』吧，\x01",
            "这个名字如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xC,
        (
            "#6P#13105F哎～缇欧好狡猾！\x02\x03",

            "#13109F我觉得还是叫\x01",
            "『邦邦城堡』比较好～！\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#11P#12500F咪西是著名吉祥物……\x02\x03",

            "#12503F而邦邦好像是\x01",
            "芙兰很喜爱的\x01",
            "玩偶的名字吧。\x02\x03",

            "#12509F哈哈……两个名字\x01",
            "都很有意思呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0404
    ChrTalk(
        0xB,
        (
            "#12P#12703F……可是一座城堡\x01",
            "总不能取两个名字。\x02\x03",

            "#12700F既然如此，就让罗伊德前辈\x01",
            "来决定如何？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0405
    ChrTalk(
        0xC,
        (
            "#6P#13100F啊，这样也好～！\x02\x03",

            "#13109F只要是罗伊德警官决定的，\x01",
            "我就没有意见，\x01",
            "请随意选择吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0406
    ChrTalk(
        0x101,
        (
            "#11P#12506F（这、这可真是责任重大啊。）\x02\x03",

            "#12500F唔，这个嘛……\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0407
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K给城堡取哪个名字？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "咪西城堡\x01",      # 0
            "邦邦城堡\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A943")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xB, 500)

    #C0408
    ChrTalk(
        0x101,
        (
            "#11P#12503F#5P对了，难得来到\x01",
            "米修拉姆……\x02\x03",

            "#12500F不如还是命名为\x01",
            "『咪西城堡』吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0409
    ChrTalk(
        0xC,
        (
            "#6P#13106F唔～这样一说，也有道理呢～\x02\x03",

            "#13102F没办法，这次就\x01",
            "听缇欧的吧！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    #C0410
    ChrTalk(
        0xB,
        "#12P#12702F呵呵……谢谢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_AA44")

    label("loc_A943")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xC, 500)

    #C0411
    ChrTalk(
        0x101,
        (
            "#11P#12503F#11P对了，反正接下来\x01",
            "还要和咪西见面很多次……\x02\x03",

            "#12500F不如还是命名为\x01",
            "『邦邦城堡』吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    #C0412
    ChrTalk(
        0xB,
        (
            "#12P#12703F……唔，也有道理啊。\x02\x03",

            "#12702F算了，就这样吧，\x01",
            "这次就采用芙兰小姐的方案。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0413
    ChrTalk(
        0xC,
        "#6P#13109F呵呵，谢谢啦，缇欧！\x02",
    )

    CloseMessageWindow()

    label("loc_AA44")

    OP_93(0x101, 0x87, 0x1F4)

    #C0414
    ChrTalk(
        0x101,
        (
            "#11P#12509F呵呵，圆满收场了啊。\x02\x03",

            "#12505F对了……缇欧、芙兰，\x01",
            "一直待在沙滩，你们有些渴了吧？\x02\x03",

            "#12500F如果有需要，我稍后给你们\x01",
            "带些冷饮之类的回来吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    TurnDirection(0xC, 0x101, 500)

    #C0415
    ChrTalk(
        0xB,
        (
            "#12P#12703F确实有点呢……\x02\x03",

            "#12700F嗯，那我要吃\x01",
            "刨冰。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xC,
        (
            "#6P#13100F啊，我也想吃～！\x02\x03",

            "#13109F罗伊德警官，可以帮我们带来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        (
            "#11P#12509F嗯，没问题。\x02\x03",

            "#12500F蔡特……\x01",
            "给你带根大香肠可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xD,
        "#01203F咕呜呜呜……嗷。\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xB,
        (
            "#12P#12702F它在说『麻烦你了』。\x02\x03",

            "#12703F……哦，不过并\x01",
            "不急哦。\x02\x03",

            "#12702F难得来这里一次，\x01",
            "罗伊德前辈也多玩玩吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        "#11P#12502F哈哈，知道了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x15E, 2)
    SetChrChipByIndex(0xB, 0x7)
    SetChrSubChip(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrChipByIndex(0xC, 0x1)
    SetChrSubChip(0xC, 0x0)
    ClearChrBattleFlags(0xC, 0x4)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)
    OP_49()
    OP_D7(0x1E)
    Return()

    # Function_44_92F9 end

    def Function_45_ACCF(): pass

    label("Function_45_ACCF")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_END)), "loc_ACEC")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ACEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_END)), "loc_ACFF")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_ACFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_END)), "loc_AD12")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_AD12")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD59")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_AD59")

    Return()

    # Function_45_ACCF end

    def Function_46_AD5A(): pass

    label("Function_46_AD5A")

    EventBegin(0x0)
    Fade(500)
    OP_68(44860, -6090, 2460, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13250, 0)
    SetCameraDistance(12750, 2000)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    SetChrPos(0x101, 44110, -7060, 2460, 90)
    OP_6F(0x79)
    OP_0D()
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B19F")

    #C0421
    ChrTalk(
        0xE,
        (
            "#13209F#6P哇哇哇……\x01",
            "修利的石头也很漂亮！\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xF,
        (
            "#13603F#11P哼、哼，没什么大不了的。\x02\x03",

            "#13600F话说回来，\x01",
            "以前从没见过这样的石头呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#12500F#5P你们两个已经回来了啊。\x01",
            "……在做什么呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AEBE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_AEBE)
    Sleep(50)

    def lambda_AECE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_AECE)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    #C0424
    ChrTalk(
        0xE,
        (
            "#13210F#12P啊，罗伊德。\x01",
            "看这个！\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xE,
        "#13209F#12P嘿嘿嘿，很漂亮吧？\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        (
            "#12500F#5P哎，雪白又滚圆的石头……\x01",
            "简直像宝石一样漂亮啊。\x02\x03",

            "#12505F这是在哪里找到的？\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xF,
        (
            "#13600F#12P刚才游泳的时候，\x01",
            "这个小鬼头捡到的。\x02\x03",

            "#13604F附近似乎\x01",
            "还有一些，\x01",
            "我们就一起找了找。\x02\x03",

            "#13602F问了一下救生员，\x01",
            "据说这东西\x01",
            "叫做『纯白之石』。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x101,
        (
            "#12500F#5P唔……这里的沙子好像\x01",
            "都是从外国运来的……\x02\x03",

            "#12503F其中应该混杂着当地\x01",
            "特有的产物。\x02\x03",

            "#12500F所以，说不定可以在这里\x01",
            "找到很大的石头呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0429
    ChrTalk(
        0xE,
        (
            "#13205F#12P真的吗！？\x02\x03",

            "#13200F嘿嘿，那大家一起来找\x01",
            "白色的石头吧！\x02\x03",

            "#13209F最后带回最大石头\x01",
            "的人就算胜利！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0430
    ChrTalk(
        0xF,
        (
            "#13602F#12P呵呵，很有趣嘛。\x02\x03",

            "#13604F你当然也会参加吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 6)
    Jump("loc_B21F")

    label("loc_B19F")


    def lambda_B1A4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_B1A4)
    Sleep(50)

    def lambda_B1B4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_B1B4)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    #C0431
    ChrTalk(
        0xF,
        (
            "#13600F#12P嗯，你还是\x01",
            "想参加吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xE,
        (
            "#13202F#12P罗伊德也来\x01",
            "一起寻找\x01",
            "『纯白之石』吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B21F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "开始寻找纯白之石\x01",      # 0
            "放弃\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B44C")

    #C0433
    ChrTalk(
        0x101,
        (
            "#12500F#5P嗯，机会难得，\x01",
            "就让我也参加吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xE,
        "#13209F#12P就这么定啦！\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xF,
        (
            "#13600F#12P那么，如果你\x01",
            "找到了『纯白之石』，\x01",
            "就来告诉我。\x02\x03",

            "#13604F我们到时候来比较大小，\x01",
            "谁的最大就算赢。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x101,
        "#12509F#5P哈哈，明白了。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xE,
        (
            "#13201F#12P好……\x01",
            "比赛开始！\x02\x03",

            "#13200F琪雅一定会找到\x01",
            "最大的石头！\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xF,
        (
            "#13603F#12P哼，我是不会\x01",
            "输给你们的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x15C, 0)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)
    ClearScenarioFlags(0x1, 4)
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)
    OP_66(0x5, 0x1)
    OP_66(0x6, 0x1)
    OP_66(0x7, 0x1)
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    SetChrPos(0x0, 45110, -7080, 2460, 90)
    Jump("loc_B514")

    label("loc_B44C")


    #C0439
    ChrTalk(
        0x101,
        "#12512F#5P唔，现在还不太方便。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xE,
        "#13205F#12P哎，这样啊？\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xF,
        (
            "#13606F#12P啧，真是扫兴的家伙。\x02\x03",

            "#13600F算了，等你有兴趣时再来和我说，\x01",
            "到时让你也加入。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0xE, 0x0, 0x0)
    OP_93(0xF, 0xB4, 0x0)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    SetChrPos(0x0, 43610, -7090, 2460, 270)

    label("loc_B514")

    EventEnd(0x5)
    Return()

    # Function_46_AD5A end

    def Function_47_B517(): pass

    label("Function_47_B517")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0442
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0443
    ChrTalk(
        0x101,
        (
            "#12503F嗯，似乎小了点吧？\x02\x03",

            "应该还能找到更大的……\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x15C, 1)
    TalkEnd(0xFF)
    Return()

    # Function_47_B517 end

    def Function_48_B5A3(): pass

    label("Function_48_B5A3")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0444
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0445
    ChrTalk(
        0x101,
        (
            "#12505F找到了……但很小啊。\x02\x03",

            "再找找看如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x15C, 2)
    TalkEnd(0xFF)
    Return()

    # Function_48_B5A3 end

    def Function_49_B629(): pass

    label("Function_49_B629")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0446
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0447
    ChrTalk(
        0x101,
        (
            "#12500F这种大小……\x01",
            "用手掌正好可以握住呢。\x02\x03",

            "#12503F琪雅和修利好像\x01",
            "也找到了差不多大的……\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x5, 0x1)
    SetScenarioFlags(0x15C, 3)
    TalkEnd(0xFF)
    Return()

    # Function_49_B629 end

    def Function_50_B6DC(): pass

    label("Function_50_B6DC")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0448
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0449
    ChrTalk(
        0x101,
        (
            "#12503F……还算比较大吧。\x02\x03",

            "#12500F如果拿它去比赛，\x01",
            "或许会有一定胜算……\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x15C, 4)
    TalkEnd(0xFF)
    Return()

    # Function_50_B6DC end

    def Function_51_B77E(): pass

    label("Function_51_B77E")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0450
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0451
    ChrTalk(
        0x101,
        (
            "#12505F噢噢……！？\x01",
            "这尺寸就像水晶球一样啊！\x02\x03",

            "#12509F哈哈，找到了这么大的，\x01",
            "应该不会输了。\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x7, 0x1)
    SetScenarioFlags(0x15C, 5)
    TalkEnd(0xFF)
    Return()

    # Function_51_B77E end

    def Function_52_B833(): pass

    label("Function_52_B833")

    EventBegin(0x0)
    Fade(500)
    SetChrPos(0x101, 18310, -6000, 15790, 0)
    SetChrSubChip(0xA, 0x2)
    OP_68(18950, -4400, 16440, 0)
    MoveCamera(312, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10000, 0)
    OP_0D()

    #C0452
    ChrTalk(
        0xA,
        "#12605F啊，罗伊德，你在做什么？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#6P#12500F哦，正在和琪雅她们……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0454
    ChrTalk(
        0x101,
        "#6P#12505F哎，莫非……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0455
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德把手伸向了\x01",
            "躺椅下面。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0456
    ChrTalk(
        0xA,
        "#12612F哎，等、等一下……！？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        "#6P#12502F──找到了！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0458
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '纯白之石'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('纯白之石', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0459
    ChrTalk(
        0x101,
        (
            "#6P#12500F竟然会埋藏在\x01",
            "这种地方……\x02\x03",

            "#12504F话说回来，真是相当大啊。\x01",
            "有了它，绝对可以取胜。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0460
    ChrTalk(
        0xA,
        (
            "#12611F我、我说你啊……\x01",
            "突然钻到那种地方，\x01",
            "究竟有何企图？\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        "#6P#12511F啊……对、对不起！\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xA,
        "#12606F呼，真是的。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x15C, 6)
    EventEnd(0x5)
    Return()

    # Function_52_B833 end

    def Function_53_BAC6(): pass

    label("Function_53_BAC6")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_68(44860, -6090, 2460, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13250, 0)
    SetCameraDistance(12750, 2000)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrPos(0xE, 45610, -7090, 1880, 270)
    SetChrPos(0xF, 45610, -7090, 3000, 270)
    SetChrPos(0x101, 44110, -7060, 2460, 90)
    SetChrSubChip(0xE, 0x0)
    SetChrSubChip(0xF, 0x0)
    OP_6F(0x79)
    OP_0D()

    #C0463
    ChrTalk(
        0xF,
        (
            "#12P#13600F那就来比比大小吧。\x02\x03",

            "#13603F喊完『一二三』之后，\x01",
            "我们同时把自己找到的\x01",
            "最大石头拿出来。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        "#5P#12500F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xE,
        "#12P#13210F准备好啦！\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xF,
        "#12P#13601F好，那就开始了……\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        "#5P#12501F一、二……\x02",
    )


    #C0468
    ChrTalk(
        0xE,
        "#3P#13201F一、二……\x02",
    )


    #C0469
    ChrTalk(
        0xF,
        "#4P#13601F一、二～\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#5P#12500F#4S三！#3S\x02",
    )


    #C0471
    ChrTalk(
        0xE,
        "#3P#13200F#4S三！！#3S\x02",
    )


    #C0472
    ChrTalk(
        0xF,
        "#4P#13600F#4S三！#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C512")
    OP_2C(0xA5, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0473
    ChrTalk(
        0xE,
        (
            "#12P#13210F哇哇哇……！！\x01",
            "罗伊德的『纯白之石』\x01",
            "好大啊！！\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xF,
        (
            "#12P#13601F唔……竟然能找到\x01",
            "那么大的……\x02\x03",

            "#13606F既然如此，看来也只能\x01",
            "老老实实地认输啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        (
            "#5P#12502F哈哈，\x01",
            "好像是我赢了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xF,
        "#12P#13606F嘁，和小孩子如此认真，真没大人风度。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0477
    ChrTalk(
        0x101,
        (
            "#5P#12506F……被你这么一说，\x01",
            "感觉好没面子啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xE,
        (
            "#12P#13200F不过，确实又大又漂亮呢。\x02\x03",

            "#13206F琪雅也想要那样的石头。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xF,
        (
            "#12P#13600F说的也是啊……\x01",
            "我也再去找找看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C0AA")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0480
    ChrTalk(
        0x101,
        (
            "#5P#12500F哈哈，\x01",
            "那就把这两块『纯白之石』\x01",
            "送给你们当礼物吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0481
    ChrTalk(
        0xE,
        "#12P#13210F真的吗！？\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xF,
        (
            "#12P#13605F可、可以吗？\x01",
            "另外，两块是指……\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#5P#12500F哦，我正好\x01",
            "找到了两块同样大小\x01",
            "的石头。\x02\x03",

            "#12509F难得来沙滩玩，\x01",
            "留下做个纪念吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0484
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将两块\x01",
            "『纯白之石』分别送给了\x01",
            "琪雅和修利。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0485
    ChrTalk(
        0xF,
        "#12P#13612F哼、哼……谢啦。\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xE,
        "#12P#13209F嘿嘿嘿，我会珍惜的！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber('纯白之石', 2)
    Jump("loc_C50D")

    label("loc_C0AA")


    #C0487
    ChrTalk(
        0x101,
        (
            "#5P#12500F（对了，机会难得……\x01",
            "  把它当作礼物送出去如何？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0488
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K要把『纯白之石』赠送给谁？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "送给琪雅\x01",      # 0
            "送给修利\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C350")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0489
    ChrTalk(
        0x101,
        (
            "#5P#12500F那就把这块\x01",
            "『纯白之石』\x01",
            "送给琪雅吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0490
    ChrTalk(
        0xE,
        "#12P#13210F哎，真的可以吗！？\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x101,
        (
            "#5P#12500F嗯，当然。\x02\x03",

            "#12509F难得来沙滩玩，\x01",
            "留下做个纪念吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0492
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将大块的『纯白之石』\x01",
            "送给了琪雅。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0493
    ChrTalk(
        0xE,
        "#12P#13209F嘿嘿嘿，我会珍惜的！！\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    #C0494
    ChrTalk(
        0xF,
        "#12P#13606F#11P哼，真不错呢……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x101,
        (
            "#5P#12500F抱歉啦，修利，\x01",
            "你的年纪比琪雅大，\x01",
            "这次就让让她吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xF, 0x10E, 0x1F4)
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0496
    ChrTalk(
        0xF,
        (
            "#12P#13612F我、我才……\x01",
            "我才不想要那种石头呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber('纯白之石', 1)
    Jump("loc_C50D")

    label("loc_C350")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0497
    ChrTalk(
        0x101,
        (
            "#5P#12500F那就把这块\x01",
            "『纯白之石』\x01",
            "送给修利吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0498
    ChrTalk(
        0xF,
        "#12P#13605F哎……可、可以收下吗？\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        (
            "#5P#12500F嗯，当然。\x02\x03",

            "#12509F难得来沙滩玩，\x01",
            "留下做个纪念吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0500
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将大块的『纯白之石』\x01",
            "送给了修利。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0501
    ChrTalk(
        0xF,
        "#12P#13612F哼、哼……谢啦。\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    #C0502
    ChrTalk(
        0xE,
        (
            "#12P#13209F#6P太好了！修利！\x01",
            "一会让我也摸摸哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x101,
        (
            "#5P#12500F抱歉啦，琪雅。\x01",
            "作为补偿，下次买新的书\x01",
            "送给你。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    #C0504
    ChrTalk(
        0xE,
        (
            "#12P#13200F啊，嗯！\x01",
            "真期待！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SubItemNumber('纯白之石', 1)

    label("loc_C50D")

    Jump("loc_C78E")

    label("loc_C512")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C5FD")
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0505
    ChrTalk(
        0xE,
        (
            "#12P#13205F哦哦！\x01",
            "大家的尺寸几乎一样啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xF,
        (
            "#12P#13600F嗯……大小都\x01",
            "差不多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#5P#12500F那这次就算是\x01",
            "平手吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xF,
        "#12P#13606F啧，真是无聊的结果啊。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        "#5P#12512F哈哈，别这么说嘛。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C78E")

    label("loc_C5FD")

    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0510
    ChrTalk(
        0xE,
        (
            "#12P#13200F哇哇，罗伊德的石头\x01",
            "好小好可爱！！\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xF,
        "#12P#13600F嗯……真是很小呢。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0512
    ChrTalk(
        0x101,
        (
            "#5P#12512F哈、哈哈哈……\x01",
            "看来是我输了啊。\x02\x03",

            "#12500F琪雅和修利的\x01",
            "基本一样大，\x01",
            "这次就算你们两个赢啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xE,
        "#12P#13209F哇！赢了！！\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xF,
        (
            "#12P#13606F哼，何必硬装出\x01",
            "那种满不在乎的样子。\x02\x03",

            "#13602F呵呵，其实你心里\x01",
            "一定很不甘心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        (
            "#5P#12506F唔……\x01",
            "才、才没有那种事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C78E")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0516
    ChrTalk(
        0x101,
        (
            "#5P#12500F对了……琪雅，修利，\x01",
            "你们要不要喝点冷饮？\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xE,
        "#12P#13200F哎，罗伊德要去买吗？\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        (
            "#5P#12504F嗯，你们一直在水边玩，\x01",
            "也有点累了吧？\x02\x03",

            "#12500F要是有什么想吃想喝的，\x01",
            "不用客气，尽管和我说。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xF,
        "#12P#13600F哼，还挺大方嘛。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xE,
        "#12P#13204F嗯～我想想……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0521
    ChrTalk(
        0xE,
        (
            "#12P#13210F啊，那就要\x01",
            "冰激凌好了！\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#5P#12500F冰激凌吗……\x01",
            "哈哈，知道了。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xF,
        (
            "#12P#13604F那我也要一样的。\x02\x03",

            "#13600F嗯，不过我还想再玩一会，\x01",
            "不用马上就送来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        (
            "#5P#12500F嗯，好的，\x01",
            "那就一会见吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x15C, 7)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    OP_65(0x7, 0x1)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    ClearScenarioFlags(0x0, 4)
    ClearScenarioFlags(0x0, 5)
    ClearScenarioFlags(0x0, 6)
    ClearScenarioFlags(0x0, 7)
    ClearScenarioFlags(0x1, 0)
    ClearScenarioFlags(0x1, 1)
    ClearScenarioFlags(0x1, 2)
    ClearScenarioFlags(0x1, 3)
    ClearScenarioFlags(0x1, 4)
    SetChrPos(0x0, 43610, -7090, 2460, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CA36")
    Call(0, 54)

    label("loc_CA36")

    EventEnd(0x5)
    Return()

    # Function_53_BAC6 end

    def Function_54_CA39(): pass

    label("Function_54_CA39")

    FadeToBright(1000, 0)
    OP_68(22000, -4500, 0, 0)
    OP_68(22000, -5000, 0, 2500)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13250, 0)
    SetChrPos(0x101, 22000, -6000, 0, 90)
    OP_6F(0x79)
    OP_0D()

    #C0525
    ChrTalk(
        0x101,
        (
            "#12500F四处游玩了一番，\x01",
            "现在也没什么可做的了。\x02\x03",

            "#12503F……啊，我好像也\x01",
            "有点口渴了呢。\x02\x03",

            "#12500F之前说好要去给\x01",
            "大家买饮料，\x01",
            "不然就去小卖部吧。\x02\x03",

            "小卖部就在台阶上面，\x01",
            "现在就去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    SetScenarioFlags(0x15E, 3)
    Return()

    # Function_54_CA39 end

    def Function_55_CB56(): pass

    label("Function_55_CB56")

    EventBegin(0x0)
    Fade(500)
    OP_68(-8270, -500, 8450, 0)
    MoveCamera(315, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13750, 0)
    SetCameraDistance(13250, 2500)
    OP_4B(0x22, 0xFF)
    SetChrPos(0x101, -7270, -1500, 8450, 270)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDBE")

    #C0526
    ChrTalk(
        0x22,
        (
            "哦，欢迎光临，\x01",
            "包场的感觉很不错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        (
            "#12502F#12P哈哈，是啊，已经四处玩了一圈。\x02\x03",

            "那个……\x01",
            "我有不少东西想点……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x22,
        (
            "哦，我刚好已经\x01",
            "把商品准备好了，\x01",
            "想要什么尽管说。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        "#12500F#12P嗯，那就……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0530
    ChrTalk(
        0x101,
        (
            "#12506F#12P……啊。\x01",
            "刚发现，钱包还放在\x01",
            "置物柜里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x22,
        "哦，不用付钱。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x22,
        (
            "玛丽亚贝尔小姐吩咐过，\x01",
            "在你们包场期间，\x01",
            "一切饮食全部免费。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x101,
        (
            "#12505F#12P是、是吗！？\x02\x03",

            "#12512F真是万分周到啊……\x01",
            "以后在玛丽亚贝尔小姐面前\x01",
            "就更加抬不起头了。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x22,
        "哈哈，好好感谢她吧。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x22,
        "好了，要点什么？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_CDFB")

    label("loc_CDBE")


    #C0536
    ChrTalk(
        0x22,
        (
            "在你们包场期间，\x01",
            "一切饮食全部免费。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x22,
        "要立刻点单吗？\x02",
    )

    CloseMessageWindow()

    label("loc_CDFB")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0538
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "在这里点了冷饮之后，\x01",
            "湖水浴场的剧情\x01",
            "就会全部结束。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【点冷饮】\x01",      # 0
            "【放弃】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D106")

    #C0539
    ChrTalk(
        0x101,
        (
            "#12500F#12P嗯，麻烦您了。\x02\x03",

            "#12503F要四罐『铃铛可乐』，\x01",
            "三杯无酒精鸡尾酒……\x02\x03",

            "#12500F两个冰激凌，\x01",
            "两份刨冰……\x01",
            "哦，还有一根大香肠。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x22, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0540
    ChrTalk(
        0x22,
        (
            "你难道想一次\x01",
            "拿这么多吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x22,
        (
            "莫非你就是那种……\x01",
            "完全不顾自己死活的老好人类型？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#12512F#12P哪、哪里，哈哈……\x01",
            "我想应该还不算。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(136, 2000, 90)
    FadeToDark(2000, 0, -1)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0543
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──就这样，众人在湖水浴场度过了愉快的时光。\x02\x03",

            "并且大家一起玩了砸西瓜等\x01",
            "沙滩必玩游戏。\x02\x03",

            "随后，一边享用着酒店送来的\x01",
            "午餐盒饭一边聊天，\x01",
            "气氛无比愉快。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15E, 4)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_END)), "loc_D0C3")
    SubItemNumber('纯白之石', 1)

    label("loc_D0C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_END)), "loc_D0D1")
    SubItemNumber('纯白之石', 1)

    label("loc_D0D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_END)), "loc_D0DF")
    SubItemNumber('纯白之石', 1)

    label("loc_D0DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_END)), "loc_D0ED")
    SubItemNumber('纯白之石', 1)

    label("loc_D0ED")

    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("t1320", 0, 0, 0)
    IdleLoop()
    Jump("loc_D16D")

    label("loc_D106")


    #C0544
    ChrTalk(
        0x101,
        "#12500F#12P不，暂时还不用。\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x22,
        "哦，是吗？\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x22,
        (
            "没关系，只要在包场时间\x01",
            "结束之前点单就可以了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D16D")

    SetChrPos(0x0, -6770, -1500, 8450, 90)
    OP_4C(0x22, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_55_CB56 end

    def Function_56_D185(): pass

    label("Function_56_D185")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1B7")
    SetScenarioFlags(0x31, 2)

    label("loc_D1B7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D1FD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_D1F7")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D1EC")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_D1F2")

    label("loc_D1EC")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_D1F2")

    Jump("loc_D1FD")

    label("loc_D1F7")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_D1FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D4A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_D26E")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D24E"),
        (SWITCH_DEFAULT, "loc_D25F"),
    )


    label("loc_D24E")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_D269")

    label("loc_D25F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D269")

    Jump("loc_D49F")

    label("loc_D26E")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_D29E")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_D29E")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D2C8"),
        (1, "loc_D3CC"),
        (2, "loc_D45D"),
        (SWITCH_DEFAULT, "loc_D495"),
    )


    label("loc_D2C8")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D2F9")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_D309")

    label("loc_D2F9")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_D309")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D35F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D35F")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D382")
    Sound(461, 0, 100, 0)

    label("loc_D382")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3A2")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_D3B2")

    label("loc_D3A2")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_D3B2")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_D1FD")

    label("loc_D3CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_D43E")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_D401")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_D419")

    label("loc_D401")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_D414")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_D419")

    label("loc_D414")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_D419")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D458")

    label("loc_D43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_D44E")
    OP_AF(0xFB)
    Jump("loc_D458")

    label("loc_D44E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D458")

    Jump("loc_D49F")

    label("loc_D45D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D476")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D490")

    label("loc_D476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_D486")
    OP_AF(0xFB)
    Jump("loc_D490")

    label("loc_D486")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D490")

    Jump("loc_D49F")

    label("loc_D495")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D49F")

    Jump("loc_D1FD")

    label("loc_D4A4")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_56_D185 end

    def Function_57_D4B2(): pass

    label("Function_57_D4B2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_D4CE")
    Jump("loc_FAD3")

    label("loc_D4CE")

    LoadChrToIndex("chr/ch15100.itc", 0x1F)
    LoadChrToIndex("chr/ch15200.itc", 0x20)
    LoadChrToIndex("chr/ch15800.itc", 0x24)
    LoadChrToIndex("chr/ch16000.itc", 0x25)
    LoadChrToIndex("apl/ch51303.itc", 0x28)
    SoundLoad(3395)
    SoundLoad(2716)
    SoundLoad(3516)
    SoundLoad(2677)
    SoundLoad(3245)
    SoundLoad(3613)
    OP_90(0x101, 3000, 0, 2500, 90)
    OP_90(0x104, 2000, 0, 1500, 90)
    OP_90(0x105, 1500, 0, 3500, 90)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, 0, 0, 0, 0)
    SetChrFlags(0xE, 0x8)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 0, 0, 0, 0)
    SetChrFlags(0xA, 0x8)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrChipByIndex(0xB, 0x20)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 0, 0, 0, 0)
    SetChrFlags(0xB, 0x8)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 0, 0, 0, 0)
    SetChrFlags(0x12, 0x8)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrChipByIndex(0xC, 0x1)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrFlags(0xC, 0x8)
    OP_4B(0x10, 0xFF)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 0, 0, 0)
    SetChrFlags(0x10, 0x8)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 0, 0, 0, 0)
    SetChrFlags(0x8, 0x8)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 0, 0, 0, 0)
    SetChrFlags(0x9, 0x8)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xF, 0x5)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 0, 0, 0, 0)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0x12, 0x40)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xF, 0x40)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x0, 0x4)
    OP_68(50000, 0, -28000, 0)
    MoveCamera(305, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(41500, 0)
    FadeToBright(1000, 0)
    OP_68(50000, 0, 12000, 10000)
    Sleep(9000)
    Fade(1000)
    OP_68(39000, -4000, -1000, 0)
    MoveCamera(45, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    OP_68(39000, 3000, -1000, 9000)
    OP_6F(0x79)
    Fade(1000)
    OP_68(86000, 3800, 6000, 0)
    MoveCamera(90, 35, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(70000, 0)
    PlaceName2(340, 200, "c_plac45", 0x0, 3000)
    MoveCamera(90, 0, 0, 9000)
    SetCameraDistance(60000, 9000)
    OP_6F(0x79)
    Fade(1000)
    OP_68(50000, -1000, 0, 0)
    MoveCamera(321, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(20000, 0)
    OP_68(20000, -1000, 0, 10000)
    Sleep(1500)

    def lambda_D833():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D833)
    Sleep(0)

    def lambda_D84B():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D84B)
    Sleep(0)

    def lambda_D863():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D863)
    Sleep(0)
    Sleep(5500)
    #Sound(2757, 255, 100, 0)    #voice#Randy
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0547
    ChrTalk(
        0x104,
        "#12809F#5P#10A#4S哟！！\x02",
    )
    #Auto

    CloseMessageWindow()
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    Fade(1000)
    OP_68(17000, -5000, 2500, 0)
    MoveCamera(321, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(12500, 2500)
    Sleep(1500)
    Sound(2080, 255, 100, 0)    #voice#Lloyd
    Sleep(1500)

    #C0548
    ChrTalk(
        0x101,
        (
            "#12502F#5P这……好惊人啊。\x02\x03",

            "#12509F我还是第一次见到沙滩，\x01",
            "没想到竟然这么漂亮呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x105,
        (
            "#12904F#5P普通的沙滩都在沿海地带，\x01",
            "沙子应该也没有这么白。\x02\x03",

            "#12902F多半是从大陆中东部\x01",
            "的『纯白天堂』沙滩上\x01",
            "运来的沙子吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_DA0D():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DA0D)
    Sleep(50)

    def lambda_DA1D():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DA1D)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    #C0550
    ChrTalk(
        0x101,
        "#12511F#12P真的吗……\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x104,
        "#12806F#6P也太不可思议了吧……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0552
    ChrTalk(
        0x105,
        (
            "#12909F#5P呵呵，再次见识到了\x01",
            "ＩＢＣ的雄厚资产力呢。\x02\x03",

            "#12900F话说回来，在女士们到来之前，\x01",
            "我们还是先把准备工作做好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x104,
        (
            "#12800F#6P哦哦，说得也是。\x02\x03",

            "#12809F在沙滩上玩，\x01",
            "遮阳伞之类的东西肯定不能少啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#12504F#12P原来如此，说起来，\x01",
            "在杂志上好像也看到过那样的照片呢。\x02\x03",

            "#12500F好，我们分头摆放吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12600.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12700.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13100.itp")
    ClearMapObjFlags(0x1, 0x4)
    OP_68(18000, -5000, 20000, 0)
    MoveCamera(305, 16, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    SetChrPos(0x101, 21000, -6000, 20000, 270)
    SetChrPos(0x104, 20500, -6000, 21500, 225)
    SetChrPos(0x105, 20500, -6000, 18500, 315)
    FadeToBright(1000, 0)
    SetCameraDistance(18000, 3000)
    OP_6F(0x79)
    OP_0D()

    #C0555
    ChrTalk(
        0x101,
        "#12504F#12P呼，这样就行了吧。\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x104,
        "#12800F#11P嗯，还可以吧？\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x105,
        (
            "#12902F#6P很不错，很不错。\x02\x03",

            "#12909F好，那我赶快\x01",
            "休息一下吧。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 3, 0, 58)
    WaitChrThread(0x105, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0558
    ChrTalk(
        0x101,
        "#12506F#12P那个……\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x104,
        (
            "#12801F#11P好像比我还会\x01",
            "游玩享受啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0xE, 0x80)
    #Sound(3042, 255, 80, 0)    #voice#KeA

    #N0560
    NpcTalk(
        0xE,
        "琪雅的声音",
        "#10A罗伊德——！\x02",
    )
    #Auto

    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0xE1, 0x1F4)

    #C0561
    ChrTalk(
        0x101,
        "#12502F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x104,
        "#12802F#11P噢，来了啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(17000, -5000, -2500, 0)
    MoveCamera(238, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(15000, 6000)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0xC, 0x8)
    BeginChrThread(0xE, 3, 0, 60)
    BeginChrThread(0xA, 3, 0, 61)
    BeginChrThread(0xB, 3, 0, 62)
    BeginChrThread(0xC, 3, 0, 64)
    WaitChrThread(0xE, 3)
    Sound(3033, 255, 100, 0)    #voice#KeA
    Sleep(1300)
    OP_63(0xE, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0563
    ChrTalk(
        0xE,
        (
            "#13209F#11P好棒啊！\x01",
            "一片雪白！\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 3)
    WaitChrThread(0xA, 3)
    WaitChrThread(0xB, 3)
    OP_6F(0x79)

    #C0564
    ChrTalk(
        0xB,
        (
            "#12705F#11P的确……\x01",
            "真让人吃惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xA,
        (
            "#12602F#11P贝尔……\x01",
            "什么时候建起了这样的地方……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x1F4)
    Sleep(100)

    #C0566
    ChrTalk(
        0xC,
        (
            "#13109F#6P姐姐！\x01",
            "快来快来～！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(16000, -5000, -2500, 4000)

    def lambda_DFDD():

        label("loc_DFDD")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_DFDD")

    QueueWorkItem2(0xE, 2, lambda_DFDD)

    def lambda_DFEF():

        label("loc_DFEF")

        TurnDirection(0xFE, 0x12, 400)
        Yield()
        Jump("loc_DFEF")

    QueueWorkItem2(0xA, 2, lambda_DFEF)

    def lambda_E001():

        label("loc_E001")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_E001")

    QueueWorkItem2(0xB, 2, lambda_E001)

    def lambda_E013():

        label("loc_E013")

        TurnDirection(0xFE, 0x12, 600)
        Yield()
        Jump("loc_E013")

    QueueWorkItem2(0xC, 2, lambda_E013)
    BeginChrThread(0x12, 3, 0, 63)
    WaitChrThread(0x12, 3)
    TurnDirection(0x12, 0xC, 500)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0xC, 0x2)

    #C0567
    ChrTalk(
        0x12,
        (
            "#13012F#5P真是的，芙兰，\x01",
            "沙滩又不会逃走。\x02",
        )
    )

    OP_6F(0x79)
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18000, 3500)
    BeginChrThread(0xC, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0xE, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 69)
    Sleep(80)
    BeginChrThread(0x12, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 69)
    OP_6F(0x79)
    EndChrThread(0xE, 0x3)
    EndChrThread(0xA, 0x3)
    EndChrThread(0xB, 0x3)
    EndChrThread(0x12, 0x3)
    EndChrThread(0xC, 0x3)
    Fade(500)
    OP_68(18450, -5000, 18500, 0)
    MoveCamera(230, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0xE, 19430, -6000, 8270, 15)
    SetChrPos(0xA, 18930, -6000, 7270, 15)
    SetChrPos(0xB, 19930, -6000, 7270, 15)
    SetChrPos(0x12, 18430, -6000, 6270, 15)
    SetChrPos(0xC, 17930, -6000, 7270, 15)
    SetChrPos(0x101, 21000, -6000, 18500, 180)
    SetChrPos(0x104, 19750, -6000, 18250, 180)
    SetChrPos(0x105, 18450, -6000, 18500, 90)
    SetChrSubChip(0x105, 0x10)
    OP_68(21000, -5000, 16750, 6000)
    MoveCamera(230, 24, 0, 6000)
    SetCameraDistance(17500, 6000)
    OP_0D()
    BeginChrThread(0x105, 3, 0, 59)

    def lambda_E1AE():
        OP_9B(0x0, 0xE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_E1AE)
    Sleep(50)

    def lambda_E1C6():
        OP_9B(0x0, 0xC, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_E1C6)
    Sleep(50)

    def lambda_E1DE():
        OP_9B(0x0, 0xA, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_E1DE)
    Sleep(50)

    def lambda_E1F6():
        OP_9B(0x0, 0xB, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_E1F6)
    Sleep(50)

    def lambda_E20E():
        OP_9B(0x0, 0x12, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_E20E)
    Sleep(50)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xB, 0)
    WaitChrThread(0x12, 0)
    OP_93(0xE, 0x0, 0x0)
    OP_93(0xA, 0x0, 0x0)
    OP_93(0xB, 0x0, 0x0)
    OP_93(0x12, 0x0, 0x0)
    OP_93(0xC, 0x0, 0x0)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(21000, -5500, 15000, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 2000)
    SetChrPos(0x101, 21000, -6000, 19500, 180)
    SetChrPos(0x104, 19750, -6000, 19250, 180)
    SetChrPos(0x105, 18100, -6000, 18550, 90)
    SetChrSubChip(0x105, 0x4)
    Sleep(1500)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0568
    AnonymousTalk(
        0xE,
        "#3613V#30W嘿嘿嘿，久等了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE1D)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13000.itp")
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0569
    AnonymousTalk(
        0xA,
        (
            "#3395V#30W呵呵，还特意给我们\x01",
            "准备了遮阳伞吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xD43)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13300.itp")
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0570
    AnonymousTalk(
        0xB,
        "#2677V#30W真体贴呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13400.itp")
    OP_24(0xA75)
    OP_93(0xC, 0x87, 0x1F4)
    OP_98(0xC, 0x64, 0x0, 0xFFFFFA24, 0x7D0, 0x0)
    OP_93(0xC, 0x0, 0x1F4)

    def lambda_E557():
        OP_98(0xFE, 0xFFFFFF9C, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_E557)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_E586():
        OP_98(0xFE, 0xFFFFFF6A, 0x0, 0x1C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_E586)
    WaitChrThread(0xC, 1)
    WaitChrThread(0x12, 1)
    OP_64(0x12)
    Sleep(200)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0571
    AnonymousTalk(
        0xC,
        (
            "#2716V#40W好啦，姐姐。\x01",
            "#30W难得来这种地方玩，\x01",
            "快点上前展示一下！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA9C)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13500.itp")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0572
    AnonymousTalk(
        0x12,
        (
            "#3516V#30W等、等一下，\x01",
            "不要推我啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDBC)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13600.itp")
    OP_C9(0x1, 0x80000000)
    Fade(500)
    OP_68(20500, -4800, 16750, 0)
    MoveCamera(300, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 21000, -6000, 18500, 180)
    SetChrPos(0x104, 19750, -6000, 18250, 180)
    SetChrPos(0x105, 18450, -6000, 17900, 90)
    SetChrSubChip(0x105, 0xC)
    OP_6F(0x79)
    OP_0D()

    #C0573
    ChrTalk(
        0x101,
        "#12505F#11P#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(2757, 255, 70, 0)    #voice#Randy
    Sleep(600)

    #C0574
    ChrTalk(
        0x104,
        (
            "#12809F#11P噢噢！\x01",
            "不错啊！不错啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x105,
        "#12902F#11P嘿，大家穿上泳装都很漂亮呢。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xA,
        "#12609F#6P是、是吗……\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xB,
        "#12706F#6P其实我并没什么自信……\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xC,
        (
            "#13109F#5P嘿嘿嘿～罗伊德警官……\x02\x03",

            "你觉得谁的泳装\x01",
            "最漂亮呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0579
    ChrTalk(
        0x101,
        "#12511F#11P哎哎！？\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x12,
        (
            "#13001F#6P真是的，芙兰……！\x01",
            "不要难为罗伊德警官啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x105,
        (
            "#12902F#5P呵呵，你怎么了？\x01",
            "从刚才开始就两眼发直。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x5A, 0x1F4)

    #C0582
    ChrTalk(
        0x104,
        (
            "#12809F#5P哈哈哈，\x01",
            "这视觉刺激是不是强过头了～？\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x101,
        (
            "#12504F#11P哈哈……\x01",
            "嗯，实在很难移开视线呢。\x02\x03",

            "#12502F#11P大家穿上泳装\x01",
            "全都非常漂亮呢。\x02\x03",

            "#12509F如果拍下照片，\x01",
            "都可以直接当作艺术海报了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0584
    ChrTalk(
        0xE,
        "#13209F#6P嘿嘿嘿～谢谢！\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xA,
        "#12612F#6P罗、罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x12,
        "#13014F#6P哎、哎……！？\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xC,
        "#13106F#5P唔……不愧是罗伊德警官……\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xB,
        "#12711F#6P……果然没节操啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0589
    ChrTalk(
        0x101,
        "#12505F#11P哎……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0590
    ChrTalk(
        0x104,
        (
            "#12806F#5P（这小子……\x01",
            "  早晚会死在女人裙下的。）\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x105,
        "#12902F#5P（不过，那也是男人的愿望吧。）\x02",
    )

    CloseMessageWindow()

    #N0592
    NpcTalk(
        0x10,
        "女子的声音",
        "哟，让大家久等啦！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(17000, -5000, -2500, 0)
    MoveCamera(238, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(15000, 6000)
    ClearChrFlags(0x10, 0x8)
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0xF, 0x8)
    BeginChrThread(0x10, 3, 0, 65)
    BeginChrThread(0x8, 3, 0, 66)
    BeginChrThread(0x9, 3, 0, 67)
    BeginChrThread(0xF, 3, 0, 68)
    WaitChrThread(0x10, 3)
    OP_63(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xF, 3)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0593
    ChrTalk(
        0x10,
        "#13405F#11P哇，好棒啊！\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x8,
        (
            "#13309F#11P呵呵……\x01",
            "简直像天堂一样呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x9,
        "#13509F#11P一片雪白……！\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xF,
        "#13605F#11P……嘿………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 3000)
    BeginChrThread(0x10, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0x8, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 69)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 69)
    OP_6F(0x79)
    EndChrThread(0x10, 0x3)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xF, 0x3)
    Fade(500)
    OP_68(21000, -5000, 18500, 0)
    MoveCamera(230, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x10, 21500, -6000, 10500, 0)
    SetChrPos(0x8, 20500, -6000, 10000, 0)
    SetChrPos(0x9, 21000, -6000, 8500, 0)
    SetChrPos(0xF, 20000, -6000, 8000, 0)
    OP_93(0xE, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0x12, 0xB4, 0x0)
    OP_93(0xC, 0xB4, 0x0)
    SetChrPos(0x105, 18450, -6000, 18500, 90)
    SetChrSubChip(0x105, 0x14)
    OP_93(0x104, 0xB4, 0x0)
    OP_68(21000, -5000, 17000, 4000)
    MoveCamera(230, 24, 0, 4000)

    def lambda_EF50():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_EF50)

    def lambda_EF65():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EF65)

    def lambda_EF7A():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_EF7A)

    def lambda_EF8F():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_EF8F)

    def lambda_EFA4():

        label("loc_EFA4")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_EFA4")

    QueueWorkItem2(0xE, 2, lambda_EFA4)

    def lambda_EFB6():

        label("loc_EFB6")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_EFB6")

    QueueWorkItem2(0xA, 2, lambda_EFB6)

    def lambda_EFC8():

        label("loc_EFC8")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_EFC8")

    QueueWorkItem2(0xB, 2, lambda_EFC8)

    def lambda_EFDA():

        label("loc_EFDA")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_EFDA")

    QueueWorkItem2(0x12, 2, lambda_EFDA)

    def lambda_EFEC():

        label("loc_EFEC")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_EFEC")

    QueueWorkItem2(0xC, 2, lambda_EFEC)
    BeginChrThread(0xE, 3, 0, 70)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 70)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 70)
    Sleep(50)
    BeginChrThread(0x12, 3, 0, 72)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 71)
    WaitChrThread(0x10, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xF, 3)
    WaitChrThread(0x10, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xF, 1)
    EndChrThread(0xE, 0x2)
    EndChrThread(0xA, 0x2)
    EndChrThread(0xB, 0x2)
    EndChrThread(0x12, 0x2)
    EndChrThread(0xC, 0x2)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(21000, -5200, 15500, 0)
    MoveCamera(180, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 2000)
    SetChrPos(0x101, 21000, -6000, 19500, 180)
    SetChrPos(0x104, 19750, -6000, 19250, 180)
    SetChrPos(0x105, 18100, -6000, 18550, 90)
    SetChrSubChip(0x105, 0x4)
    OP_93(0xE, 0x13B, 0x0)
    OP_93(0xA, 0x13B, 0x0)
    OP_93(0xB, 0x13B, 0x0)
    OP_93(0x12, 0x2D, 0x0)
    OP_93(0xC, 0x2D, 0x0)
    Sleep(1500)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0597
    AnonymousTalk(
        0x8,
        "呵呵，久等了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0598
    AnonymousTalk(
        0x10,
        (
            "哦，已经被这么多\x01",
            "可爱的孩子包围了啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0599
    AnonymousTalk(
        0x9,
        (
            "#3245V#30W啊，还帮我们准备好\x01",
            "遮阳伞和躺椅了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xCAD)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    OP_C9(0x1, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0600
    AnonymousTalk(
        0xF,
        (
            "……和我说一声的话，\x01",
            "我也会摆的。\x02",
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
    Sound(822, 0, 100, 0)
    OP_63(0x10, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x8, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x9, 0x12C, 1600, 0x36, 0x39, 0xFA, 0x0)
    Sleep(1000)
    Sleep(500)

    #C0601
    ChrTalk(
        0x101,
        "#12505F#6P#N#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0602
    ChrTalk(
        0x104,
        "#12807F#12P#N#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0603
    ChrTalk(
        0xE,
        "#13205F#5P哎……\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xA,
        "#12606F#5P……这、这个……\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x12,
        (
            "#13012F#11P#N该说是太过美丽呢……\x01",
            "还是完全被盖过了呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0606
    ChrTalk(
        0xB,
        (
            "#12706F#5P总之，魅力完全不在一个级别……\x01",
            "……大概就是这种感觉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xC,
        "#13101F#11P好、好漂亮……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    #C0608
    ChrTalk(
        0x10,
        (
            "#13402F#6P啊，你们也都\x01",
            "很可爱啊。\x02\x03",

            "#13409F嗯嗯，大饱眼福呢⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0609
    ChrTalk(
        0x8,
        (
            "#13304F#12P呵呵，是啊。\x02\x03",

            "#13302F艾莉的身材果然如我所想，\x01",
            "丰盈又性感呢。\x02\x03",

            "#13309F琪雅和缇欧也很可爱，\x01",
            "让人好想抱一抱⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xA,
        (
            "#12609F#5P啊、啊哈哈……\x01",
            "（看到塞茜尔小姐的胸部，就算被夸奖也没有感觉呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xE,
        "#13209F#5P嘿嘿嘿，真的吗？\x02",
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0612
    ChrTalk(
        0x9,
        (
            "#13509F#11P呵呵……话说回来，\x01",
            "真是个美丽的沙滩呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xF,
        (
            "#13604F#11P嗯，确实还算不坏……\x02\x03",

            "#13601F喂，你们几个到底\x01",
            "要发呆到什么时候啊？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x10)
    OP_64(0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_F6FC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_F6FC)

    def lambda_F709():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F709)

    def lambda_F716():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_F716)

    def lambda_F723():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_F723)

    def lambda_F730():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_F730)

    def lambda_F73D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_F73D)

    def lambda_F74A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F74A)
    WaitChrThread(0xE, 2)
    Sleep(50)
    WaitChrThread(0xA, 2)
    Sleep(50)
    WaitChrThread(0xB, 2)
    Sleep(50)
    WaitChrThread(0x12, 2)
    Sleep(50)
    WaitChrThread(0xC, 2)
    Sleep(50)
    WaitChrThread(0x10, 2)
    Sleep(50)
    WaitChrThread(0x8, 2)
    Sleep(500)

    #C0614
    ChrTalk(
        0x101,
        "#12511F#6P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0615
    ChrTalk(
        0x104,
        (
            "#12806F#12P#N真危险真危险……\x01",
            "瞬间就飞到另一个世界了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0616
    ChrTalk(
        0xB,
        "#12711F#5P男人可真是简单呢。\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x105,
        (
            "#12909F#12P嗯，和女性相比，\x01",
            "可以算是单细胞生物吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xC,
        (
            "#13106F#11P唔唔……\x01",
            "可不能输给别人啊。\x02\x03",

            "#13101F姐姐，加油哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x12,
        "#13012F#5P#N不、不要乱说啦～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(18375, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0620
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "接下来，做了准备体操之后，\x01",
            "大家开始在沙滩上自由活动……\x02\x03",

            "罗伊德和莉夏一起\x01",
            "陪琪雅和修利\x01",
            "练习游泳。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RemoveParty(0x3, 0xFF)
    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x8000)
    OP_4C(0xE, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xC, 0x1)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 0, 0, 0, 0)
    ClearChrFlags(0xC, 0x8000)
    OP_4C(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 0, 0, 0)
    ClearChrFlags(0x8, 0x8000)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x10, 0x3)
    SetChrSubChip(0x10, 0x0)
    SetChrPos(0x10, 0, 0, 0, 0)
    ClearChrFlags(0x10, 0x8000)
    OP_4C(0x10, 0xFF)
    SetChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 0, 0)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrChipByIndex(0xF, 0x5)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x8000)
    OP_4C(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0xA, 0, 0, 0, 0)
    ClearChrFlags(0xA, 0x8000)
    OP_4C(0xA, 0xFF)
    SetChrFlags(0xA, 0x80)
    SetChrChipByIndex(0xB, 0x7)
    SetChrSubChip(0xB, 0x0)
    SetChrPos(0xB, 0, 0, 0, 0)
    ClearChrFlags(0xB, 0x8000)
    OP_4C(0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x12, 0x9)
    SetChrSubChip(0x12, 0x0)
    SetChrPos(0x12, 0, 0, 0, 0)
    ClearChrFlags(0x12, 0x8000)
    OP_4C(0x12, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0xB, 0x40)
    ClearChrFlags(0x12, 0x40)
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x8, 0x40)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xF, 0x40)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x28)
    OP_CC(0x1, 0xFF, 0x0)

    label("loc_FAD3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FDF1")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0x9, 18200, -5650, 23100, 90)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    SetChrPos(0x8, 18200, -5650, 20700, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    SetChrPos(0xA, 18200, -5650, 18200, 90)
    SetChrChipByIndex(0xA, 0x6)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FC22")
    SetChrPos(0x11, 24500, -6000, -20000, 0)
    SetChrChipByIndex(0x11, 0x17)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x20)
    BeginChrThread(0x11, 0, 0, 6)
    SetChrPos(0x12, 27500, -6000, -18000, 0)
    SetChrChipByIndex(0x12, 0x15)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x20)
    BeginChrThread(0x12, 0, 0, 7)
    SetChrPos(0x10, 24500, -6000, -12000, 180)
    SetChrChipByIndex(0x10, 0x18)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x20)
    BeginChrThread(0x10, 0, 0, 8)
    SetChrPos(0x13, 27500, -6000, -13000, 180)
    SetChrChipByIndex(0x13, 0x1C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x20)
    BeginChrThread(0x13, 0, 0, 9)
    SetChrPos(0x14, 26000, -3000, -16000, 0)
    BeginChrThread(0x14, 0, 0, 10)
    Jump("loc_FC81")

    label("loc_FC22")

    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrPos(0x14, 25950, -6000, -13400, 0)

    label("loc_FC81")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCE8")
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrChipByIndex(0xC, 0x16)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    Jump("loc_FD20")

    label("loc_FCE8")

    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)

    label("loc_FD20")

    SetChrFlags(0xD, 0x10)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_END)), "loc_FD71")
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_FDDB")

    label("loc_FD71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_END)), "loc_FDAD")
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    Jump("loc_FDDB")

    label("loc_FDAD")

    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_FDDB")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 55710, -2000, -36910, 45)

    label("loc_FDF1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FE50")
    ClearChrBattleFlags(0x9, 0x4)
    SetChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x7)
    SetChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x7)
    SetChrFlags(0xB, 0x2)
    SetChrPos(0xB, 31510, -6050, 7720, 180)
    SetChrFlags(0xC, 0x2)
    SetChrPos(0xC, 32049, -6100, 5840, 90)
    SetChrPos(0xD, 32870, -6180, 10310, 180)

    label("loc_FE50")

    ClearMapObjFlags(0xA, 0x4)
    OP_70(0xA, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_FEA6")
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)

    label("loc_FEA6")

    LoadChrToIndex("apl/ch51305.itc", 0x1E)
    LoadChrToIndex("apl/ch51307.itc", 0x1F)
    LoadChrToIndex("apl/ch51306.itc", 0x20)
    LoadChrToIndex("apl/ch51309.itc", 0x21)
    LoadChrToIndex("apl/ch51308.itc", 0x22)
    LoadChrToIndex("apl/ch51310.itc", 0x23)
    LoadChrToIndex("chr/ch16000.itc", 0x24)
    LoadEffect(0x0, "eff\\step04.eff")
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x20)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x4)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x20)
    SetChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    BeginChrThread(0xE, 0, 0, 73)
    SetChrFlags(0xE, 0x8000)
    ClearChrFlags(0xE, 0x1)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x20)
    SetChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 0, 0, 75)
    SetChrFlags(0xF, 0x8000)
    ClearChrFlags(0xF, 0x1)
    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0xF, 0x40)
    OP_90(0x101, 59000, 0, 27000, 0)
    OP_90(0x9, 57500, 0, 27000, 0)
    OP_90(0xE, 59000, -7250, 28000, 180)
    OP_90(0xF, 57500, -7250, 28000, 180)
    OP_68(58250, -5500, 27000, 0)
    OP_68(58250, -6500, 27000, 4000)
    MoveCamera(225, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    PlayBGM("ed7161", 0)
    Sound(988, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0621
    ChrTalk(
        0x101,
        (
            "#12502F#5P哦，不错啊，琪雅。\x02\x03",

            "#12509F就这样，就这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xE,
        (
            "#13209F#12P嘿嘿嘿，是吗？\x02\x03",

            "#13201F啊……\x01",
            "好像已经学会了。\x02\x03",

            "#13210F罗伊德，把手放开吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        (
            "#12511F#5P没、没问题吗？\x02\x03",

            "#12501F那我放手了——\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)

    def lambda_10101():

        label("loc_10101")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_10101")

    QueueWorkItem2(0x101, 2, lambda_10101)
    EndChrThread(0xE, 0x0)
    ClearChrFlags(0xE, 0x2)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    Sound(989, 2, 80, 0)
    OP_25(0x3DC, 0x3C)
    Sound(3034, 255, 100, 0)    #voice#KeA
    BeginChrThread(0xE, 0, 0, 74)
    BeginChrThread(0xE, 3, 0, 77)
    OP_0D()

    #C0624
    ChrTalk(
        0x9,
        "#13505F#11P啊。\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x101,
        (
            "#12505F#5P哦哦！\x02\x03",

            "#12502F琪雅，你以前应该\x01",
            "游过泳吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xE,
        "#13200F#12P#N嗯？不记得了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0627
    ChrTalk(
        0xF,
        (
            "#13605F#11P很、很厉害嘛，小鬼头……\x02\x03",

            "#13607F莉夏姐！\x01",
            "也教我一些要领吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x9,
        (
            "#13509F#5P呵呵，好的好的。\x02\x03",

            "#13502F嗯，上半身用力\x01",
            "稍微有些大了……\x02",
        )
    )

    CloseMessageWindow()
    StopSound(988, 2000, 50)
    StopSound(989, 2000, 70)
    FadeToDark(2000, 0, -1)
    OP_0D()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xE, 0x3)
    BeginChrThread(0xE, 3, 0, 78)
    ClearChrFlags(0x9, 0x20)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x0)

    def lambda_10286():

        label("loc_10286")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_10286")

    QueueWorkItem2(0x9, 2, lambda_10286)
    EndChrThread(0xF, 0x0)
    ClearChrFlags(0xF, 0x2)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    BeginChrThread(0xF, 0, 0, 76)
    BeginChrThread(0xF, 3, 0, 79)
    Sleep(1000)
    OP_68(58250, -6500, 29000, 0)
    MoveCamera(225, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    Sound(989, 2, 80, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0629
    ChrTalk(
        0x101,
        (
            "#12509F#5P哦，两个人学得\x01",
            "都很快啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xE,
        "#13204F#12P#N嘿嘿。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0631
    ChrTalk(
        0xF,
        (
            "#13612F#11P#N哼、哼……\x02\x03",

            "这种程度根本\x01",
            "不值一提……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0632
    ChrTalk(
        0xE,
        (
            "#13210F#12P#N修利修利！\x02\x03",

            "我们游到那边的岩石吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0633
    ChrTalk(
        0xF,
        "#13611F#11P#N我、我为什么要……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0634
    ChrTalk(
        0x101,
        (
            "#12509F#5P哈哈，小心点哦。\x02\x03",

            "#12500F你们两个，绝对不要\x01",
            "游到越过岩石的地方哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xE,
        "#13209F#12P#N知道啦！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0636
    ChrTalk(
        0xF,
        (
            "#13607F#11P#N啊啊，真是的！\x01",
            "我陪你游就是了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(225, 20, 0, 5000)
    SetCameraDistance(13000, 5000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10496")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104AD")
    Sleep(1)
    Jump("loc_10496")

    label("loc_104AD")

    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    Fade(1000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xE, 64510, -7460, 28680, 75)
    SetChrPos(0xF, 62580, -7430, 29030, 75)

    def lambda_104F3():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_104F3)

    def lambda_10508():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_10508)
    OP_68(62940, -4600, 28510, 0)
    OP_68(62940, -3600, 28510, 4000)
    MoveCamera(75, 5, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(11000, 0)
    Sleep(2500)
    StopSound(989, 2000, 70)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(500)
    OP_68(58250, -6500, 27000, 0)
    MoveCamera(225, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    EndChrThread(0xE, 0x0)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x0)
    EndChrThread(0xF, 0x1)
    ClearChrFlags(0xE, 0x20)
    ClearChrFlags(0xF, 0x20)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x9, 0x8)
    OP_0D()

    #C0637
    ChrTalk(
        0x101,
        "#12512F#11P唔，没问题吧？\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x9,
        (
            "#13509F#11P呵呵，\x01",
            "这一带的水很浅，\x01",
            "不会有事的。\x02\x03",

            "#13502F说起来……\x01",
            "小琪雅真是很厉害呢。\x02\x03",

            "转瞬之间就掌握了\x01",
            "游泳的要领。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0639
    ChrTalk(
        0x101,
        (
            "#12504F#6P不过，也说不定\x01",
            "是因为她曾经游过泳，\x01",
            "身体已经记住了游泳时的要领。\x02\x03",

            "#12500F说起来，修利也很厉害啊。\x02\x03",

            "她以前从没游过泳，\x01",
            "却能学得这么快。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x9,
        (
            "#13504F#11P通过最近的练习，\x01",
            "她的身体柔韧性和协调性\x01",
            "都得到了相当程度的锻炼。\x02\x03",

            "#13502F教会她基本要领之后，\x01",
            "很快就掌握了。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x101,
        (
            "#12504F#6P是吗……\x01",
            "看来她很努力呢。\x02\x03",

            "#12505F说起来……\x01",
            "彩虹剧团好像要\x01",
            "推出新版舞剧了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x9,
        (
            "#13505F#11P是的，虽说是新版，\x01",
            "但主体仍然是\x01",
            "《金之太阳、银之月》……\x02\x03",

            "#13502F只是进行了一些改编，\x01",
            "增加了由修利扮演的\x01",
            "第三位『舞姬』。\x02\x03",

            "#13509F不仅如此，还会有以她\x01",
            "为中心的新增情节呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_10984")

    #C0643
    ChrTalk(
        0x101,
        (
            "#12511F#6P那可真是很厉害呢……\x02\x03",

            "#12512F在初次见面的时候，\x01",
            "完全没想到她能这么快\x01",
            "就活跃在舞台上……\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x9,
        (
            "#13509F#11P呵呵，是啊。\x02\x03",

            "#13510F能取得如此成绩，\x01",
            "全靠伊莉娅小姐的指导，\x01",
            "还有修利自己的努力。\x02\x03",

            "#13508F……她远比我更加……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10A83")

    label("loc_10984")


    #C0645
    ChrTalk(
        0x101,
        (
            "#12505F#6P那可真是很厉害呢……\x02\x03",

            "#12501F说起来，听说修利最初\x01",
            "很讨厌伊莉娅小姐，\x01",
            "还发生过一些事件？\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x9,
        (
            "#13504F#11P那并不是什么大事，\x01",
            "还称不上是事件……\x02\x03",

            "#13510F能取得如此成绩，\x01",
            "全靠伊莉娅小姐的指导，\x01",
            "还有修利自己的努力。\x02\x03",

            "#13508F……她远比我更加……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_10A83")


    #C0647
    ChrTalk(
        0x101,
        "#12505F#6P哎……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0648
    ChrTalk(
        0x9,
        (
            "#13509F#11P啊哈哈，没什么……\x02\x03",

            "#13510F那个……我有点累了，\x01",
            "先到对面休息一下哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        (
            "#12504F#6P是吗，辛苦啦。\x02\x03",

            "#12500F时间还有的是，\x01",
            "玩得开心点吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x9,
        "#13509F#11P好的……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(57250, -5600, 29000, 6000)
    MoveCamera(235, 10, 0, 6000)
    SetCameraDistance(13500, 6000)
    OP_93(0x9, 0x10E, 0x1F4)

    def lambda_10B9B():
        OP_9B(0x0, 0xFE, 0x0, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_10B9B)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0651
    ChrTalk(
        0x101,
        (
            "#12503F#6P（嗯……话说回来，\x01",
            "  个子虽然不高，但身材真是相当……）\x02\x03",

            "#12511F（……别想这些了。）\x02\x03",

            "#12500F（距离正午还有不少时间，\x01",
            "  要不要去和大家一起玩玩呢？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x9, 0x1)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 0, 0, 0, 0)
    ClearChrFlags(0x9, 0x8000)
    OP_4C(0x9, 0xFF)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x4)
    SetChrChipByIndex(0xE, 0x0)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xE, 0, 0, 0, 0)
    ClearChrFlags(0xE, 0x8000)
    OP_4C(0xE, 0xFF)
    SetChrFlags(0xE, 0x80)
    SetChrChipByIndex(0xF, 0x5)
    SetChrSubChip(0xF, 0x0)
    SetChrPos(0xF, 0, 0, 0, 0)
    ClearChrFlags(0xF, 0x8000)
    OP_4C(0xF, 0xFF)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0x9, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0xF, 0x40)
    OP_49()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10DC9")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 18200, -5650, 23100, 90)
    SetChrChipByIndex(0x9, 0x2)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xB, 0x2)
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    ClearChrFlags(0xC, 0x2)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_10DC9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10DDE")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_10DDE")

    OP_90(0x0, 40000, 0, 17000, 270)
    SetScenarioFlags(0x145, 0)
    OP_29(0xA5, 0x1, 0x3)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_57_D4B2 end

    def Function_58_10E05(): pass

    label("Function_58_10E05")

    OP_68(17500, -5000, 20000, 2000)
    OP_9B(0x0, 0xFE, 0x0, 0x4B0, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x4B0, 0x7D0, 0x1)
    OP_93(0xFE, 0xB4, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x12C, 0x3E8, 0x0)
    OP_6F(0x79)
    Fade(500)
    Sound(318, 0, 40, 0)
    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, 18450, -6000, 17900, 90)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x2)
    SetChrChipByIndex(0xFE, 0x28)
    Sound(812, 0, 100, 0)
    OP_A1(0xFE, 0x3E8, 0x5, 0xC, 0xB, 0xA, 0x9, 0x8)
    Sound(811, 0, 20, 0)
    OP_0D()
    Return()

    # Function_58_10E05 end

    def Function_59_10E94(): pass

    label("Function_59_10E94")

    Sound(812, 0, 100, 0)
    OP_A1(0xFE, 0x546, 0x5, 0x10, 0x11, 0x12, 0x13, 0x14)
    Sound(318, 0, 40, 0)
    Return()

    # Function_59_10E94 end

    def Function_60_10EAC(): pass

    label("Function_60_10EAC")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_60_10EAC end

    def Function_61_10ED7(): pass

    label("Function_61_10ED7")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_61_10ED7 end

    def Function_62_10F02(): pass

    label("Function_62_10F02")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6000, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_62_10F02 end

    def Function_63_10F2D(): pass

    label("Function_63_10F2D")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_63_10F2D end

    def Function_64_10F58(): pass

    label("Function_64_10F58")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4500, 0, -1500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_64_10F58 end

    def Function_65_10F83(): pass

    label("Function_65_10F83")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_65_10F83 end

    def Function_66_10FAE(): pass

    label("Function_66_10FAE")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_66_10FAE end

    def Function_67_10FD9(): pass

    label("Function_67_10FD9")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 5500, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_67_10FD9 end

    def Function_68_11004(): pass

    label("Function_68_11004")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_68_11004 end

    def Function_69_1102F(): pass

    label("Function_69_1102F")

    OP_93(0xFE, 0xF, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_69_1102F end

    def Function_70_11046(): pass

    label("Function_70_11046")

    OP_98(0xFE, 0x4B0, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_70_11046 end

    def Function_71_1105B(): pass

    label("Function_71_1105B")

    OP_98(0xFE, 0xFFFFFB50, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_71_1105B end

    def Function_72_11070(): pass

    label("Function_72_11070")

    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_72_11070 end

    def Function_73_11085(): pass

    label("Function_73_11085")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11164")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    Jump("Function_73_11085")

    label("loc_11164")

    Return()

    # Function_73_11085 end

    def Function_74_11165(): pass

    label("Function_74_11165")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11247")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    Sleep(200)
    Jump("Function_74_11165")

    label("loc_11247")

    Return()

    # Function_74_11165 end

    def Function_75_11248(): pass

    label("Function_75_11248")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11327")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    Jump("Function_75_11248")

    label("loc_11327")

    Return()

    # Function_75_11248 end

    def Function_76_11328(): pass

    label("Function_76_11328")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1140A")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, 300, -200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x4)
    Sleep(150)
    SetChrSubChip(0xFE, 0x0)
    Sleep(150)
    Sleep(200)
    Jump("Function_76_11328")

    label("loc_1140A")

    Return()

    # Function_76_11328 end

    def Function_77_1140B(): pass

    label("Function_77_1140B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1146E")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60080, -6950, 27560)
    OP_9F(0x1, 61500, -6850, 28810)
    OP_9F(0x1, 60190, -7050, 30310)
    OP_9F(0x1, 58950, -7150, 29090)
    OP_9F(0x1, 59200, -7250, 28000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("Function_77_1140B")

    label("loc_1146E")

    Return()

    # Function_77_1140B end

    def Function_78_1146F(): pass

    label("Function_78_1146F")

    SetChrPos(0xFE, 58250, -6850, 29000, 0)

    label("loc_11480")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_114D9")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60250, -6750, 31000)
    OP_9F(0x1, 58250, -7200, 33000)
    OP_9F(0x1, 56250, -7250, 31000)
    OP_9F(0x1, 58250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("loc_11480")

    label("loc_114D9")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Return()

    # Function_78_1146F end

    def Function_79_114FF(): pass

    label("Function_79_114FF")

    SetChrPos(0xFE, 58250, -6950, 30000, 0)

    label("loc_11510")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_11569")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 59250, -6950, 31000)
    OP_9F(0x1, 58250, -7250, 32000)
    OP_9F(0x1, 57250, -7250, 31000)
    OP_9F(0x1, 58250, -6950, 30000)
    OP_9F(0x2, 0xFE, 1000, 0x6)
    Jump("loc_11510")

    label("loc_11569")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6950, 30000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_79_114FF end

    def Function_80_1158F(): pass

    label("Function_80_1158F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(18000, -4400, 0, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 18000, -6000, 0, 90)
    SetChrName("")

    #A0652
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──就这样，众人在湖水浴场\x01",
            "度过了愉快的时光。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0653
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "并且大家一起玩了砸西瓜等\x01",
            "沙滩必玩游戏。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrName("")

    #A0654
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随后，一边享用着酒店送来的\x01",
            "午餐盒饭一边聊天，\x01",
            "气氛无比愉快。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    StopSound(136, 1000, 100)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 0)
    NewScene("t1320", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_80_1158F end

    def Function_81_116B8(): pass

    label("Function_81_116B8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02710.itc", 0x1E)
    LoadChrToIndex("chr/ch02751.itc", 0x1F)
    LoadChrToIndex("chr/ch41950.itc", 0x20)
    LoadChrToIndex("chr/ch41951.itc", 0x21)
    LoadChrToIndex("chr/ch42050.itc", 0x22)
    LoadChrToIndex("chr/ch42051.itc", 0x23)
    LoadChrToIndex("monster/ch82050.itc", 0x24)
    LoadChrToIndex("monster/ch82051.itc", 0x25)
    LoadChrToIndex("chr/ch41952.itc", 0x26)
    LoadChrToIndex("chr/ch00050.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("chr/ch02950.itc", 0x2A)
    LoadChrToIndex("chr/ch03150.itc", 0x2B)
    LoadChrToIndex("chr/ch03250.itc", 0x2C)
    LoadEffect(0x0, "battle/btgun00.eff")
    SoundLoad(497)
    SoundLoad(950)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrChipByIndex(0xD, 0x1E)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xD, 0x4)
    OP_90(0x101, 39900, -6010, 30100, 270)
    OP_90(0x103, 41000, -6000, 30950, 270)
    OP_90(0x104, 40730, -6000, 29440, 270)
    OP_90(0x106, 41890, -6070, 28860, 270)
    OP_90(0x109, 42050, -6090, 29980, 270)
    OP_90(0x105, 42230, -6120, 31120, 270)
    OP_90(0xD, 40800, -3000, 32000, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrChipByIndex(0x17, 0x20)
    SetChrChipByIndex(0x18, 0x20)
    SetChrChipByIndex(0x19, 0x22)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    SetChrChipByIndex(0x1D, 0x24)
    SetChrChipByIndex(0x1E, 0x24)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x1D, 0x8)
    SetChrFlags(0x1E, 0x8)
    SetChrFlags(0x1F, 0x8)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    ClearChrFlags(0x17, 0x4)
    ClearChrFlags(0x18, 0x4)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x1D, 0x4)
    ClearChrFlags(0x1E, 0x4)
    ClearChrFlags(0x1F, 0x4)
    OP_90(0x17, 9500, 1000, 2700, 90)
    OP_90(0x18, 6600, 1000, -3650, 90)
    OP_90(0x19, 3100, 1000, 3350, 90)
    OP_90(0x1D, 8550, 1000, -1650, 90)
    OP_90(0x1E, 6700, 1000, 1600, 90)
    OP_90(0x1F, 2900, 1000, -1850, 90)
    ClearChrFlags(0x15, 0x80)
    OP_78(0x2, 0x15)
    OP_49()
    SetChrPos(0x15, 45000, 20000, 30000, 270)
    OP_D5(0x15, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x2, 0x4)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x1, 0x78, 0x0, 0x20)
    OP_75(0x2, 0x1, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x3, 0x16)
    OP_49()
    SetChrPos(0x16, 45000, 20000, 30000, 270)
    OP_D5(0x16, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x65, 0xA0, 0x0, 0x20)
    SetMapObjFlags(0x0, 0x4)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0x106, 0x8)
    SetChrFlags(0xD, 0x8)
    OP_68(45000, 2500, 30000, 0)
    MoveCamera(315, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    Sound(497, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_68(45000, -500, 30000, 7000)
    MoveCamera(305, 40, 0, 7000)
    BeginChrThread(0x15, 3, 0, 82)
    BeginChrThread(0x16, 3, 0, 83)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x15, 0x3)
    EndChrThread(0x15, 0x0)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x16, 0x1)
    Sleep(1000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    ClearChrFlags(0x106, 0x8)
    ClearChrFlags(0xD, 0x8)
    OP_68(35000, -4500, 30000, 0)
    MoveCamera(60, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_68(31000, -4500, 30000, 5000)
    MoveCamera(45, 10, 0, 5000)
    BeginChrThread(0x15, 3, 0, 84)
    BeginChrThread(0x16, 3, 0, 85)

    def lambda_11AED():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11AED)
    Sleep(30)

    def lambda_11B05():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11B05)
    Sleep(30)

    def lambda_11B1D():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11B1D)
    Sleep(30)

    def lambda_11B35():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11B35)
    Sleep(30)

    def lambda_11B4D():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_11B4D)
    Sleep(30)

    def lambda_11B65():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_11B65)
    Sleep(30)

    def lambda_11B7D():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_11B7D)
    StopSound(497, 4000, 90)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0x15, 3)
    WaitChrThread(0x16, 3)
    SetMapObjFlags(0x2, 0x4)
    SetChrFlags(0x15, 0x80)
    SetMapObjFlags(0x3, 0x4)
    SetChrFlags(0x16, 0x80)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(31000, -5000, 30000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15750, 0)
    OP_0D()
    OP_68(31000, -5000, 31500, 1200)
    OP_93(0xD, 0xB4, 0x1C2)
    OP_6F(0x79)

    #N0655
    NpcTalk(
        0xD,
        "神狼蔡特",
        (
            "#01203F#3C#5P那么，我先去主题公园区域\x01",
            "尽力扰乱敌人。\x02\x03",

            "#01200F我恢复原形后会给你们发信号，\x01",
            "你们就趁机向迎宾馆前进。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11CA4():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11CA4)
    Sleep(50)

    def lambda_11CB4():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11CB4)
    Sleep(50)

    def lambda_11CC4():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11CC4)
    Sleep(50)

    def lambda_11CD4():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11CD4)
    Sleep(50)

    def lambda_11CE4():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11CE4)
    Sleep(50)

    def lambda_11CF4():
        TurnDirection(0x106, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_11CF4)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)

    #C0656
    ChrTalk(
        0x101,
        "#00013F#6P明白了。\x02",
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x103,
        (
            "#00208F#12P蔡特……\x01",
            "要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0658
    NpcTalk(
        0xD,
        "神狼蔡特",
        (
            "#01200F#3C#5P呵呵，你们也一样。\x02\x03",

            "#01203F愿女神保佑各位。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(31000, -4200, 32000, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11500, 0)
    OP_68(31000, 2100, 42000, 3000)
    MoveCamera(40, 5, 0, 3000)

    def lambda_11DEE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11DEE)

    def lambda_11DFB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_11DFB)

    def lambda_11E08():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11E08)

    def lambda_11E15():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11E15)

    def lambda_11E22():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11E22)

    def lambda_11E2F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_11E2F)
    BeginChrThread(0xD, 3, 0, 89)
    WaitChrThread(0xD, 3)
    SetChrFlags(0xD, 0x80)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    WaitChrThread(0x106, 2)
    OP_0D()
    Fade(1000)
    OP_68(31000, -4800, 30000, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_6F(0x79)
    OP_0D()

    #C0659
    ChrTalk(
        0x105,
        "#10409F#11P哈哈，真是可靠呢。\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x104,
        (
            "#00307F#12P好，我们首先向\x01",
            "酒店所在的商店街……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1D, 0x8)
    ClearChrFlags(0x1E, 0x8)
    ClearChrFlags(0x1F, 0x8)
    StopBGM(0xBB8)

    #N0661
    NpcTalk(
        0x17,
        "男人的声音",
        "#2S#2P在这里……！\x02",
    )

    CloseMessageWindow()

    #N0662
    NpcTalk(
        0x18,
        "男人的声音",
        "#2S#2P是班宁斯等人！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_11FF8():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_11FF8)
    Sleep(50)

    def lambda_12008():
        OP_93(0x103, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12008)
    Sleep(50)

    def lambda_12018():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12018)
    Sleep(50)

    def lambda_12028():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_12028)
    Sleep(50)

    def lambda_12038():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_12038)
    Sleep(50)

    def lambda_12048():
        OP_93(0x106, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_12048)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7540", 0)
    ReplaceBGM("ed7251", "ed7540")
    ReplaceBGM("ed7565", "ed7540")
    Fade(1000)
    OP_68(18000, -2500, 5000, 0)
    OP_68(18000, -5000, 5000, 6000)
    MoveCamera(240, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16000, 0)
    BeginChrThread(0x17, 3, 0, 90)
    BeginChrThread(0x18, 3, 0, 91)
    BeginChrThread(0x19, 3, 0, 92)
    BeginChrThread(0x1D, 3, 0, 95)
    BeginChrThread(0x1E, 3, 0, 96)
    BeginChrThread(0x1F, 3, 0, 97)
    BeginChrThread(0x2A, 1, 0, 98)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x19, 3)
    WaitChrThread(0x1D, 3)
    WaitChrThread(0x1E, 3)
    WaitChrThread(0x1F, 3)
    EndChrThread(0x2A, 0x1)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(31000, -5200, 30000, 0)
    MoveCamera(340, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(11500, 0)
    OP_0D()

    #C0663
    ChrTalk(
        0x104,
        (
            "#00310F#11P啧……\x01",
            "这么快就来了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x109,
        "#10107F#11P敌人为三名猎兵，三只军用魔兽！\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x106,
        (
            "#10701F#12P看样子，似乎是\x01",
            "相当强悍的精锐部队……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0666
    ChrTalk(
        0x101,
        (
            "#00007F#11P准备迎击！\x01",
            "联手打倒敌人！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetCameraDistance(11000, 0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0x27)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2A)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x2B)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x2C)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0667
    ChrTalk(
        0x104,
        "#00307F#1K#1P#N噢噢！\x02",
    )


    #C0668
    ChrTalk(
        0x105,
        "#10407F#1K#2P#N嗯！\x02",
    )


    #C0669
    ChrTalk(
        0x109,
        "#10107F#1K#4P#N是！\x02",
    )


    #N0670
    NpcTalk(
        0x101,
        "莉夏",
        "#10707F#1K#3P#N是！\x02",
    )

    SetMessageWindowPos(180, 70, -1, -1)

    #A0671
    AnonymousTalk(
        0x103,
        "#00201F#1K#N是！\x02",
    )

    #Sound(2249, 255, 100, 0)    #voice#Tio
    #Sound(2343, 255, 100, 1)    #voice#Randy
    #Sound(2417, 255, 100, 2)    #voice#Lazy
    #Sound(2478, 255, 100, 3)    #voice#Noel
    #Sound(3174, 255, 100, 4)    #voice#Rixia
    OP_57(0x1)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(29800, -5000, 27200, 0)
    MoveCamera(210, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    SetCameraDistance(10000, 1000)

    def lambda_12359():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_12359)

    def lambda_1236E():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1236E)

    def lambda_12383():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_12383)

    def lambda_12398():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_12398)

    def lambda_123AD():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_123AD)

    def lambda_123C2():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_123C2)
    BeginChrThread(0x2A, 1, 0, 98)
    Sleep(500)
    BlurSwitch(0x15E, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    OP_0D()
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x19, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x1F, 0x0)
    SetChrFlags(0x17, 0x4)
    SetChrFlags(0x18, 0x4)
    SetChrFlags(0x19, 0x4)
    SetChrFlags(0x1D, 0x4)
    SetChrFlags(0x1E, 0x4)
    SetChrFlags(0x1F, 0x4)
    EndChrThread(0x2A, 0x1)
    OP_24(0x1F1)
    OP_24(0x3B6)
    Battle("BattleInfo_904", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 99)
    Return()

    # Function_81_116B8 end

    def Function_82_12455(): pass

    label("Function_82_12455")

    BeginChrThread(0xFE, 0, 0, 86)
    OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_82_12455 end

    def Function_83_12474(): pass

    label("Function_83_12474")


    def lambda_12479():
        OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12479)
    Sleep(2000)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x32, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    Sleep(1000)
    OP_75(0x2, 0x2, 0x0)
    OP_79(0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_83_12474 end

    def Function_84_124D4(): pass

    label("Function_84_124D4")

    BeginChrThread(0xFE, 0, 0, 87)
    OP_75(0x2, 0x2, 0x0)
    SetChrPos(0xFE, 45000, -1000, 30000, 270)
    OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_84_124D4 end

    def Function_85_1250B(): pass

    label("Function_85_1250B")

    SetChrPos(0xFE, 45000, -1000, 30000, 270)

    def lambda_12521():
        OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_12521)
    Sleep(500)
    Sound(202, 0, 100, 0)
    Sound(203, 0, 50, 0)
    Sound(950, 2, 50, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x33, 0x64, 0x0, 0x8)
    Sleep(500)
    Sound(920, 0, 100, 0)
    StopSound(950, 1000, 40)
    OP_75(0x2, 0x1, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x65, 0xA0, 0x0, 0x20)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_1250B end

    def Function_86_12585(): pass

    label("Function_86_12585")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_125A9")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_86_12585")

    label("loc_125A9")

    Return()

    # Function_86_12585 end

    def Function_87_125AA(): pass

    label("Function_87_125AA")

    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x28, 0x28, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x1E, 0x1E, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0x14, 0x14, 0xBB8, 0x3E8)
    Sleep(1000)
    OP_82(0xA, 0xA, 0xBB8, 0x3E8)
    Sleep(1000)
    Return()

    # Function_87_125AA end

    def Function_88_1260F(): pass

    label("Function_88_1260F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1262A")
    OP_A1(0xFE, 0xBB8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_88_1260F")

    label("loc_1262A")

    Return()

    # Function_88_1260F end

    def Function_89_1262B(): pass

    label("Function_89_1262B")

    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x4)
    SetChrChip(0x0, 0xFE, 0x1E, 0x12C)
    BeginChrThread(0x2A, 1, 0, 98)
    BeginChrThread(0xFE, 0, 0, 88)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1B58, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x2A, 0x1)
    ClearChrFlags(0xFE, 0x1)
    Sound(844, 0, 70, 0)
    OP_9D(0xFE, 0x7918, 0xFFFFF8F8, 0xA410, 0x1388, 0x1B58)
    SetChrFlags(0xFE, 0x1)
    BeginChrThread(0x2A, 1, 0, 98)
    BeginChrThread(0xFE, 0, 0, 88)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x1388, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x2A, 0x1)
    ClearChrFlags(0xFE, 0x1)
    Sound(844, 0, 70, 0)
    OP_9D(0xFE, 0x7918, 0x8FC, 0xD2F0, 0x157C, 0x1770)
    SetChrFlags(0xFE, 0x1)
    BeginChrThread(0x2A, 1, 0, 98)
    BeginChrThread(0xFE, 0, 0, 88)
    OP_9B(0x0, 0xFE, 0xFFF6, 0x32C8, 0x1B58, 0x0)
    EndChrThread(0xFE, 0x0)
    EndChrThread(0x2A, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_89_1262B end

    def Function_90_1271C(): pass

    label("Function_90_1271C")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x1B58, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sleep(300)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x2, 0x1, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1388, 0x0)
    Return()

    # Function_90_1271C end

    def Function_91_1283B(): pass

    label("Function_91_1283B")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5DC0, 0x1388, 0x0)
    Return()

    # Function_91_1283B end

    def Function_92_12862(): pass

    label("Function_92_12862")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x4844, 0x1388, 0x0)
    Return()

    # Function_92_12862 end

    def Function_93_12889(): pass

    label("Function_93_12889")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_128A7")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_93_12889")

    label("loc_128A7")

    Return()

    # Function_93_12889 end

    def Function_94_128A8(): pass

    label("Function_94_128A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_128C6")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_94_128A8")

    label("loc_128C6")

    Return()

    # Function_94_128A8 end

    def Function_95_128C7(): pass

    label("Function_95_128C7")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x57E4, 0x1388, 0x0)
    Return()

    # Function_95_128C7 end

    def Function_96_128FF(): pass

    label("Function_96_128FF")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5208, 0x1388, 0x0)
    Return()

    # Function_96_128FF end

    def Function_97_12937(): pass

    label("Function_97_12937")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x55F0, 0x1388, 0x0)
    Return()

    # Function_97_12937 end

    def Function_98_1296F(): pass

    label("Function_98_1296F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_12988")
    Sound(845, 0, 60, 0)
    Sleep(400)
    Jump("Function_98_1296F")

    label("loc_12988")

    Return()

    # Function_98_1296F end

    def Function_99_12989(): pass

    label("Function_99_12989")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_90(0x101, 29900, 0, 30100, 225)
    OP_90(0x103, 31000, 0, 30950, 225)
    OP_90(0x104, 30730, 0, 29440, 225)
    OP_90(0x106, 31890, 0, 28860, 225)
    OP_90(0x109, 32049, 0, 29980, 225)
    OP_90(0x105, 32229, 0, 31120, 225)
    Call(0, 100)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    OP_52(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    OP_68(28170, -5200, 26570, 0)
    MoveCamera(270, 24, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    FadeToBright(1000, 0)
    OP_68(29230, -5200, 27630, 2000)
    OP_6F(0x79)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sleep(300)

    #C0672
    ChrTalk(
        0x101,
        (
            "#00010F#11P呜……\x01",
            "果然很强……！\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x104,
        (
            "#00307F#12P在这里的都是些最强级别的家伙！\x01",
            "我们必须拿出全力……！\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x103,
        (
            "#00207F#11P赶快出发吧……！\x01",
            "蔡特快要开始行动了。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#00007F#11P嗯，最初目标是商店街！\x02\x03",

            "从业人员们应该已经\x01",
            "全部撤离了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x109,
        (
            "#10101F#12P是的，不用担心\x01",
            "有人被卷入战斗！\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x105,
        (
            "#10402F#12P既然如此，\x01",
            "我们就可以放手一搏了……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, 31290, -6030, 30470, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 4)
    OP_29(0xAF, 0x1, 0x12)
    OP_1B(0x0, 0x0, 0x65)
    SetMapObjFlags(0x0, 0x4)
    OP_65(0x0, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_99_12989 end

    def Function_100_12CB6(): pass

    label("Function_100_12CB6")

    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    OP_52(0x17, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x17, 0x40)
    ClearChrFlags(0x17, 0x1)
    SetChrPos(0x17, 29420, -6000, 23550, 270)
    SetChrChipByIndex(0x18, 0xB)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    OP_52(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x18, 0x40)
    ClearChrFlags(0x18, 0x1)
    SetChrPos(0x18, 26080, -6000, 26400, 315)
    SetChrChipByIndex(0x19, 0xB)
    SetChrSubChip(0x19, 0x1)
    ClearChrFlags(0x19, 0x80)
    OP_52(0x19, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x40)
    ClearChrFlags(0x19, 0x1)
    SetChrPos(0x19, 28590, -6000, 26930, 180)
    Return()

    # Function_100_12CB6 end

    def Function_101_12D50(): pass

    label("Function_101_12D50")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    LoadChrToIndex("chr/ch41950.itc", 0x24)
    LoadChrToIndex("chr/ch41951.itc", 0x25)
    LoadChrToIndex("chr/ch41952.itc", 0x26)
    LoadChrToIndex("chr/ch42050.itc", 0x27)
    LoadChrToIndex("chr/ch42051.itc", 0x28)
    LoadChrToIndex("monster/ch82050.itc", 0x29)
    LoadChrToIndex("monster/ch82051.itc", 0x2A)
    LoadEffect(0x0, "battle/btgun00.eff")
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13000, -2000, -500, 270)
    SetChrPos(0x104, -13000, -2000, 500, 270)
    SetChrPos(0x103, -11500, -2000, -500, 270)
    SetChrPos(0x105, -11500, -2000, 500, 270)
    SetChrPos(0x109, -12000, -2000, -1300, 270)
    SetChrPos(0x106, -12350, -2000, 1300, 270)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrChipByIndex(0x1A, 0x25)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrChipByIndex(0x1C, 0x25)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrChipByIndex(0x1D, 0x2A)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x8000)
    SetChrFlags(0x1D, 0x20)
    SetChrFlags(0x1E, 0x20)
    SetChrFlags(0x1F, 0x20)
    SetChrFlags(0x20, 0x20)
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x1D, 0, 0, 94)
    BeginChrThread(0x1E, 0, 0, 94)
    BeginChrThread(0x1F, 0, 0, 94)
    BeginChrThread(0x20, 0, 0, 94)
    SetChrPos(0x1A, -33000, -2000, 1300, 90)
    SetChrPos(0x1B, -38000, -2000, 0, 90)
    SetChrPos(0x1C, -28000, -2000, -1300, 90)
    SetChrPos(0x1D, -49500, -2000, 3000, 90)
    SetChrPos(0x1E, -47000, -2000, 1000, 90)
    SetChrPos(0x1F, -48500, -2000, -1000, 90)
    SetChrPos(0x20, -47000, -2000, -3000, 90)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0x1C, 0x8)
    SetChrFlags(0x1D, 0x8)
    SetChrFlags(0x1E, 0x8)
    SetChrFlags(0x1F, 0x8)
    SetChrFlags(0x20, 0x8)
    SetChrFlags(0x1A, 0x40)
    SetChrFlags(0x1B, 0x40)
    SetChrFlags(0x1C, 0x40)
    SetChrFlags(0x1D, 0x40)
    SetChrFlags(0x1E, 0x40)
    SetChrFlags(0x1F, 0x40)
    SetChrFlags(0x20, 0x40)
    OP_68(-13000, -1000, 0, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(12000, 1500)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(-25000, -1000, 0, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15000, 0)
    SetCameraDistance(12000, 6000)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x8)
    ClearChrFlags(0x1C, 0x8)
    ClearChrFlags(0x1D, 0x8)
    ClearChrFlags(0x1E, 0x8)
    ClearChrFlags(0x1F, 0x8)
    ClearChrFlags(0x20, 0x8)
    BeginChrThread(0x1A, 3, 0, 103)
    BeginChrThread(0x1B, 3, 0, 104)
    BeginChrThread(0x1C, 3, 0, 102)
    BeginChrThread(0x1D, 3, 0, 105)
    BeginChrThread(0x1E, 3, 0, 105)
    BeginChrThread(0x1F, 3, 0, 105)
    BeginChrThread(0x20, 3, 0, 105)
    BeginChrThread(0x2A, 1, 0, 98)
    WaitChrThread(0x1A, 3)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x1D, 3)
    WaitChrThread(0x1E, 3)
    WaitChrThread(0x1F, 3)
    WaitChrThread(0x20, 3)
    EndChrThread(0x2A, 0x1)
    OP_6F(0x79)
    OP_0D()
    Fade(500)
    OP_68(-18000, -1000, 0, 0)
    OP_68(-14000, -1000, 0, 1500)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(11000, 1500)
    SetChrPos(0x1A, -24500, -2000, 1200, 90)
    SetChrPos(0x1B, -22500, -2000, 0, 90)
    SetChrPos(0x1C, -24000, -2000, -1100, 90)
    SetChrPos(0x1D, -29500, -2000, 3000, 90)
    SetChrPos(0x1E, -27000, -2000, 1300, 90)
    SetChrPos(0x1F, -28500, -2000, -1000, 90)
    SetChrPos(0x20, -27000, -2000, -3100, 90)

    def lambda_1323A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1323A)

    def lambda_1324F():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1324F)

    def lambda_13264():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_13264)

    def lambda_13279():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_13279)

    def lambda_1328E():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1328E)

    def lambda_132A3():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_132A3)

    def lambda_132B8():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_132B8)
    BeginChrThread(0x2A, 1, 0, 98)
    OP_0D()
    Fade(100)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x20)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0x23)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x1F, 0x0)
    EndChrThread(0x20, 0x0)
    EndChrThread(0x2A, 0x1)
    Battle("BattleInfo_9D0", 0x0, 0x0, 0x100, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 106)
    Return()

    # Function_101_12D50 end

    def Function_102_13362(): pass

    label("Function_102_13362")

    OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sleep(150)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sleep(150)
    Sound(567, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x2, 0x1, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1388, 0x0)
    Return()

    # Function_102_13362 end

    def Function_103_134B2(): pass

    label("Function_103_134B2")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x2, 0x2, 0x1)
    Sleep(300)
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0x5DC, 0x3, 0x2, 0x1, 0x0)
    Sleep(200)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x36B0, 0x1388, 0x0)
    Return()

    # Function_103_134B2 end

    def Function_104_13569(): pass

    label("Function_104_13569")

    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1770, 0x0)
    Return()

    # Function_104_13569 end

    def Function_105_13579(): pass

    label("Function_105_13579")

    OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x1770, 0x0)
    Return()

    # Function_105_13579 end

    def Function_106_13589(): pass

    label("Function_106_13589")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00250.itc", 0x1F)
    LoadChrToIndex("chr/ch00350.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03250.itc", 0x23)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13000, -2000, -500, 270)
    SetChrPos(0x104, -13000, -2000, 500, 270)
    SetChrPos(0x103, -11500, -2000, -500, 270)
    SetChrPos(0x105, -11500, -2000, 500, 270)
    SetChrPos(0x109, -12000, -2000, -1300, 270)
    SetChrPos(0x106, -12350, -2000, 1300, 270)
    Call(0, 107)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    OP_68(-13000, -1000, 0, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12400, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(11400, 1500)
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_0D()
    Sleep(300)
    Sound(913, 0, 60, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0678
    ChrTalk(
        0x101,
        "#00005F#11P这是……！\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x103,
        "#00202F#12P蔡特已经开始行动了！\x02",
    )

    CloseMessageWindow()
    StopSound(136, 500, 100)
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetScenarioFlags(0x22, 0)
    NewScene("t1030", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_106_13589 end

    def Function_107_13804(): pass

    label("Function_107_13804")

    SetChrChipByIndex(0x1A, 0xB)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    OP_52(0x1A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1A, 0x40)
    ClearChrFlags(0x1A, 0x1)
    SetChrPos(0x1A, -17580, -2000, -1910, 270)
    SetChrChipByIndex(0x1B, 0xB)
    SetChrSubChip(0x1B, 0x1)
    ClearChrFlags(0x1B, 0x80)
    OP_52(0x1B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1B, 0x40)
    ClearChrFlags(0x1B, 0x1)
    SetChrPos(0x1B, -15910, -2000, 640, 315)
    SetChrChipByIndex(0x1C, 0xB)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    OP_52(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1C, 0x40)
    ClearChrFlags(0x1C, 0x1)
    SetChrPos(0x1C, -18880, -2000, 120, 180)
    Return()

    # Function_107_13804 end

    def Function_108_1389E(): pass

    label("Function_108_1389E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -13000, -2000, -500, 270)
    SetChrPos(0x104, -13000, -2000, 500, 270)
    SetChrPos(0x103, -11500, -2000, -500, 270)
    SetChrPos(0x105, -11500, -2000, 500, 270)
    SetChrPos(0x109, -12000, -2000, -1300, 270)
    SetChrPos(0x106, -12350, -2000, 1300, 270)
    Call(0, 107)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    OP_68(-15000, -1000, 0, 0)
    MoveCamera(315, 26, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    FadeToBright(1000, 0)
    OP_68(-13000, -1000, 0, 2000)
    OP_6F(0x79)
    OP_0D()

    #C0680
    ChrTalk(
        0x106,
        (
            "#10702F#11P主题公园那边的战斗\x01",
            "好像已经开始了！\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        (
            "#00007F#5P好！我们就趁此机会\x01",
            "通过商店街！\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x109,
        "#10107F#12P是！队长！\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    SetChrPos(0x0, -10140, -2000, 270, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A3, 5)
    OP_29(0xAF, 0x1, 0x13)
    OP_1B(0x0, 0xFF, 0xFFFF)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_108_1389E end

    def Function_109_13A56(): pass

    label("Function_109_13A56")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch15000.itc", 0x1E)
    LoadChrToIndex("chr/ch15700.itc", 0x1F)
    LoadChrToIndex("chr/ch15100.itc", 0x20)
    LoadChrToIndex("chr/ch15200.itc", 0x21)
    LoadChrToIndex("chr/ch15500.itc", 0x22)
    LoadChrToIndex("monster/ch87150.itc", 0x23)
    LoadChrToIndex("monster/ch87153.itc", 0x2E)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    LoadChrToIndex("apl/ch51352.itc", 0x2B)
    LoadChrToIndex("apl/ch51353.itc", 0x2C)
    LoadChrToIndex("apl/ch51354.itc", 0x2D)
    Call(0, 110)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_13AC2")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_13ADC")

    label("loc_13AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_13AD6")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_13ADC")

    label("loc_13AD6")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_13ADC")

    LoadChrToIndex("monster/ch87150.itc", 0x23)
    LoadChrToIndex("monster/ch87050.itc", 0x26)
    LoadChrToIndex("monster/ch87250.itc", 0x27)
    LoadChrToIndex("monster/ch87350.itc", 0x28)
    LoadChrToIndex("monster/ch87450.itc", 0x29)
    LoadChrToIndex("monster/ch87550.itc", 0x2A)
    Call(0, 113)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_13B1D")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_13B37")

    label("loc_13B1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_13B31")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_13B37")

    label("loc_13B31")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_13B37")

    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    Call(0, 126)
    Return()

    # Function_109_13A56 end

    def Function_110_13B59(): pass

    label("Function_110_13B59")

    OP_68(41670, -5400, 440, 0)
    MoveCamera(315, 25, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9670, 0)
    LoadEffect(0x0, "eff\\mgm03_02.eff")
    LoadEffect(0x1, "eff\\mgm03_01.eff")
    LoadEffect(0x2, "eff\\step04.eff")
    LoadEffect(0x3, "battle\\ms00053.eff")
    SoundLoad(989)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrChipByIndex(0x153, 0x1F)
    SetChrFlags(0x101, 0x1000)
    SetChrFlags(0x153, 0x1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_13BFA")
    SetChrChipByIndex(0xEF, 0x20)
    Jump("loc_13C10")

    label("loc_13BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_13C0C")
    SetChrChipByIndex(0xEF, 0x21)
    Jump("loc_13C10")

    label("loc_13C0C")

    SetChrChipByIndex(0xEF, 0x22)

    label("loc_13C10")

    SetChrPos(0x101, 40230, -6910, 1770, 135)
    SetChrPos(0x153, 42190, -7020, 1260, 270)
    SetChrPos(0xEF, 40720, -6970, -210, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0683
    ChrTalk(
        0x101,
        (
            "#11P#12503F那就立刻展开作战吧。\x02\x03",

            "#12500F就按照之前说明的方针行动，没问题吧？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_13DF3")

    #C0684
    ChrTalk(
        0x102,
        (
            "#6P#12600F嗯，在水边游玩，\x01",
            "把魔兽引出来。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    #C0685
    ChrTalk(
        0x101,
        (
            "#11P#12500F是的，拜托了。\x02\x03",

            "#12503F这种魔兽恐怕拥有\x01",
            "很奇特的性质，\x01",
            "一定要多加注意。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        (
            "#6P#12601F嗯，我明白。\x02\x03",

            "#12603F驱逐划破泳装的魔兽……\x01",
            "突然接到这样的请求，还真是吃了一惊……\x02\x03",

            "#12600F但就算是为了贝尔，\x01",
            "我也一定要帮忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x153,
        "#12P#13200F加油哦，罗伊德，艾莉！\x02",
    )

    CloseMessageWindow()
    Jump("loc_140BE")

    label("loc_13DF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_13F57")

    #C0688
    ChrTalk(
        0x103,
        (
            "#6P#12700F嗯，在水边游玩，\x01",
            "引出魔兽。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    #C0689
    ChrTalk(
        0x101,
        (
            "#11P#12500F是的，拜托了。\x02\x03",

            "#12503F这种魔兽恐怕拥有\x01",
            "很奇特的性质，\x01",
            "一定要多加注意。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x103,
        (
            "#6P#12700F嗯，当然。\x02\x03",

            "#12703F驱逐划破泳装的魔兽……\x01",
            "突然接到这样的请求，的确吃了一惊……\x02\x03",

            "#12701F不过，竟敢在咪西的眼皮底下做这种坏事，\x01",
            "无论如何也不能原谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x153,
        "#12P#13200F加油哦，罗伊德，缇欧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_140BE")

    label("loc_13F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_140BE")

    #C0692
    ChrTalk(
        0x109,
        (
            "#6P#13000F是，在水边游玩，\x01",
            "将魔兽引出，没错吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    #C0693
    ChrTalk(
        0x101,
        (
            "#11P#12500F是的，拜托了。\x02\x03",

            "#12503F这种魔兽恐怕拥有\x01",
            "很奇特的性质，\x01",
            "一定要多加注意。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x109,
        (
            "#6P#13000F嗯，那是自然！\x02\x03",

            "#13003F驱逐划破泳装的魔兽……\x01",
            "突然接到这样的请求，真是吃了一惊……\x02\x03",

            "#13000F但为了在湖水浴场游玩的各位，\x01",
            "我一定会努力完成任务！\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x153,
        "#12P#13200F加油哦，罗伊德，诺艾尔！\x02",
    )

    CloseMessageWindow()

    label("loc_140BE")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(47130, -5780, 17350, 0)
    MoveCamera(308, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9650, 0)
    SetChrPos(0x101, 46390, -7080, 15860, 0)
    SetChrPos(0x153, 36870, -6410, 18860, 90)
    SetChrPos(0xEF, 46670, -7080, 19800, 180)
    FadeToBright(1000, 0)
    OP_0D()
    OP_97(0x101, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 46670, -7080, 19800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(11, 0, 70, 0)

    #C0696
    ChrTalk(
        0x101,
        "#6P#12500F看招。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_14206")

    #C0697
    ChrTalk(
        0x102,
        "#12602F呀，罗伊德真是的。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(100)

    #C0698
    ChrTalk(
        0x102,
        (
            "#12606F……呼，话说回来，\x01",
            "魔兽怎么还不出现啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142C5")

    label("loc_14206")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_14267")

    #C0699
    ChrTalk(
        0x103,
        "#12702F唔，好大胆子。\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(100)

    #C0700
    ChrTalk(
        0x103,
        (
            "#12706F……话说回来，\x01",
            "魔兽还是不出现呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142C5")

    label("loc_14267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_142C5")

    #C0701
    ChrTalk(
        0x109,
        "#13002F呜，大意了！\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x87, 0x1F4)
    Sleep(100)

    #C0702
    ChrTalk(
        0x109,
        (
            "#13006F……呼，话说回来，\x01",
            "魔兽还是不出现啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142C5")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    #C0703
    ChrTalk(
        0x101,
        (
            "#6P#12505F嗯，说不定魔兽\x01",
            "已经有所警戒了。\x02\x03",

            "#12503F不过确实有魔兽存在，\x01",
            "我们还是继续观望……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xEF, 0xB4, 0x1F4)
    Sleep(100)
    OP_97(0xEF, 0x0, 0x0, 0xFFFFFE0C, 0xBB8, 0x0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 46390, -7080, 16360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(11, 0, 70, 0)
    Sleep(100)

    #C0704
    ChrTalk(
        0x101,
        "#6P#12511F哇！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_143D7")

    #C0705
    ChrTalk(
        0x102,
        "#12609F呵呵，还你一击。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14428")

    label("loc_143D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_14400")

    #C0706
    ChrTalk(
        0x103,
        "#12704F……这是反击。\x02",
    )

    CloseMessageWindow()
    Jump("loc_14428")

    label("loc_14400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_14428")

    #C0707
    ChrTalk(
        0x109,
        "#13009F啊哈哈，反击成功！\x02",
    )

    CloseMessageWindow()

    label("loc_14428")


    #C0708
    ChrTalk(
        0x101,
        "#6P#12512F可、可恶……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_0D()
    OP_68(38460, -5480, 18640, 3000)
    MoveCamera(279, 17, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10180, 3000)
    OP_6F(0x79)
    OP_63(0x153, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0709
    ChrTalk(
        0x153,
        (
            "#5P#13206F（唔唔，琪雅也想和\x01",
            "  他们一起玩。）\x02\x03",

            "#13208F（罗伊德说很危险，\x01",
            "  但看起来明明很开心……）\x02\x03",

            "#13205F（……哎？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrChipByIndex(0x24, 0x23)
    SetChrPos(0x24, 47570, -7100, 21350, 180)
    Fade(500)
    OP_68(47030, -5480, 17480, 0)
    MoveCamera(295, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(10110, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_68(47500, -5480, 18810, 3000)
    MoveCamera(295, 40, 0, 3000)
    OP_6E(800, 3000)
    SetCameraDistance(10110, 3000)
    Sleep(1000)
    Sound(989, 2, 60, 0)
    BeginChrThread(0x24, 3, 0, 112)
    OP_6F(0x79)

    #C0710
    ChrTalk(
        0x153,
        "#13205F啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_1492A")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0711
    ChrTalk(
        0x153,
        "#13207F#4S艾莉，后面！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0712
    ChrTalk(
        0x102,
        "#12P#12605F哎……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x80)
    OP_68(46650, -5480, 17880, 1000)
    MoveCamera(313, 20, 0, 1000)
    SetCameraDistance(10110, 1000)
    Sound(976, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 47570, -7100, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(246, 0, 100, 0)
    Sound(327, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 46670, -6500, 20200, 180, 0, 45, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_9C(0x24, 0xFFFFF830, 0x0, 0xFFFFF510, 0x2BC, 0x7D0)
    Sound(833, 0, 40, 0)
    Sound(591, 0, 100, 0)
    Sleep(100)
    PlayEffect(0x0, 0x4, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x3, 0x2)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x102, 0x2B)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x8)
    SetChrFlags(0x102, 0x2)
    SetChrPos(0x102, 46670, -7080, 19300, 180)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    #Sound(3391, 255, 100, 0)    #voice#Elie

    #C0713
    ChrTalk(
        0x102,
        "#12615F#4S──呀啊啊啊啊！！？？\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    StopEffect(0x4, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sound(570, 0, 50, 0)
    OP_9E(0x24, 0xAB22, 0x483A, 0x57E40, 0x1F40, 0x1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sound(570, 0, 50, 0)

    def lambda_14876():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_14876)
    Sleep(1000)

    def lambda_14893():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14893)

    #C0714
    ChrTalk(
        0x101,
        "#6P#12511F艾、艾莉……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    #C0715
    ChrTalk(
        0x102,
        (
            "#12613F不、不用管我……\x01",
            "快去追魔兽！！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0716
    ChrTalk(
        0x101,
        "#6P#12501F明、明白了！！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x4, 0x3, 0x2)
    Jump("loc_14F85")

    label("loc_1492A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_14C5A")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0717
    ChrTalk(
        0x153,
        "#13207F#4S缇欧，后面！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0718
    ChrTalk(
        0x103,
        "#12P#12705F哎……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x80)
    OP_68(46650, -5480, 17880, 1000)
    MoveCamera(313, 20, 0, 1000)
    SetCameraDistance(10110, 1000)
    Sound(976, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 47570, -7100, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(246, 0, 100, 0)
    Sound(327, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 46670, -6500, 20200, 180, 0, 45, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_9C(0x24, 0xFFFFF830, 0x0, 0xFFFFF510, 0x2BC, 0x7D0)
    Sound(833, 0, 40, 0)
    Sound(591, 0, 100, 0)
    Sleep(100)
    PlayEffect(0x0, 0x4, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x3, 0x2)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x2C)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x8)
    SetChrFlags(0x103, 0x2)
    SetChrPos(0x103, 46670, -7080, 19300, 180)
    #Sound(2225, 255, 100, 0)    #voice#Tio
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0719
    ChrTalk(
        0x103,
        "#12710F#4S──呀……！！？？\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    StopEffect(0x4, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sound(570, 0, 50, 0)
    OP_9E(0x24, 0xAB22, 0x483A, 0x57E40, 0x1F40, 0x1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sound(570, 0, 50, 0)

    def lambda_14BA2():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_14BA2)
    Sleep(1000)

    def lambda_14BBF():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14BBF)

    #C0720
    ChrTalk(
        0x101,
        "#6P#12511F缇、缇欧……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    #C0721
    ChrTalk(
        0x103,
        (
            "#12701F我、我没关系……\x01",
            "快去……追魔兽！！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0722
    ChrTalk(
        0x101,
        "#6P#12501F明、明白了！！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x4, 0x3, 0x2)
    Jump("loc_14F85")

    label("loc_14C5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_14F85")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0723
    ChrTalk(
        0x153,
        "#13207F#4S诺艾尔，后面！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0724
    ChrTalk(
        0x109,
        "#12P#13005F哎……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x24, 0x80)
    OP_68(46650, -5480, 17880, 1000)
    MoveCamera(313, 20, 0, 1000)
    SetCameraDistance(10110, 1000)
    Sound(976, 0, 50, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 47570, -7100, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    Sound(246, 0, 100, 0)
    Sound(327, 0, 100, 0)
    PlayEffect(0x3, 0xFF, 0xFF, 0x0, 46670, -6500, 20200, 180, 0, 45, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_9C(0x24, 0xFFFFF830, 0x0, 0xFFFFF510, 0x2BC, 0x7D0)
    Sound(833, 0, 40, 0)
    Sound(591, 0, 100, 0)
    Sleep(100)
    PlayEffect(0x0, 0x4, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 45680, -7060, 18500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    StopEffect(0x3, 0x2)
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x2D)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x8)
    SetChrFlags(0x109, 0x2)
    SetChrPos(0x109, 46670, -7080, 19300, 180)
    #Sound(3517, 255, 100, 0)    #voice#Noel
    OP_82(0xC8, 0x0, 0xBB8, 0x320)

    #C0725
    ChrTalk(
        0x109,
        "#13014F#4S──哇……！！？？\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x0, 0x1, 0x2)
    StopEffect(0x4, 0x2)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7451", 0)
    OP_63(0x24, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sound(570, 0, 50, 0)
    OP_9E(0x24, 0xAB22, 0x483A, 0x57E40, 0x1F40, 0x1)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sound(570, 0, 50, 0)

    def lambda_14ED4():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_14ED4)
    Sleep(1000)

    def lambda_14EF1():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14EF1)

    #C0726
    ChrTalk(
        0x101,
        "#6P#12511F诺、诺艾尔……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    #C0727
    ChrTalk(
        0x109,
        (
            "#13006F我、我没事的，\x01",
            "先去追魔兽……！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0728
    ChrTalk(
        0x101,
        "#6P#12501F明、明白了！！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x4, 0x3, 0x2)

    label("loc_14F85")


    def lambda_14F8A():
        OP_95(0xFE, 34050, -6300, 8750, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14F8A)
    Sleep(100)

    def lambda_14FA7():
        OP_99(0xFE, 0xEF, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_14FA7)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(19420, -5480, -8710, 0)
    MoveCamera(246, 22, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15040, 0)
    SetChrPos(0x101, 24590, -6010, -1280, 225)
    SetChrPos(0x24, 27950, -6000, -4240, 225)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x153, 0xFF)
    SetChrSubChip(0x153, 0x0)
    SetChrChipByIndex(0xEF, 0xFF)
    SetChrSubChip(0xEF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_15040")
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_15063")

    label("loc_15040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_15054")
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_15063")

    label("loc_15054")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_15063")
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x52, 0xFF)

    label("loc_15063")


    def lambda_15068():
        OP_95(0xFE, 9860, -6000, -21850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_15068)
    Sleep(2000)

    def lambda_15085():
        OP_95(0xFE, 11690, -6000, -17960, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15085)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(10060, -5780, -20380, 6000)
    MoveCamera(246, 22, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(12250, 6000)
    WaitChrThread(0x24, 1)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_150F0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_150F0)
    Sleep(1000)

    def lambda_15100():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_15100)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0729
    ChrTalk(
        0x101,
        (
            "#12P#00006F呼、呼……\x01",
            "追、追到了！！\x02\x03",

            "#00001F划破女性泳装\x01",
            "的卑劣行径……\x01",
            "绝不允许你继续下去了！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x24)
    TurnDirection(0x24, 0x101, 500)
    OP_63(0x24, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(997, 0, 100, 0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    BeginChrThread(0x24, 1, 0, 111)
    Fade(250)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    Sound(805, 0, 100, 0)
    OP_0D()

    #C0730
    ChrTalk(
        0x101,
        "#12P#00007F来吧！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_948", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_110_13B59 end

    def Function_111_15203(): pass

    label("Function_111_15203")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15230")

    def lambda_15213():
        OP_A6(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_15213)
    WaitChrThread(0xFE, 2)
    Jump("Function_111_15203")

    label("loc_15230")

    Return()

    # Function_111_15203 end

    def Function_112_15231(): pass

    label("Function_112_15231")

    PlayEffect(0x0, 0x0, 0xFF, 0x0, 53980, -7250, 28200, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x0, 0x2)
    PlayEffect(0x0, 0x1, 0xFF, 0x0, 49870, -7170, 27390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x1, 0x2)
    PlayEffect(0x0, 0x2, 0xFF, 0x0, 49750, -7140, 23530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    StopEffect(0x2, 0x2)
    PlayEffect(0x0, 0x3, 0xFF, 0x0, 47570, -7100, 21350, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_112_15231 end

    def Function_113_15320(): pass

    label("Function_113_15320")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_15338")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_1535F")

    label("loc_15338")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1534E")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_1535F")

    label("loc_1534E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1535F")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_1535F")

    OP_68(10060, -5780, -20380, 0)
    MoveCamera(246, 22, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12250, 0)
    LoadEffect(0x0, "event/ev13002.eff")
    LoadEffect(0x1, "event/ev13003.eff")
    LoadEffect(0x2, "event/ev10017.eff")
    SetChrPos(0x101, 11690, -6000, -17960, 180)
    SetChrPos(0xEF, 20760, -6000, -10490, 225)
    SetChrPos(0x153, 18910, -6000, -9190, 225)
    SetChrFlags(0xEF, 0x80)
    SetChrFlags(0x153, 0x80)
    SetChrChipByIndex(0x101, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x24, 0x23)
    SetChrSubChip(0x24, 0x0)
    SetChrChipByIndex(0x25, 0x26)
    SetChrChipByIndex(0x26, 0x27)
    SetChrChipByIndex(0x27, 0x28)
    SetChrChipByIndex(0x28, 0x29)
    SetChrChipByIndex(0x29, 0x2A)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x24, 9860, -6000, -21850, 0)
    SetChrPos(0x25, 28140, -2000, -38880, 315)
    SetChrPos(0x26, 31250, -2000, -37580, 315)
    SetChrPos(0x27, 16490, -2000, -39030, 315)
    SetChrPos(0x28, 20180, -2000, -40520, 315)
    SetChrPos(0x29, 29330, -2000, -41320, 315)
    PlayBGM("ed7451", 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x24, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0731
    ChrTalk(
        0x101,
        (
            "#12P#00000F怎么样……\x01",
            "死心吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9490, -5480, -21070, 3000)

    def lambda_15525():
        OP_99(0xFE, 0x24, 0xBB8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_15525)
    Sleep(500)

    def lambda_1553C():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1553C)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(2000)
    OP_64(0x24)
    StopBGM(0xBB8)
    Sound(997, 0, 100, 0)
    Sleep(800)
    Sound(997, 0, 100, 0)
    Sleep(300)
    Sound(997, 0, 100, 0)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_155C2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_155C2)
    Sleep(100)

    def lambda_155D2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_155D2)

    #C0732
    ChrTalk(
        0x101,
        "#12P#00005F什么……！？\x02",
    )

    CloseMessageWindow()

    def lambda_155FC():
        OP_95(0xFE, 23660, -2000, -35810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_155FC)
    Sleep(100)

    def lambda_15619():
        OP_95(0xFE, 24940, -2000, -35780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_15619)
    Sleep(100)

    def lambda_15636():
        OP_95(0xFE, 21250, -2000, -36870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15636)
    Sleep(100)

    def lambda_15653():
        OP_95(0xFE, 21590, -2000, -35820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_15653)
    Sleep(100)

    def lambda_15670():
        OP_95(0xFE, 23090, -2000, -36580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_15670)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    Fade(500)
    OP_68(22400, -980, -33530, 0)
    MoveCamera(196, 24, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14520, 0)
    OP_68(21730, -980, -33480, 5000)
    MoveCamera(155, -3, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(10320, 5000)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(8410, 500)
    Sleep(100)
    Sound(997, 0, 100, 0)
    BeginChrThread(0x25, 3, 0, 114)
    BeginChrThread(0x26, 3, 0, 115)
    BeginChrThread(0x27, 3, 0, 116)
    BeginChrThread(0x28, 3, 0, 117)
    BeginChrThread(0x29, 3, 0, 118)
    WaitChrThread(0x25, 3)
    Sound(556, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 28360, -2000, -46730, -30, 0, 0, 2500, 2500, 2500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 24080, -2000, -38350, -30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 0, 0, -30, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(1500)
    Sleep(500)
    StopEffect(0x0, 0x2)
    Sleep(2000)
    SetMessageWindowPos(400, 300, -1, -1)

    #A0733
    AnonymousTalk(
        0x101,
        "#00011F还、还有同伴吗！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(22520, -980, -32840, 0)
    MoveCamera(310, 28, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(16650, 0)
    BeginChrThread(0x25, 3, 0, 119)
    Sleep(300)
    BeginChrThread(0x26, 3, 0, 120)
    Sleep(300)
    BeginChrThread(0x27, 3, 0, 121)
    Sleep(300)
    BeginChrThread(0x28, 3, 0, 122)
    Sleep(300)
    BeginChrThread(0x29, 3, 0, 123)
    OP_68(10920, -5480, -18810, 2000)
    MoveCamera(281, 22, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(12890, 2000)
    TurnDirection(0x24, 0x101, 500)
    WaitChrThread(0x24, 3)
    BeginChrThread(0x24, 3, 0, 124)
    WaitChrThread(0x28, 3)
    BeginChrThread(0x28, 3, 0, 124)
    WaitChrThread(0x26, 3)
    BeginChrThread(0x26, 3, 0, 124)
    WaitChrThread(0x25, 3)
    BeginChrThread(0x25, 3, 0, 124)
    WaitChrThread(0x29, 3)
    BeginChrThread(0x29, 3, 0, 124)
    WaitChrThread(0x27, 3)
    BeginChrThread(0x27, 3, 0, 124)
    BeginChrThread(0x2A, 1, 0, 125)
    OP_6F(0x79)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0734
    ChrTalk(
        0x101,
        "#11P#00010F呜……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xEF, 0x80)
    ClearChrFlags(0x153, 0x80)

    #N0735
    NpcTalk(
        0x153,
        "琪雅的声音",
        "#4S罗伊德！！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x26, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x27, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x28, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_15A0E():
        OP_95(0xFE, 15180, -6000, -13330, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_15A0E)

    def lambda_15A28():
        OP_95(0xFE, 15380, -6000, -15880, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_15A28)

    def lambda_15A42():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_15A42)

    def lambda_15A4F():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_15A4F)

    def lambda_15A5C():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_15A5C)

    def lambda_15A69():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_15A69)
    Fade(500)
    OP_68(12740, -5980, -10870, 0)
    MoveCamera(308, 19, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15750, 0)
    OP_93(0x101, 0x2D, 0x1F4)
    OP_68(9910, -5980, -17140, 3000)
    MoveCamera(290, 19, 0, 3000)
    WaitChrThread(0xEF, 1)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0xEF, 0x25)
    SetChrSubChip(0xEF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_15AEE")
    Sound(805, 0, 100, 0)
    Jump("loc_15AF4")

    label("loc_15AEE")

    Sound(531, 0, 100, 0)

    label("loc_15AF4")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_15B6D")

    #C0736
    ChrTalk(
        0x101,
        (
            "#00005F琪雅，还有艾莉！\x01",
            "……你没事了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x102,
        (
            "#12P#00113F有、有话稍后再说，\x01",
            "现在先把这些魔兽解决！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C59")

    label("loc_15B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_15BE3")

    #C0738
    ChrTalk(
        0x101,
        (
            "#00005F琪雅，还有缇欧！\x01",
            "……你没事了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x103,
        (
            "#12P#00203F……有话稍后再说！\x01",
            "先把眼前的魔兽击退！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C59")

    label("loc_15BE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_15C59")

    #C0740
    ChrTalk(
        0x101,
        (
            "#00005F琪雅，还有诺艾尔！\x01",
            "……你没事了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x109,
        (
            "#12P#10107F是、是的！！\x01",
            "总之，先把眼前的\x01",
            "魔兽击退吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C59")


    #C0742
    ChrTalk(
        0x101,
        "#00000F嗯，知道了！\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x153,
        "#01107F二位都要加油！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_98C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_113_15320 end

    def Function_114_15CA9(): pass

    label("Function_114_15CA9")

    OP_93(0x25, 0x13B, 0x1F4)
    OP_A1(0x25, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_114_15CA9 end

    def Function_115_15CBC(): pass

    label("Function_115_15CBC")

    OP_93(0x26, 0x13B, 0x1F4)
    OP_A1(0x26, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_115_15CBC end

    def Function_116_15CCF(): pass

    label("Function_116_15CCF")

    OP_93(0x27, 0x13B, 0x1F4)
    OP_A1(0x27, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_116_15CCF end

    def Function_117_15CE2(): pass

    label("Function_117_15CE2")

    OP_93(0x28, 0x13B, 0x1F4)
    OP_A1(0x28, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_117_15CE2 end

    def Function_118_15CF5(): pass

    label("Function_118_15CF5")

    OP_93(0x29, 0x13B, 0x1F4)
    OP_A1(0x29, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_118_15CF5 end

    def Function_119_15D08(): pass

    label("Function_119_15D08")

    OP_A1(0x25, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x25, 0x50BE, 0xFFFFE890, 0xFFFF9A34, 0x7D0, 0x1388)
    OP_95(0x25, 10410, -6000, -16510, 5000, 0x0)
    TurnDirection(0x25, 0x101, 500)
    Return()

    # Function_119_15D08 end

    def Function_120_15D48(): pass

    label("Function_120_15D48")

    OP_A1(0x26, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x26, 0x4C22, 0xFFFFE890, 0xFFFF952A, 0x7D0, 0x1388)
    OP_95(0x26, 8150, -6000, -20170, 5000, 0x0)
    TurnDirection(0x26, 0x101, 500)
    Return()

    # Function_120_15D48 end

    def Function_121_15D88(): pass

    label("Function_121_15D88")

    OP_A1(0x27, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x27, 0x5942, 0xFFFFE890, 0xFFFF94DA, 0x7D0, 0x1388)
    OP_95(0x27, 12360, -6000, -15910, 5000, 0x0)
    TurnDirection(0x27, 0x101, 500)
    Return()

    # Function_121_15D88 end

    def Function_122_15DC8(): pass

    label("Function_122_15DC8")

    OP_A1(0x28, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x28, 0x4A4C, 0xFFFFE890, 0xFFFF9098, 0x7D0, 0x1388)
    OP_95(0x28, 13700, -6000, -22060, 5000, 0x0)
    TurnDirection(0x28, 0x101, 500)
    Return()

    # Function_122_15DC8 end

    def Function_123_15E08(): pass

    label("Function_123_15E08")

    OP_A1(0x29, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x29, 0x51E0, 0xFFFFE890, 0xFFFF93CC, 0x7D0, 0x1388)
    OP_95(0x29, 14480, -6000, -18580, 5000, 0x0)
    TurnDirection(0x29, 0x101, 500)
    Return()

    # Function_123_15E08 end

    def Function_124_15E48(): pass

    label("Function_124_15E48")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15E53")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_15E71")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_15E53")

    label("loc_15E71")

    Return()

    # Function_124_15E48 end

    def Function_125_15E72(): pass

    label("Function_125_15E72")

    Sound(997, 0, 100, 0)
    Sleep(800)
    Sound(997, 0, 100, 0)
    Sleep(300)
    Sound(997, 0, 100, 0)
    Return()

    # Function_125_15E72 end

    def Function_126_15E8B(): pass

    label("Function_126_15E8B")

    EventBegin(0x0)
    OP_68(13510, -4600, -17730, 0)
    MoveCamera(239, 23, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(8670, 0)
    SetChrPos(0x101, 11690, -6000, -17960, 180)
    SetChrPos(0x153, 13410, -6000, -16830, 180)
    SetChrPos(0xEF, 13730, -6000, -18890, 180)
    SetCameraDistance(9670, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(250)
    Sound(805, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15F2F")
    Sound(531, 0, 100, 0)

    label("loc_15F2F")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0xEF, 0xFF)
    OP_0D()

    #C0744
    ChrTalk(
        0x101,
        (
            "#00006F呼……\x01",
            "总算收拾掉了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    #C0745
    ChrTalk(
        0x101,
        "#00000F你们二位都辛苦了。\x02",
    )

    CloseMessageWindow()

    def lambda_15F8A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_15F8A)
    Sleep(100)

    def lambda_15F9A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_15F9A)
    Sleep(500)

    #C0746
    ChrTalk(
        0x153,
        "#12P#01109F嘿嘿嘿，辛苦啦。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_160EF")

    #C0747
    ChrTalk(
        0x102,
        (
            "#6P#00104F这样一来，\x01",
            "总算是完成任务了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    #C0748
    ChrTalk(
        0x101,
        (
            "#00008F……那个……艾莉。\x02\x03",

            "#00006F该说什么好呢……\x01",
            "没能保护好你，真是抱歉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    #C0749
    ChrTalk(
        0x102,
        (
            "#6P#00112F真、真是的，不用在意那种事啦。\x01",
            "也怪我太大意了……\x02\x03",

            "#00103F话说回来，那样的魔兽\x01",
            "为什么会出现在湖水浴场呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1631D")

    label("loc_160EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1620A")

    #C0750
    ChrTalk(
        0x103,
        (
            "#6P#00204F这样一来，\x01",
            "总算是完成任务了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    #C0751
    ChrTalk(
        0x101,
        (
            "#00008F……那个……缇欧。\x02\x03",

            "#00006F该说什么好呢……\x01",
            "没能保护好你，真是抱歉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    #C0752
    ChrTalk(
        0x103,
        (
            "#6P#00203F……不必在意。\x01",
            "我太大意，也有责任……\x02\x03",

            "#00200F话说回来，那样的魔兽\x01",
            "为什么会出现在湖水浴场呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1631D")

    label("loc_1620A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1631D")

    #C0753
    ChrTalk(
        0x109,
        "#6P#10109F总算完成了任务啊！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    #C0754
    ChrTalk(
        0x101,
        (
            "#00008F……那个……诺艾尔。\x02\x03",

            "#00006F该说什么好呢……\x01",
            "没能保护好你，真是抱歉。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xEF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xEF)

    #C0755
    ChrTalk(
        0x109,
        (
            "#6P#10112F请、请不必介意这种事！\x01",
            "还是怪我太大意了……\x02\x03",

            "#10105F话说回来，那样的魔兽\x01",
            "为什么会出现在湖水浴场呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1631D")


    #C0756
    ChrTalk(
        0x101,
        (
            "#00006F这只是我的臆测……\x01",
            "多半是因为开发计划的影响吧。\x02\x03",

            "#00001F那些魔兽由于开发工程而失去了栖息地，\x01",
            "为了泄愤，才开始给人类捣乱……\x01",
            "这应该是可能性最大的原因了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_164DD")

    #C0757
    ChrTalk(
        0x102,
        (
            "#6P#00103F原来如此……有可能呢。\x02\x03",

            "#00101F它们不断划破泳装，\x01",
            "大概也是因为引起了巨大\x01",
            "骚乱之后，渐渐开始上瘾了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x153,
        (
            "#12P#01108F……总觉得那些小企鹅\x01",
            "也很可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x02\x03",

            "#00000F……算了，\x01",
            "现在还是先去向\x01",
            "卡尔米娜小姐报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x102,
        "#6P#00100F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16716")

    label("loc_164DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_165FA")

    #C0761
    ChrTalk(
        0x103,
        (
            "#6P#00203F原来如此……的确有可能。\x02\x03",

            "#00200F它们不断划破泳装，\x01",
            "大概也是因为引起了巨大\x01",
            "骚乱之后，渐渐开始上瘾了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x153,
        (
            "#12P#01108F……总觉得那些小企鹅\x01",
            "也很可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x02\x03",

            "#00000F……算了，\x01",
            "现在还是先去向\x01",
            "卡尔米娜小姐报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x103,
        "#6P#00200F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16716")

    label("loc_165FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16716")

    #C0765
    ChrTalk(
        0x109,
        (
            "#6P#10103F原来如此……的确有可能呢。\x02\x03",

            "#10101F它们不断划破泳装，\x01",
            "大概也是因为引起了巨大\x01",
            "骚乱之后，渐渐开始上瘾了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x153,
        (
            "#12P#01108F……总觉得那些小企鹅\x01",
            "也很可怜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x101,
        (
            "#00003F是啊……\x02\x03",

            "#00000F……算了，\x01",
            "现在还是先去向\x01",
            "卡尔米娜小姐报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x109,
        "#6P#10100F是，出发吧！\x02",
    )

    CloseMessageWindow()

    label("loc_16716")

    StopSound(136, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 3)
    NewScene("t1320", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_126_15E8B end

    SaveToFile()

Try(main)
