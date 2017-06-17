from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1540.bin",                # FileName
        "c1540",                    # MapName
        "c1540",                    # Location
        0x00AF,                     # MapIndex
        "ed7151",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 175, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1540",                  # 0
        "雷克特书记官",           # 1
        "穆拉少校",               # 2
        "尤莉亚准校",             # 3
        "雾香辅佐官",             # 4
        "共和国军官",             # 5
        "帝国军官",               # 6
        "共和国军官",             # 7
        "帝国军官",               # 8
        "王室亲卫队队员",         # 9
        "公国护卫官",             # 10
        "公国护卫官",             # 11
        "总管",                   # 12
        "总管",                   # 13
        "女仆",                   # 14
        "女仆",                   # 15
        "亚里欧斯",               # 16
        "市政府职员",             # 17
        "皮埃尔副局长",           # 18
        "警官",                   # 19
        "警官",                   # 20
        "警官",                   # 21
        "迪塔市长",               # 22
        "奥斯本宰相",             # 23
        "奥利维特皇子",           # 24
        "科洛蒂娅公主",           # 25
        "阿尔伯特大公",           # 26
        "洛克史密斯总统",         # 27
        "麦克道尔议长",           # 28
        "伊安律师",               # 29
        "达德利搜查官",           # 30
        "帝国恐怖分子",           # 31
        "帝国恐怖分子",           # 32
        "帝国恐怖分子",           # 33
        "帝国恐怖分子",           # 34
        "帝国恐怖分子",           # 35
        "帝国恐怖分子",           # 36
        "帝国恐怖分子",           # 37
        "帝国恐怖分子",           # 38
        "共和国恐怖分子",         # 39
        "共和国恐怖分子",         # 40
        "共和国恐怖分子",         # 41
        "共和国恐怖分子",         # 42
        "共和国恐怖分子",         # 43
        "共和国恐怖分子",         # 44
        "共和国恐怖分子",         # 45
        "共和国恐怖分子",         # 46
        "警官",                   # 47
        "警官",                   # 48
        "警官",                   # 49
        "警官",                   # 50
        "警备队员",               # 51
        "警备队员",               # 52
        "模型",                   # 53
        "格蕾丝",                 # 54
        "雷因兹",                 # 55
        "记者",                   # 56
        "记者",                   # 57
        "记者",                   # 58
        "记者",                   # 59
        "记者",                   # 60
        "飞艇",                   # 61
        "飞艇",                   # 62
        "椅子",                   # 63
        "椅子",                   # 64
        "笔记本型终端",           # 65
        "剧情用魔兽",             # 66
        "剧情用魔兽",             # 67
        "剧情用魔兽",             # 68
        "SE控制",                 # 69
        "bc1560",                 # 70
    ))

    ATBonus("ATBonus_A70", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_B50", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_B54", 5, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B58", 11, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_B5C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B60", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B64", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B68", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B6C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_B30", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_B34", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_B38", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_B3C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_B40", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_B44", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_B48", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_B4C", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_B70", 0x000A, 3, 6, 45, 3, 3, 30, 0, "bc1560", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84101.dat", "ms84301.dat", "ms84201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_B50", "MonsterBattlePostion_B30", "ed7544", "ed7453", "ATBonus_A70"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch11300.itc",                   # 01
        "chr/ch11200.itc",                   # 02
        "chr/ch13300.itc",                   # 03
        "chr/ch12400.itc",                   # 04
        "chr/ch41200.itc",                   # 05
        "chr/ch41000.itc",                   # 06
        "chr/ch41600.itc",                   # 07
        "chr/ch28600.itc",                   # 08
        "chr/ch25900.itc",                   # 09
        "chr/ch25600.itc",                   # 0A
        "chr/ch02400.itc",                   # 0B
        "chr/ch25800.itc",                   # 0C
        "chr/ch27800.itc",                   # 0D
        "chr/ch28200.itc",                   # 0E
        "chr/ch06400.itc",                   # 0F
        "chr/ch13302.itc",                   # 10
        "chr/ch00000.itc",                   # 11
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

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   4,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(171350,  0,       74290,   270,  453,  0x0, 0,   1,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(174860,  0,       72669,   270,  453,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(85529,   0,       80650,   135,  453,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(88940,   0,       80209,   135,  453,  0x0, 0,   5,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(171059,  0,       78610,   270,  453,  0x0, 0,   6,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(87379,   0,       80379,   135,  389,  0x0, 0,   5,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(172130,  0,       77980,   270,  389,  0x0, 0,   6,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(175050,  0,       71419,   271,  389,  0x0, 0,   7,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(88099,   0,       72809,   89,   389,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(88260,   0,       71559,   89,   389,  0x0, 0,   8,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(170720,  0,       82220,   270,  389,  0x0, 0,   9,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52180,  0,       124000,  180,  389,  0x0, 0,   12,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(173529,  0,       74540,   0,    389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-49459,  0,       112459,  89,   389,  0x0, 0,   10,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(86529,   0,       80650,   135,  389,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-52000,  0,       120730,  0,    389,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-41799,  0,       128199,  0,    389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
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
    DeclNpc(0,       0,       0,       0,    236,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 28,  86.02999877929688,     83.37000274658203,     -1.0,                  5184.0,                [0.0833333358168602,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -7.169166564941406,    -6.947500228881836,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 29,  36.47999954223633,     0.0,                   -1.0,                  56.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -12.15999984741211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 133, 9.699999809265137,     3.5,                   -1.0,                  9.0,                   [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -3.2333333492279053,   -1.75,                 0.20000001788139343,   1.0])
    DeclEvent(0x0000, 0, 134, 91.69999694824219,     76.5,                  -1.0,                  9.0,                   [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -45.849998474121094,   -25.5,                 0.20000001788139343,   1.0])

    DeclActor(80610,   0,       2930,    1000,    80610,   1500,    2930,    0x007C, 0,  132, 0x0000)
    DeclActor(86730,   0,       3250,    1000,    86730,   1500,    3250,    0x007C, 0,  132, 0x0000)

    ChipFrameInfo(3540, 0)                                       # 0

    ScpFunction((
        "Function_0_DD4",          # 00, 0
        "Function_1_E84",          # 01, 1
        "Function_2_ED7",          # 02, 2
        "Function_3_130D",         # 03, 3
        "Function_4_150C",         # 04, 4
        "Function_5_15A3",         # 05, 5
        "Function_6_1651",         # 06, 6
        "Function_7_185A",         # 07, 7
        "Function_8_18C4",         # 08, 8
        "Function_9_1B1F",         # 09, 9
        "Function_10_1BA4",        # 0A, 10
        "Function_11_1E5B",        # 0B, 11
        "Function_12_1FCE",        # 0C, 12
        "Function_13_2027",        # 0D, 13
        "Function_14_20A1",        # 0E, 14
        "Function_15_211E",        # 0F, 15
        "Function_16_21E6",        # 10, 16
        "Function_17_2204",        # 11, 17
        "Function_18_2280",        # 12, 18
        "Function_19_22FB",        # 13, 19
        "Function_20_269B",        # 14, 20
        "Function_21_271A",        # 15, 21
        "Function_22_2843",        # 16, 22
        "Function_23_28AF",        # 17, 23
        "Function_24_2971",        # 18, 24
        "Function_25_29CC",        # 19, 25
        "Function_26_3334",        # 1A, 26
        "Function_27_3989",        # 1B, 27
        "Function_28_3FD6",        # 1C, 28
        "Function_29_450A",        # 1D, 29
        "Function_30_491A",        # 1E, 30
        "Function_31_4921",        # 1F, 31
        "Function_32_494A",        # 20, 32
        "Function_33_56B7",        # 21, 33
        "Function_34_574E",        # 22, 34
        "Function_35_579F",        # 23, 35
        "Function_36_57DF",        # 24, 36
        "Function_37_64E0",        # 25, 37
        "Function_38_673D",        # 26, 38
        "Function_39_699E",        # 27, 39
        "Function_40_6DB7",        # 28, 40
        "Function_41_6E70",        # 29, 41
        "Function_42_7E74",        # 2A, 42
        "Function_43_89F7",        # 2B, 43
        "Function_44_9EB0",        # 2C, 44
        "Function_45_9F7D",        # 2D, 45
        "Function_46_A04A",        # 2E, 46
        "Function_47_A0A5",        # 2F, 47
        "Function_48_A121",        # 30, 48
        "Function_49_A17F",        # 31, 49
        "Function_50_A24C",        # 32, 50
        "Function_51_A31C",        # 33, 51
        "Function_52_A396",        # 34, 52
        "Function_53_A409",        # 35, 53
        "Function_54_A47C",        # 36, 54
        "Function_55_A4E8",        # 37, 55
        "Function_56_A53D",        # 38, 56
        "Function_57_A592",        # 39, 57
        "Function_58_A605",        # 3A, 58
        "Function_59_A766",        # 3B, 59
        "Function_60_C0CD",        # 3C, 60
        "Function_61_C15E",        # 3D, 61
        "Function_62_C1C1",        # 3E, 62
        "Function_63_C271",        # 3F, 63
        "Function_64_C473",        # 40, 64
        "Function_65_C513",        # 41, 65
        "Function_66_C54A",        # 42, 66
        "Function_67_C5C5",        # 43, 67
        "Function_68_C5FC",        # 44, 68
        "Function_69_C677",        # 45, 69
        "Function_70_C8BB",        # 46, 70
        "Function_71_C976",        # 47, 71
        "Function_72_CBA2",        # 48, 72
        "Function_73_CBE9",        # 49, 73
        "Function_74_CC32",        # 4A, 74
        "Function_75_CC75",        # 4B, 75
        "Function_76_CCCF",        # 4C, 76
        "Function_77_CE30",        # 4D, 77
        "Function_78_D0E2",        # 4E, 78
        "Function_79_D1EF",        # 4F, 79
        "Function_80_D24E",        # 50, 80
        "Function_81_D295",        # 51, 81
        "Function_82_D4C3",        # 52, 82
        "Function_83_D593",        # 53, 83
        "Function_84_D613",        # 54, 84
        "Function_85_D693",        # 55, 85
        "Function_86_D713",        # 56, 86
        "Function_87_D777",        # 57, 87
        "Function_88_D7DB",        # 58, 88
        "Function_89_D831",        # 59, 89
        "Function_90_D8A2",        # 5A, 90
        "Function_91_D8C1",        # 5B, 91
        "Function_92_D8E0",        # 5C, 92
        "Function_93_D8FF",        # 5D, 93
        "Function_94_D91E",        # 5E, 94
        "Function_95_D93D",        # 5F, 95
        "Function_96_D95C",        # 60, 96
        "Function_97_D992",        # 61, 97
        "Function_98_D9E6",        # 62, 98
        "Function_99_DA3A",        # 63, 99
        "Function_100_DA56",       # 64, 100
        "Function_101_DBED",       # 65, 101
        "Function_102_DD7E",       # 66, 102
        "Function_103_DDCE",       # 67, 103
        "Function_104_DE11",       # 68, 104
        "Function_105_DE6D",       # 69, 105
        "Function_106_DE94",       # 6A, 106
        "Function_107_DEBB",       # 6B, 107
        "Function_108_DEE2",       # 6C, 108
        "Function_109_DF09",       # 6D, 109
        "Function_110_DF67",       # 6E, 110
        "Function_111_DFBA",       # 6F, 111
        "Function_112_E021",       # 70, 112
        "Function_113_E078",       # 71, 113
        "Function_114_E0E3",       # 72, 114
        "Function_115_E13A",       # 73, 115
        "Function_116_E15C",       # 74, 116
        "Function_117_E1A3",       # 75, 117
        "Function_118_E1E0",       # 76, 118
        "Function_119_E207",       # 77, 119
        "Function_120_E22E",       # 78, 120
        "Function_121_E255",       # 79, 121
        "Function_122_E27C",       # 7A, 122
        "Function_123_E299",       # 7B, 123
        "Function_124_E2B3",       # 7C, 124
        "Function_125_E2E5",       # 7D, 125
        "Function_126_F9D0",       # 7E, 126
        "Function_127_F9EB",       # 7F, 127
        "Function_128_FA07",       # 80, 128
        "Function_129_10264",      # 81, 129
        "Function_130_11604",      # 82, 130
        "Function_131_1161C",      # 83, 131
        "Function_132_11695",      # 84, 132
        "Function_133_11903",      # 85, 133
        "Function_134_11975",      # 86, 134
        "Function_135_119D8",      # 87, 135
    ))


    def Function_0_DD4(): pass

    label("Function_0_DD4")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_E0C"),
        (1, "loc_E18"),
        (2, "loc_E24"),
        (3, "loc_E30"),
        (4, "loc_E3C"),
        (5, "loc_E48"),
        (6, "loc_E54"),
        (SWITCH_DEFAULT, "loc_E60"),
    )


    label("loc_E0C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E18")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E24")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E30")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E3C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E48")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E54")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E60")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E83")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_E6C")

    label("loc_E83")

    Return()

    # Function_0_DD4 end

    def Function_1_E84(): pass

    label("Function_1_E84")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_ED6")
    OP_95(0xFE, -4530, 0, -2520, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x1F4)
    Sleep(300)
    OP_95(0xFE, 20720, 0, -2520, 2000, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_E84")

    label("loc_ED6")

    Return()

    # Function_1_E84 end

    def Function_2_ED7(): pass

    label("Function_2_ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 4)), scpexpr(EXPR_END)), "loc_EE5")
    Jump("loc_11BA")

    label("loc_EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1068")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 11220, 0, 2300, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 7990, 0, 2300, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 20720, 0, -2520, 270)
    BeginChrThread(0x1C, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F6C")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xD, 75530, 0, 2000, 0)
    SetChrPos(0xC, 73730, 0, 2000, 0)

    label("loc_F6C")

    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 170720, 0, 82220, 270)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, 173530, 0, 74540, 0)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0xB, 87380, 0, 84160, 180)
    SetChrChipByIndex(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrPos(0x17, 89160, 0, 85000, 0)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x19, -41800, 0, 128199, 0)
    SetChrFlags(0x19, 0x10)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -52180, 0, 124000, 180)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -49460, 0, 112460, 89)
    SetChrFlags(0x16, 0x10)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -52000, 0, 120730, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104D")
    Event(0, 26)

    label("loc_104D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1063")
    Event(0, 27)

    label("loc_1063")

    Jump("loc_11BA")

    label("loc_1068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_11BA")
    ClearChrFlags(0x1A, 0x80)
    SetChrPos(0x1A, 11220, 0, 2300, 180)
    ClearChrFlags(0x1B, 0x80)
    SetChrPos(0x1B, 7990, 0, 2300, 180)
    ClearChrFlags(0x1C, 0x80)
    SetChrPos(0x1C, 20720, 0, -2520, 270)
    BeginChrThread(0x1C, 0, 0, 1)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x40)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 174860, 0, 72670, 270)
    SetChrPos(0x10, 175050, 0, 71420, 271)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x40)
    SetChrPos(0x9, 171350, 0, 74290, 270)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x40)
    SetChrPos(0xD, 171060, 0, 78610, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 172130, 0, 77980, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 84390, 150, 84160, 180)
    SetChrChipByIndex(0xB, 0x10)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x40)
    SetChrPos(0xC, 88940, 0, 80210, 135)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 87380, 0, 80380, 135)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 88100, 0, 72810, 89)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 88260, 0, 71560, 89)

    label("loc_11BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11E4")
    ClearScenarioFlags(0x25, 1)
    Call(0, 30)

    label("loc_11E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_11F8")
    ClearScenarioFlags(0x22, 0)
    Event(0, 32)
    Jump("loc_12C7")

    label("loc_11F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_120F")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 36)
    Jump("loc_12C7")

    label("loc_120F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1226")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 39)
    Jump("loc_12C7")

    label("loc_1226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_123D")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 0)
    Event(0, 41)
    Jump("loc_12C7")

    label("loc_123D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_1251")
    ClearScenarioFlags(0x22, 4)
    Event(0, 42)
    Jump("loc_12C7")

    label("loc_1251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_1265")
    ClearScenarioFlags(0x22, 5)
    Event(0, 43)
    Jump("loc_12C7")

    label("loc_1265")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_1279")
    ClearScenarioFlags(0x22, 6)
    Event(0, 58)
    Jump("loc_12C7")

    label("loc_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_128D")
    ClearScenarioFlags(0x22, 7)
    Event(0, 59)
    Jump("loc_12C7")

    label("loc_128D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_12A1")
    ClearScenarioFlags(0x23, 0)
    Event(0, 125)
    Jump("loc_12C7")

    label("loc_12A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_12B8")
    ClearScenarioFlags(0x23, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 129)
    Jump("loc_12C7")

    label("loc_12B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_12C7")
    ClearScenarioFlags(0x23, 2)
    Event(0, 128)

    label("loc_12C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12E5")
    Event(0, 37)

    label("loc_12E5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_130C")
    Event(0, 38)

    label("loc_130C")

    Return()

    # Function_2_ED7 end

    def Function_3_130D(): pass

    label("Function_3_130D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1322")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_1322")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1336")
    VolumeBGM(0x46, 0xC8)

    label("loc_1336")

    OP_10(0x13, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_134D")
    OP_10(0x13, 0x1)
    OP_10(0x3, 0x0)

    label("loc_134D")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136A")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_137D")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_137D")

    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A9")
    ModifyEventFlags(1, 2, 0x80)
    ModifyEventFlags(1, 3, 0x80)
    OP_1B(0xD, 0x0, 0x87)
    Jump("loc_13AE")

    label("loc_13A9")

    OP_1B(0xD, 0xFF, 0xFFFF)

    label("loc_13AE")

    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFrame(0xFF, "paper", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1423")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1437")
    ClearMapObjFlags(0xE, 0x4)

    label("loc_1437")

    ClearMapObjFlags(0x9, 0x10)
    ClearMapObjFlags(0xA, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 5)), scpexpr(EXPR_END)), "loc_1464")
    ClearMapObjFlags(0x8, 0x10)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)

    label("loc_1464")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_END)), "loc_148B")
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x10)
    ClearMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0xD, 0x4)

    label("loc_148B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_14D0")
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)
    Sound(128, 1, 50, 0)

    label("loc_14D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_150B")
    OP_7D(0xD2, 0xD2, 0xE6, 0x0, 0x0)
    SetMapObjFrame(0xFF, "wlight_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "ylight_add", 0x0, 0x1)

    label("loc_150B")

    Return()

    # Function_3_130D end

    def Function_4_150C(): pass

    label("Function_4_150C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1554")

    #C0001
    ChrTalk(
        0xFE,
        (
            "正式会议的进程已经过半……\x01",
            "我们必须要坚持到底啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_159F")

    label("loc_1554")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_159F")

    #C0002
    ChrTalk(
        0xFE,
        "正式会议正在进行中。\x02",
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        "你们要想看里面的情况就去回廊室吧。\x02",
    )

    CloseMessageWindow()

    label("loc_159F")

    TalkEnd(0xFE)
    Return()

    # Function_4_150C end

    def Function_5_15A3(): pass

    label("Function_5_15A3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_15E8")

    #C0004
    ChrTalk(
        0xFE,
        (
            "工作人员\x01",
            "正在布置\x01",
            "会场。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        "请各位自由通行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_164D")

    label("loc_15E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_164D")

    #C0006
    ChrTalk(
        0xFE,
        (
            "会议前半程的结束时间\x01",
            "定于１５：００。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "但根据具体情况，\x01",
            "时间多少会有一些上下浮动。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164D")

    TalkEnd(0xFE)
    Return()

    # Function_5_15A3 end

    def Function_6_1651(): pass

    label("Function_6_1651")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1749")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16EE")

    #C0008
    ChrTalk(
        0xFE,
        (
            "暂时还没有发现恐怖分子的\x01",
            "行动迹象。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "虽然我认为他们\x01",
            "不可能突破这个\x01",
            "滴水不漏的警戒系统……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "但直到最后都不能松懈。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1744")

    label("loc_16EE")


    #C0011
    ChrTalk(
        0xFE,
        (
            "虽然我认为他们\x01",
            "不可能突破这个\x01",
            "滴水不漏的警戒系统……\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        "但直到最后都不能松懈。\x02",
    )

    CloseMessageWindow()

    label("loc_1744")

    Jump("loc_1856")

    label("loc_1749")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1856")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E9")

    #C0013
    ChrTalk(
        0xFE,
        "会议终于开始了呢。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "不知恐怖分子的\x01",
            "目标到底是什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "总之，我们只要遵从\x01",
            "对策室的指示，\x01",
            "完成上级交给我们的任务就行了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1856")

    label("loc_17E9")


    #C0016
    ChrTalk(
        0xFE,
        (
            "不知恐怖分子的\x01",
            "目标到底是什么……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "总之，我们只要遵从\x01",
            "对策室的指示，\x01",
            "完成上级交给我们的任务就行了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1856")

    TalkEnd(0xFE)
    Return()

    # Function_6_1651 end

    def Function_7_185A(): pass

    label("Function_7_185A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186F")
    Call(0, 8)
    Jump("loc_18C0")

    label("loc_186F")


    #C0018
    ChrTalk(
        0xA,
        (
            "#07103F这里就交给我们，\x01",
            "你们做好周边的警戒工作吧。\x02\x03",

            "#07100F愿女神保佑你们。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C0")

    TalkEnd(0xFE)
    Return()

    # Function_7_185A end

    def Function_8_18C4(): pass

    label("Function_8_18C4")

    OP_4B(0x10, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x10, 0x0, 0)
    TurnDirection(0xA, 0x0, 0)

    #C0019
    ChrTalk(
        0x10,
        "各位，辛苦了。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        (
            "#07102F哦，是支援科的各位啊。\x02\x03",

            "你们在帮忙巡查\x01",
            "会场周边的楼层吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00000F是的，总算是\x01",
            "设法挤进警备队伍了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，话说回来，\x01",
            "这个房间里的人似乎\x01",
            "全都实力高超呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#00300F毕竟几乎都是\x01",
            "将校级别的人物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        (
            "#00200F是的，光靠这里的各位，\x01",
            "应该就足以应对各种重大事件了。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#10109F嗯嗯，而且我还听说，\x01",
            "尤莉亚准校的剑术\x01",
            "既优美又高超！\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "#07104F呵呵，过奖了，我受之有愧。\x02\x03",

            "#07100F……总之，\x01",
            "不管出现什么人，\x01",
            "我都不会让他们动殿下分毫的。\x02\x03",

            "这里就交给我们，\x01",
            "你们做好周边的警戒工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#00100F好的，明白了。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x10, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_93(0x10, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    SetScenarioFlags(0x1C3, 0)
    Call(0, 31)
    Return()

    # Function_8_18C4 end

    def Function_9_1B1F(): pass

    label("Function_9_1B1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B34")
    Call(0, 8)
    Jump("loc_1BA0")

    label("loc_1B34")


    #C0028
    ChrTalk(
        0xFE,
        (
            "不管发生什么事，\x01",
            "我们王室亲卫队都会保护科洛蒂娅殿下的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "会场就不用各位担心了，\x01",
            "请大家继续巡逻吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BA0")

    TalkEnd(0xFE)
    Return()

    # Function_9_1B1F end

    def Function_10_1BA4(): pass

    label("Function_10_1BA4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DE0")

    #C0030
    ChrTalk(
        0x101,
        "#00000F您辛苦了，穆拉少校。\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        "#00100F有什么异常吗？\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "#07302F啊，是你们。\x02\x03",

            "#07303F唔，虽然不能麻痹大意，\x01",
            "但到目前为止都还没什么问题。\x02\x03",

            "会议似乎也进行得很顺利，\x01",
            "各位首脑都没有发表激烈言辞。\x02\x03",

            "#07308F如果能就此顺利结束，\x01",
            "皇子肩上的重担也可以减轻一些……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        "#10105F穆拉少校……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        "#00200F看样子，似乎有不少内情呢。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x9,
        (
            "#07302F呵呵，算是吧。\x01",
            "话虽如此，其实一切都是\x01",
            "那家伙自己种下的恶果……\x02\x03",

            "#07303F唔，我说的似乎太多了。\x02\x03",

            "总而言之，我现在该做的事情\x01",
            "只有认真履行护卫的职责。\x02\x03",

            "#07300F你们也努力做好\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        "#00000F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 2)
    Call(0, 31)
    Jump("loc_1E57")

    label("loc_1DE0")


    #C0037
    ChrTalk(
        0x9,
        (
            "#07303F身为武官，只能在此旁观\x01",
            "会议的情况……不过，我会认真\x01",
            "履行护卫的职责。\x02\x03",

            "#07300F你们也努力做好\x01",
            "自己的工作吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E57")

    TalkEnd(0xFE)
    Return()

    # Function_10_1BA4 end

    def Function_11_1E5B(): pass

    label("Function_11_1E5B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_1E6C")
    Jump("loc_1FCA")

    label("loc_1E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_1FCA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F7C")

    #C0038
    ChrTalk(
        0xFE,
        (
            "唔，你们就是负责巡逻的\x01",
            "特别任务支援科吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "……工作辛苦了。\x01",
            "如你们所见，\x01",
            "这里没有任何异常。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "如果听明白了，就不要\x01",
            "在房间里乱转。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x101,
        "#00001F是、是的……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        "#00203F（该怎么说呢，真是直接啊。）\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#00306F（是啊，完全不给面子。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1FCA")

    label("loc_1F7C")


    #C0044
    ChrTalk(
        0xFE,
        (
            "如你们所见，\x01",
            "这里没有任何异常。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "如果听明白了，就不要\x01",
            "在房间里乱转。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FCA")

    TalkEnd(0xFE)
    Return()

    # Function_11_1E5B end

    def Function_12_1FCE(): pass

    label("Function_12_1FCE")

    TalkBegin(0xFE)

    #C0046
    ChrTalk(
        0xFE,
        (
            "……如果在此造成响动，\x01",
            "声音就会传到会场里。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "所以在这里请务必\x01",
            "保持安静。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1FCE end

    def Function_13_2027(): pass

    label("Function_13_2027")

    TalkBegin(0xFE)

    #C0048
    ChrTalk(
        0xFE,
        (
            "亚里欧斯先生好像\x01",
            "正在对面的休息室里\x01",
            "和总统的辅佐官说话。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "看样子，他们应该彼此认识，\x01",
            "到底会是什么关系呢？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_2027 end

    def Function_14_20A1(): pass

    label("Function_14_20A1")

    TalkBegin(0xFE)

    #C0050
    ChrTalk(
        0xFE,
        (
            "这里是\x01",
            "帝国和王国的\x01",
            "随行人员休息室。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "没错，也就是说，\x01",
            "尤莉亚准校刚才就在这里！\x01",
            "光是想想，就要尖叫出来了呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_14_20A1 end

    def Function_15_211E(): pass

    label("Function_15_211E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_212F")
    Jump("loc_21E2")

    label("loc_212F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_21E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_214E")
    TalkEnd(0xFE)
    Call(0, 25)
    Return()

    label("loc_214E")


    #C0052
    ChrTalk(
        0xB,
        (
            "#12004F虽然我想你们可能有话要说……\x01",
            "不过我们现在还是\x01",
            "一起静观事态发展吧。\x02\x03",

            "#12000F毕竟从警戒这层意义上来说，\x01",
            "我跟你们的立场\x01",
            "并没有多大区别呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E2")

    TalkEnd(0xFE)
    Return()

    # Function_15_211E end

    def Function_16_21E6(): pass

    label("Function_16_21E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_21F7")
    Jump("loc_2200")

    label("loc_21F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_2200")

    label("loc_2200")

    TalkEnd(0xFE)
    Return()

    # Function_16_21E6 end

    def Function_17_2204(): pass

    label("Function_17_2204")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2215")
    Jump("loc_227C")

    label("loc_2215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_227C")

    #C0053
    ChrTalk(
        0xFE,
        (
            "唔，你们就是负责巡逻的\x01",
            "特别任务支援科吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "工作辛苦了。\x01",
            "如果有什么事，请随时和我说。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227C")

    TalkEnd(0xFE)
    Return()

    # Function_17_2204 end

    def Function_18_2280(): pass

    label("Function_18_2280")

    TalkBegin(0xFE)

    #C0055
    ChrTalk(
        0xFE,
        "看来会议进行得很顺利呢。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "这里和共和国议会不同，\x01",
            "并没有穷追猛打的在野党势力，\x01",
            "总统阁下应该也感觉很轻松吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2280 end

    def Function_19_22FB(): pass

    label("Function_19_22FB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_25B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_247C")

    #C0057
    ChrTalk(
        0xFE,
        "你们几位是特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "阿尔伯特大公阁下昨天\x01",
            "承蒙各位照顾了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x101,
        (
            "#00000F哪里，承蒙照顾的\x01",
            "是我们才对。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#00100F是啊，大公阁下的医疗知识\x01",
            "真的帮了我们很大的忙。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "哈哈，大公阁下的\x01",
            "医术确实\x01",
            "非常优秀呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "另外，\x01",
            "阁下似乎很\x01",
            "赏识各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "能够与你们见面，\x01",
            "我感到非常高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        "#00302F哈哈，多谢夸奖。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x109,
        "#10100F非常感谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C3, 3)
    Jump("loc_25AF")

    label("loc_247C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_255F")

    #C0066
    ChrTalk(
        0xFE,
        (
            "说起来，听说有出现\x01",
            "恐怖分子的\x01",
            "可能呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "不过，在这种国际会议中，\x01",
            "这种情况通常也是在预想范围内的……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "毕竟无论发生什么情况，\x01",
            "都不能让各位首脑陷入危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "我们都要打起精神，\x01",
            "做好自己的分内之事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_25AF")

    label("loc_255F")


    #C0070
    ChrTalk(
        0xFE,
        (
            "我们也听说了\x01",
            "恐怖分子的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "我们都要打起精神，\x01",
            "做好自己的分内之事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25AF")

    Jump("loc_2697")

    label("loc_25B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2647")

    #C0072
    ChrTalk(
        0xFE,
        (
            "各位是特别任务支援科的成员吧？\x01",
            "巡逻辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "我们也听说了\x01",
            "恐怖分子的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "我们都要打起精神，\x01",
            "做好自己的分内之事。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2697")

    label("loc_2647")


    #C0075
    ChrTalk(
        0xFE,
        (
            "我们也听说了\x01",
            "恐怖分子的消息。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "我们都要打起精神，\x01",
            "做好自己的分内之事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2697")

    TalkEnd(0xFE)
    Return()

    # Function_19_22FB end

    def Function_20_269B(): pass

    label("Function_20_269B")

    TalkBegin(0xFE)

    #C0077
    ChrTalk(
        0xFE,
        (
            "这次的通商会议\x01",
            "对我们雷米菲利亚\x01",
            "也非常有意义。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "为了祖国更进一步的发展，\x01",
            "我非常希望这次会议\x01",
            "能取得积极的成果。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_269B end

    def Function_21_271A(): pass

    label("Function_21_271A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 1)), scpexpr(EXPR_END)), "loc_2836")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F4")

    #C0079
    ChrTalk(
        0xFE,
        "唔，这风景真是壮观啊。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "恐怖分子\x01",
            "应该不可能\x01",
            "从天而降吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xFE)

    #C0081
    ChrTalk(
        0xFE,
        (
            "……哈哈，应该不会吧，\x01",
            "怎么会有那种事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        "#00006F（……看他的背影，好像有点紧张啊。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2831")

    label("loc_27F4")


    #C0083
    ChrTalk(
        0xFE,
        (
            "哈哈，不可能吧……\x01",
            "我大概是有点累了，都开始胡思乱想了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2831")

    Jump("loc_283F")

    label("loc_2836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x142, 0)), scpexpr(EXPR_END)), "loc_283F")

    label("loc_283F")

    TalkEnd(0xFE)
    Return()

    # Function_21_271A end

    def Function_22_2843(): pass

    label("Function_22_2843")

    TalkBegin(0xFE)

    #C0084
    ChrTalk(
        0xFE,
        (
            "好了，接下来要\x01",
            "检修这个话筒……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "唔，一想到各位首脑\x01",
            "直到刚才还坐在这里，\x01",
            "就觉得有点紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2843 end

    def Function_23_28AF(): pass

    label("Function_23_28AF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_294C")

    #C0086
    ChrTalk(
        0xFE,
        (
            "（擦拭）……\x01",
            "嘿哟，嘿哟……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x0, 500)
    Sleep(300)

    #C0087
    ChrTalk(
        0xFE,
        (
            "在后半程会议中，\x01",
            "也一定得让大家\x01",
            "在这个房间里待得舒适。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        "所以我正在用心打扫！\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x59, 0x0)
    SetScenarioFlags(0x0, 6)
    Jump("loc_296D")

    label("loc_294C")


    #C0089
    ChrTalk(
        0xFE,
        (
            "（擦拭）……\x01",
            "嘿哟，嘿哟……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_296D")

    TalkEnd(0xFE)
    Return()

    # Function_23_28AF end

    def Function_24_2971(): pass

    label("Function_24_2971")

    TalkBegin(0xFE)

    #C0090
    ChrTalk(
        0xFE,
        (
            "副局长先生为何在\x01",
            "那种地方愁眉苦脸？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        (
            "虽然不碍我的事，\x01",
            "但还是有点在意呢……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_2971 end

    def Function_25_29CC(): pass

    label("Function_25_29CC")

    EventBegin(0x0)
    Fade(500)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12000.itp")
    OP_4B(0xC, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_68(83610, 1300, 82220, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15400, 0)
    SetChrPos(0x101, 84860, 0, 82570, 0)
    SetChrPos(0x102, 83260, 0, 81870, 0)
    SetChrPos(0x103, 84860, 0, 81470, 0)
    SetChrPos(0x104, 83060, 0, 80570, 0)
    SetChrPos(0x109, 85060, 0, 80570, 0)
    SetChrPos(0x105, 83460, 0, 79870, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C7, 0)), scpexpr(EXPR_END)), "loc_2BCB")

    #C0092
    ChrTalk(
        0xB,
        (
            "#5P#12000F哎呀，是你们。\x01",
            "警戒工作还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#11P#00001F雾香小姐……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0094
    AnonymousTalk(
        0xB,
        (
            "看样子，你们又得到了\x01",
            "什么新的消息吧？\x02\x03",

            "听说还被请上了\x01",
            "『埃尔赛尤号』。\x02",
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
    Jump("loc_2F41")

    label("loc_2BCB")


    #C0095
    ChrTalk(
        0xB,
        (
            "#5P#12000F你们是……\x01",
            "呵呵，好久不见呢。\x02\x03",

            "警戒工作还顺利吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        "#00001F雾香小姐……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0097
    AnonymousTalk(
        0xB,
        (
            "对了，我这次的身份与\x01",
            "之前见面时有所不同，\x01",
            "重新做个自我介绍吧。\x02\x03",

            "卡尔瓦德共和国\x01",
            "总统辅佐官，\x01",
            "雾香·楼兰。\x02\x03",

            "除此之外，还有其它身份……\x01",
            "就不一一说明了。\x02",
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

    #C0098
    ChrTalk(
        0x101,
        "#00003F原来如此。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x102,
        (
            "#12P#00100F顺便一问，您以前所说的\x01",
            "演艺界制作人是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xB,
        (
            "#5P#12004F呵呵，\x01",
            "那的确也是我的身份之一。\x02\x03",

            "#12002F至于我的事务所，\x01",
            "也确实存在于共和国。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#00200F原来如此，\x01",
            "这方面的安排也毫无漏洞啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x105,
        (
            "#12P#10302F（呵呵，拥有多重身份的\x01",
            "  女间谍啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x104,
        (
            "#12P#00309F（嗯～充满神秘感的\x01",
            "  雾香小姐也很有魅力呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x109,
        (
            "#12P#10106F（前辈，这种发言\x01",
            "  未免太欠缺紧张感了吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xB,
        (
            "#5P#12002F呵呵，我脸上\x01",
            "沾着什么东西吗？\x02\x03",

            "#12004F对了对了，\x01",
            "说起来……\x02\x03",

            "#12000F听说你们昨天\x01",
            "被请上了『埃尔赛尤号』？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F41")

    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0106
    ChrTalk(
        0x102,
        "#12P#00105F咦……\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x103,
        "#00201F……看来您已经调查过了呢。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x104,
        "#12P#00306F呼，果然厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "#5P#12004F呵呵，不过这件事情\x01",
            "倒也没有什么大不了的。\x02\x03",

            "#12000F那么……\x01",
            "你们有没有听到什么有趣的事情？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x101,
        (
            "#00003F是的，虽然只是闲聊了一会。\x02\x03",

            "#00001F不过，有很多事情\x01",
            "无论如何也弄不明白呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xB,
        (
            "#5P#12004F呵呵，这样啊。\x02\x03",

            "说到这一点，\x01",
            "我们其实是一样的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0112
    ChrTalk(
        0x101,
        "#00005F哎……？\x02",
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xB,
        (
            "#5P#12000F举个例子。\x02\x03",

            "就算我真的在\x01",
            "策划一部剧本，\x01",
            "也无法保证它能实现。\x02\x03",

            "#12003F既然多方势力各怀不同目的，\x01",
            "那么不管是谁，都一样\x01",
            "面临着各种不确定的因素。\x02\x03",

            "今后会发生什么？\x01",
            "还是什么都不会发生？\x02\x03",

            "#12000F目前没有任何人\x01",
            "能预料得到。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00001F确实如此……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        "#12P#10304F呵呵，很有道理。\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xB,
        (
            "#5P#12004F总之，我想说的就是，\x01",
            "我会站在保护总统的立场上，\x01",
            "这一点毫无疑问。\x02\x03",

            "也就是说，从这层意义来看，\x01",
            "我与你们站在同一方。\x02\x03",

            "#12000F所以就让我们\x01",
            "一起静观事态的发展吧。\x02\x03",

            "除此之外的事情……\x01",
            "我现在还不打算说。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        (
            "#00001F原来如此……\x01",
            "对我们来说，已经很有参考价值了。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_4C(0xE, 0xFF)
    SetScenarioFlags(0x1C3, 4)
    Call(0, 31)
    EventEnd(0x5)
    Return()

    # Function_25_29CC end

    def Function_26_3334(): pass

    label("Function_26_3334")

    EventBegin(0x0)
    Fade(500)
    OP_68(86650, 1400, 75180, 0)
    MoveCamera(33, 8, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21450, 0)
    SetChrPos(0x101, 87120, 0, 70000, 0)
    SetChrPos(0x102, 86120, 0, 70000, 0)
    SetChrPos(0x103, 87120, 0, 68500, 0)
    SetChrPos(0x104, 86120, 0, 68500, 0)
    SetChrPos(0x109, 87120, 0, 67000, 0)
    SetChrPos(0x105, 86120, 0, 67000, 0)
    OP_4B(0x17, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0118
    ChrTalk(
        0x101,
        (
            "#11P#00005F#12P（那是……\x01",
            "  亚里欧斯先生和雾香小姐吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x102,
        (
            "#11P#00105F#12P（好像是的，他们\x01",
            "  到底在谈什么呢……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_0D()

    #C0120
    ChrTalk(
        0x17,
        (
            "#6P#01403F#11P你离开协会差不多有一年了吧？\x02\x03",

            "#01400F习惯新环境了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xB,
        (
            "#12004F#6P……还好吧。\x02\x03",

            "#12000F不过工作强度\x01",
            "远不是在协会时\x01",
            "可以相比的。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x17,
        "#6P#01403F#11P是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    #C0123
    ChrTalk(
        0xB,
        (
            "#12000F#6P……小滴\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x17,
        (
            "#6P#01402F#11P嗯，虽然有点太过听话了，\x01",
            "但一直都很开朗。\x02\x03",

            "#01404F最近还结识了很好的朋友，\x01",
            "变得爱笑了……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        (
            "#12004F#6P是吗，\x01",
            "那可真是不错呢。\x02\x03",

            "#12003F……………………………\x02\x03",

            "纱绫小姐……\x01",
            "已经去世五年了呢。\x02\x03",

            "#12000F我第一次见到她\x01",
            "还是在六年前……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x17,
        (
            "#11P#01404F六年前……没错。\x02\x03",

            "当时你正在大陆各地\x01",
            "漫无目的地漂泊，\x01",
            "在这座城市中，偶然认识了纱绫……\x02\x03",

            "纱绫硬把你\x01",
            "拉到了我们家，\x01",
            "让你住下。\x02\x03",

            "#01402F三年前，在利贝尔的\x01",
            "协会分部与你重逢时，\x01",
            "可真是大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "#12004F#6P呵呵，是啊。\x01",
            "人与人之间的缘分\x01",
            "真是不可思议。\x02\x03",

            "#12003F……那一宿一餐带给我的温暖，\x01",
            "我一生都不会忘记。\x02\x03",

            "#12001F不过，我直到最后也没能\x01",
            "回报那份恩情……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x17,
        (
            "#11P#01404F……哪里的话，\x01",
            "纱绫能听到你这么说，\x01",
            "就一定会很开心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(86040, 1500, 67910, 0)
    MoveCamera(46, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15440, 0)
    OP_4C(0x17, 0xFF)
    OP_0D()

    #C0129
    ChrTalk(
        0x101,
        (
            "#00005F#11P（……看样子，在雾香小姐\x01",
            "  加入游击士协会之前，\x01",
            "  他们两个就已经认识了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        (
            "#00108F#12P（是啊，\x01",
            "  不过我觉得继续偷听\x01",
            "  下去就不太好了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#11P#00203F（嗯，在打扰到他们之前，\x01",
            "  还是赶快离开吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 86960, 0, 68320, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1C2, 6)
    EventEnd(0x5)
    Return()

    # Function_26_3334 end

    def Function_27_3989(): pass

    label("Function_27_3989")

    EventBegin(0x0)
    Fade(500)
    OP_68(89970, 1500, 79740, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 89590, 0, 78000, 315)
    SetChrPos(0x102, 90800, 0, 78000, 315)
    SetChrPos(0x103, 89590, 0, 76500, 315)
    SetChrPos(0x104, 90800, 0, 76500, 315)
    SetChrPos(0x109, 89590, 0, 75000, 315)
    SetChrPos(0x105, 90800, 0, 75000, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x17, 0xFF)
    OP_0D()

    #C0132
    ChrTalk(
        0x101,
        (
            "#12P#00005F（那是……\x01",
            "  亚里欧斯先生和雾香小姐吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#12P#00105F（好像是的，他们\x01",
            "  到底在谈什么呢……？）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_0D()

    #C0134
    ChrTalk(
        0x17,
        (
            "#6P#01403F#11P你离开协会差不多有一年了吧？\x02\x03",

            "#01400F习惯新环境了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xB,
        (
            "#12004F#6P……还好吧。\x02\x03",

            "#12000F不过工作强度\x01",
            "远不是在协会时\x01",
            "可以相比的。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x17,
        "#6P#01403F#11P是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0xB)
    SetChrSubChip(0xB, 0x1)
    Sleep(300)

    #C0137
    ChrTalk(
        0xB,
        (
            "#12000F#6P……小滴\x01",
            "还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x17,
        (
            "#6P#01402F#11P嗯，虽然有点太过听话了，\x01",
            "但一直都很开朗。\x02\x03",

            "#01404F最近还结识了很好的朋友，\x01",
            "变得爱笑了……\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        (
            "#12004F#6P是吗，\x01",
            "那可真是不错呢。\x02\x03",

            "#12003F……………………………\x02\x03",

            "纱绫小姐……\x01",
            "已经去世五年了呢。\x02\x03",

            "#12000F我第一次见到她\x01",
            "还是在六年前……\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x17,
        (
            "#11P#01404F六年前……没错。\x02\x03",

            "当时你正在大陆各地\x01",
            "漫无目的地漂泊，\x01",
            "在这座城市中，偶然认识了纱绫……\x02\x03",

            "纱绫硬把你\x01",
            "拉到了我们家，\x01",
            "让你住下。\x02\x03",

            "#01402F三年前，在利贝尔的\x01",
            "协会分部与你重逢时，\x01",
            "可真是大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xB,
        (
            "#12004F#6P呵呵，是啊。\x01",
            "人与人之间的缘分\x01",
            "真是不可思议。\x02\x03",

            "#12003F……那一宿一餐带给我的温暖，\x01",
            "我一生都不会忘记。\x02\x03",

            "#12001F不过，我直到最后也没能\x01",
            "回报那份恩情……\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x17,
        (
            "#11P#01404F……哪里的话，\x01",
            "纱绫能听到你这么说，\x01",
            "就一定会很开心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(90790, 1500, 76740, 0)
    MoveCamera(64, 26, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15480, 0)
    OP_4C(0x17, 0xFF)
    OP_0D()

    #C0143
    ChrTalk(
        0x101,
        (
            "#00005F#11P（……看样子，在雾香小姐\x01",
            "  加入游击士协会之前，\x01",
            "  他们两个就已经认识了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x102,
        (
            "#11P#00108F（是啊，\x01",
            "  不过我觉得继续偷听\x01",
            "  下去就不太好了。）\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x103,
        (
            "#12P#00203F（嗯，在打扰到他们之前，\x01",
            "  还是赶快离开吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 91210, 0, 76450, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0xB, 0x0)
    SetScenarioFlags(0x1C2, 6)
    EventEnd(0x5)
    Return()

    # Function_27_3989 end

    def Function_28_3FD6(): pass

    label("Function_28_3FD6")

    EventBegin(0x0)
    Fade(500)
    OP_68(88320, 1500, 84360, 0)
    MoveCamera(38, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    OP_4B(0x17, 0xFF)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4372")

    #C0146
    ChrTalk(
        0x17,
        (
            "#11P#01404F说起来……\x01",
            "艾丝蒂尔和约修亚\x01",
            "很想见你呢。\x02\x03",

            "他们听说你在纪念庆典时期\x01",
            "与林见过面时，好像相当遗憾。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xB,
        (
            "#12004F#6P呵呵，是吗，\x01",
            "那还真是抱歉啊。\x02\x03",

            "如果时间允许，\x01",
            "我自然也很想和他们见个面。\x02\x03",

            "#12002F艾丝蒂尔和约修亚在克洛斯贝尔的\x01",
            "活跃表现，我早已有所耳闻。\x02\x03",

            "我是看着那两人从新人时代\x01",
            "一步一步过来的……\x01",
            "现在真是让人刮目相看啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x17,
        (
            "#11P#01402F是啊，他们两个\x01",
            "也帮了我不少忙。\x02\x03",

            "#01404F或许该说，真不愧是\x01",
            "卡西乌斯先生的孩子吧……\x01",
            "将来的表现十分值得期待呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(86330, 1800, 73970, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14890, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 87080, 0, 73540, 0)
    SetChrPos(0x102, 88890, 0, 73750, 0)
    SetChrPos(0x103, 86550, 0, 71830, 0)
    SetChrPos(0x104, 88500, 0, 72620, 0)
    SetChrPos(0x109, 89790, 0, 72690, 0)
    SetChrPos(0x105, 87790, 0, 71090, 0)
    OP_0D()

    #C0149
    ChrTalk(
        0x101,
        (
            "#00001F#11P（说起来……\x01",
            "  雾香小姐以前曾在\x01",
            "  利贝尔的协会分部做过接待员呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        (
            "#00300F#11P（也就是说，\x01",
            "  她肯定认识\x01",
            "  艾丝蒂尔他们。）\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x102,
        (
            "#00102F#11P（呵呵，人与人\x01",
            "  之间的联系实在是\x01",
            "  难以预料。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x0, 7)
    Jump("loc_44DE")

    label("loc_4372")


    #C0152
    ChrTalk(
        0x17,
        (
            "#11P#01405F话说回来，你和金先生\x01",
            "还保持着联系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xB,
        (
            "#12004F#6P嗯，是的。\x02\x03",

            "#12000F但我们的立场身份不同，\x01",
            "也没有多少见面的机会。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(86330, 1800, 73970, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14890, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 87080, 0, 73540, 0)
    SetChrPos(0x102, 88890, 0, 73750, 0)
    SetChrPos(0x103, 86550, 0, 71830, 0)
    SetChrPos(0x104, 88500, 0, 72620, 0)
    SetChrPos(0x109, 89790, 0, 72690, 0)
    SetChrPos(0x105, 87790, 0, 71090, 0)
    OP_0D()

    #C0154
    ChrTalk(
        0x101,
        (
            "#00003F#11P（不能再继续偷听了，\x01",
            "  赶快离开吧。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_44DE")

    SetChrPos(0x0, 87080, 0, 73540, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x17, 0xFF)
    EventEnd(0x5)
    Return()

    # Function_28_3FD6 end

    def Function_29_450A(): pass

    label("Function_29_450A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48B8")
    EventBegin(0x0)
    Fade(500)
    OP_68(34230, 0, 320, 0)
    MoveCamera(58, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18390, 0)
    SetChrPos(0x101, 33280, 0, -280, 90)
    SetChrPos(0x102, 33280, 0, -1680, 90)
    SetChrPos(0x103, 32970, 0, 720, 90)
    SetChrPos(0x104, 31670, 0, -670, 90)
    SetChrPos(0x109, 31080, 0, -1750, 99)
    SetChrPos(0x105, 31070, 0, 740, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0xC, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0155
    ChrTalk(
        0x101,
        "#00005F啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(73750, 1500, 1580, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    Sound(160, 0, 100, 0)
    OP_64(0xC)
    OP_64(0xD)
    Sleep(500)

    #C0156
    ChrTalk(
        0xD,
        (
            "……嗯，导力梯\x01",
            "已经到了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xC,
        "#6P哦……请您先用。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xD,
        (
            "啊，不不，还是\x01",
            "请您先用吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xD,
        "我并不是很着急。\x02",
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xC, 0xD, 500)

    #C0160
    ChrTalk(
        0xC,
        (
            "#6P不，我毕竟是\x01",
            "后到的……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(34230, 0, 320, 0)
    MoveCamera(58, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18390, 0)
    OP_0D()

    #C0161
    ChrTalk(
        0x104,
        "#6P#00305F怎么了？罗伊德。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0162
    ChrTalk(
        0x101,
        (
            "#00001F哦，两大国的军官\x01",
            "正在导力梯前交谈……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)
    TurnDirection(0x103, 0x104, 500)

    #C0163
    ChrTalk(
        0x102,
        (
            "#00106F看样子，好像是在\x01",
            "互相谦让乘梯。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x109,
        "#12P#10108F……气、气氛好像有点尴尬啊。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)

    #C0165
    ChrTalk(
        0x105,
        (
            "#6P#10302F呵呵，他们到底在\x01",
            "客气什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x103,
        (
            "#00203F……算了，\x01",
            "我们也没有乘坐\x01",
            "导力梯的必要。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x101,
        "#00003F是啊……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 33280, 0, -280, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0xC, 0xFF)
    OP_4C(0xD, 0xFF)
    SetScenarioFlags(0x1C2, 7)
    EventEnd(0x5)
    Return()

    label("loc_48B8")

    EventBegin(0x1)

    #C0168
    ChrTalk(
        0x101,
        (
            "#00000F……帝国和共和国的军官\x01",
            "还在导力梯前。\x02\x03",

            "#00003F我们去走楼梯吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 33280, 0, -280, 270)
    EventEnd(0x4)
    Return()

    # Function_29_450A end

    def Function_30_491A(): pass

    label("Function_30_491A")

    Sound(160, 0, 100, 0)
    Return()

    # Function_30_491A end

    def Function_31_4921(): pass

    label("Function_31_4921")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C1, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4949")
    SetScenarioFlags(0x146, 3)

    label("loc_4949")

    Return()

    # Function_31_4921 end

    def Function_32_494A(): pass

    label("Function_32_494A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    CreatePortrait(0, 230, 192, 742, 256, 0, 20, 512, 64, 0, 0, 512, 64, 0xFFFFFF, 0x0, "c_vis505.itp")
    OP_90(0x101, -51500, 0, 11300, 0)
    OP_90(0x102, -51500, 0, 10200, 0)
    OP_90(0x103, -51500, 0, 9100, 0)
    OP_90(0x104, -51500, 0, 8000, 0)
    OP_90(0x109, -51500, 0, 6900, 0)
    OP_90(0x105, -51500, 0, 5800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -51500, 0, 13500, 0)
    ClearMapObjFlags(0xB, 0x10)
    OP_70(0xB, 0x3C)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x3C)
    OP_68(-54000, 1100, 12700, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    FadeToBright(2000, 0)
    BeginChrThread(0x1D, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x101, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 33)
    Sleep(50)
    BeginChrThread(0x105, 3, 0, 33)
    OP_0D()
    OP_68(-54000, 1100, -300, 8000)
    OP_6F(0x79)
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0xD, 0x10)
    OP_71(0xD, 0x0, 0x5, 0x0, 0x0)
    OP_79(0xD)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_68(-12600, 1000, 0, 0)
    MoveCamera(47, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x1D, -10500, 0, 0, 90)
    SetChrPos(0x3C, -11600, -600, 0, 90)
    SetChrPos(0x101, -12600, 0, -800, 90)
    SetChrPos(0x102, -12600, 0, 700, 90)
    SetChrPos(0x103, -13800, 0, -400, 90)
    SetChrPos(0x104, -13800, 0, 1100, 90)
    SetChrPos(0x109, -15000, 0, -600, 90)
    SetChrPos(0x105, -15000, 0, 900, 90)
    OP_6B(0x3C)
    SetChrFlags(0x3C, 0x20)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3C, 0x8)
    SetChrFlags(0x3C, 0x4)

    def lambda_4BDA():
        OP_97(0xFE, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_4BDA)

    def lambda_4BF4():
        OP_98(0xFE, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_4BF4)

    def lambda_4C0E():
        OP_97(0x101, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4C0E)
    Sleep(50)

    def lambda_4C2B():
        OP_97(0x102, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4C2B)
    Sleep(50)

    def lambda_4C48():
        OP_97(0x103, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4C48)
    Sleep(50)

    def lambda_4C65():
        OP_97(0x104, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4C65)
    Sleep(50)

    def lambda_4C82():
        OP_97(0x109, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4C82)
    Sleep(50)

    def lambda_4C9F():
        OP_97(0x105, 0x4A38, 0x0, 0x0, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4C9F)
    FadeToBright(1000, 0)
    MoveCamera(37, 21, 0, 8000)
    SetCameraDistance(18000, 8000)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(3500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    WaitChrThread(0x1D, 1)

    def lambda_4D0C():
        OP_93(0xFE, 0x110, 0x15E)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_4D0C)
    WaitChrThread(0x101, 0)

    def lambda_4D1D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D1D)
    Sleep(100)
    WaitChrThread(0x102, 0)

    def lambda_4D31():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4D31)
    WaitChrThread(0x101, 2)

    #C0169
    ChrTalk(
        0x101,
        "#6P#00001F啊……！\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x102,
        "#00101F#6P那是……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_6B(0xFF)
    OP_68(10000, 1000, 3800, 2000)
    MoveCamera(0, 19, 0, 2000)
    SetCameraDistance(20000, 2000)

    def lambda_4DA0():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_4DA0)
    OP_6F(0x79)

    #C0171
    ChrTalk(
        0x1D,
        (
            "#6P#02804F呵呵，那就是在不久之后，\x01",
            "各方势力以国际友好的名义\x01",
            "而互相展开试探的舞台──\x02\x03",

            "#02800F国际会议场。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x1D, -52000, 0, 101500, 0)
    SetChrPos(0x101, -51400, 0, 104200, 0)
    SetChrPos(0x102, -52600, 0, 104200, 0)
    SetChrPos(0x103, -50200, 0, 103400, 0)
    SetChrPos(0x104, -53800, 0, 103400, 0)
    SetChrPos(0x109, -51200, 0, 102600, 0)
    SetChrPos(0x105, -52900, 0, 102200, 0)
    OP_68(-52000, 5500, 118000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(20500, 0)
    OP_68(-52660, 3000, 105850, 6000)
    MoveCamera(23, 7, 0, 6000)
    OP_6E(700, 6000)
    SetCameraDistance(16500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1500)

    def lambda_4F14():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4F14)
    Sleep(50)

    def lambda_4F31():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4F31)
    Sleep(50)

    def lambda_4F4E():
        OP_97(0x103, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4F4E)
    Sleep(50)

    def lambda_4F6B():
        OP_97(0x104, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4F6B)
    Sleep(50)

    def lambda_4F88():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4F88)
    Sleep(50)

    def lambda_4FA5():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4FA5)
    Sleep(500)

    def lambda_4FC2():
        OP_97(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_4FC2)
    OP_6F(0x79)

    #C0172
    ChrTalk(
        0x101,
        "#00011F#11P这还真是……厉害啊。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x103,
        "#00205F#11P视野非常壮观……\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x104,
        (
            "#00302F#5P天花板这么高，\x01",
            "看来是打通了两层楼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x1D,
        (
            "#02804F#11P是啊，因此上面的\x01",
            "三十六层是Ｕ型结构。\x02\x03",

            "#02800F顺便一提，两侧的房间\x01",
            "是供各国首脑随行人员\x01",
            "休息的休息室。\x02\x03",

            "负责护卫的军官们\x01",
            "都会在里面待命。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_50F3():
        TurnDirection(0x101, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_50F3)
    Sleep(50)

    def lambda_5103():
        TurnDirection(0x109, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5103)
    Sleep(50)

    def lambda_5113():
        TurnDirection(0x102, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5113)
    Sleep(50)

    def lambda_5123():
        TurnDirection(0x105, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5123)
    Sleep(50)

    def lambda_5133():
        TurnDirection(0x103, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5133)
    Sleep(50)

    def lambda_5143():
        TurnDirection(0x104, 0x1D, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5143)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0176
    ChrTalk(
        0x109,
        "#10100F#5P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#10302F#5P确实需要\x01",
            "这种房间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x1D,
        (
            "#02804F#11P好了，让我带你们\x01",
            "去最后一个楼层吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    OP_68(13400, 900, 0, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x1D, 15500, 0, 0, 90)
    SetChrPos(0x3C, 13400, -600, 0, 90)
    SetChrPos(0x101, 13400, 0, -800, 90)
    SetChrPos(0x102, 13400, 0, 700, 90)
    SetChrPos(0x103, 12200, 0, -400, 90)
    SetChrPos(0x104, 12200, 0, 1100, 90)
    SetChrPos(0x109, 11000, 0, -600, 90)
    SetChrPos(0x105, 11000, 0, 900, 90)
    OP_6B(0x3C)
    SetChrFlags(0x3C, 0x20)
    SetChrFlags(0x3C, 0x40)
    SetChrFlags(0x3C, 0x8)
    SetChrFlags(0x3C, 0x4)
    MoveCamera(47, 21, 0, 10000)
    SetCameraDistance(19000, 10000)

    def lambda_52D9():
        OP_97(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_52D9)

    def lambda_52F3():
        OP_98(0xFE, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_52F3)

    def lambda_530D():
        OP_97(0x101, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_530D)
    Sleep(50)

    def lambda_532A():
        OP_97(0x102, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_532A)
    Sleep(50)

    def lambda_5347():
        OP_97(0x103, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5347)
    Sleep(50)

    def lambda_5364():
        OP_97(0x104, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5364)
    Sleep(50)

    def lambda_5381():
        OP_97(0x109, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5381)
    Sleep(50)

    def lambda_539E():
        OP_97(0x105, 0x61A8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_539E)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(8000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x3C, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_68(71900, 1000, 0, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x1D, 71900, 0, 0, 90)
    SetChrPos(0x3C, 71900, -500, 0, 90)
    SetChrPos(0x101, 70200, 0, -900, 90)
    SetChrPos(0x102, 70200, 0, 600, 90)
    SetChrPos(0x103, 69000, 0, -500, 90)
    SetChrPos(0x104, 69000, 0, 1000, 90)
    SetChrPos(0x109, 67800, 0, -700, 90)
    SetChrPos(0x105, 67800, 0, 800, 90)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    SetCameraDistance(20000, 7000)

    def lambda_54D1():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 0, lambda_54D1)
    BeginChrThread(0x3C, 3, 0, 35)
    Sleep(100)
    FadeToBright(1000, 0)

    def lambda_54FD():
        OP_97(0x101, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_54FD)
    Sleep(50)

    def lambda_551A():
        OP_97(0x102, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_551A)
    Sleep(50)

    def lambda_5537():
        OP_97(0x103, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5537)
    Sleep(50)

    def lambda_5554():
        OP_97(0x104, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5554)
    Sleep(50)

    def lambda_5571():
        OP_97(0x109, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5571)
    Sleep(50)

    def lambda_558E():
        OP_97(0x105, 0x1A2C, 0x0, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_558E)
    Sleep(100)

    def lambda_55AB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_55AB)
    Sleep(50)

    def lambda_55BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_55BF)
    OP_0D()
    WaitChrThread(0x1D, 0)
    BeginChrThread(0x1D, 3, 0, 34)
    WaitChrThread(0x101, 0)
    BeginChrThread(0x101, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x102, 0)
    BeginChrThread(0x102, 3, 0, 34)
    Sleep(100)
    WaitChrThread(0x103, 0)
    BeginChrThread(0x103, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x104, 0)
    BeginChrThread(0x104, 3, 0, 34)
    Sleep(100)
    WaitChrThread(0x109, 0)
    BeginChrThread(0x109, 3, 0, 34)
    Sleep(900)
    WaitChrThread(0x105, 0)
    BeginChrThread(0x105, 3, 0, 34)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_71(0x6, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x6)
    OP_0D()
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_A7(0x1D, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_32_494A end

    def Function_33_56B7(): pass

    label("Function_33_56B7")


    def lambda_56BC():
        OP_95(0xFE, -51500, 0, 14000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56BC)
    WaitChrThread(0xFE, 1)

    def lambda_56DA():
        OP_95(0xFE, -55500, 0, 14000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56DA)
    WaitChrThread(0xFE, 1)

    def lambda_56F8():
        OP_95(0xFE, -55500, 0, 1500, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_56F8)
    WaitChrThread(0xFE, 1)

    def lambda_5716():
        OP_95(0xFE, -53000, 0, -1000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5716)
    WaitChrThread(0xFE, 1)

    def lambda_5734():
        OP_95(0xFE, -48000, 0, -1000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5734)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_56B7 end

    def Function_34_574E(): pass

    label("Function_34_574E")


    def lambda_5753():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5753)
    WaitChrThread(0xFE, 1)

    def lambda_5771():
        OP_95(0xFE, 81000, 0, 5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5771)
    Sleep(700)

    def lambda_578E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_578E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_34_574E end

    def Function_35_579F(): pass

    label("Function_35_579F")


    def lambda_57A4():
        OP_97(0xFE, 0x1388, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3C, 1, lambda_57A4)
    WaitChrThread(0x3C, 1)

    def lambda_57C2():
        OP_95(0xFE, 81000, 0, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_57C2)
    WaitChrThread(0xFE, 1)
    OP_6B(0xFF)
    Return()

    # Function_35_579F end

    def Function_36_57DF(): pass

    label("Function_36_57DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    LoadChrToIndex("chr/ch05900.itc", 0x27)
    LoadChrToIndex("chr/ch05600.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02500.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02800.itp")
    CreatePortrait(4, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07200.itp")
    CreatePortrait(5, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07000.itp")
    CreatePortrait(6, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07500.itp")
    CreatePortrait(7, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu07400.itp")
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    OP_4B(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K当天１３：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0180
    AnonymousTalk(
        0x23,
        (
            "#02503F──那么，我宣布\x01",
            "『西塞姆里亚通商会议』\x01",
            "在此正式召开。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7583", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-52000, 7500, 116000, 0)
    MoveCamera(45, 29, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(23000, 0)
    OP_68(-52000, 2500, 116000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-46800, 1000, 119400, 0)
    MoveCamera(27, 15, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14000, 0)
    OP_68(-46800, 1000, 114800, 4000)
    MoveCamera(43, 21, 0, 4000)
    SetCameraDistance(14500, 4000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-57600, 900, 118600, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13000, 0)
    MoveCamera(333, 29, 0, 4000)
    SetCameraDistance(15000, 4000)
    OP_6F(0x79)
    Sleep(300)
    Fade(500)
    OP_68(-52000, 900, 123900, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(14000, 3000)
    OP_6F(0x79)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0181
    AnonymousTalk(
        0x23,
        (
            "会议的主持工作\x01",
            "将由我亨利·麦克道尔\x01",
            "僭越担当。\x02\x03",

            "整个会议预计持续五小时，\x01",
            "中途将会有一次休息。\x02\x03",

            "根据会议的实际进程，\x01",
            "时间可能多少会有一些延长，\x01",
            "还请各位理解。\x02\x03",

            "另外，我们还特意\x01",
            "邀请两名旁听者\x01",
            "参与本次会议。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetChrSubChip(0x23, 0x1)
    SetChrSubChip(0x1D, 0x1)
    OP_68(-41100, 900, 121250, 2500)
    MoveCamera(90, 15, 0, 2500)
    SetCameraDistance(15000, 2500)
    OP_6F(0x79)
    SetChrSubChip(0x1E, 0x2)
    SetChrSubChip(0x1F, 0x2)
    SetChrSubChip(0x20, 0x2)
    Sleep(300)

    #C0182
    ChrTalk(
        0x23,
        (
            "#02503F#6P#N这位是伊安·格里姆伍德律师。\x02\x03",

            "在克洛斯贝尔及周边诸国\x01",
            "均有活跃表现的法律专家。\x02\x03",

            "#02500F由于他精通国际法与国际惯例法，\x01",
            "因而我们特意邀请他参加此次会议。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x24, 0x27)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -40100, 0, 120250, 270)
    OP_0D()
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0183
    AnonymousTalk(
        0x24,
        (
            "初次见面……\x01",
            "我是伊安·格里姆伍德。\x02",
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

    #C0184
    ChrTalk(
        0x1F,
        (
            "#07200F#12P#N哦，您就是那位\x01",
            "有名的『大胡子熊律师』啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0185
    ChrTalk(
        0x21,
        (
            "唔，听说您一直积极\x01",
            "介入人权等方面的问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(100)

    #C0186
    ChrTalk(
        0x20,
        "#07002F#12P#N呵呵，请您多多指教。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0187
    ChrTalk(
        0x24,
        (
            "#5P#02210F哈哈……我会全心全意\x01",
            "做好自己的工作的。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-46900, 900, 126600, 2500)
    MoveCamera(0, 15, 0, 2500)
    SetCameraDistance(15500, 2500)
    OP_6F(0x79)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    Sleep(300)

    #C0188
    ChrTalk(
        0x23,
        (
            "#6P#02503F这位是亚里欧斯·马克莱因。\x02\x03",

            "曾在周边各国立下过\x01",
            "卓越功绩的著名游击士。\x02\x03",

            "#02500F我们邀请他代表游击士协会，\x01",
            "从中立的立场上\x01",
            "来保障此次会议的安全。\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x8)
    Sleep(130)
    SetChrSubChip(0x17, 0x9)
    Sleep(130)
    SetChrSubChip(0x17, 0xA)
    Sleep(800)
    SetChrSubChip(0x17, 0x9)
    Sleep(130)
    SetChrSubChip(0x17, 0x8)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("游击士亚里欧斯")

    #A0189
    AnonymousTalk(
        0xFF,
        (
            "我是亚里欧斯·马克莱因，\x01",
            "请多指教。\x02",
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

    #C0190
    ChrTalk(
        0x22,
        (
            "#07509F#6P#N哈哈，你就是『风之剑圣』吗？\x02\x03",

            "#07500F我在共和国也经常听到\x01",
            "你的名字呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0191
    ChrTalk(
        0x1E,
        (
            "#07404F#11P#12P#N在帝都也时有耳闻。\x02\x03",

            "#07400F据说克洛斯贝尔有一位\x01",
            "迅如疾风的『剑圣』。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x17, 0x8)
    Sleep(130)
    SetChrSubChip(0x17, 0xC)
    Sleep(130)
    SetChrSubChip(0x17, 0xD)

    #N0192
    NpcTalk(
        0x17,
        "游击士亚里欧斯",
        "#01404F……不敢当。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-52000, 1000, 120500, 0)
    MoveCamera(90, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x17, 0x2)
    SetChrSubChip(0x17, 0x0)
    SetChrSubChip(0x23, 0x0)
    SetChrSubChip(0x1D, 0x0)
    SetChrSubChip(0x1E, 0x0)
    SetChrSubChip(0x1F, 0x0)
    OP_0D()
    Sleep(300)

    #C0193
    ChrTalk(
        0x23,
        (
            "#02503F#5P那么，我们就马上开始\x01",
            "讨论各项议案吧。\x02\x03",

            "#02500F提议人──迪塔·库罗伊斯市长，\x01",
            "请予以解释和补充。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x1D,
        "#6P#02804F好的。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, -54850, 50, 123900, 180)
    OP_0D()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0195
    AnonymousTalk(
        0x1D,
        (
            "首先，请各位翻开手边的资料，\x01",
            "查阅最初的议案──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(22500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_36_57DF end

    def Function_37_64E0(): pass

    label("Function_37_64E0")

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

    #C0196
    ChrTalk(
        0x101,
        (
            "#11P#00000F好……\x01",
            "已经巡视过一圈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x109,
        (
            "#6P#10100F目前似乎\x01",
            "并没有什么问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x104,
        (
            "#5P#00302F是啊，就保持这个状态，\x01",
            "再四处看一看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00104F嗯……\x02\x03",

            "#00108F……不知会议的情况\x01",
            "怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        (
            "#11P#00006F这个嘛，市长和议长\x01",
            "肯定都在努力呢，但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x103,
        (
            "#12P#00201F主要问题还在于『铁血宰相』\x01",
            "和洛克史密斯总统，是吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
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
    Call(0, 39)
    Return()

    # Function_37_64E0 end

    def Function_38_673D(): pass

    label("Function_38_673D")

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

    #C0203
    ChrTalk(
        0x101,
        (
            "#11P#00000F好……\x01",
            "这样就算转过一圈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0x109,
        (
            "#6P#10100F目前似乎\x01",
            "并没有什么问题呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x104,
        (
            "#5P#00302F是啊，就保持这个状态，\x01",
            "再四处看一看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#00104F是啊……\x02\x03",

            "#00108F……不知会议的情况\x01",
            "怎么样了。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x101,
        (
            "#11P#00006F这个嘛，市长和议长\x01",
            "肯定都在努力呢，但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x103,
        (
            "#12P#00201F主要问题还在于『铁血宰相』\x01",
            "和洛克史密斯总统，是吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
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
    Call(0, 39)
    Return()

    # Function_38_673D end

    def Function_39_699E(): pass

    label("Function_39_699E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10900.itc", 0x1E)
    LoadChrToIndex("chr/ch11100.itc", 0x1F)
    LoadChrToIndex("chr/ch11000.itc", 0x20)
    LoadChrToIndex("chr/ch11800.itc", 0x21)
    LoadChrToIndex("chr/ch11700.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05800.itc", 0x24)
    LoadChrToIndex("chr/ch00900.itc", 0x25)
    LoadChrToIndex("chr/ch06000.itc", 0x26)
    LoadChrToIndex("chr/ch47900.itc", 0x27)
    LoadChrToIndex("apl/ch50314.itc", 0x28)
    LoadChrToIndex("chr/ch27400.itc", 0x29)
    LoadChrToIndex("chr/ch27800.itc", 0x2A)
    LoadChrToIndex("chr/ch27900.itc", 0x2B)
    LoadChrToIndex("chr/ch47500.itc", 0x2C)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SoundLoad(851)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -50800, 0, 125000, 180)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -49600, 0, 125000, 180)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -51900, 0, 125200, 180)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -54200, 0, 125000, 180)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -53100, 0, 125200, 180)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -48500, 0, 125200, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -55300, 0, 125200, 180)
    SetChrChipByIndex(0x25, 0x25)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -44300, 0, 122800, 225)
    SetChrChipByIndex(0x36, 0x0)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, -50040, 0, 120090, 180)
    SetChrChipByIndex(0x37, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, -54210, 0, 120370, 180)
    SetChrChipByIndex(0x3D, 0x26)
    SetChrSubChip(0x3D, 0x0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    SetChrPos(0x3D, -52870, 0, 116730, 358)
    SetChrChipByIndex(0x3E, 0x28)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    SetChrPos(0x3E, -53430, 0, 117400, 0)
    SetChrChipByIndex(0x3F, 0x27)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, -51370, 0, 117370, 0)
    SetChrChipByIndex(0x40, 0x29)
    SetChrSubChip(0x40, 0x0)
    ClearChrFlags(0x40, 0x80)
    SetChrFlags(0x40, 0x8000)
    SetChrPos(0x40, -53630, 0, 115630, 0)
    SetChrChipByIndex(0x41, 0x2A)
    SetChrSubChip(0x41, 0x0)
    ClearChrFlags(0x41, 0x80)
    SetChrFlags(0x41, 0x8000)
    SetChrPos(0x41, -51990, 0, 116190, 0)
    SetChrChipByIndex(0x42, 0x2B)
    SetChrSubChip(0x42, 0x0)
    ClearChrFlags(0x42, 0x80)
    SetChrFlags(0x42, 0x8000)
    SetChrPos(0x42, -50340, 0, 116750, 0)
    SetChrChipByIndex(0x43, 0x2C)
    SetChrSubChip(0x43, 0x0)
    ClearChrFlags(0x43, 0x80)
    SetChrFlags(0x43, 0x8000)
    SetChrPos(0x43, -51300, 0, 115500, 348)
    SetMapObjFrame(0xFF, "isu00", 0x0, 0x1)
    ClearMapObjFlags(0xE, 0x4)
    OP_68(-52000, 1100, 120300, 0)
    MoveCamera(33, 17, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K当天１５：０５──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(300)
    SetChrName("")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "会议的前半程终于结束了，\x01",
            "在休息之前，各媒体的记者\x01",
            "对各国首脑进行了联合采访。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(40, 19, 0, 9000)
    SetCameraDistance(21500, 9000)
    BeginChrThread(0x3E, 0, 0, 40)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(851, 2, 100, 0)
    OP_0D()
    Sleep(5000)
    StopSound(851, 2000, 100)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    EndChrThread(0x3E, 0x0)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x142, 1)
    OP_24(0x353)
    SetScenarioFlags(0x22, 2)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_39_699E end

    def Function_40_6DB7(): pass

    label("Function_40_6DB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6E6F")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6DE5")
    Sleep(500)
    Jump("loc_6E2D")

    label("loc_6DE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6DFC")
    Sleep(1000)
    Jump("loc_6E2D")

    label("loc_6DFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E13")
    Sleep(1500)
    Jump("loc_6E2D")

    label("loc_6E13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6E2A")
    Sleep(2000)
    Jump("loc_6E2D")

    label("loc_6E2A")

    Sleep(2500)

    label("loc_6E2D")

    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(810, 0, 80, 0)
    Jump("Function_40_6DB7")

    label("loc_6E6F")

    Return()

    # Function_40_6DB7 end

    def Function_41_6E70(): pass

    label("Function_41_6E70")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 215)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    OP_68(-52580, 3500, 121120, 0)
    MoveCamera(104, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18820, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0212
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K当天１６：３０──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    Sleep(300)
    SetChrName("")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "通商会议进入后半程，\x01",
            "正如伊安律师所担心的一样，\x01",
            "讨论从一开始便暗藏风波。\x02\x03",

            "帝国与共和国接连提出\x01",
            "关于克洛斯贝尔安全保障\x01",
            "方面的尖锐问题……\x02\x03",

            "迪塔市长与麦克道尔议长的表情\x01",
            "越发严峻。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    PlayBGM("ed7583", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x247), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-52580, 1500, 121120, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-53220, 1500, 119580, 100000)
    MoveCamera(81, 11, 0, 100000)

    #C0214
    ChrTalk(
        0x1E,
        (
            "#5P#07403F问题在于，区区一个宗教团体，\x01",
            "就对社会治安造成了如此严重的冲击。\x02\x03",

            "#07401F而且竟然连维持治安的组织都被操纵了，\x01",
            "这简直是前所未闻。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0215
    ChrTalk(
        0x1D,
        "#6P#02803F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0216
    ChrTalk(
        0x23,
        (
            "#02500F#6P……我们已经向各位解释过\x01",
            "当时的详细情况了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0217
    ChrTalk(
        0x1E,
        (
            "#5P#07403F问题并不在于详细情况，\x01",
            "而是处理危机状况的『能力』。\x02\x03",

            "#07401F在事件发生之时，滞留在此的帝国人的\x01",
            "生命安全与财产安全受到了威胁，这是不争的事实。\x02\x03",

            "关于这个问题，您有什么看法？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1F, 0x2)
    Sleep(300)

    #C0218
    ChrTalk(
        0x1F,
        (
            "#11P#07203F等一下，宰相。\x02\x03",

            "#07201F支付损害赔偿和抚恤金的手续\x01",
            "已经在办理之中了。\x02\x03",

            "如果再索取额外款项，\x01",
            "我们帝国的度量将会遭受质疑。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    #C0219
    ChrTalk(
        0x1E,
        (
            "#5P#07400F不，殿下，\x01",
            "问题的重点不在于此。\x02\x03",

            "关键是……\x01",
            "克洛斯贝尔自治州政府如何\x01",
            "才能保障各类『安全』。\x02\x03",

            "#07403F生命安全、财产安全、\x01",
            "贸易和金融市场的信用安全！\x02\x03",

            "#07401F只顾着进行政治斗争，\x01",
            "使那些可疑之辈有了可乘之机，\x01",
            "这样的人，又怎能保障这些安全？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0220
    ChrTalk(
        0x1F,
        "#11P#07208F……唔………\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x21,
        (
            "#4P#N不过，我听说哈尔特曼前议长下台之后，\x01",
            "腐败现象也得到了清理……\x02\x03",

            "今后只要在健全的政治体制下\x01",
            "建立坚实的安全保障体系，\x01",
            "不就没问题了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x22, 0x2)
    Sleep(300)

    #C0222
    ChrTalk(
        0x22,
        (
            "#6P#07500F#N不不，大公阁下，\x01",
            "事情可没有那么简单哦。\x02\x03",

            "在克洛斯贝尔的政治环境下，\x01",
            "原本就比较容易滋生腐败现象。\x02\x03",

            "迪塔市长和麦克道尔议长\x01",
            "确实是非常杰出的政治家……\x02\x03",

            "但是，假如他们发生了某些意外，\x01",
            "克洛斯贝尔难道不会故态复萌吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrSubChip(0x21, 0x1)
    Sleep(300)

    #C0223
    ChrTalk(
        0x21,
        "#4P#N唔……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0224
    ChrTalk(
        0x20,
        (
            "#11P#07003F……这样说或许有些悲观，\x01",
            "但在政治当中，腐败是不可避免的。\x02\x03",

            "#07008F不仅是克洛斯贝尔，无论在哪里\x01",
            "都是一样，当然也包括我国在内……\x02\x03",

            "#07001F既然如此，他们两位在任期内\x01",
            "能否建立起健全的政治体制，\x01",
            "才是我们现在更应该关心的事情吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0225
    ChrTalk(
        0x1E,
        (
            "#5P#07404F……恕我失礼，殿下年纪尚轻，\x01",
            "我也明白您愿意相信希望的心情。\x02\x03",

            "#07403F然而，克洛斯贝尔和由古老\x01",
            "王室领导的利贝尔有所不同。\x02\x03",

            "在没有可靠权威的地方，\x01",
            "政权是非常容易弱化的……\x02\x03",

            "#07401F关于这一点，历史已经证明得很清楚了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0226
    ChrTalk(
        0x20,
        "#11P#07005F这、这个……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x22, 0x0)
    Sleep(300)

    #C0227
    ChrTalk(
        0x22,
        (
            "#6P#07503F#N嗯，我国虽然没有君主，\x01",
            "但却有充满荣耀的共和国宪章。\x02\x03",

            "#07500F在一百年前的革命中，\x01",
            "各方势力与各个民族团结一致，\x01",
            "才创造出了这个奇迹。\x02\x03",

            "可以说，正是以此为依托，\x01",
            "我国的政治体系才没有因\x01",
            "腐败现象而堕落，并一直存续至今。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x23, 0x2)
    Sleep(300)
    SetChrSubChip(0x1E, 0x0)

    #C0228
    ChrTalk(
        0x23,
        (
            "#02503F#5P……按照您这种观点来说，\x01",
            "我们也有引以为傲的自治州法。\x02\x03",

            "由于各种历史遗留原因，\x01",
            "法律中确实存在不少疏漏之处……\x02\x03",

            "#02500F但我们也一直在\x01",
            "一点点地逐步改善。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)

    #C0229
    ChrTalk(
        0x1E,
        (
            "#11P#07400F……律师，\x01",
            "近十年来，自治州法的\x01",
            "补充、修正条款有多少呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0230
    ChrTalk(
        0x24,
        (
            "#5P#N#02205F这、这个嘛，\x01",
            "目前并没有详细资料。\x02\x03",

            "#02203F不过，大约有五十处左右吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0231
    ChrTalk(
        0x22,
        (
            "#6P#07505F#N十年才五十处！？\x01",
            "这未免让人有些吃惊啊！\x02\x03",

            "换句话说，一年只有五处吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1D, 0x2)
    Sleep(300)

    #C0232
    ChrTalk(
        0x1D,
        (
            "#5P#02803F不，在最近这几年，\x01",
            "有逐渐增加的趋势。\x02\x03",

            "#02801F去年应该修正及补充了\x01",
            "十二项相关条款吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_57(0x0)
    OP_5A()

    #C0233
    ChrTalk(
        0x23,
        (
            "#02505F#5P是的，其中大部分都是关于\x01",
            "金融和导力网络方面的补充条款……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_57(0x0)
    OP_5A()

    #C0234
    ChrTalk(
        0x1E,
        (
            "#11P#07403F不管怎么说，以目前的状态来看，\x01",
            "很难相信克洛斯贝尔能够迅速建立起\x01",
            "稳固有效的安全保障体制。\x02\x03",

            "#07401F我们显然还是应该根据具体现状\x01",
            "来探讨今后的对策。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0235
    ChrTalk(
        0x22,
        "#6P#07504F#N是啊，关于这一点，我也有同感。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x0)

    #C0236
    ChrTalk(
        0x1F,
        (
            "#11P#07206F……哎呀呀，真没想到\x01",
            "你们会如此意气相投。\x02\x03",

            "#07201F关于诺尔德高原的所有权问题，\x01",
            "二位是否也能马上达成一致呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0237
    ChrTalk(
        0x22,
        "#6P#07509F#N哈哈，被你将了一军啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0238
    ChrTalk(
        0x1E,
        (
            "#5P#07404F嗯，关于这个问题，\x01",
            "还是另找机会再说吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0239
    ChrTalk(
        0x20,
        "#11P#07008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0240
    ChrTalk(
        0x21,
        (
            "#4P#N唔，时间宝贵，\x01",
            "应该开始下一个议题了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0241
    ChrTalk(
        0x23,
        (
            "#02503F#5P……明白了。\x01",
            "那么，就遵照宰相阁下的提议──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(19320, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 2)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_6E70 end

    def Function_42_7E74(): pass

    label("Function_42_7E74")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05602.itc", 0x23)
    LoadChrToIndex("chr/ch05800.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x2)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x1)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -53850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -49100, 50, 123900, 135)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    OP_68(-46970, 2000, 122960, 0)
    MoveCamera(53, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21890, 0)
    VolumeBGM(0x64, 0x3E8)
    OP_68(-46970, 1000, 122960, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0x23,
        (
            "#02501F#5P宰相阁下……\x01",
            "您刚才说什么？\x02\x03",

            "不好意思，\x01",
            "请您再重复一遍。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x1E,
        (
            "#07404F#11P呵呵，只要您要求，让我说多少遍都没问题。\x02\x03",

            "#07401F解散克洛斯贝尔警备队。\x02\x03",

            "另外，让别国的维持治安部队\x01",
            "常驻于克洛斯贝尔……\x02\x03",

            "我认为这才是最现实的方法。\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x23,
        "#02501F#5P……！\x02",
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1D,
        "#6P#02801F#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0246
    ChrTalk(
        0x20,
        (
            "#5P#07007F#11P#N请、请等一下！\x02\x03",

            "宰相阁下，您难道忘记\x01",
            "《互不侵犯条约》中的条款了吗……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    #C0247
    ChrTalk(
        0x1E,
        (
            "#5P#07405F哦，是指『尽量避免通过武力手段\x01",
            "来解决克洛斯贝尔问题』吗？\x02\x03",

            "#07404F但这项提案并不意味着\x01",
            "要侵略克洛斯贝尔。\x02\x03",

            "#07402F我的意思只是，效仿军队却庸碌无能，\x01",
            "反而使广大民众陷入恐慌的无用组织\x01",
            "就应该解散。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0248
    ChrTalk(
        0x20,
        "#5P#11P#N#07005F！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x1E, 0x0)
    Sleep(300)

    #C0249
    ChrTalk(
        0x1E,
        (
            "#11P#07404F老实说，对帝国军或共和国军而言，\x01",
            "克洛斯贝尔警备队\x01",
            "简直就是形同虚设。\x02\x03",

            "就算是高性能的装甲车，\x01",
            "在战车面前也和纸糊的一样。\x02\x03",

            "#07400F与其把高昂的维护费用浪费在这种组织上，\x01",
            "倒不如将保障安全的职责托付给别国的兵力。\x02\x03",

            "#07402F对一个小小的『自治州』而言，\x01",
            "这才是最有效率的方法吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0250
    ChrTalk(
        0x21,
        (
            "#11P……我认为这种意见\x01",
            "过于极端。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0251
    ChrTalk(
        0x1F,
        (
            "#11P#07203F『别国的兵力』\x01",
            "又是指哪里呢？\x02\x03",

            "#07200F像宰相阁下这样的人物，\x01",
            "总不会丝毫不考虑历史遗留问题，\x01",
            "说出帝国军这个名字吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0252
    ChrTalk(
        0x1E,
        (
            "#11P#07404F哈哈，我可没有那样说。\x02\x03",

            "#07402F不过，如果有那个必要，\x01",
            "我们自然会抛开过去的种种恩怨，\x01",
            "提供帝国军的力量。\x02\x03",

            "如果能使塞姆里亚大陆西部地区\x01",
            "和平发展，这也是在所不辞的。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x23,
        "#02501F#5P唔……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-52480, 1200, 120270, 0)
    MoveCamera(87, 9, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21890, 0)
    SetChrPos(0x17, -46900, 0, 126600, 225)
    OP_0D()

    #C0254
    ChrTalk(
        0x22,
        (
            "#6P#07506F……好了好了，\x01",
            "请各位不要太过激动。\x02\x03",

            "#07501F我也认为宰相阁下的提案\x01",
            "有些强硬。\x02\x03",

            "#07504F不过，警备队这种\x01",
            "有别于正规军的维持治安组织\x01",
            "确实有所欠缺。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x0)
    Sleep(200)

    def lambda_868B():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_868B)
    SetChrSubChip(0x21, 0x1)
    Sleep(50)
    SetChrSubChip(0x1F, 0x0)
    Sleep(50)
    SetChrSubChip(0x1D, 0x2)
    Sleep(50)

    #C0255
    ChrTalk(
        0x1E,
        "#5P#07405F唔，那您的意思是……？\x02",
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x22,
        (
            "#6P#07502F我在此提议，\x01",
            "大幅度缩减警备队的规模……\x02\x03",

            "取而代之，由帝国军管理贝尔加德门，\x01",
            "由共和国军管理唐古拉姆门，\x01",
            "这样如何？\x02\x03",

            "如此一来，就算克洛斯贝尔市\x01",
            "发生紧急情况，军队也能马上赶到。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x1D,
        "#5P#02801F……！\x02",
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x21,
        "#11P总统，这……\x02",
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1E,
        (
            "#5P#07404F嗯，这项方案值得考虑。\x02\x03",

            "#07400F不愧是总统阁下，\x01",
            "能够在应对众多在野党势力的同时\x01",
            "保证政权顺利运转，果然厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x22,
        (
            "#6P#07509F不敢不敢，与压制了顽固的贵族势力，\x01",
            "成功发起改革的宰相阁下相比，实在是不值一提。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x20,
        "#11P#07008F你、你们……\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x1F,
        (
            "#11P#07203F……适可而止吧，\x01",
            "这可不是两国会议啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x1E,
        "#5P#07405F哦，真是失礼了。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x2)
    Sleep(300)

    #C0264
    ChrTalk(
        0x1E,
        (
            "#11P#07404F但不管怎么说，讨论就是\x01",
            "在向着这样的方向发展……\x02\x03",

            "#07402F你们二位的意见如何？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8970():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_8970)
    Sleep(100)
    SetChrSubChip(0x1D, 0x0)
    Sleep(250)

    #C0265
    ChrTalk(
        0x23,
        "#02501F#6P…………唔………………\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x1D,
        "#6P#02803F……………………………………\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(22390, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 3)
    NewScene("c1550", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_7E74 end

    def Function_43_89F7(): pass

    label("Function_43_89F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("apl/ch51233.itc", 0x26)
    LoadChrToIndex("chr/ch00900.itc", 0x27)
    LoadChrToIndex("chr/ch10900.itc", 0x28)
    LoadChrToIndex("chr/ch11100.itc", 0x29)
    LoadChrToIndex("chr/ch11000.itc", 0x2A)
    LoadChrToIndex("chr/ch11800.itc", 0x2B)
    LoadChrToIndex("chr/ch11710.itc", 0x2C)
    LoadChrToIndex("chr/ch05800.itc", 0x2D)
    LoadChrToIndex("chr/ch05900.itc", 0x2E)
    LoadChrToIndex("chr/ch02400.itc", 0x2F)
    LoadEffect(0x1, "battle/sc008100.eff")
    LoadEffect(0x2, "event/ev12001.eff")
    SoundLoad(497)
    SoundLoad(865)
    SoundLoad(861)
    SoundLoad(825)
    SoundLoad(866)
    SoundLoad(4051)
    SoundLoad(3457)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x1)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x1)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -54850, 50, 123900, 180)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x2)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    SetChrChipByIndex(0x17, 0x26)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, -46900, 0, 126600, 180)
    OP_4B(0x17, 0xFF)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x18, 0x80)
    SetMapObjFrame(0xFF, "paper", 0x1, 0x1)
    SetMapObjFlags(0xE, 0x4)
    SetChrChipByIndex(0x25, 0x27)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -52000, 0, 99000, 0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x44, 0x80)
    OP_78(0x12, 0x44)
    OP_49()
    SetChrPos(0x44, -42000, -18000, 144000, 190)
    OP_D5(0x44, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    OP_74(0x12, 0x1E)
    OP_70(0x12, 0x3D)
    OP_71(0x12, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x45, 0x80)
    OP_78(0x13, 0x45)
    OP_49()
    SetChrPos(0x45, -62000, -20000, 144000, 170)
    OP_D5(0x45, 0x0, 0x29810, 0x0, 0x0)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_70(0x13, 0x3D)
    OP_71(0x13, 0x3D, 0x78, 0x0, 0x20)
    OP_68(-54240, 3000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    VolumeBGM(0x64, 0x3E8)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-54240, 2000, 116060, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(150)

    #C0267
    ChrTalk(
        0x1D,
        (
            "#5P#02803F关于目前正在讨论的\x01",
            "这个安全保障议题……\x02\x03",

            "#02800F请允许我在此\x01",
            "提出一项提案。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x1E,
        "#11P#07405F哦……？\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x22,
        (
            "#6P#07509F哈哈哈，您从刚才开始就一言不发，\x01",
            "我还有些奇怪呢……\x02\x03",

            "#07502F请问有何高见？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x1D,
        "#5P#02800F嗯，那就是──\x02",
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrFlags(0x17, 0x20)
    OP_93(0x17, 0xE1, 0x320)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    #N0271
    NpcTalk(
        0x17,
        "游击士亚里欧斯",
        "#01407F#4051V#6P#4S#15A大家快退后！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_8EA8():
        OP_93(0xFE, 0x0, 0x320)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8EA8)
    OP_68(-52000, 1000, 128500, 2000)
    Sleep(1000)
    Fade(500)
    OP_68(-52000, 0, 135000, 0)
    MoveCamera(0, 40, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(-52000, 4000, 130000, 4000)
    MoveCamera(0, 13, 0, 4000)
    SetCameraDistance(30000, 4000)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    BeginChrThread(0x4C, 1, 0, 57)
    BeginChrThread(0x44, 3, 0, 44)
    BeginChrThread(0x45, 3, 0, 45)
    SetChrSubChip(0x1E, 0x2)

    def lambda_8F43():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_8F43)
    WaitChrThread(0x44, 3)
    WaitChrThread(0x45, 3)
    OP_6F(0x79)
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1E, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x22, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7544", 0)
    ReplaceBGM("ed7151", "ed7544")
    ReplaceBGM("ed7550", "ed7544")
    ReplaceBGM("ed7300", "ed7561")

    #C0272
    ChrTalk(
        0x23,
        "#02507F#12P#N什么！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0273
    ChrTalk(
        0x20,
        "#07005F#12P#N飞艇……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(865, 2, 100, 0)
    Sound(861, 2, 100, 0)
    OP_87(0x1, 0x0, 0x13, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x1, 0x12, "Null_gun_l", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x2, 0x12, "Null_gun_r", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    PlayEffect(0x2, 0x3, 0xFF, 0x0, -44000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0xFF, 0x0, -60000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_71(0x14, 0x0, 0x1D, 0x0, 0x0)
    OP_71(0x15, 0x0, 0x1D, 0x0, 0x0)
    SetCameraDistance(27000, 2000)
    OP_82(0x12C, 0x12C, 0xBB8, 0x1F40)
    Sleep(2000)
    Fade(500)
    SetChrPos(0x44, -40000, 1000, 144000, 0)
    SetChrPos(0x45, -60000, 1000, 144000, 0)
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -49100, 50, 123900, 0)
    OP_68(-44000, 5000, 130000, 0)
    MoveCamera(43, 5, -10, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    OP_68(-56000, 5000, 130000, 6000)
    MoveCamera(33, 5, 10, 6000)
    SetCameraDistance(24500, 6000)
    OP_0D()
    OP_71(0x14, 0x1E, 0x31, 0x0, 0x0)
    OP_71(0x15, 0x1E, 0x31, 0x0, 0x0)
    OP_6F(0x79)
    StopSound(865, 300, 100)
    StopSound(861, 300, 100)
    Sound(866, 0, 100, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)

    #C0274
    ChrTalk(
        0x21,
        "唔……！\x02",
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x1F,
        (
            "#07207F该不会是……\x01",
            "恐怖分子！？\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x1E,
        "#07401F……………………………\x02",
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x22,
        "#07505F#5P在这种时候出现了吗……！\x02",
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x1D,
        (
            "#02807F#11P请放心！\x01",
            "这是特制的强化玻璃，\x01",
            "足以承受炮击！\x02\x03",

            "但以防万一，\x01",
            "还是请各位退后！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x17, 0x2F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x20)
    BeginChrThread(0x1D, 3, 0, 46)
    BeginChrThread(0x17, 3, 0, 47)
    BeginChrThread(0x23, 3, 0, 48)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 100, 0)
    OP_87(0x1, 0x0, 0x13, "Null_gun", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x1, 0x12, "Null_gun_l", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    OP_87(0x1, 0x2, 0x12, "Null_gun_r", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x7D0, 0x7D0, 0x7D0, 0x0)
    PlayEffect(0x2, 0x3, 0xFF, 0x0, -44000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x4, 0xFF, 0x0, -60000, 3500, 129699, 0, 180, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x14, 0x32, 0x46, 0x0, 0x0)
    OP_71(0x15, 0x32, 0x46, 0x0, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0xBB8)
    Sleep(3000)
    StopSound(865, 300, 100)
    StopSound(861, 300, 100)
    Sound(866, 0, 100, 0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    StopEffect(0x3, 0x2)
    StopEffect(0x4, 0x2)
    BeginChrThread(0x44, 3, 0, 49)
    BeginChrThread(0x45, 3, 0, 50)
    Sleep(400)
    StopSound(497, 4000, 60)
    StopSound(825, 4000, 50)
    WaitChrThread(0x44, 3)
    WaitChrThread(0x45, 3)
    Fade(500)
    OP_68(-38000, 1100, 110200, 0)
    MoveCamera(50, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0x23, 0xFF)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x40)
    SetChrPos(0xA, -36500, 0, 110200, 270)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x40)
    SetChrPos(0x9, -36500, 0, 110200, 270)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x40)
    SetChrPos(0xD, -36500, 0, 110200, 270)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x40)
    SetChrPos(0x8, -36500, 0, 110200, 270)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xC, 0x40)
    SetChrPos(0xC, -67400, 0, 110200, 90)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x40)
    SetChrPos(0xB, -67400, 0, 110200, 90)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x1E, 0x28)
    SetChrSubChip(0x1E, 0x0)
    SetChrPos(0x1E, -50700, 0, 106700, 0)
    SetChrChipByIndex(0x1F, 0x29)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, -49500, 0, 106000, 0)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x0)
    SetChrPos(0x20, -50000, 0, 104300, 0)
    SetChrChipByIndex(0x21, 0x2B)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, -54000, 0, 104300, 0)
    SetChrChipByIndex(0x22, 0x2C)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -54900, 0, 105200, 0)
    SetChrChipByIndex(0x24, 0x2E)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -48900, 0, 103000, 0)
    SetChrPos(0x1D, -53100, 0, 107000, 0)
    SetChrPos(0x23, -52700, 0, 105600, 0)
    SetChrPos(0x17, -51000, 0, 108300, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x3)
    OP_68(-52000, 1100, 105600, 4000)
    MoveCamera(38, 23, 0, 4000)
    SetCameraDistance(17000, 4000)
    BeginChrThread(0xA, 3, 0, 51)
    Sleep(600)
    BeginChrThread(0x9, 3, 0, 52)
    Sleep(600)
    BeginChrThread(0xD, 3, 0, 53)
    Sleep(600)
    BeginChrThread(0x8, 3, 0, 54)
    BeginChrThread(0xB, 3, 0, 55)
    Sleep(600)
    BeginChrThread(0xC, 3, 0, 56)
    WaitChrThread(0xA, 3)

    #C0279
    ChrTalk(
        0xA,
        "#07107F#11P殿下，您没事吧！？\x02",
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x20,
        "#6P#07008F是的，还好……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x9, 3)
    OP_93(0x9, 0x0, 0x1F4)
    Sleep(150)

    #C0281
    ChrTalk(
        0x9,
        (
            "#07301F刚才那是……\x01",
            "莱恩福尔特的高速飞艇吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x0, 0x1F4)
    Sleep(150)

    #C0282
    ChrTalk(
        0x1F,
        "#12P#07201F嗯，应该没错。\x02",
    )

    CloseMessageWindow()
    OP_93(0xB, 0x0, 0x1F4)
    Sleep(150)

    #C0283
    ChrTalk(
        0xB,
        (
            "#12P#N#12001F另一艘是乌尔努公司制造的\x01",
            "军用武装飞艇吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0xC, 0x0, 0x1F4)
    Sleep(150)

    #C0284
    ChrTalk(
        0xC,
        (
            "是的，据报告说，\x01",
            "他们曾夺取到一架……！\x02",
        )
    )

    CloseMessageWindow()
    Sound(121, 0, 100, 0)
    Sound(811, 0, 50, 0)
    ClearChrFlags(0x25, 0x80)

    def lambda_98EF():
        OP_96(0xFE, 0xFFFF34E0, 0x0, 0x19258, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_98EF)

    def lambda_9909():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_9909)
    WaitChrThread(0x25, 1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)

    #C0285
    ChrTalk(
        0x25,
        "#12P#00607F#3457V#30W大家都没事吧！？\x02",
    )

    CloseMessageWindow()
    OP_24(0xD81)
    OP_C9(0x1, 0x80000000)

    def lambda_9969():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_9969)

    def lambda_9976():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9976)
    Sleep(50)

    def lambda_9986():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_9986)

    def lambda_9993():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_9993)

    def lambda_99A0():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_99A0)
    Sleep(50)

    def lambda_99B0():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_99B0)

    def lambda_99BD():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_99BD)
    Sleep(50)

    def lambda_99CD():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_99CD)

    def lambda_99DA():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_99DA)

    #C0286
    ChrTalk(
        0x23,
        "#02501F#5P是啊，还好……！\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x1D,
        "#02801F#5P不过，那些家伙去哪里了……\x02",
    )

    CloseMessageWindow()
    Sound(867, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("男人的声音")

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "……唔，\x01",
            "你们应该听得见吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-52000, 1100, 106600, 1000)
    SetCameraDistance(18000, 1000)

    def lambda_9A8C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_9A8C)

    def lambda_9A99():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_9A99)
    Sleep(50)

    def lambda_9AA9():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_9AA9)

    def lambda_9AB6():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_9AB6)

    def lambda_9AC3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_9AC3)
    Sleep(50)

    def lambda_9AD3():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_9AD3)

    def lambda_9AE0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_9AE0)

    def lambda_9AED():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9AED)

    def lambda_9AFA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_9AFA)
    Sleep(50)

    def lambda_9B0A():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_9B0A)

    def lambda_9B17():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_9B17)

    def lambda_9B24():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_9B24)

    def lambda_9B31():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_9B31)
    OP_6F(0x79)
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("男人的声音")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "出席本次会议的各位代表，\x01",
            "我们是『帝国解放战线』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(10, 60, -1, -1)
    SetChrName("青年的声音")

    #A0290
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "我们是为了保护卡尔瓦德的传统\x01",
            "而采取行动的『反移民政策主义』\x01",
            "一派的成员。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0291
    ChrTalk(
        0x21,
        "#12P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x24,
        (
            "#12P#02205F是在帝国和共和国范围内\x01",
            "活动的恐怖组织……？！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(60, 0, -1, -1)
    SetChrName("男人的声音")

    #A0293
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "我们这次为了讨伐\x01",
            "各自的死敌，\x01",
            "决定联手行动。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetChrName("男人的声音")

    #A0294
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "觉悟吧！\x01",
            "『铁血宰相』吉利亚斯·奥斯本！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 60, -1, -1)
    SetChrName("青年的声音")

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "洛克史密斯总统！\x01",
            "你就在这里消失吧！\x02",
        )
    )

    CloseMessageWindow()

    #A0296
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xA),
            "那些可恨的东方人正在不断侵蚀\x01",
            "卡尔瓦德，为了保卫我们的传统，\x01",
            "就必须要采取这种极端手段！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0297
    ChrTalk(
        0x22,
        "#6P#07506F……愚不可及。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x1E,
        "#07403F#12P嗯，难以理喻。\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x8,
        (
            "#11P#N#11508F但是……\x01",
            "似乎有点不妙呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0300
    NpcTalk(
        0x17,
        "游击士亚里欧斯",
        "#11P#01401F嗯，他们要来了。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x25,
        "#12P#00610F啧……！\x02",
    )

    CloseMessageWindow()
    OP_68(-52000, 1600, 106600, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_24(0x361)
    OP_24(0x35D)
    OP_24(0x1F1)
    OP_24(0x339)
    SetScenarioFlags(0x22, 2)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_43_89F7 end

    def Function_44_9EB0(): pass

    label("Function_44_9EB0")


    def lambda_9EB5():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EB5)
    Sleep(1500)

    def lambda_9ED2():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9ED2)
    Sleep(300)

    def lambda_9EEF():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9EEF)
    Sleep(300)

    def lambda_9F0C():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F0C)
    Sleep(300)

    def lambda_9F29():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F29)
    Sleep(300)

    def lambda_9F46():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F46)
    Sleep(300)

    def lambda_9F63():
        OP_96(0xFE, 0xFFFF5BF0, 0x0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F63)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_44_9EB0 end

    def Function_45_9F7D(): pass

    label("Function_45_9F7D")


    def lambda_9F82():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F82)
    Sleep(1500)

    def lambda_9F9F():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9F9F)
    Sleep(300)

    def lambda_9FBC():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FBC)
    Sleep(300)

    def lambda_9FD9():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FD9)
    Sleep(300)

    def lambda_9FF6():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9FF6)
    Sleep(300)

    def lambda_A013():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A013)
    Sleep(300)

    def lambda_A030():
        OP_96(0xFE, 0xFFFF0DD0, 0x0, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A030)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_45_9F7D end

    def Function_46_A04A(): pass

    label("Function_46_A04A")


    def lambda_A04F():
        OP_95(0xFE, -56700, 0, 123900, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A04F)
    WaitChrThread(0x1D, 1)

    def lambda_A06D():
        OP_95(0xFE, -59000, 0, 120600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A06D)
    WaitChrThread(0x1D, 1)

    def lambda_A08B():
        OP_95(0xFE, -59000, 0, 118600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_A08B)
    WaitChrThread(0x1D, 1)
    Return()

    # Function_46_A04A end

    def Function_47_A0A5(): pass

    label("Function_47_A0A5")


    def lambda_A0AA():
        OP_95(0xFE, -48000, 0, 124600, 3000, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A0AA)
    WaitChrThread(0x17, 1)
    Sleep(500)

    def lambda_A0CB():
        OP_97(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A0CB)
    WaitChrThread(0x17, 1)

    def lambda_A0E9():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFF830, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A0E9)
    WaitChrThread(0x17, 1)

    def lambda_A107():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFEC78, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_A107)
    WaitChrThread(0x17, 1)
    Return()

    # Function_47_A0A5 end

    def Function_48_A121(): pass

    label("Function_48_A121")

    Sleep(1000)

    def lambda_A129():
        OP_97(0xFE, 0x9C4, 0x0, 0x0, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A129)
    WaitChrThread(0x23, 1)

    def lambda_A147():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFF830, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A147)
    WaitChrThread(0x23, 1)

    def lambda_A165():
        OP_97(0xFE, 0x7D0, 0x0, 0xFFFFEC78, 0xBB8, 0x1)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_A165)
    WaitChrThread(0x23, 1)
    Return()

    # Function_48_A121 end

    def Function_49_A17F(): pass

    label("Function_49_A17F")


    def lambda_A184():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A184)
    Sleep(300)

    def lambda_A1A1():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1A1)
    Sleep(300)

    def lambda_A1BE():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1BE)
    Sleep(300)

    def lambda_A1DB():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1DB)
    Sleep(300)

    def lambda_A1F8():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A1F8)
    Sleep(300)

    def lambda_A215():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A215)
    Sleep(300)

    def lambda_A232():
        OP_96(0xFE, 0xFFFF5BF0, 0x4E20, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A232)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_49_A17F end

    def Function_50_A24C(): pass

    label("Function_50_A24C")

    Sleep(400)

    def lambda_A254():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A254)
    Sleep(300)

    def lambda_A271():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A271)
    Sleep(300)

    def lambda_A28E():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A28E)
    Sleep(300)

    def lambda_A2AB():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2AB)
    Sleep(300)

    def lambda_A2C8():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2C8)
    Sleep(300)

    def lambda_A2E5():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A2E5)
    Sleep(300)

    def lambda_A302():
        OP_96(0xFE, 0xFFFF0DD0, 0x4E20, 0x23280, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A302)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_50_A24C end

    def Function_51_A31C(): pass

    label("Function_51_A31C")


    def lambda_A321():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A321)

    def lambda_A33B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A33B)
    WaitChrThread(0xFE, 1)

    def lambda_A350():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A350)
    WaitChrThread(0xFE, 1)

    def lambda_A36E():
        OP_95(0xFE, -48800, 0, 104500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A36E)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xA, 0x20, 500)
    TurnDirection(0x20, 0xA, 500)
    Return()

    # Function_51_A31C end

    def Function_52_A396(): pass

    label("Function_52_A396")


    def lambda_A39B():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A39B)

    def lambda_A3B5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A3B5)
    WaitChrThread(0xFE, 1)

    def lambda_A3CA():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3CA)
    WaitChrThread(0xFE, 1)

    def lambda_A3E8():
        OP_95(0xFE, -48000, 0, 106500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A3E8)
    WaitChrThread(0xFE, 1)
    TurnDirection(0x1F, 0x9, 500)
    Return()

    # Function_52_A396 end

    def Function_53_A409(): pass

    label("Function_53_A409")


    def lambda_A40E():
        OP_95(0xFE, -39800, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A40E)

    def lambda_A428():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A428)
    WaitChrThread(0xFE, 1)

    def lambda_A43D():
        OP_95(0xFE, -42500, 0, 108000, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A43D)
    WaitChrThread(0xFE, 1)

    def lambda_A45B():
        OP_95(0xFE, -49200, 0, 108000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A45B)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x1E, 500)
    Return()

    # Function_53_A409 end

    def Function_54_A47C(): pass

    label("Function_54_A47C")


    def lambda_A481():
        OP_95(0xFE, -39800, 0, 110200, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A481)

    def lambda_A49B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A49B)
    WaitChrThread(0xFE, 1)

    def lambda_A4B0():
        OP_95(0xFE, -42500, 0, 108000, 4000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4B0)
    WaitChrThread(0xFE, 1)

    def lambda_A4CE():
        OP_95(0xFE, -48000, 0, 108000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4CE)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_54_A47C end

    def Function_55_A4E8(): pass

    label("Function_55_A4E8")


    def lambda_A4ED():
        OP_95(0xFE, -64400, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A4ED)

    def lambda_A507():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A507)
    WaitChrThread(0xFE, 1)

    def lambda_A51C():
        OP_95(0xFE, -55900, 0, 104400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A51C)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x22, 500)
    Return()

    # Function_55_A4E8 end

    def Function_56_A53D(): pass

    label("Function_56_A53D")


    def lambda_A542():
        OP_95(0xFE, -64400, 0, 110200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A542)

    def lambda_A55C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_A55C)
    WaitChrThread(0xFE, 1)

    def lambda_A571():
        OP_95(0xFE, -55600, 0, 106300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A571)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x22, 500)
    Return()

    # Function_56_A53D end

    def Function_57_A592(): pass

    label("Function_57_A592")

    Sound(497, 2, 10, 0)
    Sound(825, 2, 10, 0)
    Sleep(80)
    OP_25(0x1F1, 0xF)
    OP_25(0x339, 0xF)
    Sleep(80)
    OP_25(0x1F1, 0x14)
    OP_25(0x339, 0x14)
    Sleep(80)
    OP_25(0x1F1, 0x19)
    OP_25(0x339, 0x19)
    Sleep(80)
    OP_25(0x1F1, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(80)
    OP_25(0x1F1, 0x23)
    OP_25(0x339, 0x23)
    Sleep(80)
    OP_25(0x1F1, 0x28)
    OP_25(0x339, 0x28)
    Sleep(80)
    OP_25(0x1F1, 0x2D)
    OP_25(0x339, 0x2D)
    Sleep(80)
    OP_25(0x1F1, 0x32)
    OP_25(0x339, 0x32)
    Sleep(80)
    OP_25(0x1F1, 0x37)
    Sleep(80)
    OP_25(0x1F1, 0x3C)
    Return()

    # Function_57_A592 end

    def Function_58_A605(): pass

    label("Function_58_A605")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51258.itc", 0x1E)
    OP_68(-39500, 1000, 106000, 0)
    MoveCamera(49, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x1)
    SetChrFlags(0x25, 0x10)
    SetChrFlags(0x25, 0x20)
    SetChrFlags(0x25, 0x2)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -39500, 0, 106000, 270)
    SetCameraDistance(15500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0302
    ChrTalk(
        0x25,
        (
            "#00607F#11P他们竟然直接\x01",
            "冲向这边？！\x02\x03",

            "#00606F可恶，盗取构造图，原来就是为了这个……\x02\x03",

            "#00610F总之，让待命中的警备队员\x01",
            "立刻赶过来——\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetCameraDistance(15000, 300)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)

    #C0303
    ChrTalk(
        0x25,
        "#00607F#4S#11P什么！？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 3)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_A605 end

    def Function_59_A766(): pass

    label("Function_59_A766")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02450.itc", 0x5)
    LoadChrToIndex("chr/ch02451.itc", 0x6)
    LoadChrToIndex("chr/ch00950.itc", 0x7)
    LoadChrToIndex("chr/ch00951.itc", 0x8)
    LoadChrToIndex("chr/ch00952.itc", 0x9)
    LoadChrToIndex("chr/ch00953.itc", 0xA)
    LoadChrToIndex("chr/ch42250.itc", 0xB)
    LoadChrToIndex("chr/ch42251.itc", 0xC)
    LoadChrToIndex("chr/ch42252.itc", 0xD)
    LoadChrToIndex("chr/ch42253.itc", 0xE)
    LoadChrToIndex("chr/ch42254.itc", 0xF)
    LoadChrToIndex("chr/ch42350.itc", 0x10)
    LoadChrToIndex("chr/ch42351.itc", 0x11)
    LoadChrToIndex("chr/ch42352.itc", 0x12)
    LoadChrToIndex("chr/ch42353.itc", 0x13)
    LoadChrToIndex("chr/ch42550.itc", 0x14)
    LoadChrToIndex("chr/ch42551.itc", 0x15)
    LoadChrToIndex("chr/ch42552.itc", 0x16)
    LoadChrToIndex("chr/ch42553.itc", 0x17)
    LoadChrToIndex("chr/ch42554.itc", 0x18)
    LoadChrToIndex("apl/ch51236.itc", 0x19)
    LoadChrToIndex("apl/ch51262.itc", 0x1A)
    LoadChrToIndex("apl/ch51263.itc", 0x1B)
    LoadChrToIndex("apl/ch51264.itc", 0x1C)
    LoadChrToIndex("apl/ch51237.itc", 0x1D)
    LoadChrToIndex("apl/ch51265.itc", 0x1E)
    LoadChrToIndex("apl/ch51238.itc", 0x1F)
    LoadChrToIndex("apl/ch51267.itc", 0x20)
    LoadChrToIndex("chr/ch02452.itc", 0x21)
    LoadChrToIndex("chr/ch02456.itc", 0x22)
    LoadChrToIndex("chr/ch00900.itc", 0x23)
    LoadChrToIndex("apl/ch51223.itc", 0x24)
    LoadChrToIndex("apl/ch51266.itc", 0x25)
    LoadChrToIndex("apl/ch51268.itc", 0x26)
    LoadChrToIndex("chr/ch00959.itc", 0x27)
    LoadEffect(0x0, "event/ev12013.eff")
    LoadEffect(0x1, "battle/btgun00.eff")
    LoadEffect(0x2, "event/ev606_00.eff")
    LoadEffect(0x3, "battle/cr425100.eff")
    LoadEffect(0x4, "event/ev12012.eff")
    LoadEffect(0x5, "event/eva01_01.eff")
    SoundLoad(860)
    SoundLoad(861)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, -15000, 0, 0, 90)
    SetChrPos(0x102, -15000, 0, 500, 90)
    SetChrPos(0x103, -15000, 0, 0, 90)
    SetChrPos(0x104, -15000, 0, 1000, 90)
    SetChrPos(0x109, -15000, 0, -1000, 90)
    SetChrPos(0x105, -15000, 0, -1000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x5)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 12000, 0, 0, 270)
    EndChrThread(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 13000, 0, 0, 270)
    EndChrThread(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x1D)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 14000, 0, 0, 270)
    SetChrChipByIndex(0x25, 0x9)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 23700, 0, -800, 90)
    SetChrChipByIndex(0x36, 0x19)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 23900, 0, 1000, 90)
    SetChrChipByIndex(0x37, 0x19)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, 24400, 0, -1900, 90)
    SetChrChipByIndex(0x26, 0xC)
    SetChrSubChip(0x26, 0x0)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 81000, 0, 5500, 180)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0xC)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 80500, 0, 5500, 180)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x28, 0xC)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 81500, 0, 5500, 180)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x29, 0xC)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 80500, 0, 5500, 180)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2A, 0xC)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, 81500, 0, 5500, 180)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2E, 0x15)
    SetChrSubChip(0x2E, 0x0)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 81000, 0, 5500, 180)
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x2F, 0x15)
    SetChrSubChip(0x2F, 0x0)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 80500, 0, 5500, 180)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 81500, 0, 5500, 180)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x31, 0x15)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, 80500, 0, 5500, 180)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x32, 0x15)
    SetChrSubChip(0x32, 0x0)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrPos(0x32, 81500, 0, 5500, 180)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x4)
    OP_68(79000, 2500, 0, 0)
    MoveCamera(60, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_68(79000, 1500, 0, 3000)
    FadeToBright(2000, 0)
    Sleep(2500)
    Sound(160, 0, 100, 0)
    Sleep(300)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)
    OP_68(72000, 1500, 0, 4000)
    MoveCamera(53, 13, 0, 4000)
    SetCameraDistance(17000, 4000)
    BeginChrThread(0x2E, 3, 0, 83)
    Sleep(400)
    BeginChrThread(0x2F, 3, 0, 84)
    Sleep(200)
    Sound(937, 0, 100, 0)
    BeginChrThread(0x30, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x31, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x32, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x26, 3, 0, 83)
    Sleep(400)
    BeginChrThread(0x27, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x28, 3, 0, 85)
    Sleep(400)
    BeginChrThread(0x29, 3, 0, 84)
    Sleep(200)
    BeginChrThread(0x2A, 3, 0, 85)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_A7(0x2E, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2F, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x32, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x2F, 0xFF)
    EndChrThread(0x30, 0xFF)
    EndChrThread(0x31, 0xFF)
    EndChrThread(0x32, 0xFF)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    EndChrThread(0x26, 0xFF)
    EndChrThread(0x27, 0xFF)
    EndChrThread(0x28, 0xFF)
    EndChrThread(0x29, 0xFF)
    EndChrThread(0x2A, 0xFF)
    ClearChrFlags(0x46, 0x80)
    OP_78(0xF, 0x46)
    OP_49()
    SetChrPos(0x46, 25500, 0, 0, 0)
    OP_D5(0x46, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    SetChrChipByIndex(0x2E, 0x16)
    SetChrSubChip(0x2E, 0x3)
    SetChrChipByIndex(0x2F, 0x16)
    SetChrSubChip(0x2F, 0x3)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    SetChrChipByIndex(0x32, 0x16)
    SetChrSubChip(0x32, 0x3)
    SetChrPos(0x2E, 32800, 0, 1500, 270)
    SetChrPos(0x2F, 32200, 0, -100, 270)
    SetChrPos(0x30, 37500, 0, 300, 270)
    OP_A7(0x30, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x31, 37500, 0, -300, 270)
    OP_A7(0x31, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x32, 33700, 0, -2500, 270)
    OP_68(32900, 900, 0, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(29200, 900, 0, 4000)
    SetCameraDistance(17500, 4000)
    ClearScenarioFlags(0x0, 1)
    FadeToBright(1000, 0)
    BeginChrThread(0x2E, 3, 0, 101)
    BeginChrThread(0x36, 3, 0, 88)
    BeginChrThread(0x4C, 1, 0, 122)
    BeginChrThread(0x4C, 2, 0, 123)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 26000, 700, 700, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sound(860, 2, 80, 0)
    Sleep(100)
    BeginChrThread(0x2F, 3, 0, 100)
    BeginChrThread(0x37, 3, 0, 88)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 26400, 700, -1600, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    BeginChrThread(0x32, 3, 0, 101)
    BeginChrThread(0x25, 3, 0, 89)
    PlayEffect(0x3, 0x3, 0xFF, 0x0, 27500, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    BeginChrThread(0x101, 3, 0, 82)
    Sound(861, 2, 80, 0)
    OP_0D()
    Sleep(500)
    BeginChrThread(0x30, 3, 0, 86)
    Sleep(500)
    BeginChrThread(0x31, 3, 0, 87)
    Sound(2512, 255, 100, 0)    #voice#Dudley
    Sleep(3000)
    Sound(2513, 255, 100, 0)    #voice#Dudley
    OP_6F(0x79)
    OP_AD(0x1)
    EndChrThread(0x2F, 0x3)
    SetChrChipByIndex(0x2F, 0x18)
    SetChrSubChip(0x2F, 0x2)
    Sleep(100)
    SetChrSubChip(0x2F, 0x3)
    Sleep(200)
    SetChrSubChip(0x2F, 0x4)
    Sound(809, 0, 100, 0)
    Sound(250, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0x2F, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    EndChrThread(0x101, 0x3)
    EndChrThread(0x4C, 0x1)
    OP_68(24000, 500, 0, 500)
    MoveCamera(35, 25, 0, 500)
    SetCameraDistance(15500, 500)
    StopEffect(0x1, 0x0)
    StopEffect(0x2, 0x0)
    OP_82(0x12C, 0x12C, 0xBB8, 0x3E8)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 26000, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    ClearMapObjFlags(0x10, 0x4)
    OP_75(0xF, 0x1, 0x12C)
    OP_75(0x10, 0x2, 0x12C)
    EndChrThread(0x36, 0x3)
    BeginChrThread(0x36, 3, 0, 102)
    Sleep(50)
    EndChrThread(0x37, 0x3)
    BeginChrThread(0x37, 3, 0, 103)
    Sleep(50)
    EndChrThread(0x25, 0x3)
    BeginChrThread(0x25, 3, 0, 104)
    StopSound(860, 3000, 70)
    StopSound(861, 3000, 70)

    #C0304
    ChrTalk(
        0x36,
        "#13A呜哇～！\x02",
    )
    #Auto

    Sleep(50)

    #C0305
    ChrTalk(
        0x37,
        "#5P#13A啊！\x02",
    )
    #Auto

    Sleep(50)

    #C0306
    ChrTalk(
        0x25,
        "#6P#00610F#13A唔……！\x02",
    )
    #Auto

    WaitChrThread(0x25, 3)
    OP_6F(0x79)
    LoadEffect(0x0, "battle/cr024101.eff")
    LoadEffect(0x4, "battle/cr024100.eff")
    LoadEffect(0x6, "battle/cr024201.eff")
    LoadEffect(0x7, "battle/cr024401.eff")
    Fade(500)
    OP_68(34500, 700, 0, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15500, 0)
    OP_68(33500, 700, 0, 2000)
    SetCameraDistance(17500, 2000)
    StopEffect(0x3, 0x0)
    SetChrPos(0x2E, 32800, 0, 2500, 270)
    SetChrChipByIndex(0x2E, 0x14)
    SetChrSubChip(0x2E, 0x0)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x4C, 0x2)
    SetChrPos(0x2F, 32200, 0, 900, 270)
    SetChrChipByIndex(0x2F, 0x14)
    SetChrSubChip(0x2F, 0x0)
    EndChrThread(0x2F, 0xFF)
    SetChrPos(0x30, 34200, 0, 1500, 270)
    SetChrChipByIndex(0x30, 0x14)
    SetChrSubChip(0x30, 0x0)
    EndChrThread(0x30, 0xFF)
    SetChrPos(0x31, 33400, 0, -1800, 270)
    SetChrChipByIndex(0x31, 0x14)
    SetChrSubChip(0x31, 0x0)
    EndChrThread(0x31, 0xFF)
    SetChrPos(0x32, 33700, 0, -3000, 270)
    SetChrChipByIndex(0x32, 0x14)
    SetChrSubChip(0x32, 0x0)
    EndChrThread(0x32, 0xFF)
    SetChrPos(0x26, 37700, 0, -300, 270)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x27, 38900, 0, -1000, 270)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x28, 38900, 0, 0, 270)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x29, 40200, 0, -650, 270)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x25, 19700, 0, -1500, 90)
    SetChrPos(0x36, 21100, 0, 2900, 135)
    SetChrPos(0x37, 21100, 0, -3300, 90)
    SetMapObjFlags(0xF, 0x4)
    SetChrChipByIndex(0x26, 0xC)
    SetChrSubChip(0x26, 0x0)

    def lambda_B390():
        OP_95(0xFE, 29700, 0, -300, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_B390)

    def lambda_B3AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_B3AA)
    Sleep(100)
    SetChrChipByIndex(0x27, 0xC)
    SetChrSubChip(0x27, 0x0)

    def lambda_B3C6():
        OP_95(0xFE, 30900, 0, -1000, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_B3C6)

    def lambda_B3E0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x27, 2, lambda_B3E0)
    Sleep(100)
    SetChrChipByIndex(0x28, 0xC)
    SetChrSubChip(0x28, 0x0)

    def lambda_B3FC():
        OP_95(0xFE, 30900, 0, 0, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_B3FC)

    def lambda_B416():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_B416)
    Sleep(100)
    SetChrChipByIndex(0x29, 0xC)
    SetChrSubChip(0x29, 0x0)

    def lambda_B432():
        OP_95(0xFE, 32200, 0, -650, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_B432)

    def lambda_B44C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B44C)
    WaitChrThread(0x26, 1)
    SetChrChipByIndex(0x26, 0xB)
    SetChrSubChip(0x26, 0x0)
    WaitChrThread(0x27, 1)
    SetChrChipByIndex(0x27, 0xB)
    SetChrSubChip(0x27, 0x0)
    WaitChrThread(0x28, 1)
    SetChrChipByIndex(0x28, 0xB)
    SetChrSubChip(0x28, 0x0)
    WaitChrThread(0x29, 1)
    SetChrChipByIndex(0x29, 0xB)
    SetChrSubChip(0x29, 0x0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0307
    ChrTalk(
        0x26,
        "#11P#4S就是现在……！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0308
    ChrTalk(
        0x27,
        "#11P#4S取下宰相的首级！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x26, 3, 0, 105)
    BeginChrThread(0x17, 3, 0, 81)
    Sleep(150)
    BeginChrThread(0x27, 3, 0, 106)
    Sleep(150)
    BeginChrThread(0x28, 3, 0, 107)
    Sleep(150)
    BeginChrThread(0x29, 3, 0, 108)
    Fade(250)
    OP_68(24000, 700, 0, 0)
    MoveCamera(43, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(43, 25, -10, 1000)
    SetCameraDistance(16500, 1000)
    OP_0D()
    WaitChrThread(0x17, 3)

    #C0309
    ChrTalk(
        0x17,
        "#01401F#5P此路不通。\x02",
    )

    CloseMessageWindow()

    def lambda_B579():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_B579)
    Sleep(500)

    def lambda_B595():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_B595)
    Sleep(300)
    SetChrSubChip(0x26, 0x1)
    Sleep(90)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 30, 0)
    SetChrChipByIndex(0x26, 0xB)
    SetChrSubChip(0x26, 0x0)
    Sleep(300)
    SetChrSubChip(0x29, 0x2)
    Sleep(90)
    SetChrSubChip(0x29, 0x1)
    Sleep(90)
    Sound(802, 0, 100, 0)
    Sound(531, 0, 30, 0)
    SetChrChipByIndex(0x29, 0xB)
    SetChrSubChip(0x29, 0x0)

    #C0310
    ChrTalk(
        0x26,
        "#11P唔，是『风之剑圣』吗！？\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x31,
        (
            "#11P别退缩！\x01",
            "发动波浪式攻击！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(23500, 900, 0, 2000)
    MoveCamera(50, 21, 0, 2000)
    SetCameraDistance(17000, 2000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0xA, 11700, 0, 2100, 90)
    SetChrPos(0x9, 11100, 0, 700, 90)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)

    def lambda_B68F():
        OP_95(0xFE, 19400, 0, 1100, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_B68F)
    Sleep(200)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)

    def lambda_B6B4():
        OP_95(0xFE, 18900, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_B6B4)
    WaitChrThread(0xA, 1)
    Sound(318, 0, 100, 0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0x9, 1)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0x9, 0x1D)
    SetChrSubChip(0x9, 0x0)

    #C0312
    ChrTalk(
        0xA,
        "#07107F#5P我来助你一臂之力！\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x9,
        "#07307F#5P赶快把伤员带走！\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x25,
        "#00610F#6P#N感激不尽！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x25, 3, 0, 62)
    Sleep(300)
    BeginChrThread(0x36, 3, 0, 60)

    #C0315
    ChrTalk(
        0x26,
        "#12P穆拉·范德尔！\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x29,
        "#12P亚诺尔家族的守护者！\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x2E,
        "#11P另一个是利贝尔亲卫队的……！？\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x2F,
        "#11P别管那么多，干掉他们！\x02",
    )

    CloseMessageWindow()
    LoadEffect(0x0, "event/ev12015.eff")
    LoadEffect(0x2, "event/ev12017.eff")
    LoadEffect(0x4, "event/ev12018.eff")
    LoadEffect(0x8, "event/ev12019.eff")
    LoadEffect(0x6, "battle/ms00001.eff")
    OP_68(29000, 700, 0, 5000)
    MoveCamera(45, 21, 0, 5000)
    SetCameraDistance(16500, 5000)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 101)
    BeginChrThread(0x4C, 2, 0, 123)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 28000, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sound(860, 2, 80, 0)
    Sound(861, 2, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x2E, 0x16)
    SetChrSubChip(0x2E, 0x3)
    BeginChrThread(0x2E, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x2F, 0x16)
    SetChrSubChip(0x2F, 0x3)
    BeginChrThread(0x2F, 3, 0, 101)
    Sleep(50)
    SetChrChipByIndex(0x32, 0x16)
    SetChrSubChip(0x32, 0x3)
    BeginChrThread(0x32, 3, 0, 101)
    Sleep(100)
    BeginChrThread(0x17, 0, 0, 74)
    Sleep(1500)
    BeginChrThread(0xA, 0, 0, 69)
    BeginChrThread(0x9, 0, 0, 63)
    Sleep(3300)
    EndChrThread(0x25, 0x3)
    BeginChrThread(0x25, 0, 0, 73)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    StopSound(860, 1000, 75)
    StopSound(861, 1000, 75)
    OP_0D()
    OP_49()
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x36, 0x80)
    SetChrFlags(0x37, 0x80)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x25, 0xFF)
    EndChrThread(0x36, 0xFF)
    EndChrThread(0x37, 0xFF)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    EndChrThread(0x26, 0xFF)
    EndChrThread(0x27, 0xFF)
    EndChrThread(0x28, 0xFF)
    EndChrThread(0x29, 0xFF)
    EndChrThread(0x4C, 0x2)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    SetChrFlags(0x32, 0x80)
    EndChrThread(0x2E, 0xFF)
    EndChrThread(0x2F, 0xFF)
    EndChrThread(0x30, 0xFF)
    EndChrThread(0x31, 0xFF)
    EndChrThread(0x32, 0xFF)
    LoadChrToIndex("chr/ch00050.itc", 0x5)
    LoadChrToIndex("chr/ch00150.itc", 0x6)
    LoadChrToIndex("chr/ch00250.itc", 0x7)
    LoadChrToIndex("chr/ch00350.itc", 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x9)
    LoadChrToIndex("chr/ch03050.itc", 0xA)
    LoadChrToIndex("monster/ch84150.itc", 0xB)
    LoadChrToIndex("monster/ch84250.itc", 0xC)
    LoadChrToIndex("monster/ch84350.itc", 0xD)
    SoundLoad(943)
    SoundLoad(863)
    SetChrChipByIndex(0x49, 0xB)
    SetChrSubChip(0x49, 0x0)
    SetChrFlags(0x49, 0x8000)
    SetChrPos(0x49, -17500, 0, 0, 90)
    OP_A7(0x49, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x4A, 0xC)
    SetChrSubChip(0x4A, 0x0)
    SetChrFlags(0x4A, 0x8000)
    SetChrPos(0x4A, -17500, 0, 0, 90)
    OP_A7(0x4A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x4B, 0xD)
    SetChrSubChip(0x4B, 0x0)
    SetChrFlags(0x4B, 0x8000)
    SetChrPos(0x4B, -17500, 0, 0, 90)
    OP_A7(0x4B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-6000, 1100, 0, 0)
    MoveCamera(39, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    OP_68(7000, 1100, 0, 5000)
    SetCameraDistance(18000, 5000)
    FadeToBright(1000, 0)
    Sound(863, 2, 60, 0)
    BeginChrThread(0x4C, 1, 0, 124)
    BeginChrThread(0x101, 3, 0, 90)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 91)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 92)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 93)
    BeginChrThread(0x105, 3, 0, 95)
    Sleep(200)
    BeginChrThread(0x109, 3, 0, 94)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)

    #C0319
    ChrTalk(
        0x101,
        "#00011F好厉害……！\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x104,
        "#6P#00306F真强啊……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x102,
        "#00102F#5P看样子，应该没问题了……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 9500, 0, 5000, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Sound(121, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    Sleep(150)
    OP_68(8500, 1300, 1500, 1200)

    def lambda_BBD2():
        OP_96(0xFE, 0x251C, 0x0, 0xE10, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BBD2)

    def lambda_BBEC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BBEC)
    WaitChrThread(0x8, 1)
    OP_93(0x8, 0xE1, 0x1F4)

    def lambda_BC08():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BC08)
    Sleep(50)

    def lambda_BC18():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BC18)
    Sleep(50)

    def lambda_BC28():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_BC28)
    Sleep(50)

    def lambda_BC38():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BC38)
    Sleep(50)

    def lambda_BC48():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_BC48)
    Sleep(50)

    def lambda_BC58():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BC58)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    #C0322
    ChrTalk(
        0x8,
        "#5P#11505F哦，来了啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0323
    ChrTalk(
        0x101,
        "#12P#00001F雷克特先生……！\x02",
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x102,
        (
            "#6P#00101F出席会议的各位代表\x01",
            "都没事吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x8,
        "#5P#11503F嗯，目前是的。\x02",
    )

    CloseMessageWindow()
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 10500, 0, 5000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_BD3E():
        OP_96(0xFE, 0x2904, 0x0, 0xDAC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_BD3E)

    def lambda_BD58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BD58)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0xE1, 0x1F4)

    #C0326
    ChrTalk(
        0xB,
        (
            "#11P#12001F……有话稍后再说，\x01",
            "后面也来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x101,
        "#12P#00005F咦……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BDF1():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BDF1)
    Sleep(50)
    OP_93(0x105, 0x10E, 0x1F4)

    #C0328
    ChrTalk(
        0x103,
        "#11P#00201F确认到了机械音……！\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x105,
        "#11P#10301F好像有什么东西过来了呢。\x02",
    )

    CloseMessageWindow()

    def lambda_BE56():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_BE56)
    Sleep(50)

    def lambda_BE66():
        OP_93(0x104, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_BE66)
    Sleep(50)

    def lambda_BE76():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_BE76)
    Sleep(50)

    def lambda_BE86():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_BE86)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    def lambda_BEA6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BEA6)

    def lambda_BEB3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BEB3)
    Fade(500)
    OP_68(-13900, 900, 0, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    OP_68(2100, 900, 0, 4500)
    MoveCamera(30, 23, 0, 4500)
    SetCameraDistance(18000, 4500)
    ClearChrFlags(0x49, 0x80)
    ClearChrFlags(0x4A, 0x80)
    ClearChrFlags(0x4B, 0x80)
    Sound(943, 2, 70, 0)
    BeginChrThread(0x49, 3, 0, 96)
    Sleep(600)
    BeginChrThread(0x4A, 3, 0, 97)
    Sleep(600)
    BeginChrThread(0x4B, 3, 0, 98)
    OP_6F(0x79)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x5)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x6)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x8)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x9)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xA)
    SetChrSubChip(0x105, 0x0)
    OP_0D()

    #C0330
    ChrTalk(
        0x109,
        "#12P#10111F这、这是……！？\x02",
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x104,
        (
            "#11P#00307F和黑手党据点中的\x01",
            "那种东西很相似！\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        "#00007F总之，先把它们击退！\x02",
    )

    CloseMessageWindow()
    StopSound(863, 500, 60)
    EndChrThread(0x4C, 0x1)
    Sound(943, 2, 70, 0)
    EndChrThread(0x49, 0x3)
    EndChrThread(0x4A, 0x3)
    EndChrThread(0x4B, 0x3)

    def lambda_C019():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x49, 1, lambda_C019)

    def lambda_C033():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x4A, 1, lambda_C033)

    def lambda_C04D():
        OP_98(0xFE, 0x1388, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x4B, 1, lambda_C04D)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(3100, 900, 0, 500)
    SetCameraDistance(16000, 500)
    Sleep(500)
    EndChrThread(0x49, 0xFF)
    EndChrThread(0x4A, 0xFF)
    EndChrThread(0x4B, 0xFF)
    OP_24(0x3AF)
    OP_24(0x35C)
    OP_24(0x35D)
    Battle("BattleInfo_B70", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x49, 0x80)
    SetChrFlags(0x4A, 0x80)
    SetChrFlags(0x4B, 0x80)
    Call(0, 125)
    Return()

    # Function_59_A766 end

    def Function_60_C0CD(): pass

    label("Function_60_C0CD")


    def lambda_C0D2():
        OP_A6(0xFE, 0x0, 0x1E, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C0D2)
    Sleep(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    OP_93(0xFE, 0x5A, 0x0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(200)

    def lambda_C111():
        OP_96(0xFE, 0x4844, 0x0, 0xB54, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C111)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_C139():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C139)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_60_C0CD end

    def Function_61_C15E(): pass

    label("Function_61_C15E")


    def lambda_C163():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C163)
    SetChrChipByIndex(0xFE, 0x1B)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x0)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_C19C():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x320, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C19C)
    WaitChrThread(0xFE, 1)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Return()

    # Function_61_C15E end

    def Function_62_C1C1(): pass

    label("Function_62_C1C1")


    def lambda_C1C6():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C1C6)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C1F2():
        OP_95(0xFE, 21300, 0, -2500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C1F2)
    WaitChrThread(0xFE, 1)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0xB4, 0x1F4)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0x37, 3, 0, 61)
    Sleep(1300)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)

    def lambda_C248():
        OP_98(0xFE, 0xFFFFE4A8, 0x0, 0x320, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C248)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x7)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    Return()

    # Function_62_C1C1 end

    def Function_63_C271(): pass

    label("Function_63_C271")

    Sleep(100)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C281():
        OP_95(0xFE, 22000, 0, -2400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C281)
    WaitChrThread(0xFE, 1)
    Sound(288, 0, 100, 0)

    def lambda_C2A5():
        OP_95(0xFE, 24000, 0, -2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C2A5)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x25)
    SetChrSubChip(0xFE, 0x4)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)

    def lambda_C2ED():
        OP_9D(0xFE, 0x6E8C, 0x0, 0xFFFFF6A0, 0x514, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C2ED)
    Sleep(300)
    Sound(540, 0, 100, 0)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    SetChrSubChip(0xFE, 0x6)
    BeginChrThread(0x27, 3, 0, 64)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x7)
    OP_82(0x0, 0xC8, 0xBB8, 0x12C)
    Sleep(400)
    SetChrSubChip(0xFE, 0x8)

    def lambda_C344():
        OP_9D(0xFE, 0x66BC, 0x0, 0xFFFFF7CC, 0x1F4, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C344)
    WaitChrThread(0xFE, 1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x9)
    Sound(257, 0, 100, 0)
    PlayEffect(0x0, 0x2, 0xFE, 0x5, 300, 900, 1200, -20, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFE, 0x5, 300, 900, 1200, 10, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    EndChrThread(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 65)
    EndChrThread(0x32, 0x3)
    BeginChrThread(0x32, 3, 0, 67)
    Sleep(2000)
    StopEffect(0x2, 0x0)
    StopEffect(0x3, 0x0)
    SetChrSubChip(0xFE, 0xA)
    Sleep(30)
    SetChrSubChip(0xFE, 0xC)
    Sleep(30)
    SetChrSubChip(0xFE, 0xE)
    Sleep(30)
    Sound(538, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    BeginChrThread(0x31, 3, 0, 66)
    BeginChrThread(0x32, 3, 0, 68)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(90)
    SetChrSubChip(0xFE, 0x3)
    Sleep(300)
    Return()

    # Function_63_C271 end

    def Function_64_C473(): pass

    label("Function_64_C473")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_C4C7():
        OP_93(0xFE, 0x10E, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_C4C7)

    def lambda_C4D4():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C4D4)

    def lambda_C4ED():
        OP_9D(0xFE, 0x7BD4, 0x0, 0xFFFFF3E4, 0x514, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C4ED)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_64_C473 end

    def Function_65_C513(): pass

    label("Function_65_C513")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C530():
        OP_96(0xFE, 0x6DC4, 0x0, 0xFFFFF830, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C530)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_65_C513 end

    def Function_66_C54A(): pass

    label("Function_66_C54A")

    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_C586():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C586)

    def lambda_C59F():
        OP_9D(0xFE, 0x7C9C, 0x0, 0xFFFFF8F8, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C59F)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_66_C54A end

    def Function_67_C5C5(): pass

    label("Function_67_C5C5")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C5E2():
        OP_96(0xFE, 0x6DC4, 0x0, 0xFFFFF4AC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C5E2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_67_C5C5 end

    def Function_68_C5FC(): pass

    label("Function_68_C5FC")

    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)

    def lambda_C638():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C638)

    def lambda_C651():
        OP_9D(0xFE, 0x7DC8, 0x0, 0xFFFFF254, 0x384, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C651)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_68_C5FC end

    def Function_69_C677(): pass

    label("Function_69_C677")

    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C684():
        OP_95(0xFE, 22000, 0, 2400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C684)
    WaitChrThread(0xFE, 1)

    def lambda_C6A2():
        OP_95(0xFE, 24000, 0, 2400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C6A2)
    WaitChrThread(0xFE, 1)
    Sound(318, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    SetChrSubChip(0xFE, 0x3)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x10)
    SetChrFlags(0xFE, 0x2)
    BeginChrThread(0x28, 3, 0, 70)
    Sleep(100)
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C72B():
        OP_95(0xFE, 28000, 0, 2400, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C72B)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    BeginChrThread(0x26, 3, 0, 71)
    Sleep(300)
    SetChrSubChip(0xFE, 0x3)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_C769():
        OP_9D(0xFE, 0x67E8, 0x0, 0x3E8, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C769)
    WaitChrThread(0xFE, 1)

    def lambda_C78A():
        OP_9D(0xFE, 0x6400, 0x0, 0x7D0, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C78A)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x0)
    Sleep(550)
    SetChrSubChip(0xFE, 0x6)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C80B():
        OP_95(0xFE, 28600, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C80B)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)

    def lambda_C838():
        OP_9D(0xFE, 0x6978, 0x0, 0x7D0, 0x2BC, 0x1194)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C838)
    WaitChrThread(0xFE, 1)
    Sound(329, 0, 100, 0)
    PlayEffect(0x4, 0xFF, 0xFE, 0x3, 1000, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C896():
        OP_95(0xFE, 30300, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C896)
    SetChrSubChip(0xFE, 0x4)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x5)
    Sleep(500)
    Return()

    # Function_69_C677 end

    def Function_70_C8BB(): pass

    label("Function_70_C8BB")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C8C8():
        OP_95(0xFE, 28200, 0, 2000, 10000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C8C8)
    WaitChrThread(0xFE, 1)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C92A():
        TurnDirection(0xFE, 0xA, 0)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_C92A)

    def lambda_C937():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_C937)

    def lambda_C950():
        OP_9D(0xFE, 0x7A44, 0x0, 0xCE4, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C950)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_70_C8BB end

    def Function_71_C976(): pass

    label("Function_71_C976")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_C983():
        OP_95(0xFE, 29000, 0, 1400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C983)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)

    def lambda_C9B8():
        OP_95(0xFE, 28000, 0, 2000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_C9B8)
    SetChrSubChip(0xFE, 0x2)
    Sleep(70)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Sleep(400)
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    TurnDirection(0xFE, 0xA, 500)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)

    def lambda_CA10():
        OP_95(0xFE, 26700, 0, 2000, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA10)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x1)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 26500, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_CA69():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CA69)

    def lambda_CA82():
        OP_96(0xFE, 0x6F54, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CA82)
    WaitChrThread(0xFE, 1)
    Sleep(450)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28300, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_CAE2():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CAE2)

    def lambda_CAFB():
        OP_96(0xFE, 0x79E0, 0x0, 0x7D0, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CAFB)
    WaitChrThread(0xFE, 1)
    Sleep(600)
    PlayEffect(0x6, 0xFF, 0xFE, 0x0, -100, 1000, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_CB5B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CB5B)

    def lambda_CB74():
        OP_9D(0xFE, 0x8084, 0x0, 0x7D0, 0x258, 0x2328)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CB74)
    Sleep(50)
    EndChrThread(0x2E, 0x3)
    BeginChrThread(0x2E, 3, 0, 72)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_71_C976 end

    def Function_72_CBA2(): pass

    label("Function_72_CBA2")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_CBAF():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CBAF)

    def lambda_CBC8():
        OP_9D(0xFE, 0x86C4, 0x0, 0xBB8, 0x2BC, 0x1B58)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CBC8)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_72_CBA2 end

    def Function_73_CBE9(): pass

    label("Function_73_CBE9")

    SetChrPos(0x25, 17000, 0, 1800, 90)
    SetChrChipByIndex(0xFE, 0x8)
    SetChrSubChip(0xFE, 0x0)

    def lambda_CC07():
        OP_96(0xFE, 0x6400, 0x0, 0x514, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_CC07)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x9)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    BeginChrThread(0x25, 0, 0, 89)
    Return()

    # Function_73_CBE9 end

    def Function_74_CC32(): pass

    label("Function_74_CC32")

    BeginChrThread(0x17, 3, 0, 75)
    BeginChrThread(0x17, 2, 0, 77)
    Sound(3987, 255, 100, 0)    #voice#Arios
    Sound(264, 0, 100, 0)
    Sound(833, 0, 70, 0)
    Sleep(1300)
    BeginChrThread(0x17, 3, 0, 75)
    BeginChrThread(0x17, 2, 0, 77)
    Sound(264, 0, 100, 0)
    Sound(833, 0, 70, 0)
    Sleep(1300)
    BeginChrThread(0x17, 3, 0, 76)
    Return()

    # Function_74_CC32 end

    def Function_75_CC75(): pass

    label("Function_75_CC75")

    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x3)
    Sound(859, 0, 100, 0)
    Sound(534, 0, 100, 0)
    Sleep(100)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(60)
    Sound(569, 0, 100, 0)
    Sound(540, 0, 70, 0)
    SetChrSubChip(0x17, 0x1)
    Sleep(120)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(60)
    SetChrSubChip(0x17, 0x3)
    Sleep(180)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(60)
    SetChrSubChip(0x17, 0x1)
    Sleep(700)
    Return()

    # Function_75_CC75 end

    def Function_76_CCCF(): pass

    label("Function_76_CCCF")

    Sleep(500)
    BeginChrThread(0x29, 3, 0, 78)

    def lambda_CCDD():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CCDD)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 0, 0, 93, 0, 90, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x17, 0x3)
    Sleep(1200)

    def lambda_CD42():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CD42)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x3)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 500, 0, 85, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    Sleep(90)
    SetChrSubChip(0x17, 0x1)
    Sleep(300)
    EndChrThread(0x2F, 0x3)
    BeginChrThread(0x2F, 3, 0, 79)
    Sleep(100)
    EndChrThread(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 80)
    StopEffect(0x1, 0x0)
    Sleep(1100)

    def lambda_CDCF():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_CDCF)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    Sleep(270)
    PlayEffect(0x8, 0xFF, 0xFE, 0x0, 0, 0, 0, 95, 0, 90, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    SetChrSubChip(0x17, 0x3)
    Sleep(1500)
    Return()

    # Function_76_CCCF end

    def Function_77_CE30(): pass

    label("Function_77_CE30")

    StopEffect(0x1, 0x0)
    PlayEffect(0x7, 0xFF, 0x17, 0x3, 0, 500, 0, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1500, -3000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1250, -1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28000, 2000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x78)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(30)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, 28500, 1000, -2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x3, 0x1, 0xFF, 0x0, 28000, 0, 0, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    Sleep(180)
    Return()

    # Function_77_CE30 end

    def Function_78_D0E2(): pass

    label("Function_78_D0E2")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D0FA():
        OP_96(0xFE, 0x701C, 0x0, 0xFFFFFC7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D0FA)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D125():
        OP_A6(0xFE, 0x0, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D125)

    def lambda_D13E():
        OP_9D(0xFE, 0x89E4, 0x0, 0xFFFFFBB4, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D13E)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Sleep(1000)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D185():
        OP_96(0xFE, 0x701C, 0x0, 0xFFFFFC7C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D185)
    WaitChrThread(0xFE, 1)
    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D1B0():
        OP_A6(0xFE, 0x0, 0x32, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D1B0)

    def lambda_D1C9():
        OP_9D(0xFE, 0x89E4, 0x0, 0xFFFFFBB4, 0x2BC, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D1C9)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_78_D0E2 end

    def Function_79_D1EF(): pass

    label("Function_79_D1EF")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D1FC():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D1FC)

    def lambda_D215():
        OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D215)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Sleep(500)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x16)
    SetChrSubChip(0xFE, 0x3)
    BeginChrThread(0xFE, 3, 0, 101)
    Return()

    # Function_79_D1EF end

    def Function_80_D24E(): pass

    label("Function_80_D24E")

    SetChrChipByIndex(0xFE, 0x17)
    SetChrSubChip(0xFE, 0x0)

    def lambda_D25B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D25B)

    def lambda_D274():
        OP_9C(0xFE, 0x1F4, 0x0, 0x0, 0x1F4, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D274)
    WaitChrThread(0xFE, 1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_80_D24E end

    def Function_81_D295(): pass

    label("Function_81_D295")

    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, 13300, 0, 200, 90)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x17, 0x1E, 0xC8)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x2)
    PlayEffect(0x0, 0x0, 0x17, 0x3, 250, 1200, 500, 45, -45, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_D302():
        OP_9D(0xFE, 0x571C, 0x0, 0x0, 0xDAC, 0x514)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_D302)
    Sleep(500)
    Sound(844, 0, 70, 0)
    Sound(255, 0, 50, 0)
    Sound(3987, 255, 100, 0)    #voice#Arios
    WaitChrThread(0x17, 1)
    SetChrSubChip(0x17, 0x3)
    Sound(532, 0, 100, 0)
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    StopEffect(0x0, 0x0)
    PlayEffect(0x4, 0xFF, 0x17, 0x3, 0, 0, 2000, 0, 0, 0, 1100, 1100, 1100, 0xFF, 0, 0, 0, 0)
    Sound(332, 0, 100, 0)
    Sound(289, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x26, 3, 0, 109)
    Sleep(50)
    BeginChrThread(0x27, 3, 0, 111)
    BeginChrThread(0x28, 3, 0, 113)
    Sleep(50)
    BeginChrThread(0x29, 3, 0, 115)
    Sleep(700)
    OP_68(27000, 700, 0, 500)
    MoveCamera(55, 17, 0, 500)
    SetCameraDistance(16000, 500)
    Sound(534, 0, 100, 0)
    Sound(540, 0, 100, 0)
    Sound(3992, 255, 100, 0)    #voice#Arios
    SetChrFlags(0x17, 0x20)

    def lambda_D3FC():
        OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_D3FC)
    WaitChrThread(0x17, 1)
    ClearChrFlags(0x17, 0x20)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)
    PlayEffect(0x6, 0xFF, 0x17, 0x3, 0, 500, 0, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 0)
    Sound(264, 0, 100, 0)
    Sound(833, 0, 100, 0)
    BeginChrThread(0x26, 3, 0, 110)
    BeginChrThread(0x27, 3, 0, 112)
    BeginChrThread(0x28, 3, 0, 114)
    BeginChrThread(0x29, 3, 0, 116)
    Sleep(60)
    SetChrSubChip(0x17, 0x1)
    Sleep(1000)
    OP_6F(0x79)
    SetChrChip(0x1, 0x17, 0x0, 0x0)
    CancelBlur(0)
    SetChrSubChip(0x17, 0x2)
    Sleep(90)
    SetChrChipByIndex(0x17, 0x5)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_81_D295 end

    def Function_82_D4C3(): pass

    label("Function_82_D4C3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D592")
    OP_82(0x32, 0x32, 0xBB8, 0x4B0)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 31500, 0, -1700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 30500, 0, -1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 31000, 0, 700, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Jump("Function_82_D4C3")

    label("loc_D592")

    Return()

    # Function_82_D4C3 end

    def Function_83_D593(): pass

    label("Function_83_D593")


    def lambda_D598():
        OP_95(0xFE, 81000, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D598)

    def lambda_D5B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D5B2)
    WaitChrThread(0xFE, 1)

    def lambda_D5C7():
        OP_95(0xFE, 75000, 0, 0, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D5C7)
    WaitChrThread(0xFE, 1)

    def lambda_D5E5():
        OP_95(0xFE, 65000, 0, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D5E5)
    Sleep(1100)

    def lambda_D602():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D602)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_83_D593 end

    def Function_84_D613(): pass

    label("Function_84_D613")


    def lambda_D618():
        OP_95(0xFE, 80500, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D618)

    def lambda_D632():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D632)
    WaitChrThread(0xFE, 1)

    def lambda_D647():
        OP_95(0xFE, 75000, 0, -300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D647)
    WaitChrThread(0xFE, 1)

    def lambda_D665():
        OP_95(0xFE, 65000, 0, -300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D665)
    Sleep(1100)

    def lambda_D682():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D682)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_84_D613 end

    def Function_85_D693(): pass

    label("Function_85_D693")


    def lambda_D698():
        OP_95(0xFE, 81500, 0, 2200, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D698)

    def lambda_D6B2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D6B2)
    WaitChrThread(0xFE, 1)

    def lambda_D6C7():
        OP_95(0xFE, 75000, 0, 300, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6C7)
    WaitChrThread(0xFE, 1)

    def lambda_D6E5():
        OP_95(0xFE, 65000, 0, 300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D6E5)
    Sleep(1100)

    def lambda_D702():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D702)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_85_D693 end

    def Function_86_D713(): pass

    label("Function_86_D713")

    SetChrChipByIndex(0x30, 0x15)
    SetChrSubChip(0x30, 0x0)

    def lambda_D720():
        OP_96(0xFE, 0x88B8, 0x0, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D720)

    def lambda_D73A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D73A)
    WaitChrThread(0xFE, 1)

    def lambda_D74F():
        OP_96(0xFE, 0x8598, 0x0, 0x1F4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D74F)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x30, 0x16)
    SetChrSubChip(0x30, 0x3)
    BeginChrThread(0x30, 3, 0, 101)
    Return()

    # Function_86_D713 end

    def Function_87_D777(): pass

    label("Function_87_D777")

    SetChrChipByIndex(0x31, 0x15)
    SetChrSubChip(0x31, 0x0)

    def lambda_D784():
        OP_96(0xFE, 0x88B8, 0x0, 0xFFFFFED4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D784)

    def lambda_D79E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D79E)
    WaitChrThread(0xFE, 1)

    def lambda_D7B3():
        OP_96(0xFE, 0x8278, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D7B3)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x31, 0x16)
    SetChrSubChip(0x31, 0x3)
    BeginChrThread(0x31, 3, 0, 101)
    Return()

    # Function_87_D777 end

    def Function_88_D7DB(): pass

    label("Function_88_D7DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D830")
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 0, 1100, 1100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(500)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_88_D7DB")

    label("loc_D830")

    Return()

    # Function_88_D7DB end

    def Function_89_D831(): pass

    label("Function_89_D831")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D8A1")
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 0, 1200, 1100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(567, 0, 80, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(50)
    SetChrSubChip(0xFE, 0x2)
    Sleep(50)
    SetChrSubChip(0xFE, 0x3)
    Sleep(50)
    SetChrSubChip(0xFE, 0x4)
    Sleep(50)
    SetChrSubChip(0xFE, 0x0)
    Sleep(700)
    Jump("Function_89_D831")

    label("loc_D8A1")

    Return()

    # Function_89_D831 end

    def Function_90_D8A2(): pass

    label("Function_90_D8A2")


    def lambda_D8A7():
        OP_96(0xFE, 0x1B58, 0x0, 0xFFFFFF38, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D8A7)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_90_D8A2 end

    def Function_91_D8C1(): pass

    label("Function_91_D8C1")


    def lambda_D8C6():
        OP_96(0xFE, 0x1964, 0x0, 0x2BC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D8C6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_91_D8C1 end

    def Function_92_D8E0(): pass

    label("Function_92_D8E0")


    def lambda_D8E5():
        OP_96(0xFE, 0x1450, 0x0, 0x64, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D8E5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_92_D8E0 end

    def Function_93_D8FF(): pass

    label("Function_93_D8FF")


    def lambda_D904():
        OP_96(0xFE, 0x125C, 0x0, 0x3E8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D904)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_93_D8FF end

    def Function_94_D91E(): pass

    label("Function_94_D91E")


    def lambda_D923():
        OP_96(0xFE, 0x1324, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D923)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_94_D91E end

    def Function_95_D93D(): pass

    label("Function_95_D93D")


    def lambda_D942():
        OP_96(0xFE, 0x16A8, 0x0, 0xFFFFF8F8, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D942)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_95_D93D end

    def Function_96_D95C(): pass

    label("Function_96_D95C")


    def lambda_D961():
        OP_96(0xFE, 0xFFFFFE70, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D961)

    def lambda_D97B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D97B)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_96_D95C end

    def Function_97_D992(): pass

    label("Function_97_D992")


    def lambda_D997():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D997)

    def lambda_D9B1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_D9B1)
    WaitChrThread(0xFE, 1)

    def lambda_D9C6():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0x514, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D9C6)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_97_D992 end

    def Function_98_D9E6(): pass

    label("Function_98_D9E6")


    def lambda_D9EB():
        OP_96(0xFE, 0xFFFFE9BC, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_D9EB)

    def lambda_DA05():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DA05)
    WaitChrThread(0xFE, 1)

    def lambda_DA1A():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFFAEC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DA1A)
    WaitChrThread(0xFE, 1)
    BeginChrThread(0xFE, 3, 0, 99)
    Return()

    # Function_98_D9E6 end

    def Function_99_DA3A(): pass

    label("Function_99_DA3A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA55")
    OP_A1(0xFE, 0x5DC, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_99_DA3A")

    label("loc_DA55")

    Return()

    # Function_99_DA3A end

    def Function_100_DA56(): pass

    label("Function_100_DA56")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DBEC")
    ClearScenarioFlags(0x0, 1)
    SetChrSubChip(0xFE, 0x4)

    def lambda_DA6D():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DA6D)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    SetScenarioFlags(0x0, 1)
    Sleep(500)
    Jump("Function_100_DA56")

    label("loc_DBEC")

    Return()

    # Function_100_DA56 end

    def Function_101_DBED(): pass

    label("Function_101_DBED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD7D")
    SetChrSubChip(0xFE, 0x4)

    def lambda_DC01():
        OP_A6(0xFE, 0x0, 0x1E, 0x258, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DC01)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x1, 0xFF, 0xFE, 0x3, 100, 1100, 900, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(500)
    Jump("Function_101_DBED")

    label("loc_DD7D")

    Return()

    # Function_101_DBED end

    def Function_102_DD7E(): pass

    label("Function_102_DD7E")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_DD9C():
        OP_9D(0xFE, 0x5654, 0x0, 0x76C, 0x3E8, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DD9C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x87, 0x0)
    Sound(811, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_102_DD7E end

    def Function_103_DDCE(): pass

    label("Function_103_DDCE")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0x1A)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DDE6():
        OP_9D(0xFE, 0x5654, 0x0, 0xFFFFF31C, 0x384, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DDE6)
    WaitChrThread(0xFE, 1)
    Sound(862, 0, 50, 0)
    SetChrChipByIndex(0xFE, 0x1C)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_103_DDCE end

    def Function_104_DE11(): pass

    label("Function_104_DE11")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xA)
    SetChrSubChip(0xFE, 0x0)
    Sound(250, 0, 100, 0)

    def lambda_DE2F():
        OP_9D(0xFE, 0x53FC, 0x0, 0xFFFFFCE0, 0x190, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DE2F)
    WaitChrThread(0xFE, 1)

    def lambda_DE50():
        OP_A6(0xFE, 0x0, 0x32, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DE50)
    SetChrSubChip(0xFE, 0x2)
    WaitChrThread(0x25, 2)
    Return()

    # Function_104_DE11 end

    def Function_105_DE6D(): pass

    label("Function_105_DE6D")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DE7A():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DE7A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_105_DE6D end

    def Function_106_DE94(): pass

    label("Function_106_DE94")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DEA1():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFF38, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DEA1)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_106_DE94 end

    def Function_107_DEBB(): pass

    label("Function_107_DEBB")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DEC8():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0xC8, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DEC8)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_107_DEBB end

    def Function_108_DEE2(): pass

    label("Function_108_DEE2")

    SetChrChipByIndex(0xFE, 0xC)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DEEF():
        OP_97(0xFE, 0xFFFFEC78, 0x0, 0x0, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DEEF)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_108_DEE2 end

    def Function_109_DF09(): pass

    label("Function_109_DF09")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_DF27():
        OP_9D(0xFE, 0x6978, 0x0, 0x12C, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF27)
    WaitChrThread(0xFE, 1)
    Sound(862, 0, 100, 0)

    def lambda_DF4E():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DF4E)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_109_DF09 end

    def Function_110_DF67(): pass

    label("Function_110_DF67")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)
    Sound(809, 0, 100, 0)

    def lambda_DF7A():
        OP_9D(0xFE, 0x7530, 0x0, 0x320, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DF7A)
    WaitChrThread(0xFE, 1)
    Sound(811, 0, 100, 0)

    def lambda_DFA1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DFA1)
    SetChrSubChip(0xFE, 0x2)
    Return()

    # Function_110_DF67 end

    def Function_111_DFBA(): pass

    label("Function_111_DFBA")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_DFD2():
        OP_9D(0xFE, 0x6720, 0x0, 0xFFFFF768, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_DFD2)
    WaitChrThread(0xFE, 1)

    def lambda_DFF3():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_DFF3)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    Return()

    # Function_111_DFBA end

    def Function_112_E021(): pass

    label("Function_112_E021")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_E033():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_E033)

    def lambda_E040():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E040)

    def lambda_E059():
        OP_96(0xFE, 0x72D8, 0x0, 0xFFFFF448, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E059)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_112_E021 end

    def Function_113_E078(): pass

    label("Function_113_E078")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E090():
        OP_9D(0xFE, 0x6720, 0x0, 0x5DC, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E090)
    WaitChrThread(0xFE, 1)

    def lambda_E0B1():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E0B1)
    SetChrSubChip(0xFE, 0x2)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    SetChrChipByIndex(0xFE, 0xB)
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    Return()

    # Function_113_E078 end

    def Function_114_E0E3(): pass

    label("Function_114_E0E3")

    SetChrFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)

    def lambda_E0F5():
        TurnDirection(0xFE, 0x17, 500)
        ExitThread()

    QueueWorkItem(0xFE, 0, lambda_E0F5)

    def lambda_E102():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E102)

    def lambda_E11B():
        OP_96(0xFE, 0x72D8, 0x0, 0xBB8, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E11B)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x20)
    Return()

    # Function_114_E0E3 end

    def Function_115_E13A(): pass

    label("Function_115_E13A")


    def lambda_E13F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E13F)
    SetChrChipByIndex(0xFE, 0xF)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_115_E13A end

    def Function_116_E15C(): pass

    label("Function_116_E15C")

    SetChrChipByIndex(0xFE, 0xE)
    SetChrSubChip(0xFE, 0x0)

    def lambda_E169():
        OP_9D(0xFE, 0x7A44, 0x0, 0xFFFFFB50, 0x2BC, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E169)
    WaitChrThread(0xFE, 1)

    def lambda_E18A():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_E18A)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_116_E15C end

    def Function_117_E1A3(): pass

    label("Function_117_E1A3")

    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)

    def lambda_E1BB():
        OP_9C(0xFE, 0xFFFFE890, 0x0, 0x0, 0x1F4, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1BB)
    WaitChrThread(0xFE, 1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_117_E1A3 end

    def Function_118_E1E0(): pass

    label("Function_118_E1E0")


    def lambda_E1E5():
        OP_96(0xFE, 0x7C9C, 0x0, 0x12C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E1E5)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    Return()

    # Function_118_E1E0 end

    def Function_119_E207(): pass

    label("Function_119_E207")


    def lambda_E20C():
        OP_96(0xFE, 0x76C0, 0x0, 0x76C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E20C)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x12)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_119_E207 end

    def Function_120_E22E(): pass

    label("Function_120_E22E")


    def lambda_E233():
        OP_96(0xFE, 0x76C0, 0x0, 0xFFFFF894, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E233)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0x10)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_120_E22E end

    def Function_121_E255(): pass

    label("Function_121_E255")


    def lambda_E25A():
        OP_96(0xFE, 0x733C, 0x0, 0xFFFFFED4, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_E25A)
    WaitChrThread(0xFE, 1)
    SetChrChipByIndex(0xFE, 0xD)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_121_E255 end

    def Function_122_E27C(): pass

    label("Function_122_E27C")

    Sleep(1200)

    label("loc_E27F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E298")
    Sound(530, 0, 80, 0)
    Sleep(1200)
    Jump("loc_E27F")

    label("loc_E298")

    Return()

    # Function_122_E27C end

    def Function_123_E299(): pass

    label("Function_123_E299")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E2B2")
    Sound(356, 0, 50, 0)
    Sleep(1100)
    Jump("Function_123_E299")

    label("loc_E2B2")

    Return()

    # Function_123_E299 end

    def Function_124_E2B3(): pass

    label("Function_124_E2B3")

    Sleep(1000)

    label("loc_E2B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E2E4")
    Sound(264, 0, 40, 0)
    Sound(833, 0, 30, 0)
    Sleep(1600)
    Sound(264, 0, 40, 0)
    Sound(833, 0, 30, 0)
    Sleep(3000)
    Jump("loc_E2B6")

    label("loc_E2E4")

    Return()

    # Function_124_E2B3 end

    def Function_125_E2E5(): pass

    label("Function_125_E2E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x5)
    LoadChrToIndex("chr/ch00150.itc", 0x6)
    LoadChrToIndex("chr/ch00250.itc", 0x7)
    LoadChrToIndex("chr/ch00350.itc", 0x8)
    LoadChrToIndex("chr/ch02950.itc", 0x9)
    LoadChrToIndex("chr/ch03050.itc", 0xA)
    LoadChrToIndex("chr/ch02450.itc", 0xB)
    LoadChrToIndex("chr/ch02451.itc", 0xC)
    LoadChrToIndex("chr/ch00950.itc", 0xD)
    LoadChrToIndex("chr/ch00951.itc", 0xE)
    LoadChrToIndex("chr/ch00952.itc", 0xF)
    LoadChrToIndex("apl/ch51237.itc", 0x10)
    LoadChrToIndex("apl/ch51265.itc", 0x11)
    LoadChrToIndex("apl/ch51238.itc", 0x12)
    LoadChrToIndex("apl/ch51267.itc", 0x13)
    LoadChrToIndex("chr/ch42250.itc", 0x14)
    LoadChrToIndex("chr/ch42251.itc", 0x15)
    LoadChrToIndex("chr/ch02452.itc", 0x16)
    LoadChrToIndex("chr/ch42253.itc", 0x17)
    LoadChrToIndex("chr/ch42254.itc", 0x18)
    LoadChrToIndex("chr/ch42550.itc", 0x19)
    LoadChrToIndex("chr/ch42551.itc", 0x1A)
    LoadChrToIndex("chr/ch00952.itc", 0x1B)
    LoadChrToIndex("chr/ch42553.itc", 0x1C)
    LoadChrToIndex("chr/ch42554.itc", 0x1D)
    LoadChrToIndex("apl/ch51258.itc", 0x1E)
    LoadChrToIndex("apl/ch51235.itc", 0x1F)
    LoadChrToIndex("chr/ch02400.itc", 0x20)
    LoadChrToIndex("chr/ch00900.itc", 0x21)
    LoadChrToIndex("apl/ch51021.itc", 0x22)
    LoadEffect(0x1, "event/ev12010.eff")
    LoadEffect(0x2, "event/ev12011.eff")
    SoundLoad(938)
    SoundLoad(145)
    SoundLoad(803)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x101, 0x5)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x6)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x8)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x109, 0x9)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xA)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 7000, 0, -200, 270)
    SetChrPos(0x102, 6500, 0, 700, 270)
    SetChrPos(0x103, 5200, 0, 100, 270)
    SetChrPos(0x104, 4700, 0, 1000, 270)
    SetChrPos(0x109, 4900, 0, -1300, 270)
    SetChrPos(0x105, 5800, 0, -1800, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0x16)
    SetChrSubChip(0x17, 0x1)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 26900, 0, 300, 90)
    EndChrThread(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x12)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x2)
    ClearChrFlags(0xA, 0x20)
    SetChrPos(0xA, 25400, 0, 1900, 90)
    EndChrThread(0x9, 0xFF)
    SetChrChipByIndex(0x9, 0x10)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x20)
    SetChrPos(0x9, 25400, 0, -1900, 90)
    SetChrChipByIndex(0x25, 0x1B)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 24500, 0, -300, 90)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 9500, 0, 3600, 270)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 10500, 0, 3500, 270)
    SetChrChipByIndex(0x26, 0x18)
    SetChrSubChip(0x26, 0x3)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, 33500, 0, 0, 270)
    SetChrChipByIndex(0x27, 0x18)
    SetChrSubChip(0x27, 0x3)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, 33200, 0, 1700, 270)
    SetChrChipByIndex(0x28, 0x17)
    SetChrSubChip(0x28, 0x3)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    SetChrPos(0x28, 34700, 0, 1300, 270)
    SetChrChipByIndex(0x29, 0x17)
    SetChrSubChip(0x29, 0x3)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x29, 33700, 0, 3100, 270)
    SetChrChipByIndex(0x2A, 0x17)
    SetChrSubChip(0x2A, 0x2)
    SetChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrChipByIndex(0x2E, 0x1D)
    SetChrSubChip(0x2E, 0x2)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x8000)
    SetChrPos(0x2E, 34000, 0, -1900, 270)
    SetChrChipByIndex(0x2F, 0x1C)
    SetChrSubChip(0x2F, 0x2)
    ClearChrFlags(0x2F, 0x80)
    SetChrFlags(0x2F, 0x8000)
    SetChrPos(0x2F, 34900, 0, -200, 270)
    SetChrChipByIndex(0x30, 0x1C)
    SetChrSubChip(0x30, 0x3)
    ClearChrFlags(0x30, 0x80)
    SetChrFlags(0x30, 0x8000)
    SetChrPos(0x30, 35900, 0, -900, 270)
    SetChrChipByIndex(0x31, 0x1C)
    SetChrSubChip(0x31, 0x2)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrPos(0x31, 34000, 0, -3100, 270)
    SetChrChipByIndex(0x32, 0x1D)
    SetChrSubChip(0x32, 0x2)
    SetChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrChipByIndex(0x33, 0x1D)
    SetChrSubChip(0x33, 0x2)
    SetChrFlags(0x33, 0x80)
    SetChrFlags(0x33, 0x8000)
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0xA)
    ClearChrFlags(0x48, 0x80)
    OP_78(0x17, 0x48)
    OP_49()
    SetChrPos(0x48, 34300, 100, -1600, 0)
    OP_D5(0x48, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x1000)
    SetMapObjFlags(0x17, 0x4)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    OP_68(4600, 900, 930, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetCameraDistance(17000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0333
    ChrTalk(
        0x101,
        "#00010F#11P啧，居然连这种东西都派出来了……\x02",
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x103,
        (
            "#00206F#12P多半是从塔顶\x01",
            "投放至内部的。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x104,
        (
            "#11P#00301F话说回来，刚才那些东西\x01",
            "不是『结社』制造的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x105,
        (
            "#12P#10308F是在黑市上买到的，\x01",
            "还是……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x87, 0x1F4)
    Sleep(100)

    #C0337
    ChrTalk(
        0x8,
        (
            "#6P#11508F……先不管这个了，\x01",
            "那边好像也快搞定了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(29500, 700, 0, 3000)
    MoveCamera(43, 23, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)

    def lambda_E97C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_E97C)

    def lambda_E989():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_E989)
    Sleep(50)

    def lambda_E999():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E999)
    Sleep(50)

    def lambda_E9A9():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E9A9)
    Sleep(50)

    def lambda_E9B9():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E9B9)
    Sleep(50)

    def lambda_E9C9():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_E9C9)
    Sleep(50)

    def lambda_E9D9():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_E9D9)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0338
    ChrTalk(
        0x26,
        "#12P啧……这些怪物！\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x2E,
        (
            "没办法了！\x01",
            "开始最终计划！\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x2E, 0x3)
    Sound(809, 0, 100, 0)
    Sleep(200)
    SetChrSubChip(0x2E, 0x4)
    PlayEffect(0x1, 0x0, 0x2E, 0x5, 0, 0, 0, 0, -30, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    BeginChrThread(0x4C, 1, 0, 127)

    #C0340
    ChrTalk(
        0x17,
        "#01401F#7A#5P唔……\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0xA,
        "#07105F#10A#5P闪光弹……！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x9,
        "#07307F#5A#5P退后！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetChrChipByIndex(0xA, 0x13)
    SetChrSubChip(0xA, 0x2)
    BeginChrThread(0xA, 3, 0, 117)
    Sound(250, 0, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x9, 0x11)
    SetChrSubChip(0x9, 0x2)
    BeginChrThread(0x9, 3, 0, 117)
    Sound(844, 0, 80, 0)
    Sleep(50)
    SetChrChipByIndex(0x17, 0xC)
    SetChrSubChip(0x17, 0x2)
    BeginChrThread(0x17, 3, 0, 117)
    Sleep(50)
    SetChrChipByIndex(0x25, 0x22)
    SetChrSubChip(0x25, 0x0)
    BeginChrThread(0x25, 3, 0, 117)
    Sleep(200)
    StopEffect(0x0, 0x0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 29000, 0, 0, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 100, 0)
    Sound(200, 0, 100, 0)
    Sleep(100)
    Sound(174, 0, 100, 0)
    FadeToDark(500, 16777215, -1)
    OP_0D()
    Sleep(2000)
    OP_68(29500, 900, 0, 0)
    MoveCamera(43, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)
    SetChrFlags(0x29, 0x80)
    SetChrFlags(0x2E, 0x80)
    SetChrFlags(0x2F, 0x80)
    SetChrFlags(0x30, 0x80)
    SetChrFlags(0x31, 0x80)
    EndChrThread(0x17, 0xFF)
    EndChrThread(0xA, 0xFF)
    EndChrThread(0x9, 0xFF)
    EndChrThread(0x25, 0xFF)
    SetChrPos(0x17, 20900, 0, 300, 90)
    SetChrPos(0xA, 19400, 0, 1900, 90)
    SetChrPos(0x9, 19400, 0, -1900, 90)
    SetChrChipByIndex(0x25, 0xE)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, 18500, 0, -300, 90)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x10)
    ClearMapObjFlags(0x11, 0x1000)
    OP_70(0x11, 0x1E)
    OP_74(0x11, 0x3C)
    FadeToBright(2000, 16777215)
    Sound(145, 2, 100, 0)
    OP_71(0x11, 0x3C, 0x0, 0x0, 0x0)
    OP_79(0x11)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_0D()
    OP_68(33500, 1000, 0, 2500)
    MoveCamera(43, 19, 0, 2500)
    SetCameraDistance(17500, 2500)
    BeginChrThread(0x17, 3, 0, 118)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 119)
    Sleep(50)
    BeginChrThread(0x9, 3, 0, 120)
    Sleep(50)
    BeginChrThread(0x25, 3, 0, 121)
    WaitChrThread(0x25, 3)
    OP_6F(0x79)

    #C0343
    ChrTalk(
        0x9,
        "#6P#07301F啧……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0xA,
        "#07101F#5P这道卷帘门……\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x17,
        (
            "#01403F#5P……看来没那么\x01",
            "容易突破啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0346
    ChrTalk(
        0x101,
        "#00007F#6P#N各位！\x02",
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(28000, 1000, 0, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    OP_68(31000, 1000, 0, 3000)
    SetCameraDistance(16500, 3000)
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
    SetChrPos(0x101, 19500, 0, -300, 90)
    SetChrPos(0x102, 19500, 0, 1000, 90)
    SetChrPos(0x103, 18300, 0, -1700, 90)
    SetChrPos(0x104, 18300, 0, -400, 90)
    SetChrPos(0x109, 17100, 0, -1700, 90)
    SetChrPos(0x105, 17100, 0, -400, 90)
    SetChrPos(0x8, 17300, 0, 2100, 90)
    SetChrPos(0xB, 18400, 0, 2100, 90)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x17, 33500, 0, 300, 270)
    SetChrPos(0x25, 31500, 0, 0, 270)
    SetChrPos(0xA, 32400, 0, 1700, 270)
    SetChrPos(0x9, 32600, 0, -1300, 270)

    def lambda_EF17():
        OP_97(0x101, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EF17)
    Sleep(100)

    def lambda_EF34():
        OP_97(0x102, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EF34)
    Sleep(100)

    def lambda_EF51():
        OP_97(0x103, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EF51)
    Sleep(100)

    def lambda_EF6E():
        OP_97(0x104, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EF6E)
    Sleep(100)

    def lambda_EF8B():
        OP_97(0x109, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_EF8B)
    Sleep(100)

    def lambda_EFA8():
        OP_97(0x105, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_EFA8)
    Sleep(100)

    def lambda_EFC5():
        OP_97(0xB, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_EFC5)
    Sleep(100)

    def lambda_EFE2():
        OP_97(0x8, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_EFE2)
    WaitChrThread(0xB, 0)

    def lambda_F000():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_F000)
    WaitChrThread(0x8, 0)

    def lambda_F011():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_F011)

    #C0347
    ChrTalk(
        0x25,
        "#11P#00600F是你们啊……\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#00300F#6P看来已经成功\x01",
            "将他们击退了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x17,
        (
            "#11P#01403F嗯，但这样下去，\x01",
            "会让他们逃掉的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0350
    ChrTalk(
        0x101,
        "#11P#00001F#5P缇欧，有办法吗？\x02",
    )

    CloseMessageWindow()

    def lambda_F0C5():

        label("loc_F0C5")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F0C5")

    QueueWorkItem2(0x101, 2, lambda_F0C5)

    def lambda_F0D7():

        label("loc_F0D7")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F0D7")

    QueueWorkItem2(0x102, 2, lambda_F0D7)

    def lambda_F0E9():

        label("loc_F0E9")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F0E9")

    QueueWorkItem2(0x109, 2, lambda_F0E9)

    def lambda_F0FB():

        label("loc_F0FB")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F0FB")

    QueueWorkItem2(0x105, 2, lambda_F0FB)

    def lambda_F10D():

        label("loc_F10D")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F10D")

    QueueWorkItem2(0x104, 2, lambda_F10D)
    TurnDirection(0x103, 0x101, 500)

    #C0351
    ChrTalk(
        0x103,
        (
            "#6P#00201F虽然没什么自信，\x01",
            "但我会尽力而为的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F159():
        OP_95(0xFE, 32800, 0, -2700, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F159)
    Sleep(300)

    def lambda_F176():

        label("loc_F176")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F176")

    QueueWorkItem2(0x25, 2, lambda_F176)
    Sleep(50)

    def lambda_F18B():

        label("loc_F18B")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F18B")

    QueueWorkItem2(0x17, 2, lambda_F18B)
    Sleep(50)

    def lambda_F1A0():

        label("loc_F1A0")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F1A0")

    QueueWorkItem2(0x9, 2, lambda_F1A0)
    Sleep(50)

    def lambda_F1B5():

        label("loc_F1B5")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_F1B5")

    QueueWorkItem2(0xA, 2, lambda_F1B5)
    WaitChrThread(0x103, 1)

    def lambda_F1CB():
        OP_95(0xFE, 34200, 0, -2100, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F1CB)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x17, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0xA, 0x2)
    OP_93(0x103, 0x0, 0x1F4)
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(71, 0, 70, 0)
    ClearMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 126)
    Sound(938, 2, 100, 0)
    OP_0D()
    Sleep(2000)
    EndChrThread(0x103, 0x3)
    StopSound(938, 500, 100)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0352
    ChrTalk(
        0x103,
        (
            "#11P#00206F安全等级果然已经\x01",
            "提升到最高了。\x02\x03",

            "#00208F就算使用『永世系统』，\x01",
            "单凭这部笔记本型终端也……\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        "#5P#00008F是吗……\x02",
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x25, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_F305():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F305)

    def lambda_F312():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F312)

    def lambda_F31F():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_F31F)
    Sleep(50)

    def lambda_F32F():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F32F)

    def lambda_F33C():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F33C)
    Sleep(50)

    def lambda_F34C():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F34C)

    def lambda_F359():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F359)

    def lambda_F366():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F366)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x4)
    Sleep(800)
    OP_93(0x25, 0xB4, 0x1F4)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrFlags(0x25, 0x10)
    SetChrFlags(0x25, 0x2)
    SetChrFlags(0x25, 0x20)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x6)
    Sleep(500)
    SetChrSubChip(0x25, 0x7)
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Sleep(300)

    #C0354
    ChrTalk(
        0x25,
        (
            "#5P#00600F是我。\x02\x03",

            "#00603F嗯，这边总算是\x01",
            "暂时搞定了……\x02\x03",

            "………………………………\x02\x03",

            "#00601F……什么？\x02\x03",

            "他们乘坐导力梯\x01",
            "去往地下了……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0355
    ChrTalk(
        0x109,
        "#6P#N#10113F为、为什么……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0356
    ChrTalk(
        0x102,
        (
            "#00105F#5P难道他们并不打算\x01",
            "驾驶塔顶的飞艇逃离……？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x8,
        (
            "#11503F#5P嗯，依照我的猜想……\x02\x03",

            "#11501F他们大概是想引爆\x01",
            "装载在飞艇中的导力炸弹吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_F608():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F608)

    def lambda_F615():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F615)
    Sleep(50)
    OP_63(0x103, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_F655():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F655)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_F6AD():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F6AD)

    def lambda_F6BA():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F6BA)

    def lambda_F6C7():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_F6C7)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_F6EF():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F6EF)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_F714():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F714)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    ClearChrFlags(0x25, 0x10)
    ClearChrFlags(0x25, 0x2)
    ClearChrFlags(0x25, 0x20)
    SetChrChipByIndex(0x25, 0x21)
    SetChrSubChip(0x25, 0x0)
    Sound(802, 0, 100, 0)

    def lambda_F756():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_F756)
    Sleep(1000)

    #C0358
    ChrTalk(
        0x101,
        "#11P#00007F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x17,
        "#11P#01401F是吗，如果那样做的话，确实……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x9,
        (
            "#12P#07307F他们想把这栋大楼\x01",
            "连同宰相等人一起毁灭吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0xB,
        (
            "#12003F#5P恐怖分子确实有可能\x01",
            "做到那种地步呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xA,
        "#11P#07101F唔，真是愚蠢……\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x105,
        "#12P#10306F这可真是严重危机了……\x02",
    )

    CloseMessageWindow()
    OP_93(0x25, 0x5A, 0x1F4)

    #C0364
    ChrTalk(
        0x25,
        (
            "#5P#00610F可恶，既然如此，\x01",
            "就把这道卷帘门强行轰开！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    SetChrSubChip(0x103, 0x3)
    Sleep(100)
    SetChrSubChip(0x103, 0x2)

    #C0365
    ChrTalk(
        0x103,
        (
            "#11P#00204F#30W…………不………………\x02\x03",

            "#00202F#20W似乎有办法了。\x01",
            "　　　\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F908():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F908)

    def lambda_F915():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_F915)

    def lambda_F922():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_F922)
    Sleep(50)

    def lambda_F932():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F932)

    def lambda_F93F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_F93F)

    def lambda_F94C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F94C)
    Sleep(50)

    def lambda_F95C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F95C)

    def lambda_F969():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_F969)

    def lambda_F976():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F976)
    WaitChrThread(0x25, 2)

    #C0366
    ChrTalk(
        0x25,
        "#5P#00605F什么……！？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x160), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_24(0x91)
    OP_24(0x323)
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 0)
    NewScene("e4820", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_125_E2E5 end

    def Function_126_F9D0(): pass

    label("Function_126_F9D0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F9EA")
    OP_A1(0x103, 0x7D0, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_126_F9D0")

    label("loc_F9EA")

    Return()

    # Function_126_F9D0 end

    def Function_127_F9EB(): pass

    label("Function_127_F9EB")

    Sleep(200)
    Sound(555, 0, 80, 0)
    Sleep(500)
    Sound(555, 0, 60, 0)
    Sleep(200)
    Sound(555, 0, 30, 0)
    Return()

    # Function_127_F9EB end

    def Function_128_FA07(): pass

    label("Function_128_FA07")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00900.itc", 0x6)
    LoadChrToIndex("apl/ch51235.itc", 0x7)
    SoundLoad(938)
    SoundLoad(145)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0x101, 29500, 0, -300, 90)
    SetChrPos(0x102, 29500, 0, 1000, 90)
    SetChrPos(0x103, 34200, 0, -2100, 0)
    SetChrPos(0x104, 28300, 0, -400, 90)
    SetChrPos(0x109, 27100, 0, -1700, 90)
    SetChrPos(0x105, 27100, 0, -400, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    EndChrThread(0x17, 0xFF)
    SetChrChipByIndex(0x17, 0xB)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 33500, 0, 300, 270)
    EndChrThread(0xA, 0xFF)
    SetChrFlags(0xA, 0x8000)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 32400, 0, 1700, 270)
    EndChrThread(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 32600, 0, -1300, 270)
    SetChrChipByIndex(0x25, 0x6)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, 31500, 0, 0, 270)
    SetChrChipByIndex(0x8, 0x4)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 27300, 0, 2100, 135)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 28400, 0, 2100, 135)
    OP_4B(0xB, 0xFF)

    def lambda_FB8F():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FB8F)

    def lambda_FB9C():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FB9C)

    def lambda_FBA9():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FBA9)

    def lambda_FBB6():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FBB6)

    def lambda_FBC3():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FBC3)

    def lambda_FBD0():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_FBD0)

    def lambda_FBDD():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_FBDD)

    def lambda_FBEA():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FBEA)

    def lambda_FBF7():
        TurnDirection(0xFE, 0x103, 0)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FBF7)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x11, 0x10)
    ClearMapObjFlags(0x11, 0x1000)
    OP_70(0x11, 0x0)
    ClearChrFlags(0x48, 0x80)
    OP_78(0x17, 0x48)
    OP_49()
    SetChrPos(0x48, 34300, 100, -1600, 0)
    OP_D5(0x48, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x1000)
    ClearChrFlags(0x47, 0x80)
    OP_78(0x10, 0x47)
    OP_49()
    SetChrPos(0x47, 25500, 0, 0, 0)
    OP_D5(0x47, 0x0, 0x13880, 0x0, 0x0)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFrame(0xFF, "kokeru00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kokeru01", 0x0, 0x1)
    ClearMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0x7)
    SetChrSubChip(0x103, 0x0)
    BeginChrThread(0x103, 3, 0, 126)
    Sound(938, 2, 100, 0)
    OP_68(31000, 1000, 0, 0)
    MoveCamera(40, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0367
    ChrTalk(
        0x101,
        (
            "#5P#00002F约纳已经\x01",
            "回来了吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x103,
        (
            "#12P#00202F#11P是的，他应该是坐\x01",
            "今天那趟飞船回来的。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)
    Sound(839, 0, 100, 0)
    EndChrThread(0x103, 0x3)
    StopSound(938, 500, 100)
    Sleep(500)

    #C0369
    ChrTalk(
        0x103,
        (
            "#12P#00204F#11P好了，\x01",
            "塔内控制解除了。\x02",
        )
    )

    CloseMessageWindow()
    Sound(145, 2, 100, 0)
    OP_71(0x11, 0x0, 0x3C, 0x0, 0x0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FDD2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FDD2)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FDF7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_FDF7)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FE1F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FE1F)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FE44():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FE44)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FE6C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_FE6C)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FE91():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_FE91)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FEB9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_FEB9)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FEDE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FEDE)
    OP_63(0x25, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_FF03():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_FF03)
    Sleep(1000)
    OP_79(0x11)
    OP_24(0x91)
    Sound(143, 0, 100, 0)

    #C0370
    ChrTalk(
        0xA,
        "#5P#07102F太好了……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x103, 500)

    #C0371
    ChrTalk(
        0x25,
        "#5P#00602F导力梯能用了吗！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetMapObjFlags(0x17, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    TurnDirection(0x103, 0x25, 500)

    #C0372
    ChrTalk(
        0x103,
        (
            "#12P#00202F#11P是的，已经解除锁定了。\x02\x03",

            "#00206F除了恐怖分子正在搭乘的那部之外，\x01",
            "其它都可使用。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0xB,
        (
            "#12004F#5P那我就到塔顶去吧。\x02\x03",

            "#12000F去拆除飞船中的\x01",
            "导力炸弹。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xB, 500)

    #C0374
    ChrTalk(
        0x101,
        "#12P#00005F雾香小姐，您会拆除炸弹？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 500)

    #C0375
    ChrTalk(
        0xB,
        (
            "#12004F#5P嗯，对从事反间谍工作的人来说，\x01",
            "这是最基本的技能。\x02\x03",

            "#12000F雷克特书记官，\x01",
            "我们联手行动吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x8,
        "#11504F呼，真没办法。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xB, 500)

    #C0377
    ChrTalk(
        0x9,
        (
            "#11P#07303F那我们也一起去吧。\x02\x03",

            "#07300F他们很可能留下了\x01",
            "守卫用的智能兵器。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x25, 500)

    def lambda_10147():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_10147)

    #C0378
    ChrTalk(
        0xA,
        (
            "#5P#07101F请你们去追击\x01",
            "恐怖分子！\x02\x03",

            "现在立刻行动，\x01",
            "应该还有机会抓住他们！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    #C0379
    ChrTalk(
        0x17,
        "#11P#01400F明白……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x25, 0x101, 500)

    #C0380
    ChrTalk(
        0x25,
        (
            "#11P#00601F班宁斯！\x01",
            "我们开始追击！\x02\x03",

            "敌人共有两组……\x01",
            "我们也需要分头行动！\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        "#6P#00007F明白！\x02",
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x104,
        "#00307F#6P遵命！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 1)
    NewScene("c1520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_128_FA07 end

    def Function_129_10264(): pass

    label("Function_129_10264")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch10902.itc", 0x1E)
    LoadChrToIndex("chr/ch11102.itc", 0x1F)
    LoadChrToIndex("chr/ch11002.itc", 0x20)
    LoadChrToIndex("chr/ch11802.itc", 0x21)
    LoadChrToIndex("chr/ch11712.itc", 0x22)
    LoadChrToIndex("chr/ch05600.itc", 0x23)
    LoadChrToIndex("chr/ch05802.itc", 0x24)
    LoadChrToIndex("chr/ch05902.itc", 0x25)
    LoadChrToIndex("chr/ch06000.itc", 0x26)
    LoadChrToIndex("chr/ch47900.itc", 0x27)
    LoadChrToIndex("chr/ch28100.itc", 0x28)
    LoadChrToIndex("apl/ch51259.itc", 0x29)
    LoadChrToIndex("apl/ch50123.itc", 0x2A)
    SetChrPos(0x0, 0, 0, 5500, 0)
    SetChrPos(0x1, 0, 0, 5500, 0)
    SetChrPos(0x2, 0, 0, 5500, 0)
    SetChrPos(0x3, 0, 0, 5500, 0)
    SetChrChipByIndex(0x36, 0x0)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrPos(0x36, 8500, 0, 2500, 180)
    SetChrChipByIndex(0x37, 0x0)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrPos(0x37, 11500, 0, 2500, 180)
    SetChrChipByIndex(0x38, 0x0)
    SetChrSubChip(0x38, 0x0)
    ClearChrFlags(0x38, 0x80)
    SetChrFlags(0x38, 0x8000)
    SetChrFlags(0x38, 0x20)
    SetChrPos(0x38, 33800, 0, -550, 45)
    SetChrChipByIndex(0x39, 0x0)
    SetChrSubChip(0x39, 0x0)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    SetChrFlags(0x39, 0x20)
    SetChrPos(0x39, 33800, 0, 550, 135)
    SetChrChipByIndex(0x3A, 0x2A)
    SetChrSubChip(0x3A, 0x0)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    SetChrPos(0x3A, -5000, 0, -1000, 90)
    SetChrChipByIndex(0x3B, 0x2A)
    SetChrSubChip(0x3B, 0x0)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    SetChrPos(0x3B, 25000, 0, 1000, 270)
    SetChrChipByIndex(0x3D, 0x26)
    SetChrSubChip(0x3D, 0x0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    SetChrFlags(0x3D, 0x20)
    SetChrPos(0x3D, 34000, 0, 0, 270)
    BeginChrThread(0x3D, 3, 0, 130)
    SetChrChipByIndex(0x3E, 0x28)
    SetChrSubChip(0x3E, 0x0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    SetChrPos(0x3E, 34600, 50, -1300, 315)
    SetChrChipByIndex(0x3F, 0x27)
    SetChrSubChip(0x3F, 0x0)
    ClearChrFlags(0x3F, 0x80)
    SetChrFlags(0x3F, 0x8000)
    SetChrPos(0x3F, 35700, 50, 400, 270)
    OP_7D(0xFF, 0xD2, 0xC8, 0x0, 0x0)
    OP_11(0xFF, 0xC7, 0xBB, 0x12C, 0x384, 0x0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K当天１８：００──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_68(0, 1000, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    PlayBGM("ed7151", 0)
    OP_68(10000, 1000, 0, 10000)
    MoveCamera(60, 13, 0, 10000)

    def lambda_104FD():
        OP_96(0xFE, 0x61A8, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3A, 1, lambda_104FD)

    def lambda_10517():
        OP_96(0xFE, 0xFFFFEC78, 0x0, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3B, 1, lambda_10517)
    FadeToBright(1000, 0)
    OP_63(0x38, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(50)
    OP_63(0x39, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(35000, 1000, 0, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetCameraDistance(18000, 5000)
    BeginChrThread(0x3D, 0, 0, 131)
    BeginChrThread(0x38, 0, 0, 131)
    BeginChrThread(0x39, 0, 0, 131)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_64(0x36)
    OP_64(0x37)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -46450, 50, 120000, 270)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x2)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -46450, 50, 117100, 270)
    SetChrChipByIndex(0x20, 0x20)
    SetChrSubChip(0x20, 0x2)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -46450, 50, 114200, 270)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x1)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -57600, 50, 117100, 90)
    SetChrChipByIndex(0x22, 0x22)
    SetChrSubChip(0x22, 0x1)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -57600, 50, 120000, 90)
    SetChrChipByIndex(0x1D, 0x29)
    SetChrSubChip(0x1D, 0x1)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x2)
    SetChrFlags(0x1D, 0x10)
    SetChrPos(0x1D, -54850, 50, 123900, 270)
    SetChrChipByIndex(0x23, 0x24)
    SetChrSubChip(0x23, 0x2)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -50100, 50, 123900, 180)
    SetChrChipByIndex(0x24, 0x25)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -40100, 50, 121250, 270)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -45100, 0, 115300, 270)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -45100, 0, 118200, 270)
    OP_4B(0xC, 0xFF)
    SetChrChipByIndex(0xC, 0x5)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -58800, 0, 120000, 90)
    OP_4B(0xD, 0xFF)
    SetChrChipByIndex(0xD, 0x6)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -44800, 0, 121300, 270)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -44400, 0, 120400, 270)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -58800, 0, 118600, 90)
    OP_4B(0x11, 0xFF)
    SetChrChipByIndex(0x11, 0x8)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -59300, 0, 115700, 90)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    OP_70(0x14, 0x46)
    OP_70(0x15, 0x46)
    OP_68(-54240, 2000, 113000, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    OP_68(-54240, 2000, 117000, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-56210, 2000, 121490, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16170, 0)
    OP_0D()
    Sleep(300)

    #C0384
    ChrTalk(
        0x1D,
        (
            "#02803F#11P#30W……是吗……我明白了。\x02\x03",

            "#02801F……这边已经安全了，\x01",
            "放心吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1D, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0385
    ChrTalk(
        0x1D,
        "#02806F#11P#30W……………………………\x02",
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x23,
        "#11P#02500F……恐怖分子的情况怎么样了？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x1D, 0x2)
    ClearChrFlags(0x1D, 0x10)
    SetChrChipByIndex(0x1D, 0x23)
    SetChrSubChip(0x1D, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    OP_93(0x1D, 0xB4, 0x1F4)
    Fade(500)
    OP_68(-54240, 2000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    OP_0D()

    #C0387
    ChrTalk(
        0x1D,
        (
            "#02803F#5P共和国的那伙恐怖分子已经被\x01",
            "一个叫作『黑月』贸易公司的职员抓住了。\x02\x03",

            "#02801F据说他们持有共和国政府\x01",
            "交付的逮捕委托书。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x20,
        "#07005F#11P#N哎……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0389
    ChrTalk(
        0x22,
        (
            "#6P#07502F哦，这可真是好极了！\x02\x03",

            "#07509F他们是我们的朋友，\x01",
            "我可以保证他们的身份，请放心。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0xB,
        "#12004F#6P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0391
    ChrTalk(
        0x1D,
        (
            "#02806F至于来自帝国的恐怖分子……\x02\x03",

            "#02801F几乎全都被帝国政府\x01",
            "委任的猎兵团『赤色星座』\x01",
            "处死了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0392
    ChrTalk(
        0x21,
        "#6P……怎么会这样……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-49800, 2000, 116900, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13860, 0)
    SetChrSubChip(0x23, 0x0)
    OP_0D()
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0393
    ChrTalk(
        0x1F,
        (
            "#07207F#11P宰相！\x01",
            "您到底在想什么！？\x02\x03",

            "帝国政府竟然以处刑的名义，\x01",
            "在国外雇用猎兵团！？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x1E, 0x1)
    Sleep(300)

    #C0394
    ChrTalk(
        0x1E,
        (
            "#5P#07404F是的，这是为了预防万一。\x02\x03",

            "#07401F我的安危不足挂齿，但他们竟敢\x01",
            "谋害皇子殿下，实在是罪该万死。\x02\x03",

            "对于他们背后的那些愚蠢之辈而言，\x01",
            "这也是个很好的警告。\x02",
        )
    )

    CloseMessageWindow()

    #C0395
    ChrTalk(
        0x1F,
        "#07201F唔……\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x8,
        "#11508F#11P（……真是能说会道啊。）\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0397
    ChrTalk(
        0x24,
        (
            "#02205F#11P#N虽、虽然基于自治州法，\x01",
            "我们不得不予以认同……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrSubChip(0x23, 0x1)

    #C0398
    ChrTalk(
        0x23,
        (
            "#5P#02507F但是，这种做法……\x02\x03",

            "未免也太\x01",
            "有违道义了吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x22,
        "#6P#07505F#N哦，这只是个误会而已。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-54240, 2000, 116060, 0)
    MoveCamera(41, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18860, 0)
    SetChrSubChip(0x22, 0x0)

    def lambda_10E5B():
        TurnDirection(0xFE, 0x22, 0)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_10E5B)
    SetChrSubChip(0x23, 0x2)
    SetChrSubChip(0x1F, 0x0)
    SetChrSubChip(0x1E, 0x0)
    OP_0D()
    Sleep(300)

    #C0400
    ChrTalk(
        0x22,
        (
            "#6P#07504F话说回来，各位不妨想想……\x01",
            "这似乎也算是个意外的证据吧？\x02\x03",

            "#07502F事实证明，克洛斯贝尔自治州政府\x01",
            "连这种程度的突发事件\x01",
            "都无法独立解决。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x23, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0401
    ChrTalk(
        0x23,
        "#11P#02501F……！\x02",
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x1E,
        (
            "#11P#07404F没错，不仅让恐怖分子大摇大摆地\x01",
            "接近会场，而且还无能地让他们逃掉了……\x02\x03",

            "最后，\x01",
            "全靠我们的事先安排，\x01",
            "才成功阻止了他们的逃亡。\x02\x03",

            "#07402F对于刚才那项议案而言，\x01",
            "这确实是一个很好的事例啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x22,
        (
            "#6P#07503F是的，恕我失礼，就在刚才，\x01",
            "各位的生命已经受到了实质性的威胁……\x02\x03",

            "#07500F如此看来，\x01",
            "无论如何也该认真考虑一下\x01",
            "刚才那项驻军议案吧？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x23, 0x0)
    Sleep(300)

    def lambda_1114C():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_1114C)
    WaitChrThread(0x23, 2)
    Sleep(500)

    #C0404
    ChrTalk(
        0x23,
        "#5P#02501F你、你们……\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x21,
        "#12P……太霸道了………\x02",
    )

    CloseMessageWindow()

    #C0406
    ChrTalk(
        0x20,
        "#07008F#11P#N该、该不会是为了这个才……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0407
    ChrTalk(
        0x1F,
        (
            "#07201F#11P……没想到会设下\x01",
            "如此阴险毒辣的陷阱啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1D, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1D)
    OP_93(0x1D, 0xB4, 0x1F4)
    Sleep(300)

    #C0408
    ChrTalk(
        0x1D,
        (
            "#02803F#5P各位，\x01",
            "我们的讨论似乎偏离了正题。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrSubChip(0x23, 0x2)
    SetChrSubChip(0x22, 0x1)
    SetChrSubChip(0x1F, 0x2)
    OP_68(-54850, 1300, 122600, 0)
    MoveCamera(63, 14, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19000, 0)
    OP_68(-55060, 1300, 123450, 20000)
    MoveCamera(49, 16, 0, 20000)
    OP_6E(500, 20000)
    SetCameraDistance(18000, 20000)
    Sleep(1000)

    #C0409
    ChrTalk(
        0x1D,
        (
            "#02800F#5P#30W宰相阁下与总统阁下的意见\x01",
            "自然值得我们洗耳恭听……\x02\x03",

            "但在此之前，请允许我继续发表\x01",
            "被刚才的袭击所打断的提案。\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x23,
        "#11P#02505F#30W迪、迪塔……？\x02",
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x1E,
        "#11P#N#07405F#30W哦……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0412
    ChrTalk(
        0x22,
        "#12P#N#07505F#30W……唔。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0413
    ChrTalk(
        0x21,
        "#30W那么，您有何提议？\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x1D,
        (
            "#5P#02804F#30W不，并不是提议，\x01",
            "应该说是表态吧。\x02\x03",

            "尽管我也曾犹豫过……\x01",
            "但通过这起事件，我已经坚定了决心。\x02\x03",

            "#02800F现在，请允许我\x01",
            "借此机会提出一项主张。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x1E,
        "#11P#N#07401F#30W……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0416
    ChrTalk(
        0x22,
        "#12P#N#07501F#30W什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    OP_6F(0x79)

    #C0417
    ChrTalk(
        0x1D,
        (
            "#5P#02803F#30W我们已经不能再\x01",
            "被别国左右了。\x02\x03",

            "#02801F为了克洛斯贝尔及其周边地区……\x01",
            "不，是为了整个大陆的长久和平与发展……\x02",
        )
    )

    CloseMessageWindow()
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(-55060, 1300, 123450, 500)
    MoveCamera(49, 16, 0, 500)
    OP_6E(500, 500)
    SetCameraDistance(16500, 500)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(300)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0418
    ChrTalk(
        0x1D,
        (
            "#5P#02807F#4S我在此向全体市民，以及大陆各国提议──\x01",
            "『克洛斯贝尔独立』！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 3000)
    FadeToDark(3000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    Sleep(500)
    SetScenarioFlags(0x22, 0)
    NewScene("m0401", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_129_10264 end

    def Function_130_11604(): pass

    label("Function_130_11604")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1161B")
    OP_A0(0xFE, 2500, 0x0, 0xFB)
    Jump("Function_130_11604")

    label("loc_1161B")

    Return()

    # Function_130_11604 end

    def Function_131_1161C(): pass

    label("Function_131_1161C")


    def lambda_11621():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11621)
    WaitChrThread(0xFE, 1)
    Sleep(1500)
    OP_63(0x3E, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    def lambda_1165A():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1165A)
    WaitChrThread(0xFE, 1)
    Sleep(1500)

    def lambda_1167B():
        OP_98(0xFE, 0xFFFFFED4, 0x0, 0x0, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1167B)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_131_1161C end

    def Function_132_11695(): pass

    label("Function_132_11695")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118B0")
    SetChrName("")

    #A0419
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

    #C0420
    ChrTalk(
        0x101,
        (
            "#00005F说起来，在会议期间，\x01",
            "好像只能使用\x01",
            "最前面的导力梯吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        (
            "#00100F嗯，好像是出于警备上的考虑，\x01",
            "做出了这样安排。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C2, 3)), scpexpr(EXPR_END)), "loc_117FB")

    #C0422
    ChrTalk(
        0x103,
        (
            "#00200F这里似乎和疏散楼梯一样，\x01",
            "也是通过导力网络\x01",
            "进行控制和管理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x101,
        (
            "#00003F嗯，好像是这样。\x02\x03",

            "#00000F总之，如果要去其它楼层，\x01",
            "我们就乘坐最前面的导力梯吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_118A8")

    label("loc_117FB")


    #C0424
    ChrTalk(
        0x103,
        (
            "#00200F顺便一说，锁定开关\x01",
            "似乎是通过导力网络\x01",
            "来控制和管理的。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x101,
        (
            "#00003F嗯，不愧是兰花塔的\x01",
            "安保系统啊。\x02\x03",

            "#00000F总之，如果要去其它楼层，\x01",
            "我们就乘坐最前面的导力梯吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_118A8")

    SetScenarioFlags(0x1C2, 2)
    Jump("loc_118FF")

    label("loc_118B0")

    SetChrName("")

    #A0426
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

    label("loc_118FF")

    TalkEnd(0xFF)
    Return()

    # Function_132_11695 end

    def Function_133_11903(): pass

    label("Function_133_11903")

    EventBegin(0x1)
    OP_4B(0x1A, 0xFF)
    TurnDirection(0x1A, 0x0, 500)
    Sleep(500)

    #C0427
    ChrTalk(
        0x1A,
        "正式会议正在进行中。\x02",
    )

    CloseMessageWindow()

    #C0428
    ChrTalk(
        0x1A,
        "你们要想看里面的情况就去回廊室吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 9780, 0, 1430, 180)
    OP_93(0x1A, 0xB4, 0x0)
    OP_4C(0x1A, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_133_11903 end

    def Function_134_11975(): pass

    label("Function_134_11975")

    EventBegin(0x1)

    #C0429
    ChrTalk(
        0x101,
        (
            "#00003F……会场是不能进入的。\x02\x03",

            "#00001F在引起麻烦之前，还是赶快离开吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 90250, 0, 76140, 270)
    EventEnd(0x4)
    Return()

    # Function_134_11975 end

    def Function_135_119D8(): pass

    label("Function_135_119D8")

    EventBegin(0x1)

    #C0430
    ChrTalk(
        0x101,
        (
            "#00003F……会场是不能进入的。\x02\x03",

            "#00001F在引起麻烦之前，还是赶快离开吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 168870, 0, 76540, 90)
    EventEnd(0x4)
    Return()

    # Function_135_119D8 end

    SaveToFile()

Try(main)
