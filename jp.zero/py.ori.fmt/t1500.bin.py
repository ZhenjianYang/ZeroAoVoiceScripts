from ZeroScenarioHelper import *

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
        0x04,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 77, 0, 4, 0, 5],
    )

    BuildStringList((
        "t1500",                  # 0
        "警備員トニー",           # 1
        "看護師エイダ",           # 2
        "ダイソン用務員",         # 3
        "ミハイル",               # 4
        "入院患者",               # 5
        "女の子",                 # 6
        "見舞い客",               # 7
        "見舞い客",               # 8
        "ハロルド",               # 9
        "ジェド",                 # 10
        "キーンツ",               # 11
        "ケイト巡査",             # 12
        "ペーター",               # 13
        "特級釣師ロイド",         # 14
        "マリアベル",             # 15
        "ゲイリー教授",           # 16
        "ヨアヒム准教授",         # 17
        "観光客オシール",         # 18
        "観光客ラピス",           # 19
        "看護師シロン",           # 20
        "バス",                   # 21
        "バス２",                 # 22
        "セシル",                 # 23
        "シズク",                 # 24
        "キーア",                 # 25
        "アリオス",               # 26
        "事務長ロバート",         # 27
        "マーサ師長",             # 28
        "職員",                   # 29
        "バス乗客",               # 30
        "バス乗客",               # 31
        "バス乗客",               # 32
        "バス乗客",               # 33
        "バス乗客",               # 34
        "ウルスラ間道",           # 35
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

    PlaceName(-69.0, 0.0, -8.0, 0x0000, 0x0000, "ウルスラ間道")
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
        "Function_7_201C",         # 07, 7
        "Function_8_2F3B",         # 08, 8
        "Function_9_33D5",         # 09, 9
        "Function_10_35E2",        # 0A, 10
        "Function_11_39A1",        # 0B, 11
        "Function_12_3B4F",        # 0C, 12
        "Function_13_3C13",        # 0D, 13
        "Function_14_3C9D",        # 0E, 14
        "Function_15_3E8D",        # 0F, 15
        "Function_16_3F60",        # 10, 16
        "Function_17_400B",        # 11, 17
        "Function_18_42CB",        # 12, 18
        "Function_19_4350",        # 13, 19
        "Function_20_4480",        # 14, 20
        "Function_21_49C1",        # 15, 21
        "Function_22_4D20",        # 16, 22
        "Function_23_4E80",        # 17, 23
        "Function_24_509B",        # 18, 24
        "Function_25_51F2",        # 19, 25
        "Function_26_52B1",        # 1A, 26
        "Function_27_53CA",        # 1B, 27
        "Function_28_545F",        # 1C, 28
        "Function_29_5A11",        # 1D, 29
        "Function_30_5B00",        # 1E, 30
        "Function_31_5B0E",        # 1F, 31
        "Function_32_5BE2",        # 20, 32
        "Function_33_5D5D",        # 21, 33
        "Function_34_5D61",        # 22, 34
        "Function_35_5DD8",        # 23, 35
        "Function_36_5E55",        # 24, 36
        "Function_37_666F",        # 25, 37
        "Function_38_6DD3",        # 26, 38
        "Function_39_6E9E",        # 27, 39
        "Function_40_6F76",        # 28, 40
        "Function_41_7006",        # 29, 41
        "Function_42_707F",        # 2A, 42
        "Function_43_72F9",        # 2B, 43
        "Function_44_74ED",        # 2C, 44
        "Function_45_861B",        # 2D, 45
        "Function_46_86AD",        # 2E, 46
        "Function_47_871A",        # 2F, 47
        "Function_48_8D83",        # 30, 48
        "Function_49_978B",        # 31, 49
        "Function_50_982A",        # 32, 50
        "Function_51_98BC",        # 33, 51
        "Function_52_994E",        # 34, 52
        "Function_53_99E0",        # 35, 53
        "Function_54_9A35",        # 36, 54
        "Function_55_9A4E",        # 37, 55
        "Function_56_A7AD",        # 38, 56
        "Function_57_B3B2",        # 39, 57
        "Function_58_CDD6",        # 3A, 58
        "Function_59_CFD2",        # 3B, 59
        "Function_60_D5EC",        # 3C, 60
        "Function_61_D615",        # 3D, 61
        "Function_62_D620",        # 3E, 62
        "Function_63_DE2C",        # 3F, 63
        "Function_64_E37D",        # 40, 64
        "Function_65_E73D",        # 41, 65
        "Function_66_E790",        # 42, 66
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1273")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120D")

    #C0001
    ChrTalk(
        0xFE,
        "や、聖ウルスラ病院へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "そういえばそっちの青髪の君……\x01",
            "もう具合はいいのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0x103,
        (
            "#0205Fああ、はい……\x01",
            "おかげさまで。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "そっか、まぁ大事にならなくて\x01",
            "なによりだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_126E")

    label("loc_120D")


    #C0005
    ChrTalk(
        0xFE,
        (
            "昨日はそっちの青髪の子が\x01",
            "急に倒れてビックリしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        "でもまぁ、元気そうでなによりだよ。\x02",
    )

    CloseMessageWindow()

    label("loc_126E")

    Jump("loc_2018")

    label("loc_1273")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_12E9")
    TurnDirection(0xFE, 0x9, 0)

    #C0007
    ChrTalk(
        0xFE,
        (
            "僕も実を言うと、ちょっと前の\x01",
            "狼の事件から勤務時間が延びちゃってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "お互い大変だねぇ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2018")

    label("loc_12E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1378")

    #C0009
    ChrTalk(
        0xFE,
        (
            "朝早くから\x01",
            "ドスの利いた感じの連中が\x01",
            "次々に運び込まれて来てたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "や～……驚いたよ。\x01",
            "クロスベル市で何かあったのかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2018")

    label("loc_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_13DD")

    #C0011
    ChrTalk(
        0xFE,
        "や、聖ウルスラ病院へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "今日はあの可愛い子は\x01",
            "連れてこなかったのかい？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2018")

    label("loc_13DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_1446")

    #C0013
    ChrTalk(
        0xFE,
        "緑色の髪の女の子……？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "病院の外では見ていないね。\x01",
            "まだ敷地内に居るんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2018")

    label("loc_1446")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_1560")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1500")

    #C0015
    ChrTalk(
        0xFE,
        "や、ウルスラ医科大学病院へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x153,
        "#1109Fや、こんにちはー！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        "はは、元気いいねー。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "分かってるとは思うけど\x01",
            "受付は病棟のほうでお願いするよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_155B")

    label("loc_1500")


    #C0019
    ChrTalk(
        0xFE,
        (
            "今バスが出たばかりだから\x01",
            "しばらくは帰ってこないと思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        "受付は病棟のほうでね。\x02",
    )

    CloseMessageWindow()

    label("loc_155B")

    Jump("loc_2018")

    label("loc_1560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_16D4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1631")

    #C0021
    ChrTalk(
        0xFE,
        (
            "さっき、ヨアヒム先生が\x01",
            "街道に釣りにいこうとしててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "危ないから止めようと思ったら、\x01",
            "これで黙っといてくれって\x01",
            "１ミラくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "……なんていうか\x01",
            "割とケチな人だよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_16CF")

    label("loc_1631")


    #C0024
    ChrTalk(
        0xFE,
        (
            "ヨアヒム先生がこっそり\x01",
            "釣りに行こうとしててね。\x01",
            "口止め料に１ミラくれたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "……ま、結局その後\x01",
            "看護師と研修医たちに\x01",
            "連れ戻されちゃったんだけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16CF")

    Jump("loc_2018")

    label("loc_16D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1766")

    #C0026
    ChrTalk(
        0xFE,
        "や、聖ウルスラ病院へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "君たち、ケガなんてしてないだろうね？\x01",
            "折角の記念祭なんだから\x01",
            "ハメをはずしすぎないようにな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2018")

    label("loc_1766")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_18B1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1823")

    #C0028
    ChrTalk(
        0xFE,
        "や、聖ウルスラ病院へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "……そこに駐車してる車、すごいよね。\x01",
            "リムジンって言うんだっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "うーん、さすがお金持ちの人は\x01",
            "車からしてちがうねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_18AC")

    label("loc_1823")


    #C0031
    ChrTalk(
        0xFE,
        (
            "見てよ、そこのリムジン。\x01",
            "最新型だからきっとかなりの値段が\x01",
            "するんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "うーん、さすがお金持ちの人は\x01",
            "車からしてちがうねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18AC")

    Jump("loc_2018")

    label("loc_18B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1925")

    #C0033
    ChrTalk(
        0xFE,
        "や、聖ウルスラ病院へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "今、クロスベル市では\x01",
            "記念祭をやってるねぇ。\x01",
            "盛り上がってる？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2018")

    label("loc_1925")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_19B2")

    #C0035
    ChrTalk(
        0xFE,
        "や、聖ウルスラ病院へようこそ。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "世間はアルカンシェルの話題で\x01",
            "持ちきりみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        "僕も出来れば行ってみたいなぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2018")

    label("loc_19B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1B4C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABE")

    #C0038
    ChrTalk(
        0xFE,
        (
            "この病院には専用の車両\x01",
            "“救急車”が配備されてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "急患で定期バスの時間が合わなくても、\x01",
            "導力通信一本でクロスベルのどこにでも\x01",
            "飛んでいくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "少し前に重傷を負った\x01",
            "街の不良が助かったのも\x01",
            "救急車による迅速な対応のおかげなのさ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B47")

    label("loc_1ABE")


    #C0041
    ChrTalk(
        0xFE,
        (
            "救急車は急患とあらば、\x01",
            "導力通信一本でクロスベルのどこにでも\x01",
            "飛んでいくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "馬力も並の導力車なら\x01",
            "余裕で追い抜くくらいなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B47")

    Jump("loc_2018")

    label("loc_1B4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_1C6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C03")

    #C0043
    ChrTalk(
        0xFE,
        "ん……もう帰るのかい？\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        (
            "クロスベル市に戻るなら、\x01",
            "そこのバス停で待ってるといいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "今日のバスはまだまだあるから\x01",
            "慌てることはないと思うけどね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C68")

    label("loc_1C03")


    #C0046
    ChrTalk(
        0xFE,
        (
            "クロスベル市に戻るなら、\x01",
            "そこのバス停で待ってるといいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "やーしかし、夕日が綺麗だねぇ……\x02",
    )

    CloseMessageWindow()

    label("loc_1C68")

    Jump("loc_2018")

    label("loc_1C6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_1DB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D55")

    #C0048
    ChrTalk(
        0xFE,
        (
            "リットン君が襲われた夜は、\x01",
            "迷惑な商人が来ててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "やけに高い値段で\x01",
            "シーツやらを売りつけてくるから\x01",
            "その対応を頼まれてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        (
            "というわけで\x01",
            "丁度ここにはいなかったんだ。\x01",
            "力になれずすまないね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1DB4")

    label("loc_1D55")


    #C0051
    ChrTalk(
        0xFE,
        (
            "んー、あの夜は丁度、\x01",
            "ここにはいなかったんだよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        "悪いけど、気づけたことはないなぁ。\x02",
    )

    CloseMessageWindow()

    label("loc_1DB4")

    Jump("loc_2018")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_1F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F54")

    #C0053
    ChrTalk(
        0xFE,
        (
            "さっき連絡があったんだけど、\x01",
            "街道の方で定期バスが\x01",
            "魔獣に襲われたらしいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "でも、颯爽と現れた二人組の遊撃士が\x01",
            "アッという間に片付けたんだと。\x01",
            "すごいよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        (
            "#0306F連絡されてないところを見ると……\x01",
            "どうやら俺たちのことは\x01",
            "全く印象に残ってないみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0011Fま、まぁ……\x01",
            "エステルとヨシュアが\x01",
            "めちゃくちゃ凄かったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x136,
        "#1300Fふふ、あなた達もがんばらないとね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1F8B")

    label("loc_1F54")


    #C0058
    ChrTalk(
        0xFE,
        (
            "や～、やっぱ遊撃士はすごいよね。\x01",
            "要チェックだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8B")

    Jump("loc_2018")

    label("loc_1F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2018")

    #C0059
    ChrTalk(
        0xFE,
        (
            "や、こんにちは。\x01",
            "ここは聖ウルスラ医科大学病院……\x01",
            "略してウルスラ病院だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "外来の方かな？\x01",
            "門を入って奥の建物にどうぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2018")

    TalkEnd(0xFE)
    Return()

    # Function_6_1136 end

    def Function_7_201C(): pass

    label("Function_7_201C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2090")

    #C0061
    ChrTalk(
        0xFE,
        "朝の散歩は健康にいいのよね。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "私も患者さんと一緒に散歩して\x01",
            "健康になれるから一石二鳥だわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F37")

    label("loc_2090")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_20FA")

    #C0063
    ChrTalk(
        0xFE,
        "今日の当直は私なのよね……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "看護師は忙しいわ。\x01",
            "体を壊さないように\x01",
            "気を付けないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F37")

    label("loc_20FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2150")

    #C0065
    ChrTalk(
        0xFE,
        (
            "さっきの患者さん、\x01",
            "ＩＣＵの方に運ばれていったけど\x01",
            "大丈夫かしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F37")

    label("loc_2150")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21D2")

    #C0066
    ChrTalk(
        0xFE,
        (
            "患者さんとの人付き合いもあるから\x01",
            "なにかと気苦労が絶えないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "しゃっきりと\x01",
            "リフレッシュしておかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F37")

    label("loc_21D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_2245")

    #C0068
    ChrTalk(
        0xFE,
        (
            "あら、弟くん……\x01",
            "可愛い子を連れてるじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "ふふ……\x01",
            "迷子にしないように\x01",
            "気を付けるのよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F37")

    label("loc_2245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22F1")

    #C0070
    ChrTalk(
        0xFE,
        "今日で記念祭は終わりね。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "ロイド君たちも仕事で\x01",
            "忙しかったと思うけど、\x01",
            "それも今日まで。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "あと一息だから\x01",
            "お互い精一杯がんばりましょ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2364")

    label("loc_22F1")


    #C0073
    ChrTalk(
        0xFE,
        (
            "今日で記念祭も終わり……\x01",
            "休みは殆ど取れなかったけど、\x01",
            "それもあと少し。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "今日一日は\x01",
            "精一杯がんばりましょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2364")

    Jump("loc_2F37")

    label("loc_2369")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2400")

    #C0075
    ChrTalk(
        0xFE,
        (
            "ミハイル君、今日は調子良いから\x01",
            "外出許可をもらったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        (
            "敷地内だけ、だけどね。\x01",
            "普段ベッドの上だから\x01",
            "良い気分転換になるわよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F37")

    label("loc_2400")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2516")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24BB")

    #C0077
    ChrTalk(
        0xFE,
        (
            "入院患者さんから\x01",
            "記念祭の間だけ外出許可が欲しい\x01",
            "って人が結構いるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "病状もまちまちだし、\x01",
            "一度先生に確認をとらないと\x01",
            "どうして良いか分からないのよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2511")

    label("loc_24BB")


    #C0079
    ChrTalk(
        0xFE,
        (
            "折角の記念祭だから\x01",
            "遊びに行きたいのはわかるけど……\x01",
            "私に言われても困っちゃうわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2511")

    Jump("loc_2F37")

    label("loc_2516")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2855")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2813")

    #C0080
    ChrTalk(
        0xFE,
        "あら、こんにちは。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 1)), scpexpr(EXPR_END)), "loc_2696")

    #C0081
    ChrTalk(
        0xFE,
        (
            "ふふ、ランディさん。\x01",
            "昨日はライブ楽しかったわ。\x01",
            "誘ってくれてありがとう。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "フィリアもランも\x01",
            "随分楽しんでたみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0304Fフッ、レディを楽しませるのは\x01",
            "男の使命だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#0006F看護師さん３人とデートなんて、\x01",
            "ランディって相当なツワモノだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        "#0105Fほんとよね……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#0211Fというか、お盛んすぎです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_280B")

    label("loc_2696")


    #C0087
    ChrTalk(
        0xFE,
        (
            "ランディさん、ロイド君。\x01",
            "昨日はライブ楽しかったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "フィリアもランも\x01",
            "随分楽しんでたみたいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x104,
        (
            "#0304Fフッ、レディを楽しませるのは\x01",
            "男の使命だからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x101,
        (
            "#0000Fえっと……\x01",
            "こっちこそ誘ってくれて\x01",
            "ありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x102,
        (
            "#0105Fていうかあなた達……\x01",
            "看護師さんと２対３で\x01",
            "デートしてたのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#0211Fお盛んですね。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x101,
        "#0006F（そんな目で見ないでくれ……）\x02",
    )

    CloseMessageWindow()

    label("loc_280B")

    SetScenarioFlags(0x0, 1)
    Jump("loc_2850")

    label("loc_2813")


    #C0094
    ChrTalk(
        0xFE,
        (
            "昨日は楽しめたし……\x01",
            "ふふ、今日も一日がんばれそうだわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2850")

    Jump("loc_2F37")

    label("loc_2855")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_29AC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2963")

    #C0095
    ChrTalk(
        0xFE,
        "そういえば、来月は記念祭ね。\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "フィリアから誘われてるけど……\x01",
            "休みがとれるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x104,
        (
            "#0309Fハハ、楽しみにしてるから\x01",
            "がんばってくれよな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x104, 500)

    #C0098
    ChrTalk(
        0xFE,
        "うーん……まぁ、がんばってみるわね。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x101,
        "#0000F（ランディが誘ったみたいだな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_29A7")

    label("loc_2963")


    #C0100
    ChrTalk(
        0xFE,
        "記念祭、休みがとれるかしら。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0xFE,
        "まぁ、がんばるしかないかな。\x02",
    )

    CloseMessageWindow()

    label("loc_29A7")

    Jump("loc_2F37")

    label("loc_29AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2A88")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A4E")

    #C0102
    ChrTalk(
        0xFE,
        (
            "あら、セシル先輩の弟君じゃない。\x01",
            "元気にしてたかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#0006Fな、なんだかすっかり\x01",
            "看護師さんの間で\x01",
            "有名人になっちゃったな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2A83")

    label("loc_2A4E")


    #C0104
    ChrTalk(
        0xFE,
        (
            "セシル先輩の弟君じゃない。\x01",
            "元気にしてたかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A83")

    Jump("loc_2F37")

    label("loc_2A88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_2B05")

    #C0105
    ChrTalk(
        0xFE,
        (
            "夕日に染まるエルム湖って綺麗よね。\x01",
            "なんだか心が癒されるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        "……さぁて、今日の宿直もがんばらないと！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F37")

    label("loc_2B05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_2C0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BCE")
    TurnDirection(0xFE, 0xC, 0)

    #C0107
    ChrTalk(
        0xFE,
        (
            "さ、おじいちゃん。\x01",
            "もうそろそろ日が落ちるし……\x01",
            "病室にもどりましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xC,
        "ほっほっほ、そうじゃな。\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xC,
        (
            "せっかく退院も近いらしいし\x01",
            "無理はしないようにせんとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2C07")

    label("loc_2BCE")


    #C0110
    ChrTalk(
        0xFE,
        (
            "さ、そろそろおじいちゃんを連れて\x01",
            "病室に戻りましょ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C07")

    Jump("loc_2F37")

    label("loc_2C0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_2DCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D23")

    #C0111
    ChrTalk(
        0xFE,
        (
            "あ、セシル先輩。\x01",
            "……そちらの方達は？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x136,
        (
            "#1300F弟のロイドと、\x01",
            "その恋人さんたちよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        "え、えぇっ！？\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        (
            "#0011Fちょ、ちょっとセシル姉！\x01",
            "冗談が過ぎるって。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x136,
        (
            "#1309Fふふ、ちょっと\x01",
            "ふざけてみたかっただけよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        "な、なーんだびっくりした……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2DC7")

    label("loc_2D23")


    #C0117
    ChrTalk(
        0xFE,
        (
            "ロイドさんのことは\x01",
            "セシル先輩から聞かされて\x01",
            "知ってたんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "セシル先輩は言っていることが\x01",
            "本当なのか冗談なのか……\x01",
            "たまに分からなくなっちゃいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC7")

    Jump("loc_2F37")

    label("loc_2DCC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_2F37")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F00")

    #C0119
    ChrTalk(
        0xFE,
        (
            "あら、こんにちは。\x01",
            "お見舞いの方かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x104,
        (
            "#0305Fほっほう、いいねぇいいねぇ！\x02\x03",

            "#0309Fうーん、本物の白衣の天使は\x01",
            "やっぱり違うな！\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#0205F……本物の？\x01",
            "それは一体どういう……\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x102,
        "#0104Fはいはい、スルーしましょうね。\x02",
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "あ、あのう……？\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        "#0006F……なんかすみません。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F37")

    label("loc_2F00")


    #C0125
    ChrTalk(
        0xFE,
        (
            "ふふ、とても元気そうね。\x01",
            "お友達にお見舞いかしら？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F37")

    TalkEnd(0xFE)
    Return()

    # Function_7_201C end

    def Function_8_2F3B(): pass

    label("Function_8_2F3B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2FDD")

    #C0126
    ChrTalk(
        0xFE,
        (
            "たまに用務員の仕事なんて\x01",
            "小さいなんて言われてしまうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "やることは多いし、\x01",
            "なによりやりがいがある。\x01",
            "私はこの仕事は気に入っているよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_2FDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_2FEB")
    Jump("loc_33D1")

    label("loc_2FEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2FF9")
    Jump("loc_33D1")

    label("loc_2FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3073")

    #C0128
    ChrTalk(
        0xFE,
        (
            "ゲイリー教授がベンチで\x01",
            "ため息ばかりついてるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xFE,
        (
            "うーん、偉い先生にも\x01",
            "色々と悩みがあるんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_3073")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_3081")
    Jump("loc_33D1")

    label("loc_3081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_308F")
    Jump("loc_33D1")

    label("loc_308F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_309D")
    Jump("loc_33D1")

    label("loc_309D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_30DC")

    #C0130
    ChrTalk(
        0xFE,
        (
            "花が枯れないように\x01",
            "しっかり手入れせんとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_30DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_30EA")
    Jump("loc_33D1")

    label("loc_30EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3181")

    #C0131
    ChrTalk(
        0xFE,
        (
            "エルム湖の眺めのおかげか、\x01",
            "とても心が安らぐね。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        (
            "記念祭中も遠出できない\x01",
            "入院患者さんにとって、\x01",
            "ここはオアシスみたいなもんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_3181")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3210")

    #C0133
    ChrTalk(
        0xFE,
        (
            "緑色には人の心を\x01",
            "安らげる効果があるという。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "患者に少しでも\x01",
            "安心してもらえるように、\x01",
            "病院には沢山の植物を置いてるのさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_3210")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_321E")
    Jump("loc_33D1")

    label("loc_321E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3289")

    #C0135
    ChrTalk(
        0xFE,
        (
            "フェンスを取り付けたら\x01",
            "随分立派になったじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        "私も魔獣には気をつけないとな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_3289")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3309")

    #C0137
    ChrTalk(
        0xFE,
        (
            "屋上の調査は終わったのか……\x01",
            "なにか分かったかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xFE,
        (
            "おっと、屋上が空いたなら\x01",
            "清掃に取り掛かるとするかね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_3309")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3383")

    #C0139
    ChrTalk(
        0xFE,
        (
            "病院で働きだして長いけど、\x01",
            "ここまで立派な建物は\x01",
            "見たことないよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0xFE,
        "さーて、きちんと整備しないと……\x02",
    )

    CloseMessageWindow()
    Jump("loc_33D1")

    label("loc_3383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_33D1")

    #C0141
    ChrTalk(
        0xFE,
        "ん、どした迷子か？\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xFE,
        (
            "病棟なら奥に見えてる\x01",
            "でっかい建物だぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33D1")

    TalkEnd(0xFE)
    Return()

    # Function_8_2F3B end

    def Function_9_33D5(): pass

    label("Function_9_33D5")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3469")
    Jump("loc_34B3")

    label("loc_3469")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3489")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34B3")

    label("loc_3489")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34A9")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_34B3")

    label("loc_34A9")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_34B3")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_357B")

    #C0143
    ChrTalk(
        0xFE,
        (
            "昨日、ＩＢＣの人から\x01",
            "クマのぬいぐるみをもらったんだ。\x01",
            "えへへ……うれしかったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xFE,
        (
            "ディーターさんって\x01",
            "本当にやさしいおじさんなんだね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_35DA")

    label("loc_357B")


    #C0145
    ChrTalk(
        0xFE,
        "うーん、空気が美味しくていい気持ち。\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "今度はまた、シズクちゃんと\x01",
            "お散歩に来ようっと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35DA")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_9_33D5 end

    def Function_10_35E2(): pass

    label("Function_10_35E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_35F3")
    Jump("loc_399D")

    label("loc_35F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_3601")
    Jump("loc_399D")

    label("loc_3601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_360F")
    Jump("loc_399D")

    label("loc_360F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_361D")
    Jump("loc_399D")

    label("loc_361D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_362B")
    Jump("loc_399D")

    label("loc_362B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_3639")
    Jump("loc_399D")

    label("loc_3639")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3647")
    Jump("loc_399D")

    label("loc_3647")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3655")
    Jump("loc_399D")

    label("loc_3655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3663")
    Jump("loc_399D")

    label("loc_3663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3671")
    Jump("loc_399D")

    label("loc_3671")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_367F")
    Jump("loc_399D")

    label("loc_367F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_368D")
    Jump("loc_399D")

    label("loc_368D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_369B")
    Jump("loc_399D")

    label("loc_369B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_371A")

    #C0147
    ChrTalk(
        0xFE,
        (
            "ほほ、そうじゃな。\x01",
            "戻るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "折角退院も近いんじゃ、\x01",
            "無理をして体を壊しては\x01",
            "元も子もないからの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_399D")

    label("loc_371A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_38A7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_386D")

    #C0149
    ChrTalk(
        0x136,
        (
            "#1300Fおじいちゃん\x01",
            "その後、ヒザの調子はどう？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "ほほ、もうあの痛みがウソみたいじゃよ。\x01",
            "ここで治療してもらってよかったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x136,
        (
            "#1300Fふふ、よかった。\x02\x03",

            "ベルダイン先生も\x01",
            "もうすぐ退院できるって言ってたし\x01",
            "もう少しがんばりましょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        (
            "#0004F（セシル姉……\x01",
            "  やっぱり看護師の仕事は\x01",
            "  板についてるな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_38A2")

    label("loc_386D")


    #C0153
    ChrTalk(
        0xFE,
        (
            "もうすぐ退院か……\x01",
            "ほっほっほ、嬉しいことじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38A2")

    Jump("loc_399D")

    label("loc_38A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_399D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_394B")

    #C0154
    ChrTalk(
        0xFE,
        (
            "わしゃ、風呂場で転んで\x01",
            "ヒザを痛めてしもうての。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xFE,
        (
            "ここの先生に診てもらったおかげで\x01",
            "こうして外を出歩けるまでに\x01",
            "良くなったんじゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_399D")

    label("loc_394B")


    #C0156
    ChrTalk(
        0xFE,
        (
            "しかし、こんなに早く\x01",
            "歩けるようになるとは……\x01",
            "ここの先生方はウデがいいのう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_399D")

    TalkEnd(0xFE)
    Return()

    # Function_10_35E2 end

    def Function_11_39A1(): pass

    label("Function_11_39A1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_39B2")
    Jump("loc_3B4B")

    label("loc_39B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 5)), scpexpr(EXPR_END)), "loc_39C0")
    Jump("loc_3B4B")

    label("loc_39C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_39CE")
    Jump("loc_3B4B")

    label("loc_39CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_39DC")
    Jump("loc_3B4B")

    label("loc_39DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_END)), "loc_39EA")
    Jump("loc_3B4B")

    label("loc_39EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_END)), "loc_39F8")
    Jump("loc_3B4B")

    label("loc_39F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A06")
    Jump("loc_3B4B")

    label("loc_3A06")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A14")
    Jump("loc_3B4B")

    label("loc_3A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3A22")
    Jump("loc_3B4B")

    label("loc_3A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3A30")
    Jump("loc_3B4B")

    label("loc_3A30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3A3E")
    Jump("loc_3B4B")

    label("loc_3A3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3A4C")
    Jump("loc_3B4B")

    label("loc_3A4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_END)), "loc_3AD8")

    #C0157
    ChrTalk(
        0xFE,
        (
            "おばあちゃん、元気そうでよかった。\x01",
            "それに、もうすぐ退院だって！\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        (
            "退院したら、パパとママも連れて\x01",
            "皆で迎えに来るんだ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3B4B")

    label("loc_3AD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_3AE6")
    Jump("loc_3B4B")

    label("loc_3AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_END)), "loc_3AF4")
    Jump("loc_3B4B")

    label("loc_3AF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3B4B")

    #C0159
    ChrTalk(
        0xFE,
        (
            "んー……\x01",
            "おっきい病院だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        (
            "おばあちゃん、\x01",
            "元気にしてるといいな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3B4B")

    TalkEnd(0xFE)
    Return()

    # Function_11_39A1 end

    def Function_12_3B4F(): pass

    label("Function_12_3B4F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BCA")

    #C0161
    ChrTalk(
        0xFE,
        (
            "ケガして入院してる\x01",
            "友達の見舞いに来たんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0xFE,
        (
            "さーて、あいつの病室は\x01",
            "どこにあるのかなっと……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_3C0F")

    label("loc_3BCA")


    #C0163
    ChrTalk(
        0xFE,
        (
            "友達の病室は……どこだっけ？\x01",
            "……ま、適当に歩いてりゃ着くかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C0F")

    TalkEnd(0xFE)
    Return()

    # Function_12_3B4F end

    def Function_13_3C13(): pass

    label("Function_13_3C13")

    TalkBegin(0xFE)

    #C0164
    ChrTalk(
        0xFE,
        (
            "今日はボーイフレンドの\x01",
            "お見舞いに来たの。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "彼、変にツッパってるからなぁ。\x01",
            "他の患者さんに嫌な思いを\x01",
            "させてなきゃいいけど。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_3C13 end

    def Function_14_3C9D(): pass

    label("Function_14_3C9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x8D, 6)), scpexpr(EXPR_END)), "loc_3D12")

    #C0166
    ChrTalk(
        0x10,
        (
            "#3600Fさて、備品を\x01",
            "運び出してしまわないと……\x02\x03",

            "ははは、皆さんの方も\x01",
            "お仕事頑張ってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E89")

    label("loc_3D12")


    #C0167
    ChrTalk(
        0x101,
        "#0005Fあれ、ハロルドさん……？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x10,
        (
            "#3600Fやあ皆さん……お久し振りですね。\x01",
            "こんな所でお会いするとは。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x101,
        (
            "#0000Fはは……例の一件以来\x01",
            "市外の仕事も増えまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x103,
        "#0200Fハロルドさんもお仕事ですか？\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x10,
        (
            "#3600Fええ、ウルスラ病院に\x01",
            "備品や日用品を卸しに来たんです。\x02\x03",

            "やはり導力車を買ってよかった。\x01",
            "行き来がぐんと楽になりましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        "#0100Fお仕事も順調みたいですね。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x8D, 6)

    label("loc_3E89")

    TalkEnd(0xFE)
    Return()

    # Function_14_3C9D end

    def Function_15_3E8D(): pass

    label("Function_15_3E8D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_3EED")

    #C0173
    ChrTalk(
        0x11,
        (
            "……だが……ディーノのヤツ\x01",
            "いつの間にあんな力を……\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x11,
        "チッ、クソが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3F5C")

    label("loc_3EED")


    #C0175
    ChrTalk(
        0x11,
        (
            "クソが……幹部である俺に\x01",
            "舐めた真似しやがる。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x11,
        (
            "ディーノめ、帰ったら\x01",
            "たっぷりお仕置きしてやんぜ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_3F5C")

    TalkEnd(0xFE)
    Return()

    # Function_15_3E8D end

    def Function_16_3F60(): pass

    label("Function_16_3F60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_3FA8")

    #C0177
    ChrTalk(
        0x12,
        (
            "本当はあんな奴、\x01",
            "顔を合わせたくも無いんだがな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4007")

    label("loc_3FA8")


    #C0178
    ChrTalk(
        0x12,
        (
            "お袋に弁当を届けるよう\x01",
            "言われてしまってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x12,
        (
            "……くそっ、\x01",
            "オヤジの奴はどこだ……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_4007")

    TalkEnd(0xFE)
    Return()

    # Function_16_3F60 end

    def Function_17_400B(): pass

    label("Function_17_400B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCE, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_41C5")

    #C0180
    ChrTalk(
        0x101,
        (
            "#0005Fあれ、ケイト先輩……？\x01",
            "何でこんな所に！？\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        (
            "#0200F制服組に市外活動なんて\x01",
            "ありましたっけ……\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        "あ、私はただの付き添いなの。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xFE,
        (
            "今ウルスラ病院には\x01",
            "黒月の人たちが入院してるんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "捜査二課の人たちが\x01",
            "事情聴取したいそうだから\x01",
            "パトカーでお送りしたってわけ。\x02",
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
            "私、車両の運転は\x01",
            "苦手なんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        "#0000Fはは……そうだったんですか。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x102,
        "#0100Fいつもお疲れ様です。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0xCE, 7)
    Jump("loc_42C7")

    label("loc_41C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4288")

    #C0188
    ChrTalk(
        0xFE,
        (
            "黒月って、マフィア組織だったのね。\x01",
            "私も全然知らなかったなー……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "……っていうか、\x01",
            "二課の人たち時間掛かってるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "もうお昼を回ってるのに。\x01",
            "てこずってるのかしら。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_42C7")

    label("loc_4288")


    #C0191
    ChrTalk(
        0xFE,
        (
            "二課の人たち、何やってるのかしら。\x01",
            "時間掛かってるわね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_42C7")

    TalkEnd(0xFE)
    Return()

    # Function_17_400B end

    def Function_18_42CB(): pass

    label("Function_18_42CB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_434C")

    #C0192
    ChrTalk(
        0xFE,
        (
            "ここの病院には\x01",
            "我らが同士、ヨアヒム団員が\x01",
            "いらっしゃるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0xFE,
        (
            "うふふ、後で\x01",
            "お誘いしてみましょうかねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_434C")

    TalkEnd(0xFE)
    Return()

    # Function_18_42CB end

    def Function_19_4350(): pass

    label("Function_19_4350")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_447C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4436")

    #C0194
    ChrTalk(
        0xFE,
        (
            "我らが団長、フィッシャー氏が\x01",
            "クロスベル支部を作られたのは\x01",
            "２年前のことだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0xFE,
        (
            "この２年、クロスベル支部は\x01",
            "着実に活動を伸ばしているようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "釣り仲間が増えるなんて\x01",
            "嬉しいことこの上ないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_447C")

    label("loc_4436")


    #C0197
    ChrTalk(
        0xFE,
        (
            "釣り仲間に誘われて\x01",
            "旅ができるなんて……\x01",
            "嬉しいことこの上ないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_447C")

    TalkEnd(0xFE)
    Return()

    # Function_19_4350 end

    def Function_20_4480(): pass

    label("Function_20_4480")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4514")
    Jump("loc_455E")

    label("loc_4514")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4534")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_455E")

    label("loc_4534")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4554")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_455E")

    label("loc_4554")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_455E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_4615")

    #C0198
    ChrTalk(
        0xFE,
        (
            "……そろそろ私も診察室に\x01",
            "もどらねばな。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "いくら疲れているとはいえ、\x01",
            "いつまでも空けていて\x01",
            "ラゴー教授に笑われるのも癪だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_4615")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_4791")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_46AF")

    #C0200
    ChrTalk(
        0xFE,
        (
            "もっとごっそり持っていって\x01",
            "くれるのを期待していたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "はぁ……\x01",
            "魔除けの人形ともなると\x01",
            "どうも捨てにくいのだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_478C")

    label("loc_46AF")


    #C0202
    ChrTalk(
        0xFE,
        (
            "テラスにおいていた雑貨……\x01",
            "なにかいいものはあったかね？\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "……皮の編み紐？\x01",
            "それだけでいいのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "もっとごっそり持っていって\x01",
            "くれてもよかったんだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x101,
        (
            "#0006F（さすがに置物や人形は\x01",
            "  かさばるしな……）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_478C")

    Jump("loc_49B9")

    label("loc_4791")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_485D")

    #C0206
    ChrTalk(
        0xFE,
        (
            "雑貨の入ったコンテナは\x01",
            "寮の２階、男性職員寮を抜けた先の\x01",
            "テラスに置いてある。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0xFE,
        (
            "良さそうなものがあったら\x01",
            "適当に見繕って\x01",
            "持って行ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        "正直処分に困っているのでね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_485D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_4871")
    Call(0, 62)
    Jump("loc_49B9")

    label("loc_4871")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_48D5")

    #C0209
    ChrTalk(
        0xFE,
        (
            "家庭や仕事のことから\x01",
            "疲れがでていてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "教授というものも\x01",
            "なかなか大変だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_49B9")

    label("loc_48D5")


    #C0211
    ChrTalk(
        0xFE,
        "……最近どうも疲れがでていてね。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "看護師のシロンくんに\x01",
            "備品の発注を頼んだら\x01",
            "別のものが送られてくるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "息子のキーンツも\x01",
            "相変わらず不良グループから\x01",
            "抜ける気配はない……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "教授というものも\x01",
            "なかなか大変だよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)

    label("loc_49B9")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_20_4480 end

    def Function_21_49C1(): pass

    label("Function_21_49C1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B7C")
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0215
    ChrTalk(
        0x16,
        "#2900Fあらエリィ、奇遇ですわね。\x02",
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x102,
        (
            "#0105Fベル……？\x01",
            "こんな所でどうしたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x16,
        (
            "#2900Fええ、お父様に\x01",
            "付き合いで来たのですわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x103,
        "#0200Fディーター総裁の……\x02",
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x101,
        "#0000F総裁、何かご病気を……？\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x102,
        (
            "#0109Fあはは……たぶん\x01",
            "そうではないと思うけど……\x02\x03",

            "#0100Fベル、例のあれよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x16,
        (
            "#2904Fええ、その通りですわ。\x02\x03",

            "#2900F受付に行けば分かるでしょう。\x01",
            "時間があるならお父様に\x01",
            "会ってらっしゃったら？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xB4, 6)
    Jump("loc_4D1C")

    label("loc_4B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4BEC")

    #C0222
    ChrTalk(
        0x16,
        (
            "#2906Fお父様、遅いですわね。\x01",
            "何をやっているのかしら。\x02\x03",

            "あと３０分で\x01",
            "商談の時間だというのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D1C")

    label("loc_4BEC")


    #C0223
    ChrTalk(
        0x16,
        (
            "#2906F商談が重なって忙しい時期に……\x01",
            "やれやれですわ。\x02\x03",

            "#2900Fでもまあ、お父様の\x01",
            "数少ない美徳の一つですから。\x02\x03",

            "娘として付き合ってやるのも\x01",
            "やぶさかではありませんわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x102,
        (
            "#0102Fふふ、とか言って毎年\x01",
            "付き添いをしているくせに。\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x16,
        (
            "#2904F……ま、毎年たまたま時間が\x01",
            "取れるのだから、仕方ないですわ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_4D1C")

    TalkEnd(0xFE)
    Return()

    # Function_21_49C1 end

    def Function_22_4D20(): pass

    label("Function_22_4D20")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4E7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E04")

    #C0226
    ChrTalk(
        0x18,
        (
            "#2400Fリットン君も復帰してから\x01",
            "よく仕事を頑張ってくれたよ。\x02\x03",

            "しかも、ついでにこっそり\x01",
            "差し込んでおいた僕の仕事まで\x01",
            "片付けてくれたみたいでね。\x02\x03",

            "#2409Fはっはっは、\x01",
            "いい生徒を持って僕は幸せだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_4E7C")

    label("loc_4E04")


    #C0227
    ChrTalk(
        0x18,
        (
            "#2400Fリットン君が折角僕の仕事を\x01",
            "片付けてくれたんだ。\x02\x03",

            "#2409F空いた時間は釣りでもして\x01",
            "有効活用させてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E7C")

    TalkEnd(0xFE)
    Return()

    # Function_22_4D20 end

    def Function_23_4E80(): pass

    label("Function_23_4E80")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4F14")
    Jump("loc_4F5E")

    label("loc_4F14")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4F34")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F5E")

    label("loc_4F34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4F54")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4F5E")

    label("loc_4F54")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4F5E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5013")

    #C0228
    ChrTalk(
        0xFE,
        (
            "旅行において最も大事なのは、\x01",
            "その国の特色を楽しむことさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xFE,
        (
            "医療研究で有名なこの病院も\x01",
            "充分、観光地になりうるのだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_5093")

    label("loc_5013")


    #C0230
    ChrTalk(
        0xFE,
        (
            "旅行において最も大事なのは、\x01",
            "その国の特色を楽しむことさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xFE,
        (
            "クロスベルは見るところが多くて\x01",
            "いささか大変ではあるけどね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5093")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_23_4E80 end

    def Function_24_509B(): pass

    label("Function_24_509B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5158")

    #C0232
    ChrTalk(
        0xFE,
        (
            "この病院には、健康状態を検査する\x01",
            "『人間ドック』とやらの設備が\x01",
            "整っているとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "日々の家事・雑用などで\x01",
            "疲れきったこの体……\x01",
            "ぜひ調べてもらいたいものですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_51EE")

    label("loc_5158")


    #C0234
    ChrTalk(
        0xFE,
        (
            "仕事で疲れきったこの体、\x01",
            "『人間ドック』とやらで\x01",
            "悪い結果がでた暁には……\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0xFE,
        (
            "それをネタにして、\x01",
            "ご主人様に更なるお休みを\x01",
            "頂きたいところですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_51EE")

    TalkEnd(0xFE)
    Return()

    # Function_24_509B end

    def Function_25_51F2(): pass

    label("Function_25_51F2")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5289")
    Call(0, 26)
    ClearMapFlags(0x8000000)
    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_52A9")

    label("loc_5289")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_52A9")
    Call(0, 26)
    ClearMapFlags(0x8000000)
    NewScene("r1530", 0, 0, 0)
    IdleLoop()

    label("loc_52A9")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_25_51F2 end

    def Function_26_52B1(): pass

    label("Function_26_52B1")

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

    def lambda_5387():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_5387)
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x1C, 1)
    OP_71(0x7, 0x5B, 0x78, 0x1, 0x0)
    OP_79(0x7)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x7E, 0)
    Return()

    # Function_26_52B1 end

    def Function_27_53CA(): pass

    label("Function_27_53CA")

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

    # Function_27_53CA end

    def Function_28_545F(): pass

    label("Function_28_545F")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    Sound(1499, 255, 100, 0)    #voice#Noel
    Sleep(500)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5479")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A09")

    Menu(
        0,
        32,
        26,
        1,
        (
            "警備隊車両で移動をする\x01",      # 0
            "ここで休憩をする\x01",            # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59A6")
    Sound(1500, 255, 100, 0)    #voice#Noel
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_550F")
    MenuCmd(1, 1, "★クロスベル市・中央広場")
    MenuCmd(3, 1, 0x0)
    Jump("loc_552B")

    label("loc_550F")

    MenuCmd(1, 1, "　クロスベル市・中央広場")

    label("loc_552B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_555D")
    MenuCmd(1, 1, "★クロスベル市・東出口")
    MenuCmd(3, 1, 0x1)
    Jump("loc_5577")

    label("loc_555D")

    MenuCmd(1, 1, "　クロスベル市・東出口")

    label("loc_5577")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55A9")
    MenuCmd(1, 1, "★クロスベル市・西出口")
    MenuCmd(3, 1, 0x2)
    Jump("loc_55C3")

    label("loc_55A9")

    MenuCmd(1, 1, "　クロスベル市・西出口")

    label("loc_55C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55F5")
    MenuCmd(1, 1, "★クロスベル市・南出口")
    MenuCmd(3, 1, 0x3)
    Jump("loc_560F")

    label("loc_55F5")

    MenuCmd(1, 1, "　クロスベル市・南出口")

    label("loc_560F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5641")
    MenuCmd(1, 1, "★クロスベル市・北出口")
    MenuCmd(3, 1, 0x4)
    Jump("loc_565B")

    label("loc_5641")

    MenuCmd(1, 1, "　クロスベル市・北出口")

    label("loc_565B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5685")
    MenuCmd(1, 1, "★タングラム門")
    MenuCmd(3, 1, 0x5)
    Jump("loc_5697")

    label("loc_5685")

    MenuCmd(1, 1, "　タングラム門")

    label("loc_5697")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56C1")
    MenuCmd(1, 1, "★ベルガード門")
    MenuCmd(3, 1, 0x6)
    Jump("loc_56D3")

    label("loc_56C1")

    MenuCmd(1, 1, "　ベルガード門")

    label("loc_56D3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5701")
    MenuCmd(1, 1, "★ウルスラ医科大学")
    MenuCmd(3, 1, 0x7)
    Jump("loc_5717")

    label("loc_5701")

    MenuCmd(1, 1, "　ウルスラ医科大学")

    label("loc_5717")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5741")
    MenuCmd(1, 1, "★アルモリカ村")
    MenuCmd(3, 1, 0x8)
    Jump("loc_5753")

    label("loc_5741")

    MenuCmd(1, 1, "　アルモリカ村")

    label("loc_5753")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_577F")
    MenuCmd(1, 1, "★マインツ鉱山町")
    MenuCmd(3, 1, 0x9)
    Jump("loc_5793")

    label("loc_577F")

    MenuCmd(1, 1, "　マインツ鉱山町")

    label("loc_5793")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57C5")
    MenuCmd(1, 1, "★マインツ山道・隧道内")
    MenuCmd(3, 1, 0xA)
    Jump("loc_57DF")

    label("loc_57C5")

    MenuCmd(1, 1, "　マインツ山道・隧道内")

    label("loc_57DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5805")
    MenuCmd(1, 1, "★星見の塔")
    MenuCmd(3, 1, 0xB)
    Jump("loc_5813")

    label("loc_5805")

    MenuCmd(1, 1, "　星見の塔")

    label("loc_5813")

    MenuCmd(1, 1, "　やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, 240, 16, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5997")
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
        (0, "loc_58EA"),
        (1, "loc_58F8"),
        (2, "loc_5906"),
        (3, "loc_5914"),
        (4, "loc_5922"),
        (5, "loc_5930"),
        (6, "loc_593E"),
        (7, "loc_594C"),
        (8, "loc_595A"),
        (9, "loc_5968"),
        (10, "loc_5976"),
        (11, "loc_5984"),
        (SWITCH_DEFAULT, "loc_5992"),
    )


    label("loc_58EA")

    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_58F8")

    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_5906")

    NewScene("r1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_5914")

    NewScene("r1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_5922")

    NewScene("r2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_5930")

    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_593E")

    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_594C")

    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_595A")

    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_5968")

    NewScene("t0500", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_5976")

    NewScene("r2050", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_5984")

    NewScene("m1000", 0, 0, 0)
    IdleLoop()
    Jump("loc_5992")

    label("loc_5992")

    Jump("loc_59A1")

    label("loc_5997")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59A1")

    Jump("loc_5A04")

    label("loc_59A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59F1")
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
    Jump("loc_5A04")

    label("loc_59F1")

    OP_60(0x0)
    OP_57(0x0)
    Sleep(500)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_5A04")

    Jump("loc_5479")

    label("loc_5A09")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_545F end

    def Function_29_5A11(): pass

    label("Function_29_5A11")

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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_5AE5")
    Sound(1502, 255, 100, 0)    #voice#Noel
    Jump("loc_5AEB")

    label("loc_5AE5")

    Sound(1503, 255, 100, 0)    #voice#Noel

    label("loc_5AEB")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_29_5A11 end

    def Function_30_5B00(): pass

    label("Function_30_5B00")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 28)
    Return()

    # Function_30_5B00 end

    def Function_31_5B0E(): pass

    label("Function_31_5B0E")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0237
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

    #A0238
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BDD")
    OP_E0(0x2)
    MiniGame(0x6, 0xE, 0xFFFFBFBE, 0xFFFFFC18, 0xFFFF9A5C, 0xB4, 0xFFFFBCE4, 0xFFFFF830, 0xFFFF7FFE)

    label("loc_5BDD")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_31_5B0E end

    def Function_32_5BE2(): pass

    label("Function_32_5BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C1E")
    TalkBegin(0xFF)
    SetChrName("")

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Jump("loc_5D5C")

    label("loc_5C1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5C9E")
    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【導力バスを待つ】\x01",      # 0
            "【やめておく】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5C8A"),
        (1, "loc_5C92"),
        (SWITCH_DEFAULT, "loc_5C97"),
    )


    label("loc_5C8A")

    Call(0, 47)
    Jump("loc_5C97")

    label("loc_5C92")

    Jump("loc_5C97")

    label("loc_5C97")

    EventEnd(0x3)
    Jump("loc_5D5C")

    label("loc_5C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_5CAF")
    Call(0, 25)
    Jump("loc_5D5C")

    label("loc_5CAF")

    TalkBegin(0xFF)
    SetChrName("")

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バスの停留所がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_END)), "loc_5D1E")

    #C0241
    ChrTalk(
        0x101,
        (
            "#0000Fおっと……帰る前に\x01",
            "セシル姉に報告をしないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5D59")

    label("loc_5D1E")


    #C0242
    ChrTalk(
        0x101,
        (
            "#0000Fクロスベル市に戻る前に\x01",
            "魔獣の調査をしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5D59")

    TalkEnd(0xFF)

    label("loc_5D5C")

    Return()

    # Function_32_5BE2 end

    def Function_33_5D5D(): pass

    label("Function_33_5D5D")

    Call(0, 37)
    Return()

    # Function_33_5D5D end

    def Function_34_5D61(): pass

    label("Function_34_5D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D73")
    Call(0, 42)
    Jump("loc_5DD7")

    label("loc_5D73")

    TalkBegin(0xFF)

    #A0243
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "木箱の上はホコリにまみれている。\x02\x03",

            "どうやらしばらくの間、\x01",
            "放置されたままのようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_5DD7")

    Return()

    # Function_34_5D61 end

    def Function_35_5DD8(): pass

    label("Function_35_5DD8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5DEA")
    Call(0, 43)
    Jump("loc_5E54")

    label("loc_5DEA")

    TalkBegin(0xFF)

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手すりの上の部分の塗装に\x01",
            "所々、こすって剥がれた跡がある。\x02\x03",

            "どうやら最近出来たものらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_5E54")

    Return()

    # Function_35_5DD8 end

    def Function_36_5E55(): pass

    label("Function_36_5E55")

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
            "#0300F#5Pここが医科大学か……\x01",
            "へえ、なかなか立派な施設だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x103,
        (
            "#0203F#6P……『聖ウルスラ医科大学』。\x02\x03",

            "#0200F大陸有数の総合病院にして\x01",
            "医療研究機関として有名ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x101,
        (
            "#6P#0005Fそんなに有名だったのか。\x02\x03",

            "#0000F確かにバスの本数が多いあたり、\x01",
            "利用者はかなり多そうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#0104F元々は、医療先進国である\x01",
            "レミフェリア公国の協力で\x01",
            "設立されたと聞いているわね。\x02\x03",

            "#0100F周辺諸国からも重病人を\x01",
            "受け入れてるって聞いているわ。\x02",
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
            "#0302F#5Pおっと、ナース服の\x01",
            "お姉ちゃんたちがいるじゃん！\x02\x03",

            "#0309Fいやあ、眼福、眼福♪\x02",
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

    def lambda_61E4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_61E4)
    Sleep(50)

    def lambda_61F4():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_61F4)
    Sleep(50)

    def lambda_6204():
        TurnDirection(0xFE, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6204)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0250
    ChrTalk(
        0x101,
        "#0012F#12Pランディは元気だなぁ……\x02",
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x102,
        (
            "#0103F#6P今までにも何度か\x01",
            "車で訪れた事はあるけど……\x02\x03",

            "#0100Fやっぱり徒歩で来ると\x01",
            "結構な距離だったわね。\x02",
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

    def lambda_6307():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6307)
    Sleep(50)

    def lambda_6317():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6317)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)

    def lambda_632C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_632C)
    Sleep(300)

    #C0253
    ChrTalk(
        0x101,
        "#11P#0005Fティオ……？\x02",
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x102,
        "#0105Fさすがに疲れちゃった？\x02",
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x103,
        (
            "#0203F#6P……いえ、平気です。\x02\x03",

            "#0200Fアルモリカ村ほど遠い距離では\x01",
            "ありませんでしたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#11P#0001Fならいいけど……\x01",
            "あんまり無理はするなよ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(300)

    #C0257
    ChrTalk(
        0x103,
        (
            "#0204F#6Pええ、ご心配なく。\x02\x03",

            "#0202F……それよりロイドさんは\x01",
            "お知り合いのお姉さんに\x01",
            "会わなくてもいいんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x104,
        "#0305F#5Pそうか、それもあったな！\x02",
    )

    CloseMessageWindow()

    def lambda_64B5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_64B5)
    WaitChrThread(0x104, 1)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0259
    ChrTalk(
        0x104,
        (
            "#0307F#5Pほらほら、ロイド！\x01",
            "とっとと会いに行こうぜ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6514():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6514)

    def lambda_6521():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6521)

    def lambda_652E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_652E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)

    #C0260
    ChrTalk(
        0x101,
        (
            "#0006F#12P……なんでランディが\x01",
            "そんなにテンション上げるんだよ。\x02\x03",

            "#0000Fまあいいか、セシル姉だったら\x01",
            "話も通しやすそうだし……\x02\x03",

            "病院の受付で呼び出してもらおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        "#0309F#5Pよっしゃ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0262
    ChrTalk(
        0x102,
        (
            "#0102Fふふ、それじゃあ\x01",
            "正面の病棟に入りましょうか。\x02",
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

    # Function_36_5E55 end

    def Function_37_666F(): pass

    label("Function_37_666F")

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
            "#0000F#6Pさてと……\x01",
            "この上を調べさせてもらうか。\x02\x03",

            "ランディ、手伝ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x104,
        "#0300F#5Pよしきた。\x02",
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
            "木箱の上はホコリにまみれており\x01",
            "その上に何かの跡がある。\x02\x03",

            "どうやら獣の足跡のようだ。\x07\x00\x02",
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
        "#0004F#6P……ビンゴだな。\x02",
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x104,
        (
            "#0300F#6Pああ、魔獣の足跡……\x01",
            "それも狼型のヤツだろう。\x02",
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
        "#0101F#5Pやっぱり……\x02",
    )

    CloseMessageWindow()

    def lambda_68BF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_68BF)
    Sleep(50)

    def lambda_68CF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_68CF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)

    #C0269
    ChrTalk(
        0x103,
        "#0203Fとなると……\x02",
    )

    CloseMessageWindow()
    OP_68(-36200, 4000, 20200, 4000)
    MoveCamera(35, 16, 0, 4000)
    SetCameraDistance(34000, 4000)

    def lambda_6921():
        OP_95(0xFE, -36480, 3000, 20450, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6921)
    Sleep(500)

    def lambda_693E():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_693E)
    Sleep(300)

    def lambda_694E():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_694E)
    Sleep(100)

    def lambda_695E():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_695E)
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
            "#0200F#6Pあちらの方から侵入された\x01",
            "可能性が高そうですね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_69C2():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_69C2)
    WaitChrThread(0x104, 1)

    #C0271
    ChrTalk(
        0x101,
        "#0000Fああ、多分そうだろう。\x02",
    )

    CloseMessageWindow()
    OP_68(-36930, 3900, 16980, 3000)
    SetCameraDistance(26500, 3000)
    BeginChrThread(0x101, 3, 0, 40)
    BeginChrThread(0x104, 3, 0, 41)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x104, 3)

    def lambda_6A23():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6A23)

    def lambda_6A30():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6A30)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)
    Sleep(300)

    #C0272
    ChrTalk(
        0x104,
        (
            "#0300F#6P見たところそっちは、\x01",
            "それほど高さが無さそうだ。\x02\x03",

            "また入られちまわないよう、\x01",
            "何か対策をした方がいいかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x102,
        "#0103F#6Pそうね……\x02",
    )

    CloseMessageWindow()

    def lambda_6ADC():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6ADC)
    WaitChrThread(0x102, 1)
    Sleep(300)

    #C0274
    ChrTalk(
        0x102,
        (
            "#0100F#6Pでも、ここでの調査は\x01",
            "これで一通り終了かしら？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B2C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6B2C)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0275
    ChrTalk(
        0x101,
        (
            "#0001F#11Pああ、そうだな……\x02\x03",

            "#0003F……どうしてわざわざ\x01",
            "こんな所に入ってきたのか……\x02\x03",

            "それに、どうしてリットンさんを\x01",
            "中途半端に襲ったのか……\x02\x03",

            "#0001Fまだまだ謎は残っているけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6BF8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6BF8)
    Sleep(100)

    def lambda_6C08():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6C08)
    WaitChrThread(0x103, 1)
    Sleep(300)

    #C0276
    ChrTalk(
        0x103,
        (
            "#0205F#5Pさすがにそれは\x01",
            "魔獣に聞いてみないと\x01",
            "分からないのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x104,
        (
            "#0302F#5Pそうそう。\x02\x03",

            "警備隊の調書の補完が\x01",
            "出来ただけでも十分だろ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CAD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CAD)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0278
    ChrTalk(
        0x101,
        (
            "#0004F#12Pそうだな……\x02\x03",

            "#0000Fよし、とりあえず、\x01",
            "帰る前にセシル姉に報告しよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x102,
        (
            "#0102F#6Pそうね……\x01",
            "報告とお礼を言わなきゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#0309F#5Pそんじゃまあ、\x01",
            "ナースセンターでも行きますか！\x02",
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

    # Function_37_666F end

    def Function_38_6DD3(): pass

    label("Function_38_6DD3")

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

    def lambda_6E3D():
        OP_95(0xFE, -32689, 4150, 16470, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6E3D)
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

    # Function_38_6DD3 end

    def Function_39_6E9E(): pass

    label("Function_39_6E9E")

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

    def lambda_6F1A():
        OP_96(0xFE, 0xFFFF7AAE, 0x1036, 0x42C2, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F1A)
    WaitChrThread(0x104, 1)
    Sleep(2000)
    OP_64(0x104)

    def lambda_6F3E():
        OP_96(0xFE, 0xFFFF7AAE, 0x1036, 0x44B6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6F3E)
    WaitChrThread(0x104, 1)
    Sleep(1050)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Return()

    # Function_39_6E9E end

    def Function_40_6F76(): pass

    label("Function_40_6F76")


    def lambda_6F7B():
        OP_95(0xFE, -34000, 4150, 16530, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6F7B)
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

    # Function_40_6F76 end

    def Function_41_7006(): pass

    label("Function_41_7006")

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

    # Function_41_7006 end

    def Function_42_707F(): pass

    label("Function_42_707F")

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
            "木箱の上はホコリにまみれている。\x02\x03",

            "どうやらしばらくの間、\x01",
            "放置されたままのようだ。\x07\x00\x02",
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
        "#0005F#2P（あれ……？）\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x102,
        "#0105F#12P……どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        "#0003F#2Pいや……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0285
    ChrTalk(
        0x101,
        (
            "#0008F#2P（向こうから飛び乗ってきたら\x01",
            "  この上に足跡が付きそうだけど……）\x02\x03",

            "（ホコリが付いたままってことは\x01",
            "  しばらくこの状態のままだろうし……）\x02\x03",

            "#0000F（まあ、別にそこまで\x01",
            "  おかしな事じゃないかな……？）\x02",
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

    # Function_42_707F end

    def Function_43_72F9(): pass

    label("Function_43_72F9")

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
        "#0001F#5P（これは……？）\x02",
    )

    CloseMessageWindow()

    #A0287
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手すりの上の部分の塗装に\x01",
            "所々、こすって剥がれた跡がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Sleep(300)

    #C0288
    ChrTalk(
        0x103,
        "#0205F#11Pロイドさん……？\x02",
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x104,
        "#0305F#11Pなんだよ、さっきから？\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x101,
        (
            "#0012F#5Pいや……\x01",
            "大したことじゃないんだ。\x02\x03",

            "#0008F（うーん……\x01",
            "  最近の跡みたいだけど。）\x02",
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

    # Function_43_72F9 end

    def Function_44_74ED(): pass

    label("Function_44_74ED")

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
            "#1301F#12Pなるほど……\x01",
            "ここから魔獣が入り込んだのね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7668():
        OP_95(0xFE, -37280, 3000, 23830, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x136, 1, lambda_7668)

    def lambda_7682():

        label("loc_7682")

        TurnDirection(0x101, 0x136, 500)
        Yield()
        Jump("loc_7682")

    QueueWorkItem2(0x101, 1, lambda_7682)

    def lambda_7694():

        label("loc_7694")

        TurnDirection(0x102, 0x136, 500)
        Yield()
        Jump("loc_7694")

    QueueWorkItem2(0x102, 1, lambda_7694)

    def lambda_76A6():

        label("loc_76A6")

        TurnDirection(0x103, 0x136, 500)
        Yield()
        Jump("loc_76A6")

    QueueWorkItem2(0x103, 1, lambda_76A6)

    def lambda_76B8():

        label("loc_76B8")

        TurnDirection(0x104, 0x136, 500)
        Yield()
        Jump("loc_76B8")

    QueueWorkItem2(0x104, 1, lambda_76B8)
    Sleep(500)

    #C0292
    ChrTalk(
        0x101,
        (
            "#0001F#12P魔獣が何故入り込んだか\x01",
            "そこまでは判っていないけど……\x02\x03",

            "何らかの対応策は\x01",
            "とった方がいいとは思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x136,
        (
            "#1308F#5Pそうね、急ごしらえには\x01",
            "なってしまうと思うけど……\x02\x03",

            "#1301F魔獣除けのフェンスくらいなら\x01",
            "増設できるかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x104,
        (
            "#0300F#11Pああ、それだけでも\x01",
            "かなり違いがあるッスよ。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x136, 1)

    #C0295
    ChrTalk(
        0x103,
        (
            "#0200F#11Pそれなりの強度で\x01",
            "可動式のものが必要ですが……\x02\x03",

            "この病院にそんな設備が？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x136, 0xB4, 0x1F4)
    Sleep(300)

    #C0296
    ChrTalk(
        0x136,
        (
            "#1304F#5Pええ、確か野外治療用の設備で\x01",
            "そういったものがあったはずよ。\x02\x03",

            "#1300F事務長さんに相談して\x01",
            "設置してしまいましょう。\x02",
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
            "ふふ、お疲れ様でした。\x02\x03",

            "これでみんなも安心できるわ。\x01",
            "本当にあなた達のおかげね。\x02",
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
        "#0309F#6Pいや～、そんな♪\x02",
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x101,
        (
            "#0004F#6Pはは、でも実際、\x01",
            "大したことはしていないよ。\x02\x03",

            "#0000F本当に魔獣が入り込んだか\x01",
            "証明したっていうだけだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x136,
        (
            "#1304F#11Pううん、それが無かったら\x01",
            "きちんとした対策も取れずに\x01",
            "そのままだったところだもの。\x02\x03",

            "#1300Fあなた達だったら、いずれ\x01",
            "アリオスさんにも負けないくらい\x01",
            "いい仕事ができると思うわ。\x02\x03",

            "#1309Fお姉ちゃんが保証してあげる㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#0005F#6Pセシル姉……\x02",
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)

    #C0302
    ChrTalk(
        0x104,
        "#0301F#6Pか、感激ッス……！\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x102,
        (
            "#0109F#6Pありがとうございます。\x01",
            "とても、励みになります。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        "#0202F#6P……頑張ります。\x02",
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x136,
        (
            "#1309F#11Pふふ……\x02\x03",

            "#1302Fロイド、お互い休みが取れたら\x01",
            "改めてゆっくり会いましょう。\x02\x03",

            "お墓参りも一緒に行きたいしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        "#0002F#6P……うん、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x136,
        (
            "#1304F#11P後は、そうねぇ。\x02\x03",

            "#1302Fエリィちゃんとティオちゃんの\x01",
            "どちらかと付き合うことになったら\x01",
            "ぜひ報告してちょうだいね？\x02\x03",

            "#1309F目一杯お祝いしちゃうから㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0308
    ChrTalk(
        0x101,
        (
            "#0011F#6Pいや、だから……\x01",
            "どうしてそんな話になるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x136,
        (
            "#1306F#11Pなんだったらランディ君とでも\x01",
            "いいけれど……\x02\x03",

            "#1301Fその時は連絡してね？\x01",
            "そういったジャンルを読んで\x01",
            "バッチリ鍛えておくから！\x02",
        )
    )

    CloseMessageWindow()

    #C0310
    ChrTalk(
        0x101,
        "#0006F#6Pどんなジャンルだよ……\x02",
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x104,
        (
            "#0309F#6Pいや～！\x01",
            "セシルさんが喜んでくれるなら\x01",
            "俺の方は構わないッスよ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 1000)
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0312
    ChrTalk(
        0x101,
        "#0011F#4S#11Pいや、構おうよ！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0313
    ChrTalk(
        0x136,
        (
            "#1309F#11Pふふ、それじゃあ私は\x01",
            "ここで失礼しちゃおうかな。\x02\x03",

            "#1302Fみんな、気をつけて帰ってね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80C6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_80C6)
    WaitChrThread(0x101, 1)
    Sleep(300)

    #C0314
    ChrTalk(
        0x101,
        "#0002F#6P──うん。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#0102F#6Pお世話になりました。\x02",
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
        "#0309F#6Pはあ、いいなぁ……\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x102,
        (
            "#0104F#6P暖かくって包容力があって\x01",
            "頼りがいもあって……\x02\x03",

            "#0102Fふふ、とっても素敵な人ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x101,
        (
            "#0009F#6Pはは……\x01",
            "そう言ってもらえると嬉しいよ。\x02\x03",

            "#0002F実の姉さん以上に\x01",
            "世話になってきた人だからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x103,
        (
            "#0204F#6P……それで、ロイドさん。\x02\x03",

            "#0202Fセシルさんとは実際には\x01",
            "どういうご関係なんですか？\x02",
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
        "#0011F#11Pへ……\x02",
    )

    CloseMessageWindow()

    def lambda_82B8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_82B8)
    Sleep(50)

    def lambda_82C8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_82C8)
    WaitChrThread(0x102, 1)
    Sleep(300)

    #C0321
    ChrTalk(
        0x102,
        (
            "#0104F#5Pそうね……\x01",
            "ちょっとだけ気になるわね。\x02\x03",

            "#0102Fあなた、いつにも増して\x01",
            "弟君って雰囲気だったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x101,
        "#0001F#11Pな、なんだそりゃ……\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x104,
        (
            "#0310F#5Pロイド、てめえ……！\x02\x03",

            "あんな素敵なお姉さんと\x01",
            "ベタベタ甘々な関係ってか！？\x02\x03",

            "#0307Fうらやましい！\x01",
            "身体を交換してください！\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x101,
        (
            "#0006F#11P出来ないから。\x02\x03",

            "#0001F馬鹿なこと言ってないで\x01",
            "そろそろクロスベルに戻ろう。\x02\x03",

            "もう夕方だし……\x01",
            "帰ったら今日の分の調書を\x01",
            "ちゃんとまとめておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x103,
        "#0211F#6P（……誤魔化しましたね……）\x02",
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x102,
        "#0111F#5P（ええ……それも露骨に……）\x02",
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x104,
        (
            "#0310F#5P（おのれロイド……！\x01",
            "  俺のドストライクな人を……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_8548():
        OP_93(0xFE, 0x13B, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8548)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_82(0x0, 0x64, 0xBB8, 0xC8)

    #C0328
    ChrTalk(
        0x101,
        "#0003F#4S#11Pそこ、ヒソヒソ話をしない！\x02",
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

    # Function_44_74ED end

    def Function_45_861B(): pass

    label("Function_45_861B")

    OP_93(0xFE, 0x5A, 0x12C)

    def lambda_8627():
        OP_95(0xFE, 1500, 1000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8627)
    WaitChrThread(0xFE, 1)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)

    def lambda_8660():
        OP_95(0xFE, 4500, 1000, 0, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_8660)
    Sleep(500)

    def lambda_867D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_867D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    Return()

    # Function_45_861B end

    def Function_46_86AD(): pass

    label("Function_46_86AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8719")
    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    OP_98(0xFE, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    Sleep(1000)
    Jump("Function_46_86AD")

    label("loc_8719")

    Return()

    # Function_46_86AD end

    def Function_47_871A(): pass

    label("Function_47_871A")

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
            "#0000F#6Pさてと……\x01",
            "バスが来るのを待つとするか。\x02\x03",

            "時刻表によると……\x01",
            "次は１５分後くらいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x104,
        (
            "#0305F#4Pしかし随分と便利だよな。\x02\x03",

            "夜の１１時まで\x01",
            "運行してるみたいじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x103,
        (
            "#0203F#6P運賃の方もお手頃ですし……\x02\x03",

            "#0200F市の運営とのことですが\x01",
            "採算は取れてるんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x103, 500)
    Sleep(300)

    #C0332
    ChrTalk(
        0x102,
        (
            "#0102Fまあ、それだけ市の方でも\x01",
            "病院を重要視しているみたいね。\x02\x03",

            "財政的には余裕があるし、\x01",
            "市民の要望も高いみたいだから。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x102, 500)

    #C0333
    ChrTalk(
        0x103,
        "#0202F#6Pなるほど……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)

    #C0334
    ChrTalk(
        0x101,
        (
            "#0000F#5Pま、気軽に病院に行けるのは\x01",
            "やっぱり有難いかもしれないな。\x02",
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

    def lambda_8B06():
        OP_95(0xFE, -59000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8B06)
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

    def lambda_8B5A():
        OP_9B(0x0, 0xFE, 0x0, 0xED8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_8B5A)
    Sleep(100)

    def lambda_8B72():
        OP_9B(0x0, 0xFE, 0x0, 0x1324, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8B72)
    Sleep(80)

    def lambda_8B8A():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8B8A)
    Sleep(0)

    def lambda_8BA2():
        OP_9B(0x0, 0xFE, 0x0, 0x1BBC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8BA2)
    Sleep(200)

    def lambda_8BBA():
        OP_9B(0x0, 0xFE, 0x0, 0x2008, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_8BBA)
    Sleep(100)

    def lambda_8BD2():
        OP_9B(0x0, 0xFE, 0x0, 0x2454, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_8BD2)
    Sleep(150)

    def lambda_8BEA():
        OP_9B(0x0, 0xFE, 0x0, 0x28A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_8BEA)
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

    def lambda_8D11():
        OP_95(0xFE, -75000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_8D11)
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

    # Function_47_871A end

    def Function_48_8D83(): pass

    label("Function_48_8D83")

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

    def lambda_8F2C():
        OP_95(0xFE, -56000, 0, 500, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_8F2C)
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
            "#1109F#6Pえへへ……\x01",
            "すっごく楽しかったー！\x02\x03",

            "#1110Fあるくのも楽しいけど\x01",
            "バスもすっごく楽しいね！\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#0014F#11Pはは、そっか。\x02\x03",

            "#0008F（どうやら車に乗るのは\x01",
            "  初めてみたいだけど……）\x02\x03",

            "#0001F（もしかして鉄道や飛行船にも\x01",
            "  乗った事がないのか……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x153,
        (
            "#1105F#6Pそれで……\x01",
            "ここがビョーインってところ？\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x101,
        (
            "#0004F#11Pああ、医科大学っていう、\x01",
            "研究なんかもしている病院だよ。\x02\x03",

            "#0000Fキーアが忘れちゃったことを\x01",
            "思い出させてくれるかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_928C")

    #C0339
    ChrTalk(
        0x153,
        (
            "#1106F#6Pんー……別にキーア、\x01",
            "思い出さなくってもいいけど。\x02\x03",

            "#1100Fロイドとエリィは、キーアが\x01",
            "思い出した方がウレシイの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_939F")

    label("loc_928C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9317")

    #C0340
    ChrTalk(
        0x153,
        (
            "#1106F#6Pんー……別にキーア、\x01",
            "思い出さなくってもいいけど。\x02\x03",

            "#1100Fロイドとティオは、キーアが\x01",
            "思い出した方がウレシイの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_939F")

    label("loc_9317")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_939F")

    #C0341
    ChrTalk(
        0x153,
        (
            "#1106F#6Pんー……別にキーア、\x01",
            "思い出さなくってもいいけど。\x02\x03",

            "#1100Fロイドとランディは、キーアが\x01",
            "思い出した方がウレシイの？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_939F")

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
            "#0002F#11Pあ、ああ……\x01",
            "そりゃもちろんさ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_947B")

    #C0343
    ChrTalk(
        0x102,
        (
            "#0104F#5Pきっと大切にしている\x01",
            "思い出も一杯あるはずよ。\x02\x03",

            "#0102Fだから頑張って\x01",
            "思い出してみましょう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9559")

    label("loc_947B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_94F4")

    #C0344
    ChrTalk(
        0x103,
        (
            "#0203F#5P……大切にしている\x01",
            "思い出だってあるはずです。\x02\x03",

            "#0202Fだから頑張って\x01",
            "思い出してみてください。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9559")

    label("loc_94F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9559")

    #C0345
    ChrTalk(
        0x104,
        (
            "#0306F#5P大切な思い出だって\x01",
            "一つや二つじゃねえだろ。\x02\x03",

            "#0300F取り戻さないでどうするよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9559")


    #C0346
    ChrTalk(
        0x153,
        (
            "#1104F#6Pんー、わかった。\x02\x03",

            "#1110Fキーア、がんばって\x01",
            "思い出してみるね！\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#0004F#11Pああ、その意気だ。\x02\x03",

            "#0000F……ただまあ、\x01",
            "無理はしなくていいからな？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x153,
        "#1109F#6Pうんっ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_966E")

    #C0349
    ChrTalk(
        0x102,
        (
            "#0102F#5Pふふ、それじゃあ\x01",
            "受付で『神経科』について\x01",
            "問い合わせてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9721")

    label("loc_966E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_96C9")

    #C0350
    ChrTalk(
        0x103,
        (
            "#0202F#5P……それでは受付で\x01",
            "『神経科』について\x01",
            "問い合わせてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9721")

    label("loc_96C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9721")

    #C0351
    ChrTalk(
        0x104,
        (
            "#0302F#5Pよし、そんじゃあ\x01",
            "受付で『神経科』について\x01",
            "問い合わせてみようぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9721")

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

    # Function_48_8D83 end

    def Function_49_978B(): pass

    label("Function_49_978B")

    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_97A1():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97A1)

    def lambda_97BB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_97BB)
    WaitChrThread(0xFE, 1)

    def lambda_97D0():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97D0)
    WaitChrThread(0xFE, 1)

    def lambda_97EE():
        OP_95(0xFE, -46150, 0, 30, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_97EE)
    WaitChrThread(0xFE, 1)

    def lambda_980C():
        OP_95(0xFE, -33950, 0, -50, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_980C)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_49_978B end

    def Function_50_982A(): pass

    label("Function_50_982A")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_9845():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9845)

    def lambda_985F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_985F)
    WaitChrThread(0xFE, 1)

    def lambda_9874():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9874)
    WaitChrThread(0xFE, 1)

    def lambda_9892():
        OP_95(0xFE, -47080, 0, -1280, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9892)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x10E, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_50_982A end

    def Function_51_98BC(): pass

    label("Function_51_98BC")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_98D7():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_98D7)

    def lambda_98F1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_98F1)
    WaitChrThread(0xFE, 1)

    def lambda_9906():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9906)
    WaitChrThread(0xFE, 1)

    def lambda_9924():
        OP_95(0xFE, -47530, 0, 180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9924)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0xE1, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_51_98BC end

    def Function_52_994E(): pass

    label("Function_52_994E")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -55990, 600, 1320, 270)

    def lambda_9969():
        OP_95(0xFE, -56010, 0, 4180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9969)

    def lambda_9983():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9983)
    WaitChrThread(0xFE, 1)

    def lambda_9998():
        OP_95(0xFE, -50520, 0, 3410, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9998)
    WaitChrThread(0xFE, 1)

    def lambda_99B6():
        OP_95(0xFE, -48510, 0, -1230, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99B6)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    OP_93(0xFE, 0x5A, 0x1F4)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_52_994E end

    def Function_53_99E0(): pass

    label("Function_53_99E0")


    def lambda_99E5():
        OP_95(0xFE, -56060, 0, 3950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_99E5)
    WaitChrThread(0xFE, 1)

    def lambda_9A03():
        OP_95(0xFE, -55990, 600, 1320, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_9A03)
    Sleep(1200)

    def lambda_9A20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_9A20)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_53_99E0 end

    def Function_54_9A35(): pass

    label("Function_54_9A35")

    Sleep(7000)
    ClearMapObjFlags(0x6, 0x10)
    OP_71(0x6, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x6)
    Return()

    # Function_54_9A35 end

    def Function_55_9A4E(): pass

    label("Function_55_9A4E")

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

    def lambda_9B4A():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B4A)
    Sleep(100)

    def lambda_9B62():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9B62)
    Sleep(150)

    def lambda_9B7A():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9B7A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    OP_0D()

    #N0352
    NpcTalk(
        0x1E,
        "女性の声",
        "あら……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xEF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x101,
        "#0002F#6Pあ……\x02",
    )

    CloseMessageWindow()
    OP_68(-14700, 1000, -500, 3000)
    OP_6F(0x1)
    Sleep(500)
    Fade(500)
    OP_68(-21000, 1000, -500, 0)
    SetCameraDistance(23000, 0)
    OP_98(0x1E, 0xFFFFE890, 0x0, 0x0, 0x0, 0x0)

    def lambda_9C4C():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_9C4C)

    def lambda_9C61():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9C61)
    Sleep(100)

    def lambda_9C79():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_9C79)
    Sleep(150)

    def lambda_9C91():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_9C91)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x153, 1)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0x1E, 1)
    OP_6F(0x1)
    OP_0D()

    #C0354
    ChrTalk(
        0x101,
        "#0000F#6Pセシル姉……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9D11")

    #C0355
    ChrTalk(
        0x102,
        (
            "#0102F#6Pセシルさん。\x01",
            "どうもお久しぶりです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9D83")

    label("loc_9D11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9D42")

    #C0356
    ChrTalk(
        0x103,
        "#0202F#6P……お久しぶりです。\x02",
    )

    CloseMessageWindow()
    Jump("loc_9D83")

    label("loc_9D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9D83")

    #C0357
    ChrTalk(
        0x104,
        (
            "#0309F#6Pおお、セシルさん！\x01",
            "どうもお久しぶりッス！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9D83")

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
            "ふふっ……\x01",
            "２人とも元気そうね。\x02\x03",

            "記念祭はお疲れさま。\x01",
            "色々忙しかったんでしょう？\x02",
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
            "#0012F#6Pはは……まあね。\x02\x03",

            "#0006F正直、とんでもなく\x01",
            "密度の濃い５日間だったよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_9EDD")

    #C0360
    ChrTalk(
        0x102,
        (
            "#0106F#6Pまたその後の１週間が\x01",
            "色々とあったんですけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F6C")

    label("loc_9EDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_9F27")

    #C0361
    ChrTalk(
        0x103,
        (
            "#0206F#6Pまたその後の１週間が\x01",
            "色々とあったんですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F6C")

    label("loc_9F27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_9F6C")

    #C0362
    ChrTalk(
        0x104,
        (
            "#0306F#6Pまたその後の１週間が\x01",
            "色々あったんスけどね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F6C")


    #C0363
    ChrTalk(
        0x1E,
        (
            "#1302F#11Pあら、その割には２人とも\x01",
            "疲れてはいなさそうだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0364
    ChrTalk(
        0x1E,
        "#1305F#11Pあら、その子は……\x02",
    )

    CloseMessageWindow()
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    def lambda_A002():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x153, 1, lambda_A002)
    WaitChrThread(0x153, 1)

    #C0365
    ChrTalk(
        0x153,
        (
            "#1110F#6Pねえねえ、ロイド。\x02\x03",

            "このおねえちゃんも\x01",
            "ロイドたちのシリアイ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A067():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A067)
    Sleep(50)

    def lambda_A077():
        TurnDirection(0xFE, 0x153, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A077)
    Sleep(300)

    #C0366
    ChrTalk(
        0x101,
        (
            "#0000F#11Pああ、そうだよ。\x02\x03",

            "セシル姉っていって\x01",
            "俺の姉さんみたいな\x01",
            "人なんだけど──\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x1E)
    Sleep(300)

    #C0367
    ChrTalk(
        0x1E,
        (
            "#1303F#11P#40W……そ、そんな……\x02\x03",

            "#1308F#40Wま、まさかロイドが\x01",
            "私に内緒で#2S……するなんて……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A149():
        TurnDirection(0xFE, 0x1E, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A149)

    def lambda_A156():
        TurnDirection(0xFE, 0x1E, 300)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_A156)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0368
    ChrTalk(
        0x101,
        "#0005F#6Pへ……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0369
    ChrTalk(
        0x1E,
        (
            "#1306F#11Pまさかロイドが私に内緒で\x01",
            "#4S結婚しちゃったなんて……！\x02",
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
        "#0011F#4S#6Pはああっ！？\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x1E,
        (
            "#1303F#11Pううん、隠さなくてもいいわ！\x02\x03",

            "#1301Fねえあなた。\x01",
            "お名前は何ていうの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x153,
        "#1110F#6Pキーアだよー。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A384")

    #C0373
    ChrTalk(
        0x1E,
        (
            "#1309F#11Pキーアちゃん……\x01",
            "ふふっ、可愛い名前ね。\x02\x03",

            "#1308Fロイドには似てないけど\x01",
            "お母さん似なのかしら……\x02\x03",

            "でも、エリィちゃんに\x01",
            "似ているわけでもないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x102,
        "#0112F#6Pあ、あの、セシルさん……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A521")

    label("loc_A384")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A456")

    #C0375
    ChrTalk(
        0x1E,
        (
            "#1309F#11Pキーアちゃん……\x01",
            "ふふっ、可愛い名前ね。\x02\x03",

            "#1308Fロイドには似てないけど\x01",
            "お母さん似なのかしら……\x02\x03",

            "でも、ティオちゃんに\x01",
            "似ているわけでもないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x103,
        "#0211F#6Pあの、セシルさん……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_A521")

    label("loc_A456")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A521")

    #C0377
    ChrTalk(
        0x1E,
        (
            "#1309F#11Pキーアちゃん……\x01",
            "ふふっ、可愛い名前ね。\x02\x03",

            "#1308Fロイドには似てないけど\x01",
            "お母さん似なのかしら……\x02\x03",

            "#1301Fひょっとしてランディ君の\x01",
            "連れ子だったり……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        "#0305F#6Pちょ、セシルさん？\x02",
    )

    CloseMessageWindow()

    label("loc_A521")


    #C0379
    ChrTalk(
        0x101,
        (
            "#0012F#6Pだあああっ！\x01",
            "落ち着いてくれよ！\x02\x03",

            "#0011F俺がキーアの父親って……\x01",
            "いくらなんでも年齢に\x01",
            "無理がありすぎるだろう！？\x02",
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
            "#1305F#11Pあら……\x02\x03",

            "#1309F……よく考えたら\x01",
            "それもそうかもしれないわね。\x02",
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
            "#0012F#6Pいや、考えるまでも\x01",
            "ないと思うんだけど……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_A6CC")

    #C0382
    ChrTalk(
        0x102,
        (
            "#0106F#6Pセシルさんって……\x01",
            "けっこう天然なんですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A755")

    label("loc_A6CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_A710")

    #C0383
    ChrTalk(
        0x103,
        (
            "#0206F#6Pセシルさん……\x01",
            "ここまで天然だったとは。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A755")

    label("loc_A710")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_A755")

    #C0384
    ChrTalk(
        0x104,
        (
            "#0309F#6Pセシルさん……\x01",
            "そんな天然なところも素敵だぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A755")


    #C0385
    ChrTalk(
        0x153,
        "#1105F#6Pほえ～？\x02",
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

    # Function_55_9A4E end

    def Function_56_A7AD(): pass

    label("Function_56_A7AD")

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

    def lambda_A8B2():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A8B2)

    def lambda_A8C7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_A8C7)
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
            "#1101F#11Pまったくもう、ロイドってば\x01",
            "ゼンゼンわかってないんだから。\x02\x03",

            "#1108F……キオクだってべつに\x01",
            "なくってもヘイキなのに……\x02\x03",

            "#1106Fどうしてみんな\x01",
            "そんなに気にするのかなー？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-1400, 1700, 530, 5000)

    def lambda_A9C2():
        OP_9B(0x0, 0xFE, 0x0, 0x7530, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_A9C2)
    Sleep(3000)
    Fade(1000)
    OP_68(-24820, 1700, -1120, 0)
    MoveCamera(46, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(29800, 0)
    SetCameraDistance(25490, 3500)
    EndChrThread(0x20, 0x1)
    SetChrPos(0x20, -17660, 0, -310, 270)

    def lambda_AA2B():
        OP_9B(0x0, 0xFE, 0x0, 0x189C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_AA2B)
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
            "#1105F#11Pあれれ……\x02\x03",

            "ここ、どこだろ？\x02\x03",

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
            "#1114F#5Pんー……\x02\x03",

            "#1101F……キーア、\x01",
            "まいごになっちゃった？\x02",
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
        "#1105F#5Pあ……\x02",
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
            "#1502F#5P……ふふ、いい風…………\x02\x03",

            "お父さん……\x01",
            "今日はいつ来るのかなぁ。\x02",
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
        "ねーねー！\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1F, 0x0, 0x190)
    OP_68(-23780, 0, -25230, 2500)

    def lambda_AC79():
        OP_95(0xFE, -23770, -1000, -24500, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_AC79)
    WaitChrThread(0x20, 1)

    #C0392
    ChrTalk(
        0x1F,
        "#1505F#12Pあなたは……\x02",
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x20,
        (
            "#1110F#5Pねー、なにが見えるの？\x02\x03",

            "#1109Fひょっとして\x01",
            "おサカナでも泳いでる！？\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x1F,
        (
            "#1500F#12Pふふっ……\x02\x03",

            "わたしには見えないけど\x01",
            "ちゃんと泳いでると思うよ？\x02\x03",

            "ときどきパシャって\x01",
            "跳ねる音がするから……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    MoveCamera(46, 14, 0, 1500)
    OP_68(-24970, 0, -26730, 1500)

    def lambda_ADB4():
        OP_95(0xFE, -24860, -1000, -26000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_ADB4)

    def lambda_ADCE():

        label("loc_ADCE")

        TurnDirection(0xFE, 0x20, 400)
        Yield()
        Jump("loc_ADCE")

    QueueWorkItem2(0x1F, 1, lambda_ADCE)
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
            "#1105F#5Pあ、ほんとだ！\x01",
            "いっぱいいるみたい！\x02\x03",

            "#1109Fうーん、キーアも\x01",
            "ツリってしてみたいなー。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x10E, 0x190)

    #C0396
    ChrTalk(
        0x1F,
        (
            "#1500F#11Pふふっ……\x01",
            "キーアちゃんていうんだ？\x02\x03",

            "わたしはシズク。\x01",
            "シズク・マクレインっていうの。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x5A, 0x1F4)
    Sleep(300)

    #C0397
    ChrTalk(
        0x20,
        (
            "#1111F#5Pシズク、シズク……\x02\x03",

            "#1109Fうん、いい名前だね！\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x1F,
        (
            "#1500F#11Pふふっ、ありがとう。\x02\x03",

            "キーアちゃんも\x01",
            "素敵な名前だと思うよ。\x02\x03",

            "ここにはお見舞いにきたの？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x20,
        (
            "#1105F#5Pあ、ううん。\x02\x03",

            "#1108Fキーアのキオクを\x01",
            "みてもらいにきたんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x1F,
        "#1505F#11Pきおく……？\x02",
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x20,
        (
            "#1101F#5Pあのメガネのセンセイが\x01",
            "ロイドたちと離れろとかいうから\x01",
            "キーア、にげてきちゃった。\x02\x03",

            "#1104Fふふん。\x01",
            "せんりゃくてきてったいってやつ？\x02",
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
            "#1508F#11P逃げてきちゃったって……\x02\x03",

            "#1505F（あれ、ロイドたちって\x01",
            "  もしかして……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x20,
        (
            "#1110F#5Pねえねえ、シズク。\x02\x03",

            "なんでさっきから\x01",
            "ずっと目をつぶってるのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x1F,
        (
            "#1500F#11Pあ、うん……\x02\x03",

            "わたし、目が見えなくて\x01",
            "それで入院してるから……\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x20,
        (
            "#1105F#5Pふーん、そうなんだ。\x02\x03",

            "#1100Fキーアもキオクがないし、\x01",
            "おあいこかもしれないねー。\x02",
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
            "#1505F#11Pあ……記憶……\x02\x03",

            "#1508Fそっか、そうなんだ……\x02\x03",

            "……なんにも覚えてないの？\x01",
            "お父さんとか、お母さんとか。\x02",
        )
    )

    CloseMessageWindow()

    #C0407
    ChrTalk(
        0x20,
        (
            "#1100F#5P……うん、そーみたい。\x02\x03",

            "#1109Fでも、ロイドたちがいるから\x01",
            "ゼンゼンさみしくないよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x1F,
        (
            "#1500F#11Pふふ、そっか……\x02\x03",

            "#1508F……わたしもお母さんは\x01",
            "いなくなっちゃったけど……\x02\x03",

            "#1510Fお父さんがいるし、\x01",
            "病院のみんなも優しいから\x01",
            "寂しくはないかな……？\x02",
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

    # Function_56_A7AD end

    def Function_57_B3B2(): pass

    label("Function_57_B3B2")

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
        "#0000F#5Pいた……！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B50C")

    #C0410
    ChrTalk(
        0x102,
        "#0102F#5Pやっと見つけた……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B56D")

    label("loc_B50C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B53F")

    #C0411
    ChrTalk(
        0x103,
        "#0202F#5Pやっと見つけました……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B56D")

    label("loc_B53F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B56D")

    #C0412
    ChrTalk(
        0x104,
        "#0300F#5Pここにいやがったか……\x02",
    )

    CloseMessageWindow()

    label("loc_B56D")

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
            "#1110F#5Pそれでね、それでね！\x02\x03",

            "ツァイトっていう犬が\x01",
            "とってもおーきいんだよ！\x02\x03",

            "なんかえらそーだけど\x01",
            "もふもふってしててねー。\x02\x03",

            "#1109F背中をかいてやると\x01",
            "きもちよさそーにしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x1F,
        (
            "#1500F#11Pふふっ、そうなんだ。\x02\x03",

            "#1502F大きな犬さん……\x01",
            "ふわふわなんだろうなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x20,
        (
            "#1110F#5Pシズクもたまに\x01",
            "マチに来るんだよねー？\x02\x03",

            "その時にいっしょに\x01",
            "ツァイトとあそぼーよ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x1F,
        (
            "#1500F#11Pあはは……うん。\x01",
            "お父さんに頼んでみようかな？\x02\x03",

            "#1505Fあ、エステルさんたちも\x01",
            "頼んだら付き合ってくれるかも……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x20, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0417
    ChrTalk(
        0x20,
        (
            "#1105F#5Pあ、エステルって\x01",
            "ゆーげきしのおねえちゃん？\x02\x03",

            "#1100Fシズクもしってるんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x1F,
        (
            "#1500F#11Pふふ、たまに街に出た時、\x01",
            "買物とかに付き合ってくれるの。\x02\x03",

            "お父さん、いつも忙しいから……\x02",
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
            "#0002F#5Pはは……\x01",
            "シズクちゃんと一緒だったか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_B94C")

    #C0420
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふ、何だかすごく\x01",
            "盛り上がってるみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9CD")

    label("loc_B94C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_B98E")

    #C0421
    ChrTalk(
        0x103,
        (
            "#0204F#5P……ずいぶんと\x01",
            "盛り上がっていますね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B9CD")

    label("loc_B98E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_B9CD")

    #C0422
    ChrTalk(
        0x104,
        (
            "#0309F#5Pしかし随分と\x01",
            "盛り上がってるみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B9CD")


    #N0423
    NpcTalk(
        0x21,
        "男の声",
        (
            "#4Pフ……\x01",
            "子供は馴染むのが早いな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BA37():
        OP_93(0xFE, 0x167, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA37)
    Sleep(50)

    def lambda_BA47():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_BA47)
    OP_68(-23930, 900, -14040, 5000)
    OP_A7(0x21, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_BA70():
        OP_95(0xFE, -23910, 0, -12470, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_BA70)
    WaitChrThread(0x21, 1)
    OP_6F(0x1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)

    #C0424
    ChrTalk(
        0x101,
        "#0005F#12Pア、アリオスさん……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BAF1")

    #C0425
    ChrTalk(
        0x102,
        "#0104F#12Pあの、その節はどうも……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BB4E")

    label("loc_BAF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BB21")

    #C0426
    ChrTalk(
        0x103,
        "#0204F#12Pその節はどうも……\x02",
    )

    CloseMessageWindow()
    Jump("loc_BB4E")

    label("loc_BB21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BB4E")

    #C0427
    ChrTalk(
        0x104,
        "#0303F#12Pその節はどうもッス。\x02",
    )

    CloseMessageWindow()

    label("loc_BB4E")


    #C0428
    ChrTalk(
        0x21,
        (
            "#1404F#5Pこの前の件を\x01",
            "借りに思う必要はない。\x02\x03",

            "#1400Fところで──\x01",
            "あの娘が例の……？\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x101,
        (
            "#0000F#12Pああ、ミシェルさんたちから\x01",
            "話を聞いたんですね。\x02\x03",

            "#0004Fええ……\x01",
            "キーアっていいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0430
    ChrTalk(
        0x21,
        (
            "#1405F#5Pそうか……\x02\x03",

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
            "#0005F#12Pえっと……\x01",
            "キーアがどうかしましたか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BCDC")

    #C0432
    ChrTalk(
        0x102,
        "#0101F#12Pまさか見覚えでも……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD3F")

    label("loc_BCDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BD10")

    #C0433
    ChrTalk(
        0x103,
        "#0201F#12Pまさか見覚えが……！？\x02",
    )

    CloseMessageWindow()
    Jump("loc_BD3F")

    label("loc_BD10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_BD3F")

    #C0434
    ChrTalk(
        0x104,
        "#0301F#12Pまさか見覚えが……！？\x02",
    )

    CloseMessageWindow()

    label("loc_BD3F")


    #C0435
    ChrTalk(
        0x21,
        (
            "#1402F#5Pいや……\x01",
            "不思議な娘だと思ってな。\x02\x03",

            "#1404F娘は──シズクは\x01",
            "行儀が良くて人当たりはいいが\x01",
            "どうも遠慮しがちな所がある。\x02\x03",

            "それで、同年代の子供とも\x01",
            "あまり馴染まなかったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0436
    ChrTalk(
        0x101,
        (
            "#0012F#12Pああ、なるほど。\x02\x03",

            "#0002F……なんだかすごく\x01",
            "楽しそうにしていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x21,
        "#1402F#5Pそうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x21)

    #C0438
    ChrTalk(
        0x21,
        (
            "#1403F#5P……あの娘にどのような\x01",
            "背景があるかは分からない。\x02\x03",

            "#1400Fだが、関わったからには\x01",
            "最後まで責任を持つことだ。\x02\x03",

            "#1404Fそして……\x01",
            "大事に慈#2Rいつく#しんでやるといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x101,
        (
            "#0005F#12Pあ……\x02\x03",

            "#0004Fはい、そのつもりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x1F,
        "#1505F#1P……お父さん？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_BFBB")

    #C0441
    ChrTalk(
        0x20,
        (
            "#1107F#1Pああっ……\x01",
            "ロイドにエリィ！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C02C")

    label("loc_BFBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_BFF5")

    #C0442
    ChrTalk(
        0x20,
        (
            "#1107F#1Pああっ……\x01",
            "ロイドにティオ！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C02C")

    label("loc_BFF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_C02C")

    #C0443
    ChrTalk(
        0x20,
        (
            "#1107F#1Pああっ……\x01",
            "ロイドにランディ！？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C02C")


    def lambda_C031():
        OP_93(0xFE, 0xB5, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C031)
    Sleep(50)

    def lambda_C041():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_C041)
    WaitChrThread(0x101, 1)

    #C0444
    ChrTalk(
        0x101,
        "#0012F#5P気付かれちゃったか……\x02",
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x21,
        "#1402F#5P……ふむ。\x02",
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

    def lambda_C122():

        label("loc_C122")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_C122")

    QueueWorkItem2(0x20, 2, lambda_C122)

    def lambda_C134():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C134)
    Sleep(50)

    def lambda_C14C():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_C14C)
    Sleep(50)

    def lambda_C164():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_C164)
    WaitChrThread(0xEF, 1)

    def lambda_C17D():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_C17D)
    WaitChrThread(0x101, 1)

    def lambda_C18E():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C18E)
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
            "#1500F#12Pお父さん、お帰りなさい。\x02\x03",

            "お仕事、大変だった？\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x21,
        (
            "#1404F#5Pいや……\x01",
            "今回はそうでもなかったな。\x02\x03",

            "#1402Fただいま、シズク。\x02",
        )
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x20,
        (
            "#1105F#6Pこのひと、\x01",
            "シズクのおとうさん？\x02\x03",

            "#1110Fすっごく背が高いねー。\x02\x03",

            "#1109Fそれになんかつよそー！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1F, 0x10E, 0x190)

    #C0449
    ChrTalk(
        0x1F,
        "#1502F#11Pえへへ……そう？\x02",
    )

    CloseMessageWindow()
    OP_63(0x1F, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_C2DE():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_C2DE)
    Sleep(150)

    def lambda_C2EE():
        OP_93(0xFE, 0xE1, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_C2EE)
    Sleep(150)

    #C0450
    ChrTalk(
        0x1F,
        (
            "#1500F#12Pロイドさんたちも……\x01",
            "こんにちは、お久しぶりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x101,
        "#0002F#5Pああ、お久しぶり。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_C3A9")

    #C0452
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふっ、キーアちゃんと\x01",
            "仲良くしてくれたみたいね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C430")

    label("loc_C3A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_C3ED")

    #C0453
    ChrTalk(
        0x103,
        (
            "#0202F#5Pキーアと仲良く\x01",
            "してくれたみたいですね？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C430")

    label("loc_C3ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_C430")

    #C0454
    ChrTalk(
        0x104,
        (
            "#0309F#5Pはは、キー坊と仲良く\x01",
            "してくれたみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C430")


    #C0455
    ChrTalk(
        0x1F,
        (
            "#1502F#12Pあ、いえ、わたしの方こそ\x01",
            "仲良くしてもらっちゃって。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x20, 0x0, 0x1F4)
    Sleep(150)

    #C0456
    ChrTalk(
        0x20,
        (
            "#1103F#12P……ところでロイド。\x02\x03",

            "#1101Fキーア、ぜったいに\x01",
            "ここに泊まらないんだからね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        (
            "#0006F#5Pああ、それはもう分かったよ。\x02\x03",

            "#0002Fあ、でも……\x01",
            "ここに泊まればシズクちゃんと\x01",
            "一緒にいられるかもしれないぞ？\x02\x03",

            "仲良くなったみたいじゃないか。\x02",
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
            "#1110F#12Pホントー！？\x02\x03",

            "#1108Fあ、でも……やっぱり\x01",
            "ロイドたちと離れるのは……\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x1F,
        (
            "#1508F#12Pもう、ロイドさん……\x01",
            "イジワル言っちゃ駄目です。\x02\x03",

            "キーアちゃん、困ってますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        (
            "#0012F#5Pはは、そうだな。\x02\x03",

            "#0000Fゴメン、キーア。\x01",
            "今日はそろそろ帰ろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0461
    ChrTalk(
        0x20,
        (
            "#1112F#12Pえー、でもシズクと\x01",
            "もうちょっと話したいなー。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_C747")

    #C0462
    ChrTalk(
        0x102,
        (
            "#0104F#5Pふふ、また遊びに来ればいいわ。\x02\x03",

            "#0100Fシズクちゃんが街に来た時に\x01",
            "遊びに来てもらうのもいいし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C83E")

    label("loc_C747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_C7C3")

    #C0463
    ChrTalk(
        0x103,
        (
            "#0204F#5P……また遊びに来るといいです。\x02\x03",

            "#0202Fシズクさんが街に来た時に\x01",
            "遊びに来てもらうのもいいですし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C83E")

    label("loc_C7C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_C83E")

    #C0464
    ChrTalk(
        0x104,
        (
            "#0304F#5Pハハ、また遊びに来りゃいいだろ。\x02\x03",

            "#0300Fシズクちゃんが街に来た時に\x01",
            "遊びに来てもらったっていいしな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C83E")


    #C0465
    ChrTalk(
        0x20,
        "#1110F#12Pんー、そっか。\x02",
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x21,
        (
            "#1404F#5Pフフ……\x01",
            "その時はどうかよろしく頼む。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0xB4, 0x1F4)
    Sleep(300)

    #C0467
    ChrTalk(
        0x21,
        "#1402F#5P──シズク、抱き上げるぞ。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x1F,
        "#1500F#12Pあ、うん……！\x02",
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

    def lambda_C926():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C926)
    Sleep(50)

    def lambda_C936():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_C936)
    Sleep(50)

    def lambda_C946():
        TurnDirection(0xFE, 0x21, 500)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_C946)
    Sleep(300)

    #C0469
    ChrTalk(
        0x101,
        (
            "#0000F#5Pアリオスさんは、\x01",
            "今日はこちらの方に？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0xEF, 400)
    Sleep(150)

    #C0470
    ChrTalk(
        0x21,
        "#1404F#11Pああ、一泊するつもりだ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x21, 0xE1, 0x190)
    Sleep(300)

    #C0471
    ChrTalk(
        0x21,
        (
            "#1402F#11P──キーア。\x01",
            "今後もシズクと仲良くしてくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x20,
        (
            "#1109F#6Pうんっ！\x02\x03",

            "#1110Fシズク、またねー！\x02",
        )
    )

    CloseMessageWindow()

    #N0473
    NpcTalk(
        0x21,
        "シズク",
        (
            "#1502F#5Pうん……！\x01",
            "キーアちゃんもまたね！\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    OP_93(0x21, 0x0, 0x190)
    Sleep(300)
    OP_68(-24710, 200, -23040, 5000)

    def lambda_CA8E():

        label("loc_CA8E")

        TurnDirection(0x101, 0x21, 500)
        Yield()
        Jump("loc_CA8E")

    QueueWorkItem2(0x101, 1, lambda_CA8E)

    def lambda_CAA0():

        label("loc_CAA0")

        TurnDirection(0xEF, 0x21, 500)
        Yield()
        Jump("loc_CAA0")

    QueueWorkItem2(0xEF, 1, lambda_CAA0)

    def lambda_CAB2():

        label("loc_CAB2")

        TurnDirection(0x20, 0x21, 500)
        Yield()
        Jump("loc_CAB2")

    QueueWorkItem2(0x20, 1, lambda_CAB2)

    def lambda_CAC4():
        OP_95(0xFE, -23810, 0, -9390, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_CAC4)
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

    def lambda_CB28():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB28)
    Sleep(50)

    def lambda_CB38():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_CB38)
    OP_93(0x20, 0x0, 0x1F4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0xEF, 1)
    OP_6F(0x79)

    #C0474
    ChrTalk(
        0x101,
        (
            "#0002F#5Pさてと……\x01",
            "俺たちもそろそろ帰るか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_CBC5")

    #C0475
    ChrTalk(
        0x102,
        (
            "#0102F#5Pふふ、そうね。\x01",
            "いつの間にか夕方だし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC42")

    label("loc_CBC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_CC09")

    #C0476
    ChrTalk(
        0x103,
        (
            "#0202F#5Pそうですね……\x01",
            "いつの間にか夕方ですし。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CC42")

    label("loc_CC09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_CC42")

    #C0477
    ChrTalk(
        0x104,
        (
            "#0302F#5Pそうだな。\x01",
            "いつの間にか夕方だし。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CC42")


    #C0478
    ChrTalk(
        0x20,
        (
            "#1105F#12Pそーいえば……\x01",
            "わぁ、お空がマッカだねー！\x02\x03",

            "#1109Fキーア、おなか空いちゃった！\x02\x03",

            "#1110F今日のバンゴハンはなにかなー？\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        (
            "#0012F#5Pはは……\x01",
            "ほんと、キーアは元気だな。\x02\x03",

            "#0000Fそれじゃ、セシル姉に挨拶して\x01",
            "帰りのバスに乗ろうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x20,
        "#1109F#12Pうんっ！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(23550, 3000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_CD91")
    RemoveParty(0x1, 0x0)
    Jump("loc_CDAE")

    label("loc_CD91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_CDA2")
    RemoveParty(0x2, 0x0)
    Jump("loc_CDAE")

    label("loc_CDA2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_CDAE")
    RemoveParty(0x3, 0x0)

    label("loc_CDAE")

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

    # Function_57_B3B2 end

    def Function_58_CDD6(): pass

    label("Function_58_CDD6")

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

    def lambda_CE5D():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CE5D)
    Sleep(50)

    def lambda_CE75():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CE75)
    Sleep(50)

    def lambda_CE8D():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_CE8D)
    Sleep(50)

    def lambda_CEA5():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CEA5)
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
            "#0001F#6Pさてと、ヨアヒム先生の時間が\x01",
            "空いているか確かめないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x102,
        (
            "#0100F#5Pええ。\x01",
            "まずは受付に行きましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        (
            "#0306F#5Pまた釣りとかに\x01",
            "行ってなきゃいいんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x103,
        "#0211F#6P……ありそうですね。\x02",
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

    # Function_58_CDD6 end

    def Function_59_CFD2(): pass

    label("Function_59_CFD2")

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

    def lambda_D074():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D074)
    Sleep(50)

    def lambda_D08C():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D08C)
    Sleep(50)

    def lambda_D0A4():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D0A4)
    Sleep(50)

    def lambda_D0BC():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D0BC)
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
            "#0302F#6Pさてと、もう夕方だし\x01",
            "バスでとっとと帰るとすっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x101,
        "#0002F#11Pそうだな……\x02",
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x102,
        (
            "#0102F#11Pふふ、こういう時に\x01",
            "やっぱりバスは有難いわね。\x02",
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

    def lambda_D201():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D201)

    def lambda_D20E():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D20E)
    Sleep(100)

    def lambda_D21E():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D21E)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0489
    ChrTalk(
        0x101,
        "#0005F#6Pティオ……？\x02",
    )

    CloseMessageWindow()

    #C0490
    ChrTalk(
        0x104,
        (
            "#0305F#6Pなんだティオすけ。\x01",
            "さっきから妙に静かだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x103,
        "#0206F#11P#60W……別にそんな事は。\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_D2D1():
        OP_9B(0x0, 0xFE, 0x0, 0x352, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D2D1)
    WaitChrThread(0x102, 1)

    #C0492
    ChrTalk(
        0x102,
        (
            "#0101F#5Pティオちゃん……！？\x02\x03",

            "夕陽で分かりにくいけど……\x01",
            "あなた、顔が真っ青よ！？\x02",
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
        "#0011F#6Pえっ！？\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x103,
        (
            "#0202F#11P#50W……問題ありません。\x01",
            "少し気分が優れないだけで……\x02",
        )
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x104,
        (
            "#0306F#6Pおいおい。\x01",
            "問題ないじゃねーだろ。\x02\x03",

            "#0301Fとにかくどこか\x01",
            "休めるところでも──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x1770)

    #C0496
    ChrTalk(
        0x103,
        "#0206F#11P#60W……ぁ………\x02",
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
        "#0007F#6Pティオ！？\x02",
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x102,
        "#0101F#5Pた、大変……！\x02",
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
            "#0307F#6Pすぐに医者か\x01",
            "看護師を呼んでくる！\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x101,
        "#0007F#5Pああ……頼む！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 60)
    Sleep(300)
    OP_68(-48210, 1300, -210, 2000)

    def lambda_D59F():
        OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D59F)
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

    # Function_59_CFD2 end

    def Function_60_D5EC(): pass

    label("Function_60_D5EC")

    OP_95(0xFE, -49190, 0, 2050, 5000, 0x0)
    OP_95(0xFE, -35480, 0, 180, 5000, 0x0)
    Return()

    # Function_60_D5EC end

    def Function_61_D615(): pass

    label("Function_61_D615")

    OP_A1(0xFE, 0x3E8, 0x4, 0x2, 0x3, 0x4, 0x3)
    Return()

    # Function_61_D615 end

    def Function_62_D620(): pass

    label("Function_62_D620")

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
        "#11P……最近どうも疲れがでていてね。\x02",
    )

    CloseMessageWindow()

    #C0503
    ChrTalk(
        0x17,
        (
            "#11P看護師のシロンくんに\x01",
            "備品の発注を頼んだら\x01",
            "別のものが送られてくるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0504
    ChrTalk(
        0x17,
        (
            "#11P息子のキーンツも\x01",
            "相変わらず不良グループから\x01",
            "抜ける気配はない……\x02",
        )
    )

    CloseMessageWindow()

    #C0505
    ChrTalk(
        0x17,
        (
            "#11P教授というものも\x01",
            "なかなか大変だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x101,
        (
            "#6P#0005F（この病院の教授さんか……\x01",
            "  ずいぶんくたびれてるな。）\x02\x03",

            "#0003F（でも、教授さんなら\x01",
            "  プレゼントの材料に\x01",
            "  心当たりがあるかもしれない。）\x02\x03",

            "#0000Fあの、ちょっと\x01",
            "お聞きしたいんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x17,
        "#11P……ふむ、何かね？\x02",
    )

    CloseMessageWindow()

    #A0508
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは、プレゼントの材料集めを\x01",
            "していることを説明した。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0509
    ChrTalk(
        0x101,
        (
            "#6P#0000F……と、いうわけで、\x01",
            "何かよさそうな物を探してるんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x17,
        "#11Pシズク君か……ふむ。\x02",
    )

    CloseMessageWindow()

    #C0511
    ChrTalk(
        0x17,
        (
            "#11Pそういう話なら、あそこになら\x01",
            "何かあるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0512
    ChrTalk(
        0x103,
        (
            "#6P#0200Fあそこ……\x01",
            "何か心当たりが？\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x17,
        (
            "#11Pああ……この病院には、\x01",
            "大量の輸入雑貨が\x01",
            "放置されているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0514
    ChrTalk(
        0x17,
        (
            "#11Pそれもほとんど手付かずの\x01",
            "状態でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0515
    ChrTalk(
        0x102,
        (
            "#5P#0105F輸入雑貨って……\x01",
            "なんでそんなものが病院に……？\x02",
        )
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x17,
        (
            "#11P以前、看護師のシロンくんに\x01",
            "外科手術用のメスやらなにやらの\x01",
            "発注を頼んだんだがね。\x02",
        )
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x17,
        (
            "#11P医療器具の代わりに届いたのが\x01",
            "何故かそれらの雑貨だったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0518
    ChrTalk(
        0x17,
        (
            "#11Pなんでそんなことになったか……\x01",
            "私が聞きたいくらいだよ。\x02",
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
        "#6P#0300Fなんか苦労してるんスね。\x02",
    )

    CloseMessageWindow()

    #C0520
    ChrTalk(
        0x109,
        (
            "#6P#0506Fなんだか、司令に悩まされる\x01",
            "私たちも他人事じゃない感じです……\x02",
        )
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x101,
        (
            "#6P#0000Fえ、えっとそれじゃあ……\x01",
            "そこから何かいただいても？\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x17,
        (
            "#11Pああ、構わんよ。\x01",
            "正直処分に困っていたくらいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x17,
        (
            "#11P雑貨の入ったコンテナは\x01",
            "寮の２階、男性職員寮を抜けた先の\x01",
            "テラスに置いてある。\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x17,
        (
            "#11P良さそうなものがあったら\x01",
            "適当に見繕って\x01",
            "持って行ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x101,
        (
            "#6P#0000Fはい、ありがとうございます。\x02\x03",

            "#0003F（２階のテラスっていうと……\x01",
            "  狼型魔獣の事件の時に\x01",
            "  フェンスを設置したあそこだな。）\x02",
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

    # Function_62_D620 end

    def Function_63_DE2C(): pass

    label("Function_63_DE2C")

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
            "#6P#0000F教授の言っていたコンテナは\x01",
            "これみたいだな。\x02\x03",

            "それじゃ、\x01",
            "ちょっと調べてみようか。\x02",
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
            "#5P#0505Fどうですか？\x01",
            "何かよさそうな物は……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x13B, 0x1F4)

    #C0528
    ChrTalk(
        0x101,
        "#12P#0000Fああ、こんなのがあったよ。\x02",
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x102,
        (
            "#6P#0105Fまぁ……皮製の編み紐？\x02\x03",

            "#0100Fかなり頑丈に\x01",
            "作られているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x103,
        (
            "#6P#0200F……他には何か\x01",
            "なかったのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0531
    ChrTalk(
        0x101,
        (
            "#12P#0006Fう、うーん、\x01",
            "一通り見てみたけど……\x02\x03",

            "謂れもわからないような\x01",
            "奇妙な置物とか、\x01",
            "魔除けの人形ばかりでさ。\x02\x03",

            "#0000F正直、この編み紐以外に\x01",
            "良さそうなものは\x01",
            "見当たらなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x104,
        (
            "#11P#0306Fま、あのセンセイも\x01",
            "処分に困ってたらしいしな。\x02\x03",

            "#0300F一個でも使えそうなものが\x01",
            "見つかってラッキーってとこか。\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x343),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x343, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E27A")

    #C0534
    ChrTalk(
        0x101,
        (
            "#12P#0003F（この頑丈な編み紐なら\x01",
            "  アリオスさんが使っても\x01",
            "  千切れないだろうし……）\x02\x03",

            "（あとはシズクちゃんの持っている石を\x01",
            "  はめるためのペンダントトップが\x01",
            "  あればよさそうだ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E27A")

    OP_29(0x2C, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x0)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2C, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E34D")
    OP_29(0x2C, 0x1, 0x5)

    #C0535
    ChrTalk(
        0x101,
        (
            "#12P#0000F（プレゼントの材料になりそうな物も揃ったし\x01",
            "  包装用の箱とリボンも手に入ったな……）\x02\x03",

            "（よし、そろそろシズクちゃんの所に\x01",
            "  持っていってあげよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E34D")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -37600, 3000, 16800, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_65(0x8, 0x1)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_63_DE2C end

    def Function_64_E37D(): pass

    label("Function_64_E37D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E49B")

    #C0536
    ChrTalk(
        0x101,
        (
            "#0001Fこっちは街道の方だ……\x02\x03",

            "#0003Fさすがにセシル姉を\x01",
            "連れては行けないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x62, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E445")

    #C0537
    ChrTalk(
        0x136,
        (
            "#1300Fふふ、魔獣騒ぎの\x01",
            "調査だったわよね。\x02\x03",

            "付いてきて。\x01",
            "病院棟の２階に案内するわ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E49B")

    label("loc_E445")


    #C0538
    ChrTalk(
        0x136,
        (
            "#1300Fふふ、魔獣騒ぎの\x01",
            "調査だったわよね。\x02\x03",

            "現場は病院棟の屋上よ。\x01",
            "案内するわね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E49B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E4F8")

    #C0539
    ChrTalk(
        0x101,
        (
            "#0000Fこっちは街道の方だ……\x02\x03",

            "#0003F帰る前にセシル姉に\x01",
            "報告をしないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E4F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x63, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E566")

    #C0540
    ChrTalk(
        0x101,
        (
            "#0000Fもう夕方だし、\x01",
            "帰りはバスを使おう。\x02\x03",

            "バス停を調べれば\x01",
            "次のバスの時刻が分かるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E566")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E5E9")

    #C0541
    ChrTalk(
        0x101,
        (
            "#0000Fおっと……\x01",
            "せっかく来たんだし、\x01",
            "病院で相談してみないとな。\x02\x03",

            "受付で『神経科』について\x01",
            "問い合わせてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E5E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E66D")

    #C0542
    ChrTalk(
        0x101,
        (
            "#0003Fキーアを連れて\x01",
            "街道に出るわけにはいかない……\x02\x03",

            "#0000Fそれにヨアヒム先生に\x01",
            "記憶について相談してみないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E66D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA8, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E726")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6E7")

    #C0543
    ChrTalk(
        0x101,
        (
            "#0003F……キーアは多分、\x01",
            "病院の敷地内にいるはずだ。\x02\x03",

            "#0001F早いところ探し出さないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E726")

    label("loc_E6E7")


    #C0544
    ChrTalk(
        0x101,
        (
            "#0001F早くキーアを探し出そう。\x01",
            "病院の敷地内にいるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E726")

    Sleep(50)
    SetChrPos(0x0, -61000, 0, 0, 90)
    EventEnd(0x4)
    Return()

    # Function_64_E37D end

    def Function_65_E73D(): pass

    label("Function_65_E73D")

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

    # Function_65_E73D end

    def Function_66_E790(): pass

    label("Function_66_E790")

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
            "～オーベルジュ《レクチェ》～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_66_E790 end

    SaveToFile()

Try(main)
