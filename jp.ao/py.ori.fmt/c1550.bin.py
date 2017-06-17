from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "受付嬢ランフィ",         # 1
        "受付嬢コリンナ",         # 2
        "警備員ビルス",           # 3
        "警備員ウォング",         # 4
        "シズク",                 # 5
        "モレット主任",           # 6
        "受付嬢リーリエ",         # 7
        "ピエール副局長",         # 8
        "研究員ダビッド",         # 9
        "警官",                   # 10
        "警官",                   # 11
        "クローディア姫",         # 12
        "レクター書記官",         # 13
        "共和国軍将校",           # 14
        "帝国軍将校",             # 15
        "ロックスミス大統領",     # 16
        "ユリア准佐",             # 17
        "ミュラー少佐",           # 18
        "アルバート大公",         # 19
        "公室護衛官",             # 20
        "執事",                   # 21
        "執事",                   # 22
        "メイド",                 # 23
        "メイド",                 # 24
        "メイド",                 # 25
        "メイド",                 # 26
        "メイド",                 # 27
        "メイド",                 # 28
        "メイド",                 # 29
        "市役所職員",             # 30
        "市役所職員",             # 31
        "警官",                   # 32
        "警官",                   # 33
        "王室親衛隊隊士",         # 34
        "ジーク",                 # 35
        "ディーター市長",         # 36
        "オリヴァルト皇子",       # 37
        "マクダエル議長",         # 38
        "ダドリー捜査官",         # 39
        "オズボーン宰相",         # 40
        "議員",                   # 41
        "議員",                   # 42
        "議員",                   # 43
        "キーア",                 # 44
        "アリオス長官",           # 45
        "ダミー",                 # 46
        "イアン弁護士",           # 47
        "椅子",                   # 48
        "椅子",                   # 49
        "トンファー",             # 50
        "トンファー",             # 51
        "トンファーOBJ",          # 52
        "風呂敷",                 # 53
        "手紙",                   # 54
        "ノートパソコン",         # 55
        "国防軍兵士・男",         # 56
        "国防軍兵士・男",         # 57
        "国防軍兵士・男",         # 58
        "国防軍兵士・男",         # 59
        "SE制御",                 # 60
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
        "Function_6_18DE",         # 06, 6
        "Function_7_18FC",         # 07, 7
        "Function_8_1DB1",         # 08, 8
        "Function_9_2073",         # 09, 9
        "Function_10_2245",        # 0A, 10
        "Function_11_2A94",        # 0B, 11
        "Function_12_2B4A",        # 0C, 12
        "Function_13_2EA8",        # 0D, 13
        "Function_14_3336",        # 0E, 14
        "Function_15_34C9",        # 0F, 15
        "Function_16_3754",        # 10, 16
        "Function_17_38AA",        # 11, 17
        "Function_18_3961",        # 12, 18
        "Function_19_4647",        # 13, 19
        "Function_20_46EA",        # 14, 20
        "Function_21_4776",        # 15, 21
        "Function_22_4F4F",        # 16, 22
        "Function_23_51D1",        # 17, 23
        "Function_24_5409",        # 18, 24
        "Function_25_54B9",        # 19, 25
        "Function_26_5575",        # 1A, 26
        "Function_27_56B6",        # 1B, 27
        "Function_28_5926",        # 1C, 28
        "Function_29_5A1B",        # 1D, 29
        "Function_30_5B83",        # 1E, 30
        "Function_31_5D0B",        # 1F, 31
        "Function_32_5E2B",        # 20, 32
        "Function_33_5EB7",        # 21, 33
        "Function_34_5FA5",        # 22, 34
        "Function_35_63E0",        # 23, 35
        "Function_36_64FA",        # 24, 36
        "Function_37_6504",        # 25, 37
        "Function_38_6FD3",        # 26, 38
        "Function_39_6FDD",        # 27, 39
        "Function_40_70D5",        # 28, 40
        "Function_41_723B",        # 29, 41
        "Function_42_72D9",        # 2A, 42
        "Function_43_751D",        # 2B, 43
        "Function_44_766B",        # 2C, 44
        "Function_45_77C4",        # 2D, 45
        "Function_46_7866",        # 2E, 46
        "Function_47_799C",        # 2F, 47
        "Function_48_7ABB",        # 30, 48
        "Function_49_7C03",        # 31, 49
        "Function_50_8144",        # 32, 50
        "Function_51_91D0",        # 33, 51
        "Function_52_9D99",        # 34, 52
        "Function_53_9DA0",        # 35, 53
        "Function_54_9DC9",        # 36, 54
        "Function_55_ADA5",        # 37, 55
        "Function_56_AE24",        # 38, 56
        "Function_57_AE79",        # 39, 57
        "Function_58_AECE",        # 3A, 58
        "Function_59_AF23",        # 3B, 59
        "Function_60_AF78",        # 3C, 60
        "Function_61_AFCD",        # 3D, 61
        "Function_62_B022",        # 3E, 62
        "Function_63_B077",        # 3F, 63
        "Function_64_B11C",        # 40, 64
        "Function_65_B18E",        # 41, 65
        "Function_66_B212",        # 42, 66
        "Function_67_B282",        # 43, 67
        "Function_68_B306",        # 44, 68
        "Function_69_B376",        # 45, 69
        "Function_70_B3FA",        # 46, 70
        "Function_71_B46A",        # 47, 71
        "Function_72_B4A7",        # 48, 72
        "Function_73_B4F8",        # 49, 73
        "Function_74_B535",        # 4A, 74
        "Function_75_B590",        # 4B, 75
        "Function_76_B602",        # 4C, 76
        "Function_77_B67E",        # 4D, 77
        "Function_78_B6F0",        # 4E, 78
        "Function_79_B76C",        # 4F, 79
        "Function_80_B7E1",        # 50, 80
        "Function_81_C1D2",        # 51, 81
        "Function_82_C46A",        # 52, 82
        "Function_83_C702",        # 53, 83
        "Function_84_CA0E",        # 54, 84
        "Function_85_CA5F",        # 55, 85
        "Function_86_D1C0",        # 56, 86
        "Function_87_D215",        # 57, 87
        "Function_88_D275",        # 58, 88
        "Function_89_D2D5",        # 59, 89
        "Function_90_D335",        # 5A, 90
        "Function_91_D395",        # 5B, 91
        "Function_92_D3F5",        # 5C, 92
        "Function_93_D504",        # 5D, 93
        "Function_94_F8ED",        # 5E, 94
        "Function_95_F93E",        # 5F, 95
        "Function_96_F993",        # 60, 96
        "Function_97_F9E8",        # 61, 97
        "Function_98_FA3D",        # 62, 98
        "Function_99_FA92",        # 63, 99
        "Function_100_FAE7",       # 64, 100
        "Function_101_FB3C",       # 65, 101
        "Function_102_FB91",       # 66, 102
        "Function_103_FBF1",       # 67, 103
        "Function_104_FC51",       # 68, 104
        "Function_105_FCB1",       # 69, 105
        "Function_106_FD11",       # 6A, 106
        "Function_107_FD71",       # 6B, 107
        "Function_108_10BBD",      # 6C, 108
        "Function_109_10BDC",      # 6D, 109
        "Function_110_11528",      # 6E, 110
        "Function_111_11813",      # 6F, 111
        "Function_112_11E58",      # 70, 112
        "Function_113_11ED1",      # 71, 113
        "Function_114_11EEC",      # 72, 114
        "Function_115_11EFF",      # 73, 115
        "Function_116_124AD",      # 74, 116
        "Function_117_127D4",      # 75, 117
        "Function_118_12C2B",      # 76, 118
        "Function_119_13D21",      # 77, 119
        "Function_120_13D46",      # 78, 120
        "Function_121_13D6E",      # 79, 121
        "Function_122_13DE1",      # 7A, 122
        "Function_123_13E2F",      # 7B, 123
        "Function_124_16D89",      # 7C, 124
        "Function_125_16DFE",      # 7D, 125
        "Function_126_16E53",      # 7E, 126
        "Function_127_16EA8",      # 7F, 127
        "Function_128_16EFD",      # 80, 128
        "Function_129_16F52",      # 81, 129
        "Function_130_16FA7",      # 82, 130
        "Function_131_16FFC",      # 83, 131
        "Function_132_1702C",      # 84, 132
        "Function_133_1708C",      # 85, 133
        "Function_134_170EC",      # 86, 134
        "Function_135_17147",      # 87, 135
        "Function_136_171A7",      # 88, 136
        "Function_137_17207",      # 89, 137
        "Function_138_1746A",      # 8A, 138
        "Function_139_177A3",      # 8B, 139
        "Function_140_17A38",      # 8C, 140
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
            "皆さん、今日はどうも\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "大統領閣下も\x01",
            "非常に喜んでおいでですよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1860 end

    def Function_6_18DE(): pass

    label("Function_6_18DE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18F5")
    Call(0, 93)
    Return()

    label("loc_18F5")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_6_18DE end

    def Function_7_18FC(): pass

    label("Function_7_18FC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1AAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_191E")
    TalkEnd(0xFE)
    Call(0, 49)
    Return()

    label("loc_191E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A0B")

    #C0003
    ChrTalk(
        0xFE,
        (
            "クロイス容疑者は、\x01",
            "現在の事態が収拾するまでは\x01",
            "こちらで拘束されます。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "彼には多くの罪が\x01",
            "課せられるでしょうが……\x01",
            "私も強くは責められません。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "方法はどうあれ、彼がクロスベルを\x01",
            "守ろうとしたのは事実ですから……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1AA8")

    label("loc_1A0B")


    #C0006
    ChrTalk(
        0xFE,
        (
            "クロイス容疑者には\x01",
            "多くの罪が課せられるでしょうが……\x01",
            "私も強くは責められません。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "方法はどうあれ、彼がクロスベルを\x01",
            "守ろうとしたのは事実ですから……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA8")

    Jump("loc_1DAD")

    label("loc_1AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1B2D")

    #C0008
    ChrTalk(
        0xFE,
        (
            "くそっ、テロリストどもに\x01",
            "ここまでしてやられるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "警備隊さえ動ければ、\x01",
            "何とかできるはずなんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DAD")

    label("loc_1B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_1C67")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BFE")

    #C0010
    ChrTalk(
        0xFE,
        (
            "はあ、ユリア准佐……\x01",
            "あんな人が上司にいれば、\x01",
            "俺の毎日も充実するんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "って、いかんいかん。\x01",
            "一体俺は何を考えているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "まったく、緊張感が\x01",
            "足りていない証拠だな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C62")

    label("loc_1BFE")


    #C0013
    ChrTalk(
        0xFE,
        (
            "まだまだ楽観できる\x01",
            "状況でもないのに俺は何を……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "まったく、緊張感が\x01",
            "足りていない証拠だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C62")

    Jump("loc_1DAD")

    label("loc_1C67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1DAD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D31")

    #C0015
    ChrTalk(
        0xFE,
        (
            "ふう、しかしこの回廊室の\x01",
            "見渡しは、まさに壮観だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "視線を遠くにやると、まるで\x01",
            "空中散歩をしているようだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "って、いかんいかん。\x01",
            "もっと緊張感を持たないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1DAD")

    label("loc_1D31")


    #C0018
    ChrTalk(
        0xFE,
        (
            "ここにいると、ついつい\x01",
            "景色に目を奪われてしまうが……\x01",
            "もっと緊張感を持たないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        "雑念は百害あって一利なし、だ。\x02",
    )

    CloseMessageWindow()

    label("loc_1DAD")

    TalkEnd(0xFE)
    Return()

    # Function_7_18FC end

    def Function_8_1DB1(): pass

    label("Function_8_1DB1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1DFA")

    #C0020
    ChrTalk(
        0xFE,
        "異常はありません！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "引き続き巡回にあたります！\x02",
    )

    CloseMessageWindow()
    Jump("loc_206F")

    label("loc_1DFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1E78")

    #C0022
    ChrTalk(
        0xFE,
        (
            "どうやら今は、エレベーターも\x01",
            "階段も使えないようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "この分断された状況を\x01",
            "早く何とかしなければ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_206F")

    label("loc_1E78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_2013")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F8F")

    #C0024
    ChrTalk(
        0xFE,
        (
            "あの方は、帝国軍の\x01",
            "ミュラー少佐と言いましたか……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "そして、ユリア准佐は\x01",
            "王国軍・王室親衛隊の大隊長……\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "そんな肩書きを持つお２人が\x01",
            "ご一緒とは随分珍しい光景ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "まるで親しいご友人のようですが……\x01",
            "一体どういうご関係なんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_200E")

    label("loc_1F8F")


    #C0028
    ChrTalk(
        0xFE,
        (
            "こうして様子を伺っていると、\x01",
            "まるで親しいご友人のように\x01",
            "見えますが……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "お２人は一体、\x01",
            "どういうご関係なんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_200E")

    Jump("loc_206F")

    label("loc_2013")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_206F")

    #C0030
    ChrTalk(
        0xFE,
        "とうとう本会議が始まりましたね。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "この緊張感……\x01",
            "身も心も引き締まります。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_206F")

    TalkEnd(0xFE)
    Return()

    # Function_8_1DB1 end

    def Function_9_2073(): pass

    label("Function_9_2073")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2088")
    Call(0, 10)
    Jump("loc_2241")

    label("loc_2088")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21BD")

    #C0032
    ChrTalk(
        0x18,
        (
            "#07108Fそういえば先ほど\x01",
            "殿下が階段の方からお戻りに\x01",
            "なられたようだが……\x02\x03",

            "#07103Fふむ、だが今の殿下が\x01",
            "かの者に会って心が乱される\x01",
            "ようなこともあるまい。\x02\x03",

            "……余計な心配は無用だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#00005F（……レクターさんのことを\x01",
            "  言っているのか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x105,
        "#10302F（フフ、まあ色々あるんだろうね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 0)
    Jump("loc_2241")

    label("loc_21BD")


    #C0035
    ChrTalk(
        0x18,
        (
            "#07103F警戒の過程で何か判明したことが\x01",
            "あれば連絡をお願いする。\x02\x03",

            "#07100Fこちらでも、何か分かれば\x01",
            "すぐに対策本部に報せるからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2241")

    TalkEnd(0xFE)
    Return()

    # Function_9_2073 end

    def Function_10_2245(): pass

    label("Function_10_2245")

    OP_4B(0x19, 0xFF)
    OP_4B(0x18, 0xFF)
    TurnDirection(0x19, 0x0, 500)

    #C0036
    ChrTalk(
        0x19,
        "#07300Fふむ、君たちか。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x0, 500)

    #C0037
    ChrTalk(
        0x18,
        "#07100F状況に変わりはなさそうだね？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00003Fええ、とりあえずは。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x102,
        (
            "#00101Fお２人の方に\x01",
            "何か情報は入っていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x18,
        (
            "#07103Fいや、残念ながら\x01",
            "これと言ってない状況だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x19,
        (
            "#07303F……帝国方面でも\x01",
            "手は尽くしているんだがな。\x02\x03",

            "#07301F貴族派といい革新派といい、\x01",
            "どうやら尻尾を掴ませてくれる\x01",
            "気はさらさらないらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#10108Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        (
            "#00306F帝国の２大派閥……\x01",
            "とんでもなく\x01",
            "厄介な相手のようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        (
            "#00103F………………………………\x02\x03",

            "#00108Fあの、オリヴァルト皇子は昨日、\x01",
            "『第３の道』と仰っていましたよね？\x02\x03",

            "ずっと気になっていたんですが……\x02\x03",

            "#00101F宜しければ、少しお話を\x01",
            "聞かせていただけないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        "#00005Fエリィ……\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x19,
        (
            "#07302Fふむ、疑問に思うのも無理はない。\x02\x03",

            "#07304F本来なら俺が安々と\x01",
            "語れることではないのだが……\x01",
            "君たちであれば構わないか。\x02\x03",

            "#07300F一言で言うと――あいつは\x01",
            "《壁》を取り払おうとしているんだ。\x02",
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
        "#00001F《壁》を取り払う……\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x19,
        (
            "#07303F要は、革新派と貴族派の間に存在する\x01",
            "認識の壁のようなものだな。\x02\x03",

            "#07300Fさらに言えば、両者を\x01",
            "融和させようという途方もない道だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#00105F革新派と貴族派を融和……\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、それって\x01",
            "恐ろしく困難というか、\x01",
            "ほとんど理想論なんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x109,
        "#10101Fワ、ワジ君――\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x19,
        (
            "#07302Fフフ……\x01",
            "いや、まったく君の言う通りだ。\x02\x03",

            "#07304Fだが、あいつは\x01",
            "その途方もないやり方で“怪物”と\x01",
            "対決することに決めたようだ。\x02\x03",

            "庶出の皇子の気まぐれだの\x01",
            "趣味人気取りの目立ちたがり屋だの\x01",
            "陰で囁かれることを覚悟の上で。\x02\x03",

            "#07302Fそして俺も、それに\x01",
            "付き合うことを決めている。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        "#00002Fな、なるほど……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x18,
        (
            "#07104Fミュラー少佐……\x01",
            "クローディア殿下も改めて言われたように\x01",
            "リベール王国は皇子たちの味方です。\x02\x03",

            "#07102F直接の介入は不可能ですが……\x01",
            "何かあった際は助力を惜しみません。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x19,
        "#07304Fふむ、つくづく有難いことだな。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x103,
        (
            "#00202Fこれも、\x01",
            "皇子の人徳というヤツですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x19,
        (
            "#07304Fフフ、あいつには\x01",
            "到底似合わん言葉だが\x01",
            "確かにそういうものなのかもな。\x02\x03",

            "#07308Fとにかく、今はこの通商会議を\x01",
            "無事に終わらせること――\x01",
            "それが最大の使命であり目的だ。\x02\x03",

            "#07300F特務支援課の諸君……\x01",
            "君達の活躍にも期待しているぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x0, 0x0)
    OP_93(0x18, 0x0, 0x0)
    OP_4C(0x19, 0xFF)
    OP_4C(0x18, 0xFF)
    SetScenarioFlags(0x1C3, 5)
    Return()

    # Function_10_2245 end

    def Function_11_2A94(): pass

    label("Function_11_2A94")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA9")
    Call(0, 10)
    Jump("loc_2B46")

    label("loc_2AA9")


    #C0058
    ChrTalk(
        0x19,
        (
            "#07303Fとにかく、今はこの通商会議を\x01",
            "無事に終わらせること――\x01",
            "それが最大の使命であり目的だ。\x02\x03",

            "#07300F特務支援課の諸君……\x01",
            "君達の活躍にも期待しているぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B46")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A94 end

    def Function_12_2B4A(): pass

    label("Function_12_2B4A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2BF2")

    #C0059
    ChrTalk(
        0xFE,
        (
            "非常階段より行く事のできる\x01",
            "３０Ｆから下の中枢フロアは、\x01",
            "まだ安全を確保できておりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "行かれるおつもりなら、\x01",
            "どうかご注意をお願いします。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA4")

    label("loc_2BF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_2D11")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA3")

    #C0061
    ChrTalk(
        0xFE,
        (
            "み、皆さん、\x01",
            "大変なことになりましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "とりあえず、我々は持ち場である\x01",
            "このフロアの防衛に努めます。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "お互い気を引き締めて行きましょう！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2D0C")

    label("loc_2CA3")


    #C0064
    ChrTalk(
        0xFE,
        (
            "とりあえず、我々は持ち場である\x01",
            "このフロアの防衛に努めます。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "お互い気を引き締めて行きましょう！\x02",
    )

    CloseMessageWindow()

    label("loc_2D0C")

    Jump("loc_2EA4")

    label("loc_2D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_2DB5")

    #C0066
    ChrTalk(
        0xFE,
        (
            "ふう、やはり何というか\x01",
            "ＶＩＰの皆さんはオーラが\x01",
            "ハンパないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "何度構えていても、\x01",
            "皆さんがここを通られる度に\x01",
            "思わず萎縮してしまいます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EA4")

    label("loc_2DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2EA4")

    #C0068
    ChrTalk(
        0xFE,
        (
            "こちらＶＩＰフロアの右翼は\x01",
            "一番手前が市長と議長のお部屋、\x01",
            "それからオリヴァルト皇子……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "最後に一番奥の角部屋が\x01",
            "オズボーン宰相の\x01",
            "お部屋となっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "ちなみに今は\x01",
            "ルームメイクの時間なので、\x01",
            "中に入っても結構ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EA4")

    TalkEnd(0xFE)
    Return()

    # Function_12_2B4A end

    def Function_13_2EA8(): pass

    label("Function_13_2EA8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_2F54")

    #C0071
    ChrTalk(
        0xFE,
        (
            "とりあえず、左翼にいたスタッフは\x01",
            "この部屋に集めておいたぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "今は本部の指示を待つことしか\x01",
            "できねえのが悔しいが……\x01",
            "とにかく気張っていかないとな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3332")

    label("loc_2F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_3131")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3068")

    #C0073
    ChrTalk(
        0xFE,
        (
            "たった今、クローディア殿下を\x01",
            "お見かけしたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "各国のＶＩＰたちを一日に何度も\x01",
            "それも間近で見られるなんて、\x01",
            "つくづくあり得ねえ状況だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "まあとにかく、今日という日が\x01",
            "一生モンの汚点にならねえように\x01",
            "せいぜい気張っていかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_312C")

    label("loc_3068")


    #C0076
    ChrTalk(
        0xFE,
        (
            "各国のＶＩＰたちを一日に何度も\x01",
            "それも間近で見られるなんて……\x01",
            "こんなの二度とねえって話だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "まあとにかく、今日という日が\x01",
            "一生モンの汚点にならねえように\x01",
            "せいぜい気張っていかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_312C")

    Jump("loc_3332")

    label("loc_3131")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3332")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32BC")

    #C0078
    ChrTalk(
        0xFE,
        (
            "ＶＩＰフロアの左翼は手前から\x01",
            "レミフェリア、リベール、\x01",
            "カルバードの首脳の部屋になってるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "ちなみにＶＩＰフロアの警備は、\x01",
            "各国に配慮する意味で\x01",
            "最低限の人員で回していてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "まあ、国のトップたちを招く以上、\x01",
            "こんな状況でも最低限の機密性は\x01",
            "当然必要だろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "とりあえず休憩の間も首脳たちには\x01",
            "それぞれ護衛も付くから、\x01",
            "安全面は問題ナシって判断なんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3332")

    label("loc_32BC")


    #C0082
    ChrTalk(
        0xFE,
        (
            "あと休憩時間になれば、\x01",
            "この辺りを自由に出入りするは\x01",
            "難しくなるだろうからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        "部屋を確認するなら今の内だぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_3332")

    TalkEnd(0xFE)
    Return()

    # Function_13_2EA8 end

    def Function_14_3336(): pass

    label("Function_14_3336")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3428")

    #C0084
    ChrTalk(
        0xFE,
        (
            "この部屋はレミフェリアの\x01",
            "アルバート大公に使って頂く\x01",
            "ご予定なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "それで、何でも大公は\x01",
            "音楽に造詣が深いそうでして。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "今はマクダエル議長とっておきの\x01",
            "レコードコレクションを\x01",
            "準備させて頂いている所なんです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_34C5")

    label("loc_3428")


    #C0087
    ChrTalk(
        0xFE,
        (
            "マクダエル議長とアルバート大公は\x01",
            "随分仲が宜しいみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "レミフェリアはウルスラ病院の\x01",
            "スポンサーとしてでも有名ですし、\x01",
            "何だか頷けますけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34C5")

    TalkEnd(0xFE)
    Return()

    # Function_14_3336 end

    def Function_15_34C9(): pass

    label("Function_15_34C9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_34DA")
    Jump("loc_3750")

    label("loc_34DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_3644")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D5")

    #C0089
    ChrTalk(
        0xFE,
        (
            "戒厳令から一晩しか経っていませんが、\x01",
            "タワー内の皆さんの疲れは\x01",
            "すでにピークに達しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "何が起こっているかも分かりませんし……\x01",
            "やはりかなりの不安があるみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "早くこの状況が\x01",
            "収束すればいいのですが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_363F")

    label("loc_35D5")


    #C0092
    ChrTalk(
        0xFE,
        (
            "タワー内の皆さんの疲れは\x01",
            "すでにピークに達しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "早くこの状況が\x01",
            "収束すればいいのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_363F")

    Jump("loc_3750")

    label("loc_3644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_3750")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36F5")

    #C0094
    ChrTalk(
        0xFE,
        (
            "ちょろちょろちょろ……\x01",
            "全体が軽く湿る程度に～っと。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        "うん、これで鉢植えは完璧よ。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "あとはもう一度、ホコリが\x01",
            "落ちてないか確認して、と……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3750")

    label("loc_36F5")


    #C0097
    ChrTalk(
        0xFE,
        "鉢植えの方はこれで完璧よ。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "あとはもう一度、ホコリが\x01",
            "落ちてないか確認して、と……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3750")

    TalkEnd(0xFE)
    Return()

    # Function_15_34C9 end

    def Function_16_3754(): pass

    label("Function_16_3754")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3824")

    #C0099
    ChrTalk(
        0xFE,
        (
            "こちらは、アルバート大公閣下の\x01",
            "お部屋となります。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "只今はマクダエル議長が\x01",
            "ご訪問中ですが、皆さんのことは\x01",
            "お通しするよう伺っておりますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "宜しければ、どうぞ入りください。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_38A6")

    label("loc_3824")


    #C0102
    ChrTalk(
        0xFE,
        (
            "只今はマクダエル議長が\x01",
            "ご訪問中ですが、皆さんのことは\x01",
            "お通しするよう伺っております。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xFE,
        "宜しければ、どうぞお入りください。\x02",
    )

    CloseMessageWindow()

    label("loc_38A6")

    TalkEnd(0xFE)
    Return()

    # Function_16_3754 end

    def Function_17_38AA(): pass

    label("Function_17_38AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38BF")
    Call(0, 18)
    Jump("loc_3959")

    label("loc_38BF")


    #C0104
    ChrTalk(
        0xFE,
        (
            "ふむ、やはり会議の後半は\x01",
            "より気の抜けない\x01",
            "状況が待っていそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "特に、２大国からなされる\x01",
            "安全保障に関する提案には\x01",
            "より一層警戒を強めないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3959")

    TalkEnd(0xFE)
    SetChrSubChip(0x1A, 0x2)
    Return()

    # Function_17_38AA end

    def Function_18_3961(): pass

    label("Function_18_3961")

    SetChrSubChip(0x1A, 0x2)
    SetChrSubChip(0x2D, 0x1)

    #C0106
    ChrTalk(
        0x1A,
        (
            "ふう、議論がまとまったとはいえ\x01",
            "流石に２大国の首脳を\x01",
            "相手にするのは疲れますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x2D,
        (
            "#02509Fふふ、ですが大公閣下も\x01",
            "益々ご貫禄を増されましたな。\x02\x03",

            "先代も喜ばれていることでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x1A,
        "……跡目を継いでそろそろ５年。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x1A,
        (
            "最近ようやく国内の体制も\x01",
            "整ってきたとはいえ、\x01",
            "実際、私などまだまだですよ。\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3B39")
    Jump("loc_3B83")

    label("loc_3B39")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B59")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B83")

    label("loc_3B59")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3B79")
    OP_52(0x1A, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3B83")

    label("loc_3B79")

    OP_52(0x1A, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x1A, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B83")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3C3C")
    Jump("loc_3C86")

    label("loc_3C3C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C5C")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C86")

    label("loc_3C5C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3C7C")
    OP_52(0x2D, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3C86")

    label("loc_3C7C")

    OP_52(0x2D, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2D, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3C86")

    OP_52(0x2D, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2D, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2D, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 5)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3E03")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CFB")

    #C0110
    ChrTalk(
        0x1A,
        (
            "ああ、君たちは……\x01",
            "昨日は世話になったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D13")

    label("loc_3CFB")


    #C0111
    ChrTalk(
        0x1A,
        "おや、君たちは……\x02",
    )

    CloseMessageWindow()

    label("loc_3D13")


    #C0112
    ChrTalk(
        0x2D,
        "#02505Fおお、支援課の諸君じゃないか。\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x101,
        "#00000Fどうも、お邪魔しています。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x1A,
        (
            "ふむ、話は聞いたが君たちが\x01",
            "警備に参加してくれるとは有難い。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x1A,
        (
            "以前にはマクダエル議長の危機を\x01",
            "救ったこともあったと聞くし、\x01",
            "心から頼もしく思うよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_41E5")

    label("loc_3E03")


    #C0116
    ChrTalk(
        0x1A,
        "おや、君たちは……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x2D,
        "#02500Fおお、支援課の諸君じゃないか。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x101,
        "#00000Fどうも、お邪魔しています。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x1A,
        "ふむ、君たちが特務支援課か。\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x1A,
        (
            "初めまして、活躍ぶりは\x01",
            "アリオス君から聞いているよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0121
    ChrTalk(
        0x101,
        (
            "#00005Fアリオスさんと\x01",
            "お知り合いなんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x1A,
        (
            "ああ、私は以前から\x01",
            "遊撃士協会と懇意にしていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x1A,
        (
            "特にアリオス君とは\x01",
            "個人的な親交も深いんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#00000Fなるほど……そうなんですか。\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x1A,
        "そしてエリィ君、久しぶりだね。\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x1A,
        (
            "どうやら君も、特務支援課で\x01",
            "目覚しい活躍を見せているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x102,
        (
            "#00104Fいえ……\x01",
            "ですが、ありがとうございます。\x02\x03",

            "#00102F大公閣下もお元気そうで何よりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x109,
        (
            "#10105F（エリィさん……大公閣下と\x01",
            "  お知り合いだったんですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x103,
        (
            "#00203F（ある程度は慣れたつもりでしたが……\x01",
            "  相手が一国の首脳とは恐れ入ります。）\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#00306F（やれやれ、お嬢の交友関係は\x01",
            "  つくづく尋常じゃねえのな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x1A,
        (
            "しかし、評判高い君たちが\x01",
            "警備に参加してくれるとは有難い。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x1A,
        (
            "以前にはマクダエル議長の危機を\x01",
            "救ったこともあったと聞くし、\x01",
            "心から頼もしく思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41E5")


    #C0133
    ChrTalk(
        0x101,
        "#00006Fいえ、そんな恐縮です。\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x2D,
        (
            "#02500Fふむ、私も心強く思うよ。\x02\x03",

            "おかげで、会議の後半も\x01",
            "議論に集中することが出来そうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x102,
        (
            "#00108F会議の後半……\x02\x03",

            "#00101Fお祖父様、やはり\x01",
            "厳しい局面が予想されますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x2D,
        (
            "#02503Fああ、実際前半とは違って\x01",
            "自治州にとって耳の痛い指摘が\x01",
            "次々なされるだろうからね。\x02\x03",

            "まあ、それでも両国の要求は\x01",
            "いつもの事とも言ってしまえるが……\x02\x03",

            "#02501F私がもう１つ懸念なのは\x01",
            "ディーター君のことでね。\x02\x03",

            "自治州議会でも彼は革新的な\x01",
            "アイデアを次々に提案し、\x01",
            "その意気込みも素晴らしいのだが……\x02\x03",

            "いかんせん彼はまだ若い。\x01",
            "その勢いが悪い方向に向かわないか\x01",
            "心配な面もあるのだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x109,
        "#10101Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#00200F確か、イアン先生は\x01",
            "ディーター市長に何か策が\x01",
            "あると仰っていましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x2D,
        (
            "#02503Fああ、私も内容は知らないのだが\x01",
            "その策とやらがポイントに\x01",
            "なってくることは間違いだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x1A,
        (
            "そして、その策が\x01",
            "吉と出るか凶と出るか……\x01",
            "全ては会議の流れ次第ということですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x2D,
        (
            "#02503Fええ、そういうことです。\x02\x03",

            "#02500Fまあ、会議においては市長を\x01",
            "支えるのが議長たる\x01",
            "私の仕事であり絶対命題だ。\x02\x03",

            "とにかく、私は私で\x01",
            "やるべきことを尽くさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#00101Fおじいさま……\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C4, 0)
    ClearChrFlags(0x2D, 0x10)
    ClearChrFlags(0x1A, 0x10)
    Return()

    # Function_18_3961 end

    def Function_19_4647(): pass

    label("Function_19_4647")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_465C")
    Call(0, 18)
    Jump("loc_46E2")

    label("loc_465C")


    #C0143
    ChrTalk(
        0xFE,
        (
            "#02500F会議においては市長を\x01",
            "支えるのが議長たる\x01",
            "私の仕事であり絶対命題だ。\x02\x03",

            "とにかく、私は私で\x01",
            "やるべきことを尽くさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E2")

    TalkEnd(0xFE)
    SetChrSubChip(0x2D, 0x1)
    Return()

    # Function_19_4647 end

    def Function_20_46EA(): pass

    label("Function_20_46EA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_46FB")
    Jump("loc_4772")

    label("loc_46FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_4738")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4716")
    Call(0, 21)
    Jump("loc_4733")

    label("loc_4716")


    #C0144
    ChrTalk(
        0x2A,
        "#08000Fピュイ、ピュイ！\x02",
    )

    CloseMessageWindow()

    label("loc_4733")

    Jump("loc_4772")

    label("loc_4738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_4772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4753")
    Call(0, 22)
    Jump("loc_4772")

    label("loc_4753")


    #C0145
    ChrTalk(
        0x2A,
        "#08000Fピュイ、ピュ～イ！\x02",
    )

    CloseMessageWindow()

    label("loc_4772")

    TalkEnd(0xFE)
    Return()

    # Function_20_46EA end

    def Function_21_4776(): pass

    label("Function_21_4776")

    OP_4B(0x13, 0xFF)
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)

    #C0146
    ChrTalk(
        0x13,
        (
            "#07008Fねえ、ジーク。\x01",
            "もしお祖母様が出席されていたら\x01",
            "なんて発言されていたかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x2A,
        "#08000Fピュイ、ピューイ。\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x13,
        (
            "#07000Fふふ、そうね。\x01",
            "……私は私、よね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x13, 0x0, 500)

    #C0149
    ChrTalk(
        0x13,
        "#07002Fあ、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000Fすみません……\x01",
            "急にお訪ねしてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x13,
        (
            "#07009Fいえ、お気になさらないで下さい。\x02\x03",

            "１人でいると\x01",
            "色々と考え込んでしまって……\x01",
            "むしろ来て下さって嬉しいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x109,
        "#10105F姫殿下……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x102,
        (
            "#00108F……考え込むというのはやはり、\x01",
            "会議の後半についてでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x13,
        (
            "#07000Fええ、それもありますが……\x01",
            "もう少し根本的な所ですね。\x02\x03",

            "#07003F私も王太女として外交における\x01",
            "駆け引きの類にはある程度の\x01",
            "心得はあるつもりなのですが……\x02\x03",

            "およそ交渉事に必要とされる\x01",
            "洞察力に判断力、そしてバランス感覚……\x02\x03",

            "#07001F会議の前半においても、\x01",
            "それらの圧倒的な違いを\x01",
            "まざまざと痛感させられたので。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x103,
        "#00201Fそんなにですか……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x104,
        (
            "#00303Fまあですが、それだけ\x01",
            "冷静に分析できるっつうのも\x01",
            "十分凄いことッスよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        (
            "#10100Fはい、それに殿下は\x01",
            "確か私やロイドさんたちと\x01",
            "年齢が同じでいらっしゃるのに……\x02\x03",

            "本当に恐れ入ります。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x13,
        (
            "#07002Fふふ、ありがとうございます。\x02\x03",

            "#07003Fでも確かに、弱音ばかり\x01",
            "吐いていても仕方ありませんね。\x02\x03",

            "大陸の情勢が動いているとはいえ、\x01",
            "焦らず一歩一歩でも\x01",
            "経験を糧にして前に進まないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x105,
        (
            "#10302Fそうそう、それに\x01",
            "リラックスも大事なんじゃない？\x02\x03",

            "今だって、せっかくの\x01",
            "休憩時間なわけなんだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x101,
        (
            "#00006Fワジ……姫殿下に対して\x01",
            "その態度、何とかならないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x13,
        (
            "#07009Fふふ、全然構いません。\x01",
            "過度に気を遣われるより\x01",
            "その方が私も気持ちが楽なので。\x02\x03",

            "#07002Fでも……何だか不思議です。\x02\x03",

            "皆さんとお話をしていると、\x01",
            "まるでエステルさんたちを\x01",
            "相手にしている気になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        "#00106Fそんな、身に余るお言葉です。\x02",
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x13,
        (
            "#07000Fふふ、そうだ皆さん、\x01",
            "紅茶でもお淹れしましょうか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0164
    ChrTalk(
        0x101,
        "#00005Fいえ、とんでもありません。\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x103,
        "#00206Fええ、それに今は警戒中ですし。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x13,
        (
            "#07004Fすみません、それもそうですね。\x02\x03",

            "#07000Fでは皆さん、くれぐれも\x01",
            "お気を付け下さいね。\x02\x03",

            "私も、自らの務めを果たせるよう\x01",
            "頑張りますので。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#00002Fはい、了解です。\x02",
    )

    CloseMessageWindow()
    OP_93(0x13, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x13, 0xFF)
    SetScenarioFlags(0x1C4, 1)
    Return()

    # Function_21_4776 end

    def Function_22_4F4F(): pass

    label("Function_22_4F4F")

    OP_4B(0x20, 0xFF)
    TurnDirection(0x20, 0x0, 500)

    #C0168
    ChrTalk(
        0x20,
        "あら、皆さんは巡回担当の……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        "#00000Fええ、お邪魔しています。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x0, 500)

    #C0170
    ChrTalk(
        0x2A,
        "#08000Fピュイ！\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00102Fふふ、あなたはクローディア殿下と\x01",
            "一緒にいたジーク君ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x103,
        (
            "#00205Fなるほど、彼がキーアの\x01",
            "言っていた白ハヤブサの……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x2A,
        "#08000Fピュイ、ピュイ！\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        "#00301Fう～ん、何て言ってんだ？\x02",
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x109,
        "#10100Fティオちゃん、分かる？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x103,
        (
            "#00202Fええ、皆さんには『こんにちは』。\x01",
            "私には『初めまして』と。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        "#10302Fフフ、よく覚えているものだね。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x2A,
        "#08009Fピュイ、ピューイ！\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        (
            "#00202F『クローディア姫の友人なら当然だ』\x01",
            "だそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        "#00002Fはは、ありがとうな。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x2A,
        "#08009Fピュイ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x2A, 0x0, 0x0)
    OP_4C(0x20, 0xFF)
    SetScenarioFlags(0x1C3, 6)
    Return()

    # Function_22_4F4F end

    def Function_23_51D1(): pass

    label("Function_23_51D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_51E2")
    Jump("loc_5405")

    label("loc_51E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_531A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_529B")

    #C0182
    ChrTalk(
        0xFE,
        (
            "私たちはタワー内に\x01",
            "閉じ込められた人たちの\x01",
            "お世話をしているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "右翼の方には女の子もいて……\x01",
            "こんな事に巻き込まれてしまって\x01",
            "かわいそうですよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_5315")

    label("loc_529B")


    #C0184
    ChrTalk(
        0xFE,
        (
            "右翼の方には女の子もいて……\x01",
            "しかも、なんだか元気がないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0xFE,
        (
            "あとでお菓子でも持っていって\x01",
            "あげようかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5315")

    Jump("loc_5405")

    label("loc_531A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5372")

    #C0186
    ChrTalk(
        0xFE,
        (
            "と、とにかく……\x01",
            "我々スタッフも落ち着いて\x01",
            "行動しないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5405")

    label("loc_5372")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5380")
    Jump("loc_5405")

    label("loc_5380")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5405")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_539B")
    Call(0, 22)
    Jump("loc_5405")

    label("loc_539B")


    #C0187
    ChrTalk(
        0xFE,
        (
            "皆さん、ジーク君と\x01",
            "お知り合いだったんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "ふふ、ジーク君って、\x01",
            "とってもお利口さんですよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5405")

    TalkEnd(0xFE)
    Return()

    # Function_23_51D1 end

    def Function_24_5409(): pass

    label("Function_24_5409")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_54AC")

    #C0189
    ChrTalk(
        0xFE,
        "特務支援課の皆さんですね。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "皆さんのことは\x01",
            "いつでもお通しするよう\x01",
            "クローディア殿下から伺っています。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        "どうぞ、ご自由にお入り下さい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_54B5")

    label("loc_54AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_54B5")

    label("loc_54B5")

    TalkEnd(0xFE)
    Return()

    # Function_24_5409 end

    def Function_25_54B9(): pass

    label("Function_25_54B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_54CA")
    Jump("loc_5571")

    label("loc_54CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5568")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E5")
    Call(0, 21)
    Jump("loc_5563")

    label("loc_54E5")


    #C0192
    ChrTalk(
        0x13,
        (
            "#07000F皆さん、\x01",
            "雑談に付き合ってくださって\x01",
            "ありがとうございました。\x02\x03",

            "ここからも、お互いに\x01",
            "気を引き締めて行きましょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5563")

    Jump("loc_5571")

    label("loc_5568")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5571")

    label("loc_5571")

    TalkEnd(0xFE)
    Return()

    # Function_25_54B9 end

    def Function_26_5575(): pass

    label("Function_26_5575")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_560A")

    #C0193
    ChrTalk(
        0xFE,
        (
            "皆さんのお邪魔にならないよう、\x01",
            "我々はここでじっとしています。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "こういう時こそ理性的な行動を\x01",
            "心がけないといけませんからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_56B2")

    label("loc_560A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5618")
    Jump("loc_56B2")

    label("loc_5618")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_56B2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5633")
    Call(0, 27)
    Jump("loc_56B2")

    label("loc_5633")


    #C0195
    ChrTalk(
        0xFE,
        (
            "みっしぃの顔が\x01",
            "プリントされたお饅頭、ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "このような場では、\x01",
            "些か洒落が効きすぎている\x01",
            "ような気もするのですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_56B2")

    TalkEnd(0xFE)
    Return()

    # Function_26_5575 end

    def Function_27_56B6(): pass

    label("Function_27_56B6")

    OP_4B(0x1C, 0xFF)
    OP_4B(0x21, 0xFF)

    #C0197
    ChrTalk(
        0x1C,
        (
            "ふむ、しかし大統領に出すお茶請けは\x01",
            "本当にこれでよかったんですかねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x21,
        (
            "あはは、まあ職員の皆さんが\x01",
            "一生懸命考えたという話ですし、\x01",
            "心配はいらないと思いますよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x21,
        (
            "それにほら、何よりこのご当地感が\x01",
            "いいじゃないですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x1C,
        (
            "う～む、それならそれで\x01",
            "他にもあったと思うのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x102,
        (
            "#00105F（？　用意したお茶菓子に\x01",
            "  問題でもあったのかしら？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0202
    ChrTalk(
        0x103,
        (
            "#00201F（あれは、みっしぃ饅頭……\x01",
            "  通称『みしまん』ではないですか。）\x02\x03",

            "（問題も何も、\x01",
            "  これ以上ないベストな選択かと。）\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x109,
        "#10106F（そ、そうなのかな……？）\x02",
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x101,
        (
            "#00002F（はは、でも何ていうか\x01",
            "  話のネタにはなりそうだな。）\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x1C, 0xFF)
    OP_4C(0x21, 0xFF)
    SetScenarioFlags(0x1C4, 2)
    Return()

    # Function_27_56B6 end

    def Function_28_5926(): pass

    label("Function_28_5926")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5972")

    #C0205
    ChrTalk(
        0xFE,
        (
            "ま、まずは深呼吸しなきゃ……\x01",
            "すぅーー、はぁーーーっ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5A17")

    label("loc_5972")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_END)), "loc_5980")
    Jump("loc_5A17")

    label("loc_5980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5A17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_599B")
    Call(0, 27)
    Jump("loc_5A17")

    label("loc_599B")


    #C0206
    ChrTalk(
        0xFE,
        (
            "う～ん、そう言われると私も\x01",
            "何だか不安になって来ましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "でも、今さら他のものを\x01",
            "考えて用意している暇はないし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A17")

    TalkEnd(0xFE)
    Return()

    # Function_28_5926 end

    def Function_29_5A1B(): pass

    label("Function_29_5A1B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B15")

    #C0208
    ChrTalk(
        0x17,
        (
            "#07500F君たち、まだいたのかね。\x02\x03",

            "ふむ、よければここで一緒に\x01",
            "お茶でも飲んでいくかね？\x02\x03",

            "#07509F饅頭もあるし、\x01",
            "寛#2Rくつろ#いでもらって構わんぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x101,
        (
            "#00006Fいえ……\x01",
            "そういうわけには。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x102,
        "#00100Fええ、どうもお邪魔しました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_5B7F")

    label("loc_5B15")


    #C0211
    ChrTalk(
        0x17,
        (
            "#07503Fモグモグ……\x01",
            "しかし、この饅頭は絶品だな。\x02\x03",

            "#07509Fハハハ、いくつか\x01",
            "土産に買って帰るとするか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B7F")

    TalkEnd(0xFE)
    Return()

    # Function_29_5A1B end

    def Function_30_5B83(): pass

    label("Function_30_5B83")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_5C1B")

    #C0212
    ChrTalk(
        0xFE,
        (
            "あ、当たり前ですけど……\x01",
            "お部屋掃除どころじゃないですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "ぶるぶるっ……\x01",
            "悪いことを色々考えると\x01",
            "どうにも震えが止まりません。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D07")

    label("loc_5C1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_5C29")
    Jump("loc_5D07")

    label("loc_5C29")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_5D07")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CAA")

    #C0214
    ChrTalk(
        0xFE,
        (
            "ここから見る景色って、\x01",
            "本当に絶景ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xFE,
        (
            "窓拭きをしていると、\x01",
            "ついつい見入っちゃいます。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_5D07")

    label("loc_5CAA")

    OP_93(0xFE, 0x5A, 0x0)

    #C0216
    ChrTalk(
        0xFE,
        (
            "しゅっしゅっしゅっ……\x01",
            "ふんふふ～ん♪\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "きゅっきゅっきゅっ……\x01",
            "るんるる～ん♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D07")

    TalkEnd(0xFE)
    Return()

    # Function_30_5B83 end

    def Function_31_5D0B(): pass

    label("Function_31_5D0B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DBD")

    #C0218
    ChrTalk(
        0xFE,
        (
            "ここは休憩時に市長と議長が\x01",
            "共同で使用されるお部屋なんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "今まさに会議で戦われている\x01",
            "市長と議長のために、真心込めて\x01",
            "お掃除させてもらっています。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_5E27")

    label("loc_5DBD")


    #C0220
    ChrTalk(
        0xFE,
        (
            "パタパタパタ……\x01",
            "がんば～れ、ディーター市長ぉ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        (
            "パタパタパタ……\x01",
            "負ける～な、マクダエル議長ぉ♪\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5E27")

    TalkEnd(0xFE)
    Return()

    # Function_31_5D0B end

    def Function_32_5E2B(): pass

    label("Function_32_5E2B")

    TalkBegin(0xFE)

    #C0222
    ChrTalk(
        0xFE,
        (
            "ふう、これで後は\x01",
            "会議の後半を残すのみだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "まあ本当はここからが\x01",
            "大変なんだけど……市長と議長には\x01",
            "頑張ってもらわないとね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_32_5E2B end

    def Function_33_5EB7(): pass

    label("Function_33_5EB7")

    TalkBegin(0xFE)

    #C0224
    ChrTalk(
        0xFE,
        (
            "ああ、皆さん。\x01",
            "今、ディーター市長はお隣の\x01",
            "オリヴァルト皇子のお部屋に。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "そして、マクダエル議長は\x01",
            "左翼にあるアルバート大公の\x01",
            "お部屋にそれぞれご訪問中です。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xFE,
        (
            "よろしければ直接、お部屋の方を\x01",
            "訪ねてみてはいかがでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_33_5EB7 end

    def Function_34_5FA5(): pass

    label("Function_34_5FA5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_5FB6")
    Jump("loc_63DC")

    label("loc_5FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_61DA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_60FD")

    #C0227
    ChrTalk(
        0xFE,
        (
            "大統領は国防軍以外にも、\x01",
            "私設部隊として怪しげな人たちを\x01",
            "運用していたようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0xFE,
        (
            "あの街を襲った猟兵たちや、\x01",
            "この場にあまり似合わない不良少年が\x01",
            "タワー内にいたのを見た事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "少なからず疑問を覚えつつも、\x01",
            "口出しすることはありませんでしたが……\x01",
            "今思えば、怪しい点は多々ありましたね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_61D5")

    label("loc_60FD")


    #C0230
    ChrTalk(
        0xFE,
        (
            "あの街を襲った猟兵たちや、\x01",
            "この場にあまり似合わない不良少年が\x01",
            "タワー内にいたのを見た事があります。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "少なからず疑問を覚えつつも、\x01",
            "口出しすることはありませんでしたが……\x01",
            "今思えば、怪しい点は多々ありましたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_61D5")

    Jump("loc_63DC")

    label("loc_61DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_625F")

    #C0232
    ChrTalk(
        0xFE,
        (
            "まさか、会議場に\x01",
            "直接テロリストが\x01",
            "乗り込んで来るなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "こんな事態、いったい\x01",
            "誰が予想できたでしょうか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_63DC")

    label("loc_625F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_626D")
    Jump("loc_63DC")

    label("loc_626D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_63DC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6351")

    #C0234
    ChrTalk(
        0xFE,
        (
            "ここは休憩の間、\x01",
            "オリヴァルト皇子のために\x01",
            "開放するお部屋です。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "何といっても皇子は、\x01",
            "帝国の社交界でのご活躍が\x01",
            "有名な正真正銘の風流人……\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xFE,
        (
            "部屋のセッティングにも\x01",
            "自然と気合いが入りますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_63DC")

    label("loc_6351")


    #C0237
    ChrTalk(
        0xFE,
        (
            "オリヴァルト皇子といえば、\x01",
            "帝国の社交界でのご活躍が\x01",
            "有名な正真正銘の風流人……\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xFE,
        (
            "部屋のセッティングにも\x01",
            "自然と気合いが入りますよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_63DC")

    TalkEnd(0xFE)
    Return()

    # Function_34_5FA5 end

    def Function_35_63E0(): pass

    label("Function_35_63E0")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_6459")

    #C0239
    ChrTalk(
        0xFE,
        (
            "本当に、悪夢を\x01",
            "見ているとしか思えません……\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xFE,
        (
            "……みんな、これから\x01",
            "どうなっちゃうんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_64F6")

    label("loc_6459")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_END)), "loc_6467")
    Jump("loc_64F6")

    label("loc_6467")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_64F6")

    #C0241
    ChrTalk(
        0xFE,
        (
            "オリヴァルト皇子は薔薇の花、\x01",
            "特に赤い薔薇が大好きだそうなので\x01",
            "こうして飾っているんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xFE,
        "ふふ、喜んで頂けると嬉しいですね。\x02",
    )

    CloseMessageWindow()

    label("loc_64F6")

    TalkEnd(0xFE)
    Return()

    # Function_35_63E0 end

    def Function_36_64FA(): pass

    label("Function_36_64FA")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_36_64FA end

    def Function_37_6504(): pass

    label("Function_37_6504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EBD")

    #C0243
    ChrTalk(
        0x2B,
        (
            "#02809Fハハ、なるほど。\x01",
            "それは将来に期待が持てる\x01",
            "若者たちですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x2C,
        (
            "#07204Fああ、そして彼らはまだ\x01",
            "何色にも染まりきっていない。\x02\x03",

            "#07202Fだから、ますます――\x02",
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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_666A")
    Jump("loc_66B4")

    label("loc_666A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_668A")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66B4")

    label("loc_668A")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_66AA")
    OP_52(0x2C, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_66B4")

    label("loc_66AA")

    OP_52(0x2C, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2C, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_66B4")

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
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_676D")
    Jump("loc_67B7")

    label("loc_676D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_678D")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67B7")

    label("loc_678D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_67AD")
    OP_52(0x2B, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_67B7")

    label("loc_67AD")

    OP_52(0x2B, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0x2B, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_67B7")

    OP_52(0x2B, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x2B, 0x10)
    Sleep(100)

    #C0245
    ChrTalk(
        0x2C,
        (
            "#07205Fおお、支援課の諸君じゃないか。\x02\x03",

            "#07209Fよければ少し、\x01",
            "雑談に付き合っていかないかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#00002Fあ、はい。\x01",
            "お２人のお邪魔でなければ。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x102,
        (
            "#00102Fちなみに今はどんな\x01",
            "お話をされていたんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x2B,
        (
            "#02804Fああ、実は皇子殿下は\x01",
            "帝国にある士官学校の\x01",
            "理事を務めておられてね。\x02\x03",

            "#02800Fその話を伺っていたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x103,
        (
            "#00205F理事というと、\x01",
            "学校の責任者の１人ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x104,
        "#00302Fへえ、そんなことまでしてるんスね。\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x2C,
        (
            "#07204Fフフ、あくまで名前を\x01",
            "貸している程度に過ぎないけどね。\x02\x03",

            "#07202Fそういう意味では、\x01",
            "私なんかよりディーター市長の方が\x01",
            "貢献してくれていると言っていい。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x109,
        "#10105Fディーター市長が……？\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x2B,
        (
            "#02804Fああいや、あくまで\x01",
            "ビジネス的な意味だけどね。\x02\x03",

            "#02800Fその士官学校がエプスタイン財団から\x01",
            "導力ネットを試験導入するにあたって\x01",
            "ＩＢＣから少々融資させて頂いたんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        "#00105Fそ、そうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#00205Fそういえば、帝国方面でも\x01",
            "導力ネットの試験導入が始まっていると\x01",
            "財団本部で聞きましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、流石は\x01",
            "各国に支店を持つ国際銀行。\x01",
            "事業の手広さがハンパじゃないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x2C,
        (
            "#07202Fふむ、君たちに\x01",
            "こんな話をしたのも何かの縁だ。\x02\x03",

            "#07209Fもし機会があれば、\x01",
            "我が士官学校で特別講義なんかを\x01",
            "やってみる気はないかい？\x02\x03",

            "#07212Fその気があれば\x01",
            "講師と士官候補生の禁断の関係、\x01",
            "なんてのもアリだろうしね。\x02",
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
        "#00006Fな、なんの話ですか……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x2B, 0x1)

    #C0259
    ChrTalk(
        0x2B,
        (
            "#02809Fハハ、オリヴァルト殿下は\x01",
            "やはり大変愉快でいらっしゃる。\x02\x03",

            "次はお酒でも飲みながら、\x01",
            "落ち着いてお話したいものですな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2C, 0x0)

    #C0260
    ChrTalk(
        0x2C,
        (
            "#07209Fフフ、確かに。\x01",
            "こちらこそ是非ご一緒したいね。\x02",
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
            "#00109F（皇子殿下とおじさま……\x01",
            "  かなり意気投合してるみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#00012F（ああ、スケールの大きい趣味人同士、\x01",
            "  気が合うってところかな？）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 7)
    Jump("loc_6FD2")

    label("loc_6EBD")


    #C0263
    ChrTalk(
        0x2B,
        (
            "#02805Fちなみに殿下は\x01",
            "お酒には強い方なのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x2C,
        (
            "#07202Fああ、それなりにはね。\x02\x03",

            "#07204F……もっとも、世の中には\x01",
            "いくらでも上がいるものだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#00200F（皇子殿下……\x01",
            "  何だか遠い目をしていますね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#00000F（……？　何かお酒で\x01",
            "  大切な思い出でもあるのかな？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6FD2")

    Return()

    # Function_37_6504 end

    def Function_38_6FD3(): pass

    label("Function_38_6FD3")

    TalkBegin(0xFE)
    Call(0, 37)
    TalkEnd(0xFE)
    Return()

    # Function_38_6FD3 end

    def Function_39_6FDD(): pass

    label("Function_39_6FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FF0")
    Call(0, 51)
    Return()

    label("loc_6FF0")

    TalkBegin(0xFE)

    #C0267
    ChrTalk(
        0x14,
        (
            "#11501Fおっ、あれはアルモリカ村か？\x02\x03",

            "#11509F蜂がせっせと蜜を運んでるぜぇ。\x02",
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
        "#00006Fいや、見えるはずないですから。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_39_6FDD end

    def Function_40_70D5(): pass

    label("Function_40_70D5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_71B6")

    #C0269
    ChrTalk(
        0xFE,
        (
            "私たちは、戒厳令からずっと\x01",
            "こちらに拘束されていたんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xFE,
        (
            "そういえば、大統領はなんだか\x01",
            "不思議な雰囲気の女の子を\x01",
            "連れていたみたいでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0xFE,
        (
            "もしかしてあれが、\x01",
            "噂の《御子》なんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_7237")

    label("loc_71B6")


    #C0272
    ChrTalk(
        0xFE,
        (
            "大統領はなんだか\x01",
            "不思議な雰囲気の女の子を\x01",
            "連れていたみたいでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0xFE,
        (
            "もしかしてあれが、\x01",
            "噂の《御子》なんでしょうか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7237")

    TalkEnd(0xFE)
    Return()

    # Function_40_70D5 end

    def Function_41_723B(): pass

    label("Function_41_723B")

    TalkBegin(0xFE)

    #C0274
    ChrTalk(
        0xFE,
        (
            "独立国の無効宣言以来、\x01",
            "タワーで働く私たちにも\x01",
            "不安な状況が続いていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xFE,
        (
            "ま、まさかこんな事になるとは。\x01",
            "これからどうなるんだろうか……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_41_723B end

    def Function_42_72D9(): pass

    label("Function_42_72D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74A4")

    #C0276
    ChrTalk(
        0xFE,
        "エ、エリィ様……！？\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x102,
        (
            "#00102Fランフィさん……\x01",
            "ご無事でよかったです。\x02\x03",

            "こちらにはＩＢＣの人たちが\x01",
            "集まっているみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0xFE,
        (
            "は、はい……\x01",
            "マリアベルお嬢様のご命令で……\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xFE,
        (
            "市内は大変なことになっていますし、\x01",
            "ディーター様とマリアベルお嬢様は\x01",
            "どうしてしまわれたんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        (
            "#00001F……とにかく、\x01",
            "今はここにいてください。\x02\x03",

            "この状況は俺たちが\x01",
            "なんとかしてみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xFE,
        (
            "わ、分かりました……\x01",
            "どうかよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_7519")

    label("loc_74A4")


    #C0282
    ChrTalk(
        0xFE,
        (
            "ディーター様とマリアベルお嬢様は\x01",
            "どうしてしまわれたんでしょうか……\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xFE,
        "……それに、一緒にいたあの人は確か……\x02",
    )

    CloseMessageWindow()

    label("loc_7519")

    TalkEnd(0xFE)
    Return()

    # Function_42_72D9 end

    def Function_43_751D(): pass

    label("Function_43_751D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75F6")

    #C0284
    ChrTalk(
        0xFE,
        (
            "このフロアには大統領たちはいないが……\x01",
            "他の人たちは何かを知ってるかもしれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xFE,
        (
            "この場はひとまず任せておいて、\x01",
            "君たちは心置きなく捜査に励みたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0xFE,
        "……ただし、無茶はしないようにな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 3)
    Jump("loc_7667")

    label("loc_75F6")


    #C0287
    ChrTalk(
        0xFE,
        (
            "この場はひとまず任せておいて、\x01",
            "君たちは心置きなく捜査に励みたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0xFE,
        "……ただし、無茶はしないようにな。\x02",
    )

    CloseMessageWindow()

    label("loc_7667")

    TalkEnd(0xFE)
    Return()

    # Function_43_751D end

    def Function_44_766B(): pass

    label("Function_44_766B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7754")

    #C0289
    ChrTalk(
        0xFE,
        (
            "俺はマリアベルお嬢さんを信じて\x01",
            "技術部に残ったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0xFE,
        (
            "クレイはどうしても信用できないって\x01",
            "技術部を飛び出していったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xFE,
        (
            "ケンカ別れしちゃったけど……\x01",
            "どうやらあいつのほうが\x01",
            "正しかったみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 4)
    Jump("loc_77C0")

    label("loc_7754")


    #C0292
    ChrTalk(
        0xFE,
        (
            "……どうやらクレイのほうが\x01",
            "正しかったみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0xFE,
        (
            "ケンカ別れしちゃったけど、\x01",
            "仲直りできるかな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_77C0")

    TalkEnd(0xFE)
    Return()

    # Function_44_766B end

    def Function_45_77C4(): pass

    label("Function_45_77C4")

    TalkBegin(0xFE)

    #C0294
    ChrTalk(
        0xFE,
        (
            "戒厳令が出た後、市外の情報は\x01",
            "完全にシャットアウトされて\x01",
            "しまったのでございますー。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0xFE,
        (
            "導力ネットの端末も使えませんし、\x01",
            "やれやれでございますねー……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_45_77C4 end

    def Function_46_7866(): pass

    label("Function_46_7866")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_795B")

    #C0296
    ChrTalk(
        0xFE,
        (
            "保安部としては、タワーの構造や\x01",
            "職員達の勤務形態をある程度\x01",
            "把握しておく必要があるんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0xFE,
        (
            "オルキスタワーに移ってから、\x01",
            "どうも隠し事が増えた気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0xFE,
        (
            "マリアベルお嬢様たちは\x01",
            "一体どうされてしまったんだ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_7998")

    label("loc_795B")


    #C0299
    ChrTalk(
        0xFE,
        (
            "マリアベルお嬢様たちは\x01",
            "一体どうされてしまったんだ……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7998")

    TalkEnd(0xFE)
    Return()

    # Function_46_7866 end

    def Function_47_799C(): pass

    label("Function_47_799C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A88")

    #C0300
    ChrTalk(
        0xFE,
        (
            "危険度Ｓ、猟兵団《赤い星座》……\x01",
            "ディーター大統領が彼らと\x01",
            "繋がっていたという疑惑はあった。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0xFE,
        (
            "なんせ、ＩＢＣを爆破したあいつらが\x01",
            "大手を振ってうろついていたのだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        "……大統領……もはや信用できんな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 6)
    Jump("loc_7AB7")

    label("loc_7A88")


    #C0303
    ChrTalk(
        0xFE,
        (
            "ディーター大統領……\x01",
            "もはや信用できんな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AB7")

    TalkEnd(0xFE)
    Return()

    # Function_47_799C end

    def Function_48_7ABB(): pass

    label("Function_48_7ABB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BB6")

    #C0304
    ChrTalk(
        0xC,
        (
            "#11228Fお父さんはずっと……\x01",
            "悩んでいたんだと思います。\x02\x03",

            "お母さんのこと……わたしのこと……\x02\x03",

            "色々なことを考えているうちに\x01",
            "……後戻りが出来なくなって……\x02\x03",

            "#11227F……みなさん……\x01",
            "どうかお父さんの事を\x01",
            "よろしくお願いします……！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 7)
    Jump("loc_7BFF")

    label("loc_7BB6")


    #C0305
    ChrTalk(
        0xC,
        (
            "#11227Fみなさん……\x01",
            "どうかお父さんの事を\x01",
            "よろしくお願いします……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7BFF")

    TalkEnd(0xFE)
    Return()

    # Function_48_7ABB end

    def Function_49_7C03(): pass

    label("Function_49_7C03")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F6E")

    #C0306
    ChrTalk(
        0x11,
        (
            "#11Pお疲れ様です、\x01",
            "特務支援課の皆さんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x101,
        (
            "#6P#00003F#6Pええ、お疲れ様です。\x02\x03",

            "#00005Fこちらの部屋にはもしかして……？\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x11,
        (
            "#11Pはい、クロイス大統領……\x01",
            "いえ容疑者を拘束してあります。\x02",
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
        "#6P#00108F……大統領は、どんな様子ですか？\x02",
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x11,
        (
            "#11P我々警官隊が拘束した時には\x01",
            "茫然自失といった様子でしたが……\x01",
            "今は平静を取り戻しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x11,
        (
            "#11P抵抗する様子もないので、\x01",
            "我々も最低限の人員のみを\x01",
            "割いている状況です。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x11,
        (
            "#11Pセルゲイ警部からの指示で、\x01",
            "皆さんなら面会も可能ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x104,
        "#6P#00306Fそうか……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x103,
        "#6P#00208F……どうしますか、ロイドさん。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AF, 7)
    Jump("loc_7FF7")

    label("loc_7F6E")


    #C0315
    ChrTalk(
        0x11,
        (
            "#11Pこちらの部屋には、\x01",
            "クロイス容疑者の身柄を\x01",
            "拘束してあります。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x11,
        (
            "#11Pセルゲイ警部からの指示で、\x01",
            "皆さんなら面会も可能ですが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7FF7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8001")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_810D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "ディーターと面会する\x01",      # 0
            "やめておく\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_806B")
    Call(0, 50)
    Return()

    label("loc_806B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8108")

    #C0317
    ChrTalk(
        0x101,
        "#6P#00006F……今はやめておきます。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x11,
        "#11P了解しました。\x02",
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x11,
        (
            "#11Pクロイス容疑者との面会を\x01",
            "希望される場合は、\x01",
            "私に声をかけてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8108")

    Jump("loc_8001")

    label("loc_810D")

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

    # Function_49_7C03 end

    def Function_50_8144(): pass

    label("Function_50_8144")


    #C0320
    ChrTalk(
        0x101,
        (
            "#6P#00003F……よろしくお願いします。\x02\x03",

            "#00008F彼が今何を考えているのか……\x01",
            "話を聞いておきたい気がする。\x02",
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
        "#11P了解しました……それでは。\x02",
    )

    CloseMessageWindow()
    OP_93(0x11, 0x0, 0x1F4)

    def lambda_820C():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_820C)
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
    OP_8E(0x2B, "ディーター大統領")
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
            "#11301F#5P………………君たちか。\x02\x03",

            "#11304F……フフ、何の用だね？\x01",
            "今や国際的犯罪者となったこの私に……\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        "#12P#00001F……ディーターさん。\x02",
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x102,
        "#12P#00108F…………おじさま…………\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x2B,
        (
            "#11306F#5P……こうして１人になって\x01",
            "ようやく気づいたよ。\x02\x03",

            "ベルの言うとおり、\x01",
            "私はグリムウッド先生の思い通りに\x01",
            "動かされていたにすぎなかったのだとね。\x02\x03",

            "#11303F声高に《正義》という理想を掲げ、\x01",
            "そのためならば犠牲すらも厭#2Rいと#わなかった。\x02\x03",

            "#11311F……その結果、どうだ？\x01",
            "一人娘にすら見捨てられて、\x01",
            "今や大統領の座も失おうとしている。\x02\x03",

            "#11302F……ハハハハ……\x01",
            "あの《結社》の少年ではないが、\x01",
            "まるで哀れな道化師#6Rピ エ ロ#のようだ。\x02",
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
            "#12P#00006F……俺たちは、\x01",
            "あなたを完全には否定できません。\x02\x03",

            "#00008F自分の《正義》のためならば、\x01",
            "どこまでも信念を貫き通す……\x02\x03",

            "#00001F方法がどうあれ、\x01",
            "あなたがクロスベルの平和を\x01",
            "守ろうとしたのは事実ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#12P#00303F……だな。\x02\x03",

            "#00301F俺たちも、以前ＩＢＣで\x01",
            "あんたが言った言葉には\x01",
            "感じるものがあったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#12P#00203F『人は正義を求めてしまう生き物』……\x01",
            "確かにそう言えるのかもしれませんね。\x02\x03",

            "#00208F独立宣言に市民たちが賛同したのも、\x01",
            "あなたのその《正義》を追及する姿に\x01",
            "魅力を感じたからこそなんでしょう。\x02",
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
            "#12P#00106Fでも……おじさまのやり方は\x01",
            "やはり、間違っていたと思います。\x02\x03",

            "#00108Fたとえあのまま独立国が存続し、\x01",
            "おじさまの《正義》が認められて\x01",
            "平和が訪れたとして……\x02\x03",

            "その過程で切り捨てられた人々の傷は、\x01",
            "簡単に癒えることはありません。\x02\x03",

            "#00101F誰かを犠牲にすることを前提として\x01",
            "掴み取られる平和……\x02\x03",

            "それはおじさまが\x01",
            "あの独立宣言の壇上で仰られた、\x01",
            "“欺瞞”そのものではないでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x2B,
        (
            "#11304F#5P……フフ、そうだな。\x01",
            "エリィ、君の言うとおりだよ。\x02\x03",

            "キーア君という力を手にいれたことで、\x01",
            "私は己の《正義》に対して\x01",
            "盲目的になっていたのかもしれない。\x02\x03",

            "#11302Fグリムウッド先生にしてみても、\x01",
            "そんな欺瞞に気付けずにいる私など\x01",
            "さぞ扱いやすかったことだろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BBB")

    #C0333
    ChrTalk(
        0x10A,
        "#12P#00603F（……イアン先生……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C2A")

    label("loc_8BBB")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8BF5")

    #C0334
    ChrTalk(
        0x105,
        "#12P#10403F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_8C2A")

    label("loc_8BF5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8C2A")

    #C0335
    ChrTalk(
        0x106,
        "#12P#10703F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_8C2A")


    #C0336
    ChrTalk(
        0x2B,
        (
            "#11303F#5Pだが……《正義》というものが\x01",
            "力と意志によって行使されるという、\x01",
            "その考え自体は変わらない。\x02\x03",

            "#11301F君たちが、君たちの《正義》を\x01",
            "追い求め続けるというなら……\x02\x03",

            "君たちなりの力と意志を\x01",
            "先生たちに示す必要があるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x101,
        (
            "#12P#00006F……簡単ではないでしょうが……\x01",
            "なんとしてもやり遂げるつもりです。\x02\x03",

            "#00013Fキーアを取り戻すのに\x01",
            "それが必要だというのなら……！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8DD3")

    #C0338
    ChrTalk(
        0x106,
        "#12P#10701F……そうですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E3E")

    label("loc_8DD3")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E0D")

    #C0339
    ChrTalk(
        0x109,
        "#12P#10101Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_8E3E")

    label("loc_8E0D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_8E3E")

    #C0340
    ChrTalk(
        0x105,
        "#12P#10402Fフフ、そうだね。\x02",
    )

    CloseMessageWindow()

    label("loc_8E3E")


    #C0341
    ChrTalk(
        0x2B,
        (
            "#11301F#5P……ならば、私になど\x01",
            "もはや用はあるまい。\x02\x03",

            "#11303F先生もそうだが……我が娘ながら\x01",
            "ベルも正直、底知れぬ人間だ。\x02\x03",

            "#11304F君たちがキーア君を取り戻し、\x01",
            "前に進むことが出来るかどうか……\x02\x03",

            "#11300Fここで見極めさせてもらうとしよう。\x02",
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
        "#6P#00301Fお嬢……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x103,
        "#6P#00208F……大丈夫ですか？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(150)

    #C0345
    ChrTalk(
        0x102,
        (
            "#5P#00104F……うん、大丈夫。\x02\x03",

            "#00108Fベルにあんな風に切り捨てられて\x01",
            "少し心配だったけど……\x02\x03",

            "#00102F意外としっかりしてらっしゃったから。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#12P#00004F……ああ、俺も少し安心したよ。\x02\x03",

            "#00000F彼の言う通り……\x01",
            "俺たちは前に進むとしよう。\x02",
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

    # Function_50_8144 end

    def Function_51_91D0(): pass

    label("Function_51_91D0")

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
            "#11P#11504Fいや、それにしても\x01",
            "贅沢な眺めですね。\x02\x03",

            "#11500F特務支援課の皆さんも\x01",
            "そう思いませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#6P#00011Fレクターさん……\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#6P#00108Fどうしてこんな所に……\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x14,
        (
            "#11P#11504Fはは、宰相閣下の控え室に\x01",
            "その随行スタッフがいることに\x01",
            "何か不思議がおありですか？\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 3)), scpexpr(EXPR_END)), "loc_945A")

    #A0351
    AnonymousTalk(
        0x14,
        (
            "やあ、またお会いしましたね。\x02\x03",

            "ああいえ……\x01",
            "初めての間違いでしたか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_94B3")

    label("loc_945A")


    #A0352
    AnonymousTalk(
        0x14,
        (
            "皆さんとお会いするのは\x01",
            "数週間ぶりですね。\x02\x03",

            "ああいえ……\x01",
            "初めての間違いでしたか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_94B3")

    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0353
    ChrTalk(
        0x102,
        (
            "#6P#00106Fあの……お願いですから\x01",
            "真顔で冗談を言わないで下さい。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x103,
        (
            "#12P#00211F……何ていうか、\x01",
            "相変わらず食えない人ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x14,
        (
            "#11P#11509Fハハ、それがオレの\x01",
            "チャームポイントだからなァ。\x02\x03",

            "#11502Fで、さっきから何か言いたそうな\x01",
            "顔をしているようだが？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#6P#00006Fええ、おかげ様で\x01",
            "こちらも幾つか掴んでいる状況です。\x02\x03",

            "#00013Fこの通商会議においての……\x01",
            "貴方がた帝国政府の動きについて。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x14,
        (
            "#11P#11510Fふぅん、なるほどねぇ。\x01",
            "アンタらがどこまで\x01",
            "掴んでるかは知らないが……\x02\x03",

            "#11504Fなら、こんなのは知ってるか？\x02\x03",

            "#11501F――オレは『貴族派』と内通して\x01",
            "ギリアス・オズボーンの首を狙っている。\x02",
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
        "#6P#10107Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x105,
        "#6P#10301Fへぇ……？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x102,
        (
            "#6P#00106F……騙されないで。\x01",
            "これがこの人の手だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x104,
        (
            "#6P#00301F前と同じような手を\x01",
            "２度は喰らうかっつーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x103,
        "#12P#00211Fさすがに見くびりすぎかと。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x14,
        (
            "#11P#11509Fハハッ、こりゃ参ったな。\x02\x03",

            "#11502Fま、本音を言うと\x01",
            "もっと大層なリアクションを\x01",
            "期待したんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、意外と本当だったり\x01",
            "するっていうオチじゃないよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x101,
        (
            "#6P#00006F……レクター書記官。\x01",
            "貴方の立場と狙いが何でも構いません。\x02\x03",

            "#00008Fだが、俺の見たところ……\x01",
            "貴方はどんな仕事でも責任をもって\x01",
            "最後までやり遂げるタイプだと思います。\x02\x03",

            "#00001Fその意味で、俺たちは通商会議中、\x01",
            "少なくとも警備面においては\x01",
            "協力できるはずだ……\x02\x03",

            "#00000F──違いますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x14,
        (
            "#11P#11504Fクク……なるほどな。\x02\x03",

            "#11508Fま、さっきの発言は冗談として――\x01",
            "そう考えると色々想像が膨らむだろ？\x02\x03",

            "#11501F常にあらゆるパターンを\x01",
            "探る手を休めない。\x02\x03",

            "#11509Fそれがいい物書きになる秘訣だぜぇ？\x02",
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
            "#6P#00006F誰も作家になろうとは\x01",
            "思っていませんが……\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x104,
        (
            "#6P#00301Fったく、どこまでも\x01",
            "人を喰ったヤツだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x14,
        (
            "#11P#11504Fま、今のはオレから出来る\x01",
            "アドバイスみたいなもんだ。\x02\x03",

            "#11500Fせいぜい色々考えて、\x01",
            "あらゆるケースに備えるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x109,
        "#6P#10106F……ご忠告、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#6P#00006F（はあ……しかし\x01",
            "  本当に読めない人だな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        (
            "#6P#00108F（ええ、何だかおかげで\x01",
            "  余計混乱した気がするわね。）\x02",
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

    # Function_51_91D0 end

    def Function_52_9D99(): pass

    label("Function_52_9D99")

    Sound(160, 0, 100, 0)
    Return()

    # Function_52_9D99 end

    def Function_53_9DA0(): pass

    label("Function_53_9DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DC8")
    SetScenarioFlags(0x146, 3)

    label("loc_9DC8")

    Return()

    # Function_53_9DA0 end

    def Function_54_9DC9(): pass

    label("Function_54_9DC9")

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
            "#6P#02803Fここは会議に参加する\x01",
            "各国首脳に用意された\x01",
            "控え室のあるフロアだ。\x02\x03",

            "#02800Fざっとだけ案内しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x101,
        "#00000F#11Pお願いします。\x02",
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
        "#00305F#5Pおお、さすが豪華だなー。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x105,
        (
            "#6P#10302Fフフ、こんな部屋で優雅に\x01",
            "時間を過ごしたいもんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0377
    ChrTalk(
        0x2B,
        (
            "#6P#02804Fこちらはオリヴァルト殿下に\x01",
            "使ってもらう予定の控え室だ。\x02\x03",

            "#02800F左翼にも部屋があって\x01",
            "参加者ごとに割り当ててある。\x02\x03",

            "#02809Fまあ、会議でヒートアップした頭を\x01",
            "冷やしてもらうための場所かな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A41B():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A41B)
    Sleep(50)

    def lambda_A42B():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A42B)
    Sleep(50)

    def lambda_A43B():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A43B)
    Sleep(50)

    def lambda_A44B():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A44B)
    Sleep(50)

    def lambda_A45B():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A45B)
    Sleep(50)

    def lambda_A46B():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A46B)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0378
    ChrTalk(
        0x109,
        "#11P#10112Fな、なるほど。\x02",
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x103,
        (
            "#00205F#11P一応、こうした部屋にも\x01",
            "導力ケーブルは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x2B,
        (
            "#6P#02805Fああ、目立たぬ形で\x01",
            "配線がされているはずだ。\x02\x03",

            "#02804Fまあ、他の部屋については\x01",
            "割愛するとして──\x02\x03",

            "#02800F最後にあそこだけ\x01",
            "案内しておくとしようか。\x02",
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

    def lambda_A6FF():
        OP_98(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x35, 1, lambda_A6FF)

    def lambda_A719():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A719)
    Sleep(50)

    def lambda_A736():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A736)
    Sleep(50)

    def lambda_A753():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A753)
    Sleep(50)

    def lambda_A770():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A770)
    Sleep(50)

    def lambda_A78D():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A78D)
    Sleep(50)

    def lambda_A7AA():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A7AA)
    Sleep(50)

    def lambda_A7C7():
        OP_97(0xFE, 0xFFFFC568, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A7C7)
    FadeToBright(1000, 0)
    Sleep(600)

    def lambda_A7ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_A7ED)
    Sleep(300)

    def lambda_A801():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A801)
    Sleep(600)

    def lambda_A815():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A815)
    Sleep(300)

    def lambda_A829():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A829)
    OP_0D()
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x29)
    SetChrSubChip(0x11, 0x0)

    #C0381
    ChrTalk(
        0x11,
        "#12A#5Pこれはディーター市長！\x02",
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
        "#12A#5Pお疲れさまです！\x02",
    )
    #Auto

    Sleep(1200)
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x2B, 1)

    #C0383
    ChrTalk(
        0x2B,
        "#02809F#11Pハハ、楽にしてくれたまえ。\x02",
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
            "#6P#02804Fこの回廊室からは会議の様子を\x01",
            "一通り確認することができる。\x02\x03",

            "#02800F機密性の高い会議などでは\x01",
            "カーテンを閉じることもあるが\x01",
            "今回は開いておく予定だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        "#00000F#11Pなるほど……\x02",
    )

    CloseMessageWindow()

    def lambda_A99E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A99E)
    Sleep(50)

    def lambda_A9AE():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A9AE)
    Sleep(50)

    def lambda_A9BE():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A9BE)
    Sleep(50)

    def lambda_A9CE():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A9CE)
    Sleep(50)

    def lambda_A9DE():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A9DE)
    Sleep(50)

    def lambda_A9EE():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A9EE)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    OP_68(-2000, 1500, -124000, 3000)
    MoveCamera(35, 17, 0, 3000)
    SetCameraDistance(19500, 3000)

    def lambda_AA38():
        OP_97(0x101, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AA38)
    Sleep(200)

    def lambda_AA55():
        OP_97(0x103, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AA55)
    Sleep(200)

    def lambda_AA72():
        OP_97(0x109, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AA72)
    Sleep(200)

    def lambda_AA8F():
        OP_97(0x102, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AA8F)
    Sleep(200)

    def lambda_AAAC():
        OP_97(0x104, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AAAC)
    Sleep(200)

    def lambda_AAC9():
        OP_97(0x105, 0x0, 0x0, 0x9C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AAC9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_AAFB():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_AAFB)
    OP_6F(0x79)

    #C0386
    ChrTalk(
        0x101,
        (
            "#00002F#11P会議場の様子を確かめられるのは\x01",
            "ちょっとありがたいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#00104F#11Pそうね、何かあったら\x01",
            "駆けつける事が出来そうだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x109,
        (
            "#10100F#11Pそういう意味では\x01",
            "巡回ルートにしたいですね。\x02",
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
            "#6P#02803Fさて、これで君たちが警備する\x01",
            "３つのフロアを案内したが……\x02\x03",

            "#02800F最後にとっておきの場所へ\x01",
            "案内させてもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AC86():
        TurnDirection(0x101, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AC86)
    Sleep(50)

    def lambda_AC96():
        TurnDirection(0x109, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AC96)
    Sleep(50)

    def lambda_ACA6():
        TurnDirection(0x102, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ACA6)
    Sleep(50)

    def lambda_ACB6():
        TurnDirection(0x105, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_ACB6)
    Sleep(50)

    def lambda_ACC6():
        TurnDirection(0x103, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ACC6)
    Sleep(50)

    def lambda_ACD6():
        TurnDirection(0x104, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ACD6)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0390
    ChrTalk(
        0x101,
        "#00005F#5Pとっておきの場所……\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x104,
        "#00302F#11Pへぇ、どこッスか？\x02",
    )

    CloseMessageWindow()

    #C0392
    ChrTalk(
        0x2B,
        (
            "#6P#02809Fフフ……このビルでもっとも\x01",
            "見晴らしのいい場所さ。\x02",
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

    # Function_54_9DC9 end

    def Function_55_ADA5(): pass

    label("Function_55_ADA5")

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

    # Function_55_ADA5 end

    def Function_56_AE24(): pass

    label("Function_56_AE24")


    def lambda_AE29():
        OP_95(0xFE, 81000, 0, 1500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE29)

    def lambda_AE43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE43)
    WaitChrThread(0xFE, 1)

    def lambda_AE58():
        OP_95(0xFE, 77500, 0, -1000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE58)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_56_AE24 end

    def Function_57_AE79(): pass

    label("Function_57_AE79")


    def lambda_AE7E():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AE7E)

    def lambda_AE98():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AE98)
    WaitChrThread(0xFE, 1)

    def lambda_AEAD():
        OP_95(0xFE, 79200, 0, -400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AEAD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_57_AE79 end

    def Function_58_AECE(): pass

    label("Function_58_AECE")


    def lambda_AED3():
        OP_95(0xFE, 81000, 0, 2000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AED3)

    def lambda_AEED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AEED)
    WaitChrThread(0xFE, 1)

    def lambda_AF02():
        OP_95(0xFE, 78300, 0, 500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF02)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_58_AECE end

    def Function_59_AF23(): pass

    label("Function_59_AF23")


    def lambda_AF28():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF28)

    def lambda_AF42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF42)
    WaitChrThread(0xFE, 1)

    def lambda_AF57():
        OP_95(0xFE, 80400, 0, -100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF57)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_59_AF23 end

    def Function_60_AF78(): pass

    label("Function_60_AF78")


    def lambda_AF7D():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AF7D)

    def lambda_AF97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AF97)
    WaitChrThread(0xFE, 1)

    def lambda_AFAC():
        OP_95(0xFE, 79500, 0, 800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFAC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_60_AF78 end

    def Function_61_AFCD(): pass

    label("Function_61_AFCD")


    def lambda_AFD2():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_AFD2)

    def lambda_AFEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_AFEC)
    WaitChrThread(0xFE, 1)

    def lambda_B001():
        OP_95(0xFE, 80800, 0, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B001)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_61_AFCD end

    def Function_62_B022(): pass

    label("Function_62_B022")


    def lambda_B027():
        OP_95(0xFE, 81000, 0, 3000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B027)

    def lambda_B041():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B041)
    WaitChrThread(0xFE, 1)

    def lambda_B056():
        OP_95(0xFE, 79900, 0, 2100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B056)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xE1, 0x1F4)
    Return()

    # Function_62_B022 end

    def Function_63_B077(): pass

    label("Function_63_B077")


    def lambda_B07C():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B07C)
    WaitChrThread(0xFE, 1)

    def lambda_B09A():
        OP_95(0xFE, 109000, 0, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B09A)
    WaitChrThread(0xFE, 1)

    def lambda_B0B8():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0B8)
    WaitChrThread(0xFE, 1)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x0)

    def lambda_B0EE():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B0EE)
    Sleep(500)

    def lambda_B10B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B10B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_63_B077 end

    def Function_64_B11C(): pass

    label("Function_64_B11C")


    def lambda_B121():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B121)
    WaitChrThread(0xFE, 1)
    Sleep(1000)
    MoveCamera(35, 19, 0, 7000)
    SetCameraDistance(19000, 7000)

    def lambda_B156():
        OP_95(0xFE, 109000, -600, -112500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B156)
    WaitChrThread(0xFE, 1)

    def lambda_B174():
        OP_95(0xFE, 111000, -600, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B174)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_64_B11C end

    def Function_65_B18E(): pass

    label("Function_65_B18E")


    def lambda_B193():
        OP_97(0xFE, 0xFFFFF254, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B193)
    Sleep(300)

    def lambda_B1B0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B1B0)
    WaitChrThread(0xFE, 1)

    def lambda_B1C5():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1C5)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_B1E6():
        OP_97(0xFE, 0x0, 0x0, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B1E6)
    WaitChrThread(0xFE, 1)

    def lambda_B204():

        label("loc_B204")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B204")

    QueueWorkItem2(0xFE, 2, lambda_B204)
    Return()

    # Function_65_B18E end

    def Function_66_B212(): pass

    label("Function_66_B212")


    def lambda_B217():
        OP_97(0xFE, 0xFFFFF448, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B217)
    Sleep(300)

    def lambda_B234():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B234)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x0)
    Sleep(100)

    def lambda_B256():
        OP_97(0xFE, 0x0, 0x0, 0x4268, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B256)
    WaitChrThread(0xFE, 1)

    def lambda_B274():

        label("loc_B274")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B274")

    QueueWorkItem2(0xFE, 2, lambda_B274)
    Return()

    # Function_66_B212 end

    def Function_67_B282(): pass

    label("Function_67_B282")


    def lambda_B287():
        OP_97(0xFE, 0xFFFFEDA4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B287)
    Sleep(400)

    def lambda_B2A4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B2A4)
    WaitChrThread(0xFE, 1)

    def lambda_B2B9():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2B9)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_B2DA():
        OP_97(0xFE, 0x0, 0x0, 0x3F48, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B2DA)
    WaitChrThread(0xFE, 1)

    def lambda_B2F8():

        label("loc_B2F8")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B2F8")

    QueueWorkItem2(0xFE, 2, lambda_B2F8)
    Return()

    # Function_67_B282 end

    def Function_68_B306(): pass

    label("Function_68_B306")


    def lambda_B30B():
        OP_97(0xFE, 0xFFFFEF98, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B30B)
    Sleep(400)

    def lambda_B328():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B328)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x1)
    Sleep(100)

    def lambda_B34A():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B34A)
    WaitChrThread(0xFE, 1)

    def lambda_B368():

        label("loc_B368")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B368")

    QueueWorkItem2(0xFE, 2, lambda_B368)
    Return()

    # Function_68_B306 end

    def Function_69_B376(): pass

    label("Function_69_B376")


    def lambda_B37B():
        OP_97(0xFE, 0xFFFFE8F4, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B37B)
    Sleep(500)

    def lambda_B398():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B398)
    WaitChrThread(0xFE, 1)

    def lambda_B3AD():
        OP_97(0xFE, 0xFFFFFC18, 0x0, 0x3E8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3AD)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_B3CE():
        OP_97(0xFE, 0x0, 0x0, 0x3B60, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3CE)
    WaitChrThread(0xFE, 1)

    def lambda_B3EC():

        label("loc_B3EC")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B3EC")

    QueueWorkItem2(0xFE, 2, lambda_B3EC)
    Return()

    # Function_69_B376 end

    def Function_70_B3FA(): pass

    label("Function_70_B3FA")


    def lambda_B3FF():
        OP_97(0xFE, 0xFFFFEAE8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B3FF)
    Sleep(500)

    def lambda_B41C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B41C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    OP_AD(0x2)
    Sleep(100)

    def lambda_B43E():
        OP_97(0xFE, 0x0, 0x0, 0x3778, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B43E)
    WaitChrThread(0xFE, 1)

    def lambda_B45C():

        label("loc_B45C")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_B45C")

    QueueWorkItem2(0xFE, 2, lambda_B45C)
    Return()

    # Function_70_B3FA end

    def Function_71_B46A(): pass

    label("Function_71_B46A")


    def lambda_B46F():
        OP_95(0xFE, 111000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B46F)
    WaitChrThread(0xFE, 1)

    def lambda_B48D():
        OP_95(0xFE, 113000, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B48D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_71_B46A end

    def Function_72_B4A7(): pass

    label("Function_72_B4A7")


    def lambda_B4AC():
        OP_95(0xFE, 109000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4AC)
    WaitChrThread(0xFE, 1)

    def lambda_B4CA():
        OP_95(0xFE, 100000, 0, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4CA)
    Sleep(3200)

    def lambda_B4E7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B4E7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_72_B4A7 end

    def Function_73_B4F8(): pass

    label("Function_73_B4F8")


    def lambda_B4FD():
        OP_95(0xFE, 109000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B4FD)
    WaitChrThread(0xFE, 1)

    def lambda_B51B():
        OP_95(0xFE, 103000, -600, -130500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B51B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_73_B4F8 end

    def Function_74_B535(): pass

    label("Function_74_B535")


    def lambda_B53A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B53A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x0)

    def lambda_B562():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B562)
    Sleep(2700)

    def lambda_B57F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B57F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_74_B535 end

    def Function_75_B590(): pass

    label("Function_75_B590")


    def lambda_B595():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC43C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B595)
    WaitChrThread(0xFE, 1)

    def lambda_B5B3():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5B3)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 0)

    def lambda_B5D4():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B5D4)
    Sleep(2700)

    def lambda_B5F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B5F1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_75_B590 end

    def Function_76_B602(): pass

    label("Function_76_B602")


    def lambda_B607():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC568, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B607)
    WaitChrThread(0xFE, 1)
    Sleep(700)

    def lambda_B628():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFFA88, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B628)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x1)

    def lambda_B650():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B650)
    Sleep(2800)

    def lambda_B66D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B66D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_76_B602 end

    def Function_77_B67E(): pass

    label("Function_77_B67E")


    def lambda_B683():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBFF0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B683)
    WaitChrThread(0xFE, 1)

    def lambda_B6A1():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6A1)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 1)

    def lambda_B6C2():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6C2)
    Sleep(2800)

    def lambda_B6DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B6DF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_77_B67E end

    def Function_78_B6F0(): pass

    label("Function_78_B6F0")


    def lambda_B6F5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFC694, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B6F5)
    WaitChrThread(0xFE, 1)
    Sleep(1100)

    def lambda_B716():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF510, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B716)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_AD(0x2)

    def lambda_B73E():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B73E)
    Sleep(2900)

    def lambda_B75B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B75B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_78_B6F0 end

    def Function_79_B76C(): pass

    label("Function_79_B76C")


    def lambda_B771():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFBBA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B771)
    WaitChrThread(0xFE, 1)
    Sleep(500)

    def lambda_B792():
        OP_97(0xFE, 0xFFFFF8F8, 0x0, 0xFFFFF8F8, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B792)
    WaitChrThread(0xFE, 1)
    SetScenarioFlags(0x0, 2)

    def lambda_B7B3():
        OP_97(0xFE, 0xFFFFDCD8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_B7B3)
    Sleep(2900)

    def lambda_B7D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_B7D0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_79_B76C end

    def Function_80_B7E1(): pass

    label("Function_80_B7E1")

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
        "#12P#10101F始まりましたね……\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x101,
        (
            "#11P#00003F……ああ。\x02\x03",

            "#00000Fでも、アリオスさんが\x01",
            "呼ばれているのは聞いてたけど\x01",
            "イアン先生まで呼ばれてるなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x103,
        (
            "#00202F#5Pしかも《熊ヒゲ先生》の名前で\x01",
            "知られているみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x102,
        (
            "#00104F国際会議では、様々な合意や\x01",
            "協定が交わされる事があるわ。\x02\x03",

            "#00100Fその場合、既存の国際法や\x01",
            "国際慣習法などに照らし合わせて\x01",
            "妥当かどうか判断する必要があるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x101,
        "#5P#00005Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x105,
        (
            "#12P#10302Fそのためのアドバイザーが\x01",
            "あの熊ヒゲ先生ってわけだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x104,
        (
            "#6P#00306Fしかし始まったはいいが……\x01",
            "さすがに小難しそうな話を\x01",
            "してるみてぇだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2E, 0x10E, 0x1F4)
    Sleep(150)

    #C0400
    ChrTalk(
        0x2E,
        (
            "#00603F#11Pまあ、会議の内容に関しては\x01",
            "我々が関与するところではない。\x02\x03",

            "#00600Fこの通商会議が無事に終わるか、\x01",
            "それだけに集中しておけ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1500)

    def lambda_BCAB():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BCAB)
    Sleep(50)

    def lambda_BCBB():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BCBB)
    Sleep(50)

    def lambda_BCCB():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BCCB)
    Sleep(50)

    def lambda_BCDB():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BCDB)
    Sleep(50)

    def lambda_BCEB():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BCEB)
    Sleep(50)

    def lambda_BCFB():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BCFB)
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
        "#00001F#6Pはい、心得ています。\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x102,
        (
            "#5P#00101Fそれでは早速、\x01",
            "打ち合わせどおりに？\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x2E,
        (
            "#00604F#11Pああ、お前たちには\x01",
            "３４Ｆ、３５Ｆ、３６Ｆを\x01",
            "一通り巡回してもらう。\x02\x03",

            "#00602F一応、お前たちの身分は\x01",
            "全関係者に伝えている状況だ。\x02\x03",

            "各国首脳のスタッフや\x01",
            "招待されたマスコミなどにも\x01",
            "話を聞いてみるといいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x109,
        "#6P#10100F了解しました！\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x2E,
        (
            "#00603F#11Pそれでは私は３４Ｆに戻る。\x02\x03",

            "#00600F……女神#4Rエイドス#の加護を。\x01",
            "何かあれば連絡してこい。\x02",
        )
    )

    CloseMessageWindow()
    OP_92(0x2E, 0xDAC, 0xFFFE0430, 0x1F4)
    OP_68(9000, 1300, -130000, 4000)

    def lambda_BEFD():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_BEFD)
    WaitChrThread(0x2E, 1)

    def lambda_BF1B():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_BF1B)
    Sleep(2000)

    def lambda_BF38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_BF38)
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
            "#00008F#5P……やっぱりダドリーさんも\x01",
            "何かあると思っているらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x102,
        "#5P#00103Fええ……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x103,
        (
            "#00211F#5Pこれだけ怪しげな動きがあって\x01",
            "何もないのは不自然かと……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(150)

    #C0409
    ChrTalk(
        0x109,
        (
            "#12P#10101Fどうやら気合いを入れて\x01",
            "巡回する必要がありそうですね！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C080():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_C080)
    Sleep(50)

    def lambda_C090():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_C090)
    Sleep(50)

    def lambda_C0A0():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_C0A0)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)

    #C0410
    ChrTalk(
        0x104,
        "#6P#00304Fだな。\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x105,
        "#6P#10300Fさっそく巡回を始めるかい？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(150)

    #C0412
    ChrTalk(
        0x101,
        (
            "#5P#00001Fああ、一通り回りながら\x01",
            "関係者に話を聞いてみよう。\x02",
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

    # Function_80_B7E1 end

    def Function_81_C1D2(): pass

    label("Function_81_C1D2")

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
            "#11P#00000Fよし……\x01",
            "これで一通り回ったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x109,
        (
            "#6P#10100F今のところは\x01",
            "特に問題なさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x104,
        (
            "#5P#00302Fああ、この調子でもう一度、\x01",
            "見て回るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x102,
        (
            "#00104Fそうね……\x02\x03",

            "#00108F……会議の方は\x01",
            "どうなっているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x101,
        (
            "#11P#00006Fそうだな、市長や議長が\x01",
            "頑張っているとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x103,
        (
            "#12P#00201F問題は《鉄血宰相》に\x01",
            "ロックスミス大統領ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、休憩時間になったら\x01",
            "誰かに聞けばいいんじゃない？\x02",
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

    # Function_81_C1D2 end

    def Function_82_C46A(): pass

    label("Function_82_C46A")

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
            "#11P#00000Fよし……\x01",
            "これで一通り回ったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x109,
        (
            "#6P#10100F今のところは\x01",
            "特に問題なさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x104,
        (
            "#5P#00302Fああ、この調子でもう一度、\x01",
            "見て回るとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x102,
        (
            "#00104Fそうね……\x02\x03",

            "#00108F……会議の方は\x01",
            "どうなっているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0424
    ChrTalk(
        0x101,
        (
            "#11P#00006Fそうだな、市長や議長が\x01",
            "頑張っているとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x103,
        (
            "#12P#00201F問題は《鉄血宰相》に\x01",
            "ロックスミス大統領ですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0426
    ChrTalk(
        0x105,
        (
            "#12P#10302Fま、休憩時間になったら\x01",
            "誰かに聞けばいいんじゃない？\x02",
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

    # Function_82_C46A end

    def Function_83_C702(): pass

    label("Function_83_C702")

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
        "#5P──お待ちしていました。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x15,
        (
            "#5Pクロスベル警察、\x01",
            "特務支援課の方々ですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x101,
        (
            "#11P#00001F……はい。\x01",
            "こちらが大統領閣下の？\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x15,
        (
            "#5Pええ、あなた方が来たら\x01",
            "通すように言われています。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0x0, 0x1F4)

    def lambda_C88A():
        OP_95(0xFE, -3200, 0, 28500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_C88A)
    WaitChrThread(0x15, 1)
    OP_93(0x15, 0xB4, 0x1F4)

    #C0431
    ChrTalk(
        0x15,
        "#5Pどうぞ、中にお入りください。\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x101,
        "#11P#00003Fそれでは……\x02",
    )

    CloseMessageWindow()

    #C0433
    ChrTalk(
        0x102,
        "#11P#00100F失礼します。\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x109,
        (
            "#12P#10108F（大陸最大の国家のひとつ、\x01",
            "  カルバードの首脳ですか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0435
    ChrTalk(
        0x104,
        (
            "#11P#00306F（さすがにちょいとばかり\x01",
            "  緊張してきたぜ……）\x02",
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

    # Function_83_C702 end

    def Function_84_CA0E(): pass

    label("Function_84_CA0E")


    def lambda_CA13():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA13)
    WaitChrThread(0xFE, 1)

    def lambda_CA31():
        OP_95(0xFE, -5500, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA31)
    Sleep(600)

    def lambda_CA4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CA4E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_CA0E end

    def Function_85_CA5F(): pass

    label("Function_85_CA5F")

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
        "#5P──お疲れさまでした。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x15,
        (
            "#5Pオズボーン宰相のお部屋は\x01",
            "反対側になると思います。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CC28():

        label("loc_CC28")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC28")

    QueueWorkItem2(0x101, 2, lambda_CC28)

    def lambda_CC3A():

        label("loc_CC3A")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC3A")

    QueueWorkItem2(0x102, 2, lambda_CC3A)
    Sleep(50)

    def lambda_CC4F():

        label("loc_CC4F")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC4F")

    QueueWorkItem2(0x103, 2, lambda_CC4F)
    Sleep(50)

    def lambda_CC64():

        label("loc_CC64")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC64")

    QueueWorkItem2(0x109, 2, lambda_CC64)
    Sleep(50)

    def lambda_CC79():

        label("loc_CC79")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC79")

    QueueWorkItem2(0x105, 2, lambda_CC79)
    Sleep(50)

    def lambda_CC8E():

        label("loc_CC8E")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_CC8E")

    QueueWorkItem2(0x104, 2, lambda_CC8E)

    #C0438
    ChrTalk(
        0x101,
        "#11P#00011F……あ、どうも。\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x102,
        "#11P#00103Fわざわざ有難うございます。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x15,
        "#5Pいえ、それでは。\x02",
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

    def lambda_CDC7():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_CDC7)
    Sleep(50)

    def lambda_CDD7():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_CDD7)
    Sleep(50)

    def lambda_CDE7():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_CDE7)
    Sleep(50)

    def lambda_CDF7():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_CDF7)
    Sleep(50)

    def lambda_CE07():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_CE07)
    Sleep(50)

    def lambda_CE17():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_CE17)
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
            "#10309F#11Pはは、人当たりはいいけど\x01",
            "さすが大国のトップだねぇ。\x02\x03",

            "#10302Fとんでもない大狸じゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x109,
        (
            "#6P#10106Fワジ君……\x01",
            "滅多なこと言わないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x103,
        (
            "#00206F#11Pでも、結構露骨でしたよね。\x02\x03",

            "#00211Fわたしたちを威圧するのが\x01",
            "目的ではなさそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x102,
        (
            "#00108F#5P多分、体裁を整えるのが\x01",
            "目的だったんだと思うわ……\x02\x03",

            "#00103F共和国の大統領が、\x01",
            "教団事件の解決に貢献した私たちに\x01",
            "勲章を贈るという体裁が……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x101,
        (
            "#6P#00003Fクロスベルの事件は\x01",
            "自分たちにとっての事件……\x02\x03",

            "#00001Fつまり宗主国としての領有権を\x01",
            "改めて強調してきたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x104,
        (
            "#00306F#5Pおいおい……\x01",
            "そのために呼んだのかよ。\x02\x03",

            "#00301F大国のトップってのは\x01",
            "やっぱりとんでもねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x105,
        (
            "#10304F#11Pま、自治州議会の議員とは\x01",
            "明らかに格が違いそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x109,
        (
            "#12P#10108F……宰相の方は\x01",
            "どんな話があるんでしょう？\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x101,
        (
            "#6P#00001F……分からない。\x01",
            "とにかく肚を括っておこう。\x02",
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

    # Function_85_CA5F end

    def Function_86_D1C0(): pass

    label("Function_86_D1C0")


    def lambda_D1C5():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1C5)

    def lambda_D1DF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D1DF)
    WaitChrThread(0xFE, 1)

    def lambda_D1F4():
        OP_95(0xFE, -1500, 0, 26400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1F4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_86_D1C0 end

    def Function_87_D215(): pass

    label("Function_87_D215")


    def lambda_D21A():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D21A)

    def lambda_D234():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D234)
    WaitChrThread(0xFE, 1)

    def lambda_D249():
        OP_95(0xFE, -1200, 0, 27700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D249)
    WaitChrThread(0xFE, 1)

    def lambda_D267():

        label("loc_D267")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D267")

    QueueWorkItem2(0xFE, 2, lambda_D267)
    Return()

    # Function_87_D215 end

    def Function_88_D275(): pass

    label("Function_88_D275")


    def lambda_D27A():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D27A)

    def lambda_D294():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D294)
    WaitChrThread(0xFE, 1)

    def lambda_D2A9():
        OP_95(0xFE, 100, 0, 26800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2A9)
    WaitChrThread(0xFE, 1)

    def lambda_D2C7():

        label("loc_D2C7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D2C7")

    QueueWorkItem2(0xFE, 2, lambda_D2C7)
    Return()

    # Function_88_D275 end

    def Function_89_D2D5(): pass

    label("Function_89_D2D5")


    def lambda_D2DA():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D2DA)

    def lambda_D2F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D2F4)
    WaitChrThread(0xFE, 1)

    def lambda_D309():
        OP_95(0xFE, 400, 0, 28100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D309)
    WaitChrThread(0xFE, 1)

    def lambda_D327():

        label("loc_D327")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D327")

    QueueWorkItem2(0xFE, 2, lambda_D327)
    Return()

    # Function_89_D2D5 end

    def Function_90_D335(): pass

    label("Function_90_D335")


    def lambda_D33A():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D33A)

    def lambda_D354():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D354)
    WaitChrThread(0xFE, 1)

    def lambda_D369():
        OP_95(0xFE, -1500, 0, 25100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D369)
    WaitChrThread(0xFE, 1)

    def lambda_D387():

        label("loc_D387")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D387")

    QueueWorkItem2(0xFE, 2, lambda_D387)
    Return()

    # Function_90_D335 end

    def Function_91_D395(): pass

    label("Function_91_D395")


    def lambda_D39A():
        OP_95(0xFE, -3200, 0, 27000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D39A)

    def lambda_D3B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D3B4)
    WaitChrThread(0xFE, 1)

    def lambda_D3C9():
        OP_95(0xFE, 100, 0, 25500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D3C9)
    WaitChrThread(0xFE, 1)

    def lambda_D3E7():

        label("loc_D3E7")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_D3E7")

    QueueWorkItem2(0xFE, 2, lambda_D3E7)
    Return()

    # Function_91_D395 end

    def Function_92_D3F5(): pass

    label("Function_92_D3F5")

    EventBegin(0x0)

    def lambda_D3FC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_D3FC)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(111800, 1100, -102500, 2000)
    MoveCamera(45, 15, 0, 2000)
    SetCameraDistance(19500, 2000)
    OP_6F(0x79)
    SetChrName("ロイド")

    #A0450
    AnonymousTalk(
        0xFF,
        (
            "#00001F（あれが宰相の部屋か……）\x02\x03",

            "#00003F（多分、あそこを訪ねたら\x01",
            "  休憩時間も終わりだろう。）\x02\x03",

            "#00008F（他にやり残した事はないかな？）\x02",
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

    # Function_92_D3F5 end

    def Function_93_D504(): pass

    label("Function_93_D504")

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
        "#11Pクロスベル警察、特務支援課だな？\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x0, 0x1F4)

    def lambda_D5EE():
        OP_95(0xFE, 111300, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_D5EE)
    WaitChrThread(0x16, 1)
    OP_93(0x16, 0xE1, 0x1F4)

    #C0452
    ChrTalk(
        0x16,
        (
            "#5P宰相閣下がお待ちだ。\x01",
            "そのまま入るがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#6P#00001Fは、はい。\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x102,
        "#6P#00104Fそれでは失礼します。\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x103,
        "#6P#00211F（……何か偉そうですね。）\x02",
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x105,
        (
            "#10306F（さすが帝国軍人。\x01",
            "  無駄に威圧的だねぇ。）\x02",
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
            "#6P#00003F#6P──失礼します。\x01",
            "オズボーン宰相閣下。\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x102,
        (
            "#00100F#6Pクロスベル警察、特務支援課、\x01",
            "お招きにより参上しました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0459
    ChrTalk(
        0x2F,
        "#07404F#11P#N……入ってきたまえ。\x02",
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

    def lambda_DA7C():
        OP_96(0xFE, 0x2673C, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DA7C)
    Sleep(300)

    def lambda_DA99():
        OP_96(0xFE, 0x266D8, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA99)
    Sleep(50)

    def lambda_DAB6():
        OP_96(0xFE, 0x260FC, 0x0, 0x1AA90, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DAB6)
    Sleep(100)

    def lambda_DAD3():
        OP_96(0xFE, 0x26098, 0x0, 0x1AE78, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DAD3)
    Sleep(100)

    def lambda_DAF0():
        OP_96(0xFE, 0x26548, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_DAF0)
    Sleep(100)

    def lambda_DB0D():
        OP_96(0xFE, 0x26098, 0x0, 0x1A450, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_DB0D)
    WaitChrThread(0x109, 1)

    def lambda_DB2B():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_DB2B)
    WaitChrThread(0x105, 1)

    def lambda_DB3C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_DB3C)
    Sleep(500)

    #C0460
    ChrTalk(
        0x2F,
        (
            "#07400F#11P──この光景、実に見事だ。\x02\x03",

            "地上をこの高さから\x01",
            "見下ろせるような建造物を\x01",
            "人間が作り出せるとは……\x02\x03",

            "#07404Fフフ、かつて栄華を誇ったという\x01",
            "古代文明に届く所業だろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x101,
        "#6P#00000F……確かに。\x02",
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x103,
        (
            "#6P#00200F１２００年前の\x01",
            "ゼムリア文明のことですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x104,
        (
            "#00305F#6Pああ、何でも魔法みたいに\x01",
            "便利な文明があったそうだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x2F,
        (
            "#07400F#11P単なる理想郷というわけでは\x01",
            "必ずしも無かったようだ。\x02\x03",

            "#07404F昨年、リベールの異変時に\x01",
            "出現した巨大な浮遊都市……\x02\x03",

            "あれもゼムリアの時代に建造され、\x01",
            "そして人の手で封印されたそうだ。\x02\x03",

            "#07401F人の可能性と愚かさの象徴として。\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x101,
        "#6P#00001F人の可能性と、愚かさ……\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x102,
        (
            "#00108F#6Pその……\x01",
            "ずいぶんお詳しいのですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x2F,
        (
            "#07404F#11Pフフ、それほどでもない。\x02\x03",

            "#07400F特にクロスベルに関しては\x01",
            "ヨアヒムなる教団司祭ほどにも\x01",
            "真実に至っていないだろう。\x02",
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
        "#6P#00208Fそんなことまで……\x02",
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x2F,
        (
            "#07404F#11Pフフ、それに\x01",
            "分からない事があるからこそ\x01",
            "世の中というものは面白い。\x02\x03",

            "手の内が全て見えた遊戯#4Rゲーム#など\x01",
            "退屈の極みというものだ。\x02\x03",

            "#07400Fそう思わないか？\x01",
            "ワジ・ヘミスフィア。\x02",
        )
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x105,
        (
            "#6P#N#10306F……ふぅん。\x01",
            "僕の名前もご存知なのか。\x02\x03",

            "#10300Fいや、逆に名前しか\x01",
            "知らないということかな？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0472
    ChrTalk(
        0x2F,
        (
            "#07400F#11Pいや、さして興味が\x01",
            "無いというだけのことだ。\x02\x03",

            "#07404F《闘神》の継承の方が\x01",
            "むしろ興味をそそられるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x104,
        "#00301F#6P……あんた……\x02",
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        (
            "#6P#00006F《帝国軍情報局》……\x02\x03",

            "#00001F素晴らしい情報収集能力を\x01",
            "お持ちのようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x2F,
        "#07404F#11Pフフ……\x02",
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
            "エレボニア帝国政府代表、\x01",
            "ギリアス・オズボーンだ。\x02\x03",

            "諸君のことはレクターから\x01",
            "色々と聞いている。\x02\x03",

            "それでは残りの休憩時間、\x01",
            "話に付き合ってもらおうか？\x02",
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
            "#12P#00003F……それで、宰相閣下。\x02\x03",

            "#00001Fお話に付き合うというのは\x01",
            "一体どういう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x103,
        (
            "#12P#00211Fどうやら、大抵のことは\x01",
            "すでにご存知みたいですが。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)

    #C0479
    ChrTalk(
        0x2F,
        (
            "#07404F#11Pなに、単なるお喋りだ。\x02\x03",

            "#07400Fもしくは意識調査と\x01",
            "言い換えてもいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x109,
        "#6P#10105F意識調査……\x02",
    )

    CloseMessageWindow()

    #C0481
    ChrTalk(
        0x2F,
        (
            "#07403F#11Pああ、直截#4Rちょくさい#に尋ねよう。\x02\x03",

            "#07402F……君たちはこのクロスベルが\x01",
            "どれだけ持つと考えている？\x02",
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
        "#12P#00013F#4Sッ……！\x02",
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x105,
        "#6P#10306Fまた露骨な質問だね……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x2F, 0x1)
    Sleep(300)

    #C0484
    ChrTalk(
        0x2F,
        (
            "#07400F#5Pフフ、別に他意はない。\x02\x03",

            "#07403Fただ栄枯盛衰は歴史の常──\x01",
            "滅びなかった国は存在しない。\x02\x03",

            "ましてや導力革命によって\x01",
            "あらゆるものが加速し始めた\x01",
            "この時代において……\x02\x03",

            "#07401Fこの因縁の地がどこまで\x01",
            "現状のままでいられると思う？\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x102,
        "#00108F#6P……そ、それは……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x32, 0x0, 0xBB8, 0x96)

    #C0486
    ChrTalk(
        0x109,
        (
            "#6P#10107F──い、いつまでもです！\x02\x03",

            "守ろうという意志が\x01",
            "自治州の民にあるのならば！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    Sleep(150)

    #C0487
    ChrTalk(
        0x101,
        "#11P#00005Fノエル……\x02",
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x2F,
        (
            "#07400F#5Pそう、意志は常に重要だ。\x02\x03",

            "時に趨勢#4Rすうせい#をひっくり返し、\x01",
            "歴史そのものを動かすことも\x01",
            "まれではないだろう。\x02\x03",

            "#07404F人は無力な存在ではない。\x01",
            "私もその可能性を信じている。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x2)

    #C0489
    ChrTalk(
        0x109,
        "#6P#10100Fそ、それじゃあ……\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x2F,
        (
            "#07400F#5P──だが、その意志同士が\x01",
            "ぶつかり合った場合はどうだ？\x02",
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
            "#07401F#5P簡単だ──小さな意志は\x01",
            "より大きな意志に呑み込まれ、\x01",
            "その火勢を大きくするだろう。\x02\x03",

            "#07404Fそうして生まれた業火が\x01",
            "地上に幾つも現れた時……\x02\x03",

            "あらゆる正義と倫理は灼熱に溶け、\x01",
            "世界は一面の炎に包まれる。\x02\x03",

            "#07402F──そんな光景が容易に\x01",
            "幻視できるのではないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0493
    ChrTalk(
        0x103,
        "#12P#00210F#40W……ぁぁ………\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x109,
        "#6P#10110F#40W……ううっ……！\x02",
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
            "#12P#00003F#30W……確かに……\x01",
            "帝国や共和国に比べたら\x01",
            "『小さな意志』かもしれません……\x02\x03",

            "#00008Fですが……大きな炎が小さな炎を\x01",
            "必ず飲み込むとは限らないでしょう。\x02\x03",

            "#00007F#20Wかつて帝国の侵攻を退けた\x01",
            "リベール王国のように……！\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        "#00102F#6Pあ……\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x105,
        "#6P#10304F１２年前の『百日戦役』か……\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x2F,
        (
            "#07404F#5Pフフ、その通り。\x01",
            "意志には『強さ』が問われる。\x02\x03",

            "リベールの小さくも強き意志が\x01",
            "帝国の大きくも乱れた意志に\x01",
            "見事打ち克#2Rか#ったということだ。\x02\x03",

            "それは確かにクロスベルにとって\x01",
            "一つの教訓と言えるだろう。\x02\x03",

            "#07402F──果たしてクロスベルの民に\x01",
            "リベールの民ほどの誇りと強さが\x01",
            "備わっているかは知らぬが。\x02",
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
            "#07404F#11Pフフ、休憩時間も終わりだ。\x01",
            "話はここまでとしておこう。\x02\x03",

            "#07400F──ああ、帝国政府からは\x01",
            "特に勲章を贈るつもりはない。\x02\x03",

            "下手に『平民』に勲章を贈ったら\x01",
            "貴族勢力がうるさいのでね。\x02",
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
        "#5P……お前たち、運が良かったな。\x02",
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x16,
        (
            "#5Pあれほど上機嫌な閣下は\x01",
            "あまり見られるものではない。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F0AB():

        label("loc_F0AB")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_F0AB")

    QueueWorkItem2(0x101, 2, lambda_F0AB)

    def lambda_F0BD():

        label("loc_F0BD")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_F0BD")

    QueueWorkItem2(0x102, 2, lambda_F0BD)
    Sleep(50)

    def lambda_F0D2():

        label("loc_F0D2")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_F0D2")

    QueueWorkItem2(0x103, 2, lambda_F0D2)

    def lambda_F0E4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F0E4)
    Sleep(50)

    def lambda_F0F4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F0F4)

    def lambda_F101():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F101)

    #C0505
    ChrTalk(
        0x101,
        "#12P#00005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x104,
        "#6P#00301Fおいおい……なんの冗談だ？\x02",
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x16,
        (
            "#5Pお前たちのことを\x01",
            "気に入ったということだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0508
    ChrTalk(
        0x16,
        (
            "#5P重い言葉かもしれんが\x01",
            "まずは受け止めてみるがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0509
    ChrTalk(
        0x16,
        (
            "#5P──私の立場から\x01",
            "言えたことではないがな。\x02",
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

    def lambda_F2D7():
        TurnDirection(0x102, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F2D7)
    Sleep(50)

    def lambda_F2E7():
        TurnDirection(0x104, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F2E7)
    Sleep(50)

    def lambda_F2F7():
        TurnDirection(0x101, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_F2F7)
    Sleep(50)

    def lambda_F307():
        TurnDirection(0x109, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F307)
    Sleep(50)

    def lambda_F317():
        TurnDirection(0x105, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F317)
    Sleep(50)

    def lambda_F327():
        TurnDirection(0x103, 0x35, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F327)
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
        "#5P#00106F……途轍もなかったわね。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x104,
        "#6P#00310Fつうか、化物すぎんだろ……\x02",
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x101,
        (
            "#11P#00006F……ああ、何ていうか\x01",
            "立ってる次元が違う気がする。\x02\x03",

            "#00001F──ティオ、大丈夫か？\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x103,
        (
            "#6P#00206Fはい……何とか。\x02\x03",

            "#00208Fあの人から伝わってきた\x01",
            "炎のイメージが強烈すぎて\x01",
            "めまいを起こしましたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x109,
        (
            "#5P#10106F無理ないよ……あたしですら\x01",
            "何か見えた気がしたもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x105,
        (
            "#10308F#5P《鉄血宰相》か……\x01",
            "まさに怪物って感じだね。\x02\x03",

            "#10303Fクロスベル程度なら\x01",
            "一呑みにしてしまいそうだな。\x02",
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
            "#11P#00003F──でも、俺たちを嬲#2Rなぶ#るために\x01",
            "呼び出したわけでもないだろう。\x02\x03",

            "大統領もそうだけど……\x01",
            "俺たちに興味があったというのも\x01",
            "嘘じゃないと思う。\x02\x03",

            "#00000Fなら、いい勉強をさせてもらったと\x01",
            "考えた方がいいかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F632():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_F632)
    Sleep(0)

    def lambda_F642():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_F642)
    Sleep(0)

    def lambda_F652():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F652)
    Sleep(0)

    def lambda_F662():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_F662)
    Sleep(0)

    def lambda_F672():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_F672)
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
        "#10302F#5Pフフ、言うじゃない。\x02",
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x102,
        (
            "#5P#00104F……貴方のそういう所は\x01",
            "ちょっと真似できないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0519
    ChrTalk(
        0x104,
        (
            "#6P#00309Fああ……\x01",
            "ポジティブすぎんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x109,
        (
            "#5P#10101Fで、でも確かに……\x01",
            "落ち込んでも仕方ないですよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x103,
        (
            "#6P#00202Fそうですね……\x01",
            "得られた教訓は活かさないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x101,
        (
            "#11P#00003Fとにかく休憩時間も終わりだ。\x02\x03",

            "#00001Fダドリーさんの所に戻って\x01",
            "会見の結果を伝えておこう。\x02",
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

    # Function_93_D504 end

    def Function_94_F8ED(): pass

    label("Function_94_F8ED")


    def lambda_F8F2():
        OP_95(0xFE, 111300, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F8F2)
    WaitChrThread(0xFE, 1)

    def lambda_F910():
        OP_95(0xFE, 113000, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F910)
    Sleep(600)

    def lambda_F92D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F92D)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_F8ED end

    def Function_95_F93E(): pass

    label("Function_95_F93E")


    def lambda_F943():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F943)

    def lambda_F95D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F95D)
    WaitChrThread(0xFE, 1)

    def lambda_F972():
        OP_95(0xFE, 151000, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F972)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_95_F93E end

    def Function_96_F993(): pass

    label("Function_96_F993")


    def lambda_F998():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F998)

    def lambda_F9B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_F9B2)
    WaitChrThread(0xFE, 1)

    def lambda_F9C7():
        OP_95(0xFE, 151000, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F9C7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_96_F993 end

    def Function_97_F9E8(): pass

    label("Function_97_F9E8")


    def lambda_F9ED():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_F9ED)

    def lambda_FA07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FA07)
    WaitChrThread(0xFE, 1)

    def lambda_FA1C():
        OP_95(0xFE, 150100, 0, 104600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA1C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_97_F9E8 end

    def Function_98_FA3D(): pass

    label("Function_98_FA3D")


    def lambda_FA42():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA42)

    def lambda_FA5C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FA5C)
    WaitChrThread(0xFE, 1)

    def lambda_FA71():
        OP_95(0xFE, 150100, 0, 106900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA71)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_98_FA3D end

    def Function_99_FA92(): pass

    label("Function_99_FA92")


    def lambda_FA97():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FA97)

    def lambda_FAB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FAB1)
    WaitChrThread(0xFE, 1)

    def lambda_FAC6():
        OP_95(0xFE, 149200, 0, 105200, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FAC6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_99_FA92 end

    def Function_100_FAE7(): pass

    label("Function_100_FAE7")


    def lambda_FAEC():
        OP_96(0xFE, 0x24540, 0x0, 0x19E10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FAEC)

    def lambda_FB06():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FB06)
    WaitChrThread(0xFE, 1)

    def lambda_FB1B():
        OP_95(0xFE, 149200, 0, 106300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB1B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_100_FAE7 end

    def Function_101_FB3C(): pass

    label("Function_101_FB3C")


    def lambda_FB41():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB41)

    def lambda_FB5B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FB5B)
    WaitChrThread(0xFE, 1)

    def lambda_FB70():
        OP_95(0xFE, 109100, 0, -103400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB70)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_101_FB3C end

    def Function_102_FB91(): pass

    label("Function_102_FB91")


    def lambda_FB96():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FB96)

    def lambda_FBB0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FBB0)
    WaitChrThread(0xFE, 1)

    def lambda_FBC5():
        OP_95(0xFE, 109300, 0, -102300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FBC5)
    WaitChrThread(0xFE, 1)

    def lambda_FBE3():

        label("loc_FBE3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FBE3")

    QueueWorkItem2(0xFE, 2, lambda_FBE3)
    Return()

    # Function_102_FB91 end

    def Function_103_FBF1(): pass

    label("Function_103_FBF1")


    def lambda_FBF6():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FBF6)

    def lambda_FC10():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FC10)
    WaitChrThread(0xFE, 1)

    def lambda_FC25():
        OP_95(0xFE, 107600, 0, -103100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC25)
    WaitChrThread(0xFE, 1)

    def lambda_FC43():

        label("loc_FC43")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FC43")

    QueueWorkItem2(0xFE, 2, lambda_FC43)
    Return()

    # Function_103_FBF1 end

    def Function_104_FC51(): pass

    label("Function_104_FC51")


    def lambda_FC56():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC56)

    def lambda_FC70():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FC70)
    WaitChrThread(0xFE, 1)

    def lambda_FC85():
        OP_95(0xFE, 107300, 0, -102000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FC85)
    WaitChrThread(0xFE, 1)

    def lambda_FCA3():

        label("loc_FCA3")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FCA3")

    QueueWorkItem2(0xFE, 2, lambda_FCA3)
    Return()

    # Function_104_FC51 end

    def Function_105_FCB1(): pass

    label("Function_105_FCB1")


    def lambda_FCB6():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FCB6)

    def lambda_FCD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FCD0)
    WaitChrThread(0xFE, 1)

    def lambda_FCE5():
        OP_95(0xFE, 109000, 0, -101000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FCE5)
    WaitChrThread(0xFE, 1)

    def lambda_FD03():

        label("loc_FD03")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FD03")

    QueueWorkItem2(0xFE, 2, lambda_FD03)
    Return()

    # Function_105_FCB1 end

    def Function_106_FD11(): pass

    label("Function_106_FD11")


    def lambda_FD16():
        OP_95(0xFE, 110500, 0, -102500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD16)

    def lambda_FD30():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_FD30)
    WaitChrThread(0xFE, 1)

    def lambda_FD45():
        OP_95(0xFE, 108000, 0, -100300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_FD45)
    WaitChrThread(0xFE, 1)

    def lambda_FD63():

        label("loc_FD63")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_FD63")

    QueueWorkItem2(0xFE, 2, lambda_FD63)
    Return()

    # Function_106_FD11 end

    def Function_107_FD71(): pass

    label("Function_107_FD71")

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
        "#12P#10107F……これって……\x02",
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x103,
        (
            "#00206F#11P……イアン先生が\x01",
            "心配していた通りですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x105,
        (
            "#12P#10308F鉄血宰相と大統領に\x01",
            "押し切られてるって感じだね。\x02\x03",

            "#10301F反論の糸口はないのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x102,
        (
            "#00106F#11P……実際、自治州法に様々な\x01",
            "構造的欠陥があるのは事実なの。\x02\x03",

            "#00108Fだからおじいさまにしても\x01",
            "ディーターおじさまにしても\x01",
            "反論しにくいのでしょうけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x101,
        (
            "#11P#00006F──だが、その構造的欠陥は\x01",
            "７０年前の自治州成立時に\x01",
            "２大国から押し付けられたものだ。\x02\x03",

            "#00013Fその上でのあの強引な発言は\x01",
            "到底納得できるもんじゃないな……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x104,
        "#5P#00301Fハッ、確信犯ってことかよ。\x02",
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
            "#00601F#11Pいずれにせよ、会議の内容は\x01",
            "我々の関知するところではない。\x02\x03",

            "今は会議そのものが無事、\x01",
            "終了することに集中しておけ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1500, 1300, -127550, 1300)

    def lambda_1026E():
        TurnDirection(0x101, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1026E)
    Sleep(50)

    def lambda_1027E():
        TurnDirection(0x102, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1027E)
    Sleep(50)

    def lambda_1028E():
        TurnDirection(0x109, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1028E)
    Sleep(50)

    def lambda_1029E():
        TurnDirection(0x103, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1029E)
    Sleep(50)

    def lambda_102AE():
        TurnDirection(0x105, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_102AE)
    Sleep(50)

    def lambda_102BE():
        TurnDirection(0x104, 0x2E, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_102BE)
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
        "#00001F#6P……はい、もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x102,
        "#5P#00108Fそれではまた、一通り巡回を──\x02",
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
            "#00603F#5P捜査一課、ダドリーだ。\x02\x03",

            "#00605F……エマ君か。\x01",
            "いったいどうした──\x02",
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
        "#00607F#5Pなんだと……！？\x02",
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x101,
        "#00001F#6P（……なんだ？）\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x102,
        "#5P#00108F（何かあったみたいね……）\x02",
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
            "#00606F#11P──《赤い星座》と《黒月》が\x01",
            "それぞれの拠点から動いたそうだ。\x02\x03",

            "#00601F一課の監視を振り切ったらしい。\x02",
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
        "#00005F#6Pなっ……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0539
    ChrTalk(
        0x104,
        "#6P#00307Fなんだと！？\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x2E,
        (
            "#00603F#11P狼狽#4Rうろた#えるな。\x01",
            "これも想定の範囲内だ。\x02\x03",

            "#00601F何かあったら知らせるから\x01",
            "引き続き警戒しておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0541
    ChrTalk(
        0x101,
        "#00001F#6Pりょ、了解です。\x02",
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

    def lambda_106BA():
        OP_95(0xFE, 5500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_106BA)
    Sleep(500)

    #C0542
    ChrTalk(
        0x2E,
        (
            "#5P#00603F#12A──ああ、そうだ。\x02\x03",

            "#20A#00601F予備の警官隊を\x01",
            "動かしてもいいから……\x02",
        )
    )
    #Auto

    WaitChrThread(0x2E, 1)

    def lambda_10732():
        OP_95(0xFE, 11500, 0, -130000, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_10732)
    Sleep(2000)

    def lambda_1074F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2E, 2, lambda_1074F)
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
            "#6P#00308Fクソ……\x01",
            "本当に動きやがったか……\x02\x03",

            "#00310F一体何をするつもりだ！？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10876():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10876)
    Sleep(50)

    def lambda_10886():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10886)
    Sleep(50)

    def lambda_10896():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10896)
    Sleep(50)

    def lambda_108A6():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_108A6)
    Sleep(50)

    def lambda_108B6():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_108B6)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0544
    ChrTalk(
        0x103,
        "#11P#00208Fランディさん……\x02",
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x101,
        (
            "#00006F#11Pランディ、落ち着いてくれ。\x02\x03",

            "#00001Fいくら《赤い星座》でも\x01",
            "ここに仕掛けるとは思えない。\x02",
        )
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x102,
        (
            "#00108F#11Pそうね、ビルの正面は\x01",
            "警官隊が守っているし……\x02",
        )
    )

    CloseMessageWindow()

    #C0547
    ChrTalk(
        0x109,
        (
            "#11P#10101Fまさかこんな時に\x01",
            "抗争を始めるとか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x105,
        (
            "#12P#10306Fうーん、それもちょっと\x01",
            "不自然な気がするねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    Sleep(300)
    OP_82(0x64, 0x64, 0xBB8, 0x1F4)
    SetChrName("老人の声")

    #A0549
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#4S──なんですと！？\x07\x00\x02",
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

    def lambda_10ADD():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10ADD)
    Sleep(50)

    def lambda_10AED():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10AED)
    Sleep(50)

    def lambda_10AFD():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10AFD)
    Sleep(50)

    def lambda_10B0D():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_10B0D)
    Sleep(50)

    def lambda_10B1D():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10B1D)
    Sleep(50)

    def lambda_10B2D():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10B2D)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0550
    ChrTalk(
        0x101,
        "#11P#00011F今のは……？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x102,
        "#00112F#11Pお、おじいさま……？\x02",
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

    # Function_107_FD71 end

    def Function_108_10BBD(): pass

    label("Function_108_10BBD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_10BDB")
    OP_A1(0x2E, 0x7D0, 0x8, 0x8, 0x9, 0xA, 0x9, 0x8, 0xB, 0xC, 0xB)
    Jump("Function_108_10BBD")

    label("loc_10BDB")

    Return()

    # Function_108_10BBD end

    def Function_109_10BDC(): pass

    label("Function_109_10BDC")

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
        "#11P#00010Fくっ……！\x02",
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x109,
        "#12P#10106Fひ、酷い……\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x103,
        "#00208F#11P無茶苦茶です……\x02",
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x104,
        (
            "#11P#00301F……よくもあそこまで\x01",
            "面の皮が厚くなれるもんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x102,
        (
            "#00106F#11P……でも、全く根拠が無い\x01",
            "提案というわけではないわ。\x02\x03",

            "#00108Fこういう流れにだけは\x01",
            "なって欲しくなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x105,
        (
            "#12P#10308Fフム、ここが凌#2Rしの#ぎどころって\x01",
            "感じだけど……\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_10F5A():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_10F5A)
    Sleep(50)

    def lambda_10F6A():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_10F6A)
    Sleep(50)

    def lambda_10F7A():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_10F7A)
    Sleep(50)

    def lambda_10F8A():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10F8A)
    Sleep(50)

    def lambda_10F9A():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_10F9A)
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
        "#5P#00001Fこんな時に……\x02",
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x102,
        "#00101F#11Pダドリーさんから？\x02",
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
            "#00001Fはい、バニングスで──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男の声")

    #A0561
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "俺だ、セルゲイだ。\x02",
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
            "#00005Fセルゲイ課長？\x01",
            "どうしたんですか──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0563
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "時間がない、手短に話す。\x02\x03",

            "──ソーニャから連絡があった。\x02\x03",

            "タングラム、ベルガード両門の付近に\x01",
            "設置されたレーダー施設が破壊された。\x02\x03",

            "自治州領空に侵入する不審な飛行船を\x01",
            "捕捉するための対空レーダーだ。\x02",
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
            "#00011F#3Sな……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("セルゲイの声")

    #A0565
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どうやら噂になっていた\x01",
            "テロリストどもの仕業らしい。\x02\x03",

            "ダドリーにも伝えたから\x01",
            "お前たちの方でも備えておけ。\x02",
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
            "#00007Fわ、分かりました！\x02",
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
        "#00101F#11Pど、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0568
    ChrTalk(
        0x104,
        (
            "#6P#00307Fまさか叔父貴どもが\x01",
            "何かやらかしたのか！？\x02",
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
            "#11P#00013Fい、いや、\x01",
            "そっちじゃなくて──\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(30, 60, -1, -1)
    SetChrName("男性の声")

    #A0570
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "──皆さん。\x01",
            "少々、よろしいか？\x07\x00\x02",
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

    def lambda_11486():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11486)
    Sleep(50)

    def lambda_11496():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_11496)
    Sleep(50)

    def lambda_114A6():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_114A6)
    Sleep(50)

    def lambda_114B6():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_114B6)
    Sleep(50)

    def lambda_114C6():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_114C6)
    Sleep(50)

    def lambda_114D6():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_114D6)
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

    # Function_109_10BDC end

    def Function_110_11528(): pass

    label("Function_110_11528")

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
        "#11P#00107Fあ──\x02",
    )

    CloseMessageWindow()

    #C0572
    ChrTalk(
        0x105,
        (
            "#12P#10310Fこれは……\x01",
            "とんでもない事になったね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0573
    ChrTalk(
        0x103,
        (
            "#5P#00203F……オルキスタワーの\x01",
            "制御を奪われたようです。\x02\x03",

            "#00201F昨日のハッカーの\x01",
            "仕業かもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xE1, 0x1F4)

    #C0574
    ChrTalk(
        0x101,
        (
            "#11P#00010Fくっ、俺たちも行くぞ！\x02\x03",

            "#00007Fとにかく３５Ｆに降りて\x01",
            "首脳たちの安全を確保しないと！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11729():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11729)
    Sleep(50)

    def lambda_11739():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_11739)
    Sleep(50)

    def lambda_11749():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_11749)
    Sleep(50)

    def lambda_11759():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_11759)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    #C0575
    ChrTalk(
        0x109,
        "#12P#10107F──了解です！\x02",
    )

    CloseMessageWindow()

    #C0576
    ChrTalk(
        0x104,
        (
            "#6P#00307Fエレベーターが駄目なら\x01",
            "非常階段しかなさそうだな！\x02",
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

    # Function_110_11528 end

    def Function_111_11813(): pass

    label("Function_111_11813")

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
            "#12P#10101Fさ、さっきまで\x01",
            "通れたはずなのに……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0578
    ChrTalk(
        0x101,
        "#6P#00013Fティオ、行けるか……！？\x02",
    )

    CloseMessageWindow()

    def lambda_119AA():

        label("loc_119AA")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119AA")

    QueueWorkItem2(0x102, 2, lambda_119AA)

    def lambda_119BC():

        label("loc_119BC")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119BC")

    QueueWorkItem2(0x104, 2, lambda_119BC)

    def lambda_119CE():

        label("loc_119CE")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119CE")

    QueueWorkItem2(0x109, 2, lambda_119CE)

    def lambda_119E0():

        label("loc_119E0")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119E0")

    QueueWorkItem2(0x105, 2, lambda_119E0)

    def lambda_119F2():

        label("loc_119F2")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_119F2")

    QueueWorkItem2(0x101, 2, lambda_119F2)

    #C0579
    ChrTalk(
        0x103,
        "#11P#00201F……何とかやってみます。\x02",
    )

    CloseMessageWindow()

    def lambda_11A2D():
        OP_95(0xFE, -54700, 0, 2200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11A2D)
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
            "ティオはシャッター脇のコネクタに\x01",
            "導力ケーブルを接続した。\x07\x00\x02",
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

            "#00203F#20W……少々やっかいですね。\x02\x03",

            "#00201Fでも、これなら何とか……\x02",
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

    def lambda_11BD9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11BD9)
    Sleep(50)

    def lambda_11BE9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11BE9)
    Sleep(50)

    def lambda_11BF9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11BF9)
    Sleep(50)

    def lambda_11C09():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_11C09)
    Sleep(50)

    def lambda_11C19():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11C19)
    Sleep(500)

    #C0582
    ChrTalk(
        0x102,
        "#00102F開いた……！\x02",
    )

    CloseMessageWindow()
    OP_79(0xC)

    #C0583
    ChrTalk(
        0x104,
        "#00309Fさすがティオすけ！\x02",
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
            "#00206Fいえ、セキュリティが\x01",
            "低めに設定されていただけです。\x02\x03",

            "#00208Fですが今の解除で\x01",
            "他の扉のセキュリティが\x01",
            "強化されてしまいました。\x02\x03",

            "#00201Fとても全部は開いて\x01",
            "いられないかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x105,
        "#12P#N#10306Fそりゃまた用意周到な……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0586
    ChrTalk(
        0x101,
        (
            "#12P#00010Fくっ……\x01",
            "とにかく下に降りるぞ！\x02",
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

    # Function_111_11813 end

    def Function_112_11E58(): pass

    label("Function_112_11E58")


    def lambda_11E5D():
        OP_95(0xFE, -55700, 0, 3300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E5D)
    WaitChrThread(0xFE, 1)

    def lambda_11E7B():
        OP_95(0xFE, -55700, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E7B)
    WaitChrThread(0xFE, 1)

    def lambda_11E99():
        OP_95(0xFE, -52000, 0, 13500, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11E99)
    WaitChrThread(0xFE, 1)

    def lambda_11EB7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11EB7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_112_11E58 end

    def Function_113_11ED1(): pass

    label("Function_113_11ED1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11EEB")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_113_11ED1")

    label("loc_11EEB")

    Return()

    # Function_113_11ED1 end

    def Function_114_11EEC(): pass

    label("Function_114_11EEC")

    Sound(145, 2, 100, 0)
    Sleep(2000)
    Sound(143, 0, 70, 0)
    OP_24(0x91)
    Return()

    # Function_114_11EEC end

    def Function_115_11EFF(): pass

    label("Function_115_11EFF")

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

    def lambda_120B6():
        OP_96(0xFE, 0xFFFFFC18, 0x0, 0x6978, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x42, 1, lambda_120B6)
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
    SetChrName("ディーター大統領")

    #A0587
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──その意味で、我々は等しく\x01",
            "女神の前に罪を背負っている……\x02\x03",

            "欺瞞#4R ぎ まん#と怯懦#4Rきょうだ#。\x01",
            "それがその罪の名であろう。\x02",
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
    SetChrName("ディーター大統領")

    #A0588
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "過去、犠牲になった魂に\x01",
            "報いるためにも……！\x02\x03",

            "そして先日の襲撃によって\x01",
            "傷付いた人々に報いるためにも！\x02\x03",

            "我々の子供たちに、平和で\x01",
            "誇り高き未来を届けるためにも！\x02",
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
    SetChrName("ディーター大統領")

    #A0589
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S今こそ我々は、欺瞞#4R ぎ　まん#と怯懦#4Rきょうだ#を捨て\x01",
            "誇りと勇気をもって\x01",
            "立ち上がらなくてはならない！\x07\x00\x02",
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
        "キャンベル議員",
        "#5Pむ、無茶苦茶だ……\x02",
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x31,
        (
            "#6Pだ、だが……\x01",
            "確かにそう質#2Rただ#されると……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0592
    ChrTalk(
        0x2D,
        "#5P#02501F（………ディーター君…………）\x02",
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

    # Function_115_11EFF end

    def Function_116_124AD(): pass

    label("Function_116_124AD")

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
    SetChrName("大統領の声")

    #A0593
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "実は、アリオス長官は\x01",
            "かつては優秀な捜査官として\x01",
            "クロスベル警察にも所属していた。\x02\x03",

            "そしてギルドでは、ご存知のように\x01",
            "国際的な案件を数多く解決してきた\x01",
            "素晴らしい実績を持っている。\x02\x03",

            "その意味で、決して見当外れな\x01",
            "人事ではないということを\x01",
            "改めて保証させていただこう。\x07\x00\x02",
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
            "#40W……お父さん……\x01",
            "……………どうして…………\x02",
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

    # Function_116_124AD end

    def Function_117_127D4(): pass

    label("Function_117_127D4")

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
        "#6P#11230F青い《壁》が……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x34, 0xC, 400)
    Sleep(150)

    #C0596
    ChrTalk(
        0x34,
        (
            "#10503F……心配は無用だ。\x02\x03",

            "#10502Fお前に害が及ぶ事はないから\x01",
            "安心するといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0597
    ChrTalk(
        0xC,
        "#6P#11221Fっ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x34, 500)
    OP_68(163400, 1100, 56750, 500)
    MoveCamera(41, 19, 0, 500)
    SetCameraDistance(16000, 500)

    def lambda_12975():
        OP_96(0xFE, 0x27E48, 0x0, 0xDCB4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12975)
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
            "#12P#11226F#30Wわ、私のことより\x01",
            "お父さんの方が……！\x02\x03",

            "#11227F#30W……どうして……\x01",
            "どうしてこんなことに……！\x02\x03",

            "#11232F#30Wお母さんだってきっと……\x01",
            "……哀しんでるはずだよ……！\x02",
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
            "#10504F#5P……そうだな。\x02\x03",

            "サヤがいればきっと……\x01",
            "困った顔で説教されただろう。\x02",
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
            "#4071V#40W#25A──シズク。\x02\x03",

            "#4072V#40W#30Aお前に一つ、頼みたいことがある。\x02",
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

    # Function_117_127D4 end

    def Function_118_12C2B(): pass

    label("Function_118_12C2B")

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
        "#5P#00001F着いたか……\x02",
    )

    CloseMessageWindow()

    #C0602
    ChrTalk(
        0x102,
        (
            "#00108F#6P主任の話だと、かなりの人が\x01",
            "フロアにいるみたいだけど……\x02",
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
        "神経質そうな声",
        "#2Sお、お前たちは……！？\x02",
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

    def lambda_12ED7():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_12ED7)
    Sleep(50)

    def lambda_12EE7():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_12EE7)
    Sleep(50)

    def lambda_12EF7():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_12EF7)
    Sleep(50)

    def lambda_12F07():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_12F07)
    Sleep(50)

    def lambda_12F17():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_12F17)
    Sleep(50)

    def lambda_12F27():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_12F27)
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
        "#00011Fふ、副局長！？\x02",
    )

    CloseMessageWindow()

    #C0605
    ChrTalk(
        0x102,
        "#12P#00105Fどうしてここに……\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0606
    ChrTalk(
        0xF,
        "#5Pそ、それはこちらの台詞だ！\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0xF,
        (
            "#5P私はその……\x01",
            "昨夜出された戒厳令について\x01",
            "長官に問い合わせに来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0xF,
        (
            "#5Pそしたらそのまま拘束されて\x01",
            "こちらのフロアに……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13132")

    #C0609
    ChrTalk(
        0x10A,
        "#12P#N#00606F……そうでしたか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1319A")

    label("loc_13132")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13173")

    #C0610
    ChrTalk(
        0x109,
        "#12P#N#10106Fそうだったんですか……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1319A")

    label("loc_13173")


    #C0611
    ChrTalk(
        0x102,
        "#12P#00106Fそうだったんですか……\x02",
    )

    CloseMessageWindow()

    label("loc_1319A")


    #C0612
    ChrTalk(
        0x104,
        (
            "#00309Fいや、なんつーか、\x01",
            "ちょっと意外ッスね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13227")

    #C0613
    ChrTalk(
        0x105,
        (
            "#12P#N#10402Fフフ、上に問い合わせる\x01",
            "気概をお持ちだったとはね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1326D")

    label("loc_13227")


    #C0614
    ChrTalk(
        0x103,
        (
            "#12P#N#00204F上に問い合わせる気概が\x01",
            "おありとは思いませんでした。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1326D")

    OP_63(0xF, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0615
    ChrTalk(
        0xF,
        "#5Pど、どういう意味だねっ！？\x02",
    )

    CloseMessageWindow()

    #C0616
    ChrTalk(
        0xF,
        (
            "#5P第一君たちは、国防軍から\x01",
            "指名手配されていた筈だろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xF,
        "#5Pいったい何をしているのかね！？\x02",
    )

    CloseMessageWindow()

    #C0618
    ChrTalk(
        0x101,
        "#00006Fその……色々ありまして。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1338B")

    #C0619
    ChrTalk(
        0x103,
        (
            "#12P#N#00205Fそちらのあなたは……\x01",
            "ＩＢＣの技術部にいた？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_133C5")

    label("loc_1338B")


    #C0620
    ChrTalk(
        0x102,
        (
            "#12P#00105Fそちらの貴方は……\x01",
            "ＩＢＣの技術部にいた？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_133C5")


    #C0621
    ChrTalk(
        0x10,
        "#5Pああ……研究員のダビッドさ。\x02",
    )

    CloseMessageWindow()

    #C0622
    ChrTalk(
        0x10,
        (
            "#5P俺も昨日、マリアベルお嬢さんから\x01",
            "技術部の解散を伝えられてね……\x02",
        )
    )

    CloseMessageWindow()

    #C0623
    ChrTalk(
        0x10,
        (
            "#5P相棒もいないし、呆然としていたら\x01",
            "このフロアに連れて来られて……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_134D7")

    #C0624
    ChrTalk(
        0x106,
        (
            "#12P#N#10708F……まずはお互いの状況を\x01",
            "確認した方が良さそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13592")

    label("loc_134D7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13538")

    #C0625
    ChrTalk(
        0x109,
        (
            "#12P#N#10108Fえっと、まずはお互いの状況を\x01",
            "確認した方が良さそうですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13592")

    label("loc_13538")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13592")

    #C0626
    ChrTalk(
        0x10A,
        (
            "#12P#N#00603Fフム、まずはお互いの状況を\x01",
            "確認した方が良さそうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13592")

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
        "#5Pそ、そんな事になっていたとは……\x02",
    )

    CloseMessageWindow()

    #C0628
    ChrTalk(
        0xF,
        (
            "#5P独立国の無効宣言以来、\x01",
            "雲行きが怪しいとは思ったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0629
    ChrTalk(
        0xD,
        "#11Pど、どうしてこんな事に……\x02",
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0xE,
        (
            "#5P何だか悪い夢でも\x01",
            "見ているような気分です……\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x10,
        (
            "#5Pそうか……クレイのやつは\x01",
            "ロバーツ主任に協力してるのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x10,
        (
            "#5Pどうりで２、３日前から\x01",
            "タワーへのハッキングの仕方が\x01",
            "更に巧妙になってたわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0633
    ChrTalk(
        0x102,
        (
            "#6P#00103Fそれで……副局長。\x02\x03",

            "#00101F結局、このフロアに\x01",
            "大統領サイドの関係者は？\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0xF,
        "#5Pう、うむ……\x02",
    )

    CloseMessageWindow()

    #C0635
    ChrTalk(
        0xF,
        (
            "#5P大統領やマリアベル嬢はもちろん、\x01",
            "国防長官や猟兵どももいない。\x02",
        )
    )

    CloseMessageWindow()

    #C0636
    ChrTalk(
        0xF,
        (
            "#5Pそれに……\x01",
            "君たちの所にいたあの娘もな。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x101,
        "#12P#00006F……そうですか……\x02",
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x102,
        "#6P#00108F一体どのフロアに……\x02",
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x103,
        (
            "#12P#00203F……とりあえず主任からの\x01",
            "連絡を待つべきかと。\x02\x03",

            "#00201F現在、大急ぎで上層エリアを\x01",
            "調べてくれていると思います。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 500)
    Sleep(150)

    #C0640
    ChrTalk(
        0x104,
        (
            "#6P#00303Fその間、このフロアにいる\x01",
            "他のメンツでも確認しておこうぜ。\x02\x03",

            "#00301Fひょっとしたら何か\x01",
            "知ってるヤツがいるかもしれねぇ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0641
    ChrTalk(
        0x101,
        (
            "#11P#00006F……そうだな。\x01",
            "一通り話を聞いてみるか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13AE0")

    #C0642
    ChrTalk(
        0x10A,
        (
            "#00600F#12P副局長。\x01",
            "この場は頼めますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B65")

    label("loc_13AE0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B23")

    #C0643
    ChrTalk(
        0x109,
        (
            "#10101F#12P副局長。\x01",
            "この場は頼めますか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13B65")

    label("loc_13B23")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_13B65")

    #C0644
    ChrTalk(
        0x105,
        (
            "#10400F#12P副局長さん。\x01",
            "この場は頼めるかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13B65")


    def lambda_13B6A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_13B6A)
    Sleep(100)

    def lambda_13B7A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_13B7A)

    #C0645
    ChrTalk(
        0xF,
        "#5Pああ、任せておきたまえ。\x02",
    )

    CloseMessageWindow()

    #C0646
    ChrTalk(
        0xF,
        (
            "#5P……その、君たちもアレだ。\x01",
            "あんまり無茶はしないように。\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xF,
        (
            "#5P真実を掴む前に倒れてしまったら\x01",
            "元も子もないぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0x101,
        (
            "#12P#00000F……はい。\x01",
            "肝に銘じておきます。\x02",
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

    # Function_118_12C2B end

    def Function_119_13D21(): pass

    label("Function_119_13D21")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D45")
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    Jump("Function_119_13D21")

    label("loc_13D45")

    Return()

    # Function_119_13D21 end

    def Function_120_13D46(): pass

    label("Function_120_13D46")

    Sleep(500)

    label("loc_13D49")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_13D6D")
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1600)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(1300)
    Jump("loc_13D49")

    label("loc_13D6D")

    Return()

    # Function_120_13D46 end

    def Function_121_13D6E(): pass

    label("Function_121_13D6E")


    def lambda_13D73():
        OP_95(0xFE, -2800, 0, 11100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13D73)

    def lambda_13D8D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13D8D)
    WaitChrThread(0xFE, 1)
    OP_68(-2000, 1000, 2850, 3500)
    MoveCamera(37, 21, 0, 3500)
    SetCameraDistance(18000, 3500)

    def lambda_13DC7():
        OP_95(0xFE, -2500, 0, 4700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13DC7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_121_13D6E end

    def Function_122_13DE1(): pass

    label("Function_122_13DE1")


    def lambda_13DE6():
        OP_95(0xFE, -2800, 0, 11000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13DE6)

    def lambda_13E00():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13E00)
    WaitChrThread(0xFE, 1)

    def lambda_13E15():
        OP_95(0xFE, -1300, 0, 5300, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13E15)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_122_13DE1 end

    def Function_123_13E2F(): pass

    label("Function_123_13E2F")

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
        "#00005F#5P（あ……）\x02",
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

            "#11226F……キーアちゃん………\x01",
            "………お父さん……どうして……\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x101,
        "#00002Fシズクちゃん……！\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_141C9():

        label("loc_141C9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_141C9")

    QueueWorkItem2(0xC, 2, lambda_141C9)
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
        "#11230Fあ……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)
    Sleep(300)

    #C0653
    ChrTalk(
        0x102,
        (
            "#12P#00109Fよかった……\x01",
            "無事だったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0654
    ChrTalk(
        0x103,
        (
            "#12P#00202Fシズクさんもオルキスタワーに\x01",
            "連れて来られていたんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0655
    ChrTalk(
        0x104,
        (
            "#00304Fあのオッサンの事だから\x01",
            "別の場所かと思ったが……\x02\x03",

            "#00302Fとにかく無事でよかったぜ。\x02",
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
            "#30Wロイドさん、ランディさん……\x01",
            "……エリィさんにティオさんも……\x02\x03",

            "……そっか……\x01",
            "こんな顔をしていたんですね……\x02",
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
        "#00005Fシズクちゃん、ひょっとして。\x02",
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x102,
        "#12P#00102F目が……見えるようになったの？\x02",
    )

    CloseMessageWindow()

    #C0659
    ChrTalk(
        0xC,
        (
            "#11226F#5P……はい。\x01",
            "キーアちゃんのおかげです。\x02\x03",

            "不思議な力で、目の神経を\x01",
            "繋いでくれたみたいで……\x02\x03",

            "#11231Fもう光だけじゃなくて……\x01",
            "色と形もちゃんと分かります。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_145DF")

    #C0660
    ChrTalk(
        0x109,
        "#10105F#5Pす、凄い……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1464A")

    label("loc_145DF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14618")

    #C0661
    ChrTalk(
        0x10A,
        "#00605F#5P……信じられん力だ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1464A")

    label("loc_14618")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1464A")

    #C0662
    ChrTalk(
        0x106,
        "#10712F#5P信じられません……\x02",
    )

    CloseMessageWindow()

    label("loc_1464A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1469C")

    #C0663
    ChrTalk(
        0x105,
        (
            "#10408F#5P《零の至宝》の力は\x01",
            "生命活動にも影響する……？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1470F")

    label("loc_1469C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_146D9")

    #C0664
    ChrTalk(
        0x106,
        "#10708F#5Pまさに“奇蹟”ですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1470F")

    label("loc_146D9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1470F")

    #C0665
    ChrTalk(
        0x10A,
        "#00606F#5Pまさに“奇蹟”だな……\x02",
    )

    CloseMessageWindow()

    label("loc_1470F")


    #C0666
    ChrTalk(
        0x104,
        (
            "#00309Fいや、なんにせよ\x01",
            "良かったじゃないか！\x02",
        )
    )

    CloseMessageWindow()

    #C0667
    ChrTalk(
        0x101,
        (
            "#00004Fああ……こればかりは\x01",
            "キーアもお手柄だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0668
    ChrTalk(
        0xC,
        (
            "#11231F#5Pはい……本当に\x01",
            "キーアちゃんにはいくらお礼を\x01",
            "言っても足りないくらいで……\x02\x03",

            "#11233F#30W……でも……\x01",
            "でもっ……ううううっ！\x02",
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
        "#12P#00101Fシズクちゃん……！？\x02",
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x101,
        "#00011Fど、どうしたんだ？\x02",
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
            "#11227F#5P#30Wキーアちゃん、笑っていたけど\x01",
            "とっても辛そうでした……！\x02\x03",

            "これが自分の役割なんだ……\x01",
            "……自分の望みなんだって\x01",
            "無理に言い聞かせてるみたいで！\x02\x03",

            "#11232F本当はディーターさんたちに\x01",
            "協力なんてしたくないのに……！\x02\x03",

            "ロイドさんたちのところに\x01",
            "戻りたくてしょうがないのに……！\x02",
        )
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x101,
        "#00008Fあ……\x02",
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x104,
        "#00306Fそっか……\x02",
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
            "#11233F#5P#30Wどうしてキーアちゃんが\x01",
            "あんな事に……？\x02\x03",

            "それに……\x01",
            "……どうしてお父さんは……\x02\x03",

            "#11234F……わたし……わたし………\x02",
        )
    )

    CloseMessageWindow()

    #C0675
    ChrTalk(
        0x103,
        "#12P#00208F……シズクさん……\x02",
    )

    CloseMessageWindow()
    OP_68(163420, 900, 56850, 1200)

    def lambda_14B1B():
        OP_95(0xFE, 162800, 0, 57000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_14B1B)
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
            "#6P#00104F……ありがとう。\x01",
            "キーアちゃんの事を想ってくれて。\x02\x03",

            "#00108Fそれと……\x01",
            "一人ぼっちで辛かったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0xC,
        "#11233F#5P#30Wうううっ……グスッ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0678
    ChrTalk(
        0x101,
        (
            "#00003F……シズクちゃん。\x01",
            "俺たちはキーアを\x01",
            "取り戻しに来たんだ。\x02\x03",

            "#00001Fあの子や、アリオスさんたちが\x01",
            "どこにいるか知ってるかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0679
    ChrTalk(
        0xC,
        (
            "#11233F#5P#30Wごめんなさい……\x01",
            "わたし何も知らなくって……\x02\x03",

            "キーアちゃんは昨日から\x01",
            "見かけていなくて……\x02\x03",

            "#11234Fそれと……お父さんからは\x01",
            "ロイドさんへの伝言を預かりました……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0680
    ChrTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14DB1")

    #C0681
    ChrTalk(
        0x10A,
        "#00605F#5Pマクレインが……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_14E22")

    label("loc_14DB1")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14DEC")

    #C0682
    ChrTalk(
        0x109,
        "#10105F#5Pア、アリオスさんが！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_14E22")

    label("loc_14DEC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14E22")

    #C0683
    ChrTalk(
        0x105,
        "#10405F#5P《風の剣聖》が……！？\x02",
    )

    CloseMessageWindow()

    label("loc_14E22")

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
        "#00001Fこの包みは……\x02",
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0xC,
        (
            "#11226F#11P……お父さんがロイドさんに\x01",
            "渡してくれって……\x02\x03",

            "#11221Fどうぞ、開けてみてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0686
    ChrTalk(
        0x101,
        "#00005Fあ、ああ……\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_150DB")
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    label("loc_150DB")

    Sleep(1000)

    #C0687
    ChrTalk(
        0x101,
        "#00007F#30W……これは………\x02",
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
        "#00208F#30Wガイさんが使っていた……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_151F9")

    #A0689
    AnonymousTalk(
        0x10A,
        (
            "#00606F#30W……間違いない。\x01",
            "ヤツが使っていた得物#4Rトンファー#だ。\x02\x03",

            "#00608F現場から持ち去られていて\x01",
            "行方不明になっていた……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_151F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15271")

    #A0690
    AnonymousTalk(
        0x105,
        (
            "#10405F#30Wこれは刀傷……？\x02\x03",

            "#10401F……ということは\x01",
            "ガイ・バニングスを\x01",
            "手に掛けたのは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1536A")

    label("loc_15271")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_152ED")

    #A0691
    AnonymousTalk(
        0x109,
        (
            "#10105F#30Wこれは刀傷……？\x02\x03",

            "#10101Fということは……\x01",
            "ロイドさんのお兄さんを\x01",
            "手に掛けたのは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1536A")

    label("loc_152ED")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1536A")

    #A0692
    AnonymousTalk(
        0x106,
        (
            "#10703F#30Wこれは……刀傷ですね。\x02\x03",

            "#10708Fということは……\x01",
            "ロイドさんのお兄さんを\x01",
            "手に掛けたのは……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1536A")

    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0693
    ChrTalk(
        0x102,
        "#12P#00108F#30Wロイド……\x02",
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
            "#11233F#11P#40W……ごめんなさい……\x01",
            "…………本当にごめんなさい……\x02\x03",

            "#40Wお父さんが……父が酷いことを……\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x101,
        (
            "#00006F──シズクちゃん。\x01",
            "負い目を感じる必要はないよ。\x02\x03",

            "#00008F本当にアリオスさんが、\x01",
            "兄貴を手に掛けたと\x01",
            "決まったわけじゃないし……\x02\x03",

            "#00013Fどうやら、まだ見えていない、\x01",
            "隠された真相がありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0xC,
        "#11227F#11P#30Wえ……\x02",
    )

    CloseMessageWindow()

    #C0698
    ChrTalk(
        0x104,
        "#00301Fどういう事だ？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_156D5")

    #C0699
    ChrTalk(
        0x101,
        (
            "#00008Fこの刀傷を見る限り、\x01",
            "兄貴とアリオスさんが激しく\x01",
            "やり合った可能性は高いだろう。\x02\x03",

            "#00003F刀傷の数を見る限り……\x01",
            "あの《風の剣聖》を相手に\x01",
            "兄貴もかなり善戦したんだと思う。\x02\x03",

            "#00013F……だが………\x02",
        )
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x10A,
        (
            "#6P#00603F──ガイの直接の死因は\x01",
            "銃による背後からの狙撃#22R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#。\x02\x03",

            "#00601Fそういう事だな、バニングス？\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x101,
        "#00001Fはい。\x02",
    )

    CloseMessageWindow()
    Jump("loc_157F6")

    label("loc_156D5")


    #C0702
    ChrTalk(
        0x101,
        (
            "#00008Fこの刀傷を見る限り、\x01",
            "兄貴とアリオスさんが激しく\x01",
            "やり合った可能性は高いだろう。\x02\x03",

            "#00003F刀傷の数を見る限り……\x01",
            "あの《風の剣聖》を相手に\x01",
            "兄貴もかなり善戦したんだと思う。\x02\x03",

            "#00013F──だが、兄貴の直接の死因は\x01",
            "背後から銃で撃たれた#20R㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲　㈲#ことだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_157F6")


    #C0703
    ChrTalk(
        0x103,
        "#6P#00205Fあ……\x02",
    )

    CloseMessageWindow()

    #C0704
    ChrTalk(
        0x102,
        "#12P#00105Fそれって……\x02",
    )

    CloseMessageWindow()

    #C0705
    ChrTalk(
        0x101,
        (
            "#00000F──シズクちゃん。\x01",
            "手紙も読ませてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0xC,
        "#11230F#11Pは、はい……\x02",
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
            "#4073V#40W──ロイドへ#1500W。\x01",
            "#40W長らく渡せなかった品を\x01",
            "これを機会にお返しする。\x02\x03",

            "#4074V#40Wその品が全て──\x01",
            "釈明をするつもりはない。\x02\x03",

            "#4075V#40Wなお、街に現れた魔導兵は\x01",
            "白き神機が大鐘を通じて\x01",
            "操っているものだ。\x02\x03",

            "#4076V#40W白き神機を何とかすれば\x01",
            "全て沈黙させられるだろう。\x07\x00\x02",
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
        "#00108F#30W……これは……\x02",
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
            "#00303F……白き神機ってのは、\x01",
            "あの映像で見たヤツか。\x02\x03",

            "#00301Fガレリア要塞をアイスみてぇに\x01",
            "くり抜きやがった……\x02",
        )
    )

    CloseMessageWindow()

    #C0711
    ChrTalk(
        0x103,
        (
            "#6P#00201Fでも、空間を消滅させる力は\x01",
            "使えなくなっているはずです。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BA6")

    #C0712
    ChrTalk(
        0x10A,
        (
            "#6P#00608Fしかしマクレインの奴、\x01",
            "一体どういうつもりで……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C41")

    label("loc_15BA6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15BF6")

    #C0713
    ChrTalk(
        0x106,
        (
            "#6P#10708Fでも《風の剣聖》は\x01",
            "一体どういうつもりで……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15C41")

    label("loc_15BF6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15C41")

    #C0714
    ChrTalk(
        0x109,
        (
            "#6P#10108Fでもアリオスさんは\x01",
            "一体どういうつもりで……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15C41")

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
            scpstr(SCPSTR_CODE_ITEM, 0x3F2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3F2, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_15CE7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_15CE7)

    def lambda_15CF4():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_15CF4)

    def lambda_15D01():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_15D01)
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
        "#00302Fおお……\x02",
    )

    CloseMessageWindow()

    #C0717
    ChrTalk(
        0x103,
        "#6P#00202Fロイドさん……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15DD0")

    #C0718
    ChrTalk(
        0x105,
        (
            "#6P#10402Fへえ……\x01",
            "まるで誂#2Rあつら#えたみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15E55")

    label("loc_15DD0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15E15")

    #C0719
    ChrTalk(
        0x109,
        "#6P#10100Fまるで誂#2Rあつら#えたみたい……\x02",
    )

    CloseMessageWindow()
    Jump("loc_15E55")

    label("loc_15E15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_15E55")

    #C0720
    ChrTalk(
        0x106,
        "#6P#10702Fまるで誂#2Rあつら#えたような……\x02",
    )

    CloseMessageWindow()

    label("loc_15E55")


    #C0721
    ChrTalk(
        0x101,
        (
            "#00004Fああ……\x01",
            "不思議と手に馴染むよ。\x02",
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
            "#00004F──シズクちゃん。\x01",
            "伝言、ありがとう。\x02\x03",

            "#00000Fここから先は、\x01",
            "どうか俺たちに任せてくれ。\x02\x03",

            "キーアの事も……\x01",
            "そしてアリオスさんの事も。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_15F61():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_15F61)
    Sleep(50)

    def lambda_15F71():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_15F71)
    Sleep(50)

    def lambda_15F81():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_15F81)

    def lambda_15F8E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_15F8E)

    #C0723
    ChrTalk(
        0xC,
        (
            "#11226F#11P#30W……はい………\x02\x03",

            "#11228Fお父さんはずっと……\x01",
            "悩んでいたんだと思います。\x02\x03",

            "お母さんのこと……わたしのこと……\x02\x03",

            "#11233F色々なことを考えているうちに\x01",
            "……後戻りが出来なくなって……\x02\x03",

            "#11227F………それで………グス………\x02",
        )
    )

    CloseMessageWindow()

    #C0724
    ChrTalk(
        0x101,
        (
            "#00002F大丈夫──\x01",
            "後戻りが出来ないなんて\x01",
            "そんな事があるもんか。\x02",
        )
    )

    CloseMessageWindow()

    #C0725
    ChrTalk(
        0x102,
        (
            "#12P#00104Fお父さんの事は\x01",
            "きっと連れ戻してみせるわ。\x02\x03",

            "#00100F特務支援課の名に賭けて。\x02",
        )
    )

    CloseMessageWindow()

    #C0726
    ChrTalk(
        0x104,
        (
            "#00306Fま、こんな可愛い一人娘を\x01",
            "泣かせるような不良オヤジは\x01",
            "一発ぶん殴ってやらねぇとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x103,
        (
            "#6P#00204F……ですね。\x02\x03",

            "#00202F首に縄を掛けてでも\x01",
            "連れて帰りましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0728
    ChrTalk(
        0xC,
        (
            "#11231F#11P#30W……ぐすっ……\x01",
            "…………はいっ………！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1644A")

    #C0729
    ChrTalk(
        0x10A,
        (
            "#6P#00606Fしかしマクレインを\x01",
            "連れ戻す話はともかく……\x02\x03",

            "#00601F大統領の関係者たちは\x01",
            "一体どこに行ったんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16557")

    label("loc_1644A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_164D2")

    #C0730
    ChrTalk(
        0x105,
        (
            "#6P#10406Fしかし《風の剣聖》を\x01",
            "連れ戻す話はともかく……\x02\x03",

            "#10401F大統領の関係者たちは\x01",
            "どこに行ったんだろうね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16557")

    label("loc_164D2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16557")

    #C0731
    ChrTalk(
        0x106,
        (
            "#6P#10706Fしかし《風の剣聖》を\x01",
            "連れ戻す話はともかく……\x02\x03",

            "#10708F大統領の関係者たちは\x01",
            "どこに行ったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16557")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_165A9")

    #C0732
    ChrTalk(
        0x109,
        (
            "#6P#10108Fやっぱりキーアちゃんも\x01",
            "居ないみたいですし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663E")

    label("loc_165A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_165F9")

    #C0733
    ChrTalk(
        0x106,
        (
            "#6P#10708Fやはりキーアちゃんも\x01",
            "居ないみたいですし……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1663E")

    label("loc_165F9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1663E")

    #C0734
    ChrTalk(
        0x105,
        (
            "#6P#10408Fやっぱりキーアも\x01",
            "居ないみたいだしね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1663E")


    #C0735
    ChrTalk(
        0x101,
        "#00006F#11Pそうだな……\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x102,
        (
            "#5P#00108F……伝言を残したという事は\x01",
            "ひょっとしてタワーには──\x02",
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
            "#00005F#11Pおっと……\x01",
            "（スピーカーモードにするか）\x02",
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
    SetChrName("主任の声")

    #A0738
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、ロイド君たち！\x02\x03",

            "直通エレベーターのセキュリティ、\x01",
            "やっと解除できたよ～！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0739
    AnonymousTalk(
        0x101,
        "#00002F本当ですか！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0740
    AnonymousTalk(
        0x102,
        "#00104Fよかった、これで……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("主任の声")

    #A0741
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ただ、どうも他のフロアには\x01",
            "ほとんど人が残っていないんだ。\x02\x03",

            "こちらのサーチから逃れて\x01",
            "隠れているとも思えないし。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0742
    AnonymousTalk(
        0x103,
        "#00201Fそれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0743
    AnonymousTalk(
        0x104,
        (
            "#00301Fおいおい、そんじゃあ\x01",
            "キー坊たちは一体どこに……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("主任の声")

    #A0744
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ただ一箇所……\x02\x03",

            "オルキスタワーの屋上に\x01",
            "“誰か”がいるみたいだね。\x02\x03",

            "あの白い人形と一緒に。\x07\x00\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A15")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0746
    AnonymousTalk(
        0x109,
        (
            "#10101F……エレベーターで屋上に\x01",
            "行くことは可能なんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16AD0")

    label("loc_16A15")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16A74")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0747
    AnonymousTalk(
        0x105,
        (
            "#10401F……エレベーターで屋上に\x01",
            "行くことは可能なのかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_16AD0")

    label("loc_16A74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_16AD0")
    SetMessageWindowPos(50, 30, -1, -1)

    #A0748
    AnonymousTalk(
        0x10A,
        (
            "#00601F……エレベーターで屋上に\x01",
            "行くことは可能なのですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_16AD0")

    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("主任の声")

    #A0749
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ああ、ロックは解除したから\x01",
            "そのまま上がれるはずだ。\x02\x03",

            "行くのであれば気をつけて！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0750
    AnonymousTalk(
        0x103,
        "#00203F了解です。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0751
    AnonymousTalk(
        0x101,
        "#00000Fそれでは失礼します。\x02",
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
        "#5P#00108F《結社》の博士か、それとも……\x02",
    )

    CloseMessageWindow()

    #C0753
    ChrTalk(
        0x104,
        (
            "#12P#00301F分からん……\x01",
            "行ってみるしかねぇだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0754
    ChrTalk(
        0x103,
        (
            "#6P#00203F近くにある直通エレベーターが\x01",
            "使用可能になっている筈です。\x02\x03",

            "#00201F必要なら１Ｆまで戻って\x01",
            "準備を整えておきましょう。\x02",
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
        "#11P#00007Fああ……！\x02",
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

    # Function_123_13E2F end

    def Function_124_16D89(): pass

    label("Function_124_16D89")

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

    # Function_124_16D89 end

    def Function_125_16DFE(): pass

    label("Function_125_16DFE")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_16E14():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16E14)
    WaitChrThread(0xFE, 1)

    def lambda_16E32():
        OP_95(0xFE, 163300, 0, 55200, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16E32)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_125_16DFE end

    def Function_126_16E53(): pass

    label("Function_126_16E53")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_16E69():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16E69)
    WaitChrThread(0xFE, 1)

    def lambda_16E87():
        OP_95(0xFE, 162000, 0, 54800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16E87)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_126_16E53 end

    def Function_127_16EA8(): pass

    label("Function_127_16EA8")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_16EBE():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16EBE)
    WaitChrThread(0xFE, 1)

    def lambda_16EDC():
        OP_95(0xFE, 162000, 0, 53600, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16EDC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_127_16EA8 end

    def Function_128_16EFD(): pass

    label("Function_128_16EFD")

    SetChrPos(0xFE, 156600, 0, 52000, 90)

    def lambda_16F13():
        OP_95(0xFE, 161000, 0, 52000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F13)
    WaitChrThread(0xFE, 1)

    def lambda_16F31():
        OP_95(0xFE, 163300, 0, 54000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F31)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_128_16EFD end

    def Function_129_16F52(): pass

    label("Function_129_16F52")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_16F68():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F68)
    WaitChrThread(0xFE, 1)

    def lambda_16F86():
        OP_95(0xFE, 161700, 0, 58130, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F86)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x1F4)
    Return()

    # Function_129_16F52 end

    def Function_130_16FA7(): pass

    label("Function_130_16FA7")

    SetChrPos(0xFE, 154000, 0, 60000, 90)

    def lambda_16FBD():
        OP_95(0xFE, 161300, 0, 60000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16FBD)
    WaitChrThread(0xFE, 1)

    def lambda_16FDB():
        OP_95(0xFE, 163100, 0, 58800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16FDB)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_130_16FA7 end

    def Function_131_16FFC(): pass

    label("Function_131_16FFC")


    def lambda_17001():
        OP_95(0xFE, 110200, 0, -110500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17001)

    def lambda_1701B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1701B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_16FFC end

    def Function_132_1702C(): pass

    label("Function_132_1702C")


    def lambda_17031():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17031)

    def lambda_1704B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1704B)
    WaitChrThread(0xFE, 1)

    def lambda_17060():
        OP_95(0xFE, 109600, 0, -109200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17060)
    WaitChrThread(0xFE, 1)

    def lambda_1707E():

        label("loc_1707E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_1707E")

    QueueWorkItem2(0xFE, 2, lambda_1707E)
    Return()

    # Function_132_1702C end

    def Function_133_1708C(): pass

    label("Function_133_1708C")


    def lambda_17091():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17091)

    def lambda_170AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_170AB)
    WaitChrThread(0xFE, 1)

    def lambda_170C0():
        OP_95(0xFE, 108600, 0, -111500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_170C0)
    WaitChrThread(0xFE, 1)

    def lambda_170DE():

        label("loc_170DE")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_170DE")

    QueueWorkItem2(0xFE, 2, lambda_170DE)
    Return()

    # Function_133_1708C end

    def Function_134_170EC(): pass

    label("Function_134_170EC")


    def lambda_170F1():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_170F1)

    def lambda_1710B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1710B)
    WaitChrThread(0xFE, 1)

    def lambda_17120():
        OP_95(0xFE, 109600, 0, -112200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17120)
    WaitChrThread(0xFE, 1)

    def lambda_1713E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1713E)
    Return()

    # Function_134_170EC end

    def Function_135_17147(): pass

    label("Function_135_17147")


    def lambda_1714C():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1714C)

    def lambda_17166():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17166)
    WaitChrThread(0xFE, 1)

    def lambda_1717B():
        OP_95(0xFE, 108000, 0, -109800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1717B)
    WaitChrThread(0xFE, 1)

    def lambda_17199():

        label("loc_17199")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_17199")

    QueueWorkItem2(0xFE, 2, lambda_17199)
    Return()

    # Function_135_17147 end

    def Function_136_171A7(): pass

    label("Function_136_171A7")


    def lambda_171AC():
        OP_95(0xFE, 110000, 0, -110500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_171AC)

    def lambda_171C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_171C6)
    WaitChrThread(0xFE, 1)

    def lambda_171DB():
        OP_95(0xFE, 107500, 0, -111300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_171DB)
    WaitChrThread(0xFE, 1)

    def lambda_171F9():

        label("loc_171F9")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_171F9")

    QueueWorkItem2(0xFE, 2, lambda_171F9)
    Return()

    # Function_136_171A7 end

    def Function_137_17207(): pass

    label("Function_137_17207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17414")
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
        "#00013Fやはりか――\x02",
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0x102,
        (
            "#00101F３器ともシャッターが\x01",
            "閉まっているわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0758
    ChrTalk(
        0x103,
        (
            "#00201Fビルの制御を奪われた以上、\x01",
            "エレベーターは使えないと\x01",
            "考えた方がよさそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x104,
        (
            "#00303Fなら、例えシャッターを\x01",
            "力づくでこじ開けたとしても\x01",
            "どうしようもねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0760
    ChrTalk(
        0x109,
        "#10107Fええ、非常階段に急ぎましょう！\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1C2, 5)
    EventEnd(0x5)
    Jump("loc_17469")

    label("loc_17414")

    EventBegin(0x1)

    #C0761
    ChrTalk(
        0x101,
        (
            "#00007Fエレベーターは使えない……\x01",
            "非常階段の方に向かうぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 109910, 0, -130740, 270)
    EventEnd(0x4)

    label("loc_17469")

    Return()

    # Function_137_17207 end

    def Function_138_1746A(): pass

    label("Function_138_1746A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_174C4")

    #A0762
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターは\x01",
            "他のフロアで使用中らしく、\x01",
            "止まる気配がない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_1779F")

    label("loc_174C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17730")
    SetChrName("")

    #A0763
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターのシャッターは\x01",
            "固く閉ざされている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0764
    ChrTalk(
        0x101,
        (
            "#00000Fそういえば、会議中は\x01",
            "手前のエレベーター以外は\x01",
            "使えないんだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x102,
        (
            "#00100Fええ、確か警備上の理由で\x01",
            "そういう事になっていたわね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_17656")

    #C0766
    ChrTalk(
        0x103,
        (
            "#00200F非常階段同様、\x01",
            "ここも導力ネットによって\x01",
            "制御・管理されているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0767
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そうらしいな。\x02\x03",

            "まあいい、移動する時は\x01",
            "手前のエレベーターを使おう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17728")

    label("loc_17656")


    #C0768
    ChrTalk(
        0x103,
        (
            "#00200Fちなみに、ロックの開閉は\x01",
            "導力ネットによって\x01",
            "制御・管理されているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0769
    ChrTalk(
        0x101,
        (
            "#00000Fああ、流石はオルキスターの\x01",
            "セキュリティってところだな。\x02\x03",

            "まあいい、移動する時は\x01",
            "手前のエレベーターを使おう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17728")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_1779F")

    label("loc_17730")

    SetChrName("")

    #A0770
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターのシャッターは\x01",
            "固く閉ざされている。\x02\x03",

            "会議中、このエレベーターは\x01",
            "使用できないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_1779F")

    TalkEnd(0xFF)
    Return()

    # Function_138_1746A end

    def Function_139_177A3(): pass

    label("Function_139_177A3")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_179CB")
    SetChrName("")

    #A0771
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "非常階段のシャッターは\x01",
            "固く閉ざされている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0772
    ChrTalk(
        0x101,
        "#00000Fこっちは３７階方面か。\x02",
    )

    CloseMessageWindow()

    #C0773
    ChrTalk(
        0x102,
        (
            "#00100Fええ、そして会議中は完全に\x01",
            "封鎖するという話だったわね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_END)), "loc_17911")

    #C0774
    ChrTalk(
        0x103,
        (
            "#00200Fエレベーター同様、\x01",
            "こちらも導力ネットで\x01",
            "制御されているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0x101,
        (
            "#00000F完璧なセキュリティは\x01",
            "あり得ない――だったか。\x02\x03",

            "万が一の事態も\x01",
            "想定しておかないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179C3")

    label("loc_17911")


    #C0776
    ChrTalk(
        0x103,
        (
            "#00200Fシャッターのロックは\x01",
            "導力ネットによって\x01",
            "制御されているようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0777
    ChrTalk(
        0x101,
        (
            "#00000F完璧なセキュリティは\x01",
            "あり得ない――だったか。\x02\x03",

            "万が一の事態も\x01",
            "想定しておかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_179C3")

    SetScenarioFlags(0x1C2, 3)
    Jump("loc_17A34")

    label("loc_179CB")

    SetChrName("")

    #A0778
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "非常階段のシャッターは\x01",
            "固く閉ざされている。\x02\x03",

            "会議中、この先の階へは\x01",
            "行き来できないようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_17A34")

    TalkEnd(0xFF)
    Return()

    # Function_139_177A3 end

    def Function_140_17A38(): pass

    label("Function_140_17A38")

    EventBegin(0x1)

    #C0779
    ChrTalk(
        0x101,
        (
            "#00001Fおっと、左翼の最奥の部屋に\x01",
            "大統領がいるんだったな。\x02\x03",

            "宰相の所に行く前に\x01",
            "まずは大統領を訪ねよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 4370, 0, -1430, 270)
    EventEnd(0x4)
    Return()

    # Function_140_17A38 end

    SaveToFile()

Try(main)
