from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "警備員トニー",           # 1
        "看護師エイダ",           # 2
        "ダイソン用務員",         # 3
        "セイランド教授",         # 4
        "ハロルド",               # 5
        "リーシャ",               # 6
        "ビリー",                 # 7
        "運転士",                 # 8
        "セシル",                 # 9
        "バス",                   # 10
        "国防軍兵士",             # 11
        "国防軍兵士",             # 12
        "国防軍兵士",             # 13
        "国防軍兵士",             # 14
        "セシル",                 # 15
        "フラン",                 # 16
        "車",                     # 17
        "メルカバ玖号機",         # 18
        "看護士Ａ",               # 19
        "看護士Ｂ",               # 20
        "研修医Ａ",               # 21
        "研修医Ｂ",               # 22
        "子供",                   # 23
        "おじさん",               # 24
        "おじいさま",             # 25
        "おばあさま",             # 26
        "見舞い客Ａ",             # 27
        "見舞い客Ｂ",             # 28
        "見舞い客Ｃ",             # 29
        "見舞い客Ｄ",             # 30
        "SE制御",                 # 31
        "bt1510",                 # 32
        "ウルスラ間道",           # 33
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

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "ウルスラ間道")
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
        "Function_7_181B",         # 07, 7
        "Function_8_1948",         # 08, 8
        "Function_9_196F",         # 09, 9
        "Function_10_1A03",        # 0A, 10
        "Function_11_2A74",        # 0B, 11
        "Function_12_369F",        # 0C, 12
        "Function_13_3D2B",        # 0D, 13
        "Function_14_3ECF",        # 0E, 14
        "Function_15_3F88",        # 0F, 15
        "Function_16_4097",        # 10, 16
        "Function_17_431E",        # 11, 17
        "Function_18_43AB",        # 12, 18
        "Function_19_46EE",        # 13, 19
        "Function_20_473A",        # 14, 20
        "Function_21_480E",        # 15, 21
        "Function_22_5476",        # 16, 22
        "Function_23_5486",        # 17, 23
        "Function_24_5499",        # 18, 24
        "Function_25_54AC",        # 19, 25
        "Function_26_54BF",        # 1A, 26
        "Function_27_54D2",        # 1B, 27
        "Function_28_5D66",        # 1C, 28
        "Function_29_5E4A",        # 1D, 29
        "Function_30_5F01",        # 1E, 30
        "Function_31_5FC1",        # 1F, 31
        "Function_32_603D",        # 20, 32
        "Function_33_60AC",        # 21, 33
        "Function_34_60E6",        # 22, 34
        "Function_35_6135",        # 23, 35
        "Function_36_616F",        # 24, 36
        "Function_37_61A9",        # 25, 37
        "Function_38_61F8",        # 26, 38
        "Function_39_6232",        # 27, 39
        "Function_40_626C",        # 28, 40
        "Function_41_6C64",        # 29, 41
        "Function_42_6D7F",        # 2A, 42
        "Function_43_6E1D",        # 2B, 43
        "Function_44_6E49",        # 2C, 44
        "Function_45_6E54",        # 2D, 45
        "Function_46_7559",        # 2E, 46
        "Function_47_757B",        # 2F, 47
        "Function_48_75A0",        # 30, 48
        "Function_49_75C5",        # 31, 49
        "Function_50_75DD",        # 32, 50
        "Function_51_75F5",        # 33, 51
        "Function_52_760D",        # 34, 52
        "Function_53_7625",        # 35, 53
        "Function_54_8DB0",        # 36, 54
        "Function_55_8DDF",        # 37, 55
        "Function_56_8E13",        # 38, 56
        "Function_57_8EA3",        # 39, 57
        "Function_58_8EF1",        # 3A, 58
        "Function_59_8F05",        # 3B, 59
        "Function_60_8F76",        # 3C, 60
        "Function_61_8F85",        # 3D, 61
        "Function_62_900E",        # 3E, 62
        "Function_63_9013",        # 3F, 63
        "Function_64_90B9",        # 40, 64
        "Function_65_90BE",        # 41, 65
        "Function_66_9140",        # 42, 66
        "Function_67_91E7",        # 43, 67
        "Function_68_927E",        # 44, 68
        "Function_69_92A3",        # 45, 69
        "Function_70_92C8",        # 46, 70
        "Function_71_9313",        # 47, 71
        "Function_72_9370",        # 48, 72
        "Function_73_93AA",        # 49, 73
        "Function_74_93BA",        # 4A, 74
        "Function_75_93CD",        # 4B, 75
        "Function_76_93F1",        # 4C, 76
        "Function_77_9415",        # 4D, 77
        "Function_78_9439",        # 4E, 78
        "Function_79_945D",        # 4F, 79
        "Function_80_99D2",        # 50, 80
        "Function_81_9A2D",        # 51, 81
        "Function_82_9A47",        # 52, 82
        "Function_83_9A64",        # 53, 83
        "Function_84_9A81",        # 54, 84
        "Function_85_9A9B",        # 55, 85
        "Function_86_9AB8",        # 56, 86
        "Function_87_9AF5",        # 57, 87
        "Function_88_9AF6",        # 58, 88
        "Function_89_9B11",        # 59, 89
        "Function_90_9B3C",        # 5A, 90
        "Function_91_A83B",        # 5B, 91
        "Function_92_A83C",        # 5C, 92
        "Function_93_B0C1",        # 5D, 93
        "Function_94_B3A5",        # 5E, 94
        "Function_95_BCA2",        # 5F, 95
        "Function_96_C658",        # 60, 96
        "Function_97_D2A0",        # 61, 97
        "Function_98_D342",        # 62, 98
        "Function_99_D398",        # 63, 99
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
            "#1Kバス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "クロスベル市南口\x01",            # 0
            "分岐停留所（中州付近）\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17F3")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_1813")

    label("loc_17F3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1813")
    Call(0, 7)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_1813")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_6_1757 end

    def Function_7_181B(): pass

    label("Function_7_181B")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_1944")
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

    def lambda_18FB():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_18FB)
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

    label("loc_1944")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_7_181B end

    def Function_8_1948(): pass

    label("Function_8_1948")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -56560, 0, 4080, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_8_1948 end

    def Function_9_196F(): pass

    label("Function_9_196F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_19CA")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19BF")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_19C5")

    label("loc_19BF")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_19C5")

    Jump("loc_19EE")

    label("loc_19CA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_19E8")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_19EE")

    label("loc_19E8")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_19EE")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_9_196F end

    def Function_10_1A03(): pass

    label("Function_10_1A03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1B5D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AD8")

    #C0002
    ChrTalk(
        0x8,
        (
            "おいおい……あの青白く光る\x01",
            "巨大な木は一体なんなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x8,
        (
            "あんなものが突然現れるなんて……\x01",
            "いくらなんでも訳がわからないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0x8,
        (
            "と、とにかく気合を入れて\x01",
            "警備していかないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1B58")

    label("loc_1AD8")


    #C0005
    ChrTalk(
        0x8,
        (
            "あんな巨大な木が突然現れるなんて……\x01",
            "いくらなんでも訳がわからないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "と、とにかく気合を入れて\x01",
            "警備していかないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B58")

    Jump("loc_2A70")

    label("loc_1B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_1C9B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C0B")

    #C0007
    ChrTalk(
        0x8,
        (
            "独立国の無効宣言の影響で、\x01",
            "国防軍も混乱しているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "救急車やバスの護衛は\x01",
            "今のところ続けられているけど、\x01",
            "やっぱり色々と不安になるな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C96")

    label("loc_1C0B")


    #C0009
    ChrTalk(
        0x8,
        (
            "例の無効宣言の影響で、\x01",
            "国防軍も混乱しているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        (
            "国防軍の護衛がないと\x01",
            "救急車の行き来もできないし、\x01",
            "色々と不安になってくるな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C96")

    Jump("loc_2A70")

    label("loc_1C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_1E23")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D8F")

    #C0011
    ChrTalk(
        0x8,
        (
            "国防軍の護衛がないと\x01",
            "救急車も行き来できないのは\x01",
            "正直、よくない状況だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "街道に出た《幻獣》と、\x01",
            "国防軍による移動制限……\x01",
            "この二つは大きな問題だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        (
            "せめて、街道の護衛には\x01",
            "もう少し人を割いて欲しいよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E1E")

    label("loc_1D8F")


    #C0014
    ChrTalk(
        0x8,
        (
            "国防軍の護衛がないと\x01",
            "救急車も行き来できないのは\x01",
            "正直、よくない状況だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x8,
        (
            "せめて国防軍は、街道の護衛に\x01",
            "もう少し人を割いて欲しいよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E1E")

    Jump("loc_2A70")

    label("loc_1E23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1F9C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F08")

    #C0016
    ChrTalk(
        0x8,
        (
            "国防軍の奴ら、留置場からの\x01",
            "逃亡犯とやらを捜索してたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "なんだかあっさりと\x01",
            "引き上げちゃったみたいだな。\x01",
            "一体どうしちゃったんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            "……ま、いいか。\x01",
            "とりあえず警備に戻らないとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1F97")

    label("loc_1F08")


    #C0019
    ChrTalk(
        0x8,
        (
            "国防軍の奴ら、留置場からの\x01",
            "逃亡犯を捜索しに来てたんだが\x01",
            "あっさり引き上げちゃったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        (
            "……ま、いいか。\x01",
            "とりあえず警備に戻らないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F97")

    Jump("loc_2A70")

    label("loc_1F9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2324")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_21D4")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2130")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_209B")

    #C0021
    ChrTalk(
        0x8,
        (
            "やれやれ、医療物資を\x01",
            "騙し取ろうなんて、\x01",
            "悪いヤツがいるもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "とりあえず取り戻せたから\x01",
            "よかったようなものの……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x8,
        (
            "みんなが頑張ってるときに\x01",
            "そういう話を聞くと、\x01",
            "悲しくなっちゃうよな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_212B")

    label("loc_209B")


    #C0024
    ChrTalk(
        0x8,
        (
            "やれやれ、医療物資を\x01",
            "騙し取ろうなんて、\x01",
            "悪いヤツがいるもんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "みんなが頑張ってるときに\x01",
            "そういう話を聞くと、\x01",
            "悲しくなっちゃうよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_212B")

    Jump("loc_21CF")

    label("loc_2130")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_21CF")

    #C0026
    ChrTalk(
        0x8,
        (
            "やれやれ、医療物資を\x01",
            "騙し取るなんて、\x01",
            "悪いヤツがいるもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "困っている人がいるのに\x01",
            "そんな事をするなんて、\x01",
            "人間として最低だよな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21CF")

    label("loc_21CF")

    Jump("loc_231F")

    label("loc_21D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22A6")

    #C0028
    ChrTalk(
        0x8,
        (
            "おっかしいなあ、\x01",
            "とっくに着いてても\x01",
            "いい頃なんだが……\x02",
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
            "おっと失礼、\x01",
            "ウルスラ医大にようこそ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x8,
        (
            "お見舞いなら、\x01",
            "病棟１階のロビーで\x01",
            "手続きを頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    Jump("loc_231F")

    label("loc_22A6")


    #C0031
    ChrTalk(
        0x8,
        (
            "この間の襲撃事件で\x01",
            "患者さんが激増したんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "病院内では先生方が\x01",
            "すごく忙しそうにしてる。\x01",
            "僕もがんばらなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231F")

    Jump("loc_2A70")

    label("loc_2324")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_249E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_240E")

    #C0033
    ChrTalk(
        0x8,
        (
            "やー、今日は雨か。\x01",
            "こういうとき警備はつらいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x8,
        (
            "それにしても、\x01",
            "昨日はたくさん救急車が来て\x01",
            "大変だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "かなり派手な事故だったそうだけど、\x01",
            "犠牲者が出なかったのは\x01",
            "奇跡としかいいようがないね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2499")

    label("loc_240E")


    #C0036
    ChrTalk(
        0x8,
        (
            "昨日はたくさん救急車が来て\x01",
            "大変だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "かなり派手な事故だったそうだけど、\x01",
            "犠牲者が出なかったのは\x01",
            "奇跡としかいいようがないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2499")

    Jump("loc_2A70")

    label("loc_249E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_252B")

    #C0038
    ChrTalk(
        0x8,
        (
            "遊撃士さんたちが\x01",
            "色々な場所を調べてるようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "大型の魔獣が出るなんて\x01",
            "噂もあるみたいだし……\x01",
            "僕も気をつけないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A70")

    label("loc_252B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2665")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25FD")

    #C0040
    ChrTalk(
        0x8,
        "や、ウルスラ医大にようこそ。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            "さっき、セイランド教授が\x01",
            "休憩所のほうに歩いていったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "教授、最近よくあの場所で\x01",
            "たたずんでいるみたいだ。\x01",
            "……色々考え事があるんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2660")

    label("loc_25FD")


    #C0043
    ChrTalk(
        0x8,
        (
            "セイランド教授、最近よく\x01",
            "休憩所のほうに出てきてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "……色々考え事があるんだろうな。\x02",
    )

    CloseMessageWindow()

    label("loc_2660")

    Jump("loc_2A70")

    label("loc_2665")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_26F6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2680")
    Call(0, 15)
    Jump("loc_26F1")

    label("loc_2680")


    #C0045
    ChrTalk(
        0x8,
        (
            "ああ、そのときは\x01",
            "シロンちゃんの記入ミスが\x01",
            "原因だったそうだから……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            "とりあえず今回は\x01",
            "問題ないと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F1")

    Jump("loc_2A70")

    label("loc_26F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28F9")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x78, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2791")

    #C0047
    ChrTalk(
        0x8,
        (
            "アルバート大公のリムジンが\x01",
            "先ほどお帰りになられたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x8,
        (
            "や～、緊張したけど……\x01",
            "ちゃんと出迎えることが\x01",
            "できてよかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F4")

    label("loc_2791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2869")

    #C0049
    ChrTalk(
        0x8,
        (
            "レミフェリアのアルバート大公が、\x01",
            "視察にいらっしゃってるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x8,
        (
            "や～、事前に話は聞いてたけど\x01",
            "いざ出迎えるとなると\x01",
            "滅茶苦茶緊張するもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "お帰りになるまで、\x01",
            "失礼のないようにしないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_28F4")

    label("loc_2869")


    #C0052
    ChrTalk(
        0x8,
        (
            "や～、事前に話は聞いてたけど\x01",
            "いざ出迎えるとなると\x01",
            "滅茶苦茶緊張するもんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "大公がお帰りになるまで、\x01",
            "失礼のないようにしないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F4")

    Jump("loc_2A70")

    label("loc_28F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A70")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D3")

    #C0054
    ChrTalk(
        0x8,
        (
            "や、こんにちは。\x01",
            "ここは聖ウルスラ医科大学病院だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x8,
        (
            "長いから、『ウルスラ病院』とか、\x01",
            "『ウルスラ医大』って略す人が多いね。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        (
            "おっと、診療やお見舞いの受付なら\x01",
            "奥の建物でよろしくな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A70")

    label("loc_29D3")


    #C0057
    ChrTalk(
        0x8,
        (
            "教団事件の時に銃で撃たれた傷も、\x01",
            "ここの先生にキレイさっぱり\x01",
            "治してもらったんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x8,
        (
            "ウルスラ医大の誇る医療技術は\x01",
            "まさに偉大だ！　……なんつってね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A70")

    TalkEnd(0xFE)
    Return()

    # Function_10_1A03 end

    def Function_11_2A74(): pass

    label("Function_11_2A74")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2C47")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B94")

    #C0059
    ChrTalk(
        0x9,
        (
            "国防軍が、街道を行き来する\x01",
            "救急車やバスの護衛に\x01",
            "人手を回してくれたみたいでね。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x9,
        (
            "街での騒動で怪我をした人や、\x01",
            "しばらく病院に通えていなかった人も\x01",
            "大分来れるようになったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x9,
        (
            "遊撃士のエオリアさんも\x01",
            "手伝いに来てくれたし、\x01",
            "病院はひとまず安心かしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2C42")

    label("loc_2B94")


    #C0062
    ChrTalk(
        0x9,
        (
            "遊撃士のエオリアさんも\x01",
            "手伝いに来てくれたし、\x01",
            "病院はひとまず安心かしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x9,
        (
            "でも、あんな巨大な木が現れて、\x01",
            "患者さんたちに不安が広がってる。\x01",
            "私も精一杯頑張らないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C42")

    Jump("loc_369B")

    label("loc_2C47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_2DA0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D1F")

    #C0064
    ChrTalk(
        0x9,
        (
            "入院している患者さんたちは、\x01",
            "市内にいる家族がとても心配みたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x9,
        (
            "こちらからはロクに連絡も取れない\x01",
            "状況だから仕方ないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x9,
        (
            "なんとか患者さんたちの不安を\x01",
            "和らげてあげないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2D9B")

    label("loc_2D1F")


    #C0067
    ChrTalk(
        0x9,
        (
            "入院している患者さんたちは、\x01",
            "市内にいる家族がとても心配みたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x9,
        (
            "なんとか患者さんたちの不安を\x01",
            "和らげてあげないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D9B")

    Jump("loc_369B")

    label("loc_2DA0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_2EC2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E57")

    #C0069
    ChrTalk(
        0x9,
        (
            "私は国防軍や大統領なんかより、\x01",
            "弟君たちの意思を尊重するわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x9,
        "きっと無事でいてちょうだい。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x9,
        (
            "それと、セシル先輩に\x01",
            "あまり心配をかけないようにね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2EBD")

    label("loc_2E57")


    #C0072
    ChrTalk(
        0x9,
        (
            "弟君たち、\x01",
            "きっと無事でいてちょうだい。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x9,
        (
            "それと、セシル先輩に\x01",
            "あまり心配をかけないようにね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EBD")

    Jump("loc_369B")

    label("loc_2EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F99")

    #C0074
    ChrTalk(
        0x9,
        (
            "弟君たち、国防軍と\x01",
            "争っていたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x9,
        (
            "……ううん、\x01",
            "やっぱり気にしないで。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x9,
        (
            "どんなことがあっても、\x01",
            "私たちは弟君の味方だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00002F……ありがとうございます。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_2FD2")

    label("loc_2F99")


    #C0078
    ChrTalk(
        0x9,
        (
            "どんなことがあっても、\x01",
            "私たちは弟君の味方だからね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FD2")

    Jump("loc_369B")

    label("loc_2FD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3076")

    #C0079
    ChrTalk(
        0x9,
        (
            "あの事件で相当な数の\x01",
            "患者さんが運ばれてきたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x9,
        (
            "治療もなかなか追いつかなくて……\x01",
            "手術の必要がある人が\x01",
            "何人も順番待ちをしている状態よ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_369B")

    label("loc_3076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3084")
    Jump("loc_369B")

    label("loc_3084")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_31A4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_315D")

    #C0081
    ChrTalk(
        0x9,
        (
            "シズクちゃん、今回の手術を\x01",
            "かなり前向きに捉えてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x9,
        (
            "あの子が諦めてないんだもの、\x01",
            "周囲にいる私たちが\x01",
            "悲観的になっちゃだめよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x9,
        (
            "……うん、私たちも\x01",
            "信じてがんばらなきゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_319F")

    label("loc_315D")


    #C0084
    ChrTalk(
        0x9,
        (
            "私たちも\x01",
            "シズクちゃんの完治を信じて、\x01",
            "がんばらなくっちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_319F")

    Jump("loc_369B")

    label("loc_31A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_329C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324D")

    #C0085
    ChrTalk(
        0x9,
        (
            "セイランド教授だから\x01",
            "あそこまでの手術が\x01",
            "できたと言えるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x9,
        (
            "シズクちゃん……\x01",
            "やっぱり今の医療技術じゃ\x01",
            "完全には治せないのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3297")

    label("loc_324D")


    #C0087
    ChrTalk(
        0x9,
        (
            "シズクちゃん……\x01",
            "やっぱり今の医療技術じゃ\x01",
            "完全には治せないのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3297")

    Jump("loc_369B")

    label("loc_329C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3339")

    #C0088
    ChrTalk(
        0x9,
        (
            "今日はいよいよ通商会議の\x01",
            "本会議が開かれるらしいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x9,
        (
            "一体どんな会議になるのかしら。\x01",
            "ちゃんとチェックしておかないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_33B1")

    label("loc_3339")


    #C0090
    ChrTalk(
        0x9,
        (
            "フィリアもランも\x01",
            "興味なさそうだったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "一体どんな会議になるのかしら。\x01",
            "ちゃんとチェックしておかないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33B1")

    Jump("loc_369B")

    label("loc_33B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3509")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34A4")

    #C0092
    ChrTalk(
        0x9,
        (
            "さっき、アルバート大公が\x01",
            "わざわざ挨拶してくださったの。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x9,
        (
            "一国の元首様だし、\x01",
            "偉そうな人かな、なんて\x01",
            "勝手に思ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "私みたいな一看護師に\x01",
            "声をかけてくれるなんて、\x01",
            "意外と気さくなお方みたいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3504")

    label("loc_34A4")


    #C0095
    ChrTalk(
        0x9,
        (
            "アルバート大公って\x01",
            "意外と気さくなお方みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x9,
        (
            "ふふ、\x01",
            "一気に親近感が湧いちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3504")

    Jump("loc_369B")

    label("loc_3509")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_369B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x159, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_364E")

    #C0097
    ChrTalk(
        0x9,
        (
            "あら、ランディさんに弟君。\x01",
            "ひさしぶりね。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00006F（『弟君』か……\x01",
            "  ほんと定着しちゃったなあ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x104,
        (
            "#00302Fハハ、エイダちゃんたちは\x01",
            "元気にしてたかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x9,
        (
            "ええ、ランもフィリアも\x01",
            "相変わらずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "そっちは新メンバーも\x01",
            "増えたみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "機会があったら\x01",
            "今度また遊びましょうね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x159, 4)
    Jump("loc_369B")

    label("loc_364E")


    #C0103
    ChrTalk(
        0x9,
        "ふふ、再会できて嬉しいわ。\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x9,
        (
            "機会があったら\x01",
            "今度また遊びましょうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_369B")

    TalkEnd(0xFE)
    Return()

    # Function_11_2A74 end

    def Function_12_369F(): pass

    label("Function_12_369F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_36B0")
    Jump("loc_3D27")

    label("loc_36B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_36BE")
    Jump("loc_3D27")

    label("loc_36BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_36CC")
    Jump("loc_3D27")

    label("loc_36CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_384A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B9")

    #C0105
    ChrTalk(
        0xA,
        (
            "病院で使う備品の多くは、\x01",
            "ハロルドさんという商人と\x01",
            "主に取引きしていたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xA,
        (
            "今はもっぱら、国防軍の支給品に\x01",
            "頼っている状況でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xA,
        (
            "あまりいい品質とは言えないけど、\x01",
            "この状況じゃ仕方ないだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3845")

    label("loc_37B9")


    #C0108
    ChrTalk(
        0xA,
        (
            "今、病院で使う備品の多くは、\x01",
            "国防軍の支給品に頼っている状況でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xA,
        (
            "あまりいい品質とは言えないけど、\x01",
            "この状況じゃ仕方ないだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3845")

    Jump("loc_3D27")

    label("loc_384A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_39D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3950")

    #C0110
    ChrTalk(
        0xA,
        (
            "クロスベル市の襲撃だなんて、\x01",
            "本当にとんでもない事件が\x01",
            "起こってしまったものだよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xA,
        (
            "あれから１週間近く経つとはいえ、\x01",
            "まだショックは拭い去れないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xA,
        (
            "復興は進んでるとはいえ、\x01",
            "クロスベルは立ち直ることが\x01",
            "できるんだろうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_39CD")

    label("loc_3950")


    #C0113
    ChrTalk(
        0xA,
        (
            "復興は進んでるとはいえ、\x01",
            "襲撃事件のショックは\x01",
            "本当に大きいと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xA,
        (
            "クロスベルは立ち直ることが\x01",
            "できるんだろうか……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_39CD")

    Jump("loc_3D27")

    label("loc_39D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_39E0")
    Jump("loc_3D27")

    label("loc_39E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3A55")

    #C0115
    ChrTalk(
        0xA,
        (
            "このコンテナ……\x01",
            "中から魔除けの人形が\x01",
            "どっさり出てきてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        (
            "……なんで\x01",
            "こんなものがあるんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D27")

    label("loc_3A55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3B81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3B1E")

    #C0117
    ChrTalk(
        0xA,
        (
            "街では独立提唱の話題で\x01",
            "もちきりなんだってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xA,
        (
            "クロスベルの住民としては、\x01",
            "ある意味悲願とも言える\x01",
            "ことだからねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xA,
        (
            "僕も独立には、ぜひとも\x01",
            "賛成したいところだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3B7C")

    label("loc_3B1E")


    #C0120
    ChrTalk(
        0xA,
        (
            "僕も独立には、ぜひとも\x01",
            "賛成したいところだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xA,
        (
            "住民投票には\x01",
            "忘れずに参加しないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B7C")

    Jump("loc_3D27")

    label("loc_3B81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3B8F")
    Jump("loc_3D27")

    label("loc_3B8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3D1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C81")

    #C0122
    ChrTalk(
        0xA,
        (
            "レミフェリア公国では、\x01",
            "大公家が医療の分野に\x01",
            "特に力を入れているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xA,
        (
            "医療先進国レミフェリア。\x01",
            "君も聞いた事があるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xA,
        (
            "うーむ、そんな国に住んでたら\x01",
            "病気の心配なんてしなくても\x01",
            "よさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3D19")

    label("loc_3C81")


    #C0125
    ChrTalk(
        0xA,
        (
            "レミフェリア公国では、\x01",
            "大公家が医療の分野に\x01",
            "特に力を入れているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xA,
        (
            "うーむ、そんな国に住んでたら\x01",
            "病気の心配なんてしなくても\x01",
            "よさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D19")

    Jump("loc_3D27")

    label("loc_3D1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3D27")

    label("loc_3D27")

    TalkEnd(0xFE)
    Return()

    # Function_12_369F end

    def Function_13_3D2B(): pass

    label("Function_13_3D2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E71")

    #C0127
    ChrTalk(
        0xB,
        "……………………\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x101,
        "#00005Fセイランド教授……？\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x0, 500)

    #C0129
    ChrTalk(
        0xB,
        "……ああ、お前たちか。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xB,
        (
            "悪いが今は忙しい。\x01",
            "１人にしておいてくれるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#00108F（やっぱり、シズクちゃんの\x01",
            "  手術のことで悩んでるのかしら……）\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        (
            "#00003F（ああ、執刀医は\x01",
            "  彼女だったって話だしな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xB, 0xB4, 0x0)
    SetScenarioFlags(0x0, 4)
    Jump("loc_3ECB")

    label("loc_3E71")


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
            "#00003F（考え事をしているみたいだ。\x01",
            "  ……邪魔しちゃ悪いな。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECB")

    TalkEnd(0xFE)
    Return()

    # Function_13_3D2B end

    def Function_14_3ECF(): pass

    label("Function_14_3ECF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EE4")
    Call(0, 15)
    Jump("loc_3F84")

    label("loc_3EE4")


    #C0135
    ChrTalk(
        0xC,
        (
            "#03605Fところで……\x01",
            "今回のシーツの数量は\x01",
            "３０枚で良かったでしょうか？\x02\x03",

            "#03600F以前、５０枚のところを\x01",
            "５００枚と発注されたことが\x01",
            "ありましたし、念のため……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F84")

    TalkEnd(0xFE)
    Return()

    # Function_14_3ECF end

    def Function_15_3F88(): pass

    label("Function_15_3F88")

    OP_4B(0x8, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0136
    ChrTalk(
        0x8,
        (
            "や、ハロルドさんじゃないか。\x01",
            "今日は何しにきたんだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        (
            "#03600Fええ、注文されていたシーツを\x01",
            "お届けにあがりました。\x02\x03",

            "さっそく納品したいのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x8,
        (
            "ああ、それじゃあちょっと\x01",
            "運び入れを手伝うとするかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xC,
        "#03609Fはは、いつもすみません。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    OP_4C(0x8, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_15_3F88 end

    def Function_16_4097(): pass

    label("Function_16_4097")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_41D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4166")

    #C0140
    ChrTalk(
        0xFE,
        (
            "おかげで医療物資を\x01",
            "無事に届けることができたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "このクロスベルの非常時に、\x01",
            "ひでえヤツがいたもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "ま、捕まってくれて\x01",
            "ひと安心したけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_41CE")

    label("loc_4166")


    #C0143
    ChrTalk(
        0xFE,
        (
            "このクロスベルの非常時に、\x01",
            "ひでえヤツがいたもんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "ま、捕まってくれて\x01",
            "ひと安心したけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_41CE")

    Jump("loc_431A")

    label("loc_41D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_431A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42AA")

    #C0145
    ChrTalk(
        0xFE,
        (
            "くそっ、この非常時に\x01",
            "医療物資を届けてやれないなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "……いや、終わっちまったことを\x01",
            "ウジウジ言っても仕方ねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "あんたたちも気にせずに、\x01",
            "頭を切り替えて仕事してくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_431A")

    label("loc_42AA")


    #C0148
    ChrTalk(
        0xFE,
        (
            "終わっちまったことを\x01",
            "ウジウジ言っても仕方ねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "あんたたちも気にせずに、\x01",
            "頭を切り替えて仕事してくれ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_431A")

    TalkEnd(0xFE)
    Return()

    # Function_16_4097 end

    def Function_17_431E(): pass

    label("Function_17_431E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_43A7")

    #C0150
    ChrTalk(
        0xF,
        (
            "こちらは、アルバート大公の\x01",
            "送迎用リムジンです。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xF,
        (
            "閣下にはアリオスさんが\x01",
            "護衛についていますし、\x01",
            "私どもも安心ですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_43A7")

    TalkEnd(0xFE)
    Return()

    # Function_17_431E end

    def Function_18_43AB(): pass

    label("Function_18_43AB")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_43DD")
    SetScenarioFlags(0x31, 2)

    label("loc_43DD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4423")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_441D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4412")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_4418")

    label("loc_4412")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_4418")

    Jump("loc_4423")

    label("loc_441D")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_4423")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_46E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_449C")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_447C"),
        (SWITCH_DEFAULT, "loc_448D"),
    )


    label("loc_447C")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_4497")

    label("loc_448D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4497")

    Jump("loc_46DB")

    label("loc_449C")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_44D0")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_44D0")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4504"),
        (1, "loc_4608"),
        (2, "loc_4699"),
        (SWITCH_DEFAULT, "loc_46D1"),
    )


    label("loc_4504")

    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    OP_74(0x8, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_4535")
    OP_70(0x8, 0x12C)
    OP_71(0x8, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_4545")

    label("loc_4535")

    OP_70(0x8, 0xF0)
    OP_71(0x8, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_4545")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_459B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_459B")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45BE")
    Sound(461, 0, 100, 0)

    label("loc_45BE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_45DE")
    OP_70(0x8, 0x14A)
    OP_71(0x8, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_45EE")

    label("loc_45DE")

    OP_70(0x8, 0x10E)
    OP_71(0x8, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_45EE")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x8, "light", 0x1, 0x1)
    OP_70(0x8, 0x0)
    Jump("loc_4423")

    label("loc_4608")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_467A")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_463D")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_4655")

    label("loc_463D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_4650")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_4655")

    label("loc_4650")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_4655")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4694")

    label("loc_467A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_468A")
    OP_AF(0xFB)
    Jump("loc_4694")

    label("loc_468A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4694")

    Jump("loc_46DB")

    label("loc_4699")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46B2")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_46CC")

    label("loc_46B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_46C2")
    OP_AF(0xFB)
    Jump("loc_46CC")

    label("loc_46C2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46CC")

    Jump("loc_46DB")

    label("loc_46D1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_46DB")

    Jump("loc_4423")

    label("loc_46E0")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_18_43AB end

    def Function_19_46EE(): pass

    label("Function_19_46EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_4736")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力バスは運行を見合わせているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_4736")

    Call(0, 6)
    Return()

    # Function_19_46EE end

    def Function_20_473A(): pass

    label("Function_20_473A")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0153
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4809")
    OP_E2(0x2)
    MiniGame(0x6, 0x11, 0xFFFFBFBE, 0xFFFFFC18, 0xFFFF9A5C, 0xB4, 0xFFFFBCE4, 0xFFFFF830, 0xFFFF7FFE)

    label("loc_4809")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_473A end

    def Function_21_480E(): pass

    label("Function_21_480E")

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
        "#00005F#5Pおっと……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 0)

    def lambda_4994():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4994)

    #C0156
    ChrTalk(
        0x102,
        "#00105F#12P他の部署からの連絡かしら？\x02",
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
            "#00000F#30Wはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("逞しい声")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ウフフっ……\x01",
            "アタシよ、アタシ。\x02\x03",

            "誰だか判るかしら？\x02",
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
            "#00012Fミシェルさん……\x01",
            "えっと、どうしたんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ウフフ、一発で判るなんて\x01",
            "なかなか冴えてるじゃない。\x02\x03",

            "それとも愛のなせる業かしら？\x02",
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
            "#00006Fいえ、ミシェルさん以外に\x01",
            "該当者が思いつかなかっただけで。\x02\x03",

            "#00000Fひょっとして、そちらに伺ってる\x01",
            "キーアのことですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0162
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あ、それなんだけど。\x02\x03",

            "あの子、シズクちゃんを連れて\x01",
            "港湾区に遊びに行っちゃったわ。\x02\x03",

            "ツァイトだったかしら？\x01",
            "あの警察犬が一緒だったから\x01",
            "大丈夫だとは思うんだけど。\x02",
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
            "#00002Fああ、ツァイトが一緒なら\x01",
            "何の心配もいらないと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0164
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あら、やっぱり？\x02\x03",

            "話は聞いていたけど、\x01",
            "カレ、すっごく貫禄があるわね。\x02\x03",

            "さすが伝説の《神狼》と\x01",
            "言われてるだけはあるじゃない？\x02",
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
            "#00004Fハハ……さすがに伝説の狼とは\x01",
            "別物だとは思いますけど。\x02\x03",

            "#00005Fあ、わざわざその事を\x01",
            "知らせてくれたんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0166
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ううん、こちらが本題なんだけど。\x02\x03",

            "実は、アリオスがアナタたちと\x01",
            "情報交換がしたいらしいのよ。\x02\x03",

            "夕方くらいに戻って来るんだけど\x01",
            "何とか時間が取れないかしら？\x02",
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
            "#00000F夕方ですか……\x01",
            "それだったら大丈夫かと。\x02\x03",

            "情報交換ということは、\x01",
            "やはり通商会議についてですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0168
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それもあるけど……\x01",
            "《黒月》と《赤い星座》に関してね。\x02",
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
            "#00003F……判りました。\x02\x03",

            "#00001F一通り用事を済ませたら\x01",
            "そちらに伺います。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ミシェルの声")

    #A0170
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ええ、待ってるわ。\x07\x00\x02",
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
            "#00100F#12P遊撃士協会の\x01",
            "ミシェルさんからみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        "#00305F#11P何かあったのかよ？\x02",
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
        "#00006F#5Pいや、情報交換の申し出さ。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0174
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはミシェルの用件について\x01",
            "他のメンバーに説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0175
    ChrTalk(
        0x104,
        (
            "#00303F#11P《黒月》と《赤い星座》か……\x02\x03",

            "#00301F確かにアリオスのオッサンなら\x01",
            "自治州外の情報にも詳しそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x105,
        (
            "#10304F#11Pフフ、渡りに舟かもしれないね。\x02\x03",

            "#10300Fそれじゃあ今から\x01",
            "クロスベル市に戻るのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x101,
        (
            "#00000F#5Pいや、アリオスさんが\x01",
            "戻ってくるのは夕方らしい。\x02\x03",

            "それまでは、こちらの用事を\x01",
            "済ませていても大丈夫だろう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14F, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x149, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5370")

    #C0178
    ChrTalk(
        0x102,
        (
            "#00104F#12P《赤い星座》の情報は\x01",
            "一通り集められたけど……\x02\x03",

            "#00102Fせっかく車があるから\x01",
            "まだ色々回っても良さそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53EC")

    label("loc_5370")


    #C0179
    ChrTalk(
        0x102,
        (
            "#00103F#12P《赤い星座》の情報も\x01",
            "それほど集まっていないし……\x02\x03",

            "#00100Fせっかく車があるから\x01",
            "色々回ってみても良さそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53EC")


    #C0180
    ChrTalk(
        0x109,
        (
            "#10100F#11Pそれでは、用事を済ませたら\x01",
            "東通りのギルドに行きましょう。\x02",
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

    # Function_21_480E end

    def Function_22_5476(): pass

    label("Function_22_5476")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_22_5476 end

    def Function_23_5486(): pass

    label("Function_23_5486")

    Sleep(50)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_23_5486 end

    def Function_24_5499(): pass

    label("Function_24_5499")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_24_5499 end

    def Function_25_54AC(): pass

    label("Function_25_54AC")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_25_54AC end

    def Function_26_54BF(): pass

    label("Function_26_54BF")

    Sleep(200)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
    Return()

    # Function_26_54BF end

    def Function_27_54D2(): pass

    label("Function_27_54D2")

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
            "#00208F#6Pやっぱり普段よりも\x01",
            "お見舞い客が多そうですね……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_594D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_594D)
    Sleep(150)

    def lambda_595D():
        OP_93(0xFE, 0x10F, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_595D)
    Sleep(100)

    def lambda_596D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_596D)
    Sleep(50)

    def lambda_597D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_597D)
    Sleep(50)

    def lambda_598D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_598D)
    Sleep(50)

    def lambda_599D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_599D)
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
            "#00106F#11Pええ、重傷を負った人が\x01",
            "市内だけでも大勢いるから……\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00008F#11P……ドノバン警部や\x01",
            "イリアさんも入院してるんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x109,
        (
            "#10106F#6Pはい……２人ともまだ\x01",
            "昏睡状態のままだそうです。\x02\x03",

            "#10108Fドノバン警部は……\x01",
            "フランたちを庇ったらしくて。\x02\x03",

            "フランの回復が早かったのも\x01",
            "警部のおかげだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        "#00006F#11Pそっか……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x104,
        (
            "#00306F#5P豪快なオッサンだったが……\x01",
            "大したもんだよな。\x02\x03",

            "#00308Fできればイリアさん共々、\x01",
            "様子を見舞えるといいんだが……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x192, 4)), scpexpr(EXPR_END)), "loc_5BE0")

    #C0187
    ChrTalk(
        0x102,
        (
            "#00103F#11Pそうね……\x01",
            "シュリちゃんが今日は\x01",
            "来ているみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BFB")

    label("loc_5BE0")


    #C0188
    ChrTalk(
        0x102,
        "#00103F#11Pそうね……\x02",
    )

    CloseMessageWindow()

    label("loc_5BFB")


    def lambda_5C00():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 3, lambda_5C00)
    Sleep(250)

    #C0189
    ChrTalk(
        0x105,
        (
            "#10300F#5Pそれで、\x01",
            "妹さんの病室はどこだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x109,
        (
            "#10105F#6Pあ、うん……３０１だけど。\x02\x03",

            "#10100Fその前に、受付に一言、\x01",
            "言った方がいいかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x101,
        (
            "#00000F#11P分かった、行ってみよう。\x02\x03",

            "#00003F（……セシル姉も相当、\x01",
            "  忙しくしてるんだろうな。）\x02",
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

    # Function_27_54D2 end

    def Function_28_5D66(): pass

    label("Function_28_5D66")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5D82():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5D82)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, -9000, 4000, 0x0)
    Sleep(500)
    BeginChrThread(0x1D, 1, 0, 31)
    OP_95(0xFE, -24000, 0, -3750, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1750, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1750, 4000, 0x0)

    def lambda_5E14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5E14)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_28_5D66 end

    def Function_29_5E4A(): pass

    label("Function_29_5E4A")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5E66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5E66)
    OP_95(0xFE, -22000, 0, 1750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 3750, 4000, 0x0)
    OP_95(0xFE, -24000, 0, 11000, 4000, 0x0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)

    def lambda_5EC8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5EC8)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_29_5E4A end

    def Function_30_5F01(): pass

    label("Function_30_5F01")

    Sleep(1000)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0x5, 0x0, 0x8)
    OP_79(0x1)
    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_5F35():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5F35)
    OP_95(0xFE, -24000, 0, 3500, 4000, 0x0)
    OP_71(0x1, 0x5, 0x0, 0x0, 0x8)
    OP_95(0xFE, -22000, 0, 1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, 1500, 4000, 0x0)

    def lambda_5F8E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_5F8E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    SetChrFlags(0xFE, 0x4)
    BeginChrThread(0x1B, 1, 0, 29)
    Return()

    # Function_30_5F01 end

    def Function_31_5FC1(): pass

    label("Function_31_5FC1")

    ClearChrFlags(0xFE, 0x4)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_95(0xFE, -24000, 0, -3500, 4000, 0x0)
    OP_95(0xFE, -22000, 0, -1500, 4000, 0x0)
    OP_95(0xFE, 2000, 0, -1500, 4000, 0x0)

    def lambda_6019():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6019)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
    OP_64(0xFE)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_31_5FC1 end

    def Function_32_603D(): pass

    label("Function_32_603D")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x960, 0x0)
    OP_93(0xFE, 0x10E, 0x3E8)
    Sleep(1000)
    OP_93(0xFE, 0x5A, 0x3E8)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x960, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_608B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_608B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x9C4, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_32_603D end

    def Function_33_60AC(): pass

    label("Function_33_60AC")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x4A38, 0x6D6, 0x0)

    def lambda_60C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_60C5)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x6D6, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_33_60AC end

    def Function_34_60E6(): pass

    label("Function_34_60E6")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC0, 0x3E8, 0x0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x8)
    OP_79(0x2)

    def lambda_6114():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6114)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_34_60E6 end

    def Function_35_6135(): pass

    label("Function_35_6135")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x6F54, 0x3E8, 0x0)

    def lambda_614E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_614E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x3E8, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_35_6135 end

    def Function_36_616F(): pass

    label("Function_36_616F")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x8CA0, 0x5DC, 0x0)

    def lambda_6188():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6188)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x5DC, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_36_616F end

    def Function_37_61A9(): pass

    label("Function_37_61A9")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x578, 0x0)

    def lambda_61C2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_61C2)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x578, 0x0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_37_61A9 end

    def Function_38_61F8(): pass

    label("Function_38_61F8")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0x9858, 0x44C, 0x0)

    def lambda_6211():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_6211)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x44C, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_38_61F8 end

    def Function_39_6232(): pass

    label("Function_39_6232")

    ClearChrFlags(0xFE, 0x4)
    OP_9B(0x0, 0xFE, 0x0, 0xA028, 0x44C, 0x0)

    def lambda_624B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_624B)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x4B0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_39_6232 end

    def Function_40_626C(): pass

    label("Function_40_626C")

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

    def lambda_636E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_636E)
    Sleep(100)

    def lambda_6386():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6386)
    Sleep(50)

    def lambda_639E():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_639E)
    Sleep(50)

    def lambda_63B6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_63B6)
    Sleep(50)

    def lambda_63CE():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63CE)
    Sleep(50)

    def lambda_63E6():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_63E6)
    OP_68(-48920, 1000, -570, 2700)
    SetCameraDistance(19720, 2700)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_6440():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6440)
    Sleep(300)

    def lambda_6450():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6450)
    Sleep(300)

    def lambda_6460():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6460)
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
            "#00005Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年の声")

    #A0193
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あー、いたいた。\x02\x03",

            "今、どこにいんのさ。\x02",
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
            "#00003Fあのな……\x01",
            "こういう時はちゃんと\x01",
            "名乗るのが礼儀だろ？\x02\x03",

            "#00000Fウルスラ病院だけど……\x01",
            "どうしたんだ、ヨナ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0195
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アンタら、確か今日から\x01",
            "支援業務に戻ってんだろ？\x02\x03",

            "ちょっとボクの頼みを\x01",
            "聞いてくんないかな～って。\x02",
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
            "#00006Fいや、だから勝手に警察の\x01",
            "データベースを覗くなって……\x02\x03",

            "#00001Fそれにこっちだって\x01",
            "忙しいのは忙しいんだから──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0197
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフン、この前、\x01",
            "行方不明の遊撃士の捜索を\x01",
            "手伝ってやったのは誰だよ？\x02\x03",

            "借り、返すって言ってたよな～？\x02",
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
            "#00013Fぐっ……\x02\x03",

            "#00006F……仕方ない。\x01",
            "何でもは引き受けられないけど\x01",
            "話だけは聞いておこうか。\x02\x03",

            "#00000Fどこまで行けばいいんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0199
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "だったら港湾区にある\x01",
            "灯台の前まで来てくれよ。\x02\x03",

            "そこで待ってるからさ♪\x02",
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
            "#00005F灯台？\x01",
            "何だってそんな場所で……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフン、来てのお楽しみだって。\x02\x03",

            "そんじゃあ待ってるぜー。\x02",
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
            "#00011F#2Pあっ……まったく。\x02",
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
            "#00211F#11Pまたヨナが勝手なことを\x01",
            "言い出したんですか？\x02",
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
        "#00012F#6Pいや、まあ……\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0205
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "港湾区の波止場にある\x01",
            "灯台前に呼ばれたことを話した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0206
    ChrTalk(
        0x104,
        (
            "#00305F#5Pハア？\x01",
            "何だってそんな場所で……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x105,
        (
            "#10300F#11P港湾区の灯台というと、\x01",
            "爆破された《黒月》の建物の\x01",
            "わりと近くだったね。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x102,
        (
            "#00103F#5P確かに、リンさんたちの\x01",
            "調査も手伝ってもらったし……\x02\x03",

            "#00100F話を聞いてあげるくらいは\x01",
            "いいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        (
            "#10100F#11P一区切り付いたら\x01",
            "さっそく行ってみましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x101,
        "#00000F#6Pああ、そうしよう。\x02",
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x103,
        (
            "#00206F#11Pまあ、こちらの都合を聞かずに\x01",
            "勝手に言ってきたことですから。\x02\x03",

            "#00211F多少待たせても問題はないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0x104,
        "#00309F#5Pハハ、それもそうだな。\x02",
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

    # Function_40_626C end

    def Function_41_6C64(): pass

    label("Function_41_6C64")

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
        "#00013F（国防軍の部隊が……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0214
    AnonymousTalk(
        0x105,
        (
            "#10401F（警備中かな……？\x01",
            "  タイミングが悪かったね。）\x02",
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

    # Function_41_6C64 end

    def Function_42_6D7F(): pass

    label("Function_42_6D7F")

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

    # Function_42_6D7F end

    def Function_43_6E1D(): pass

    label("Function_43_6E1D")

    OP_74(0xD, 0x1E)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    SetMapObjFrame(0xD, "light", 0x0, 0x1)
    SetMapObjFrame(0xD, "mark00", 0x0, 0x1)
    Return()

    # Function_43_6E1D end

    def Function_44_6E49(): pass

    label("Function_44_6E49")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_44_6E49 end

    def Function_45_6E54(): pass

    label("Function_45_6E54")

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
        "#5Pはあ、暇だよなー。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x12,
        (
            "#5Pこんな場所を警備なんて\x01",
            "タイクツすぎるっての。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x13,
        "#6Pボヤくなって。\x02",
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x13,
        (
            "#6P例の支援課のバニングスが\x01",
            "逃亡したままなんだからな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x13, 500)
    Sleep(100)

    #C0219
    ChrTalk(
        0x12,
        (
            "#5Pハッ、たかが捜査官１人に\x01",
            "何が出来るってんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x12,
        (
            "#5Pとっくに外国あたりに\x01",
            "逃げ出してるんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x14,
        (
            "#12Pしかし、とんでもない化物を\x01",
            "連れてるって噂だが……\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x14,
        (
            "#12P第４連隊の連中が\x01",
            "喰われたってのは本当なのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x14, 500)
    Sleep(100)

    #C0223
    ChrTalk(
        0x12,
        "#5Pハハ、ただのデマだろ。\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x12,
        (
            "#5Pそんな事より、せっかくだから\x01",
            "イリアの顔を拝みたいよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x12,
        "#5P確か、まだ入院してるんだろ？\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x15,
        "#11Pああ、そのはずだぜ。\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x15,
        (
            "#11Pとっとと怪我を治してもらって\x01",
            "復活して欲しいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #N0228
    NpcTalk(
        0x101,
        "ロイドの声",
        "#11P──それは同感だよ。\x02",
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

    def lambda_72A0():
        OP_93(0x12, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_72A0)
    Sleep(50)

    def lambda_72B0():
        OP_93(0x13, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_72B0)
    Sleep(50)

    def lambda_72C0():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_72C0)
    Sleep(50)

    def lambda_72D0():
        OP_93(0x15, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_72D0)
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
        "#11Pロイド・バニングス！？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x13,
        "#11Pくっ、本当に現れるとは！\x02",
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
            "#01203F#6P#3Cやれやれ。\x01",
            "化物とは失敬な。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x105,
        (
            "#10402F#6Pいや、あの元の姿を見たら\x01",
            "さすがに仕方ないんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x101,
        (
            "#00003F#6P──争うつもりはない。\x02\x03",

            "#00007Fだが、立ち塞がるのなら\x01",
            "遠慮なく撃破させてもらう！\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x14,
        "#11P生意気な……！\x02",
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x13,
        (
            "#11P少数だ！\x01",
            "一気に制圧するぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x12,
        "#11P了解#4Rラジャー#！\x02",
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

    # Function_45_6E54 end

    def Function_46_7559(): pass

    label("Function_46_7559")

    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_46_7559 end

    def Function_47_757B(): pass

    label("Function_47_757B")

    Sleep(50)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_47_757B end

    def Function_48_75A0(): pass

    label("Function_48_75A0")

    Sleep(100)
    SetChrFlags(0xFE, 0x1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x24)
    SetChrSubChip(0xFE, 0x0)
    ClearChrFlags(0xFE, 0x1000)
    Return()

    # Function_48_75A0 end

    def Function_49_75C5(): pass

    label("Function_49_75C5")

    SetChrChipByIndex(0x12, 0x27)
    SetChrSubChip(0x12, 0x0)
    OP_9B(0x1, 0xFE, 0xA, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_49_75C5 end

    def Function_50_75DD(): pass

    label("Function_50_75DD")

    SetChrChipByIndex(0x13, 0x29)
    SetChrSubChip(0x13, 0x0)
    OP_9B(0x1, 0xFE, 0x15E, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_50_75DD end

    def Function_51_75F5(): pass

    label("Function_51_75F5")

    SetChrChipByIndex(0x14, 0x26)
    SetChrSubChip(0x14, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_51_75F5 end

    def Function_52_760D(): pass

    label("Function_52_760D")

    SetChrChipByIndex(0x15, 0x29)
    SetChrSubChip(0x15, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1388, 0x1)
    Return()

    # Function_52_760D end

    def Function_53_7625(): pass

    label("Function_53_7625")

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
        "#40W#11P……ぐうっ……\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x13,
        "#40W#11Pつ、強い……\x02",
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
        "#10404F#5Pさて──僕の出番かな。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-54200, 800, 860, 1200)
    MoveCamera(36, 25, 0, 1200)
    OP_6E(500, 1200)
    SetCameraDistance(20500, 1200)

    def lambda_7A08():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7A08)
    OP_9B(0x0, 0x105, 0x0, 0x190, 0x3E8, 0x0)
    Sleep(300)
    BeginChrThread(0x105, 0, 0, 54)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    Sleep(500)

    #C0240
    ChrTalk(
        0x101,
        "#00005F#12P（星杯のメダル……？）\x02",
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
            "#10403F#30W#5P#40A我が深淵にて煌く\x01",
            "蒼金#4Rあおがね#の刻印よ……\x02",
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
            "#10401F#30W#5P#51A識#2Rしき#の銀耀と結び付きて、\x01",
            "偽りの記憶を彼らに与えよ。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 59)
    Sleep(800)

    #C0243
    ChrTalk(
        0x13,
        "#50W#11P#2S…………あ、\x02",
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
        "#00011F#12P（これは……）\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x107,
        (
            "#01203F#3C#6P（ふむ、教会に伝わる\x01",
            "  暗示の術のたぐいのようだ。）\x02\x03",

            "#01200F（何やら不思議な力も\x01",
            "  使っているようだが……）\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x105,
        (
            "#10403F#5P──君たちは先ほど、\x01",
            "大型の幻獣の接近を確認した。\x02\x03",

            "何とか撃退したはいいが、\x01",
            "全員が負傷してしまったため\x01",
            "一時的に帰投することになった。\x02\x03",

            "#10401Fバニングスの姿は見ていないし、\x01",
            "当分現れそうな気配もない。\x02",
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
        "#50W#11P#2S……………………（コクコク）\x02",
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
        "#50W#11P#2S……現れそうな気配もない。\x02",
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

    def lambda_7DC2():

        label("loc_7DC2")

        TurnDirection(0xFE, 0x15, 500)
        Yield()
        Jump("loc_7DC2")

    QueueWorkItem2(0x105, 3, lambda_7DC2)
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
        "#00006F#11Pす、凄いな……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x107,
        (
            "#01203F#12P#3Cただの暗示の術ならば\x01",
            "あそこまで具体的に操れまい。\x02\x03",

            "#01200F察するに《聖痕#4Rスティグマ#》の力を\x01",
            "利用したというところか。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x105,
        (
            "#10404F#5Pハハ……\x01",
            "さすが伝説の聖獣だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        "#00001F#11P《聖痕#4Rスティグマ#》……？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x105,
        (
            "#10406F#5P……ま、ちょっとした\x01",
            "昔のトラウマってところさ。\x02\x03",

            "#10408Fいずれにせよ、完璧ではないから\x01",
            "２、３日で暗示は解けるだろう。\x02\x03",

            "#10401F軍も警戒してくるだろうから\x01",
            "今後は使えないと思って欲しいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x101,
        "#00003F#11Pそうか……了解だ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_C9(0x0, 0x80000000)

    #N0256
    NpcTalk(
        0x103,
        "少女の声",
        "#6P#2686V#30W#20Aワジさん、ツァイト……？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)

    def lambda_80AE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_80AE)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x107, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-44070, 400, 120, 2000)
    MoveCamera(76, 17, 0, 2000)
    OP_6E(500, 2000)
    SetCameraDistance(19770, 2000)

    def lambda_8126():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8126)
    Sleep(50)

    def lambda_8136():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8136)
    Sleep(50)

    def lambda_8146():
        OP_93(0x107, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_8146)
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
        "#00005F#11P#12P#Nティオ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0259
    ChrTalk(
        0x107,
        "#01200F#2P#3C#6P#Nフム、無事のようだな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0260
    ChrTalk(
        0x105,
        "#10404F#6P#Nやれやれ、一安心だね。\x02",
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
            "#00014F#6Pよかった……！\x01",
            "病院にいるっていうから\x01",
            "一体どうしたのかと……\x02\x03",

            "#00002F大丈夫か？\x01",
            "ケガとかしていないか？\x02",
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
        "#00213F#11P#2687V#50W#28A#2S……ロイド……さん………\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0263
    ChrTalk(
        0x103,
        "#00212F#11P#2688V#20W#4S#15A#4Sロイドさんっ……！！\x02",
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

    def lambda_8450():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8450)

    def lambda_845D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_845D)
    OP_6F(0x79)
    SetCameraDistance(15500, 40000)

    #C0264
    ChrTalk(
        0x101,
        (
            "#00011F#6Pうぐっ……\x01",
            "（きょ、胸甲が……）\x02",
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
            "#00213F#11P#2689V#60W#25Aい、今までどこに……！\x02\x03",

            "#00215F#2690V#25A拘置所に捕まってるって聞いて……！\x02\x03",

            "#00212F#2691V#87A……だ、脱走して\x01",
            "軍の人たちに追われてるって……\x01",
            "ど、導力ネットで、見かけて……！\x02\x03",

            "#00213F#2692V#55Aわ、わたし……ヒック……\x01",
            "………ずっと心配で…………っ！\x02",
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
        "#00008F#6Pティオ……\x02",
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
            "#00006F#6P……ゴメン。\x01",
            "心配させちゃったみたいだな。\x02\x03",

            "#00002Fでも、もう大丈夫だから。\x02\x03",

            "ツァイトやワジの助けを借りて\x01",
            "クロスベルに戻って来たから……\x02\x03",

            "#00004Fだから……安心してくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x80000000)

    #C0268
    ChrTalk(
        0x103,
        "#00215F#11P#2693V#40W#28A……ううっ……ぐすっ……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #N0269
    NpcTalk(
        0x17,
        "娘の声",
        (
            "#11P#2724V#30W#N#29Aうわわっ……\x01",
            "ラブラブですねー。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #N0270
    NpcTalk(
        0x16,
        "女性の声",
        (
            "#11P#N#48A#30Wふふっ、お邪魔するのは\x01",
            "ちょっと気が咎めるけど……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-52280, 1200, -1700, 2500)
    SetCameraDistance(17000, 2500)

    def lambda_87C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_87C5)

    def lambda_87D6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_87D6)
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
            "#00002F#6Pセシル姉！\x01",
            "それに……フラン！\x02",
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
            "#2725V#30Wえへへ……\x01",
            "お久しぶりです、ロイドさん！\x02",
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
            "#30W本当によく無事で……\x02\x03",

            "……心配したわ、ロイド。\x02",
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
            "#00006F#6Pゴメン……\x01",
            "みんなに心配をかけて。\x02\x03",

            "#00002Fでもフラン。\x01",
            "すっかり元気みたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x17,
        (
            "#06409F#11Pはい、もうとっくに\x01",
            "ケガも全快しちゃってます！\x02\x03",

            "#06406Fまあクロスベルが\x01",
            "あんな事になってしまったので\x01",
            "職場復帰は出来てませんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#00006F#6Pそうか……\x01",
            "でも本当に良かった。\x02",
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
            "#00215F#11P#30W……ところで。\x01",
            "ワジさんのその格好は？\x02\x03",

            "#00216Fツァイトも今までどこに……\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x105,
        "#10404F#6Pフフ、まあ色々あってね。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x107,
        (
            "#01200F#6P#3Cとりあえず今までの経緯を\x01",
            "一通り説明させてもらおう。\x02",
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
        "#01305F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x17,
        "#06411F#11Pい、今のって……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x103,
        "#00205F#11P？　どうしたんですか？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        "#00012F#6Pいや、どうしたって……\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x105,
        (
            "#10402F#6Pハハ、ひょっとして\x01",
            "いつも言葉が分かってたから\x01",
            "気付いていないとか？\x02",
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
            "#00205F#11P#4Sツァ、ツァイト！？\x02\x03",

            "#00207Fどうして人間の言葉を\x01",
            "喋ってるんですか───！？\x02",
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

    # Function_53_7625 end

    def Function_54_8DB0(): pass

    label("Function_54_8DB0")

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

    # Function_54_8DB0 end

    def Function_55_8DDF(): pass

    label("Function_55_8DDF")

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

    # Function_55_8DDF end

    def Function_56_8E13(): pass

    label("Function_56_8E13")

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

    # Function_56_8E13 end

    def Function_57_8EA3(): pass

    label("Function_57_8EA3")

    Sleep(300)

    label("loc_8EA6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8EF0")
    PlayEffect(0x0, 0xFF, 0x105, 0x3, 0, 1050, 800, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_8EA6")

    label("loc_8EF0")

    Return()

    # Function_57_8EA3 end

    def Function_58_8EF1(): pass

    label("Function_58_8EF1")

    EndChrThread(0xFE, 0x2)
    Sleep(300)
    StopEffect(0x2, 0x2)
    StopSound(852, 500, 90)
    Sleep(300)
    Return()

    # Function_58_8EF1 end

    def Function_59_8F05(): pass

    label("Function_59_8F05")


    def lambda_8F0A():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_8F0A)
    Sleep(200)

    def lambda_8F26():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_8F26)
    Sleep(200)

    def lambda_8F42():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_8F42)
    Sleep(200)

    def lambda_8F5E():
        OP_A6(0xFE, 0x1E, 0x0, 0xFA, 0xBB8)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8F5E)
    Sleep(200)
    Return()

    # Function_59_8F05 end

    def Function_60_8F76(): pass

    label("Function_60_8F76")

    Sleep(250)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
    Return()

    # Function_60_8F76 end

    def Function_61_8F85(): pass

    label("Function_61_8F85")

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

    # Function_61_8F85 end

    def Function_62_900E(): pass

    label("Function_62_900E")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_62_900E end

    def Function_63_9013(): pass

    label("Function_63_9013")

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

    # Function_63_9013 end

    def Function_64_90B9(): pass

    label("Function_64_90B9")

    SetChrSubChip(0xFE, 0x1)
    Return()

    # Function_64_90B9 end

    def Function_65_90BE(): pass

    label("Function_65_90BE")

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

    # Function_65_90BE end

    def Function_66_9140(): pass

    label("Function_66_9140")

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

    def lambda_91BE():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x384, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_91BE)
    Sleep(300)
    Sound(463, 0, 100, 0)
    OP_71(0xD, 0x1F, 0x3C, 0x1, 0x8)
    OP_79(0xD)
    Return()

    # Function_66_9140 end

    def Function_67_91E7(): pass

    label("Function_67_91E7")

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

    # Function_67_91E7 end

    def Function_68_927E(): pass

    label("Function_68_927E")


    def lambda_9283():

        label("loc_9283")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9283")

    QueueWorkItem2(0xFE, 2, lambda_9283)
    Sleep(400)
    OP_9B(0x1, 0xFE, 0x5A, 0x6D6, 0x7D0, 0x0)
    Return()

    # Function_68_927E end

    def Function_69_92A3(): pass

    label("Function_69_92A3")


    def lambda_92A8():

        label("loc_92A8")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_92A8")

    QueueWorkItem2(0xFE, 2, lambda_92A8)
    Sleep(100)
    OP_9B(0x1, 0xFE, 0x5A, 0x4E2, 0x3E8, 0x0)
    Return()

    # Function_69_92A3 end

    def Function_70_92C8(): pass

    label("Function_70_92C8")

    Sleep(600)
    OP_9B(0x0, 0xFE, 0x5A, 0x1F4, 0x7D0, 0x1)
    OP_9D(0xFE, 0xFFFF259A, 0x0, 0xFFFFF7CC, 0x15E, 0x5DC)
    OP_9B(0x0, 0xFE, 0x0, 0xFA, 0x3E8, 0x1)

    def lambda_9305():

        label("loc_9305")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_9305")

    QueueWorkItem2(0xFE, 2, lambda_9305)
    Return()

    # Function_70_92C8 end

    def Function_71_9313(): pass

    label("Function_71_9313")

    OP_9B(0x0, 0xFE, 0x0, 0x2198, 0x1770, 0x0)
    BeginChrThread(0xFE, 3, 0, 75)
    Sound(811, 0, 50, 0)
    Sound(898, 0, 100, 0)
    BeginChrThread(0x101, 3, 0, 76)

    def lambda_933F():
        OP_A6(0xFE, 0x0, 0x1E, 0x1F4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_933F)
    Sleep(100)

    def lambda_935B():
        OP_A6(0xFE, 0x0, 0x14, 0x190, 0x3E8)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_935B)
    Return()

    # Function_71_9313 end

    def Function_72_9370(): pass

    label("Function_72_9370")

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

    # Function_72_9370 end

    def Function_73_93AA(): pass

    label("Function_73_93AA")

    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_73_93AA end

    def Function_74_93BA(): pass

    label("Function_74_93BA")

    Sleep(100)
    OP_9B(0x0, 0xFE, 0x163, 0x1F40, 0x7D0, 0x0)
    Return()

    # Function_74_93BA end

    def Function_75_93CD(): pass

    label("Function_75_93CD")

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

    # Function_75_93CD end

    def Function_76_93F1(): pass

    label("Function_76_93F1")

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

    # Function_76_93F1 end

    def Function_77_9415(): pass

    label("Function_77_9415")

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

    # Function_77_9415 end

    def Function_78_9439(): pass

    label("Function_78_9439")

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

    # Function_78_9439 end

    def Function_79_945D(): pass

    label("Function_79_945D")

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
            "その後、ロイドたちはツァイトと合流し……\x02\x03",

            "セシルにも別れを告げてウルスラ病院を後にした。\x07\x00\x02",
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
            "──帰り際、ワジが病院前に\x01",
            "七耀脈の力場の“隙間”を見つけ……\x02\x03",

            "“法陣”で固定することで\x01",
            "《メルカバ》に迎えに来てもらう事が\x01",
            "可能になるのだった。\x07\x00\x02",
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
            "ティオとフランが参加した事により\x01",
            "メルカバ内の端末で、手配魔獣などの要請を\x01",
            "受けることが出来るようになりました。\x02\x03",

            "キャビンにある端末が利用できるので\x01",
            "活用してください。\x07\x00\x02",
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

    # Function_79_945D end

    def Function_80_99D2(): pass

    label("Function_80_99D2")

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

    # Function_80_99D2 end

    def Function_81_9A2D(): pass

    label("Function_81_9A2D")

    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(1000)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_81_9A2D end

    def Function_82_9A47(): pass

    label("Function_82_9A47")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(900)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_82_9A47 end

    def Function_83_9A64(): pass

    label("Function_83_9A64")

    Sleep(300)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(800)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_83_9A64 end

    def Function_84_9A81(): pass

    label("Function_84_9A81")

    Sleep(500)
    OP_93(0xFE, 0x10E, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_84_9A81 end

    def Function_85_9A9B(): pass

    label("Function_85_9A9B")

    Sleep(400)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x7D0, 0x1)
    Return()

    # Function_85_9A9B end

    def Function_86_9AB8(): pass

    label("Function_86_9AB8")

    OP_96(0xFE, 0xFFFF4480, 0x251C, 0x4268, 0xBB8, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2328, 0x4268, 0x7D0, 0x1)
    OP_96(0xFE, 0xFFFF4480, 0x2134, 0x4268, 0x3E8, 0x1)
    Return()

    # Function_86_9AB8 end

    def Function_87_9AF5(): pass

    label("Function_87_9AF5")

    Return()

    # Function_87_9AF5 end

    def Function_88_9AF6(): pass

    label("Function_88_9AF6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9B10")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x1, 0x2, 0x1)
    Jump("Function_88_9AF6")

    label("loc_9B10")

    Return()

    # Function_88_9AF6 end

    def Function_89_9B11(): pass

    label("Function_89_9B11")

    SetMapObjFrame(0xF, "Null_fream", 0x2, "start")
    Sleep(20000)
    SetMapObjFrame(0xF, "Null_fream", 0x2, "loop")
    Return()

    # Function_89_9B11 end

    def Function_90_9B3C(): pass

    label("Function_90_9B3C")

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

    def lambda_9C38():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C38)
    Sleep(50)

    def lambda_9C55():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9C55)
    Sleep(50)

    def lambda_9C72():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9C72)
    Sleep(50)

    def lambda_9C8F():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9C8F)
    Sleep(50)

    def lambda_9CAC():
        OP_97(0xFE, 0x1F40, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9CAC)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    OP_6F(0x1)
    Sleep(500)

    #N0289
    NpcTalk(
        0x16,
        "女性の声",
        "……ロイド……！？\x02",
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
        "#00002Fあ……！\x02",
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

    def lambda_9DDD():
        OP_95(0xFE, -21270, 0, -10, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9DDD)
    Sleep(50)

    def lambda_9DFA():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9DFA)
    Sleep(50)

    def lambda_9E17():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9E17)
    Sleep(50)

    def lambda_9E34():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9E34)
    Sleep(50)

    def lambda_9E51():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9E51)
    Sleep(50)

    def lambda_9E6E():
        OP_97(0xFE, 0x2AF8, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9E6E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x16, 1)

    #C0291
    ChrTalk(
        0x101,
        (
            "#6P#00009Fセシル姉……\x01",
            "はは、いきなり会えたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x16,
        (
            "#11P#01300Fふふ……お帰りなさい、ロイド。\x02\x03",

            "#01309Fエリィさん、ランディ君や\x01",
            "ノエルさんも……\x01",
            "みんな、元気にしてたかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x102,
        "#6P#00100Fふふ、ご無沙汰してます。\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        "#6P#00309Fお久しぶりッス、セシルさん！\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x109,
        (
            "#5P#10109Fふふっ、本当に久しぶりですね。\x02\x03",

            "#10100Fあたしとは教団事件で\x01",
            "病院が襲撃された時に\x01",
            "お会いして以来でしたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x16,
        "#11P#01309Fふふ……そうだったわね。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x105,
        "#6P#10302Fへえ、この人が噂のお姉さんかい？\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0298
    ChrTalk(
        0x16,
        (
            "#11P#01305Fあら、見かけない子もいるみたいだけど……\x02\x03",

            "#01300Fもしかして、ノエルさんとあなたが\x01",
            "噂の新メンバーになるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、そういうことになるかな。\x02\x03",

            "#10302F僕はワジ・ヘミスフィア。\x01",
            "今後ともよろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x16,
        (
            "#11P#01309Fふふ、よろしくね。\x02\x03",

            "#01300Fそれじゃあ……わたしの方も\x01",
            "改めて自己紹介させてもらおうかしら。\x02",
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
            "こほん……\x01",
            "このウルスラ病院に勤める、\x01",
            "看護師のセシル・ノイエスです。\x02\x03",

            "ふふ、私の可愛い弟のロイドを、\x01",
            "どうかよろしくお願いしますね。\x02",
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
            "#6P#00006Fセシル姉ってば……\x01",
            "厳密には姉弟じゃないだろ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 500)
    Sleep(500)

    #C0303
    ChrTalk(
        0x101,
        (
            "#6P#00000Fコホン、えっと……\x01",
            "子供のころから何かと\x01",
            "お世話になっている人なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x16,
        "#11P#01306Fもう、ロイドったら照れちゃって。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(500)

    #C0305
    ChrTalk(
        0x101,
        "#6P#00012Fて、照れてるわけじゃないって。\x02",
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
            "#11P#01304Fうーん、それにしても……\x01",
            "ワジ君もノエルさんも\x01",
            "とっても美人よねえ。\x02\x03",

            "#01300Fロイド、そろそろ\x01",
            "お付き合いする相手は\x01",
            "誰か決まったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x109,
        "#5P#10105Fお、お付き合い！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0308
    ChrTalk(
        0x101,
        (
            "#6P#00006Fセシル姉……前にも言ったけど、\x01",
            "支援課はそういうのじゃないから。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x16,
        (
            "#11P#01305Fはっ……そうよね。\x01",
            "私としたことが配慮が足りなかったわ。\x02\x03",

            "#01303F今この場にティオちゃんがいないのに\x01",
            "そういう話をするのも不公平よね。\x02\x03",

            "#01300Fティオちゃんが帰ってきてから、\x01",
            "ゆっくりとパートナーを選んで……\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        (
            "#6P#00011Fだ、だから……\x01",
            "なんでそうなるんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        (
            "#6P#00109Fふふ、なんだか\x01",
            "セシルさんを見ると安心するわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x104,
        "#6P#00309Fおお、天然ぶりも健在みたいだしな。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        "#11P#00006Fツッコむ側の身にもなってくれ……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x16,
        (
            "#11P#01304Fふふ……それにしても、\x01",
            "そんなに長い間離れていないのに\x01",
            "随分と懐かしい気がするわね。\x02\x03",

            "#01300Fちょうど私も休憩時間なの。\x01",
            "よかったら一緒にお茶でもどうかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x101,
        (
            "#6P#00004Fそれじゃあ、せっかくだし……\x02\x03",

            "#00002Fみんな、お言葉に\x01",
            "甘えさせてもらおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x109,
        "#5P#10109Fはい、ご一緒させていただきます！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("t1510", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_90_9B3C end

    def Function_91_A83B(): pass

    label("Function_91_A83B")

    Return()

    # Function_91_A83B end

    def Function_92_A83C(): pass

    label("Function_92_A83C")

    EventBegin(0x0)
    Fade(500)
    OP_68(-47260, 1700, -1110, 0)
    MoveCamera(44, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x106, -48500, 0, -230, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_AA4E")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x102, -46300, 0, -1330, 90)
    SetChrPos(0x103, -46300, 0, 870, 90)
    SetChrPos(0x104, -48400, 0, 1030, 90)

    def lambda_A8D4():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A8D4)

    def lambda_A8EE():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A8EE)

    def lambda_A908():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A908)

    def lambda_A922():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A922)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A972")
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_A95D():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A95D)

    label("loc_A972")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9AD")
    SetChrPos(0x105, -48000, 0, -1070, 90)

    def lambda_A998():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A998)

    label("loc_A9AD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A9E8")
    SetChrPos(0x10A, -48000, 0, -1070, 90)

    def lambda_A9D3():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_A9D3)

    label("loc_A9E8")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA21")
    WaitChrThread(0x109, 1)

    label("loc_AA21")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA35")
    WaitChrThread(0x105, 1)

    label("loc_AA35")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AA49")
    WaitChrThread(0x10A, 1)

    label("loc_AA49")

    Jump("loc_AD3A")

    label("loc_AA4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_AB5C")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x105, -48400, 0, 1030, 90)
    SetChrPos(0x109, -48000, 0, -1070, 90)

    def lambda_AAB1():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AAB1)

    def lambda_AACB():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_AACB)

    def lambda_AAE5():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AAE5)

    def lambda_AAFF():
        OP_95(0xFE, -46400, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AAFF)

    def lambda_AB19():
        OP_95(0xFE, -46000, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AB19)
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
    Jump("loc_AD3A")

    label("loc_AB5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_AC6A")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x104, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)
    SetChrPos(0x105, -48300, 0, -1070, 90)

    def lambda_ABBF():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ABBF)

    def lambda_ABD9():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ABD9)

    def lambda_ABF3():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ABF3)

    def lambda_AC0D():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AC0D)

    def lambda_AC27():
        OP_95(0xFE, -46300, 0, -1070, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AC27)
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
    Jump("loc_AD3A")

    label("loc_AC6A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_AD3A")
    SetChrPos(0x101, -46100, 0, -230, 90)
    SetChrPos(0x103, -46300, 0, -1330, 90)
    SetChrPos(0x105, -46300, 0, 870, 90)
    SetChrPos(0x107, -48800, 0, 1030, 90)

    def lambda_ACBC():
        OP_95(0xFE, -44100, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ACBC)

    def lambda_ACD6():
        OP_95(0xFE, -44300, 0, -1330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_ACD6)

    def lambda_ACF0():
        OP_95(0xFE, -44300, 0, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ACF0)

    def lambda_AD0A():
        OP_95(0xFE, -46800, 0, 1030, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_AD0A)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)

    label("loc_AD3A")


    #C0317
    ChrTalk(
        0x106,
        (
            "#6P#10708Fすみません、私は病院の外で\x01",
            "待たせていただきます。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_AEE5")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ADF8")

    def lambda_AD99():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AD99)
    Sleep(50)

    def lambda_ADA9():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ADA9)
    Sleep(50)

    def lambda_ADB9():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ADB9)
    Sleep(50)

    def lambda_ADC9():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_ADC9)
    Sleep(50)

    def lambda_ADD9():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ADD9)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_ADF8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE6C")

    def lambda_AE0D():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AE0D)
    Sleep(50)

    def lambda_AE1D():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AE1D)
    Sleep(50)

    def lambda_AE2D():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AE2D)
    Sleep(50)

    def lambda_AE3D():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AE3D)
    Sleep(50)

    def lambda_AE4D():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AE4D)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_AE6C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEE0")

    def lambda_AE81():
        TurnDirection(0x10A, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_AE81)
    Sleep(50)

    def lambda_AE91():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AE91)
    Sleep(50)

    def lambda_AEA1():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AEA1)
    Sleep(50)

    def lambda_AEB1():
        TurnDirection(0x102, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AEB1)
    Sleep(50)

    def lambda_AEC1():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AEC1)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)

    label("loc_AEE0")

    Jump("loc_B022")

    label("loc_AEE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_AF57")

    def lambda_AEF3():
        TurnDirection(0x109, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_AEF3)
    Sleep(50)

    def lambda_AF03():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AF03)
    Sleep(50)

    def lambda_AF13():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF13)
    Sleep(50)

    def lambda_AF23():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF23)
    Sleep(50)

    def lambda_AF33():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF33)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_B022")

    label("loc_AF57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_AFC9")

    def lambda_AF65():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_AF65)
    Sleep(50)

    def lambda_AF75():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AF75)
    Sleep(50)

    def lambda_AF85():
        TurnDirection(0x104, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF85)
    Sleep(50)

    def lambda_AF95():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF95)
    Sleep(50)

    def lambda_AFA5():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AFA5)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    Jump("loc_B022")

    label("loc_AFC9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_B022")

    def lambda_AFD7():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_AFD7)
    Sleep(50)

    def lambda_AFE7():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_AFE7)
    Sleep(50)

    def lambda_AFF7():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AFF7)
    Sleep(50)

    def lambda_B007():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B007)
    Sleep(50)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)

    label("loc_B022")


    #C0318
    ChrTalk(
        0x101,
        (
            "#11P#00003Fああ、分かった。\x01",
            "また後でな。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B08C")
    RemoveParty(0x6, 0xFF)
    AddParty(0x6, 0xFF, 0xFF)

    label("loc_B08C")

    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -44100, 0, -230, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_B0BE")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_B0BE")

    EventEnd(0x5)
    Return()

    # Function_92_A83C end

    def Function_93_B0C1(): pass

    label("Function_93_B0C1")

    EventBegin(0x0)
    Fade(500)
    OP_68(-49470, 1000, -560, 0)
    MoveCamera(46, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18720, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 1)), scpexpr(EXPR_END)), "loc_B1B5")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x102, -46820, 0, -830, 270)
    SetChrPos(0x103, -46820, 0, 370, 270)
    SetChrPos(0x104, -45620, 0, -1030, 270)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B164")
    SetChrPos(0x109, -45620, 0, 570, 270)

    label("loc_B164")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B185")
    SetChrPos(0x105, -45620, 0, 570, 270)

    label("loc_B185")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B1A6")
    SetChrPos(0x10A, -45620, 0, 570, 270)

    label("loc_B1A6")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_B2DC")

    label("loc_B1B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A3, 3)), scpexpr(EXPR_END)), "loc_B222")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x109, -45620, 0, -1030, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_B2DC")

    label("loc_B222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_B28F")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x104, -46820, 0, 370, 270)
    SetChrPos(0x105, -45620, 0, 570, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_B2DC")

    label("loc_B28F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_END)), "loc_B2DC")
    SetChrPos(0x101, -48020, 0, -230, 270)
    SetChrPos(0x103, -46820, 0, -830, 270)
    SetChrPos(0x105, -46820, 0, 370, 270)
    SetChrPos(0x107, -45320, 0, -1230, 270)

    label("loc_B2DC")

    OP_4B(0xD, 0xFF)
    OP_0D()

    #C0319
    ChrTalk(
        0xD,
        (
            "#6P#10702Fおかえりなさい、皆さん。\x01",
            "……用事は済みましたか？\x02",
        )
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        "#11P#00000Fああ、行くとしよう。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A2, 7)), scpexpr(EXPR_END)), "loc_B3A2")
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)

    label("loc_B3A2")

    EventEnd(0x5)
    Return()

    # Function_93_B0C1 end

    def Function_94_B3A5(): pass

    label("Function_94_B3A5")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B450")
    SetChrPos(0x109, -51500, 0, -1420, 90)

    label("loc_B450")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B471")
    SetChrPos(0x105, -51500, 0, -1420, 90)

    label("loc_B471")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B492")
    SetChrPos(0x10A, -51500, 0, -1420, 90)

    label("loc_B492")

    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)

    def lambda_B4AB():
        OP_95(0xFE, -44520, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B4AB)
    Sleep(30)

    def lambda_B4C8():
        OP_95(0xFE, -44520, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B4C8)
    Sleep(30)

    def lambda_B4E5():
        OP_95(0xFE, -44520, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B4E5)
    Sleep(30)

    def lambda_B502():
        OP_95(0xFE, -45820, 0, 1110, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B502)
    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B544")

    def lambda_B52F():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B52F)

    label("loc_B544")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B56E")

    def lambda_B559():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B559)

    label("loc_B56E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B598")

    def lambda_B583():
        OP_95(0xFE, -45820, 0, -1420, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B583)

    label("loc_B598")

    Sleep(30)

    def lambda_B5A0():
        OP_95(0xFE, -48500, 0, -230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B5A0)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    #C0321
    ChrTalk(
        0x106,
        (
            "#6P#10703Fそれでは皆さん。\x01",
            "私はここで……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_B5F9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B5F9)

    def lambda_B606():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B606)

    def lambda_B613():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B613)

    def lambda_B620():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B620)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B645")

    def lambda_B63D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B63D)

    label("loc_B645")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B662")

    def lambda_B65A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B65A)

    label("loc_B662")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B67F")

    def lambda_B677():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_B677)

    label("loc_B67F")

    WaitChrThread(0x104, 1)
    Sleep(500)

    #C0322
    ChrTalk(
        0x102,
        "#11P#00105Fリーシャさん……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        "#5P#00303Fふう……まあ仕方ねぇか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0324
    ChrTalk(
        0x101,
        (
            "#11P#00003F……なあ、リーシャ。\x02\x03",

            "#00000Fせめてイリアさんの声だけでも\x01",
            "聞いて行かないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0325
    ChrTalk(
        0x106,
        "#6P#10705F…………ぇ……………\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x101,
        (
            "#11P#00003F全てのケリを付けるまで\x01",
            "イリアさんには会わない……\x02\x03",

            "君のその気持ちは分かるし、\x01",
            "尊重したいとも思うけど……\x02\x03",

            "#00000Fせめて、病室の外から\x01",
            "俺たちとイリアさんが話しているのを\x01",
            "聞くくらいはいいんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x106,
        (
            "#6P#10705Fあ……\x02\x03",

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
            "#5P#00302Fだな、そのくらいの\x01",
            "ご褒美があってもいいだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x103,
        (
            "#11P#00203Fここから先、まだまだ困難が\x01",
            "待ち受けている可能性は高そうですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x102,
        (
            "#11P#00100F大切な人の声を聞くことは\x01",
            "きっと力になってくれると思うわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BA41")

    #C0331
    ChrTalk(
        0x109,
        (
            "#11P#10105Fそうですよ、リーシャさん！\x02\x03",

            "#10101Fリーシャさんがいるって事は\x01",
            "バレないように気を付けますから！\x02\x03",

            "#10104Fその、あたしもフランと会えて\x01",
            "ずいぶん元気付けられましたし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BA41")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BAFC")

    #C0332
    ChrTalk(
        0x105,
        (
            "#11P#10404Fフフ、いいんじゃないかな？\x02\x03",

            "#10400F本当の意味で再会しなければ\x01",
            "君の誓いは守れるだろうし。\x02\x03",

            "#10408F……本当に会えなくなってからじゃ\x01",
            "手遅れってこともあるよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BAFC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BBAE")

    #C0333
    ChrTalk(
        0x10A,
        (
            "#11P#00603F《銀#2Rイン#》──\x01",
            "いや、リーシャ・マオ。\x02\x03",

            "#00600F警察官の私が言うのも何だが\x01",
            "今は非常時だ。\x02\x03",

            "#00602Fせめて悔いの残らないように\x01",
            "するがいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BBAE")

    Sleep(1500)
    OP_64(0x106)

    #C0334
    ChrTalk(
        0x106,
        (
            "#6P#10704F……みなさん。\x01",
            "ありがとうございます。\x02\x03",

            "#10702F……お言葉に甘えて……\x01",
            "病室前まではご一緒させてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x101,
        "#11P#00002Fああ……！\x02",
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x102,
        "#11P#00100Fええ、分かったわ……！\x02",
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

    # Function_94_B3A5 end

    def Function_95_BCA2(): pass

    label("Function_95_BCA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 4)), scpexpr(EXPR_END)), "loc_C3C8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BCC0")
    Call(0, 96)
    Jump("loc_C3C3")

    label("loc_BCC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1FE")

    #C0337
    ChrTalk(
        0x10,
        (
            "#01300Fロイド……アリオスさんを\x01",
            "打ち破ったみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#00000Fああ、さすがに相当苦戦したけど……\x01",
            "皆と力を合わせたおかげだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x102,
        (
            "#00103F共に高めあう好敵手であり\x01",
            "越えるべき《壁》でもあった\x01",
            "アリオスさん……\x02\x03",

            "#00100F正直、誰か１人でも欠けてたら\x01",
            "絶対に敵わなかったと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        "#00304F……だな。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x10,
        (
            "#01309Fふふ、あなたたちは全員で\x01",
            "『支援課』なんでしょう？\x01",
            "充分に誇っていいと思うわ。\x02",
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
            "#01304Fアリオスさんと話したことは\x01",
            "そこまで多くはなかったけど……\x02\x03",

            "あの人は昔からずっと、\x01",
            "心の中に重い物を\x01",
            "背負っていたような気がする。\x02\x03",

            "#01308Fシズクちゃんや奥さん、\x01",
            "ガイさんのことも１人で背負って……\x01",
            "とても見ていられないくらいだった。\x02\x03",

            "#01300Fあの人は際限なく強い人だから、\x01",
            "誰かに頼るということも\x01",
            "出来なかったんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x103,
        (
            "#00200F強さゆえの孤独……\x01",
            "確かにそうかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x10,
        (
            "#01302Fふふ、だけどあなた達と\x01",
            "全力で戦って敗れたことで、\x01",
            "きっとそれからも解放されたと思う。\x02\x03",

            "#01304Fガイさんも心配していたろうし、\x01",
            "彼の婚約者として、私が代わりに\x01",
            "お礼を言わせてもらうわ。\x02\x03",

            "#01309Fガイさんの親友、アリオスさんを\x01",
            "救ってくれてありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x101,
        (
            "#00004Fはは……どういたしまして。\x02\x03",

            "#00000Fあとはキーアを取り戻すだけだ。\x01",
            "待っていてくれ、セシル姉。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x10,
        (
            "#01300Fええ、分かったわ。\x02\x03",

            "#01303Fロイド、みんな……\x01",
            "最後まで気をつけて。\x02\x03",

            "#01302Fキーアちゃんと一緒に\x01",
            "笑顔で戻ることを、\x01",
            "ここで祈っているから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1AC, 5)
    Jump("loc_C3C3")

    label("loc_C1FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C34F")

    #C0347
    ChrTalk(
        0x10,
        (
            "#01303Fロイド、みんな……\x01",
            "最後まで気をつけて。\x02\x03",

            "#01302Fキーアちゃんと一緒に\x01",
            "笑顔で戻ることを、\x01",
            "ここで祈っているから。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#00000Fああ、待っていてくれ。\x02\x03",

            "#00003F（……兄貴の事件の真実も\x01",
            "  とりあえずは判明したけど……\x01",
            "  今、言うべきじゃなさそうだ。）\x02\x03",

            "#00008F（イアン先生にも、改めて\x01",
            "  事情を聞いてみないとな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_C3C3")

    label("loc_C34F")


    #C0349
    ChrTalk(
        0x10,
        (
            "#01303Fロイド、みんな……\x01",
            "最後まで気をつけて。\x02\x03",

            "キーアちゃんと一緒に\x01",
            "笑顔で戻ることを、\x01",
            "ここで祈っているから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3C3")

    Jump("loc_C654")

    label("loc_C3C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_C62F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3E3")
    Call(0, 96)
    Jump("loc_C62A")

    label("loc_C3E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C5BA")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C50A")
    TurnDirection(0x10, 0x106, 0)

    #C0350
    ChrTalk(
        0x10,
        (
            "#01300Fリーシャさん、あなたもどうか\x01",
            "気をつけてちょうだいね。\x02\x03",

            "#01304Fイリアも直接口には出さないけど、\x01",
            "あなたの事はいつだって\x01",
            "気にかけていると思うから。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C4CF")

    #C0351
    ChrTalk(
        0x106,
        "#10708F……そうですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_C505")

    label("loc_C4CF")


    #C0352
    ChrTalk(
        0x106,
        (
            "#10702Fはい……！\x01",
            "きっと無事に戻ると約束します。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C505")

    Jump("loc_C5B2")

    label("loc_C50A")


    #C0353
    ChrTalk(
        0x10,
        (
            "#01300Fキーアちゃんと一緒に、\x01",
            "全員が無事に帰ってくる約束……\x01",
            "絶対に忘れないでね。\x02\x03",

            "#01304Fその約束がある限り、\x01",
            "私はここでみんなの帰りを\x01",
            "待っていられると思うから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C5B2")

    SetScenarioFlags(0x0, 7)
    Jump("loc_C62A")

    label("loc_C5BA")


    #C0354
    ChrTalk(
        0x10,
        (
            "#01300F私はここで、\x01",
            "みんなの帰りを待っているわ。\x02\x03",

            "#01304Fロイドたちに、女神様のご加護が\x01",
            "ありますように……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C62A")

    Jump("loc_C654")

    label("loc_C62F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 2)), scpexpr(EXPR_END)), "loc_C63D")
    Jump("loc_C654")

    label("loc_C63D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_END)), "loc_C64B")
    Jump("loc_C654")

    label("loc_C64B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_C654")

    label("loc_C654")

    TalkEnd(0xFE)
    Return()

    # Function_95_BCA2 end

    def Function_96_C658(): pass

    label("Function_96_C658")

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
        "#5P#00000Fセシル姉……ここにいたのか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x10, 0x101, 300)

    #C0356
    ChrTalk(
        0x10,
        (
            "#12P#01300Fええ、突然あんなものが\x01",
            "現れたから驚いてしまって……\x02\x03",

            "#01304F……でも、不思議な樹ね。\x02\x03",

            "明らかに異質な存在なのに、\x01",
            "なんだか愛しいような……\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x102,
        (
            "#5P#00108F（ベルはあの《大樹》を\x01",
            "  『キーアちゃんそのもの』と\x01",
            "  言っていた……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C8A2")

    #C0358
    ChrTalk(
        0x105,
        (
            "#11P#10403F（彼女ならそれを感じても\x01",
            "  おかしくないかもね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C969")

    label("loc_C8A2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C909")

    #C0359
    ChrTalk(
        0x109,
        (
            "#11P#10103F（セシルさんならそれを感じても\x01",
            "  おかしくないかもしれませんね。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C969")

    label("loc_C909")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_C969")

    #C0360
    ChrTalk(
        0x106,
        (
            "#11P#10703F（セシルさんならそれを感じても\x01",
            "  おかしくないかもしれません。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C969")

    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    #C0361
    ChrTalk(
        0x10,
        (
            "#12P#01303Fロイド、それにみんな……\x02\x03",

            "#01301F……あの場所に向かうのね？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x101,
        (
            "#5P#00003F……ああ。\x02\x03",

            "#00001Fあの《大樹》には全ての真実と……\x01",
            "キーアが待っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x102,
        (
            "#5P#00101Fこの先どんな危険があるとしても、\x01",
            "私たちは行かなければなりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x10,
        "#12P#01308Fそう……\x02",
    )

    CloseMessageWindow()
    OP_63(0x10, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10)

    #C0365
    ChrTalk(
        0x10,
        (
            "#12P#01303F本当なら、ロイドたちには\x01",
            "そんな危険を冒してほしくない……\x02\x03",

            "#01308F私は、一度大事な人を失っているから。\x01",
            "……あんな気持ちはもう味わいたくないわ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CB7F")

    #C0366
    ChrTalk(
        0x106,
        "#11P#10705Fセシルさん……\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBEE")

    label("loc_CB7F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBB9")

    #C0367
    ChrTalk(
        0x10A,
        "#11P#00608F…………………………\x02",
    )

    CloseMessageWindow()
    Jump("loc_CBEE")

    label("loc_CBB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CBEE")

    #C0368
    ChrTalk(
        0x105,
        "#11P#10408F…………………………\x02",
    )

    CloseMessageWindow()

    label("loc_CBEE")


    #C0369
    ChrTalk(
        0x10,
        (
            "#12P#01303F……でも、ガイさんが生きてたら……\x01",
            "きっとロイドたちと\x01",
            "同じ事をしようとしてたと思う。\x02\x03",

            "#01302Fそこにどんな危険があっても、\x01",
            "大切なものを守るために\x01",
            "飛び込んでいったと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x101,
        "#5P#00000Fセシル姉……\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x10,
        (
            "#12P#01304F……だからみんな、\x01",
            "ひとつだけ約束して。\x02\x03",

            "#01300Fキーアちゃんを含めて、\x01",
            "全員が無事に帰ってくる事を。\x02\x03",

            "#01309Fその約束がある限り、\x01",
            "私はここでみんなの帰りを\x01",
            "待っていられると思うから。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x101,
        (
            "#5P#00005Fセシル姉……\x02\x03",

            "#00004F……分かった。\x01",
            "もう少しだけ待っていてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x103,
        (
            "#11P#00200F相当厳しい試練には\x01",
            "なるでしょうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x102,
        (
            "#5P#00102Fええ、キーアちゃんを取り戻して\x01",
            "絶対に帰ってきます。\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x104,
        (
            "#5P#00309Fあのアリオスのオッサンも\x01",
            "叩きなおしてやんねえといけねえしな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CED7")

    #C0376
    ChrTalk(
        0x10A,
        "#11P#00602Fああ、もちろんだ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF40")

    label("loc_CED7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF0F")

    #C0377
    ChrTalk(
        0x109,
        "#11P#10102Fええ、そうですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_CF40")

    label("loc_CF0F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_CF40")

    #C0378
    ChrTalk(
        0x105,
        "#11P#10402Fフフ、そうだね。\x02",
    )

    CloseMessageWindow()

    label("loc_CF40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x6D), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_D1D0")

    #C0379
    ChrTalk(
        0x10,
        (
            "#12P#01304F……ふふ、ありがとうみんな。\x01",
            "これでようやく安心できるわ。\x02",
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
            "#12P#01309Fそれじゃあ、約束の印として\x01",
            "これを渡しておこうかしら。\x02",
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
            "を手に入れた。\x02",
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
        "#5P#00005Fこれは……？\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x10,
        (
            "#12P#01300F私が看護師の試験を受ける時に\x01",
            "ガイさんが渡してくれたものなの。\x02\x03",

            "#01304F辛いとき、握り締めると\x01",
            "不思議と勇気がわいてくる……\x01",
            "そんなお守りよ。\x02\x03",

            "#01300Fとっても大切なものだから、\x01",
            "無事に戻ってきっと返しに来てね。\x02",
        )
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x101,
        (
            "#5P#00000F……ああ、分かった。\x01",
            "ありがたく借りさせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x10,
        (
            "#12P#01309Fふふ、ロイドたちに\x01",
            "女神様のご加護が\x01",
            "ありますように……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D254")

    label("loc_D1D0")


    #C0386
    ChrTalk(
        0x10,
        (
            "#12P#01304F……ふふ、ありがとうみんな。\x01",
            "これでようやく安心できるわ。\x02\x03",

            "#01309Fロイドたちに、女神様のご加護が\x01",
            "ありますように……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D254")

    OP_5A()
    SetScenarioFlags(0x1AC, 4)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24090, -1000, -22920, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1AD, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BC, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D9, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DE, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D29D")
    OP_E0(0x34, 0x0)

    label("loc_D29D")

    EventEnd(0x5)
    Return()

    # Function_96_C658 end

    def Function_97_D2A0(): pass

    label("Function_97_D2A0")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D32B")

    #C0387
    ChrTalk(
        0x101,
        (
            "#00000Fフランが準備を済ませるまで、\x01",
            "病院を出るわけにはいかないな。\x02\x03",

            "イリアさんやドノバン警部の\x01",
            "お見舞いをしてこよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D32B")

    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_97_D2A0 end

    def Function_98_D342(): pass

    label("Function_98_D342")

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

    # Function_98_D342 end

    def Function_99_D398(): pass

    label("Function_99_D398")

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
            "～ビュッフェ《レクチェ》～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_99_D398 end

    SaveToFile()

Try(main)
