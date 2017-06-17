from ScenarioHelper import *

def main():
    CreateScenaFile(
        "c1600.bin",                # FileName
        "c1600",                    # MapName
        "c1600",                    # Location
        0x00B2,                     # MapIndex
        "ed7550",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x01',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 178, 0, 2, 0, 3],
    )

    BuildStringList((
        "c1600",                  # 0
        "乔伊",                   # 1
        "滴",                     # 2
        "约纳",                   # 3
        "罗伯兹主任",             # 4
        "迪塔市长",               # 5
        "战鬼西格蒙德",           # 6
        "谢莉",                   # 7
        "瓦鲁多",                 # 8
        "琪雅",                   # 9
        "玛丽亚贝尔",             # 10
        "阿瑞安赫德",             # 11
        "诺华提斯博士",           # 12
        "小丑肯帕雷拉",           # 13
        "赛尔盖科长",             # 14
        "飞艇",                   # 15
        "飞艇",                   # 16
        "飞艇影",                 # 17
        "飞艇影",                 # 18
        "帝国恐怖分子",           # 19
        "帝国恐怖分子",           # 20
        "帝国恐怖分子",           # 21
        "帝国恐怖分子",           # 22
        "帝国恐怖分子",           # 23
        "帝国恐怖分子",           # 24
        "帝国恐怖分子",           # 25
        "共和国恐怖分子",         # 26
        "共和国恐怖分子",         # 27
        "共和国恐怖分子",         # 28
        "共和国恐怖分子",         # 29
        "共和国恐怖分子",         # 30
        "共和国恐怖分子",         # 31
        "共和国恐怖分子",         # 32
        "神机",                   # 33
        "神机",                   # 34
        "神机",                   # 35
        "梅尔卡瓦",               # 36
        "影像",                   # 37
        "影像",                   # 38
        "影像",                   # 39
        "影像",                   # 40
        "影像",                   # 41
        "影像",                   # 42
        "SE控制",                 # 43
        "bc1600",                 # 44
    ))

    ATBonus("ATBonus_6D4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_794", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_798", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_79C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_774", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_778", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_77C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_780", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_784", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_788", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_78C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_790", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_7B4", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bc1600", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_794", "MonsterBattlePostion_774", "ed7554", "ed7554", "ATBonus_6D4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch27600.itc",                   # 02
        "apl/ch51731.itc",                   # 03
        "chr/ch05410.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "chr/ch00000.itc",                   # 10
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

    DeclNpc(-119,    0,       22069,   0,    389,  0x0, 0,   2,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(8680,    0,       -16479,  135,  389,  0x0, 0,   4,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(32200,   -4400,   -27850,  75,   453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(28399,   -4400,   -27750,  45,   453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 34,  22.0,                  -23.0,                 -5.400000095367432,    625.0,                 [0.14142131805419922,  0.07071070373058319,   -0.0,                  0.0,                   -0.14142140746116638,  0.07071065902709961,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -6.363961219787598,    0.07070967555046082,   1.0800000429153442,    1.0])
    DeclEvent(0x0000, 0, 62,  0.0,                   -22.0,                 -1.0,                  156.25,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  4.400000095367432,     0.20000000298023224,   1.0])

    DeclActor(0,       0,       0,       1500,    0,       1500,    0,       0x007C, 0,  93, 0x0000)

    ChipFrameInfo(2420, 0)                                       # 0

    ScpFunction((
        "Function_0_974",          # 00, 0
        "Function_1_A24",          # 01, 1
        "Function_2_B80",          # 02, 2
        "Function_3_D57",          # 03, 3
        "Function_4_132C",         # 04, 4
        "Function_5_1525",         # 05, 5
        "Function_6_1612",         # 06, 6
        "Function_7_17F2",         # 07, 7
        "Function_8_1DFD",         # 08, 8
        "Function_9_2147",         # 09, 9
        "Function_10_2C5B",        # 0A, 10
        "Function_11_2CB0",        # 0B, 11
        "Function_12_2D05",        # 0C, 12
        "Function_13_2D5A",        # 0D, 13
        "Function_14_2DCA",        # 0E, 14
        "Function_15_2E1F",        # 0F, 15
        "Function_16_2E74",        # 10, 16
        "Function_17_2EA4",        # 11, 17
        "Function_18_2F0C",        # 12, 18
        "Function_19_2F49",        # 13, 19
        "Function_20_2F8D",        # 14, 20
        "Function_21_2FD1",        # 15, 21
        "Function_22_3015",        # 16, 22
        "Function_23_3059",        # 17, 23
        "Function_24_309D",        # 18, 24
        "Function_25_30E1",        # 19, 25
        "Function_26_3125",        # 1A, 26
        "Function_27_36AC",        # 1B, 27
        "Function_28_370C",        # 1C, 28
        "Function_29_376C",        # 1D, 29
        "Function_30_388F",        # 1E, 30
        "Function_31_399B",        # 1F, 31
        "Function_32_3A6A",        # 20, 32
        "Function_33_3B39",        # 21, 33
        "Function_34_3EE5",        # 22, 34
        "Function_35_53C6",        # 23, 35
        "Function_36_54BE",        # 24, 36
        "Function_37_54DD",        # 25, 37
        "Function_38_54FC",        # 26, 38
        "Function_39_555B",        # 27, 39
        "Function_40_557A",        # 28, 40
        "Function_41_55C2",        # 29, 41
        "Function_42_560F",        # 2A, 42
        "Function_43_69B4",        # 2B, 43
        "Function_44_6CD1",        # 2C, 44
        "Function_45_6D85",        # 2D, 45
        "Function_46_6DD5",        # 2E, 46
        "Function_47_6E2B",        # 2F, 47
        "Function_48_6EE5",        # 30, 48
        "Function_49_6F8E",        # 31, 49
        "Function_50_7079",        # 32, 50
        "Function_51_70B9",        # 33, 51
        "Function_52_713C",        # 34, 52
        "Function_53_794F",        # 35, 53
        "Function_54_8040",        # 36, 54
        "Function_55_8157",        # 37, 55
        "Function_56_88F6",        # 38, 56
        "Function_57_8A6A",        # 39, 57
        "Function_58_8AA9",        # 3A, 58
        "Function_59_8F41",        # 3B, 59
        "Function_60_8F70",        # 3C, 60
        "Function_61_900D",        # 3D, 61
        "Function_62_9024",        # 3E, 62
        "Function_63_B645",        # 3F, 63
        "Function_64_B673",        # 40, 64
        "Function_65_B6D4",        # 41, 65
        "Function_66_B735",        # 42, 66
        "Function_67_B75A",        # 43, 67
        "Function_68_C1C5",        # 44, 68
        "Function_69_C1D8",        # 45, 69
        "Function_70_C20D",        # 46, 70
        "Function_71_1008E",       # 47, 71
        "Function_72_100B3",       # 48, 72
        "Function_73_1011A",       # 49, 73
        "Function_74_10181",       # 4A, 74
        "Function_75_101E8",       # 4B, 75
        "Function_76_1024F",       # 4C, 76
        "Function_77_102B6",       # 4D, 77
        "Function_78_102F8",       # 4E, 78
        "Function_79_1031A",       # 4F, 79
        "Function_80_10336",       # 50, 80
        "Function_81_10352",       # 51, 81
        "Function_82_1036E",       # 52, 82
        "Function_83_1038A",       # 53, 83
        "Function_84_103A6",       # 54, 84
        "Function_85_103CA",       # 55, 85
        "Function_86_103D5",       # 56, 86
        "Function_87_103E0",       # 57, 87
        "Function_88_103EB",       # 58, 88
        "Function_89_103F6",       # 59, 89
        "Function_90_10401",       # 5A, 90
        "Function_91_1040C",       # 5B, 91
        "Function_92_10487",       # 5C, 92
        "Function_93_1049F",       # 5D, 93
        "Function_94_104FA",       # 5E, 94
    ))


    def Function_0_974(): pass

    label("Function_0_974")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_9AC"),
        (1, "loc_9B8"),
        (2, "loc_9C4"),
        (3, "loc_9D0"),
        (4, "loc_9DC"),
        (5, "loc_9E8"),
        (6, "loc_9F4"),
        (SWITCH_DEFAULT, "loc_A00"),
    )


    label("loc_9AC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9B8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9C4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9D0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9DC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9E8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_9F4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A00")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A23")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A0C")

    label("loc_A23")

    Return()

    # Function_0_974 end

    def Function_1_A24(): pass

    label("Function_1_A24")

    SetMapObjFlags(0x5, 0x2000000)
    SetMapObjFlags(0x14, 0x2000000)
    SetMapObjFlags(0x9, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x15, 0x2000000)
    SetMapObjFlags(0x17, 0x2000000)
    SetMapObjFlags(0x6, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_AB7")
    ClearMapObjFlags(0x6, 0x2000000)
    ClearMapObjFlags(0x7, 0x2000000)
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)

    label("loc_AB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_AC6")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_AC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_AE1")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0xA, 0x2000000)

    label("loc_AE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_AF0")
    ClearMapObjFlags(0x5, 0x2000000)

    label("loc_AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_B0B")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x9, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)

    label("loc_B0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2B")
    ClearMapObjFlags(0x5, 0x2000000)
    ClearMapObjFlags(0x14, 0x2000000)
    ClearMapObjFlags(0x18, 0x2000000)

    label("loc_B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_B70")
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x15, 0x2000000)
    ClearMapObjFlags(0x17, 0x2000000)
    ClearMapObjFlags(0x16, 0x2000000)
    SetMapObjFlags(0x18, 0x2000000)

    label("loc_B70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_B7F")
    ClearMapObjFlags(0x16, 0x2000000)

    label("loc_B7F")

    Return()

    # Function_1_A24 end

    def Function_2_B80(): pass

    label("Function_2_B80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BBD")
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 180)
    OP_8E(0xC, "迪塔总统")

    label("loc_BBD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_BD5")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_C3B")

    label("loc_BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_BED")
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    Jump("loc_C3B")

    label("loc_BED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_BFB")
    Jump("loc_C3B")

    label("loc_BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C09")
    Jump("loc_C3B")

    label("loc_C09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_C21")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    Jump("loc_C3B")

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_C3B")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    OP_93(0x8, 0x13B, 0x0)

    label("loc_C3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_C4F")
    ClearScenarioFlags(0x22, 0)
    Event(0, 8)
    Jump("loc_D40")

    label("loc_C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_C63")
    ClearScenarioFlags(0x22, 1)
    Event(0, 9)
    Jump("loc_D40")

    label("loc_C63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_C77")
    ClearScenarioFlags(0x22, 2)
    Event(0, 26)
    Jump("loc_D40")

    label("loc_C77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_C8E")
    ClearScenarioFlags(0x22, 3)
    SetScenarioFlags(0x0, 5)
    Event(0, 42)
    Jump("loc_D40")

    label("loc_C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_CA2")
    ClearScenarioFlags(0x22, 4)
    Event(0, 52)
    Jump("loc_D40")

    label("loc_CA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_CB6")
    ClearScenarioFlags(0x22, 5)
    Event(0, 53)
    Jump("loc_D40")

    label("loc_CB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_CCA")
    ClearScenarioFlags(0x22, 6)
    Event(0, 54)
    Jump("loc_D40")

    label("loc_CCA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_CDE")
    ClearScenarioFlags(0x22, 7)
    Event(0, 55)
    Jump("loc_D40")

    label("loc_CDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_CF2")
    ClearScenarioFlags(0x23, 0)
    Event(0, 56)
    Jump("loc_D40")

    label("loc_CF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_D06")
    ClearScenarioFlags(0x23, 1)
    Event(0, 58)
    Jump("loc_D40")

    label("loc_D06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 2)), scpexpr(EXPR_END)), "loc_D1A")
    ClearScenarioFlags(0x23, 2)
    Event(0, 67)
    Jump("loc_D40")

    label("loc_D1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 3)), scpexpr(EXPR_END)), "loc_D31")
    ClearScenarioFlags(0x23, 3)
    SetScenarioFlags(0x0, 4)
    Event(0, 70)
    Jump("loc_D40")

    label("loc_D31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 4)), scpexpr(EXPR_END)), "loc_D40")
    ClearScenarioFlags(0x23, 4)
    Event(0, 94)

    label("loc_D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D56")
    SetMapFlags(0x10000000)
    Event(0, 33)

    label("loc_D56")

    Return()

    # Function_2_B80 end

    def Function_3_D57(): pass

    label("Function_3_D57")

    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF032877), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_F0(0x1, 0x4B0)
    OP_F3(100000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D94")
    SetMapObjFrame(0xFF, "CS00", 0x1, 0x2)
    SetMapObjFrame(0xFF, "CS01", 0x1, 0x2)
    Jump("loc_DA0")

    label("loc_D94")

    SetMapObjFrame(0xFF, "CS02", 0x1, 0x2)

    label("loc_DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_DB7")
    Sound(132, 1, 50, 0)
    ClearScenarioFlags(0x0, 5)
    Jump("loc_DD6")

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD0")
    Sound(132, 1, 50, 0)
    Jump("loc_DD6")

    label("loc_DD0")

    Sound(132, 1, 100, 0)

    label("loc_DD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_DF0")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 4)
    Jump("loc_E1E")

    label("loc_DF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E0C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_E1E")

    label("loc_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_E1E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x97), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_E1E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E36")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E36")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4E")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_E4E")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EB0")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x0, 0x1)

    label("loc_EB0")

    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_100A")
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    Jump("loc_112E")

    label("loc_100A")

    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "close")
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)

    label("loc_112E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1151")
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x8, 0x20)
    OP_70(0x8, 0x2)
    Jump("loc_1157")

    label("loc_1151")

    SetMapObjFlags(0x8, 0x4)

    label("loc_1157")

    SetMapObjFrame(0xFF, "last", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_122D")
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x42E)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x14, 0x29)
    SetChrPos(0x29, 0, 0, 6500, 180)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x1000)
    SetMapObjFlags(0x14, 0x4)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x42E)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_122D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12C7")
    LoadEffect(0x9, "map/mprain01.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_12C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_132B")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x12C, 0x384, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)

    label("loc_132B")

    Return()

    # Function_3_D57 end

    def Function_4_132C(): pass

    label("Function_4_132C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_133D")
    Jump("loc_1521")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_14A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x189, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1433")

    #C0001
    ChrTalk(
        0xFE,
        (
            "呼……这个地方太棒了，\x01",
            "来多少次都不会腻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "今天本打算在这里看书，\x01",
            "但光是欣赏景色\x01",
            "就已经很满足了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "如果不嫌弃，\x01",
            "这本书就给你们看吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '沐浴阳光的阿尼艾丝10卷'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('沐浴阳光的阿尼艾丝10卷', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x189, 1)
    Jump("loc_14A2")

    label("loc_1433")


    #C0005
    ChrTalk(
        0xFE,
        (
            "呼……这个地方太棒了，\x01",
            "来多少次都不会腻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "只要看到这里的景色，\x01",
            "对那起袭击事件的恐惧\x01",
            "也渐渐消散了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14A2")

    Jump("loc_1521")

    label("loc_14A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1521")

    #C0007
    ChrTalk(
        0xFE,
        (
            "虽然站在这里完全看不到，\x01",
            "但警备队应该正在\x01",
            "那个方位战斗吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "在如此优美的景色下，却……\x01",
            "真是令人悲哀啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1521")

    TalkEnd(0xFE)
    Return()

    # Function_4_132C end

    def Function_5_1525(): pass

    label("Function_5_1525")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_15A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1547")
    TalkEnd(0xFE)
    Call(0, 7)
    Return()

    label("loc_1547")


    #C0009
    ChrTalk(
        0x9,
        (
            "#11223F……各位一定\x01",
            "没问题的。\x02\x03",

            "#11222F琪雅……\x01",
            "我最重要的朋友，\x01",
            "就拜托大家了……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_160E")

    label("loc_15A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_160E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AF, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C0")
    Call(0, 6)
    Jump("loc_160E")

    label("loc_15C0")


    #C0010
    ChrTalk(
        0x9,
        (
            "#11228F我爸爸……\x01",
            "还有琪雅\x01",
            "就拜托大家了。\x02\x03",

            "#11223F我会一直在这里等着的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_160E")

    TalkEnd(0xFE)
    Return()

    # Function_5_1525 end

    def Function_6_1612(): pass

    label("Function_6_1612")

    OP_93(0x9, 0x87, 0x0)

    #C0011
    ChrTalk(
        0x9,
        "#11221F爸爸，琪雅……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        (
            "#00005F小滴……\x01",
            "你在这里啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x9, 0x0, 500)

    #C0013
    ChrTalk(
        0x9,
        (
            "#11220F是大家啊……\x01",
            "我在看\x01",
            "那棵大树。\x02\x03",

            "#11230F爸爸和琪雅\x01",
            "真的在那种地方吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#00203F……嗯，不会错的。\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        (
            "#00108F但不知他们在\x01",
            "大树内的什么地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        "#11223F是吗………………\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00003F……小滴，等着吧。\x02\x03",

            "#00001F我们一定会把亚里欧斯先生\x01",
            "和琪雅带回来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        "#00302F嗯，所以你就别担心了。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "#11223F……好的。\x02\x03",

            "#11221F我爸爸……\x01",
            "还有琪雅\x01",
            "就拜托大家了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0x87, 0x0)
    SetScenarioFlags(0x1AF, 2)
    Return()

    # Function_6_1612 end

    def Function_7_17F2(): pass

    label("Function_7_17F2")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_4B(0x9, 0xFF)
    OP_68(7690, 1100, -15570, 0)
    MoveCamera(110, 28, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(9990, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 7530, 0, -15000, 135)
    SetChrPos(0x1, 9360, 0, -14520, 180)
    SetChrPos(0x2, 6860, 0, -16500, 90)
    SetChrPos(0x3, 8570, 0, -13930, 180)
    SetChrPos(0x4, 5900, 0, -15300, 110)
    SetChrPos(0x5, 7050, 0, -13540, 155)
    OP_93(0x9, 0x13B, 0x0)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人将打倒了\x01",
            "亚里欧斯……\x02\x03",

            "以及他并非是杀害\x01",
            "盖伊的真凶等情况\x01",
            "向小滴做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(1000, 0)
    OP_0D()

    #C0021
    ChrTalk(
        0x9,
        "#11225F……是这样吗……\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#6P#00004F……嗯。\x02\x03",

            "#00000F亚里欧斯先生一定\x01",
            "会回到小滴身边的……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        "#11233F……呜……呜……\x02",
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x9,
        (
            "#11234F呜呜……太好了……\x02\x03",

            "#11233F爸爸他……没有向他最重要的朋友……\x01",
            "没有向罗伊德警官的哥哥\x01",
            "下手……\x02\x03",

            "#11234F我一直在想，如果凶手\x01",
            "真的是爸爸，爸爸也许就\x01",
            "再也不能回头了……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x102,
        "#6P#00108F小滴……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#6P#00002F哈哈……我不是和你说过嘛，\x01",
            "这个世界上绝不存在\x01",
            "无法回头的路。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B6F")

    #C0027
    ChrTalk(
        0x10A,
        (
            "#6P#00602F……等着吧，\x01",
            "我保证会把\x01",
            "马克莱因带回来。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C14")

    label("loc_1B6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1BC0")

    #C0028
    ChrTalk(
        0x109,
        (
            "#6P#10102F等着吧，\x01",
            "我们一定会把\x01",
            "亚里欧斯先生带回来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C14")

    label("loc_1BC0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C14")

    #C0029
    ChrTalk(
        0x105,
        (
            "#6P#10402F我们一定会把\x01",
            "亚里欧斯先生带回来。\x01",
            "放心吧，一言为定。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C14")


    #C0030
    ChrTalk(
        0x9,
        "#11222F呜……嗯……！！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        (
            "#12P#00202F……接下来，\x01",
            "就只剩下夺回琪雅了。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x104,
        (
            "#6P#00309F嗯，这也是为了让小滴\x01",
            "绽开笑容啊！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CDE")

    #C0033
    ChrTalk(
        0x105,
        (
            "#6P#10409F呵呵，事到如今，\x01",
            "无论如何都必须成功。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D66")

    label("loc_1CDE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D20")

    #C0034
    ChrTalk(
        0x109,
        (
            "#6P#10109F事到如今，\x01",
            "无论如何都要成功！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D66")

    label("loc_1D20")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D66")

    #C0035
    ChrTalk(
        0x106,
        (
            "#6P#10709F事到如今，\x01",
            "无论如何都必须\x01",
            "成功才行呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D66")


    #C0036
    ChrTalk(
        0x9,
        (
            "#11223F……大家能打败我爸爸，\x01",
            "接下来也一定没问题的。\x02\x03",

            "#11227F琪雅……\x01",
            "我最重要的朋友\x01",
            "就拜托大家了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_93(0x9, 0x87, 0x0)
    OP_4C(0x9, 0xFF)
    SetScenarioFlags(0x1AF, 1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_7_17F2 end

    def Function_8_1DFD(): pass

    label("Function_8_1DFD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    OP_68(23800, -43600, 6100, 0)
    MoveCamera(305, 17, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(12000, 0)
    SetChrPos(0x101, 23800, -44600, 6100, 90)
    SetChrPos(0x102, 23800, -44600, 7200, 90)
    SetChrPos(0x109, 23000, -44600, 7000, 90)
    SetChrPos(0x103, 23000, -44600, 5900, 90)
    SetChrPos(0x104, 22200, -44600, 5700, 90)
    SetChrPos(0x105, 23600, -44600, 5100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 20800, -44600, 7500, 90)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1500, 0)
    MoveCamera(305, 23, 0, 6000)
    OP_6E(1100, 6000)
    SetCameraDistance(82000, 6000)
    OP_6F(0x79)
    Sleep(500)
    Fade(1000)
    OP_68(0, -53600, -25000, 0)
    MoveCamera(315, -15, 15, 0)
    OP_6E(1100, 0)
    SetCameraDistance(80000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SetChrFlags(0xC, 0x8)
    OP_68(0, -73600, -75000, 11000)
    MoveCamera(215, 30, 15, 11000)
    SetCameraDistance(180000, 11000)
    OP_6F(0x79)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x102, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x104, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x109, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("c1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_8_1DFD end

    def Function_9_2147(): pass

    label("Function_9_2147")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05600.itc", 0x1E)
    LoadChrToIndex("apl/ch51259.itc", 0x1F)
    SoundLoad(803)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrPos(0x101, -19000, -6000, 0, 270)
    SetChrPos(0x102, -19000, -6000, 0, 270)
    SetChrPos(0x103, -19000, -6000, 0, 270)
    SetChrPos(0x104, -19000, -6000, 0, 270)
    SetChrPos(0x109, -19000, -6000, 0, 270)
    SetChrPos(0x105, -19000, -6000, 0, 270)
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
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -19000, -6000, 0, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-20000, -5000, 0, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-23000, -5000, 0, 6000)
    SetCameraDistance(16000, 6000)
    BeginChrThread(0xC, 3, 0, 16)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 13)
    WaitChrThread(0x109, 3)

    #C0037
    ChrTalk(
        0x109,
        "#11P#10109F哇啊啊……！\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 3)

    #C0038
    ChrTalk(
        0x105,
        (
            "#11P#10302F这……\x01",
            "实在是壮观啊。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_68(0, 0, 0, 9000)
    MoveCamera(225, 13, 0, 9000)
    OP_6E(900, 9000)
    SetCameraDistance(130000, 9000)
    BeginChrThread(0xC, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 17)
    Sleep(900)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 17)
    OP_6F(0x79)
    EndChrThread(0xC, 0xFF)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    SetChrPos(0x101, -19700, -4400, -20300, 180)
    SetChrPos(0x102, -20300, -4400, -19700, 180)
    SetChrPos(0x103, -20000, -4400, -20000, 180)
    SetChrPos(0x104, -19700, -4400, -20300, 180)
    SetChrPos(0x109, -20300, -4400, -19700, 180)
    SetChrPos(0x105, -20000, -4400, -20000, 180)
    SetChrPos(0xC, -20000, -4400, -20000, 180)
    BeginChrThread(0x101, 0, 0, 18)
    Sleep(1000)
    Fade(1000)
    OP_68(-29000, -3900, -29000, 0)
    MoveCamera(225, 17, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(16500, 0)
    OP_0D()
    OP_68(-24400, -3900, -38800, 6000)
    MoveCamera(205, 19, 0, 6000)
    SetCameraDistance(23500, 6000)
    OP_6F(0x79)
    WaitChrThread(0x109, 3)

    #C0039
    ChrTalk(
        0x101,
        (
            "#00004F#11P哈哈……\x01",
            "让人叹为观止……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        "#00102F#11P嗯，是呀……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x103, 3)

    #C0041
    ChrTalk(
        0x103,
        (
            "#00202F#11P……看起来，城市\x01",
            "就像微缩模型一样。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x104,
        (
            "#00309F#11P嘿～到了晚上，\x01",
            "景色一定会更加美丽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-28800, -3300, -31300, 0)
    MoveCamera(205, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()

    #C0043
    ChrTalk(
        0xC,
        (
            "#12P#02809F哈哈，我准备将\x01",
            "这个地方作为展望台，\x01",
            "日后向市民们开放。\x02\x03",

            "#02800F如果光让政府人员享受，\x01",
            "未免也太浪费了嘛。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_262F():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_262F)
    Sleep(50)

    def lambda_263F():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_263F)
    Sleep(50)

    def lambda_264F():
        TurnDirection(0x103, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_264F)
    Sleep(50)

    def lambda_265F():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_265F)
    Sleep(50)

    def lambda_266F():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_266F)
    Sleep(50)

    def lambda_267F():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_267F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    def lambda_26A4():

        label("loc_26A4")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_26A4")

    QueueWorkItem2(0x101, 2, lambda_26A4)

    def lambda_26B6():

        label("loc_26B6")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_26B6")

    QueueWorkItem2(0x102, 2, lambda_26B6)

    def lambda_26C8():

        label("loc_26C8")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_26C8")

    QueueWorkItem2(0x103, 2, lambda_26C8)

    def lambda_26DA():

        label("loc_26DA")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_26DA")

    QueueWorkItem2(0x109, 2, lambda_26DA)

    def lambda_26EC():

        label("loc_26EC")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_26EC")

    QueueWorkItem2(0x105, 2, lambda_26EC)

    def lambda_26FE():

        label("loc_26FE")

        TurnDirection(0xFE, 0xC, 500)
        Yield()
        Jump("loc_26FE")

    QueueWorkItem2(0x104, 2, lambda_26FE)

    #C0044
    ChrTalk(
        0x101,
        "#00002F#5P嗯，这想法不错啊。\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00109F#5P呵呵，好想带\x01",
            "琪雅来这里呢。\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0xC, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0046
    ChrTalk(
        0xC,
        "#12P#02805F哦，不好意思。\x02",
    )

    CloseMessageWindow()
    OP_93(0xC, 0x5A, 0x1F4)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xC, 0x1F)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x10)
    OP_0D()
    Sound(804, 0, 100, 0)
    OP_24(0x323)
    Sleep(300)
    SetChrSubChip(0xC, 0x1)
    Sleep(300)

    #C0047
    ChrTalk(
        0xC,
        (
            "#11P#02801F嗯，是我。\x02\x03",

            "#02803F……是吗，知道了，\x01",
            "我这就过去。\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    SetChrSubChip(0xC, 0x0)
    Sleep(300)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x2)
    ClearChrFlags(0xC, 0x10)
    TurnDirection(0xC, 0x101, 500)
    Sleep(300)

    #C0048
    ChrTalk(
        0xC,
        (
            "#12P#02800F首脑们好像已经\x01",
            "到达兰花塔下了。\x02\x03",

            "非常抱歉，\x01",
            "我要失陪了。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x101,
        (
            "#00004F#5P是吗……\x01",
            "真是非常感谢您。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        "#00204F#5P多谢您的引领。\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        "#00309F#5P呀～真是太开心了。\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x109,
        "#10102F#5P这真是一次愉快的体验！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xC,
        (
            "#12P#02804F哈哈，彼此彼此，\x01",
            "我也充分转换了心情。\x02\x03",

            "#02800F那么，稍后再见了，\x01",
            "警备工作要加油啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x101,
        "#00000F#5P是，交给我们吧。\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#10302F#5P嗯，为了回报您的引荐之情，\x01",
            "我一定会努力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#00104F#5P我会向女神祈祷，\x01",
            "祝愿本次会议顺利成功。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xC,
        "#12P#02809F哈哈，我也会祈祷的。\x02",
    )

    CloseMessageWindow()
    OP_92(0xC, 0xFFFFADF8, 0xFFFFADF8, 0x1F4)
    OP_68(-25800, -3300, -28300, 5000)
    SetCameraDistance(17500, 5000)

    def lambda_2A55():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2A55)
    WaitChrThread(0xC, 1)
    OP_6F(0x79)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    SetChrFlags(0xC, 0x80)
    Fade(500)
    OP_68(-28350, -3300, -32000, 0)
    MoveCamera(205, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0058
    ChrTalk(
        0x101,
        (
            "#00000F#5P好了，我们去找\x01",
            "达德利警官吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2AFD():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2AFD)
    Sleep(50)

    def lambda_2B0D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2B0D)
    Sleep(50)

    def lambda_2B1D():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2B1D)
    Sleep(50)

    def lambda_2B2D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2B2D)
    Sleep(50)

    def lambda_2B3D():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2B3D)
    Sleep(50)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    #C0059
    ChrTalk(
        0x103,
        (
            "#12P#00202F我记得他在三十四层的\x01",
            "警备对策室。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#6P#00306F话说回来，要是能一直这样下去，\x01",
            "不发生任何意外就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        "#6P#10108F是啊……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    StopSound(132, 1000, 100)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x323)
    SetScenarioFlags(0x22, 1)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_9_2147 end

    def Function_10_2C5B(): pass

    label("Function_10_2C5B")


    def lambda_2C60():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C60)

    def lambda_2C7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2C7A)
    WaitChrThread(0xFE, 1)

    def lambda_2C8F():
        OP_95(0xFE, -23500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2C8F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_10_2C5B end

    def Function_11_2CB0(): pass

    label("Function_11_2CB0")


    def lambda_2CB5():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CB5)

    def lambda_2CCF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2CCF)
    WaitChrThread(0xFE, 1)

    def lambda_2CE4():
        OP_95(0xFE, -23500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2CE4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_11_2CB0 end

    def Function_12_2D05(): pass

    label("Function_12_2D05")


    def lambda_2D0A():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D0A)

    def lambda_2D24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D24)
    WaitChrThread(0xFE, 1)

    def lambda_2D39():
        OP_95(0xFE, -21500, -6000, -600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D39)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_12_2D05 end

    def Function_13_2D5A(): pass

    label("Function_13_2D5A")


    def lambda_2D5F():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D5F)

    def lambda_2D79():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2D79)
    WaitChrThread(0xFE, 1)

    def lambda_2D8E():
        OP_95(0xFE, -21500, -6000, 600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2D8E)
    WaitChrThread(0xFE, 1)
    Sound(107, 0, 100, 0)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_79(0x0)
    SetMapObjFlags(0x0, 0x10)
    Return()

    # Function_13_2D5A end

    def Function_14_2DCA(): pass

    label("Function_14_2DCA")


    def lambda_2DCF():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DCF)

    def lambda_2DE9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2DE9)
    WaitChrThread(0xFE, 1)

    def lambda_2DFE():
        OP_95(0xFE, -22500, -6000, 1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2DFE)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_14_2DCA end

    def Function_15_2E1F(): pass

    label("Function_15_2E1F")


    def lambda_2E24():
        OP_95(0xFE, -20700, -6000, 0, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E24)

    def lambda_2E3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E3E)
    WaitChrThread(0xFE, 1)

    def lambda_2E53():
        OP_95(0xFE, -22500, -6000, -1200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E53)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_15_2E1F end

    def Function_16_2E74(): pass

    label("Function_16_2E74")


    def lambda_2E79():
        OP_95(0xFE, -25000, -6000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2E79)

    def lambda_2E93():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2E93)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_2E74 end

    def Function_17_2EA4(): pass

    label("Function_17_2EA4")

    OP_92(0xFE, 0xFFFF9FE8, 0xFFFFD8F0, 0x1F4)

    def lambda_2EB6():
        OP_95(0xFE, -24600, -6000, -10000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EB6)
    WaitChrThread(0xFE, 1)

    def lambda_2ED4():
        OP_95(0xFE, -21000, -4400, -18600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2ED4)
    WaitChrThread(0xFE, 1)

    def lambda_2EF2():
        OP_95(0xFE, -21000, -4400, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2EF2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_17_2EA4 end

    def Function_18_2F0C(): pass

    label("Function_18_2F0C")

    BeginChrThread(0xC, 3, 0, 25)
    Sleep(700)
    BeginChrThread(0x101, 3, 0, 19)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 20)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 23)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 22)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 24)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 21)
    Return()

    # Function_18_2F0C end

    def Function_19_2F49(): pass

    label("Function_19_2F49")


    def lambda_2F4E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F4E)
    WaitChrThread(0xFE, 1)

    def lambda_2F6C():
        OP_95(0xFE, -28000, -4400, -32600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F6C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_19_2F49 end

    def Function_20_2F8D(): pass

    label("Function_20_2F8D")


    def lambda_2F92():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2F92)
    WaitChrThread(0xFE, 1)

    def lambda_2FB0():
        OP_95(0xFE, -29800, -4400, -32800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FB0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_20_2F8D end

    def Function_21_2FD1(): pass

    label("Function_21_2FD1")


    def lambda_2FD6():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FD6)
    WaitChrThread(0xFE, 1)

    def lambda_2FF4():
        OP_95(0xFE, -28700, -4400, -31400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2FF4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_21_2FD1 end

    def Function_22_3015(): pass

    label("Function_22_3015")


    def lambda_301A():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_301A)
    WaitChrThread(0xFE, 1)

    def lambda_3038():
        OP_95(0xFE, -26400, -4400, -31800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3038)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_22_3015 end

    def Function_23_3059(): pass

    label("Function_23_3059")


    def lambda_305E():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_305E)
    WaitChrThread(0xFE, 1)

    def lambda_307C():
        OP_95(0xFE, -30700, -4400, -31900, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_307C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xBE, 0x1F4)
    Return()

    # Function_23_3059 end

    def Function_24_309D(): pass

    label("Function_24_309D")


    def lambda_30A2():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30A2)
    WaitChrThread(0xFE, 1)

    def lambda_30C0():
        OP_95(0xFE, -27100, -4400, -30600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30C0)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_24_309D end

    def Function_25_30E1(): pass

    label("Function_25_30E1")


    def lambda_30E6():
        OP_97(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_30E6)
    WaitChrThread(0xFE, 1)

    def lambda_3104():
        OP_95(0xFE, -29400, -4400, -28800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3104)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xA0, 0x1F4)
    Return()

    # Function_25_30E1 end

    def Function_26_3125(): pass

    label("Function_26_3125")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    LoadChrToIndex("chr/ch42250.itc", 0x1E)
    LoadChrToIndex("chr/ch42251.itc", 0x1F)
    LoadChrToIndex("chr/ch42350.itc", 0x20)
    LoadChrToIndex("chr/ch42351.itc", 0x21)
    LoadChrToIndex("chr/ch42550.itc", 0x22)
    LoadChrToIndex("chr/ch42551.itc", 0x23)
    SoundLoad(497)
    SetChrChipByIndex(0x1A, 0x21)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1B, 0x21)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1E, 0x21)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x1F, 0x21)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x20, 0x21)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, 10900, 4000, 4800, 0)
    SetChrChipByIndex(0x21, 0x23)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -10600, 3300, -3000, 270)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x22, 0x23)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -10600, 3300, -3000, 270)
    OP_A7(0x22, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x23, 0x23)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -10600, 3300, -3000, 270)
    OP_A7(0x23, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x24, 0x23)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -10600, 3300, -3000, 270)
    OP_A7(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x23)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -10600, 3300, -3000, 270)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    SetChrPos(0x26, -10600, 3300, -3000, 270)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x27, 0x23)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x27, -10600, 3300, -3000, 270)
    OP_A7(0x27, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x7, 0x16)
    OP_49()
    SetChrPos(0x16, 11000, 60000, 0, 170)
    OP_D5(0x16, 0x0, 0x29810, 0x0, 0x0)
    SetMapObjFlags(0x7, 0x1000)
    OP_74(0x7, 0x1E)
    OP_70(0x7, 0x3D)
    OP_71(0x7, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x17, 0x80)
    OP_78(0x6, 0x17)
    OP_49()
    SetChrPos(0x17, -11000, 62000, 0, 190)
    OP_D5(0x17, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0x6, 0x1000)
    OP_74(0x6, 0x1E)
    OP_70(0x6, 0x3D)
    OP_71(0x6, 0x3D, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xC, 0x18)
    OP_78(0xB, 0x19)
    OP_49()
    SetChrPos(0x18, 10000, 100, 0, 170)
    OP_D5(0x18, 0x0, 0x29810, 0x0, 0x0)
    SetChrPos(0x19, -10000, 100, 0, 190)
    OP_D5(0x19, 0x0, 0x2E630, 0x0, 0x0)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFlags(0xB, 0x1000)
    OP_68(0, 28000, 0, 0)
    MoveCamera(165, -35, 0, 0)
    OP_6E(1100, 0)
    SetCameraDistance(190000, 0)

    def lambda_34B7():
        OP_96(0xFE, 0x2AF8, 0x9C40, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_34B7)

    def lambda_34D1():
        OP_96(0xFE, 0xFFFFD508, 0xA410, 0x0, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_34D1)
    Sound(497, 2, 100, 0)
    MoveCamera(15, -35, 0, 9000)
    SetCameraDistance(110000, 9000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x16, 0xFF)
    EndChrThread(0x17, 0xFF)
    SetChrPos(0x17, -10000, 22000, 0, 190)
    SetChrPos(0x16, 10000, 20000, 0, 170)
    BeginChrThread(0x16, 3, 0, 31)
    BeginChrThread(0x17, 3, 0, 32)
    OP_68(0, 9000, 0, 0)
    MoveCamera(45, 40, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(45000, 0)
    OP_68(0, 2000, 0, 5000)
    MoveCamera(35, 17, 0, 5000)
    SetCameraDistance(35000, 5000)
    Sleep(1500)
    Sound(942, 0, 100, 0)
    WaitChrThread(0x16, 3)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    Sound(495, 0, 100, 0)
    Sound(833, 0, 50, 0)
    WaitChrThread(0x17, 3)
    OP_82(0xC8, 0xC8, 0xBB8, 0x12C)
    Sound(495, 0, 100, 0)
    Sound(833, 0, 50, 0)
    StopSound(497, 1000, 100)
    Sleep(300)
    Sound(105, 0, 100, 0)
    OP_71(0x6, 0x12D, 0x168, 0x0, 0x0)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 27)
    Sleep(1500)
    BeginChrThread(0x16, 3, 0, 28)
    Sleep(2500)
    Fade(500)
    OP_68(0, -1500, 0, 0)
    MoveCamera(0, 7, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(35000, 0)
    OP_0D()
    OP_68(0, -5000, 0, 10000)
    MoveCamera(90, 3, 0, 10000)
    SetCameraDistance(39000, 10000)
    Sleep(7000)
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_6F(0x79)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x1F1)
    SetScenarioFlags(0x22, 6)
    NewScene("c1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_26_3125 end

    def Function_27_36AC(): pass

    label("Function_27_36AC")

    ClearChrFlags(0x21, 0x80)
    BeginChrThread(0x21, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x22, 0x80)
    BeginChrThread(0x22, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x23, 0x80)
    BeginChrThread(0x23, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x24, 0x80)
    BeginChrThread(0x24, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x25, 0x80)
    BeginChrThread(0x25, 3, 0, 29)
    Sleep(4000)
    ClearChrFlags(0x26, 0x80)
    BeginChrThread(0x26, 3, 0, 29)
    Sleep(500)
    ClearChrFlags(0x27, 0x80)
    BeginChrThread(0x27, 3, 0, 29)
    Return()

    # Function_27_36AC end

    def Function_28_370C(): pass

    label("Function_28_370C")

    ClearChrFlags(0x1A, 0x80)
    BeginChrThread(0x1A, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1B, 0x80)
    BeginChrThread(0x1B, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1C, 0x80)
    BeginChrThread(0x1C, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1D, 0x80)
    BeginChrThread(0x1D, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x1E, 0x80)
    BeginChrThread(0x1E, 3, 0, 30)
    Sleep(2500)
    ClearChrFlags(0x1F, 0x80)
    BeginChrThread(0x1F, 3, 0, 30)
    Sleep(500)
    ClearChrFlags(0x20, 0x80)
    BeginChrThread(0x20, 3, 0, 30)
    Return()

    # Function_28_370C end

    def Function_29_376C(): pass

    label("Function_29_376C")


    def lambda_3771():
        OP_95(0xFE, -12600, 3300, -3000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3771)

    def lambda_378B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_378B)
    WaitChrThread(0xFE, 1)

    def lambda_37A0():
        OP_95(0xFE, -12000, 3300, -4800, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37A0)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 30, 0)

    def lambda_37CF():
        OP_9D(0xFE, 0xFFFFD440, 0x0, 0xFFFFDA80, 0x320, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37CF)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_3801():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3801)
    WaitChrThread(0xFE, 1)

    def lambda_381F():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_381F)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3842():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3842)
    WaitChrThread(0xFE, 1)

    def lambda_3861():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3861)
    Sleep(500)

    def lambda_387E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_387E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_29_376C end

    def Function_30_388F(): pass

    label("Function_30_388F")


    def lambda_3894():
        OP_95(0xFE, 8400, 4000, 4400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3894)
    WaitChrThread(0xFE, 1)

    def lambda_38B2():
        OP_95(0xFE, 6800, 4000, -1300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38B2)
    WaitChrThread(0xFE, 1)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_38DB():
        OP_9D(0xFE, 0x11F8, 0x0, 0xFFFFE890, 0xBE, 0x320)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38DB)
    WaitChrThread(0xFE, 1)
    Sound(326, 0, 40, 0)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_390D():
        OP_95(0xFE, 0, 0, -18500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_390D)
    WaitChrThread(0xFE, 1)

    def lambda_392B():
        OP_95(0xFE, 0, 0, -22000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_392B)
    WaitChrThread(0xFE, 1)
    ClearChrFlags(0xFE, 0x4)

    def lambda_394E():
        OP_9E(0xFE, 0x0, 0x0, 0x15F90, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_394E)
    WaitChrThread(0xFE, 1)

    def lambda_396D():
        OP_95(0xFE, -18000, -6000, 0, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_396D)
    Sleep(500)

    def lambda_398A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_398A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_30_388F end

    def Function_31_399B(): pass

    label("Function_31_399B")


    def lambda_39A0():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_39A0)

    def lambda_39B9():
        OP_D5(0xFE, 0x0, 0x2E630, 0x0, 0xED8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_39B9)

    def lambda_39D2():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39D2)
    Sleep(2800)

    def lambda_39EF():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_39EF)
    Sleep(300)

    def lambda_3A0C():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A0C)
    Sleep(300)

    def lambda_3A29():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A29)
    Sleep(300)

    def lambda_3A46():
        OP_96(0xFE, 0x2710, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A46)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x7, 0x20)
    OP_74(0x7, 0x0)
    Return()

    # Function_31_399B end

    def Function_32_3A6A(): pass

    label("Function_32_3A6A")


    def lambda_3A6F():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3A6F)

    def lambda_3A88():
        OP_D5(0xFE, 0x0, 0x29810, 0x0, 0xDAC)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_3A88)

    def lambda_3AA1():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AA1)
    Sleep(2500)

    def lambda_3ABE():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ABE)
    Sleep(300)

    def lambda_3ADB():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ADB)
    Sleep(300)

    def lambda_3AF8():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AF8)
    Sleep(300)

    def lambda_3B15():
        OP_96(0xFE, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B15)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x6, 0x20)
    OP_74(0x6, 0x0)
    Return()

    # Function_32_3A6A end

    def Function_33_3B39(): pass

    label("Function_33_3B39")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -19000, -6000, 0, 270)
    SetChrPos(0x102, -19000, -6000, 0, 270)
    SetChrPos(0x103, -19000, -6000, 0, 270)
    SetChrPos(0x104, -19000, -6000, 0, 270)
    SetChrPos(0x109, -19000, -6000, 0, 270)
    SetChrPos(0x105, -19000, -6000, 0, 270)
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
    ClearMapFlags(0x10000000)
    OP_68(-20000, -5000, 0, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(107, 0, 100, 0)
    ClearMapObjFlags(0x0, 0x10)
    OP_71(0x0, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x0)
    OP_68(-23000, -5000, 0, 6000)
    SetCameraDistance(16000, 6000)
    BeginChrThread(0x101, 3, 0, 10)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 15)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 14)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 12)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 13)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0062
    ChrTalk(
        0x102,
        "#11P#00105F啊……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 3)
    OP_68(-25000, -4500, 0, 2500)
    MoveCamera(335, 17, 0, 2500)
    SetCameraDistance(14500, 2500)
    OP_6F(0x79)
    Sleep(300)

    #C0063
    ChrTalk(
        0x109,
        (
            "#12P#10102F雨好像\x01",
            "稍小一些了。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00309F嗯……话说回来，\x01",
            "这里的景色还是如此壮观啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#12P#00002F嗯，如果在晴天过来，\x01",
            "肯定会更加美丽……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)
    Sleep(700)
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(400)

    #C0066
    ChrTalk(
        0x101,
        (
            "#11P#00005F约纳和主任\x01",
            "在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3E0C():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E0C)
    Sleep(50)

    def lambda_3E1C():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E1C)
    Sleep(50)

    def lambda_3E2C():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E2C)
    Sleep(50)

    def lambda_3E3C():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3E3C)
    Sleep(50)

    def lambda_3E4C():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3E4C)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)

    #C0067
    ChrTalk(
        0x103,
        (
            "#12P#00204F应该在塔顶的\x01",
            "某个角落。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x105,
        "#10300F找找看吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -22000, -6000, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x164, 7)
    ModifyEventFlags(1, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_33_3B39 end

    def Function_34_3EE5(): pass

    label("Function_34_3EE5")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadChrToIndex("apl/ch51405.itc", 0x20)
    LoadChrToIndex("chr/ch29300.itc", 0x21)
    SoundLoad(2280)
    SoundLoad(2683)
    SoundLoad(2281)
    SoundLoad(943)
    SoundLoad(938)
    SoundLoad(852)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    LoadEffect(0x2, "event/ev14010.eff")
    LoadEffect(0x3, "event/ev14026.eff")
    LoadEffect(0x4, "event/ev14027.eff")
    LoadEffect(0x5, "event/ev14028.eff")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis328.itp")
    CreatePortrait(1, 308, 154, 340, 186, 0, 0, 32, 36, 0, 0, 32, 32, 0xFFFFFF, 0x0, "c_vis329.itp")
    SetChrPos(0x101, 22400, -4400, -22300, 135)
    SetChrPos(0x103, 21700, -4400, -23000, 135)
    SetChrPos(0x102, 20700, -4400, -22300, 135)
    SetChrPos(0x104, 21700, -4400, -21300, 135)
    SetChrPos(0x109, 19700, -4400, -21900, 135)
    SetChrPos(0x105, 20700, -4400, -20900, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 28400, -4400, -27750, 45)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x4)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xA, 0x2)
    SetChrFlags(0xA, 0x20)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, 31900, -4400, -27650, 75)
    BeginChrThread(0xA, 2, 0, 36)
    ClearMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x8, 0x1000)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x2)
    OP_68(21700, -3200, -22650, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(15000, 1200)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_413B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_413B)

    #N0069
    NpcTalk(
        0xB,
        "罗伯兹主任的声音",
        "呀，正等你们呢。\x02",
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
    BeginChrThread(0x32, 1, 0, 41)
    OP_68(29300, -3200, -26900, 2000)
    MoveCamera(15, 17, 0, 2000)
    SetCameraDistance(13500, 2000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(27740, -3200, -26940, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0xA, 32200, -4400, -27850, 75)

    def lambda_4258():
        OP_97(0x101, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4258)
    Sleep(100)

    def lambda_4275():
        OP_97(0x103, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4275)
    Sleep(100)

    def lambda_4292():
        OP_97(0x104, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4292)
    Sleep(100)

    def lambda_42AF():
        OP_97(0x102, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_42AF)
    Sleep(100)

    def lambda_42CC():
        OP_97(0x105, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_42CC)
    Sleep(100)

    def lambda_42E9():
        OP_97(0x109, 0x11F8, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_42E9)
    WaitChrThread(0x109, 0)

    #C0070
    ChrTalk(
        0x101,
        (
            "#00002F#5P这就是可以探知\x01",
            "警报信号的装置吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xB,
        (
            "#12P嗯，但如果光靠它，\x01",
            "也只能探测到半径１０赛尔矩\x01",
            "范围内的信号。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xB,
        "#12P所以，接下来就需要缇欧出马了。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        (
            "#5P#00204F我没有问题。\x02\x03",

            "#00200F不过……\x01",
            "下雨不会造成影响吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "#12P嗯，雨已经很小了，\x01",
            "应该不会有太大影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        (
            "#12P但让缇欧遭受风吹雨打，\x01",
            "我实在是于心不忍啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xB,
        (
            "#12P对了，缇欧，\x01",
            "在你启动传感器的时候，\x01",
            "我来给你撑伞……\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#5P#00203F不用了，\x01",
            "那样反而会分散注意力。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xB,
        "#12P呜……\x02",
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
    Sleep(1000)
    EndChrThread(0xA, 0x2)
    StopSound(938, 500, 40)

    #C0079
    ChrTalk(
        0xA,
        (
            "#02303F#5P好了，\x01",
            "我已经准备完毕了。\x02\x03",

            "#02300F你随时都可以\x01",
            "启动永世系统。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        (
            "#5P#00204F那就开始吧。\x02\x03",

            "#00200F已经输入过林小姐她们的\x01",
            "艾尼格玛Ⅱ号码了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xB,
        (
            "#12P嗯，事先就向协会\x01",
            "问到了号码。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xB,
        "#12P已经输入测定器了。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        "#5P#00202F明白了。\x02",
    )

    CloseMessageWindow()

    def lambda_464C():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_464C)
    Sleep(50)

    def lambda_465C():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_465C)
    Sleep(50)

    def lambda_466C():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_466C)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    def lambda_4688():

        label("loc_4688")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_4688")

    QueueWorkItem2(0x101, 2, lambda_4688)

    def lambda_469A():

        label("loc_469A")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_469A")

    QueueWorkItem2(0x102, 2, lambda_469A)

    def lambda_46AC():

        label("loc_46AC")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_46AC")

    QueueWorkItem2(0x109, 2, lambda_46AC)

    def lambda_46BE():

        label("loc_46BE")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_46BE")

    QueueWorkItem2(0x105, 2, lambda_46BE)

    def lambda_46D0():

        label("loc_46D0")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_46D0")

    QueueWorkItem2(0x104, 2, lambda_46D0)

    def lambda_46E2():

        label("loc_46E2")

        TurnDirection(0xFE, 0x103, 500)
        Yield()
        Jump("loc_46E2")

    QueueWorkItem2(0xB, 2, lambda_46E2)
    Sleep(150)

    #C0084
    ChrTalk(
        0x101,
        "#11P#00001F缇欧，拜托你了。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#00108F#5P请务必要找到\x01",
            "林小姐她们的所在地。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x15E, 0x1F4)
    Sleep(100)

    #C0086
    ChrTalk(
        0x103,
        "#6P#00202F好，那么──\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)
    OP_92(0x103, 0x6C98, 0xFFFF8C60, 0x1F4)
    OP_68(28160, -3400, -29390, 2000)

    def lambda_4795():
        OP_95(0xFE, 27800, -4400, -29600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4795)
    WaitChrThread(0x103, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0xB, 0x2)
    OP_93(0x103, 0x87, 0x1F4)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()

    def lambda_47E6():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_47E6)
    Sleep(500)
    #Sound(2280, 255, 100, 0)    #voice#Tio

    #C0087
    ChrTalk(
        0x103,
        (
            "#5P#00203F#30W永世系统启动。\x02\x03",

            "#00201F#30W开始以矩阵方式\x01",
            "连接测定器……\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x8E8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7352", 0)
    MoveCamera(346, 20, 0, 18000)
    SetCameraDistance(15950, 18000)
    Sound(852, 2, 100, 0)
    Sound(943, 2, 100, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x5, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0xA, 0x29, 0x0, 0x0)
    OP_79(0x8)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Sound(938, 2, 50, 0)
    BeginChrThread(0xA, 2, 0, 36)

    #C0088
    ChrTalk(
        0xA,
        (
            "#02304F#6P确认连接。\x02\x03",

            "#02302F没有问题，\x01",
            "就这样继续吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xB,
        (
            "#5P测定器的导力供给\x01",
            "也稳定在高水平上。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        "#5P缇欧，拜托了。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x103,
        (
            "#5P#00203F好，\x01",
            "那我就开始了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0092
    ChrTalk(
        0x103,
        "#5P#00201F#2683V#40W#20A释放传感功能……\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1000)

    #C0093
    ChrTalk(
        0x103,
        (
            "#5P#00203F#20A#40W永世系统…#800W…\x01",
            "#30W#00207F#4S解除限制！\x02",
        )
    )
    #Auto

    Sleep(1200)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    MoveCamera(333, 19, -5, 4000)
    SetCameraDistance(22000, 4000)
    BeginChrThread(0x101, 3, 0, 38)
    BeginChrThread(0x103, 3, 0, 39)
    Sound(357, 0, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    EndChrThread(0xA, 0x2)
    Fade(500)
    OP_68(27800, -3300, -29600, 0)
    MoveCamera(100, 20, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    BeginChrThread(0xA, 2, 0, 37)
    OP_68(34800, -2800, -36600, 7000)
    MoveCamera(100, 10, -15, 7000)
    SetCameraDistance(36000, 7000)
    BeginChrThread(0xB, 3, 0, 35)
    OP_6F(0x79)
    WaitChrThread(0xB, 3)

    #C0094
    ChrTalk(
        0x104,
        "#00305F#6P哦哦……！\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x109,
        "#6P#10111F刚、刚才那是……\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x105,
        (
            "#10305F#6P好像有股『波流』一样的东西\x01",
            "扩散了出去……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0xA, 0x2)
    Fade(500)
    OP_68(28060, -3400, -29350, 0)
    MoveCamera(350, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    BeginChrThread(0xA, 2, 0, 36)
    OP_0D()
    OP_71(0x8, 0x5A, 0x64, 0x0, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    StopSound(852, 500, 90)
    StopSound(943, 500, 40)
    EndChrThread(0x103, 0x3)
    Sleep(500)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    StopBGM(0x1770)
    Sleep(500)

    #C0097
    ChrTalk(
        0x103,
        "#6P#00206F……呼。\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xB,
        "#5P嗯嗯，看来成功了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(27400, -3200, -27000, 1200)

    def lambda_4CAA():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4CAA)
    Sleep(50)

    def lambda_4CBA():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4CBA)
    Sleep(50)

    def lambda_4CCA():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4CCA)
    Sleep(50)

    def lambda_4CDA():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4CDA)
    Sleep(50)

    def lambda_4CEA():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4CEA)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0099
    ChrTalk(
        0x101,
        "#5P#00007F真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x102,
        (
            "#00101F#5P已经查到林小姐她们的\x01",
            "所在地了！？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    TurnDirection(0xB, 0x101, 500)

    #C0101
    ChrTalk(
        0xB,
        (
            "#12P嗯，但准确来说，\x01",
            "是艾尼格玛Ⅱ的所在地。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0102
    ChrTalk(
        0x103,
        (
            "#6P#00203F我也感知到了\x01",
            "两个警报信号。\x02\x03",

            "#00201F由这里向南，相当远的地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xA,
        (
            "#02302F#6P嗯，我现在就解析出来，\x01",
            "然后输出到地图情报上……\x02\x03",

            "#02309F（咔哒咔哒）……看，出来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    EndChrThread(0xA, 0x2)
    StopSound(938, 500, 40)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(2000)
    SetMessageWindowPos(10, 40, -1, -1)

    #A0104
    AnonymousTalk(
        0x101,
        "#00005F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 80, -1, -1)

    #A0105
    AnonymousTalk(
        0x109,
        (
            "#10101F这里是……\x01",
            "艾鲁姆湖的南侧……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 20, -1, -1)

    #A0106
    AnonymousTalk(
        0x104,
        (
            "#00301F这是怎么回事……\x01",
            "这种地方有什么东西吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(20, 80, -1, -1)

    #A0107
    AnonymousTalk(
        0x102,
        (
            "#00108F据、据我所知，\x01",
            "那里应该是杳无人烟的\x01",
            "湿地……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(80, 20, -1, -1)

    #A0108
    AnonymousTalk(
        0x105,
        (
            "#10301F两位游击士姐姐就在\x01",
            "那种地方吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 180, -1, -1)

    #A0109
    AnonymousTalk(
        0xA,
        (
            "#02305F虽然不太明白，\x01",
            "但事情似乎并不寻常。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(220, 60, -1, -1)

    #A0110
    AnonymousTalk(
        0xB,
        "嗯，真是令人担心啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    #A0111
    AnonymousTalk(
        0x103,
        "#00208F罗伊德前辈……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(10, 40, -1, -1)

    #A0112
    AnonymousTalk(
        0x101,
        "#00008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x101, 0x3)
    OP_68(31000, -3300, -28800, 0)
    MoveCamera(13, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x101, 30300, -4400, -29500, 55)
    SetChrPos(0x103, 30800, -4400, -30900, 15)
    SetChrPos(0x102, 29600, -4400, -28800, 55)
    SetChrPos(0x104, 28600, -4400, -28300, 100)
    SetChrPos(0x109, 28600, -4400, -30000, 55)
    SetChrPos(0x105, 29300, -4400, -30700, 55)
    SetChrPos(0xB, 30400, -4400, -26800, 100)
    SetChrPos(0xA, 31900, -4400, -27650, 75)
    OP_70(0x8, 0x2)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_93(0x101, 0xF0, 0x1F4)

    #C0113
    ChrTalk(
        0x101,
        (
            "#11P#00003F总之，我们先回\x01",
            "米歇尔先生那里吧。\x02\x03",

            "#00001F另外，以防万一，\x01",
            "还是先让警察总部\x01",
            "帮忙准备小艇为好。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_51C3():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_51C3)
    Sleep(50)

    def lambda_51D3():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_51D3)
    Sleep(50)

    def lambda_51E3():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_51E3)
    Sleep(50)

    def lambda_51F3():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_51F3)
    Sleep(50)

    def lambda_5203():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5203)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0114
    ChrTalk(
        0x102,
        "#00106F#5P是呀……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x109,
        (
            "#6P#10101F嗯，从这种情况来看，\x01",
            "事态很紧急！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5270():
        TurnDirection(0x101, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5270)
    Sleep(50)

    def lambda_5280():
        TurnDirection(0x102, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5280)
    Sleep(50)

    def lambda_5290():
        TurnDirection(0x103, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5290)
    Sleep(50)

    def lambda_52A0():
        TurnDirection(0x104, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_52A0)
    Sleep(50)

    def lambda_52B0():
        TurnDirection(0x109, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_52B0)
    Sleep(50)

    def lambda_52C0():
        TurnDirection(0x105, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_52C0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0116
    ChrTalk(
        0x101,
        (
            "#6P#00000F罗伯兹主任、约纳，\x01",
            "多谢你们的协助。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5318():
        TurnDirection(0xB, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 0, lambda_5318)
    Sleep(50)

    def lambda_5328():
        TurnDirection(0xA, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_5328)
    Sleep(50)
    WaitChrThread(0xB, 0)
    WaitChrThread(0xA, 0)

    #C0117
    ChrTalk(
        0xB,
        (
            "#5P哪里哪里，\x01",
            "收尾工作就交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        "#02302F#11P嗯，你们多加小心啊～\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15500, 2000)
    StopSound(132, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x3AF)
    OP_24(0x3AA)
    OP_24(0x354)
    SetScenarioFlags(0x22, 1)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_3EE5 end

    def Function_35_53C6(): pass

    label("Function_35_53C6")

    Sleep(2600)
    StopEffect(0x2, 0x2)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 29400, -2900, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(1014, 0, 100, 0)
    Sleep(1000)
    Sound(895, 0, 100, 0)
    PlayEffect(0x5, 0xFF, 0x103, 0x1, 0, 1500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    Sound(998, 0, 100, 0)
    Sound(922, 0, 100, 0)
    Sound(833, 0, 40, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x2, 0xFF, 0x103, 0x1, 0, 2000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    Sleep(1000)
    CancelBlur(1500)
    Sleep(2000)
    Return()

    # Function_35_53C6 end

    def Function_36_54BE(): pass

    label("Function_36_54BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54DC")
    SetChrSubChip(0xFE, 0x4)
    Sleep(90)
    SetChrSubChip(0xFE, 0x5)
    Sleep(90)
    Jump("Function_36_54BE")

    label("loc_54DC")

    Return()

    # Function_36_54BE end

    def Function_37_54DD(): pass

    label("Function_37_54DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54FB")
    SetChrSubChip(0xFE, 0x0)
    Sleep(90)
    SetChrSubChip(0xFE, 0x1)
    Sleep(90)
    Jump("Function_37_54DD")

    label("loc_54FB")

    Return()

    # Function_37_54DD end

    def Function_38_54FC(): pass

    label("Function_38_54FC")

    Sound(943, 2, 50, 0)
    OP_71(0x8, 0x29, 0x32, 0x0, 0x0)
    OP_79(0x8)
    Sound(311, 0, 50, 0)
    PlayEffect(0x3, 0x2, 0xFF, 0x0, 29400, -4400, -26600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_71(0x8, 0x32, 0x59, 0x0, 0x20)
    Return()

    # Function_38_54FC end

    def Function_39_555B(): pass

    label("Function_39_555B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5579")
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_39_555B")

    label("loc_5579")

    Return()

    # Function_39_555B end

    def Function_40_557A(): pass

    label("Function_40_557A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_55C1")
    Sound(1021, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Jump("Function_40_557A")

    label("loc_55C1")

    Return()

    # Function_40_557A end

    def Function_41_55C2(): pass

    label("Function_41_55C2")

    Sound(938, 2, 0, 0)
    Sleep(200)
    OP_25(0x3AA, 0x5)
    Sleep(200)
    OP_25(0x3AA, 0xA)
    Sleep(200)
    OP_25(0x3AA, 0xF)
    Sleep(200)
    OP_25(0x3AA, 0x14)
    Sleep(200)
    OP_25(0x3AA, 0x19)
    Sleep(200)
    OP_25(0x3AA, 0x1E)
    Sleep(200)
    OP_25(0x3AA, 0x23)
    Sleep(200)
    OP_25(0x3AA, 0x28)
    Sleep(200)
    OP_25(0x3AA, 0x2D)
    Sleep(200)
    OP_25(0x3AA, 0x32)
    Return()

    # Function_41_55C2 end

    def Function_42_560F(): pass

    label("Function_42_560F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("apl/ch51545.itc", 0x20)
    LoadChrToIndex("chr/ch03300.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    LoadChrToIndex("chr/ch13400.itc", 0x24)
    LoadChrToIndex("chr/ch03600.itc", 0x25)
    LoadChrToIndex("chr/ch03500.itc", 0x26)
    LoadChrToIndex("apl/ch51548.itc", 0x27)
    LoadChrToIndex("apl/ch51543.itc", 0x28)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    LoadEffect(0x0, "event/ev500_00.eff")
    LoadEffect(0x1, "event/ev10005.eff")
    LoadEffect(0x2, "event/ev10001.eff")
    LoadEffect(0x4, "event/ev15071.eff")
    LoadEffect(0x5, "event/ev17022.eff")
    LoadEffect(0x6, "event/ev10008.eff")
    LoadEffect(0x7, "event/eva03_01.eff")
    SoundLoad(832)
    SoundLoad(852)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -1000, 180)
    OP_8E(0xC, "迪塔总统")
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 1600, 0, -5000, 0)
    OP_A7(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 300, -5000, 0)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -1200, 0, 400, 180)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -2400, 0, 400, 180)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, 400, 0, 1000, 180)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4300, 90)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5000, 0, -2900, 90)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -5500, 0, -5000, 90)
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x5, 0x4)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x0)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x9, 0x29)
    OP_D5(0x29, 0x0, 0x20F58, 0x0, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    SetMapObjFlags(0x9, 0x4)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0x0)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    OP_78(0xA, 0x2A)
    OP_D5(0x2A, 0x0, 0x36EE8, 0x0, 0x0)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    OP_74(0xA, 0x1E)
    OP_70(0xA, 0x0)
    SetChrFlags(0x2A, 0x1)
    OP_52(0x2A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(0, 0, 0, 0)
    MoveCamera(180, 25, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(100000, 0)
    MoveCamera(45, 15, 0, 10000)
    OP_68(0, 1000, 0, 10000)
    SetCameraDistance(12000, 10000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 1300, -3000, 0)
    MoveCamera(120, 17, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12000, 0)
    SetCameraDistance(14000, 5000)
    OP_0D()
    BeginChrThread(0x32, 1, 0, 50)
    BeginChrThread(0x10, 3, 0, 45)
    Sleep(700)
    BeginChrThread(0x11, 3, 0, 45)
    Sleep(1100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1)
    CancelBlur(1500)
    WaitChrThread(0x10, 3)
    Sound(852, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x10, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)

    #C0119
    ChrTalk(
        0xC,
        "#11302F#6P哦哦……！\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xD,
        "#04500F#6P哦……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xF,
        "#01605F#6P小不点，你……\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xE,
        (
            "#04602F#6P#N嘿～\x01",
            "好像很厉害呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(190, 1300, -3970, 1500)
    OP_95(0xC, -60, 0, -2170, 1200, 0x0)
    OP_6F(0x79)

    #C0123
    ChrTalk(
        0xC,
        (
            "#11304F#6P琪雅……不，\x01",
            "我还是效仿教团成员，\x01",
            "称呼您为『圣子』吧。\x02\x03",

            "#11302F欢迎您再次\x01",
            "降临于这个世界。\x02\x03",

            "作为库罗伊斯家族的现任当家，\x01",
            "能亲自迎接您，实在是荣幸之至。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0124
    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30W…………嗯。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0125
    ChrTalk(
        0x11,
        (
            "#10804F#11P呵呵，父亲，\x01",
            "寒暄就到此为止吧。\x02\x03",

            "#10802F差不多也该\x01",
            "领受他们的赠品了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xC,
        "#11305F#6P哦哦，对啊。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, 170, -1, -1)
    SetChrName("男人的声音")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，看来我的努力\x01",
            "终于要开花结果了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(-2000, 1300, -4300, 2000)
    MoveCamera(45, 13, 0, 2000)
    SetCameraDistance(13000, 2000)
    Sleep(1000)
    Sound(977, 0, 100, 0)
    Sound(832, 2, 100, 0)
    BeginChrThread(0x13, 3, 0, 46)
    Sleep(500)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x14, 3, 0, 46)
    Sleep(500)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x12, 3, 0, 46)

    def lambda_5FD9():
        TurnDirection(0xC, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_5FD9)
    Sleep(50)

    def lambda_5FE9():
        TurnDirection(0x11, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_5FE9)
    Sleep(50)

    def lambda_5FF9():
        TurnDirection(0x10, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_5FF9)
    Sleep(50)

    def lambda_6009():
        TurnDirection(0xD, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6009)
    Sleep(50)

    def lambda_6019():
        TurnDirection(0xE, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6019)
    Sleep(50)

    def lambda_6029():
        TurnDirection(0xF, 0x14, 500)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6029)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x10, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    OP_6F(0x79)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    Sleep(1)
    CancelBlur(1500)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x12, 3)
    OP_68(-2500, 1300, -4300, 1700)
    Sleep(1700)
    SetChrChipByIndex(0x14, 0x28)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x20)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x14, 0x2)
    Sleep(120)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0x14, 0x1)
    Sleep(400)
    OP_6F(0x79)
    StopSound(832, 500, 100)
    Sleep(300)

    #C0128
    ChrTalk(
        0x12,
        (
            "#6P#04900F#3C伟大至宝的再世啊……\x02\x03",

            "我谨代表『噬身之蛇』的盟主，\x01",
            "恭贺您降临于世。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x13,
        (
            "#04704F#6P呵呵，在此准备了一些薄礼，\x01",
            "权作『贡品』。\x02\x03",

            "#04700F还请您笑纳。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12302F#11P……谢谢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x0, 0x1F4)
    Fade(500)
    OP_68(0, 1700, -5000, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(11000, 0)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x20)
    ClearChrFlags(0x14, 0x10)
    ClearChrFlags(0x14, 0x2)
    Sound(812, 0, 100, 0)
    OP_4B(0x10, 0xFF)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x1)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(10500, 800)

    def lambda_61F0():
        TurnDirection(0xC, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_61F0)
    Sleep(0)

    def lambda_6200():
        TurnDirection(0xD, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_6200)
    Sleep(0)

    def lambda_6210():
        TurnDirection(0xE, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_6210)
    Sleep(0)

    def lambda_6220():
        TurnDirection(0xF, 0x10, 0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_6220)
    Sleep(0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitChrThread(0xF, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    OP_68(0, 7000, -5000, 4000)
    MoveCamera(0, -5, 0, 4000)
    Sleep(2000)
    StopSound(132, 2000, 40)
    StopSound(852, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x340)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_06.pmf", 0x229, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    OP_A7(0x28, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x29, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x2A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_93(0xC, 0x0, 0x1F4)
    OP_93(0xF, 0x2D, 0x1F4)
    OP_93(0xD, 0x13B, 0x1F4)
    OP_93(0xE, 0x13B, 0x1F4)
    OP_93(0x11, 0x0, 0x1F4)
    OP_93(0x13, 0x0, 0x1F4)
    OP_93(0x14, 0x0, 0x1F4)
    OP_93(0x12, 0x0, 0x1F4)
    BeginChrThread(0x28, 3, 0, 47)
    BeginChrThread(0x29, 3, 0, 48)
    BeginChrThread(0x2A, 3, 0, 49)
    OP_68(0, 19000, 1000, 0)
    MoveCamera(215, 40, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(25000, 0)
    OP_68(0, 3000, 1000, 8500)
    MoveCamera(135, 27, 0, 8500)
    SetCameraDistance(20000, 8500)
    SoundLoad(979)
    Sound(852, 2, 100, 0)
    Sound(132, 2, 100, 0)
    Sound(979, 2, 100, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 3, 0, 51)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x7, 0x3, 0xFF, 0x0, 0, 30000, 0, 0, 270, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0x4, 0xFF, 0x0, 0, 30000, 0, 0, 270, 0, 2000, 1000, 2000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(6500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    StopEffect(0x3, 0x0)
    StopEffect(0x4, 0x0)
    CancelBlur(0)
    Fade(500)
    OP_68(0, 4500, 6500, 0)
    MoveCamera(0, -23, 0, 0)
    OP_6E(900, 0)
    SetCameraDistance(9500, 0)
    SetChrFlags(0xF, 0x8)
    OP_68(0, 3000, 6500, 1500)
    MoveCamera(0, -13, 0, 1500)
    SetCameraDistance(10500, 1500)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 3000, 6500, 0)
    MoveCamera(23, 13, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(13000, 0)
    ClearChrFlags(0xF, 0x8)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4C(0x10, 0xFF)
    OP_68(0, 1900, 3000, 4000)
    MoveCamera(33, 9, 0, 4000)
    OP_6E(800, 4000)
    SetCameraDistance(21000, 4000)
    OP_6F(0x79)
    WaitChrThread(0x2A, 3)
    Sleep(300)

    #C0131
    ChrTalk(
        0xF,
        "#01607F#6P这、这是……！\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xE,
        (
            "#04612F#12P呜啊啊啊！\x01",
            "好威风啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xD,
        (
            "#04502F#12P呵呵……\x01",
            "很不错的玩具。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x11,
        (
            "#10804F#12P#N『神机永世』……\x02\x03",

            "#10800F供『至宝』展现奇迹的\x01",
            "三架媒介……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(800)
    OP_68(0, 1000, -1000, 0)
    MoveCamera(24, 12, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(15500, 0)
    SetCameraDistance(15000, 1500)
    OP_6F(0x79)
    OP_0D()

    #C0135
    ChrTalk(
        0xC,
        "#11P#11304F#12P……成品真是超乎预想。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x13, 500)

    #C0136
    ChrTalk(
        0xC,
        (
            "#11P#11300F『结社』的诸位，\x01",
            "我欠你们一个人情啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_66AA():
        TurnDirection(0x13, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_66AA)
    Sleep(50)

    def lambda_66BA():
        TurnDirection(0x12, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_66BA)
    Sleep(50)

    def lambda_66CA():
        TurnDirection(0x14, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_66CA)
    Sleep(50)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)

    def lambda_66E6():
        TurnDirection(0xFE, 0x10, 500)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_66E6)

    #C0137
    ChrTalk(
        0x13,
        (
            "#5P#04709F#6P哈哈，我们在资金方面\x01",
            "也一直承蒙相助嘛。\x02\x03",

            "#04702F可以直接使用极限级的\x01",
            "运行数据，也省了不少事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x12,
        (
            "#04900F#3C#6P#N而且此事\x01",
            "正合『盟主』之意……\x02\x03",

            "你不必认为亏欠人情。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0139
    ChrTalk(
        0x11,
        (
            "#10809F#11P呵呵……\x01",
            "还真是慷慨大方啊。\x02\x03",

            "#10802F琪雅，接下来就要\x01",
            "拜托你了，可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12301F#12P嗯……知道了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    Fade(250)
    Sound(802, 0, 50, 0)
    OP_4B(0x10, 0x1)
    SetChrChipByIndex(0x10, 0x27)
    SetChrSubChip(0x10, 0x2)
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(500)
    OP_68(0, 1900, 3000, 2000)
    MoveCamera(33, 9, 0, 2000)
    OP_6E(800, 2000)
    SetCameraDistance(21000, 2000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(273, 0, 70, 0)
    PlayEffect(0x4, 0x1, 0xFF, 0x0, -7000, 5000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x4, 0x2, 0xFF, 0x0, 9000, 5000, 2000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6903():
        OP_93(0xC, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_6903)
    Sleep(50)

    def lambda_6913():
        OP_93(0x11, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_6913)
    Sleep(50)

    def lambda_6923():
        OP_93(0x13, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_6923)
    Sleep(50)

    def lambda_6933():
        OP_93(0x12, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_6933)
    Sleep(50)

    def lambda_6943():
        OP_93(0x14, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_6943)
    Sleep(50)
    WaitChrThread(0xC, 0)
    WaitChrThread(0x11, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x14, 0)
    Sleep(2000)
    StopEffect(0x1, 0x2)
    StopEffect(0x2, 0x2)
    BeginChrThread(0x29, 3, 0, 43)
    BeginChrThread(0x2A, 3, 0, 44)
    WaitChrThread(0x29, 3)
    Sleep(2000)
    StopSound(979, 2000, 100)
    StopSound(132, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    CancelBlur(0)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x229), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x24, 3)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_42_560F end

    def Function_43_69B4(): pass

    label("Function_43_69B4")

    OP_68(0, 2900, 3000, 1500)
    SetCameraDistance(23000, 1500)
    Sound(935, 0, 100, 0)

    def lambda_69D9():
        OP_96(0xFE, 0xFFFFE4A8, 0x7D0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_69D9)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x14A, 0x15E, 0x0, 0x0)
    OP_79(0x9)
    OP_74(0x9, 0xA)
    OP_71(0x9, 0xA, 0x32, 0x0, 0x20)
    WaitChrThread(0x29, 1)
    OP_6F(0x79)
    Sound(905, 0, 100, 0)
    OP_71(0x9, 0x65, 0x6E, 0x15E, 0x0)
    OP_79(0x9)
    OP_71(0x9, 0x6F, 0x96, 0x0, 0x20)
    OP_68(0, 3900, -3000, 2500)
    MoveCamera(60, 7, 15, 2500)
    SetCameraDistance(40000, 6500)
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 500, 3000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 1000, 3000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 0, 10000, -7000, 90, 0, 0, 1500, 3000, 1500, 0xFF, 0, 0, 0, 0)
    Sound(833, 0, 50, 0)
    Sound(499, 0, 100, 0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x5, 0xFF, 0x9, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_9F(0x0, 0x29)
    OP_9F(0x1, 8000, 3000, -4000)
    OP_9F(0x1, 20000, 4000, -7000)
    OP_9F(0x1, 500000, 7000, -8000)

    def lambda_6CA4():
        OP_9F(0x2, 0x29, 20000, 0x6)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_6CA4)
    Sleep(1000)

    def lambda_6CB6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_6CB6)
    Sleep(300)

    def lambda_6CC6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_6CC6)
    OP_6F(0x41)
    Return()

    # Function_43_69B4 end

    def Function_44_6CD1(): pass

    label("Function_44_6CD1")

    Sound(978, 0, 50, 0)
    OP_25(0x3D3, 0x64)
    OP_71(0xA, 0x5A, 0x33, 0x0, 0x0)

    def lambda_6CEC():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_6CEC)
    WaitChrThread(0x2A, 1)
    OP_79(0xA)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)
    Sleep(2000)
    OP_9F(0x0, 0x2A)
    OP_9F(0x1, -5000, 3000, -3000)
    OP_9F(0x1, -20000, 4000, -6000)
    OP_9F(0x1, -200000, 7000, -7000)

    def lambda_6D4A():
        OP_9F(0x2, 0x2A, 10000, 0x6)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_6D4A)
    Sleep(1000)

    def lambda_6D5C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_6D5C)
    Sleep(100)

    def lambda_6D6C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6D6C)
    Sleep(100)

    def lambda_6D7C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_6D7C)
    Return()

    # Function_44_6CD1 end

    def Function_45_6D85(): pass

    label("Function_45_6D85")

    PlayEffect(0x1, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1800)

    def lambda_6DC4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6DC4)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_45_6D85 end

    def Function_46_6DD5(): pass

    label("Function_46_6DD5")

    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 80, 0)

    def lambda_6E1A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6E1A)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_46_6DD5 end

    def Function_47_6E2B(): pass

    label("Function_47_6E2B")

    SetChrPos(0x28, 0, 20000, 7000, 180)
    OP_71(0x5, 0x5B, 0x82, 0x0, 0x20)

    def lambda_6E4D():
        OP_96(0xFE, 0x0, 0x1F4, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E4D)
    WaitChrThread(0xFE, 1)
    OP_71(0x5, 0x83, 0x96, 0x0, 0x0)

    def lambda_6E77():
        OP_96(0xFE, 0x0, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6E77)
    WaitChrThread(0xFE, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x1F4, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 70, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    CancelBlur(500)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_47_6E2B end

    def Function_48_6EE5(): pass

    label("Function_48_6EE5")

    SetChrPos(0x29, -7000, 25000, 2000, 135)
    OP_71(0x9, 0xB, 0x32, 0x0, 0x20)

    def lambda_6F07():
        OP_96(0xFE, 0xFFFFE4A8, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F07)
    Sleep(13000)
    Sound(905, 0, 70, 0)
    OP_71(0x9, 0x122, 0x136, 0x0, 0x0)
    OP_79(0x9)
    OP_74(0x9, 0xF)
    OP_71(0x9, 0x136, 0x14A, 0x0, 0x20)
    WaitChrThread(0xFE, 1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0xFA, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(902, 0, 100, 0)
    Sound(833, 0, 70, 0)
    CancelBlur(500)
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_48_6EE5 end

    def Function_49_6F8E(): pass

    label("Function_49_6F8E")

    SetChrPos(0x2A, 9000, 28000, 2000, 225)
    OP_71(0xA, 0xA, 0x32, 0x0, 0x20)

    def lambda_6FB0():
        OP_96(0xFE, 0x2328, 0x3E8, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6FB0)
    WaitChrThread(0xFE, 1)
    OP_71(0xA, 0x33, 0x5A, 0x0, 0x0)

    def lambda_6FDA():
        OP_96(0xFE, 0x2328, 0x0, 0x7D0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6FDA)
    WaitChrThread(0xFE, 1)
    Sound(978, 0, 100, 0)
    Sound(833, 0, 100, 0)
    OP_25(0x3D3, 0x1E)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, 9000, 0, 2000, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_82(0x0, 0x2BC, 0xBB8, 0x1F4)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_79(0xA)
    OP_71(0xA, 0x172, 0x19A, 0x3E8, 0x20)
    CancelBlur(500)
    Sleep(1000)
    Return()

    # Function_49_6F8E end

    def Function_50_7079(): pass

    label("Function_50_7079")

    Sound(921, 0, 100, 0)
    Sound(922, 0, 50, 0)
    Sound(977, 0, 80, 0)
    Sound(832, 2, 100, 0)
    Sleep(700)
    Sound(922, 0, 40, 0)
    Sound(977, 0, 60, 0)
    Sleep(800)
    Sound(936, 0, 80, 0)
    Sleep(1000)
    Sound(936, 0, 80, 0)
    StopSound(832, 1000, 100)
    Return()

    # Function_50_7079 end

    def Function_51_70B9(): pass

    label("Function_51_70B9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_713B")
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70E9")
    OP_82(0x0, 0xF, 0xBB8, 0x1F4)
    Jump("loc_7133")

    label("loc_70E9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_710E")
    OP_82(0x4B, 0x96, 0x1388, 0x1F4)
    Jump("loc_7133")

    label("loc_710E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7133")
    OP_82(0x19, 0x32, 0x1388, 0x1F4)
    Jump("loc_7133")

    label("loc_7133")

    Sleep(500)
    Jump("Function_51_70B9")

    label("loc_713B")

    Return()

    # Function_51_70B9 end

    def Function_52_713C(): pass

    label("Function_52_713C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch03700.itc", 0x1F)
    LoadChrToIndex("apl/ch51545.itc", 0x20)
    LoadChrToIndex("chr/ch03300.itc", 0x21)
    LoadChrToIndex("chr/ch03400.itc", 0x22)
    LoadChrToIndex("chr/ch02100.itc", 0x23)
    LoadChrToIndex("chr/ch13400.itc", 0x24)
    LoadChrToIndex("chr/ch03600.itc", 0x25)
    LoadChrToIndex("chr/ch03500.itc", 0x26)
    LoadChrToIndex("apl/ch51532.itc", 0x27)
    LoadEffect(0x0, "event/ev500_00.eff")
    SoundLoad(852)
    SoundLoad(3978)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -1500, 0, -2000, 270)
    OP_8E(0xC, "迪塔总统")
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -600, 0, -6300, 270)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x2)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 0, 300, -4900, 270)
    OP_52(0x10, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x10, 1, 0, 0)
    PlayEffect(0x0, 0x0, 0x10, 0x1, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -3700, 0, -700, 270)
    SetChrChipByIndex(0xE, 0x22)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -4100, 0, 400, 270)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -1900, 0, -200, 270)
    OP_52(0xD, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x13, 0x24)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4000, 0, -4300, 270)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5000, 0, -3300, 270)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -5500, 0, -5000, 270)
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    OP_68(-7500, 2200, -4000, 0)
    MoveCamera(40, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14500, 0)
    Sound(852, 2, 100, 0)
    OP_68(-2800, 1200, -3040, 3000)
    SetCameraDistance(13500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0141
    ChrTalk(
        0xE,
        "#04612F#3978V#5S#11P#13A呀哈！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0142
    ChrTalk(
        0xF,
        "#11P#01611F……那、那是什么……\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x14,
        (
            "#12P#04809F啊哈哈，实在是太厉害了！\x02\x03",

            "#04802F『零之至宝』……\x01",
            "真是名副其实啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x13,
        (
            "#12P#04702F哼哼，竟能同时操纵三架\x01",
            "最终型的极限级智能兵器……！\x02\x03",

            "而且还能使其成为『奇迹』的代行者，\x01",
            "展开自律行动……！\x02\x03",

            "#04709F哈哈，看来可以向那位大人\x01",
            "提交一份精彩的报告了！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x12,
        "#12P#04900F#3C#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xD,
        (
            "#11P#04504F哼……\x01",
            "的确很厉害。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x11,
        (
            "#12P#10811F呵呵，在初期阶段，\x01",
            "基本也就是这样啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#12312F#40W………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x320)

    #C0149
    ChrTalk(
        0xC,
        (
            "#11P#11309F呵呵呵……\x01",
            "#4S哈哈哈哈哈哈哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-1650, 1200, -2100, 1500)
    MoveCamera(90, 21, 0, 1500)
    SetCameraDistance(13000, 1500)
    OP_6F(0x79)
    SetCameraDistance(12000, 10000)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    Sleep(110)
    Sound(812, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0150
    ChrTalk(
        0xC,
        (
            "#11304F#30W从这一刻起，\x01",
            "克洛斯贝尔正式成为『圣地』！\x02\x03",

            "#11302F也就是击退帝国与共和国，\x01",
            "为整个大陆带来新秩序的\x01",
            "根据地……！\x02\x03",

            "以及将我们库罗伊斯家族的理想与正义\x01",
            "弘扬至全世界的中心……！\x02",
        )
    )

    CloseMessageWindow()
    OP_6F(0x79)
    SetCameraDistance(23000, 5000)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0xBB8)

    #C0151
    ChrTalk(
        0xC,
        "#11309F#5S#40W#30A哈哈哈哈哈哈哈！\x02",
    )
    #Auto

    Sleep(2000)
    StopSound(132, 2000, 100)
    StopSound(852, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0x1770)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 3)
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_52_713C end

    def Function_53_794F(): pass

    label("Function_53_794F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch13400.itc", 0x1F)
    LoadChrToIndex("chr/ch03600.itc", 0x20)
    LoadChrToIndex("chr/ch04200.itc", 0x21)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 12300, -33620, 23500, 0)
    OP_52(0x10, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 6900, 0, -14700, 135)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 5700, 0, -15500, 135)
    SetChrChipByIndex(0x12, 0x21)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 7500, 0, -16200, 135)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 0, 180)
    OP_D5(0x28, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x406)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "open")
    OP_70(0x1, 0x12D)
    OP_70(0x2, 0x12D)
    OP_70(0x3, 0x12D)
    OP_70(0x4, 0x12D)
    OP_68(0, 6500, 0, 0)
    MoveCamera(147, -3, 0, 0)
    OP_6E(750, 0)
    SetCameraDistance(16500, 0)
    OP_F0(0x0, 0x1)
    OP_68(0, 3500, 0, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(6800, 1200, -16300, 4000)
    MoveCamera(90, 13, 0, 4000)
    SetCameraDistance(12500, 4000)
    OP_6F(0x79)
    SetCameraDistance(11500, 30000)
    Sleep(300)

    #C0152
    ChrTalk(
        0x14,
        (
            "#6P#04804F好了，『幻焰计划』的舞台\x01",
            "已经转移至帝国……\x02\x03",

            "#04802F接下来，你准备按照原定计划，\x01",
            "暂时静观其变吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x12,
        (
            "#04923F嗯，是的。\x02\x03",

            "#04921F在帝国那边的行动进展到下一阶段之前，\x01",
            "我就再陪他们一阵吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x13,
        (
            "#04704F#5P呵呵，『零之至宝』如今的力量\x01",
            "已经可以与消失的『幻之至宝』相匹敌。\x02\x03",

            "而且还逐渐展现出了\x01",
            "原版并不具备的潜在能力……\x02\x03",

            "#04702F哼哼，究竟能进化到什么地步呢？\x01",
            "就让我好好见识下库罗伊斯家族的本事吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x14, 0x13, 500)
    Sleep(100)

    #C0155
    ChrTalk(
        0x14,
        (
            "#12P#04809F呵呵……\x01",
            "博士，你可真是兴致勃勃。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x14, 0x87, 0x1F4)

    #C0156
    ChrTalk(
        0x14,
        (
            "#6P#04805F说起来，『他们』\x01",
            "终于开始行动了？\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x12,
        (
            "#04924F这反倒是个好机会。\x02\x03",

            "#04922F为了今后，也应该彻底明确\x01",
            "他们与我们的立场差别。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x13,
        (
            "#04700F#5P呵呵，那些事情就交给你们啦。\x02\x03",

            "#04704F我就在这里继续收集\x01",
            "『零之至宝』的数据……\x02\x03",

            "#04702F确认联系人与神的\x01",
            "终极媒介是否存在！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(6800, -800, -16300, 3000)
    StopSound(132, 2000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x1)
    OP_68(12300, -32820, 23400, 0)
    MoveCamera(150, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(35000, 0)
    SetCameraDistance(15000, 9000)
    Sound(132, 2, 50, 0)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopSound(132, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("e4020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_794F end

    def Function_54_8040(): pass

    label("Function_54_8040")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch11600.itc", 0x1E)
    LoadChrToIndex("chr/ch04200.itc", 0x1F)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x103, 0x8)
    SetChrFlags(0x104, 0x8)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, 17450, 0, -5600, 225)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, 16250, 0, -8350, 45)
    OP_68(17260, 1000, -7120, 0)
    MoveCamera(68, 17, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(12000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_8136")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8149")
    Sleep(1)
    Jump("loc_8136")

    label("loc_8149")

    FadeToDark(1000, 0, -1)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_54_8040 end

    def Function_55_8157(): pass

    label("Function_55_8157")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu12300.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    LoadChrToIndex("chr/ch11600.itc", 0x1F)
    LoadEffect(0x0, "event\\ev500_00.eff")
    SoundLoad(3634)
    SoundLoad(3635)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -22000, -4400, -22000, 225)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -27500, -4400, -32600, 150)
    PlayEffect(0x0, 0xFF, 0x10, 0x0, 0, 750, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xAF, 0x9B, 0x12C, 0x384, 0x0)
    SetMapObjFrame(0xFF, "sky00", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x0, 0x1)
    OP_68(-22300, -3300, -44000, 0)
    MoveCamera(195, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(28000, 0)
    OP_68(-27500, -3300, -32600, 7000)
    SetCameraDistance(14000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0159
    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30W………………………………\x07\x00\x02",
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
    ClearChrFlags(0x11, 0x80)

    #N0160
    NpcTalk(
        0x11,
        "玛丽亚贝尔的声音",
        (
            "呵呵……\x01",
            "被他们将了一军呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(-24000, -3300, -24000, 0)
    MoveCamera(180, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    OP_68(-27350, -3300, -31200, 5000)
    MoveCamera(150, 17, 0, 5000)
    SetCameraDistance(13500, 5000)

    def lambda_8464():
        OP_95(0xFE, -26500, -4400, -26500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8464)
    WaitChrThread(0x11, 1)

    def lambda_8482():
        OP_95(0xFE, -27000, -4400, -29500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8482)
    WaitChrThread(0x11, 1)
    TurnDirection(0x10, 0x11, 400)
    OP_6F(0x79)
    SetCameraDistance(11500, 50000)
    Sleep(150)

    #C0161
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12300F贝尔……\x02\x03",

            "#12308F迪塔好像在找你，\x01",
            "不用过去吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0162
    AnonymousTalk(
        0x11,
        (
            "呵呵，就让父亲\x01",
            "再着急一阵子吧。\x02\x03",

            "没有『钟』的共鸣，\x01",
            "很难张开『结界』吧？\x02",
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

    #C0163
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12303F#30W……嗯，目前来看，是这样的。\x02\x03",

            "#12308F虽然那些神机还可以行动，\x01",
            "但却不能使用『空』之力……\x02\x03",

            "#12315F罗伊德他们……要来了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x11,
        (
            "#6P#02913F呵呵，真伤脑筋啊。\x02\x03",

            "这样一来，就不得不\x01",
            "按照计划行动了。\x02\x03",

            "#02911F按照『他』的计划。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12303F#30W………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x11,
        (
            "#6P#02902F一切都要看琪雅的决定……\x01",
            "我们会完全遵从于你。\x02\x03",

            "#02903F是在此放弃，\x01",
            "还是实现一切愿望。\x02\x03",

            "#02912F差不多也该做出选择了。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#40W…………嗯。\x02\x03",

            "#12302F从一开始，就没有别的路可以走，\x01",
            "琪雅懂的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x10, 0x73, 0x1F4)
    Sleep(300)
    OP_63(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)
    Sleep(800)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)

    #C0168
    ChrTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#11P#12304F#3634V#40W#59A为了罗伊德、艾莉、缇欧、兰迪，\x01",
            "还有滴和大家……\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(11000, 2000)
    StopSound(132, 2000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0169
    AnonymousTalk(
        0x10,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#3635V#40W#32A我一定会实现一切愿望。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopBGM(0x1770)
    WaitBGM()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("e302B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_8157 end

    def Function_56_88F6(): pass

    label("Function_56_88F6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "event/ev17031.eff")
    SoundLoad(980)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 0, 0)
    OP_93(0x28, 0xB4, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-570, 2100, -8640, 0)
    MoveCamera(144, 45, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(130610, 0)
    Sound(980, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_68(3650, 11100, 4520, 10000)
    MoveCamera(133, -7, 0, 10000)
    OP_6E(800, 10000)
    SetCameraDistance(54000, 10000)
    BeginChrThread(0x29, 0, 0, 57)
    OP_0D()
    Sleep(7000)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 200000, 45500, -200000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_6F(0x79)
    Sleep(1000)
    StopSound(980, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopEffect(0x0, 0x2)
    SetScenarioFlags(0x23, 2)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_56_88F6 end

    def Function_57_8A6A(): pass

    label("Function_57_8A6A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8AA8")
    Sleep(600)
    OP_98(0xFE, 0x0, 0xFFFFF8F8, 0x0, 0x258, 0x1)
    Sleep(600)
    OP_98(0xFE, 0x0, 0x708, 0x0, 0x258, 0x1)
    Jump("Function_57_8A6A")

    label("loc_8AA8")

    Return()

    # Function_57_8A6A end

    def Function_58_8AA9(): pass

    label("Function_58_8AA9")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_F3(200000)
    BlurSwitch(0x0, 0x55FFFFFF, 0x0, 0x1, 0x0)
    LoadEffect(0x0, "event/ev17031.eff")
    LoadEffect(0x7, "event/ev17022.eff")
    LoadEffect(0x8, "event/eva03_01.eff")
    SoundLoad(980)
    OP_A7(0x0, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x2, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x3, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x28, 0x80)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 0, 0)
    OP_93(0x28, 0xB4, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1194), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    OP_78(0x9, 0x29)
    OP_49()
    SetChrPos(0x29, -15000, 10200, 60080, 0)
    OP_93(0x29, 0xB4, 0x0)
    SetMapObjFlags(0x9, 0x1000)
    OP_74(0x9, 0x1E)
    OP_70(0x9, 0xDD)
    SetChrFlags(0x29, 0x1)
    OP_52(0x29, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x29, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r0 (66)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r1(67)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_r2(68)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l0(69)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l1(70)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    OP_87(0x7, 0xFF, 0x9, "Null_wing_l2(71)", 0x7, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1F4, 0x1F4, 0x1F4, 0x0)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x13, 0x2B)
    OP_49()
    SetChrPos(0x2B, 200000, 45000, -200000, 0)
    OP_93(0x2B, 0x13B, 0x0)
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    OP_74(0x13, 0x1E)
    OP_71(0x13, 0x1, 0x78, 0x0, 0x20)
    OP_FF(0x13, 0x96, 0x96, 0x96)
    OP_75(0x13, 0x1, 0x0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 200000, 45500, -200000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(980, 2, 20, 0)
    FadeToBright(1000, 0)
    OP_68(5000, 9900, 1500, 0)
    MoveCamera(154, 2, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(42350, 0)
    OP_68(5000, 9900, 1500, 5000)
    MoveCamera(136, 3, 0, 5000)
    OP_6E(800, 5000)
    SetCameraDistance(42350, 5000)
    OP_0D()
    Sleep(1500)
    OP_75(0x13, 0x2, 0x0)
    OP_93(0x29, 0xA1, 0x28)
    EndChrThread(0x29, 0x0)
    BeginChrThread(0x29, 0, 0, 60)
    BeginChrThread(0x29, 1, 0, 61)
    Sleep(500)
    Sound(499, 0, 100, 0)
    Sound(998, 0, 100, 0)
    Sleep(4000)
    OP_6F(0x79)
    OP_FF(0x13, 0x3E8, 0x3E8, 0x3E8)
    SetMapObjFlags(0x13, 0x4)
    PlayEffect(0x8, 0xFF, 0x29, 0x5, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x8, 0xFF, 0x29, 0x5, 0, 0, 0, 180, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(999, 0, 100, 0)
    OP_68(133720, 25300, -151690, 0)
    MoveCamera(323, 6, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(107240, 0)
    Fade(500)
    OP_0D()
    BlurSwitch(0x3E8, 0x77FFFFFF, 0x0, 0x1, 0xA)
    Sleep(1500)
    EndChrThread(0x29, 0x0)
    OP_6F(0x79)
    StopSound(980, 1000, 10)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 3)
    NewScene("e4310", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_58_8AA9 end

    def Function_59_8F41(): pass

    label("Function_59_8F41")

    ClearMapObjFlags(0x9, 0x20)
    OP_79(0x9)
    Sound(982, 0, 100, 0)
    Sound(905, 0, 100, 0)
    OP_71(0x9, 0xC9, 0xDC, 0x0, 0x0)
    Sleep(300)
    Sleep(1000)
    OP_79(0x9)
    OP_70(0x9, 0xDD)
    Return()

    # Function_59_8F41 end

    def Function_60_8F70(): pass

    label("Function_60_8F70")

    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0xFA0, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x1F40, 0x1)
    OP_9B(0x1, 0xFE, 0x0, 0x1F4, 0x2EE0, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 5500, 10200, 3080)
    OP_9F(0x1, 50000, 10200, -120000)
    OP_9F(0x1, 72000, 14200, -155000)
    OP_9F(0x1, 95000, 18200, -180000)
    OP_9F(0x1, 120000, 22200, -200000)
    OP_9F(0x1, 150000, 25200, -215000)
    OP_9F(0x1, 203000, 33200, -225000)
    OP_9F(0x2, 0xFE, 65000, 0x2)
    Return()

    # Function_60_8F70 end

    def Function_61_900D(): pass

    label("Function_61_900D")

    Sleep(2000)
    OP_74(0x9, 0x3)
    OP_71(0x9, 0x104, 0x103, 0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_61_900D end

    def Function_62_9024(): pass

    label("Function_62_9024")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 64)
    Call(0, 65)
    LoadEffect(0x0, "event/ev17050.eff")
    LoadEffect(0x1, "event/ev17051.eff")
    SoundLoad(943)
    SoundLoad(933)
    SoundLoad(927)
    SoundLoad(950)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu11300.itp")
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    OP_49()
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x42E)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xC, 0x3)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 180)
    OP_8E(0xC, "迪塔总统")
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x44C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, -600, 0, -20000, 0)
    SetChrPos(0x102, 600, 0, -20000, 0)
    SetChrPos(0x103, -1100, 0, -21100, 0)
    SetChrPos(0x104, 1100, 0, -21100, 0)
    SetChrPos(0xF4, -600, 0, -22200, 0)
    SetChrPos(0xF5, 600, 0, -22200, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(0, 1100, -20000, 0)
    MoveCamera(55, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(500, 0)
    OP_0D()

    #N0170
    NpcTalk(
        0xC,
        "男性的声音",
        (
            "……哎呀呀，\x01",
            "不速之客\x01",
            "竟然能到达这里。\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7356", 0)
    OP_68(0, 2500, -2000, 3000)
    MoveCamera(0, 9, 0, 3000)
    SetCameraDistance(13000, 3000)
    OP_6F(0x79)
    Sleep(500)

    #C0171
    ChrTalk(
        0x102,
        "#2P#00107F#N……迪塔叔叔……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0172
    ChrTalk(
        0x101,
        "#1P#00007F#N迪塔先生……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1300, -5000, 0)
    MoveCamera(34, 11, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, -500, 0, -15500, 0)
    SetChrPos(0x102, 500, 0, -15500, 0)
    SetChrPos(0x103, -1000, 0, -17000, 0)
    SetChrPos(0x104, 1000, 0, -17000, 0)
    SetChrPos(0xF4, 0, 0, -16700, 0)
    SetChrPos(0xF5, 0, 0, -17700, 0)
    SetCameraDistance(18000, 2000)

    def lambda_940E():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_940E)
    Sleep(50)

    def lambda_942B():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFDECC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_942B)
    Sleep(50)

    def lambda_9448():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFDA1C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_9448)
    Sleep(50)

    def lambda_9465():
        OP_96(0xFE, 0xFFFFF95C, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9465)

    def lambda_947F():
        OP_96(0xFE, 0x6A4, 0x0, 0xFFFFD8F0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_947F)

    def lambda_9499():
        OP_96(0xFE, 0x0, 0x0, 0xFFFFD5D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 1, lambda_9499)
    WaitChrThread(0xF5, 1)
    OP_6F(0x79)
    SetCameraDistance(17000, 30000)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0173
    AnonymousTalk(
        0xC,
        (
            "呵呵……\x01",
            "久违了，诸位。\x02\x03",

            "不过，我好像并没有\x01",
            "约你们过来共进午餐……\x02\x03",

            "莫非是你们\x01",
            "搞错日期了？\x02",
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

    #C0174
    ChrTalk(
        0x101,
        (
            "#00003F#12P未经预约便来拜访，\x01",
            "实在抱歉。\x02\x03",

            "#00001F但我们也有\x01",
            "无法退让的要求。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x103,
        (
            "#12P#N#00206F例如取消独立决定、\x01",
            "撤收市内的魔导兵等，\x01",
            "实在是一言难尽……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0176
    ChrTalk(
        0x104,
        (
            "#00307F#12P但首先，还是请你\x01",
            "立刻把阿琪还给我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xC,
        "#5P#11304F嗯，没问题啊。\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0178
    ChrTalk(
        0x101,
        "#00011F#12P什么……\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xC,
        (
            "#5P#11300F呵呵，你们似乎\x01",
            "存在着一些误会。\x02\x03",

            "我们并没有强行逼迫\x01",
            "琪雅提供协助。\x02\x03",

            "#11303F克洛斯贝尔面临着\x01",
            "巨大的困难……\x02\x03",

            "#11301F琪雅为了解决这些困难，\x01",
            "才会主动协助我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x103,
        "#12P#N#00208F这……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0181
    ChrTalk(
        0x102,
        (
            "#00106F#12P但这种局面正是\x01",
            "迪塔叔叔一手造成的吧？\x02\x03",

            "#00108F在幕后操纵猎兵团，\x01",
            "指示他们袭击克洛斯贝尔市，\x01",
            "从而煽动市民们支持独立的情绪……\x02\x03",

            "#00101F通过冻结帝国和共和国的资产，成功导演了\x01",
            "这场令自治州面临存亡危机的大戏……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9937")

    #C0182
    ChrTalk(
        0x10A,
        (
            "#00606F#12P#N……真伪暂且不论，\x01",
            "这种行为真是不可饶恕啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99CC")

    label("loc_9937")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_997E")

    #C0183
    ChrTalk(
        0x105,
        (
            "#10404F#12P#N嗯，这简直是\x01",
            "自导自演的极致了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_99CC")

    label("loc_997E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_99CC")

    #C0184
    ChrTalk(
        0x109,
        (
            "#10106F#12P#N……暂且不论真伪，\x01",
            "这种行为实在是不可饶恕。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_99CC")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A31")

    #C0185
    ChrTalk(
        0x106,
        (
            "#10708F#12P#N之后，您就将这种\x01",
            "烂摊子推到琪雅的面前，\x01",
            "迫使她作出抉择……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AF0")

    label("loc_9A31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A93")

    #C0186
    ChrTalk(
        0x109,
        (
            "#10108F#12P#N之后，您就把这种\x01",
            "烂摊子推到琪雅的面前，\x01",
            "逼迫她作出抉择……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9AF0")

    label("loc_9A93")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AF0")

    #C0187
    ChrTalk(
        0x105,
        (
            "#10408F#12P#N之后，您就把这种\x01",
            "烂摊子推到琪雅的面前，\x01",
            "迫使她作出抉择……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9AF0")

    OP_57(0x0)
    OP_5A()

    #C0188
    ChrTalk(
        0x104,
        (
            "#00301F#12P身为一个以爽朗笑容而著称的魅力中年，\x01",
            "这种做法未免也太卑劣了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00006F#12P迪塔总统……\x01",
            "不，还是称呼您\x01",
            "迪塔先生吧。\x02\x03",

            "#00013F这就是您的『正义』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xC,
        "#5P#11304F嗯，正是。\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(0, 1200, 10, 0)
    MoveCamera(57, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    MoveCamera(37, 11, 0, 50000)
    SetCameraDistance(19000, 50000)
    OP_0D()
    Sleep(150)

    #C0191
    ChrTalk(
        0xC,
        (
            "#5P#11303F现实中的政治\x01",
            "并没有那么美好。\x02\x03",

            "像那种程度的政治策略，\x01",
            "已经算是手下留情了。\x02\x03",

            "#11301F在十二年前，帝国侵略\x01",
            "利贝尔时所引发的悲剧，\x01",
            "你们可曾知道？\x02\x03",

            "还有共和国在民主化时期\x01",
            "断然实行的血腥肃清行动……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x101,
        "#00007F#12P#N即、即使如此……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0193
    ChrTalk(
        0x102,
        (
            "#00108F#12P#N仅凭这些说辞，难道就能将\x01",
            "迪塔叔叔的所作所为正当化吗……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0194
    ChrTalk(
        0xC,
        (
            "#11304F正当化并不需要凭借什么，\x01",
            "而是要用力量与意志来实现。\x02\x03",

            "#11300F我虽然是库罗伊斯家族的当家，\x01",
            "但对家族的使命\x01",
            "并不是很热衷。\x02\x03",

            "说起那方面的事务，\x01",
            "倒是我女儿更加熟悉。\x02\x03",

            "#11303F然而，当我得知始祖们\x01",
            "梦寐以求的全新『至宝』\x01",
            "真的有可能诞生之时……\x02\x03",

            "我狂喜不已，无比感谢女神\x01",
            "让我诞生在库罗伊斯家族。\x02\x03",

            "#11302F因为我终于可以获得\x01",
            "平定这动荡的时代，\x01",
            "伸张『正义』的力量了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        "#00205F#12P#N『正义』……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0196
    ChrTalk(
        0x101,
        (
            "#00011F#12P#N如此说来，您这一系列的所作所为……\x02\x03",

            "#00006F并不是为了一己私利，\x01",
            "也不是为了满足统治欲望……\x02\x03",

            "#00010F而是为了实现\x01",
            "『正义』……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0197
    ChrTalk(
        0xC,
        (
            "#11309F哈哈，除此之外，\x01",
            "你觉得还会有什么理由？\x02\x03",

            "#11300F十年前，当ＩＢＣ的资产额\x01",
            "达到大陆第一的时候，\x01",
            "我就已经没有继续追求财富的必要了。\x02\x03",

            "至于统治整个大陆这种过时的幻想，\x01",
            "我也没有丝毫兴趣。\x02\x03",

            "#11306F我只是无法忍受而已。\x02\x03",

            "无法忍受这个被名为『国家』的框架所束缚，\x01",
            "不断重复着无谓纷争的世界。\x02\x03",

            "#11303F从这种意义上说，\x01",
            "我并不拘泥于『独立国』这种形式。\x02\x03",

            "就算遵照麦克道尔议长的观点，\x01",
            "宣布它不具备合法性也无妨。\x02\x03",

            "#11301F只要我理想中的『正义』\x01",
            "能遍及整个世界……\x02\x03",

            "#11302F并在『正义』的基础上保守秩序，\x01",
            "构筑起一个和平的世界就够了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A243")

    #C0198
    ChrTalk(
        0x10A,
        "#00610F#12P#N……太荒唐了。\x02",
    )

    CloseMessageWindow()

    label("loc_A243")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A274")

    #C0199
    ChrTalk(
        0x105,
        "#10401F#12P#N认真的吗……？\x02",
    )

    CloseMessageWindow()

    label("loc_A274")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2B4")

    #C0200
    ChrTalk(
        0x109,
        (
            "#10106F#12P#N虽、虽然不是\x01",
            "完全无法赞同……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2B4")

    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2F9")

    #C0201
    ChrTalk(
        0x106,
        (
            "#10706F#12P#N……在我听来，\x01",
            "不过是痴人说梦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2F9")

    OP_57(0x0)
    OP_5A()

    #C0202
    ChrTalk(
        0x104,
        (
            "#00306F#12P#N怎么说呢……没想到\x01",
            "他竟然如此执著。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0203
    ChrTalk(
        0x103,
        (
            "#00208F#12P#N……但是，从某种程度上说，\x01",
            "他对『正义』的幻想的确可以实现……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0204
    ChrTalk(
        0x102,
        (
            "#00106F#12P#N是啊，只要拥有琪雅\x01",
            "这个『零之至宝』……\x02\x03",

            "#00108F……这可是现存的政治思想中所没有的，\x01",
            "称得上是犯规的决定性砝码啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0205
    ChrTalk(
        0x101,
        "#00008F#12P#N#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, -5000, 0)
    MoveCamera(147, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetMapObjFlags(0x5, 0x4)
    SetChrPos(0xF4, 500, 0, -9700, 0)
    SetChrPos(0xF5, -500, 0, -10700, 0)
    MoveCamera(151, 13, 0, 30000)
    SetCameraDistance(19000, 30000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0206
    ChrTalk(
        0x101,
        (
            "#00006F#11P迪塔先生。\x02\x03",

            "我……曾经从您的想法中\x01",
            "获益匪浅。\x02\x03",

            "#00001F然而，我对您的『正义』……\x01",
            "似乎有些高估了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0207
    ChrTalk(
        0xC,
        "#6P#11301F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#00008F我们是警察，\x01",
            "而且隶属于特别任务支援科。\x02\x03",

            "#00003F我们会遵循法律这条规则，\x01",
            "通过亲近市民来体现『正义』。\x02\x03",

            "#00001F不过……\x01",
            "这未必就是正确的做法，\x01",
            "我们也会时常感到迷茫。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A69C")

    #C0209
    ChrTalk(
        0x10A,
        (
            "#11P#00603F……当然。\x01",
            "在治安维持和安全保障等方面，\x01",
            "并没有绝对意义上的正确答案。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A69C")


    #C0210
    ChrTalk(
        0x102,
        (
            "#11P#00106F……是啊。\x01",
            "由于立场的不同，\x01",
            "『正义』的标准也会有所改变……\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x103,
        (
            "#11P#00204F就算心怀迷茫，不时遭遇失败，\x01",
            "也依然要追求『正义』……\x02\x03",

            "#00202F这正是迪塔先生\x01",
            "曾经说过的话啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x104,
        (
            "#5P#00302F怎么说呢……您的实际行为似乎和\x01",
            "在那场演讲中发表的观点全然不同啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xC,
        (
            "#6P#11303F……那只是在力量与意志\x01",
            "有所不足的情况下\x01",
            "谈到的方法论而已。\x02\x03",

            "如果在两者都已具备的情况下，\x01",
            "却仍然不行使『正义』……\x02\x03",

            "#11301F岂不就是『惰怠』了吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0214
    ChrTalk(
        0x101,
        "#00013F#4S#11P不对！\x02",
    )

    CloseMessageWindow()

    def lambda_A879():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFE2B4, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A879)
    WaitChrThread(0x101, 1)
    Sleep(150)

    #C0215
    ChrTalk(
        0x101,
        (
            "#00003F#11P『正义』是不断变化，\x01",
            "没有定形的东西……！\x02\x03",

            "对大家来说，只有不断追寻『正义』，\x01",
            "才能体现出它的价值……！\x02\x03",

            "#00007F而您的做法，只是将\x01",
            "『正义』统一成固定样式，\x01",
            "并强迫所有人接受而已……！\x02\x03",

            "这种东西，真的是您\x01",
            "所追求的『正义』吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xC,
        (
            "#6P#11310F唔……\x02\x03",

            "#11307F如今，我已经打破了\x01",
            "克洛斯贝尔的政治僵局，\x01",
            "并且完成了数项改革！\x02\x03",

            "你是要否定这些成果吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x102,
        (
            "#11P#00106F……这两件事不能混为一谈。\x02\x03",

            "#00108F我们并没有否定\x01",
            "迪塔叔叔的所有行为，\x01",
            "而且也确实从您身上学到了很多东西。\x02\x03",

            "#00101F正因如此……我们才必须要\x01",
            "指出您的欺瞒与误解。\x02\x03",

            "#00107F作为一直都尊敬着您的人……\x01",
            "无论如何也希望您能认识到自己的错误！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0218
    ChrTalk(
        0xC,
        "#6P#11302F#4S好吧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 1100, 2000, 0)
    MoveCamera(0, 9, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    ClearMapObjFlags(0x5, 0x4)
    SetChrPos(0xF4, -500, 0, -9700, 0)
    SetChrPos(0xF5, 500, 0, -10700, 0)
    OP_0D()
    Sleep(150)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(70)
    SetChrSubChip(0xC, 0x2)
    OP_68(0, 1100, -4000, 1500)
    MoveCamera(0, 21, 0, 1500)
    SetCameraDistance(27000, 1500)
    OP_6F(0x79)
    Fade(500)
    BeginChrThread(0x32, 1, 0, 66)
    SetMapObjFrame(0xFF, "futa03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "move")
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_AC7A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AC7A)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_AC9F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AC9F)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0219
    ChrTalk(
        0x101,
        "#6P#00005F……！？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x104,
        "#00307F#6P#N什、什么！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(10, 1300, 0, 0)
    MoveCamera(0, 25, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    OP_93(0x103, 0x0, 0x0)
    OP_93(0x104, 0x0, 0x0)
    MoveCamera(45, 13, 0, 10000)
    SetCameraDistance(13500, 10000)
    OP_0D()
    SetMessageWindowPos(250, 250, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADB6")

    #A0221
    AnonymousTalk(
        0x105,
        (
            "#10407F这是……\x01",
            "『魔导』的力量……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE2F")

    label("loc_ADB6")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADF7")

    #A0222
    AnonymousTalk(
        0x106,
        (
            "#10707F这是……\x01",
            "『魔导』的力量……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AE2F")

    label("loc_ADF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE2F")

    #A0223
    AnonymousTalk(
        0x109,
        (
            "#10107F导力魔法……\x01",
            "不，好像不是！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AE2F")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(0, 250, -1, -1)

    #A0224
    AnonymousTalk(
        0x103,
        (
            "#00201F大家小心！\x02\x03",

            "从兰花塔中传来的\x01",
            "巨大灵力开始以他\x01",
            "为中心汇聚了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)

    #C0225
    ChrTalk(
        0xC,
        (
            "#11304F呵呵，虽然不及贝尔，\x01",
            "但身为库罗伊斯家族的当家，\x01",
            "这种程度的小伎俩还是略通一二的……\x02\x03",

            "#11300F只要再利用这兰花塔的\x01",
            "『灵子变换功能』……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0226
    ChrTalk(
        0xC,
        "#11307F#4S#38A就可以做到这种事！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_6F(0x79)
    Sound(950, 2, 40, 0)
    Sound(935, 0, 100, 0)
    PlayEffect(0x1, 0x1, 0xC, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_AFAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_AFAC)
    StopEffect(0x0, 0x2)
    WaitChrThread(0xC, 2)
    OP_68(0, 4000, 5000, 3000)
    SetChrFlags(0xC, 0x20)

    def lambda_AFDA():
        OP_96(0xFE, 0x0, 0xFA0, 0x157C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_AFDA)
    WaitChrThread(0xC, 1)
    StopEffect(0x1, 0x2)
    Sound(930, 0, 100, 0)
    StopSound(933, 1000, 100)
    StopSound(950, 1000, 40)
    OP_6F(0x79)
    Sleep(1500)
    StopSound(927, 1000, 100)

    #C0227
    ChrTalk(
        0x102,
        "#00105F啊……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B060")

    #C0228
    ChrTalk(
        0x10A,
        "#00605F竟然被吸收进去了……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0CB")

    label("loc_B060")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B09A")

    #C0229
    ChrTalk(
        0x109,
        "#10111F被、被吸收进去了……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_B0CB")

    label("loc_B09A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B0CB")

    #C0230
    ChrTalk(
        0x106,
        "#10712F被吸收进去了……！？\x02",
    )

    CloseMessageWindow()

    label("loc_B0CB")

    OP_68(0, 4000, 5000, 6000)
    MoveCamera(0, -5, 0, 6000)
    SetCameraDistance(12500, 6000)
    Sound(140, 0, 100, 0)
    Sound(859, 0, 50, 0)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Sleep(1000)
    BeginChrThread(0x28, 3, 0, 63)
    Sleep(2000)
    OP_6F(0x79)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("男性的声音")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W嗯……视野与控制感都很好。\x02",
        )
    )

    CloseMessageWindow()

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W看来可以在接受『至宝』力量的\x01",
            "同时进行人工操纵。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitChrThread(0x28, 3)
    StopBGM(0xBB8)
    OP_68(0, 2500, -7500, 2500)
    MoveCamera(0, 5, 0, 2500)
    SetCameraDistance(11000, 2500)
    Sleep(2000)

    def lambda_B1D6():
        OP_97(0x101, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B1D6)
    Sleep(50)

    def lambda_B1F3():
        OP_97(0x102, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B1F3)
    Sleep(50)

    def lambda_B210():
        OP_97(0x103, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B210)
    Sleep(50)

    def lambda_B22D():
        OP_97(0x104, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B22D)
    Sleep(50)

    def lambda_B24A():
        OP_97(0xF4, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B24A)
    Sleep(50)

    def lambda_B267():
        OP_97(0xF5, 0x0, 0x0, 0x7D0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B267)
    OP_6F(0x79)
    WaitChrThread(0xF5, 0)
    Sleep(300)

    #C0233
    ChrTalk(
        0x102,
        "#00107F#12P#N迪、迪塔叔叔……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #N0234
    NpcTalk(
        0x101,
        "缇欧",
        (
            "#00207F#6P#N在灵子性质的相位空间\x01",
            "操控智能兵器……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0235
    ChrTalk(
        0x104,
        "#00310F#12P#N喂喂，竟然还能这样！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7554", 0)
    Fade(250)
    OP_68(0, 4000, 5000, 0)
    MoveCamera(0, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 0, 0, -6700, 0)
    SetChrPos(0xF5, 0, 0, -7800, 0)
    SetCameraDistance(14500, 1000)
    OP_0D()
    OP_71(0x5, 0x492, 0x4BA, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x4BA, 0x4CE, 0x0, 0x20)
    Sound(951, 0, 100, 0)
    Sleep(100)
    Sound(833, 0, 100, 0)
    Sound(859, 0, 100, 0)
    OP_6F(0x79)
    OP_68(0, 2000, -1000, 12000)
    MoveCamera(35, 5, 0, 12000)
    SetCameraDistance(17000, 12000)
    Sleep(1000)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("迪塔的声音")

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#80A哈哈，这正是展现『正义』，\x01",
            "惩戒世间的白色机体……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4CE, 0x4E2, 0x0, 0x0)
    OP_79(0x5)
    Sound(951, 0, 100, 0)
    OP_71(0x5, 0x335, 0x348, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x349, 0x352, 0x0, 0x20)
    Sound(833, 0, 100, 0)
    Sleep(800)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("迪塔的声音")

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#36A来吧，\x01",
            "就让我们来『证明』一下。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 100, -1, -1)
    SetChrName("迪塔的声音")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#80A我的『正义』和你们的『正义』……\x01",
            "究竟谁是谁非！\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B5C1")
    Sound(540, 0, 50, 0)

    label("loc_B5C1")

    OP_0D()
    Sleep(300)

    #C0239
    ChrTalk(
        0x101,
        "#00010F#12P#N啧……求之不得！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0240
    ChrTalk(
        0x102,
        (
            "#00107F#12P#N我们会尽全力\x01",
            "挑战的……！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x3B6)
    OP_24(0x39F)
    OP_24(0x3A5)
    OP_24(0x3AF)
    Battle("BattleInfo_7B4", 0x30200011, 0x0, 0x100, 0x11, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 67)
    Return()

    # Function_62_9024 end

    def Function_63_B645(): pass

    label("Function_63_B645")

    OP_71(0x5, 0x442, 0x492, 0x0, 0x0)
    Sleep(200)
    Sound(905, 0, 100, 0)
    Sleep(1000)
    Sound(905, 0, 100, 0)
    OP_79(0x5)
    OP_71(0x5, 0x406, 0x42E, 0x0, 0x20)
    Return()

    # Function_63_B645 end

    def Function_64_B673(): pass

    label("Function_64_B673")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B68B")
    LoadChrToIndex("chr/ch03150.itc", 0x23)

    label("loc_B68B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6A3")
    LoadChrToIndex("chr/ch03250.itc", 0x23)

    label("loc_B6A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6BB")
    LoadChrToIndex("chr/ch02950.itc", 0x23)

    label("loc_B6BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6D3")
    LoadChrToIndex("chr/ch00950.itc", 0x23)

    label("loc_B6D3")

    Return()

    # Function_64_B673 end

    def Function_65_B6D4(): pass

    label("Function_65_B6D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6EC")
    LoadChrToIndex("chr/ch03150.itc", 0x24)

    label("loc_B6EC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B704")
    LoadChrToIndex("chr/ch03250.itc", 0x24)

    label("loc_B704")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B71C")
    LoadChrToIndex("chr/ch02950.itc", 0x24)

    label("loc_B71C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B734")
    LoadChrToIndex("chr/ch00950.itc", 0x24)

    label("loc_B734")

    Return()

    # Function_65_B6D4 end

    def Function_66_B735(): pass

    label("Function_66_B735")

    Sound(922, 0, 100, 0)
    Sound(927, 2, 100, 0)
    Sound(933, 2, 100, 0)
    Sound(943, 2, 100, 0)
    Sleep(1000)
    OP_24(0x3AF)
    Sound(143, 0, 50, 0)
    Return()

    # Function_66_B735 end

    def Function_67_B75A(): pass

    label("Function_67_B75A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51769.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00350.itc", 0x22)
    Call(0, 64)
    Call(0, 65)
    LoadEffect(0x0, "event/ev17052.eff")
    LoadEffect(0x1, "event/ev17051.eff")
    SoundLoad(933)
    SoundLoad(927)
    SoundLoad(943)
    SoundLoad(950)
    SoundLoad(579)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0xC, 0x2)
    SetChrFlags(0xC, 0x20)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x5)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 2000, 5500, 180)
    OP_8E(0xC, "迪塔总统")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x22)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0xF4, 0x23)
    SetChrSubChip(0xF4, 0x0)
    SetChrChipByIndex(0xF5, 0x24)
    SetChrSubChip(0xF5, 0x0)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 0, 0, -6700, 0)
    SetChrPos(0xF5, 0, 0, -7800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x3A2)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x18, 0x1000)
    SetMapObjFrame(0xFF, "futa03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "open")
    OP_68(0, 3500, -1000, 0)
    MoveCamera(35, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    BeginChrThread(0x32, 1, 0, 69)
    OP_68(0, 1500, -1000, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0241
    ChrTalk(
        0x101,
        "#00000F#12P成、成功了吗……！\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x104,
        "#00300F#12P总算是……！\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7554", 0)
    PlayEffect(0x0, 0x0, 0xFF, 0x0, 0, 0, 6500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(930, 0, 80, 0)
    Sound(933, 2, 100, 0)
    Sound(927, 2, 100, 0)
    EndChrThread(0x32, 0x1)
    Sleep(1000)
    SetMapObjFlags(0x18, 0x4)
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

    #C0243
    ChrTalk(
        0x103,
        (
            "#00207F#12P灵子能源正在\x01",
            "再次填充！\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x102,
        "#00110F#12P怎么会……！\x02",
    )

    CloseMessageWindow()
    OP_68(0, 2000, -1000, 2000)
    Sound(905, 0, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x3A3, 0x3CA, 0x0, 0x0)
    Sleep(2000)
    Sound(902, 0, 70, 0)
    OP_79(0x5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x20)
    Sound(951, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("迪塔的声音")

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W呵呵，『零之至宝』\x01",
            "会赐给这架机体无限的力量。\x02",
        )
    )

    CloseMessageWindow()

    #A0246
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W只要没受到致命性的损伤，\x01",
            "它是不可能败北的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0247
    ChrTalk(
        0x101,
        "#00010F#12P#N呜……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC46")

    #C0248
    ChrTalk(
        0x10A,
        "#00610F#12P#N原来是这样……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BC46")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC7E")

    #C0249
    ChrTalk(
        0x105,
        "#10410F#12P#N这也太犯规了吧……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BC7E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCBC")

    #C0250
    ChrTalk(
        0x109,
        "#10110F#12P#N呜……必须要想个办法……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BCBC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BD02")

    #C0251
    ChrTalk(
        0x106,
        "#10708F#12P#N（……一定要努力找寻胜机……！）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_BD02")

    Sleep(500)
    Sound(955, 0, 100, 0)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("迪塔的声音")

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W呵呵，我丝毫没有打算\x01",
            "取你们的性命。\x02",
        )
    )

    CloseMessageWindow()

    #A0253
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W只要你们乖乖投降，\x01",
            "并协助我成就理想……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    Sound(954, 0, 100, 0)
    Sound(922, 0, 100, 0)
    StopSound(933, 1000, 100)
    StopSound(927, 1000, 100)
    Fade(250)
    ClearMapObjFlags(0x5, 0x20)
    OP_70(0x5, 0xB)
    OP_0D()
    StopEffect(0x0, 0x2)
    Sleep(1500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(10, 70, -1, -1)
    SetChrName("迪塔的声音")

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S！？\x02",
        )
    )

    CloseMessageWindow()
    Sound(955, 0, 100, 0)

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "什、什么……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    OP_70(0x14, 0xB)
    Fade(1000)
    SetMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    Sleep(1500)

    #C0256
    ChrTalk(
        0x104,
        "#00301F#12P#N怎、怎么了？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0257
    ChrTalk(
        0x103,
        (
            "#00205F#12P#N灵子能源的供给\x01",
            "中断了……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_71(0x14, 0x564, 0x58C, 0x0, 0x0)
    Sound(905, 0, 100, 0)
    Sound(954, 0, 100, 0)
    OP_79(0x14)
    Sound(902, 0, 100, 0)
    OP_68(0, 1000, -1000, 2000)
    MoveCamera(35, 19, 0, 2000)
    SetCameraDistance(35000, 2000)
    Sleep(1500)
    Fade(500)
    BeginChrThread(0x32, 1, 0, 68)
    Sound(927, 2, 100, 0)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    OP_0D()
    SetMapObjFrame(0xFF, "futa00", 0x2, "move2")
    Sleep(1300)
    Fade(500)
    OP_68(50000, -4500, -50000, 0)
    MoveCamera(340, 21, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(50000, 0)
    OP_68(0, -4500, -10000, 9000)
    MoveCamera(0, 33, 0, 9000)
    SetCameraDistance(115000, 9000)
    OP_71(0x1, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x2, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x3, 0x12C, 0x0, 0x0, 0x0)
    OP_71(0x4, 0x12C, 0x0, 0x0, 0x0)
    Sleep(2000)
    Sound(579, 2, 30, 0)
    OP_79(0x1)
    OP_79(0x2)
    OP_79(0x3)
    OP_79(0x4)
    StopSound(927, 500, 100)
    StopSound(579, 500, 20)
    Sound(954, 0, 100, 0)
    Sound(143, 0, 30, 0)
    SetMapObjFrame(0xFF, "futa01", 0x2, "move2")
    OP_6F(0x79)
    Fade(500)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    Sleep(1500)
    Fade(500)
    OP_68(0, 2000, 5500, 0)
    MoveCamera(25, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    OP_68(0, 2000, 3500, 3500)
    MoveCamera(35, 11, 0, 3500)
    SetCameraDistance(17000, 3500)
    Sound(930, 0, 100, 0)
    Sound(950, 2, 40, 0)
    Sound(933, 2, 100, 0)
    PlayEffect(0x1, 0x1, 0xC, 0x5, 0, 500, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_C126():
        OP_96(0xFE, 0x0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_C126)
    WaitChrThread(0xC, 1)

    def lambda_C144():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_C144)
    WaitChrThread(0xC, 2)
    StopEffect(0x1, 0x2)
    StopSound(950, 1000, 30)
    StopSound(933, 1000, 100)
    Sound(935, 0, 100, 0)
    OP_6F(0x79)
    Sleep(800)

    #C0258
    ChrTalk(
        0xC,
        "#11310F#5P不、不可能……！\x02",
    )

    CloseMessageWindow()
    StopSound(132, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3A5)
    OP_24(0x39F)
    OP_24(0x3B6)
    OP_24(0x243)
    OP_24(0x3AF)
    SetScenarioFlags(0x24, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_67_B75A end

    def Function_68_C1C5(): pass

    label("Function_68_C1C5")

    Sound(943, 2, 50, 0)
    Sleep(1500)
    OP_24(0x3AF)
    Sound(143, 0, 60, 0)
    Return()

    # Function_68_C1C5 end

    def Function_69_C1D8(): pass

    label("Function_69_C1D8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C20C")
    Sound(203, 0, 50, 0)
    Sleep(900)
    Sound(203, 0, 60, 0)
    Sleep(1100)
    Sound(203, 0, 50, 0)
    Sleep(800)
    Sound(203, 0, 40, 0)
    Sleep(1000)
    Jump("Function_69_C1D8")

    label("loc_C20C")

    Return()

    # Function_69_C1D8 end

    def Function_70_C20D(): pass

    label("Function_70_C20D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrChipPat(0x4, 0x1, 0x1F)
    SetChrChipPat(0x5, 0x1, 0x20)
    ClearScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x0, 1)
    ClearScenarioFlags(0x0, 2)
    ClearScenarioFlags(0x0, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C24B")
    AddParty(0x8, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 0)

    label("loc_C24B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C263")
    AddParty(0x4, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 1)

    label("loc_C263")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C27B")
    AddParty(0x5, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 2)

    label("loc_C27B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C293")
    AddParty(0x9, 0xFF, 0xFF)
    SetScenarioFlags(0x0, 3)

    label("loc_C293")

    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch13400.itc", 0x1F)
    LoadChrToIndex("chr/ch02500.itc", 0x20)
    LoadChrToIndex("apl/ch51732.itc", 0x21)
    LoadChrToIndex("apl/ch51113.itc", 0x22)
    LoadChrToIndex("apl/ch51734.itc", 0x23)
    LoadEffect(0x0, "event/ev10000.eff")
    LoadEffect(0x1, "event/ev10001.eff")
    LoadEffect(0x2, "event/ev17054.eff")
    SoundLoad(3787)
    SoundLoad(112)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04700.itp")
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, 0, 0)
    OP_8E(0xC, "迪塔总统")
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, 10000, 0, 1500, 270)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x101, -800, 0, -5500, 0)
    SetChrPos(0x102, 800, 0, -5500, 0)
    SetChrPos(0x103, -1700, 0, -7000, 0)
    SetChrPos(0x104, 1700, 0, -7000, 0)
    SetChrPos(0xF4, 100, 0, -6700, 0)
    SetChrPos(0xF5, -100, 0, -7800, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    OP_78(0x5, 0x28)
    SetChrPos(0x28, 0, 0, 6500, 180)
    OP_D5(0x28, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x14, 0x4)
    OP_74(0x5, 0x1E)
    OP_70(0x5, 0x58C)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    OP_78(0x14, 0x29)
    SetChrPos(0x29, 0, 0, 6500, 180)
    OP_D5(0x29, 0x0, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x14, 0x1000)
    ClearMapObjFlags(0x14, 0x4)
    OP_74(0x14, 0x1E)
    OP_70(0x14, 0x58C)
    SetChrFlags(0x28, 0x1)
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFrame(0xFF, "sky00", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kumo01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kumo01a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "back00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "back02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "a_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "b_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "c_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "d_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "03_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa02", 0x1, 0x1)
    SetMapObjFrame(0xFF, "futa03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "futa00", 0x2, "close")
    SetMapObjFrame(0xFF, "futa01", 0x2, "close")
    OP_70(0x1, 0x0)
    OP_70(0x2, 0x0)
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    ClearChrFlags(0x2C, 0x80)
    ClearChrFlags(0x2D, 0x80)
    ClearChrFlags(0x2E, 0x80)
    ClearChrFlags(0x2F, 0x80)
    ClearChrFlags(0x30, 0x80)
    ClearChrFlags(0x31, 0x80)
    OP_78(0xD, 0x2C)
    OP_78(0xE, 0x2D)
    OP_78(0xF, 0x2E)
    OP_78(0x10, 0x2F)
    OP_78(0x11, 0x30)
    OP_78(0x12, 0x31)
    OP_49()
    SetChrPos(0x2C, 15000, 6000, -3000, 0)
    SetChrPos(0x2D, 15100, 7000, -7500, 0)
    SetChrPos(0x2E, 15100, 7000, 1500, 0)
    SetChrPos(0x2F, 15200, 5000, 5000, 0)
    SetChrPos(0x30, 15200, 5000, -11000, 0)
    SetChrPos(0x31, 15000, 6000, -3000, 0)
    OP_D5(0x2C, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2D, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x2F, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x30, 0x0, 0x15F90, 0x0, 0x0)
    OP_D5(0x31, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFlags(0xE, 0x1000)
    SetMapObjFlags(0xF, 0x1000)
    SetMapObjFlags(0x10, 0x1000)
    SetMapObjFlags(0x11, 0x1000)
    SetMapObjFlags(0x12, 0x1000)
    OP_FF(0xD, 0x168, 0x168, 0x168)
    OP_FF(0xE, 0x140, 0x140, 0x140)
    OP_FF(0xF, 0x140, 0x140, 0x140)
    OP_FF(0x10, 0x140, 0x140, 0x140)
    OP_FF(0x11, 0x140, 0x140, 0x140)
    OP_FF(0x12, 0x17C, 0x17C, 0x17C)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0x15, 0x2B)
    OP_49()
    SetChrPos(0x2B, 0, 15000, 6000, 180)
    OP_D5(0x2B, 0x1388, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x1, 0x78, 0x0, 0x20)
    ClearChrFlags(0x18, 0x80)
    OP_78(0x17, 0x18)
    OP_49()
    SetChrPos(0x18, 0, 15000, 6000, 180)
    OP_D5(0x18, 0x1388, 0x2BF20, 0x0, 0x0)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x17, 0x1000)
    OP_68(210, 2500, 5500, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18050, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(210, 1500, 5500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0259
    ChrTalk(
        0xC,
        (
            "#12P#11307F这、这是怎么回事！？\x02\x03",

            "为什么『至宝』的供给\x01",
            "会突然停止……！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 40, -1, -1)
    SetChrName("阴森的声音")

    #A0260
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵，因为没时间\x01",
            "做这些无聊事了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(14, 280, 60, 3)
    PlayBGM("ed7580", 0)
    SetChrFlags(0x102, 0x8)
    OP_68(10000, 1000, 1500, 2000)
    SetCameraDistance(14000, 2000)
    TurnDirection(0xC, 0x13, 500)
    TurnDirection(0x101, 0x13, 0)
    TurnDirection(0x102, 0x13, 0)
    TurnDirection(0x103, 0x13, 0)
    TurnDirection(0x104, 0x13, 0)
    TurnDirection(0xF4, 0x13, 0)
    TurnDirection(0xF5, 0x13, 0)
    OP_6F(0x79)
    ClearChrFlags(0x102, 0x8)
    SetCameraDistance(13000, 2000)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    ClearChrFlags(0x13, 0x80)

    def lambda_C9E3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_C9E3)
    WaitChrThread(0x13, 2)
    Sleep(1000)

    #C0261
    ChrTalk(
        0x101,
        "#00013F『结社』的……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CA50")

    #C0262
    ChrTalk(
        0x105,
        (
            "#10407F『十三工房』的\x01",
            "Ｆ·诺华提斯……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CA6F")

    label("loc_CA50")


    #C0263
    ChrTalk(
        0x103,
        "#00207F诺华提斯博士……！\x02",
    )

    CloseMessageWindow()

    label("loc_CA6F")

    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(5960, 1000, 1210, 0)
    MoveCamera(55, 11, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(150)

    #C0264
    ChrTalk(
        0xC,
        (
            "#6P#11310F诺华提斯博士……\x01",
            "这到底是怎么回事！？\x02\x03",

            "难道『结社』在机体上\x01",
            "动了什么手脚！？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0265
    AnonymousTalk(
        0x13,
        (
            "呵呵，正如我之前所说，\x01",
            "这次只是顺便帮帮你而已。\x02\x03",

            "如今已经取得了令人满意的数据，\x01",
            "我差不多也该失陪了。\x02\x03",

            "按照契约，这架最终型也要一并收回。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(200)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0266
    ChrTalk(
        0xC,
        (
            "#6P#11307F你说契约……！？\x02\x03",

            "荒谬，这架机体是我们\x01",
            "从『结社』手中买下的！\x02\x03",

            "岂能让你带走！\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x13,
        (
            "#11P#04704F不不，其实契约\x01",
            "内容略有变更。\x02\x03",

            "已经修改为\x01",
            "由我们回收\x01",
            "使用完毕的机体了。\x02\x03",

            "#04702F当然，是在阁下的千金──\x01",
            "玛丽亚贝尔·库罗伊斯小姐的许可之下。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0xC,
        "#6P#11305F什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(260, 10, -1, -1)
    SetChrName("女孩的声音")

    #A0269
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#3787V#30W#37A哦呵呵……正是如此。\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0270
    ChrTalk(
        0x101,
        "#5P#00011F#6P#N这、这声音是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0271
    ChrTalk(
        0x102,
        "#00107F贝尔#6P#N……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7572", 0)
    Fade(500)
    OP_68(15000, 5500, -3000, 0)
    MoveCamera(62, 0, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14000, 0)
    OP_93(0xC, 0x5A, 0x0)
    OP_93(0x101, 0x5A, 0x0)
    OP_93(0x102, 0x5A, 0x0)
    OP_93(0x103, 0x5A, 0x0)
    OP_93(0x104, 0x5A, 0x0)
    OP_93(0xF4, 0x5A, 0x0)
    OP_93(0xF5, 0x5A, 0x0)
    SetCameraDistance(16000, 3000)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2C, 3, 0, 79)
    OP_6F(0x79)
    Sleep(500)

    #C0272
    ChrTalk(
        0xC,
        (
            "#11310F#6P#N贝尔……这到底是……？\x02\x03",

            "#11307F还有……你到底在哪里！？\x02\x03",

            "不在兰花塔内吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 160, -1, -1)

    #A0273
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，我早就\x01",
            "离开那里了。\x02\x03",

            "和琪雅他们一起哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0274
    ChrTalk(
        0x101,
        "#00005F#6P#N什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0275
    ChrTalk(
        0x102,
        (
            "#00101F#6P#N确、确实没有在\x01",
            "任何楼层见到他们……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    MoveCamera(57, -5, 0, 3000)
    SetCameraDistance(19500, 3000)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2D, 3, 0, 80)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2E, 3, 0, 81)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x2F, 3, 0, 82)
    Sleep(500)
    Sound(922, 0, 100, 0)
    BeginChrThread(0x30, 3, 0, 83)
    OP_6F(0x79)
    Sleep(300)

    #C0276
    ChrTalk(
        0x101,
        "#00007F#6P#N亚里欧斯先生……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D0BC")

    #C0277
    ChrTalk(
        0x10A,
        "#00610F#6P#N马克莱因……！\x02",
    )

    CloseMessageWindow()

    label("loc_D0BC")


    #C0278
    ChrTalk(
        0x104,
        (
            "#00307F#6P#N叔叔……！\x01",
            "谢莉……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D113")

    #C0279
    ChrTalk(
        0x106,
        "#10701F#6P#N血腥谢莉……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D113")


    #C0280
    ChrTalk(
        0x103,
        "#00201F#6P#N连瓦鲁多先生也……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D16F")

    #C0281
    ChrTalk(
        0x105,
        "#10401F#6P#N果然和他们在一起吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D16F")

    Sleep(150)
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("亚里欧斯")

    #A0282
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(120, 120, -1, -1)

    #A0283
    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(30, 160, -1, -1)

    #A0284
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哇！\x01",
            "热闹起来了呢！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(370, 160, -1, -1)

    #A0285
    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啧……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0286
    ChrTalk(
        0xC,
        (
            "#11310F#6P#N怎、怎么回事……\x02\x03",

            "#11307F你们……\x01",
            "背叛我了吗！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(240, 110, -1, -1)
    SetChrName("亚里欧斯")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……总统，非常抱歉。\x02\x03",

            "但我原本就没打算\x01",
            "协助您的计划。\x02\x03",

            "我只是在协助『律师』\x01",
            "和玛丽亚贝尔小姐的计划而已。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0288
    ChrTalk(
        0xC,
        (
            "#11305F#30W#6P#N『律师』……\x02\x03",

            "#11310F难……难不成……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("男性的声音")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，正是如此。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(250)
    OP_68(15000, 5500, -3000, 0)
    MoveCamera(90, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(14500, 0)
    OP_FF(0xD, 0x140, 0x140, 0x140)
    SetChrPos(0x2C, 15100, 5000, -7000, 0)
    SetChrPos(0x2D, 15200, 7500, -10000, 0)
    SetChrPos(0x30, 15300, 4000, -12000, 0)
    SetChrPos(0x2E, 15100, 7500, 2000, 0)
    SetChrPos(0x2F, 15200, 4000, 4000, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_0D()
    Sound(922, 0, 100, 0)
    BeginChrThread(0x31, 3, 0, 84)
    Sleep(500)
    CancelBlur(1000)
    SetCameraDistance(17500, 1000)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D463")
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0290
    ChrTalk(
        0x101,
        "#00007F#4S#12P#N……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D463")


    #C0291
    ChrTalk(
        0x102,
        "#00105F#12P#N………啊…………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0292
    ChrTalk(
        0x103,
        "#00205F#12P#N……哎…………？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0293
    ChrTalk(
        0x104,
        "#00305F#12P#N……骗、骗人的吧………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D50F")

    #C0294
    ChrTalk(
        0x10A,
        "#00605F#12P#N伊、伊安律师……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D53D")

    #C0295
    ChrTalk(
        0x109,
        "#10111F#12P#N怎、怎么会……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D53D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D573")

    #C0296
    ChrTalk(
        0x105,
        "#10410F#12P#N没想到……竟然是这样。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_D573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_D710")

    #C0297
    ChrTalk(
        0x101,
        "#00013F#12P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("伊安律师")

    #A0298
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "唔，看样子，\x01",
            "罗伊德已经察觉到\x01",
            "我与此事的牵连了吧……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0299
    ChrTalk(
        0x101,
        (
            "#00006F#12P#N……嗯。\x01",
            "那位名叫尼尔森的记者\x01",
            "给了我一些提示。\x02\x03",

            "#00008F再加上皮特和守墓老人……\x01",
            "还有雾香小姐和雷克特先生的意见……\x02\x03",

            "#00013F所有情报的碎片，\x01",
            "最终都指向了您的参与。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, 150, -1, -1)
    SetChrName("伊安律师")

    #A0300
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，看来你已经\x01",
            "完全赶上盖伊了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_D710")

    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(300)

    #C0301
    ChrTalk(
        0xC,
        (
            "#6P#11310F#N格里姆伍德律师……\x01",
            "这究竟是怎么回事……！？\x02\x03",

            "您、您曾经给过我\x01",
            "许多建议……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("伊安律师")

    #A0302
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯……你确实是个\x01",
            "很有教导价值的学生。\x02\x03",

            "不仅是个超一流的经营者，\x01",
            "以政治家的标准来说，也算不差。\x02\x03",

            "但你却有个致命的缺点，\x01",
            "那就是太过沉溺于梦想。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(50)
    OP_82(0x32, 0x0, 0x7D0, 0xC8)

    #C0303
    ChrTalk(
        0xC,
        "#6P#11305F#N……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    #A0304
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，父亲似乎一直都\x01",
            "以为计划是按照自己的\x01",
            "想法顺利进展的……\x02\x03",

            "但事实上，却只是在他人的诱导之下，\x01",
            "沿着律师安排好的剧本步步推进而已。\x02\x03",

            "从处理教团的方式、通商会议的具体安排，\x01",
            "到袭击克洛斯贝尔市和独立宣言……\x02\x03",

            "这些想法，当初又是谁\x01",
            "灌输给父亲的呢？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0305
    ChrTalk(
        0xC,
        "#6P#11310F#30W#N………啊……………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("伊安律师")

    #A0306
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "如果你能将这部剧本顺利演下去，\x01",
            "我原本并不打算走到台前……\x02\x03",

            "但如今看来，我已经不能\x01",
            "继续待在幕后了。\x02\x03",

            "『碧零计划』，\x01",
            "将由我继续执行下去。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0307
    ChrTalk(
        0xC,
        "#6P#11310F#N碧……零……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0308
    ChrTalk(
        0x101,
        "#00007F#6P#N那、那是什么！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    #A0309
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，就是『零之至宝』的完成形态……\x02\x03",

            "可以支配时空，改变因果律的\x01",
            "『碧之大树』……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(270, 110, -1, -1)

    #A0310
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S在此诞生的一刻……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(929, 0, 40, 0)
    Sound(934, 0, 40, 0)
    Sound(112, 2, 100, 0)
    PlayEffect(0x2, 0x0, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
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
    Sleep(50)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    StopBGM(0x1388)
    OP_68(8000, 3000, -6000, 1000)
    SetCameraDistance(24000, 1000)

    def lambda_DC8B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_DC8B)

    def lambda_DC98():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_DC98)

    def lambda_DCA5():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_DCA5)
    Sleep(50)

    def lambda_DCB5():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_DCB5)
    Sleep(50)

    def lambda_DCC5():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_DCC5)
    Sleep(50)

    def lambda_DCD5():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_DCD5)
    Sleep(50)

    def lambda_DCE5():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_DCE5)
    Sleep(50)

    def lambda_DCF5():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_DCF5)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0311
    ChrTalk(
        0x104,
        "#00305F#5P这道光是……！？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x102,
        "#00105F#5P蓝色的光芒……！？\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x103,
        (
            "#00207F#5P……东南偏南方向！\x01",
            "是湿地那边！\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        "#00010F#5P那是……！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7555", 0)
    OP_68(8000, 3000, -7000, 2000)
    SetCameraDistance(24500, 2000)
    StopSound(132, 1000, 40)
    StopSound(112, 1000, 90)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_07a.pmf", 0x22B, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    ClearMapObjFlags(0x16, 0x4)
    StopEffect(0x0, 0x0)
    OP_68(0, 2000, -20000, 0)
    MoveCamera(150, 9, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18500, 0)
    Sound(132, 2, 50, 0)
    Sound(112, 2, 80, 0)
    OP_68(0, 2000, -13000, 4000)
    MoveCamera(145, 9, 0, 4000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0x7D0)

    #C0315
    ChrTalk(
        0x101,
        "#5P#00010F#6P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DEED")

    #C0316
    ChrTalk(
        0x109,
        "#5P#10111F#6P#N什么啊……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DEED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF1B")

    #C0317
    ChrTalk(
        0x105,
        "#5P#10410F#6P#N这、这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DF1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF4D")

    #C0318
    ChrTalk(
        0x10A,
        "#5P#00610F#6P#N……怎么可能……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DF4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF7D")

    #C0319
    ChrTalk(
        0x106,
        "#5P#10701F#6P#N……大树……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_DF7D")

    WaitBGM()
    Sleep(10)
    PlayBGM("ed7571", 0)
    Sleep(500)

    #N0320
    NpcTalk(
        0x104,
        "诺华提斯博士",
        (
            "#04702F#5P#N呵呵，太棒了！\x02\x03",

            "真可谓奇迹的产物……\x01",
            "而且可以说是远远超越了『盐之桩』的\x01",
            "『预料外的奇迹』啊！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0321
    ChrTalk(
        0xC,
        "#11305F#6P#N…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopSound(112, 2000, 70)
    Fade(500)
    OP_68(8000, 3000, -3000, 0)
    MoveCamera(50, 3, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0322
    ChrTalk(
        0x101,
        (
            "#00007F#4S#6P#N等、等一下！\x02\x03",

            "#00010F#3S你说那棵巨大的树\x01",
            "是『零之至宝』的完成形态……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_E0EC():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_E0EC)
    Sleep(30)

    def lambda_E0FC():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_E0FC)
    Sleep(30)

    def lambda_E10C():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_E10C)
    Sleep(30)

    def lambda_E11C():
        OP_93(0xF4, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_E11C)
    Sleep(30)

    def lambda_E12C():
        OP_93(0xF5, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_E12C)
    Sleep(30)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0323
    ChrTalk(
        0x102,
        (
            "#00107F#6P#N那琪雅……\x01",
            "……那孩子到底在哪里！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(270, 110, -1, -1)

    #A0324
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，你在说什么？\x02\x03",

            "你们要找的琪雅……\x01",
            "站在原地不就可以看得到吗？\x02\x03",

            "那棵『碧之大树』本身\x01",
            "就是琪雅呀。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
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
    Sleep(300)
    SetMessageWindowPos(300, 70, -1, -1)
    SetChrName("亚里欧斯")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……她并没有丧失\x01",
            "自己的身心。\x02\x03",

            "你们可以放心……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(190, 100, -1, -1)
    SetChrName("伊安律师")

    #A0326
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "然而，从此刻开始，她将成为\x01",
            "世间一切事理的『调停者』。\x02\x03",

            "无论是对她还是对你们来说，\x01",
            "这都不是一件坏事。\x02\x03",

            "如果可以，希望你们能默默守望着她。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0327
    ChrTalk(
        0x103,
        "#00206F#6P#N到、到底在说什么……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0328
    ChrTalk(
        0x104,
        "#00310F#6P#N这也太莫名其妙了……\x02",
    )

    CloseMessageWindow()
    OP_68(15000, 5000, -5000, 1600)
    MoveCamera(69, -5, 0, 1600)
    SetCameraDistance(19500, 1600)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E4AD")
    SetMessageWindowPos(0, 170, -1, -1)

    #A0329
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "确实如此。\x02\x03",

            "不过，只要玩得\x01",
            "开心就好了。\x02\x03",

            "对吧，莉夏⊥\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0330
    ChrTalk(
        0x106,
        "#10701F#6P#N…………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_E4F3")

    label("loc_E4AD")

    SetMessageWindowPos(0, 170, -1, -1)

    #A0331
    AnonymousTalk(
        0xE,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "确实如此。\x02\x03",

            "不过，只要玩得\x01",
            "开心就好了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_E4F3")

    SetMessageWindowPos(10, 110, -1, -1)

    #A0332
    AnonymousTalk(
        0xD,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哼哼，如果你们企图阻挠，\x01",
            "我们可是不会手下留情的。\x02\x03",

            "这也是契约的内容之一。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E610")
    SetMessageWindowPos(370, 160, -1, -1)

    #A0333
    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……虽然这些家伙的企图\x01",
            "与我无关……\x02\x03",

            "但你们要是过来，\x01",
            "我一定会把你们彻底打垮……\x02\x03",

            "听到了吗，瓦吉……？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0334
    ChrTalk(
        0x105,
        "#10401F#6P#N……瓦鲁多。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_E67F")

    label("loc_E610")

    SetMessageWindowPos(370, 160, -1, -1)

    #A0335
    AnonymousTalk(
        0xF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "……虽然这些家伙的企图\x01",
            "与我无关……\x02\x03",

            "但你们要是过来，\x01",
            "我一定会把你们彻底打垮……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_E67F")

    SetMessageWindowPos(160, 150, -1, -1)

    #A0336
    AnonymousTalk(
        0x11,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦呵呵……\x01",
            "那么，要和各位说再见了。\x02\x03",

            "另外……父亲，\x01",
            "多年以来，一直承蒙您的照顾。\x02\x03",

            "虽然您生性单纯、浪漫主义，\x01",
            "而且愚不可及……\x02\x03",

            "但我丝毫都\x01",
            "不讨厌您哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(977, 0, 100, 0)
    BeginChrThread(0x31, 3, 0, 90)
    Sleep(200)
    BeginChrThread(0x2C, 3, 0, 85)
    Sleep(200)
    BeginChrThread(0x2D, 3, 0, 86)
    Sleep(200)
    Sound(977, 0, 50, 0)
    BeginChrThread(0x2E, 3, 0, 87)
    Sleep(200)
    BeginChrThread(0x2F, 3, 0, 88)
    Sleep(200)
    BeginChrThread(0x30, 3, 0, 89)
    WaitChrThread(0x30, 3)
    Fade(500)
    OP_68(5000, 1500, -1000, 0)
    MoveCamera(35, 11, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(19000, 0)
    OP_93(0xC, 0x5A, 0x0)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(2000, 1500, -1000, 3000)
    OP_0D()
    OP_6F(0x79)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)

    #C0337
    ChrTalk(
        0xC,
        "#5P#11311F#40W…………贝尔……………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xC, 0x21)
    SetChrSubChip(0xC, 0x0)
    Sleep(1000)

    def lambda_E88B():
        OP_A6(0xFE, 0x0, 0x1E, 0x2EE, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_E88B)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xC, 0x1)
    Sleep(130)
    SetChrSubChip(0xC, 0x2)
    Sleep(130)
    SetChrSubChip(0xC, 0x3)
    Sleep(500)
    TurnDirection(0x13, 0xC, 500)

    #C0338
    ChrTalk(
        0x13,
        (
            "#04704F呵呵，如果不是任务在身，\x01",
            "我本可以奉陪到最后的……\x02\x03",

            "#04700F罢了，我就在远方\x01",
            "等待后续消息吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    Sound(901, 0, 100, 0)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    Sleep(500)
    Fade(1000)
    SetMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    OP_0D()
    OP_68(0, 2000, -1000, 2000)
    MoveCamera(31, 5, 0, 2000)
    SetCameraDistance(18000, 2000)
    Sound(980, 2, 30, 0)
    BeginChrThread(0x28, 3, 0, 77)
    Sleep(300)
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

    def lambda_EA2C():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EA2C)
    Sleep(50)

    def lambda_EA3C():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EA3C)
    Sleep(50)

    def lambda_EA4C():
        OP_93(0x103, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EA4C)
    Sleep(50)

    def lambda_EA5C():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EA5C)
    Sleep(50)

    def lambda_EA6C():
        OP_93(0xF4, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_EA6C)
    Sleep(50)

    def lambda_EA7C():
        OP_93(0xF5, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_EA7C)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)

    #C0339
    ChrTalk(
        0x101,
        "#00007F#12P#N……啊………\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x28, 3)
    BeginChrThread(0x28, 3, 0, 78)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10000, 0, 1500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)

    def lambda_EB12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_EB12)
    WaitChrThread(0x13, 2)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    OP_D3(0x13, 0x5, "Null_hand_l(63)")
    OP_93(0x13, 0x0, 0x0)
    ClearChrFlags(0x13, 0x1)
    OP_52(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(310, 4200, 5930, 2000)
    MoveCamera(31, 7, 0, 2000)
    SetCameraDistance(15000, 2000)
    Sleep(500)
    Sound(223, 0, 100, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 1900, 3900, 4750, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_EBC2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_EBC2)
    WaitChrThread(0x13, 2)
    Sound(936, 0, 100, 0)
    Sleep(1200)

    #C0340
    ChrTalk(
        0x13,
        (
            "#5P#04709F哈哈，那我也就此失陪了。\x02\x03",

            "#04704F虽然继续顽抗也是徒劳无益，\x01",
            "但你们就尽管挣扎吧。\x02\x03",

            "#04702F这样也能留下点\x01",
            "有意义的数据。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(955, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 4900, 6000, 700)
    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x51E, 0x532, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x532, 0x55A, 0x0, 0x20)
    OP_6F(0x79)
    MoveCamera(25, 15, 0, 3000)
    SetCameraDistance(22000, 3000)
    Sound(223, 0, 100, 0)
    Sound(919, 0, 70, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 0, 0, 6500, 0, 0, 0, 5000, 5000, 5000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    Sound(936, 0, 100, 0)
    StopSound(980, 1000, 30)
    OP_75(0x5, 0x1, 0x1F4)

    def lambda_ED13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_ED13)

    def lambda_ED24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_ED24)
    WaitChrThread(0x13, 2)
    SetChrFlags(0x13, 0x80)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(0, 2000, -1000, 0)
    MoveCamera(31, 5, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18500, 0)
    OP_0D()

    #C0341
    ChrTalk(
        0x103,
        "#00201F#30W#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#00310F#30W#11P搞出这么多烂摊子，\x01",
            "却说走就走了吗……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x6, 0, 0, -21000, 0)
    SetChrPos(0x7, 0, 0, -22000, 0)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    StopBGM(0x1770)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_EE45")

    #N0343
    NpcTalk(
        0x105,
        "瓦吉的声音",
        "大家没事吧……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_EEA6")

    label("loc_EE45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_EE7A")

    #N0344
    NpcTalk(
        0x109,
        "诺艾尔的声音",
        "各位……都没事吧！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_EEA6")

    label("loc_EE7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_EEA6")

    #N0345
    NpcTalk(
        0x10A,
        "达德利的声音",
        "都还好吗……！？\x02",
    )

    CloseMessageWindow()

    label("loc_EEA6")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF5, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(0, 1200, -10000, 2250)
    MoveCamera(55, 13, 0, 2250)
    OP_6E(600, 2250)
    SetCameraDistance(15000, 2250)

    def lambda_EF4E():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_EF4E)
    Sleep(50)

    def lambda_EF5E():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_EF5E)
    Sleep(50)

    def lambda_EF6E():
        OP_93(0x103, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_EF6E)
    Sleep(50)

    def lambda_EF7E():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_EF7E)
    Sleep(50)

    def lambda_EF8E():
        OP_93(0xF4, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_EF8E)
    Sleep(50)

    def lambda_EF9E():
        OP_93(0xF5, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_EF9E)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    def lambda_EFC3():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x6, 1, lambda_EFC3)
    Sleep(200)

    def lambda_EFE0():
        OP_96(0xFE, 0x320, 0x0, 0xFFFFCF2C, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x7, 1, lambda_EFE0)
    WaitChrThread(0x6, 1)
    WaitChrThread(0x7, 1)
    OP_6F(0x79)

    #C0346
    ChrTalk(
        0x101,
        "#00008F你们来了……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F075")

    #C0347
    ChrTalk(
        0x106,
        (
            "#10708F#12P刚才那到底是……\x02\x03",

            "#10707F还有那棵巨大的树，\x01",
            "究竟是什么……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13A")

    label("loc_F075")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F0D6")

    #C0348
    ChrTalk(
        0x10A,
        (
            "#00610F#12P刚才那到底是……\x02\x03",

            "#00607F还有那棵巨大的树，\x01",
            "究竟是什么东西……！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_F13A")

    label("loc_F0D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F13A")

    #C0349
    ChrTalk(
        0x109,
        (
            "#10108F#12P刚、刚才那到底是……\x02\x03",

            "#10107F还、还有那棵巨大的树，\x01",
            "究竟是什么东西……！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F13A")


    #C0350
    ChrTalk(
        0x102,
        "#5P#00106F这、这个……\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        "#5P#00206F该怎么说才好呢……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrPos(0x15, -8500, -2000, -20000, 90)

    #N0352
    NpcTalk(
        0x15,
        "赛尔盖的声音",
        (
            "……看来事情\x01",
            "还没结束啊。\x02",
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
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7567", 0)
    Fade(500)
    OP_68(0, 1000, -21800, 0)
    MoveCamera(145, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x6, -1200, 0, -12500, 0)
    SetChrPos(0x7, 1200, 0, -12500, 0)

    def lambda_F2BA():
        OP_95(0xFE, -2200, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F2BA)
    Sleep(500)
    Sound(112, 2, 50, 0)
    WaitChrThread(0x15, 1)

    def lambda_F2E1():
        OP_95(0xFE, 0, 0, -21800, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F2E1)
    WaitChrThread(0x15, 1)
    OP_68(0, 1000, -10000, 4000)
    MoveCamera(145, 15, 0, 4000)

    def lambda_F31B():
        OP_95(0xFE, 0, 0, -11500, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_F31B)
    WaitChrThread(0x15, 1)
    OP_6F(0x79)

    #C0353
    ChrTalk(
        0x101,
        "#6P#00005F科长……！\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x104,
        "#00301F#6P下面的情况还好吗？\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x15,
        (
            "#11P#01003F嗯，魔导兵都消失了，\x01",
            "所以我们顺利进来了。\x02\x03",

            "#01001F不过……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x15, 0xB4, 0x1F4)
    Sleep(900)
    OP_68(-450, 1500, -5360, 1500)
    SetCameraDistance(18700, 1500)
    OP_93(0x15, 0x0, 0x1F4)
    OP_6F(0x79)
    Sleep(500)

    #C0356
    ChrTalk(
        0xC,
        "#11311F#40W#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x15,
        (
            "#11P#01006F……这究竟\x01",
            "是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x102,
        "#00108F#6P嗯……\x02",
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#6P#00006F#6P……这个……\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18200, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(300)
    SetChrPos(0x101, -450, 0, -9600, 180)
    SetChrPos(0x102, 450, 0, -9100, 180)
    SetChrPos(0x103, -1500, 0, -9600, 135)
    SetChrPos(0x104, 1500, 0, -9600, 225)
    SetChrPos(0xF4, -1050, 0, -8000, 180)
    SetChrPos(0xF5, 1050, 0, -8000, 180)
    SetChrPos(0x6, -1750, 0, -11400, 45)
    SetChrPos(0x7, 1750, 0, -11400, 315)
    SetChrPos(0x15, 0, 0, -12900, 0)
    OP_68(-120, 1100, -11660, 0)
    MoveCamera(143, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetChrName("")

    #A0360
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人向科长说明了前因后果。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(14500, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_F604")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F5DD")

    #C0361
    ChrTalk(
        0x106,
        "#11P#10712F竟、竟有这种事……\x02",
    )

    Jump("loc_F5FE")

    label("loc_F5DD")


    #C0362
    ChrTalk(
        0x106,
        "#5P#10712F竟、竟有这种事……\x02",
    )


    label("loc_F5FE")

    CloseMessageWindow()
    Jump("loc_F6D9")

    label("loc_F604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F679")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F64C")

    #C0363
    ChrTalk(
        0x109,
        "#11P#10106F竟、竟然发生了这种事……\x02",
    )

    Jump("loc_F673")

    label("loc_F64C")


    #C0364
    ChrTalk(
        0x106,
        "#5P#10706F竟、竟然发生了这种事……\x02",
    )


    label("loc_F673")

    CloseMessageWindow()
    Jump("loc_F6D9")

    label("loc_F679")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F6D9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F6B9")

    #C0365
    ChrTalk(
        0x105,
        "#11P#10406F真是太惊人了……\x02",
    )

    Jump("loc_F6D8")

    label("loc_F6B9")


    #C0366
    ChrTalk(
        0x105,
        "#5P#10406F真是太惊人了……\x02",
    )


    label("loc_F6D8")

    CloseMessageWindow()

    label("loc_F6D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_F760")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F72A")

    #C0367
    ChrTalk(
        0x10A,
        (
            "#11P#00608F没想到伊安律师\x01",
            "是幕后黑手之一……\x02",
        )
    )

    Jump("loc_F75A")

    label("loc_F72A")


    #C0368
    ChrTalk(
        0x10A,
        (
            "#5P#00608F没想到伊安律师\x01",
            "是幕后黑手之一……\x02",
        )
    )


    label("loc_F75A")

    CloseMessageWindow()
    Jump("loc_F875")

    label("loc_F760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_F7F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F7B9")

    #C0369
    ChrTalk(
        0x105,
        (
            "#11P#10403F那个大胡子熊律师\x01",
            "居然是幕后黑手之一啊……\x02",
        )
    )

    Jump("loc_F7F1")

    label("loc_F7B9")


    #C0370
    ChrTalk(
        0x105,
        (
            "#5P#10403F那个大胡子熊律师\x01",
            "居然是幕后黑手之一啊……\x02",
        )
    )


    label("loc_F7F1")

    CloseMessageWindow()
    Jump("loc_F875")

    label("loc_F7F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_F875")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_F846")

    #C0371
    ChrTalk(
        0x109,
        (
            "#11P#10108F伊安律师\x01",
            "居然是幕后黑手之一……\x02",
        )
    )

    Jump("loc_F874")

    label("loc_F846")


    #C0372
    ChrTalk(
        0x109,
        (
            "#5P#10108F伊安律师\x01",
            "居然是幕后黑手之一……\x02",
        )
    )


    label("loc_F874")

    CloseMessageWindow()

    label("loc_F875")


    #C0373
    ChrTalk(
        0x15,
        (
            "#11P#01006F……原来如此。\x02\x03",

            "#01001F从财政界到国际形势，从警察到协会，\x01",
            "那位律师深谙各方面的内情。\x02\x03",

            "#01003F只要他有意，\x01",
            "的确有能力全盘操控。\x02\x03",

            "#01000F问题在于他的动机……\x01",
            "但现在似乎不是追究这个的时候。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x101,
        "#00006F#6P是的……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(200)
    SetChrName("")
    BeginChrThread(0x101, 0, 0, 74)
    WaitChrThread(0x101, 0)

    #C0375
    ChrTalk(
        0x101,
        (
            "#13P#00001F瓦吉，\x01",
            "可以呼叫梅尔卡瓦吗？\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    #C0376
    ChrTalk(
        0x105,
        "#13P#10402F呵呵，就知道你会这么说。\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_93(0x105, 0x10E, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 80, 0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x4)
    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    Sleep(500)
    SetChrSubChip(0x105, 0x5)
    Sound(804, 0, 100, 0)
    Sleep(500)

    #C0377
    ChrTalk(
        0x15,
        "#11P#01000F……要去吗？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA48")

    def lambda_FA40():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x6, 2, lambda_FA40)

    label("loc_FA48")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA67")

    def lambda_FA5F():
        TurnDirection(0xFE, 0x15, 500)
        ExitThread()

    QueueWorkItem(0x7, 2, lambda_FA5F)

    label("loc_FA67")

    OP_93(0x101, 0xB4, 0x1F4)

    #C0378
    ChrTalk(
        0x101,
        (
            "#00003F#6P嗯，这或许已经\x01",
            "超出了警察的工作范畴……\x02\x03",

            "#00013F但是，琪雅和一切真相\x01",
            "都在那里等着我们，\x01",
            "实在是无法置之不理。\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x102,
        (
            "#00101F#6P……我也赞同，\x01",
            "必须要阻止贝尔……\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x103,
        (
            "#00204F#6P嗯，事到如今，\x01",
            "无论怎样也要一起走到最后。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x104,
        (
            "#00302F#6P叔叔他们似乎也摩拳擦掌，\x01",
            "在那里等着我们呢。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 0, 0, 72)
    WaitChrThread(0x109, 0)

    #C0382
    ChrTalk(
        0x109,
        (
            "#6P#10107F我……\x01",
            "我也要一起去！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x105, 0x4)
    Sound(804, 0, 100, 0)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 80, 0)
    SetChrChipByIndex(0x105, 0xFF)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(150)
    TurnDirection(0x105, 0x15, 500)
    BeginChrThread(0x105, 0, 0, 73)
    WaitChrThread(0x105, 0)

    #C0383
    ChrTalk(
        0x105,
        (
            "#6P#10404F嗯，反正也要提供梅尔卡瓦，\x01",
            "我就奉陪到最后吧。\x02\x03",

            "#10400F似乎也有必要\x01",
            "和瓦鲁多做个了断啊。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x106, 0, 0, 75)
    WaitChrThread(0x106, 0)

    #C0384
    ChrTalk(
        0x106,
        (
            "#6P#10703F……我也要和『她』\x01",
            "做个了结。\x02\x03",

            "#10708F这也是为了给自己一个交代……\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x10A, 0, 0, 76)
    WaitChrThread(0x10A, 0)

    #C0385
    ChrTalk(
        0x10A,
        (
            "#6P#00603F……我也要对\x01",
            "马克莱因和伊安律师二人\x01",
            "进行详细的调查审讯。\x02\x03",

            "#00601F一起去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x15,
        (
            "#11P#01004F呵呵……\x01",
            "看来阻止你们也只会白费唇舌了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x32, 1, 0, 91)
    OP_68(1020, 1900, -13060, 3000)
    MoveCamera(143, 12, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(18500, 3000)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x2B, 0, 60000, -10000, 0)
    OP_D5(0x2B, 0x0, 0x0, 0x0, 0x0)
    ClearMapObjFlags(0x15, 0x4)

    def lambda_FDDB():
        OP_96(0x2B, 0x0, 0x2710, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_FDDB)
    BeginChrThread(0x2B, 3, 0, 71)
    OP_68(0, 45000, 0, 0)
    MoveCamera(231, -60, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(55000, 0)
    MoveCamera(211, -30, 0, 7000)
    SetCameraDistance(45000, 7000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    SetChrPos(0x18, 11000, 0, -2000, 200)
    OP_D5(0x18, 0x0, 0x30D40, 0x0, 0x0)
    OP_75(0x17, 0x2, 0xBB8)
    OP_68(1020, 1900, -13060, 0)
    MoveCamera(143, 12, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    OP_68(-240, 1100, -11750, 3000)
    MoveCamera(143, 17, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0387
    ChrTalk(
        0x15,
        (
            "#11P#01003F连同拘捕总统在内，\x01",
            "市里和塔内的事情就交给我们吧。\x02\x03",

            "#01001F你们只管放手去做，直到得出\x01",
            "能令自己满意的答案为止。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0x7D0, 0xC8)

    #C0388
    ChrTalk(
        0x15,
        (
            "#01007F#11P不要负了『特别任务支援科』之名……\x01",
            "更重要的是，不要负了你们自己的心意！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x12C, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(80, 50, -1, -1)
    SetChrName("罗伊德等人")

    #A0389
    AnonymousTalk(
        0xFF,
        "#4S是……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 3000)
    StopSound(132, 490, 40)
    StopSound(112, 490, 40)
    FadeToDark(2000, 0, -1)
    Sleep(500)
    StopSound(497, 1500, 50)
    StopSound(496, 1500, 50)
    OP_0D()
    EndChrThread(0x2B, 0xFF)
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, 60, 3)
    StopBGM(0xFA0)
    WaitBGM()
    OP_24(0x84)
    OP_24(0x70)
    Sleep(2000)
    OP_29(0xB1, 0x1, 0xF)
    OP_29(0xB1, 0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_END)), "loc_1007F")
    OP_E0(0x33, 0x0)
    OP_E0(0x80, 0x0)
    Sleep(500)

    label("loc_1007F")

    OP_E5(0x3)
    SetScenarioFlags(0x23, 6)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_70_C20D end

    def Function_71_1008E(): pass

    label("Function_71_1008E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_100B2")
    OP_82(0xA, 0xA, 0xBB8, 0x1F4)
    Sleep(500)
    Jump("Function_71_1008E")

    label("loc_100B2")

    Return()

    # Function_71_1008E end

    def Function_72_100B3(): pass

    label("Function_72_100B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_100CD")
    OP_FC(0x1)
    Jump("loc_10116")

    label("loc_100CD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_100E7")
    OP_FC(0x2)
    Jump("loc_10116")

    label("loc_100E7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10101")
    OP_FC(0x1)
    Jump("loc_10116")

    label("loc_10101")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10116")
    OP_FC(0x2)

    label("loc_10116")

    Sleep(1)
    Return()

    # Function_72_100B3 end

    def Function_73_1011A(): pass

    label("Function_73_1011A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10134")
    OP_FC(0x6)
    Jump("loc_1017D")

    label("loc_10134")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1014E")
    OP_FC(0x6)
    Jump("loc_1017D")

    label("loc_1014E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10168")
    OP_FC(0xB)
    Jump("loc_1017D")

    label("loc_10168")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1017D")
    OP_FC(0x5)

    label("loc_1017D")

    Sleep(1)
    Return()

    # Function_73_1011A end

    def Function_74_10181(): pass

    label("Function_74_10181")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1019B")
    OP_FC(0xB)
    Jump("loc_101E4")

    label("loc_1019B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_101B5")
    OP_FC(0xB)
    Jump("loc_101E4")

    label("loc_101B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_101CF")
    OP_FC(0x6)
    Jump("loc_101E4")

    label("loc_101CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_101E4")
    OP_FC(0x6)

    label("loc_101E4")

    Sleep(1)
    Return()

    # Function_74_10181 end

    def Function_75_101E8(): pass

    label("Function_75_101E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10202")
    OP_FC(0x1)
    Jump("loc_1024B")

    label("loc_10202")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1021C")
    OP_FC(0x2)
    Jump("loc_1024B")

    label("loc_1021C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10236")
    OP_FC(0x1)
    Jump("loc_1024B")

    label("loc_10236")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1024B")
    OP_FC(0x2)

    label("loc_1024B")

    Sleep(1)
    Return()

    # Function_75_101E8 end

    def Function_76_1024F(): pass

    label("Function_76_1024F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10269")
    OP_FC(0x1)
    Jump("loc_102B2")

    label("loc_10269")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF5, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_10283")
    OP_FC(0x2)
    Jump("loc_102B2")

    label("loc_10283")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x6, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1029D")
    OP_FC(0x1)
    Jump("loc_102B2")

    label("loc_1029D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x7, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_102B2")
    OP_FC(0x2)

    label("loc_102B2")

    Sleep(1)
    Return()

    # Function_76_1024F end

    def Function_77_102B6(): pass

    label("Function_77_102B6")

    Sound(905, 0, 100, 0)
    Sound(904, 2, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x3A3, 0x3CA, 0x0, 0x0)
    Sleep(2000)
    Sound(902, 0, 70, 0)
    OP_79(0x5)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0xB, 0x32, 0x0, 0x0)
    Sound(951, 0, 100, 0)
    OP_24(0x388)
    Return()

    # Function_77_102B6 end

    def Function_78_102F8(): pass

    label("Function_78_102F8")

    Sound(905, 0, 100, 0)
    OP_71(0x5, 0x4E2, 0x4F6, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x4F6, 0x51E, 0x0, 0x20)
    Return()

    # Function_78_102F8 end

    def Function_79_1031A(): pass

    label("Function_79_1031A")

    OP_71(0xD, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xD)
    OP_71(0xD, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_79_1031A end

    def Function_80_10336(): pass

    label("Function_80_10336")

    OP_71(0xE, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xE)
    OP_71(0xE, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_80_10336 end

    def Function_81_10352(): pass

    label("Function_81_10352")

    OP_71(0xF, 0x0, 0x64, 0x0, 0x8)
    OP_79(0xF)
    OP_71(0xF, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_81_10352 end

    def Function_82_1036E(): pass

    label("Function_82_1036E")

    OP_71(0x10, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x10)
    OP_71(0x10, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_82_1036E end

    def Function_83_1038A(): pass

    label("Function_83_1038A")

    OP_71(0x11, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x11)
    OP_71(0x11, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_83_1038A end

    def Function_84_103A6(): pass

    label("Function_84_103A6")

    OP_74(0x12, 0xF)
    OP_71(0x12, 0x0, 0x64, 0x0, 0x8)
    OP_79(0x12)
    OP_74(0x12, 0x1E)
    OP_71(0x12, 0x64, 0xC8, 0x0, 0x20)
    Return()

    # Function_84_103A6 end

    def Function_85_103CA(): pass

    label("Function_85_103CA")

    OP_75(0xD, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_85_103CA end

    def Function_86_103D5(): pass

    label("Function_86_103D5")

    OP_75(0xE, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_86_103D5 end

    def Function_87_103E0(): pass

    label("Function_87_103E0")

    OP_75(0xF, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_87_103E0 end

    def Function_88_103EB(): pass

    label("Function_88_103EB")

    OP_75(0x10, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_88_103EB end

    def Function_89_103F6(): pass

    label("Function_89_103F6")

    OP_75(0x11, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_89_103F6 end

    def Function_90_10401(): pass

    label("Function_90_10401")

    OP_75(0x12, 0x1, 0x3E8)
    Sleep(2000)
    Return()

    # Function_90_10401 end

    def Function_91_1040C(): pass

    label("Function_91_1040C")

    Sound(497, 2, 0, 0)
    Sound(496, 2, 0, 0)
    Sleep(200)
    OP_25(0x1F1, 0x5)
    OP_25(0x1F0, 0x5)
    Sleep(200)
    OP_25(0x1F1, 0xA)
    OP_25(0x1F0, 0xA)
    Sleep(200)
    OP_25(0x1F1, 0xF)
    OP_25(0x1F0, 0xF)
    Sleep(200)
    OP_25(0x1F1, 0x14)
    OP_25(0x1F0, 0x14)
    Sleep(200)
    OP_25(0x1F1, 0x19)
    OP_25(0x1F0, 0x19)
    Sleep(200)
    OP_25(0x1F1, 0x1E)
    OP_25(0x1F0, 0x1E)
    Sleep(200)
    OP_25(0x1F1, 0x23)
    OP_25(0x1F0, 0x23)
    Sleep(200)
    OP_25(0x1F1, 0x28)
    OP_25(0x1F0, 0x28)
    Sleep(200)
    OP_25(0x1F1, 0x2D)
    OP_25(0x1F0, 0x2D)
    Sleep(200)
    OP_25(0x1F1, 0x32)
    OP_25(0x1F0, 0x32)
    Return()

    # Function_91_1040C end

    def Function_92_10487(): pass

    label("Function_92_10487")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    EventEnd(0x5)
    SetCameraDistance(13000, 0)
    Return()

    # Function_92_10487 end

    def Function_93_1049F(): pass

    label("Function_93_1049F")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    StopEffect(0x9, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0390
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 0)
    OP_65(0x0, 0x1)
    EventEnd(0x3)
    Return()

    # Function_93_1049F end

    def Function_94_104FA(): pass

    label("Function_94_104FA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch05620.itc", 0x1E)
    LoadChrToIndex("chr/ch30000.itc", 0x1F)
    LoadChrToIndex("chr/ch02500.itc", 0x20)
    SetChrPos(0x0, 0, -33620, 0, 0)
    SetChrPos(0x1, 0, -33620, 0, 0)
    SetChrPos(0x2, 0, -33620, 0, 0)
    SetChrPos(0x3, 0, -33620, 0, 0)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -800, 0, -16900, 180)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, 800, 0, -16900, 180)
    SetChrChipByIndex(0x1C, 0x1F)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -1800, 0, -19500, 45)
    SetChrChipByIndex(0x1D, 0x20)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, 3700, 0, -17500, 270)
    SetChrChipByIndex(0xC, 0x1E)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x4)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, 0, 0, -17000, 180)
    ClearMapObjFlags(0x16, 0x4)
    OP_68(0, 900, -19000, 0)
    MoveCamera(140, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Return()

    # Function_94_104FA end

    SaveToFile()

Try(main)
