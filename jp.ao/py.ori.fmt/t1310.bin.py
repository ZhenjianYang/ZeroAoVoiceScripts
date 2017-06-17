from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "セシル",                 # 1
        "リーシャ",               # 2
        "エリィ",                 # 3
        "ティオ",                 # 4
        "フラン",                 # 5
        "ツァイト",               # 6
        "キーア",                 # 7
        "シュリ",                 # 8
        "イリア",                 # 9
        "ランディ",               # 10
        "ノエル",                 # 11
        "ワジ",                   # 12
        "ボール",                 # 13
        "メルカバ",               # 14
        "メルカバ",               # 15
        "猟兵",                   # 16
        "猟兵",                   # 17
        "猟兵",                   # 18
        "猟兵",                   # 19
        "猟兵",                   # 20
        "猟兵",                   # 21
        "軍用犬",                 # 22
        "軍用犬",                 # 23
        "軍用犬",                 # 24
        "軍用犬",                 # 25
        "エリザベート",           # 26
        "タッパー",               # 27
        "監視員ウェイブ",         # 28
        "ペングー",               # 29
        "ペングー",               # 30
        "ペングー",               # 31
        "ペングー",               # 32
        "ペングー",               # 33
        "ペングー",               # 34
        "SE制御",                 # 35
        "bt1310",                 # 36
        "bt1310",                 # 37
        "bt1310",                 # 38
        "bt1320",                 # 39
        "ホテル・デルフィニア方面",# 40
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

    PlaceName(-50.0, 0.0, 0.0, 0x0000, 0x0000, "ホテル・デルフィニア方面")

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
        "Function_16_1717",        # 10, 16
        "Function_17_1BC7",        # 11, 17
        "Function_18_1EEA",        # 12, 18
        "Function_19_20ED",        # 13, 19
        "Function_20_233A",        # 14, 20
        "Function_21_245A",        # 15, 21
        "Function_22_25D5",        # 16, 22
        "Function_23_2719",        # 17, 23
        "Function_24_2B90",        # 18, 24
        "Function_25_2FA3",        # 19, 25
        "Function_26_3240",        # 1A, 26
        "Function_27_3406",        # 1B, 27
        "Function_28_346E",        # 1C, 28
        "Function_29_374E",        # 1D, 29
        "Function_30_3CA8",        # 1E, 30
        "Function_31_3DFA",        # 1F, 31
        "Function_32_421B",        # 20, 32
        "Function_33_4390",        # 21, 33
        "Function_34_4423",        # 22, 34
        "Function_35_448F",        # 23, 35
        "Function_36_44FB",        # 24, 36
        "Function_37_4554",        # 25, 37
        "Function_38_5A4A",        # 26, 38
        "Function_39_6E2F",        # 27, 39
        "Function_40_7505",        # 28, 40
        "Function_41_8232",        # 29, 41
        "Function_42_9D02",        # 2A, 42
        "Function_43_9D1A",        # 2B, 43
        "Function_44_A7F6",        # 2C, 44
        "Function_45_C706",        # 2D, 45
        "Function_46_C791",        # 2E, 46
        "Function_47_D114",        # 2F, 47
        "Function_48_D1B8",        # 30, 48
        "Function_49_D250",        # 31, 49
        "Function_50_D31F",        # 32, 50
        "Function_51_D3E1",        # 33, 51
        "Function_52_D4B0",        # 34, 52
        "Function_53_D799",        # 35, 53
        "Function_54_EA7C",        # 36, 54
        "Function_55_EBDF",        # 37, 55
        "Function_56_F3AE",        # 38, 56
        "Function_57_F6F1",        # 39, 57
        "Function_58_13416",       # 3A, 58
        "Function_59_134A5",       # 3B, 59
        "Function_60_134BD",       # 3C, 60
        "Function_61_134E8",       # 3D, 61
        "Function_62_13513",       # 3E, 62
        "Function_63_1353E",       # 3F, 63
        "Function_64_13569",       # 40, 64
        "Function_65_13594",       # 41, 65
        "Function_66_135BF",       # 42, 66
        "Function_67_135EA",       # 43, 67
        "Function_68_13615",       # 44, 68
        "Function_69_13640",       # 45, 69
        "Function_70_13657",       # 46, 70
        "Function_71_1366C",       # 47, 71
        "Function_72_13681",       # 48, 72
        "Function_73_13696",       # 49, 73
        "Function_74_13776",       # 4A, 74
        "Function_75_13859",       # 4B, 75
        "Function_76_13939",       # 4C, 76
        "Function_77_13A1C",       # 4D, 77
        "Function_78_13A80",       # 4E, 78
        "Function_79_13B10",       # 4F, 79
        "Function_80_13BA0",       # 50, 80
        "Function_81_13CF7",       # 51, 81
        "Function_82_14ADC",       # 52, 82
        "Function_83_14AFB",       # 53, 83
        "Function_84_14B5B",       # 54, 84
        "Function_85_14B92",       # 55, 85
        "Function_86_14C0C",       # 56, 86
        "Function_87_14C31",       # 57, 87
        "Function_88_14C96",       # 58, 88
        "Function_89_14CB2",       # 59, 89
        "Function_90_14DA3",       # 5A, 90
        "Function_91_14EC2",       # 5B, 91
        "Function_92_14EE9",       # 5C, 92
        "Function_93_14F10",       # 5D, 93
        "Function_94_14F2F",       # 5E, 94
        "Function_95_14F4E",       # 5F, 95
        "Function_96_14F86",       # 60, 96
        "Function_97_14FBE",       # 61, 97
        "Function_98_14FF6",       # 62, 98
        "Function_99_15010",       # 63, 99
        "Function_100_1535D",      # 64, 100
        "Function_101_153F7",      # 65, 101
        "Function_102_15A09",      # 66, 102
        "Function_103_15B59",      # 67, 103
        "Function_104_15C10",      # 68, 104
        "Function_105_15C20",      # 69, 105
        "Function_106_15C30",      # 6A, 106
        "Function_107_15EAD",      # 6B, 107
        "Function_108_15F47",      # 6C, 108
        "Function_109_16111",      # 6D, 109
        "Function_110_16214",      # 6E, 110
        "Function_111_17A92",      # 6F, 111
        "Function_112_17AC0",      # 70, 112
        "Function_113_17BAF",      # 71, 113
        "Function_114_18566",      # 72, 114
        "Function_115_18579",      # 73, 115
        "Function_116_1858C",      # 74, 116
        "Function_117_1859F",      # 75, 117
        "Function_118_185B2",      # 76, 118
        "Function_119_185C5",      # 77, 119
        "Function_120_18605",      # 78, 120
        "Function_121_18645",      # 79, 121
        "Function_122_18685",      # 7A, 122
        "Function_123_186C5",      # 7B, 123
        "Function_124_18705",      # 7C, 124
        "Function_125_1872F",      # 7D, 125
        "Function_126_18748",      # 7E, 126
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
    Jump("loc_1713")

    label("loc_1607")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1713")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AD")

    #C0001
    ChrTalk(
        0x22,
        (
            "君たち、今日ビーチを\x01",
            "貸切にしてるお客さんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0x22,
        (
            "ちぇっ、うらやましいなあ。\x01",
            "俺もあんな美女たちと一緒に\x01",
            "水遊びをしたいところだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1713")

    label("loc_16AD")


    #C0003
    ChrTalk(
        0x22,
        (
            "ああ、売店の商品は\x01",
            "今ちょっと準備中なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x22,
        (
            "悪いけど、もう少ししてから\x01",
            "また来てくれるかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1713")

    TalkEnd(0x22)
    Return()

    # Function_15_15E9 end

    def Function_16_1717(): pass

    label("Function_16_1717")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_183A")

    #C0005
    ChrTalk(
        0xFE,
        (
            "『ホワイトストーン』は、\x01",
            "この辺りでたまに見つかる\x01",
            "真っ白で綺麗な石だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "『ホワイトヘブン』の砂浜に\x01",
            "ときどき埋まっている石らしいし、\x01",
            "多分一緒に運ばれてきたんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "あんたも探してるんなら、\x01",
            "水辺ばかりじゃなく、\x01",
            "砂浜の方も調べてみるといいぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18E6")

    label("loc_183A")


    #C0008
    ChrTalk(
        0xFE,
        (
            "ホワイトストーンはもともと\x01",
            "『ホワイトヘブン』の砂浜に\x01",
            "ときどき埋まっている石らしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "あんたも探してるんなら、\x01",
            "水辺ばかりじゃなく、\x01",
            "砂浜の方も調べてみるといいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18E6")

    Jump("loc_1BC3")

    label("loc_18EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_1A38")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B9")

    #C0010
    ChrTalk(
        0xFE,
        (
            "しかし、噂の水着切り裂き魔が\x01",
            "あんな魔獣だったとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "俺はてっきりどこぞの変質者か\x01",
            "何かと思っていたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "まあ、ひとまず解決して何よりだ。\x01",
            "あんたらには礼をいうぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A33")

    label("loc_19B9")


    #C0013
    ChrTalk(
        0xFE,
        (
            "しかし、噂の水着切り裂き魔が\x01",
            "あんな魔獣だったとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "まあ、ひとまず解決して何よりだ。\x01",
            "あんたらには礼をいうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A33")

    Jump("loc_1BC3")

    label("loc_1A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_1BC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B32")

    #C0015
    ChrTalk(
        0xFE,
        (
            "俺は、このビーチで\x01",
            "危険な事が起こらないよう、\x01",
            "監視の目を光らせてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "このあたりはまだ浅いが、\x01",
            "沖に行き過ぎると子供じゃ\x01",
            "足がつかなくなったりする。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "水遊びするときは、くれぐれも\x01",
            "遠くに行き過ぎないようにな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1BC3")

    label("loc_1B32")


    #C0018
    ChrTalk(
        0xFE,
        (
            "このあたりはまだ浅いが、\x01",
            "沖に行き過ぎると子供じゃ\x01",
            "足がつかなくなったりする。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "水遊びするときは、くれぐれも\x01",
            "遠くに行き過ぎないようにな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BC3")

    TalkEnd(0xFE)
    Return()

    # Function_16_1717 end

    def Function_17_1BC7(): pass

    label("Function_17_1BC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1CDC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BEE")
    TalkEnd(0xFE)
    Call(0, 52)
    Return()

    label("loc_1BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CAB")

    #C0020
    ChrTalk(
        0xA,
        (
            "#12613Fまったくもう。\x01",
            "いきなりこんな所に\x01",
            "潜り込むなんて……\x02\x03",

            "#12611Fあなた、もう少し\x01",
            "デリカシーってものを\x01",
            "持った方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        "#12506Fめ、面目ないです……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1CD7")

    label("loc_1CAB")


    #C0022
    ChrTalk(
        0xA,
        (
            "#12613Fふう、まったく\x01",
            "ロイドったら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CD7")

    Jump("loc_1EE6")

    label("loc_1CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CF2")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E64")

    #C0023
    ChrTalk(
        0xA,
        (
            "#12600F日焼け止めを塗ってもらって\x01",
            "ありがたいんだけど……\x02\x03",

            "#12613Fや、やっぱり、\x01",
            "同僚のあなたに塗られるのは\x01",
            "ちょっと恥ずかしかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#12512Fは、はは。\x01",
            "俺も正直照れちゃってたよ。\x02\x03",

            "#12503F（それにしても……ゴクリ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        (
            "#12612F……あの、ロイド？\x01",
            "そんなにまじまじと\x01",
            "見ないで欲しいのだけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0026
    ChrTalk(
        0x101,
        "#12511Fゴ、ゴメン。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EE6")

    label("loc_1E64")


    #C0027
    ChrTalk(
        0xA,
        (
            "#12613F同僚のあなたに塗られるのは\x01",
            "ちょっと恥ずかしかったわ。\x02\x03",

            "#12611Fまあ、ランディとかに塗られるより\x01",
            "良かったとは思うけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EE6")

    TalkEnd(0xFE)
    Return()

    # Function_17_1BC7 end

    def Function_18_1EEA(): pass

    label("Function_18_1EEA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1F99")

    #C0028
    ChrTalk(
        0x8,
        (
            "#13305Fあらロイド、キーアちゃんたちと\x01",
            "何か探しているの？\x02\x03",

            "#13303Fホワイトストーン……？\x01",
            "うーん、この辺りでは見てないわね。\x01",
            "力になれなくてごめんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20E9")

    label("loc_1F99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FAF")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_1FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_208E")

    #C0029
    ChrTalk(
        0x8,
        (
            "#13304Fふふ、いい気持ちだったわ。\x01",
            "ありがとう、ロイド。\x02\x03",

            "#13309F……あ、そうだわ。\x01",
            "お返しに今度は私がロイドに\x01",
            "日焼け止めを塗ってあげようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#12512Fい、いいから！\x01",
            "セシル姉はゆっくり寝ててくれよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_20E9")

    label("loc_208E")


    #C0031
    ChrTalk(
        0x8,
        (
            "#13304F気持ちよくて、\x01",
            "このまま眠っちゃいそう。\x02\x03",

            "#13309Fふふ、何かあったら起こしてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E9")

    TalkEnd(0xFE)
    Return()

    # Function_18_1EEA end

    def Function_19_20ED(): pass

    label("Function_19_20ED")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2185")

    #C0032
    ChrTalk(
        0x9,
        (
            "#13505F白くて丸い、綺麗な石……？\x01",
            "いえ、見てませんね。\x02\x03",

            "#13503Fこの砂浜自体が白くて綺麗ですし、\x01",
            "探すとなると難しそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2336")

    label("loc_2185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_219B")
    TalkEnd(0xFE)
    Call(0, 40)
    Return()

    label("loc_219B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229C")

    #C0033
    ChrTalk(
        0x9,
        "#13508Fふう……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#12505F……リーシャ？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#13505Fあ、いえ、すみません。\x01",
            "ちょっと考え事をしてました。\x02\x03",

            "#13504Fえっと、ロイドさん。\x01",
            "ありがとうございました。\x02\x03",

            "#13502Fふふ、とりあえず、\x01",
            "これで日焼けの心配は\x01",
            "しなくてよさそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2336")

    label("loc_229C")


    #C0036
    ChrTalk(
        0x9,
        (
            "#13504Fとりあえず、\x01",
            "これで日焼けの心配は\x01",
            "しなくてよさそうですね。\x02\x03",

            "#13502Fイリアさんやシュリちゃんも\x01",
            "楽しんでるみたいですし……\x01",
            "ふふ、よかったです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2336")

    TalkEnd(0xFE)
    Return()

    # Function_19_20ED end

    def Function_20_233A(): pass

    label("Function_20_233A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23A6")

    #C0037
    ChrTalk(
        0x11,
        (
            "#12805Fん、白い石ころを探してるって？\x02\x03",

            "#12803F生憎だがこの辺りじゃ見てねえなあ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2456")

    label("loc_23A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23B5")
    Jump("loc_2456")

    label("loc_23B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C7")
    Call(0, 21)
    Jump("loc_2456")

    label("loc_23C7")


    #C0038
    ChrTalk(
        0x11,
        (
            "#12800Fサーフィンでもしてえとこだが、\x01",
            "ボードの貸し出しはしてない\x01",
            "らしいんだよな。\x02\x03",

            "#12806F女性陣にいいトコを見せる\x01",
            "チャンスなんだがなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2456")

    TalkEnd(0xFE)
    Return()

    # Function_20_233A end

    def Function_21_245A(): pass

    label("Function_21_245A")

    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)

    #C0039
    ChrTalk(
        0x12,
        (
            "#13002Fしばらく休憩したら、\x01",
            "また何か別のことをやりたいですね。\x02\x03",

            "#13004Fうーん、ビーチでの遊びって\x01",
            "他にどういうのがあったでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x11,
        (
            "#12800Fそうだな、ビーチの定番は\x01",
            "割とやりつくした感があるが……\x02\x03",

            "#12806F本当ならナンパにでも\x01",
            "洒落込みたいが、ビーチが貸切じゃ\x01",
            "お姉さんとの出会いもねえしよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x12,
        "#13006F先輩、ほんと相変わらずですねえ……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x10)
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 6)
    SetScenarioFlags(0x0, 5)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    Return()

    # Function_21_245A end

    def Function_22_25D5(): pass

    label("Function_22_25D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_266C")

    #C0042
    ChrTalk(
        0x12,
        (
            "#13000F何か探し物をしてるなら、\x01",
            "視点を変えてみると\x01",
            "いいかもしれませんね。\x02\x03",

            "#13003F意外と思わぬ所に\x01",
            "あったりするものですし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2715")

    label("loc_266C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267B")
    Jump("loc_2715")

    label("loc_267B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_268D")
    Call(0, 21)
    Jump("loc_2715")

    label("loc_268D")


    #C0043
    ChrTalk(
        0x12,
        (
            "#13003Fうーん、ビーチでの遊びって\x01",
            "他にどういうのがあったでしょう。\x02\x03",

            "#13000Fもっとこう、大人数で楽しめるのが\x01",
            "あればいいんですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2715")

    TalkEnd(0xFE)
    Return()

    # Function_22_25D5 end

    def Function_23_2719(): pass

    label("Function_23_2719")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2916")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2856")

    #C0044
    ChrTalk(
        0x13,
        (
            "#12900Fホワイトストーンか……\x01",
            "確か、ホワイトヘヴンの砂粒と\x01",
            "同じ材質の石だと聞いた事があるよ。\x02\x03",

            "#12904F長い年月をかけてほとんどの\x01",
            "ホワイトストーンは砂に変わるけど、\x01",
            "時々、綺麗に形が残る事があるそうだ。\x02\x03",

            "#12902Fフフ、大きな物が見つかったら\x01",
            "かなりラッキーだと思っていいだろうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2911")

    label("loc_2856")


    #C0045
    ChrTalk(
        0x13,
        (
            "#12904F長い年月をかけてほとんどの\x01",
            "ホワイトストーンは砂に変わるけど、\x01",
            "時々、綺麗に形が残る事があるそうだ。\x02\x03",

            "#12902Fフフ、大きな物が見つかったら\x01",
            "かなりラッキーだと思っていいだろうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2911")

    Jump("loc_2B8C")

    label("loc_2916")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2925")
    Jump("loc_2B8C")

    label("loc_2925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B04")

    #C0046
    ChrTalk(
        0x13,
        (
            "#12906Fやれやれ、慣れない遊びで\x01",
            "すっかり疲れちゃったよ。\x02\x03",

            "#12900F元来、体を動かす遊びは\x01",
            "あんまり得意じゃないんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#12503Fそれにしちゃ、\x01",
            "息一つ乱れてないみたいだが……\x02\x03",

            "#12502Fていうかルールとかにも\x01",
            "結構詳しかった気がするし、\x01",
            "実は結構得意なんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x13,
        (
            "#12904Fフフ、まさか。\x01",
            "僕は正真正銘の都会っ子だよ？\x02\x03",

            "#12900Fビーチバレーのルールだって、\x01",
            "暇つぶしに読んだ雑誌に\x01",
            "載ってたのを覚えてただけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        "#12503F（それはそれで凄い気がする……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_2B8C")

    label("loc_2B04")


    #C0050
    ChrTalk(
        0x13,
        (
            "#12906Fやれやれ、慣れない遊びで\x01",
            "すっかり疲れちゃったよ。\x02\x03",

            "#12909Fフフ、僕もエリィたちに混ざって\x01",
            "デッキチェアで優雅に過ごそうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B8C")

    TalkEnd(0xFE)
    Return()

    # Function_23_2719 end

    def Function_24_2B90(): pass

    label("Function_24_2B90")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D13")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C80")

    #C0051
    ChrTalk(
        0x10,
        (
            "#13400Fキーアちゃんはシュリと\x01",
            "遊んでくれてるみたいね？\x02\x03",

            "#13404Fふふ、あの子って\x01",
            "同年代の友達がいないから、\x01",
            "懐かれるのに慣れてないのよね。\x02\x03",

            "#13402F今日は色々と新しい面が見れるかも。\x01",
            "フフ、楽しみだわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2D0E")

    label("loc_2C80")


    #C0052
    ChrTalk(
        0x10,
        (
            "#13404Fシュリって同年代の友達がいないから、\x01",
            "懐かれるのに慣れてないのよね。\x02\x03",

            "#13402F今日は色々と新しい面が見れるかも。\x01",
            "フフ、楽しみだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D0E")

    Jump("loc_2F9F")

    label("loc_2D13")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D22")
    Jump("loc_2F9F")

    label("loc_2D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F0E")

    #C0053
    ChrTalk(
        0x10,
        (
            "#13409Fいやー、たまにはこんな\x01",
            "スポーツに励むのもいいわね。\x02\x03",

            "#13402F可愛い女の子たちの\x01",
            "水着姿も楽しめるし……\x01",
            "やっぱり来て良かったわ。\x02",
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
            "#12512Fイリアさんって、実は\x01",
            "アーティストの皮をかぶった\x01",
            "オジさんなんじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x10,
        (
            "#13406Fあら、失礼しちゃうわね。\x02\x03",

            "#13402Fフフン、そういう弟君も、\x01",
            "セシルやリーシャたちの\x01",
            "水着姿に釘付けなんじゃないの～？\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#12511Fノ、ノーコメントで。\x02\x03",

            "#12506F（というか、イリアさんの水着が\x01",
            "　一番すごい気がします……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2F9F")

    label("loc_2F0E")


    #C0057
    ChrTalk(
        0x10,
        (
            "#13404Fそういえば、練習以外で\x01",
            "こんなに体を動かしたのも\x01",
            "久しぶりかもしれないわね～。\x02\x03",

            "#13402Fうんうん、やっぱり\x01",
            "招待を受けて大正解だったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F9F")

    TalkEnd(0xFE)
    Return()

    # Function_24_2B90 end

    def Function_25_2FA3(): pass

    label("Function_25_2FA3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3042")

    #C0058
    ChrTalk(
        0xB,
        (
            "#12705Fホワイトストーン……\x01",
            "この砂浜にそんなものが？\x02\x03",

            "#12703F砂の城の土台に\x01",
            "この辺りの砂を使いましたが、\x01",
            "そんなものは見てませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_323C")

    label("loc_3042")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3058")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_3058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AF")

    #C0059
    ChrTalk(
        0xB,
        (
            "#12703F砂の素材でこれだけのものを\x01",
            "作れるなんて半信半疑でしたが……\x02\x03",

            "#12702F今ならむしろ、砂さえあれば\x01",
            "なんでも作れる気すらします。\x02\x03",

            "#12704Fふふ、今度はツァイトの\x01",
            "おうちを作ってあげるのも\x01",
            "いいかもしれませんね。\x02",
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
            "#12506F（ツァイトも、さすがに\x01",
            "  砂はイヤなんじゃ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xD,
        "#01203Fグルル……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_323C")

    label("loc_31AF")


    #C0062
    ChrTalk(
        0xB,
        (
            "#12704F今なら、砂さえあれば\x01",
            "なんでも作れる気すらします。\x02\x03",

            "#12702Fふふ、今度はツァイトの\x01",
            "おうちを作ってあげるのも\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_323C")

    TalkEnd(0xFE)
    Return()

    # Function_25_2FA3 end

    def Function_26_3240(): pass

    label("Function_26_3240")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32C1")

    #C0063
    ChrTalk(
        0xC,
        (
            "#13105Fあれ、何を探してるんですか～？\x02\x03",

            "#13103Fホワイトストーン……？\x01",
            "うーん、ちょっと分かりませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3402")

    label("loc_32C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32D7")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_32D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33B2")

    #C0064
    ChrTalk(
        0xC,
        (
            "#13109Fいや～、本当に立派な\x01",
            "お城が完成しましたね～！\x02\x03",

            "#13106Fカメラを持ってきていれば\x01",
            "写真に収めてたんですけど……\x01",
            "ぶー、残念です～。\x02\x03",

            "#13101Fせめて、心の感光クオーツに\x01",
            "しっかりと焼き付けないと！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_3402")

    label("loc_33B2")


    #C0065
    ChrTalk(
        0xC,
        (
            "#13101Fこのお城の姿、心の感光クオーツに\x01",
            "しっかりと焼き付けて帰りますよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3402")

    TalkEnd(0xFE)
    Return()

    # Function_26_3240 end

    def Function_27_3406(): pass

    label("Function_27_3406")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3435")

    #C0066
    ChrTalk(
        0xD,
        "#01200F……ウォン？\x02",
    )

    CloseMessageWindow()
    Jump("loc_346A")

    label("loc_3435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_344B")
    TalkEnd(0xFE)
    Call(0, 43)
    Return()

    label("loc_344B")


    #C0067
    ChrTalk(
        0xD,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()

    label("loc_346A")

    TalkEnd(0xFE)
    Return()

    # Function_27_3406 end

    def Function_28_346E(): pass

    label("Function_28_346E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_34F9")

    #C0068
    ChrTalk(
        0xE,
        (
            "#13210Fあ、ロイドー。\x01",
            "『ホワイトストーン』は\x01",
            "もう見つけたー？\x02\x03",

            "#13209Fえへへ、おっきいのが\x01",
            "どこかにないかなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_374A")

    label("loc_34F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350F")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_350F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 0)), scpexpr(EXPR_END)), "loc_36DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3648")

    #C0069
    ChrTalk(
        0xE,
        (
            "#13210Fこのホワイトストーン、\x01",
            "やっぱりおっきいー！\x02\x03",

            "#13209Fミシュラムでイチバンの\x01",
            "思い出ができちゃったかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#12509Fはは、来たばかりなのに\x01",
            "それは早いだろ。\x02\x03",

            "#12504Fでも、そんなに喜んでくれると\x01",
            "俺まで嬉しくなっちゃうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xE,
        (
            "#13209Fえへへ、ありがとーロイド。\x01",
            "大切にするね！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_36D7")

    label("loc_3648")


    #C0072
    ChrTalk(
        0xE,
        (
            "#13202Fえへへ、ミシュラムでイチバンの\x01",
            "思い出ができちゃったかも。\x02\x03",

            "#13209Fありがとー、ロイド。\x01",
            "この『ホワイトストーン』、\x01",
            "大切にするね！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36D7")

    Jump("loc_374A")

    label("loc_36DC")


    #C0073
    ChrTalk(
        0xE,
        (
            "#13209Fホワイトストーンを探すの、\x01",
            "楽しかったねー。\x02\x03",

            "#13204Fえへへ、後でツァイトにも\x01",
            "見せてあげよーっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_374A")

    TalkEnd(0xFE)
    Return()

    # Function_28_346E end

    def Function_29_374E(): pass

    label("Function_29_374E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A21")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_378A")
    Call(0, 30)
    Jump("loc_3A1C")

    label("loc_378A")

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
            "話す\x01",                          # 0
            "ホワイトストーンを見せる\x01",      # 1
            "やめる\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3800")
    Call(0, 30)
    Jump("loc_3A1C")

    label("loc_3800")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A0D")

    #C0074
    ChrTalk(
        0xF,
        (
            "#13605Fむっ……\x01",
            "『ホワイトストーン』を\x01",
            "見つけたみたいだな。\x02\x03",

            "#13600F早速オレたちの\x01",
            "『ホワイトストーン』と\x01",
            "大きさ比べをするか？\x02",
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
            "勝負を挑む\x01",          # 0
            "やっぱりやめる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399F")

    #C0075
    ChrTalk(
        0x101,
        "#12504Fああ、早速勝負を始めよう。\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xF,
        (
            "#13605Fふーん、自信満々だな。\x02\x03",

            "#13604Fそんじゃ、チビッコを呼んで来る。\x01",
            "フフン、あとで吠え面かくなよ？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    Call(0, 53)
    Return()

    label("loc_399F")


    #C0077
    ChrTalk(
        0x101,
        "#12500Fいや、もう少し待ってくれ。\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xF,
        (
            "#13606Fちぇっ、なんだよ。\x01",
            "男ならバーンと決めてみせろっての。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A1C")

    label("loc_3A0D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A1C")

    label("loc_3A1C")

    Jump("loc_3CA4")

    label("loc_3A21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A37")
    TalkEnd(0xFE)
    Call(0, 46)
    Return()

    label("loc_3A37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14E, 2)), scpexpr(EXPR_END)), "loc_3C11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BB5")

    #C0079
    ChrTalk(
        0xF,
        (
            "#13600Fあ、あのさ、えっと……\x01",
            "さっきはありがとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x101,
        (
            "#12500Fホワイトストーンのことか？\x01",
            "それなら気にしなくていいよ。\x02\x03",

            "#12509Fはは、今度アルカンシェルの\x01",
            "皆に見せてあげるといい。\x02",
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
            "#13611Fば、ばかっ……\x01",
            "そんな子供っぽいマネ\x01",
            "できるかっつーの！\x02\x03",

            "#13606F常識で考えろよ、まったく……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#12506F（年頃の女の子は難しいな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3C0C")

    label("loc_3BB5")


    #C0083
    ChrTalk(
        0xF,
        (
            "#13603Fホワイトストーンのことは\x01",
            "ありがとな。\x02\x03",

            "#13608F……フ、フン、それだけだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0C")

    Jump("loc_3CA4")

    label("loc_3C11")


    #C0084
    ChrTalk(
        0xF,
        (
            "#13603F石ころ探しもいいけど……\x01",
            "ビーチに来たんだし、\x01",
            "ちゃんと泳ぎたいんだよな。\x02\x03",

            "#13602Fせっかくだからリーシャ姉より\x01",
            "上手くなれたらいいな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3CA4")

    TalkEnd(0xFE)
    Return()

    # Function_29_374E end

    def Function_30_3CA8(): pass

    label("Function_30_3CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D77")

    #C0085
    ChrTalk(
        0xF,
        (
            "#13600F『ホワイトストーン』を\x01",
            "見つけたら、オレに教えてくれ。\x02\x03",

            "最後に大きさを比べっこして、\x01",
            "一番大きいのを持ってた奴が勝ちな。\x02\x03",

            "#13604Fま、オレがおまえらなんかに\x01",
            "負けるわけないけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3DF9")

    label("loc_3D77")


    #C0086
    ChrTalk(
        0xF,
        (
            "#13600F誰の『ホワイトストーン』が\x01",
            "一番大きいか、後で勝負だからな。\x02\x03",

            "#13604Fま、オレがおまえらなんかに\x01",
            "負けるわけないけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DF9")

    Return()

    # Function_30_3CA8 end

    def Function_31_3DFA(): pass

    label("Function_31_3DFA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_3E0B")
    Jump("loc_4217")

    label("loc_3E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_4217")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x188, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4207")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E7B")

    #C0087
    ChrTalk(
        0x101,
        (
            "#12500Fあれ、この黒猫……\x01",
            "どこかで見かけた気がするな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "にゃあ～……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E8D")

    label("loc_3E7B")


    #C0089
    ChrTalk(
        0xFE,
        "にゃあ～……\x02",
    )

    CloseMessageWindow()

    label("loc_3E8D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D9, 0x0)"), scpexpr(EXPR_END)), "loc_40C6")

    #C0090
    ChrTalk(
        0x101,
        (
            "#12505F……もしかして\x01",
            "お腹が減っているのかな？\x02",
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
            "『ねこまんま』をあげる\x01",      # 0
            "やめる\x01",                      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40B2")

    #C0091
    ChrTalk(
        0x101,
        "#12500Fよかったら食べな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあげた。\x02",
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
        "にゃにやゃゃあ～㈱\x02",
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        "がつがつ……\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        "#12509Fはは、そんなにお腹が減ってたのか？\x02",
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 1700, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0096
    ChrTalk(
        0xFE,
        "にゃおん㈱\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x2F3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x2F3, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0098
    ChrTalk(
        0x101,
        (
            "#12505Fえっ……この本をくれるのか？\x02\x03",

            "#12500Fはは、ありがとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x188, 5)
    SubItemNumber(0x1D9, 1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_40C1")

    label("loc_40B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_40C1")

    label("loc_40C1")

    Jump("loc_41FF")

    label("loc_40C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4179")

    #C0099
    ChrTalk(
        0x101,
        (
            "#12505F……もしかして\x01",
            "お腹が減っているのかな。\x02\x03",

            "#12503F『ねこまんま』を持ってたら\x01",
            "あげてもよかったんだけど……\x02\x03",

            "#12512Fあいにく今は持ってないんだ。\x01",
            "ごめんな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41ED")

    label("loc_4179")


    #C0100
    ChrTalk(
        0x101,
        (
            "#12503F『ねこまんま』を持ってたら\x01",
            "あげてもよかったんだけど……\x02\x03",

            "#12512Fあいにく今は持ってないんだ。\x01",
            "ごめんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41ED")


    #C0101
    ChrTalk(
        0xFE,
        "にゃおん……\x02",
    )

    CloseMessageWindow()

    label("loc_41FF")

    SetScenarioFlags(0x1, 6)
    Jump("loc_4217")

    label("loc_4207")


    #C0102
    ChrTalk(
        0xFE,
        "にゃおん㈱\x02",
    )

    CloseMessageWindow()

    label("loc_4217")

    TalkEnd(0xFE)
    Return()

    # Function_31_3DFA end

    def Function_32_421B(): pass

    label("Function_32_421B")

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
            "　　　湖水浴を楽しむ際のご注意\x01",
            "──────────────────\x01",
            "・必ず準備運動をして下さい。\x01",
            "・服を着たまま水に入らないで下さい。\x01",
            "  （水着は受付で貸し出しています）\x01",
            "・監視員の指示に従ってください。\x01",
            "──────────────────\x01",
            "  マナーを守って楽しく遊びましょう。\x01",
            "  　　　　　──ミシュラム事業部より\x07\x00\x02",
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

    # Function_32_421B end

    def Function_33_4390(): pass

    label("Function_33_4390")

    EventBegin(0x1)

    #C0104
    ChrTalk(
        0x101,
        (
            "#12500Fおっと……\x01",
            "こっちは建物の中だな。\x02\x03",

            "せっかくマリアベルさんが\x01",
            "貸切にしてくれたんだ。\x01",
            "今はレイクビーチを楽しもう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -10330, -2000, -920, 90)
    EventEnd(0x4)
    Return()

    # Function_33_4390 end

    def Function_34_4423(): pass

    label("Function_34_4423")

    EventBegin(0x1)

    #C0105
    ChrTalk(
        0x101,
        (
            "#12500F『ホワイトストーン』は\x01",
            "浜辺のどこかにあるはずだ。\x01",
            "もう少し探してみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11580, -5080, -120, 90)
    EventEnd(0x4)
    Return()

    # Function_34_4423 end

    def Function_35_448F(): pass

    label("Function_35_448F")

    EventBegin(0x1)

    #C0106
    ChrTalk(
        0x101,
        (
            "#12500F『ホワイトストーン』は\x01",
            "浜辺のどこかにあるはずだ。\x01",
            "もう少し探してみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 11210, -4940, 46030, 90)
    EventEnd(0x4)
    Return()

    # Function_35_448F end

    def Function_36_44FB(): pass

    label("Function_36_44FB")

    EventBegin(0x1)

    #C0107
    ChrTalk(
        0x101,
        (
            "#12500Fおっと……ビーチバレーの\x01",
            "邪魔にならないように探そう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 32500, -6000, -13500, 90)
    EventEnd(0x5)
    Return()

    # Function_36_44FB end

    def Function_37_4554(): pass

    label("Function_37_4554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4566")
    Call(0, 36)
    Return()

    label("loc_4566")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BF4")
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
        "#13400F#11P──よし♪\x02",
    )

    CloseMessageWindow()

    def lambda_46C0():
        TurnDirection(0x13, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_46C0)
    Sleep(50)

    def lambda_46D0():
        TurnDirection(0x11, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_46D0)
    Sleep(50)

    def lambda_46E0():
        TurnDirection(0x12, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_46E0)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    #C0109
    ChrTalk(
        0x11,
        "#12809F#5Pくうう、流石ッスね……！！\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x12,
        "#13006F#6Pボールが見えませんでした……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x10, 500)

    #C0111
    ChrTalk(
        0x13,
        (
            "#12902F#12Pフフ、全身のバネを使った\x01",
            "申し分ないスパイクだったね。\x02\x03",

            "#12904Fさすがはイリア・プラティエと\x01",
            "言ったところかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10, 0x13, 500)

    #C0112
    ChrTalk(
        0x10,
        "#13409F#5Pフフ、どういたしまして♪\x02",
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
        "#12505F#6Pす、すごい……！！\x02",
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

    def lambda_48B0():
        TurnDirection(0x10, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_48B0)
    Sleep(50)

    def lambda_48C0():
        TurnDirection(0x13, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_48C0)
    Sleep(50)

    def lambda_48D0():
        TurnDirection(0x11, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_48D0)
    Sleep(50)

    def lambda_48E0():
        TurnDirection(0x12, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_48E0)
    Sleep(50)
    WaitChrThread(0x10, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x12, 0)

    #C0114
    ChrTalk(
        0x10,
        (
            "#13400F#11Pああ弟君、見てたんだ？\x02\x03",

            "#13409Fフフ、あたしの必殺技は\x01",
            "どうだった？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#12512F#6Pは、はい……\x01",
            "本当に凄かったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x11,
        (
            "#12802F#5Pいや、マジで恐れ入ったッス。\x02\x03",

            "#12804F俺のスパイクも\x01",
            "難なくレシーブされちまうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x12,
        (
            "#13000F#5Pワジ君も、ここしかないって所に\x01",
            "トスしてイリアさんをアシストしてたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x13,
        (
            "#12900F#11Pフフ、僕のはただのまぐれさ。\x01",
            "それに君たちもなかなかの\x01",
            "コンビネーションだったじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#12504F#6Pいや……正直、\x01",
            "みんなハイレベルすぎて\x01",
            "言葉も出ないくらいだよ。\x02\x03",

            "#12500Fこの面子で大会なんかに出たら、\x01",
            "すぐにでも優勝を狙えるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x10,
        (
            "#13404F#11Pフフ、まあ現実はそんな\x01",
            "簡単にはいかないでしょうけど、\x01",
            "いいトコいくかもしれないわね。\x02\x03",

            "#13409Fそうだ、次のゲームは弟君も混ざらない？\x01",
            "一緒にビーチバレーを楽しみましょ♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15D, 2)
    Jump("loc_4D0A")

    label("loc_4BF4")

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
            "#13400F#11Pせっかくだし、\x01",
            "次のゲームは弟君も混ざらない？\x02\x03",

            "#13409F一緒にビーチバレーを楽しみましょ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D0A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ビーチバレーに参加する\x01",      # 0
            "やめておく\x01",                  # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58C1")

    #C0122
    ChrTalk(
        0x101,
        (
            "#12500F#6Pそれじゃあ、お言葉に甘えて\x01",
            "参加させてもらいます。\x02\x03",

            "#12506Fと言っても、ビーチバレーのルールは\x01",
            "あまり詳しくないんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x12,
        (
            "#13000F基本は普通のバレーボールと同じですよ。\x02\x03",

            "#13004F違いを大雑把に言うなら、\x01",
            "チームが二人一組だってことと\x01",
            "砂浜でやるって所くらいですかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x13,
        (
            "#12900Fあと、実際は先に２１点取って\x01",
            "ようやく１セット勝利になるんだけど……\x02\x03",

            "今回は気軽に楽しもうってことで、\x01",
            "１ゲーム１２点先取の変則マッチでやってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x101,
        (
            "#12500F#6Pふむ、なるほど……\x01",
            "ひとまず問題はなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x11,
        (
            "#12802F#5Pまあ、細かい話は置いといて\x01",
            "早速チーム分けと行こうじゃねえか。\x02\x03",

            "#12806Fロイドが入るなら、誰か１人抜けて\x01",
            "審判に回らなきゃならねえしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x101,
        (
            "#12505F#6Pあ、そうか……\x01",
            "なんだか邪魔しちゃったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x10,
        (
            "#13409F#11Pあはは、別にいいわよ。\x02\x03",

            "#13400Fそれじゃ弟君、チームを組みたい\x01",
            "パートナーを選んでくれるかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#12500F#6P分かりました、じゃあ……\x02",
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
            "#1K誰とチームを組む？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ランディ\x01",      # 0
            "ノエル\x01",        # 1
            "ワジ\x01",          # 2
            "イリア\x01",        # 3
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
        (0, "loc_5161"),
        (1, "loc_5328"),
        (2, "loc_5504"),
        (3, "loc_56D3"),
        (SWITCH_DEFAULT, "loc_58A2"),
    )


    label("loc_5161")


    #C0131
    ChrTalk(
        0x101,
        "#12500F#6Pランディ、よろしく頼む。\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x11,
        "#12800F#5Pよっしゃ、任せとけ！\x02",
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x12,
        (
            "#13004F#5Pそれじゃあ、残りのチームと\x01",
            "審判に回る人も決めましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x13,
        (
            "#12900Fまあ、こっちは公平に\x01",
            "ジャンケンでいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x10,
        (
            "#13409F#11Pフフ、了解。\x01",
            "さっさと決めちゃいましょ。\x02",
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
            "ジャンケンの結果\x01",
            "審判にはイリアが回り……\x07\x00\x02",
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
            "ロイド・ランディチームと\x01",
            "ワジ・ノエルチームの対戦が\x01",
            "幕を開けるのだった。\x07\x00\x02",
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
            "そして──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 3)
    Call(1, 9)
    Jump("loc_58A2")

    label("loc_5328")


    #C0139
    ChrTalk(
        0x101,
        "#12500F#6Pノエル、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x12,
        (
            "#13000F#5P分かりました！\x01",
            "頑張りましょう、ロイドさん！\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x13,
        (
            "#12904Fそれじゃ、残りのチームと\x01",
            "審判に回る人も決めようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x10,
        (
            "#13400F#11Pまあ、こっちは公平に\x01",
            "ジャンケンでいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x11,
        (
            "#12809F#5Pそうッスね、\x01",
            "さっさと決めちまいましょう！\x02",
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
            "ジャンケンの結果\x01",
            "審判にはランディが回り……\x07\x00\x02",
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
            "ロイド・ノエルチームと\x01",
            "イリア・ワジチームの対戦が\x01",
            "幕を開けるのだった。\x07\x00\x02",
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
            "そして──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 4)
    Call(1, 24)
    Jump("loc_58A2")

    label("loc_5504")


    #C0147
    ChrTalk(
        0x101,
        "#12500F#6Pワジ、よろしく頼む。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x13,
        "#12900Fフフ、お安い御用さ。\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x10,
        (
            "#13404F#11Pそれじゃ、残りのチームと\x01",
            "審判に回る人も決めましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x11,
        (
            "#12800F#5Pまあ、こっちは公平に\x01",
            "ジャンケンでいいんじゃないッスか？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x12,
        (
            "#13009F#5Pそうですね、ぱぱっと決めて\x01",
            "ゲームを始めましょう！\x02",
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
            "ジャンケンの結果\x01",
            "審判にはノエルが回り……\x07\x00\x02",
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
            "ロイド・ワジチームと\x01",
            "イリア・ランディチームの対戦が\x01",
            "幕を開けるのだった。\x07\x00\x02",
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
            "そして──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 5)
    Call(1, 49)
    Jump("loc_58A2")

    label("loc_56D3")


    #C0155
    ChrTalk(
        0x101,
        "#12500F#6Pイリアさん、お願いします。\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x10,
        "#13400F#11Pオッケー、よろしくね！\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x11,
        (
            "#12804F#5Pそれじゃ、残りのチームと\x01",
            "審判に回る人も決めちまうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x12,
        (
            "#13000F#5Pまあ、こっちは公平に\x01",
            "ジャンケンでよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x13,
        (
            "#12902Fフフ、だね。\x01",
            "ま、早いところ決めるとしようか。\x02",
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
            "ジャンケンの結果\x01",
            "審判にはワジが回り……\x07\x00\x02",
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
            "ロイド・イリアチームと\x01",
            "ランディ・ノエルチームの対戦が\x01",
            "幕を開けるのだった。\x07\x00\x02",
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
            "そして──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15D, 6)
    Call(1, 69)
    Jump("loc_58A2")

    label("loc_58A2")

    Call(0, 38)
    Call(0, 39)
    Call(0, 45)
    SetChrPos(0x0, 20000, -6000, -15000, 0)
    Jump("loc_5A2F")

    label("loc_58C1")


    #C0163
    ChrTalk(
        0x101,
        "#12500F#6Pえっと、ちょっと今は……\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x10,
        (
            "#13405F#11Pあら、そう？\x01",
            "まあ無理にとは言わないけど。\x02\x03",

            "#13400Fそれじゃ、参加したくなったら\x01",
            "いつでも声をかけてちょうだいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A1E")
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

    label("loc_5A1E")

    SetChrPos(0x0, 32500, -6000, -13500, 90)

    label("loc_5A2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5A47")
    Call(0, 54)

    label("loc_5A47")

    EventEnd(0x5)
    Return()

    # Function_37_4554 end

    def Function_38_5A4A(): pass

    label("Function_38_5A4A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_5DF6")
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
            "#12809F#6Pはは、なかなか\x01",
            "いい勝負だったんじゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x13,
        "#12902Fフフ、確かに悪くなかったかな。\x02",
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
            "#13401F#5Pむ～、ズルい！\x01",
            "みんなだけで楽しんじゃって。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5C27():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C27)
    Sleep(50)

    def lambda_5C37():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_5C37)
    Sleep(50)

    def lambda_5C47():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5C47)
    Sleep(50)

    def lambda_5C57():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5C57)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    #C0168
    ChrTalk(
        0x12,
        "#13005F#11Pえっ……？\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x10,
        (
            "#13406F#5Pやっぱりあんな楽しそうな勝負、\x01",
            "見てるだけじゃ物足りないわ！\x02\x03",

            "#13409Fね、次は私も混ぜて\x01",
            "もう１ゲームやりましょ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#12500F#6Pはは、それじゃあ今度は\x01",
            "別のチームに分かれてやりましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x11,
        (
            "#12809F#12Pハハ、いいんじゃねえか。\x02\x03",

            "#12800Fそれじゃあロイド、\x01",
            "次にチームを組みたい\x01",
            "パートナーを選んでくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0172
    ChrTalk(
        0x101,
        "#12500F#5Pああ、そうだな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_685B")

    label("loc_5DF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_614D")
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
        "#13009F#6Pはあ～……熱い勝負でしたね！\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x10,
        "#13409F#11Pうんうん、いい汗かいちゃった。\x02",
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
            "#12806F#5Pむう……ロイドが入ったとたん\x01",
            "なんだか白熱してきやがったな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5F6F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5F6F)
    Sleep(50)

    def lambda_5F7F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_5F7F)
    Sleep(50)

    def lambda_5F8F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_5F8F)
    Sleep(50)

    def lambda_5F9F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_5F9F)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x13, 2)

    #C0176
    ChrTalk(
        0x13,
        "#12905F#12Pん、どうかしたかい？\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x11,
        (
            "#12803F#5Pいや、やっぱり俺だけ\x01",
            "見てるだけってのも\x01",
            "不公平な話だろうが？\x02\x03",

            "#12800F今度は俺も混ぜてくれ。\x01",
            "んで、もう１ゲームやろうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x101,
        (
            "#12500F#6Pああ、それじゃあ今度は\x01",
            "別のチームに分かれてやろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x12,
        (
            "#13009F#12Pええ、よさそうですね。\x02\x03",

            "#13000Fそれではロイドさん、\x01",
            "次にチームを組みたい\x01",
            "パートナーを選んでください！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0180
    ChrTalk(
        0x101,
        "#12500F#5Pああ、そうだな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_685B")

    label("loc_614D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_6489")
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
        "#12902F#6Pフフ、なかなか楽しかったよ。\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x11,
        "#12809F#11Pああ、結構いい勝負だったよな。\x02",
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
            "#13001F#5P……あの、みなさんっ！\x01",
            "できたらもう１ゲームやりませんか！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_62C3():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_62C3)
    Sleep(50)

    def lambda_62D3():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_62D3)
    Sleep(50)

    def lambda_62E3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_62E3)
    Sleep(50)

    def lambda_62F3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_62F3)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x10, 2)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x13, 2)

    #C0184
    ChrTalk(
        0x10,
        "#13405F#11Pあら……？\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x12,
        (
            "#13006F#5Pその、先ほどのゲームをみていたら\x01",
            "どうにも抑えきれなくなって……\x02\x03",

            "#13002F今度は是非、私も入れてください！\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#12500F#6Pああ、それじゃあ今度は\x01",
            "別のチームに分かれてやろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x13,
        "#12904F#12Pフフ、僕も構わないよ。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x13,
        (
            "#12902F#12Pそれじゃあロイド、\x01",
            "次にチームを組みたい\x01",
            "パートナーを選ぶといい。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)

    #C0189
    ChrTalk(
        0x101,
        "#12500F#5Pああ、そうだな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_685B")

    label("loc_6489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_685B")
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
        "#13409F#6Pいや～、なかなか燃えたわね！\x02",
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x12,
        "#13009F#11Pはい、とっても楽しかったです！\x02",
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
            "#12900F#5Pフフ、それじゃあこんな所で\x01",
            "お開きってところかな？\x02\x03",

            "#12904F僕もそろそろ喉が渇いたし。\x02",
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
            "#12504F#12Pいや……せっかくだから\x01",
            "もう１ゲームしないか？\x02\x03",

            "#12500F今度はワジも混ざってさ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_667E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_667E)
    Sleep(50)

    def lambda_668E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_668E)
    Sleep(50)

    def lambda_669E():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_669E)
    WaitChrThread(0x11, 2)
    WaitChrThread(0x12, 2)
    WaitChrThread(0x10, 2)

    #C0194
    ChrTalk(
        0x11,
        (
            "#12800F#11Pおお、それはよさそうじゃねえか。\x01",
            "ワジも審判じゃヒマだったろ？\x02",
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
            "#12906F#5Pいや、別に僕はどっちでも\x01",
            "いいって感じなんだけど……\x02\x03",

            "#12900F……フフ、まあ仕方ない。\x01",
            "君たちがノリノリなら\x01",
            "付き合ってあげてもいいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x10,
        (
            "#13409F#12Pフフ、話は決まったわね。\x02\x03",

            "#13400Fそれじゃあ弟君、\x01",
            "次にチームを組みたい\x01",
            "パートナーを選ぶといいわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0197
    ChrTalk(
        0x101,
        (
            "#12500F#6Pええ、分かりました。\x01",
            "それじゃあ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_685B")

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
            "#1K誰とチームを組む？\x07\x00\x02",
        )
    )

    MenuCmd(0, 0)
    MenuCmd(1, 0, "ランディ")
    MenuCmd(1, 0, "ノエル")
    MenuCmd(1, 0, "ワジ")
    MenuCmd(1, 0, "イリア")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 3)), scpexpr(EXPR_END)), "loc_68C9")
    MenuCmd(3, 0, 0x0)

    label("loc_68C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 4)), scpexpr(EXPR_END)), "loc_68D6")
    MenuCmd(3, 0, 0x1)

    label("loc_68D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 5)), scpexpr(EXPR_END)), "loc_68E3")
    MenuCmd(3, 0, 0x2)

    label("loc_68E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 6)), scpexpr(EXPR_END)), "loc_68F0")
    MenuCmd(3, 0, 0x3)

    label("loc_68F0")

    MenuCmd(2, 0, -1, 85, 0)
    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6935"),
        (1, "loc_6A6D"),
        (2, "loc_6BBA"),
        (3, "loc_6CEC"),
        (SWITCH_DEFAULT, "loc_6E2E"),
    )


    label("loc_6935")

    TurnDirection(0x101, 0x11, 500)

    #C0199
    ChrTalk(
        0x101,
        (
            "#12500F#6P#Nそれじゃあ、今度はランディ。\x01",
            "よろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x11, 0x101, 500)

    #C0200
    ChrTalk(
        0x11,
        "#12809F#5P#Nよっしゃ、任せとけ！\x02",
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
            "再び行われたジャンケンで\x01",
            "２ゲーム目の審判には\x01",
            "イリアが選ばれ……\x07\x00\x02",
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
            "ロイド・ランディチームと\x01",
            "ワジ・ノエルチームの対戦が\x01",
            "続けて行われる事になった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 9)
    Jump("loc_6E2E")

    label("loc_6A6D")

    TurnDirection(0x101, 0x12, 500)

    #C0203
    ChrTalk(
        0x101,
        (
            "#12500F#6P#Nそれじゃあ、今度はノエル。\x01",
            "よろしく頼むよ。\x02",
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
            "#13009F#5P#N分かりました！\x01",
            "頑張りましょう、ロイドさん！\x02",
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
            "再び行われたジャンケンで\x01",
            "２ゲーム目の審判には\x01",
            "ランディが選ばれ……\x07\x00\x02",
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
            "ロイド・ノエルチームと\x01",
            "イリア・ワジチームの対戦が\x01",
            "続けて行われる事になった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 24)
    Jump("loc_6E2E")

    label("loc_6BBA")

    TurnDirection(0x101, 0x13, 500)

    #C0207
    ChrTalk(
        0x101,
        (
            "#12500F#6P#Nそれじゃあ、今度はワジ。\x01",
            "よろしく頼む。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x13, 0x101, 500)

    #C0208
    ChrTalk(
        0x13,
        "#12902F#5P#Nフフ、お安い御用さ。\x02",
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
            "再び行われたジャンケンで\x01",
            "２ゲーム目の審判には\x01",
            "ノエルが選ばれ……\x07\x00\x02",
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
            "ロイド・ワジチームと\x01",
            "イリア・ランディチームの対戦が\x01",
            "続けて行われる事になった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 49)
    Jump("loc_6E2E")

    label("loc_6CEC")

    TurnDirection(0x101, 0x10, 500)

    #C0211
    ChrTalk(
        0x101,
        (
            "#12500F#6P#Nそれじゃあ、今度はイリアさん。\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x10, 0x101, 500)

    #C0212
    ChrTalk(
        0x10,
        "#13409F#5P#Nオッケー、よろしくね！\x02",
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
            "再び行われたジャンケンで\x01",
            "２ゲーム目の審判には\x01",
            "ワジが選ばれ……\x07\x00\x02",
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
            "ロイド・イリアチームと\x01",
            "ランディ・ノエルチームの対戦が\x01",
            "続けて行われる事になった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Call(1, 69)
    Jump("loc_6E2E")

    label("loc_6E2E")

    Return()

    # Function_38_5A4A end

    def Function_39_6E2F(): pass

    label("Function_39_6E2F")

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
            "#6P#13409F……いやー、楽しかったわね！\x02\x03",

            "#13400F弟君が入ったおかげで\x01",
            "チーム分けも色々楽しめたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x101,
        (
            "#12500Fはは、２ゲーム連続は\x01",
            "結構キツかったですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x11,
        (
            "#6P#12803Fああ、それに……\x02\x03",

            "#12809Fお約束のサービスシーンが\x01",
            "なかったのは残念極まりねえぜ。\x02\x03",

            "#12806Fノエルあたりが\x01",
            "かましてくれることを\x01",
            "期待してたんだがなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x10,
        "#6P#13405Fああ、確かにっ！！\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x13,
        (
            "#6P#12904Fフフ、ついついビーチバレーに\x01",
            "熱中しちゃってたね。\x02",
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
            "#6P#13006Fせ、先輩にワジ君……\x01",
            "なに言ってるんですか、もう。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x101,
        (
            "#12512Fイリアさんの過剰反応も\x01",
            "気になるんですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0222
    ChrTalk(
        0x101,
        (
            "#12500Fああそうだ、皆。\x01",
            "喉とか渇いてないか？\x02\x03",

            "何だったら、俺が売店で\x01",
            "冷たいものとか買ってくるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x10,
        (
            "#6P#13400Fおっと、気が利くわね弟君。\x01",
            "ん～、なにがいいかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x11,
        (
            "#6P#12800F確か、聞いた所によると\x01",
            "ミシュラムに新しく発売した\x01",
            "ジュースがあるみたいッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x12,
        (
            "#6P#13000Fああ、それはあたしも\x01",
            "聞いた事があります。\x02\x03",

            "#13004F『ベルコーラ』っていって、\x01",
            "シュワシュワして爽快な\x01",
            "飲み物らしいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x13,
        (
            "#6P#12902Fフフ、それは\x01",
            "なかなか良さそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x101,
        (
            "#12500Fそれじゃあ、\x01",
            "みんな『ベルコーラ』でいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x10,
        (
            "#6P#13400Fうん、よろしくお願いするわね。\x02\x03",

            "#13404Fまあ、今はそこまで\x01",
            "喉が渇いてるわけじゃないから\x01",
            "急がなくてもいいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#12500Fはは、分かりました。\x01",
            "それじゃあまた後で持ってきますよ。\x02",
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

    # Function_39_6E2F end

    def Function_40_7505(): pass

    label("Function_40_7505")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8080")

    #C0230
    ChrTalk(
        0x8,
        "#5P#13302Fあら、ロイドじゃない。\x02",
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x9,
        "#11P#13502Fふふ、お疲れ様です。\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#12P#12504Fセシル姉たちは日光浴か。\x02\x03",

            "#12500F湖にはまだ入ってないみたいだけど、\x01",
            "ちゃんと楽しんでるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x8,
        (
            "#5P#13304Fええ、ここでゆっくりするだけでも\x01",
            "充分楽しませてもらってるわ。\x02\x03",

            "#13309Fエリィさんやリーシャさんとも\x01",
            "色々とおしゃべりできるし。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0xA,
        (
            "#12602Fあはは、私たちも\x01",
            "それは楽しいんですけど……\x01",
            "たまにちょっと困っちゃいますよ。\x02\x03",

            "#12606Fセシルさんったら、さっきから\x01",
            "『ロイドとの仲はどう？』とか、\x01",
            "そんなことばっかり聞くんですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x9,
        (
            "#11P#13509Fえ、ええ……\x01",
            "ちょっとびっくりしちゃいました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0236
    ChrTalk(
        0x101,
        "#12P#12506Fあ、あのなあセシル姉……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x8,
        (
            "#5P#13309Fふふ、だって気になるじゃない？\x02\x03",

            "姉たるもの、弟の交友関係は\x01",
            "常にチェックしておかないとね。\x02\x03",

            "#13301Fそして誰が将来のお嫁さんになるか、\x01",
            "バッチリ当たりをつけておかないと！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x101,
        (
            "#12P#12506Fい、いやいや。\x01",
            "そういうのはいいから！\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x9,
        (
            "#11P#13500F（う～ん、さすがイリアさんの\x01",
            "  幼馴染の方だけはありますね……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0240
    ChrTalk(
        0x8,
        (
            "#5P#13302Fそうだ、ロイド。\x01",
            "せっかくだしあなたも\x01",
            "日光浴していかない？\x02\x03",

            "#13309Fデッキチェアにも空きがあるし、\x01",
            "色々とお話しましょうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#12P#12512Fい、いや～……\x01",
            "さすがにこの輪に入るのは\x01",
            "ちょっと恥ずかしいというか……\x02\x03",

            "#12500F今回は遠慮させてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x8,
        "#5P#13305Fあら、そう？\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xA,
        (
            "#12600Fふふ、今更恥ずかしがる\x01",
            "ことなんてないでしょうに。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x9,
        (
            "#11P#13503Fええ、そうですよ。\x01",
            "私も色々お話してみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x101,
        (
            "#12P#12502Fはは、そう言ってくれるのは\x01",
            "ありがたいんだけど……\x02",
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
            "#5P#13303Fうーん……それじゃあ……\x02\x03",

            "#13309Fその代わりに、\x01",
            "私たちに日焼け止めを\x01",
            "塗ってくれないかしら？\x02",
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
        "#12P#12505Fえ……………………\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0xC8, 0xBB8, 0x1F4)

    #C0248
    ChrTalk(
        0x101,
        "#12P#12511F#4Sええええええええっ！？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xA,
        "#12605Fちょ、ちょっとセシルさん！？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x9,
        "#11P#13506Fさ、さすがにそれはちょっと……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x8,
        (
            "#5P#13302Fふふ、いいじゃない。\x01",
            "私は全然問題ないわよ？\x02\x03",

            "#13304Fエリィさんもリーシャさんも、\x01",
            "なるべく日焼けは避けたいって\x01",
            "さっき言ってたじゃない？\x02\x03",

            "#13309Fそれに『今更恥ずかしがる\x01",
            "ことなんてない』って、\x01",
            "エリィさんも言ってたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xA,
        "#12605Fそ、それはその……\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0253
    ChrTalk(
        0xA,
        (
            "#12607Fわ、分かりました！\x02\x03",

            "#12613Fそれじゃあ……\x01",
            "ロイド、お願いするわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 500)

    #C0254
    ChrTalk(
        0x101,
        "#12P#12505Fエ、エリィ……？\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xA,
        (
            "#12611Fだ、だって他のみんなは\x01",
            "それぞれ自分の遊びに夢中じゃない？\x02\x03",

            "#12606Fなるべく日焼けを避けたいのは\x01",
            "本当の話だし……\x02\x03",

            "#12613Fランディとかに塗られるよりは\x01",
            "あなたのほうがいいかと思って。\x02",
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
            "#11P#13503Fそ……そうですね。\x02\x03",

            "#13506Fイリアさんも、ホテルの部屋で\x01",
            "私が日焼け止めを塗りましたし……\x02\x03",

            "#13502Fその、ロイドさんなら\x01",
            "そこまで抵抗はないかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x9, 500)

    #C0257
    ChrTalk(
        0x101,
        "#12P#12511Fリ、リーシャまで！？\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x8,
        (
            "#5P#13304Fふふ、ほらロイド。\x01",
            "お姉ちゃんとこんな可愛い子達が\x01",
            "せっかく頼んでるんだから。\x02\x03",

            "#13302F日焼け止め、塗ってくれるわよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    SetScenarioFlags(0x15D, 0)
    Jump("loc_80C4")

    label("loc_8080")


    #C0259
    ChrTalk(
        0x8,
        (
            "#5P#13302Fあら、ロイド。\x01",
            "私たちに日焼け止めを\x01",
            "塗ってくれるの？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_80C4")

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
            "セシルたちに日焼け止めを塗る\x01",      # 0
            "やめておく\x01",                        # 1
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
        (0, "loc_813C"),
        (1, "loc_8144"),
        (SWITCH_DEFAULT, "loc_8231"),
    )


    label("loc_813C")

    Call(0, 41)
    Jump("loc_8231")

    label("loc_8144")


    #C0260
    ChrTalk(
        0x101,
        (
            "#12P#12511Fそ、その、ちょっと待ってくれ。\x01",
            "心の準備がっ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x8,
        (
            "#5P#13302Fあら……ふふ、仕方ないわね。\x01",
            "なら後でいらっしゃい。\x02\x03",

            "#13304Fでも、なるべく急いでね。\x01",
            "このままじゃ日焼けしちゃうから。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 21500, -6000, 20700, 90)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    ClearMapObjFlags(0x1, 0x1000)
    EventEnd(0x5)
    Jump("loc_8231")

    label("loc_8231")

    Return()

    # Function_40_7505 end

    def Function_41_8232(): pass

    label("Function_41_8232")

    EventBegin(0x0)

    #C0262
    ChrTalk(
        0x101,
        (
            "#12P#12501Fわ、分かったよ……\x01",
            "謹んで、塗らせてもらうから！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xA,
        "#12611F謹んでって……\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x9,
        (
            "#11P#13509Fあはは……テンションが\x01",
            "なんだか変になってますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x8,
        (
            "#5P#13300Fふふ、じゃあさっそく\x01",
            "お願いしちゃいましょう。\x02\x03",

            "#13303F最初は誰に塗ってくれるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        "#12P#12506Fえ、えっと……\x02",
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
            "#1K誰から日焼け止めを塗る？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "エリィから塗る\x01",        # 0
            "セシルから塗る\x01",        # 1
            "リーシャから塗る\x01",      # 2
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
        (0, "loc_83FB"),
        (1, "loc_89EA"),
        (2, "loc_9057"),
        (SWITCH_DEFAULT, "loc_9725"),
    )


    label("loc_83FB")

    OP_50(0x65, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xA, 500)

    #C0268
    ChrTalk(
        0x101,
        (
            "#12P#12500Fそれじゃあ……\x01",
            "エリィから塗らせてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0xA,
        (
            "#12612Fわ、私っ！？\x02\x03",

            "#12613F……い、いいけど……\x01",
            "変なところ、触らないでよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x101,
        "#12P#12503Fぜ、善処させていただきます……\x02",
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
            "#11P#12501Fそ、それじゃあ失礼して……\x02\x03",

            "#12503F（ぴとっ。）\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x64, 0x64, 0xBB8, 0x12C)

    def lambda_85EC():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_85EC)

    #C0272
    ChrTalk(
        0xA,
        "#6P#12615F#4S……ひゃあっ！？\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x101,
        "#11P#12505Fゴ、ゴメン！　大丈夫か？\x02",
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xA,
        (
            "#6P#12613Fう、うん……\x01",
            "冷たくてちょっとびっくりしただけ。\x02\x03",

            "#12602F大丈夫だから、続けてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#11P#12503Fそ、そっか、じゃあ……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(13500, 9000)
    BeginChrThread(0x101, 3, 0, 42)
    Sleep(2000)

    #C0276
    ChrTalk(
        0x101,
        (
            "#11P#12506F（はあ、これは予想以上に\x01",
            "  心臓に悪いな……）\x02\x03",

            "#12508F（それにしてもエリィ、\x01",
            "  本当に綺麗だよな……）\x02\x03",

            "#12503F（肌なんか真っ白だし、\x01",
            "  パールグレイの髪が\x01",
            "  よく映えてるっていうか……）\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    #C0277
    ChrTalk(
        0xA,
        (
            "#6P#12612F……ちょ、ちょっと。\x01",
            "突然黙らないでちょうだい。\x02\x03",

            "#12611Fまさか、いやらしい事を\x01",
            "考えてたんじゃないでしょうね？\x02",
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
            "#11P#12511Fめ、滅相もございません！\x02\x03",

            "#12503F（下手したら、マリアベルさんに\x01",
            "　本当に湖底に沈められる……！！）\x02\x03",

            "#12501F（……心を限りなく無にするんだ。\x01",
            "  とにかく無の境地に……！）\x02",
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
            "#11P#N#13506Fロイドさん……\x01",
            "なんだか東通りのお地蔵様のような\x01",
            "顔になってるみたいですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0280
    ChrTalk(
        0x8,
        (
            "#11P#13309Fふふ、ロイド。\x01",
            "エリィさんが終わったら\x01",
            "私たちのほうもお願いね。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_9725")

    label("loc_89EA")

    OP_50(0x6D, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0281
    ChrTalk(
        0x101,
        (
            "#12P#12500Fそれじゃあ……\x01",
            "セシル姉から塗らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x8,
        (
            "#5P#13309Fふふ、分かったわ。\x01",
            "それじゃあお願いするわね。\x02",
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
        "#11P#12500F……どうかな、セシル姉。\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x8,
        (
            "#6P#13304Fうん、そんな感じよ。\x01",
            "あとは薄く塗り広げてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x101,
        "#11P#12500Fうん、分かった。\x02",
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#6P#13304F……ふふ、なんだかこうしてると\x01",
            "昔を思い出すわね。\x02\x03",

            "#13302F子供の頃は、ときどきお風呂で\x01",
            "ロイドと背中を流しっこしたっけ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0287
    ChrTalk(
        0x101,
        (
            "#11P#12511Fだあああっ、セ、セシル姉ってば！！\x01",
            "みんなの前で何を言ってるんだよ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    OP_63(0x8, 0xFFFFFE0C, 1700, 0x2, 0x7, 0x50, 0x1)

    def lambda_8CD1():
        OP_A6(0xFE, 0x32, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_8CD1)

    #C0288
    ChrTalk(
        0x8,
        (
            "#6P#13306Fきゃっ！\x02\x03",

            "#13309F……ふふ、もうロイドったら。\x01",
            "変なところ触っちゃダメよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0289
    ChrTalk(
        0x101,
        "#11P#12511Fわっ、ゴ、ゴメン！！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    SetCameraDistance(13500, 9000)
    Sleep(2000)

    #C0290
    ChrTalk(
        0x101,
        (
            "#11P#12506F（ああ、もうっ……\x01",
            "  セシル姉は無防備すぎるよ！？）\x02\x03",

            "#12508F（そ、それに、肌を出したら\x01",
            "  こんな破壊力抜群の……）\x02\x03",

            "#12506F（……って、ダメだろ俺！\x01",
            "  セシル姉にそんなこと考えちゃ！）\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    #C0291
    ChrTalk(
        0x8,
        (
            "#6P#13305Fロイド、どうかしたの？\x01",
            "さっきから同じところばっかり\x01",
            "塗ってるみたいだけど……\x02\x03",

            "#13308F……もしかして私、太ってるかしら？\x02\x03",

            "#13306F患者さんや師長が\x01",
            "よくお菓子を下さるから、\x01",
            "つい食べちゃうのよねえ……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x101,
        (
            "#11P#12512Fい、いやいや、\x01",
            "全然そんなことないから！！\x01",
            "心配しなくても十分に綺麗……\x02\x03",

            "#12506F……ああいや、じゃなくて！！\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x8,
        "#6P#13309Fふふっ、ありがとうロイド。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xA,
        (
            "#6P#12611F（うーん……\x01",
            "  相変わらず甘々だこと。）\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x9,
        (
            "#11P#13509F（あはは……\x01",
            "  話に聞いてた通りみたいですね。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_9725")

    label("loc_9057")

    OP_50(0x6A, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0x9, 500)

    #C0296
    ChrTalk(
        0x101,
        (
            "#12P#12500Fそれじゃあ……\x01",
            "リーシャ、君から塗らせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x9,
        (
            "#11P#13505Fは、はいっ！\x02\x03",

            "#13503Fあの、不束者ですが\x01",
            "よろしくお願いしますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0298
    ChrTalk(
        0x101,
        "#12P#12506F……それ、なんか間違ってるから。\x02",
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
        "#11P#12502Fよっと……ど、どうかな？\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x9,
        (
            "#6P#13503Fあ、はい。\x01",
            "そんなものだと思います。\x02\x03",

            "#13506Fはあ、でも本当に助かりました。\x01",
            "アルカンシェルの舞台に出るのに\x01",
            "日焼けなんてできませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、それはそうか。\x02\x03",

            "#12505Fあれ、でも……\x01",
            "イリアさんの日焼け止めは\x01",
            "君が塗ったんじゃないのか？\x02\x03",

            "#12511Fその時に交代で塗ってもらえば──\x01",
            "……って、あ。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x9,
        (
            "#6P#13509Fえ、ええっと……あはは。\x01",
            "つまりはそういうことです。\x02\x03",

            "#13506Fイリアさんにこんな無防備な\x01",
            "格好をさらしたら、何をされるか\x01",
            "分かりませんから……\x02",
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
            "#11P#12512F（オジサン丸出しのイリアさんより\x01",
            "  俺の方がマシだってことか……\x01",
            "  それもまた複雑な理由だけど。）\x02\x03",

            "#12501F（……それにしてもリーシャ、\x01",
            "  見た目じゃ分かりにくいけど\x01",
            "  かなり鍛えられてるんだよな。）\x02\x03",

            "#12508F（このプロポーションを保ちつつ\x01",
            "  あそこまでの身体能力……\x01",
            "  これも才能ってヤツなのかな。）\x02\x03",

            "#12503F（というか何よりも\x01",
            "  この身長でコレは、まさに\x01",
            "  凶器と言っても過言じゃあ……）\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)

    #C0304
    ChrTalk(
        0x9,
        "#6P#13505Fロ、ロイドさん？　その、視線が……\x02",
    )

    CloseMessageWindow()
    OP_4B(0x101, 0xFF)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    #C0305
    ChrTalk(
        0x101,
        (
            "#11P#12511Fわっ、ゴ、ゴメン！\x02\x03",

            "#12512Fい、いやその、違うんだ。\x01",
            "やっぱり鍛えてるな～って思って……\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0xA,
        (
            "#6P#N#12611Fはあ……男の子って\x01",
            "どうしてこうなのかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0307
    ChrTalk(
        0x8,
        (
            "#13309Fふふ、ロイド。\x01",
            "リーシャさんが終わったら\x01",
            "私たちのほうもお願いね。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x101, 0xFF)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_64(0x101)
    Jump("loc_9725")

    label("loc_9725")

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
            "#6P#12506F（あ、改めて見ると\x01",
            "  すごい光景だなあ……）\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x8,
        (
            "#5P#13304Fはあ～……ありがとう、ロイド。\x01",
            "とってもリラックスできたわ。\x02\x03",

            "#13309Fうふふ、このまま眠っちゃいそう。\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0xA,
        (
            "#1P#12606Fセ、セシルさん。\x01",
            "その格好で寝るのは色々と\x01",
            "危険だと思うんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x9,
        (
            "#2P#13509Fあはは……\x01",
            "ちょっと大らかすぎますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x8,
        "#13304Fふふ、だって気持ちがいいんだもの。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0313
    ChrTalk(
        0x101,
        (
            "#6P#12500Fそれじゃあ、目が覚めるように\x01",
            "皆に冷たい飲み物でも買ってこようか？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0xA,
        "#1P#12605Fあら、いいの？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#6P#12503F（ある意味、夢みたいな体験を\x01",
            "  させてもらったからな……）\x02\x03",

            "#12512F（正直、これくらいしないと\x01",
            "  女神から罰が下りそうだよ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x9,
        "#2P#13505F……ロイドさん？\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        (
            "#6P#12512Fあ、ああいや、なんでもないよ。\x02\x03",

            "#12500Fそれじゃあ、ノンアルコールの\x01",
            "カクテルか何かでいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        (
            "#5P#13302Fええ、それでお願いするわ。\x02\x03",

            "#13309Fああ、急がなくてもいいからね。\x01",
            "ロイドも色々楽しんでらっしゃい。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x101,
        (
            "#6P#12500Fああ、ありがとう。\x01",
            "それじゃあ後でね。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9CEE")
    Call(0, 54)
    EventEnd(0x5)
    Jump("loc_9D01")

    label("loc_9CEE")

    SetChrPos(0x0, 21500, -6000, 20700, 90)
    EventEnd(0x5)

    label("loc_9D01")

    Return()

    # Function_41_8232 end

    def Function_42_9D02(): pass

    label("Function_42_9D02")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9D19")
    OP_A0(0xFE, 500, 0x0, 0x3)
    Jump("Function_42_9D02")

    label("loc_9D19")

    Return()

    # Function_42_9D02 end

    def Function_43_9D1A(): pass

    label("Function_43_9D1A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2CB")

    #C0320
    ChrTalk(
        0xC,
        "#6P#13101Fさくさく……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0xB,
        "#12P#12701Fペタペタ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0322
    ChrTalk(
        0x101,
        "#11P#12505F（な、なんだか集中してるなあ……）\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0xD,
        "#01200F……グルル……ウォン。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9ED8")
    Jump("loc_9F22")

    label("loc_9ED8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9EF8")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F22")

    label("loc_9EF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F18")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_9F22")

    label("loc_9F18")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9F22")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9FD8")
    Jump("loc_A022")

    label("loc_9FD8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_9FF8")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A022")

    label("loc_9FF8")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A018")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A022")

    label("loc_A018")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A022")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0324
    ChrTalk(
        0xB,
        "#12P#12705F……ああ、ロイドさん。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0xC,
        "#6P#13100Fどうかしたんですか～？\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#11P#12512Fはは、邪魔しちゃったかな。\x02\x03",

            "#12500Fいや、そんな一所懸命に\x01",
            "何を作ってるのかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0xC,
        (
            "#6P#13100Fいえいえ、とんでもないです。\x02\x03",

            "#13109F一応、砂でお城を作っていた\x01",
            "ところなんですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0xB,
        (
            "#12P#12700Fいわゆる、『サンドクラフト』ですね。\x02\x03",

            "#12706Fただ、なかなか上手くいかなくて……\x01",
            "先ほどから作っては壊しの繰り返しです。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        "#11P#12503Fう～ん、なかなか難しそうだな。\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0xC,
        (
            "#6P#13100Fそうだ、せっかくですし、\x01",
            "ロイドさんも手伝ってみませんか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x101,
        "#11P#12505Fえっ……俺が？\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0xB,
        (
            "#12P#12702Fええ、そうですね。\x01",
            "作業が進展するかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15E, 1)
    Jump("loc_A557")

    label("loc_A2CB")

    OP_52(0x101, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xB, 0x10)
    TurnDirection(0xB, 0x101, 0)
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A35C")
    Jump("loc_A3A6")

    label("loc_A35C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A37C")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3A6")

    label("loc_A37C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A39C")
    OP_52(0xB, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A3A6")

    label("loc_A39C")

    OP_52(0xB, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xB, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A3A6")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A45C")
    Jump("loc_A4A6")

    label("loc_A45C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A47C")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A4A6")

    label("loc_A47C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A49C")
    OP_52(0xC, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A4A6")

    label("loc_A49C")

    OP_52(0xC, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xC, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A4A6")

    OP_52(0xC, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xC, 0x10)

    #C0333
    ChrTalk(
        0xC,
        (
            "#6P#13100Fあ、ロイドさん。\x01",
            "砂の城作りを手伝って\x01",
            "くれるんですか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0xB,
        (
            "#12P#12702F是非お願いします。\x01",
            "作業が進展するかもしれませんし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A557")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "砂の城作りを手伝う\x01",      # 0
            "やめておく\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A6E7")

    #C0335
    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、分かった。\x01",
            "俺でよければ手伝わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0xC,
        (
            "#6P#13109Fさっすがロイドさん！\x01",
            "ありがとうございます～！\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#11P#12502Fはは、とは言っても\x01",
            "俺もまるっきりの初心者だけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0xB,
        (
            "#12P#12702Fまあ、みんな似たようなものですし。\x02\x03",

            "#12704Fでは、早速よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Call(0, 44)
    Call(0, 45)
    Jump("loc_A7CA")

    label("loc_A6E7")


    #C0339
    ChrTalk(
        0x101,
        "#11P#12512Fうーん、今はちょっと……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0xC,
        "#6P#13106Fえー、そんなあ。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xB,
        (
            "#12P#12702Fまあ、その気になったら\x01",
            "是非声をかけてください。\x02\x03",

            "#12704Fそれまでフランさんと\x01",
            "頑張ってますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0xD,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)

    label("loc_A7CA")

    SetChrPos(0x0, 29920, -6000, 8910, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A7F3")
    Call(0, 54)

    label("loc_A7F3")

    EventEnd(0x5)
    Return()

    # Function_43_9D1A end

    def Function_44_A7F6(): pass

    label("Function_44_A7F6")

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
        "#6P#13100F……ふう、だいぶできてきましたね～。\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xB,
        "#12P#12700Fええ、完成まであと少し──\x02",
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
        "#01203F……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0xB,
        "#12P#12706F……やはり、なかなか難しいです。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#11P#12500Fうーん、もしかすると\x01",
            "砂の強度に問題がある\x01",
            "のかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0xC,
        (
            "#6P#13105F強度ですかー……\x02\x03",

            "#13106F一応、バケツに砂と水を入れて\x01",
            "土台はしっかりと作ったんですけどね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#11P#12500Fそれでも、作っていると\x01",
            "砂が乾いてくるだろうしな。\x02\x03",

            "#12504F水を足しつつやった方がいいって、\x01",
            "聞いたことがある気がする。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0xB,
        (
            "#12P#12705Fなるほど……\x01",
            "理に適っていそうです。\x02\x03",

            "#12702Fそれじゃあ、水はどれくらいずつ\x01",
            "足した方がいいんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        "#11P#12503Fえーっと、そうだな……\x02",
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
            "#1K足していく水の量はどうする？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "たっぷり\x01",        # 0
            "少し多めに\x01",      # 1
            "ほんの少し\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACE3")
    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0353
    ChrTalk(
        0x101,
        (
            "#11P#12500F確か、ほんの少し……\x01",
            "湿らす程度で大丈夫だったと思う。\x02\x03",

            "#12504Fあまり水をつけすぎても\x01",
            "逆に強度は下がるだろうしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0xC,
        (
            "#6P#13100F確かに、言われてみると\x01",
            "そんな気がしますね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0xB,
        (
            "#12P#12702Fでは、ロイドさんの言う通りに\x01",
            "やってみるとしましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE7A")

    label("loc_ACE3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AD86")

    #C0356
    ChrTalk(
        0x101,
        (
            "#11P#12500Fここは思い切って、\x01",
            "たっぷり水を使いながら\x01",
            "やったほうがいいんじゃないか？\x02\x03",

            "#12504Fその方が強度が上がる……\x01",
            "ような気がするけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE08")

    label("loc_AD86")


    #C0357
    ChrTalk(
        0x101,
        (
            "#11P#12500F多分、少し多めに水を使いつつ\x01",
            "やったほうがいいんじゃないか？\x02\x03",

            "#12504Fその方が強度が上がる……\x01",
            "ような気がするけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE08")


    #C0358
    ChrTalk(
        0xC,
        "#6P#13105Fそんなものなんですかね～？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0xB,
        (
            "#12P#12700Fまあ、ロイドさんの言う通りに\x01",
            "やってみるとしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE7A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0xA, 0x1)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B01C")
    OP_63(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xB, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0360
    ChrTalk(
        0xB,
        "#12P#12702Fかなり完成に近づいてきましたね。\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xC,
        (
            "#6P#13109Fうんうん、ロイドさんの\x01",
            "アドバイスのおかげだね！\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        "#11P#12502Fはは、そう言ってもらえると嬉しいよ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0363
    ChrTalk(
        0xB,
        (
            "#12P#12702Fふふ……では、いよいよ\x01",
            "仕上げに入りましょう。\x02\x03",

            "メインの城の部分の\x01",
            "ディテールアップですが……\x01",
            "ロイドさんにお願いしていいですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B1C2")

    label("loc_B01C")


    #C0364
    ChrTalk(
        0xB,
        "#12P#12700Fかなり完成に近づいてきましたが……\x02",
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
        "#6P#13105Fな、なんだかびちゃびちゃしてるね～。\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#11P#12506F（う、うーん……\x01",
            "  やっぱり水が多すぎたのかも……）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0367
    ChrTalk(
        0xB,
        (
            "#12P#12703Fまあ、今のところ\x01",
            "崩れる気配はなさそうですし……\x01",
            "そろそろ仕上げに入りましょう。\x02\x03",

            "#12702Fメインの城の部分の\x01",
            "ディテールアップですが……\x01",
            "ロイドさんにお願いしていいですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B1C2")


    #C0368
    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、分かった。\x01",
            "任せてくれ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0369
    ChrTalk(
        0xC,
        (
            "#6P#13100F全てはロイドさんにかかってます！\x01",
            "よろしくお願いしますね～！\x02",
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
            "#11P#12506F（プ、プレッシャーを\x01",
            "  かけられてしまった……\x01",
            "  けどまあ、仕方ないか。）\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#11P#12501F（さて、水で強度を\x01",
            "  高めているとはいえ、\x01",
            "  素材はあくまで砂……）\x02\x03",

            "#12503F（重要なのは恐らく、\x01",
            "  スピードと力加減だ。\x01",
            "  ……どう作業を進める？）\x02",
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
            "#1Kスピードと力加減はどうする？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ゆっくり／繊細に\x01",      # 0
            "ゆっくり／力強く\x01",      # 1
            "素早く／繊細に\x01",        # 2
            "素早く／力強く\x01",        # 3
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
        (0, "loc_B428"),
        (1, "loc_B47B"),
        (2, "loc_B4CC"),
        (3, "loc_B527"),
        (SWITCH_DEFAULT, "loc_B576"),
    )


    label("loc_B428")


    #C0373
    ChrTalk(
        0x101,
        (
            "#11P#12500F（よし……ゆっくりと繊細な力で\x01",
            "  ディテールを整えていこう！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B47B")


    #C0374
    ChrTalk(
        0x101,
        (
            "#11P#12500F（よし……ゆっくりと力強く、\x01",
            "  ディテールを整えていこう！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B4CC")

    RunExpression(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0375
    ChrTalk(
        0x101,
        (
            "#11P#12500F（よし……迅速かつ繊細な力で\x01",
            "  ディテールを整えていこう！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B527")


    #C0376
    ChrTalk(
        0x101,
        (
            "#11P#12500F（よし……迅速かつ力強く、\x01",
            "  ディテールを整えていこう！）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B576")

    label("loc_B576")

    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B594")
    Jump("loc_B966")

    label("loc_B594")

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
        "#11P#12511F#4Sあ゛。#3S\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0xB,
        "#12P#12705Fあ……\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0xC,
        (
            "#6P#13100Fあー……あはは。\x01",
            "やっちゃいましたね～。\x02",
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
            "#11P#12505Fいやその、なんというか……\x02\x03",

            "#12506F……ゴメンナサイ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0381
    ChrTalk(
        0xB,
        (
            "#12P#12703F……まあ仕方ないでしょう。\x02\x03",

            "#12700Fとりあえず、１から地道に\x01",
            "作り直すとしましょうか。\x02\x03",

            "ロイドさんは、私とフランさんの\x01",
            "サポートに回ってください。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x101,
        "#11P#12512Fりょ、了解。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0383
    ChrTalk(
        0xC,
        (
            "#6P#13109Fロイドさん、どうか\x01",
            "気を落とさないで下さいね～。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B886")

    #C0384
    ChrTalk(
        0x101,
        (
            "#11P#12506F（水加減は合ってた\x01",
            "  はずなんだけど……）\x02\x03",

            "（はああ……立場がないな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B966")

    label("loc_B886")

    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8FE")

    #C0385
    ChrTalk(
        0x101,
        (
            "#11P#12506F（作業の仕方は間違ってなかった\x01",
            "  はずなんだけど……）\x02\x03",

            "（はああ……立場がないな。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B966")

    label("loc_B8FE")


    #C0386
    ChrTalk(
        0x101,
        (
            "#11P#12506F（水加減も作業の仕方も、\x01",
            "  間違ってたとしか思えない……）\x02\x03",

            "（はああ……立場がないな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B966")

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
        "#11P#12500Fふう……こんな所かな。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0388
    ChrTalk(
        0xC,
        (
            "#6P#13100Fついに……\x01",
            "ついに完成したんですね～！！\x02\x03",

            "#13109Fキャ～！　やったやった～！！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BB23")
    OP_2C(0xA5, 0x1)
    TurnDirection(0xB, 0x101, 500)

    #C0389
    ChrTalk(
        0xB,
        (
            "#12P#12704F……感無量です。\x01",
            "ロイドさん、お疲れ様でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        (
            "#11P#12502Fはは……そんな。\x01",
            "２人が頑張ったおかげさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0391
    ChrTalk(
        0xC,
        (
            "#6P#13109Fいえいえ、ロイドさんのおかげですよ～！\x01",
            "本当にありがとうございます！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BC05")

    label("loc_BB23")

    TurnDirection(0xB, 0x101, 500)

    #C0392
    ChrTalk(
        0xB,
        (
            "#12P#12702F……とりあえず、よかったです。\x01",
            "完成まで色々ありましたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        "#11P#12506Fそ、その節は本当にすいませんでした。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0394
    ChrTalk(
        0xC,
        (
            "#6P#13109Fあはは、もういいですってば～。\x01",
            "こうして完成にはこぎつけたんですし！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BC05")

    TurnDirection(0xB, 0xD, 500)

    #C0395
    ChrTalk(
        0xB,
        (
            "#12P#12702F#5Pツァイトもお疲れ様でした。\x02\x03",

            "#12704F終盤は、不足した砂や水の補給を\x01",
            "手伝ってくれましたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xD,
        "#01200Fグルル……ウォン。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 500)

    #C0397
    ChrTalk(
        0x101,
        "#11P#12500F#5Pはは、さすがはツァイトだよな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x101, 0x87, 0x1F4)

    #C0398
    ChrTalk(
        0x101,
        (
            "#11P#12505Fそうだ、そういえば……\x01",
            "この城って名前はあるのか？\x02",
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
        "#6P#13105F名前……ですか～？\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        (
            "#11P#12500Fいや、せっかく苦労して作ったんだし、\x01",
            "そういうものがあれば\x01",
            "思い出になるんじゃないかと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xB,
        (
            "#12P#12703F一理ありますね。\x01",
            "ふむ、それなら……\x02\x03",

            "#12700F『みっしぃキャッスル』、\x01",
            "というのはいかがでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0xC,
        (
            "#6P#13105Fえ～、ティオちゃんズルい！\x02\x03",

            "#13109Fだったらあたしは\x01",
            "『バンバンキャッスル』がいいな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x101,
        (
            "#11P#12500Fみっしぃはおなじみだけど……\x02\x03",

            "#12503Fバンバンっていうのは、\x01",
            "フランのお気に入りの\x01",
            "ヌイグルミだったっけ。\x02\x03",

            "#12509Fはは……どっちもかなり\x01",
            "趣味が入ってるなあ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0404
    ChrTalk(
        0xB,
        (
            "#12P#12703F……ですが、同じ城に\x01",
            "２つの名前はつけられません。\x02\x03",

            "#12700Fこの際ですし、ロイドさんが\x01",
            "どっちがいいか決めてくれませんか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x101, 500)

    #C0405
    ChrTalk(
        0xC,
        (
            "#6P#13100Fあっ、それはいいかも～！\x02\x03",

            "#13109Fロイドさんが決めるなら\x01",
            "文句はないですし、ビシっと\x01",
            "選んじゃってください！\x02",
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
            "#11P#12506F（な、なにげに責任重大だな。）\x02\x03",

            "#12500Fうーん、そうだなあ……\x02",
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
            "#1K城の名前はどっちにする？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "みっしぃキャッスル\x01",      # 0
            "バンバンキャッスル\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2C2")
    OP_50(0x66, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xB, 500)

    #C0408
    ChrTalk(
        0x101,
        (
            "#11P#12503F#5Pそうだな、せっかく\x01",
            "ミシュラムに来たことだし……\x02\x03",

            "#12500F今回は『みっしぃキャッスル』で\x01",
            "いいんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0409
    ChrTalk(
        0xC,
        (
            "#6P#13106Fむ～、言われてみればそうですね～。\x02\x03",

            "#13102Fしかたないなあ、今回は\x01",
            "ティオちゃんにゆずってあげる！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    #C0410
    ChrTalk(
        0xB,
        "#12P#12702Fふふ……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3FD")

    label("loc_C2C2")

    OP_50(0x6E, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    TurnDirection(0x101, 0xC, 500)

    #C0411
    ChrTalk(
        0x101,
        (
            "#11P#12503F#11Pそうだな、みっしぃには\x01",
            "後でいくらでも会えるだろうし……\x02\x03",

            "#12500F今回は『バンバンキャッスル』で\x01",
            "いいんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xC, 500)

    #C0412
    ChrTalk(
        0xB,
        (
            "#12P#12703F……ふむ、一理ありますね。\x02\x03",

            "#12702Fまあいいでしょう、今回は\x01",
            "フランさん案ということで。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0xB, 500)

    #C0413
    ChrTalk(
        0xC,
        "#6P#13109Fふふっ、ありがとうティオちゃん！\x02",
    )

    CloseMessageWindow()

    label("loc_C3FD")

    OP_93(0x101, 0x87, 0x1F4)

    #C0414
    ChrTalk(
        0x101,
        (
            "#11P#12509Fはは、丸く収まったみたいだな。\x02\x03",

            "#12505Fそうだ……ティオ、フラン。\x01",
            "ずっと砂浜にいて、喉が渇かないか？\x02\x03",

            "#12500F良かったら、後で\x01",
            "冷たいものでも持って来るけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)
    TurnDirection(0xC, 0x101, 500)

    #C0415
    ChrTalk(
        0xB,
        (
            "#12P#12703Fそうですね……\x02\x03",

            "#12700Fわたしは、売店にあった\x01",
            "カキ氷を食べてみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xC,
        (
            "#6P#13100Fあっ、あたしも食べた～い！\x02\x03",

            "#13109Fロイドさん、お願いしてもいいですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        (
            "#11P#12509Fああ、任せてくれ。\x02\x03",

            "#12500Fツァイトには……\x01",
            "フランクフルトでいいかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0xD,
        "#01203Fグルルル……ウォン。\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0xB,
        (
            "#12P#12702F『頼んだ』だそうです。\x02\x03",

            "#12703F……ああ、でも急がなくても\x01",
            "全然結構ですから。\x02\x03",

            "#12702Fせっかく来てるんですし、\x01",
            "ロイドさんも楽しんでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        "#11P#12502Fはは、了解。\x02",
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

    # Function_44_A7F6 end

    def Function_45_C706(): pass

    label("Function_45_C706")

    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_END)), "loc_C723")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C723")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_END)), "loc_C736")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_END)), "loc_C749")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_C749")

    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C790")
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_C790")

    Return()

    # Function_45_C706 end

    def Function_46_C791(): pass

    label("Function_46_C791")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CB, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CCCC")

    #C0421
    ChrTalk(
        0xE,
        (
            "#13209F#6Pわあああっ……\x01",
            "シュリのもキレーだね！\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0xF,
        (
            "#13603F#11Pフ、フン、大した事ねーよ。\x02\x03",

            "#13600Fにしてもこんな石、今まで\x01",
            "見たことなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#12500F#5P２人とも、戻ってきてたのか。\x01",
            "……何やってるんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C911():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_C911)
    Sleep(50)

    def lambda_C921():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_C921)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    #C0424
    ChrTalk(
        0xE,
        (
            "#13210F#12Pあ、ロイドー。\x01",
            "これを見てみてー！\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0xE,
        "#13209F#12Pえへへ、キレイでしょー？\x02",
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x101,
        (
            "#12500F#5Pへえ、丸くて真っ白で……\x01",
            "宝石みたいに綺麗な石だな。\x02\x03",

            "#12505Fこれ、どうしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0xF,
        (
            "#13600F#12Pさっき、泳いでいる途中で\x01",
            "このチビッコが拾ってきてさ。\x02\x03",

            "#13604Fどうも、あっちこっちに\x01",
            "落ちてるみたいだから\x01",
            "ちょっと探してみてたんだ。\x02\x03",

            "#13602F監視員の人に聞いてみたら、\x01",
            "『ホワイトストーン』って言う\x01",
            "石なんだってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x101,
        (
            "#12500F#5Pふーむ、ここの砂って\x01",
            "外国から運んできたみたいだし……\x02\x03",

            "#12503F多分、その辺りで取れるものが\x01",
            "混ざってたってところだろうな。\x02\x03",

            "#12500Fその分だと、結構大きいのも\x01",
            "埋まってるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0429
    ChrTalk(
        0xE,
        (
            "#13205F#12Pホントー！？\x02\x03",

            "#13200Fねえねえ、それじゃあみんなで、\x01",
            "この白い石を探してみようよ！\x02\x03",

            "#13209Fそれで、最後に一番おっきいのを\x01",
            "持ってた人が勝ちになるの！！\x02",
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
            "#13602F#12Pフフン、面白そうじゃん。\x02\x03",

            "#13604F当然アンタも参加するよな？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1CB, 6)
    Jump("loc_CD70")

    label("loc_CCCC")


    def lambda_CCD1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_CCD1)
    Sleep(50)

    def lambda_CCE1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_CCE1)
    WaitChrThread(0xE, 2)
    WaitChrThread(0xF, 2)

    #C0431
    ChrTalk(
        0xF,
        (
            "#13600F#12Pん、やっぱりアンタも\x01",
            "混ざりたいのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0xE,
        (
            "#13202F#12Pロイドも一緒に、\x01",
            "『ホワイトストーン』を\x01",
            "探してみよーよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CD70")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ホワイトストーン探しを始める\x01",      # 0
            "やめておく\x01",                        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D02F")

    #C0433
    ChrTalk(
        0x101,
        (
            "#12500F#5Pああ、せっかくだし\x01",
            "参加させてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0xE,
        "#13209F#12P決まりだねー！\x02",
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0xF,
        (
            "#13600F#12Pそんじゃ、アンタも\x01",
            "『ホワイトストーン』を見つけたら、\x01",
            "オレに教えてくれ。\x02\x03",

            "#13604F最後に大きさを比べっこして、\x01",
            "一番大きいのを持ってた奴が勝ちな。\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x101,
        "#12509F#5Pはは、了解だ。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0xE,
        (
            "#13201F#12Pよぉーし……\x01",
            "それじゃあスタートだー！\x02\x03",

            "#13200Fキーア、ゼッタイ一番大きいのを\x01",
            "見つけてくるからねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0xF,
        (
            "#13603F#12Pフン、お前らなんかに\x01",
            "負けてたまるかっての。\x02",
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
    Jump("loc_D111")

    label("loc_D02F")


    #C0439
    ChrTalk(
        0x101,
        "#12512F#5Pうーん、今は止めておくよ。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0xE,
        "#13205F#12Pえー、そうなんだー？\x02",
    )

    CloseMessageWindow()

    #C0441
    ChrTalk(
        0xF,
        (
            "#13606F#12Pちぇっ、ノリが悪いなあ。\x02\x03",

            "#13600Fま、気が向いたら声をかけてくれ。\x01",
            "そん時は混ぜてやるよ。\x02",
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

    label("loc_D111")

    EventEnd(0x5)
    Return()

    # Function_46_C791 end

    def Function_47_D114(): pass

    label("Function_47_D114")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0442
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0443
    ChrTalk(
        0x101,
        (
            "#12503Fうーん、少し小さいかな？\x02\x03",

            "もっと大きいのがありそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x15C, 1)
    TalkEnd(0xFF)
    Return()

    # Function_47_D114 end

    def Function_48_D1B8(): pass

    label("Function_48_D1B8")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0444
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32B, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0445
    ChrTalk(
        0x101,
        (
            "#12505Fあったけど……小さいな。\x02\x03",

            "もう少し探してみるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x15C, 2)
    TalkEnd(0xFF)
    Return()

    # Function_48_D1B8 end

    def Function_49_D250(): pass

    label("Function_49_D250")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0446
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x329),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x329, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0447
    ChrTalk(
        0x101,
        (
            "#12500F手のひらにすっぽり\x01",
            "収まるくらいの大きさだ。\x02\x03",

            "#12503Fキーアもシュリもこのくらいは\x01",
            "見つけてそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x5, 0x1)
    SetScenarioFlags(0x15C, 3)
    TalkEnd(0xFF)
    Return()

    # Function_49_D250 end

    def Function_50_D31F(): pass

    label("Function_50_D31F")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0448
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x329),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x329, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0449
    ChrTalk(
        0x101,
        (
            "#12503F……そこそこ大きいくらいかな？\x02\x03",

            "#12500Fこれなら少しはいい勝負が\x01",
            "できるかもしれないけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x15C, 4)
    TalkEnd(0xFF)
    Return()

    # Function_50_D31F end

    def Function_51_D3E1(): pass

    label("Function_51_D3E1")

    TalkBegin(0xFF)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0450
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0451
    ChrTalk(
        0x101,
        (
            "#12505Fおおっ……！？\x01",
            "水晶玉みたいなサイズだ！\x02\x03",

            "#12509Fはは、これだけ大きかったら\x01",
            "まず負ける事はなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_65(0x7, 0x1)
    SetScenarioFlags(0x15C, 5)
    TalkEnd(0xFF)
    Return()

    # Function_51_D3E1 end

    def Function_52_D4B0(): pass

    label("Function_52_D4B0")

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
        "#12605Fあらロイド、何をしてるの？\x02",
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#6P#12500Fああ、今はキーアたちと……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0454
    ChrTalk(
        0x101,
        "#6P#12505Fってあれ、もしかして……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0455
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはデッキチェアの下に\x01",
            "手を伸ばした。\x07\x00\x02",
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
        "#12612Fえっ、ちょ、ちょっと……！？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        "#6P#12502F──あった！\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x32C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32C, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0459
    ChrTalk(
        0x101,
        (
            "#6P#12500Fこんなところに\x01",
            "埋まってるなんて……\x02\x03",

            "#12504Fでも、相当大きいな。\x01",
            "これなら絶対に勝てるはずだ。\x02",
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
            "#12611Fあ、あなたねえ……\x01",
            "いきなりそんな所に潜り込んで、\x01",
            "どういうつもりなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        "#6P#12511Fあっ……ゴ、ゴメン！\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0xA,
        "#12606Fふう、まったくもう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x15C, 6)
    EventEnd(0x5)
    Return()

    # Function_52_D4B0 end

    def Function_53_D799(): pass

    label("Function_53_D799")

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
            "#12P#13600Fそれじゃあ大きさを比べるぞ。\x02\x03",

            "#13603F『いっせーの、せ』で、\x01",
            "自分が持ってる\x01",
            "一番大きい石を出すんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x101,
        "#5P#12500Fああ、了解だ。\x02",
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0xE,
        "#12P#13210F準備オッケーだよー！\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0xF,
        "#12P#13601Fよし、じゃあ行くぞ……\x02",
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x101,
        "#5P#12501Fいっ、せ～の……\x02",
    )


    #C0468
    ChrTalk(
        0xE,
        "#3P#13201Fいっ、せーのぉ……\x02",
    )


    #C0469
    ChrTalk(
        0xF,
        "#4P#13601Fいっ、せ～の……\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x101,
        "#5P#12500F#4Sせっ！#3S\x02",
    )


    #C0471
    ChrTalk(
        0xE,
        "#3P#13200F#4Sせー！！#3S\x02",
    )


    #C0472
    ChrTalk(
        0xF,
        "#4P#13600F#4Sせっ！#3S\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E427")
    OP_2C(0xA5, 0x1)
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xF, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0473
    ChrTalk(
        0xE,
        (
            "#12P#13210Fわあああっ……！！\x01",
            "ロイドの『ホワイトストーン』、\x01",
            "すっごく大っきいー！！\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0xF,
        (
            "#12P#13601Fくっ……まさかそんなのを\x01",
            "見つけてくるなんて。\x02\x03",

            "#13606Fさすがにコレは、\x01",
            "負けを認めるしかなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x101,
        (
            "#5P#12502Fはは、それじゃあ\x01",
            "俺の勝ちってことでよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0xF,
        "#12P#13606Fちぇっ、子供相手に大人気ないヤツ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0477
    ChrTalk(
        0x101,
        (
            "#5P#12506F……それを言われると\x01",
            "立場がないんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0xE,
        (
            "#12P#13200Fでも、本当に大きくてキレーだねー。\x02\x03",

            "#13206Fキーアもそんなのが欲しかったなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0xF,
        (
            "#12P#13600Fそうだなあ……\x01",
            "オレも、もう少し探してみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DE97")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0480
    ChrTalk(
        0x101,
        (
            "#5P#12500Fはは、それじゃあ\x01",
            "この『ホワイトストーン』は\x01",
            "２人にプレゼントするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0481
    ChrTalk(
        0xE,
        "#12P#13210Fホントにー！？\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0xF,
        (
            "#12P#13605Fい、いいのか？\x01",
            "それに２つなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#5P#12500Fああ、ちょうど\x01",
            "同じくらいの大きさのを\x01",
            "もう一つ拾ってたんだ。\x02\x03",

            "#12509Fせっかくビーチに来たんだし、\x01",
            "その思い出にするといいよ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0484
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはキーアとシュリに\x01",
            "大きな『ホワイトストーン』を\x01",
            "ひとつずつ渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0485
    ChrTalk(
        0xF,
        "#12P#13612Fフ、フン……ありがとよ。\x02",
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0xE,
        "#12P#13209Fえへへ、大事にするねー！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber(0x32C, 2)
    Jump("loc_E422")

    label("loc_DE97")


    #C0487
    ChrTalk(
        0x101,
        (
            "#5P#12500F（そうだ、せっかくだし……\x01",
            "  プレゼントしてあげようかな？）\x02",
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
            "#1K『ホワイトストーン』をどっちにプレゼントする？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "キーアにあげる\x01",      # 0
            "シュリにあげる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1E3")
    OP_50(0x64, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0489
    ChrTalk(
        0x101,
        (
            "#5P#12500Fそれじゃあ、\x01",
            "この『ホワイトストーン』は\x01",
            "キーアにプレゼントするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0490
    ChrTalk(
        0xE,
        "#12P#13210Fえっ、ホントにいいのー！？\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x101,
        (
            "#5P#12500Fああ、もちろんだ。\x02\x03",

            "#12509Fせっかくビーチに来たんだし、\x01",
            "その思い出にするといい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0492
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはキーアに\x01",
            "大きな『ホワイトストーン』を渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0493
    ChrTalk(
        0xE,
        "#12P#13209Fえへへ、大事にするねー！！\x02",
    )

    CloseMessageWindow()
    OP_93(0xF, 0xB4, 0x1F4)

    #C0494
    ChrTalk(
        0xF,
        "#12P#13606F#11Pちぇっ、いいなあ……\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x101,
        (
            "#5P#12500Fゴメンな、シュリ。\x01",
            "君はキーアよりお姉さんだから、\x01",
            "今回は我慢してくれるかな？\x02",
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
            "#12P#13612Fベ、別に……\x01",
            "そんな石ころ欲しくなかったし！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C1, 0)
    SubItemNumber(0x32C, 1)
    Jump("loc_E422")

    label("loc_E1E3")

    OP_50(0x6F, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0497
    ChrTalk(
        0x101,
        (
            "#5P#12500Fそれじゃあ、\x01",
            "この『ホワイトストーン』は\x01",
            "シュリにプレゼントするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0498
    ChrTalk(
        0xF,
        "#12P#13605Fえっ……い、いいのか？\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x101,
        (
            "#5P#12500Fああ、もちろんだ。\x02\x03",

            "#12509Fせっかくビーチに来たんだし、\x01",
            "その思い出にするといい。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0500
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはシュリに\x01",
            "大きな『ホワイトストーン』を渡した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0501
    ChrTalk(
        0xF,
        "#12P#13612Fフ、フン……ありがとよ。\x02",
    )

    CloseMessageWindow()
    OP_93(0xE, 0x0, 0x1F4)

    #C0502
    ChrTalk(
        0xE,
        (
            "#12P#13209F#6Pよかったねー、シュリ！\x01",
            "あとで触らせてねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x101,
        (
            "#5P#12500Fゴメンな、キーア。\x01",
            "代わりに今度、新しい本でも\x01",
            "買ってきてあげるからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xE, 0x10E, 0x1F4)

    #C0504
    ChrTalk(
        0xE,
        (
            "#12P#13200Fあ、うん！\x01",
            "楽しみにしてるねー！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14E, 2)
    SubItemNumber(0x32C, 1)

    label("loc_E422")

    Jump("loc_E73B")

    label("loc_E427")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E556")
    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0505
    ChrTalk(
        0xE,
        (
            "#12P#13205Fおおー、\x01",
            "みんなおんなじくらいだねー！\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0xF,
        (
            "#12P#13600Fああ……どれも大きさは\x01",
            "大して変わらないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x101,
        (
            "#5P#12500Fそれじゃあ、今回は\x01",
            "引き分けって感じかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0xF,
        "#12P#13606Fちぇっ、つまんねー結果だなぁ。\x02",
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x101,
        "#5P#12512Fはは、そう言うなって。\x02",
    )

    CloseMessageWindow()
    Jump("loc_E73B")

    label("loc_E556")

    OP_63(0xE, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0510
    ChrTalk(
        0xE,
        (
            "#12P#13200Fわああっ、ロイドの石、\x01",
            "ちっちゃくてかわいー！！\x02",
        )
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0xF,
        "#12P#13600Fああ……かなり小さいな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0512
    ChrTalk(
        0x101,
        (
            "#5P#12512Fは、ははは……\x01",
            "どうやら負けちゃったみたいだな。\x02\x03",

            "#12500Fキーアとシュリのは\x01",
            "同じくらいみたいだし、\x01",
            "今回は２人の勝ちってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0xE,
        "#12P#13209Fわーい、やったー！！\x02",
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0xF,
        (
            "#12P#13606Fちぇっ、なんだか\x01",
            "余裕を見せやがって。\x02\x03",

            "#13602Fフフ、内心はかなり\x01",
            "悔しがってたりしてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x101,
        (
            "#5P#12506Fぐっ……\x01",
            "そ、そんなことないから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E73B")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0516
    ChrTalk(
        0x101,
        (
            "#5P#12500Fそうだ……キーア、シュリ。\x01",
            "なにか冷たいものとかいらないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0xE,
        "#12P#13200Fえ、ロイド持ってきてくれるのー？\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x101,
        (
            "#5P#12504Fああ、ずっと水辺で遊んでて、\x01",
            "そろそろ疲れてるだろう？\x02\x03",

            "#12500F飲み食いしたい物があったら、\x01",
            "遠慮なく言ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0xF,
        "#12P#13600Fふーん、気が利くじゃん。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0xE,
        "#12P#13204Fん～……それじゃあね～……\x02",
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0521
    ChrTalk(
        0xE,
        (
            "#12P#13210Fあ、売店にあった\x01",
            "アイスクリームが食べたいかもー！\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#5P#12500Fアイスクリームか……\x01",
            "はは、分かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0xF,
        (
            "#12P#13604Fじゃあ、オレもそれで。\x02\x03",

            "#13600Fああでも、もうちょい遊んでたいから\x01",
            "すぐには持ってこなくていいからな？\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x101,
        (
            "#5P#12500Fああ、了解。\x01",
            "それじゃあまた後でな。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15D, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EA79")
    Call(0, 54)

    label("loc_EA79")

    EventEnd(0x5)
    Return()

    # Function_53_D799 end

    def Function_54_EA7C(): pass

    label("Function_54_EA7C")

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
            "#12500Fみんな一通り遊んで、\x01",
            "今はノンビリしているみたいだ。\x02\x03",

            "#12503F……っと、なんだか俺も\x01",
            "喉が渇いてきたな。\x02\x03",

            "#12500Fみんなに冷たい物を買ってくる\x01",
            "約束をしてるし、\x01",
            "そろそろ売店に行ってみるか。\x02\x03",

            "売店は階段を上がったところだ。\x01",
            "……ちょっと覗いてみよう。\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x0, 0)
    SetScenarioFlags(0x15E, 3)
    Return()

    # Function_54_EA7C end

    def Function_55_EBDF(): pass

    label("Function_55_EBDF")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEE7")

    #C0526
    ChrTalk(
        0x22,
        (
            "やあ、いらっしゃい。\x01",
            "貸切のビーチは楽しんでるかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        (
            "#12502F#12Pはは、一通り楽しんできた所です。\x02\x03",

            "あの、色々とまとめて\x01",
            "注文したいんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x22,
        (
            "ああ、さっきちょうど\x01",
            "商品の準備が整ったところだよ。\x01",
            "なんでも注文してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x101,
        "#12500F#12Pえーっと、それじゃ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0530
    ChrTalk(
        0x101,
        (
            "#12506F#12P……あ。\x01",
            "そういえばロッカーに\x01",
            "財布を置いてきちゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x22,
        "ああ、お代は結構さ。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x22,
        (
            "マリアベルさんの言いつけでね。\x01",
            "君たちが貸切の時間帯は飲食代が\x01",
            "全てサービスになってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x101,
        (
            "#12505F#12Pそ、そうだったんですか！？\x02\x03",

            "#12512F至れり尽くせりというか……\x01",
            "マリアベルさんには\x01",
            "頭が上がらないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0534
    ChrTalk(
        0x22,
        "はは、充分感謝するといいよ。\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x22,
        "それじゃ、注文するかい？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_EF46")

    label("loc_EEE7")


    #C0536
    ChrTalk(
        0x22,
        (
            "君たちが貸切の時間帯は飲食代が\x01",
            "全てサービスになってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x22,
        "早速なにか注文するかい？\x02",
    )

    CloseMessageWindow()

    label("loc_EF46")

    FadeToDark(300, 0, 100)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0538
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ここで冷たい物を注文すると\x01",
            "レイクビーチでのイベントが\x01",
            "全て終了します。\x07\x00\x02",
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
            "【冷たい物を注文する】\x01",      # 0
            "【やめておく】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F317")

    #C0539
    ChrTalk(
        0x101,
        (
            "#12500F#12Pええ、よろしくお願いします。\x02\x03",

            "#12503Fえっと、ベルコーラが４つと、\x01",
            "ノンアルコールカクテルが３つ……\x02\x03",

            "#12500Fアイスクリームが２つと、\x01",
            "カキ氷が２つ……ああ、それと\x01",
            "フランクフルトを１つお願いします。\x02",
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
            "一度にそれだけ\x01",
            "持ってくつもりなのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x22,
        (
            "もしかしてキミ……\x01",
            "お人好しすぎて自滅するタイプ？\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        (
            "#12512F#12Pい、いや、はは……\x01",
            "そんなことはないと思うんですけど。\x02",
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
            "──こうしてビーチでの楽しい一時は過ぎて行った。\x02\x03",

            "その後、ロイドたちはお約束の\x01",
            "スイカ割りなどを全員で楽しんでから──\x02\x03",

            "ホテルが届けてくれた\x01",
            "ランチボックスに舌鼓を打ちながら\x01",
            "大いに盛り上がるのだった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0x15E, 4)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 1)), scpexpr(EXPR_END)), "loc_F2D4")
    SubItemNumber(0x32B, 1)

    label("loc_F2D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 2)), scpexpr(EXPR_END)), "loc_F2E2")
    SubItemNumber(0x32B, 1)

    label("loc_F2E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 3)), scpexpr(EXPR_END)), "loc_F2F0")
    SubItemNumber(0x329, 1)

    label("loc_F2F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 4)), scpexpr(EXPR_END)), "loc_F2FE")
    SubItemNumber(0x329, 1)

    label("loc_F2FE")

    AddParty(0x3, 0xFF, 0xFF)
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x22, 0)
    NewScene("t1320", 0, 0, 0)
    IdleLoop()
    Jump("loc_F396")

    label("loc_F317")


    #C0544
    ChrTalk(
        0x101,
        "#12500F#12Pいえ、まだ大丈夫です。\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x22,
        "おっと、そうかい？\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x22,
        (
            "まあ、貸切の時間帯が終わる前に\x01",
            "よろしくおねがいするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F396")

    SetChrPos(0x0, -6770, -1500, 8450, 90)
    OP_4C(0x22, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_55_EBDF end

    def Function_56_F3AE(): pass

    label("Function_56_F3AE")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F3E0")
    SetScenarioFlags(0x31, 2)

    label("loc_F3E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F426")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_F420")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F415")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_F41B")

    label("loc_F415")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_F41B")

    Jump("loc_F426")

    label("loc_F420")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_F426")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F6E3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_F49F")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F47F"),
        (SWITCH_DEFAULT, "loc_F490"),
    )


    label("loc_F47F")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_F49A")

    label("loc_F490")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F49A")

    Jump("loc_F6DE")

    label("loc_F49F")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F4D3")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_F4D3")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_F507"),
        (1, "loc_F60B"),
        (2, "loc_F69C"),
        (SWITCH_DEFAULT, "loc_F6D4"),
    )


    label("loc_F507")

    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_74(0x0, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F538")
    OP_70(0x0, 0x12C)
    OP_71(0x0, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_F548")

    label("loc_F538")

    OP_70(0x0, 0xF0)
    OP_71(0x0, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_F548")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F59E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F59E")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5C1")
    Sound(461, 0, 100, 0)

    label("loc_F5C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F5E1")
    OP_70(0x0, 0x14A)
    OP_71(0x0, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_F5F1")

    label("loc_F5E1")

    OP_70(0x0, 0x10E)
    OP_71(0x0, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_F5F1")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x0, "light", 0x1, 0x1)
    OP_70(0x0, 0x0)
    Jump("loc_F426")

    label("loc_F60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_F67D")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_F640")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_F658")

    label("loc_F640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F653")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_F658")

    label("loc_F653")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_F658")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F697")

    label("loc_F67D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F68D")
    OP_AF(0xFB)
    Jump("loc_F697")

    label("loc_F68D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F697")

    Jump("loc_F6DE")

    label("loc_F69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6B5")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_F6CF")

    label("loc_F6B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_F6C5")
    OP_AF(0xFB)
    Jump("loc_F6CF")

    label("loc_F6C5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6CF")

    Jump("loc_F6DE")

    label("loc_F6D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_F6DE")

    Jump("loc_F426")

    label("loc_F6E3")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_56_F3AE end

    def Function_57_F6F1(): pass

    label("Function_57_F6F1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_F70D")
    Jump("loc_11F20")

    label("loc_F70D")

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

    def lambda_FA72():
        OP_9B(0x0, 0x101, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FA72)
    Sleep(0)

    def lambda_FA8A():
        OP_9B(0x0, 0x104, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FA8A)
    Sleep(0)

    def lambda_FAA2():
        OP_9B(0x0, 0x105, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FAA2)
    Sleep(0)
    Sleep(5500)
    #Sound(2757, 255, 100, 0)    #voice#Randy
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0547
    ChrTalk(
        0x104,
        "#12809F#5P#10A#4Sヒューッ！！\x02",
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
            "#12502F#5P凄いな、これは……\x02\x03",

            "#12509Fビーチなんて初めてだけど\x01",
            "こんな綺麗だとは思わなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x105,
        (
            "#12904F#5P普通のビーチは海沿いだし\x01",
            "砂もこんなに白くはないかな。\x02\x03",

            "#12902F多分、大陸中東部にある\x01",
            "『ホワイトヘヴン』って砂浜から\x01",
            "砂を運んできたんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_FC84():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_FC84)
    Sleep(50)

    def lambda_FC94():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FC94)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)

    #C0550
    ChrTalk(
        0x101,
        "#12511F#12Pマジか……\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x104,
        "#12806F#6Pあり得なさすぎだろ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0552
    ChrTalk(
        0x105,
        (
            "#12909F#5Pフフ、改めてＩＢＣの\x01",
            "資産力が垣間見れるよね。\x02\x03",

            "#12900Fそれより、女性陣が来る前に\x01",
            "準備した方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x104,
        (
            "#12800F#6Pおお、そうだな。\x02\x03",

            "#12809Fやっぱビーチに\x01",
            "パラソルとかは定番だろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#12504F#12Pなるほど、雑誌とかでも\x01",
            "そんな写真があった気がする。\x02\x03",

            "#12500Fよし、手分けして設置するか。\x02",
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
        "#12504F#12Pふう、こんなもんかな。\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x104,
        "#12800F#11Pああ、いんじゃね？\x02",
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x105,
        (
            "#12902F#6P上出来、上出来。\x02\x03",

            "#12909Fそれじゃあ早速、\x01",
            "僕は休ませてもらおうかな。\x02",
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
        "#12506F#12Pあのな……\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x104,
        (
            "#12801F#11P何だか俺以上に\x01",
            "遊び慣れてやがるな……\x02",
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
        "キーアの声",
        "#10Aロイドー！\x02",
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
        "#12502F#12Pあ……\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x104,
        "#12802F#11Pお、来たみてぇだな。\x02",
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
            "#13209F#11Pスゴイねえ！\x01",
            "まっしろだよー！\x02",
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
            "#12705F#11P確かに……\x01",
            "これは驚きです。\x02",
        )
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0xA,
        (
            "#12602F#11Pベルったら……\x01",
            "いつの間にこんなものを。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xC, 0x10E, 0x1F4)
    Sleep(100)

    #C0566
    ChrTalk(
        0xC,
        (
            "#13109F#6Pほら、お姉ちゃん！\x01",
            "早く早く～！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(16000, -5000, -2500, 4000)

    def lambda_102A4():

        label("loc_102A4")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_102A4")

    QueueWorkItem2(0xE, 2, lambda_102A4)

    def lambda_102B6():

        label("loc_102B6")

        TurnDirection(0xFE, 0x12, 400)
        Yield()
        Jump("loc_102B6")

    QueueWorkItem2(0xA, 2, lambda_102B6)

    def lambda_102C8():

        label("loc_102C8")

        TurnDirection(0xFE, 0x12, 500)
        Yield()
        Jump("loc_102C8")

    QueueWorkItem2(0xB, 2, lambda_102C8)

    def lambda_102DA():

        label("loc_102DA")

        TurnDirection(0xFE, 0x12, 600)
        Yield()
        Jump("loc_102DA")

    QueueWorkItem2(0xC, 2, lambda_102DA)
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
            "#13012F#5Pもう、フランったら。\x01",
            "ビーチは逃げないでしょ。\x02",
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

    def lambda_10483():
        OP_9B(0x0, 0xE, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_10483)
    Sleep(50)

    def lambda_1049B():
        OP_9B(0x0, 0xC, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_1049B)
    Sleep(50)

    def lambda_104B3():
        OP_9B(0x0, 0xA, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_104B3)
    Sleep(50)

    def lambda_104CB():
        OP_9B(0x0, 0xB, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_104CB)
    Sleep(50)

    def lambda_104E3():
        OP_9B(0x0, 0x12, 0x0, 0x1F40, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_104E3)
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
        "#3613V#30Wえへへ、お待たせー。\x02",
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
            "#3395V#30Wふふ、わざわざパラソルを\x01",
            "用意してくれたんだ？\x02",
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
        "#2677V#30Wさすが、気が利きますね。\x02",
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

    def lambda_10848():
        OP_98(0xFE, 0xFFFFFF9C, 0x0, 0xC8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10848)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_10877():
        OP_98(0xFE, 0xFFFFFF6A, 0x0, 0x1C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_10877)
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
            "#2716V#40Wほら、おねえちゃん。\x01",
            "#30Wせっかくだから前に出て\x01",
            "アピールしなきゃ！\x02",
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
            "#3516V#30Wちょ、ちょっと。\x01",
            "そんな押さないでってば！\x02",
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
            "#12809F#11Pほっほう！\x01",
            "いいじゃんいいじゃん！\x02",
        )
    )

    CloseMessageWindow()

    #C0575
    ChrTalk(
        0x105,
        "#12902F#11Pへえ、みんな似合ってるねぇ。\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0xA,
        "#12609F#6Pそ、そうかしら。\x02",
    )

    CloseMessageWindow()

    #C0577
    ChrTalk(
        0xB,
        "#12706F#6Pあまり自信はありませんが……\x02",
    )

    CloseMessageWindow()

    #C0578
    ChrTalk(
        0xC,
        (
            "#13109F#5Pえへへ～、ロイドさん。\x02\x03",

            "誰の水着姿が\x01",
            "いちばん似合ってますかー？\x02",
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
        "#12511F#11Pええっ！？\x02",
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x12,
        (
            "#13001F#6Pもう、フラン……！\x01",
            "ロイドさんを困らせないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x105,
        (
            "#12902F#5Pフフ、どうしたんだい？\x01",
            "さっきからボーッとしてるけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x5A, 0x1F4)

    #C0582
    ChrTalk(
        0x104,
        (
            "#12809F#5Pハッハッハッ。\x01",
            "さすがに刺激が強すぎか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0583
    ChrTalk(
        0x101,
        (
            "#12504F#11Pハハ……\x01",
            "うん、ちょっと目の毒かな。\x02\x03",

            "#12502F#11P──みんな、物凄く\x01",
            "似合っててビックリしたよ。\x02\x03",

            "#12509Fそのままグラビア写真とか\x01",
            "撮られてもおかしくないくらいだ。\x02",
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
        "#13209F#6Pえへへ～、ありがとー！\x02",
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0xA,
        "#12612F#6Pロ、ロイド……\x02",
    )

    CloseMessageWindow()

    #C0586
    ChrTalk(
        0x12,
        "#13014F#6Pえ、えっ……！？\x02",
    )

    CloseMessageWindow()

    #C0587
    ChrTalk(
        0xC,
        "#13106F#5Pくっ、さすがはロイドさん……\x02",
    )

    CloseMessageWindow()

    #C0588
    ChrTalk(
        0xB,
        "#12711F#6P……やはりタチが悪いです。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0589
    ChrTalk(
        0x101,
        "#12505F#11Pあれっ……？\x02",
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
            "#12806F#5P（こいつ……\x01",
            "  いつかゼッテー身を滅ぼすな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x105,
        "#12902F#5P（ま、それも男子の本懐じゃない？）\x02",
    )

    CloseMessageWindow()

    #N0592
    NpcTalk(
        0x10,
        "女性の声",
        "やっほー、お待たせー。\x02",
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
        "#13405F#11Pうっわ、これは凄いわね！\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x8,
        (
            "#13309F#11Pふふっ……\x01",
            "天国みたいな場所ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0595
    ChrTalk(
        0x9,
        "#13509F#11P一面真っ白です……！\x02",
    )

    CloseMessageWindow()

    #C0596
    ChrTalk(
        0xF,
        "#13605F#11P……へえ………\x02",
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

    def lambda_112F5():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_112F5)

    def lambda_1130A():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1130A)

    def lambda_1131F():
        OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1131F)

    def lambda_11334():
        OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_11334)

    def lambda_11349():

        label("loc_11349")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_11349")

    QueueWorkItem2(0xE, 2, lambda_11349)

    def lambda_1135B():

        label("loc_1135B")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_1135B")

    QueueWorkItem2(0xA, 2, lambda_1135B)

    def lambda_1136D():

        label("loc_1136D")

        TurnDirection(0xFE, 0x10, 500)
        Yield()
        Jump("loc_1136D")

    QueueWorkItem2(0xB, 2, lambda_1136D)

    def lambda_1137F():

        label("loc_1137F")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_1137F")

    QueueWorkItem2(0x12, 2, lambda_1137F)

    def lambda_11391():

        label("loc_11391")

        TurnDirection(0xFE, 0x8, 500)
        Yield()
        Jump("loc_11391")

    QueueWorkItem2(0xC, 2, lambda_11391)
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
        "ふふっ、お待たせ。\x02",
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
            "お、もう可愛い子たちに\x01",
            "囲まれてるじゃないの～。\x02",
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
            "#3245V#30Wあ、パラソルとか\x01",
            "用意してくださったんですね。\x02",
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
            "……言ってくれりゃあ\x01",
            "オレがやったのに。\x02",
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
        "#13205F#5Pほえ～……\x02",
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0xA,
        "#12606F#5P……な、何だか……\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x12,
        (
            "#13012F#11P#N綺麗というか……\x01",
            "圧倒されるというか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0606
    ChrTalk(
        0xB,
        (
            "#12706F#5Pオーラが違う……\x01",
            "……そんな感じですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xC,
        "#13101F#11Pす、すごいですっ……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x10, 0xB4, 0x1F4)

    #C0608
    ChrTalk(
        0x10,
        (
            "#13402F#6Pあら、貴女たちだって\x01",
            "なかなかイケてるじゃない。\x02\x03",

            "#13409Fうんうん、眼福眼福㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xB4, 0x1F4)

    #C0609
    ChrTalk(
        0x8,
        (
            "#13304F#12Pふふ、そうね。\x02\x03",

            "#13302Fエリィちゃんも思った通り\x01",
            "すっごくグラマーだし。\x02\x03",

            "#13309Fキーアちゃんもティオちゃんも\x01",
            "抱きしめちゃいたいくらいだわ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0xA,
        (
            "#12609F#5Pあ、あはは……\x01",
            "（セシルさんの胸で言われても。）\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0xE,
        "#13209F#5Pえへへ、ホントー？\x02",
    )

    CloseMessageWindow()
    OP_64(0x9)

    #C0612
    ChrTalk(
        0x9,
        (
            "#13509F#11Pふふっ……でも、\x01",
            "本当に綺麗なビーチですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0613
    ChrTalk(
        0xF,
        (
            "#13604F#11Pま、まあ悪くないかな……\x02\x03",

            "#13601F──って、アンタら、\x01",
            "いつまでボケッとしてんだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x10)
    OP_64(0x8)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_11AF3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_11AF3)

    def lambda_11B00():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_11B00)

    def lambda_11B0D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11B0D)

    def lambda_11B1A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_11B1A)

    def lambda_11B27():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_11B27)

    def lambda_11B34():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_11B34)

    def lambda_11B41():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_11B41)
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
        "#12511F#6P#Nハッ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0615
    ChrTalk(
        0x104,
        (
            "#12806F#12P#Nあぶねえあぶねえ……\x01",
            "一瞬アッチの世界に行ってたぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0616
    ChrTalk(
        0xB,
        "#12711F#5P男って単純ですね。\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0x105,
        (
            "#12909F#12Pま、女性に比べたら\x01",
            "シンプルな生き物だよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0xC,
        (
            "#13106F#11Pむむっ……\x01",
            "これは負けてられないかも。\x02\x03",

            "#13101Fお姉ちゃん、頑張ろうね！\x02",
        )
    )

    CloseMessageWindow()

    #C0619
    ChrTalk(
        0x12,
        "#13012F#5P#Nむ、無茶言わないでよ～。\x02",
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
            "その後、準備体操をしてから\x01",
            "それぞれビーチで自由行動となり……\x02\x03",

            "ロイドはリーシャと共に\x01",
            "キーアとシュリに泳ぎの練習を\x01",
            "付けてあげることにした。\x07\x00\x02",
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

    label("loc_11F20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1223E")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1206F")
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
    Jump("loc_120CE")

    label("loc_1206F")

    SetChrPos(0x11, 20720, -6000, -18530, 180)
    SetChrFlags(0x11, 0x10)
    SetChrPos(0x12, 20720, -6000, -20070, 0)
    SetChrFlags(0x12, 0x10)
    SetChrPos(0x10, 26710, -6000, -12660, 135)
    SetChrPos(0x13, 14500, -6000, -5300, 135)
    SetChrPos(0x14, 25950, -6000, -13400, 0)

    label("loc_120CE")

    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12135")
    SetChrPos(0xB, 32360, -6120, 7690, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 31000, -6020, 6450, 90)
    SetChrChipByIndex(0xC, 0x16)
    SetChrSubChip(0xC, 0x0)
    EndChrThread(0xC, 0x0)
    SetChrBattleFlags(0xC, 0x4)
    SetChrPos(0xD, 33170, -6160, 9360, 180)
    Jump("loc_1216D")

    label("loc_12135")

    SetChrPos(0xB, 32460, -6150, 9460, 180)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0xC, 30460, -6010, 6150, 90)
    SetChrPos(0xD, 32460, -6150, 8360, 0)

    label("loc_1216D")

    SetChrFlags(0xD, 0x10)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 7)), scpexpr(EXPR_END)), "loc_121BE")
    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)
    Jump("loc_12228")

    label("loc_121BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15C, 0)), scpexpr(EXPR_END)), "loc_121FA")
    SetChrPos(0xE, 58610, -7350, 1880, 0)
    BeginChrThread(0xE, 0, 0, 4)
    SetChrPos(0xF, 62000, -7380, -21040, 0)
    BeginChrThread(0xF, 0, 0, 5)
    Jump("loc_12228")

    label("loc_121FA")

    SetChrPos(0xE, 45610, -7090, 1880, 0)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xF, 45610, -7090, 3000, 180)
    BeginChrThread(0xF, 0, 0, 0)

    label("loc_12228")

    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x21, 55710, -2000, -36910, 45)

    label("loc_1223E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1229D")
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

    label("loc_1229D")

    ClearMapObjFlags(0xA, 0x4)
    OP_70(0xA, 0x0)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_122F3")
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

    label("loc_122F3")

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
            "#12502F#5Pお、いいなキーア。\x02\x03",

            "#12509Fその調子、その調子。\x02",
        )
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0xE,
        (
            "#13209F#12Pえへへ、そうー？\x02\x03",

            "#13201Fあ……\x01",
            "なんか分かってきたかも。\x02\x03",

            "#13210Fロイド、手をはなしてー。\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x101,
        (
            "#12511F#5Pだ、大丈夫か？\x02\x03",

            "#12501Fそれじゃ──\x02",
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

    def lambda_1255E():

        label("loc_1255E")

        TurnDirection(0xFE, 0xE, 500)
        Yield()
        Jump("loc_1255E")

    QueueWorkItem2(0x101, 2, lambda_1255E)
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
        "#13505F#11Pあら。\x02",
    )

    CloseMessageWindow()

    #C0625
    ChrTalk(
        0x101,
        (
            "#12505F#5Pおおっ！\x02\x03",

            "#12502Fキーア、やっぱり泳いだ事、\x01",
            "あったんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0xE,
        "#13200F#12P#Nんー、分からないけど。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0627
    ChrTalk(
        0xF,
        (
            "#13605F#11Pや、やるじゃんチビ……\x02\x03",

            "#13607Fリーシャ姉！\x01",
            "オレにもコツ教えてっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0x9,
        (
            "#13509F#5Pふふっ、はいはい。\x02\x03",

            "#13502Fそうね、ちょっと上半身に\x01",
            "力が入りすぎているから……\x02",
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

    def lambda_1271F():

        label("loc_1271F")

        TurnDirection(0xFE, 0xF, 500)
        Yield()
        Jump("loc_1271F")

    QueueWorkItem2(0x9, 2, lambda_1271F)
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
            "#12509F#5Pなんだ、２人とも\x01",
            "あっという間だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xE,
        "#13204F#12P#Nえっへん。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0631
    ChrTalk(
        0xF,
        (
            "#13612F#11P#Nフ、フン。\x02\x03",

            "こんなの出来るように\x01",
            "なったってイミねーし……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0632
    ChrTalk(
        0xE,
        (
            "#13210F#12P#Nねえねえ、シュリ！\x02\x03",

            "あっちの岩まで泳ごー！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0633
    ChrTalk(
        0xF,
        "#13611F#11P#Nな、なんでオレが……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0634
    ChrTalk(
        0x101,
        (
            "#12509F#5Pハハ、気を付けてな。\x02\x03",

            "#12500F２人とも、岩より向こうには\x01",
            "絶対に行ったらダメだぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xE,
        "#13209F#12P#Nらじゃー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0636
    ChrTalk(
        0xF,
        (
            "#13607F#11P#Nああもう！\x01",
            "付き合えばいいんだろ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(225, 20, 0, 5000)
    SetCameraDistance(13000, 5000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_12971")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12988")
    Sleep(1)
    Jump("loc_12971")

    label("loc_12988")

    EndChrThread(0xE, 0x3)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    Fade(1000)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x9, 0x8)
    SetChrPos(0xE, 64510, -7460, 28680, 75)
    SetChrPos(0xF, 62580, -7430, 29030, 75)

    def lambda_129CE():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_129CE)

    def lambda_129E3():
        OP_9B(0x1, 0xFE, 0x0, 0x3A98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_129E3)
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
        "#12512F#11Pうーん、大丈夫かな？\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x9,
        (
            "#13509F#11Pふふ、このあたりは\x01",
            "かなり浅いみたいですから\x01",
            "大丈夫ですよ。\x02\x03",

            "#13502Fそれにしても……\x01",
            "キーアちゃん、凄いですね。\x02\x03",

            "あっという間にコツを\x01",
            "掴んじゃったみたいですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)

    #C0639
    ChrTalk(
        0x101,
        (
            "#12504F#6P前にも泳げていたのを\x01",
            "身体が思い出しただけかも\x01",
            "しれないけどね。\x02\x03",

            "#12500Fでも、シュリも結構すごいよな？\x02\x03",

            "今まで一度も、泳いだことが\x01",
            "無いって言ってたのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0640
    ChrTalk(
        0x9,
        (
            "#13504F#11Pここ最近の練習で\x01",
            "身体のバネとしなやかさが\x01",
            "相当鍛えられていますから。\x02\x03",

            "#13502Fちょっとコツを教えたら\x01",
            "あっという間でしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x101,
        (
            "#12504F#6Pそうか……\x01",
            "頑張っているみたいだな。\x02\x03",

            "#12505Fそういえば……\x01",
            "アルカンシェルの舞台、\x01",
            "リニューアルするんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0642
    ChrTalk(
        0x9,
        (
            "#13505F#11Pはい、リニューアルといっても\x01",
            "『金の太陽、銀の月』であるのは\x01",
            "変わらないんですけど……\x02\x03",

            "#13502Fシュリちゃんが新たな\x01",
            "第三の『姫』として登場する\x01",
            "アレンジが入っているんです。\x02\x03",

            "#13509F彼女がメインのシーンなんかも\x01",
            "追加されているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_12F3B")

    #C0643
    ChrTalk(
        0x101,
        (
            "#12511F#6Pそりゃ凄いな……\x02\x03",

            "#12512Fまさか最初に会った時は\x01",
            "こんなに早く活躍するなんて\x01",
            "思わなかったけれど……\x02",
        )
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x9,
        (
            "#13509F#11Pふふっ、そうですね。\x02\x03",

            "#13510F多分、イリアさんの導きと\x01",
            "シュリちゃん自身の頑張りが\x01",
            "あったからだと思います。\x02\x03",

            "#13508F……私なんかよりずっと……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13064")

    label("loc_12F3B")


    #C0645
    ChrTalk(
        0x101,
        (
            "#12505F#6Pそりゃ凄いな……\x02\x03",

            "#12501F何でも、最初はイリアさんに\x01",
            "反発して事件を起こそうと\x01",
            "してたんだって？\x02",
        )
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0x9,
        (
            "#13504F#11P事件というほど大げさな\x01",
            "ものではなかったですけど……\x02\x03",

            "#13510F多分、イリアさんの導きと\x01",
            "シュリちゃん自身の頑張りが\x01",
            "あったからだと思います。\x02\x03",

            "#13508F……私なんかよりずっと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13064")


    #C0647
    ChrTalk(
        0x101,
        "#12505F#6Pえ……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x9)

    #C0648
    ChrTalk(
        0x9,
        (
            "#13509F#11Pあはは、大したことじゃ……\x02\x03",

            "#13510Fその、ちょっと疲れたので\x01",
            "向こうで休んでいますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x101,
        (
            "#12504F#6Pそっか、お疲れ。\x02\x03",

            "#12500Fまだまだ時間はあるから\x01",
            "ノンビリ楽しんでいこう。\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x9,
        "#13509F#11Pはい……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(57250, -5600, 29000, 6000)
    MoveCamera(235, 10, 0, 6000)
    SetCameraDistance(13500, 6000)
    OP_93(0x9, 0x10E, 0x1F4)

    def lambda_131A0():
        OP_9B(0x0, 0xFE, 0x0, 0x9470, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_131A0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0651
    ChrTalk(
        0x101,
        (
            "#12503F#6P（うーん、それにしても\x01",
            "  背はそんな高くないのに相当……）\x02\x03",

            "#12511F（──じゃなくて。）\x02\x03",

            "#12500F（まだ正午まで時間はあるし、\x01",
            "  俺もみんなに混ぜてもらおうかな？）\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_133DA")
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

    label("loc_133DA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_133EF")
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)

    label("loc_133EF")

    OP_90(0x0, 40000, 0, 17000, 270)
    SetScenarioFlags(0x145, 0)
    OP_29(0xA5, 0x1, 0x3)
    ModifyEventFlags(1, 3, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_57_F6F1 end

    def Function_58_13416(): pass

    label("Function_58_13416")

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

    # Function_58_13416 end

    def Function_59_134A5(): pass

    label("Function_59_134A5")

    Sound(812, 0, 100, 0)
    OP_A1(0xFE, 0x546, 0x5, 0x10, 0x11, 0x12, 0x13, 0x14)
    Sound(318, 0, 40, 0)
    Return()

    # Function_59_134A5 end

    def Function_60_134BD(): pass

    label("Function_60_134BD")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0xBB8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_60_134BD end

    def Function_61_134E8(): pass

    label("Function_61_134E8")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_61_134E8 end

    def Function_62_13513(): pass

    label("Function_62_13513")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6000, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_62_13513 end

    def Function_63_1353E(): pass

    label("Function_63_1353E")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 7500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_63_1353E end

    def Function_64_13569(): pass

    label("Function_64_13569")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4500, 0, -1500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_64_13569 end

    def Function_65_13594(): pass

    label("Function_65_13594")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 8000, 0, -3000, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_65_13594 end

    def Function_66_135BF(): pass

    label("Function_66_135BF")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 6500, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2904, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_66_135BF end

    def Function_67_135EA(): pass

    label("Function_67_135EA")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 5500, 0, -3500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_67_135EA end

    def Function_68_13615(): pass

    label("Function_68_13615")

    ClearChrFlags(0xFE, 0x4)
    OP_90(0xFE, 4000, 0, -2500, 90)
    OP_9B(0x0, 0xFE, 0x0, 0x2CEC, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_68_13615 end

    def Function_69_13640(): pass

    label("Function_69_13640")

    OP_93(0xFE, 0xF, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
    Return()

    # Function_69_13640 end

    def Function_70_13657(): pass

    label("Function_70_13657")

    OP_98(0xFE, 0x4B0, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_70_13657 end

    def Function_71_1366C(): pass

    label("Function_71_1366C")

    OP_98(0xFE, 0xFFFFFB50, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_71_1366C end

    def Function_72_13681(): pass

    label("Function_72_13681")

    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x3E8, 0x0)
    Return()

    # Function_72_13681 end

    def Function_73_13696(): pass

    label("Function_73_13696")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13775")
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
    Jump("Function_73_13696")

    label("loc_13775")

    Return()

    # Function_73_13696 end

    def Function_74_13776(): pass

    label("Function_74_13776")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13858")
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
    Jump("Function_74_13776")

    label("loc_13858")

    Return()

    # Function_74_13776 end

    def Function_75_13859(): pass

    label("Function_75_13859")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13938")
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
    Jump("Function_75_13859")

    label("loc_13938")

    Return()

    # Function_75_13859 end

    def Function_76_13939(): pass

    label("Function_76_13939")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13A1B")
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
    Jump("Function_76_13939")

    label("loc_13A1B")

    Return()

    # Function_76_13939 end

    def Function_77_13A1C(): pass

    label("Function_77_13A1C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13A7F")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60080, -6950, 27560)
    OP_9F(0x1, 61500, -6850, 28810)
    OP_9F(0x1, 60190, -7050, 30310)
    OP_9F(0x1, 58950, -7150, 29090)
    OP_9F(0x1, 59200, -7250, 28000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("Function_77_13A1C")

    label("loc_13A7F")

    Return()

    # Function_77_13A1C end

    def Function_78_13A80(): pass

    label("Function_78_13A80")

    SetChrPos(0xFE, 58250, -6850, 29000, 0)

    label("loc_13A91")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13AEA")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 60250, -6750, 31000)
    OP_9F(0x1, 58250, -7200, 33000)
    OP_9F(0x1, 56250, -7250, 31000)
    OP_9F(0x1, 58250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Jump("loc_13A91")

    label("loc_13AEA")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6850, 29000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    Return()

    # Function_78_13A80 end

    def Function_79_13B10(): pass

    label("Function_79_13B10")

    SetChrPos(0xFE, 58250, -6950, 30000, 0)

    label("loc_13B21")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_13B7A")
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 59250, -6950, 31000)
    OP_9F(0x1, 58250, -7250, 32000)
    OP_9F(0x1, 57250, -7250, 31000)
    OP_9F(0x1, 58250, -6950, 30000)
    OP_9F(0x2, 0xFE, 1000, 0x6)
    Jump("loc_13B21")

    label("loc_13B7A")

    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 67250, -6950, 30000)
    OP_9F(0x2, 0xFE, 2000, 0x6)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_79_13B10 end

    def Function_80_13BA0(): pass

    label("Function_80_13BA0")

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
            "──こうしてビーチでの\x01",
            "楽しい一時は過ぎて行った。\x07\x00\x02",
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
            "その後、ロイドたちはお約束の\x01",
            "スイカ割りなどを楽しんでから──\x07\x00\x02",
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
            "ホテルが届けてくれた\x01",
            "ランチボックスに舌鼓を打ちながら\x01",
            "大いに盛り上がるのだった。\x07\x00\x02",
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

    # Function_80_13BA0 end

    def Function_81_13CF7(): pass

    label("Function_81_13CF7")

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

    def lambda_1412C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1412C)
    Sleep(30)

    def lambda_14144():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_14144)
    Sleep(30)

    def lambda_1415C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1415C)
    Sleep(30)

    def lambda_14174():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_14174)
    Sleep(30)

    def lambda_1418C():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1418C)
    Sleep(30)

    def lambda_141A4():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_141A4)
    Sleep(30)

    def lambda_141BC():
        OP_9B(0x0, 0xFE, 0x5, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_141BC)
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
        "神狼ツァイト",
        (
            "#01203F#3C#5Pさて、私はテーマパークの方で\x01",
            "せいぜい暴れて来よう。\x02\x03",

            "#01200F元の姿に戻ったら合図をするので\x01",
            "隙を突いて屋敷に向かうがいい。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_142FB():
        TurnDirection(0x101, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_142FB)
    Sleep(50)

    def lambda_1430B():
        TurnDirection(0x103, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1430B)
    Sleep(50)

    def lambda_1431B():
        TurnDirection(0x104, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1431B)
    Sleep(50)

    def lambda_1432B():
        TurnDirection(0x105, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1432B)
    Sleep(50)

    def lambda_1433B():
        TurnDirection(0x109, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1433B)
    Sleep(50)

    def lambda_1434B():
        TurnDirection(0x106, 0xD, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_1434B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x106, 0)

    #C0656
    ChrTalk(
        0x101,
        "#00013F#6P分かった。\x02",
    )

    CloseMessageWindow()

    #C0657
    ChrTalk(
        0x103,
        (
            "#00208F#12Pツァイト……\x01",
            "どうか気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #N0658
    NpcTalk(
        0xD,
        "神狼ツァイト",
        (
            "#01200F#3C#5Pフフ、おぬしらの方もな。\x02\x03",

            "#01203F女神の加護を。\x02",
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

    def lambda_1445B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1445B)

    def lambda_14468():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_14468)

    def lambda_14475():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_14475)

    def lambda_14482():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_14482)

    def lambda_1448F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_1448F)

    def lambda_1449C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1449C)
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
        "#10409F#11Pハハ、頼もしいねぇ。\x02",
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0x104,
        (
            "#00307F#12Pよし、こっちもまずは\x01",
            "ホテルのアーケードまで──\x02",
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
        "男の声",
        "#2S#2Pいたぞ……！\x02",
    )

    CloseMessageWindow()

    #N0662
    NpcTalk(
        0x18,
        "男の声",
        "#2S#2Pバニングスたちだ！\x02",
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

    def lambda_1466F():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1466F)
    Sleep(50)

    def lambda_1467F():
        OP_93(0x103, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1467F)
    Sleep(50)

    def lambda_1468F():
        OP_93(0x104, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1468F)
    Sleep(50)

    def lambda_1469F():
        OP_93(0x105, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1469F)
    Sleep(50)

    def lambda_146AF():
        OP_93(0x109, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_146AF)
    Sleep(50)

    def lambda_146BF():
        OP_93(0x106, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_146BF)
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
            "#00310F#11Pチッ……\x01",
            "もう来やがったか！\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x109,
        "#10107F#11P敵猟兵３、軍用魔獣３！\x02",
    )

    CloseMessageWindow()

    #C0665
    ChrTalk(
        0x106,
        (
            "#10701F#12Pどうやらかなりの\x01",
            "精鋭のようです……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0666
    ChrTalk(
        0x101,
        (
            "#00007F#11P迎撃用意！\x01",
            "連携して撃破するぞ！\x02",
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
        "#00307F#1K#1P#Nおおっ！\x02",
    )


    #C0668
    ChrTalk(
        0x105,
        "#10407F#1K#2P#Nああ！\x02",
    )


    #C0669
    ChrTalk(
        0x109,
        "#10107F#1K#4P#Nはい！\x02",
    )


    #N0670
    NpcTalk(
        0x101,
        "リーシャ",
        "#10707F#1K#3P#Nはいっ！\x02",
    )

    SetMessageWindowPos(180, 70, -1, -1)

    #A0671
    AnonymousTalk(
        0x103,
        "#00201F#1K#Nはい！\x02",
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

    def lambda_149E0():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_149E0)

    def lambda_149F5():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_149F5)

    def lambda_14A0A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_14A0A)

    def lambda_14A1F():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_14A1F)

    def lambda_14A34():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_14A34)

    def lambda_14A49():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_14A49)
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

    # Function_81_13CF7 end

    def Function_82_14ADC(): pass

    label("Function_82_14ADC")

    BeginChrThread(0xFE, 0, 0, 86)
    OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_82_14ADC end

    def Function_83_14AFB(): pass

    label("Function_83_14AFB")


    def lambda_14B00():
        OP_96(0xFE, 0xAFC8, 0xFFFFE458, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14B00)
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

    # Function_83_14AFB end

    def Function_84_14B5B(): pass

    label("Function_84_14B5B")

    BeginChrThread(0xFE, 0, 0, 87)
    OP_75(0x2, 0x2, 0x0)
    SetChrPos(0xFE, 45000, -1000, 30000, 270)
    OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
    EndChrThread(0xFE, 0x0)
    Return()

    # Function_84_14B5B end

    def Function_85_14B92(): pass

    label("Function_85_14B92")

    SetChrPos(0xFE, 45000, -1000, 30000, 270)

    def lambda_14BA8():
        OP_96(0xFE, 0xAFC8, 0x3A98, 0x7530, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14BA8)
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

    # Function_85_14B92 end

    def Function_86_14C0C(): pass

    label("Function_86_14C0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14C30")
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_86_14C0C")

    label("loc_14C30")

    Return()

    # Function_86_14C0C end

    def Function_87_14C31(): pass

    label("Function_87_14C31")

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

    # Function_87_14C31 end

    def Function_88_14C96(): pass

    label("Function_88_14C96")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14CB1")
    OP_A1(0xFE, 0xBB8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_88_14C96")

    label("loc_14CB1")

    Return()

    # Function_88_14C96 end

    def Function_89_14CB2(): pass

    label("Function_89_14CB2")

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

    # Function_89_14CB2 end

    def Function_90_14DA3(): pass

    label("Function_90_14DA3")

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

    # Function_90_14DA3 end

    def Function_91_14EC2(): pass

    label("Function_91_14EC2")

    SetChrChipByIndex(0xFE, 0x21)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5DC0, 0x1388, 0x0)
    Return()

    # Function_91_14EC2 end

    def Function_92_14EE9(): pass

    label("Function_92_14EE9")

    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x4844, 0x1388, 0x0)
    Return()

    # Function_92_14EE9 end

    def Function_93_14F10(): pass

    label("Function_93_14F10")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14F2E")
    OP_A1(0xFE, 0x6A4, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_93_14F10")

    label("loc_14F2E")

    Return()

    # Function_93_14F10 end

    def Function_94_14F2F(): pass

    label("Function_94_14F2F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_14F4D")
    OP_A1(0xFE, 0xBB8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("Function_94_14F2F")

    label("loc_14F4D")

    Return()

    # Function_94_14F2F end

    def Function_95_14F4E(): pass

    label("Function_95_14F4E")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x57E4, 0x1388, 0x0)
    Return()

    # Function_95_14F4E end

    def Function_96_14F86(): pass

    label("Function_96_14F86")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x5208, 0x1388, 0x0)
    Return()

    # Function_96_14F86 end

    def Function_97_14FBE(): pass

    label("Function_97_14FBE")

    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xFE, 0, 0, 94)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    OP_9B(0x0, 0xFE, 0xFFC4, 0x55F0, 0x1388, 0x0)
    Return()

    # Function_97_14FBE end

    def Function_98_14FF6(): pass

    label("Function_98_14FF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1500F")
    Sound(845, 0, 60, 0)
    Sleep(400)
    Jump("Function_98_14FF6")

    label("loc_1500F")

    Return()

    # Function_98_14FF6 end

    def Function_99_15010(): pass

    label("Function_99_15010")

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
            "#00010F#11Pくっ……\x01",
            "さすがに手強い……！\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x104,
        (
            "#00307F#12P最強クラスの連中だ！\x01",
            "全力で行くしかねぇ……！\x02",
        )
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x103,
        (
            "#00207F#11P急ぎましょう……！\x01",
            "ツァイトの陽動が始まります。\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x101,
        (
            "#00007F#11Pああ、アーケードに出るぞ！\x02\x03",

            "たしか従業員も全員、\x01",
            "退去しているはずだな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x109,
        (
            "#10101F#12Pはい、戦闘に巻き込む\x01",
            "心配はいりません！\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x105,
        (
            "#10402F#12Pだったら存分に\x01",
            "やり合えそうだね……！\x02",
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

    # Function_99_15010 end

    def Function_100_1535D(): pass

    label("Function_100_1535D")

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

    # Function_100_1535D end

    def Function_101_153F7(): pass

    label("Function_101_153F7")

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

    def lambda_158E1():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_158E1)

    def lambda_158F6():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_158F6)

    def lambda_1590B():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1590B)

    def lambda_15920():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_15920)

    def lambda_15935():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_15935)

    def lambda_1594A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1594A)

    def lambda_1595F():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1595F)
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

    # Function_101_153F7 end

    def Function_102_15A09(): pass

    label("Function_102_15A09")

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

    # Function_102_15A09 end

    def Function_103_15B59(): pass

    label("Function_103_15B59")

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

    # Function_103_15B59 end

    def Function_104_15C10(): pass

    label("Function_104_15C10")

    OP_9B(0x0, 0xFE, 0x0, 0x61A8, 0x1770, 0x0)
    Return()

    # Function_104_15C10 end

    def Function_105_15C20(): pass

    label("Function_105_15C20")

    OP_9B(0x0, 0xFE, 0x0, 0x88B8, 0x1770, 0x0)
    Return()

    # Function_105_15C20 end

    def Function_106_15C30(): pass

    label("Function_106_15C30")

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
        "#00005F#11Pこれは……！\x02",
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0x103,
        "#00202F#12Pツァイトの陽動です！\x02",
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

    # Function_106_15C30 end

    def Function_107_15EAD(): pass

    label("Function_107_15EAD")

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

    # Function_107_15EAD end

    def Function_108_15F47(): pass

    label("Function_108_15F47")

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
            "#10702F#11Pテーマパークの方で\x01",
            "戦闘が始まったようです！\x02",
        )
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        (
            "#00007F#5Pよし、この隙に\x01",
            "アーケードを抜けるぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x109,
        "#10107F#12Pイエス・サー！\x02",
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

    # Function_108_15F47 end

    def Function_109_16111(): pass

    label("Function_109_16111")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_1617D")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_16197")

    label("loc_1617D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16191")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_16197")

    label("loc_16191")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_16197")

    LoadChrToIndex("monster/ch87150.itc", 0x23)
    LoadChrToIndex("monster/ch87050.itc", 0x26)
    LoadChrToIndex("monster/ch87250.itc", 0x27)
    LoadChrToIndex("monster/ch87350.itc", 0x28)
    LoadChrToIndex("monster/ch87450.itc", 0x29)
    LoadChrToIndex("monster/ch87550.itc", 0x2A)
    Call(0, 113)
    LoadChrToIndex("chr/ch00050.itc", 0x24)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_161D8")
    LoadChrToIndex("chr/ch00150.itc", 0x25)
    Jump("loc_161F2")

    label("loc_161D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_161EC")
    LoadChrToIndex("chr/ch00250.itc", 0x25)
    Jump("loc_161F2")

    label("loc_161EC")

    LoadChrToIndex("chr/ch02950.itc", 0x25)

    label("loc_161F2")

    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    Call(0, 126)
    Return()

    # Function_109_16111 end

    def Function_110_16214(): pass

    label("Function_110_16214")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_162B5")
    SetChrChipByIndex(0xEF, 0x20)
    Jump("loc_162CB")

    label("loc_162B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_162C7")
    SetChrChipByIndex(0xEF, 0x21)
    Jump("loc_162CB")

    label("loc_162C7")

    SetChrChipByIndex(0xEF, 0x22)

    label("loc_162CB")

    SetChrPos(0x101, 40230, -6910, 1770, 135)
    SetChrPos(0x153, 42190, -7020, 1260, 270)
    SetChrPos(0xEF, 40720, -6970, -210, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0683
    ChrTalk(
        0x101,
        (
            "#11P#12503Fそれじゃあ、早速作戦を始めよう。\x02\x03",

            "#12500Fさっき説明した通りでいいな？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_164F4")

    #C0684
    ChrTalk(
        0x102,
        (
            "#6P#12600Fええ、波打ち際で遊んで\x01",
            "魔獣をおびきだすのよね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    #C0685
    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、よろしく頼む。\x02\x03",

            "#12503Fなんせ、ただでさえ\x01",
            "おかしな性質を持った魔獣だ。\x01",
            "十分に注意してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x102,
        (
            "#6P#12601Fうん、分かってる。\x02\x03",

            "#12603F水着を切り裂く魔獣の退治なんて、\x01",
            "突然頼まれて驚いたけど……\x02\x03",

            "#12600Fベルのためでもあるし、\x01",
            "是非協力させてもらうわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0687
    ChrTalk(
        0x153,
        "#12P#13200Fがんばってね、ロイド、エリィ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_16833")

    label("loc_164F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16692")

    #C0688
    ChrTalk(
        0x103,
        (
            "#6P#12700Fええ、波打ち際で遊んで\x01",
            "魔獣をおびきだすんですね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    #C0689
    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、よろしく頼む。\x02\x03",

            "#12503Fなんせ、ただでさえ\x01",
            "おかしな性質を持った魔獣だ。\x01",
            "十分に注意してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0690
    ChrTalk(
        0x103,
        (
            "#6P#12700Fはい、もちろんです。\x02\x03",

            "#12703F水着を切り裂く魔獣の退治、\x01",
            "突然頼まれて驚きましたが……\x02\x03",

            "#12701Fみっしぃのお膝元での悪事、\x01",
            "到底許すわけにはいきません。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x153,
        "#12P#13200Fがんばってね、ロイド、ティオ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_16833")

    label("loc_16692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16833")

    #C0692
    ChrTalk(
        0x109,
        (
            "#6P#13000Fはい、波打ち際で遊んで\x01",
            "魔獣をおびきだすんですね！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(300)

    #C0693
    ChrTalk(
        0x101,
        (
            "#11P#12500Fああ、よろしく頼む。\x02\x03",

            "#12503Fなんせ、ただでさえ\x01",
            "おかしな性質を持った魔獣だ。\x01",
            "十分に注意してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x109,
        (
            "#6P#13000Fええ、もちろんです！\x02\x03",

            "#13003F水着を切り裂く魔獣の退治なんて、\x01",
            "突然頼まれて驚きましたけど……\x02\x03",

            "#13000Fビーチで遊ぶ皆さんのためにも、\x01",
            "頑張って退治しましょう！\x02",
        )
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0x153,
        "#12P#13200Fがんばってね、ロイド、ノエル！\x02",
    )

    CloseMessageWindow()

    label("loc_16833")

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
        "#6P#12500Fそれっ。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16991")

    #C0697
    ChrTalk(
        0x102,
        "#12602Fきゃっ、もうロイドったら。\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0x87, 0x1F4)
    Sleep(100)

    #C0698
    ChrTalk(
        0x102,
        (
            "#12606F……ふう、それにしても魔獣は\x01",
            "なかなか現れないわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A80")

    label("loc_16991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16A0A")

    #C0699
    ChrTalk(
        0x103,
        "#12702Fむっ、やりましたね。\x02",
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(100)

    #C0700
    ChrTalk(
        0x103,
        (
            "#12706F……それにしても魔獣とやらは\x01",
            "なかなか現れませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16A80")

    label("loc_16A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16A80")

    #C0701
    ChrTalk(
        0x109,
        "#13002Fくうっ、やりましたね！\x02",
    )

    CloseMessageWindow()
    OP_93(0x109, 0x87, 0x1F4)
    Sleep(100)

    #C0702
    ChrTalk(
        0x109,
        (
            "#13006F……ふう、それにしても魔獣は\x01",
            "なかなか現れませんね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A80")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(100)

    #C0703
    ChrTalk(
        0x101,
        (
            "#6P#12505Fああ、もしかしたら\x01",
            "警戒しているのかもしれないな。\x02\x03",

            "#12503Fだが、魔獣がいるのは間違いない。\x01",
            "ここは様子を見て……\x02",
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
        "#6P#12511Fうわっ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_16BB4")

    #C0705
    ChrTalk(
        0x102,
        "#12609Fふふ、お返しよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C0B")

    label("loc_16BB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_16BE1")

    #C0706
    ChrTalk(
        0x103,
        "#12704F……おかえしです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16C0B")

    label("loc_16BE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_16C0B")

    #C0707
    ChrTalk(
        0x109,
        "#13009Fあはは、お返しです！\x02",
    )

    CloseMessageWindow()

    label("loc_16C0B")


    #C0708
    ChrTalk(
        0x101,
        "#6P#12512Fや、やったな……！\x02",
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
            "#5P#13206F（あーあ、キーアも\x01",
            "  ロイドたちと遊びたいな。）\x02\x03",

            "#13208F（危ないからって言ってたケド、\x01",
            "  ふつーに楽しそうだし……）\x02\x03",

            "#13205F（……あれっ？）\x02",
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
        "#13205Fあっ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_17157")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0711
    ChrTalk(
        0x153,
        "#13207F#4Sエリィっ、うしろー！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0712
    ChrTalk(
        0x102,
        "#12P#12605Fえっ……\x02",
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
        "#12615F#4S──きゃああああっ！！？？\x02",
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

    def lambda_1708B():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_1708B)
    Sleep(1000)

    def lambda_170A8():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_170A8)

    #C0714
    ChrTalk(
        0x101,
        "#6P#12511Fエ、エリィッ……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    #C0715
    ChrTalk(
        0x102,
        (
            "#12613Fこ、ここはいいから……\x01",
            "魔獣を追ってちょうだい！！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0716
    ChrTalk(
        0x101,
        "#6P#12501Fわ、分かった！！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x102, 0x5DC, 0x3, 0x4, 0x3, 0x2)
    Jump("loc_177EA")

    label("loc_17157")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_174A3")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0717
    ChrTalk(
        0x153,
        "#13207F#4Sティオっ、うしろー！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0718
    ChrTalk(
        0x103,
        "#12P#12705Fえ……\x02",
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
        "#12710F#4S──きゃっ……！！？？\x02",
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

    def lambda_173DB():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_173DB)
    Sleep(1000)

    def lambda_173F8():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_173F8)

    #C0720
    ChrTalk(
        0x101,
        "#6P#12511Fティ、ティオッ……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    #C0721
    ChrTalk(
        0x103,
        (
            "#12701Fこ、ここはいいですから……\x01",
            "早く、魔獣を！！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0722
    ChrTalk(
        0x101,
        "#6P#12501Fわ、分かった！！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x103, 0x5DC, 0x3, 0x4, 0x3, 0x2)
    Jump("loc_177EA")

    label("loc_174A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_177EA")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0723
    ChrTalk(
        0x153,
        "#13207F#4Sノエルっ、うしろー！！\x02",
    )

    CloseMessageWindow()
    StopSound(989, 2000, 50)
    StopBGM(0x7D0)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0724
    ChrTalk(
        0x109,
        "#12P#13005Fえ……\x02",
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
        "#13014F#4S──ひゃあ……！！？？\x02",
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

    def lambda_17727():
        OP_95(0xFE, 39070, -6800, 10350, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17727)
    Sleep(1000)

    def lambda_17744():
        OP_97(0xFE, 0x0, 0x0, 0x1F4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17744)

    #C0726
    ChrTalk(
        0x101,
        "#6P#12511Fノ、ノエルッ……！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x2, 0x3, 0x4)

    #C0727
    ChrTalk(
        0x109,
        (
            "#13006Fこ、ここはいいですから、\x01",
            "魔獣の追跡をっ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)

    #C0728
    ChrTalk(
        0x101,
        "#6P#12501Fわ、分かった！！\x02",
    )

    CloseMessageWindow()
    OP_A1(0x109, 0x5DC, 0x3, 0x4, 0x3, 0x2)

    label("loc_177EA")


    def lambda_177EF():
        OP_95(0xFE, 34050, -6300, 8750, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_177EF)
    Sleep(100)

    def lambda_1780C():
        OP_99(0xFE, 0xEF, 0x1F4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_1780C)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_178A5")
    RemoveParty(0x1, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_178C8")

    label("loc_178A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_178B9")
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x52, 0xFF)
    Jump("loc_178C8")

    label("loc_178B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_178C8")
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x52, 0xFF)

    label("loc_178C8")


    def lambda_178CD():
        OP_95(0xFE, 9860, -6000, -21850, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_178CD)
    Sleep(2000)

    def lambda_178EA():
        OP_95(0xFE, 11690, -6000, -17960, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_178EA)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(10060, -5780, -20380, 6000)
    MoveCamera(246, 22, 0, 6000)
    OP_6E(800, 6000)
    SetCameraDistance(12250, 6000)
    WaitChrThread(0x24, 1)
    OP_63(0x24, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)

    def lambda_17955():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17955)
    Sleep(1000)

    def lambda_17965():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17965)
    Sleep(1000)
    WaitChrThread(0x101, 1)
    OP_6F(0x1)

    #C0729
    ChrTalk(
        0x101,
        (
            "#12P#00006Fはあっ、はあっ……\x01",
            "お、追い詰めたぞ！！\x02\x03",

            "#00001F女性の水着を切り裂くなんて\x01",
            "卑劣な行い……これ以上、\x01",
            "許すわけにはいかない！\x02",
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
        "#12P#00007Fいくぞっ！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    EndChrThread(0x24, 0x1)
    Battle("BattleInfo_948", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_110_16214 end

    def Function_111_17A92(): pass

    label("Function_111_17A92")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_17ABF")

    def lambda_17AA2():
        OP_A6(0xFE, 0x28, 0x0, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17AA2)
    WaitChrThread(0xFE, 2)
    Jump("Function_111_17A92")

    label("loc_17ABF")

    Return()

    # Function_111_17A92 end

    def Function_112_17AC0(): pass

    label("Function_112_17AC0")

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

    # Function_112_17AC0 end

    def Function_113_17BAF(): pass

    label("Function_113_17BAF")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_17BC7")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    Jump("loc_17BEE")

    label("loc_17BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_17BDD")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    Jump("loc_17BEE")

    label("loc_17BDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_17BEE")
    AddParty(0x52, 0xFF, 0xFF)
    AddParty(0x8, 0xFF, 0xFF)

    label("loc_17BEE")

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
            "#12P#00000Fどうだ……\x01",
            "観念してもらうぞっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(9490, -5480, -21070, 3000)

    def lambda_17DC0():
        OP_99(0xFE, 0x24, 0xBB8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17DC0)
    Sleep(500)

    def lambda_17DD7():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17DD7)
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

    def lambda_17E5D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_17E5D)
    Sleep(100)

    def lambda_17E6D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_17E6D)

    #C0732
    ChrTalk(
        0x101,
        "#12P#00005F何……！？\x02",
    )

    CloseMessageWindow()

    def lambda_17E95():
        OP_95(0xFE, 23660, -2000, -35810, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_17E95)
    Sleep(100)

    def lambda_17EB2():
        OP_95(0xFE, 24940, -2000, -35780, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_17EB2)
    Sleep(100)

    def lambda_17ECF():
        OP_95(0xFE, 21250, -2000, -36870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_17ECF)
    Sleep(100)

    def lambda_17EEC():
        OP_95(0xFE, 21590, -2000, -35820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_17EEC)
    Sleep(100)

    def lambda_17F09():
        OP_95(0xFE, 23090, -2000, -36580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_17F09)
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
        "#00011Fな、仲間がいたのか！？\x02",
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
        "#11P#00010Fくっ……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xEF, 0x80)
    ClearChrFlags(0x153, 0x80)

    #N0735
    NpcTalk(
        0x153,
        "キーアの声",
        "#4Sロイドーッ！！\x02",
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

    def lambda_182B1():
        OP_95(0xFE, 15180, -6000, -13330, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_182B1)

    def lambda_182CB():
        OP_95(0xFE, 15380, -6000, -15880, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_182CB)

    def lambda_182E5():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_182E5)

    def lambda_182F2():
        OP_93(0xFE, 0x2D, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_182F2)

    def lambda_182FF():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_182FF)

    def lambda_1830C():
        OP_93(0xFE, 0x0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_1830C)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18391")
    Sound(805, 0, 100, 0)
    Jump("loc_18397")

    label("loc_18391")

    Sound(531, 0, 100, 0)

    label("loc_18397")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_18412")

    #C0736
    ChrTalk(
        0x101,
        (
            "#00005Fエリィ、キーア！\x01",
            "……大丈夫なのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0737
    ChrTalk(
        0x102,
        (
            "#12P#00113Fは、話は後！\x01",
            "今は魔獣をやっつけましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1850A")

    label("loc_18412")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_1848E")

    #C0738
    ChrTalk(
        0x101,
        (
            "#00005Fティオ、キーア！\x01",
            "……大丈夫なのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0739
    ChrTalk(
        0x103,
        (
            "#12P#00203F……話は後です！\x01",
            "今は魔獣を退治しましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1850A")

    label("loc_1848E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1850A")

    #C0740
    ChrTalk(
        0x101,
        (
            "#00005Fノエル、キーア！\x01",
            "……大丈夫なのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x109,
        (
            "#12P#10107Fは、はい！！\x01",
            "とにかく今は魔獣を\x01",
            "退治しましょう！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1850A")


    #C0742
    ChrTalk(
        0x101,
        "#00000Fああ、分かった！\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x153,
        "#01107F２人とも、ファイトー！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Battle("BattleInfo_98C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_113_17BAF end

    def Function_114_18566(): pass

    label("Function_114_18566")

    OP_93(0x25, 0x13B, 0x1F4)
    OP_A1(0x25, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_114_18566 end

    def Function_115_18579(): pass

    label("Function_115_18579")

    OP_93(0x26, 0x13B, 0x1F4)
    OP_A1(0x26, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_115_18579 end

    def Function_116_1858C(): pass

    label("Function_116_1858C")

    OP_93(0x27, 0x13B, 0x1F4)
    OP_A1(0x27, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_116_1858C end

    def Function_117_1859F(): pass

    label("Function_117_1859F")

    OP_93(0x28, 0x13B, 0x1F4)
    OP_A1(0x28, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_117_1859F end

    def Function_118_185B2(): pass

    label("Function_118_185B2")

    OP_93(0x29, 0x13B, 0x1F4)
    OP_A1(0x29, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Return()

    # Function_118_185B2 end

    def Function_119_185C5(): pass

    label("Function_119_185C5")

    OP_A1(0x25, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x25, 0x50BE, 0xFFFFE890, 0xFFFF9A34, 0x7D0, 0x1388)
    OP_95(0x25, 10410, -6000, -16510, 5000, 0x0)
    TurnDirection(0x25, 0x101, 500)
    Return()

    # Function_119_185C5 end

    def Function_120_18605(): pass

    label("Function_120_18605")

    OP_A1(0x26, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 100, 0)
    OP_9D(0x26, 0x4C22, 0xFFFFE890, 0xFFFF952A, 0x7D0, 0x1388)
    OP_95(0x26, 8150, -6000, -20170, 5000, 0x0)
    TurnDirection(0x26, 0x101, 500)
    Return()

    # Function_120_18605 end

    def Function_121_18645(): pass

    label("Function_121_18645")

    OP_A1(0x27, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x27, 0x5942, 0xFFFFE890, 0xFFFF94DA, 0x7D0, 0x1388)
    OP_95(0x27, 12360, -6000, -15910, 5000, 0x0)
    TurnDirection(0x27, 0x101, 500)
    Return()

    # Function_121_18645 end

    def Function_122_18685(): pass

    label("Function_122_18685")

    OP_A1(0x28, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x28, 0x4A4C, 0xFFFFE890, 0xFFFF9098, 0x7D0, 0x1388)
    OP_95(0x28, 13700, -6000, -22060, 5000, 0x0)
    TurnDirection(0x28, 0x101, 500)
    Return()

    # Function_122_18685 end

    def Function_123_186C5(): pass

    label("Function_123_186C5")

    OP_A1(0x29, 0x5DC, 0x1, 0x0)
    Sound(809, 0, 80, 0)
    OP_9D(0x29, 0x51E0, 0xFFFFE890, 0xFFFF93CC, 0x7D0, 0x1388)
    OP_95(0x29, 14480, -6000, -18580, 5000, 0x0)
    TurnDirection(0x29, 0x101, 500)
    Return()

    # Function_123_186C5 end

    def Function_124_18705(): pass

    label("Function_124_18705")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1872E")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    Jump("loc_18710")

    label("loc_1872E")

    Return()

    # Function_124_18705 end

    def Function_125_1872F(): pass

    label("Function_125_1872F")

    Sound(997, 0, 100, 0)
    Sleep(800)
    Sound(997, 0, 100, 0)
    Sleep(300)
    Sound(997, 0, 100, 0)
    Return()

    # Function_125_1872F end

    def Function_126_18748(): pass

    label("Function_126_18748")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_187EC")
    Sound(531, 0, 100, 0)

    label("loc_187EC")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrChipByIndex(0xEF, 0xFF)
    OP_0D()

    #C0744
    ChrTalk(
        0x101,
        (
            "#00006Fふう……\x01",
            "とりあえず何とかなったな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x153, 500)
    Sleep(500)

    #C0745
    ChrTalk(
        0x101,
        "#00000F２人とも、お疲れ様。\x02",
    )

    CloseMessageWindow()

    def lambda_18855():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_18855)
    Sleep(100)

    def lambda_18865():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_18865)
    Sleep(500)

    #C0746
    ChrTalk(
        0x153,
        "#12P#01109Fえへへ、お疲れ様ー。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_189EA")

    #C0747
    ChrTalk(
        0x102,
        (
            "#6P#00104Fこれでとりあえず、\x01",
            "一件落着って感じかしら。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    #C0748
    ChrTalk(
        0x101,
        (
            "#00008F……その、エリィ。\x02\x03",

            "#00006Fなんというか……\x01",
            "守ってやれなくてごめんな。\x02",
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
            "#6P#00112Fも、もう、気にしないでちょうだい。\x01",
            "私も油断していたところがあるし……\x02\x03",

            "#00103Fそれよりも、なんであんな魔獣が\x01",
            "ビーチに現れたのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C70")

    label("loc_189EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18B2F")

    #C0750
    ChrTalk(
        0x103,
        (
            "#6P#00204Fこれでとりあえず、\x01",
            "一件落着って感じですか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    #C0751
    ChrTalk(
        0x101,
        (
            "#00008F……その、ティオ。\x02\x03",

            "#00006Fなんというか……\x01",
            "守ってやれなくてごめんな。\x02",
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
            "#6P#00203F……お気づかないなく。\x01",
            "わたしも油断していましたし……\x02\x03",

            "#00200Fそれよりも、なんであんな魔獣が\x01",
            "ビーチに現れたんでしょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18C70")

    label("loc_18B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_18C70")

    #C0753
    ChrTalk(
        0x109,
        "#6P#10109Fこれでとりあえず一件落着ですね！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xEF, 500)
    Sleep(500)

    #C0754
    ChrTalk(
        0x101,
        (
            "#00008F……その、ノエル。\x02\x03",

            "#00006Fなんというか……\x01",
            "守ってやれなくてごめんな。\x02",
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
            "#6P#10112Fそ、そんな気にしないでください！\x01",
            "あたしも油断がありましたし……\x02\x03",

            "#10105Fそれよりも、なんであんな魔獣が\x01",
            "ビーチに現れたんでしょうね？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C70")


    #C0756
    ChrTalk(
        0x101,
        (
            "#00006Fこれは俺の憶測だけど……\x01",
            "多分、開発の影響じゃないかな。\x02\x03",

            "#00001F開発で行き場を失った魔獣が、\x01",
            "腹いせに人間に嫌がらせを始めた……\x01",
            "っていうのが一番しっくりくるよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 6)), scpexpr(EXPR_END)), "loc_18E78")

    #C0757
    ChrTalk(
        0x102,
        (
            "#6P#00103Fなるほど……ありそうね。\x02\x03",

            "#00101F水着を切り裂いていたのも、\x01",
            "それで大騒ぎになったのを見て\x01",
            "味をしめていたという所かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x153,
        (
            "#12P#01108F……なんだかあのコたちも\x01",
            "カワイソーだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x101,
        (
            "#00003F確かにな……\x02\x03",

            "#00000F……まあ、ひとまずは\x01",
            "カルミナさんたちのところに\x01",
            "報告に行くとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x102,
        "#6P#00100Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1912D")

    label("loc_18E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15B, 7)), scpexpr(EXPR_END)), "loc_18FD1")

    #C0761
    ChrTalk(
        0x103,
        (
            "#6P#00203Fなるほど……ありそうです。\x02\x03",

            "#00200F水着を切り裂いていたのも、\x01",
            "それで大騒ぎになったのを見て\x01",
            "味をしめていたという事ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0762
    ChrTalk(
        0x153,
        (
            "#12P#01108F……なんだかあのコたちも\x01",
            "カワイソーだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0763
    ChrTalk(
        0x101,
        (
            "#00003F確かにな……\x02\x03",

            "#00000F……まあ、ひとまずは\x01",
            "カルミナさんたちのところに\x01",
            "報告に行くとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x103,
        "#6P#00200Fええ、そうですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1912D")

    label("loc_18FD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 5)), scpexpr(EXPR_END)), "loc_1912D")

    #C0765
    ChrTalk(
        0x109,
        (
            "#6P#10103Fなるほど……ありそうですね。\x02\x03",

            "#10101F水着を切り裂いていたのも、\x01",
            "それで大騒ぎになったのを見て\x01",
            "味をしめていたという所でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x153,
        (
            "#12P#01108F……なんだかあのコたちも\x01",
            "カワイソーだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x101,
        (
            "#00003F確かにな……\x02\x03",

            "#00000F……まあ、ひとまずは\x01",
            "カルミナさんたちのところに\x01",
            "報告に行くとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x109,
        "#6P#10100Fはい、行きましょう！\x02",
    )

    CloseMessageWindow()

    label("loc_1912D")

    StopSound(136, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 3)
    NewScene("t1320", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_126_18748 end

    SaveToFile()

Try(main)
