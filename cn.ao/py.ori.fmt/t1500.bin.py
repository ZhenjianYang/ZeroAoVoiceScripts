from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1500.bin",                # FileName
        "t1500",                    # MapName
        "t1500",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x1D,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1500",                  # 0
        "警备员托尼",             # 1
        "艾达护士",               # 2
        "勤杂工戴森",             # 3
        "赛兰德教授",             # 4
        "哈罗德",                 # 5
        "莉夏",                   # 6
        "比利",                   # 7
        "司机",                   # 8
        "塞茜尔",                 # 9
        "巴士",                   # 10
        "国防军士兵",             # 11
        "国防军士兵",             # 12
        "国防军士兵",             # 13
        "国防军士兵",             # 14
        "塞茜尔",                 # 15
        "芙兰",                   # 16
        "车",                     # 17
        "梅尔卡瓦九号机",         # 18
        "护士Ａ",                 # 19
        "护士Ｂ",                 # 20
        "实习医生Ａ",             # 21
        "实习医生Ｂ",             # 22
        "小孩子",                 # 23
        "大叔",                   # 24
        "老爷爷",                 # 25
        "老婆婆",                 # 26
        "探视者Ａ",               # 27
        "探视者Ｂ",               # 28
        "探视者Ｃ",               # 29
        "探视者Ｄ",               # 30
        "SE控制",                 # 31
        "bt1510",                 # 32
        "乌尔斯拉间道",           # 33
    ))

    ATBonus("ATBonus_7E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_8C0", 5, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C8", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 11, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 12, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_8A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_8A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_8AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_8B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_8B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 5, 5, 45)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_8E0", 0x0002, 255, 6, 45, 3, 3, 30, 0, "bt1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms41501.dat", "ms41401.dat", "ms41401.dat", "ms41501.dat", 0, 0, 0, 0, "MonsterBattlePostion_8C0", "MonsterBattlePostion_8A0", "ed7452", "ed7453", "ATBonus_7E0"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch28600.itc",                   # 00
        "chr/ch29800.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch44800.itc",                   # 03
        "chr/ch09300.itc",                   # 04
        "chr/ch03200.itc",                   # 05
        "chr/ch23600.itc",                   # 06
        "chr/ch28300.itc",                   # 07
        "chr/ch05300.itc",                   # 08
    ))

    DeclNpc(-47560,  0,       4000,    270,  261,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-23040,  -1000,   -25909,  0,    257,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-30000,  -1000,   -20299,  246,  389,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-21979,  -1000,   -26030,  180,  389,  0x0, 0,   3,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-48889,  0,       4000,    90,   389,  0x0, 0,   4,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-50020,  0,       -230,    90,   389,  0x0, 0,   5,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-52479,  0,       13199,   180,  385,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-54090,  0,       11979,   180,  389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-24200,  -1000,   -24709,  180,  389,  0x0, 0,   8,   0,   0,   0,   0,   95,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 21,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 27,  -42.0,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.0,                  -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 40,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 90,  -42.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.166666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 92,  -44.75,                0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.916666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 93,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 94,  -43.75,                0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.583333969116211,    -0.0,                  0.20000000298023224,   1.0])

    DeclActor(-58000,  0,       4000,    1500,    -58000,  1500,    4000,    0x007C, 0,  19, 0x0000)
    DeclActor(-16830,  -1000,   -27510,  1200,    -17180,  -2000,   -32770,  0x007C, 0,  20, 0x0000)
    DeclActor(-49410,  0,       16470,   1200,    -49410,  2000,    16470,   0x007C, 0,  18, 0x0000)
    DeclActor(-48000,  0,       17000,   1200,    -48000,  2000,    17000,   0x007C, 0,  18, 0x0000)
    DeclActor(-7880,   0,       6560,    1200,    -7880,   1500,    6560,    0x007C, 0,  98, 0x0000)
    DeclActor(-36860,  0,       14360,   1200,    -36860,  1500,    14360,   0x007C, 0,  99, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")

    ChipFrameInfo(2740, 0)                                       # 0

    ScpFunction((
        "Function_0_AB4",          # 00, 0
        "Function_1_B6C",          # 01, 1
        "Function_2_C24",          # 02, 2
        "Function_3_C85",          # 03, 3
        "Function_4_D00",          # 04, 4
        "Function_5_1432",         # 05, 5
        "Function_6_1757",         # 06, 6
        "Function_7_1817",         # 07, 7
        "Function_8_1944",         # 08, 8
        "Function_9_196B",         # 09, 9
        "Function_10_19FF",        # 0A, 10
        "Function_11_27D8",        # 0B, 11
        "Function_12_3189",        # 0C, 12
        "Function_13_36D9",        # 0D, 13
        "Function_14_383D",        # 0E, 14
        "Function_15_38CE",        # 0F, 15
        "Function_16_3999",        # 10, 16
        "Function_17_3BF6",        # 11, 17
        "Function_18_3C61",        # 12, 18
        "Function_19_3F8E",        # 13, 19
        "Function_20_3FC8",        # 14, 20
        "Function_21_4090",        # 15, 21
        "Function_22_4B8D",        # 16, 22
        "Function_23_4B9D",        # 17, 23
        "Function_24_4BB0",        # 18, 24
        "Function_25_4BC3",        # 19, 25
        "Function_26_4BD6",        # 1A, 26
        "Function_27_4BE9",        # 1B, 27
        "Function_28_53CF",        # 1C, 28
        "Function_29_54B3",        # 1D, 29
        "Function_30_556A",        # 1E, 30
        "Function_31_562A",        # 1F, 31
        "Function_32_56A6",        # 20, 32
        "Function_33_5715",        # 21, 33
        "Function_34_574F",        # 22, 34
        "Function_35_579E",        # 23, 35
        "Function_36_57D8",        # 24, 36
        "Function_37_5812",        # 25, 37
        "Function_38_5861",        # 26, 38
        "Function_39_589B",        # 27, 39
        "Function_40_58D5",        # 28, 40
        "Function_41_61DF",        # 29, 41
        "Function_42_62F8",        # 2A, 42
        "Function_43_6396",        # 2B, 43
        "Function_44_63C2",        # 2C, 44
        "Function_45_63CD",        # 2D, 45
        "Function_46_6A4E",        # 2E, 46
        "Function_47_6A70",        # 2F, 47
        "Function_48_6A95",        # 30, 48
        "Function_49_6ABA",        # 31, 49
        "Function_50_6AD2",        # 32, 50
        "Function_51_6AEA",        # 33, 51
        "Function_52_6B02",        # 34, 52
        "Function_53_6B1A",        # 35, 53
        "Function_54_8113",        # 36, 54
        "Function_55_8142",        # 37, 55
        "Function_56_8176",        # 38, 56
        "Function_57_8206",        # 39, 57
        "Function_58_8254",        # 3A, 58
        "Function_59_8268",        # 3B, 59
        "Function_60_82D9",        # 3C, 60
        "Function_61_82E8",        # 3D, 61
        "Function_62_8371",        # 3E, 62
        "Function_63_8376",        # 3F, 63
        "Function_64_841C",        # 40, 64
        "Function_65_8421",        # 41, 65
        "Function_66_84A3",        # 42, 66
        "Function_67_854A",        # 43, 67
        "Function_68_85E1",        # 44, 68
        "Function_69_8606",        # 45, 69
        "Function_70_862B",        # 46, 70
        "Function_71_8676",        # 47, 71
        "Function_72_86D3",        # 48, 72
        "Function_73_870D",        # 49, 73
        "Function_74_871D",        # 4A, 74
        "Function_75_8730",        # 4B, 75
        "Function_76_8754",        # 4C, 76
        "Function_77_8778",        # 4D, 77
        "Function_78_879C",        # 4E, 78
        "Function_79_87C0",        # 4F, 79
        "Function_80_8CDF",        # 50, 80
        "Function_81_8D3A",        # 51, 81
        "Function_82_8D54",        # 52, 82
        "Function_83_8D71",        # 53, 83
        "Function_84_8D8E",        # 54, 84
        "Function_85_8DA8",        # 55, 85
        "Function_86_8DC5",        # 56, 86
        "Function_87_8E02",        # 57, 87
        "Function_88_8E03",        # 58, 88
        "Function_89_8E1E",        # 59, 89
        "Function_90_8E49",        # 5A, 90
        "Function_91_9986",        # 5B, 91
        "Function_92_9987",        # 5C, 92
        "Function_93_A1F4",        # 5D, 93
        "Function_94_A4CA",        # 5E, 94
        "Function_95_ACC3",        # 5F, 95
        "Function_96_B4D3",        # 60, 96
        "Function_97_BF7D",        # 61, 97
        "Function_98_BFFF",        # 62, 98
        "Function_99_C055",        # 63, 99
    ))


    def Function_0_AB4(): pass

    label("Function_0_AB4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_AF4"),
        (1, "loc_B00"),
        (2, "loc_B0C"),
        (3, "loc_B18"),
        (4, "loc_B24"),
        (5, "loc_B30"),
        (6, "loc_B3C"),
        (SWITCH_DEFAULT, "loc_B48"),
    )


    label("loc_AF4")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B00")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B0C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B18")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B24")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B30")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B3C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B48")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B54")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B6B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_B54")

    label("loc_B6B")

    Return()

    # Function_0_AB4 end

    def Function_1_B6C(): pass

    label("Function_1_B6C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_BAC"),
        (1, "loc_BB8"),
        (2, "loc_BC4"),
        (3, "loc_BD0"),
        (4, "loc_BDC"),
        (5, "loc_BE8"),
        (6, "loc_BF4"),
        (SWITCH_DEFAULT, "loc_C00"),
    )


    label("loc_BAC")

    OP_A0(0xFE, 450, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BB8")

    OP_A0(0xFE, 550, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BC4")

    OP_A0(0xFE, 600, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BD0")

    OP_A0(0xFE, 400, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BDC")

    OP_A0(0xFE, 650, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BE8")

    OP_A0(0xFE, 350, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_BF4")

    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C00")

    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C23")
    OP_A0(0xFE, 500, 0x0, 0xFB)
    Jump("loc_C0C")

    label("loc_C23")

    Return()

    # Function_1_B6C end

    def Function_2_C24(): pass

    label("Function_2_C24")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C84")
    OP_95(0xFE, -23040, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, -1000, -23250, 2000, 0x0)
    OP_95(0xFE, -23040, -1000, -23250, 2000, 0x0)
    Jump("Function_2_C24")

    label("loc_C84")

    Return()

    # Function_2_C24 end

    def Function_3_C85(): pass

    label("Function_3_C85")

    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CCC")
    ClearMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_CCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_CFF")
    ClearMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x7, 0x2000000)
    SetMapObjFlags(0x8, 0x2000000)
    SetMapObjFlags(0xA, 0x2000000)
    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)

    label("loc_CFF")

    Return()

    # Function_3_C85 end

    def Function_4_D00(): pass

    label("Function_4_D00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_D24")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x9, -20070, 0, -3580, 270)
    Jump("loc_E8E")

    label("loc_D24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_D38")
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_E8E")

    label("loc_D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_D4C")
    BeginChrThread(0x9, 0, 0, 2)
    Jump("loc_E8E")

    label("loc_D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_D65")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_E8E")

    label("loc_D65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_DC6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DA6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D9C")
    ClearChrFlags(0xE, 0x80)
    Jump("loc_DA1")

    label("loc_D9C")

    SetChrFlags(0x8, 0x80)

    label("loc_DA1")

    Jump("loc_DAB")

    label("loc_DA6")

    SetChrFlags(0x8, 0x10)

    label("loc_DAB")

    SetChrPos(0x9, -23040, -1000, -25910, 180)
    ClearChrFlags(0xA, 0x80)
    Jump("loc_E8E")

    label("loc_DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DD9")
    SetChrFlags(0x9, 0x80)
    Jump("loc_E8E")

    label("loc_DD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E03")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -36570, 3000, 16290, 90)
    Jump("loc_E8E")

    label("loc_E03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E26")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_E8E")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E49")
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x10)
    Jump("loc_E8E")

    label("loc_E49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E74")
    BeginChrThread(0x9, 0, 0, 2)
    ClearChrFlags(0xA, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6F")
    ClearChrFlags(0xF, 0x80)

    label("loc_E6F")

    Jump("loc_E8E")

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E8E")
    SetChrPos(0x9, -12330, -1000, -17370, 90)

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 2)), scpexpr(EXPR_END)), "loc_E9C")
    ClearChrFlags(0xD, 0x80)

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EB0")
    ClearScenarioFlags(0x22, 0)
    Event(0, 41)
    Jump("loc_EED")

    label("loc_EB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_EC7")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 45)
    Jump("loc_EED")

    label("loc_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_EDE")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x0, 0)
    Event(0, 53)
    Jump("loc_EED")

    label("loc_EDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_EED")
    ClearScenarioFlags(0x22, 3)
    Event(0, 79)

    label("loc_EED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1391")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A")
    SetScenarioFlags(0x38, 0)

    label("loc_F7A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F90")
    SetScenarioFlags(0x38, 1)

    label("loc_F90")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA6")
    SetScenarioFlags(0x38, 2)

    label("loc_FA6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBC")
    SetScenarioFlags(0x38, 3)

    label("loc_FBC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")
    SetScenarioFlags(0x38, 4)

    label("loc_FD2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    SetScenarioFlags(0x38, 5)

    label("loc_FE8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFE")
    SetScenarioFlags(0x38, 6)

    label("loc_FFE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1014")
    SetScenarioFlags(0x38, 7)

    label("loc_1014")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102A")
    SetScenarioFlags(0x39, 0)

    label("loc_102A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1040")
    SetScenarioFlags(0x39, 1)

    label("loc_1040")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1056")
    SetScenarioFlags(0x39, 2)

    label("loc_1056")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106C")
    SetScenarioFlags(0x39, 3)

    label("loc_106C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1082")
    SetScenarioFlags(0x39, 4)

    label("loc_1082")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1098")
    SetScenarioFlags(0x39, 5)

    label("loc_1098")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AE")
    SetScenarioFlags(0x39, 6)

    label("loc_10AE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C4")
    SetScenarioFlags(0x39, 7)

    label("loc_10C4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DA")
    SetScenarioFlags(0x3A, 0)

    label("loc_10DA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F0")
    SetScenarioFlags(0x3A, 1)

    label("loc_10F0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1106")
    SetScenarioFlags(0x3A, 2)

    label("loc_1106")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111C")
    SetScenarioFlags(0x3A, 3)

    label("loc_111C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1132")
    SetScenarioFlags(0x3A, 4)

    label("loc_1132")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1148")
    SetScenarioFlags(0x3A, 5)

    label("loc_1148")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_115E")
    SetScenarioFlags(0x3A, 6)

    label("loc_115E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1174")
    SetScenarioFlags(0x3A, 7)

    label("loc_1174")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118A")
    SetScenarioFlags(0x3B, 0)

    label("loc_118A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A0")
    SetScenarioFlags(0x3B, 1)

    label("loc_11A0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B6")
    SetScenarioFlags(0x3B, 2)

    label("loc_11B6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CC")
    SetScenarioFlags(0x3B, 3)

    label("loc_11CC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E2")
    SetScenarioFlags(0x3B, 4)

    label("loc_11E2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F8")
    SetScenarioFlags(0x3B, 5)

    label("loc_11F8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_120E")
    SetScenarioFlags(0x3B, 6)

    label("loc_120E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1224")
    SetScenarioFlags(0x3B, 7)

    label("loc_1224")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123A")
    SetScenarioFlags(0x3D, 5)

    label("loc_123A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1250")
    SetScenarioFlags(0x3D, 6)

    label("loc_1250")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1266")
    SetScenarioFlags(0x3D, 7)

    label("loc_1266")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A1")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1391")

    label("loc_12A1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C4")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1391")

    label("loc_12C4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12E7")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1391")

    label("loc_12E7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130A")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1391")

    label("loc_130A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132D")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1391")

    label("loc_132D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1350")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1391")

    label("loc_1350")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1391")

    label("loc_1373")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1391")
    SetScenarioFlags(0x3C, 7)

    label("loc_1391")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13A7")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2D, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BD")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_13BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13EF")
    SetChrPos(0x0, -50230, 0, 16410, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 9)

    label("loc_13EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1422")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1422")
    SetChrPos(0x0, -48000, 0, 17000, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_1422")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_1431")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 8)

    label("loc_1431")

    Return()

    # Function_4_D00 end

    def Function_5_1432(): pass

    label("Function_5_1432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_144C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_145E")

    label("loc_144C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_145E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x233), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_145E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 1)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6F, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1484")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1484")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_149C")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_149C")

    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14B4")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_14B4")

    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14DF")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_14DF")

    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    ModifyEventFlags(0, 6, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_151B")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1516")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1516")
    ModifyEventFlags(1, 6, 0x80)

    label("loc_1516")

    Jump("loc_154C")

    label("loc_151B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_154C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 2)), scpexpr(EXPR_END)), "loc_1537")
    ModifyEventFlags(1, 5, 0x80)
    Jump("loc_154C")

    label("loc_1537")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_154C")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_154C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_15D0")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_15D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_15E7")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    Jump("loc_15E7")

    label("loc_15E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_15F5")
    Jump("loc_1697")

    label("loc_15F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_162F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_162A")
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFrame(0xE, "light", 0x0, 0x1)
    SetMapObjFlags(0xE, 0x1000)

    label("loc_162A")

    Jump("loc_1697")

    label("loc_162F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_163D")
    Jump("loc_1697")

    label("loc_163D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_164B")
    Jump("loc_1697")

    label("loc_164B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1659")
    Jump("loc_1697")

    label("loc_1659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_166D")
    ClearMapObjFlags(0xB, 0x4)
    Jump("loc_1697")

    label("loc_166D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_168E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1689")
    ClearMapObjFlags(0xA, 0x4)

    label("loc_1689")

    Jump("loc_1697")

    label("loc_168E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1697")

    label("loc_1697")

    MiniGame(0x2F, 0x2, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x11, 0x80)
    SetMapObjFlags(0x7, 0x4)
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -17180, -2000, -32770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1734")
    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)

    label("loc_1734")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_174C")
    OP_1B(0x0, 0x0, 0x61)

    label("loc_174C")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_5_1432 end

    def Function_6_1757(): pass

    label("Function_6_1757")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "克洛斯贝尔市南出口\x01",          # 0
            "岔口停靠站（河滩附近）\x01",      # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17EF")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_180F")

    label("loc_17EF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_180F")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_180F")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1757 end

    def Function_7_1817(): pass

    label("Function_7_1817")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1940")
    Fade(500)
    OP_68(-59000, 1000, 2200, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -56600, 0, 3800, 180)
    SetChrPos(0x1, -56600, 0, 4900, 180)
    SetChrPos(0x2, -56600, 0, 6000, 180)
    SetChrPos(0x3, -56600, 0, 7200, 180)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x11, 0x80)
    OP_78(0x7, 0x11)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x11, -71000, 0, 500, 90)
    OP_D5(0x11, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_18F7():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_18F7)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x11, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_1940")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_1817 end

    def Function_8_1944(): pass

    label("Function_8_1944")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56560, 0, 4080, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_8_1944 end

    def Function_9_196B(): pass

    label("Function_9_196B")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_19C6")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19BB")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_19C1")

    label("loc_19BB")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_19C1")

    Jump("loc_19EA")

    label("loc_19C6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19E4")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_19EA")

    label("loc_19E4")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_19EA")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_196B end

    def Function_10_19FF(): pass

    label("Function_10_19FF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B2B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABC")

    #C0002
    ChrTalk(
        0x8,
        (
            "喂喂……那棵闪烁着蓝白色光芒的\x01",
            "巨大树木到底是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "竟然会突然出现那种东西……\x01",
            "这也太莫名其妙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "总、总之，也只有打起\x01",
            "十二分的精神进行警备了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B26")

    label("loc_1ABC")


    #C0005
    ChrTalk(
        0x8,
        (
            "竟然会突然出现那么巨大的树……\x01",
            "这也太莫名其妙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "总、总之，也只有打起\x01",
            "十二分的精神进行警备了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B26")

    Jump("loc_27D4")

    label("loc_1B2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1C39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBB")

    #C0007
    ChrTalk(
        0x8,
        (
            "受独立无效宣言的影响，\x01",
            "国防军似乎一片混乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "虽然他们现在还在负责\x01",
            "急救车和巴士的护卫，\x01",
            "但还是令人不放心啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C34")

    label("loc_1BBB")


    #C0009
    ChrTalk(
        0x8,
        (
            "受独立无效宣言的影响，\x01",
            "国防军似乎一片混乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "如果没有了国防军的护卫，\x01",
            "急救车就无法正常往来了，\x01",
            "真是令人不安啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C34")

    Jump("loc_27D4")

    label("loc_1C39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1DA3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D1B")

    #C0011
    ChrTalk(
        0x8,
        (
            "如果没有了国防军的护卫，\x01",
            "急救车就无法正常往来了，\x01",
            "老实说，情况真是不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "郊外出现了『幻兽』，\x01",
            "国防军还下达了禁行令……\x01",
            "这两个问题真是很严重。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "至少也该多分点人手\x01",
            "在郊外担当护卫员啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1D9E")

    label("loc_1D1B")


    #C0014
    ChrTalk(
        0x8,
        (
            "如果没有了国防军的护卫，\x01",
            "急救车就无法正常往来了，\x01",
            "老实说，情况真是不妙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "国防军至少也该多分点人手\x01",
            "在郊外担当护卫员啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D9E")

    Jump("loc_27D4")

    label("loc_1DA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6A")

    #C0016
    ChrTalk(
        0x8,
        (
            "国防军的那些家伙之前还在\x01",
            "搜索从拘留所逃亡的犯人……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "但不知为什么，一下子就\x01",
            "全都撤退了。\x01",
            "这到底是怎么回事呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "……算啦，不管了，\x01",
            "我得继续做好自己的警备工作。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EFB")

    label("loc_1E6A")


    #C0019
    ChrTalk(
        0x8,
        (
            "国防军的那些家伙之前还在\x01",
            "搜索从拘留所逃亡的犯人……\x01",
            "但不知为什么，一下子就全都撤退了。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "……算啦，不管了，\x01",
            "我得继续做好自己的警备工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFB")

    Jump("loc_27D4")

    label("loc_1F00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_21F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_20C8")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2044")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCD")

    #C0021
    ChrTalk(
        0x8,
        (
            "哎呀呀，竟然\x01",
            "骗取医疗物资，\x01",
            "世上还真有这种坏人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "虽说总算把物资\x01",
            "取回来了……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "但在大家齐心努力的\x01",
            "时候听到这种事情，\x01",
            "实在是有些难过。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_203F")

    label("loc_1FCD")


    #C0024
    ChrTalk(
        0x8,
        (
            "哎呀呀，竟然\x01",
            "骗取医疗物资，\x01",
            "世上还真有这种坏人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "在大家齐心努力的\x01",
            "时候听到这种事情，\x01",
            "实在是有些难过。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_203F")

    Jump("loc_20C3")

    label("loc_2044")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_20C3")

    #C0026
    ChrTalk(
        0x8,
        (
            "哎呀呀，竟然\x01",
            "骗取医疗物资，\x01",
            "世上还真有这种坏人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "大家正处于困境，\x01",
            "他却做出这种事，\x01",
            "真是太差劲了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20C3")

    label("loc_20C3")

    Jump("loc_21EB")

    label("loc_20C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2184")

    #C0028
    ChrTalk(
        0x8,
        (
            "好奇怪啊，\x01",
            "按理说，早就\x01",
            "应该到了……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    #C0029
    ChrTalk(
        0x8,
        (
            "哦，失礼了，\x01",
            "欢迎来到乌尔斯拉医科大学。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "要探病的话，\x01",
            "请到病房楼一层的\x01",
            "大厅办理手续。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_21EB")

    label("loc_2184")


    #C0031
    ChrTalk(
        0x8,
        (
            "由于之前的袭击事件，\x01",
            "大量伤员被送到了医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "医院里的医生们\x01",
            "都忙得不可开交，\x01",
            "我也得继续努力。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21EB")

    Jump("loc_27D4")

    label("loc_21F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_233A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22BE")

    #C0033
    ChrTalk(
        0x8,
        (
            "呀，今天下雨啊。\x01",
            "在这种时候警备可真不轻松。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "话说回来，\x01",
            "昨天来了好多急救车，\x01",
            "真是不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "听说发生了相当严重的事故，\x01",
            "不过没有出现死难者，\x01",
            "也可以算是不幸中的万幸了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2335")

    label("loc_22BE")


    #C0036
    ChrTalk(
        0x8,
        (
            "昨天来了好多急救车，\x01",
            "真是不得了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "听说发生了相当严重的事故，\x01",
            "不过没有出现死难者，\x01",
            "也可以算是不幸中的万幸了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2335")

    Jump("loc_27D4")

    label("loc_233A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_23A3")

    #C0038
    ChrTalk(
        0x8,
        (
            "游击士们似乎\x01",
            "正在各处调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "有传闻说，\x01",
            "郊外出现了大型魔兽……\x01",
            "我也得小心一些啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27D4")

    label("loc_23A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_249F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2453")

    #C0040
    ChrTalk(
        0x8,
        "哟，欢迎来到乌尔斯拉医科大学。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "赛兰德教授刚才\x01",
            "往休息处那边走去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "教授最近经常去\x01",
            "那个地方静静地站着。\x01",
            "……她大概有许多事需要思考吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_249A")

    label("loc_2453")


    #C0043
    ChrTalk(
        0x8,
        (
            "赛兰德教授最近\x01",
            "经常去休息处。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "……她大概有许多事需要思考吧。\x02",
    )

    CloseMessageWindow()

    label("loc_249A")

    Jump("loc_27D4")

    label("loc_249F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2506")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BA")
    Call(0, 15)
    Jump("loc_2501")

    label("loc_24BA")


    #C0045
    ChrTalk(
        0x8,
        (
            "啊，那次\x01",
            "好像是因为\x01",
            "希伦写错了……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "这次应该\x01",
            "不会再有问题了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2501")

    Jump("loc_27D4")

    label("loc_2506")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2691")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2581")

    #C0047
    ChrTalk(
        0x8,
        (
            "阿尔伯特大公刚刚已经\x01",
            "乘高级轿车离开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "呼～紧张死了……\x01",
            "幸好在迎接时\x01",
            "没有出什么问题。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_268C")

    label("loc_2581")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2625")

    #C0049
    ChrTalk(
        0x8,
        (
            "雷米菲利亚的阿尔伯特大公\x01",
            "来医院视察了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "呼～虽然事先得到了通知，\x01",
            "但到了迎接的时候，\x01",
            "真是紧张死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "在他离开之前，\x01",
            "可千万不能失礼。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_268C")

    label("loc_2625")


    #C0052
    ChrTalk(
        0x8,
        (
            "呼～虽然事先得到了通知，\x01",
            "但到了迎接的时候，\x01",
            "真是紧张死了。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "在大公离开之前，\x01",
            "可千万不能失礼。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_268C")

    Jump("loc_27D4")

    label("loc_2691")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_27D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2765")

    #C0054
    ChrTalk(
        0x8,
        (
            "呀，你们好。\x01",
            "这里是圣乌尔斯拉医科大学医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "因为名字太长了，所以很多人都把它简称为\x01",
            "『乌尔斯拉医院』或『乌尔斯拉医科大学』。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "哦，如果要诊疗或探病，\x01",
            "请到里面的接待处登记。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27D4")

    label("loc_2765")


    #C0057
    ChrTalk(
        0x8,
        (
            "我在教团事件中\x01",
            "受的枪伤，被这里\x01",
            "的医生完全治好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "乌尔斯拉医科大学引以为傲的\x01",
            "医疗技术真是太伟大了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27D4")

    TalkEnd(0xFE)
    Return()

    # Function_10_19FF end

    def Function_11_27D8(): pass

    label("Function_11_27D8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2961")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28CC")

    #C0059
    ChrTalk(
        0x9,
        (
            "国防军拨了一些人手，\x01",
            "来护卫往来于郊外的\x01",
            "急救车和巴士。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "在市里那起骚动中受伤的人们，\x01",
            "还有前一段时间无法来医院的人们，\x01",
            "现在基本都可以过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "游击士艾欧莉娅小姐\x01",
            "也来帮忙了，\x01",
            "医院目前总算是恢复正常了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_295C")

    label("loc_28CC")


    #C0062
    ChrTalk(
        0x9,
        (
            "游击士艾欧莉娅小姐\x01",
            "也来帮忙了，\x01",
            "医院目前总算是恢复正常了。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "可是，那棵巨型大树的出现，\x01",
            "又令患者们的不安开始蔓延。\x01",
            "我也得竭尽全力才是。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_295C")

    Jump("loc_3185")

    label("loc_2961")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2A52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29FF")

    #C0064
    ChrTalk(
        0x9,
        (
            "住院的患者们\x01",
            "似乎非常担心市内的家人。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "但现在很难与市里取得联络，\x01",
            "就算着急也没办法……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "必须要尽力安抚\x01",
            "患者们的情绪。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2A4D")

    label("loc_29FF")


    #C0067
    ChrTalk(
        0x9,
        (
            "住院的患者们\x01",
            "似乎非常担心市内的家人。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "必须要尽力安抚\x01",
            "患者们的情绪。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4D")

    Jump("loc_3185")

    label("loc_2A52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2B30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADD")

    #C0069
    ChrTalk(
        0x9,
        (
            "比起国防军和总统，\x01",
            "我更尊重你们的信念。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        "你们一定要平安归来啊。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "还有，不要让塞茜尔前辈\x01",
            "太担心哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2B2B")

    label("loc_2ADD")


    #C0072
    ChrTalk(
        0x9,
        (
            "警察弟弟，\x01",
            "你们一定要平安归来啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "还有，不要让塞茜尔前辈\x01",
            "太担心哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B2B")

    Jump("loc_3185")

    label("loc_2B30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2C03")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BD3")

    #C0074
    ChrTalk(
        0x9,
        (
            "警察弟弟，听说你们\x01",
            "与国防军展开了斗争……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "……不，\x01",
            "没什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "无论发生什么事，\x01",
            "我们都站在你们这边。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00002F……谢谢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2BFE")

    label("loc_2BD3")


    #C0078
    ChrTalk(
        0x9,
        (
            "无论发生什么事，\x01",
            "我们都站在你们这边。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFE")

    Jump("loc_3185")

    label("loc_2C03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2C78")

    #C0079
    ChrTalk(
        0x9,
        (
            "由于那起事件，\x01",
            "大量伤员被送到了医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "治疗速度很难跟上……\x01",
            "等待接受手术的人\x01",
            "已经排起了长队。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3185")

    label("loc_2C78")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2C86")
    Jump("loc_3185")

    label("loc_2C86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2D64")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D2B")

    #C0081
    ChrTalk(
        0x9,
        (
            "小滴好像对这次的手术\x01",
            "相当乐观。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "那孩子自己都没有\x01",
            "放弃，我们就更\x01",
            "不能有悲观的想法。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "……嗯，我们也应该\x01",
            "充满信心，继续努力。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D5F")

    label("loc_2D2B")


    #C0084
    ChrTalk(
        0x9,
        (
            "我们也必须要坚信\x01",
            "小滴可以痊愈，\x01",
            "继续努力工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D5F")

    Jump("loc_3185")

    label("loc_2D64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DF7")

    #C0085
    ChrTalk(
        0x9,
        (
            "赛兰德教授能完成\x01",
            "那种程度的手术，\x01",
            "已经很厉害了……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "但是……\x01",
            "凭现在的医疗技术，果然还是\x01",
            "无法治好小滴的眼睛吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2E35")

    label("loc_2DF7")


    #C0087
    ChrTalk(
        0x9,
        (
            "小滴……\x01",
            "凭现在的医疗技术，果然还是\x01",
            "无法治好她的眼睛吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E35")

    Jump("loc_3185")

    label("loc_2E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2F12")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EAF")

    #C0088
    ChrTalk(
        0x9,
        (
            "今天终于要召开\x01",
            "通商会议的正式会议了。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "究竟会有什么样的进展呢？\x01",
            "我可得密切关注。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2F0D")

    label("loc_2EAF")


    #C0090
    ChrTalk(
        0x9,
        (
            "菲莉亚和兰好像\x01",
            "都没什么兴趣……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "但通商会议究竟会有什么样的进展呢？\x01",
            "我可得密切关注。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F0D")

    Jump("loc_3185")

    label("loc_2F12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FCA")

    #C0092
    ChrTalk(
        0x9,
        (
            "阿尔伯特大公刚才还\x01",
            "主动和我打招呼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "他贵为一国元首，\x01",
            "我本以为会是个\x01",
            "架子很大的人……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "但他竟然会向我这个\x01",
            "普通护士打招呼，\x01",
            "真是意外地随和呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3012")

    label("loc_2FCA")


    #C0095
    ChrTalk(
        0x9,
        (
            "阿尔伯特大公\x01",
            "真是意外地随和呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "呵呵，\x01",
            "让人一下就有了亲切感。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3012")

    Jump("loc_3185")

    label("loc_3017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3185")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3136")

    #C0097
    ChrTalk(
        0x9,
        (
            "哎呀，是兰迪先生和警察弟弟，\x01",
            "好久不见啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00006F（『警察弟弟』吗……\x01",
            "  这称呼真是固定下来了呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00302F哈哈，艾达，\x01",
            "你们都还好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "嗯，兰和菲莉亚\x01",
            "也都是老样子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "看来你们增添了\x01",
            "新成员……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "以后有机会的话，\x01",
            "我们还要一起去玩哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 4)
    Jump("loc_3185")

    label("loc_3136")


    #C0103
    ChrTalk(
        0x9,
        "呵呵，能再见到你们，好开心哦。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "以后有机会的话，\x01",
            "我们还要一起去玩哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3185")

    TalkEnd(0xFE)
    Return()

    # Function_11_27D8 end

    def Function_12_3189(): pass

    label("Function_12_3189")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_319A")
    Jump("loc_36D5")

    label("loc_319A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_31A8")
    Jump("loc_36D5")

    label("loc_31A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_31B6")
    Jump("loc_36D5")

    label("loc_31B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_32F8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_327D")

    #C0105
    ChrTalk(
        0xA,
        (
            "医院所使用的用品，\x01",
            "原本大多都是从商人\x01",
            "哈罗德先生那里订购的……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "但现在几乎都要靠\x01",
            "国防军的配给。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "虽然用品的质量让人难以恭维，\x01",
            "但在如今这种状况下，也没办法了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_32F3")

    label("loc_327D")


    #C0108
    ChrTalk(
        0xA,
        (
            "医院所使用的用品，\x01",
            "如今基本都要靠国防军配给。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "虽然用品的质量让人难以恭维，\x01",
            "但在如今这种状况下，也没办法了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32F3")

    Jump("loc_36D5")

    label("loc_32F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3432")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C4")

    #C0110
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔市竟然\x01",
            "遭受了袭击，真是\x01",
            "耸人听闻的事件呀……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "已经过了将近一个星期，\x01",
            "但那时的震惊依然挥之不去。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "虽说复兴工作有所进展，\x01",
            "但克洛斯贝尔真的能\x01",
            "恢复原状吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_342D")

    label("loc_33C4")


    #C0113
    ChrTalk(
        0xA,
        (
            "虽说复兴工作有所进展，\x01",
            "但袭击事件肯定给\x01",
            "大家造成了很大的打击。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "克洛斯贝尔真的能\x01",
            "恢复原状吗……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_342D")

    Jump("loc_36D5")

    label("loc_3432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3440")
    Jump("loc_36D5")

    label("loc_3440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_349D")

    #C0115
    ChrTalk(
        0xA,
        (
            "我在这个集装箱里\x01",
            "翻出来好多\x01",
            "驱邪用的人偶。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "……为什么\x01",
            "会有这种东西？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36D5")

    label("loc_349D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3593")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_354A")

    #C0117
    ChrTalk(
        0xA,
        (
            "听说市里到处都在谈论着\x01",
            "独立提案的事。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "身为克洛斯贝尔居民，\x01",
            "从某种意义上来说，\x01",
            "这也算是一个期待已久的愿望了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "我也非常\x01",
            "赞成独立。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_358E")

    label("loc_354A")


    #C0120
    ChrTalk(
        0xA,
        (
            "我也非常\x01",
            "赞成独立。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "等到居民投票的时候，\x01",
            "可不能忘了参加。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358E")

    Jump("loc_36D5")

    label("loc_3593")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_35A1")
    Jump("loc_36D5")

    label("loc_35A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_36CC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3659")

    #C0122
    ChrTalk(
        0xA,
        (
            "据说雷米菲利亚公国的\x01",
            "大公家族对医疗领域\x01",
            "相当重视。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        (
            "你应该也听说过医疗发达国家\x01",
            "雷米菲利亚吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "唔，要是住在那样\x01",
            "的国家，似乎就不用\x01",
            "担心生病了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_36C7")

    label("loc_3659")


    #C0125
    ChrTalk(
        0xA,
        (
            "据说雷米菲利亚公国的\x01",
            "大公家族对医疗领域\x01",
            "相当重视。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "唔，要是住在那样\x01",
            "的国家，似乎就不用\x01",
            "担心生病了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C7")

    Jump("loc_36D5")

    label("loc_36CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_36D5")

    label("loc_36D5")

    TalkEnd(0xFE)
    Return()

    # Function_12_3189 end

    def Function_13_36D9(): pass

    label("Function_13_36D9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37ED")

    #C0127
    ChrTalk(
        0xB,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#00005F赛兰德教授……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 500)

    #C0129
    ChrTalk(
        0xB,
        "……哦，是你们啊。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "抱歉，我现在很忙，\x01",
            "能不能让我一个人静一静？\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#00108F（看来是在为小滴的\x01",
            "  手术而烦恼吧……）\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#00003F（嗯，听说她是\x01",
            "  主刀医师……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3839")

    label("loc_37ED")


    #C0133
    ChrTalk(
        0xB,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        (
            "#00003F（她似乎在思考问题，\x01",
            "  打扰人家可不好。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3839")

    TalkEnd(0xFE)
    Return()

    # Function_13_36D9 end

    def Function_14_383D(): pass

    label("Function_14_383D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3852")
    Call(0, 15)
    Jump("loc_38CA")

    label("loc_3852")


    #C0135
    ChrTalk(
        0xC,
        (
            "#03605F对了……\x01",
            "这次的床单数量\x01",
            "是三十条吧？\x02\x03",

            "#03600F以前有一次，需要五十条，\x01",
            "却在订单里写成了五百条，\x01",
            "为防万一……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38CA")

    TalkEnd(0xFE)
    Return()

    # Function_14_383D end

    def Function_15_38CE(): pass

    label("Function_15_38CE")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0136
    ChrTalk(
        0x8,
        (
            "呀，这不是哈罗德先生吗，\x01",
            "您今天来医院有事吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        (
            "#03600F嗯，我来送\x01",
            "医院订购的床单。\x02\x03",

            "现在正要交货呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "啊，既然如此，\x01",
            "我来帮您搬进去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xC,
        "#03609F哈哈，总是麻烦你呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_15_38CE end

    def Function_16_3999(): pass

    label("Function_16_3999")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3AC7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A5A")

    #C0140
    ChrTalk(
        0xFE,
        (
            "多亏你们，总算把医疗物资\x01",
            "平安送到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "竟然在这种非常时期趁火打劫，\x01",
            "真是个卑劣的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "好在你们已经把他抓住，\x01",
            "总算可以暂时安心了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3AC2")

    label("loc_3A5A")


    #C0143
    ChrTalk(
        0xFE,
        (
            "竟然在这种非常时期趁火打劫，\x01",
            "真是个卑劣的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "好在你们已经把他抓住，\x01",
            "总算可以暂时安心了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC2")

    Jump("loc_3BF2")

    label("loc_3AC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_3BF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B8C")

    #C0145
    ChrTalk(
        0xFE,
        (
            "可恶，在这种非常时期，\x01",
            "却没能把医疗物资顺利送到……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "……不，事情已经发生了，\x01",
            "再怎么发牢骚也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "你们几个也是一样，\x01",
            "赶快转换心情，投入到工作中吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3BF2")

    label("loc_3B8C")


    #C0148
    ChrTalk(
        0xFE,
        (
            "事情已经发生了，\x01",
            "再怎么发牢骚也无济于事。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "你们几个也是一样，\x01",
            "赶快转换心情，投入到工作中吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3BF2")

    TalkEnd(0xFE)
    Return()

    # Function_16_3999 end

    def Function_17_3BF6(): pass

    label("Function_17_3BF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3C5D")

    #C0150
    ChrTalk(
        0xF,
        (
            "这是接送阿尔伯特大公\x01",
            "用的高级轿车。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xF,
        (
            "有亚里欧斯先生\x01",
            "担任阁下的护卫，\x01",
            "我们很放心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C5D")

    TalkEnd(0xFE)
    Return()

    # Function_17_3BF6 end

    def Function_18_3C61(): pass

    label("Function_18_3C61")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C93")
    SetScenarioFlags(0x31, 2)

    label("loc_3C93")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_3CD3")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3CC8")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_3CCE")

    label("loc_3CC8")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_3CCE")

    Jump("loc_3CD9")

    label("loc_3CD3")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_3CD9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3F80")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_3D4A")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3D2A"),
        (SWITCH_DEFAULT, "loc_3D3B"),
    )


    label("loc_3D2A")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_3D45")

    label("loc_3D3B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3D45")

    Jump("loc_3F7B")

    label("loc_3D4A")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3D7A")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_3D7A")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3DA4"),
        (1, "loc_3EA8"),
        (2, "loc_3F39"),
        (SWITCH_DEFAULT, "loc_3F71"),
    )


    label("loc_3DA4")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3DD5")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_3DE5")

    label("loc_3DD5")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_3DE5")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E3B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3E3B")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E5E")
    Sound(461, 0, 100, 0)

    label("loc_3E5E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3E7E")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_3E8E")

    label("loc_3E7E")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_3E8E")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_3CD9")

    label("loc_3EA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_3F1A")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_3EDD")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_3EF5")

    label("loc_3EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3EF0")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_3EF5")

    label("loc_3EF0")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_3EF5")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F34")

    label("loc_3F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3F2A")
    OP_AF(0xFB)
    Jump("loc_3F34")

    label("loc_3F2A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F34")

    Jump("loc_3F7B")

    label("loc_3F39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F52")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3F6C")

    label("loc_3F52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_3F62")
    OP_AF(0xFB)
    Jump("loc_3F6C")

    label("loc_3F62")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F6C")

    Jump("loc_3F7B")

    label("loc_3F71")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3F7B")

    Jump("loc_3CD9")

    label("loc_3F80")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_18_3C61 end

    def Function_19_3F8E(): pass

    label("Function_19_3F8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_3FC4")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力巴士已经停运了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_3FC4")

    Call(0, 6)
    Return()

    # Function_19_3F8E end

    def Function_20_3FC8(): pass

    label("Function_20_3FC8")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0153
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(-17220, 0, -31290, 1500)
    MoveCamera(60, 36, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(22000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0154
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_408B")
    OP_E2(0x2)
    MiniGame(0x6, 0x11, 0xFFFFBFBE, 0xFFFFFC18, 0xFFFF9A5C, 0xB4, 0xFFFFBCE4, 0xFFFFF830, 0xFFFF7FFE)

    label("loc_408B")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_3FC8 end

    def Function_21_4090(): pass

    label("Function_21_4090")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    SetChrPos(0x101, -47420, 0, 290, 270)
    SetChrPos(0x102, -46710, 0, -820, 270)
    SetChrPos(0x104, -46010, 0, 1050, 270)
    SetChrPos(0x105, -44880, 0, -1000, 270)
    SetChrPos(0x109, -44460, 0, 420, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(-45000, 1000, 0, 0)
    MoveCamera(33, 22, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21160, 0)
    OP_68(-54310, 1000, 260, 4500)
    BeginChrThread(0x101, 0, 0, 22)
    BeginChrThread(0x102, 0, 0, 23)
    BeginChrThread(0x104, 0, 0, 24)
    BeginChrThread(0x105, 0, 0, 25)
    BeginChrThread(0x109, 0, 0, 26)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(3000)
    Sound(803, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x101, 0)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0155
    ChrTalk(
        0x101,
        "#00005F#5P哦……?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_4213():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4213)

    #C0156
    ChrTalk(
        0x102,
        "#00105F#12P是其它部门打来的吗？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    #Sound(2084, 255, 100, 0)    #voice#Lloyd
    SetMessageWindowPos(90, 130, -1, -1)

    #A0157
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F#30W您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("嘹亮的声音")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦呵呵……\x01",
            "是我啦，是我。\x02\x03",

            "猜到人家是谁了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0159
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00012F米歇尔先生……\x01",
            "那个……有什么事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦呵呵，竟然一下就猜出来了，\x01",
            "挺机灵的嘛。\x02\x03",

            "还是说，这是因为爱呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0161
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006F不，只是除了米歇尔先生之外，\x01",
            "没有别人会这样说话而已。\x02\x03",

            "#00000F莫非事情和去协会\x01",
            "打扰的琪雅有关？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哦，你说那孩子啊。\x02\x03",

            "她带着小滴\x01",
            "去港湾区玩了。\x02\x03",

            "那条警犬……是叫蔡特吧？\x01",
            "它也一起去了，\x01",
            "我想应该没问题的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0163
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00002F嗯，有蔡特同行，\x01",
            "应该就不用担心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哎呀，果然是这样吗？\x02\x03",

            "久闻大名，\x01",
            "它确实威风凛凛呢。\x02\x03",

            "不愧是传说中的\x01",
            "『神狼』啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0165
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00004F哈哈……我想它终究不是\x01",
            "传说中的那匹狼吧。\x02\x03",

            "#00005F啊，您是特意通知\x01",
            "我们这件事的吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "不，接下来才是正题。\x02\x03",

            "其实是亚里欧斯想和你们\x01",
            "交换情报啦。\x02\x03",

            "他大概会在傍晚时分回来，\x01",
            "你们能不能抽点时间过来？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0167
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00000F傍晚吗……\x01",
            "应该没问题。\x02\x03",

            "说到交换情报，\x01",
            "当然是关于通商会议的吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "也有这方面的内容……\x01",
            "但主要还是关于『黑月』和『赤色星座』的情报。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0169
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F……明白了。\x02\x03",

            "#00001F我们把手头的事情处理完以后，\x01",
            "就会前去拜访的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("米歇尔的声音")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "嗯，等你们哦。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)

    #C0171
    ChrTalk(
        0x102,
        (
            "#00100F#12P好像是游击士协会的\x01",
            "米歇尔先生啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        "#00305F#11P出什么事了吗？\x02",
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
    OP_93(0x101, 0x5A, 0x1F4)

    #C0173
    ChrTalk(
        0x101,
        "#00006F#5P没有，只是要和我们交换情报。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德向其他成员\x01",
            "说明了米歇尔的提议。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0175
    ChrTalk(
        0x104,
        (
            "#00303F#11P『黑月』和『赤色星座』吗……\x02\x03",

            "#00301F的确，亚里欧斯那大叔对自治州外的\x01",
            "情报应该也了解得很清楚。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x105,
        (
            "#10304F#11P呵呵，说不定正是及时雨呢。\x02\x03",

            "#10300F那么，我们现在就\x01",
            "回克洛斯贝尔市吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#00000F#5P不，亚里欧斯先生\x01",
            "要到傍晚才能回去。\x02\x03",

            "在那之前，我们先把\x01",
            "自己的工作完成吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4A99")

    #C0178
    ChrTalk(
        0x102,
        (
            "#00104F#12P虽说已经收集到了不少\x01",
            "有关『赤色星座』的情报……\x02\x03",

            "#00102F但我们难得有了导力车，\x01",
            "再四处转转也不错。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4B0B")

    label("loc_4A99")


    #C0179
    ChrTalk(
        0x102,
        (
            "#00103F#12P目前还没有收集到多少\x01",
            "有关『赤色星座』的情报……\x02\x03",

            "#00100F我们难得有了导力车，\x01",
            "还是再四处转转为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B0B")


    #C0180
    ChrTalk(
        0x109,
        (
            "#10100F#11P好，把手头的事情办完之后，\x01",
            "我们就去东街的协会吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -55000, 0, -250, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 2)
    OP_29(0xA3, 0x1, 0x6)
    ModifyEventFlags(0, 0, 0x80)
    OP_24(0x323)
    EventEnd(0x5)
    Return()

    # Function_21_4090 end

    def Function_22_4B8D(): pass

    label("Function_22_4B8D")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_4B8D end

    def Function_23_4B9D(): pass

    label("Function_23_4B9D")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_4B9D end

    def Function_24_4BB0(): pass

    label("Function_24_4BB0")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_4BB0 end

    def Function_25_4BC3(): pass

    label("Function_25_4BC3")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_4BC3 end

    def Function_26_4BD6(): pass

    label("Function_26_4BD6")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_4BD6 end

    def Function_27_4BE9(): pass

    label("Function_27_4BE9")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch29700.itc", 0x1E)
    LoadChrToIndex("chr/ch29900.itc", 0x20)
    LoadChrToIndex("chr/ch29400.itc", 0x21)
    LoadChrToIndex("chr/ch32800.itc", 0x22)
    LoadChrToIndex("chr/ch23000.itc", 0x23)
    LoadChrToIndex("chr/ch21000.itc", 0x24)
    LoadChrToIndex("chr/ch20000.itc", 0x25)
    LoadChrToIndex("chr/ch23300.itc", 0x26)
    LoadChrToIndex("chr/ch20400.itc", 0x27)
    LoadChrToIndex("chr/ch21200.itc", 0x28)
    LoadChrToIndex("chr/ch20900.itc", 0x29)
    LoadChrToIndex("chr/ch20500.itc", 0x2A)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x21)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x22)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x23)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x24)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x25)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x26)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x27)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x28)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x29)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x2A)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetMapObjFlags(0x1, 0x1000)
    SetMapObjFlags(0x2, 0x1000)
    OP_68(-18000, 6000, 1300, 0)
    MoveCamera(55, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(33000, 0)
    OP_68(-18000, 1000, 1300, 10000)
    MoveCamera(45, 25, 0, 10000)
    SetCameraDistance(35000, 10000)
    SetChrPos(0x1A, -5000, 1000, -1750, 270)
    OP_A7(0x1A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1B, 5000, 1000, 1750, 270)
    OP_A7(0x1B, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1C, -24000, 0, 14000, 180)
    OP_A7(0x1C, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x1D, -24000, 0, -7000, 180)
    SetChrPos(0x1E, -16500, 0, -500, 90)
    SetChrPos(0x1F, -17000, 0, 500, 90)
    SetChrPos(0x20, -22000, 0, 0, 90)
    SetChrPos(0x21, -25500, 0, -300, 90)
    SetChrPos(0x22, -34000, 0, 700, 90)
    SetChrPos(0x23, -38000, 0, -500, 90)
    SetChrPos(0x24, -37500, 0, 500, 90)
    SetChrPos(0x25, -40000, 0, -750, 90)
    BeginChrThread(0x1A, 1, 0, 28)
    BeginChrThread(0x1C, 1, 0, 30)
    BeginChrThread(0x1E, 1, 0, 32)
    BeginChrThread(0x1F, 1, 0, 33)
    BeginChrThread(0x20, 1, 0, 34)
    BeginChrThread(0x21, 1, 0, 35)
    BeginChrThread(0x22, 1, 0, 36)
    BeginChrThread(0x23, 1, 0, 37)
    BeginChrThread(0x24, 1, 0, 38)
    BeginChrThread(0x25, 1, 0, 39)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0x1A, 0x1)
    EndChrThread(0x1B, 0x1)
    EndChrThread(0x1C, 0x1)
    EndChrThread(0x1D, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    OP_64(0x1A)
    OP_64(0x1B)
    OP_64(0x1C)
    OP_64(0x1D)
    OP_71(0x1, 0x5, 0x5, 0x0, 0x8)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_71(0x2, 0xA, 0xA, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrPos(0x101, -34900, 0, -950, 90)
    SetChrPos(0x102, -34900, 0, 450, 90)
    SetChrPos(0x103, -36500, 0, -1700, 90)
    SetChrPos(0x104, -36500, 0, 1200, 90)
    SetChrPos(0x109, -38100, 0, -1150, 90)
    SetChrPos(0x105, -38100, 0, 650, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-35310, 1100, -350, 0)
    MoveCamera(38, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    OP_68(-36310, 1100, -350, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0181
    ChrTalk(
        0x103,
        (
            "#00208F#6P前来探视的人果然\x01",
            "比往常多呢……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5054():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5054)
    Sleep(150)

    def lambda_5064():
        OP_93(0xFE, 0x10F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5064)
    Sleep(100)

    def lambda_5074():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5074)
    Sleep(50)

    def lambda_5084():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5084)
    Sleep(50)

    def lambda_5094():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5094)
    Sleep(50)

    def lambda_50A4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_50A4)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)

    #C0182
    ChrTalk(
        0x102,
        (
            "#00106F#11P嗯，光是市内，\x01",
            "就有很多人身负重伤……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00008F#11P……连多诺邦警督\x01",
            "和伊莉娅小姐都住院了。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x109,
        (
            "#10106F#6P是的……听说他们两人\x01",
            "都还处于昏迷状态。\x02\x03",

            "#10108F多诺邦警督……\x01",
            "似乎是为了保护芙兰他们才……\x02\x03",

            "芙兰这么快就能痊愈，\x01",
            "也是多亏了警督。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        "#00006F#11P是吗……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        (
            "#00306F#5P那个豪爽的大叔……\x01",
            "真是了不起啊。\x02\x03",

            "#00308F如果可以，真想去\x01",
            "探望他们一下……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_5275")

    #C0187
    ChrTalk(
        0x102,
        (
            "#00103F#11P是呀……\x01",
            "修利今天\x01",
            "好像也来了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_528E")

    label("loc_5275")


    #C0188
    ChrTalk(
        0x102,
        "#00103F#11P是呀……\x02",
    )

    CloseMessageWindow()

    label("loc_528E")


    def lambda_5293():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_5293)
    Sleep(250)

    #C0189
    ChrTalk(
        0x105,
        (
            "#10300F#5P对了，\x01",
            "你妹妹的病房是哪间？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x109,
        (
            "#10105F#6P啊，嗯……是３０１。\x02\x03",

            "#10100F在进去探视之前，\x01",
            "最好先去接待处打声招呼。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#00000F#11P明白了，我们走吧。\x02\x03",

            "#00003F（……塞茜尔姐姐应该\x01",
            "  也相当忙碌吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    OP_D7(0x24)
    OP_D7(0x25)
    OP_D7(0x26)
    OP_D7(0x27)
    OP_D7(0x28)
    OP_D7(0x29)
    OP_D7(0x2A)
    SetChrPos(0x0, -38500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x180, 5)
    OP_29(0xAC, 0x1, 0x2)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_27_4BE9 end

    def Function_28_53CF(): pass

    label("Function_28_53CF")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_53EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_53EB)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -9000, 4000, 0x0)
    Sleep(500)
    BeginChrThread(0x1D, 1, 0, 31)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1750, 4000, 0x0)

    def lambda_547D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_547D)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_28_53CF end

    def Function_29_54B3(): pass

    label("Function_29_54B3")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_54CF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_54CF)
    OP_95(0xFE, -22000, 0, 1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 11000, 4000, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)

    def lambda_5531():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5531)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_29_54B3 end

    def Function_30_556A(): pass

    label("Function_30_556A")

    Sleep(1000)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_559E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_559E)
    OP_95(0xFE, -24000, 0, 3500, 4000, 0x0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_95(0xFE, -22000, 0, 1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, 1500, 4000, 0x0)

    def lambda_55F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_55F7)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0x1B, 1, 0, 29)
    Return()

    # Function_30_556A end

    def Function_31_562A(): pass

    label("Function_31_562A")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -24000, 0, -3500, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1500, 4000, 0x0)

    def lambda_5682():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5682)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_31_562A end

    def Function_32_56A6(): pass

    label("Function_32_56A6")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x960, 0x0)
    OP_93(0xFE, 0x10E, 0x3E8)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x960, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_56F4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_56F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_32_56A6 end

    def Function_33_5715(): pass

    label("Function_33_5715")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0x6D6, 0x0)

    def lambda_572E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_572E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x6D6, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_33_5715 end

    def Function_34_574F(): pass

    label("Function_34_574F")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x3E8, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_577D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_577D)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_34_574F end

    def Function_35_579E(): pass

    label("Function_35_579E")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x6F54, 0x3E8, 0x0)

    def lambda_57B7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_57B7)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_35_579E end

    def Function_36_57D8(): pass

    label("Function_36_57D8")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA0, 0x5DC, 0x0)

    def lambda_57F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_57F1)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x5DC, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_36_57D8 end

    def Function_37_5812(): pass

    label("Function_37_5812")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x578, 0x0)

    def lambda_582B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_582B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x578, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_5812 end

    def Function_38_5861(): pass

    label("Function_38_5861")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x44C, 0x0)

    def lambda_587A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_587A)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x44C, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_5861 end

    def Function_39_589B(): pass

    label("Function_39_589B")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0xA028, 0x44C, 0x0)

    def lambda_58B4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_58B4)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_589B end

    def Function_40_58D5(): pass

    label("Function_40_58D5")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-46690, 1000, -40, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19720, 0)
    SetChrPos(0x101, -45000, 0, -700, 270)
    SetChrPos(0x102, -45000, 0, 700, 270)
    SetChrPos(0x103, -43500, 0, -700, 270)
    SetChrPos(0x104, -43500, 0, 700, 270)
    SetChrPos(0x109, -42000, 0, -700, 270)
    SetChrPos(0x105, -42000, 0, 700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_59D7():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59D7)
    Sleep(100)

    def lambda_59EF():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_59EF)
    Sleep(50)

    def lambda_5A07():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A07)
    Sleep(50)

    def lambda_5A1F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A1F)
    Sleep(50)

    def lambda_5A37():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_5A37)
    Sleep(50)

    def lambda_5A4F():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5A4F)
    OP_68(-48920, 1000, -570, 2700)
    SetCameraDistance(19720, 2700)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_5AA9():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5AA9)
    Sleep(300)

    def lambda_5AB9():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5AB9)
    Sleep(300)

    def lambda_5AC9():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_5AC9)
    Sleep(300)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0192
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年的声音")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "啊，接通了……\x02\x03",

            "你们现在在哪里？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0194
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00003F我说……\x01",
            "在这种时候，应该先报上自己的\x01",
            "名字吧？这可是基本礼仪。\x02\x03",

            "#00000F我们在乌尔斯拉医院……\x01",
            "怎么了？约纳。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "我记得你们从今天开始\x01",
            "就恢复正常业务了吧？\x02\x03",

            "所以想问问你们，\x01",
            "能不能接受我的委托～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0196
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00006F哎，你不要随便偷窥\x01",
            "警察局的数据库啊……\x02\x03",

            "#00001F另外，我们\x01",
            "还很忙……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哼哼，之前帮你们\x01",
            "搜索失踪游击士的\x01",
            "又是谁呢？\x02\x03",

            "你们说过要还我人情的吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0198
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00013F这……\x02\x03",

            "#00006F……没办法。\x01",
            "虽然不是任何委托都能接受，\x01",
            "不过就先听听你有什么事吧。\x02\x03",

            "#00000F要去哪里找你？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0199
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "那就来港湾区的\x01",
            "灯塔前吧。\x02\x03",

            "我在那里等你们¤\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0200
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005F灯塔？\x01",
            "为什么要去那种地方……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哼哼，来了就知道了。\x02\x03",

            "等你们哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(813, 0, 70, 0)
    Sleep(300)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0202
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00011F#2P啊……真是的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(300)

    #C0203
    ChrTalk(
        0x103,
        (
            "#00211F#11P约纳又提什么\x01",
            "任性的要求了吗？\x02",
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
    Sleep(150)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0204
    ChrTalk(
        0x101,
        "#00012F#6P啊，嗯……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "向大家说明了被叫往港湾区\x01",
            "码头灯塔前的事情。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0206
    ChrTalk(
        0x104,
        (
            "#00305F#5P啊？\x01",
            "为什么要去那种地方……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x105,
        (
            "#10300F#11P说到港湾区的灯塔，\x01",
            "离遭到爆破的『黑月』\x01",
            "事务所挺近的呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#00103F#5P在搜寻林小姐她们的时候，\x01",
            "我们确实接受过他的协助……\x02\x03",

            "#00100F只是去了解一下情况，\x01",
            "应该没关系吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        (
            "#10100F#11P等我们把工作处理完之后，\x01",
            "就过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#00000F#6P嗯，就这么办吧。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x103,
        (
            "#00206F#11P他都没问我们的时间是否方便，\x01",
            "就擅自决定了下来。\x02\x03",

            "#00211F让他等等也是应该的。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x104,
        "#00309F#5P哈哈，那倒也是。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -51000, 0, -700, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x181, 2)
    OP_29(0xAC, 0x1, 0x7)
    ModifyEventFlags(0, 2, 0x80)
    OP_24(0x323)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_40_58D5 end

    def Function_41_61DF(): pass

    label("Function_41_61DF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    Call(0, 42)
    Call(0, 43)
    Call(0, 44)
    OP_68(-55000, 800, -300, 0)
    MoveCamera(71, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(32200, 0)
    FadeToBright(1000, 0)
    OP_68(-52000, 800, -300, 4000)
    MoveCamera(71, 19, 0, 4000)
    OP_6E(500, 4000)
    SetCameraDistance(26800, 4000)
    OP_0D()
    OP_6F(0x79)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0213
    AnonymousTalk(
        0x101,
        "#00013F（国防军的部队……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0214
    AnonymousTalk(
        0x105,
        (
            "#10401F（正在警备中吗……？\x01",
            "  我们来的时机真不巧啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r1540", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_41_61DF end

    def Function_42_62F8(): pass

    label("Function_42_62F8")

    LoadChrToIndex("apl/ch51616.itc", 0x1E)
    LoadChrToIndex("apl/ch51617.itc", 0x1F)
    SetChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x12, 0x1E)
    SetChrSubChip(0x12, 0x0)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x1F)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x1F)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x12, -50960, 0, 750, 225)
    SetChrPos(0x13, -53240, 0, 680, 135)
    SetChrPos(0x14, -53040, 0, -1550, 43)
    SetChrPos(0x15, -51030, 0, -1630, 315)
    Return()

    # Function_42_62F8 end

    def Function_43_6396(): pass

    label("Function_43_6396")

    OP_74(0xD, 0x1E)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark00", 0x0, 0x1)
    Return()

    # Function_43_6396 end

    def Function_44_63C2(): pass

    label("Function_44_63C2")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_44_63C2 end

    def Function_45_63CD(): pass

    label("Function_45_63CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00051.itc", 0x21)
    LoadChrToIndex("chr/ch03150.itc", 0x22)
    LoadChrToIndex("chr/ch03151.itc", 0x23)
    LoadChrToIndex("chr/ch02750.itc", 0x24)
    LoadChrToIndex("chr/ch02751.itc", 0x25)
    LoadChrToIndex("chr/ch41450.itc", 0x26)
    LoadChrToIndex("chr/ch41451.itc", 0x27)
    LoadChrToIndex("chr/ch41550.itc", 0x28)
    LoadChrToIndex("chr/ch41551.itc", 0x29)
    Call(0, 42)
    Call(0, 43)
    Call(0, 44)
    SetChrPos(0x101, -67340, 0, -1250, 90)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x105, -67880, 0, 500, 90)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x107, -69900, 0, -550, 90)
    SetChrChipByIndex(0x107, 0x25)
    SetChrSubChip(0x107, 0x0)
    PlayBGM("ed7561", 0)
    OP_68(-52000, 2200, -300, 0)
    MoveCamera(71, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24150, 0)
    FadeToBright(1000, 0)
    OP_68(-52000, 1200, -300, 3000)
    MoveCamera(71, 24, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(23000, 3000)
    OP_0D()
    OP_6F(0x79)

    #C0215
    ChrTalk(
        0x12,
        "#5P唉，好闲啊。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x12,
        (
            "#5P在这种地方进行警备，\x01",
            "真是太无聊了。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x13,
        "#6P不要发牢骚。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x13,
        (
            "#6P那个支援科的班宁斯\x01",
            "还在逃亡中呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(100)

    #C0219
    ChrTalk(
        0x12,
        (
            "#5P哼，区区一个搜查官\x01",
            "又能有什么作为。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x12,
        (
            "#5P他大概早就\x01",
            "逃到外国去了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x14,
        (
            "#12P可是，听说他带着一头\x01",
            "很可怕的怪物……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x14,
        (
            "#12P据说第四连队有人被\x01",
            "吃掉了，是真的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x14, 500)
    Sleep(100)

    #C0223
    ChrTalk(
        0x12,
        "#5P哈哈，那只是谣传而已吧。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x12,
        (
            "#5P比起那些，难得的机会，\x01",
            "真想亲眼看看伊莉娅啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x12,
        "#5P我记得她还在住院吧？\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x15,
        "#11P嗯，应该是的。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x15,
        (
            "#11P真希望她能早日恢复，\x01",
            "重返舞台啊。\x02",
        )
    )

    CloseMessageWindow()

    #N0228
    NpcTalk(
        0x101,
        "罗伊德的声音",
        "#11P关于这一点，我也有同感。\x02",
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-59000, 800, -300, 1500)
    MoveCamera(36, 25, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(20500, 1500)

    def lambda_67A1():
        OP_93(0x12, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_67A1)
    Sleep(50)

    def lambda_67B1():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_67B1)
    Sleep(50)

    def lambda_67C1():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_67C1)
    Sleep(50)

    def lambda_67D1():
        OP_93(0x15, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_67D1)
    Sleep(50)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    Sleep(1000)
    BeginChrThread(0x101, 0, 0, 46)
    BeginChrThread(0x105, 0, 0, 47)
    BeginChrThread(0x107, 0, 0, 48)
    Sleep(1000)
    OP_68(-55500, 800, -300, 1300)
    MoveCamera(36, 25, 0, 1300)
    OP_6E(500, 1300)
    SetCameraDistance(20500, 1300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0229
    ChrTalk(
        0x12,
        "#11P罗伊德·班宁斯！？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x13,
        "#11P呜，竟然真的出现了！\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    Sleep(150)
    SetChrChipByIndex(0x13, 0x28)
    SetChrSubChip(0x13, 0x0)
    Sleep(150)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x12, 0x26)
    SetChrSubChip(0x12, 0x0)
    Sleep(150)
    SetChrChipByIndex(0x15, 0x28)
    SetChrSubChip(0x15, 0x0)
    Sleep(150)

    #C0231
    ChrTalk(
        0x107,
        (
            "#01203F#6P#3C哎呀呀，\x01",
            "竟然说我是怪物，真是失礼啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x105,
        (
            "#10402F#6P呵呵，看到你原本的姿态，\x01",
            "也难怪人家会那样说啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#00003F#6P我并不想做无谓的战斗。\x02\x03",

            "#00007F但是，你们若要阻挠，\x01",
            "我也只能毫不留情地打倒你们了！\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x14,
        "#11P太嚣张了……！\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x13,
        (
            "#11P他们势单力薄！\x01",
            "一口气压制住！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x12,
        "#11P明白！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetCameraDistance(19000, 500)
    BeginChrThread(0x12, 0, 0, 49)
    BeginChrThread(0x13, 0, 0, 50)
    BeginChrThread(0x14, 0, 0, 51)
    BeginChrThread(0x15, 0, 0, 52)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    SetScenarioFlags(0x22, 2)
    Battle("BattleInfo_8E0", 0x30200011, 0x0, 0x0, 0x24, 0xFF)
    FadeToDark(0, 0, -1)
    ClearScenarioFlags(0x22, 2)
    Call(0, 53)
    Return()

    # Function_45_63CD end

    def Function_46_6A4E(): pass

    label("Function_46_6A4E")

    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_46_6A4E end

    def Function_47_6A70(): pass

    label("Function_47_6A70")

    Sleep(50)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_47_6A70 end

    def Function_48_6A95(): pass

    label("Function_48_6A95")

    Sleep(100)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_48_6A95 end

    def Function_49_6ABA(): pass

    label("Function_49_6ABA")

    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_49_6ABA end

    def Function_50_6AD2(): pass

    label("Function_50_6AD2")

    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_50_6AD2 end

    def Function_51_6AEA(): pass

    label("Function_51_6AEA")

    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_51_6AEA end

    def Function_52_6B02(): pass

    label("Function_52_6B02")

    SetChrChipByIndex(0x15, 0x29)
    SetChrSubChip(0x15, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_52_6B02 end

    def Function_53_6B1A(): pass

    label("Function_53_6B1A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(2724)
    SoundLoad(2725)
    SoundLoad(2686)
    SoundLoad(2687)
    SoundLoad(2688)
    SoundLoad(2689)
    SoundLoad(2690)
    SoundLoad(2691)
    SoundLoad(2692)
    SoundLoad(2693)
    SoundLoad(2866)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00203.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu06400.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01300.itp")
    AddParty(0x2, 0xFF, 0xFF)
    OP_32(0x2, 0x0, 0x52)
    OP_32(0x2, 0x5, 0x64)
    OP_42(0x2, 0x419, 0xFF)
    OP_42(0x2, 0x5ED, 0xFF)
    OP_42(0x2, 0x651, 0xFF)
    OP_38(0x2, 0x81, 0x2)
    OP_38(0x2, 0x82, 0x2)
    OP_38(0x2, 0x83, 0x2)
    OP_38(0x2, 0x86, 0x2)
    OP_42(0x2, 0xAF, 0x1)
    OP_42(0x2, 0x66, 0x2)
    OP_42(0x2, 0x7A, 0x3)
    OP_42(0x2, 0xA2, 0x6)
    ClearScenarioFlags(0x20, 3)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    LoadChrToIndex("chr/ch05300.itc", 0x20)
    LoadChrToIndex("chr/ch08500.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch03150.itc", 0x23)
    LoadChrToIndex("chr/ch02750.itc", 0x24)
    LoadChrToIndex("chr/ch41453.itc", 0x25)
    LoadChrToIndex("chr/ch41553.itc", 0x26)
    LoadChrToIndex("apl/ch51700.itc", 0x27)
    LoadChrToIndex("apl/ch51701.itc", 0x28)
    LoadEffect(0x0, "event/ev17027.eff")
    LoadEffect(0x3, "event/ev17004.eff")
    LoadEffect(0x4, "event/ev17005.eff")
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x23)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x24)
    SetChrSubChip(0x107, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrPos(0x101, -55340, 0, -1250, 90)
    SetChrPos(0x105, -55880, 0, 500, 90)
    SetChrPos(0x107, -57900, 0, -550, 90)
    SetChrPos(0x103, -44000, 0, 150, 270)
    SetChrPos(0x16, -44000, 0, -1200, 270)
    SetChrPos(0x17, -44000, 0, 0, 270)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x16, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x2)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x26)
    SetChrSubChip(0x13, 0x2)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x25)
    SetChrSubChip(0x14, 0x2)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x26)
    SetChrSubChip(0x15, 0x2)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x12, -50370, 0, 640, 270)
    SetChrPos(0x13, -52240, 0, 580, 270)
    SetChrPos(0x14, -52040, 0, -1450, 270)
    SetChrPos(0x15, -50440, 0, -1520, 270)
    SetChrChipByIndex(0x16, 0x20)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    Call(0, 43)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x18, -52000, 0, 4000, 268)
    OP_78(0xD, 0x18)
    Call(0, 44)
    OP_68(-54300, 800, -300, 0)
    MoveCamera(36, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0237
    ChrTalk(
        0x14,
        "#40W#11P……呜……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x13,
        "#40W#11P好、好强……\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    Sleep(100)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    Sleep(300)

    #C0239
    ChrTalk(
        0x105,
        "#10404F#5P好，该我出场了。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-54200, 800, 860, 1200)
    MoveCamera(36, 25, 0, 1200)
    OP_6E(500, 1200)
    SetCameraDistance(20500, 1200)

    def lambda_6EF3():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6EF3)
    OP_9B(0x0, 0x105, 0x0, 0x190, 0x3E8, 0x0)
    Sleep(300)
    BeginChrThread(0x105, 0, 0, 54)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(500)

    #C0240
    ChrTalk(
        0x101,
        "#00005F#12P（星杯徽章……？）\x02",
    )

    CloseMessageWindow()
    PlayBGM("ed7304", 0)
    SetCameraDistance(20000, 20000)
    Sleep(1000)
    #Sound(2866, 255, 50, 0)    #voice#Lazy

    #C0241
    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10403F#30W#5P#40A闪耀于吾之深渊的\x01",
            "苍金刻印啊……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x105, 0, 0, 56)
    WaitChrThread(0x105, 0)

    #C0242
    ChrTalk(
        0x105,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#10401F#30W#5P#51A连结识之银耀，\x01",
            "赐予汝等虚伪之记忆吧。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 59)
    Sleep(800)

    #C0243
    ChrTalk(
        0x13,
        "#50W#11P#2S…………啊。\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0244
    ChrTalk(
        0x14,
        "#50W#11P#2S…………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0245
    ChrTalk(
        0x101,
        "#00011F#12P（这是……）\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x107,
        (
            "#01203F#3C#6P（唔，看来是教会传承的\x01",
            "  暗示类法术。）\x02\x03",

            "#01200F（另外，似乎还动用了某种\x01",
            "  不可思议的力量……）\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x105,
        (
            "#10403F#5P你们刚才发现\x01",
            "有大型幻兽接近。\x02\x03",

            "虽然拼尽全力将其击退，\x01",
            "但全员都负了伤，\x01",
            "只得暂时归队。\x02\x03",

            "#10401F你们并未见到班宁斯，\x01",
            "也没有发现他的任何行踪。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    BeginChrThread(0x13, 0, 0, 62)
    WaitChrThread(0x13, 0)
    Sleep(500)

    #C0248
    ChrTalk(
        0x13,
        "#50W#11P#2S……………………（不停点头）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    BeginChrThread(0x14, 0, 0, 64)
    WaitChrThread(0x14, 0)
    Sleep(500)

    #C0249
    ChrTalk(
        0x14,
        "#50W#11P#2S……没有发现班宁斯的任何行踪。\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_68(-53350, 800, 2710, 3000)
    OP_52(0x12, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x12, 0, 0, 61)
    BeginChrThread(0x13, 0, 0, 63)
    BeginChrThread(0x14, 0, 0, 65)
    BeginChrThread(0x15, 0, 0, 66)
    BeginChrThread(0x105, 0, 0, 55)

    def lambda_7241():

        label("loc_7241")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_7241")

    QueueWorkItem2(0x105, 3, lambda_7241)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x12, 0)
    WaitChrThread(0x13, 0)
    WaitChrThread(0x14, 0)
    WaitChrThread(0x15, 0)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    EndChrThread(0x105, 0x3)
    BeginChrThread(0x18, 0, 0, 67)
    BeginChrThread(0x101, 0, 0, 68)
    BeginChrThread(0x105, 0, 0, 69)
    BeginChrThread(0x107, 0, 0, 70)
    Sleep(1500)
    OP_68(-55360, 1500, -1970, 2000)
    MoveCamera(64, 37, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19550, 2000)
    OP_6F(0x79)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x107, 0x2)
    WaitChrThread(0x18, 0)
    SetMapObjFlags(0xD, 0x4)
    Sleep(300)

    #C0250
    ChrTalk(
        0x101,
        "#00006F#11P好、好厉害啊……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x107,
        (
            "#01203F#12P#3C如果是普通的暗示法术，\x01",
            "应该无法做出如此具体的操控。\x02\x03",

            "#01200F据我推测，应该是动用了\x01",
            "『圣痕』之力吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x105,
        (
            "#10404F#5P哈哈……\x01",
            "不愧是传说中的圣兽呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#00001F#11P『圣痕』……？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x105,
        (
            "#10406F#5P……嗯，说来话长，\x01",
            "牵扯到了我过去的一点心理阴影。\x02\x03",

            "#10408F这种暗示法术并不完美，\x01",
            "过两三天左右，效果就会解除。\x02\x03",

            "#10401F而军方也会有所警戒，\x01",
            "今后应该是不能再用了。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        "#00003F#11P是吗……明白了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)

    #N0256
    NpcTalk(
        0x103,
        "少女的声音",
        "#6P#2686V#30W#20A瓦吉先生、蔡特……？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_74F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_74F1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-44070, 400, 120, 2000)
    MoveCamera(76, 17, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19770, 2000)

    def lambda_7569():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7569)
    Sleep(50)

    def lambda_7579():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7579)
    Sleep(50)

    def lambda_7589():
        OP_93(0x107, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_7589)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0257
    AnonymousTalk(
        0x103,
        "#40W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0258
    ChrTalk(
        0x101,
        "#00005F#11P#12P#N缇欧……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0259
    ChrTalk(
        0x107,
        "#01200F#2P#3C#6P#N嗯，看来你平安无事啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0260
    ChrTalk(
        0x105,
        "#10404F#6P#N哎呀呀，总算放心了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, -53360, 0, -1680, 90)
    SetChrPos(0x105, -54080, 0, 130, 90)
    SetChrPos(0x107, -55410, 0, -1850, 90)
    SetChrSubChip(0x107, 0x5)
    TurnDirection(0x101, 0x103, 0)
    TurnDirection(0x103, 0x101, 0)
    OP_68(-49050, 1000, -1000, 0)
    MoveCamera(52, 11, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19080, 0)
    Fade(500)
    OP_0D()
    OP_9B(0x0, 0x101, 0x0, 0x190, 0x3E8, 0x0)

    #C0261
    ChrTalk(
        0x101,
        (
            "#00014F#6P太好了……！\x01",
            "听说你在医院，\x01",
            "还以为出了什么事……\x02\x03",

            "#00002F还好吧？\x01",
            "你没有受伤吧？\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0262
    ChrTalk(
        0x103,
        "#00213F#11P#2687V#50W#28A#2S……罗伊德……前辈………\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0263
    ChrTalk(
        0x103,
        "#00212F#11P#2688V#20W#4S#15A#4S罗伊德前辈……！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    BeginChrThread(0x103, 0, 0, 71)
    OP_68(-52640, 1200, -1760, 1800)
    MoveCamera(47, 20, 0, 1800)
    OP_6E(500, 1800)
    SetCameraDistance(17000, 1800)
    WaitChrThread(0x103, 0)

    def lambda_7877():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_7877)

    def lambda_7884():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_7884)
    OP_6F(0x79)
    SetCameraDistance(15500, 40000)

    #C0264
    ChrTalk(
        0x101,
        (
            "#00011F#6P呜啊……\x01",
            "（胸、胸甲……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0265
    ChrTalk(
        0x103,
        (
            "#00213F#11P#2689V#60W#25A你、你这段时间在哪里……！？\x02\x03",

            "#00215F#2690V#25A听说你被抓进了拘留所……！\x02\x03",

            "#00212F#2691V#87A……我、我还在导力网络上看到消息，\x01",
            "说你越狱逃亡，\x01",
            "正在被军方追捕……！\x02\x03",

            "#00213F#2692V#55A我、我……呜……\x01",
            "………一直都好担心…………！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0266
    ChrTalk(
        0x101,
        "#00008F#6P缇欧……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 0, 0, 78)
    BeginChrThread(0x103, 0, 0, 77)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    #C0267
    ChrTalk(
        0x101,
        (
            "#00006F#6P……抱歉，\x01",
            "让你担心了。\x02\x03",

            "#00002F不过，已经没事了。\x02\x03",

            "在蔡特和瓦吉的帮助下，\x01",
            "我已经回到克洛斯贝尔了……\x02\x03",

            "#00004F所以……你就放心吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #C0268
    ChrTalk(
        0x103,
        "#00215F#11P#2693V#40W#28A……呜呜……呜……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #N0269
    NpcTalk(
        0x17,
        "女孩的声音",
        (
            "#11P#2724V#30W#N#29A哇哇……\x01",
            "你们好亲热啊。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #N0270
    NpcTalk(
        0x16,
        "女性的声音",
        (
            "#11P#N#48A#30W呵呵，真不忍心\x01",
            "打扰你们……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-52280, 1200, -1700, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_7B8A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_7B8A)

    def lambda_7B9B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_7B9B)
    SetChrPos(0x16, -42500, 0, -1200, 270)
    SetChrPos(0x17, -42500, 0, 0, 270)
    BeginChrThread(0x17, 0, 0, 73)
    Sleep(100)
    BeginChrThread(0x16, 0, 0, 74)
    Sleep(1500)

    #C0271
    ChrTalk(
        0x101,
        (
            "#00002F#6P塞茜尔姐姐！\x01",
            "还有……芙兰！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x17, 0)
    WaitChrThread(0x16, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #A0272
    AnonymousTalk(
        0x17,
        (
            "#2725V#30W嘿嘿……\x01",
            "好久不见了，罗伊德警官！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xAA5)
    OP_C9(0x1, 0x80000000)
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

    #A0273
    AnonymousTalk(
        0x16,
        (
            "#30W你平安无事，真是太好了……\x02\x03",

            "……我好担心，罗伊德。\x02",
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

    #C0274
    ChrTalk(
        0x101,
        (
            "#00006F#6P抱歉……\x01",
            "让你们担心了。\x02\x03",

            "#00002F话说回来，芙兰，\x01",
            "你好像已经恢复健康了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x17,
        (
            "#06409F#11P嗯，伤势早就\x01",
            "痊愈了！\x02\x03",

            "#06406F但克洛斯贝尔已经\x01",
            "变成了现在这种样子，\x01",
            "我也没法回去工作……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#00006F#6P是吗……\x01",
            "不过，你能恢复真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(2277, 255, 80, 0)    #voice#Tio
    Sleep(300)
    BeginChrThread(0x103, 0, 0, 72)
    WaitChrThread(0x103, 0)
    Sleep(500)

    #C0277
    ChrTalk(
        0x103,
        (
            "#00215F#11P#30W……对了，\x01",
            "瓦吉先生这身打扮是……？\x02\x03",

            "#00216F还有蔡特，你这段时间到底跑到哪里去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x105,
        "#10404F#6P呵呵，一言难尽呢。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x107,
        (
            "#01200F#6P#3C总之，我先把至今为止的\x01",
            "事情经过做个说明吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0280
    ChrTalk(
        0x16,
        "#01305F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x17,
        "#06411F#11P刚、刚才那是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x103,
        "#00205F#11P嗯？怎么了？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        "#00012F#6P这个……你不觉得奇怪吗……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x105,
        (
            "#10402F#6P哈哈，莫非是因为\x01",
            "本来就语言相通，\x01",
            "所以没有察觉吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    Sleep(500)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0285
    ChrTalk(
        0x103,
        (
            "#00205F#11P#4S蔡、蔡特！？\x02\x03",

            "#00207F你怎么会\x01",
            "说人类的语言了！？\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 2000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    SetScenarioFlags(0x22, 0)
    NewScene("t1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_53_6B1A end

    def Function_54_8113(): pass

    label("Function_54_8113")

    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x1000)
    SetChrFlags(0xFE, 0x2)
    Sleep(100)
    Sound(531, 0, 50, 0)
    Sound(859, 0, 40, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Return()

    # Function_54_8113 end

    def Function_55_8142(): pass

    label("Function_55_8142")

    Sleep(4000)
    BeginChrThread(0x105, 1, 0, 58)
    WaitChrThread(0x105, 1)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    ClearChrFlags(0xFE, 0x2)
    Return()

    # Function_55_8142 end

    def Function_56_8176(): pass

    label("Function_56_8176")

    Sound(895, 0, 100, 0)
    Sound(222, 0, 30, 0)
    Sound(852, 2, 100, 0)
    PlayEffect(0x3, 0x1, 0x105, 0x5, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    PlayEffect(0x4, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(700)
    StopEffect(0x1, 0x2)
    BeginChrThread(0xFE, 2, 0, 57)
    Return()

    # Function_56_8176 end

    def Function_57_8206(): pass

    label("Function_57_8206")

    Sleep(300)

    label("loc_8209")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8253")
    PlayEffect(0x0, 0xFF, 0x105, 0x3, 0, 1050, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_8209")

    label("loc_8253")

    Return()

    # Function_57_8206 end

    def Function_58_8254(): pass

    label("Function_58_8254")

    EndChrThread(0xFE, 0x2)
    Sleep(300)
    StopEffect(0x2, 0x2)
    StopSound(852, 500, 90)
    Sleep(300)
    Return()

    # Function_58_8254 end

    def Function_59_8268(): pass

    label("Function_59_8268")


    def lambda_826D():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_826D)
    Sleep(200)

    def lambda_8289():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_8289)
    Sleep(200)

    def lambda_82A5():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_82A5)
    Sleep(200)

    def lambda_82C1():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_82C1)
    Sleep(200)
    Return()

    # Function_59_8268 end

    def Function_60_82D9(): pass

    label("Function_60_82D9")

    Sleep(250)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_60_82D9 end

    def Function_61_82E8(): pass

    label("Function_61_82E8")

    Sleep(900)
    SetChrSubChip(0x12, 0x1)
    Sleep(700)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x60E, 0x384, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_61_82E8 end

    def Function_62_8371(): pass

    label("Function_62_8371")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_62_8371 end

    def Function_63_8376(): pass

    label("Function_63_8376")

    Sleep(200)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x28A, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x64, 0x384, 0x0)
    Sound(464, 0, 100, 0)
    OP_71(0xD, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0xD)
    OP_9B(0x0, 0xFE, 0x0, 0x96, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_63_8376 end

    def Function_64_841C(): pass

    label("Function_64_841C")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_64_841C end

    def Function_65_8421(): pass

    label("Function_65_8421")

    Sleep(1200)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x9C4, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x2D, 0x2EE, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x15E, 0x384, 0x0)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
    Return()

    # Function_65_8421 end

    def Function_66_84A3(): pass

    label("Function_66_84A3")

    Sleep(1500)
    SetChrSubChip(0x15, 0x1)
    Sleep(700)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    BeginChrThread(0xFE, 1, 0, 1)
    OP_93(0xFE, 0x0, 0x12C)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA, 0x384, 0x1)
    OP_9B(0x0, 0xFE, 0x13B, 0x60E, 0x384, 0x0)
    OP_9B(0x0, 0xFE, 0x2D, 0xFA, 0x384, 0x1)
    BeginChrThread(0xFE, 3, 0, 60)
    OP_9C(0xFE, 0x0, 0x1F4, 0x3E8, 0x226, 0x1F4)

    def lambda_8521():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8521)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0xD, 0x1F, 0x3C, 0x1, 0x8)
    OP_79(0xD)
    Return()

    # Function_66_84A3 end

    def Function_67_854A(): pass

    label("Function_67_854A")

    Sound(465, 0, 100, 0)
    SetMapObjFrame(0xD, "light", 0x1, 0x1)
    Sleep(500)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x167, 0xFA, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x167, 0xFA, 0xBB8, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -53500, 0, 3700)
    OP_9F(0x1, -55000, 0, 2900)
    OP_9F(0x1, -57000, 0, 1600)
    OP_9F(0x1, -60000, 0, 500)
    OP_9F(0x1, -69000, 0, 0)
    OP_9F(0x2, 0xFE, 4500, 0x6)
    Return()

    # Function_67_854A end

    def Function_68_85E1(): pass

    label("Function_68_85E1")


    def lambda_85E6():

        label("loc_85E6")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_85E6")

    QueueWorkItem2(0xFE, 2, lambda_85E6)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x5A, 0x6D6, 0x7D0, 0x0)
    Return()

    # Function_68_85E1 end

    def Function_69_8606(): pass

    label("Function_69_8606")


    def lambda_860B():

        label("loc_860B")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_860B")

    QueueWorkItem2(0xFE, 2, lambda_860B)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x5A, 0x4E2, 0x3E8, 0x0)
    Return()

    # Function_69_8606 end

    def Function_70_862B(): pass

    label("Function_70_862B")

    Sleep(600)
    OP_9B(0x0, 0xFE, 0x5A, 0x1F4, 0x7D0, 0x1)
    OP_9D(0xFE, 0xFFFF259A, 0x0, 0xFFFFF7CC, 0x15E, 0x5DC)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)

    def lambda_8668():

        label("loc_8668")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_8668")

    QueueWorkItem2(0xFE, 2, lambda_8668)
    Return()

    # Function_70_862B end

    def Function_71_8676(): pass

    label("Function_71_8676")

    OP_9B(0x0, 0xFE, 0x0, 0x2198, 0x1770, 0x0)
    BeginChrThread(0xFE, 3, 0, 75)
    Sound(811, 0, 50, 0)
    Sound(898, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 76)

    def lambda_86A2():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_86A2)
    Sleep(100)

    def lambda_86BE():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_86BE)
    Return()

    # Function_71_8676 end

    def Function_72_86D3(): pass

    label("Function_72_86D3")

    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1000)
    Sound(812, 0, 100, 0)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x3E8, 0x0)
    Return()

    # Function_72_86D3 end

    def Function_73_870D(): pass

    label("Function_73_870D")

    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_73_870D end

    def Function_74_871D(): pass

    label("Function_74_871D")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_74_871D end

    def Function_75_8730(): pass

    label("Function_75_8730")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1005)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(300)
    Return()

    # Function_75_8730 end

    def Function_76_8754(): pass

    label("Function_76_8754")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x8)
    Sleep(100)
    SetChrSubChip(0xFE, 0x9)
    Sleep(100)
    SetChrSubChip(0xFE, 0xA)
    Sleep(300)
    Return()

    # Function_76_8754 end

    def Function_77_8778(): pass

    label("Function_77_8778")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x2)
    Sleep(150)
    SetChrSubChip(0xFE, 0x3)
    Sleep(150)
    SetChrSubChip(0xFE, 0x4)
    Sleep(450)
    Return()

    # Function_77_8778 end

    def Function_78_879C(): pass

    label("Function_78_879C")

    SetChrChipByIndex(0xFE, 0x28)
    SetChrFlags(0xFE, 0x2)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0xA)
    Sleep(150)
    SetChrSubChip(0xFE, 0xB)
    Sleep(150)
    SetChrSubChip(0xFE, 0xC)
    Sleep(450)
    Return()

    # Function_78_879C end

    def Function_79_87C0(): pass

    label("Function_79_87C0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    AddParty(0x6, 0xFF, 0xFF)
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    LoadChrToIndex("chr/ch06900.itc", 0x1F)
    LoadChrToIndex("chr/ch03154.itc", 0x20)
    LoadEffect(0x0, "battle/mgaria0.eff")
    SoundLoad(497)
    SetChrPos(0x101, -10000, 0, 750, 90)
    SetChrPos(0x103, -10200, 0, -850, 90)
    SetChrPos(0x105, -11550, 0, 1350, 90)
    SetChrPos(0x17, -11700, 0, -1450, 90)
    SetChrPos(0x107, -12050, 0, 100, 90)
    SetChrSubChip(0x107, 0x5)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -6000, 1000, 0, 270)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x19, 0x80)
    OP_78(0x11, 0x19)
    OP_93(0x19, 0xB4, 0x0)
    OP_68(-10000, 3000, 0, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(25000, 0)
    FadeToBright(1000, 0)
    OP_68(-10000, 1000, 0, 3000)
    MoveCamera(45, 23, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(25000, 3000)
    OP_6F(0x79)
    SetChrName("")

    #A0286
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "随后，罗伊德等人和蔡特会合……\x02\x03",

            "与塞茜尔告别后，离开了乌尔斯拉医院。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(27000, 5000)
    BeginChrThread(0x101, 0, 0, 81)
    BeginChrThread(0x103, 0, 0, 82)
    BeginChrThread(0x105, 0, 0, 83)
    BeginChrThread(0x107, 0, 0, 84)
    BeginChrThread(0x17, 0, 0, 85)
    BeginChrThread(0x16, 0, 0, 87)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    EndChrThread(0x101, 0x0)
    EndChrThread(0x103, 0x0)
    EndChrThread(0x105, 0x0)
    EndChrThread(0x107, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x16, 0x0)
    SetChrPos(0x105, -51000, 100, 17000, 90)
    SetChrPos(0x101, -51300, 0, 15600, 90)
    SetChrPos(0x103, -52380, 0, 17080, 90)
    SetChrPos(0x107, -51330, 0, 18780, 124)
    SetChrPos(0x17, -51810, 0, 14140, 51)
    SetChrSubChip(0x107, 0x5)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    OP_71(0x11, 0x65, 0xA0, 0x0, 0x20)
    SetMapObjFlags(0x9, 0x4)
    OP_68(-50250, 1000, 17000, 0)
    MoveCamera(48, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20150, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sound(357, 0, 50, 0)
    PlayEffect(0x0, 0x0, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_68(-49850, 1000, 17000, 18000)
    SetCameraDistance(15000, 18000)
    BeginChrThread(0x105, 3, 0, 88)
    BeginChrThread(0x19, 1, 0, 89)
    Sleep(500)
    Sound(935, 0, 100, 0)
    Sleep(1500)
    StopEffect(0x0, 0x2)
    SetChrName("")

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "回程时，瓦吉在医院门前\x01",
            "发现了七耀脉力场的『狭间』……\x02\x03",

            "在用『法阵』固定之后，\x01",
            "『梅尔卡瓦』前来迎接，\x01",
            "今后可以随时在此处降落了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x26, 1, 0, 80)
    Fade(500)
    OP_68(-49730, 1500, 16190, 0)
    MoveCamera(64, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(37770, 0)
    OP_68(-43790, 1000, 18370, 6000)
    MoveCamera(68, 48, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(60530, 6000)
    ClearMapObjFlags(0x11, 0x4)
    SetChrPos(0x19, -48000, 18250, 17000, 180)
    OP_D5(0x19, 0x0, 0x2BF20, 0x0, 0x0)
    BeginChrThread(0x19, 0, 0, 86)
    Sleep(4000)
    StopSound(497, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x19, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    StopBGM(0xFA0)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    Sound(814, 0, 100, 0)

    #A0288
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "由于缇欧和芙兰加入队伍，\x01",
            "可以在梅尔卡瓦内的终端上\x01",
            "接受通缉魔兽等支援请求了。\x02\x03",

            "船舱的终端能够自由使用，\x01",
            "请灵活运用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x22, 3)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_79_87C0 end

    def Function_80_8CDF(): pass

    label("Function_80_8CDF")

    Sound(497, 2, 10, 0)
    Sleep(50)
    OP_25(0x1F1, 0xF)
    Sleep(50)
    OP_25(0x1F1, 0x14)
    Sleep(50)
    OP_25(0x1F1, 0x19)
    Sleep(50)
    OP_25(0x1F1, 0x1E)
    Sleep(50)
    OP_25(0x1F1, 0x23)
    Sleep(50)
    OP_25(0x1F1, 0x28)
    Sleep(50)
    OP_25(0x1F1, 0x2D)
    Sleep(50)
    OP_25(0x1F1, 0x32)
    Sleep(50)
    OP_25(0x1F1, 0x37)
    Sleep(50)
    OP_25(0x1F1, 0x3C)
    Sleep(50)
    OP_25(0x1F1, 0x41)
    Sleep(50)
    OP_25(0x1F1, 0x46)
    Return()

    # Function_80_8CDF end

    def Function_81_8D3A(): pass

    label("Function_81_8D3A")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_81_8D3A end

    def Function_82_8D54(): pass

    label("Function_82_8D54")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(900)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_82_8D54 end

    def Function_83_8D71(): pass

    label("Function_83_8D71")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(800)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_83_8D71 end

    def Function_84_8D8E(): pass

    label("Function_84_8D8E")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_84_8D8E end

    def Function_85_8DA8(): pass

    label("Function_85_8DA8")

    Sleep(400)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_85_8DA8 end

    def Function_86_8DC5(): pass

    label("Function_86_8DC5")

    OP_96(0xFE, 0xFFFF4480, 0x251C, 0x4268, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2328, 0x4268, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2134, 0x4268, 0x3E8, 0x1)
    Return()

    # Function_86_8DC5 end

    def Function_87_8E02(): pass

    label("Function_87_8E02")

    Return()

    # Function_87_8E02 end

    def Function_88_8E03(): pass

    label("Function_88_8E03")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8E1D")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_88_8E03")

    label("loc_8E1D")

    Return()

    # Function_88_8E03 end

    def Function_89_8E1E(): pass

    label("Function_89_8E1E")

    SetMapObjFrame(0xF, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0xF, "Null_fream", 0x2, "loop")
    Return()

    # Function_89_8E1E end

    def Function_90_8E49(): pass

    label("Function_90_8E49")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    ClearChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrPos(0x16, -9000, 0, -500, 270)
    OP_68(-37710, 1000, 350, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19060, 0)
    SetChrPos(0x101, -41980, 0, 500, 90)
    SetChrPos(0x102, -42590, 0, -900, 90)
    SetChrPos(0x109, -42700, 0, 1300, 90)
    SetChrPos(0x105, -44040, 0, -1300, 90)
    SetChrPos(0x104, -43990, 0, 300, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01300.itp")
    OP_0D()
    OP_68(-34660, 1000, -430, 5000)

    def lambda_8F45():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F45)
    Sleep(50)

    def lambda_8F62():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8F62)
    Sleep(50)

    def lambda_8F7F():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_8F7F)
    Sleep(50)

    def lambda_8F9C():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_8F9C)
    Sleep(50)

    def lambda_8FB9():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8FB9)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Sleep(500)

    #N0289
    NpcTalk(
        0x16,
        "女性的声音",
        "……罗伊德……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0290
    ChrTalk(
        0x101,
        "#00002F啊……！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-9210, 1000, -500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19060, 0)
    OP_0D()
    Sleep(800)
    OP_68(-23280, 1000, -240, 5000)
    MoveCamera(44, 25, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(17390, 5000)

    def lambda_90EC():
        OP_95(0xFE, -21270, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_90EC)
    Sleep(50)

    def lambda_9109():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9109)
    Sleep(50)

    def lambda_9126():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9126)
    Sleep(50)

    def lambda_9143():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9143)
    Sleep(50)

    def lambda_9160():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9160)
    Sleep(50)

    def lambda_917D():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_917D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x16, 1)

    #C0291
    ChrTalk(
        0x101,
        (
            "#6P#00009F塞茜尔姐姐……\x01",
            "哈哈，突然就见面了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x16,
        (
            "#11P#01300F呵呵……欢迎回来，罗伊德。\x02\x03",

            "#01309F还有艾莉、兰迪\x01",
            "和诺艾尔……\x01",
            "大家都还好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        "#6P#00100F呵呵，久疏问候了。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        "#6P#00309F好久不见，塞茜尔小姐！\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x109,
        (
            "#5P#10109F呵呵，真是好久不见。\x02\x03",

            "#10100F上次和塞茜尔小姐见面，\x01",
            "还是在医院遇袭的\x01",
            "时候呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x16,
        "#11P#01309F呵呵……是呀。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        "#6P#10302F哦，这位就是传说中的姐姐吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0298
    ChrTalk(
        0x16,
        (
            "#11P#01305F哎呀，还有个没见过的孩子……\x02\x03",

            "#01300F莫非诺艾尔和你\x01",
            "就是传说中的新成员？\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，算是这样吧。\x02\x03",

            "#10302F我叫瓦吉·赫米斯菲亚，\x01",
            "今后请多多关照。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x16,
        (
            "#11P#01309F呵呵，彼此彼此。\x02\x03",

            "#01300F那么……我也做个\x01",
            "正式的自我介绍吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0301
    AnonymousTalk(
        0x16,
        (
            "嗯……\x01",
            "我是在乌尔斯拉医院工作的\x01",
            "护士塞茜尔·诺伊艾丝。\x02\x03",

            "呵呵，我可爱的弟弟罗伊德\x01",
            "就拜托各位照顾了。\x02",
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
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0302
    ChrTalk(
        0x101,
        (
            "#6P#00006F塞茜尔姐姐……\x01",
            "严格来说，我们并不是姐弟吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    #C0303
    ChrTalk(
        0x101,
        (
            "#6P#00000F嗯，那个……\x01",
            "这位是从我孩提时代起\x01",
            "就一直照顾我的姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x16,
        "#11P#01306F真是的，罗伊德，你害什么羞嘛。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)

    #C0305
    ChrTalk(
        0x101,
        "#6P#00012F我、我不是害羞啦。\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0x16, 0x13B, 0x1F4)
    Sleep(1000)
    OP_93(0x16, 0x10E, 0x1F4)
    Sleep(1000)

    #C0306
    ChrTalk(
        0x16,
        (
            "#11P#01304F嗯，话说回来……\x01",
            "瓦吉和诺艾尔\x01",
            "都很漂亮呢。\x02\x03",

            "#01300F罗伊德，你差不多\x01",
            "也该决定要\x01",
            "和谁交往了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x109,
        "#5P#10105F交、交往！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0308
    ChrTalk(
        0x101,
        (
            "#6P#00006F塞茜尔姐姐……我之前就说过了，\x01",
            "支援科又不是那种地方。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x16,
        (
            "#11P#01305F啊……也是，\x01",
            "我考虑得不够周全呢。\x02\x03",

            "#01303F小缇欧现在不在场，\x01",
            "谈论这些未免不公平。\x02\x03",

            "#01300F等小缇欧回来之后，\x01",
            "你再慢慢挑选伴侣……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#6P#00011F都、都说了……\x01",
            "唉！为什么会变成这样啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        (
            "#6P#00109F呵呵，不知为什么，\x01",
            "看到塞茜尔小姐，心情就平静下来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x104,
        "#6P#00309F哦哦，这种迟钝的性格还是没有变啊。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#11P#00006F你们也得考虑一下我有多辛苦啊……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x16,
        (
            "#11P#01304F呵呵……话说回来，\x01",
            "虽然并没有分别很久，\x01",
            "但感觉好怀念啊。\x02\x03",

            "#01300F刚好到了我的休息时间，\x01",
            "不如大家一起喝个茶吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#6P#00004F那么，机会难得……\x02\x03",

            "#00002F各位，我们就\x01",
            "恭敬不如从命吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x109,
        "#5P#10109F好的，算我一个！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1510", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_90_8E49 end

    def Function_91_9986(): pass

    label("Function_91_9986")

    Return()

    # Function_91_9986 end

    def Function_92_9987(): pass

    label("Function_92_9987")

    EventBegin(0x0)
    Fade(500)
    OP_68(-47260, 1700, -1110, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x106, -48500, 0, -230, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_9B99")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x102, -46300, 0, -1330, 90)
    SetChrPos(0x103, -46300, 0, 870, 90)
    SetChrPos(0x104, -48400, 0, 1030, 90)

    def lambda_9A1F():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9A1F)

    def lambda_9A39():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9A39)

    def lambda_9A53():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9A53)

    def lambda_9A6D():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9A6D)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9ABD")
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_9AA8():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9AA8)

    label("loc_9ABD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9AF8")
    SetChrPos(0x105, -48000, 0, -1070, 90)

    def lambda_9AE3():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9AE3)

    label("loc_9AF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B33")
    SetChrPos(0x10A, -48000, 0, -1070, 90)

    def lambda_9B1E():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_9B1E)

    label("loc_9B33")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B6C")
    WaitChrThread(0x109, 1)

    label("loc_9B6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B80")
    WaitChrThread(0x105, 1)

    label("loc_9B80")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9B94")
    WaitChrThread(0x10A, 1)

    label("loc_9B94")

    Jump("loc_9E85")

    label("loc_9B99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_9CA7")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x105, -48400, 0, 1030, 90)
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_9BFC():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9BFC)

    def lambda_9C16():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9C16)

    def lambda_9C30():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9C30)

    def lambda_9C4A():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9C4A)

    def lambda_9C64():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9C64)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x109, 1)
    Jump("loc_9E85")

    label("loc_9CA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_9DB5")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)
    SetChrPos(0x105, -48300, 0, -1070, 90)

    def lambda_9D0A():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9D0A)

    def lambda_9D24():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9D24)

    def lambda_9D3E():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9D3E)

    def lambda_9D58():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9D58)

    def lambda_9D72():
        OP_95(0xFE, -46300, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9D72)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x105, 1)
    Jump("loc_9E85")

    label("loc_9DB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_9E85")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x105, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)

    def lambda_9E07():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9E07)

    def lambda_9E21():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_9E21)

    def lambda_9E3B():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E3B)

    def lambda_9E55():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_9E55)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)

    label("loc_9E85")


    #C0317
    ChrTalk(
        0x106,
        (
            "#6P#10708F不好意思，我就在\x01",
            "医院外等大家。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_A01E")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9F31")

    def lambda_9ED2():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9ED2)
    Sleep(50)

    def lambda_9EE2():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9EE2)
    Sleep(50)

    def lambda_9EF2():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9EF2)
    Sleep(50)

    def lambda_9F02():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9F02)
    Sleep(50)

    def lambda_9F12():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9F12)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_9F31")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9FA5")

    def lambda_9F46():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9F46)
    Sleep(50)

    def lambda_9F56():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9F56)
    Sleep(50)

    def lambda_9F66():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9F66)
    Sleep(50)

    def lambda_9F76():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9F76)
    Sleep(50)

    def lambda_9F86():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9F86)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_9FA5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A019")

    def lambda_9FBA():
        TurnDirection(0x10A, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_9FBA)
    Sleep(50)

    def lambda_9FCA():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9FCA)
    Sleep(50)

    def lambda_9FDA():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_9FDA)
    Sleep(50)

    def lambda_9FEA():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_9FEA)
    Sleep(50)

    def lambda_9FFA():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9FFA)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_A019")

    Jump("loc_A15B")

    label("loc_A01E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_A090")

    def lambda_A02C():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A02C)
    Sleep(50)

    def lambda_A03C():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A03C)
    Sleep(50)

    def lambda_A04C():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A04C)
    Sleep(50)

    def lambda_A05C():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A05C)
    Sleep(50)

    def lambda_A06C():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A06C)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_A15B")

    label("loc_A090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_A102")

    def lambda_A09E():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_A09E)
    Sleep(50)

    def lambda_A0AE():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A0AE)
    Sleep(50)

    def lambda_A0BE():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A0BE)
    Sleep(50)

    def lambda_A0CE():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A0CE)
    Sleep(50)

    def lambda_A0DE():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A0DE)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_A15B")

    label("loc_A102")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_A15B")

    def lambda_A110():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_A110)
    Sleep(50)

    def lambda_A120():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A120)
    Sleep(50)

    def lambda_A130():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_A130)
    Sleep(50)

    def lambda_A140():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_A140)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    label("loc_A15B")


    #C0318
    ChrTalk(
        0x101,
        (
            "#11P#00003F嗯，知道了，\x01",
            "待会见吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_32(0xFF, 0xF9, 0x0)
    SetScenarioFlags(0x1AD, 2)
    RemoveParty(0x5, 0xFF)
    ClearChrFlags(0xD, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    ModifyEventFlags(1, 5, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A1BF")
    RemoveParty(0x6, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)

    label("loc_A1BF")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -44100, 0, -230, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_A1F1")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_A1F1")

    EventEnd(0x5)
    Return()

    # Function_92_9987 end

    def Function_93_A1F4(): pass

    label("Function_93_A1F4")

    EventBegin(0x0)
    Fade(500)
    OP_68(-49470, 1000, -560, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_A2E8")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x102, -46820, 0, -830, 270)
    SetChrPos(0x103, -46820, 0, 370, 270)
    SetChrPos(0x104, -45620, 0, -1030, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A297")
    SetChrPos(0x109, -45620, 0, 570, 270)

    label("loc_A297")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2B8")
    SetChrPos(0x105, -45620, 0, 570, 270)

    label("loc_A2B8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A2D9")
    SetChrPos(0x10A, -45620, 0, 570, 270)

    label("loc_A2D9")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_A40F")

    label("loc_A2E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_A355")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x109, -45620, 0, -1030, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_A40F")

    label("loc_A355")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_A3C2")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_A40F")

    label("loc_A3C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_A40F")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x105, -46820, 0, 370, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)

    label("loc_A40F")

    OP_4B(0xD, 0xFF)
    OP_0D()

    #C0319
    ChrTalk(
        0xD,
        (
            "#6P#10702F各位，你们回来了啊。\x01",
            "……事情都办完了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#11P#00000F嗯，我们走吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearScenarioFlags(0x1AD, 2)
    ModifyEventFlags(1, 4, 0x80)
    ModifyEventFlags(0, 5, 0x80)
    SetChrFlags(0xD, 0x80)
    AddParty(0x5, 0xFF, 0xFF)
    SetChrChipPat(0x5, 0x1, 0x20)
    LoadChrChipPat()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -48820, 0, -230, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_A4C7")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_A4C7")

    EventEnd(0x5)
    Return()

    # Function_93_A1F4 end

    def Function_94_A4CA(): pass

    label("Function_94_A4CA")

    EventBegin(0x0)
    Fade(500)
    OP_68(-46080, 1000, -230, 0)
    MoveCamera(51, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -50520, 0, -230, 90)
    SetChrPos(0x102, -50500, 0, 1110, 90)
    SetChrPos(0x103, -50500, 0, -1420, 90)
    SetChrPos(0x104, -51500, 0, 1110, 90)
    SetChrPos(0x106, -51500, 0, -230, 90)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A575")
    SetChrPos(0x109, -51500, 0, -1420, 90)

    label("loc_A575")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A596")
    SetChrPos(0x105, -51500, 0, -1420, 90)

    label("loc_A596")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A5B7")
    SetChrPos(0x10A, -51500, 0, -1420, 90)

    label("loc_A5B7")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_A5D0():
        OP_95(0xFE, -44520, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A5D0)
    Sleep(30)

    def lambda_A5ED():
        OP_95(0xFE, -44520, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A5ED)
    Sleep(30)

    def lambda_A60A():
        OP_95(0xFE, -44520, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A60A)
    Sleep(30)

    def lambda_A627():
        OP_95(0xFE, -45820, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A627)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A669")

    def lambda_A654():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A654)

    label("loc_A669")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A693")

    def lambda_A67E():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A67E)

    label("loc_A693")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A6BD")

    def lambda_A6A8():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_A6A8)

    label("loc_A6BD")

    Sleep(30)

    def lambda_A6C5():
        OP_95(0xFE, -48500, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_A6C5)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    #C0321
    ChrTalk(
        0x106,
        (
            "#6P#10703F那么……\x01",
            "我就在这里等大家……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_A71C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A71C)

    def lambda_A729():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A729)

    def lambda_A736():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A736)

    def lambda_A743():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A743)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A768")

    def lambda_A760():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A760)

    label("loc_A768")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A785")

    def lambda_A77D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A77D)

    label("loc_A785")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A7A2")

    def lambda_A79A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_A79A)

    label("loc_A7A2")

    WaitChrThread(0x104, 1)
    Sleep(500)

    #C0322
    ChrTalk(
        0x102,
        "#11P#00105F莉夏小姐……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        "#5P#00303F呼……没办法啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0324
    ChrTalk(
        0x101,
        (
            "#11P#00003F……那个，莉夏。\x02\x03",

            "#00000F至少去听听\x01",
            "伊莉娅小姐的声音吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0325
    ChrTalk(
        0x106,
        "#6P#10705F…………哎……………\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#11P#00003F在将一切了结之前，\x01",
            "不愿去见伊莉娅小姐……\x02\x03",

            "我很理解你这种心情，\x01",
            "也尊重你的决定……\x02\x03",

            "#00000F不过，在病房门外\x01",
            "听听我们和伊莉娅小姐的\x01",
            "对话总可以吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x106,
        (
            "#6P#10705F啊……\x02\x03",

            "#10708F……………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    #C0328
    ChrTalk(
        0x104,
        (
            "#5P#00302F是啊，这没什么大不了的，\x01",
            "就当作是给自己的奖励吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#11P#00203F前方恐怕还有\x01",
            "千难万险在等着我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#11P#00100F听到珍重之人的声音，\x01",
            "一定能产生更强的前进动力。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AABE")

    #C0331
    ChrTalk(
        0x109,
        (
            "#11P#10105F没错，莉夏小姐！\x02\x03",

            "#10101F我们一定会小心，\x01",
            "不让她察觉到你的存在！\x02\x03",

            "#10104F那个……我见到芙兰时，\x01",
            "也受到了很大的鼓舞呢……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AABE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AB59")

    #C0332
    ChrTalk(
        0x105,
        (
            "#11P#10404F呵呵，这不是很好吗？\x02\x03",

            "#10400F只要不直接见面，\x01",
            "就不算违背你的誓言。\x02\x03",

            "#10408F……等到想见却无法再见的时候，\x01",
            "可就一切都晚了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AB59")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ABF1")

    #C0333
    ChrTalk(
        0x10A,
        (
            "#11P#00603F『银』……\x01",
            "不，莉夏·毛。\x02\x03",

            "#00600F身为警察，我说这些可能不太合适，\x01",
            "但现在是非常时期。\x02\x03",

            "#00602F至少不要给自己\x01",
            "留下遗憾。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_ABF1")

    Sleep(1500)
    OP_64(0x106)

    #C0334
    ChrTalk(
        0x106,
        (
            "#6P#10704F……各位，\x01",
            "谢谢你们。\x02\x03",

            "#10702F……那就承蒙各位的好意……\x01",
            "让我随行到病房前吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        "#11P#00002F嗯……！\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        "#11P#00100F嗯，明白了……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x1AD, 3)
    ModifyEventFlags(0, 6, 0x80)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -44520, 0, -230, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_94_A4CA end

    def Function_95_ACC3(): pass

    label("Function_95_ACC3")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_B2EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ACE1")
    Call(0, 96)
    Jump("loc_B2E6")

    label("loc_ACE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B143")

    #C0337
    ChrTalk(
        0x10,
        (
            "#01300F罗伊德……你们\x01",
            "打败了亚里欧斯先生啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#00000F嗯，真是一场相当艰苦的战斗……\x01",
            "多亏了大家齐心合力。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#00103F亚里欧斯先生不仅是\x01",
            "与我们共同进步的好对手，\x01",
            "也是我们必须要跨越的『壁障』……\x02\x03",

            "#00100F说实话，少了任何一个人，\x01",
            "我们都绝对战胜不了他。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        "#00304F……是啊。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x10,
        (
            "#01309F呵呵，因为你们全部加起来，\x01",
            "才是真正的『支援科』吧？\x01",
            "这就足以感到自豪了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    #C0342
    ChrTalk(
        0x10,
        (
            "#01304F我和亚里欧斯先生\x01",
            "并没有说过多少话……\x02\x03",

            "但我能感觉得到，\x01",
            "他的心中一直\x01",
            "都有着沉重的负担。\x02\x03",

            "#01308F小滴和他的夫人，还有盖伊的事，\x01",
            "他都独自一人背负……\x01",
            "真是让人于心不忍。\x02\x03",

            "#01300F而他又比任何人都强大，\x01",
            "所以也无法\x01",
            "依赖他人吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x103,
        (
            "#00200F因为强大而孤独……\x01",
            "或许正是如此呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x10,
        (
            "#01302F呵呵，但他和你们\x01",
            "全力交战，并被你们打败，\x01",
            "今后一定能得到解放。\x02\x03",

            "#01304F盖伊当年肯定也一直很担心他。\x01",
            "作为盖伊的未婚妻，就由我代替他\x01",
            "向你们道谢吧。\x02\x03",

            "#01309F谢谢你们拯救了盖伊的挚友\x01",
            "亚里欧斯先生。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#00004F哈哈……不客气。\x02\x03",

            "#00000F接下来，就剩下夺回琪雅了。\x01",
            "等着我们，塞茜尔姐姐。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x10,
        (
            "#01300F嗯，好的。\x02\x03",

            "#01303F罗伊德，还有各位……\x01",
            "直到最后关头都不能大意哦。\x02\x03",

            "#01302F我会在此祈祷，\x01",
            "祝愿你们和小琪雅一起\x01",
            "带着笑容归来。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 5)
    Jump("loc_B2E6")

    label("loc_B143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B276")

    #C0347
    ChrTalk(
        0x10,
        (
            "#01303F罗伊德，还有各位……\x01",
            "直到最后关头都不能大意哦。\x02\x03",

            "#01302F我会在此祈祷，\x01",
            "祝愿你们和小琪雅一起\x01",
            "带着笑容归来。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#00000F嗯，等我们吧。\x02\x03",

            "#00003F（……总算解明了大哥那起事件的\x01",
            "  真相……但现在似乎还不到告诉\x01",
            "  塞茜尔姐姐的时候。）\x02\x03",

            "#00008F（还需要向伊安律师\x01",
            "  问清楚具体情况……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_B2E6")

    label("loc_B276")


    #C0349
    ChrTalk(
        0x10,
        (
            "#01303F罗伊德，还有各位……\x01",
            "直到最后关头都不能大意哦。\x02\x03",

            "我会在此祈祷，\x01",
            "祝愿你们和小琪雅一起\x01",
            "带着笑容归来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B2E6")

    Jump("loc_B4CF")

    label("loc_B2EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_B4AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B306")
    Call(0, 96)
    Jump("loc_B4A5")

    label("loc_B306")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B463")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3E3")
    TurnDirection(0x10, 0x106, 0)

    #C0350
    ChrTalk(
        0x10,
        (
            "#01300F莉夏，你也要\x01",
            "多加小心哦。\x02\x03",

            "#01304F伊莉娅虽然不会\x01",
            "直接说出口，但她\x01",
            "一直都非常关心你。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B3B0")

    #C0351
    ChrTalk(
        0x106,
        "#10708F……是吗……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B3DE")

    label("loc_B3B0")


    #C0352
    ChrTalk(
        0x106,
        (
            "#10702F好的……！\x01",
            "我保证一定会平安归来。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3DE")

    Jump("loc_B45B")

    label("loc_B3E3")


    #C0353
    ChrTalk(
        0x10,
        (
            "#01300F和小琪雅一起，\x01",
            "全员平安归来的约定……\x01",
            "一定不要忘记哦。\x02\x03",

            "#01304F只要有这约定，\x01",
            "我就能在这里\x01",
            "等待大家归来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B45B")

    SetScenarioFlags(0x0, 7)
    Jump("loc_B4A5")

    label("loc_B463")


    #C0354
    ChrTalk(
        0x10,
        (
            "#01300F我会在这里\x01",
            "等待大家归来。\x02\x03",

            "#01304F愿女神\x01",
            "保佑你们……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B4A5")

    Jump("loc_B4CF")

    label("loc_B4AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_B4B8")
    Jump("loc_B4CF")

    label("loc_B4B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_B4C6")
    Jump("loc_B4CF")

    label("loc_B4C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_B4CF")

    label("loc_B4CF")

    TalkEnd(0xFE)
    Return()

    # Function_95_ACC3 end

    def Function_96_B4D3(): pass

    label("Function_96_B4D3")

    EventBegin(0x0)
    Fade(500)
    OP_68(-24280, 400, -23490, 0)
    MoveCamera(32, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15570, 0)
    SetChrPos(0x101, -24090, -1000, -22920, 180)
    SetChrPos(0x102, -25290, -1000, -22000, 180)
    SetChrPos(0x103, -22850, -1000, -22000, 225)
    SetChrPos(0x104, -24260, -1000, -21430, 180)
    SetChrPos(0xF4, -22050, -1000, -22590, 225)
    SetChrPos(0xF5, -22790, -1000, -20810, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrSubChip(0x10, 0x0)
    OP_93(0x10, 0xB4, 0x0)
    OP_0D()

    #C0355
    ChrTalk(
        0x101,
        "#5P#00000F塞茜尔姐姐……你在这里啊。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 300)

    #C0356
    ChrTalk(
        0x10,
        (
            "#12P#01300F嗯，突然出现那种东西，\x01",
            "真是吓了我一跳……\x02\x03",

            "#01304F……不过，真是棵不可思议的树。\x02\x03",

            "虽然是非常异常的东西，\x01",
            "但却让人产生爱怜的感觉……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        (
            "#5P#00108F（贝尔说那棵\x01",
            "  『大树』就是\x01",
            "  『小琪雅自身』……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B6F7")

    #C0358
    ChrTalk(
        0x105,
        (
            "#11P#10403F（她会有这种感觉，\x01",
            "  或许也不奇怪吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B79C")

    label("loc_B6F7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B74C")

    #C0359
    ChrTalk(
        0x109,
        (
            "#11P#10103F（塞茜尔小姐会有这种感觉，\x01",
            "  或许也不奇怪呢。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B79C")

    label("loc_B74C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B79C")

    #C0360
    ChrTalk(
        0x106,
        (
            "#11P#10703F（塞茜尔小姐会有这种感觉，\x01",
            "  或许也不足为奇。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B79C")

    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    #C0361
    ChrTalk(
        0x10,
        (
            "#12P#01303F罗伊德，还有大家……\x02\x03",

            "#01301F……你们要去那个地方了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        (
            "#5P#00003F……嗯。\x02\x03",

            "#00001F琪雅，还有一切事情的真相……\x01",
            "都在那棵『大树』中等着我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#5P#00101F无论前方有怎样的危险，\x01",
            "我们都必须要继续前行。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x10,
        "#12P#01308F是吗……\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    #C0365
    ChrTalk(
        0x10,
        (
            "#12P#01303F说实话，我真不希望\x01",
            "你们去冒这个险……\x02\x03",

            "#01308F因为我曾经失去过重要的人……\x01",
            "实在是不想再次体会那种心情了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B972")

    #C0366
    ChrTalk(
        0x106,
        "#11P#10705F塞茜尔小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9E1")

    label("loc_B972")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9AC")

    #C0367
    ChrTalk(
        0x10A,
        "#11P#00608F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_B9E1")

    label("loc_B9AC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B9E1")

    #C0368
    ChrTalk(
        0x105,
        "#11P#10408F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_B9E1")


    #C0369
    ChrTalk(
        0x10,
        (
            "#12P#01303F……可是，如果盖伊还活着……\x01",
            "他也一定会做出\x01",
            "和你们一样的选择。\x02\x03",

            "#01302F为了守护重要的人，\x01",
            "无论要面对怎样的危险，\x01",
            "他都会奋不顾身的。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        "#5P#00000F塞茜尔姐姐……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x10,
        (
            "#12P#01304F……所以，\x01",
            "请你们答应我一件事。\x02\x03",

            "#01300F一定要带着小琪雅，\x01",
            "全员平安归来。\x02\x03",

            "#01309F只要有这个约定，\x01",
            "我就能在这里\x01",
            "等待大家归来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#5P#00005F塞茜尔姐姐……\x02\x03",

            "#00004F……明白了，\x01",
            "你再稍微等我们一段时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x103,
        (
            "#11P#00200F虽然这肯定会是一场\x01",
            "非常严峻的试炼……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x102,
        (
            "#5P#00102F嗯，但我们一定会\x01",
            "夺回小琪雅，平安归来。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x104,
        (
            "#5P#00309F而且还要把亚里欧斯\x01",
            "那个大叔给打醒呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC44")

    #C0376
    ChrTalk(
        0x10A,
        "#11P#00602F嗯，当然。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCA1")

    label("loc_BC44")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BC74")

    #C0377
    ChrTalk(
        0x109,
        "#11P#10102F嗯，是呀。\x02",
    )

    CloseMessageWindow()
    Jump("loc_BCA1")

    label("loc_BC74")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BCA1")

    #C0378
    ChrTalk(
        0x105,
        "#11P#10402F呵呵，是啊。\x02",
    )

    CloseMessageWindow()

    label("loc_BCA1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6D), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BEDD")

    #C0379
    ChrTalk(
        0x10,
        (
            "#12P#01304F……呵呵，谢谢大家，\x01",
            "这下我总算放心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    #C0380
    ChrTalk(
        0x10,
        (
            "#12P#01309F那么，作为约定的信物，\x01",
            "把这个交给你们吧。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0381
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3A0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x3A0, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1DE, 2)

    #C0382
    ChrTalk(
        0x101,
        "#5P#00005F这是……？\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x10,
        (
            "#12P#01300F这是盖伊在我参加护士考试时\x01",
            "送给我的东西。\x02\x03",

            "#01304F难过的时候，只要握紧它，\x01",
            "便会有一股勇气神奇般地涌上心头……\x01",
            "就是这样的护身符呢。\x02\x03",

            "#01300F这是很重要的东西，\x01",
            "所以一定要平安归来，然后还给我哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#5P#00000F……嗯，知道了。\x01",
            "十分感谢，那我们就暂借一下啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x10,
        (
            "#12P#01309F呵呵，\x01",
            "愿女神\x01",
            "保佑你们……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF31")

    label("loc_BEDD")


    #C0386
    ChrTalk(
        0x10,
        (
            "#12P#01304F……呵呵，谢谢大家，\x01",
            "这下我总算放心了。\x02\x03",

            "#01309F愿女神\x01",
            "保佑你们……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF31")

    OP_5A()
    SetScenarioFlags(0x1AC, 4)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24090, -1000, -22920, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BF7A")
    OP_E0(0x34, 0x0)

    label("loc_BF7A")

    EventEnd(0x5)
    Return()

    # Function_96_B4D3 end

    def Function_97_BF7D(): pass

    label("Function_97_BF7D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BFE8")

    #C0387
    ChrTalk(
        0x101,
        (
            "#00000F在芙兰做好准备之前，\x01",
            "我们不能离开医院啊。\x02\x03",

            "先去探望伊莉娅小姐\x01",
            "和多诺邦警督吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BFE8")

    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_97_BF7D end

    def Function_98_BFFF(): pass

    label("Function_98_BFFF")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0388
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "St.Ursula \x01",
            "Medical College\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_98_BFFF end

    def Function_99_C055(): pass

    label("Function_99_C055")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0389
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "Medical College\x01",
            "～招待所『雷克切』～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_99_C055 end

    SaveToFile()

Try(main)
