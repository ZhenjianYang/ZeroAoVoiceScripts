from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1550.bin",                # FileName
        "c1550",                    # MapName
        "c1550",                    # Location
        0x00B0,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 176, 0, 3, 0, 4],
    )

    BuildStringList((
        "c1550",                  # 0
        "接待小姐兰菲",           # 1
        "接待小姐柯琳娜",         # 2
        "警备员比尔斯",           # 3
        "警备员汪古",             # 4
        "滴",                     # 5
        "莫雷特主任",             # 6
        "接待小姐莉莉埃",         # 7
        "皮埃尔副局长",           # 8
        "研究员达比德",           # 9
        "警官",                   # 10
        "警官",                   # 11
        "科洛蒂娅公主",           # 12
        "雷克特书记官",           # 13
        "共和国军官",             # 14
        "帝国军官",               # 15
        "洛克史密斯总统",         # 16
        "尤莉亚准校",             # 17
        "穆拉少校",               # 18
        "阿尔伯特大公",           # 19
        "公国护卫官",             # 20
        "总管",                   # 21
        "总管",                   # 22
        "女仆",                   # 23
        "女仆",                   # 24
        "女仆",                   # 25
        "女仆",                   # 26
        "女仆",                   # 27
        "女仆",                   # 28
        "女仆",                   # 29
        "市政府职员",             # 30
        "市政府职员",             # 31
        "警官",                   # 32
        "警官",                   # 33
        "王室亲卫队队员",         # 34
        "基库",                   # 35
        "迪塔市长",               # 36
        "奥利维特皇子",           # 37
        "麦克道尔议长",           # 38
        "达德利搜查官",           # 39
        "奥斯本宰相",             # 40
        "议员",                   # 41
        "议员",                   # 42
        "议员",                   # 43
        "琪雅",                   # 44
        "亚里欧斯长官",           # 45
        "模型",                   # 46
        "伊安律师",               # 47
        "椅子",                   # 48
        "椅子",                   # 49
        "旋棍",                   # 50
        "旋棍",                   # 51
        "旋棍OBJ",                # 52
        "包袱皮",                 # 53
        "信",                     # 54
        "笔记本型终端",           # 55
        "国防军士兵·男",         # 56
        "国防军士兵·男",         # 57
        "国防军士兵·男",         # 58
        "国防军士兵·男",         # 59
        "SE控制",                 # 60
    ))

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch11000.itc",                   # 01
        "chr/ch12400.itc",                   # 02
        "chr/ch41200.itc",                   # 03
        "chr/ch41000.itc",                   # 04
        "chr/ch11700.itc",                   # 05
        "chr/ch05410.itc",                   # 06
        "apl/ch51233.itc",                   # 07
        "chr/ch29400.itc",                   # 08
        "chr/ch27400.itc",                   # 09
        "chr/ch30500.itc",                   # 0A
        "chr/ch10902.itc",                   # 0B
        "chr/ch11002.itc",                   # 0C
        "chr/ch11102.itc",                   # 0D
        "chr/ch05802.itc",                   # 0E
        "chr/ch05902.itc",                   # 0F
        "chr/ch25600.itc",                   # 10
        "chr/ch25700.itc",                   # 11
        "chr/ch34500.itc",                   # 12
        "chr/ch25800.itc",                   # 13
        "chr/ch25900.itc",                   # 14
        "chr/ch11200.itc",                   # 15
        "chr/ch11300.itc",                   # 16
        "chr/ch11802.itc",                   # 17
        "chr/ch28600.itc",                   # 18
        "chr/ch28000.itc",                   # 19
        "chr/ch27900.itc",                   # 1A
        "chr/ch05602.itc",                   # 1B
        "chr/ch13802.itc",                   # 1C
        "chr/ch41600.itc",                   # 1D
        "chr/ch27902.itc",                   # 1E
        "chr/ch06402.itc",                   # 1F
        "chr/ch11712.itc",                   # 20
    ))

    DeclNpc(0,       300,     31700,   180,  389,  0x0, 0,   30,  0,   255, 255, 0,   42,  255,  0)
    DeclNpc(7110,    300,     32759,   90,   385,  0x0, 0,   10,  0,   0,   0,   0,   45,  255,  0)
    DeclNpc(3910,    0,       5050,    180,  385,  0x0, 0,   24,  0,   0,   0,   0,   46,  255,  0)
    DeclNpc(1700,    0,       -22129,  180,  385,  0x0, 0,   24,  0,   0,   0,   0,   47,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   255, 255, 0,   48,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   255, 255, 0,   41,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   255, 255, 0,   40,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   31,  0,   255, 255, 0,   43,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   255, 255, 0,   44,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   255, 255, 0,   25,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   39,  255,  0)
    DeclNpc(-120139, 0,       103459,  270,  389,  0x0, 0,   3,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   29,  255,  0)
    DeclNpc(2180,    0,       -126910, 45,   389,  0x0, 0,   21,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(3180,    0,       -126910, 45,   389,  0x0, 0,   22,  0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   23,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   24,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   19,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   20,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   16,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   18,  0,   0,   0,   0,   30,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   17,  0,   0,   0,   0,   31,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   16,  0,   0,   0,   0,   35,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   25,  0,   0,   0,   0,   32,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   26,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(103339,  0,       -128889, 180,  389,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(3849,    0,       899,     180,  389,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   29,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   28,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   27,  0,   255, 255, 0,   38,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   13,  0,   255, 255, 0,   36,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   14,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    246,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 92,  109.0,                 -122.5,                -1.0,                  81.0,                  [0.1666666716337204,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -18.166667938232422,   40.833335876464844,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 137, 112.3499984741211,     -130.72999572753906,   -1.0,                  36.0,                  [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -37.45000076293945,    32.682498931884766,    0.20000001788139343,   1.0])

    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  138, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  138, 0x0000)
    DeclActor(-51570,  0,       3070,    1000,    -51570,  1500,    3070,    0x007C, 0,  139, 0x0000)

    ChipFrameInfo(2824, 0)                                       # 0

    ScpFunction((
        "Function_0_B08",          # 00, 0
        "Function_1_BB8",          # 01, 1
        "Function_2_C0B",          # 02, 2
        "Function_3_C5E",          # 03, 3
        "Function_4_1570",         # 04, 4
        "Function_5_1860",         # 05, 5
        "Function_6_18BA",         # 06, 6
        "Function_7_18D8",         # 07, 7
        "Function_8_1CE7",         # 08, 8
        "Function_9_1EFD",         # 09, 9
        "Function_10_2087",        # 0A, 10
        "Function_11_27B8",        # 0B, 11
        "Function_12_285A",        # 0C, 12
        "Function_13_2B2C",        # 0D, 13
        "Function_14_2F2A",        # 0E, 14
        "Function_15_3059",        # 0F, 15
        "Function_16_326E",        # 10, 16
        "Function_17_3384",        # 11, 17
        "Function_18_342D",        # 12, 18
        "Function_19_3F57",        # 13, 19
        "Function_20_3FD4",        # 14, 20
        "Function_21_4050",        # 15, 21
        "Function_22_46A9",        # 16, 22
        "Function_23_48BF",        # 17, 23
        "Function_24_4A63",        # 18, 24
        "Function_25_4AF3",        # 19, 25
        "Function_26_4B83",        # 1A, 26
        "Function_27_4C67",        # 1B, 27
        "Function_28_4E61",        # 1C, 28
        "Function_29_4F26",        # 1D, 29
        "Function_30_5052",        # 1E, 30
        "Function_31_5184",        # 1F, 31
        "Function_32_5256",        # 20, 32
        "Function_33_52D0",        # 21, 33
        "Function_34_5376",        # 22, 34
        "Function_35_56F1",        # 23, 35
        "Function_36_57D1",        # 24, 36
        "Function_37_57DB",        # 25, 37
        "Function_38_6146",        # 26, 38
        "Function_39_6150",        # 27, 39
        "Function_40_623C",        # 28, 40
        "Function_41_633C",        # 29, 41
        "Function_42_63C4",        # 2A, 42
        "Function_43_6583",        # 2B, 43
        "Function_44_6681",        # 2C, 44
        "Function_45_67B4",        # 2D, 45
        "Function_46_6822",        # 2E, 46
        "Function_47_6918",        # 2F, 47
        "Function_48_69EF",        # 30, 48
        "Function_49_6ADF",        # 31, 49
        "Function_50_6F88",        # 32, 50
        "Function_51_7DB0",        # 33, 51
        "Function_52_8805",        # 34, 52
        "Function_53_880C",        # 35, 53
        "Function_54_8835",        # 36, 54
        "Function_55_975B",        # 37, 55
        "Function_56_97DA",        # 38, 56
        "Function_57_982F",        # 39, 57
        "Function_58_9884",        # 3A, 58
        "Function_59_98D9",        # 3B, 59
        "Function_60_992E",        # 3C, 60
        "Function_61_9983",        # 3D, 61
        "Function_62_99D8",        # 3E, 62
        "Function_63_9A2D",        # 3F, 63
        "Function_64_9AD2",        # 40, 64
        "Function_65_9B44",        # 41, 65
        "Function_66_9BC8",        # 42, 66
        "Function_67_9C38",        # 43, 67
        "Function_68_9CBC",        # 44, 68
        "Function_69_9D2C",        # 45, 69
        "Function_70_9DB0",        # 46, 70
        "Function_71_9E20",        # 47, 71
        "Function_72_9E5D",        # 48, 72
        "Function_73_9EAE",        # 49, 73
        "Function_74_9EEB",        # 4A, 74
        "Function_75_9F46",        # 4B, 75
        "Function_76_9FB8",        # 4C, 76
        "Function_77_A034",        # 4D, 77
        "Function_78_A0A6",        # 4E, 78
        "Function_79_A122",        # 4F, 79
        "Function_80_A197",        # 50, 80
        "Function_81_AAC0",        # 51, 81
        "Function_82_AD26",        # 52, 82
        "Function_83_AF8E",        # 53, 83
        "Function_84_B268",        # 54, 84
        "Function_85_B2B9",        # 55, 85
        "Function_86_B9A4",        # 56, 86
        "Function_87_B9F9",        # 57, 87
        "Function_88_BA59",        # 58, 88
        "Function_89_BAB9",        # 59, 89
        "Function_90_BB19",        # 5A, 90
        "Function_91_BB79",        # 5B, 91
        "Function_92_BBD9",        # 5C, 92
        "Function_93_BCE0",        # 5D, 93
        "Function_94_DE63",        # 5E, 94
        "Function_95_DEB4",        # 5F, 95
        "Function_96_DF09",        # 60, 96
        "Function_97_DF5E",        # 61, 97
        "Function_98_DFB3",        # 62, 98
        "Function_99_E008",        # 63, 99
        "Function_100_E05D",       # 64, 100
        "Function_101_E0B2",       # 65, 101
        "Function_102_E107",       # 66, 102
        "Function_103_E167",       # 67, 103
        "Function_104_E1C7",       # 68, 104
        "Function_105_E227",       # 69, 105
        "Function_106_E287",       # 6A, 106
        "Function_107_E2E7",       # 6B, 107
        "Function_108_F06F",       # 6C, 108
        "Function_109_F08E",       # 6D, 109
        "Function_110_F93E",       # 6E, 110
        "Function_111_FBEF",       # 6F, 111
        "Function_112_101CC",      # 70, 112
        "Function_113_10245",      # 71, 113
        "Function_114_10260",      # 72, 114
        "Function_115_10273",      # 73, 115
        "Function_116_10772",      # 74, 116
        "Function_117_10A53",      # 75, 117
        "Function_118_10E60",      # 76, 118
        "Function_119_11DE6",      # 77, 119
        "Function_120_11E0B",      # 78, 120
        "Function_121_11E33",      # 79, 121
        "Function_122_11EA6",      # 7A, 122
        "Function_123_11EF4",      # 7B, 123
        "Function_124_14932",      # 7C, 124
        "Function_125_149A7",      # 7D, 125
        "Function_126_149FC",      # 7E, 126
        "Function_127_14A51",      # 7F, 127
        "Function_128_14AA6",      # 80, 128
        "Function_129_14AFB",      # 81, 129
        "Function_130_14B50",      # 82, 130
        "Function_131_14BA5",      # 83, 131
        "Function_132_14BD5",      # 84, 132
        "Function_133_14C35",      # 85, 133
        "Function_134_14C95",      # 86, 134
        "Function_135_14CF0",      # 87, 135
        "Function_136_14D50",      # 88, 136
        "Function_137_14DB0",      # 89, 137
        "Function_138_14FBB",      # 8A, 138
        "Function_139_1526C",      # 8B, 139
        "Function_140_154C9",      # 8C, 140
    ))


    def Function_0_B08(): pass

    label("Function_0_B08")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_B40"),
        (1, "loc_B4C"),
        (2, "loc_B58"),
        (3, "loc_B64"),
        (4, "loc_B70"),
        (5, "loc_B7C"),
        (6, "loc_B88"),
        (SWITCH_DEFAULT, "loc_B94"),
    )


    label("loc_B40")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B4C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B58")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B64")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B70")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B7C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B88")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_B94")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_BA0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BB7")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_BA0")

    label("loc_BB7")

    Return()

    # Function_0_B08 end

    def Function_1_BB8(): pass

    label("Function_1_BB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0A")
    OP_95(0xFE, 110000, 0, -107310, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0xB4, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 110000, 0, -126470, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(300)
    Jump("Function_1_BB8")

    label("loc_C0A")

    Return()

    # Function_1_BB8 end

    def Function_2_C0B(): pass

    label("Function_2_C0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C5D")
    OP_95(0xFE, -132100, 0, 100800, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -122620, 0, 100800, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_2_C0B")

    label("loc_C5D")

    Return()

    # Function_2_C0B end

    def Function_3_C5E(): pass

    label("Function_3_C5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C88")
    ClearScenarioFlags(0x25, 1)
    Call(0, 52)

    label("loc_C88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D68")
    SetChrChipByIndex(0x2F, 0xB)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 5650, -5850, -106000, 270)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 5650, -5850, -108800, 270)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5650, -5850, -111700, 270)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 1800, -5850, -102100, 180)
    SetChrChipByIndex(0x36, 0xF)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 11800, -5850, -104800, 270)
    SetChrChipByIndex(0x34, 0x7)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 5000, -5800, -99450, 180)

    label("loc_D68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D96")
    SetChrPos(0x15, -3200, 0, 27000, 90)
    ClearChrFlags(0x15, 0x80)

    label("loc_D96")

    SetChrPos(0x17, -130150, 150, 105800, 90)
    ClearChrFlags(0x17, 0x80)
    SetChrChipByIndex(0x17, 0x20)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    EndChrThread(0x17, 0x0)
    SetChrBattleFlags(0x17, 0x4)
    SetChrPos(0x16, 111300, 0, -102500, 270)
    ClearChrFlags(0x16, 0x80)

    label("loc_DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E54")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 111300, 0, -102500, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 110390, 0, -126470, 0)
    BeginChrThread(0x12, 0, 0, 1)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, -3110, 0, 1600, 90)
    ClearChrFlags(0x2B, 0x80)
    SetChrPos(0x2B, 156990, 0, 110700, 180)
    SetChrChipByIndex(0x2B, 0x1B)
    SetChrSubChip(0x2B, 0x0)
    EndChrThread(0x2B, 0x0)
    SetChrBattleFlags(0x2B, 0x4)
    Jump("loc_141C")

    label("loc_E54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_FAA")
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -121320, 0, 5490, 270)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -123130, 0, 5700, 90)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -128710, 150, 3860, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -134450, 0, 3390, 270)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x20, -122470, 0, 50530, 0)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -122470, 0, 51740, 180)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, -122350, 0, 57760, 225)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -126560, 150, 110790, 180)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    EndChrThread(0x8, 0x0)
    SetChrBattleFlags(0x8, 0x4)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, -121670, 0, 111190, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -122620, 0, 100800, 270)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, -132640, 0, 109740, 135)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, 163500, 0, 57920, 90)
    BeginChrThread(0xC, 0, 0, 0)
    Jump("loc_141C")

    label("loc_FAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_END)), "loc_FB8")
    Jump("loc_141C")

    label("loc_FB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_10A2")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 149450, 0, 58300, 180)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x27, 110360, 0, -114690, 180)
    SetChrPos(0x1D, 110360, 0, -115990, 0)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, -2480, 0, 25200, 180)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x20, -127400, 0, 108660, 270)
    SetChrPos(0x21, -128400, 0, 108660, 90)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x12, -122940, 0, 102860, 90)
    SetChrPos(0x1C, -121540, 0, 102860, 270)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x22, 153210, 0, 51920, 0)
    SetChrPos(0x24, 153210, 0, 52920, 180)
    Jump("loc_141C")

    label("loc_10A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_END)), "loc_10B0")
    Jump("loc_141C")

    label("loc_10B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_12AF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_10D8")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -120140, 0, 103460, 270)

    label("loc_10D8")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 8690, 0, -132450, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -9280, 0, -132230, 90)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x18, 2180, 0, -126910, 0)
    SetChrPos(0x19, 3180, 0, -126910, 0)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 3850, 0, 900, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_1165")
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, 103340, 0, -128889, 180)

    label("loc_1165")

    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, -3280, 0, 13320, 90)
    ClearChrFlags(0x29, 0x80)
    SetChrPos(0x29, -3280, 0, 21260, 90)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x2D, 0x80)
    SetChrPos(0x1A, -128710, 150, 3860, 180)
    SetChrPos(0x2D, -130100, 150, 3080, 90)
    SetChrChipByIndex(0x1A, 0x17)
    SetChrSubChip(0x1A, 0x0)
    EndChrThread(0x1A, 0x0)
    SetChrBattleFlags(0x1A, 0x4)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    EndChrThread(0x2D, 0x0)
    SetChrBattleFlags(0x2D, 0x4)
    SetChrSubChip(0x1A, 0x2)
    SetChrSubChip(0x2D, 0x1)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x2A, -134080, 0, 52160, 0)
    SetChrPos(0x13, -134280, 0, 53360, 180)
    BeginChrThread(0x13, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_12AA")
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x25, 153850, 0, 3760, 90)
    SetChrPos(0x26, 155060, 0, 3760, 270)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2B, 0x80)
    SetChrPos(0x2C, 159940, 150, 57060, 270)
    SetChrPos(0x2B, 158000, 150, 57950, 180)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    EndChrThread(0x2C, 0x0)
    SetChrBattleFlags(0x2C, 0x4)
    SetChrChipByIndex(0x2B, 0x1B)
    SetChrSubChip(0x2B, 0x0)
    EndChrThread(0x2B, 0x0)
    SetChrBattleFlags(0x2B, 0x4)
    SetChrSubChip(0x2B, 0x1)
    SetChrFlags(0x2C, 0x10)
    SetChrFlags(0x2B, 0x10)

    label("loc_12AA")

    Jump("loc_141C")

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_141C")
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 8690, 0, -132450, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -9280, 0, -132230, 90)
    ClearChrFlags(0x27, 0x80)
    SetChrPos(0x27, 103340, 0, -128889, 180)
    ClearChrFlags(0x28, 0x80)
    SetChrPos(0x28, 3850, 0, 900, 180)
    ClearChrFlags(0x1E, 0x80)
    SetChrPos(0x1E, -122130, 0, -3260, 90)
    ClearChrFlags(0x1F, 0x80)
    SetChrPos(0x1F, -134000, 0, 5590, 315)
    ClearChrFlags(0x2A, 0x80)
    OP_52(0x2A, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x20, 0x80)
    SetChrPos(0x2A, -134080, 0, 52160, 0)
    SetChrPos(0x20, -134280, 0, 53360, 180)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x21, 0x80)
    SetChrPos(0x1C, -125880, 0, 107290, 180)
    SetChrPos(0x21, -124670, 0, 106100, 270)
    SetChrFlags(0x1C, 0x10)
    SetChrFlags(0x21, 0x10)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x22, 163430, 0, -1430, 90)
    ClearChrFlags(0x23, 0x80)
    SetChrPos(0x23, 153670, 0, 6380, 0)
    ClearChrFlags(0x1D, 0x80)
    SetChrPos(0x1D, 160670, 0, 60390, 0)
    ClearChrFlags(0x24, 0x80)
    SetChrPos(0x24, 150610, 0, 51190, 270)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, 161310, 0, 111420, 0)
    SetChrFlags(0x14, 0x10)

    label("loc_141C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1430")
    ClearScenarioFlags(0x22, 0)
    Event(0, 54)
    Jump("loc_14DC")

    label("loc_1430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1444")
    ClearScenarioFlags(0x22, 1)
    Event(0, 80)
    Jump("loc_14DC")

    label("loc_1444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1458")
    ClearScenarioFlags(0x22, 2)
    Event(0, 107)
    Jump("loc_14DC")

    label("loc_1458")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_146C")
    ClearScenarioFlags(0x22, 3)
    Event(0, 109)
    Jump("loc_14DC")

    label("loc_146C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1480")
    ClearScenarioFlags(0x22, 4)
    Event(0, 110)
    Jump("loc_14DC")

    label("loc_1480")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1494")
    ClearScenarioFlags(0x22, 5)
    Event(0, 115)
    Jump("loc_14DC")

    label("loc_1494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_14A8")
    ClearScenarioFlags(0x22, 6)
    Event(0, 116)
    Jump("loc_14DC")

    label("loc_14A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_14B9")
    ClearScenarioFlags(0x22, 7)
    Jump("loc_14DC")

    label("loc_14B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_14CD")
    ClearScenarioFlags(0x23, 0)
    Event(0, 117)
    Jump("loc_14DC")

    label("loc_14CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_14DC")
    ClearScenarioFlags(0x23, 1)
    Event(0, 85)

    label("loc_14DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14FA")
    Event(0, 81)

    label("loc_14FA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1521")
    Event(0, 82)

    label("loc_1521")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_153B")
    Event(0, 111)

    label("loc_153B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1555")
    Event(0, 118)

    label("loc_1555")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x76), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_156F")
    Event(0, 123)

    label("loc_156F")

    Return()

    # Function_3_C5E end

    def Function_4_1570(): pass

    label("Function_4_1570")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1589")
    VolumeBGM(0x46, 0xC8)
    Jump("loc_15A0")

    label("loc_1589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15CB")
    SetBarrier(0x0, 0x0, 0x1, 0x0, -4000, -1000, 27000, 5000, 5000, 90000)

    label("loc_15CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15DF")
    ClearMapObjFlags(0x2, 0x10)

    label("loc_15DF")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15F7")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_15F7")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1613")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1613")

    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1642")
    SetMapObjFrame(0xFF, "bs", 0x1, 0x1)
    Jump("loc_164C")

    label("loc_1642")

    SetMapObjFrame(0xFF, "bs", 0x0, 0x1)

    label("loc_164C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166E")
    ClearMapObjFlags(0x16, 0x4)
    OP_70(0x16, 0x46)
    ClearMapObjFlags(0x17, 0x4)
    OP_70(0x17, 0x46)

    label("loc_166E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16B3")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_16B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_16EE")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_16EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_170E")
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_170E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_171D")
    ClearMapObjFlags(0x2, 0x10)

    label("loc_171D")

    ClearMapObjFlags(0x9, 0x10)
    ClearMapObjFlags(0xA, 0x10)
    ClearMapObjFlags(0xB, 0x10)
    ClearMapObjFlags(0xD, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    ClearMapObjFlags(0x8, 0x10)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1771")
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    Jump("loc_1811")

    label("loc_1771")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17B6")
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_17A5")
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0x6, 0x10)
    Jump("loc_17B1")

    label("loc_17A5")

    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0x6, 0x10)

    label("loc_17B1")

    Jump("loc_1811")

    label("loc_17B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17E3")
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)
    Jump("loc_1811")

    label("loc_17E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1809")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    Jump("loc_1811")

    label("loc_1809")

    OP_66(0x0, 0x1)
    OP_66(0x1, 0x1)

    label("loc_1811")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_1824")
    OP_65(0x2, 0x1)
    SetMapObjFlags(0xC, 0x4)

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_END)), "loc_1833")
    SetMapObjFlags(0x9, 0x4)

    label("loc_1833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_184C")
    OP_52(0x2A, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_184C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_185F")
    OP_1B(0x15, 0x0, 0x8C)

    label("loc_185F")

    Return()

    # Function_4_1570 end

    def Function_5_1860(): pass

    label("Function_5_1860")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1877")
    Call(0, 83)
    Return()

    label("loc_1877")

    TalkBegin(0xFE)

    #C0001
    ChrTalk(
        0xFE,
        (
            "各位，今天实在是\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "总统阁下也\x01",
            "很高兴呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1860 end

    def Function_6_18BA(): pass

    label("Function_6_18BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18D1")
    Call(0, 93)
    Return()

    label("loc_18D1")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_18BA end

    def Function_7_18D8(): pass

    label("Function_7_18D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1A3D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FA")
    TalkEnd(0xFE)
    Call(0, 49)
    Return()

    label("loc_18FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B9")

    #C0003
    ChrTalk(
        0xFE,
        (
            "在此次事态平息之前，\x01",
            "我们将会把嫌疑人\x01",
            "库罗伊斯拘留在此。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "尽管他涉嫌\x01",
            "多项罪行……\x01",
            "但我却无法强烈谴责他。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "因为不管方法如何，他确实是\x01",
            "真心想要守护克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1A38")

    label("loc_19B9")


    #C0006
    ChrTalk(
        0xFE,
        (
            "尽管犯罪嫌疑人库罗伊斯\x01",
            "涉嫌多项罪行……\x01",
            "但我却无法强烈谴责他。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "因为不管方法如何，他确实是\x01",
            "真心想要守护克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A38")

    Jump("loc_1CE3")

    label("loc_1A3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1AAF")

    #C0008
    ChrTalk(
        0xFE,
        (
            "可恶，没想到那些恐怖分子\x01",
            "能做到这种地步。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "如果警备队可以行动，\x01",
            "应该能将事情解决，但是……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1CE3")

    label("loc_1AAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_1BBD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B60")

    #C0010
    ChrTalk(
        0xFE,
        (
            "呼，我要是能有个\x01",
            "尤莉亚准校那样的上司，\x01",
            "每天都会过得很充实吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "呃，不对不对，\x01",
            "我在胡思乱想什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "真是的，这说明我的\x01",
            "紧张感还不够啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1BB8")

    label("loc_1B60")


    #C0013
    ChrTalk(
        0xFE,
        (
            "目前的情况还不容乐观，\x01",
            "我却在胡思乱想……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "真是的，这说明我的\x01",
            "紧张感还不够啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BB8")

    Jump("loc_1CE3")

    label("loc_1BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1CE3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C71")

    #C0015
    ChrTalk(
        0xFE,
        (
            "呼，话说回来，这间回廊室的\x01",
            "视野可真是壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "将视线投向远方的时候，\x01",
            "感觉就像在空中漫步一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "呃，不行不行，\x01",
            "我必须要保持足够的紧张感。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1CE3")

    label("loc_1C71")


    #C0018
    ChrTalk(
        0xFE,
        (
            "待在这里的时候，\x01",
            "眼光不知不觉就被景色吸引住了……\x01",
            "我必须要保持足够的紧张感啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "杂念是有百害而无一利的。\x02",
    )

    CloseMessageWindow()

    label("loc_1CE3")

    TalkEnd(0xFE)
    Return()

    # Function_7_18D8 end

    def Function_8_1CE7(): pass

    label("Function_8_1CE7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D1C")

    #C0020
    ChrTalk(
        0xFE,
        "没有异常！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "巡逻继续进行！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1EF9")

    label("loc_1D1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1D84")

    #C0022
    ChrTalk(
        0xFE,
        (
            "看样子，导力梯和楼梯\x01",
            "现在都无法使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "必须要尽快想办法\x01",
            "改变这种被隔绝的状况……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1EF9")

    label("loc_1D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_1EAF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5F")

    #C0024
    ChrTalk(
        0xFE,
        (
            "那位是帝国军的\x01",
            "穆拉少校吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "而尤莉亚准校是\x01",
            "王国军·王室亲卫队的大队长……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "这种头衔的两个人会在一起，\x01",
            "还真是少见呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "看起来简直就像是亲密的朋友……\x01",
            "他们到底是什么关系呢？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1EAA")

    label("loc_1E5F")


    #C0028
    ChrTalk(
        0xFE,
        (
            "看上去，\x01",
            "他们简直就像是\x01",
            "亲密的朋友……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "这两位到底\x01",
            "是什么关系呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EAA")

    Jump("loc_1EF9")

    label("loc_1EAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1EF9")

    #C0030
    ChrTalk(
        0xFE,
        "正式会议终于开始了。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "这种紧张的感觉……\x01",
            "让我身心紧绷。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EF9")

    TalkEnd(0xFE)
    Return()

    # Function_8_1CE7 end

    def Function_9_1EFD(): pass

    label("Function_9_1EFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F12")
    Call(0, 10)
    Jump("loc_2083")

    label("loc_1F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2009")

    #C0032
    ChrTalk(
        0x18,
        (
            "#07108F说起来，\x01",
            "殿下刚才似乎是从\x01",
            "楼梯那边回来的……\x02\x03",

            "#07103F唔，但如今的殿下\x01",
            "就算见到了那个人，\x01",
            "也不会方寸大乱的。\x02\x03",

            "……担心应该是多余的。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00005F（……是指雷克特\x01",
            "  先生吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        "#10302F（呵呵，看来应该别有内情吧。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_2083")

    label("loc_2009")


    #C0035
    ChrTalk(
        0x18,
        (
            "#07103F如果在巡逻过程中了解到了什么情况，\x01",
            "请和我们联系。\x02\x03",

            "#07100F我们要是掌握到了新消息，\x01",
            "也会立刻向对策总部报告的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2083")

    TalkEnd(0xFE)
    Return()

    # Function_9_1EFD end

    def Function_10_2087(): pass

    label("Function_10_2087")

    OP_4B(0x19, 0xFF)
    OP_4B(0x18, 0xFF)
    TurnDirection(0x19, 0x0, 500)

    #C0036
    ChrTalk(
        0x19,
        "#07300F唔，是你们啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x0, 500)

    #C0037
    ChrTalk(
        0x18,
        "#07100F没有什么特殊情况吧？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00003F嗯，一切正常。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00101F二位得到什么\x01",
            "新消息了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x18,
        (
            "#07103F不，很遗憾，\x01",
            "目前并没有什么新消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x19,
        (
            "#07303F……帝国的相关人员\x01",
            "也在全力探查。\x02\x03",

            "#07301F但贵族派与革新派\x01",
            "都很谨慎，\x01",
            "并没有留下任何把柄。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#10108F是吗……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#00306F帝国的两大派系……\x01",
            "似乎是相当\x01",
            "不好对付的对手呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00103F………………………………\x02\x03",

            "#00108F那个……关于奥利维特皇子昨日\x01",
            "提到的『第三条路』……\x02\x03",

            "我一直很在意。\x02\x03",

            "#00101F如果方便，能容我询问一下\x01",
            "其中的含义吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#00005F艾莉……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x19,
        (
            "#07302F嗯，也难怪你会抱有疑问。\x02\x03",

            "#07304F虽然这些内容本不可\x01",
            "由我轻易言之……\x01",
            "不过告诉你们应该没问题吧。\x02\x03",

            "#07300F一言以蔽之——那家伙\x01",
            "想打破『壁障』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0047
    ChrTalk(
        0x101,
        "#00001F打破『壁障』……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x19,
        (
            "#07303F所谓壁障，大致来说就是存在于\x01",
            "革新派与贵族派之间的认知隔阂。\x02\x03",

            "#07300F也就是说，他想走的是\x01",
            "试图令两者融合的荆棘之路。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#00105F革新派与贵族派的融合……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，这种目标\x01",
            "与其说是困难至极，\x01",
            "倒不如说是近乎于理想主义了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#10101F瓦、瓦吉……！\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x19,
        (
            "#07302F呵呵……\x01",
            "无妨，事实正如你所说。\x02\x03",

            "#07304F但是，那家伙似乎已经下定了决心，\x01",
            "准备用这种荒谬绝伦的方法\x01",
            "与『怪物』展开对决。\x02\x03",

            "即使被人暗中评价为庶出皇子的心血来潮，\x01",
            "或是哗众取宠、博取人气的无聊行为，\x01",
            "他也无所畏惧。\x02\x03",

            "#07302F而我也已经决定\x01",
            "与他共同进退。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#00002F原、原来如此……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x18,
        (
            "#07104F穆拉少校……\x01",
            "正如科洛蒂娅殿下之前所说，\x01",
            "利贝尔王国会与皇子殿下站在同一方。\x02\x03",

            "#07102F虽然无法直接介入……\x01",
            "但在关键时刻，我们一定会不遗余力地提供协助。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x19,
        "#07304F嗯，真是万分感谢。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        (
            "#00202F这也算是皇子殿下的\x01",
            "仁德所至吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x19,
        (
            "#07304F呵呵，虽然那家伙\x01",
            "有些配不上这个词，\x01",
            "但或许正是如此吧。\x02\x03",

            "#07308F总之，我们目前最重要\x01",
            "的使命与目标，\x01",
            "就是让此次通商会议顺利结束。\x02\x03",

            "#07300F特别任务支援科的各位……\x01",
            "也期待你们能有活跃的表现。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x0, 0x0)
    OP_93(0x18, 0x0, 0x0)
    OP_4C(0x19, 0xFF)
    OP_4C(0x18, 0xFF)
    SetScenarioFlags(0x1C3, 5)
    Return()

    # Function_10_2087 end

    def Function_11_27B8(): pass

    label("Function_11_27B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27CD")
    Call(0, 10)
    Jump("loc_2856")

    label("loc_27CD")


    #C0058
    ChrTalk(
        0x19,
        (
            "#07303F总之，我们目前最重要\x01",
            "的使命与目标，\x01",
            "就是让此次通商会议顺利结束。\x02\x03",

            "#07300F特别任务支援科的各位……\x01",
            "也期待你们能有活跃的表现。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2856")

    TalkEnd(0xFE)
    Return()

    # Function_11_27B8 end

    def Function_12_285A(): pass

    label("Function_12_285A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_28EA")

    #C0059
    ChrTalk(
        0xFE,
        (
            "通过疏散楼梯，可以前往\x01",
            "三十层以下的中枢楼层，\x01",
            "但那个区域目前还无法确保安全。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "各位如果打算前往的话，\x01",
            "请务必多加小心。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B28")

    label("loc_28EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_29CD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2975")

    #C0061
    ChrTalk(
        0xFE,
        (
            "各、各位，\x01",
            "出大事了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "总之，我们会坚守岗位，\x01",
            "努力做好这个楼层的防卫工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "大家都要打起精神啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_29C8")

    label("loc_2975")


    #C0064
    ChrTalk(
        0xFE,
        (
            "总之，我们会坚守岗位，\x01",
            "努力做好这个楼层的防卫工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "大家都要打起精神啊！\x02",
    )

    CloseMessageWindow()

    label("loc_29C8")

    Jump("loc_2B28")

    label("loc_29CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2A6D")

    #C0066
    ChrTalk(
        0xFE,
        (
            "呼，该怎么说呢，\x01",
            "各位首脑的气场\x01",
            "果然非同寻常啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "虽然已经努力做好了心理准备，\x01",
            "但他们每次从这里经过的时候，\x01",
            "我还是会不由自主地紧张不安。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B28")

    label("loc_2A6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2B28")

    #C0068
    ChrTalk(
        0xFE,
        (
            "在ＶＩＰ楼层的右侧，\x01",
            "首间是市长和议长使用的房间，\x01",
            "然后是奥利维特皇子的房间……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "最里面则是\x01",
            "奥斯本宰相的\x01",
            "房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "顺带一提，\x01",
            "现在是清扫客房的时间，\x01",
            "你们可以随意出入。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B28")

    TalkEnd(0xFE)
    Return()

    # Function_12_285A end

    def Function_13_2B2C(): pass

    label("Function_13_2B2C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_2BC6")

    #C0071
    ChrTalk(
        0xFE,
        (
            "总之，我把左侧的工作人员\x01",
            "全部集中在这个房间里了！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "现在只能等待总部的指示，\x01",
            "让人感觉很不甘心……\x01",
            "但无论如何，还是要打起精神啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F26")

    label("loc_2BC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_2D49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9E")

    #C0073
    ChrTalk(
        0xFE,
        (
            "我刚才见到了\x01",
            "科洛蒂娅殿下……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "一天之内竟然能多次见到各国首脑，\x01",
            "而且还是在近距离看到……\x01",
            "这真是难以想象啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "总之，为了不让今天\x01",
            "成为我一辈子的污点，\x01",
            "必须要打起十二分的精神啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2D44")

    label("loc_2C9E")


    #C0076
    ChrTalk(
        0xFE,
        (
            "一天之内竟然能多次见到各国首脑，\x01",
            "而且还是在近距离看到……\x01",
            "这种事一生也不会再有第二次了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "总之，为了不让今天\x01",
            "成为我一辈子的污点，\x01",
            "必须要打起十二分的精神啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D44")

    Jump("loc_2F26")

    label("loc_2D49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2F26")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EC0")

    #C0078
    ChrTalk(
        0xFE,
        (
            "从我们这边算起，ＶＩＰ楼层左侧的\x01",
            "各房间分别为雷米菲利亚、利贝尔、\x01",
            "卡尔瓦德首脑的休息室。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "顺带一提，考虑到各国的具体情况，\x01",
            "在ＶＩＰ楼层只配备了\x01",
            "最低限度的人员进行警备。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "既然邀请了各国首脑，\x01",
            "即使是在这种情况下，\x01",
            "自然也需要保持最起码的保密性……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "不管怎么说，在休息时间，\x01",
            "各位首脑都有自己的护卫人员，\x01",
            "在安全方面应该不会有什么问题。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2F26")

    label("loc_2EC0")


    #C0082
    ChrTalk(
        0xFE,
        (
            "等到了休息时间，\x01",
            "一般人就不能\x01",
            "自由出入这个楼层了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "如果想确认一下各房间的情况，就趁现在吧。\x02",
    )

    CloseMessageWindow()

    label("loc_2F26")

    TalkEnd(0xFE)
    Return()

    # Function_13_2B2C end

    def Function_14_2F2A(): pass

    label("Function_14_2F2A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCA")

    #C0084
    ChrTalk(
        0xFE,
        (
            "这个房间是安排给\x01",
            "雷米菲利亚的\x01",
            "阿尔伯特大公使用的。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "据说大公在音乐方面\x01",
            "造诣很深。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "我们正在为他\x01",
            "准备麦克道尔议长\x01",
            "珍藏的唱片。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3055")

    label("loc_2FCA")


    #C0087
    ChrTalk(
        0xFE,
        (
            "麦克道尔议长和阿尔伯特大公的\x01",
            "交情好像很亲密呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "说起来，雷米菲利亚还是\x01",
            "乌尔斯拉医院的资助方呢，\x01",
            "他们的关系如此融洽，也不难理解。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3055")

    TalkEnd(0xFE)
    Return()

    # Function_14_2F2A end

    def Function_15_3059(): pass

    label("Function_15_3059")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_306A")
    Jump("loc_326A")

    label("loc_306A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_312F")

    #C0089
    ChrTalk(
        0xFE,
        (
            "戒严令颁布之后，才过了一个晚上，\x01",
            "但塔内所有人的疲劳度\x01",
            "却已经达到顶点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "连发生了什么事都不知道……\x01",
            "大家自然都感到相当不安。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "真希望这种状况\x01",
            "能早点平息……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_317B")

    label("loc_312F")


    #C0092
    ChrTalk(
        0xFE,
        (
            "塔内所有人的疲劳度\x01",
            "已经达到顶点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "真希望这种状况\x01",
            "能早点平息……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_317B")

    Jump("loc_326A")

    label("loc_3180")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_326A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321B")

    #C0094
    ChrTalk(
        0xFE,
        (
            "浇水浇水浇水……\x01",
            "整体上保持微微湿润的程度～\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        "嗯，这样一来，盆栽就完美了。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "接下来，再看一看\x01",
            "有没有泥土落在地上……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_326A")

    label("loc_321B")


    #C0097
    ChrTalk(
        0xFE,
        "嗯，这样一来，盆栽就完美了。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "接下来，再看一看\x01",
            "有没有泥土落在地上……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_326A")

    TalkEnd(0xFE)
    Return()

    # Function_15_3059 end

    def Function_16_326E(): pass

    label("Function_16_326E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3314")

    #C0099
    ChrTalk(
        0xFE,
        (
            "这里是阿尔伯特大公阁下\x01",
            "的房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "麦克道尔议长正在里面访问，\x01",
            "不过他交代过，如果各位来了，\x01",
            "随时可以入内。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "如果有需要，大家就请进吧。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_3380")

    label("loc_3314")


    #C0102
    ChrTalk(
        0xFE,
        (
            "麦克道尔议长正在里面访问，\x01",
            "不过他交代过，如果各位来了，\x01",
            "随时可以入内。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "如果有需要，大家就请进吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3380")

    TalkEnd(0xFE)
    Return()

    # Function_16_326E end

    def Function_17_3384(): pass

    label("Function_17_3384")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3399")
    Call(0, 18)
    Jump("loc_3425")

    label("loc_3399")


    #C0104
    ChrTalk(
        0xFE,
        (
            "唔，到了会议的后半程部分，\x01",
            "等待着我们的肯定会是\x01",
            "更加严峻的状况。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "尤其是两大国将提出的\x01",
            "关于安全保障的提案，\x01",
            "更需要进一步提高警惕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3425")

    TalkEnd(0xFE)
    SetChrSubChip(0x1A, 0x2)
    Return()

    # Function_17_3384 end

    def Function_18_342D(): pass

    label("Function_18_342D")

    SetChrSubChip(0x1A, 0x2)
    SetChrSubChip(0x2D, 0x1)

    #C0106
    ChrTalk(
        0x1A,
        (
            "呼，虽说讨论总算达成了共识，\x01",
            "但应对两大国的首脑\x01",
            "还真是让人疲劳啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x2D,
        (
            "#02509F呵呵，哪里，\x01",
            "大公阁下已经越来越有威严了。\x02\x03",

            "前代大公肯定也会为此感到欣慰的。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x1A,
        "……我继承大公之位，已经接近五年了。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x1A,
        (
            "国内的体制终于在\x01",
            "最近步入到正轨，\x01",
            "但老实说，我仍然不够成熟啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x1A, 0x10)
    TurnDirection(0x1A, 0x0, 0)
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_35E9")
    Jump("loc_3633")

    label("loc_35E9")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3609")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3633")

    label("loc_3609")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3629")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3633")

    label("loc_3629")

    OP_52(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3633")

    OP_52(0x1A, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x1A, 0x10)
    Sleep(500)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2D, 0x10)
    TurnDirection(0x2D, 0x0, 0)
    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_36EC")
    Jump("loc_3736")

    label("loc_36EC")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_370C")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3736")

    label("loc_370C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_372C")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3736")

    label("loc_372C")

    OP_52(0x2D, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3736")

    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2D, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_387F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_37A7")

    #C0110
    ChrTalk(
        0x1A,
        (
            "啊，你们是……\x01",
            "昨天承蒙各位的照顾了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_37BD")

    label("loc_37A7")


    #C0111
    ChrTalk(
        0x1A,
        "哎呀，你们是……\x02",
    )

    CloseMessageWindow()

    label("loc_37BD")


    #C0112
    ChrTalk(
        0x2D,
        "#02505F哦，是支援科的各位啊。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        "#00000F您好，打扰了。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x1A,
        (
            "唔，你们能够参与警备工作，\x01",
            "真是帮了大忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x1A,
        (
            "听说你们曾在麦克道尔议长\x01",
            "陷入危难之时将他解救，\x01",
            "有你们在，真是让人安心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BD1")

    label("loc_387F")


    #C0116
    ChrTalk(
        0x1A,
        "哎呀，你们是……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x2D,
        "#02500F哦，是支援科的各位啊。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00000F您好，打扰了。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1A,
        "唔，你们就是特别任务支援科啊。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x1A,
        (
            "初次见面，我听亚里欧斯说起过\x01",
            "你们的活跃表现。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x101,
        (
            "#00005F您认识\x01",
            "亚里欧斯先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1A,
        (
            "嗯，我和游击士协会\x01",
            "一直都有密切往来。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x1A,
        (
            "尤其是和亚里欧斯，\x01",
            "我们的私人交情也很深。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#00000F原来如此……是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x1A,
        "还有艾莉，好久不见了。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x1A,
        (
            "看来你在特别任务支援科\x01",
            "表现得很活跃呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        (
            "#00104F哪里……\x01",
            "多谢您的称赞。\x02\x03",

            "#00102F大公阁下身体健康，真是让人高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x109,
        (
            "#10105F（艾莉小姐……\x01",
            "  认识大公阁下啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        (
            "#00203F（虽然已经在一定程度上习惯了……\x01",
            "  但竟然和一国首脑都有往来，真是令人吃惊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#00306F（哎呀呀，越来越觉得大小姐的\x01",
            "  交际圈非同寻常了啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1A,
        (
            "像你们这样广受好评的人才能够\x01",
            "参加警备工作，真是令人高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x1A,
        (
            "听说你们曾在麦克道尔议长\x01",
            "陷入危难之时将他解救，\x01",
            "有你们在，真是让人安心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BD1")


    #C0133
    ChrTalk(
        0x101,
        "#00006F不敢当，您过奖了。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x2D,
        (
            "#02500F嗯，我也觉得很安心啊。\x02\x03",

            "托你们的福，我觉得在会议的后半程\x01",
            "也可以全身心地投入讨论了。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#00108F会议的后半程……\x02\x03",

            "#00101F外公，您认为后半程的\x01",
            "会议形势会很严峻吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x2D,
        (
            "#02503F嗯，与前半程不同，\x01",
            "他们恐怕将会接连提出\x01",
            "各种刺耳的指责。\x02\x03",

            "不过，我们对两大国提出的要求\x01",
            "也早已见怪不怪了……\x02\x03",

            "#02501F另一个让我不放心的\x01",
            "不安定因素则是迪塔。\x02\x03",

            "他在自治州议会上提出过\x01",
            "很多富有革新性的建议，\x01",
            "其热情与干劲令人佩服……\x02\x03",

            "但他毕竟还年轻，\x01",
            "我总担心他那种热情会使\x01",
            "局势向着不好的方向发展。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x109,
        "#10101F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#00200F的确，伊安律师\x01",
            "也说迪塔市长\x01",
            "有什么计划……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x2D,
        (
            "#02503F嗯，我也不知道具体内容，\x01",
            "不过，他的计划想必会\x01",
            "成为关键。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x1A,
        (
            "这个计划带来的结果\x01",
            "究竟是吉是凶……\x01",
            "就全都要取决于会议的讨论过程了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x2D,
        (
            "#02503F嗯，就是这样。\x02\x03",

            "#02500F在会议中为市长提供支持，\x01",
            "也是我这个议长的\x01",
            "职责与义务。\x02\x03",

            "无论如何，\x01",
            "我会尽己所能的。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#00101F外公……\x01",
            "拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C4, 0)
    ClearChrFlags(0x2D, 0x10)
    ClearChrFlags(0x1A, 0x10)
    Return()

    # Function_18_342D end

    def Function_19_3F57(): pass

    label("Function_19_3F57")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F6C")
    Call(0, 18)
    Jump("loc_3FCC")

    label("loc_3F6C")


    #C0143
    ChrTalk(
        0xFE,
        (
            "#02500F在会议中为市长提供支持，\x01",
            "也是我这个议长的\x01",
            "职责与义务。\x02\x03",

            "无论如何，\x01",
            "我会尽己所能的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FCC")

    TalkEnd(0xFE)
    SetChrSubChip(0x2D, 0x1)
    Return()

    # Function_19_3F57 end

    def Function_20_3FD4(): pass

    label("Function_20_3FD4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_3FE5")
    Jump("loc_404C")

    label("loc_3FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_401A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4000")
    Call(0, 21)
    Jump("loc_4015")

    label("loc_4000")


    #C0144
    ChrTalk(
        0x2A,
        "#08000F啾，啾！\x02",
    )

    CloseMessageWindow()

    label("loc_4015")

    Jump("loc_404C")

    label("loc_401A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_404C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4035")
    Call(0, 22)
    Jump("loc_404C")

    label("loc_4035")


    #C0145
    ChrTalk(
        0x2A,
        "#08000F啾，啾～！\x02",
    )

    CloseMessageWindow()

    label("loc_404C")

    TalkEnd(0xFE)
    Return()

    # Function_20_3FD4 end

    def Function_21_4050(): pass

    label("Function_21_4050")

    OP_4B(0x13, 0xFF)
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)

    #C0146
    ChrTalk(
        0x13,
        (
            "#07008F基库，如果出席本次\x01",
            "会议的是祖母大人，\x01",
            "她又会如何发言呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x2A,
        "#08000F啾，啾。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x13,
        (
            "#07000F呵呵，说的也是。\x01",
            "……我就是我，是吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x0, 500)

    #C0149
    ChrTalk(
        0x13,
        "#07002F啊，各位。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000F抱歉……\x01",
            "我们来得太突然了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x13,
        (
            "#07009F不，请不用在意。\x02\x03",

            "我在独处的时候，\x01",
            "总会胡思乱想……\x01",
            "大家能来，我很高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x109,
        "#10105F公主殿下……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        (
            "#00108F……说到胡思乱想，\x01",
            "自然与后半程的会议有关吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x13,
        (
            "#07000F嗯，也有这方面的原因……\x01",
            "但最重要的还是更根本的问题。\x02\x03",

            "#07003F身为王太女，\x01",
            "我对外交手段与谈判技巧\x01",
            "多少也有些心得……\x02\x03",

            "但通过前半程的会议，\x01",
            "我却深刻地体会到……\x02\x03",

            "#07001F无论是交涉过程中所需的洞察力、\x01",
            "判断力，还是平衡调控的能力……\x01",
            "我都比其他与会者差得太多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x103,
        "#00201F有那么严重吗……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        (
            "#00303F不过，您能这么\x01",
            "冷静地分析，\x01",
            "也已经很厉害了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        (
            "#10100F是啊，殿下和我们\x01",
            "基本同龄，\x01",
            "却具备着如此高的外交能力……\x02\x03",

            "真是令人自愧不如。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x13,
        (
            "#07002F呵呵，谢谢。\x02\x03",

            "#07003F说来也是呢，光说一些\x01",
            "丧气话，也起不到任何作用。\x02\x03",

            "虽说大陆的形势正在改变，\x01",
            "但我们还是要戒骄戒躁，\x01",
            "一步一步地积累经验。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        (
            "#10302F没错没错，而且\x01",
            "放松也是很重要的哦。\x02\x03",

            "现在可是难得\x01",
            "的休息时间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#00006F瓦吉……你对公主殿下的\x01",
            "态度就不能庄重些吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x13,
        (
            "#07009F呵呵，我完全不在意的。\x01",
            "比起过度客气，\x01",
            "这样反而让我更加轻松。\x02\x03",

            "#07002F说起来……真是不可思议。\x02\x03",

            "和你们说话的时候，\x01",
            "感觉就像和艾丝蒂尔\x01",
            "他们在一起时一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        "#00106F真是不敢当。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x13,
        (
            "#07000F呵呵，对了，\x01",
            "我给大家泡杯红茶吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0164
    ChrTalk(
        0x101,
        "#00005F不，不用客气了。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        "#00206F是的，我们还在进行警戒工作。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x13,
        (
            "#07004F抱歉，说的也是呢。\x02\x03",

            "#07000F那么，就请各位\x01",
            "多加小心吧。\x02\x03",

            "我也会努力\x01",
            "完成自己的任务的。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#00002F好的，明白了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1C4, 1)
    Return()

    # Function_21_4050 end

    def Function_22_46A9(): pass

    label("Function_22_46A9")

    OP_4B(0x20, 0xFF)
    TurnDirection(0x20, 0x0, 500)

    #C0168
    ChrTalk(
        0x20,
        "啊，各位是负责巡逻的……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#00000F嗯，打扰了。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x0, 500)

    #C0170
    ChrTalk(
        0x2A,
        "#08000F啾！\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00102F呵呵，是陪伴在科洛蒂娅殿下\x01",
            "身边的基库啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x103,
        (
            "#00205F原来如此，它就是\x01",
            "琪雅说的白隼……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x2A,
        "#08000F啾，啾！\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        "#00301F嗯？它在说什么？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        "#10100F缇欧能听明白吗？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        (
            "#00202F是的，它在对大家说『你们好』，\x01",
            "对我说『初次见面』。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        "#10302F呵呵，记得很清楚呢。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x2A,
        "#08009F啾，啾！\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#00202F它说『既然是科洛蒂娅公主的朋友，\x01",
            "我当然会记得』。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        "#00002F哈哈，谢啦。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x2A,
        "#08009F啾！\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x20, 0xFF)
    SetScenarioFlags(0x1C3, 6)
    Return()

    # Function_22_46A9 end

    def Function_23_48BF(): pass

    label("Function_23_48BF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_48D0")
    Jump("loc_4A5F")

    label("loc_48D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_49B8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4955")

    #C0182
    ChrTalk(
        0xFE,
        (
            "我们负责\x01",
            "照顾被困在\x01",
            "塔内的人。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "右侧那边的房间里还有一个小女孩……\x01",
            "被卷进这种事件，\x01",
            "真是可怜啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_49B3")

    label("loc_4955")


    #C0184
    ChrTalk(
        0xFE,
        (
            "右侧那边的房间里还有一个小女孩……\x01",
            "她好像很没精神。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "我待会给她拿一些\x01",
            "点心过去吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_49B3")

    Jump("loc_4A5F")

    label("loc_49B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_49FE")

    #C0186
    ChrTalk(
        0xFE,
        (
            "无、无论如何……\x01",
            "我们这些工作人员\x01",
            "必须要冷静行动。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A5F")

    label("loc_49FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4A0C")
    Jump("loc_4A5F")

    label("loc_4A0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4A5F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A27")
    Call(0, 22)
    Jump("loc_4A5F")

    label("loc_4A27")


    #C0187
    ChrTalk(
        0xFE,
        (
            "各位认识\x01",
            "基库啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "呵呵，基库可是\x01",
            "非常聪明的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4A5F")

    TalkEnd(0xFE)
    Return()

    # Function_23_48BF end

    def Function_24_4A63(): pass

    label("Function_24_4A63")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_4AE6")

    #C0189
    ChrTalk(
        0xFE,
        "是特别任务支援科的各位吧？\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "科洛蒂娅殿下吩咐过，\x01",
            "各位随时可以\x01",
            "自由通行。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        "如果有需要，大家就请进吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4AEF")

    label("loc_4AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4AEF")

    label("loc_4AEF")

    TalkEnd(0xFE)
    Return()

    # Function_24_4A63 end

    def Function_25_4AF3(): pass

    label("Function_25_4AF3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_4B04")
    Jump("loc_4B7F")

    label("loc_4B04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4B76")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B1F")
    Call(0, 21)
    Jump("loc_4B71")

    label("loc_4B1F")


    #C0192
    ChrTalk(
        0x13,
        (
            "#07000F各位，\x01",
            "感谢你们\x01",
            "陪我聊天。\x02\x03",

            "我们都要打起精神，\x01",
            "接下来也要一起努力哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B71")

    Jump("loc_4B7F")

    label("loc_4B76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4B7F")

    label("loc_4B7F")

    TalkEnd(0xFE)
    Return()

    # Function_25_4AF3 end

    def Function_26_4B83(): pass

    label("Function_26_4B83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_4BEE")

    #C0193
    ChrTalk(
        0xFE,
        (
            "为了不打扰到各位，\x01",
            "我们会在这里待命。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "在这种特殊时期，\x01",
            "行动时就更要保持理智啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4C63")

    label("loc_4BEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4BFC")
    Jump("loc_4C63")

    label("loc_4BFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4C63")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C17")
    Call(0, 27)
    Jump("loc_4C63")

    label("loc_4C17")


    #C0195
    ChrTalk(
        0xFE,
        (
            "印着咪西头像的\x01",
            "包子吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "在这种场合下， \x01",
            "总觉得有些\x01",
            "不太严肃……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C63")

    TalkEnd(0xFE)
    Return()

    # Function_26_4B83 end

    def Function_27_4C67(): pass

    label("Function_27_4C67")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x21, 0xFF)

    #C0197
    ChrTalk(
        0x1C,
        (
            "唔，真的可以给总统\x01",
            "准备这样的茶点吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x21,
        (
            "啊哈哈，这也是各位工作人员\x01",
            "绞尽脑汁才想出的决定，\x01",
            "应该不用担心啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x21,
        (
            "而且这种富有本地特色的感觉\x01",
            "不是很好嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x1C,
        (
            "唔～话虽如此，\x01",
            "但应该还有其它选择……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x102,
        (
            "#00105F（嗯？准备的茶点\x01",
            "  有什么问题吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0202
    ChrTalk(
        0x103,
        (
            "#00201F（那不是咪西包子吗……\x01",
            "  一般被称为『咪西包』。）\x02\x03",

            "（并没有什么问题吧？\x01",
            "  我认为没有比这更好的选择了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x109,
        "#10106F（是、是这样吗……？）\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00002F（哈哈，选用这种茶点，\x01",
            "  今后也许会成为话题呢。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1C, 0xFF)
    OP_4C(0x21, 0xFF)
    SetScenarioFlags(0x1C4, 2)
    Return()

    # Function_27_4C67 end

    def Function_28_4E61(): pass

    label("Function_28_4E61")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_4E9D")

    #C0205
    ChrTalk(
        0xFE,
        (
            "首、首先要做个深呼吸……\x01",
            "呼……哈……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F22")

    label("loc_4E9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4EAB")
    Jump("loc_4F22")

    label("loc_4EAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4F22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC6")
    Call(0, 27)
    Jump("loc_4F22")

    label("loc_4EC6")


    #C0206
    ChrTalk(
        0xFE,
        (
            "唔～听你这么一说，\x01",
            "我也有些不安了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "但是，事到如今，\x01",
            "也没时间准备其它点心了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F22")

    TalkEnd(0xFE)
    Return()

    # Function_28_4E61 end

    def Function_29_4F26(): pass

    label("Function_29_4F26")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FEC")

    #C0208
    ChrTalk(
        0x17,
        (
            "#07500F你们还在这里啊。\x02\x03",

            "唔，方便的话，\x01",
            "要不要和我一起喝杯茶？\x02\x03",

            "#07509F而且还有包子，\x01",
            "不妨在这里休息一下吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00006F不……\x01",
            "那怎么能行。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x102,
        "#00100F嗯，真是打扰您了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_504E")

    label("loc_4FEC")


    #C0211
    ChrTalk(
        0x17,
        (
            "#07503F（嚼嚼）……\x01",
            "话说回来，这包子真是极品啊。\x02\x03",

            "#07509F哈哈哈，多买一些，\x01",
            "当礼物带回去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_504E")

    TalkEnd(0xFE)
    Return()

    # Function_29_4F26 end

    def Function_30_5052(): pass

    label("Function_30_5052")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_50C6")

    #C0212
    ChrTalk(
        0xFE,
        (
            "现、现在好像不是\x01",
            "打扫房间的时候啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "（发抖）……\x01",
            "一想到那些不好的事情，\x01",
            "就忍不住发抖呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5180")

    label("loc_50C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_50D4")
    Jump("loc_5180")

    label("loc_50D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5180")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_513F")

    #C0214
    ChrTalk(
        0xFE,
        (
            "从这里看到的景色\x01",
            "真是绝妙无比啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "擦玻璃的时候，\x01",
            "不知不觉就会看入迷。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5180")

    label("loc_513F")

    OP_93(0xFE, 0x5A, 0x0)

    #C0216
    ChrTalk(
        0xFE,
        (
            "（擦拭）……\x01",
            "哼哼哼～¤\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "（擦拭）……\x01",
            "啦啦啦～¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5180")

    TalkEnd(0xFE)
    Return()

    # Function_30_5052 end

    def Function_31_5184(): pass

    label("Function_31_5184")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5200")

    #C0218
    ChrTalk(
        0xFE,
        (
            "这里是市长和议长\x01",
            "在休息时间共用的房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "为了正在会议上奋战的\x01",
            "市长和议长，\x01",
            "我一定要精心打扫。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5252")

    label("loc_5200")


    #C0220
    ChrTalk(
        0xFE,
        (
            "（掸灰尘）……\x01",
            "加油啊～迪塔市长¤\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "（掸灰尘）……\x01",
            "不要输～麦克道尔议长¤\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5252")

    TalkEnd(0xFE)
    Return()

    # Function_31_5184 end

    def Function_32_5256(): pass

    label("Function_32_5256")

    TalkBegin(0xFE)

    #C0222
    ChrTalk(
        0xFE,
        (
            "呼，接下来，\x01",
            "就只剩下后半程会议啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "不过，真正艰难的挑战，\x01",
            "现在才刚刚开始……\x01",
            "希望市长和议长能坚持下去。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_5256 end

    def Function_33_52D0(): pass

    label("Function_33_52D0")

    TalkBegin(0xFE)

    #C0224
    ChrTalk(
        0xFE,
        (
            "啊，各位，\x01",
            "迪塔市长正在隔壁的房间\x01",
            "拜访奥利维特皇子。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "而麦克道尔议长则在\x01",
            "位于左翼的阿尔伯特大公\x01",
            "休息室拜访。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "各位如果方便，\x01",
            "可以直接进去见他们。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_52D0 end

    def Function_34_5376(): pass

    label("Function_34_5376")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5387")
    Jump("loc_56ED")

    label("loc_5387")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_5555")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_549C")

    #C0227
    ChrTalk(
        0xFE,
        (
            "除了国防军之外，\x01",
            "总统似乎还雇佣了一些可疑的人\x01",
            "担当他的私人部队。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "我在兰花塔内见到过\x01",
            "那些袭击城市的猎兵，\x01",
            "还有本不该出现在这里的不良青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "虽然心中存有不少疑问，\x01",
            "但那毕竟不是我可以出言干预的问题……\x01",
            "现在回想起来，真是有不少可疑之处呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_5550")

    label("loc_549C")


    #C0230
    ChrTalk(
        0xFE,
        (
            "我在兰花塔内见到过\x01",
            "那些袭击城市的猎兵，\x01",
            "还有本不该出现在这里的不良青年。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "虽然心中存有不少疑问，\x01",
            "但那毕竟不是我可以出言干预的问题……\x01",
            "现在回想起来，真是有不少可疑之处呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5550")

    Jump("loc_56ED")

    label("loc_5555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_55AE")

    #C0232
    ChrTalk(
        0xFE,
        (
            "没想到恐怖分子\x01",
            "居然会直接\x01",
            "闯向会场……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "谁能预想到\x01",
            "这种事态呢……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56ED")

    label("loc_55AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_55BC")
    Jump("loc_56ED")

    label("loc_55BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_56ED")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5676")

    #C0234
    ChrTalk(
        0xFE,
        (
            "这里是奥利维特皇子\x01",
            "在休息时间使用的\x01",
            "房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "皇子是一位\x01",
            "真正的风雅人士，\x01",
            "在帝国的社交界有着活跃表现……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "在布置房间的时候，\x01",
            "我们自然也很花费心思。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_56ED")

    label("loc_5676")


    #C0237
    ChrTalk(
        0xFE,
        (
            "奥利维特皇子是一位\x01",
            "真正的风雅人士，\x01",
            "在帝国的社交界有着活跃表现……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "在布置房间的时候，\x01",
            "我们自然也很花费心思。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56ED")

    TalkEnd(0xFE)
    Return()

    # Function_34_5376 end

    def Function_35_56F1(): pass

    label("Function_35_56F1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_574C")

    #C0239
    ChrTalk(
        0xFE,
        (
            "我只能认为\x01",
            "自己是在做噩梦……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "……各位，接下来\x01",
            "到底会怎么样呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_57CD")

    label("loc_574C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_575A")
    Jump("loc_57CD")

    label("loc_575A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_57CD")

    #C0241
    ChrTalk(
        0xFE,
        (
            "听说奥利维特皇子\x01",
            "非常喜爱玫瑰花，尤其是红玫瑰，\x01",
            "所以我们才会这样布置房间。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "呵呵，希望他会喜欢。\x02",
    )

    CloseMessageWindow()

    label("loc_57CD")

    TalkEnd(0xFE)
    Return()

    # Function_35_56F1 end

    def Function_36_57D1(): pass

    label("Function_36_57D1")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_36_57D1 end

    def Function_37_57DB(): pass

    label("Function_37_57DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_605E")

    #C0243
    ChrTalk(
        0x2B,
        (
            "#02809F哈哈，原来如此。\x01",
            "那都是些前途无量的\x01",
            "年轻人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x2C,
        (
            "#07204F是啊，而且他们就像是一张白纸，\x01",
            "还没有被染上任何颜色。\x02\x03",

            "#07202F正因为如此，就更加——\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2C, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2C, 0x10)
    TurnDirection(0x2C, 0x0, 0)
    OP_52(0x2C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5939")
    Jump("loc_5983")

    label("loc_5939")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5959")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5983")

    label("loc_5959")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5979")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5983")

    label("loc_5979")

    OP_52(0x2C, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5983")

    OP_52(0x2C, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2C, 0x10)
    Sleep(50)
    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x2B, 0x10)
    TurnDirection(0x2B, 0x0, 0)
    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5A3C")
    Jump("loc_5A86")

    label("loc_5A3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5A5C")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A86")

    label("loc_5A5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_5A7C")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_5A86")

    label("loc_5A7C")

    OP_52(0x2B, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A86")

    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2B, 0x10)
    Sleep(100)

    #C0245
    ChrTalk(
        0x2C,
        (
            "#07205F哦，这不是支援科的各位吗。\x02\x03",

            "#07209F方便的话，\x01",
            "陪我们聊聊吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#00002F啊，好的，\x01",
            "如果不会打扰到二位的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#00102F请问两位刚才\x01",
            "在讨论什么话题呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x2B,
        (
            "#02804F哦，皇子殿下\x01",
            "担任了帝国\x01",
            "某所士官学校的理事。\x02\x03",

            "#02800F我们刚才正聊到这个。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        (
            "#00205F所谓的理事，\x01",
            "就是学校的负责人之一吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        "#00302F哦？您连那种工作都有涉足啊。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x2C,
        (
            "#07204F呵呵，也只是\x01",
            "挂了个名字而已啦。\x02\x03",

            "#07202F从这层意义上说，\x01",
            "迪塔市长的贡献\x01",
            "可比我大得多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x109,
        "#10105F迪塔市长的贡献……？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x2B,
        (
            "#02804F哪里哪里，我只是提供了\x01",
            "一些商业方面的支持而已。\x02\x03",

            "#02800F那所士官学校当时正准备\x01",
            "从爱普斯泰恩财团引进导力网络，\x01",
            "所以ＩＢＣ提供了一些资金。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        "#00105F是、是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#00205F说起来，我在财团总部听说，\x01",
            "帝国也已经开始\x01",
            "引进导力网络了……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，不愧是在各国\x01",
            "都拥有分行的国际银行，\x01",
            "业务范围果然十分广泛啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x2C,
        (
            "#07202F嗯，能跟你们聊到这个，\x01",
            "也算是一种缘分。\x02\x03",

            "#07209F有机会的话，\x01",
            "要不要在我的士官学校\x01",
            "举办一次特别讲座？\x02\x03",

            "#07212F你们要是愿意，\x01",
            "说不定还可以发展一段讲师与\x01",
            "士官候补生之间的禁忌关系呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0258
    ChrTalk(
        0x101,
        "#00006F说、说什么呢……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x2B, 0x1)

    #C0259
    ChrTalk(
        0x2B,
        (
            "#02809F哈哈，奥利维特殿下的心情\x01",
            "果然很愉快啊。\x02\x03",

            "希望下次能一边喝酒，\x01",
            "一边和你好好聊聊。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2C, 0x0)

    #C0260
    ChrTalk(
        0x2C,
        (
            "#07209F呵呵，的确，\x01",
            "我也希望有那个机会呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1200)

    #C0261
    ChrTalk(
        0x102,
        (
            "#00109F（皇子殿下和迪塔叔叔……\x01",
            "  似乎非常意气相投呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#00012F（嗯，他们两位都有过人气度，\x01",
            "  且富有情趣，所以很合得来吧？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 7)
    Jump("loc_6145")

    label("loc_605E")


    #C0263
    ChrTalk(
        0x2B,
        (
            "#02805F对了，\x01",
            "殿下的酒量好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x2C,
        (
            "#07202F啊，还算可以吧。\x02\x03",

            "#07204F……不过，这个世界上\x01",
            "真是天外有天啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#00200F（皇子殿下……\x01",
            "  若有所思地遥望着远方呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#00000F（嗯……？是不是有过什么\x01",
            "  与酒有关的宝贵经历呢？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6145")

    Return()

    # Function_37_57DB end

    def Function_38_6146(): pass

    label("Function_38_6146")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_38_6146 end

    def Function_39_6150(): pass

    label("Function_39_6150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6163")
    Call(0, 51)
    Return()

    label("loc_6163")

    TalkBegin(0xFE)

    #C0267
    ChrTalk(
        0x14,
        (
            "#11501F哦，那就是阿尔摩利卡村吗？\x02\x03",

            "#11509F小蜜蜂正在勤劳地采蜜呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0268
    ChrTalk(
        0x101,
        "#00006F那……那是不可能看得到的。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_6150 end

    def Function_40_623C(): pass

    label("Function_40_623C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_62E3")

    #C0269
    ChrTalk(
        0xFE,
        (
            "从发布戒严令开始，\x01",
            "我们就一直被拘禁在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "说起来，总统还\x01",
            "带着一个感觉\x01",
            "很不可思议的女孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "莫非那就是\x01",
            "传说中的『圣子』吗……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_6338")

    label("loc_62E3")


    #C0272
    ChrTalk(
        0xFE,
        (
            "总统带着\x01",
            "一个感觉\x01",
            "很不可思议的女孩子。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "莫非那就是\x01",
            "传说中的『圣子』吗……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6338")

    TalkEnd(0xFE)
    Return()

    # Function_40_623C end

    def Function_41_633C(): pass

    label("Function_41_633C")

    TalkBegin(0xFE)

    #C0274
    ChrTalk(
        0xFE,
        (
            "自从独立无效宣言发布以来，\x01",
            "我们这些在塔内工作的人\x01",
            "一直很不安……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "但、但实在没想到事情会变成这样。\x01",
            "今后到底会怎样呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_633C end

    def Function_42_63C4(): pass

    label("Function_42_63C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6520")

    #C0276
    ChrTalk(
        0xFE,
        "艾、艾莉小姐……！？\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x102,
        (
            "#00102F兰菲小姐……\x01",
            "你没事真是太好了。\x02\x03",

            "ＩＢＣ的人\x01",
            "都在这里吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "是、是的……\x01",
            "这是玛丽亚贝尔小姐的命令……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "市内发生了严重的情况， \x01",
            "迪塔总裁和玛丽亚贝尔小姐\x01",
            "到底在做什么啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#00001F……总而言之，\x01",
            "请你们暂时留在此地。\x02\x03",

            "我们会设法\x01",
            "改变现状的。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "我、我明白了……\x01",
            "那就拜托大家了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_657F")

    label("loc_6520")


    #C0282
    ChrTalk(
        0xFE,
        (
            "迪塔总裁和玛丽亚贝尔小姐\x01",
            "到底在做什么啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        "……而且，跟他们在一起的那个人好像是……\x02",
    )

    CloseMessageWindow()

    label("loc_657F")

    TalkEnd(0xFE)
    Return()

    # Function_42_63C4 end

    def Function_43_6583(): pass

    label("Function_43_6583")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6628")

    #C0284
    ChrTalk(
        0xFE,
        (
            "总统他们不在这个楼层……\x01",
            "不过，其他人或许知道些什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "这里暂且交给我们，\x01",
            "你们就安心进行调查工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        "……不过，一定不要太乱来啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_667D")

    label("loc_6628")


    #C0287
    ChrTalk(
        0xFE,
        (
            "这里暂且交给我们，\x01",
            "你们就安心进行调查工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        "……不过，一定不要太乱来啊。\x02",
    )

    CloseMessageWindow()

    label("loc_667D")

    TalkEnd(0xFE)
    Return()

    # Function_43_6583 end

    def Function_44_6681(): pass

    label("Function_44_6681")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_674E")

    #C0289
    ChrTalk(
        0xFE,
        (
            "我是因为相信玛丽亚贝尔小姐，\x01",
            "才会留在技术部的……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "但库雷却无论如何都无法相信她，\x01",
            "所以离开了技术部。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "在他临走时，我们还吵了一架……\x01",
            "如今看来，那家伙的选择\x01",
            "才是正确的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_67B0")

    label("loc_674E")


    #C0292
    ChrTalk(
        0xFE,
        (
            "……看来库雷的选择\x01",
            "才是正确的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "在他临走时，我们还吵了一架，\x01",
            "不知以后还能不能和好……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_67B0")

    TalkEnd(0xFE)
    Return()

    # Function_44_6681 end

    def Function_45_67B4(): pass

    label("Function_45_67B4")

    TalkBegin(0xFE)

    #C0294
    ChrTalk(
        0xFE,
        (
            "戒严令颁布之后，\x01",
            "市外的消息\x01",
            "就被完全封锁了。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "导力网络的终端也不能用了，\x01",
            "真不知该说什么好……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_67B4 end

    def Function_46_6822(): pass

    label("Function_46_6822")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68E7")

    #C0296
    ChrTalk(
        0xFE,
        (
            "对于保安部门来说，\x01",
            "了解塔内构造和职员们的\x01",
            "工作情况都是有必要的……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "但自从搬到兰花塔之后，\x01",
            "总觉得秘而不宣的事情越来越多。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐他们\x01",
            "到底干了什么啊……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_6914")

    label("loc_68E7")


    #C0299
    ChrTalk(
        0xFE,
        (
            "玛丽亚贝尔小姐他们\x01",
            "到底干了什么啊……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6914")

    TalkEnd(0xFE)
    Return()

    # Function_46_6822 end

    def Function_47_6918(): pass

    label("Function_47_6918")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_69C6")

    #C0300
    ChrTalk(
        0xFE,
        (
            "迪塔总统涉嫌勾结\x01",
            "危险度Ｓ级的猎兵团\x01",
            "『赤色星座』……\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "因为那些炸了ＩＢＣ的家伙\x01",
            "竟然可以大摇大摆地到处闲晃。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        "……已经不能再……信任总统了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_69EB")

    label("loc_69C6")


    #C0303
    ChrTalk(
        0xFE,
        (
            "迪塔总统……\x01",
            "已经不值得信任了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_69EB")

    TalkEnd(0xFE)
    Return()

    # Function_47_6918 end

    def Function_48_69EF(): pass

    label("Function_48_69EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AAA")

    #C0304
    ChrTalk(
        0xC,
        (
            "#11228F我觉得爸爸……\x01",
            "一直都在烦恼。\x02\x03",

            "关于妈妈……关于我……\x02\x03",

            "要考虑的事情实在太多，\x01",
            "使他走上了一条无法回头的路……\x02\x03",

            "#11227F……各位……\x01",
            "爸爸就拜托\x01",
            "你们了……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_6ADB")

    label("loc_6AAA")


    #C0305
    ChrTalk(
        0xC,
        (
            "#11227F……各位……\x01",
            "爸爸就拜托\x01",
            "你们了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6ADB")

    TalkEnd(0xFE)
    Return()

    # Function_48_69EF end

    def Function_49_6ADF(): pass

    label("Function_49_6ADF")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x11, 0xFF)
    SetChrFlags(0x12, 0x80)
    OP_68(110010, 1100, -102270, 0)
    MoveCamera(30, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 109100, 0, -103400, 90)
    SetChrPos(0x102, 108800, 0, -102500, 90)
    SetChrPos(0x103, 107600, 0, -103100, 90)
    SetChrPos(0x104, 107300, 0, -102200, 90)
    SetChrPos(0xF4, 109000, 0, -100900, 135)
    SetChrPos(0xF5, 108000, 0, -100300, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6DF8")

    #C0306
    ChrTalk(
        0x11,
        (
            "#11P辛苦了，\x01",
            "是特别任务支援科的各位吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        (
            "#6P#00003F#6P是的，你也辛苦了。\x02\x03",

            "#00005F这个房间难道是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x11,
        (
            "#11P是的，总统……\x01",
            "不，犯罪嫌疑人库罗伊斯就被关押在这里。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0309
    ChrTalk(
        0x102,
        "#6P#00108F……总统的情况如何？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x11,
        (
            "#11P被我们警队拘捕的时候，\x01",
            "他一副茫然若失的样子……\x01",
            "但现在已经恢复了平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x11,
        (
            "#11P由于他没有反抗的迹象，\x01",
            "所以我们将看管人员\x01",
            "减少到了最低限度。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x11,
        (
            "#11P遵照赛尔盖警督的指示，\x01",
            "各位可以与他会面……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x104,
        "#6P#00306F是吗……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#6P#00208F……罗伊德前辈，该怎么办？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 7)
    Jump("loc_6E5D")

    label("loc_6DF8")


    #C0315
    ChrTalk(
        0x11,
        (
            "#11P这个房间里\x01",
            "关押着犯罪嫌疑人\x01",
            "库罗伊斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x11,
        (
            "#11P遵照赛尔盖警督的指示，\x01",
            "各位可以与他会面……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6E5D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6E67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F51")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "与迪塔会面\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EC1")
    Call(0, 50)
    Return()

    label("loc_6EC1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F4C")

    #C0317
    ChrTalk(
        0x101,
        "#6P#00006F……现在还是算了。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x11,
        "#11P我明白了。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "#11P各位想和犯罪嫌疑人\x01",
            "库罗伊斯会面的时候，\x01",
            "跟我说一声就可以了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6F4C")

    Jump("loc_6E67")

    label("loc_6F51")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x11, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 110390, 0, -126470, 0)
    BeginChrThread(0x12, 0, 0, 1)
    EventEnd(0x5)
    Return()

    # Function_49_6ADF end

    def Function_50_6F88(): pass

    label("Function_50_6F88")


    #C0320
    ChrTalk(
        0x101,
        (
            "#6P#00003F……那就麻烦你了。\x02\x03",

            "#00008F我想知道……\x01",
            "他如今正在想些什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        "#6P#00106F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x11,
        "#11P明白了……请进。\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x0, 0x1F4)

    def lambda_7026():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_7026)
    WaitChrThread(0x11, 1)
    OP_93(0x11, 0xE1, 0x1F4)
    ClearMapObjFlags(0x2, 0x10)
    BeginChrThread(0x101, 3, 0, 94)
    Sleep(700)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    BeginChrThread(0x102, 3, 0, 94)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x103, 3, 0, 94)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 94)
    OP_0D()
    LoadChrToIndex("apl/ch51716.itc", 0x28)
    SetChrChipByIndex(0x2B, 0x28)
    SetChrSubChip(0x2B, 0x0)
    SetChrPos(0x2B, 156990, 0, 110700, 45)
    OP_8E(0x2B, "迪塔总统")
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x104, 0x0)
    OP_68(156330, 1500, 108970, 0)
    MoveCamera(39, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16050, 0)
    SetChrPos(0x11, 162130, 0, 110210, 225)
    SetChrPos(0x27, 161880, 0, 102310, 315)
    OP_4B(0x27, 0xFF)
    SetChrPos(0x101, 156570, 0, 108170, 356)
    SetChrPos(0x102, 158130, 0, 108480, 322)
    SetChrPos(0x103, 158750, 0, 107480, 315)
    SetChrPos(0x104, 159040, 0, 108660, 322)
    SetChrPos(0xF4, 155360, 0, 107640, 45)
    SetChrPos(0xF5, 157370, 0, 107370, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetCameraDistance(14610, 2000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0323
    ChrTalk(
        0x2B,
        (
            "#11301F#5P………………是你们啊。\x02\x03",

            "#11304F……呵呵，有什么事吗？\x01",
            "找我这个已经是国际罪犯的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        "#12P#00001F……迪塔先生。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        "#12P#00108F…………迪塔叔叔…………\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x2B,
        (
            "#11306F#5P……经过这段时间的独处，\x01",
            "我终于明白了。\x02\x03",

            "正如贝尔所说，\x01",
            "一直以来，我只是在按照格里姆伍德\x01",
            "律师的想法而行动。\x02\x03",

            "#11303F大声疾呼『正义』这一理想，\x01",
            "为此不惜做出一切牺牲。\x02\x03",

            "#11311F……但结果又如何呢？\x01",
            "独生女儿都对我弃之不顾，\x01",
            "如今更是连总统的地位都失去了。\x02\x03",

            "#11302F……哈哈哈哈……\x01",
            "我虽然不是『结社』的那个少年，\x01",
            "但现在真像一个悲哀的小丑啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x2, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x3, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_64(0x4)
    OP_64(0x5)
    Sleep(500)

    #C0327
    ChrTalk(
        0x101,
        (
            "#12P#00006F……我们无法\x01",
            "否定您的一切。\x02\x03",

            "#00008F为了实现自己的『正义』，\x01",
            "把信念贯彻到底……\x02\x03",

            "#00001F方法暂且不论，\x01",
            "您想要维护克洛斯贝尔的和平\x01",
            "是不争的事实。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#12P#00303F……是啊。\x02\x03",

            "#00301F你以前在ＩＢＣ\x01",
            "说过的话也让我们\x01",
            "很有感触。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#12P#00203F『人是一种会追求正义的生物』……\x01",
            "或许正如您所说。\x02\x03",

            "#00208F市民们之所以会赞同独立宣言，\x01",
            "大概也是因为觉得您追寻\x01",
            "『正义』的身影很有魅力吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x2B,
        "#11303F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        (
            "#12P#00106F但我还是觉得……\x01",
            "迪塔叔叔的做法是错误的。\x02\x03",

            "#00108F就算独立国一直存续，\x01",
            "迪塔叔叔的『正义』得到世人的认同，\x01",
            "并迎来和平时代……\x02\x03",

            "在此过程中被牺牲的那些人\x01",
            "所受的创伤也是难以痊愈的。\x02\x03",

            "#00101F以牺牲他人为前提\x01",
            "而获取和平……\x02\x03",

            "不正是迪塔叔叔在发表\x01",
            "独立宣言的演讲台上\x01",
            "所说的『欺瞒』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x2B,
        (
            "#11304F#5P……呵呵，是啊。\x01",
            "艾莉，你说的没错呢。\x02\x03",

            "自从得到琪雅的力量之后，\x01",
            "我对自己『正义』的追求似乎就\x01",
            "越来越盲目了。\x02\x03",

            "#11302F在格里姆伍德律师看来，\x01",
            "一直没能发现这种欺瞒的我\x01",
            "想必很容易操控吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_784F")

    #C0333
    ChrTalk(
        0x10A,
        "#12P#00603F（……伊安律师……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_78BE")

    label("loc_784F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7889")

    #C0334
    ChrTalk(
        0x105,
        "#12P#10403F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_78BE")

    label("loc_7889")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_78BE")

    #C0335
    ChrTalk(
        0x106,
        "#12P#10703F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_78BE")


    #C0336
    ChrTalk(
        0x2B,
        (
            "#11303F#5P但是……『正义』永远\x01",
            "都要凭借力量与意志来实现，\x01",
            "我至今仍然坚持这种观点。\x02\x03",

            "#11301F如果你们决定继续\x01",
            "追寻你们自己的『正义』……\x02\x03",

            "那就必须要向律师他们\x01",
            "展现出你们的力量与意志。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#12P#00006F这肯定不是一件\x01",
            "简单的事……\x02\x03",

            "#00013F但为了带回琪雅，\x01",
            "我们一定会努力做到的……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A09")

    #C0338
    ChrTalk(
        0x106,
        "#12P#10701F……是啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A66")

    label("loc_7A09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A39")

    #C0339
    ChrTalk(
        0x109,
        "#12P#10101F嗯，当然。\x02",
    )

    CloseMessageWindow()
    Jump("loc_7A66")

    label("loc_7A39")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A66")

    #C0340
    ChrTalk(
        0x105,
        "#12P#10402F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_7A66")


    #C0341
    ChrTalk(
        0x2B,
        (
            "#11301F#5P……既然如此，我也就\x01",
            "没什么话需要对你们说了。\x02\x03",

            "#11303F律师先生自不必说……\x01",
            "我女儿贝尔也是个深不可测的人。\x02\x03",

            "#11304F你们究竟能否把琪雅带回来，\x01",
            "并继续前进……\x02\x03",

            "#11300F就让我在这里拭目以待吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_70(0x2, 0x0)
    SetChrPos(0x11, 111300, 0, -102500, 270)
    SetChrPos(0x27, -3110, 0, 1600, 90)
    SetChrPos(0x101, 109100, 0, -103400, 90)
    SetChrPos(0x102, 109600, 0, -101800, 90)
    SetChrPos(0x103, 107600, 0, -103600, 90)
    SetChrPos(0x104, 107000, 0, -102400, 90)
    SetChrPos(0xF4, 108500, 0, -100900, 135)
    SetChrPos(0xF5, 107500, 0, -100800, 135)
    OP_68(109860, 400, -101510, 0)
    MoveCamera(44, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17830, 0)
    TurnDirection(0x101, 0x102, 0)
    TurnDirection(0x103, 0x102, 0)
    TurnDirection(0x104, 0x102, 0)
    TurnDirection(0xF4, 0x102, 0)
    TurnDirection(0xF5, 0x102, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(300)

    #C0342
    ChrTalk(
        0x102,
        "#5P#00106F………………………………\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x104,
        "#6P#00301F大小姐……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x103,
        "#6P#00208F……没事吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(150)

    #C0345
    ChrTalk(
        0x102,
        (
            "#5P#00104F……嗯，没事的。\x02\x03",

            "#00108F贝尔当时那么绝情地对迪塔叔叔弃之不顾，\x01",
            "我原本还有些担心……\x02\x03",

            "#00102F但他真是意外地坚强。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#12P#00004F……嗯，我也放心了。\x02\x03",

            "#00000F正如他所说……\x01",
            "我们继续前进吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 110390, 0, -126470, 0)
    BeginChrThread(0x12, 0, 0, 1)
    OP_4C(0x11, 0xFF)
    OP_4C(0x27, 0xFF)
    SetChrPos(0x0, 109100, 0, -103400, 180)
    SetScenarioFlags(0x1AF, 6)
    EventEnd(0x5)
    Return()

    # Function_50_6F88 end

    def Function_51_7DB0(): pass

    label("Function_51_7DB0")

    EventBegin(0x0)
    OP_4B(0x14, 0xFF)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11500.itp")
    OP_68(158620, 1300, 109080, 0)
    MoveCamera(36, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16290, 0)
    SetChrPos(0x101, 158620, 0, 109080, 45)
    SetChrPos(0x102, 157420, 0, 109080, 45)
    SetChrPos(0x103, 159110, 0, 107900, 45)
    SetChrPos(0x104, 157120, 0, 107350, 45)
    SetChrPos(0x109, 156000, 0, 107350, 45)
    SetChrPos(0x105, 155330, 0, 107970, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0347
    ChrTalk(
        0x14,
        (
            "#11P#11504F哎呀，话说回来，\x01",
            "这风景还真是夸张呢。\x02\x03",

            "#11500F特别任务支援科的各位，\x01",
            "你们也这样想吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#6P#00011F雷克特先生……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#6P#00108F您为何会在这里……\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x14,
        (
            "#11P#11504F哈哈，宰相阁下的随行人员\x01",
            "待在宰相的休息室里，\x01",
            "又有什么好奇怪的？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x14, 0xE1, 0x1F4)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_8022")

    #A0351
    AnonymousTalk(
        0x14,
        (
            "你们好啊，又见面了呢。\x02\x03",

            "啊，不对……\x01",
            "我搞错了，应该是初次见面吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_8079")

    label("loc_8022")


    #A0352
    AnonymousTalk(
        0x14,
        (
            "上次与各位见面，\x01",
            "是在几周之前了呢。\x02\x03",

            "啊，不对……\x01",
            "我搞错了，应该是初次见面吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_8079")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0353
    ChrTalk(
        0x102,
        (
            "#6P#00106F那个……请您不要\x01",
            "这么一本正经地开玩笑。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x103,
        (
            "#12P#00211F……还是和以前一样\x01",
            "难以捉摸呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x14,
        (
            "#11P#11509F哈哈，这正是\x01",
            "我的魅力所在啊。\x02\x03",

            "#11502F嗯？看你们的表情，\x01",
            "似乎是有话想说啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#6P#00006F是的，托您的福，\x01",
            "我们掌握到了一些消息。\x02\x03",

            "#00013F也就是你们帝国政府\x01",
            "在本次通商会议中的动向……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x14,
        (
            "#11P#11510F嗯，原来如此。\x01",
            "虽然不知道你们\x01",
            "已经掌握了多少……\x02\x03",

            "#11504F不过，知道这件事吗？\x02\x03",

            "#11501F我暗中串通『贵族派』，\x01",
            "准备取吉利亚斯·奥斯本的性命。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0358
    ChrTalk(
        0x109,
        "#6P#10107F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x105,
        "#6P#10301F咦……？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        (
            "#6P#00106F……别上当，\x01",
            "这就是他的惯用手段。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#6P#00301F谁会被同样的伎俩\x01",
            "连骗两次啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x103,
        "#12P#00211F未免也太小看人了。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x14,
        (
            "#11P#11509F哈哈，真是失败。\x02\x03",

            "#11502F哎，老实说，\x01",
            "我还期待你们表现出\x01",
            "更激烈的反应呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，该不会\x01",
            "弄假成真吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        (
            "#6P#00006F……雷克特书记官，\x01",
            "您的立场和目的与我们无关。\x02\x03",

            "#00008F在我看来……\x01",
            "您是那种无论接受什么样的工作，\x01",
            "都会负责到底的人。\x02\x03",

            "#00001F从这层意义来说，\x01",
            "在通商会议的过程中，我们至少\x01",
            "可以在警备工作中互相协助……\x02\x03",

            "#00000F难道不是吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x14,
        (
            "#11P#11504F呵呵……原来如此。\x02\x03",

            "#11508F好啦，就把刚才那些发言当作玩笑话吧。\x01",
            "但这样一说，更会让你们浮想联翩吧？\x02\x03",

            "#11501F永远不要停止\x01",
            "对一切可能性的探询。\x02\x03",

            "#11509F这就是写出好故事的秘诀哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x4, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x5, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0367
    ChrTalk(
        0x101,
        (
            "#6P#00006F这里又没有\x01",
            "想当作家的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x104,
        (
            "#6P#00301F真是的，这家伙到底\x01",
            "有多喜欢捉弄人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x14,
        (
            "#11P#11504F刚才说的那些，\x01",
            "就算是我给你们的建议吧。\x02\x03",

            "#11500F你们不妨好好思考一下，\x01",
            "以便应对各种有可能发生的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x109,
        "#6P#10106F……谢谢您的忠告。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#6P#00006F（呼……真是个\x01",
            "  捉摸不透的人啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#6P#00108F（是啊，和他谈完之后，\x01",
            "  反而更加迷惑了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x14, 0x0, 0x0)
    OP_4C(0x14, 0xFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1C4, 3)
    Call(0, 53)
    EventEnd(0x5)
    Return()

    # Function_51_7DB0 end

    def Function_52_8805(): pass

    label("Function_52_8805")

    Sound(160, 0, 100, 0)
    Return()

    # Function_52_8805 end

    def Function_53_880C(): pass

    label("Function_53_880C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8834")
    SetScenarioFlags(0x146, 3)

    label("loc_8834")

    Return()

    # Function_53_880C end

    def Function_54_8835(): pass

    label("Function_54_8835")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x28)
    LoadChrToIndex("apl/ch51231.itc", 0x29)
    CreatePortrait(0, 16, 192, 528, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis506.itp")
    OP_68(81000, 1000, 4000, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 81000, 0, 5500, 180)
    SetChrPos(0x102, 81000, 0, 5500, 180)
    SetChrPos(0x103, 81000, 0, 5500, 180)
    SetChrPos(0x104, 81000, 0, 5500, 180)
    SetChrPos(0x109, 81000, 0, 5500, 180)
    SetChrPos(0x105, 81000, 0, 5500, 180)
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
    SetChrChipByIndex(0x2B, 0x28)
    SetChrSubChip(0x2B, 0x0)
    ClearChrFlags(0x2B, 0x80)
    SetChrFlags(0x2B, 0x8000)
    SetChrPos(0x2B, 81000, 0, 5500, 180)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(79000, 1000, 300, 5000)
    SetCameraDistance(18500, 5000)
    BeginChrThread(0x101, 0, 0, 55)
    FadeToBright(1000, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0373
    ChrTalk(
        0x2B,
        (
            "#6P#02803F这个楼层是为\x01",
            "与会各国首脑\x01",
            "准备的休息区域。\x02\x03",

            "#02800F我给你们大致介绍一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x101,
        "#00000F#11P麻烦您了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x2B, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, 112700, 0, -131500, 270)
    SetChrPos(0x102, 112700, 0, -130000, 270)
    SetChrPos(0x103, 113900, 0, -131100, 270)
    SetChrPos(0x104, 113900, 0, -129600, 270)
    SetChrPos(0x109, 115100, 0, -131300, 270)
    SetChrPos(0x105, 115100, 0, -129800, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x2B, 111000, 0, -130500, 270)
    SetChrPos(0x35, 111000, -600, -130500, 270)
    OP_68(109220, 1500, -130990, 0)
    MoveCamera(34, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrFlags(0x35, 0x20)
    SetChrFlags(0x35, 0x40)
    SetChrFlags(0x35, 0x8)
    SetChrFlags(0x35, 0x4)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    OP_68(108910, 1500, -111640, 13000)
    FadeToBright(1000, 0)
    BeginChrThread(0x2B, 3, 0, 63)
    BeginChrThread(0x35, 3, 0, 64)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 65)
    Sleep(400)
    BeginChrThread(0x103, 3, 0, 67)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 66)
    BeginChrThread(0x109, 3, 0, 69)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 68)
    Sleep(100)
    BeginChrThread(0x105, 3, 0, 70)
    OP_0D()
    WaitChrThread(0x2B, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x101, 3, 0, 71)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 71)
    OP_0D()
    EndChrThread(0x2B, 0xFF)
    EndChrThread(0x35, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, 153000, 0, 55500, 90)
    SetChrPos(0x102, 152600, 0, 56800, 90)
    SetChrPos(0x103, 152600, 0, 53900, 135)
    SetChrPos(0x104, 151900, 0, 57900, 45)
    SetChrPos(0x109, 151700, 0, 55500, 90)
    SetChrPos(0x105, 150800, 0, 53700, 135)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x2B, 149300, 0, 56000, 90)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(163300, 1500, 56000, 0)
    MoveCamera(53, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_68(153300, 900, 56000, 5000)
    SetCameraDistance(18000, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0375
    ChrTalk(
        0x104,
        "#00305F#5P哦，果然很豪华啊。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，真想在这种房间里\x01",
            "度过一段优雅时光呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x2B,
        (
            "#6P#02804F这里是准备给\x01",
            "奥利维特殿下使用的休息室。\x02\x03",

            "#02800F这个楼层的左翼也有房间，\x01",
            "将由各位参与会议者分别使用。\x02\x03",

            "#02809F总之，这个地方的作用就是让那些\x01",
            "在会议上头脑发热的人冷静一下。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8E53():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8E53)
    Sleep(50)

    def lambda_8E63():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8E63)
    Sleep(50)

    def lambda_8E73():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8E73)
    Sleep(50)

    def lambda_8E83():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E83)
    Sleep(50)

    def lambda_8E93():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_8E93)
    Sleep(50)

    def lambda_8EA3():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8EA3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0378
    ChrTalk(
        0x109,
        "#11P#10112F原、原来如此。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x103,
        (
            "#00205F#11P那么，这些房间中\x01",
            "也有导力线路……？\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x2B,
        (
            "#6P#02805F是的，为了房间的美观，\x01",
            "铺设了暗线。\x02\x03",

            "#02804F其它的房间\x01",
            "就不一一带你们去看了……\x02\x03",

            "#02800F最后就领你们\x01",
            "去看看那个地方吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6B(0x35)
    EndChrThread(0x2B, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x2B, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(12000, 900, -130000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 12200, 0, -129300, 270)
    SetChrPos(0x102, 11600, 0, -130699, 270)
    SetChrPos(0x103, 13300, 0, -129800, 270)
    SetChrPos(0x104, 13000, 0, -131000, 270)
    SetChrPos(0x109, 14400, 0, -129300, 270)
    SetChrPos(0x105, 14700, 0, -130699, 270)
    SetChrPos(0x2B, 10000, 0, -130000, 270)
    SetChrPos(0x35, 12000, -600, -130000, 270)
    SetChrChipByIndex(0x11, 0x0)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 7400, 0, -127600, 225)
    SetChrChipByIndex(0x12, 0x0)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -7400, 0, -127600, 135)

    def lambda_9115():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_9115)

    def lambda_912F():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_912F)
    Sleep(50)

    def lambda_914C():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_914C)
    Sleep(50)

    def lambda_9169():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9169)
    Sleep(50)

    def lambda_9186():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9186)
    Sleep(50)

    def lambda_91A3():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91A3)
    Sleep(50)

    def lambda_91C0():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_91C0)
    Sleep(50)

    def lambda_91DD():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_91DD)
    FadeToBright(1000, 0)
    Sleep(600)

    def lambda_9203():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9203)
    Sleep(300)

    def lambda_9217():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9217)
    Sleep(600)

    def lambda_922B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_922B)
    Sleep(300)

    def lambda_923F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_923F)
    OP_0D()
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)

    #C0381
    ChrTalk(
        0x11,
        "#12A#5P啊，迪塔市长！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    Sleep(2500)
    OP_4B(0x12, 0xFF)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x0)

    #C0382
    ChrTalk(
        0x12,
        "#12A#5P您辛苦了！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x2B, 1)

    #C0383
    ChrTalk(
        0x2B,
        "#02809F#11P哈哈，不用那么紧张。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x35, 1)
    OP_6B(0xFF)
    WaitChrThread(0x105, 1)
    OP_93(0x2B, 0x5A, 0x1F4)

    #C0384
    ChrTalk(
        0x2B,
        (
            "#6P#02804F在这间回廊室里，\x01",
            "可以俯瞰会议现场的情况。\x02\x03",

            "#02800F在召开机密性较高的会议时，\x01",
            "将会把帘子拉上，\x01",
            "但这次是预定将帘子打开的。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        "#00000F#11P原来如此……\x02",
    )

    CloseMessageWindow()

    def lambda_9388():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9388)
    Sleep(50)

    def lambda_9398():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9398)
    Sleep(50)

    def lambda_93A8():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_93A8)
    Sleep(50)

    def lambda_93B8():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_93B8)
    Sleep(50)

    def lambda_93C8():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_93C8)
    Sleep(50)

    def lambda_93D8():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_93D8)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    OP_68(-2000, 1500, -124000, 3000)
    MoveCamera(35, 17, 0, 3000)
    SetCameraDistance(19500, 3000)

    def lambda_9422():
        OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9422)
    Sleep(200)

    def lambda_943F():
        OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_943F)
    Sleep(200)

    def lambda_945C():
        OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_945C)
    Sleep(200)

    def lambda_9479():
        OP_97(0x102, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9479)
    Sleep(200)

    def lambda_9496():
        OP_97(0x104, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9496)
    Sleep(200)

    def lambda_94B3():
        OP_97(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_94B3)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_94E5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_94E5)
    OP_6F(0x79)

    #C0386
    ChrTalk(
        0x101,
        (
            "#00002F#11P这样就能确认到会场内的情况了，\x01",
            "真是值得庆幸啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#00104F#11P是啊，如果发生了特殊情况，\x01",
            "我们也可以马上赶到。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x109,
        (
            "#10100F#11P既然如此，我们应该\x01",
            "把这里加进巡逻路线呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-3000, 900, -128000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    #C0389
    ChrTalk(
        0x2B,
        (
            "#6P#02803F好了，已经把你们负责警备的\x01",
            "三个楼层介绍完了……\x02\x03",

            "#02800F接下来，就带你们去\x01",
            "我秘藏的好地方吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9652():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9652)
    Sleep(50)

    def lambda_9662():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9662)
    Sleep(50)

    def lambda_9672():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9672)
    Sleep(50)

    def lambda_9682():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9682)
    Sleep(50)

    def lambda_9692():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9692)
    Sleep(50)

    def lambda_96A2():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_96A2)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0390
    ChrTalk(
        0x101,
        "#00005F#5P秘藏的好地方……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x104,
        "#00302F#11P嘿，是哪里呢？\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x2B,
        (
            "#6P#02809F呵呵……是这栋大楼\x01",
            "视野最好的地方。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_54_8835 end

    def Function_55_975B(): pass

    label("Function_55_975B")

    Sound(160, 0, 100, 0)
    Sleep(500)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x7, 0x10)
    OP_71(0x7, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x7)
    BeginChrThread(0x2B, 3, 0, 56)
    Sleep(900)
    BeginChrThread(0x101, 3, 0, 57)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 58)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 59)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 60)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 61)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 62)
    Sleep(1300)
    Sound(107, 0, 100, 0)
    OP_71(0x7, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x7)
    SetMapObjFlags(0x7, 0x10)
    Return()

    # Function_55_975B end

    def Function_56_97DA(): pass

    label("Function_56_97DA")


    def lambda_97DF():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97DF)

    def lambda_97F9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_97F9)
    WaitChrThread(0xFE, 1)

    def lambda_980E():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_980E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_56_97DA end

    def Function_57_982F(): pass

    label("Function_57_982F")


    def lambda_9834():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9834)

    def lambda_984E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_984E)
    WaitChrThread(0xFE, 1)

    def lambda_9863():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9863)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_57_982F end

    def Function_58_9884(): pass

    label("Function_58_9884")


    def lambda_9889():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9889)

    def lambda_98A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_98A3)
    WaitChrThread(0xFE, 1)

    def lambda_98B8():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_98B8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_58_9884 end

    def Function_59_98D9(): pass

    label("Function_59_98D9")


    def lambda_98DE():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_98DE)

    def lambda_98F8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_98F8)
    WaitChrThread(0xFE, 1)

    def lambda_990D():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_990D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_59_98D9 end

    def Function_60_992E(): pass

    label("Function_60_992E")


    def lambda_9933():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9933)

    def lambda_994D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_994D)
    WaitChrThread(0xFE, 1)

    def lambda_9962():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9962)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_60_992E end

    def Function_61_9983(): pass

    label("Function_61_9983")


    def lambda_9988():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9988)

    def lambda_99A2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_99A2)
    WaitChrThread(0xFE, 1)

    def lambda_99B7():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99B7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_61_9983 end

    def Function_62_99D8(): pass

    label("Function_62_99D8")


    def lambda_99DD():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99DD)

    def lambda_99F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_99F7)
    WaitChrThread(0xFE, 1)

    def lambda_9A0C():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A0C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_62_99D8 end

    def Function_63_9A2D(): pass

    label("Function_63_9A2D")


    def lambda_9A32():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A32)
    WaitChrThread(0xFE, 1)

    def lambda_9A50():
        OP_95(0xFE, 109000, 0, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A50)
    WaitChrThread(0xFE, 1)

    def lambda_9A6E():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A6E)
    WaitChrThread(0xFE, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)

    def lambda_9AA4():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9AA4)
    Sleep(500)

    def lambda_9AC1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9AC1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_63_9A2D end

    def Function_64_9AD2(): pass

    label("Function_64_9AD2")


    def lambda_9AD7():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9AD7)
    WaitChrThread(0xFE, 1)
    Sleep(1000)
    MoveCamera(35, 19, 0, 7000)
    SetCameraDistance(19000, 7000)

    def lambda_9B0C():
        OP_95(0xFE, 109000, -600, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B0C)
    WaitChrThread(0xFE, 1)

    def lambda_9B2A():
        OP_95(0xFE, 111000, -600, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B2A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_64_9AD2 end

    def Function_65_9B44(): pass

    label("Function_65_9B44")


    def lambda_9B49():
        OP_97(0xFE, 0xFFFFF254, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B49)
    Sleep(300)

    def lambda_9B66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9B66)
    WaitChrThread(0xFE, 1)

    def lambda_9B7B():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B7B)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_9B9C():
        OP_97(0xFE, 0x0, 0x0, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9B9C)
    WaitChrThread(0xFE, 1)

    def lambda_9BBA():

        label("loc_9BBA")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_9BBA")

    QueueWorkItem2(0xFE, 2, lambda_9BBA)
    Return()

    # Function_65_9B44 end

    def Function_66_9BC8(): pass

    label("Function_66_9BC8")


    def lambda_9BCD():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9BCD)
    Sleep(300)

    def lambda_9BEA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9BEA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    Sleep(100)

    def lambda_9C0C():
        OP_97(0xFE, 0x0, 0x0, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C0C)
    WaitChrThread(0xFE, 1)

    def lambda_9C2A():

        label("loc_9C2A")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_9C2A")

    QueueWorkItem2(0xFE, 2, lambda_9C2A)
    Return()

    # Function_66_9BC8 end

    def Function_67_9C38(): pass

    label("Function_67_9C38")


    def lambda_9C3D():
        OP_97(0xFE, 0xFFFFEDA4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C3D)
    Sleep(400)

    def lambda_9C5A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9C5A)
    WaitChrThread(0xFE, 1)

    def lambda_9C6F():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C6F)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_9C90():
        OP_97(0xFE, 0x0, 0x0, 0x3F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9C90)
    WaitChrThread(0xFE, 1)

    def lambda_9CAE():

        label("loc_9CAE")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_9CAE")

    QueueWorkItem2(0xFE, 2, lambda_9CAE)
    Return()

    # Function_67_9C38 end

    def Function_68_9CBC(): pass

    label("Function_68_9CBC")


    def lambda_9CC1():
        OP_97(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9CC1)
    Sleep(400)

    def lambda_9CDE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9CDE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x1)
    Sleep(100)

    def lambda_9D00():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D00)
    WaitChrThread(0xFE, 1)

    def lambda_9D1E():

        label("loc_9D1E")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_9D1E")

    QueueWorkItem2(0xFE, 2, lambda_9D1E)
    Return()

    # Function_68_9CBC end

    def Function_69_9D2C(): pass

    label("Function_69_9D2C")


    def lambda_9D31():
        OP_97(0xFE, 0xFFFFE8F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D31)
    Sleep(500)

    def lambda_9D4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9D4E)
    WaitChrThread(0xFE, 1)

    def lambda_9D63():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D63)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_9D84():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9D84)
    WaitChrThread(0xFE, 1)

    def lambda_9DA2():

        label("loc_9DA2")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_9DA2")

    QueueWorkItem2(0xFE, 2, lambda_9DA2)
    Return()

    # Function_69_9D2C end

    def Function_70_9DB0(): pass

    label("Function_70_9DB0")


    def lambda_9DB5():
        OP_97(0xFE, 0xFFFFEAE8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DB5)
    Sleep(500)

    def lambda_9DD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9DD2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x2)
    Sleep(100)

    def lambda_9DF4():
        OP_97(0xFE, 0x0, 0x0, 0x3778, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9DF4)
    WaitChrThread(0xFE, 1)

    def lambda_9E12():

        label("loc_9E12")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_9E12")

    QueueWorkItem2(0xFE, 2, lambda_9E12)
    Return()

    # Function_70_9DB0 end

    def Function_71_9E20(): pass

    label("Function_71_9E20")


    def lambda_9E25():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E25)
    WaitChrThread(0xFE, 1)

    def lambda_9E43():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E43)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_9E20 end

    def Function_72_9E5D(): pass

    label("Function_72_9E5D")


    def lambda_9E62():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E62)
    WaitChrThread(0xFE, 1)

    def lambda_9E80():
        OP_95(0xFE, 100000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9E80)
    Sleep(3200)

    def lambda_9E9D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9E9D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_9E5D end

    def Function_73_9EAE(): pass

    label("Function_73_9EAE")


    def lambda_9EB3():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EB3)
    WaitChrThread(0xFE, 1)

    def lambda_9ED1():
        OP_95(0xFE, 103000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9ED1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_9EAE end

    def Function_74_9EEB(): pass

    label("Function_74_9EEB")


    def lambda_9EF0():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EF0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x0)

    def lambda_9F18():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F18)
    Sleep(2700)

    def lambda_9F35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9F35)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_9EEB end

    def Function_75_9F46(): pass

    label("Function_75_9F46")


    def lambda_9F4B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F4B)
    WaitChrThread(0xFE, 1)

    def lambda_9F69():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F69)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_9F8A():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F8A)
    Sleep(2700)

    def lambda_9FA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9FA7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_75_9F46 end

    def Function_76_9FB8(): pass

    label("Function_76_9FB8")


    def lambda_9FBD():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FBD)
    WaitChrThread(0xFE, 1)
    Sleep(700)

    def lambda_9FDE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FDE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x1)

    def lambda_A006():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A006)
    Sleep(2800)

    def lambda_A023():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A023)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_76_9FB8 end

    def Function_77_A034(): pass

    label("Function_77_A034")


    def lambda_A039():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBFF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A039)
    WaitChrThread(0xFE, 1)

    def lambda_A057():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A057)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_A078():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A078)
    Sleep(2800)

    def lambda_A095():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A095)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_A034 end

    def Function_78_A0A6(): pass

    label("Function_78_A0A6")


    def lambda_A0AB():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0AB)
    WaitChrThread(0xFE, 1)
    Sleep(1100)

    def lambda_A0CC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF510, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0CC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x2)

    def lambda_A0F4():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A0F4)
    Sleep(2900)

    def lambda_A111():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A111)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_78_A0A6 end

    def Function_79_A122(): pass

    label("Function_79_A122")


    def lambda_A127():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A127)
    WaitChrThread(0xFE, 1)
    Sleep(500)

    def lambda_A148():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A148)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_A169():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A169)
    Sleep(2900)

    def lambda_A186():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A186)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_79_A122 end

    def Function_80_A197(): pass

    label("Function_80_A197")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x28)
    SetChrPos(0x101, -3000, 0, -127400, 0)
    SetChrPos(0x102, -1700, 0, -126900, 0)
    SetChrPos(0x103, -4100, 0, -126900, 0)
    SetChrPos(0x104, -5400, 0, -127400, 0)
    SetChrPos(0x109, -2500, 0, -128300, 0)
    SetChrPos(0x105, -4500, 0, -128300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 0, 0, -127700, 0)
    SetChrChipByIndex(0x2F, 0xB)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 5650, -5850, -106000, 270)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 5650, -5850, -108800, 270)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5650, -5850, -111700, 270)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 1800, -5850, -102100, 180)
    SetChrChipByIndex(0x36, 0xF)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 11800, -5850, -104800, 270)
    SetChrChipByIndex(0x34, 0x7)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 5000, -5800, -99450, 180)
    SetMapObjFrame(0xFF, "bs", 0x1, 0x1)
    OP_68(-3000, 300, -126900, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    VolumeBGM(0x46, 0x3E8)
    OP_68(-3000, 1300, -126900, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0393
    ChrTalk(
        0x109,
        "#12P#10101F开始了呢……\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#11P#00003F……是啊。\x02\x03",

            "#00000F话说回来，虽然早就听说\x01",
            "亚里欧斯先生接到了与会邀请，\x01",
            "但没想到连伊安律师都被请来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x103,
        (
            "#00202F#5P而且『大胡子熊律师』\x01",
            "这个名字好像广为人知呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#00104F在国际性会议上，经常需要\x01",
            "达成一致意见或签署协定。\x02\x03",

            "#00100F在那种情况下，就需要对照\x01",
            "现有的国际法与国际惯例法，\x01",
            "来判断协定是否妥当。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        "#5P#00005F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x105,
        (
            "#12P#10302F就是说，那位大胡子熊律师\x01",
            "是为此而请到的顾问吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x104,
        (
            "#6P#00306F会议虽然开始了……\x01",
            "但他们讲的都是一些\x01",
            "很深奥的事情啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(150)

    #C0400
    ChrTalk(
        0x2E,
        (
            "#00603F#11P会议的内容\x01",
            "无需我们关心。\x02\x03",

            "#00600F我们只要集中精力警备，\x01",
            "让这场通商会议平安结束就够了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1500)

    def lambda_A5FF():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A5FF)
    Sleep(50)

    def lambda_A60F():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A60F)
    Sleep(50)

    def lambda_A61F():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A61F)
    Sleep(50)

    def lambda_A62F():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A62F)
    Sleep(50)

    def lambda_A63F():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A63F)
    Sleep(50)

    def lambda_A64F():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A64F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    #C0401
    ChrTalk(
        0x101,
        "#00001F#6P是，我明白。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#5P#00101F那我们这就按照\x01",
            "预定计划行动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x2E,
        (
            "#00604F#11P嗯，你们就去\x01",
            "三十四、三十五、三十六这三个楼层\x01",
            "巡逻一圈吧。\x02\x03",

            "#00602F事先已经把你们的身份\x01",
            "告知给所有相关人员了。\x02\x03",

            "你们可以向各国首脑的随行人员\x01",
            "和受邀而来的媒体记者们\x01",
            "询问情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x109,
        "#6P#10100F明白了！\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x2E,
        (
            "#00603F#11P那我就先回三十四层了。\x02\x03",

            "#00600F……愿女神保佑你们，\x01",
            "如果遇到什么情况，就和我联系。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x2E, 0xDAC, 0xFFFE0430, 0x1F4)
    OP_68(9000, 1300, -130000, 4000)

    def lambda_A819():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_A819)
    WaitChrThread(0x2E, 1)

    def lambda_A837():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_A837)
    Sleep(2000)

    def lambda_A854():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_A854)
    WaitChrThread(0x2E, 1)
    SetChrFlags(0x2E, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(-3000, 1300, -126900, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()

    #C0406
    ChrTalk(
        0x101,
        (
            "#00008F#5P……看来达德利警官\x01",
            "也觉得状况有点不对劲呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x102,
        "#5P#00103F是啊……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x103,
        (
            "#00211F#5P之前明明有那么多可疑的征兆，\x01",
            "如今风平浪静，反而感觉很不自然……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(150)

    #C0409
    ChrTalk(
        0x109,
        (
            "#12P#10101F看来我们必须要\x01",
            "集中精力巡逻呢！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A980():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A980)
    Sleep(50)

    def lambda_A990():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A990)
    Sleep(50)

    def lambda_A9A0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A9A0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)

    #C0410
    ChrTalk(
        0x104,
        "#6P#00304F是啊。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x105,
        "#6P#10300F那就马上开始吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(150)

    #C0412
    ChrTalk(
        0x101,
        (
            "#5P#00001F嗯，一边巡逻，\x01",
            "一边向相关人员询问情况吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x28)
    SetChrPos(0x0, -3000, 0, -128000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 8690, 0, -132450, 270)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -9280, 0, -132230, 90)
    SetScenarioFlags(0x142, 0)
    OP_29(0xA4, 0x1, 0x1)
    OP_32(0xFF, 0xFE, 0x0)
    Sleep(500)
    EventEnd(0x5)
    SetChrFlags(0x2F, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrFlags(0x36, 0x8000)
    SetChrFlags(0x34, 0x8000)
    Return()

    # Function_80_A197 end

    def Function_81_AAC0(): pass

    label("Function_81_AAC0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(73000, 1200, -1000, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 74500, 0, -1000, 270)
    SetChrPos(0x102, 73800, 0, 200, 225)
    SetChrPos(0x103, 73800, 0, -2200, 315)
    SetChrPos(0x104, 72200, 0, 200, 135)
    SetChrPos(0x109, 71500, 0, -1000, 90)
    SetChrPos(0x105, 72200, 0, -2200, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0413
    ChrTalk(
        0x101,
        (
            "#11P#00000F好……\x01",
            "已经巡视过一圈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x109,
        (
            "#6P#10100F目前似乎\x01",
            "并没有什么问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        (
            "#5P#00302F是啊，就保持这个状态，\x01",
            "再四处看一看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        (
            "#00104F嗯……\x02\x03",

            "#00108F……不知会议的情况\x01",
            "怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        (
            "#11P#00006F这个嘛，市长和议长\x01",
            "肯定都在努力呢，但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x103,
        (
            "#12P#00201F主要问题还在于『铁血宰相』\x01",
            "和洛克史密斯总统，是吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x105,
        (
            "#12P#10302F好啦，等到了休息时间，\x01",
            "找个人问一下就是了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_81_AAC0 end

    def Function_82_AD26(): pass

    label("Function_82_AD26")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-55500, 1200, -1500, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, -54000, 0, -1500, 270)
    SetChrPos(0x102, -54700, 0, -300, 225)
    SetChrPos(0x103, -54700, 0, -2700, 315)
    SetChrPos(0x104, -56300, 0, -300, 135)
    SetChrPos(0x109, -57000, 0, -1500, 90)
    SetChrPos(0x105, -56300, 0, -2700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0420
    ChrTalk(
        0x101,
        (
            "#11P#00000F好……\x01",
            "这样就算转过一圈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x109,
        (
            "#6P#10100F目前似乎\x01",
            "并没有什么问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x104,
        (
            "#5P#00302F是啊，就保持这个状态，\x01",
            "再四处看一看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        (
            "#00104F嗯……\x02\x03",

            "#00108F……不知会议的情况\x01",
            "怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x101,
        (
            "#11P#00006F这个嘛，市长和议长\x01",
            "肯定都在努力呢，但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x103,
        (
            "#12P#00201F主要问题还在于『铁血宰相』\x01",
            "和洛克史密斯总统，是吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x105,
        (
            "#12P#10302F好啦，等到了休息时间，\x01",
            "找个人问一下就是了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 2)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_82_AD26 end

    def Function_83_AF8E(): pass

    label("Function_83_AF8E")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x15, 0xFF)
    OP_68(-1790, 1200, 27440, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrFlags(0x29, 0x80)
    SetChrPos(0x101, -1500, 0, 26400, 270)
    SetChrPos(0x102, -1200, 0, 27700, 270)
    SetChrPos(0x103, 100, 0, 26800, 270)
    SetChrPos(0x104, 400, 0, 28100, 270)
    SetChrPos(0x109, -1500, 0, 25100, 315)
    SetChrPos(0x105, 100, 0, 25500, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetBarrier(0x2, 0x0, 0x1)
    OP_0D()

    #C0427
    ChrTalk(
        0x15,
        "#5P等你们很久了。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x15,
        (
            "#5P各位就是克洛斯贝尔警察局·\x01",
            "特别任务支援科的成员吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x101,
        (
            "#11P#00001F……是的，\x01",
            "这里是总统阁下的房间吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x15,
        (
            "#5P正是，总统已经吩咐过了，\x01",
            "各位可以随意入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)

    def lambda_B112():
        OP_95(0xFE, -3200, 0, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_B112)
    WaitChrThread(0x15, 1)
    OP_93(0x15, 0xB4, 0x1F4)

    #C0431
    ChrTalk(
        0x15,
        "#5P请进吧。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        "#11P#00003F那我们就不客气了……\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x102,
        "#11P#00100F打扰了。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x109,
        (
            "#12P#10108F（大陆最大的国家之一，\x01",
            "  卡尔瓦德的首脑……）\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x104,
        (
            "#11P#00306F（终究还是\x01",
            "  有点紧张啊……）\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 84)
    Sleep(700)
    Sound(103, 0, 100, 0)
    BeginChrThread(0x102, 3, 0, 84)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x103, 3, 0, 84)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 84)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("e4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_83_AF8E end

    def Function_84_B268(): pass

    label("Function_84_B268")


    def lambda_B26D():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B26D)
    WaitChrThread(0xFE, 1)

    def lambda_B28B():
        OP_95(0xFE, -5500, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B28B)
    Sleep(600)

    def lambda_B2A8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B2A8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_B268 end

    def Function_85_B2B9(): pass

    label("Function_85_B2B9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2350, 1200, 27000, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17200, 0)
    SetChrPos(0x101, -5500, 0, 27000, 90)
    SetChrPos(0x102, -5500, 0, 27000, 90)
    SetChrPos(0x103, -5500, 0, 27000, 90)
    SetChrPos(0x104, -5500, 0, 27000, 90)
    SetChrPos(0x109, -5500, 0, 27000, 90)
    SetChrPos(0x105, -5500, 0, 27000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x35, -800, 0, 26600, 0)
    SetChrFlags(0x29, 0x80)
    OP_4B(0x15, 0xFF)
    SetChrPos(0x15, -3200, 0, 28500, 180)
    SetBarrier(0x2, 0x0, 0x1)
    Sound(103, 0, 100, 0)
    FadeToBright(1000, 0)
    BeginChrThread(0x104, 3, 0, 89)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 91)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 88)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 90)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 87)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 86)
    WaitChrThread(0x101, 3)

    #C0436
    ChrTalk(
        0x15,
        "#5P各位辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x15,
        (
            "#5P奥斯本宰相的房间\x01",
            "在对面。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B460():

        label("loc_B460")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_B460")

    QueueWorkItem2(0x101, 2, lambda_B460)

    def lambda_B472():

        label("loc_B472")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_B472")

    QueueWorkItem2(0x102, 2, lambda_B472)
    Sleep(50)

    def lambda_B487():

        label("loc_B487")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_B487")

    QueueWorkItem2(0x103, 2, lambda_B487)
    Sleep(50)

    def lambda_B49C():

        label("loc_B49C")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_B49C")

    QueueWorkItem2(0x109, 2, lambda_B49C)
    Sleep(50)

    def lambda_B4B1():

        label("loc_B4B1")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_B4B1")

    QueueWorkItem2(0x105, 2, lambda_B4B1)
    Sleep(50)

    def lambda_B4C6():

        label("loc_B4C6")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_B4C6")

    QueueWorkItem2(0x104, 2, lambda_B4C6)

    #C0438
    ChrTalk(
        0x101,
        "#11P#00011F……啊，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x102,
        "#11P#00103F谢谢您特意告诉我们。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x15,
        "#5P不客气，请慢走。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x15, 3, 0, 84)
    Sleep(1500)
    OP_68(-800, 1200, 26600, 2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_6F(0x79)
    WaitChrThread(0x15, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)

    def lambda_B5F7():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_B5F7)
    Sleep(50)

    def lambda_B607():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_B607)
    Sleep(50)

    def lambda_B617():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B617)
    Sleep(50)

    def lambda_B627():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B627)
    Sleep(50)

    def lambda_B637():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B637)
    Sleep(50)

    def lambda_B647():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B647)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    #C0441
    ChrTalk(
        0x105,
        (
            "#10309F#11P哈哈，态度倒是很和蔼，\x01",
            "但毕竟是大国的首脑啊。\x02\x03",

            "#10302F真是只厉害的老狐狸。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x109,
        (
            "#6P#10106F瓦吉……\x01",
            "不要乱说。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x103,
        (
            "#00206F#11P确实很露骨呢。\x02\x03",

            "#00211F但他的目的好像\x01",
            "并不是威慑我们……\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        (
            "#00108F#5P我想他的用意\x01",
            "只是确立形式而已……\x02\x03",

            "#00103F我们为解决教团事件而作出了贡献，\x01",
            "而共和国的总统授予我们勋章，\x01",
            "这就是他所追求的形式……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x101,
        (
            "#6P#00003F言下之意是──\x01",
            "克洛斯贝尔的事件就是他们自己的事件。\x02\x03",

            "#00001F也就是说，他通过这种形式，\x01",
            "再次强调了自己作为宗主国的领属权……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x104,
        (
            "#00306F#5P喂喂……\x01",
            "特意把我们叫来，就是为了这个吗？\x02\x03",

            "#00301F大国的首脑\x01",
            "果然心计过人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x105,
        (
            "#10304F#11P自治州议会的那些议员与他相比，\x01",
            "显然不在一个层次上呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x109,
        (
            "#12P#10108F……宰相又有什么事情\x01",
            "要和我们说呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        (
            "#6P#00001F……不知道，\x01",
            "总之，先做好心理准备吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4C(0x15, 0xFF)
    SetChrPos(0x0, -1500, 0, 27000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x142, 3)
    OP_29(0xA4, 0x1, 0x3)
    ModifyEventFlags(1, 0, 0x80)
    OP_1B(0x15, 0xFF, 0xFFFF)
    ClearChrFlags(0x29, 0x80)
    EventEnd(0x5)
    Return()

    # Function_85_B2B9 end

    def Function_86_B9A4(): pass

    label("Function_86_B9A4")


    def lambda_B9A9():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9A9)

    def lambda_B9C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B9C3)
    WaitChrThread(0xFE, 1)

    def lambda_B9D8():
        OP_95(0xFE, -1500, 0, 26400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9D8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_86_B9A4 end

    def Function_87_B9F9(): pass

    label("Function_87_B9F9")


    def lambda_B9FE():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B9FE)

    def lambda_BA18():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA18)
    WaitChrThread(0xFE, 1)

    def lambda_BA2D():
        OP_95(0xFE, -1200, 0, 27700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA2D)
    WaitChrThread(0xFE, 1)

    def lambda_BA4B():

        label("loc_BA4B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BA4B")

    QueueWorkItem2(0xFE, 2, lambda_BA4B)
    Return()

    # Function_87_B9F9 end

    def Function_88_BA59(): pass

    label("Function_88_BA59")


    def lambda_BA5E():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA5E)

    def lambda_BA78():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BA78)
    WaitChrThread(0xFE, 1)

    def lambda_BA8D():
        OP_95(0xFE, 100, 0, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BA8D)
    WaitChrThread(0xFE, 1)

    def lambda_BAAB():

        label("loc_BAAB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BAAB")

    QueueWorkItem2(0xFE, 2, lambda_BAAB)
    Return()

    # Function_88_BA59 end

    def Function_89_BAB9(): pass

    label("Function_89_BAB9")


    def lambda_BABE():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BABE)

    def lambda_BAD8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BAD8)
    WaitChrThread(0xFE, 1)

    def lambda_BAED():
        OP_95(0xFE, 400, 0, 28100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BAED)
    WaitChrThread(0xFE, 1)

    def lambda_BB0B():

        label("loc_BB0B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BB0B")

    QueueWorkItem2(0xFE, 2, lambda_BB0B)
    Return()

    # Function_89_BAB9 end

    def Function_90_BB19(): pass

    label("Function_90_BB19")


    def lambda_BB1E():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB1E)

    def lambda_BB38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB38)
    WaitChrThread(0xFE, 1)

    def lambda_BB4D():
        OP_95(0xFE, -1500, 0, 25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB4D)
    WaitChrThread(0xFE, 1)

    def lambda_BB6B():

        label("loc_BB6B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BB6B")

    QueueWorkItem2(0xFE, 2, lambda_BB6B)
    Return()

    # Function_90_BB19 end

    def Function_91_BB79(): pass

    label("Function_91_BB79")


    def lambda_BB7E():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BB7E)

    def lambda_BB98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_BB98)
    WaitChrThread(0xFE, 1)

    def lambda_BBAD():
        OP_95(0xFE, 100, 0, 25500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_BBAD)
    WaitChrThread(0xFE, 1)

    def lambda_BBCB():

        label("loc_BBCB")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_BBCB")

    QueueWorkItem2(0xFE, 2, lambda_BBCB)
    Return()

    # Function_91_BB79 end

    def Function_92_BBD9(): pass

    label("Function_92_BBD9")

    EventBegin(0x0)

    def lambda_BBE0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_BBE0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(111800, 1100, -102500, 2000)
    MoveCamera(45, 15, 0, 2000)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)
    SetChrName("罗伊德")

    #A0450
    AnonymousTalk(
        0xFF,
        (
            "#00001F（那就是宰相的房间……）\x02\x03",

            "#00003F（拜访过宰相之后，\x01",
            "  休息时间差不多也就结束了。）\x02\x03",

            "#00008F（还有没有其它的事情要做呢？）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 109000, 0, -122500, 0)
    SetScenarioFlags(0x142, 4)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_92_BBD9 end

    def Function_93_BCE0(): pass

    label("Function_93_BCE0")

    EventBegin(0x0)
    Fade(500)
    OP_4B(0x16, 0xFF)
    OP_68(110500, 1100, -102500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 109100, 0, -103400, 90)
    SetChrPos(0x102, 108800, 0, -102500, 90)
    SetChrPos(0x103, 107600, 0, -103100, 90)
    SetChrPos(0x104, 107300, 0, -102200, 90)
    SetChrPos(0x109, 109000, 0, -100900, 135)
    SetChrPos(0x105, 108000, 0, -100300, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0451
    ChrTalk(
        0x16,
        "#11P是克洛斯贝尔警察局的特别任务支援科吧？\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x0, 0x1F4)

    def lambda_BDD0():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_BDD0)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0xE1, 0x1F4)

    #C0452
    ChrTalk(
        0x16,
        (
            "#5P宰相阁下在等候你们，\x01",
            "直接进去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#6P#00001F好、好的。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x102,
        "#6P#00104F打扰了。\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x103,
        "#6P#00211F（……态度很高傲呢。）\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x105,
        (
            "#10306F（不愧是帝国军人，\x01",
            "  一副盛气凌人的样子啊。）\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 94)
    Sleep(700)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    BeginChrThread(0x102, 3, 0, 94)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    BeginChrThread(0x103, 3, 0, 94)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 94)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    StopBGM(0xFA0)
    LoadChrToIndex("chr/ch00002.itc", 0x28)
    LoadChrToIndex("chr/ch00102.itc", 0x29)
    LoadChrToIndex("chr/ch00202.itc", 0x2A)
    LoadChrToIndex("chr/ch00302.itc", 0x2B)
    LoadChrToIndex("chr/ch02902.itc", 0x2C)
    LoadChrToIndex("chr/ch03002.itc", 0x2D)
    LoadChrToIndex("chr/ch10900.itc", 0x2E)
    LoadChrToIndex("chr/ch10902.itc", 0x2F)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    OP_68(148000, 1100, 106000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, 146500, 0, 106000, 90)
    SetChrPos(0x102, 146500, 0, 106000, 90)
    SetChrPos(0x103, 146500, 0, 106000, 90)
    SetChrPos(0x104, 146500, 0, 106000, 90)
    SetChrPos(0x109, 146500, 0, 106000, 90)
    SetChrPos(0x105, 146500, 0, 106000, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x2E)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 160900, 0, 110700, 0)
    OP_52(0x2F, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2F, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2F, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(153000, 1100, 106000, 5000)
    SetCameraDistance(17500, 5000)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 3, 0, 95)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 96)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 97)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 98)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 99)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 100)
    WaitChrThread(0x105, 3)
    Sound(104, 0, 100, 0)
    OP_6F(0x79)

    #C0457
    ChrTalk(
        0x101,
        (
            "#6P#00003F#6P打扰了，\x01",
            "奥斯本宰相阁下。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        (
            "#00100F#6P克洛斯贝尔警察局·特别任务支援科，\x01",
            "应邀前来拜访。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0459
    ChrTalk(
        0x2F,
        "#07404F#11P#N……进来吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7583", 0)
    OP_68(159600, 1000, 110400, 2000)
    MoveCamera(43, 17, 0, 2000)
    OP_6F(0x79)
    SetCameraDistance(17000, 40000)
    SetChrPos(0x101, 150500, 0, 107200, 90)
    SetChrPos(0x102, 150400, 0, 108200, 90)
    SetChrPos(0x103, 148900, 0, 107200, 90)
    SetChrPos(0x104, 148800, 0, 108200, 90)
    SetChrPos(0x109, 150000, 0, 106600, 90)
    SetChrPos(0x105, 148800, 0, 106600, 90)

    def lambda_C22E():
        OP_96(0xFE, 0x2673C, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C22E)
    Sleep(300)

    def lambda_C24B():
        OP_96(0xFE, 0x266D8, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C24B)
    Sleep(50)

    def lambda_C268():
        OP_96(0xFE, 0x260FC, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_C268)
    Sleep(100)

    def lambda_C285():
        OP_96(0xFE, 0x26098, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C285)
    Sleep(100)

    def lambda_C2A2():
        OP_96(0xFE, 0x26548, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C2A2)
    Sleep(100)

    def lambda_C2BF():
        OP_96(0xFE, 0x26098, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C2BF)
    WaitChrThread(0x109, 1)

    def lambda_C2DD():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_C2DD)
    WaitChrThread(0x105, 1)

    def lambda_C2EE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_C2EE)
    Sleep(500)

    #C0460
    ChrTalk(
        0x2F,
        (
            "#07400F#11P这景色实在壮观。\x02\x03",

            "没想到人类竟能建造出\x01",
            "可以自这种高度俯瞰\x01",
            "世界的高耸建筑……\x02\x03",

            "#07404F呵呵，这项伟业或许已经达到\x01",
            "过去盛极一时的古代文明的高度了。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        "#6P#00000F……的确。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x103,
        (
            "#6P#00200F您指的是一千两百年前的\x01",
            "古塞姆里亚文明吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x104,
        (
            "#00305F#6P哦，听说那是无论做任何事情\x01",
            "都像魔法一样便利的文明。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x2F,
        (
            "#07400F#11P不过，那似乎并不是\x01",
            "真正意义上的理想世界。\x02\x03",

            "#07404F去年，在利贝尔异变中出现的\x01",
            "那座巨大浮游都市……\x02\x03",

            "据说也是古塞姆里亚时代的产物，\x01",
            "之后被人类亲手封印。\x02\x03",

            "#07401F正是人类无限可能性与愚蠢的象征。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        "#6P#00001F人类的无限可能性与愚蠢……\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#00108F#6P那个……\x01",
            "您好像了解得很详细啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x2F,
        (
            "#07404F#11P呵呵，倒也没有。\x02\x03",

            "#07400F特别是关于克洛斯贝尔的事情，\x01",
            "我并没有像教团的祭司约亚西姆一样，\x01",
            "掌握到万物之真实。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
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
    Sleep(1000)
    OP_82(0x32, 0x0, 0xBB8, 0xC8)

    #C0468
    ChrTalk(
        0x101,
        "#6P#00013F……！\x02",
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x103,
        "#6P#00208F连那些事都……\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x2F,
        (
            "#07404F#11P呵呵，正因为\x01",
            "存在着无数未知之事，\x01",
            "这个世界才会如此有趣。\x02\x03",

            "如果将一切都了解得一清二楚，\x01",
            "游戏也就无聊至极了。\x02\x03",

            "#07400F你难道不这样想吗？\x01",
            "瓦吉·赫米斯菲亚。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x105,
        (
            "#6P#N#10306F……呼，\x01",
            "您连我的名字都知道啊。\x02\x03",

            "#10300F但反过来说，\x01",
            "或许也仅仅知道名字吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0472
    ChrTalk(
        0x2F,
        (
            "#07400F#11P那只是因为我对你\x01",
            "没什么兴趣而已。\x02\x03",

            "#07404F相比之下，倒是『斗神』的继承者\x01",
            "让我更感兴趣呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x104,
        "#00301F#6P……你……\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        (
            "#6P#00006F『帝国军情报局』……\x02\x03",

            "#00001F似乎拥有相当优秀的\x01",
            "情报收集能力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x2F,
        "#07404F#11P呵呵……\x02",
    )

    CloseMessageWindow()
    OP_93(0x2F, 0x10E, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0476
    AnonymousTalk(
        0x2F,
        (
            "我是埃雷波尼亚帝国政府代表\x01",
            "吉利亚斯·奥斯本。\x02\x03",

            "之前听雷克特说起过\x01",
            "不少关于各位的事情。\x02\x03",

            "在剩余的休息时间中，\x01",
            "各位能否陪我谈谈呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(16500, 1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x2)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x2)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x2C)
    SetChrSubChip(0x109, 0x2)
    SetChrChipByIndex(0x105, 0x2D)
    SetChrSubChip(0x105, 0x2)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrChipByIndex(0x2F, 0x2F)
    SetChrSubChip(0x2F, 0x0)
    SetChrPos(0x102, 157600, 50, 107600, 160)
    SetChrPos(0x104, 156200, 50, 107600, 160)
    SetChrPos(0x101, 158600, 50, 104000, 0)
    SetChrPos(0x103, 157650, 50, 104000, 0)
    SetChrPos(0x109, 156700, 50, 104000, 0)
    SetChrPos(0x105, 155750, 50, 104000, 0)
    SetChrPos(0x2F, 159900, 50, 105900, 270)
    ClearChrFlags(0x37, 0x80)
    OP_78(0xF, 0x37)
    ClearChrFlags(0x38, 0x80)
    OP_78(0x10, 0x38)
    OP_49()
    SetChrPos(0x37, 157500, 0, 107700, 0)
    OP_D5(0x37, 0x0, 0x53020, 0x0, 0x0)
    SetChrPos(0x38, 156100, 0, 107700, 0)
    OP_D5(0x38, 0x0, 0x53020, 0x0, 0x0)
    OP_68(158600, 2600, 106100, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    OP_68(158600, 800, 106100, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0477
    ChrTalk(
        0x101,
        (
            "#12P#00003F……那么，宰相阁下。\x02\x03",

            "#00001F您所谓的谈谈，\x01",
            "是指什么话题呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x103,
        (
            "#12P#00211F看样子，大部分的事情\x01",
            "都已在您的掌握之中了。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0479
    ChrTalk(
        0x2F,
        (
            "#07404F#11P别紧张，只是单纯的聊天而已。\x02\x03",

            "#07400F也可以算是\x01",
            "想法调查吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x109,
        "#6P#10105F想法调查……\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x2F,
        (
            "#07403F#11P不错，我就直截了当地发问了。\x02\x03",

            "#07402F……你们认为\x01",
            "克洛斯贝尔还能维持多久？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    SetCameraDistance(15500, 80000)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0482
    ChrTalk(
        0x101,
        "#12P#00013F#4S……！\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x105,
        "#6P#10306F又是这么露骨的问题呢……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x2F, 0x1)
    Sleep(300)

    #C0484
    ChrTalk(
        0x2F,
        (
            "#07400F#5P呵呵，我没有别的意思。\x02\x03",

            "#07403F兴亡盛衰是历史进程中的必然，\x01",
            "永盛不灭的国家是不存在的。\x02\x03",

            "更何况，在如今这个时代，\x01",
            "一切都在导力革命的推动下\x01",
            "加速发展……\x02\x03",

            "#07401F你们觉得这片因缘之地的现状\x01",
            "还能够维持多久？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x102,
        "#00108F#6P……这、这个……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    #C0486
    ChrTalk(
        0x109,
        (
            "#6P#10107F永、永远！\x02\x03",

            "只要自治州的人民\x01",
            "怀有守护它的意志！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    #C0487
    ChrTalk(
        0x101,
        "#11P#00005F诺艾尔……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x2F,
        (
            "#07400F#5P没错，意志永远都是很重要的。\x02\x03",

            "有时甚至可以扭转大局，\x01",
            "改变历史的潮流，\x01",
            "类似的情况并不少见。\x02\x03",

            "#07404F人类并非软弱无力，\x01",
            "我也相信人类所拥有的无限可能性。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0489
    ChrTalk(
        0x109,
        "#6P#10100F也、也就是说……\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x2F,
        (
            "#07400F#5P但是，当两方怀有坚定意志的人\x01",
            "发生冲突时，又会如何？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    #C0491
    ChrTalk(
        0x109,
        "#6P#10111F……！\x02",
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x2F,
        (
            "#07401F#5P答案很简单──弱小的意志\x01",
            "将会被强大的意志吞噬，\x01",
            "使火势更加猛烈。\x02\x03",

            "#07404F当由此而生的业火\x01",
            "在大地各处不断燃起之时……\x02\x03",

            "一切正义与伦理都会在灼热中消融，\x01",
            "世界将被一片火海所笼罩。\x02\x03",

            "#07402F那副情景，\x01",
            "是不是很容易想象呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x103,
        "#12P#00210F#40W……啊啊………\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x109,
        "#6P#10110F#40W……呜……！\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x104,
        "#00311F#6P#30W……………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0496
    ChrTalk(
        0x101,
        (
            "#12P#00003F#30W……的确……\x01",
            "与帝国或共和国相比，\x01",
            "我们或许只是『弱小的意志』……\x02\x03",

            "#00008F但是……弱小的火焰也未必会被\x01",
            "强大的火焰吞噬吧？\x02\x03",

            "#00007F#20W就像曾经击退过帝国\x01",
            "侵略军的利贝尔王国……！\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        "#00102F#6P啊……\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x105,
        "#6P#10304F十二年前的『百日战役』吗……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x2F,
        (
            "#07404F#5P呵呵，正如你所说，\x01",
            "意志的『强度』是很重要的。\x02\x03",

            "利贝尔那看似弱小，实则强韧的意志，\x01",
            "精彩地压倒了帝国那表面强大，\x01",
            "但却如同一盘散沙的零乱意志。\x02\x03",

            "对克洛斯贝尔而言，\x01",
            "这确实是很振奋精神的一课。\x02\x03",

            "#07402F然而，克洛斯贝尔人民\x01",
            "是否具备利贝尔人民\x01",
            "拥有的自豪感与坚强呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        "#12P#00013F……！\x02",
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x102,
        "#00108F#6P…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x2F, 0x0)
    Sleep(300)

    #C0502
    ChrTalk(
        0x2F,
        (
            "#07404F#11P呵呵，休息时间已经结束了，\x01",
            "这次就先聊到这里吧。\x02\x03",

            "#07400F哦，对了，帝国政府\x01",
            "并没有授予你们勋章的打算。\x02\x03",

            "如果随意将勋章授予平民，\x01",
            "恐怕会引起贵族势力的不满呢。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_68(110500, 1100, -102500, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x105, 0x4)
    SetChrPos(0x101, 113000, 0, -102500, 270)
    SetChrPos(0x102, 113000, 0, -102500, 270)
    SetChrPos(0x103, 113000, 0, -102500, 270)
    SetChrPos(0x104, 113000, 0, -102500, 270)
    SetChrPos(0x109, 113000, 0, -102500, 270)
    SetChrPos(0x105, 113000, 0, -102500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x35, 108200, 0, -102800, 0)
    OP_70(0x2, 0x0)
    Sleep(2000)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    BeginChrThread(0x105, 3, 0, 106)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 105)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 104)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 103)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 102)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 101)
    Sleep(1200)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    WaitChrThread(0x101, 3)
    StopBGM(0x1B58)

    #C0503
    ChrTalk(
        0x16,
        "#5P……你们的运气真好啊。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x16,
        (
            "#5P很少能看到阁下\x01",
            "心情那么好的时候。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_D6B9():

        label("loc_D6B9")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_D6B9")

    QueueWorkItem2(0x101, 2, lambda_D6B9)

    def lambda_D6CB():

        label("loc_D6CB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_D6CB")

    QueueWorkItem2(0x102, 2, lambda_D6CB)
    Sleep(50)

    def lambda_D6E0():

        label("loc_D6E0")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_D6E0")

    QueueWorkItem2(0x103, 2, lambda_D6E0)

    def lambda_D6F2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_D6F2)
    Sleep(50)

    def lambda_D702():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_D702)

    def lambda_D70F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_D70F)

    #C0505
    ChrTalk(
        0x101,
        "#12P#00005F咦……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x104,
        "#6P#00301F喂喂……这是开的什么玩笑啊？\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x16,
        (
            "#5P换句话说，\x01",
            "阁下似乎很赏识你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x16,
        (
            "#5P虽然这话的分量不轻，\x01",
            "但你们暂且坦然受之吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x16,
        (
            "#5P以我的身份来说，\x01",
            "本不该对你们说这些呢。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x16, 3, 0, 94)
    Sleep(800)
    Sound(103, 0, 100, 0)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    OP_68(108800, 1100, -102180, 2000)
    MoveCamera(56, 25, 0, 2000)
    SetCameraDistance(16650, 2000)
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
    WaitChrThread(0x16, 3)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)

    def lambda_D8D1():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_D8D1)
    Sleep(50)

    def lambda_D8E1():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_D8E1)
    Sleep(50)

    def lambda_D8F1():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_D8F1)
    Sleep(50)

    def lambda_D901():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D901)
    Sleep(50)

    def lambda_D911():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_D911)
    Sleep(50)

    def lambda_D921():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_D921)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7583", 0)

    #C0510
    ChrTalk(
        0x102,
        "#5P#00106F……真是难以置信。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x104,
        "#6P#00310F竟然有这么可怕的怪物……\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x101,
        (
            "#11P#00006F……是啊，该怎么说呢，\x01",
            "我们和他好像完全不在一个层次上。\x02\x03",

            "#00001F缇欧，你没事吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x103,
        (
            "#6P#00206F是的……还好。\x02\x03",

            "#00208F感觉他散发出了\x01",
            "极其强烈的火焰，\x01",
            "让我有些头晕……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x109,
        (
            "#5P#10106F这也难怪……连我都\x01",
            "仿佛看到了什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x105,
        (
            "#10308F#5P『铁血宰相』……\x01",
            "简直就是个怪物啊。\x02\x03",

            "#10303F似乎一口就能把这个\x01",
            "小小的克洛斯贝尔吞噬。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0516
    ChrTalk(
        0x101,
        (
            "#11P#00003F不过，他应该并不是为了\x01",
            "嘲弄我们而把我们叫去的。\x02\x03",

            "总统也是一样……\x01",
            "他们声称对我们感兴趣，\x01",
            "恐怕并不假。\x02\x03",

            "#00000F既然如此，我们就把这些经历\x01",
            "视为一次难得的学习吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_DBB2():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DBB2)
    Sleep(0)

    def lambda_DBC2():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DBC2)
    Sleep(0)

    def lambda_DBD2():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_DBD2)
    Sleep(0)

    def lambda_DBE2():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_DBE2)
    Sleep(0)

    def lambda_DBF2():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DBF2)
    Sleep(0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0517
    ChrTalk(
        0x105,
        "#10302F#5P呵呵，真会说啊。\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        (
            "#5P#00104F……你这种性格，\x01",
            "别人还真是模仿不来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x104,
        (
            "#6P#00309F是啊……\x01",
            "未免也太乐观了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x109,
        (
            "#5P#10101F不、不过，确实如罗伊德警官所说……\x01",
            "就算垂头丧气也是无济于事的！\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x103,
        (
            "#6P#00202F是啊……\x01",
            "既然得到了教训，就应该活学活用。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#11P#00003F总之，休息时间已经结束了。\x02\x03",

            "#00001F我们这就回达德利警官那里，\x01",
            "向他报告会见结果吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x1C4, 4)
    SetScenarioFlags(0x22, 3)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_93_BCE0 end

    def Function_94_DE63(): pass

    label("Function_94_DE63")


    def lambda_DE68():
        OP_95(0xFE, 111300, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DE68)
    WaitChrThread(0xFE, 1)

    def lambda_DE86():
        OP_95(0xFE, 113000, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DE86)
    Sleep(600)

    def lambda_DEA3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DEA3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_DE63 end

    def Function_95_DEB4(): pass

    label("Function_95_DEB4")


    def lambda_DEB9():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DEB9)

    def lambda_DED3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DED3)
    WaitChrThread(0xFE, 1)

    def lambda_DEE8():
        OP_95(0xFE, 151000, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DEE8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_95_DEB4 end

    def Function_96_DF09(): pass

    label("Function_96_DF09")


    def lambda_DF0E():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF0E)

    def lambda_DF28():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DF28)
    WaitChrThread(0xFE, 1)

    def lambda_DF3D():
        OP_95(0xFE, 151000, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF3D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_96_DF09 end

    def Function_97_DF5E(): pass

    label("Function_97_DF5E")


    def lambda_DF63():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF63)

    def lambda_DF7D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DF7D)
    WaitChrThread(0xFE, 1)

    def lambda_DF92():
        OP_95(0xFE, 150100, 0, 104600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF92)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_97_DF5E end

    def Function_98_DFB3(): pass

    label("Function_98_DFB3")


    def lambda_DFB8():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DFB8)

    def lambda_DFD2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DFD2)
    WaitChrThread(0xFE, 1)

    def lambda_DFE7():
        OP_95(0xFE, 150100, 0, 106900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DFE7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_98_DFB3 end

    def Function_99_E008(): pass

    label("Function_99_E008")


    def lambda_E00D():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E00D)

    def lambda_E027():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E027)
    WaitChrThread(0xFE, 1)

    def lambda_E03C():
        OP_95(0xFE, 149200, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E03C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_99_E008 end

    def Function_100_E05D(): pass

    label("Function_100_E05D")


    def lambda_E062():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E062)

    def lambda_E07C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E07C)
    WaitChrThread(0xFE, 1)

    def lambda_E091():
        OP_95(0xFE, 149200, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E091)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_100_E05D end

    def Function_101_E0B2(): pass

    label("Function_101_E0B2")


    def lambda_E0B7():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E0B7)

    def lambda_E0D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E0D1)
    WaitChrThread(0xFE, 1)

    def lambda_E0E6():
        OP_95(0xFE, 109100, 0, -103400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E0E6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_101_E0B2 end

    def Function_102_E107(): pass

    label("Function_102_E107")


    def lambda_E10C():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E10C)

    def lambda_E126():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E126)
    WaitChrThread(0xFE, 1)

    def lambda_E13B():
        OP_95(0xFE, 109300, 0, -102300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E13B)
    WaitChrThread(0xFE, 1)

    def lambda_E159():

        label("loc_E159")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E159")

    QueueWorkItem2(0xFE, 2, lambda_E159)
    Return()

    # Function_102_E107 end

    def Function_103_E167(): pass

    label("Function_103_E167")


    def lambda_E16C():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E16C)

    def lambda_E186():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E186)
    WaitChrThread(0xFE, 1)

    def lambda_E19B():
        OP_95(0xFE, 107600, 0, -103100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E19B)
    WaitChrThread(0xFE, 1)

    def lambda_E1B9():

        label("loc_E1B9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E1B9")

    QueueWorkItem2(0xFE, 2, lambda_E1B9)
    Return()

    # Function_103_E167 end

    def Function_104_E1C7(): pass

    label("Function_104_E1C7")


    def lambda_E1CC():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1CC)

    def lambda_E1E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E1E6)
    WaitChrThread(0xFE, 1)

    def lambda_E1FB():
        OP_95(0xFE, 107300, 0, -102000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1FB)
    WaitChrThread(0xFE, 1)

    def lambda_E219():

        label("loc_E219")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E219")

    QueueWorkItem2(0xFE, 2, lambda_E219)
    Return()

    # Function_104_E1C7 end

    def Function_105_E227(): pass

    label("Function_105_E227")


    def lambda_E22C():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E22C)

    def lambda_E246():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E246)
    WaitChrThread(0xFE, 1)

    def lambda_E25B():
        OP_95(0xFE, 109000, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E25B)
    WaitChrThread(0xFE, 1)

    def lambda_E279():

        label("loc_E279")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E279")

    QueueWorkItem2(0xFE, 2, lambda_E279)
    Return()

    # Function_105_E227 end

    def Function_106_E287(): pass

    label("Function_106_E287")


    def lambda_E28C():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E28C)

    def lambda_E2A6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E2A6)
    WaitChrThread(0xFE, 1)

    def lambda_E2BB():
        OP_95(0xFE, 108000, 0, -100300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E2BB)
    WaitChrThread(0xFE, 1)

    def lambda_E2D9():

        label("loc_E2D9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_E2D9")

    QueueWorkItem2(0xFE, 2, lambda_E2D9)
    Return()

    # Function_106_E287 end

    def Function_107_E2E7(): pass

    label("Function_107_E2E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x28)
    LoadChrToIndex("apl/ch51258.itc", 0x29)
    SoundLoad(803)
    SetChrPos(0x101, -3000, 0, -127400, 0)
    SetChrPos(0x102, -1700, 0, -126900, 0)
    SetChrPos(0x103, -4100, 0, -126900, 0)
    SetChrPos(0x104, -5400, 0, -127400, 0)
    SetChrPos(0x109, -2500, 0, -128300, 0)
    SetChrPos(0x105, -4500, 0, -128300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 0, 0, -127700, 0)
    SetChrChipByIndex(0x2F, 0xB)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 5650, -5850, -106000, 270)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 5650, -5850, -108800, 270)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5650, -5850, -111700, 270)
    EndChrThread(0x13, 0xFF)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 1800, -5850, -102100, 180)
    SetChrChipByIndex(0x36, 0xF)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 11800, -5850, -104800, 270)
    SetChrChipByIndex(0x34, 0x7)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 5000, -5800, -99450, 180)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetMapObjFrame(0xFF, "bs", 0x1, 0x1)
    OP_68(-3000, 300, -126900, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    VolumeBGM(0x50, 0x3E8)
    OP_68(-3000, 1300, -126900, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0523
    ChrTalk(
        0x109,
        "#12P#10107F……这是……\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x103,
        (
            "#00206F#11P……正如伊安律师\x01",
            "所担心的一样啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x105,
        (
            "#12P#10308F场上局面似乎完全被\x01",
            "铁血宰相和总统控制了呢。\x02\x03",

            "#10301F难道没有反击的突破口吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x102,
        (
            "#00106F#11P……自治州法的确存在着\x01",
            "多方面的根本上的缺陷，这是事实。\x02\x03",

            "#00108F所以无论是外公\x01",
            "还是迪塔叔叔，\x01",
            "都很难发起有效的反驳……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        (
            "#11P#00006F不过，那些根本上的缺陷都是在七十年前，\x01",
            "也就是自治州刚刚成立的时候，\x01",
            "由两大国的强行决定所致。\x02\x03",

            "#00013F他们明知如此，却还发表那种强硬的发言，\x01",
            "实在是让人无法接受……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x104,
        "#5P#00301F哈，也就是所谓的政治流氓吧？\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x2E,
        "#00603F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(300)

    #C0530
    ChrTalk(
        0x2E,
        (
            "#00601F#11P不管怎么说，会议的内容\x01",
            "并不需要我们去操心。\x02\x03",

            "我们只要集中精神，确保本次\x01",
            "会议能够平安结束即可。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1300)

    def lambda_E7B0():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E7B0)
    Sleep(50)

    def lambda_E7C0():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E7C0)
    Sleep(50)

    def lambda_E7D0():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E7D0)
    Sleep(50)

    def lambda_E7E0():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E7E0)
    Sleep(50)

    def lambda_E7F0():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E7F0)
    Sleep(50)

    def lambda_E800():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E800)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    #C0531
    ChrTalk(
        0x101,
        "#00001F#6P……是，那当然。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x102,
        "#5P#00108F那我们就再巡逻一次——\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x2E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_93(0x2E, 0xB4, 0x1F4)
    SetChrFlags(0x2E, 0x20)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2E, 0x2)
    SetChrChipByIndex(0x2E, 0x29)
    SetChrSubChip(0x2E, 0x6)
    Sleep(300)
    SetChrSubChip(0x2E, 0x7)

    #C0533
    ChrTalk(
        0x2E,
        (
            "#00603F#5P我是搜查一科的达德利。\x02\x03",

            "#00605F……艾玛吗？\x01",
            "发生了什么情况——\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0534
    ChrTalk(
        0x2E,
        "#00607F#5P你说什么……！？\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        "#00001F#6P（……怎么了？）\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x102,
        "#5P#00108F（好像有情况呢……）\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x2E, 0x20)
    ClearChrFlags(0x2E, 0x10)
    ClearChrFlags(0x2E, 0x2)
    SetChrChipByIndex(0x2E, 0x28)
    SetChrSubChip(0x2E, 0x0)
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(300)

    #C0537
    ChrTalk(
        0x2E,
        (
            "#00606F#11P据说『赤色星座』和『黑月』\x01",
            "都已从各自的据点出动了。\x02\x03",

            "#00601F而且他们还甩掉了一科的监视。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0538
    ChrTalk(
        0x101,
        "#00005F#6P这……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0539
    ChrTalk(
        0x104,
        "#6P#00307F什么！？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x2E,
        (
            "#00603F#11P不要慌张，\x01",
            "这也在预想范围内。\x02\x03",

            "#00601F如果有什么情况，我会通知你们的，\x01",
            "你们继续执行警备工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x101,
        "#00001F#6P明、明白。\x02",
    )

    CloseMessageWindow()
    OP_92(0x2E, 0xDAC, 0xFFFE0430, 0x1F4)
    SetChrFlags(0x2E, 0x20)
    SetChrFlags(0x2E, 0x10)
    SetChrFlags(0x2E, 0x2)
    SetChrChipByIndex(0x2E, 0x29)
    SetChrSubChip(0x2E, 0x8)
    OP_68(9000, 1300, -130000, 4000)
    BeginChrThread(0x2E, 3, 0, 108)

    def lambda_EBC4():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_EBC4)
    Sleep(500)

    #C0542
    ChrTalk(
        0x2E,
        (
            "#5P#00603F#12A哦，对了。\x02\x03",

            "#20A#00601F已经可以派出\x01",
            "后备警队了……\x02",
        )
    )
    #Auto

    WaitChrThread(0x2E, 1)

    def lambda_EC2A():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_EC2A)
    Sleep(2000)

    def lambda_EC47():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_EC47)
    WaitChrThread(0x2E, 1)
    EndChrThread(0x2E, 0xFF)
    SetChrFlags(0x2E, 0x80)
    OP_6F(0x79)
    Fade(500)
    OP_68(-3000, 1300, -126900, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    OP_0D()
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

    #C0543
    ChrTalk(
        0x104,
        (
            "#6P#00308F可恶……\x01",
            "真的出动了吗……\x02\x03",

            "#00310F他们到底想干什么！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_ED62():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ED62)
    Sleep(50)

    def lambda_ED72():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ED72)
    Sleep(50)

    def lambda_ED82():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ED82)
    Sleep(50)

    def lambda_ED92():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_ED92)
    Sleep(50)

    def lambda_EDA2():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EDA2)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0544
    ChrTalk(
        0x103,
        "#11P#00208F兰迪前辈……\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        (
            "#00006F#11P兰迪，冷静一些。\x02\x03",

            "#00001F就算是『赤色星座』，\x01",
            "恐怕也不会对这里发动袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        (
            "#00108F#11P是啊，大楼正面\x01",
            "有警队驻守……\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x109,
        (
            "#11P#10101F他们该不会是想在这种时候\x01",
            "和对方开战吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x105,
        (
            "#12P#10306F唔……那种可能性\x01",
            "也不太大。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    Sleep(300)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    SetChrName("老人的声音")

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4S您说什么？！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_EF95():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EF95)
    Sleep(50)

    def lambda_EFA5():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EFA5)
    Sleep(50)

    def lambda_EFB5():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EFB5)
    Sleep(50)

    def lambda_EFC5():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EFC5)
    Sleep(50)

    def lambda_EFD5():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EFD5)
    Sleep(50)

    def lambda_EFE5():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EFE5)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0550
    ChrTalk(
        0x101,
        "#11P#00011F刚才是……？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#00112F#11P外、外公……？\x02",
    )

    CloseMessageWindow()
    OP_68(-3000, 300, -126900, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_24(0x323)
    SetScenarioFlags(0x22, 4)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_107_E2E7 end

    def Function_108_F06F(): pass

    label("Function_108_F06F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F08D")
    OP_A1(0x2E, 0x7D0, 0x8, 0x8, 0x9, 0xA, 0x9, 0x8, 0xB, 0xC, 0xB)
    Jump("Function_108_F06F")

    label("loc_F08D")

    Return()

    # Function_108_F06F end

    def Function_109_F08E(): pass

    label("Function_109_F08E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrPos(0x101, -3000, 0, -127400, 0)
    SetChrPos(0x102, -1700, 0, -126900, 0)
    SetChrPos(0x103, -4100, 0, -126900, 0)
    SetChrPos(0x104, -5400, 0, -127400, 0)
    SetChrPos(0x109, -2500, 0, -128300, 0)
    SetChrPos(0x105, -4500, 0, -128300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x2F, 0xB)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 5650, -5850, -106000, 270)
    SetChrChipByIndex(0x2C, 0xD)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x80)
    SetChrFlags(0x2C, 0x8000)
    SetChrPos(0x2C, 5650, -5850, -108800, 270)
    SetChrChipByIndex(0x13, 0xC)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 5650, -5850, -111700, 270)
    EndChrThread(0x13, 0xFF)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, 1800, -5850, -102100, 180)
    SetChrChipByIndex(0x36, 0xF)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 11800, -5850, -104800, 270)
    SetChrChipByIndex(0x34, 0x7)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 5000, -5800, -99450, 180)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetMapObjFrame(0xFF, "bs", 0x1, 0x1)
    OP_68(-3560, 300, -126600, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16110, 0)
    VolumeBGM(0x50, 0x3E8)
    OP_68(-3560, 1300, -126600, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0552
    ChrTalk(
        0x101,
        "#11P#00010F唔……！\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x109,
        "#12P#10106F太、太过分了……\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x103,
        "#00208F#11P真是胡搅蛮缠……\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x104,
        (
            "#11P#00301F……脸皮居然\x01",
            "厚到那种程度。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x102,
        (
            "#00106F#11P……不过，那项提案\x01",
            "也并非毫无根据。\x02\x03",

            "#00108F但是真的很不希望\x01",
            "事情向那个方向发展啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x105,
        (
            "#12P#10308F唔，看来\x01",
            "已经遇到最大难关了……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F3CE():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F3CE)
    Sleep(50)

    def lambda_F3DE():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F3DE)
    Sleep(50)

    def lambda_F3EE():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F3EE)
    Sleep(50)

    def lambda_F3FE():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F3FE)
    Sleep(50)

    def lambda_F40E():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F40E)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x2)
    Sleep(500)

    #C0558
    ChrTalk(
        0x101,
        "#5P#00001F偏偏在这种时候……\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x102,
        "#00101F#11P是达德利警官打来的？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x3)
    Sleep(300)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0560
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00001F您好，我是班宁斯——\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男人的声音")

    #A0561
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是我，赛尔盖。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0562
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F赛尔盖科长？\x01",
            "出什么事了？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0563
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "没时间了，我长话短说。\x02\x03",

            "索妮亚刚刚联系过我。\x02\x03",

            "安置在唐古拉姆门和贝尔加德门附近的\x01",
            "雷达设施遭到了破坏。\x02\x03",

            "那些都是对空雷达，用于探查\x01",
            "侵入自治州领空的可疑飞艇。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0564
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#3S什么……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("赛尔盖的声音")

    #A0565
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "看样子，恐怕是传闻中的\x01",
            "那些恐怖分子干的好事。\x02\x03",

            "我已经把这件事告诉达德利了，\x01",
            "你们也做好准备吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0566
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F明、明白！\x02",
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
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)

    #C0567
    ChrTalk(
        0x102,
        "#00101F#11P怎、怎么了？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x104,
        (
            "#6P#00307F难道叔叔他们\x01",
            "已经行动了！？\x02",
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
    Sound(802, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 500)

    #C0569
    ChrTalk(
        0x101,
        (
            "#11P#00013F不，并不是\x01",
            "那方面的——\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    SetChrName("男性的声音")

    #A0570
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "各位，\x01",
            "请容我打断一下。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_F89C():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F89C)
    Sleep(50)

    def lambda_F8AC():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F8AC)
    Sleep(50)

    def lambda_F8BC():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F8BC)
    Sleep(50)

    def lambda_F8CC():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F8CC)
    Sleep(50)

    def lambda_F8DC():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F8DC)
    Sleep(50)

    def lambda_F8EC():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F8EC)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    OP_68(-3560, 300, -126600, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x22, 5)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_109_F08E end

    def Function_110_F93E(): pass

    label("Function_110_F93E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -3000, 0, -127400, 0)
    SetChrPos(0x102, -1700, 0, -126900, 0)
    SetChrPos(0x103, -4100, 0, -126900, 0)
    SetChrPos(0x104, -5400, 0, -127400, 0)
    SetChrPos(0x109, -2500, 0, -128300, 0)
    SetChrPos(0x105, -4500, 0, -128300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-3560, 300, -126600, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16110, 0)
    OP_68(-3560, 1300, -126600, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0571
    ChrTalk(
        0x102,
        "#11P#00107F啊……\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x105,
        (
            "#12P#10310F这下……\x01",
            "事情可闹大了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0573
    ChrTalk(
        0x103,
        (
            "#5P#00203F……兰花塔的控制权\x01",
            "已被夺取。\x02\x03",

            "#00201F说不定是昨天那个\x01",
            "黑客干的。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0574
    ChrTalk(
        0x101,
        (
            "#11P#00010F啧，我们赶快出发吧！\x02\x03",

            "#00007F总之，尽快下到三十五层，\x01",
            "去确保各位首脑的安全！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_FB11():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_FB11)
    Sleep(50)

    def lambda_FB21():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_FB21)
    Sleep(50)

    def lambda_FB31():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_FB31)
    Sleep(50)

    def lambda_FB41():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_FB41)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    #C0575
    ChrTalk(
        0x109,
        "#12P#10107F明白！\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x104,
        (
            "#6P#00307F既然导力梯不能用了，\x01",
            "我们就只能走疏散楼梯了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -3000, 0, -128000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0xA4, 0x1, 0x4)
    OP_29(0xA4, 0x1, 0x5)
    EventEnd(0x5)
    Return()

    # Function_110_F93E end

    def Function_111_FBEF(): pass

    label("Function_111_FBEF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51235.itc", 0x28)
    SoundLoad(938)
    SoundLoad(145)
    SoundLoad(143)
    OP_68(-55500, 1700, 3700, 0)
    MoveCamera(37, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -55700, 0, 700, 0)
    SetChrPos(0x102, -56700, 0, -300, 0)
    SetChrPos(0x103, -54700, 0, 300, 0)
    SetChrPos(0x104, -54700, 0, -1200, 0)
    SetChrPos(0x109, -55700, 0, -800, 0)
    SetChrPos(0x105, -56700, 0, -1800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x3E, 0x80)
    OP_78(0x13, 0x3E)
    OP_49()
    SetChrPos(0x3E, -55100, 100, 2200, 0)
    OP_D5(0x3E, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFlags(0x13, 0x4)
    FadeToBright(1000, 0)
    OP_68(-55700, 1300, 1700, 2000)
    MoveCamera(53, 19, 0, 2000)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)

    #C0577
    ChrTalk(
        0x109,
        (
            "#12P#10101F刚、刚才都还\x01",
            "能通行呢……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0578
    ChrTalk(
        0x101,
        "#6P#00013F缇欧，能想想办法吗……！？\x02",
    )

    CloseMessageWindow()

    def lambda_FD7E():

        label("loc_FD7E")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_FD7E")

    QueueWorkItem2(0x102, 2, lambda_FD7E)

    def lambda_FD90():

        label("loc_FD90")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_FD90")

    QueueWorkItem2(0x104, 2, lambda_FD90)

    def lambda_FDA2():

        label("loc_FDA2")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_FDA2")

    QueueWorkItem2(0x109, 2, lambda_FDA2)

    def lambda_FDB4():

        label("loc_FDB4")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_FDB4")

    QueueWorkItem2(0x105, 2, lambda_FDB4)

    def lambda_FDC6():

        label("loc_FDC6")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_FDC6")

    QueueWorkItem2(0x101, 2, lambda_FDC6)

    #C0579
    ChrTalk(
        0x103,
        "#11P#00201F……我试试看。\x02",
    )

    CloseMessageWindow()

    def lambda_FDF7():
        OP_95(0xFE, -54700, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_FDF7)
    WaitChrThread(0x103, 1)
    Sound(853, 0, 100, 0)
    Sound(318, 0, 100, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0580
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "缇欧将导力缆线接在了\x01",
            "卷帘门旁边的接口上。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x103, 0x10E, 0x1F4)
    Sleep(150)
    Fade(250)
    Sound(802, 0, 100, 0)
    ClearMapObjFlags(0x13, 0x4)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 113)
    Sound(938, 2, 100, 0)
    SetCameraDistance(17200, 0)
    OP_0D()
    Sleep(1300)

    #C0581
    ChrTalk(
        0x103,
        (
            "#00205F#30W#11P………………………………\x02\x03",

            "#00203F#20W……稍微有点麻烦呢。\x02\x03",

            "#00201F不过，还有点办法……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-55000, 1500, 3700, 0)
    MoveCamera(39, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    SetCameraDistance(17500, 2000)
    Sound(140, 0, 100, 0)
    Sleep(500)
    EndChrThread(0x103, 0x3)
    StopSound(938, 300, 100)
    BeginChrThread(0x43, 1, 0, 114)
    ClearMapObjFlags(0xC, 0x10)
    OP_71(0xC, 0x0, 0x3C, 0x0, 0x0)
    Sleep(500)

    def lambda_FF8B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FF8B)
    Sleep(50)

    def lambda_FF9B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FF9B)
    Sleep(50)

    def lambda_FFAB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FFAB)
    Sleep(50)

    def lambda_FFBB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FFBB)
    Sleep(50)

    def lambda_FFCB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FFCB)
    Sleep(500)

    #C0582
    ChrTalk(
        0x102,
        "#00102F打开了……！\x02",
    )

    CloseMessageWindow()
    OP_79(0xC)

    #C0583
    ChrTalk(
        0x104,
        "#00309F不愧是阿缇！\x02",
    )

    CloseMessageWindow()
    OP_68(-55700, 1300, 1700, 1500)
    MoveCamera(53, 19, 0, 1500)
    SetCameraDistance(17500, 1500)
    Sleep(1250)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetMapObjFlags(0x13, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    OP_6F(0x79)
    TurnDirection(0x103, 0x104, 500)

    #C0584
    ChrTalk(
        0x103,
        (
            "#00206F哪里，只是因为安全等级\x01",
            "设定得比较低而已。\x02\x03",

            "#00208F不过，刚才的解锁操作\x01",
            "已经使其它门的\x01",
            "安全等级强化了。\x02\x03",

            "#00201F想全部打开\x01",
            "是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x105,
        "#12P#N#10306F准备得还真是周到啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0586
    ChrTalk(
        0x101,
        (
            "#12P#00010F唔……\x01",
            "总之先下楼吧！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 112)
    Sleep(650)
    BeginChrThread(0x103, 3, 0, 112)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 112)
    Sleep(400)
    BeginChrThread(0x109, 3, 0, 112)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 112)
    Sleep(400)
    BeginChrThread(0x105, 3, 0, 112)
    OP_68(-55700, 300, 1700, 3000)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_24(0x3AA)
    OP_24(0x91)
    SetScenarioFlags(0x22, 7)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_111_FBEF end

    def Function_112_101CC(): pass

    label("Function_112_101CC")


    def lambda_101D1():
        OP_95(0xFE, -55700, 0, 3300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101D1)
    WaitChrThread(0xFE, 1)

    def lambda_101EF():
        OP_95(0xFE, -55700, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_101EF)
    WaitChrThread(0xFE, 1)

    def lambda_1020D():
        OP_95(0xFE, -52000, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1020D)
    WaitChrThread(0xFE, 1)

    def lambda_1022B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1022B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_112_101CC end

    def Function_113_10245(): pass

    label("Function_113_10245")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1025F")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_113_10245")

    label("loc_1025F")

    Return()

    # Function_113_10245 end

    def Function_114_10260(): pass

    label("Function_114_10260")

    Sound(145, 2, 100, 0)
    Sleep(2000)
    Sound(143, 0, 70, 0)
    OP_24(0x91)
    Return()

    # Function_114_10260 end

    def Function_115_10273(): pass

    label("Function_115_10273")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51616.itc", 0x28)
    LoadChrToIndex("chr/ch27702.itc", 0x29)
    LoadChrToIndex("chr/ch27802.itc", 0x2A)
    SetChrPos(0x0, 3000, 0, 2500, 0)
    SetChrPos(0x1, 3000, 0, 2500, 0)
    SetChrPos(0x2, 3000, 0, 2500, 0)
    SetChrPos(0x3, 3000, 0, 2500, 0)
    SetChrChipByIndex(0x2D, 0xE)
    SetChrSubChip(0x2D, 0x1)
    ClearChrFlags(0x2D, 0x80)
    SetChrFlags(0x2D, 0x8000)
    SetChrPos(0x2D, -128000, 0, 58100, 180)
    SetChrChipByIndex(0x30, 0x29)
    SetChrSubChip(0x30, 0x1)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, -126300, 0, 58100, 180)
    SetChrChipByIndex(0x31, 0x2A)
    SetChrSubChip(0x31, 0x2)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, -128000, 0, 53800, 0)
    SetChrChipByIndex(0x32, 0x1E)
    SetChrSubChip(0x32, 0x2)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrPos(0x32, -126300, 0, 53800, 0)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_FF(0x15, 0x320, 0x320, 0x320)
    SetMapObjFrame(0x15, "01", 0x0, 0x1)
    SetMapObjFrame(0x15, "02", 0x1, 0x1)
    SetMapObjFrame(0x15, "03", 0x0, 0x1)
    SetChrChipByIndex(0x3F, 0x28)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, -3500, 0, 19000, 90)
    SetChrChipByIndex(0x40, 0x28)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    SetChrPos(0x40, -3500, 0, 10900, 90)
    SetChrChipByIndex(0x41, 0x28)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    SetChrPos(0x41, -3500, 0, 27000, 90)
    SetChrChipByIndex(0x42, 0x28)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    SetChrPos(0x42, -1000, 0, 0, 0)

    def lambda_1042A():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x6978, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_1042A)
    OP_68(-1000, 1300, 2000, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    OP_68(-1000, 700, 17000, 7000)
    MoveCamera(39, 21, 0, 7000)
    SetCameraDistance(25500, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-120000, 1500, 56000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(-125000, 1500, 56000, 4000)
    SetCameraDistance(15000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(210, 90, -1, -1)
    SetChrName("迪塔总统")

    #A0587
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从这层意义上说，\x01",
            "我们在女神的面前都是有罪的……\x02\x03",

            "欺瞒与怯懦，\x01",
            "这就是我们的罪名。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetMapObjFrame(0x15, "01", 0x1, 0x1)
    SetMapObjFrame(0x15, "02", 0x0, 0x1)
    SetMapObjFrame(0x15, "03", 0x0, 0x1)
    Sleep(300)
    SetMessageWindowPos(210, 90, -1, -1)
    SetChrName("迪塔总统")

    #A0588
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "为了慰藉那些\x01",
            "牺牲者的灵魂……！\x02\x03",

            "为了回报在数日前的袭击中\x01",
            "遭受伤害的各位！\x02\x03",

            "也为了给我们的孩子们\x01",
            "创造和平、有尊严的未来！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetMapObjFrame(0x15, "01", 0x0, 0x1)
    SetMapObjFrame(0x15, "02", 0x0, 0x1)
    SetMapObjFrame(0x15, "03", 0x1, 0x1)
    Sleep(300)
    SetMessageWindowPos(210, 90, -1, -1)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetChrName("迪塔总统")

    #A0589
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S我们如今必须要\x01",
            "舍弃欺瞒与怯懦，\x01",
            "鼓起勇气，高傲地站起来！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-127000, 1200, 56000, 1500)
    OP_6F(0x79)

    #N0590
    NpcTalk(
        0x30,
        "坎贝尔议员",
        "#5P真、真是乱来……\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x31,
        (
            "#6P但、但是……\x01",
            "听他这么一说，确实……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0592
    ChrTalk(
        0x2D,
        "#5P#02501F（………迪塔…………）\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 5)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_115_10273 end

    def Function_116_10772(): pass

    label("Function_116_10772")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch08702.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11201.itp")
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 157800, 0, 58000, 180)
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    OP_FF(0x14, 0x320, 0x320, 0x320)
    ClearChrFlags(0x3E, 0x80)
    OP_78(0x14, 0x3E)
    OP_49()
    SetChrPos(0x3E, 162000, 500, 56000, 0)
    OP_D5(0x3E, 0x0, 0x15F90, 0x0, 0x0)
    OP_68(161000, 2500, 56000, 0)
    MoveCamera(55, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(12000, 0)
    OP_68(159000, 2100, 56000, 4000)
    MoveCamera(45, 15, 0, 4000)
    SetCameraDistance(14000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(200, 120, -1, -1)
    SetChrName("总统的声音")

    #A0593
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "实际上，亚里欧斯长官\x01",
            "曾是克洛斯贝尔警察局的\x01",
            "一名优秀搜查官。\x02\x03",

            "而且正如大家所知，他在从事游击士\x01",
            "工作的期间，曾解决过多起国际性案件，\x01",
            "立下了赫赫功绩。\x02\x03",

            "这些事实足以\x01",
            "令我们相信，\x01",
            "这个人选绝不会有错。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(158490, 900, 58440, 2000)
    MoveCamera(20, 15, 0, 2000)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0594
    AnonymousTalk(
        0xC,
        (
            "#40W……爸爸……\x01",
            "……………为什么…………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(13500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x23, 5)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_116_10772 end

    def Function_117_10A53(): pass

    label("Function_117_10A53")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch03800.itc", 0x28)
    LoadChrToIndex("apl/ch51717.itc", 0x29)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10500.itp")
    SoundLoad(4071)
    SoundLoad(4072)
    SetChrChipByIndex(0x34, 0x28)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrPos(0x34, 163400, 0, 57000, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 163400, 0, 56000, 90)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_68(163400, -800, 56500, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(163400, 1200, 56500, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0595
    ChrTalk(
        0xC,
        "#6P#11230F蓝色的『壁障』……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x34, 0xC, 400)
    Sleep(150)

    #C0596
    ChrTalk(
        0x34,
        (
            "#10503F……不用担心。\x02\x03",

            "#10502F不会让你受到伤害的，\x01",
            "尽管放心吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xC,
        "#6P#11221F……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x34, 500)
    OP_68(163400, 1100, 56750, 500)
    MoveCamera(41, 19, 0, 500)
    SetCameraDistance(16000, 500)

    def lambda_10BE6():
        OP_96(0xFE, 0x27E48, 0x0, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_10BE6)
    WaitChrThread(0xC, 1)
    Fade(250)
    Sound(812, 0, 100, 0)
    Sound(811, 0, 20, 0)
    SetChrChipByIndex(0x34, 0x29)
    SetChrSubChip(0x34, 0x0)
    SetChrFlags(0x34, 0x10)
    SetChrFlags(0x34, 0x2)
    SetChrFlags(0x34, 0x20)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_0D()
    Sleep(110)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0x34, 0x1)
    Sleep(110)
    SetChrSubChip(0x34, 0x2)
    OP_6F(0x79)
    SetCameraDistance(15500, 20000)

    #C0598
    ChrTalk(
        0xC,
        (
            "#12P#11226F#30W我、我没事的，\x01",
            "倒是爸爸……！\x02\x03",

            "#11227F#30W……为什么……\x01",
            "为什么要这样做……！\x02\x03",

            "#11232F#30W妈妈一定……\x01",
            "……也会很伤心的……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(898, 0, 100, 0)
    SetChrSubChip(0x34, 0x3)
    Sleep(130)
    SetChrSubChip(0x34, 0x4)
    Sleep(130)
    SetChrSubChip(0x34, 0x5)
    Sleep(500)

    #C0599
    ChrTalk(
        0x34,
        (
            "#10504F#5P……是啊。\x02\x03",

            "如果纱绫还在的话……\x01",
            "肯定会一脸不满地教训我。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x34, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x34)
    Sleep(300)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x34, 0x6)
    Sleep(130)
    SetChrSubChip(0x34, 0x7)
    Sleep(130)
    SetChrSubChip(0x34, 0x8)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0600
    AnonymousTalk(
        0x34,
        (
            "#4071V#40W#25A……滴。\x02\x03",

            "#4072V#40W#30A我有一件事想拜托你。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 7)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_117_10A53 end

    def Function_118_10E60(): pass

    label("Function_118_10E60")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06400.itc", 0x28)
    OP_68(-1500, 1100, 0, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18250, 0)
    SetChrPos(0x101, -1000, 0, -100, 90)
    SetChrPos(0x102, -2100, 0, 0, 90)
    SetChrPos(0x103, -2100, 0, -1300, 90)
    SetChrPos(0x104, -2100, 0, 1200, 90)
    SetChrPos(0xF4, -3200, 0, 600, 90)
    SetChrPos(0xF5, -3200, 0, -800, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetCameraDistance(17500, 1500)
    FadeToBright(1000, 0)
    Sleep(500)
    BeginChrThread(0x101, 2, 0, 119)
    Sleep(100)
    BeginChrThread(0x102, 2, 0, 120)
    Sleep(300)
    BeginChrThread(0xF4, 2, 0, 119)
    BeginChrThread(0xF5, 2, 0, 120)
    Sleep(400)
    BeginChrThread(0x103, 2, 0, 120)
    Sleep(200)
    BeginChrThread(0x104, 2, 0, 119)
    OP_0D()
    Sleep(500)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x5A, 0x0)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0xF5, 0x2)
    Sleep(300)

    #C0601
    ChrTalk(
        0x101,
        "#5P#00001F到了……\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x102,
        (
            "#00108F#6P据主任说，这个楼层中\x01",
            "应该有不少人……\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0xF, 0x28)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x40)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -5500, 0, 11000, 90)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x40)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -5500, 0, 11000, 90)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    EndChrThread(0x10, 0xFF)
    SetChrSubChip(0x10, 0x0)

    #N0603
    NpcTalk(
        0xF,
        "略带神经质的声音",
        "#2S你、你们是……！？\x02",
    )

    CloseMessageWindow()
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-2500, 1100, 11000, 2000)

    def lambda_110F4():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_110F4)
    Sleep(50)

    def lambda_11104():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11104)
    Sleep(50)

    def lambda_11114():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11114)
    Sleep(50)

    def lambda_11124():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_11124)
    Sleep(50)

    def lambda_11134():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11134)
    Sleep(50)

    def lambda_11144():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_11144)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    Sound(103, 0, 100, 0)
    BeginChrThread(0xF, 3, 0, 121)
    Sleep(800)
    BeginChrThread(0x10, 3, 0, 122)
    Sleep(2500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0604
    ChrTalk(
        0x101,
        "#00011F副、副局长！？\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x102,
        "#12P#00105F您为何会在这里……\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0606
    ChrTalk(
        0xF,
        "#5P这、这是我要说的话！\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xF,
        (
            "#5P我……\x01",
            "我来向长官质问关于昨晚颁布的\x01",
            "戒严令的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xF,
        (
            "#5P结果却被关\x01",
            "在了这个楼层……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11321")

    #C0609
    ChrTalk(
        0x10A,
        "#12P#N#00606F……原来是这样。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1137D")

    label("loc_11321")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1135C")

    #C0610
    ChrTalk(
        0x109,
        "#12P#N#10106F原来是这样啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1137D")

    label("loc_1135C")


    #C0611
    ChrTalk(
        0x102,
        "#12P#00106F原来是这样啊……\x02",
    )

    CloseMessageWindow()

    label("loc_1137D")


    #C0612
    ChrTalk(
        0x104,
        (
            "#00309F哎呀，该怎么说呢，\x01",
            "真是有点意外啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11400")

    #C0613
    ChrTalk(
        0x105,
        (
            "#12P#N#10402F呵呵，没想到您还有\x01",
            "这种敢于质问上级的气概。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1143A")

    label("loc_11400")


    #C0614
    ChrTalk(
        0x103,
        (
            "#12P#N#00204F真没想到您还有\x01",
            "这种敢于质问上级的气概。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1143A")

    OP_63(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0615
    ChrTalk(
        0xF,
        "#5P这、这叫什么话！？\x02",
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0xF,
        (
            "#5P话说回来，你们应该是被\x01",
            "国防军公开通缉的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xF,
        "#5P跑到这种地方做什么！？\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        "#00006F那个……一言难尽呢。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11532")

    #C0619
    ChrTalk(
        0x103,
        (
            "#12P#N#00205F那边那位是……\x01",
            "ＩＢＣ技术部的成员？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_11566")

    label("loc_11532")


    #C0620
    ChrTalk(
        0x102,
        (
            "#12P#00105F那边那位是……\x01",
            "ＩＢＣ技术部的成员？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11566")


    #C0621
    ChrTalk(
        0x10,
        "#5P是的……我是研究员达比德。\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x10,
        (
            "#5P我昨天接到了玛丽亚贝尔小姐发来的\x01",
            "解散技术部的通知……\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x10,
        (
            "#5P老搭档已经不在了，在我发呆的时候，\x01",
            "就被人带到了这个楼层……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1165C")

    #C0624
    ChrTalk(
        0x106,
        (
            "#12P#N#10708F……看来我们首先\x01",
            "应该互相确认一下情况呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116FD")

    label("loc_1165C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_116B1")

    #C0625
    ChrTalk(
        0x109,
        (
            "#12P#N#10108F那个……看来我们首先\x01",
            "应该互相确认一下情况呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_116FD")

    label("loc_116B1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_116FD")

    #C0626
    ChrTalk(
        0x10A,
        (
            "#12P#N#00603F唔，看来我们首先\x01",
            "应该互相确认一下情况呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116FD")

    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(500)
    OP_68(-122300, 1100, 2650, 0)
    MoveCamera(42, 25, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetChrPos(0x101, -122500, 0, 1500, 0)
    SetChrPos(0x102, -123800, 0, 1200, 45)
    SetChrPos(0x103, -122900, 0, 300, 0)
    SetChrPos(0x104, -124900, 0, 1400, 45)
    SetChrPos(0xF4, -121200, 0, 800, 315)
    SetChrPos(0xF5, -120900, 0, 2000, 315)
    SetChrPos(0xF, -122100, 0, 3800, 180)
    SetChrPos(0x10, -123200, 0, 4000, 180)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -120700, 0, 4200, 225)
    EndChrThread(0xD, 0xFF)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -124000, 0, 4800, 180)
    EndChrThread(0xE, 0xFF)
    SetChrSubChip(0xE, 0x0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7151", "ed7302")
    ReplaceBGM("ed7550", "ed7302")
    SetCameraDistance(17000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)

    #C0627
    ChrTalk(
        0xF,
        "#5P没、没想到事情会变成这样……\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xF,
        (
            "#5P自从独立无效宣言发表以来，\x01",
            "我就觉得风向不对……\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xD,
        "#11P为、为什么会遇到这种事……\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xE,
        (
            "#5P感觉就好像\x01",
            "在做噩梦一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x10,
        (
            "#5P是吗……库雷那家伙\x01",
            "在给罗伯兹主任帮忙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x10,
        (
            "#5P难怪从两三天前开始，\x01",
            "入侵塔内系统的黑客手法\x01",
            "变得更加巧妙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x102,
        (
            "#6P#00103F对了……副局长。\x02\x03",

            "#00101F这个楼层中有没有\x01",
            "总统一派的人员？\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xF,
        "#5P唔、唔唔……\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xF,
        (
            "#5P总统和玛丽亚贝尔小姐自不用说，\x01",
            "国防长官和那些猎兵也都不在这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xF,
        (
            "#5P还有……\x01",
            "你们以前照看的那个小女孩也不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        "#12P#00006F……是吗……\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x102,
        "#6P#00108F到底去了哪个楼层呢……\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x103,
        (
            "#12P#00203F……现在就先耐心等待\x01",
            "主任的联络吧。\x02\x03",

            "#00201F我想他应该正在\x01",
            "加紧调查上层区域。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    #C0640
    ChrTalk(
        0x104,
        (
            "#6P#00303F在这段时间，我们就向这个\x01",
            "楼层的其他人员了解一下情况吧。\x02\x03",

            "#00301F说不定有人\x01",
            "知道些什么。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0641
    ChrTalk(
        0x101,
        (
            "#11P#00006F……是啊，\x01",
            "和所有人谈谈吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11BBF")

    #C0642
    ChrTalk(
        0x10A,
        (
            "#00600F#12P副局长，\x01",
            "这里就交给您了，可以吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C4E")

    label("loc_11BBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C06")

    #C0643
    ChrTalk(
        0x109,
        (
            "#10101F#12P副局长，\x01",
            "这里就交给您了，可以吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11C4E")

    label("loc_11C06")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_11C4E")

    #C0644
    ChrTalk(
        0x105,
        (
            "#10400F#12P副局长先生，\x01",
            "这里就交给您了，没问题吧？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11C4E")


    def lambda_11C53():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11C53)
    Sleep(100)

    def lambda_11C63():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11C63)

    #C0645
    ChrTalk(
        0xF,
        "#5P嗯，交给我吧。\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xF,
        (
            "#5P……那个，你们……\x01",
            "可不要太莽撞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xF,
        (
            "#5P要是在查明真相之前就倒下了，\x01",
            "可就得不偿失啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x101,
        (
            "#12P#00000F……是，\x01",
            "我们会铭记在心的。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    ClearChrFlags(0xF, 0x40)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x40)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, -121320, 0, 5490, 270)
    BeginChrThread(0xD, 0, 0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -123130, 0, 5700, 90)
    BeginChrThread(0xE, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, -128710, 150, 3860, 180)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrSubChip(0xF, 0x0)
    EndChrThread(0xF, 0x0)
    SetChrBattleFlags(0xF, 0x4)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -134450, 0, 3390, 270)
    BeginChrThread(0x10, 0, 0, 0)
    OP_49()
    OP_D7(0x28)
    SetChrPos(0x0, -121800, 0, 1620, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A6, 6)
    OP_29(0xB1, 0x1, 0xD)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_118_10E60 end

    def Function_119_11DE6(): pass

    label("Function_119_11DE6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11E0A")
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    Jump("Function_119_11DE6")

    label("loc_11E0A")

    Return()

    # Function_119_11DE6 end

    def Function_120_11E0B(): pass

    label("Function_120_11E0B")

    Sleep(500)

    label("loc_11E0E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11E32")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    Jump("loc_11E0E")

    label("loc_11E32")

    Return()

    # Function_120_11E0B end

    def Function_121_11E33(): pass

    label("Function_121_11E33")


    def lambda_11E38():
        OP_95(0xFE, -2800, 0, 11100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E38)

    def lambda_11E52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11E52)
    WaitChrThread(0xFE, 1)
    OP_68(-2000, 1000, 2850, 3500)
    MoveCamera(37, 21, 0, 3500)
    SetCameraDistance(18000, 3500)

    def lambda_11E8C():
        OP_95(0xFE, -2500, 0, 4700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E8C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_121_11E33 end

    def Function_122_11EA6(): pass

    label("Function_122_11EA6")


    def lambda_11EAB():
        OP_95(0xFE, -2800, 0, 11000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11EAB)

    def lambda_11EC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_11EC5)
    WaitChrThread(0xFE, 1)

    def lambda_11EDA():
        OP_95(0xFE, -1300, 0, 5300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11EDA)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_122_11EA6 end

    def Function_123_11EF4(): pass

    label("Function_123_11EF4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    LoadChrToIndex("apl/ch51727.itc", 0x29)
    LoadChrToIndex("apl/ch50091.itc", 0x2A)
    LoadChrToIndex("apl/ch50005.itc", 0x2B)
    LoadChrToIndex("apl/ch51726.itc", 0x2C)
    SoundLoad(803)
    SoundLoad(4073)
    SoundLoad(4074)
    SoundLoad(4075)
    SoundLoad(4076)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis336.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis030.itp")
    CreatePortrait(2, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11202.itp")
    OP_68(151770, 1100, 57250, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18550, 0)
    SetChrPos(0x101, 150700, 0, 55450, 90)
    SetChrPos(0x102, 150700, 0, 56550, 90)
    SetChrPos(0x103, 149800, 0, 54900, 90)
    SetChrPos(0x104, 149800, 0, 57100, 90)
    SetChrPos(0xF4, 148900, 0, 55450, 90)
    SetChrPos(0xF5, 148900, 0, 56550, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x40)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 163400, 0, 57000, 90)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x3B, 0x80)
    OP_78(0x11, 0x3B)
    OP_49()
    SetChrPos(0x3B, 158000, 500, 56000, 0)
    OP_D5(0x3B, 0x0, 0x53020, 0x0, 0x0)
    SetMapObjFlags(0x11, 0x1000)
    ClearChrFlags(0x3C, 0x80)
    OP_78(0x12, 0x3C)
    OP_49()
    SetChrPos(0x3C, 158000, 500, 56000, 0)
    OP_D5(0x3C, 0x0, 0x4E20, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x1000)
    StopBGM(0xFA0)
    SetCameraDistance(17800, 1500)
    FadeToBright(1000, 0)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0649
    ChrTalk(
        0x101,
        "#00005F#5P（啊……）\x02",
    )

    CloseMessageWindow()
    OP_68(163680, 1100, 57070, 3000)
    MoveCamera(45, 19, 0, 3000)
    SetCameraDistance(17800, 3000)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)

    #C0650
    ChrTalk(
        0xC,
        (
            "#11228F#30W………………………………\x02\x03",

            "#11226F……琪雅………\x01",
            "………爸爸……为什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x101,
        "#00002F小滴……！\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_12278():

        label("loc_12278")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_12278")

    QueueWorkItem2(0xC, 2, lambda_12278)
    OP_68(163400, 900, 56500, 4000)
    MoveCamera(49, 25, 0, 4000)
    SetCameraDistance(16500, 4000)
    BeginChrThread(0x101, 3, 0, 125)
    Sleep(500)
    BeginChrThread(0x102, 3, 0, 126)
    Sleep(500)
    BeginChrThread(0x104, 3, 0, 128)
    Sleep(500)
    BeginChrThread(0x103, 3, 0, 127)
    BeginChrThread(0xF4, 3, 0, 129)
    Sleep(1000)
    BeginChrThread(0xF5, 3, 0, 130)

    #C0652
    ChrTalk(
        0xC,
        "#11230F啊……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    Sleep(300)

    #C0653
    ChrTalk(
        0x102,
        (
            "#12P#00109F太好了……\x01",
            "你没事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x103,
        (
            "#12P#00202F滴也被带到\x01",
            "兰花塔了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x104,
        (
            "#00304F我还以为那个大叔\x01",
            "会把你安置在其它地方呢……\x02\x03",

            "#00302F总之，你没事就好。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x2C)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x1)
    Sleep(130)
    SetChrSubChip(0xC, 0x0)
    Sleep(130)
    SetChrSubChip(0xC, 0x1)
    Sleep(130)
    SetChrSubChip(0xC, 0x2)
    OP_CB(0x4, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0656
    AnonymousTalk(
        0xC,
        (
            "#30W罗伊德警官，兰迪先生……\x01",
            "……还有艾莉小姐和缇欧小姐……\x02\x03",

            "……是吗……\x01",
            "原来你们的相貌是这样的……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x4, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x4, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x4, 0x3)
    OP_CC(0x0, 0x4, 0x0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0657
    ChrTalk(
        0x101,
        "#00005F小滴，难道……\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x102,
        "#12P#00102F你的眼睛……已经能看见东西了？\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xC,
        (
            "#11226F#5P……是的，\x01",
            "多亏琪雅。\x02\x03",

            "她用不可思议的力量\x01",
            "把我的视神经接上了……\x02\x03",

            "#11231F现在不仅能感觉到光……\x01",
            "连颜色和形状都可以看得很清楚。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12628")

    #C0660
    ChrTalk(
        0x109,
        "#10105F#5P好、好厉害……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12695")

    label("loc_12628")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12665")

    #C0661
    ChrTalk(
        0x10A,
        "#00605F#5P……真是难以置信的力量。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12695")

    label("loc_12665")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12695")

    #C0662
    ChrTalk(
        0x106,
        "#10712F#5P真是难以置信……\x02",
    )

    CloseMessageWindow()

    label("loc_12695")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_126E7")

    #C0663
    ChrTalk(
        0x105,
        (
            "#10408F#5P『零之至宝』的力量\x01",
            "对生命体也能产生影响……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_12750")

    label("loc_126E7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1271E")

    #C0664
    ChrTalk(
        0x106,
        "#10708F#5P简直就是奇迹呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12750")

    label("loc_1271E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12750")

    #C0665
    ChrTalk(
        0x10A,
        "#00606F#5P简直就是奇迹啊……\x02",
    )

    CloseMessageWindow()

    label("loc_12750")


    #C0666
    ChrTalk(
        0x104,
        (
            "#00309F哈哈，不管怎么说，\x01",
            "这是件好事啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#00004F嗯……这全都是\x01",
            "琪雅的功劳啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xC,
        (
            "#11231F#5P是的……真不知该\x01",
            "怎么感谢\x01",
            "琪雅才好……\x02\x03",

            "#11233F#30W……可是……\x01",
            "可是……呜呜呜呜！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0xC, 0x3)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    BeginChrThread(0xC, 2, 0, 124)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0669
    ChrTalk(
        0x102,
        "#12P#00101F小滴……！？\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#00011F怎、怎么了？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xC, 2)
    SetChrSubChip(0xC, 0x9)
    Sleep(130)
    SetChrSubChip(0xC, 0xA)
    Sleep(150)

    #C0671
    ChrTalk(
        0xC,
        (
            "#11227F#5P#30W琪雅虽然在笑，\x01",
            "但看起来好难过……！\x02\x03",

            "她好像一直在强迫自己相信……\x01",
            "相信这一切都是她的职责\x01",
            "和真心的愿望！\x02\x03",

            "#11232F其实她根本就不想\x01",
            "协助迪塔先生他们……！\x02\x03",

            "她明明很想回到\x01",
            "罗伊德警官和大家的身边……！\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x101,
        "#00008F啊……\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x104,
        "#00306F是吗……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xC, 0xB)
    Sleep(130)
    SetChrSubChip(0xC, 0xC)
    Sleep(150)

    #C0674
    ChrTalk(
        0xC,
        (
            "#11233F#5P#30W琪雅为什么\x01",
            "要做那种事……？\x02\x03",

            "而且……\x01",
            "爸爸……为什么要……\x02\x03",

            "#11234F……我……我………\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x103,
        "#12P#00208F……滴……\x02",
    )

    CloseMessageWindow()
    OP_68(163420, 900, 56850, 1200)

    def lambda_12AAA():
        OP_95(0xFE, 162800, 0, 57000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12AAA)
    WaitChrThread(0x102, 1)
    TurnDirection(0x102, 0xC, 500)
    Sound(812, 0, 100, 0)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x2C)
    SetChrSubChip(0x102, 0x11)
    Sleep(100)
    SetChrSubChip(0x102, 0x12)
    Sleep(500)

    #C0676
    ChrTalk(
        0x102,
        (
            "#6P#00104F……谢谢你一直\x01",
            "担心琪雅。\x02\x03",

            "#00108F孤单一人……\x01",
            "肯定很难过吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xC,
        "#11233F#5P#30W呜呜呜……呜呜……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0678
    ChrTalk(
        0x101,
        (
            "#00003F……小滴，\x01",
            "我们来此的目的\x01",
            "正是接回琪雅。\x02\x03",

            "#00001F你知道她和亚里欧斯先生他们\x01",
            "在哪里吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xC,
        (
            "#11233F#5P#30W对不起……\x01",
            "我什么都不知道……\x02\x03",

            "从昨天开始，\x01",
            "我就一直没有见过琪雅……\x02\x03",

            "#11234F另外……爸爸要我\x01",
            "传话给罗伊德警官……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0680
    ChrTalk(
        0x101,
        "#00005F哎……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12CCA")

    #C0681
    ChrTalk(
        0x10A,
        "#00605F#5P马克莱因他……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_12D3F")

    label("loc_12CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12D09")

    #C0682
    ChrTalk(
        0x109,
        "#10105F#5P亚、亚里欧斯先生他……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_12D3F")

    label("loc_12D09")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12D3F")

    #C0683
    ChrTalk(
        0x105,
        "#10405F#5P『风之剑圣』要……！？\x02",
    )

    CloseMessageWindow()

    label("loc_12D3F")

    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0x101, 158200, 0, 57400, 180)
    ClearChrFlags(0x102, 0x20)
    ClearChrFlags(0x102, 0x10)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x102, 158200, 0, 54600, 350)
    SetChrPos(0x103, 155800, 0, 54600, 45)
    SetChrPos(0x104, 156800, 0, 57400, 135)
    SetChrPos(0xF4, 155600, 0, 57400, 135)
    SetChrPos(0xF5, 154700, 0, 55400, 90)
    ClearChrFlags(0xC, 0x20)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0xC, 0x2)
    SetChrChipByIndex(0xC, 0x6)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0xC, 159300, 0, 56400, 270)
    SetChrChipByIndex(0x3D, 0x2A)
    SetChrSubChip(0x3D, 0x1E)
    SetChrFlags(0x3D, 0x8000)
    SetChrPos(0x3D, 158350, 250, 56000, 0)
    SetChrChipByIndex(0x3A, 0x29)
    SetChrSubChip(0x3A, 0x1B)
    SetChrFlags(0x3A, 0x8000)
    SetChrFlags(0x3A, 0x2)
    SetChrFlags(0x3A, 0x10)
    SetChrFlags(0x3A, 0x20)
    SetChrPos(0x3A, 157600, 250, 55800, 0)
    SetChrChipByIndex(0x39, 0x29)
    SetChrSubChip(0x39, 0x1B)
    SetChrFlags(0x39, 0x8000)
    SetChrFlags(0x39, 0x2)
    SetChrFlags(0x39, 0x10)
    SetChrFlags(0x39, 0x20)
    SetChrPos(0x39, 157800, 300, 55800, 0)
    ClearMapObjFlags(0x11, 0x4)
    OP_68(157500, 1100, 56000, 0)
    MoveCamera(39, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(16500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0684
    ChrTalk(
        0x101,
        "#00001F这个包袱是……\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0xC,
        (
            "#11226F#11P……爸爸叫我\x01",
            "交给罗伊德警官的……\x02\x03",

            "#11221F请打开看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x101,
        "#00005F好、好的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    Fade(500)
    SetCameraDistance(16000, 300)
    Sound(898, 0, 100, 0)
    SetMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearChrFlags(0x3D, 0x80)
    ClearChrBattleFlags(0x3D, 0x8000)
    ClearChrFlags(0x39, 0x80)
    ClearChrBattleFlags(0x39, 0x8000)
    ClearChrFlags(0x3A, 0x80)
    ClearChrBattleFlags(0x3A, 0x8000)
    OP_0D()
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_12FDE")
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_12FDE")

    Sleep(1000)

    #C0687
    ChrTalk(
        0x101,
        "#00007F#30W……这是………\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7534", 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(800)

    #A0688
    AnonymousTalk(
        0x103,
        "#00208F#30W盖伊先生用过的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_130D4")

    #A0689
    AnonymousTalk(
        0x10A,
        (
            "#00606F#30W……没错，\x01",
            "正是那家伙用过的旋棍。\x02\x03",

            "#00608F被人从现场带走之后，\x01",
            "就一直下落不明……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_130D4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13140")

    #A0690
    AnonymousTalk(
        0x105,
        (
            "#10405F#30W这是刀痕……？\x02\x03",

            "#10401F……如此说来，\x01",
            "杀害盖伊·班宁斯的人\x01",
            "就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_13213")

    label("loc_13140")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_131AA")

    #A0691
    AnonymousTalk(
        0x109,
        (
            "#10105F#30W这是刀痕……？\x02\x03",

            "#10101F这么说……\x01",
            "杀害罗伊德警官\x01",
            "哥哥的人就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_13213")

    label("loc_131AA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13213")

    #A0692
    AnonymousTalk(
        0x106,
        (
            "#10703F#30W这是……刀痕呢。\x02\x03",

            "#10708F也就是说……\x01",
            "杀害罗伊德警官\x01",
            "哥哥的人就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_13213")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0693
    ChrTalk(
        0x102,
        "#12P#00108F#30W罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x101,
        "#00008F#40W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0695
    ChrTalk(
        0xC,
        (
            "#11233F#11P#40W……对不起……\x01",
            "…………真对不起……\x02\x03",

            "#40W爸爸他……爸爸他做了这么过分的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x101,
        (
            "#00006F小滴，\x01",
            "你并没有负疚的必要啊。\x02\x03",

            "#00008F而且，目前还不能断定\x01",
            "杀害大哥的人\x01",
            "就是亚里欧斯先生……\x02\x03",

            "#00013F恐怕还有一些不为人知的\x01",
            "真相隐藏在水面之下。\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0xC,
        "#11227F#11P#30W哎……\x02",
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x104,
        "#00301F这是什么意思？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_134ED")

    #C0699
    ChrTalk(
        0x101,
        (
            "#00008F从这些刀痕看来，\x01",
            "大哥应该与亚里欧斯先生\x01",
            "进行过很激烈的打斗。\x02\x03",

            "#00003F由刀痕的数量来看……\x01",
            "虽然对手是『风之剑圣』，\x01",
            "但大哥的表现仍然非常神勇。\x02\x03",

            "#00013F……然而………\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x10A,
        (
            "#6P#00603F盖伊的直接死因\x01",
            "却是遭到了来自背后的枪击。\x02\x03",

            "#00601F是这样吧？班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x101,
        "#00001F是的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_135C3")

    label("loc_134ED")


    #C0702
    ChrTalk(
        0x101,
        (
            "#00008F从这些刀痕看来，\x01",
            "大哥应该与亚里欧斯先生\x01",
            "进行过很激烈的打斗。\x02\x03",

            "#00003F由刀痕的数量来看……\x01",
            "虽然对手是『风之剑圣』，\x01",
            "但大哥的表现仍然非常神勇。\x02\x03",

            "#00013F……然而，大哥的直接死因\x01",
            "却是遭到了来自背后的枪击。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_135C3")


    #C0703
    ChrTalk(
        0x103,
        "#6P#00205F啊……\x02",
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x102,
        "#12P#00105F也就是说……\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#00000F小滴，\x01",
            "给我看看那封信吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0xC,
        "#11230F#11P好、好的……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x3D, 0x80)
    SetChrBattleFlags(0x3D, 0x8000)
    SetChrChipByIndex(0x101, 0x2B)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0707
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4073V#40W致罗伊德#1500W。\x01",
            "#40W借此机会，把长久以来\x01",
            "一直未能交给你的物品奉还。\x02\x03",

            "#4074V#40W关于此物，\x01",
            "我并不打算做过多说明。\x02\x03",

            "#4075V#40W另外，出现在市内的魔导兵\x01",
            "是白色神机通过大钟\x01",
            "而操控的。\x02\x03",

            "#4076V#40W只要设法解决白色神机，\x01",
            "应该就可平息一切事态了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xFEC)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    #A0708
    AnonymousTalk(
        0x101,
        "#00008F#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0709
    AnonymousTalk(
        0x102,
        "#00108F#30W……这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0710
    ChrTalk(
        0x104,
        (
            "#00303F……这里提到的白色神机，\x01",
            "是我们当时在影像中看到的那个吗？\x02\x03",

            "#00301F它就像挖起一勺冰激凌一样，\x01",
            "毫不费力地把卡雷利亚要塞剜掉了一大片……\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x103,
        (
            "#6P#00201F不过，它应该已经无法使用\x01",
            "那种令空间消失的力量了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13959")

    #C0712
    ChrTalk(
        0x10A,
        (
            "#6P#00608F话说回来，马克莱因那家伙\x01",
            "到底是怎么想的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139EC")

    label("loc_13959")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_139A5")

    #C0713
    ChrTalk(
        0x106,
        (
            "#6P#10708F说起来，『风之剑圣』\x01",
            "到底是怎么想的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_139EC")

    label("loc_139A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_139EC")

    #C0714
    ChrTalk(
        0x109,
        (
            "#6P#10108F说起来，亚里欧斯先生\x01",
            "到底是怎么想的……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_139EC")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x39, 0x80)
    SetChrBattleFlags(0x39, 0x8000)
    SetChrFlags(0x3A, 0x80)
    SetChrBattleFlags(0x3A, 0x8000)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0715
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '零·破坏者'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('零·破坏者', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_13A8C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13A8C)

    def lambda_13A99():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_13A99)

    def lambda_13AA6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_13AA6)
    OP_68(157850, 1100, 56700, 1000)
    MoveCamera(21, 21, 0, 1000)
    SetCameraDistance(16000, 1000)
    OP_6F(0x79)
    Sleep(150)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x10)
    Sound(263, 0, 70, 0)
    OP_A0(0x101, 2000, 0x8, 0x17)
    Sleep(300)

    #C0716
    ChrTalk(
        0x104,
        "#00302F哦哦……\x02",
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x103,
        "#6P#00202F罗伊德前辈……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B69")

    #C0718
    ChrTalk(
        0x105,
        (
            "#6P#10402F嘿……\x01",
            "简直就像是量身定做的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13BE2")

    label("loc_13B69")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13BAA")

    #C0719
    ChrTalk(
        0x109,
        "#6P#10100F简直就像是量身定做的一样……\x02",
    )

    CloseMessageWindow()
    Jump("loc_13BE2")

    label("loc_13BAA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13BE2")

    #C0720
    ChrTalk(
        0x106,
        "#6P#10702F简直就像是量身定做的……\x02",
    )

    CloseMessageWindow()

    label("loc_13BE2")


    #C0721
    ChrTalk(
        0x101,
        (
            "#00004F是啊……\x01",
            "称手程度简直不可思议。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x10)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    OP_68(157500, 1100, 56000, 1300)
    MoveCamera(39, 21, 0, 1300)
    SetCameraDistance(17500, 1300)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(150)
    OP_6F(0x79)

    #C0722
    ChrTalk(
        0x101,
        (
            "#00004F小滴，\x01",
            "多谢你传话给我们。\x02\x03",

            "#00000F无论是琪雅……\x01",
            "还是亚里欧斯先生。\x02\x03",

            "之后的事情\x01",
            "就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_13CC8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13CC8)
    Sleep(50)

    def lambda_13CD8():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_13CD8)
    Sleep(50)

    def lambda_13CE8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_13CE8)

    def lambda_13CF5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_13CF5)

    #C0723
    ChrTalk(
        0xC,
        (
            "#11226F#11P#30W……好的………\x02\x03",

            "#11228F我觉得爸爸……\x01",
            "一直都在苦恼。\x02\x03",

            "关于妈妈……关于我……\x02\x03",

            "#11233F要考虑的事情实在太多，\x01",
            "使他走上了一条无法回头的路……\x02\x03",

            "#11227F………最后就………呜………\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x101,
        (
            "#00002F别担心──\x01",
            "这个世界上绝不存在\x01",
            "无法回头的路。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x102,
        (
            "#12P#00104F我们以特别任务\x01",
            "支援科的名义发誓。\x02\x03",

            "#00100F一定会把你爸爸带回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x104,
        (
            "#00306F嘿，竟然让这么可爱的\x01",
            "独生女儿伤心哭泣，到时一定\x01",
            "要狠狠揍那个不良大叔一拳。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x103,
        (
            "#6P#00204F……没错。\x02\x03",

            "#00202F就算用绳子硬拖，\x01",
            "也要把他给带回来。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xC,
        (
            "#11231F#11P#30W……呜……\x01",
            "…………嗯………！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    SetChrFlags(0x3D, 0x80)
    SetChrBattleFlags(0x3D, 0x8000)
    SetChrFlags(0x39, 0x80)
    SetChrBattleFlags(0x39, 0x8000)
    OP_68(112000, 1200, -110500, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 112500, 0, -110500, 270)
    SetChrPos(0x102, 112500, 0, -110500, 270)
    SetChrPos(0x103, 112500, 0, -110500, 270)
    SetChrPos(0x104, 112500, 0, -110500, 270)
    SetChrPos(0xF4, 112500, 0, -110500, 270)
    SetChrPos(0xF5, 112500, 0, -110500, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF4, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xF5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x4)
    SetChrPos(0xC, 163500, 0, 57920, 90)
    OP_4C(0xC, 0xFF)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7302", 0)
    FadeToBright(1000, 0)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x1)
    OP_68(109500, 1200, -110500, 5000)
    BeginChrThread(0xF5, 3, 0, 136)
    Sleep(700)
    BeginChrThread(0xF4, 3, 0, 135)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 133)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 134)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 132)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 131)
    WaitChrThread(0x101, 3)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Sound(104, 0, 100, 0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14149")

    #C0729
    ChrTalk(
        0x10A,
        (
            "#6P#00606F带回马克莱因的事情\x01",
            "暂且不谈……\x02\x03",

            "#00601F总统一派的人员\x01",
            "到底去哪里了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14226")

    label("loc_14149")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_141BB")

    #C0730
    ChrTalk(
        0x105,
        (
            "#6P#10406F带回『风之剑圣』的事情\x01",
            "暂且不谈……\x02\x03",

            "#10401F总统一派的人员\x01",
            "到底去什么地方了？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14226")

    label("loc_141BB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14226")

    #C0731
    ChrTalk(
        0x106,
        (
            "#6P#10706F带回『风之剑圣』一事\x01",
            "暂且不谈……\x02\x03",

            "#10708F总统一派的人员\x01",
            "究竟去了什么地方？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14226")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14264")

    #C0732
    ChrTalk(
        0x109,
        (
            "#6P#10108F小琪雅似乎也\x01",
            "不在这里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D9")

    label("loc_14264")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_142A2")

    #C0733
    ChrTalk(
        0x106,
        (
            "#6P#10708F小琪雅似乎也\x01",
            "不在这里……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_142D9")

    label("loc_142A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_142D9")

    #C0734
    ChrTalk(
        0x105,
        (
            "#6P#10408F琪雅似乎也\x01",
            "不在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_142D9")


    #C0735
    ChrTalk(
        0x101,
        "#00006F#11P是啊……\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x102,
        (
            "#5P#00108F……既然让小滴传话给我们，\x01",
            "就说明他们已经不在塔内……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0737
    ChrTalk(
        0x101,
        (
            "#00005F#11P啊……\x01",
            "（打开扬声器吧）\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x2, 0x3)
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("主任的声音")

    #A0738
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，罗伊德！\x02\x03",

            "直达导力梯的安全系统\x01",
            "终于解除了～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0739
    AnonymousTalk(
        0x101,
        "#00002F真的吗！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0740
    AnonymousTalk(
        0x102,
        "#00104F太好了，这样一来……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("主任的声音")

    #A0741
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不过，其它楼层已经\x01",
            "基本没人了。\x02\x03",

            "应该没有人能躲过\x01",
            "我们的搜索。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0742
    AnonymousTalk(
        0x103,
        "#00201F这……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0743
    AnonymousTalk(
        0x104,
        (
            "#00301F喂喂，既然如此，\x01",
            "阿琪他们到底去了哪里……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("主任的声音")

    #A0744
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "只有一个可能……\x02\x03",

            "兰花塔的塔顶上\x01",
            "似乎有人。\x02\x03",

            "那台白色的智能兵器也在那里。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(100)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0745
    AnonymousTalk(
        0x101,
        "#00013F……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14622")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0746
    AnonymousTalk(
        0x109,
        (
            "#10101F……可以乘导力梯\x01",
            "前往塔顶吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_146B3")

    label("loc_14622")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1466D")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0747
    AnonymousTalk(
        0x105,
        (
            "#10401F……可以乘导力梯\x01",
            "前往塔顶吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_146B3")

    label("loc_1466D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_146B3")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0748
    AnonymousTalk(
        0x10A,
        (
            "#00601F……可以乘导力梯\x01",
            "前往塔顶吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_146B3")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("主任的声音")

    #A0749
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，锁定已经解除了，\x01",
            "你们可以直接上去。\x02\x03",

            "如果要去的话，务必多加小心！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0750
    AnonymousTalk(
        0x103,
        "#00203F明白。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0751
    AnonymousTalk(
        0x101,
        "#00000F那我这就挂断了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x2, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0752
    ChrTalk(
        0x102,
        "#5P#00108F是『结社』的博士吗？还是……\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x104,
        (
            "#12P#00301F不知道……\x01",
            "只能上去看看了。\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x103,
        (
            "#6P#00203F附近的直达导力梯\x01",
            "应该已经可以使用了。\x02\x03",

            "#00201F如果有必要，\x01",
            "我们可以先回一层去准备一下。\x02",
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
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0755
    ChrTalk(
        0x101,
        "#11P#00007F好……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0xC, 0x40)
    ClearChrFlags(0xC, 0x8000)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    OP_D7(0x2B)
    OP_D7(0x2C)
    SetChrPos(0x0, 109120, 0, -111930, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A6, 7)
    OP_29(0xB1, 0x1, 0xE)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM(-1, -1)
    ReplaceBGM("ed7151", "ed7352")
    ReplaceBGM("ed7550", "ed7352")
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_123_11EF4 end

    def Function_124_14932(): pass

    label("Function_124_14932")

    SetChrSubChip(0xC, 0x4)
    Sleep(130)
    SetChrSubChip(0xC, 0x5)
    Sleep(130)
    SetChrSubChip(0xC, 0x6)
    Sleep(130)
    SetChrSubChip(0xC, 0x7)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(300)
    SetChrSubChip(0xC, 0x5)
    Sleep(130)
    SetChrSubChip(0xC, 0x6)
    Sleep(130)
    SetChrSubChip(0xC, 0x7)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(500)
    SetChrSubChip(0xC, 0x5)
    Sleep(130)
    SetChrSubChip(0xC, 0x6)
    Sleep(130)
    SetChrSubChip(0xC, 0x7)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Sleep(300)
    SetChrSubChip(0xC, 0x5)
    Sleep(130)
    SetChrSubChip(0xC, 0x6)
    Sleep(130)
    SetChrSubChip(0xC, 0x7)
    Sleep(130)
    SetChrSubChip(0xC, 0x4)
    Return()

    # Function_124_14932 end

    def Function_125_149A7(): pass

    label("Function_125_149A7")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_149BD():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_149BD)
    WaitChrThread(0xFE, 1)

    def lambda_149DB():
        OP_95(0xFE, 163300, 0, 55200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_149DB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_125_149A7 end

    def Function_126_149FC(): pass

    label("Function_126_149FC")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_14A12():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14A12)
    WaitChrThread(0xFE, 1)

    def lambda_14A30():
        OP_95(0xFE, 162000, 0, 54800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14A30)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_126_149FC end

    def Function_127_14A51(): pass

    label("Function_127_14A51")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_14A67():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14A67)
    WaitChrThread(0xFE, 1)

    def lambda_14A85():
        OP_95(0xFE, 162000, 0, 53600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14A85)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_127_14A51 end

    def Function_128_14AA6(): pass

    label("Function_128_14AA6")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_14ABC():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14ABC)
    WaitChrThread(0xFE, 1)

    def lambda_14ADA():
        OP_95(0xFE, 163300, 0, 54000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14ADA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_128_14AA6 end

    def Function_129_14AFB(): pass

    label("Function_129_14AFB")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_14B11():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14B11)
    WaitChrThread(0xFE, 1)

    def lambda_14B2F():
        OP_95(0xFE, 161700, 0, 58130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14B2F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_129_14AFB end

    def Function_130_14B50(): pass

    label("Function_130_14B50")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_14B66():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14B66)
    WaitChrThread(0xFE, 1)

    def lambda_14B84():
        OP_95(0xFE, 163100, 0, 58800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14B84)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_130_14B50 end

    def Function_131_14BA5(): pass

    label("Function_131_14BA5")


    def lambda_14BAA():
        OP_95(0xFE, 110200, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14BAA)

    def lambda_14BC4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14BC4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_14BA5 end

    def Function_132_14BD5(): pass

    label("Function_132_14BD5")


    def lambda_14BDA():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14BDA)

    def lambda_14BF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14BF4)
    WaitChrThread(0xFE, 1)

    def lambda_14C09():
        OP_95(0xFE, 109600, 0, -109200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C09)
    WaitChrThread(0xFE, 1)

    def lambda_14C27():

        label("loc_14C27")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_14C27")

    QueueWorkItem2(0xFE, 2, lambda_14C27)
    Return()

    # Function_132_14BD5 end

    def Function_133_14C35(): pass

    label("Function_133_14C35")


    def lambda_14C3A():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C3A)

    def lambda_14C54():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14C54)
    WaitChrThread(0xFE, 1)

    def lambda_14C69():
        OP_95(0xFE, 108600, 0, -111500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C69)
    WaitChrThread(0xFE, 1)

    def lambda_14C87():

        label("loc_14C87")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_14C87")

    QueueWorkItem2(0xFE, 2, lambda_14C87)
    Return()

    # Function_133_14C35 end

    def Function_134_14C95(): pass

    label("Function_134_14C95")


    def lambda_14C9A():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C9A)

    def lambda_14CB4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14CB4)
    WaitChrThread(0xFE, 1)

    def lambda_14CC9():
        OP_95(0xFE, 109600, 0, -112200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14CC9)
    WaitChrThread(0xFE, 1)

    def lambda_14CE7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14CE7)
    Return()

    # Function_134_14C95 end

    def Function_135_14CF0(): pass

    label("Function_135_14CF0")


    def lambda_14CF5():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14CF5)

    def lambda_14D0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14D0F)
    WaitChrThread(0xFE, 1)

    def lambda_14D24():
        OP_95(0xFE, 108000, 0, -109800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14D24)
    WaitChrThread(0xFE, 1)

    def lambda_14D42():

        label("loc_14D42")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_14D42")

    QueueWorkItem2(0xFE, 2, lambda_14D42)
    Return()

    # Function_135_14CF0 end

    def Function_136_14D50(): pass

    label("Function_136_14D50")


    def lambda_14D55():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14D55)

    def lambda_14D6F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14D6F)
    WaitChrThread(0xFE, 1)

    def lambda_14D84():
        OP_95(0xFE, 107500, 0, -111300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14D84)
    WaitChrThread(0xFE, 1)

    def lambda_14DA2():

        label("loc_14DA2")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_14DA2")

    QueueWorkItem2(0xFE, 2, lambda_14DA2)
    Return()

    # Function_136_14D50 end

    def Function_137_14DB0(): pass

    label("Function_137_14DB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14F77")
    EventBegin(0x0)
    Fade(500)
    OP_68(74590, 1500, -850, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 70580, 0, -490, 90)
    SetChrPos(0x102, 70580, 0, -1690, 90)
    SetChrPos(0x103, 70600, 0, 720, 90)
    SetChrPos(0x104, 69600, 0, -500, 90)
    SetChrPos(0x109, 69570, 0, -2070, 90)
    SetChrPos(0x105, 69670, 0, 740, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0756
    ChrTalk(
        0x101,
        "#00013F果然……\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x102,
        (
            "#00101F三扇卷帘门\x01",
            "都关着呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x103,
        (
            "#00201F大楼已经被对方控制了，\x01",
            "想使用导力梯\x01",
            "恐怕是不可能的。\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x104,
        (
            "#00303F也就是说，\x01",
            "我们就算强行破坏卷帘门\x01",
            "也没有用处啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x109,
        "#10107F是的，我们赶快走疏散楼梯吧！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1C2, 5)
    EventEnd(0x5)
    Jump("loc_14FBA")

    label("loc_14F77")

    EventBegin(0x1)

    #C0761
    ChrTalk(
        0x101,
        (
            "#00007F导力梯无法使用……\x01",
            "走疏散楼梯吧！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    EventEnd(0x4)

    label("loc_14FBA")

    Return()

    # Function_137_14DB0 end

    def Function_138_14FBB(): pass

    label("Function_138_14FBB")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1500F")

    #A0762
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "似乎有人在其它楼层\x01",
            "使用导力梯，\x01",
            "还是不要在这里久等了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_15268")

    label("loc_1500F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15219")
    SetChrName("")

    #A0763
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯前的卷帘门\x01",
            "紧紧关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0764
    ChrTalk(
        0x101,
        (
            "#00000F说起来，在会议期间，\x01",
            "好像只能使用\x01",
            "最前面的导力梯吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x102,
        (
            "#00100F嗯，好像是出于警备上的考虑，\x01",
            "做出了这样安排。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_1516B")

    #C0766
    ChrTalk(
        0x103,
        (
            "#00200F这里似乎和疏散楼梯一样，\x01",
            "也是通过导力网络\x01",
            "进行控制和管理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x101,
        (
            "#00000F嗯，好像是这样。\x02\x03",

            "总之，如果要去其它楼层，\x01",
            "我们就乘坐最前面的导力梯吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15211")

    label("loc_1516B")


    #C0768
    ChrTalk(
        0x103,
        (
            "#00200F顺便一说，锁定开关\x01",
            "似乎是通过导力网络\x01",
            "来控制和管理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x101,
        (
            "#00000F嗯，不愧是兰花塔的\x01",
            "安保系统啊。\x02\x03",

            "总之，如果要去其它楼层，\x01",
            "我们就乘坐最前面的导力梯吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15211")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_15268")

    label("loc_15219")

    SetChrName("")

    #A0770
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力梯前的卷帘门\x01",
            "紧紧关闭着。\x02\x03",

            "在会议期间，\x01",
            "无法使用这部导力梯。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_15268")

    TalkEnd(0xFF)
    Return()

    # Function_138_14FBB end

    def Function_139_1526C(): pass

    label("Function_139_1526C")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15470")
    SetChrName("")

    #A0771
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "疏散楼梯前的卷帘门\x01",
            "紧紧关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0772
    ChrTalk(
        0x101,
        "#00000F这边是通往三十七层吧。\x02",
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x102,
        (
            "#00100F嗯，在会议期间，\x01",
            "上层将会完全封锁呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_153BA")

    #C0774
    ChrTalk(
        0x103,
        (
            "#00200F这里似乎和导力梯一样，\x01",
            "也是通过导力网络\x01",
            "进行控制的。\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x101,
        (
            "#00000F迪塔先生说过，不存在完美无缺的\x01",
            "安全防护系统……\x02\x03",

            "得好好考虑一下，\x01",
            "如果真有什么万一，应该如何应对。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15468")

    label("loc_153BA")


    #C0776
    ChrTalk(
        0x103,
        (
            "#00200F卷帘门的锁定开关\x01",
            "似乎是通过导力网络\x01",
            "进行控制的……\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x101,
        (
            "#00000F迪塔先生说过，不存在完美无缺的\x01",
            "安全防护系统……\x02\x03",

            "得好好考虑一下，\x01",
            "如果真有什么万一，应该如何应对。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15468")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_154C5")

    label("loc_15470")

    SetChrName("")

    #A0778
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "疏散楼梯前的卷帘门\x01",
            "紧紧关闭着。\x02\x03",

            "在会议过程中，\x01",
            "上方楼层是禁止通行的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_154C5")

    TalkEnd(0xFF)
    Return()

    # Function_139_1526C end

    def Function_140_154C9(): pass

    label("Function_140_154C9")

    EventBegin(0x1)

    #C0779
    ChrTalk(
        0x101,
        (
            "#00001F哦，总统应该在\x01",
            "左侧最里面的房间。\x02\x03",

            "去见宰相之前，\x01",
            "还是先去拜访总统吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 4370, 0, -1430, 270)
    EventEnd(0x4)
    Return()

    # Function_140_154C9 end

    SaveToFile()

Try(main)
