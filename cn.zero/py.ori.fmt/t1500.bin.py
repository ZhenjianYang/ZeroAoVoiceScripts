from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t1500.bin",                # FileName
        "t1500",                    # MapName
        "t1500",                    # Location
        0x004D,                     # MapIndex
        "ed7123",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1500",                  # 0
        "警备员托尼",             # 1
        "艾达护士",               # 2
        "勤杂工戴森",             # 3
        "米海尔",                 # 4
        "住院患者",               # 5
        "女孩",                   # 6
        "探视者",                 # 7
        "探视者",                 # 8
        "哈罗德",                 # 9
        "杰德",                   # 10
        "琴兹",                   # 11
        "凯特巡警",               # 12
        "彼德",                   # 13
        "特级钓师罗伊德",         # 14
        "玛丽亚贝尔",             # 15
        "盖里教授",               # 16
        "约亚西姆副教授",         # 17
        "游客奥希尔",             # 18
        "游客拉皮斯",             # 19
        "希伦护士",               # 20
        "巴士",                   # 21
        "巴士２",                 # 22
        "塞茜尔",                 # 23
        "滴",                     # 24
        "琪雅",                   # 25
        "亚里欧斯",               # 26
        "罗伯特事务长",           # 27
        "玛萨护士长",             # 28
        "职员",                   # 29
        "巴士乘客",               # 30
        "巴士乘客",               # 31
        "巴士乘客",               # 32
        "巴士乘客",               # 33
        "巴士乘客",               # 34
        "乌尔斯拉间道",           # 35
    ))

    AddCharChip((
        "chr/ch33400.itc",                   # 00
        "chr/ch22300.itc",                   # 01
        "chr/ch28600.itc",                   # 02
        "chr/ch29800.itc",                   # 03
        "chr/ch20200.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch34002.itc",                   # 06
        "chr/ch20400.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch09300.itc",                   # 09
        "chr/ch31700.itc",                   # 0A
        "apl/ch50385.itc",                   # 0B
        "chr/ch30600.itc",                   # 0C
        "apl/ch50165.itc",                   # 0D
        "apl/ch50169.itc",                   # 0E
        "chr/ch05500.itc",                   # 0F
        "chr/ch32702.itc",                   # 10
        "chr/ch07100.itc",                   # 11
        "chr/ch32302.itc",                   # 12
        "chr/ch34500.itc",                   # 13
        "chr/ch29900.itc",                   # 14
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

    DeclNpc(-47560,  0,       4000,    270,  261,  0x0, 0,   2,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-23040,  -1000,   -25909,  0,    257,  0x0, 0,   3,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-30000,  -1000,   -20299,  246,  389,  0x0, 0,   4,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(-31450,  -899,    -16190,  180,  469,  0x0, 0,   6,   0,   255, 255, 0,   9,   255,  0)
    DeclNpc(-25180,  -1000,   -26069,  180,  389,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(-22350,  0,       -1309,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-21309,  0,       2299,    90,   389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-28590,  0,       2440,    135,  389,  0x0, 0,   8,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52279,  0,       16629,   267,  389,  0x0, 0,   9,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-18430,  0,       -11560,  180,  389,  0x0, 0,   10,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-16340,  0,       -330,    45,   389,  0x0, 0,   11,  0,   0,   2,   0,   16,  255,  0)
    DeclNpc(-52270,  0,       13590,   305,  389,  0x0, 0,   12,  0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-21770,  -1000,   -26059,  180,  405,  0x0, 0,   13,  0,   255, 255, 0,   18,  255,  0)
    DeclNpc(-24059,  -1000,   -26069,  180,  405,  0x0, 0,   14,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(-51279,  0,       15350,   270,  389,  0x0, 0,   15,  0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-16829,  -1000,   -16360,  180,  469,  0x0, 0,   16,  0,   255, 255, 0,   20,  255,  0)
    DeclNpc(-29469,  -990,    -26069,  180,  389,  0x0, 0,   17,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-21010,  150,     -9489,   270,  405,  0x0, 0,   18,  0,   255, 255, 0,   23,  255,  0)
    DeclNpc(-9789,   0,       6489,    90,   385,  0x0, 0,   19,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-27200,  6000,    20219,   0,    389,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   0,   3,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 36,  -42.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.166666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 55,  -25.0,                 0.0,                   -1.0,                  5625.0,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.03333333134651184,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.0,                   -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 57,  -24.0,                 -17.0,                 -2.0,                  76.5625,               [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2857142686843872,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.800000190734863,     4.857142448425293,     0.4000000059604645,    1.0])
    DeclEvent(0x0000, 0, 58,  -42.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   14.166666984558105,    -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 59,  -47.5,                 0.0,                   -1.0,                  225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   15.833333969116211,    -0.0,                  0.20000000298023224,   1.0])

    DeclActor(-58000,  0,       4000,    1500,    -58000,  1500,    4000,    0x007C, 0,  32, 0x0000)
    DeclActor(-35100,  3000,    17000,   2000,    -35100,  4000,    17000,   0x007C, 0,  33, 0x0000)
    DeclActor(-36600,  3000,    25600,   2000,    -36600,  4000,    25600,   0x007C, 0,  34, 0x0000)
    DeclActor(-42000,  3000,    20600,   2000,    -42000,  4000,    20600,   0x007C, 0,  35, 0x0000)
    DeclActor(-16830,  -1000,   -27510,  1200,    -17180,  -2000,   -32770,  0x007C, 0,  31, 0x0000)
    DeclActor(-7880,   0,       6560,    1200,    -7880,   1500,    6560,    0x007C, 0,  65, 0x0000)
    DeclActor(-36860,  0,       14360,   1200,    -36860,  1500,    14360,   0x007C, 0,  66, 0x0000)
    DeclActor(-49630,  0,       17190,   1200,    -49630,  2000,    17190,   0x007C, 0,  30, 0x0000)
    DeclActor(-35100,  3000,    17000,   2000,    -35100,  4000,    17000,   0x007C, 0,  63, 0x0000)

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(-23.0, 0.0, 18.0, 0x0000, 0x0052, "")
    PlaceName(-57.900001525878906, 0.0, 4.199999809265137, 0x0000, 0x0055, "")
    PlaceName(-48.0, 0.0, 17.25, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_944",          # 00, 0
        "Function_1_9FC",          # 01, 1
        "Function_2_A5D",          # 02, 2
        "Function_3_A88",          # 03, 3
        "Function_4_AAE",          # 04, 4
        "Function_5_DBA",          # 05, 5
        "Function_6_1136",         # 06, 6
        "Function_7_1E86",         # 07, 7
        "Function_8_2C03",         # 08, 8
        "Function_9_3057",         # 09, 9
        "Function_10_3216",        # 0A, 10
        "Function_11_3577",        # 0B, 11
        "Function_12_3705",        # 0C, 12
        "Function_13_37AD",        # 0D, 13
        "Function_14_3807",        # 0E, 14
        "Function_15_39C7",        # 0F, 15
        "Function_16_3A8C",        # 10, 16
        "Function_17_3B1D",        # 11, 17
        "Function_18_3D6F",        # 12, 18
        "Function_19_3DD8",        # 13, 19
        "Function_20_3EE4",        # 14, 20
        "Function_21_4375",        # 15, 21
        "Function_22_4672",        # 16, 22
        "Function_23_4790",        # 17, 23
        "Function_24_497D",        # 18, 24
        "Function_25_4ABC",        # 19, 25
        "Function_26_4B77",        # 1A, 26
        "Function_27_4C90",        # 1B, 27
        "Function_28_4D25",        # 1C, 28
        "Function_29_52BD",        # 1D, 29
        "Function_30_53AC",        # 1E, 30
        "Function_31_53BA",        # 1F, 31
        "Function_32_5482",        # 20, 32
        "Function_33_55E9",        # 21, 33
        "Function_34_55ED",        # 22, 34
        "Function_35_564A",        # 23, 35
        "Function_36_56A9",        # 24, 36
        "Function_37_5DED",        # 25, 37
        "Function_38_64C7",        # 26, 38
        "Function_39_6592",        # 27, 39
        "Function_40_666A",        # 28, 40
        "Function_41_66FA",        # 29, 41
        "Function_42_6773",        # 2A, 42
        "Function_43_69BF",        # 2B, 43
        "Function_44_6B9B",        # 2C, 44
        "Function_45_7B4A",        # 2D, 45
        "Function_46_7BDC",        # 2E, 46
        "Function_47_7C49",        # 2F, 47
        "Function_48_827E",        # 30, 48
        "Function_49_8B60",        # 31, 49
        "Function_50_8BFF",        # 32, 50
        "Function_51_8C91",        # 33, 51
        "Function_52_8D23",        # 34, 52
        "Function_53_8DB5",        # 35, 53
        "Function_54_8E0A",        # 36, 54
        "Function_55_8E23",        # 37, 55
        "Function_56_9A78",        # 38, 56
        "Function_57_A533",        # 39, 57
        "Function_58_BCC1",        # 3A, 58
        "Function_59_BEA1",        # 3B, 59
        "Function_60_C477",        # 3C, 60
        "Function_61_C4A0",        # 3D, 61
        "Function_62_C4AB",        # 3E, 62
        "Function_63_CBB3",        # 3F, 63
        "Function_64_D056",        # 40, 64
        "Function_65_D3DC",        # 41, 65
        "Function_66_D42F",        # 42, 66
    ))


    def Function_0_944(): pass

    label("Function_0_944")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_984"),
        (1, "loc_990"),
        (2, "loc_99C"),
        (3, "loc_9A8"),
        (4, "loc_9B4"),
        (5, "loc_9C0"),
        (6, "loc_9CC"),
        (SWITCH_DEFAULT, "loc_9D8"),
    )


    label("loc_984")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_990")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_99C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9A8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9B4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9C0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9CC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9D8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9FB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9E4")

    label("loc_9FB")

    Return()

    # Function_0_944 end

    def Function_1_9FC(): pass

    label("Function_1_9FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A5C")
    OP_95(0xFE, -23040, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, 0, -6950, 2000, 0x0)
    OP_95(0xFE, -24930, -1000, -23250, 2000, 0x0)
    OP_95(0xFE, -23040, -1000, -23250, 2000, 0x0)
    Jump("Function_1_9FC")

    label("loc_A5C")

    Return()

    # Function_1_9FC end

    def Function_2_A5D(): pass

    label("Function_2_A5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A87")
    OP_94(0xFE, 0xFFFFB01E, 0xFFFFF8DA, 0xFFFFC9BE, 0x564, 0x3E8)
    Sleep(400)
    Jump("Function_2_A5D")

    label("loc_A87")

    Return()

    # Function_2_A5D end

    def Function_3_A88(): pass

    label("Function_3_A88")

    SetChrPos(0xFE, -58500, 0, 500, 4000)
    OP_97(0xFE, 0xFFFF8AD0, 0x0, 0x0, 0x1388, 0x0)
    Return()

    # Function_3_A88 end

    def Function_4_AAE(): pass

    label("Function_4_AAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_AC2")
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_B00")

    label("loc_AC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_AD0")
    Jump("loc_B00")

    label("loc_AD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_ADE")
    Jump("loc_B00")

    label("loc_ADE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_AEC")
    Jump("loc_B00")

    label("loc_AEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_AFA")
    Jump("loc_B00")

    label("loc_AFA")

    BeginChrThread(0x9, 0, 0, 1)

    label("loc_B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_B0E")
    Jump("loc_D43")

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_B21")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_D43")

    label("loc_B21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_B57")
    SetChrPos(0x8, -24640, 0, -1950, 135)
    SetChrPos(0x9, -23350, 0, -3110, 315)
    BeginChrThread(0x9, 0, 0, 0)
    Jump("loc_D43")

    label("loc_B57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_B74")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_D43")

    label("loc_B74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_B8C")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0x17, 0x80)
    Jump("loc_D43")

    label("loc_B8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_B9F")
    SetChrFlags(0x9, 0x80)
    Jump("loc_D43")

    label("loc_B9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_BCF")
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BCA")
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)

    label("loc_BCA")

    Jump("loc_D43")

    label("loc_BCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_BE2")
    ClearChrFlags(0x12, 0x80)
    Jump("loc_D43")

    label("loc_BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BF0")
    Jump("loc_D43")

    label("loc_BF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_C23")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0x9, -30620, -1000, -17090, 317)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_D43")

    label("loc_C23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_C36")
    ClearChrFlags(0x16, 0x80)
    Jump("loc_D43")

    label("loc_C36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_C49")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_D43")

    label("loc_C49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_C5D")
    BeginChrThread(0x9, 0, 0, 1)
    Jump("loc_D43")

    label("loc_C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_C7B")
    ClearChrFlags(0x10, 0x80)
    BeginChrThread(0x9, 0, 0, 1)
    ClearChrFlags(0x18, 0x80)
    Jump("loc_D43")

    label("loc_C7B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_C8E")
    ClearChrFlags(0xA, 0x80)
    Jump("loc_D43")

    label("loc_C8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_CD9")
    SetChrPos(0xA, -39100, 3000, 21560, 315)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xD, -26990, 0, 1930, 270)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0x9, -26490, -1000, -25270, 180)
    Jump("loc_D43")

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_D02")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x9, -26490, -1000, -25270, 180)
    Jump("loc_D43")

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_D2B")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0x9, -26490, -1000, -25270, 180)
    Jump("loc_D43")

    label("loc_D2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_D43")
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)

    label("loc_D43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D5B")
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)

    label("loc_D5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D6F")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 44)
    Jump("loc_D92")

    label("loc_D6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_D83")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 48)
    Jump("loc_D92")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_D92")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 56)

    label("loc_D92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 0)), scpexpr(EXPR_END)), "loc_DA1")
    ClearScenarioFlags(0x7E, 0)
    Event(0, 27)

    label("loc_DA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7E, 1)), scpexpr(EXPR_END)), "loc_DB9")
    ClearScenarioFlags(0x7E, 1)
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 29)

    label("loc_DB9")

    Return()

    # Function_4_AAE end

    def Function_5_DBA(): pass

    label("Function_5_DBA")

    SetMapObjFlags(0x7, 0x4)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    ModifyEventFlags(0, 4, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DEC")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_DEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFF")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E12")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E25")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E38")
    ModifyEventFlags(1, 4, 0x80)

    label("loc_E38")

    OP_65(0x1, 0x1)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E56")
    OP_66(0x1, 0x1)

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E68")
    OP_66(0x2, 0x1)

    label("loc_E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E7A")
    OP_66(0x3, 0x1)

    label("loc_E7A")

    OP_65(0x8, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E98")
    OP_66(0x8, 0x1)

    label("loc_E98")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -17180, -2000, -32770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF0")

    label("loc_EF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F1C")
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    Jump("loc_F6F")

    label("loc_F1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F48")
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    Jump("loc_F6F")

    label("loc_F48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F6F")
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)

    label("loc_F6F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_FB9")
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x1, 0x2)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_FED")

    label("loc_FB9")

    SetMapObjFrame(0xFF, "model6", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x1, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x2)

    label("loc_FED")

    SetMapObjFlags(0xB, 0x4)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_102A")
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    OP_66(0x7, 0x1)
    Jump("loc_102F")

    label("loc_102A")

    OP_16(0x3, 0x3, 0x1, 0x0)

    label("loc_102F")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1056")
    ClearMapObjFlags(0x8, 0x4)

    label("loc_1056")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1069")
    ModifyEventFlags(1, 10, 0x80)

    label("loc_1069")

    SetMapObjFlags(0x9, 0x4)
    SetMapObjFrame(0x9, "light", 0x0, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    SetMapObjFrame(0xA, "patlight", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10B3")
    ClearMapObjFlags(0x9, 0x4)

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10C7")
    ClearMapObjFlags(0xA, 0x4)

    label("loc_10C7")

    OP_1B(0x0, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10DF")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_10DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10F2")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_10F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1105")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_1105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1118")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_1118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_112B")
    OP_1B(0x0, 0x0, 0x40)

    label("loc_112B")

    ClearMapObjFlags(0x6, 0x10)
    OP_70(0x6, 0xA)
    Return()

    # Function_5_DBA end

    def Function_6_1136(): pass

    label("Function_6_1136")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1263")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11FF")

    #C0001
    ChrTalk(
        0xFE,
        "啊！欢迎来到圣乌尔斯拉医院。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "说起来，那个蓝头发的孩子……\x01",
            "你的身体已经好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#0205F嗯，是的……\x01",
            "托您的福。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "这样啊，不管怎么说，\x01",
            "身体没有大碍就好了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_125E")

    label("loc_11FF")


    #C0005
    ChrTalk(
        0xFE,
        (
            "那个蓝头发的孩子昨天突然\x01",
            "就倒下了，真是吓了我一跳。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "不过现在看起来很精神，这就好了。\x02",
    )

    CloseMessageWindow()

    label("loc_125E")

    Jump("loc_1E82")

    label("loc_1263")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_12D9")
    TurnDirection(0xFE, 0x9, 0)

    #C0007
    ChrTalk(
        0xFE,
        (
            "因为不久之前的狼形魔兽事件，\x01",
            "我的工作时间也稍微延长了一些呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "说实话，大家都很辛苦啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E82")

    label("loc_12D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1364")

    #C0009
    ChrTalk(
        0xFE,
        (
            "清晨时分，\x01",
            "一些让人感觉很阴森恐怖的人\x01",
            "接二连三被送了进来。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "哎呀～……被吓了一跳呢，\x01",
            "克洛斯贝尔市发生什么事件了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E82")

    label("loc_1364")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_13BD")

    #C0011
    ChrTalk(
        0xFE,
        "啊！欢迎来到圣乌尔斯拉医院。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "今天没有把那个可爱的孩子\x01",
            "也带来吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E82")

    label("loc_13BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_141C")

    #C0013
    ChrTalk(
        0xFE,
        "绿色头发的女孩子吗……？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "没有在医院外面见到呢。\x01",
            "会不会还在医院里面啊？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E82")

    label("loc_141C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_150A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C0")

    #C0015
    ChrTalk(
        0xFE,
        "啊！欢迎来到乌尔斯拉医科大学附属医院。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x153,
        "#1109F哟，你好啊！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "哈哈，精神真好呢～\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "我想你们也都知道，\x01",
            "接待处在病房楼那边。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1505")

    label("loc_14C0")


    #C0019
    ChrTalk(
        0xFE,
        (
            "巴士才刚刚开走，\x01",
            "暂时应该不会回来哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "接待处在病房楼那边。\x02",
    )

    CloseMessageWindow()

    label("loc_1505")

    Jump("loc_1E82")

    label("loc_150A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1642")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15C7")

    #C0021
    ChrTalk(
        0xFE,
        (
            "刚才约亚西姆医生\x01",
            "打算去郊外钓鱼。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "我觉得很危险，本想要阻止他，\x01",
            "但是他给了我一米拉，\x01",
            "让我为他保密。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……该怎么说呢，\x01",
            "没想到他是一个这么小气的人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_163D")

    label("loc_15C7")


    #C0024
    ChrTalk(
        0xFE,
        (
            "约亚西姆医生想要\x01",
            "偷偷去钓鱼，\x01",
            "还给了我一米拉的封口费。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "……不过，他最后还是\x01",
            "被护士和实习医生们\x01",
            "给拖了回去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_163D")

    Jump("loc_1E82")

    label("loc_1642")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_16C0")

    #C0026
    ChrTalk(
        0xFE,
        "啊！欢迎来到圣乌尔斯拉医院。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "你们应该没有受伤吧？\x01",
            "难得的纪念庆典，\x01",
            "注意不要闹过头，最后反而乐极生悲。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E82")

    label("loc_16C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_17C9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175F")

    #C0028
    ChrTalk(
        0xFE,
        "啊！欢迎来到圣乌尔斯拉医院。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "……停在那边的那辆车，真是好棒啊！\x01",
            "是加长型豪华轿车吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "嗯，有钱人开的车\x01",
            "果然别具格调。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17C4")

    label("loc_175F")


    #C0031
    ChrTalk(
        0xFE,
        (
            "快看那边的加长轿车。\x01",
            "那可是最新型的，\x01",
            "价格肯定非常昂贵吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "嗯，有钱人开的车\x01",
            "果然别具格调。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17C4")

    Jump("loc_1E82")

    label("loc_17C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1833")

    #C0033
    ChrTalk(
        0xFE,
        "啊！欢迎来到圣乌尔斯拉医院。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "现在，克洛斯贝尔市内\x01",
            "正在举行纪念庆典吧。\x01",
            "很热闹吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E82")

    label("loc_1833")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_18BA")

    #C0035
    ChrTalk(
        0xFE,
        "啊，欢迎来到圣乌尔斯拉医院。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "现在彩虹剧团的话题好像\x01",
            "在外面闹得沸沸扬扬呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "如果可以的话，我也想去看看啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E82")

    label("loc_18BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A62")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C0")

    #C0038
    ChrTalk(
        0xFE,
        (
            "这所医院里配备有专用的车辆——\x01",
            "『急救车』。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "即使是来不及等定期巴士的急诊病人，\x01",
            "只要使用导力通讯联络我们，\x01",
            "无论他在克洛斯贝尔何处，我们都能迅速赶到。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "前段时间之所以能及时救治\x01",
            "身受重伤的街头混混，\x01",
            "也是多亏了急救车的速度。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1A5D")

    label("loc_19C0")


    #C0041
    ChrTalk(
        0xFE,
        (
            "急诊病人的话，\x01",
            "只要使用导力通讯联络我们，\x01",
            "无论他在克洛斯贝尔何处，我们都能迅速赶到。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "跟普通马力的导力车相比，\x01",
            "急救车的速度可以轻松把它们甩在身后。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A5D")

    Jump("loc_1E82")

    label("loc_1A62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1B65")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B07")

    #C0043
    ChrTalk(
        0xFE,
        "嗯……已经准备回去了吗？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "如果想要回克洛斯贝尔市，\x01",
            "在那边的巴士站等一会就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "今天的巴士应该还有几班，\x01",
            "没必要急急忙忙的。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B60")

    label("loc_1B07")


    #C0046
    ChrTalk(
        0xFE,
        (
            "如果想要回克洛斯贝尔市，\x01",
            "在那边的巴士站等一会就好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "话说，夕阳真是漂亮呢……\x02",
    )

    CloseMessageWindow()

    label("loc_1B60")

    Jump("loc_1E82")

    label("loc_1B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1C6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C1F")

    #C0048
    ChrTalk(
        0xFE,
        (
            "利顿被袭击的那天晚上，\x01",
            "来了一个很烦的商人。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "想以非常高的价格\x01",
            "向我们推销床单，\x01",
            "我被叫去应付他了。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "因此刚好就\x01",
            "不在这里。\x01",
            "没有帮到你们，真是抱歉。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C66")

    label("loc_1C1F")


    #C0051
    ChrTalk(
        0xFE,
        (
            "嗯……我那天晚上\x01",
            "刚好不在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "不好意思，我没有什么线索。\x02",
    )

    CloseMessageWindow()

    label("loc_1C66")

    Jump("loc_1E82")

    label("loc_1C6B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1DF2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBE")

    #C0053
    ChrTalk(
        0xFE,
        (
            "刚才有联络说，\x01",
            "开在郊外的定期巴士\x01",
            "受到了魔兽的袭击。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "但是英勇登场的两位游击士\x01",
            "瞬间就将那些家伙给收拾了。\x01",
            "好厉害啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        (
            "#0306F联络中完全没提到我们……\x01",
            "说明对方对我们\x01",
            "根本就没有印象呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0011F好了好了……\x01",
            "是因为艾丝蒂尔和约修亚\x01",
            "实在很强，给人印象太深吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x136,
        "#1300F呵呵，你们也必须多加努力了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DED")

    label("loc_1DBE")


    #C0058
    ChrTalk(
        0xFE,
        (
            "哎呀～游击士果然好厉害啊，\x01",
            "要着重注意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DED")

    Jump("loc_1E82")

    label("loc_1DF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1E82")

    #C0059
    ChrTalk(
        0xFE,
        (
            "哟，你们好。\x01",
            "这里是乌尔斯拉医科大学附属医院……\x01",
            "简称乌尔斯拉医院。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "你们不是医院相关人员吧？\x01",
            "进门之后请直接进入里面的建筑物。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E82")

    TalkEnd(0xFE)
    Return()

    # Function_6_1136 end

    def Function_7_1E86(): pass

    label("Function_7_1E86")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1EF6")

    #C0061
    ChrTalk(
        0xFE,
        "早上散步有益身体健康。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "我跟患者一起散步的同时，\x01",
            "也促进了自己的健康，真是一举两得呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFF")

    label("loc_1EF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_1F60")

    #C0063
    ChrTalk(
        0xFE,
        "今天是我负责值班呢……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "护士这个工作是很忙的。\x01",
            "必须要多加注意，\x01",
            "不能把身体累坏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFF")

    label("loc_1F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1FB4")

    #C0065
    ChrTalk(
        0xFE,
        (
            "之前的那些伤员\x01",
            "被送进了ＩＣＵ（重症监护室），\x01",
            "他们不会有事吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFF")

    label("loc_1FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_201A")

    #C0066
    ChrTalk(
        0xFE,
        (
            "我们与患者也有私交，\x01",
            "所以免不了经常劳心伤神。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "也就是说，\x01",
            "必须要打起精神来啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFF")

    label("loc_201A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2083")

    #C0068
    ChrTalk(
        0xFE,
        (
            "哎呀，警察弟弟……\x01",
            "你带着一个好可爱的小女孩啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "呵呵……\x01",
            "注意不要让她\x01",
            "迷路了哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFF")

    label("loc_2083")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2191")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_211D")

    #C0070
    ChrTalk(
        0xFE,
        "纪念庆典今天就要结束了。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "我想你们这几天\x01",
            "工作也都很忙吧，\x01",
            "不过也就到今天为止了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "只剩一点了，\x01",
            "大家都努力加油吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_218C")

    label("loc_211D")


    #C0073
    ChrTalk(
        0xFE,
        (
            "纪念庆典今天就要结束了……\x01",
            "虽然最近都没怎么好好休息，\x01",
            "不过马上就熬到头啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "今天一整天都\x01",
            "努力加油吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_218C")

    Jump("loc_2BFF")

    label("loc_2191")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2228")

    #C0075
    ChrTalk(
        0xFE,
        (
            "米海尔今天的状态不错，\x01",
            "还获得了外出许可哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "虽然只能在医院用地里走一走而已。\x01",
            "不过平时他都躺在床上，\x01",
            "所以应该也能放松心情了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BFF")

    label("loc_2228")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2332")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CD")

    #C0077
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，\x01",
            "有很多住院患者都想要\x01",
            "获得临时外出许可。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "不过他们的病情各不相同，\x01",
            "如果不向医生确认一下，\x01",
            "我也不知道该怎么处理。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_232D")

    label("loc_22CD")


    #C0079
    ChrTalk(
        0xFE,
        (
            "因为是难得的纪念庆典，\x01",
            "所以我也很理解他们想要去玩的心情……\x01",
            "但就算和我说这些也无济于事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_232D")

    Jump("loc_2BFF")

    label("loc_2332")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_25E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A3")

    #C0080
    ChrTalk(
        0xFE,
        "哎呀，中午好。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_2472")

    #C0081
    ChrTalk(
        0xFE,
        (
            "呵呵，兰迪先生，\x01",
            "昨天的演唱会真不错，\x01",
            "谢谢你邀请我。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "兰和菲莉亚\x01",
            "好像都玩得很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0304F哈哈，让女士开心\x01",
            "正是男人的使命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#0006F竟然同时跟三个护士约会，\x01",
            "兰迪你还真是个中高手呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#0105F确实呢……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#0211F不如说是气血旺盛得过头了吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_259B")

    label("loc_2472")


    #C0087
    ChrTalk(
        0xFE,
        (
            "兰迪先生，罗伊德，\x01",
            "昨天的演唱会真不错。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "兰和菲莉亚\x01",
            "好像都玩得很开心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        (
            "#0304F哈哈，让女士开心\x01",
            "正是男人的使命啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0000F那个……\x01",
            "我才应该\x01",
            "谢谢你们的邀请。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#0105F原来你们……\x01",
            "还和护士小姐们\x01",
            "二对三的约会了呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#0211F真是血气旺盛呢。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#0006F（别用那种眼神看我……）\x02",
    )

    CloseMessageWindow()

    label("loc_259B")

    SetScenarioFlags(0x0, 1)
    Jump("loc_25E0")

    label("loc_25A3")


    #C0094
    ChrTalk(
        0xFE,
        (
            "昨天玩得很开心……\x01",
            "呵呵，感觉今天一整天都能努力工作了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E0")

    Jump("loc_2BFF")

    label("loc_25E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_272C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26E1")

    #C0095
    ChrTalk(
        0xFE,
        "说起来，下个月就是纪念庆典了。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "虽然菲莉亚邀请我去玩……\x01",
            "但不知道能不能申请到休假呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        (
            "#0309F哈哈，我很期待呢。\x01",
            "要努力争取到休假哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0098
    ChrTalk(
        0xFE,
        "嗯……好吧，我会试着努力的。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#0000F（好像是兰迪约了她们……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2727")

    label("loc_26E1")


    #C0100
    ChrTalk(
        0xFE,
        "不知道能不能在纪念庆典期间请到假呢。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "算了，只能好好努力了。\x02",
    )

    CloseMessageWindow()

    label("loc_2727")

    Jump("loc_2BFF")

    label("loc_272C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_27EE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BA")

    #C0102
    ChrTalk(
        0xFE,
        (
            "哎呀，这不是塞茜尔前辈的弟弟吗，\x01",
            "最近过得好吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#0006F总、总觉得好像\x01",
            "不知不觉就在护士间\x01",
            "成为了名人呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_27E9")

    label("loc_27BA")


    #C0104
    ChrTalk(
        0xFE,
        (
            "这不是塞茜尔前辈的弟弟吗，\x01",
            "最近过得好吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27E9")

    Jump("loc_2BFF")

    label("loc_27EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_285B")

    #C0105
    ChrTalk(
        0xFE,
        (
            "夕阳下的艾鲁姆湖真美啊，\x01",
            "让人觉得心灵都被治愈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "……好了，今天也要好好加油值夜班！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2BFF")

    label("loc_285B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2922")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28F4")
    TurnDirection(0xFE, 0xC, 0)

    #C0107
    ChrTalk(
        0xFE,
        (
            "好啦，老爷爷。\x01",
            "太阳都快要下山了……\x01",
            "我们回病房吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        "呵呵，说得也是呢。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        (
            "总算快要出院了，\x01",
            "还是别勉强的好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_291D")

    label("loc_28F4")


    #C0110
    ChrTalk(
        0xFE,
        (
            "好了，差不多该把老爷爷\x01",
            "带回病房了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_291D")

    Jump("loc_2BFF")

    label("loc_2922")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2AAC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A23")

    #C0111
    ChrTalk(
        0xFE,
        (
            "啊，塞茜尔前辈。\x01",
            "那几位是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x136,
        (
            "#1300F是我弟弟罗伊德……\x01",
            "和他的恋人们。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "咦、咦咦……！？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0011F等、等一下，塞茜尔姐姐！\x01",
            "玩笑开过头了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x136,
        (
            "#1309F呵呵，只是想稍微\x01",
            "开个玩笑而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "什、什么啊，吓死我了……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2AA7")

    label("loc_2A23")


    #C0117
    ChrTalk(
        0xFE,
        (
            "关于罗伊德警官的事，\x01",
            "已经从塞茜尔前辈那里\x01",
            "听说过了。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "塞茜尔前辈所说的事\x01",
            "到底是真的还是在开玩笑……\x01",
            "偶尔会让人搞不清楚呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AA7")

    Jump("loc_2BFF")

    label("loc_2AAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2BFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BCE")

    #C0119
    ChrTalk(
        0xFE,
        (
            "哎呀，下午好。\x01",
            "请问几位是来探病的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        (
            "#0305F哦哦，真不错、真不错！\x02\x03",

            "#0309F嗯，真正的白衣天使\x01",
            "果然就是不一样呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#0205F……真正的？\x01",
            "那是什么意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x102,
        "#0104F好了好了，这个话题就到此为止吧。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "那、那个……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#0006F……总觉得很对不起您呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2BFF")

    label("loc_2BCE")


    #C0125
    ChrTalk(
        0xFE,
        (
            "呵呵，看起来非常精神呢。\x01",
            "是来看望朋友的吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BFF")

    TalkEnd(0xFE)
    Return()

    # Function_7_1E86 end

    def Function_8_2C03(): pass

    label("Function_8_2C03")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2C8D")

    #C0126
    ChrTalk(
        0xFE,
        (
            "虽然勤杂工的工作\x01",
            "偶尔会被人小看……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "但是要做的事情有很多，\x01",
            "而且，最重要的是它十分有意义。\x01",
            "我很喜欢这份工作哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2C9B")
    Jump("loc_3053")

    label("loc_2C9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2CA9")
    Jump("loc_3053")

    label("loc_2CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2D17")

    #C0128
    ChrTalk(
        0xFE,
        (
            "盖里教授坐在长椅上\x01",
            "不停地叹着气呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "嗯，即使是了不起的医生，\x01",
            "也会有各种各样的烦恼吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2D17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_2D25")
    Jump("loc_3053")

    label("loc_2D25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2D33")
    Jump("loc_3053")

    label("loc_2D33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D41")
    Jump("loc_3053")

    label("loc_2D41")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2D82")

    #C0130
    ChrTalk(
        0xFE,
        (
            "为了不让花朵枯萎，\x01",
            "必须多花点心思照料它们呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2D90")
    Jump("loc_3053")

    label("loc_2D90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2E2D")

    #C0131
    ChrTalk(
        0xFE,
        (
            "大概是因为眺望了艾鲁姆湖的美景吧，\x01",
            "我现在的心情非常平静。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "对于在纪念庆典期间也无法外出的\x01",
            "住院患者来说，\x01",
            "这里就如同沙漠中的绿洲一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2E2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2EBC")

    #C0133
    ChrTalk(
        0xFE,
        (
            "绿色有让人心情\x01",
            "平静的效果。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "虽然作用不是非常大，但我们希望\x01",
            "可以借此让患者们稍微安心一些。\x01",
            "所以医院里放置了很多植物呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2EBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2ECA")
    Jump("loc_3053")

    label("loc_2ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2F23")

    #C0135
    ChrTalk(
        0xFE,
        (
            "装上防护栏之后，\x01",
            "医院看起来气派了不少呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "我也必须要小心魔兽了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2F23")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2F8D")

    #C0137
    ChrTalk(
        0xFE,
        (
            "楼顶的调查结束了吗……\x01",
            "有什么线索了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "哦哦，要是楼顶空出来了，\x01",
            "我就过去打扫吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2F8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2FFF")

    #C0139
    ChrTalk(
        0xFE,
        (
            "虽然在医院工作很长时间了，\x01",
            "但还是觉得这里的建筑\x01",
            "相当气派呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "好了，必须好好整理一下了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3053")

    label("loc_2FFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3053")

    #C0141
    ChrTalk(
        0xFE,
        "嗯？怎么了？迷路了吗？\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "要找病房楼的话，\x01",
            "里面那栋高大的建筑就是。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3053")

    TalkEnd(0xFE)
    Return()

    # Function_8_2C03 end

    def Function_9_3057(): pass

    label("Function_9_3057")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_30EB")
    Jump("loc_3135")

    label("loc_30EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_310B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3135")

    label("loc_310B")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_312B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3135")

    label("loc_312B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3135")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31CB")

    #C0143
    ChrTalk(
        0xFE,
        (
            "昨天从ＩＢＣ的人那里\x01",
            "得到了玩偶。\x01",
            "嘿嘿……好高兴哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "迪塔先生\x01",
            "真是一个亲切的叔叔呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_320E")

    label("loc_31CB")


    #C0145
    ChrTalk(
        0xFE,
        "嗯，清新的空气真让人心情舒畅。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "下次找小滴\x01",
            "一起散步好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_320E")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_3057 end

    def Function_10_3216(): pass

    label("Function_10_3216")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3227")
    Jump("loc_3573")

    label("loc_3227")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3235")
    Jump("loc_3573")

    label("loc_3235")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_3243")
    Jump("loc_3573")

    label("loc_3243")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3251")
    Jump("loc_3573")

    label("loc_3251")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_325F")
    Jump("loc_3573")

    label("loc_325F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_326D")
    Jump("loc_3573")

    label("loc_326D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_327B")
    Jump("loc_3573")

    label("loc_327B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3289")
    Jump("loc_3573")

    label("loc_3289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3297")
    Jump("loc_3573")

    label("loc_3297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_32A5")
    Jump("loc_3573")

    label("loc_32A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_32B3")
    Jump("loc_3573")

    label("loc_32B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_32C1")
    Jump("loc_3573")

    label("loc_32C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_32CF")
    Jump("loc_3573")

    label("loc_32CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_334A")

    #C0147
    ChrTalk(
        0xFE,
        (
            "呵呵，说得也是呢。\x01",
            "我们回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "难得就快要出院了，\x01",
            "如果太过勉强而把身体搞坏，\x01",
            "那可就是得不偿失了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3573")

    label("loc_334A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_34A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_346F")

    #C0149
    ChrTalk(
        0x136,
        (
            "#1300F老爷爷，\x01",
            "那之后膝盖的情况怎么样了？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "呵呵，好得就像没受过伤一样。\x01",
            "在这里接受治疗真是太正确了。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x136,
        (
            "#1300F呵呵，那真是太好了。\x02\x03",

            "贝尔达因医生也说\x01",
            "您马上就可以出院了，\x01",
            "再稍微努力一下吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0004F（塞茜尔姐姐……\x01",
            "　果然已经非常\x01",
            "　习惯护士的工作了。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_34A2")

    label("loc_346F")


    #C0153
    ChrTalk(
        0xFE,
        (
            "马上就要出院了吗……\x01",
            "呵～呵～呵～真是高兴啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A2")

    Jump("loc_3573")

    label("loc_34A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3573")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3529")

    #C0154
    ChrTalk(
        0xFE,
        (
            "我在澡堂摔倒，\x01",
            "弄伤了膝盖。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "多亏了这里的医生替我治疗\x01",
            "才能恢复成现在这样，\x01",
            "可以到外面行走了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_3573")

    label("loc_3529")


    #C0156
    ChrTalk(
        0xFE,
        (
            "话说回来，我都没想到那么快\x01",
            "就可以走动了……\x01",
            "这里的医生们真的很优秀。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3573")

    TalkEnd(0xFE)
    Return()

    # Function_10_3216 end

    def Function_11_3577(): pass

    label("Function_11_3577")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_3588")
    Jump("loc_3701")

    label("loc_3588")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3596")
    Jump("loc_3701")

    label("loc_3596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_35A4")
    Jump("loc_3701")

    label("loc_35A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_35B2")
    Jump("loc_3701")

    label("loc_35B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_35C0")
    Jump("loc_3701")

    label("loc_35C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_35CE")
    Jump("loc_3701")

    label("loc_35CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_35DC")
    Jump("loc_3701")

    label("loc_35DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_35EA")
    Jump("loc_3701")

    label("loc_35EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_35F8")
    Jump("loc_3701")

    label("loc_35F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3606")
    Jump("loc_3701")

    label("loc_3606")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3614")
    Jump("loc_3701")

    label("loc_3614")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3622")
    Jump("loc_3701")

    label("loc_3622")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_36A6")

    #C0157
    ChrTalk(
        0xFE,
        (
            "奶奶看起来很精神，真是太好了。\x01",
            "而且听说她马上就可以出院了呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "奶奶出院时，我一定会跟爸爸妈妈\x01",
            "一起来接她的！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3701")

    label("loc_36A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_36B4")
    Jump("loc_3701")

    label("loc_36B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_36C2")
    Jump("loc_3701")

    label("loc_36C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3701")

    #C0159
    ChrTalk(
        0xFE,
        (
            "嗯……\x01",
            "好大的医院啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "希望奶奶\x01",
            "一切都好呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3701")

    TalkEnd(0xFE)
    Return()

    # Function_11_3577 end

    def Function_12_3705(): pass

    label("Function_12_3705")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376C")

    #C0161
    ChrTalk(
        0xFE,
        (
            "我来探望\x01",
            "因为受伤而住院的朋友。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "不过，那家伙的病房\x01",
            "究竟在什么地方呢……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_37A9")

    label("loc_376C")


    #C0163
    ChrTalk(
        0xFE,
        (
            "朋友的病房……在哪里呢？\x01",
            "……算了，随便走走总会找到的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37A9")

    TalkEnd(0xFE)
    Return()

    # Function_12_3705 end

    def Function_13_37AD(): pass

    label("Function_13_37AD")

    TalkBegin(0xFE)

    #C0164
    ChrTalk(
        0xFE,
        (
            "我今天是来探望\x01",
            "男朋友的。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "他非常固执，\x01",
            "希望不要给其他患者\x01",
            "添麻烦才好啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_37AD end

    def Function_14_3807(): pass

    label("Function_14_3807")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 6)), scpexpr(EXPR_END)), "loc_3864")

    #C0166
    ChrTalk(
        0x10,
        (
            "#3600F好了，必须把这些\x01",
            "医疗用品搬出去……\x02\x03",

            "哈哈哈，各位\x01",
            "还请加油工作。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_39C3")

    label("loc_3864")


    #C0167
    ChrTalk(
        0x101,
        "#0005F咦，哈罗德先生……？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x10,
        (
            "#3600F各位好……很久不见了呢，\x01",
            "没想到会在这种地方再会。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#0000F哈哈……自从上次的事件以来，\x01",
            "市外的工作也增加了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x103,
        "#0200F哈罗德先生也是因为工作来这里的吗？\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x10,
        (
            "#3600F嗯，我是来给乌尔斯拉医院\x01",
            "送医疗用品跟日用品的。\x02\x03",

            "购买导力车果然是个正确的决定，\x01",
            "来回方便了很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        "#0100F您的生意好像也很顺利呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 6)

    label("loc_39C3")

    TalkEnd(0xFE)
    Return()

    # Function_14_3807 end

    def Function_15_39C7(): pass

    label("Function_15_39C7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3A27")

    #C0173
    ChrTalk(
        0x11,
        (
            "……话说……迪诺那家伙\x01",
            "是什么时候拥有了那种力量的……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x11,
        "嘁，该死的……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A88")

    label("loc_3A27")


    #C0175
    ChrTalk(
        0x11,
        (
            "该死的……竟敢瞧不起\x01",
            "身为干部的我。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x11,
        (
            "可恶的迪诺，等我回去之后，\x01",
            "一定要好好收拾你……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_3A88")

    TalkEnd(0xFE)
    Return()

    # Function_15_39C7 end

    def Function_16_3A8C(): pass

    label("Function_16_3A8C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3ACA")

    #C0177
    ChrTalk(
        0x12,
        (
            "说实话，我本来是不想\x01",
            "来见那种家伙的……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B19")

    label("loc_3ACA")


    #C0178
    ChrTalk(
        0x12,
        (
            "妈妈竟然让我过来\x01",
            "给老爸送饭。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x12,
        (
            "……可恶，\x01",
            "他到底在什么地方啊……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3B19")

    TalkEnd(0xFE)
    Return()

    # Function_16_3A8C end

    def Function_17_3B1D(): pass

    label("Function_17_3B1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C8F")

    #C0180
    ChrTalk(
        0x101,
        (
            "#0005F咦，凯特前辈……？\x01",
            "你为什么会在这种地方！？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#0200F警察局的正规军有\x01",
            "市外活动吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "是啊，不过我只是个跟班而已。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "黑月的人正在\x01",
            "乌尔斯拉医院住院呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "搜查二科的人要来\x01",
            "进行案情查访，\x01",
            "我才开巡逻车送他们过来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0185
    ChrTalk(
        0xFE,
        (
            "虽然我很不擅长\x01",
            "开车。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        "#0000F哈哈……原来是这样啊。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        "#0100F真是辛苦您了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 7)
    Jump("loc_3D6B")

    label("loc_3C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D3A")

    #C0188
    ChrTalk(
        0xFE,
        (
            "黑月是……黑手党组织啊，\x01",
            "我以前完全不知道呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "……话说回来，\x01",
            "二科的人花得时间可真长呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "都已经耗去整整一上午了，\x01",
            "大概是碰到棘手的人了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3D6B")

    label("loc_3D3A")


    #C0191
    ChrTalk(
        0xFE,
        (
            "二科的人到底在干什么啊？\x01",
            "时间花得太长了……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D6B")

    TalkEnd(0xFE)
    Return()

    # Function_17_3B1D end

    def Function_18_3D6F(): pass

    label("Function_18_3D6F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3DD4")

    #C0192
    ChrTalk(
        0xFE,
        (
            "在这个医院里\x01",
            "有我们的成员——\x01",
            "约亚西姆团员在。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "呵呵，待会\x01",
            "试着去邀请他一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DD4")

    TalkEnd(0xFE)
    Return()

    # Function_18_3D6F end

    def Function_19_3DD8(): pass

    label("Function_19_3DD8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3EE0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3EA0")

    #C0194
    ChrTalk(
        0xFE,
        (
            "我们团长费瑟尔，\x01",
            "在克洛斯贝尔设立分部\x01",
            "已经是两年前的事情了。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "这两年，克洛斯贝尔分部\x01",
            "的活动确实丰富了很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "没有什么能比热爱垂钓的伙伴\x01",
            "增加更让人高兴了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_3EE0")

    label("loc_3EA0")


    #C0197
    ChrTalk(
        0xFE,
        (
            "被热爱垂钓的伙伴们\x01",
            "邀请去旅游……\x01",
            "没有比这更高兴的事情了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3EE0")

    TalkEnd(0xFE)
    Return()

    # Function_19_3DD8 end

    def Function_20_3EE4(): pass

    label("Function_20_3EE4")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3F78")
    Jump("loc_3FC2")

    label("loc_3F78")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3F98")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FC2")

    label("loc_3F98")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3FB8")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3FC2")

    label("loc_3FB8")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3FC2")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_405D")

    #C0198
    ChrTalk(
        0xFE,
        (
            "……我差不多也该\x01",
            "回诊察室了。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "就算已经很累了，\x01",
            "不过我也不想因为一直休息\x01",
            "而被拉格教授取笑。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436D")

    label("loc_405D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_4199")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_40DB")

    #C0200
    ChrTalk(
        0xFE,
        (
            "本来还指望你们\x01",
            "能全部都拿走的……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "毕竟是辟邪用的人偶，\x01",
            "再怎么说也不能随便丢弃啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4194")

    label("loc_40DB")


    #C0202
    ChrTalk(
        0xFE,
        (
            "你们在放在露台的杂物中……\x01",
            "找到什么有用的东西了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "……皮绳吗？\x01",
            "只要那个就好了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "你们多拿走一些\x01",
            "也是可以的。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#0006F（那些杂货和人偶\x01",
            "　实在是太占地方了吧……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_4194")

    Jump("loc_436D")

    label("loc_4199")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_424D")

    #C0206
    ChrTalk(
        0xFE,
        (
            "放有杂货的集装箱\x01",
            "在位于宿舍二楼，穿过男性职员\x01",
            "宿舍尽头的露台上。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "要是发现了什么\x01",
            "有用的东西，就随便\x01",
            "拿走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "说实话，我正头疼该怎么处理那些东西呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_436D")

    label("loc_424D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4261")
    Call(0, 62)
    Jump("loc_436D")

    label("loc_4261")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_42BB")

    #C0209
    ChrTalk(
        0xFE,
        (
            "由于家庭和工作方面的问题，\x01",
            "让我感到很疲惫了。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "做教授\x01",
            "也很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436D")

    label("loc_42BB")


    #C0211
    ChrTalk(
        0xFE,
        "……最近似乎有点累了。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "拜托护士希伦小姐\x01",
            "订购一些医疗用品，\x01",
            "却送来了其它东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "儿子琴兹也还是\x01",
            "跟以前一样，\x01",
            "没有退出不良团伙的意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "做教授\x01",
            "也很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_436D")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_3EE4 end

    def Function_21_4375(): pass

    label("Function_21_4375")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4504")
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0215
    ChrTalk(
        0x16,
        "#2900F哎呀，艾莉，真是好巧呢。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        (
            "#0105F贝尔……？\x01",
            "你在这种地方干什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x16,
        (
            "#2900F啊，我是陪父亲\x01",
            "过来的。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        "#0200F陪迪塔总裁吗……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        "#0000F总裁生了什么病吗……？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x102,
        (
            "#0109F啊哈哈……我想大概\x01",
            "不是那么回事……\x02\x03",

            "#0100F贝尔，是为那件事而来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x16,
        (
            "#2904F嗯，没错。\x02\x03",

            "#2900F你们去接待处看看就明白了。\x01",
            "如果各位时间宽裕的话，\x01",
            "去见见我父亲怎么样？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 6)
    Jump("loc_466E")

    label("loc_4504")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_455C")

    #C0222
    ChrTalk(
        0x16,
        (
            "#2906F父亲好慢啊，\x01",
            "到底在干什么呢。\x02\x03",

            "离商谈的时间\x01",
            "只剩下三十分钟了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_466E")

    label("loc_455C")


    #C0223
    ChrTalk(
        0x16,
        (
            "#2906F竟在这种商谈众多的繁忙时期……\x01",
            "我真是服了他呢。\x02\x03",

            "#2900F不过，算啦，因为这是父亲\x01",
            "为数不多的美德之一。\x02\x03",

            "作为女儿，也不能斤斤计较，\x01",
            "不去陪他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，嘴上虽然这样说，\x01",
            "但你每年都会陪他来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x16,
        (
            "#2904F……哈，只不过是每年都\x01",
            "刚好有时间而已，没办法啦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_466E")

    TalkEnd(0xFE)
    Return()

    # Function_21_4375 end

    def Function_22_4672(): pass

    label("Function_22_4672")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_478C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_472E")

    #C0226
    ChrTalk(
        0x18,
        (
            "#2400F利顿也重回工作岗位了，\x01",
            "他工作很努力呢。\x02\x03",

            "而且还悄悄\x01",
            "把我偷偷推给他的，\x01",
            "原本属于我的工作也给做完了。\x02\x03",

            "#2409F哈～哈～哈～\x01",
            "有个好学生的我真是幸福啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_478C")

    label("loc_472E")


    #C0227
    ChrTalk(
        0x18,
        (
            "#2400F还好有利顿帮我把工作\x01",
            "给做完了。\x02\x03",

            "#2409F空出来的时间就去钓钓鱼，\x01",
            "有效地利用一下吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_478C")

    TalkEnd(0xFE)
    Return()

    # Function_22_4672 end

    def Function_23_4790(): pass

    label("Function_23_4790")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4824")
    Jump("loc_486E")

    label("loc_4824")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4844")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_486E")

    label("loc_4844")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4864")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_486E")

    label("loc_4864")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_486E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_490B")

    #C0228
    ChrTalk(
        0xFE,
        (
            "旅行最重要的事情\x01",
            "就是享受当地的特色。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "即使是以医疗研究而闻名的医院，\x01",
            "也完全有资本成为景点。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_4975")

    label("loc_490B")


    #C0230
    ChrTalk(
        0xFE,
        (
            "旅行最重要的事情\x01",
            "就是享受当地的特色。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔可以参观的地方太多了，\x01",
            "所以玩起来也有点辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4975")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_4790 end

    def Function_24_497D(): pass

    label("Function_24_497D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A36")

    #C0232
    ChrTalk(
        0xFE,
        (
            "在这所医院里面设置有\x01",
            "检查身体健康状态的，\x01",
            "被称为『全面健康检查』的设备……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "因为每天都要干各种家务杂活，\x01",
            "使身体囤积了相当多的疲劳……\x01",
            "一定要去检查一下呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_4AB8")

    label("loc_4A36")


    #C0234
    ChrTalk(
        0xFE,
        (
            "要是我因为工作过度疲劳，\x01",
            "而被那个『全面健康检查』设备\x01",
            "诊断出什么坏结果……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "就以这个为借口，\x01",
            "让主人给我\x01",
            "多放几天假好了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AB8")

    TalkEnd(0xFE)
    Return()

    # Function_24_497D end

    def Function_25_4ABC(): pass

    label("Function_25_4ABC")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士车站。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B4F")
    Call(0, 26)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_4B6F")

    label("loc_4B4F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B6F")
    Call(0, 26)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_4B6F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_25_4ABC end

    def Function_26_4B77(): pass

    label("Function_26_4B77")

    Fade(1000)
    OP_68(-59000, 1000, 2200, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_E0(0x1)
    SetChrPos(0x0, -56600, 0, 3800, 180)
    SetChrPos(0x1, -56600, 0, 4900, 180)
    SetChrPos(0x2, -56600, 0, 6000, 180)
    SetChrPos(0x3, -56600, 0, 7200, 180)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x7, 0x1C)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1C, -75000, 0, 500, 90)
    OP_D3(0x1C, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    OP_0D()

    def lambda_4C4D():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_4C4D)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x1C, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_26_4B77 end

    def Function_27_4C90(): pass

    label("Function_27_4C90")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -56560, 0, 4080, 180)
    SetChrPos(0x1, -56560, 0, 4080, 180)
    SetChrPos(0x2, -56560, 0, 4080, 180)
    SetChrPos(0x3, -56560, 0, 4080, 180)
    OP_68(-56560, 1000, 4080, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_6F(0x1)
    Sleep(1)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_27_4C90 end

    def Function_28_4D25(): pass

    label("Function_28_4D25")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4D3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52B5")

    Menu(
        0,
        32,
        26,
        1,
        (
            "使用警备队车辆进行移动\x01",      # 0
            "在此处休息\x01",                  # 1
            "放弃\x01",                        # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5252")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DCD")
    MenuCmd(1, 1, "★克洛斯贝尔市·中央广场")
    MenuCmd(3, 1, 0x0)
    Jump("loc_4DE9")

    label("loc_4DCD")

    MenuCmd(1, 1, "　克洛斯贝尔市·中央广场")

    label("loc_4DE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E1B")
    MenuCmd(1, 1, "★克洛斯贝尔市·东出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_4E35")

    label("loc_4E1B")

    MenuCmd(1, 1, "　克洛斯贝尔市·东出口")

    label("loc_4E35")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4E67")
    MenuCmd(1, 1, "★克洛斯贝尔市·西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_4E81")

    label("loc_4E67")

    MenuCmd(1, 1, "　克洛斯贝尔市·西出口")

    label("loc_4E81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EB3")
    MenuCmd(1, 1, "★克洛斯贝尔市·南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_4ECD")

    label("loc_4EB3")

    MenuCmd(1, 1, "　克洛斯贝尔市·南出口")

    label("loc_4ECD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EFF")
    MenuCmd(1, 1, "★克洛斯贝尔市·北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_4F19")

    label("loc_4EFF")

    MenuCmd(1, 1, "　克洛斯贝尔市·北出口")

    label("loc_4F19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F41")
    MenuCmd(1, 1, "★唐古拉姆门")
    MenuCmd(3, 1, 0x5)
    Jump("loc_4F51")

    label("loc_4F41")

    MenuCmd(1, 1, "　唐古拉姆门")

    label("loc_4F51")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4F79")
    MenuCmd(1, 1, "★贝尔加德门")
    MenuCmd(3, 1, 0x6)
    Jump("loc_4F89")

    label("loc_4F79")

    MenuCmd(1, 1, "　贝尔加德门")

    label("loc_4F89")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FB7")
    MenuCmd(1, 1, "★乌尔斯拉医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_4FCD")

    label("loc_4FB7")

    MenuCmd(1, 1, "　乌尔斯拉医科大学")

    label("loc_4FCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4FF7")
    MenuCmd(1, 1, "★阿尔摩利卡村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_5009")

    label("loc_4FF7")

    MenuCmd(1, 1, "　阿尔摩利卡村")

    label("loc_5009")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5033")
    MenuCmd(1, 1, "★矿山镇玛因兹")
    MenuCmd(3, 1, 0x9)
    Jump("loc_5045")

    label("loc_5033")

    MenuCmd(1, 1, "　矿山镇玛因兹")

    label("loc_5045")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5075")
    MenuCmd(1, 1, "★玛因兹山道·隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_508D")

    label("loc_5075")

    MenuCmd(1, 1, "　玛因兹山道·隧道内")

    label("loc_508D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50B3")
    MenuCmd(1, 1, "★星见之塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_50C1")

    label("loc_50B3")

    MenuCmd(1, 1, "　星见之塔")

    label("loc_50C1")

    MenuCmd(1, 1, "　放弃")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5243")
    OP_60(0x0)
    Sleep(500)
    Sound(1501, 255, 100, 0)    #voice#Noel
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0xF1, 0x10E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0xB)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    Sleep(500)
    OP_0D()
    Sound(488, 0, 100, 0)
    Sleep(2500)
    SetScenarioFlags(0x7E, 1)
    SetScenarioFlags(0x7F, 6)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5196"),
        (1, "loc_51A4"),
        (2, "loc_51B2"),
        (3, "loc_51C0"),
        (4, "loc_51CE"),
        (5, "loc_51DC"),
        (6, "loc_51EA"),
        (7, "loc_51F8"),
        (8, "loc_5206"),
        (9, "loc_5214"),
        (10, "loc_5222"),
        (11, "loc_5230"),
        (SWITCH_DEFAULT, "loc_523E"),
    )


    label("loc_5196")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_51A4")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_51B2")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_51C0")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_51CE")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_51DC")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_51EA")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_51F8")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_5206")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_5214")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_5222")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_5230")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_523E")

    label("loc_523E")

    Jump("loc_524D")

    label("loc_5243")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_524D")

    Jump("loc_52B0")

    label("loc_5252")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_529D")
    OP_60(0x0)
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_52B0")

    label("loc_529D")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_52B0")

    Jump("loc_4D3F")

    label("loc_52B5")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_4D25 end

    def Function_29_52BD(): pass

    label("Function_29_52BD")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    Sleep(1)
    SetChrPos(0x0, -51320, 0, 17590, 270)
    SetChrPos(0x1, -51320, 0, 17590, 270)
    SetChrPos(0x2, -51320, 0, 17590, 270)
    SetChrPos(0x3, -51320, 0, 17590, 270)
    SetChrPos(0x4, -51320, 0, 17590, 270)
    SetChrPos(0x5, -51320, 0, 17590, 270)
    Sleep(1)
    OP_68(-51320, 1000, 17590, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    OP_6F(0x1)
    Sleep(1)
    Sound(489, 0, 100, 0)
    Sleep(2000)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5391")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_5397")

    label("loc_5391")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_5397")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_29_52BD end

    def Function_30_53AC(): pass

    label("Function_30_53AC")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)
    Return()

    # Function_30_53AC end

    def Function_31_53BA(): pass

    label("Function_31_53BA")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0237
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
    )

    CloseMessageWindow()
    OP_68(-17220, 0, -31290, 1500)
    MoveCamera(60, 36, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(22000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0238
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_547D")
    OP_E0(0x2)
    MiniGame(0x6, 0xE, 0xFFFFBFBE, 0xFFFFFC18, 0xFFFF9A5C, 0xB4, 0xFFFFBCE4, 0xFFFFF830, 0xFFFF7FFE)

    label("loc_547D")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_31_53BA end

    def Function_32_5482(): pass

    label("Function_32_5482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54BC")
    TalkBegin(0xFF)
    SetChrName("")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_55E8")

    label("loc_54BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5534")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【等待导力巴士】\x01",      # 0
            "【放弃】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5520"),
        (1, "loc_5528"),
        (SWITCH_DEFAULT, "loc_552D"),
    )


    label("loc_5520")

    Call(0, 47)
    Jump("loc_552D")

    label("loc_5528")

    Jump("loc_552D")

    label("loc_552D")

    EventEnd(0x3)
    Jump("loc_55E8")

    label("loc_5534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5545")
    Call(0, 25)
    Jump("loc_55E8")

    label("loc_5545")

    TalkBegin(0xFF)
    SetChrName("")

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个巴士停靠站。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_55AE")

    #C0241
    ChrTalk(
        0x101,
        (
            "#0000F对了……回去之前\x01",
            "必须得去跟塞茜尔姐姐报告。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55E5")

    label("loc_55AE")


    #C0242
    ChrTalk(
        0x101,
        (
            "#0000F在回克洛斯贝尔市之前，\x01",
            "必须对魔兽进行调查。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_55E5")

    TalkEnd(0xFF)

    label("loc_55E8")

    Return()

    # Function_32_5482 end

    def Function_33_55E9(): pass

    label("Function_33_55E9")

    Call(0, 37)
    Return()

    # Function_33_55E9 end

    def Function_34_55ED(): pass

    label("Function_34_55ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55FF")
    Call(0, 42)
    Jump("loc_5649")

    label("loc_55FF")

    TalkBegin(0xFF)

    #A0243
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "木箱上面布满了灰尘。\x02\x03",

            "看来很长一段时间\x01",
            "都没有人管过了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_5649")

    Return()

    # Function_34_55ED end

    def Function_35_564A(): pass

    label("Function_35_564A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_565C")
    Call(0, 43)
    Jump("loc_56A8")

    label("loc_565C")

    TalkBegin(0xFF)

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扶手上部的油漆\x01",
            "有多处剥落的痕迹。\x02\x03",

            "看上去像是最近才留下的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_56A8")

    Return()

    # Function_35_564A end

    def Function_36_56A9(): pass

    label("Function_36_56A9")

    EventBegin(0x0)
    ModifyEventFlags(0, 0, 0x80)
    Fade(1000)
    SetChrPos(0x101, -37200, 0, -1000, 90)
    SetChrPos(0x102, -38600, 0, -1000, 90)
    SetChrPos(0x103, -38600, 0, 400, 90)
    SetChrPos(0x104, -37200, 0, 400, 90)
    OP_68(-27020, -500, 13870, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(47750, 0)
    PlaceName2(340, 200, "c_plac15", 0x0, 5000)
    OP_68(-16610, -500, 50, 10000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-34620, 700, -20, 0)
    MoveCamera(42, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24700, 0)
    SetChrPos(0x101, -35740, 0, -950, 90)
    SetChrPos(0x102, -37220, 0, 560, 90)
    SetChrPos(0x103, -37220, 0, -950, 90)
    SetChrPos(0x104, -35740, 0, 560, 90)
    OP_0D()

    #C0245
    ChrTalk(
        0x104,
        (
            "#0300F#5P这里就是医科大学啊……\x01",
            "哦，看上去很气派嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        (
            "#0203F#6P……『圣乌尔斯拉医科大学』。\x02\x03",

            "#0200F大陆首屈一指的综合医院，\x01",
            "是一家非常著名的医疗研究机构。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#6P#0005F原来这么有名啊。\x02\x03",

            "#0000F确实，巴士的班次这么频繁，\x01",
            "说明前来就诊的人应该非常多吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#0104F听说原本是由医疗发达国家——\x01",
            "雷米菲利亚公国\x01",
            "帮助建造的。\x02\x03",

            "#0100F据说周边各国的重症患者\x01",
            "也会被送到这里来呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0249
    ChrTalk(
        0x104,
        (
            "#0302F#5P对了，这里有穿着\x01",
            "护士服的姐姐们吧！\x02\x03",

            "#0309F哎呀，真养眼真养眼¤\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_59FA():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_59FA)
    Sleep(50)

    def lambda_5A0A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A0A)
    Sleep(50)

    def lambda_5A1A():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A1A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0250
    ChrTalk(
        0x101,
        "#0012F#12P兰迪真精神呢……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        (
            "#0103F#6P虽然之前坐车\x01",
            "来过很多次了……\x02\x03",

            "#0100F不过步行的话，\x01",
            "果然要走很长时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x103,
        "#0208F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_5AFF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5AFF)
    Sleep(50)

    def lambda_5B0F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5B0F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_5B24():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5B24)
    Sleep(300)

    #C0253
    ChrTalk(
        0x101,
        "#11P#0005F缇欧……？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        "#0105F果然还是太累了吗？\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#0203F#6P……不，没事的。\x02\x03",

            "#0200F还没有去\x01",
            "阿尔摩利卡村的距离那么长……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#11P#0001F你没事就好……\x01",
            "不过别太勉强自己了哦。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0257
    ChrTalk(
        0x103,
        (
            "#0204F#6P嗯，不用担心。\x02\x03",

            "#0202F……比起这个，\x01",
            "罗伊德前辈还不快去\x01",
            "见见你那个姐姐吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x104,
        "#0305F#5P说得也是，还有这件事呢！\x02",
    )

    CloseMessageWindow()

    def lambda_5C77():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5C77)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0259
    ChrTalk(
        0x104,
        (
            "#0307F#5P好了好了，罗伊德！\x01",
            "快点去见见那位姐姐吧！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CD4():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5CD4)

    def lambda_5CE1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5CE1)

    def lambda_5CEE():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5CEE)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0260
    ChrTalk(
        0x101,
        (
            "#0006F#12P……为什么兰迪的\x01",
            "兴致那么高啊。\x02\x03",

            "#0000F算了，塞茜尔姐姐\x01",
            "也比较好说话……\x02\x03",

            "请医院的接待员叫她出来吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        "#0309F#5P好！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0262
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，那么\x01",
            "我们去正面的病房楼吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -37900, 0, -300, 90)
    SetScenarioFlags(0x61, 6)
    OP_29(0x3F, 0x1, 0x8)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_36_56A9 end

    def Function_37_5DED(): pass

    label("Function_37_5DED")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00001.itc", 0x1E)
    LoadChrToIndex("chr/ch00301.itc", 0x1F)
    OP_68(-34930, 3900, 16980, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, -36910, 3000, 16290, 90)
    SetChrPos(0x102, -38300, 3000, 16300, 90)
    SetChrPos(0x103, -38300, 3000, 17300, 90)
    SetChrPos(0x104, -37000, 3000, 17300, 90)
    FadeToBright(1000, 0)
    OP_0D()

    #C0263
    ChrTalk(
        0x101,
        (
            "#0000F#6P那么……\x01",
            "来调查一下这上面吧。\x02\x03",

            "兰迪，帮把手。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        "#0300F#5P好的。\x02",
    )

    CloseMessageWindow()
    OP_68(-34930, 4700, 16980, 2500)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(300)
    BeginChrThread(0x104, 3, 0, 39)
    OP_6F(0x1)
    Sleep(5300)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)
    FadeToDark(300, 0, 100)

    #A0265
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "布满灰尘的木箱上\x01",
            "有着某种痕迹。\x02\x03",

            "似乎是野兽的脚印。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    #C0266
    ChrTalk(
        0x101,
        "#0004F#6P……没错。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x104,
        (
            "#0300F#6P嗯，魔兽的足迹……\x01",
            "而且还是狼形魔兽的足迹。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0268
    ChrTalk(
        0x102,
        "#0101F#5P果然……\x02",
    )

    CloseMessageWindow()

    def lambda_5FF9():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5FF9)
    Sleep(50)

    def lambda_6009():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6009)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    #C0269
    ChrTalk(
        0x103,
        "#0203F这样看来……\x02",
    )

    CloseMessageWindow()
    OP_68(-36200, 4000, 20200, 4000)
    MoveCamera(35, 16, 0, 4000)
    SetCameraDistance(34000, 4000)

    def lambda_605B():
        OP_95(0xFE, -36480, 3000, 20450, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_605B)
    Sleep(500)

    def lambda_6078():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6078)
    Sleep(300)

    def lambda_6088():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6088)
    Sleep(100)

    def lambda_6098():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6098)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x103, 1)
    OP_93(0x103, 0x0, 0x1F4)
    OP_6F(0x11)

    #C0270
    ChrTalk(
        0x103,
        (
            "#0200F#6P魔兽很可能是从\x01",
            "那边侵入的呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_60EA():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_60EA)
    WaitChrThread(0x104, 1)

    #C0271
    ChrTalk(
        0x101,
        "#0000F嗯，大概没错。\x02",
    )

    CloseMessageWindow()
    OP_68(-36930, 3900, 16980, 3000)
    SetCameraDistance(26500, 3000)
    BeginChrThread(0x101, 3, 0, 40)
    BeginChrThread(0x104, 3, 0, 41)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)

    def lambda_6143():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6143)

    def lambda_6150():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6150)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0272
    ChrTalk(
        0x104,
        (
            "#0300F#6P这样看起来，\x01",
            "那里也不是很高。\x02\x03",

            "为了防止它们再次闯入，\x01",
            "还是制定相关对策比较好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        "#0103F#6P说得也是呢……\x02",
    )

    CloseMessageWindow()

    def lambda_61E6():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61E6)
    WaitChrThread(0x102, 1)
    Sleep(300)

    #C0274
    ChrTalk(
        0x102,
        (
            "#0100F#6P话说，对这里的调查工作，\x01",
            "这样就算告一段落了吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6238():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6238)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0275
    ChrTalk(
        0x101,
        (
            "#0001F#11P嗯，说得没错……\x02\x03",

            "#0003F……不过它们为什么要特地\x01",
            "闯入这种地方呢……\x02\x03",

            "还有，为什么对利顿医生的\x01",
            "袭击行为只进行了一半……\x02\x03",

            "#0001F谜团还有很多呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_62EA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_62EA)
    Sleep(100)

    def lambda_62FA():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_62FA)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0276
    ChrTalk(
        0x103,
        (
            "#0205F#5P那种事情\x01",
            "就只有魔兽才知道了，\x01",
            "即使为此烦恼也没有意义哦……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#0302F#5P没错没错，\x02\x03",

            "能将警备队的调查书补充完整，\x01",
            "就已经算是不错的收获了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_63A7():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63A7)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0278
    ChrTalk(
        0x101,
        (
            "#0004F#12P说得也是呢……\x02\x03",

            "#0000F好了，总之，\x01",
            "回去之前先向塞茜尔姐姐报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        (
            "#0102F#6P说得也是呢……\x01",
            "必须去向塞茜尔小姐报告和道谢呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#0309F#5P那么，\x01",
            "我们就向护士中心进发吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(26000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetChrPos(0x0, -37600, 3000, 16800, 270)
    OP_65(0x1, 0x1)
    OP_66(0x2, 0x1)
    SetScenarioFlags(0x63, 1)
    OP_29(0x3F, 0x1, 0x10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7123", 0)
    EventEnd(0x5)
    Return()

    # Function_37_5DED end

    def Function_38_64C7(): pass

    label("Function_38_64C7")

    SetChrFlags(0x101, 0x4)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x101, 0xFFFF7748, 0xE42, 0x40B0, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x101, 0xFFFF7B30, 0x1036, 0x4092, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(55, 0, 100, 0)
    Sleep(300)

    def lambda_6531():
        OP_95(0xFE, -32689, 4150, 16470, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6531)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(1000)
    OP_64(0x101)
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(1500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_38_64C7 end

    def Function_39_6592(): pass

    label("Function_39_6592")

    SetChrFlags(0x104, 0x4)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x104, 0xFFFF76BC, 0xE42, 0x4470, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(31, 0, 100, 0)
    Sleep(500)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x104, 0xFFFF7AAE, 0x1036, 0x44B6, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(54, 0, 100, 0)
    Sleep(1000)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    def lambda_660E():
        OP_96(0xFE, 0xFFFF7AAE, 0x1036, 0x42C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_660E)
    WaitChrThread(0x104, 1)
    Sleep(2000)
    OP_64(0x104)

    def lambda_6632():
        OP_96(0xFE, 0xFFFF7AAE, 0x1036, 0x44B6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6632)
    WaitChrThread(0x104, 1)
    Sleep(1050)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_39_6592 end

    def Function_40_666A(): pass

    label("Function_40_666A")


    def lambda_666F():
        OP_95(0xFE, -34000, 4150, 16530, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_666F)
    WaitChrThread(0x101, 1)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x101, 0xFFFF7748, 0xE42, 0x40B0, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(58, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    SetChrChipByIndex(0xFE, 0x1E)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x101, 0xFFFF6FD2, 0xBB8, 0x3FA2, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(59, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(300)
    ClearChrFlags(0x101, 0x4)
    Return()

    # Function_40_666A end

    def Function_41_66FA(): pass

    label("Function_41_66FA")

    OP_93(0x104, 0x10E, 0x1F4)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x104, 0xFFFF76BC, 0xE42, 0x4470, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(60, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x1F)
    SetChrSubChip(0xFE, 0x3)
    OP_9D(0x104, 0xFFFF6F78, 0xBB8, 0x4394, 0x3E8, 0x1388)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(61, 0, 100, 0)
    Sound(30, 0, 100, 0)
    Sleep(500)
    ClearChrFlags(0x104, 0x4)
    Return()

    # Function_41_66FA end

    def Function_42_6773(): pass

    label("Function_42_6773")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-37000, 4000, 24200, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -37000, 3000, 24200, 0)
    SetChrPos(0x102, -36800, 3000, 21670, 0)
    SetChrPos(0x103, -37670, 3000, 22640, 0)
    SetChrPos(0x104, -36210, 3000, 22900, 0)
    OP_0D()

    #A0281
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "木箱上面布满了灰尘。\x02\x03",

            "看起来已经被弃置\x01",
            "很长时间了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0282
    ChrTalk(
        0x101,
        "#0005F#2P（咦……？）\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x102,
        "#0105F#12P……怎么了？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        "#0003F#2P没什么……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0285
    ChrTalk(
        0x101,
        (
            "#0008F#2P（如果从对面跳过来的话，\x01",
            "　应该会在上面留下足迹，不过……）\x02\x03",

            "（这上面还是布满了灰尘，也就是说，\x01",
            "　这种状态保持很长一段时间了……）\x02\x03",

            "#0000F（不过，这也不是什么非常\x01",
            "　奇怪的事情吧……？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -37000, 3000, 23200, 0)
    OP_68(-37000, 4000, 23200, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26000, 0)
    OP_66(0x3, 0x1)
    SetScenarioFlags(0x63, 2)
    OP_29(0x3F, 0x1, 0x11)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_42_6773 end

    def Function_43_69BF(): pass

    label("Function_43_69BF")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-40800, 4200, 21500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x101, -40800, 3000, 21500, 270)
    SetChrPos(0x102, -38230, 3000, 22130, 270)
    SetChrPos(0x103, -39000, 3000, 20760, 270)
    SetChrPos(0x104, -39000, 3000, 22800, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0286
    ChrTalk(
        0x101,
        "#0001F#5P（这是……？）\x02",
    )

    CloseMessageWindow()

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扶手上部的油漆\x01",
            "有多处剥落的痕迹。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)

    #C0288
    ChrTalk(
        0x103,
        "#0205F#11P罗伊德前辈……？\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x104,
        "#0305F#11P怎么了吗？从刚才开始就若有所思的。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0012F#5P没事……\x01",
            "没什么大不了的。\x02\x03",

            "#0008F（嗯……\x01",
            "　似乎是最近才留下的痕迹。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -39800, 3000, 21500, 270)
    OP_68(-39800, 4000, 21500, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26000, 0)
    SetScenarioFlags(0x63, 3)
    OP_29(0x3F, 0x1, 0x12)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_69BF end

    def Function_44_6B9B(): pass

    label("Function_44_6B9B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    OP_68(-34700, 4000, 20700, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26500, 0)
    SetChrPos(0x101, -35700, 3000, 20000, 270)
    SetChrPos(0x102, -35700, 3000, 21400, 270)
    SetChrPos(0x103, -34500, 3000, 20000, 270)
    SetChrPos(0x104, -34500, 3000, 21400, 270)
    SetChrPos(0x136, -37300, 3000, 20700, 270)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    FadeToBright(1000, 0)
    OP_68(-35700, 4000, 20700, 3000)
    OP_0D()
    OP_6F(0x1)
    OP_93(0x136, 0xB4, 0x12C)
    Sleep(1000)
    OP_93(0x136, 0x15E, 0x1F4)
    Sleep(1000)

    #C0291
    ChrTalk(
        0x136,
        (
            "#1301F#12P原来如此……\x01",
            "魔兽就是从这里闯入的啊。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6D10():
        OP_95(0xFE, -37280, 3000, 23830, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_6D10)

    def lambda_6D2A():

        label("loc_6D2A")

        TurnDirection(0x101, 0x136, 500)
        Yield()
        Jump("loc_6D2A")

    QueueWorkItem2(0x101, 1, lambda_6D2A)

    def lambda_6D3C():

        label("loc_6D3C")

        TurnDirection(0x102, 0x136, 500)
        Yield()
        Jump("loc_6D3C")

    QueueWorkItem2(0x102, 1, lambda_6D3C)

    def lambda_6D4E():

        label("loc_6D4E")

        TurnDirection(0x103, 0x136, 500)
        Yield()
        Jump("loc_6D4E")

    QueueWorkItem2(0x103, 1, lambda_6D4E)

    def lambda_6D60():

        label("loc_6D60")

        TurnDirection(0x104, 0x136, 500)
        Yield()
        Jump("loc_6D60")

    QueueWorkItem2(0x104, 1, lambda_6D60)
    Sleep(500)

    #C0292
    ChrTalk(
        0x101,
        (
            "#0001F#12P虽然还不清楚魔兽\x01",
            "为什么要进来……\x02\x03",

            "但以防万一，还是制定一下\x01",
            "相关对策比较好。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x136,
        (
            "#1308F#5P是啊，虽然时间上\x01",
            "不太宽裕……\x02\x03",

            "#1301F我想至少可以装上一个\x01",
            "防止魔兽入侵的防护栏。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        (
            "#0300F#11P嗯，光是装上那个，\x01",
            "就会安全很多了。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x136, 1)

    #C0295
    ChrTalk(
        0x103,
        (
            "#0200F#11P既要有一定的强度，\x01",
            "又必须是可活动的……\x02\x03",

            "这所医院有那样的设备吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x136, 0xB4, 0x1F4)
    Sleep(300)

    #C0296
    ChrTalk(
        0x136,
        (
            "#1304F#5P嗯，记得用于野外治疗的设备中\x01",
            "应该有这样的东西。\x02\x03",

            "#1300F和事务长商量一下，\x01",
            "把它安装上去吧。\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_68(-36180, 4000, 30470, 0)
    MoveCamera(36, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30450, 0)
    OP_68(-37360, 4000, 21820, 10000)
    SetMapObjFrame(0xFF, "model6", 0x1, 0x1)
    SetMapObjFrame(0xFF, "model5", 0x0, 0x1)
    SetMapObjFrame(0xFF, "CA02", 0x0, 0x1)
    LoadChrToIndex("chr/ch28000.itc", 0x1E)
    LoadChrToIndex("chr/ch29600.itc", 0x1F)
    LoadChrToIndex("chr/ch26000.itc", 0x20)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0x1E)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -34230, 3000, 24220, 90)
    SetChrFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0x1F)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -32750, 3000, 24110, 270)
    SetChrFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -36060, 3390, 24850, 0)
    SetChrFlags(0x24, 0x8000)
    BeginChrThread(0x24, 0, 0, 46)
    SetChrPos(0x101, -11300, 0, -700, 90)
    SetChrPos(0x102, -11300, 0, 700, 90)
    SetChrPos(0x103, -12700, 0, -700, 90)
    SetChrPos(0x104, -12700, 0, 700, 90)
    SetChrPos(0x136, -9000, 0, 0, 270)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFD, 0xD5, 0xC6, 0x19, 0xC8, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    EndChrThread(0x24, 0x3)
    Fade(2000)
    OP_68(-10300, 2000, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_68(-10300, 1000, 0, 4000)
    OP_6F(0x1)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0297
    AnonymousTalk(
        0x136,
        (
            "呵呵，辛苦了。\x02\x03",

            "这样一来，大家就都可以安心了，\x01",
            "真是多亏了你们呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0298
    ChrTalk(
        0x104,
        "#0309F#6P没有那回事啦，过奖了¤\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0004F#6P哈哈，事实上\x01",
            "我们并没有做什么。\x02\x03",

            "#0000F只是证明了是真的\x01",
            "有魔兽入侵过而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x136,
        (
            "#1304F#11P嗯，但如果连魔兽是否入侵过都不确定，\x01",
            "那么就无法采取正确的防范措施，\x01",
            "问题也就一直得不到解决。\x02\x03",

            "#1300F我想你们总有一天\x01",
            "一定能像亚里欧斯先生那样，\x01",
            "漂亮地完成任务。\x02\x03",

            "#1309F姐姐向你们保证⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#0005F#6P塞茜尔姐姐……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0302
    ChrTalk(
        0x104,
        "#0301F#6P感、感激不尽……！\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#0109F#6P非常感谢，\x01",
            "这番话对我们来说真是很大的鼓励。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        "#0202F#6P……我们会加油的。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x136,
        (
            "#1309F#11P呵呵……\x02\x03",

            "#1302F罗伊德，等我们两个都有时间了，\x01",
            "再好好聚聚吧。\x02\x03",

            "我也想和你一起去扫墓呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        "#0002F#6P……嗯，说得也是。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x136,
        (
            "#1304F#11P还有就是……\x02\x03",

            "#1302F如果你和艾莉或者小缇欧\x01",
            "开始交往了，\x01",
            "一定要跟我报告哦!\x02\x03",

            "#1309F我一定会好好为你庆祝的⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0308
    ChrTalk(
        0x101,
        (
            "#0011F#6P不，我说塞茜尔姐姐……\x01",
            "为什么会突然扯到这上面啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x136,
        (
            "#1306F#11P要不然，你和兰迪交往\x01",
            "也是可以的……\x02\x03",

            "#1301F到时候要联系我哦！\x01",
            "我会先看点那方面的书，\x01",
            "做好心理准备的！\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        "#0006F#6P哪方面的书啊……\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x104,
        (
            "#0309F#6P哎呀～！\x01",
            "要是能让塞茜尔小姐高兴的话，\x01",
            "我是不介意的哦！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 1000)
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0312
    ChrTalk(
        0x101,
        "#0011F#4S#11P喂，你给我介意一下啊！\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0313
    ChrTalk(
        0x136,
        (
            "#1309F#11P呵呵，那么我\x01",
            "就先失陪了。\x02\x03",

            "#1302F各位，回去的路上要小心哦。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7667():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7667)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0314
    ChrTalk(
        0x101,
        "#0002F#6P──嗯。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#0102F#6P承蒙您照顾了。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x136, 3, 0, 45)
    Sleep(3000)
    OP_68(-12000, 1000, 0, 4000)
    WaitChrThread(0x136, 3)
    OP_6F(0x1)

    #C0316
    ChrTalk(
        0x104,
        "#0309F#6P哈，真好啊……\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x102,
        (
            "#0104F#6P性格温和，又有包容力，\x01",
            "也很可靠……\x02\x03",

            "#0102F呵呵，是非常优秀的人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#0009F#6P哈哈……\x01",
            "你们能这么说，我很高兴。\x02\x03",

            "#0002F因为她比\x01",
            "亲姐姐还要照顾我。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x103,
        (
            "#0204F#6P……那么，罗伊德前辈。\x02\x03",

            "#0202F你实际上跟塞茜尔小姐是\x01",
            "何种关系呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x103, 600)

    #C0320
    ChrTalk(
        0x101,
        "#0011F#11P咦……？\x02",
    )

    CloseMessageWindow()

    def lambda_781B():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_781B)
    Sleep(50)

    def lambda_782B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_782B)
    WaitChrThread(0x102, 1)
    Sleep(300)

    #C0321
    ChrTalk(
        0x102,
        (
            "#0104F#5P说得也是呢……\x01",
            "我也有点在意。\x02\x03",

            "#0102F你看上去比平常\x01",
            "更有弟弟的感觉呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        "#0001F#11P那、那是什么意思啊……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        (
            "#0310F#5P罗伊德，你这家伙……！\x02\x03",

            "居然和那样优秀的姐姐\x01",
            "关系甜蜜暧昧吗！？\x02\x03",

            "#0307F真是太让人羡慕了！\x01",
            "请跟我交换身体吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#0006F#11P怎么可能做得到。\x02\x03",

            "#0001F别说傻话了，\x01",
            "差不多该回克洛斯贝尔了。\x02\x03",

            "太阳已经下山了……\x01",
            "回去之后还要整理总结\x01",
            "今天的调查报告书呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x103,
        "#0211F#6P（……在转移话题了……）\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        "#0111F#5P（嗯……做得真明显……）\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x104,
        (
            "#0310F#5P（该死的罗伊德……！\x01",
            "　竟然把那么符合我喜好的人……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7A6F():
        OP_93(0xFE, 0x13B, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7A6F)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0328
    ChrTalk(
        0x101,
        "#0003F#4S#11P你们几个，不要在那里嘀咕个没完了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    RemoveParty(0x35, 0x0)
    SetChrPos(0x0, -11510, 0, -140, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, -26990, 0, 1930, 270)
    SetScenarioFlags(0x63, 7)
    OP_29(0x3F, 0x1, 0x14)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_44_6B9B end

    def Function_45_7B4A(): pass

    label("Function_45_7B4A")

    OP_93(0xFE, 0x5A, 0x12C)

    def lambda_7B56():
        OP_95(0xFE, 1500, 1000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B56)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_7B8F():
        OP_95(0xFE, 4500, 1000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B8F)
    Sleep(500)

    def lambda_7BAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7BAC)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    Return()

    # Function_45_7B4A end

    def Function_46_7BDC(): pass

    label("Function_46_7BDC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7C48")
    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    Jump("Function_46_7BDC")

    label("loc_7C48")

    Return()

    # Function_46_7BDC end

    def Function_47_7C49(): pass

    label("Function_47_7C49")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch20400.itc", 0x1E)
    LoadChrToIndex("chr/ch20300.itc", 0x1F)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    OP_4B(0xD, 0xFF)
    SetChrFlags(0xD, 0x40)
    EventBegin(0x0)
    OP_68(-59370, 1400, 2570, 0)
    MoveCamera(49, 15, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -58140, 0, 2890, 0)
    SetChrPos(0x102, -57140, 0, 1620, 0)
    SetChrPos(0x103, -59300, 0, 1290, 0)
    SetChrPos(0x104, -58230, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0329
    ChrTalk(
        0x101,
        (
            "#0000F#6P那么……\x01",
            "我们就等巴士来吧。\x02\x03",

            "根据时刻表来看……\x01",
            "下一班车大概在十五分钟之后到达呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x104,
        (
            "#0305F#4P话说这个真的很方便呢。\x02\x03",

            "似乎一直运行到\x01",
            "晚上十一点。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x103,
        (
            "#0203F#6P车费也不贵……\x02\x03",

            "#0200F据说运营方是市政府，\x01",
            "不知道能不能保证收支平衡呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0332
    ChrTalk(
        0x102,
        (
            "#0102F呵呵，市政府对医院\x01",
            "似乎也是非常重视的。\x02\x03",

            "毕竟财政方面还算宽裕，\x01",
            "而且市民对这方面的需求也比较高。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0333
    ChrTalk(
        0x103,
        "#0202F#6P原来如此……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0334
    ChrTalk(
        0x101,
        (
            "#0000F#5P不管怎么说，来医院的交通如此便利，\x01",
            "实在是很值得庆幸呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-59000, 1000, 2200, 0)
    MoveCamera(66, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrPos(0x101, -56600, 0, 3800, 180)
    SetChrPos(0x102, -56600, 0, 4900, 180)
    SetChrPos(0x103, -56600, 0, 6000, 180)
    SetChrPos(0x104, -56600, 0, 7100, 180)
    SetChrPos(0x25, -56600, 0, 8200, 180)
    SetChrPos(0x26, -56600, 0, 9300, 180)
    SetChrPos(0xD, -56600, 0, 10400, 180)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x1C, 0x80)
    OP_78(0x7, 0x1C)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1C, -75000, 0, 500, 90)
    OP_D3(0x1C, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_8001():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8001)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x1C, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    Sleep(300)
    OP_71(0x7, 0x1, 0x1E, 0x1, 0x0)
    OP_79(0x7)
    Sound(464, 0, 100, 0)
    Sleep(1000)

    def lambda_8055():
        OP_9B(0x0, 0xFE, 0x0, 0xED8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8055)
    Sleep(100)

    def lambda_806D():
        OP_9B(0x0, 0xFE, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_806D)
    Sleep(80)

    def lambda_8085():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8085)
    Sleep(0)

    def lambda_809D():
        OP_9B(0x0, 0xFE, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_809D)
    Sleep(200)

    def lambda_80B5():
        OP_9B(0x0, 0xFE, 0x0, 0x2008, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_80B5)
    Sleep(100)

    def lambda_80CD():
        OP_9B(0x0, 0xFE, 0x0, 0x2454, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_80CD)
    Sleep(150)

    def lambda_80E5():
        OP_9B(0x0, 0xFE, 0x0, 0x28A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_80E5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x25, 1)
    WaitChrThread(0x26, 1)
    Sound(463, 0, 100, 0)
    WaitChrThread(0xD, 1)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-58690, 1000, 2150, 0)
    MoveCamera(75, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23360, 0)
    SetChrPos(0x1C, -59000, 0, 500, 270)
    OP_D3(0x1C, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_70(0x7, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_71(0x7, 0x3C, 0x5A, 0x0, 0x0)
    Sound(467, 0, 100, 0)
    Sound(465, 0, 100, 0)
    OP_79(0x7)
    OP_68(-62690, 1000, 2150, 4000)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_820C():
        OP_95(0xFE, -75000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_820C)
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7000", "ed7000")
    OP_6F(0x1)
    EndChrThread(0x1C, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    SetScenarioFlags(0x5C, 0)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_47_7C49 end

    def Function_48_827E(): pass

    label("Function_48_827E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch21100.itc", 0x1E)
    LoadChrToIndex("chr/ch21600.itc", 0x1F)
    LoadChrToIndex("chr/ch21800.itc", 0x20)
    LoadChrToIndex("chr/ch21900.itc", 0x21)
    OP_68(-51620, 2800, 4480, 0)
    MoveCamera(86, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23730, 0)
    SetChrPos(0x101, -50500, 0, -800, 270)
    SetChrPos(0xEF, -51500, 0, -800, 270)
    SetChrPos(0x153, -52500, 0, -800, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x153, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    OP_A7(0x25, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x1F)
    SetChrSubChip(0x26, 0x0)
    OP_A7(0x26, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    SetChrChipByIndex(0x27, 0x7)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x20)
    SetChrSubChip(0x28, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    SetChrChipByIndex(0x29, 0x21)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrPos(0x27, -56040, 0, 5750, 180)
    SetChrPos(0x28, -56040, 0, 6950, 180)
    SetChrPos(0x29, -56040, 0, 8150, 180)
    OP_4B(0x1D, 0xFF)
    SetMapObjFlags(0x7, 0x1000)
    ClearMapObjFlags(0x7, 0x4)
    ClearChrFlags(0x1D, 0x80)
    OP_78(0x7, 0x1D)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x1D, -75000, 0, 500, 90)
    OP_D3(0x1D, 0x0, 0x15F90, 0x0, 0x0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)

    def lambda_8427():
        OP_95(0xFE, -56000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8427)
    Sound(466, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_68(-51620, 200, 4480, 6000)
    OP_6F(0x1)
    OP_0D()
    WaitChrThread(0x1D, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1, 0x1E, 0x1, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x7)
    BeginChrThread(0x25, 3, 0, 49)
    Sleep(750)
    BeginChrThread(0x26, 3, 0, 49)
    Sleep(750)
    BeginChrThread(0x101, 3, 0, 50)
    Sleep(750)
    BeginChrThread(0x153, 3, 0, 52)
    Sleep(750)
    BeginChrThread(0xEF, 3, 0, 51)
    Sleep(750)
    Sleep(1500)
    BeginChrThread(0x27, 3, 0, 53)
    Sleep(350)
    BeginChrThread(0x28, 3, 0, 53)
    Sleep(350)
    BeginChrThread(0x29, 3, 0, 53)
    Sleep(350)
    Sleep(1500)
    EndChrThread(0x27, 0x3)
    EndChrThread(0x28, 0x3)
    EndChrThread(0x29, 0x3)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    Fade(1000)
    OP_68(-46640, 200, 360, 0)
    MoveCamera(40, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21360, 0)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x153, 3)
    WaitChrThread(0xEF, 3)
    OP_0D()

    #C0335
    ChrTalk(
        0x153,
        (
            "#1109F#6P嘿嘿……\x01",
            "实在是太开心了！\x02\x03",

            "#1110F虽然走路很开心，\x01",
            "但坐巴士也很开心呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#0014F#11P哈哈，这样啊。\x02\x03",

            "#0008F（琪雅看起来好像是\x01",
            "　第一次坐导力车呢……）\x02\x03",

            "#0001F（莫非她也没坐过\x01",
            "　导力列车或飞行船吗……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x153,
        (
            "#1105F#6P话说……\x01",
            "这里就是叫做医院的地方吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#0004F#11P是啊，叫做医科大学，\x01",
            "也是一个进行各种研究的医院哦。\x02\x03",

            "#0000F说不定可以帮琪雅把\x01",
            "忘记的事情想起来。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8735")

    #C0339
    ChrTalk(
        0x153,
        (
            "#1106F#6P嗯……琪雅其实\x01",
            "并不在乎想不想得起来。\x02\x03",

            "#1100F但如果琪雅想起来的话，\x01",
            "罗伊德和艾莉会更高兴吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8822")

    label("loc_8735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_87AE")

    #C0340
    ChrTalk(
        0x153,
        (
            "#1106F#6P嗯……琪雅其实\x01",
            "并不在乎想不想得起来。\x02\x03",

            "#1100F但如果琪雅想起来的话，\x01",
            "罗伊德和缇欧会更高兴吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8822")

    label("loc_87AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_8822")

    #C0341
    ChrTalk(
        0x153,
        (
            "#1106F#6P嗯……琪雅其实\x01",
            "并不在乎想不想得起来。\x02\x03",

            "#1100F但如果琪雅想起来的话，\x01",
            "罗伊德和兰迪会更高兴吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8822")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0342
    ChrTalk(
        0x101,
        (
            "#0002F#11P嗯、嗯……\x01",
            "当然会更高兴。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_88DA")

    #C0343
    ChrTalk(
        0x102,
        (
            "#0104F#5P琪雅肯定有许多\x01",
            "非常珍贵的回忆。\x02\x03",

            "#0102F所以要加油\x01",
            "想起来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8986")

    label("loc_88DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8939")

    #C0344
    ChrTalk(
        0x103,
        (
            "#0203F#5P……琪雅应该会有非常\x01",
            "珍贵的回忆。\x02\x03",

            "#0202F所以努力\x01",
            "加油回想起来吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8986")

    label("loc_8939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_8986")

    #C0345
    ChrTalk(
        0x104,
        (
            "#0306F#5P阿琪应该有很多\x01",
            "珍贵的回忆。\x02\x03",

            "#0300F不取回来怎么行呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8986")


    #C0346
    ChrTalk(
        0x153,
        (
            "#1104F#6P嗯，我知道了。\x02\x03",

            "#1110F琪雅会加油\x01",
            "想起来的！\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#0004F#11P嗯，就是要有那股气势。\x02\x03",

            "#0000F……但是，\x01",
            "也不要太勉强哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x153,
        "#1109F#6P嗯！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_8A67")

    #C0349
    ChrTalk(
        0x102,
        (
            "#0102F#5P呵呵，那么\x01",
            "去接待处问问关于\x01",
            "『神经科』的事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF6")

    label("loc_8A67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_8AB0")

    #C0350
    ChrTalk(
        0x103,
        (
            "#0202F#5P……那么去\x01",
            "接待处问问关于\x01",
            "『神经科』的事吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8AF6")

    label("loc_8AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_8AF6")

    #C0351
    ChrTalk(
        0x104,
        (
            "#0302F#5P好了，那么\x01",
            "去接待处问问关于\x01",
            "『神经科』的事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8AF6")

    OP_57(0x0)
    OP_5A()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(471, 0, 100, 0)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    SetChrPos(0x0, -48100, 0, -400, 90)
    ModifyEventFlags(1, 1, 0x80)
    SetScenarioFlags(0xA8, 4)
    OP_29(0x48, 0x1, 0x6)
    Sleep(500)
    EventEnd(0x5)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x79, 0xB4, 0x0, 0x20)
    OP_4C(0x1D, 0xFF)
    Return()

    # Function_48_827E end

    def Function_49_8B60(): pass

    label("Function_49_8B60")

    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_8B76():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8B76)

    def lambda_8B90():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B90)
    WaitChrThread(0xFE, 1)

    def lambda_8BA5():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8BA5)
    WaitChrThread(0xFE, 1)

    def lambda_8BC3():
        OP_95(0xFE, -46150, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8BC3)
    WaitChrThread(0xFE, 1)

    def lambda_8BE1():
        OP_95(0xFE, -33950, 0, -50, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8BE1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_49_8B60 end

    def Function_50_8BFF(): pass

    label("Function_50_8BFF")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_8C1A():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C1A)

    def lambda_8C34():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8C34)
    WaitChrThread(0xFE, 1)

    def lambda_8C49():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C49)
    WaitChrThread(0xFE, 1)

    def lambda_8C67():
        OP_95(0xFE, -47080, 0, -1280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8C67)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x10E, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_50_8BFF end

    def Function_51_8C91(): pass

    label("Function_51_8C91")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_8CAC():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CAC)

    def lambda_8CC6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8CC6)
    WaitChrThread(0xFE, 1)

    def lambda_8CDB():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CDB)
    WaitChrThread(0xFE, 1)

    def lambda_8CF9():
        OP_95(0xFE, -47530, 0, 180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8CF9)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xE1, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_51_8C91 end

    def Function_52_8D23(): pass

    label("Function_52_8D23")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_8D3E():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D3E)

    def lambda_8D58():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8D58)
    WaitChrThread(0xFE, 1)

    def lambda_8D6D():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D6D)
    WaitChrThread(0xFE, 1)

    def lambda_8D8B():
        OP_95(0xFE, -48510, 0, -1230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8D8B)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_52_8D23 end

    def Function_53_8DB5(): pass

    label("Function_53_8DB5")


    def lambda_8DBA():
        OP_95(0xFE, -56060, 0, 3950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DBA)
    WaitChrThread(0xFE, 1)

    def lambda_8DD8():
        OP_95(0xFE, -55990, 600, 1320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8DD8)
    Sleep(1200)

    def lambda_8DF5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8DF5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_53_8DB5 end

    def Function_54_8E0A(): pass

    label("Function_54_8E0A")

    Sleep(7000)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)
    Return()

    # Function_54_8E0A end

    def Function_55_8E23(): pass

    label("Function_55_8E23")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch05300.itc", 0x1E)
    OP_68(-22700, 1000, -500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24000, 0)
    SetChrPos(0x101, -26700, 0, -1100, 90)
    SetChrPos(0x153, -28000, 0, -500, 90)
    SetChrPos(0xEF, -26700, 0, 100, 90)
    SetChrPos(0x1E, -9000, 0, -500, 270)
    SetChrChipByIndex(0x1E, 0x1E)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    OP_4B(0x1E, 0xFF)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01300.itp")
    ModifyEventFlags(0, 1, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    FadeToBright(1000, 0)

    def lambda_8F1F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8F1F)
    Sleep(100)

    def lambda_8F37():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_8F37)
    Sleep(150)

    def lambda_8F4F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_8F4F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    OP_0D()

    #N0352
    NpcTalk(
        0x1E,
        "女性的声音",
        "咦……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x101,
        "#0002F#6P啊……\x02",
    )

    CloseMessageWindow()
    OP_68(-14700, 1000, -500, 3000)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-21000, 1000, -500, 0)
    SetCameraDistance(23000, 0)
    OP_98(0x1E, 0xFFFFE890, 0x0, 0x0, 0x0, 0x0)

    def lambda_9021():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9021)

    def lambda_9036():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9036)
    Sleep(100)

    def lambda_904E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_904E)
    Sleep(150)

    def lambda_9066():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9066)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1E, 1)
    OP_6F(0x1)
    OP_0D()

    #C0354
    ChrTalk(
        0x101,
        "#0000F#6P塞茜尔姐姐……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_90E4")

    #C0355
    ChrTalk(
        0x102,
        (
            "#0102F#6P塞茜尔小姐，\x01",
            "您好，好久不见了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_914E")

    label("loc_90E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9111")

    #C0356
    ChrTalk(
        0x103,
        "#0202F#6P……好久不见了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_914E")

    label("loc_9111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_914E")

    #C0357
    ChrTalk(
        0x104,
        (
            "#0309F#6P哦哦，塞茜尔小姐！\x01",
            "你好，好久不见了！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_914E")

    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0358
    AnonymousTalk(
        0x1E,
        (
            "呵呵……\x01",
            "你们两个都很精神呢。\x02\x03",

            "纪念庆典期间辛苦你们了。\x01",
            "很多事情忙得不可开交吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0359
    ChrTalk(
        0x101,
        (
            "#0012F#6P哈哈……算是吧。\x02\x03",

            "#0006F说实话，这五天的\x01",
            "工作强度真不是一般的大。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_929E")

    #C0360
    ChrTalk(
        0x102,
        (
            "#0106F#6P而且在那之后的一周里\x01",
            "也发生了很多事情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9325")

    label("loc_929E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_92E4")

    #C0361
    ChrTalk(
        0x103,
        (
            "#0206F#6P而且在那之后的一周里\x01",
            "也发生了很多事情……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9325")

    label("loc_92E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9325")

    #C0362
    ChrTalk(
        0x104,
        (
            "#0306F#6P而且在那之后的一周里\x01",
            "也发生了很多事情……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9325")


    #C0363
    ChrTalk(
        0x1E,
        (
            "#1302F#11P哎呀，但是你们两人看上去\x01",
            "并不是很疲倦呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x1E,
        "#1305F#11P啊，这孩子是……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    def lambda_93AF():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_93AF)
    WaitChrThread(0x153, 1)

    #C0365
    ChrTalk(
        0x153,
        (
            "#1110F#6P那个那个，罗伊德。\x02\x03",

            "这个姐姐也是\x01",
            "罗伊德的朋友吗？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9408():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9408)
    Sleep(50)

    def lambda_9418():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9418)
    Sleep(300)

    #C0366
    ChrTalk(
        0x101,
        (
            "#0000F#11P嗯，没错哦。\x02\x03",

            "她是塞茜尔姐姐，\x01",
            "就像我的\x01",
            "亲姐姐一样──\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1E)
    Sleep(300)

    #C0367
    ChrTalk(
        0x1E,
        (
            "#1303F#11P#40W……怎、怎么会……\x02\x03",

            "#1308F#40W罗、罗伊德居然\x01",
            "一直#2S……瞒着我……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_94CA():
        TurnDirection(0xFE, 0x1E, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_94CA)

    def lambda_94D7():
        TurnDirection(0xFE, 0x1E, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_94D7)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0368
    ChrTalk(
        0x101,
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0369
    ChrTalk(
        0x1E,
        (
            "#1306F#11P罗伊德居然背着我\x01",
            "#4S结婚了……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)

    #C0370
    ChrTalk(
        0x101,
        "#0011F#4S#6P啊！？\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x1E,
        (
            "#1303F#11P嗯，不用对我隐瞒了！\x02\x03",

            "#1301F小朋友，\x01",
            "你叫什么名字！？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x153,
        "#1110F#6P我叫琪雅。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_96B3")

    #C0373
    ChrTalk(
        0x1E,
        (
            "#1309F#11P小琪雅啊……\x01",
            "呵呵，真是可爱的名字。\x02\x03",

            "#1308F不过长得不太像罗伊德呢，\x01",
            "莫非是像母亲……\x02\x03",

            "但是，长得也不像\x01",
            "艾莉呀……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x102,
        "#0112F#6P那、那个，塞茜尔小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9828")

    label("loc_96B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9767")

    #C0375
    ChrTalk(
        0x1E,
        (
            "#1309F#11P小琪雅……\x01",
            "呵呵，真是可爱的名字呢。\x02\x03",

            "#1308F不过长得不太像罗伊德呢，\x01",
            "莫非是像母亲……\x02\x03",

            "但是，长得也不像\x01",
            "小缇欧呀……\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        "#0211F#6P那个，塞茜尔小姐……\x02",
    )

    CloseMessageWindow()
    Jump("loc_9828")

    label("loc_9767")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9828")

    #C0377
    ChrTalk(
        0x1E,
        (
            "#1309F#11P小琪雅……\x01",
            "呵呵，真是可爱的名字呢。\x02\x03",

            "#1308F不过长得不太像罗伊德，\x01",
            "莫非是像母亲……\x02\x03",

            "#1301F还是说，是兰迪跟其他女人\x01",
            "生的孩子吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        "#0305F#6P等、等等，塞茜尔小姐……\x02",
    )

    CloseMessageWindow()

    label("loc_9828")


    #C0379
    ChrTalk(
        0x101,
        (
            "#0012F#6P啊啊啊啊！\x01",
            "你冷静一点啦！\x02\x03",

            "#0011F说什么我是琪雅的父亲……\x01",
            "从年龄上来看，\x01",
            "也根本不可能吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1100)
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x1E)

    #C0380
    ChrTalk(
        0x1E,
        (
            "#1305F#11P咦……\x02\x03",

            "#1309F……仔细一想的话，\x01",
            "说得也是呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0381
    ChrTalk(
        0x101,
        (
            "#0012F#6P这、这种事根本不用仔细想\x01",
            "也能明白吧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_999D")

    #C0382
    ChrTalk(
        0x102,
        (
            "#0106F#6P塞茜尔小姐……\x01",
            "有点天然呆啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A20")

    label("loc_999D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_99DF")

    #C0383
    ChrTalk(
        0x103,
        (
            "#0206F#6P塞茜尔小姐……\x01",
            "没想到竟然那么天然呆。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9A20")

    label("loc_99DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9A20")

    #C0384
    ChrTalk(
        0x104,
        (
            "#0309F#6P塞茜尔小姐……\x01",
            "这种天然呆的性格也好棒啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9A20")


    #C0385
    ChrTalk(
        0x153,
        "#1105F#6P咦咦～？\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(24000, 2000)
    OP_6F(0x10)
    OP_0D()
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetScenarioFlags(0x5C, 1)
    NewScene("t1510", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_55_8E23 end

    def Function_56_9A78(): pass

    label("Function_56_9A78")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    StopEffect(0x8, 0x0)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch05400.itc", 0x1F)
    OP_68(1400, 1700, 530, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(31300, 0)
    SetChrPos(0x101, 100000, 0, 0, 0)
    SetChrPos(0xEF, 100000, 0, 0, 0)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, 4000, 1000, 0, 270)
    OP_A7(0x20, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -23770, -1000, -26000, 180)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    SetCameraDistance(29800, 2500)
    OP_6F(0x10)
    OP_0D()
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_9B7D():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_9B7D)

    def lambda_9B92():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_9B92)
    WaitChrThread(0x20, 1)
    WaitChrThread(0x20, 2)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)

    #C0386
    ChrTalk(
        0x20,
        (
            "#1101F#11P真是的，罗伊德\x01",
            "完全不了解别人的心情。\x02\x03",

            "#1108F……记忆那种东西，\x01",
            "即使没有也无所谓的……\x02\x03",

            "#1106F为什么大家\x01",
            "都那么在意呢？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-1400, 1700, 530, 5000)

    def lambda_9C61():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_9C61)
    Sleep(3000)
    Fade(1000)
    OP_68(-24820, 1700, -1120, 0)
    MoveCamera(46, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(29800, 0)
    SetCameraDistance(25490, 3500)
    EndChrThread(0x20, 0x1)
    SetChrPos(0x20, -17660, 0, -310, 270)

    def lambda_9CCA():
        OP_9B(0x0, 0xFE, 0x0, 0x189C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_9CCA)
    WaitChrThread(0x20, 1)
    OP_63(0x20, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)
    OP_93(0x20, 0xB4, 0x12C)
    Sleep(750)
    OP_93(0x20, 0x10E, 0x1F4)
    OP_93(0x20, 0x0, 0x1F4)
    Sleep(750)
    OP_93(0x20, 0x10E, 0x12C)
    Sleep(750)

    #C0387
    ChrTalk(
        0x20,
        (
            "#1105F#11P咦咦……\x02\x03",

            "这里是哪里啊？\x02\x03",

            "？？？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x20)
    OP_93(0x20, 0xB4, 0x12C)
    Sleep(500)

    #C0388
    ChrTalk(
        0x20,
        (
            "#1114F#5P嗯……\x02\x03",

            "#1101F……琪雅这是\x01",
            "迷路了吗？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0389
    ChrTalk(
        0x20,
        "#1105F#5P啊……\x02",
    )

    CloseMessageWindow()
    OP_68(-24820, 1700, -4120, 3000)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7523", 0)
    OP_68(-24150, 0, -34360, 0)
    MoveCamera(46, 18, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22830, 0)
    FadeToBright(1000, 0)
    OP_68(-24020, 0, -26990, 6000)
    SetCameraDistance(20600, 6000)
    OP_6F(0x1)
    Sleep(300)

    #C0390
    ChrTalk(
        0x1F,
        (
            "#1502F#5P……呵呵，好清爽的风啊…………\x02\x03",

            "爸爸……\x01",
            "今天什么时候过来呢？\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x20, -24000, 0, -14410, 180)
    Sleep(300)
    #Sound(2035, 255, 100, 0)    #voice#KeA
    Sleep(150)

    #C0391
    ChrTalk(
        0x20,
        "喂喂！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1F, 0x0, 0x190)
    OP_68(-23780, 0, -25230, 2500)

    def lambda_9F00():
        OP_95(0xFE, -23770, -1000, -24500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_9F00)
    WaitChrThread(0x20, 1)

    #C0392
    ChrTalk(
        0x1F,
        "#1505F#12P你是……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x20,
        (
            "#1110F#5P那个，从这里能看到什么吗？\x02\x03",

            "#1109F莫非\x01",
            "有鱼在水里游吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x1F,
        (
            "#1500F#12P呵呵……\x02\x03",

            "虽然我看不见，\x01",
            "但我想应该有鱼在水里游哦。\x02\x03",

            "有时候能听到\x01",
            "鱼儿欢快地跳出水面的声音……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    MoveCamera(46, 14, 0, 1500)
    OP_68(-24970, 0, -26730, 1500)

    def lambda_A023():
        OP_95(0xFE, -24860, -1000, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A023)

    def lambda_A03D():

        label("loc_A03D")

        TurnDirection(0xFE, 0x20, 400)
        Yield()
        Jump("loc_A03D")

    QueueWorkItem2(0x1F, 1, lambda_A03D)
    WaitChrThread(0x20, 1)
    EndChrThread(0x1F, 0x1)
    OP_93(0x20, 0xB4, 0x1F4)
    Sleep(500)
    OP_63(0x20, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0395
    ChrTalk(
        0x20,
        (
            "#1105F#5P啊，真的呢！\x01",
            "好像有很多哦！\x02\x03",

            "#1109F嗯，琪雅\x01",
            "也想钓鱼。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x10E, 0x190)

    #C0396
    ChrTalk(
        0x1F,
        (
            "#1500F#11P呵呵……\x01",
            "你叫小琪雅吗？\x02\x03",

            "我是滴，\x01",
            "滴·马克莱因。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x5A, 0x1F4)
    Sleep(300)

    #C0397
    ChrTalk(
        0x20,
        (
            "#1111F#5P滴、滴……\x02\x03",

            "#1109F嗯，真是好名字！\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x1F,
        (
            "#1500F#11P呵呵，谢谢。\x02\x03",

            "我觉得小琪雅的名字\x01",
            "也很棒。\x02\x03",

            "你是来这里探病的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x20,
        (
            "#1105F#5P啊，不是哦。\x02\x03",

            "#1108F琪雅是来\x01",
            "让医生找回记忆的……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x1F,
        "#1505F#11P记忆……？\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x20,
        (
            "#1101F#5P那个戴眼镜的医生\x01",
            "要让琪雅跟罗伊德他们分开，\x01",
            "所以琪雅就逃了出来。\x02\x03",

            "#1104F呵呵，\x01",
            "也就是所谓的战略性撤退。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0402
    ChrTalk(
        0x1F,
        (
            "#1508F#11P你说逃出来……\x02\x03",

            "#1505F（咦，罗伊德他们？\x01",
            "　莫非……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x20,
        (
            "#1110F#5P喂喂，滴。\x02\x03",

            "为什么从刚才开始\x01",
            "就一直闭着眼睛呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x1F,
        (
            "#1500F#11P啊，那个……\x02\x03",

            "因为我的眼睛看不见东西，\x01",
            "所以才会住院的……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x20,
        (
            "#1105F#5P哦，原来是这样啊。\x02\x03",

            "#1100F琪雅也没有记忆，\x01",
            "我们同病相怜呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0406
    ChrTalk(
        0x1F,
        (
            "#1505F#11P啊……记忆……\x02\x03",

            "#1508F嗯，原来是这样啊……\x02\x03",

            "……你什么都记不起来了吗？\x01",
            "爸爸、妈妈之类的。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x20,
        (
            "#1100F#5P……嗯，好像是这样的。\x02\x03",

            "#1109F但是，有罗伊德他们在，\x01",
            "所以一点也不寂寞！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x1F,
        (
            "#1500F#11P呵呵，这样啊……\x02\x03",

            "#1508F……我也一样，\x01",
            "虽然妈妈已经不在人世了……\x02\x03",

            "#1510F但我还有爸爸在，\x01",
            "医院的各位也都很温柔，\x01",
            "所以应该是不寂寞的吧……\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19600, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetScenarioFlags(0xA9, 0)
    SetScenarioFlags(0xA9, 7)
    StopBGM(0x1388)
    WaitBGM()
    EventEnd(0x5)
    NewScene("t1600", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_56_9A78 end

    def Function_57_A533(): pass

    label("Function_57_A533")

    EventBegin(0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EventBegin(0x0)
    LoadChrToIndex("chr/ch08200.itc", 0x1E)
    LoadChrToIndex("chr/ch05400.itc", 0x1F)
    LoadChrToIndex("chr/ch02400.itc", 0x20)
    LoadChrToIndex("apl/ch50384.itc", 0x21)
    OP_68(-23910, 800, -12480, 0)
    MoveCamera(41, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23640, 0)
    SetChrPos(0x101, -23500, 0, -15070, 180)
    SetChrPos(0xEF, -24520, 0, -14530, 180)
    SetChrChipByIndex(0x20, 0x1E)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    SetChrPos(0x20, -24570, -1000, -26000, 90)
    SetChrChipByIndex(0x1F, 0x1F)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -23240, -1000, -26000, 270)
    SetChrChipByIndex(0x21, 0x20)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x21, -23910, 0, -2470, 180)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ModifyEventFlags(0, 2, 0x80)
    StopBGM(0xFA0)
    FadeToBright(1000, 0)
    OP_68(-23910, 800, -15480, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0409
    ChrTalk(
        0x101,
        "#0000F#5P找到了……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A68B")

    #C0410
    ChrTalk(
        0x102,
        "#0102F#5P终于找到了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6DE")

    label("loc_A68B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A6B6")

    #C0411
    ChrTalk(
        0x103,
        "#0202F#5P终于找到了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A6DE")

    label("loc_A6B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A6DE")

    #C0412
    ChrTalk(
        0x104,
        "#0300F#5P原来在这里啊……\x02",
    )

    CloseMessageWindow()

    label("loc_A6DE")

    OP_5A()
    Fade(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-24970, 0, -26730, 0)
    MoveCamera(46, 14, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(20600, 0)
    SetCameraDistance(20000, 20000)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7514", 0)

    #C0413
    ChrTalk(
        0x20,
        (
            "#1110F#5P还有、还有哦！\x02\x03",

            "还有一条叫蔡特的大狗，\x01",
            "它非常非常大哦！\x02\x03",

            "平时总是一副很骄傲的样子，\x01",
            "全身毛茸茸的。\x02\x03",

            "#1109F如果骑在它背上的话，\x01",
            "肯定会非常舒服呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x1F,
        (
            "#1500F#11P呵呵，这样啊。\x02\x03",

            "#1502F很大的狗……\x01",
            "身上的毛应该很柔软吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x20,
        (
            "#1110F#5P滴偶尔也会\x01",
            "来市里吧？\x02\x03",

            "到时候来一起\x01",
            "跟蔡特玩吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x1F,
        (
            "#1500F#11P啊哈哈……嗯。\x01",
            "是不是该拜托下爸爸呢？\x02\x03",

            "#1505F啊，拜托艾丝蒂尔他们的话，\x01",
            "应该会陪我去的吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0417
    ChrTalk(
        0x20,
        (
            "#1105F#5P啊，艾丝蒂尔就是\x01",
            "那个游击士姐姐吧？\x02\x03",

            "#1100F滴也认识她啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x1F,
        (
            "#1500F#11P呵呵，有时去市里时，\x01",
            "她会陪我去买东西。\x02\x03",

            "因为爸爸一直都很忙……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(-23930, 900, -16040, 0)
    MoveCamera(47, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23640, 0)
    OP_0D()

    #C0419
    ChrTalk(
        0x101,
        (
            "#0002F#5P哈哈……\x01",
            "原来是和小滴在一起啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_AA2B")

    #C0420
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵，好像\x01",
            "聊得很开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA92")

    label("loc_AA2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_AA5D")

    #C0421
    ChrTalk(
        0x103,
        (
            "#0204F#5P……聊得\x01",
            "非常开心呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AA92")

    label("loc_AA5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_AA92")

    #C0422
    ChrTalk(
        0x104,
        (
            "#0309F#5P话说她们似乎聊得\x01",
            "非常起劲呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_AA92")


    #N0423
    NpcTalk(
        0x21,
        "男人的声音",
        (
            "#4P呵呵……\x01",
            "小孩子都是很快就能互相熟悉起来的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_AB0C():
        OP_93(0xFE, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AB0C)
    Sleep(50)

    def lambda_AB1C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_AB1C)
    OP_68(-23930, 900, -14040, 5000)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_AB45():
        OP_95(0xFE, -23910, 0, -12470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_AB45)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0424
    ChrTalk(
        0x101,
        "#0005F#12P亚、亚里欧斯先生……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_ABC8")

    #C0425
    ChrTalk(
        0x102,
        "#0104F#12P上次的事件承蒙您照顾了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC2B")

    label("loc_ABC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_AC00")

    #C0426
    ChrTalk(
        0x103,
        "#0204F#12P上次的事件真是感激不尽……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AC2B")

    label("loc_AC00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_AC2B")

    #C0427
    ChrTalk(
        0x104,
        "#0303F#12P上次的事件谢谢了。\x02",
    )

    CloseMessageWindow()

    label("loc_AC2B")


    #C0428
    ChrTalk(
        0x21,
        (
            "#1404F#5P之前那件事，\x01",
            "你们并没有必要觉得欠我人情。\x02\x03",

            "#1400F话说回来──\x01",
            "那个女孩就是……？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x101,
        (
            "#0000F#12P是啊，您是从米歇尔先生\x01",
            "那里听说的吧。\x02\x03",

            "#0004F嗯……\x01",
            "她的名字叫做琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x21,
        (
            "#1405F#5P是吗……\x02\x03",

            "………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xEF, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0431
    ChrTalk(
        0x101,
        (
            "#0005F#12P那个……\x01",
            "琪雅怎么了吗？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_ADA7")

    #C0432
    ChrTalk(
        0x102,
        "#0101F#12P难道您和琪雅以前见过面……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE10")

    label("loc_ADA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_ADDF")

    #C0433
    ChrTalk(
        0x103,
        "#0201F#12P难道您以前见过琪雅……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE10")

    label("loc_ADDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_AE10")

    #C0434
    ChrTalk(
        0x104,
        "#0301F#12P难道您以前见过她……！？\x02",
    )

    CloseMessageWindow()

    label("loc_AE10")


    #C0435
    ChrTalk(
        0x21,
        (
            "#1402F#5P没有……\x01",
            "只是觉得她是个很不可思议的女孩子。\x02\x03",

            "#1404F虽然我女儿──滴是个懂礼貌，\x01",
            "而且待人随和的孩子，\x01",
            "但她有时会对人客气过头。\x02\x03",

            "因此跟同龄的孩子\x01",
            "不怎么亲近……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x101,
        (
            "#0012F#12P啊，原来如此。\x02\x03",

            "#0002F……感觉她们\x01",
            "两个相处得很好呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x21,
        "#1402F#5P是啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    #C0438
    ChrTalk(
        0x21,
        (
            "#1403F#5P……虽然不知道那个女孩子\x01",
            "究竟有什么样的背景。\x02\x03",

            "#1400F但是既然与她扯上关系了，\x01",
            "你们就要负责任到底。\x02\x03",

            "#1404F而且……\x01",
            "还要认真将她照顾好。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x101,
        (
            "#0005F#12P啊……\x02\x03",

            "#0004F是，我也正有此意。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x1F,
        "#1505F#1P……爸爸？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B044")

    #C0441
    ChrTalk(
        0x20,
        (
            "#1107F#1P啊……\x01",
            "罗伊德和艾莉！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A7")

    label("loc_B044")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B078")

    #C0442
    ChrTalk(
        0x20,
        (
            "#1107F#1P啊……\x01",
            "罗伊德和缇欧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B0A7")

    label("loc_B078")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B0A7")

    #C0443
    ChrTalk(
        0x20,
        (
            "#1107F#1P啊……\x01",
            "罗伊德和兰迪！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B0A7")


    def lambda_B0AC():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B0AC)
    Sleep(50)

    def lambda_B0BC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B0BC)
    WaitChrThread(0x101, 1)

    #C0444
    ChrTalk(
        0x101,
        "#0012F#5P发现我们了啊……\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x21,
        "#1402F#5P……嗯。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-24710, 200, -23740, 0)
    MoveCamera(44, 16, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27550, 0)
    SetCameraDistance(24550, 3000)
    SetChrPos(0x1F, -23760, -1000, -24640, 0)
    SetChrPos(0x20, -25130, -1000, -24700, 45)
    SetChrPos(0x101, -24850, -1000, -17000, 180)
    SetChrPos(0xEF, -26280, -1000, -17870, 180)
    SetChrPos(0x21, -23900, -1000, -18210, 180)

    def lambda_B195():

        label("loc_B195")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_B195")

    QueueWorkItem2(0x20, 2, lambda_B195)

    def lambda_B1A7():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B1A7)
    Sleep(50)

    def lambda_B1BF():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B1BF)
    Sleep(50)

    def lambda_B1D7():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B1D7)
    WaitChrThread(0xEF, 1)

    def lambda_B1F0():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B1F0)
    WaitChrThread(0x101, 1)

    def lambda_B201():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B201)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x21, 1)
    EndChrThread(0x20, 0x2)
    OP_6F(0x79)
    OP_0D()

    #C0446
    ChrTalk(
        0x1F,
        (
            "#1500F#12P爸爸，欢迎回来。\x02\x03",

            "工作辛苦吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x21,
        (
            "#1404F#5P不……\x01",
            "这次并不辛苦。\x02\x03",

            "#1402F我回来了，滴。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x20,
        (
            "#1105F#6P这个人就是\x01",
            "滴的爸爸吗？\x02\x03",

            "#1110F好高啊。\x02\x03",

            "#1109F而且看起来好像很强！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x10E, 0x190)

    #C0449
    ChrTalk(
        0x1F,
        "#1502F#11P嘿嘿……是吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_B315():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_B315)
    Sleep(150)

    def lambda_B325():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B325)
    Sleep(150)

    #C0450
    ChrTalk(
        0x1F,
        (
            "#1500F#12P还有两位也是……\x01",
            "下午好，好久不见了。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        "#0002F#5P嗯，好久不见。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B3CA")

    #C0452
    ChrTalk(
        0x102,
        (
            "#0109F#5P呵呵，好像和小琪雅\x01",
            "成为朋友了吧？谢谢你哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B433")

    label("loc_B3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B3FE")

    #C0453
    ChrTalk(
        0x103,
        (
            "#0202F#5P谢谢你和琪雅\x01",
            "做朋友哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B433")

    label("loc_B3FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B433")

    #C0454
    ChrTalk(
        0x104,
        (
            "#0309F#5P哈哈，谢谢你跟阿琪\x01",
            "做朋友啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B433")


    #C0455
    ChrTalk(
        0x1F,
        (
            "#1502F#12P啊，不，我才应该感谢\x01",
            "琪雅跟我成为朋友呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x0, 0x1F4)
    Sleep(150)

    #C0456
    ChrTalk(
        0x20,
        (
            "#1103F#12P……罗伊德。\x02\x03",

            "#1101F琪雅绝对不要\x01",
            "搬到这里来哦！\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        (
            "#0006F#5P嗯，琪雅的决心我已经充分理解了。\x02\x03",

            "#0002F啊，但是……\x01",
            "如果搬到这里的话，说不定\x01",
            "可以跟小滴在一起哦。\x02\x03",

            "你们不是成了好朋友吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0458
    ChrTalk(
        0x20,
        (
            "#1110F#12P真的吗！？\x02\x03",

            "#1108F啊，但是……琪雅还是不想\x01",
            "跟罗伊德还有大家分开……\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x1F,
        (
            "#1508F#12P真是的，罗伊德警官……\x01",
            "不可以说欺负人的话哦。\x02\x03",

            "小琪雅会困扰的。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        (
            "#0012F#5P哈哈，说得也是呢。\x02\x03",

            "#0000F对不起，琪雅。\x01",
            "今天差不多该回去了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x20,
        (
            "#1112F#12P嗯，但琪雅还想跟滴\x01",
            "再说一会话。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B6DC")

    #C0462
    ChrTalk(
        0x102,
        (
            "#0104F#5P呵呵，下次再来玩就好了。\x02\x03",

            "#0100F小滴来市里时，\x01",
            "也可以让她来我们那里玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7A5")

    label("loc_B6DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B744")

    #C0463
    ChrTalk(
        0x103,
        (
            "#0204F#5P……下次再来玩就好了。\x02\x03",

            "#0202F小滴来市里的时候，\x01",
            "也可以让她来我们支援科玩。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B7A5")

    label("loc_B744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B7A5")

    #C0464
    ChrTalk(
        0x104,
        (
            "#0304F#5P哈哈，下次再来玩就好了啊。\x02\x03",

            "#0300F小滴来市里时，\x01",
            "也可以让她来我们那边玩。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B7A5")


    #C0465
    ChrTalk(
        0x20,
        "#1110F#12P嗯，这样啊。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x21,
        (
            "#1404F#5P呵呵……\x01",
            "那到时就拜托了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0xB4, 0x1F4)
    Sleep(300)

    #C0467
    ChrTalk(
        0x21,
        "#1402F#5P──滴，我要抱你上去了。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x1F,
        "#1500F#12P嗯……！\x02",
    )

    CloseMessageWindow()
    OP_68(-24710, 200, -23540, 2000)
    OP_9B(0x0, 0x1F, 0x0, 0x3E8, 0x5DC, 0x0)
    OP_6F(0x79)
    Fade(500)
    SetChrChipByIndex(0x21, 0x21)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    Sound(804, 0, 100, 0)
    OP_0D()

    def lambda_B877():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B877)
    Sleep(50)

    def lambda_B887():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_B887)
    Sleep(50)

    def lambda_B897():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_B897)
    Sleep(300)

    #C0469
    ChrTalk(
        0x101,
        (
            "#0000F#5P亚里欧斯先生今天\x01",
            "要住在这里吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0xEF, 400)
    Sleep(150)

    #C0470
    ChrTalk(
        0x21,
        "#1404F#11P是啊，准备住一晚上。\x02",
    )

    CloseMessageWindow()
    OP_93(0x21, 0xE1, 0x190)
    Sleep(300)

    #C0471
    ChrTalk(
        0x21,
        (
            "#1402F#11P──琪雅，\x01",
            "今后也请和滴好好相处。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x20,
        (
            "#1109F#6P嗯！\x02\x03",

            "#1110F滴，下次见！\x02",
        )
    )

    CloseMessageWindow()

    #N0473
    NpcTalk(
        0x21,
        "滴",
        (
            "#1502F#5P嗯……！\x01",
            "小琪雅，再见！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    OP_93(0x21, 0x0, 0x190)
    Sleep(300)
    OP_68(-24710, 200, -23040, 5000)

    def lambda_B9B3():

        label("loc_B9B3")

        TurnDirection(0x101, 0x21, 500)
        Yield()
        Jump("loc_B9B3")

    QueueWorkItem2(0x101, 1, lambda_B9B3)

    def lambda_B9C5():

        label("loc_B9C5")

        TurnDirection(0xEF, 0x21, 500)
        Yield()
        Jump("loc_B9C5")

    QueueWorkItem2(0xEF, 1, lambda_B9C5)

    def lambda_B9D7():

        label("loc_B9D7")

        TurnDirection(0x20, 0x21, 500)
        Yield()
        Jump("loc_B9D7")

    QueueWorkItem2(0x20, 1, lambda_B9D7)

    def lambda_B9E9():
        OP_95(0xFE, -23810, 0, -9390, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_B9E9)
    WaitChrThread(0x21, 1)
    ClearChrFlags(0x21, 0x8000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xEF, 0x1)
    EndChrThread(0x20, 0x1)
    OP_6F(0x1)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    Sleep(1000)
    OP_68(-25130, 200, -23360, 1000)
    MoveCamera(36, 16, 0, 1000)

    def lambda_BA4D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA4D)
    Sleep(50)

    def lambda_BA5D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_BA5D)
    OP_93(0x20, 0x0, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x79)

    #C0474
    ChrTalk(
        0x101,
        (
            "#0002F#5P那么……\x01",
            "我们也差不多该回去了吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BAEA")

    #C0475
    ChrTalk(
        0x102,
        (
            "#0102F#5P呵呵，说得也是呢，\x01",
            "不知不觉已经黄昏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB5D")

    label("loc_BAEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BB2A")

    #C0476
    ChrTalk(
        0x103,
        (
            "#0202F#5P说得也是呢……\x01",
            "不知不觉已经黄昏了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BB5D")

    label("loc_BB2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BB5D")

    #C0477
    ChrTalk(
        0x104,
        (
            "#0302F#5P是啊，\x01",
            "不知不觉已经黄昏了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BB5D")


    #C0478
    ChrTalk(
        0x20,
        (
            "#1105F#12P这么说来……\x01",
            "哇，天空好红哦！\x02\x03",

            "#1109F琪雅肚子饿了！\x02\x03",

            "#1110F今天晚饭要吃什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        (
            "#0012F#5P哈哈……\x01",
            "琪雅真的很有活力呢。\x02\x03",

            "#0000F那么，去跟塞茜尔姐打声招呼，\x01",
            "然后就坐巴士回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x20,
        "#1109F#12P嗯！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23550, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BC7C")
    RemoveParty(0x1, 0x0)
    Jump("loc_BC99")

    label("loc_BC7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BC8D")
    RemoveParty(0x2, 0x0)
    Jump("loc_BC99")

    label("loc_BC8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BC99")
    RemoveParty(0x3, 0x0)

    label("loc_BC99")

    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    StopBGM(0x1388)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x12E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 3)
    NewScene("c010B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_57_A533 end

    def Function_58_BCC1(): pass

    label("Function_58_BCC1")

    EventBegin(0x0)
    Fade(1000)
    OP_68(-35700, 900, 0, 0)
    MoveCamera(35, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    SetCameraDistance(21000, 2500)
    SetChrPos(0x101, -42200, 0, -1000, 90)
    SetChrPos(0x102, -42200, 0, 400, 90)
    SetChrPos(0x103, -43600, 0, -1000, 90)
    SetChrPos(0x104, -43600, 0, 400, 90)

    def lambda_BD48():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BD48)
    Sleep(50)

    def lambda_BD60():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BD60)
    Sleep(50)

    def lambda_BD78():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BD78)
    Sleep(50)

    def lambda_BD90():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BD90)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    ModifyEventFlags(0, 3, 0x80)
    OP_0D()
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0481
    ChrTalk(
        0x101,
        (
            "#0001F#6P那么，赶快去确认一下，\x01",
            "看看约亚西姆医生现在是否有时间吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x102,
        (
            "#0100F#5P嗯，\x01",
            "先去接待处吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        (
            "#0306F#5P但愿他不要\x01",
            "又出去钓鱼了才好。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x103,
        "#0211F#6P……很有可能呢。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -37900, 0, -300, 90)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    SetScenarioFlags(0xC3, 2)
    OP_29(0x4C, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_58_BCC1 end

    def Function_59_BEA1(): pass

    label("Function_59_BEA1")

    EventBegin(0x0)
    LoadChrToIndex("apl/ch50410.itc", 0x1E)
    Fade(1000)
    OP_68(-50560, 1300, 0, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(18250, 3000)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0xA, 0xA, 0x0, 0x0)
    OP_79(0x6)
    SetChrPos(0x101, -44720, 0, -560, 270)
    SetChrPos(0x102, -43930, 0, 910, 270)
    SetChrPos(0x103, -42520, 0, -220, 270)
    SetChrPos(0x104, -46240, 0, 700, 270)

    def lambda_BF43():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BF43)
    Sleep(50)

    def lambda_BF5B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BF5B)
    Sleep(50)

    def lambda_BF73():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_BF73)
    Sleep(50)

    def lambda_BF8B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BF8B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    ModifyEventFlags(0, 4, 0x80)
    OP_6F(0x10)
    OP_0D()
    OP_93(0x104, 0x5A, 0x1F4)

    #C0485
    ChrTalk(
        0x104,
        (
            "#0302F#6P好了，已经黄昏了。\x01",
            "快点坐巴士回去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        "#0002F#11P说得也是呢……\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x102,
        (
            "#0102F#11P呵呵，这种时候\x01",
            "就会庆幸有巴士坐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0488
    ChrTalk(
        0x103,
        "#0208F#11P#50W…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-49060, 1300, 0, 1500)

    def lambda_C0BC():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C0BC)

    def lambda_C0C9():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C0C9)
    Sleep(100)

    def lambda_C0D9():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C0D9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0489
    ChrTalk(
        0x101,
        "#0005F#6P缇欧……？\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        (
            "#0305F#6P总感觉阿缇你……\x01",
            "从刚才开始就安静得有些不对劲啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x103,
        "#0206F#11P#60W……没那回事。\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_C18A():
        OP_9B(0x0, 0xFE, 0x0, 0x352, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C18A)
    WaitChrThread(0x102, 1)

    #C0492
    ChrTalk(
        0x102,
        (
            "#0101F#5P缇欧……！？\x02\x03",

            "虽然被夕阳照得有些看不出来……\x01",
            "但你的脸色很苍白啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0493
    ChrTalk(
        0x101,
        "#0011F#6P哎！？\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x103,
        (
            "#0202F#11P#50W……没问题，\x01",
            "只是有一点不舒服而已……\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x104,
        (
            "#0306F#6P喂喂，\x01",
            "怎么会没问题啊。\x02\x03",

            "#0301F总之，先找个\x01",
            "地方休──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    #C0496
    ChrTalk(
        0x103,
        "#0206F#11P#60W……啊………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrFlags(0x103, 0x2)
    SetChrFlags(0x103, 0x10)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(910, 0, 100, 0)
    OP_0D()
    Sleep(150)
    Sound(820, 0, 100, 0)
    SetChrSubChip(0x103, 0x1)
    Sleep(150)
    SetChrSubChip(0x103, 0x2)
    Sleep(300)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0497
    ChrTalk(
        0x101,
        "#0007F#6P缇欧！？\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x102,
        "#0101F#5P不、不好了……！\x02",
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x103,
        "#11P#60W…………………………………\x02",
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x104,
        (
            "#0307F#6P我马上就去叫\x01",
            "医生或护士过来！\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x101,
        "#0007F#5P嗯……拜托了！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 60)
    Sleep(300)
    OP_68(-48210, 1300, -210, 2000)

    def lambda_C42A():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C42A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    EndChrThread(0x104, 0x3)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x2)
    ClearChrFlags(0x103, 0x10)
    OP_49()
    OP_D5(0x1E)
    Sleep(2000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x203), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x5C, 0)
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_59_BEA1 end

    def Function_60_C477(): pass

    label("Function_60_C477")

    OP_95(0xFE, -49190, 0, 2050, 5000, 0x0)
    OP_95(0xFE, -35480, 0, 180, 5000, 0x0)
    Return()

    # Function_60_C477 end

    def Function_61_C4A0(): pass

    label("Function_61_C4A0")

    OP_A1(0xFE, 0x3E8, 0x4, 0x2, 0x3, 0x4, 0x3)
    Return()

    # Function_61_C4A0 end

    def Function_62_C4AB(): pass

    label("Function_62_C4AB")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-18180, 0, -17650, 0)
    MoveCamera(352, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17500, 0)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x101, -18160, -1000, -18590, 45)
    SetChrPos(0x102, -18950, -1000, -17790, 45)
    SetChrPos(0x103, -19750, -1000, -18590, 45)
    SetChrPos(0x104, -18950, -1000, -19390, 45)
    SetChrPos(0x109, -18160, -1000, -20020, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x17, 0x2)
    FadeToBright(500, 0)
    OP_0D()

    #C0502
    ChrTalk(
        0x17,
        "#11P……最近真是心力憔悴啊。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x17,
        (
            "#11P拜托希伦护士\x01",
            "订购了医疗用品，\x01",
            "却送来了其它东西……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x17,
        (
            "#11P儿子琴兹也\x01",
            "跟以前一样，\x01",
            "没有脱离不良团伙的意思……\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x17,
        (
            "#11P做教授\x01",
            "也很辛苦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x101,
        (
            "#6P#0005F（他是这所医院的教授吗……\x01",
            "　看起来好像很疲惫呢。）\x02\x03",

            "#0003F（但是，教授的话，\x01",
            "　应该会对做礼物的材料\x01",
            "　有什么线索吧。）\x02\x03",

            "#0000F那个，不好意思。\x01",
            "有点事情想请教您……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x17,
        "#11P……噢，什么事情呢？\x02",
    )

    CloseMessageWindow()

    #A0508
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将正在收集礼物\x01",
            "材料的事情做了说明。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0509
    ChrTalk(
        0x101,
        (
            "#6P#0000F……也就是说，\x01",
            "我们正在寻找合适的材料。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x17,
        "#11P是为了滴吗……\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x17,
        (
            "#11P如果是这样的话，在那里\x01",
            "也许能找到什么。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x103,
        (
            "#6P#0200F那里……\x01",
            "您有什么头绪吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x17,
        (
            "#11P是啊……在这所医院\x01",
            "里面，闲置着大量的\x01",
            "进口杂货。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x17,
        (
            "#11P而且基本上都是\x01",
            "还没有人用过的。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x102,
        (
            "#5P#0105F进口杂货指的是……\x01",
            "为什么医院会有那种东西……？\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x17,
        (
            "#11P以前，我拜托希伦护士\x01",
            "订购外科手术用\x01",
            "的手术刀等医疗器具。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x17,
        (
            "#11P但不知为何，送来的不是医疗器具，\x01",
            "而是放在那里的一堆杂货。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x17,
        (
            "#11P为什么会出现这种情况……\x01",
            "我自己都还想搞清楚呢。\x02",
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
    Sleep(1000)

    #C0519
    ChrTalk(
        0x104,
        "#6P#0300F您看起来很辛苦呢。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x109,
        (
            "#6P#0506F该怎么说呢……经常为司令而头痛的\x01",
            "我们也感同身受呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x101,
        (
            "#6P#0000F那、那就是说……\x01",
            "我们可以从那里拿点什么吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x17,
        (
            "#11P嗯，没问题。\x01",
            "说实话，我正在烦恼要怎么处理那堆杂物呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x17,
        (
            "#11P装有杂货的集装箱\x01",
            "就放置在宿舍二层的露台，\x01",
            "穿过男职员宿舍就能找到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x17,
        (
            "#11P要是发现了\x01",
            "什么合适的东西，\x01",
            "就随便拿走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#6P#0000F好，谢谢您了。\x02\x03",

            "#0003F（二楼露台是指……\x01",
            "　狼形魔兽事件中，\x01",
            "　安装了防护栏的地方吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18160, -1000, -18590, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -23040, -1000, -25910, 0)
    BeginChrThread(0x9, 0, 0, 1)
    OP_29(0x2C, 0x1, 0x3)
    EventEnd(0x5)
    Return()

    # Function_62_C4AB end

    def Function_63_CBB3(): pass

    label("Function_63_CBB3")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-36870, 4000, 16950, 0)
    MoveCamera(35, 29, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23790, 0)
    SetChrPos(0x101, -36910, 3000, 16290, 90)
    SetChrPos(0x102, -38300, 3000, 16300, 90)
    SetChrPos(0x103, -38300, 3000, 17300, 90)
    SetChrPos(0x104, -37000, 3000, 17300, 90)
    SetChrPos(0x109, -37000, 3000, 18600, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrSubChip(0x17, 0x2)
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0526
    ChrTalk(
        0x101,
        (
            "#6P#0000F这个好像就是\x01",
            "教授所说的集装箱了。\x02\x03",

            "那么，\x01",
            "稍微找一找吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()

    #C0527
    ChrTalk(
        0x109,
        (
            "#5P#0505F怎么样？\x01",
            "有什么可以用的东西吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)

    #C0528
    ChrTalk(
        0x101,
        "#12P#0000F嗯，找到了这样的东西。\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x102,
        (
            "#6P#0105F啊……皮绳吗？\x02\x03",

            "#0100F似乎编得\x01",
            "很结实呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x103,
        (
            "#6P#0200F……还有其它\x01",
            "可用的东西吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x101,
        (
            "#12P#0006F呃，那个，\x01",
            "翻过一遍后……\x02\x03",

            "虽然不知道原因，\x01",
            "但尽是一些奇怪的装饰品，\x01",
            "还有辟邪的人偶。\x02\x03",

            "#0000F看样子，\x01",
            "除了这根皮绳之外，\x01",
            "就找不到其它的有用之物了。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x104,
        (
            "#11P#0306F算啦，那个医生不是也\x01",
            "正在头痛要怎么处理这些东西吗。\x02\x03",

            "#0300F即使只找到一件看起来可以用的\x01",
            "东西，也算很幸运了吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0533
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '选秀活动特别奖纪念盾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('选秀活动特别奖纪念盾', 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF83")

    #C0534
    ChrTalk(
        0x101,
        (
            "#12P#0003F（如果是这么结实的绳子，\x01",
            "　即使是亚里欧斯先生用\x01",
            "　应该也不会断吧……）\x02\x03",

            "（之后再找个\x01",
            "　可以镶嵌小滴那块石头的\x01",
            "　挂坠扣就好了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CF83")

    OP_29(0x2C, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D026")
    OP_29(0x2C, 0x1, 0x5)

    #C0535
    ChrTalk(
        0x101,
        (
            "#12P#0000F（制作礼物的材料收集齐了，\x01",
            "　包装用的盒子与缎带也找到了……）\x02\x03",

            "（好了，差不多该拿去给\x01",
            "　小滴了。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D026")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -37600, 3000, 16800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x8, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_63_CBB3 end

    def Function_64_D056(): pass

    label("Function_64_D056")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D16E")

    #C0536
    ChrTalk(
        0x101,
        (
            "#0001F这里是通往郊外的方向……\x02\x03",

            "#0003F怎么说也不能把塞茜尔姐姐\x01",
            "带到那种地方去。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D118")

    #C0537
    ChrTalk(
        0x136,
        (
            "#1300F呵呵，是要进行\x01",
            "魔兽骚乱的调查吧。\x02\x03",

            "跟我来，\x01",
            "我带你们去病房楼二楼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D16E")

    label("loc_D118")


    #C0538
    ChrTalk(
        0x136,
        (
            "#1300F呵呵，是要进行\x01",
            "魔兽骚乱的调查吧。\x02\x03",

            "事发现场在病房楼的楼顶，\x01",
            "我带你们去吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D16E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1C7")

    #C0539
    ChrTalk(
        0x101,
        (
            "#0000F这边是郊外的方向……\x02\x03",

            "#0003F回去之前\x01",
            "必须向塞茜尔姐姐报告一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D1C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D23B")

    #C0540
    ChrTalk(
        0x101,
        (
            "#0000F已经黄昏了，\x01",
            "回去的时候乘坐巴士吧。\x02\x03",

            "只要调查巴士站，\x01",
            "应该就能知道下一班巴士的抵达时间了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D23B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D2B4")

    #C0541
    ChrTalk(
        0x101,
        (
            "#0000F对了……\x01",
            "好不容易来了一次，\x01",
            "得去医院找医生商量一下呢。\x02\x03",

            "到接待处去询问下有关\x01",
            "『神经科』的事吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D2B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D31E")

    #C0542
    ChrTalk(
        0x101,
        (
            "#0003F不能带着琪雅\x01",
            "去市外啊……\x02\x03",

            "#0000F而且还必须向约亚西姆医生\x01",
            "询问有关琪雅记忆的事。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D31E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D3C5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D386")

    #C0543
    ChrTalk(
        0x101,
        (
            "#0003F……琪雅大概\x01",
            "还在医院用地的范围内。\x02\x03",

            "#0001F必须快一点找到她呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D3C5")

    label("loc_D386")


    #C0544
    ChrTalk(
        0x101,
        (
            "#0001F快一点把琪雅找出来吧。\x01",
            "她应该还在医院用地的范围内。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D3C5")

    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_64_D056 end

    def Function_65_D3DC(): pass

    label("Function_65_D3DC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0545
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
    TalkEnd(0xFF)
    Return()

    # Function_65_D3DC end

    def Function_66_D42F(): pass

    label("Function_66_D42F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0546
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
    TalkEnd(0xFF)
    Return()

    # Function_66_D42F end

    SaveToFile()

Try(main)
