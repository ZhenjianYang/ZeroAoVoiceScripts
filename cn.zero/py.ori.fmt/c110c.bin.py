from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c110c.bin",                # FileName
        "c110c",                    # MapName
        "c110c",                    # Location
        0x0016,                     # MapIndex
        "ed7100",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 22, 0, 2, 0, 3],
    )

    BuildStringList((
        "c110c",                  # 0
        "弗兰茨巡警",             # 1
        "夏娜",                   # 2
        "亚比",                   # 3
        "库罗玛",                 # 4
        "奥特",                   # 5
        "塔基库",                 # 6
        "迪利克",                 # 7
        "席莉",                   # 8
        "多诺邦警督",             # 9
        "雷蒙德搜查官",           # 10
        "乔里基科长",             # 11
        "阿蕾莎",                 # 12
        "史蒂芬",                 # 13
        "警官",                   # 14
        "赛尔盖科长",             # 15
        "凯特巡警 ",              # 16
        "格蕾丝",                 # 17
        "雷因兹",                 # 18
        "艾丝蒂尔",               # 19
        "约修亚",                 # 20
        "游击士林",               # 21
        "游击士艾欧莉娅",         # 22
        "游客",                   # 23
        "游客",                   # 24
        "游客",                   # 25
        "游客",                   # 26
        "警官",                   # 27
        "哈罗德",                 # 28
        "索菲亚",                 # 29
        "蔡特",                   # 30
        "客人",                   # 31
        "客人",                   # 32
        "中央广场",               # 33
        "西街",                   # 34
        "行政区",                 # 35
        "住宅街",                 # 36
        "欢乐街",                 # 37
        "东街",                   # 38
        "旧城区",                 # 39
        "港湾区",                 # 40
        "ＩＢＣ",                 # 41
        "站前街道",               # 42
        "后巷",                   # 43
        "乌尔斯拉间道",           # 44
        "东克洛斯贝尔街道",       # 45
        "西克洛斯贝尔街道",       # 46
        "玛因兹山道",             # 47
    ))

    AddCharChip((
        "chr/ch30000.itc",                   # 00
        "chr/ch20300.itc",                   # 01
        "chr/ch20600.itc",                   # 02
        "chr/ch20800.itc",                   # 03
        "chr/ch28100.itc",                   # 04
        "chr/ch32300.itc",                   # 05
        "chr/ch24900.itc",                   # 06
        "chr/ch30300.itc",                   # 07
        "chr/ch30200.itc",                   # 08
        "chr/ch30100.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch20000.itc",                   # 0B
        "chr/ch20100.itc",                   # 0C
        "chr/ch23400.itc",                   # 0D
        "chr/ch23500.itc",                   # 0E
        "chr/ch30600.itc",                   # 0F
        "chr/ch09300.itc",                   # 10
        "chr/ch09402.itc",                   # 11
        "chr/ch06000.itc",                   # 12
        "chr/ch02500.itc",                   # 13
        "chr/ch00602.itc",                   # 14
        "chr/ch00702.itc",                   # 15
        "chr/ch32000.itc",                   # 16
        "chr/ch32100.itc",                   # 17
        "chr/ch24500.itc",                   # 18
        "chr/ch22700.itc",                   # 19
        "chr/ch34200.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(-15050,  2500,    27399,   180,  389,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(23239,   2500,    -6429,   270,  261,  0x0, 0,   1,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(23340,   2500,    -7389,   270,  261,  0x0, 0,   26,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(6929,    2490,    -6650,   225,  261,  0x0, 0,   6,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(8369,    2390,    -14850,  90,   261,  0x0, 0,   3,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(-8739,   2500,    6070,    180,  389,  0x0, 0,   4,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(-11430,  2500,    10270,   190,  261,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-13659,  2500,    10739,   190,  261,  0x0, 0,   24,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(-5829,   2500,    27989,   359,  389,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-4250,   2500,    27879,   359,  389,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-6500,   2500,    30750,   359,  405,  0x0, 0,   9,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-14069,  2500,    6230,    360,  389,  0x0, 0,   25,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-15340,  2500,    6219,    360,  389,  0x0, 0,   2,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(2450,    2500,    13770,   142,  389,  0x0, 0,   0,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(-3559,   2500,    25170,   270,  389,  0x0, 0,   19,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(-4869,   2500,    30729,   270,  389,  0x0, 0,   15,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-8229,   2500,    26780,   45,   389,  0x0, 0,   18,  0,   0,   0,   0,   29,  255,  0)
    DeclNpc(-9369,   2500,    27190,   45,   389,  0x0, 0,   4,   0,   0,   0,   0,   30,  255,  0)
    DeclNpc(-3630,   2500,    -12920,  180,  469,  0x0, 0,   20,  0,   255, 255, 0,   31,  255,  0)
    DeclNpc(-4769,   2500,    -12920,  180,  469,  0x0, 0,   21,  0,   255, 255, 0,   32,  255,  0)
    DeclNpc(1470,    2500,    -12529,  0,    389,  0x0, 0,   22,  0,   0,   0,   0,   33,  255,  0)
    DeclNpc(1870,    2500,    -10829,  225,  389,  0x0, 0,   23,  0,   0,   0,   0,   34,  255,  0)
    DeclNpc(-9420,   2500,    -11609,  45,   261,  0x0, 0,   11,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(-10239,  2500,    -10750,  45,   261,  0x0, 0,   12,  0,   0,   0,   0,   25,  255,  0)
    DeclNpc(14340,   2500,    4010,    112,  261,  0x0, 0,   13,  0,   0,   0,   0,   26,  255,  0)
    DeclNpc(15750,   2500,    3609,    292,  261,  0x0, 0,   14,  0,   0,   0,   0,   27,  255,  0)
    DeclNpc(3329,    2500,    12640,   322,  389,  0x0, 0,   0,   0,   0,   0,   0,   28,  255,  0)
    DeclNpc(-17799,  2500,    800,     180,  389,  0x0, 0,   16,  0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-17219,  2599,    -400,    270,  468,  0x0, 0,   17,  0,   255, 255, 0,   5,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-5890,   2500,    31840,   1200,    -5890,   4000,    31840,   0x007C, 0,  46, 0x0000)
    DeclActor(16550,   2410,    10660,   1200,    16550,   3910,    10660,   0x007C, 0,  47, 0x0000)

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "中央广场")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "西街")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "行政区")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "住宅街")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "欢乐街")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "东街")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "旧城区")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "港湾区")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "站前街道")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "后巷")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-60.130001068115234, 0.0, -126.0999984741211, 0x0000, 0x0051, "")
    PlaceName(9.75, 0.0, -92.30000305175781, 0x0000, 0x0054, "")
    PlaceName(-28.280000686645508, 0.0, -136.5, 0x0000, 0x0057, "")
    PlaceName(-61.099998474121094, 0.0, -88.4000015258789, 0x0000, 0x0053, "")
    PlaceName(-34.45000076293945, 0.0, -57.20000076293945, 0x0000, 0x0053, "")
    PlaceName(-100.43000030517578, 0.0, -94.9000015258789, 0x0000, 0x0053, "")
    PlaceName(-113.0999984741211, 0.0, -67.5999984741211, 0x0000, 0x0053, "")
    PlaceName(-81.9000015258789, 0.0, -26.0, 0x0000, 0x0052, "")
    PlaceName(-75.7300033569336, 0.0, -42.900001525878906, 0x0000, 0x0053, "")
    PlaceName(-64.3499984741211, 0.0, -53.95000076293945, 0x0000, 0x0053, "")
    PlaceName(-27.299999237060547, 0.0, 38.349998474121094, 0x0000, 0x0051, "")
    PlaceName(118.30000305175781, 0.0, -137.8000030517578, 0x0000, 0x0052, "")
    PlaceName(96.19999694824219, 0.0, -255.4499969482422, 0x0000, 0x0053, "")
    PlaceName(79.30000305175781, 0.0, -231.39999389648438, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_7D8",          # 00, 0
        "Function_1_890",          # 01, 1
        "Function_2_969",          # 02, 2
        "Function_3_DB1",          # 03, 3
        "Function_4_EF4",          # 04, 4
        "Function_5_EF8",          # 05, 5
        "Function_6_EFC",          # 06, 6
        "Function_7_107A",         # 07, 7
        "Function_8_131C",         # 08, 8
        "Function_9_137B",         # 09, 9
        "Function_10_147C",        # 0A, 10
        "Function_11_198E",        # 0B, 11
        "Function_12_1D95",        # 0C, 12
        "Function_13_1EC3",        # 0D, 13
        "Function_14_26B9",        # 0E, 14
        "Function_15_2D31",        # 0F, 15
        "Function_16_2EAF",        # 10, 16
        "Function_17_31E8",        # 11, 17
        "Function_18_32A2",        # 12, 18
        "Function_19_3350",        # 13, 19
        "Function_20_349B",        # 14, 20
        "Function_21_355F",        # 15, 21
        "Function_22_36FF",        # 16, 22
        "Function_23_3762",        # 17, 23
        "Function_24_3965",        # 18, 24
        "Function_25_3AFD",        # 19, 25
        "Function_26_3C8A",        # 1A, 26
        "Function_27_3E35",        # 1B, 27
        "Function_28_401E",        # 1C, 28
        "Function_29_40E2",        # 1D, 29
        "Function_30_4394",        # 1E, 30
        "Function_31_4437",        # 1F, 31
        "Function_32_45BE",        # 20, 32
        "Function_33_4768",        # 21, 33
        "Function_34_48FE",        # 22, 34
        "Function_35_496A",        # 23, 35
        "Function_36_4D5A",        # 24, 36
        "Function_37_500A",        # 25, 37
        "Function_38_6747",        # 26, 38
        "Function_39_6766",        # 27, 39
        "Function_40_67B0",        # 28, 40
        "Function_41_69C5",        # 29, 41
        "Function_42_78A4",        # 2A, 42
        "Function_43_78B9",        # 2B, 43
        "Function_44_7DF6",        # 2C, 44
        "Function_45_83DB",        # 2D, 45
        "Function_46_8401",        # 2E, 46
        "Function_47_847B",        # 2F, 47
    ))


    def Function_0_7D8(): pass

    label("Function_0_7D8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_818"),
        (1, "loc_824"),
        (2, "loc_830"),
        (3, "loc_83C"),
        (4, "loc_848"),
        (5, "loc_854"),
        (6, "loc_860"),
        (SWITCH_DEFAULT, "loc_86C"),
    )


    label("loc_818")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_824")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_830")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_83C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_848")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_854")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_860")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_86C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_878")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_88F")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_878")

    label("loc_88F")

    Return()

    # Function_0_7D8 end

    def Function_1_890(): pass

    label("Function_1_890")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_968")
    OP_95(0xFE, 17250, 2500, -14850, 1000, 0x0)
    OP_95(0xFE, 17250, 2500, -70, 1000, 0x0)
    OP_95(0xFE, 3810, 2500, 8270, 1000, 0x0)
    OP_95(0xFE, -6210, 2500, 23860, 1000, 0x0)
    OP_95(0xFE, -18440, 2500, 23260, 1000, 0x0)
    OP_95(0xFE, -20840, 2450, 19170, 1000, 0x0)
    OP_95(0xFE, -19000, 2500, 6490, 1000, 0x0)
    OP_95(0xFE, -19000, 2500, -3620, 1000, 0x0)
    OP_95(0xFE, -8180, 2500, -14970, 1000, 0x0)
    OP_95(0xFE, 8370, 2390, -14850, 1000, 0x0)
    Jump("Function_1_890")

    label("loc_968")

    Return()

    # Function_1_890 end

    def Function_2_969(): pass

    label("Function_2_969")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B9B")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A34")
    SetChrPos(0x0, 30170, 2500, -90, 270)
    SetChrPos(0x1, 30170, 2500, -90, 270)
    SetChrPos(0x2, 30170, 2500, -90, 270)
    SetChrPos(0x3, 30170, 2500, -90, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A07")
    SetChrPos(0x4, 30170, 2500, -90, 270)
    SetChrPos(0x5, 30170, 2500, -90, 270)
    Jump("loc_A26")

    label("loc_A07")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A26")
    SetChrPos(0x4, 30170, 2500, -90, 270)

    label("loc_A26")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B9B")

    label("loc_A34")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_AFA")
    SetChrPos(0x0, -40390, 0, 24150, 90)
    SetChrPos(0x1, -40390, 0, 24150, 90)
    SetChrPos(0x2, -40390, 0, 24150, 90)
    SetChrPos(0x3, -40390, 0, 24150, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_ACD")
    SetChrPos(0x4, -40390, 0, 24150, 90)
    SetChrPos(0x5, -40390, 0, 24150, 90)
    Jump("loc_AEC")

    label("loc_ACD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AEC")
    SetChrPos(0x4, -40390, 0, 24150, 90)

    label("loc_AEC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_B9B")

    label("loc_AFA")

    SetChrPos(0x0, 19940, 0, -37920, 0)
    SetChrPos(0x1, 19940, 0, -37920, 0)
    SetChrPos(0x2, 19940, 0, -37920, 0)
    SetChrPos(0x3, 19940, 0, -37920, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B73")
    SetChrPos(0x4, 19940, 0, -37920, 0)
    SetChrPos(0x5, 19940, 0, -37920, 0)
    Jump("loc_B92")

    label("loc_B73")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B92")
    SetChrPos(0x4, 19940, 0, -37920, 0)

    label("loc_B92")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_B9B")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_BD9")
    ClearChrFlags(0x8, 0x80)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x20, 0x10)
    SetChrFlags(0x21, 0x10)
    Jump("loc_D76")

    label("loc_BD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 6)), scpexpr(EXPR_END)), "loc_BE7")
    Jump("loc_D76")

    label("loc_BE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 5)), scpexpr(EXPR_END)), "loc_C45")
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x8, 0x80)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    TurnDirection(0x13, 0x14, 0)
    TurnDirection(0x14, 0x13, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 26270, 2500, 1570, 180)
    SetChrFlags(0x1E, 0x10)
    Jump("loc_D76")

    label("loc_C45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_C99")
    ClearChrFlags(0x8, 0x80)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    TurnDirection(0x13, 0x14, 0)
    TurnDirection(0x14, 0x13, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 26270, 2500, 1570, 180)
    SetChrFlags(0x1E, 0x10)
    Jump("loc_D76")

    label("loc_C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_D02")
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -9520, 2500, 29080, 40)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x16, 0x80)
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x21, 0xB4, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    Jump("loc_D76")

    label("loc_D02")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_D2D")
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x21, 0x10)
    ClearChrFlags(0x22, 0x80)
    Jump("loc_D76")

    label("loc_D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_D76")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 420, 2500, 9250, 326)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -470, 2500, 10590, 146)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)

    label("loc_D76")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1B, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D8A")
    Event(0, 41)

    label("loc_D8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D9E")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 40)
    Jump("loc_DB0")

    label("loc_D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_DB0")
    ClearScenarioFlags(0x5C, 1)
    SetScenarioFlags(0x2, 0)
    Event(0, 44)

    label("loc_DB0")

    Return()

    # Function_2_969 end

    def Function_3_DB1(): pass

    label("Function_3_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_DC3")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_DC3")

    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFrame(0x8, "light", 0x0, 0x1)
    SetMapObjFlags(0x8, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_DF7")
    Jump("loc_E0C")

    label("loc_DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_E0C")
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)

    label("loc_E0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_END)), "loc_E1D")
    OP_24(0x7B)
    Jump("loc_E39")

    label("loc_E1D")

    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)

    label("loc_E39")

    LoadEffect(0x7, "event\\ev308_02.eff")
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, -16000, -1500, 16000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 12000, -1500, -12000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 12000, -1500, 16000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_3_DB1 end

    def Function_4_EF4(): pass

    label("Function_4_EF4")

    Call(0, 37)
    Return()

    # Function_4_EF4 end

    def Function_5_EF8(): pass

    label("Function_5_EF8")

    Call(0, 37)
    Return()

    # Function_5_EF8 end

    def Function_6_EFC(): pass

    label("Function_6_EFC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F54")

    #C0001
    ChrTalk(
        0xFE,
        "车站一带非常拥挤混乱。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "请注意不要丢东西，\x01",
            "不要让小孩走失～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1076")

    label("loc_F54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_FB6")

    #C0003
    ChrTalk(
        0xFE,
        (
            "为了引导游行的秩序，\x01",
            "我在市内四处奔波了好久……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "呼、呼……\x01",
            "累、累死了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1076")

    label("loc_FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1029")

    #C0005
    ChrTalk(
        0xFE,
        (
            "游行活动的警备工作\x01",
            "由我们公共安全科\x01",
            "全权负责。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……在这种人群中，\x01",
            "想保证道路顺畅都很困难。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1076")

    label("loc_1029")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1037")
    Jump("loc_1076")

    label("loc_1037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1076")

    #C0007
    ChrTalk(
        0xFE,
        "嘟嘟～！请不要推搡！\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "请不要跑到车辆的前面！\x02",
    )

    CloseMessageWindow()

    label("loc_1076")

    TalkEnd(0xFE)
    Return()

    # Function_6_EFC end

    def Function_7_107A(): pass

    label("Function_7_107A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1169")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1102")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    #C0009
    ChrTalk(
        0xFE,
        (
            "亚比……\x01",
            "你已经累了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "好～那么就让\x01",
            "妈妈来背你吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        (
            "真、真的吗～？\x01",
            "好～耶！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_1164")

    label("loc_1102")


    #C0012
    ChrTalk(
        0xFE,
        (
            "在纪念庆典期间，每天都在玩，\x01",
            "好像已经累坏了。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "这也难怪呢……\x01",
            "也许连我都玩得有些过火了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1164")

    Jump("loc_1318")

    label("loc_1169")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_11D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1184")
    Call(0, 8)
    Jump("loc_11D4")

    label("loc_1184")


    #C0014
    ChrTalk(
        0xFE,
        (
            "今年真是留下了\x01",
            "很不错的回忆。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "呵呵，克洛斯贝尔的\x01",
            "纪念庆典真是有趣呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11D4")

    Jump("loc_1318")

    label("loc_11D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_122D")
    TurnDirection(0xFE, 0xA, 0)

    #C0016
    ChrTalk(
        0xFE,
        "看啊，那就是游行哦。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "一边放着音乐，\x01",
            "一边在市内巡游。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1318")

    label("loc_122D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_12AC")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    #C0018
    ChrTalk(
        0xFE,
        "亚比，好吃吗？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "能不能也分给\x01",
            "妈妈一点呀～？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        "嗯，分给你！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "妈妈，一起来\x01",
            "吃吧～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_1318")

    label("loc_12AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1318")

    #C0022
    ChrTalk(
        0xFE,
        (
            "我今年才刚刚\x01",
            "搬来克洛斯贝尔，\x01",
            "还是第一次参加纪念庆典呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "真是很壮观啊……\x01",
            "让我大吃一惊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1318")

    TalkEnd(0xFE)
    Return()

    # Function_7_107A end

    def Function_8_131C(): pass

    label("Function_8_131C")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    #C0024
    ChrTalk(
        0x9,
        "游行好有趣哦～！\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0025
    ChrTalk(
        0xA,
        "嗯，真的～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_8_131C end

    def Function_9_137B(): pass

    label("Function_9_137B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_13B3")
    TurnDirection(0xFE, 0x9, 0)

    #C0026
    ChrTalk(
        0xFE,
        "妈妈，我突然有点想睡了……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1478")

    label("loc_13B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_13C4")
    Call(0, 8)
    Jump("loc_1478")

    label("loc_13C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_13F1")

    #C0027
    ChrTalk(
        0xFE,
        (
            "游～行？\x01",
            "那是什么东西啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1478")

    label("loc_13F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1434")

    #C0028
    ChrTalk(
        0xFE,
        (
            "妈妈买了冰激凌\x01",
            "给我吃～\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "嘿嘿嘿，真好吃～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1478")

    label("loc_1434")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1478")
    TurnDirection(0xFE, 0x9, 0)

    #C0030
    ChrTalk(
        0xFE,
        "好漂亮啊～彩纸屑～！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "喂，妈妈，好棒呀～！\x02",
    )

    CloseMessageWindow()

    label("loc_1478")

    TalkEnd(0xFE)
    Return()

    # Function_9_137B end

    def Function_10_147C(): pass

    label("Function_10_147C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A6")
    Call(0, 43)
    Return()

    label("loc_14A6")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_14B3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1503")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1503")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1523")
    OP_AF(0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1985")

    label("loc_1523")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1537")
    Jump("loc_1985")

    label("loc_1537")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1985")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1684")

    #C0032
    ChrTalk(
        0xFE,
        (
            "听说各位抓到了盗窃犯，\x01",
            "这是真的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "太好了……这样一来，\x01",
            "被盗的米拉就能拿回来了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "那个，作为谢礼，\x01",
            "请收下这个吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x1CF, 1)

    #C0036
    ChrTalk(
        0x104,
        "#0300F噢，谢啦。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "真是承蒙关照了。\x01",
            "下次请以客人的身份光临吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBC, 7)
    Jump("loc_1985")

    label("loc_1684")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_173C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E7")

    #C0038
    ChrTalk(
        0xFE,
        (
            "今天也有不少警察\x01",
            "在来回奔波啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "啊，对了。\x01",
            "好像有闭幕式吧？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1737")

    label("loc_16E7")


    #C0040
    ChrTalk(
        0xFE,
        (
            "庆典的最终日，游客\x01",
            "似乎也很多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "可能是因为大家都想来\x01",
            "看看闭幕式吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1737")

    Jump("loc_1985")

    label("loc_173C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_17D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B4")

    #C0042
    ChrTalk(
        0xFE,
        (
            "啊，不好……\x01",
            "香橙咖啡好像\x01",
            "快要卖完了……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "不好意思，如果想点的话，\x01",
            "就请抓紧时间吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_17D1")

    label("loc_17B4")


    #C0044
    ChrTalk(
        0xFE,
        (
            "今天真的是\x01",
            "超级忙啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D1")

    Jump("loc_1985")

    label("loc_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_18CA")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1846")

    #C0045
    ChrTalk(
        0xFE,
        (
            "光注意着招呼客人……\x01",
            "真是大意了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "呼，这下销售额可就……\x02",
    )

    CloseMessageWindow()
    Jump("loc_18C5")

    label("loc_1846")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1893")

    #C0047
    ChrTalk(
        0xFE,
        (
            "游行的车队差不多\x01",
            "也该来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "我、我也好紧张呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_18C5")

    label("loc_1893")


    #C0049
    ChrTalk(
        0xFE,
        (
            "游行活动好像马上\x01",
            "就要开始了呢。\x01",
            "（紧张……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18C5")

    Jump("loc_1985")

    label("loc_18CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1936")

    #C0050
    ChrTalk(
        0xFE,
        (
            "听说市政厅那边今天\x01",
            "也要举办活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "一群很有精英气质的人\x01",
            "从早上开始就聚集在那里了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1985")

    label("loc_1936")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1985")

    #C0052
    ChrTalk(
        0xFE,
        (
            "欢迎光临，\x01",
            "欢迎光临～！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "客人真是很多啊……\x01",
            "连我都吃了一惊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1985")

    Jump("loc_14B3")

    label("loc_198A")

    TalkEnd(0xFE)
    Return()

    # Function_10_147C end

    def Function_11_198E(): pass

    label("Function_11_198E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1A20")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19EC")

    #C0054
    ChrTalk(
        0xFE,
        "今天就是最终日了啊……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "要玩的话就要把握机会了……！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A1B")

    label("loc_19EC")


    #C0056
    ChrTalk(
        0xFE,
        (
            "好，今天要去哪里呢。\x01",
            "从哪里开始玩起呢！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A1B")

    Jump("loc_1D91")

    label("loc_1A20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1AE9")

    #C0057
    ChrTalk(
        0xFE,
        "市长的演说真精彩。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "还有『咪西』也很可爱！\x02",
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

    #C0059
    ChrTalk(
        0x101,
        "#0003F（在、在说什么呢……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D91")

    label("loc_1AE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1BA7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6E")

    #C0060
    ChrTalk(
        0xFE,
        (
            "虽说是纪念庆典，\x01",
            "但玩得太过火也不好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "人还是要保持自制心的！\x01",
            "在不忘掉自制的前提下尽情享受吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1BA2")

    label("loc_1B6E")


    #C0062
    ChrTalk(
        0xFE,
        "……带相机了吧？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "游行马上就要开始了哦！！\x02",
    )

    CloseMessageWindow()

    label("loc_1BA2")

    Jump("loc_1D91")

    label("loc_1BA7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1CCF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6C")

    #C0064
    ChrTalk(
        0xFE,
        (
            "哇噢！今天将在市政厅\x01",
            "召开国际研讨会呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "在市长的号召之下，国内外的\x01",
            "众多专家学者纷纷响应而来……！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "他们的研究讨论\x01",
            "必定会给克洛斯贝尔\x01",
            "带来一道耀眼的曙光！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1CCA")

    label("loc_1C6C")


    #C0067
    ChrTalk(
        0xFE,
        (
            "市政厅那里今天要\x01",
            "召开国际研讨会呢！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "……我受不了这种死板的场合，\x01",
            "所以就不去旁听了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CCA")

    Jump("loc_1D91")

    label("loc_1CCF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3D")

    #C0069
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村的\x01",
            "外卖蛋包饭……吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "这么一说，\x01",
            "我就必须要去\x01",
            "吃一次看看了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D91")

    label("loc_1D3D")


    #C0071
    ChrTalk(
        0xFE,
        (
            "我最讨厌诱人的东西\x01",
            "就放在自己眼前却\x01",
            "触及不到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "所以必须要去吃吃看才行。\x02",
    )

    CloseMessageWindow()

    label("loc_1D91")

    TalkEnd(0xFE)
    Return()

    # Function_11_198E end

    def Function_12_1D95(): pass

    label("Function_12_1D95")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1DA6")
    Jump("loc_1EBF")

    label("loc_1DA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1DB4")
    Jump("loc_1EBF")

    label("loc_1DB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1DC2")
    Jump("loc_1EBF")

    label("loc_1DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1DD0")
    Jump("loc_1EBF")

    label("loc_1DD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1EBF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E83")

    #C0073
    ChrTalk(
        0xFE,
        (
            "本来是想在工作的间隙\x01",
            "出来稍微休息一下的，不过……\x01",
            "嘁，真是吵闹啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "纪念庆典结束的一周之后，\x01",
            "预算会议就要开始了吧？\x01",
            "现在可不是放松的时候啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1EBF")

    label("loc_1E83")


    #C0075
    ChrTalk(
        0xFE,
        (
            "啊～可恶，想想就不爽。\x01",
            "但现在可不是\x01",
            "放松的时候啊～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EBF")

    TalkEnd(0xFE)
    Return()

    # Function_12_1D95 end

    def Function_13_1EC3(): pass

    label("Function_13_1EC3")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1ED0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F20")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1F20")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F40")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_26B0")

    label("loc_1F40")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F54")
    Jump("loc_26B0")

    label("loc_1F54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_201D")

    #C0076
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "看来来村子的游客\x01",
            "不会比这更多了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "今年的客流高峰应该就到此为止了，\x01",
            "差不多也该撤摊了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "你们几个，如果想买什么的话，\x01",
            "就趁现在和我说吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B0")

    label("loc_201D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_20A2")

    #C0079
    ChrTalk(
        0xFE,
        (
            "为了庆典最终日，最后再加把劲……\x01",
            "努力把现在的存货\x01",
            "全部都卖光吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "你们也要买点什么吗？\x01",
            "有需要的话就尽管开口。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_26B0")

    label("loc_20A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_243F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_21A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_215E")

    #C0081
    ChrTalk(
        0xFE,
        (
            "刚才接到了联络，\x01",
            "连环盗窃犯好像已经被抓住了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔的警察\x01",
            "还真是出乎意料地可靠啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "说实话，我还是第一次感觉到\x01",
            "他们如此可靠呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21A3")

    label("loc_215E")


    #C0084
    ChrTalk(
        0xFE,
        "这样就可以继续经营店铺了……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "为了振兴村子，\x01",
            "必须要努力啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A3")

    Jump("loc_243A")

    label("loc_21A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23CB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2323")

    #C0086
    ChrTalk(
        0x101,
        (
            "#0001F不好意思，能否\x01",
            "稍微向您请教一些事呢？\x02\x03",

            "我们正在对盗窃事件\x01",
            "进行调查……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "（紧张）……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "不、不用担心，\x01",
            "我们的店就在警察局总部门口啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "可是，附近的店铺\x01",
            "都遭到过毒手了，\x01",
            "还是会紧张啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        (
            "#0101F（这家铺子的人\x01",
            "  好像非常警戒呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#0003F（他似乎没有什么和犯人有关的线索，\x01",
            "  就不要和他说太多了。）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x9)
    Jump("loc_23C6")

    label("loc_2323")


    #C0092
    ChrTalk(
        0xFE,
        (
            "（紧张）……\x01",
            "我们的店就在警察局总部门口。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "不、不用担心，\x01",
            "绝对没问题的。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0003F（确实如此，店开在总部门口的话，\x01",
            "  犯人应该也不会冒险下手了吧……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23C6")

    Jump("loc_243A")

    label("loc_23CB")


    #C0095
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村那边\x01",
            "传来了联络哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "据说那边也有不少\x01",
            "游客造访。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "希望村子可以因此\x01",
            "变得热闹起来啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243A")

    Jump("loc_26B0")

    label("loc_243F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2576")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24FD")

    #C0098
    ChrTalk(
        0xFE,
        "村里的特产好像卖得很不错呢。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "时不时就能看见一些游客\x01",
            "向村子那边出发呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "纪念庆典还剩下两天，\x01",
            "但利用庆典来搞活村子经济的想法\x01",
            "已经充分展现出成果了呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2571")

    label("loc_24FD")


    #C0101
    ChrTalk(
        0xFE,
        (
            "村里的特产大卖，\x01",
            "又聚集了不少游客……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "虽然纪念庆典还剩下两天，\x01",
            "但搞活村子经济的效果已经充分体现出来了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2571")

    Jump("loc_26B0")

    label("loc_2576")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_26B0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262B")

    #C0103
    ChrTalk(
        0xFE,
        (
            "这是阿尔摩利卡的著名特产——\x01",
            "高纯度蜂蜜。\x01",
            "有兴趣的话，不妨尝尝看。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "如果想去酿出这种蜂蜜的\x01",
            "阿尔摩利卡村看看，\x01",
            "只要在东出口乘坐导力巴士就可以了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_26B0")

    label("loc_262B")


    #C0105
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村被\x01",
            "广阔的自然地带所环绕，\x01",
            "是一座非常祥和宁静的村落。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "如果纪念庆典的喧闹让你们感到疲劳，\x01",
            "就不妨去那里放松一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26B0")

    Jump("loc_1ED0")

    label("loc_26B5")

    TalkEnd(0xFE)
    Return()

    # Function_13_1EC3 end

    def Function_14_26B9(): pass

    label("Function_14_26B9")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_26C6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D2D")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",      # 0
            "购物\x01",      # 1
            "放弃\x01",      # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2716")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2716")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2736")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D28")

    label("loc_2736")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_274A")
    Jump("loc_2D28")

    label("loc_274A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D28")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2879")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27E3")

    #C0107
    ChrTalk(
        0xFE,
        (
            "虽然比昨天轻松多了，\x01",
            "但还是很忙啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "算啦，熬过今天之后\x01",
            "就可以回村子了。\x01",
            "最后再坚持一下吧！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2874")

    label("loc_27E3")


    #C0109
    ChrTalk(
        0xFE,
        (
            "话说回来，都已经是最终日了啊……\x01",
            "真是转瞬之间就结束的\x01",
            "都市生活啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "没能去米修拉姆玩一玩，也算是心头\x01",
            "的一大遗憾……算了，以后总有机会。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2874")

    Jump("loc_2D28")

    label("loc_2879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_28F5")

    #C0111
    ChrTalk(
        0xFE,
        (
            "村子里的店，\x01",
            "就先放在一边吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "那里的店很重要！但这里的摊子也很重要！\x01",
            "而我现在的责任就是这边的工作！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D28")

    label("loc_28F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2B36")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_29D7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_297C")

    #C0113
    ChrTalk(
        0xFE,
        (
            "要不要来一份阿尔摩利卡村\x01",
            "的特制蛋包饭啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "……呼，必须要努力\x01",
            "把下降的销售额挽回啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_29D2")

    label("loc_297C")


    #C0115
    ChrTalk(
        0xFE,
        (
            "……不知村子那边\x01",
            "现在如何了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "大概和平常一样，\x01",
            "奇斯还是一直坐在那里吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29D2")

    Jump("loc_2B31")

    label("loc_29D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2A77")

    #C0117
    ChrTalk(
        0xFE,
        "（紧紧盯着）……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "你们几个……\x01",
            "应该不是什么可疑人物吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "如、如果敢在我们这里闹事，\x01",
            "我马上就会把你们给抓起来哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B31")

    label("loc_2A77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ADB")

    #C0120
    ChrTalk(
        0xFE,
        "呼啊～好累啊！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "老爸教我的料理，\x01",
            "总算是学会了，\x01",
            "但一个人做果然很辛苦啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2B31")

    label("loc_2ADB")


    #C0122
    ChrTalk(
        0xFE,
        (
            "……不知村子那边\x01",
            "现在如何了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "大概和平常一样，\x01",
            "奇斯还是一直坐在那里吧……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B31")

    Jump("loc_2D28")

    label("loc_2B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2C66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BEF")

    #C0124
    ChrTalk(
        0xFE,
        (
            "克洛斯贝尔市\x01",
            "今天也很热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "真是吃了一惊啊，\x01",
            "稍一不留意，就有这么多\x01",
            "人在排队了。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "哈，为了吃东西居然不惜排那么\x01",
            "长时间的队，城市人真是奇怪啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2C61")

    label("loc_2BEF")


    #C0127
    ChrTalk(
        0xFE,
        (
            "为了吃东西居然不惜排那么\x01",
            "长时间的队，城市人真是有趣啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "如果是我的话，就会马上放弃，\x01",
            "改去别的地方吃啦～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C61")

    Jump("loc_2D28")

    label("loc_2C66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2D28")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CDC")

    #C0129
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村的名产——\x01",
            "酒馆『白蜡亭』的\x01",
            "独特料理哦～\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "如果有时间，\x01",
            "请务必赏光啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2D28")

    label("loc_2CDC")


    #C0131
    ChrTalk(
        0xFE,
        (
            "呼，没想到连我\x01",
            "都会被动员而来啊，\x01",
            "不过呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "算了，反正也很开心。\x02",
    )

    CloseMessageWindow()

    label("loc_2D28")

    Jump("loc_26C6")

    label("loc_2D2D")

    TalkEnd(0xFE)
    Return()

    # Function_14_26B9 end

    def Function_15_2D31(): pass

    label("Function_15_2D31")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2D42")
    Jump("loc_2EAB")

    label("loc_2D42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2D50")
    Jump("loc_2EAB")

    label("loc_2D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E45")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE8")

    #C0133
    ChrTalk(
        0xFE,
        (
            "游击士今天好像也要\x01",
            "在市内分头行动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "呼……\x01",
            "既然如此，就没办法啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "我们至少要让游行活动\x01",
            "保持秩序，不混乱啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_2E40")

    label("loc_2DE8")


    #C0136
    ChrTalk(
        0xFE,
        (
            "在游击士的面前，\x01",
            "绝对不能丢脸。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "要和普通警官们合作，\x01",
            "一定不能让游行陷入混乱。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E40")

    Jump("loc_2EAB")

    label("loc_2E45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E53")
    Jump("loc_2EAB")

    label("loc_2E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2EAB")

    #C0138
    ChrTalk(
        0xFE,
        "哟，好多的人啊。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "到处都有大大小小的争吵和纠纷，\x01",
            "你们也要多加注意啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EAB")

    TalkEnd(0xFE)
    Return()

    # Function_15_2D31 end

    def Function_16_2EAF(): pass

    label("Function_16_2EAF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2EC0")
    Jump("loc_31E4")

    label("loc_2EC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2F25")

    #C0140
    ChrTalk(
        0xFE,
        (
            "我跟着游行队伍\x01",
            "跑到了港湾区，\x01",
            "刚刚才回来呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "啊～好累啊……\x01",
            "好想喝杯果汁啊～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_31E4")

    label("loc_2F25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_304D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FEA")

    #C0142
    ChrTalk(
        0xFE,
        "哎呀，昨天真是帮大忙了～\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "在上次的事件中，你们\x01",
            "能比一科抢先一步立功，\x01",
            "真是名不虚传啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#0012F哈哈，哪里，\x01",
            "没有那种事啦……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "什么嘛～\x01",
            "没必要不好意思啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_3048")

    label("loc_2FEA")


    #C0146
    ChrTalk(
        0xFE,
        (
            "连我们都被调过来\x01",
            "负责游行活动的警备工作了呢～\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "哎呀呀，短时间内似乎\x01",
            "是闲不下来了呢～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3048")

    Jump("loc_31E4")

    label("loc_304D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_305B")
    Jump("loc_31E4")

    label("loc_305B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_31E4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_316C")

    #C0148
    ChrTalk(
        0xFE,
        (
            "现在正在追捕盗窃犯呢。\x01",
            "每年庆典期间，趁着骚乱\x01",
            "而做恶的家伙都会屡禁不绝啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "哎呀呀，那就只能\x01",
            "由我来处罚他们啦～！\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#0000F怎、怎么感觉像是乐在其中呢。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "啊哈哈，那是当然啊～\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "因为像这种庆典活动中的盗窃犯，\x01",
            "只是单纯的犯罪而已～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_31E4")

    label("loc_316C")


    #C0153
    ChrTalk(
        0xFE,
        (
            "我比较喜欢处理这种简单明了，\x01",
            "不需要考虑太多的事件～\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "像议员啦，幕后关系这种复杂的背景，\x01",
            "能不去考虑就最好不过～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31E4")

    TalkEnd(0xFE)
    Return()

    # Function_16_2EAF end

    def Function_17_31E8(): pass

    label("Function_17_31E8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3265")

    #C0155
    ChrTalk(
        0xFE,
        (
            "啊，今年的游行用车\x01",
            "真是很多啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "哎～一、二、三……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "嗯～还是没有到齐啊，\x01",
            "应该是有七辆的～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_329E")

    label("loc_3265")


    #C0158
    ChrTalk(
        0xFE,
        (
            "如果游行的车辆不到齐，\x01",
            "就没法制定警备工作的计划啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_329E")

    TalkEnd(0xFE)
    Return()

    # Function_17_31E8 end

    def Function_18_32A2(): pass

    label("Function_18_32A2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_32F4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C0")
    Call(0, 19)
    Jump("loc_32EF")

    label("loc_32C0")


    #C0159
    ChrTalk(
        0xFE,
        (
            "最终日肯定会非常拥挤，\x01",
            "不如早点离开算了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32EF")

    Jump("loc_334C")

    label("loc_32F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_334C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_330F")
    Call(0, 19)
    Jump("loc_334C")

    label("loc_330F")


    #C0160
    ChrTalk(
        0xFE,
        (
            "阿尔摩利卡村的蜂蜜实在是太棒了。\x01",
            "真是被那美味感动了啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_334C")

    TalkEnd(0xFE)
    Return()

    # Function_18_32A2 end

    def Function_19_3350(): pass

    label("Function_19_3350")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x13, 0x14, 0)
    TurnDirection(0x14, 0x13, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_33C7")

    #C0161
    ChrTalk(
        0x13,
        (
            "那么，游行也已经欣赏够了，\x01",
            "差不多也该回村子了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x14,
        "……嗯，也是啊，妈妈。\x02",
    )

    CloseMessageWindow()
    Jump("loc_348C")

    label("loc_33C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_348C")

    #C0163
    ChrTalk(
        0x13,
        (
            "呼呼！村里的特产\x01",
            "好像卖得相当不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x13,
        (
            "嘿，史蒂芬，快看啊。\x01",
            "这是我们家旁边那家店\x01",
            "所出售的蜂蜜呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x14,
        "嘿～……不错嘛。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x13,
        (
            "真是的，这孩子，\x01",
            "怎么只有这么一点反应！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x0, 0x0)

    label("loc_348C")

    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_19_3350 end

    def Function_20_349B(): pass

    label("Function_20_349B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_34E5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34B9")
    Call(0, 19)
    Jump("loc_34E0")

    label("loc_34B9")


    #C0167
    ChrTalk(
        0xFE,
        (
            "不知为什么，\x01",
            "我有些想回村里了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34E0")

    Jump("loc_355B")

    label("loc_34E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_355B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3500")
    Call(0, 19)
    Jump("loc_355B")

    label("loc_3500")


    #C0168
    ChrTalk(
        0xFE,
        (
            "这好像还是第一次看到\x01",
            "那蜂蜜放在店里贩卖呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "……仔细看看的话，好像真是很美味呢。\x02",
    )

    CloseMessageWindow()

    label("loc_355B")

    TalkEnd(0xFE)
    Return()

    # Function_20_349B end

    def Function_21_355F(): pass

    label("Function_21_355F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_35DB")

    #C0170
    ChrTalk(
        0xFE,
        (
            "闭幕式也预定在\x01",
            "这里的大会堂中\x01",
            "举行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "会场的警备，还有对市民的引导……\x01",
            "今天的工作也堆积如山啊！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36FB")

    label("loc_35DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_35E9")
    Jump("loc_36FB")

    label("loc_35E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_367C")

    #C0172
    ChrTalk(
        0xFE,
        (
            "十点出发，\x01",
            "到达欢乐街是三十分钟之后……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "科长，彩虹剧团门前\x01",
            "的人应该非常多。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "为了不让游行队伍被打断，\x01",
            "请您进行指示吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36FB")

    label("loc_367C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_36F2")

    #C0175
    ChrTalk(
        0xFE,
        (
            "今天要在市政厅的大会堂\x01",
            "中召开研讨会。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "麦克道尔市长也会参加，\x01",
            "我们必须认真做好警备工作才行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_36FB")

    label("loc_36F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_36FB")

    label("loc_36FB")

    TalkEnd(0xFE)
    Return()

    # Function_21_355F end

    def Function_22_36FF(): pass

    label("Function_22_36FF")

    TalkBegin(0xFE)

    #C0177
    ChrTalk(
        0xFE,
        "今天有游行活动哦。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "虽说是徐徐行进，\x01",
            "但毕竟要在人群中来回跑动。\x01",
            "一点都疏忽不得啊。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_36FF end

    def Function_23_3762(): pass

    label("Function_23_3762")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E3")

    #C0179
    ChrTalk(
        0xFE,
        (
            "#1006F真是的，连我都被叫出来了，\x01",
            "到底在想什么呢。\x02\x03",

            "#1000F……喂，你们几个，\x01",
            "快来替我工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0003F啊，可我们也正忙着处理\x01",
            "支援请求呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x104,
        (
            "#0300F我说～在这种特殊时期，\x01",
            "科长就不能自己稍微干点事情吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0182
    ChrTalk(
        0xFE,
        (
            "#1000F你们根本就不知道\x01",
            "监管游行的工作有多麻烦，\x01",
            "所以才会这样说。\x02\x03",

            "#1006F真是的……这跟你们的杂务工作\x01",
            "可不是一个等级的啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_3961")

    label("loc_38E3")


    #C0183
    ChrTalk(
        0xFE,
        (
            "#1003F（点烟）……\x01",
            "看来只有用隐藏秘技来逃跑了吧。\x02\x03",

            "好麻烦啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#0203F科长，请您偶尔也踏踏实实地\x01",
            "完成自己分内的工作。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3961")

    TalkEnd(0xFE)
    Return()

    # Function_23_3762 end

    def Function_24_3965(): pass

    label("Function_24_3965")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_39A7")

    #C0185
    ChrTalk(
        0xFE,
        (
            "今天是最终日吗……\x01",
            "还真是有些恋恋不舍啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_39A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_39F4")

    #C0186
    ChrTalk(
        0xFE,
        (
            "中央广场应该是有\x01",
            "很多店铺的。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "其实也不用那么担心啦。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_39F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3A4B")

    #C0188
    ChrTalk(
        0xFE,
        "今天有一项重要活动。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "正是为了看这个，\x01",
            "我才会从村子里赶来的～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_3A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3ABB")

    #C0190
    ChrTalk(
        0xFE,
        (
            "『克洛斯贝尔的现在和未来』\x01",
            "……好像是这个名字吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "据说要召开一场以此为主题的\x01",
            "研讨会哦。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3AF9")

    label("loc_3ABB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3AF9")

    #C0192
    ChrTalk(
        0xFE,
        (
            "不愧是克洛斯贝尔的市政厅。\x01",
            "壮观，太壮观了……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF9")

    TalkEnd(0xFE)
    Return()

    # Function_24_3965 end

    def Function_25_3AFD(): pass

    label("Function_25_3AFD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3B65")

    #C0193
    ChrTalk(
        0xFE,
        "最后还要再去逛逛那些露天店啊。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "首先是特别美味的——\x01",
            "什么什么村的那个蛋包饭！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C86")

    label("loc_3B65")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3BAE")

    #C0195
    ChrTalk(
        0xFE,
        (
            "相机里的感光回路\x01",
            "已经用完了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        "要去哪里买呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C86")

    label("loc_3BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3BF4")

    #C0197
    ChrTalk(
        0xFE,
        "领头的车子就要驶出了～\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "一定要把它拍进照片啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3C86")

    label("loc_3BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3C56")

    #C0199
    ChrTalk(
        0xFE,
        (
            "市政厅今天好像\x01",
            "有活动要举办哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "从刚才开始，就有数不清的\x01",
            "职员们进进出出。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3C86")

    label("loc_3C56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3C86")

    #C0201
    ChrTalk(
        0xFE,
        (
            "必须要把这个场面\x01",
            "拍下来才行呀～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C86")

    TalkEnd(0xFE)
    Return()

    # Function_25_3AFD end

    def Function_26_3C8A(): pass

    label("Function_26_3C8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3CEF")

    #C0202
    ChrTalk(
        0xFE,
        (
            "哎呀，等一下。\x01",
            "米拉已经所剩无几了……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "没办法，\x01",
            "只能去ＩＢＣ取些钱了吗……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E31")

    label("loc_3CEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3D2C")

    #C0204
    ChrTalk(
        0xFE,
        (
            "不愧是克洛斯贝尔的庆典啊！\x01",
            "就是华丽壮观！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E31")

    label("loc_3D2C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3D83")

    #C0205
    ChrTalk(
        0xFE,
        (
            "根据我的预感，\x01",
            "游行队伍将会从这边过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "喂，你快把相机准备好！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3E31")

    label("loc_3D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3DD7")

    #C0207
    ChrTalk(
        0xFE,
        (
            "今天一直有警察\x01",
            "在四处转悠。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "哈哈～！\x01",
            "是不是发生什么事了～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3E31")

    label("loc_3DD7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3E31")

    #C0209
    ChrTalk(
        0xFE,
        "那么，好好玩一玩吧～！\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "庆典万岁！克洛斯贝尔万岁！\x01",
            "必须要尽情玩个够啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E31")

    TalkEnd(0xFE)
    Return()

    # Function_26_3C8A end

    def Function_27_3E35(): pass

    label("Function_27_3E35")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3E8F")

    #C0211
    ChrTalk(
        0xFE,
        "我今天要去购物哦。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "绝对要去！\x01",
            "只有这件事我是绝对不会让步的！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_401A")

    label("loc_3E8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3EF8")

    #C0213
    ChrTalk(
        0xFE,
        (
            "来参加庆典虽然很不错，\x01",
            "但我还一次\x01",
            "都没去购物过呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "不爽！\x01",
            "我好想去买东西呀！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_401A")

    label("loc_3EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3F4A")

    #C0215
    ChrTalk(
        0xFE,
        (
            "啊啊啊，明明想在上午\x01",
            "去百货店的～\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "但游行竟然\x01",
            "都要开始了！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_401A")

    label("loc_3F4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3FB0")

    #C0217
    ChrTalk(
        0xFE,
        (
            "我说你啊～不是答应过\x01",
            "要带我去购物的吗！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "为什么一直都在逛\x01",
            "这些露天店铺啊～！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_401A")

    label("loc_3FB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_401A")

    #C0219
    ChrTalk(
        0xFE,
        "购物啊，我要去大采购！\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "观光什么的，以后再说就好了嘛！\x01",
            "怎么能错过纪念庆典的打折促销啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_401A")

    TalkEnd(0xFE)
    Return()

    # Function_27_3E35 end

    def Function_28_401E(): pass

    label("Function_28_401E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4064")

    #C0221
    ChrTalk(
        0xFE,
        "今天也非常忙啊！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "各位也请努力\x01",
            "执行任务吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_40DE")

    label("loc_4064")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4072")
    Jump("loc_40DE")

    label("loc_4072")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4080")
    Jump("loc_40DE")

    label("loc_4080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_40D5")

    #C0223
    ChrTalk(
        0xFE,
        (
            "我今天要和前辈\x01",
            "一起进行警备工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "必须要绷紧神经，加强戒备！\x02",
    )

    CloseMessageWindow()
    Jump("loc_40DE")

    label("loc_40D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_40DE")

    label("loc_40DE")

    TalkEnd(0xFE)
    Return()

    # Function_28_401E end

    def Function_29_40E2(): pass

    label("Function_29_40E2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_4216")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_417D")

    #C0225
    ChrTalk(
        0x18,
        (
            "#2100F啊，对了对了，\x01",
            "关于那个拍照的委托，如果照片数量够了，\x01",
            "就拿到通讯社的接待处去吧。\x02\x03",

            "拜托你们了哦～¤\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 4)
    Jump("loc_4211")

    label("loc_417D")


    #C0226
    ChrTalk(
        0x18,
        (
            "#2100F今年游行的人数\x01",
            "大概是有史以来最多的一次了。\x02\x03",

            "#2104F从前面到后面，\x01",
            "所有角度的照片\x01",
            "全都要好好拍下来！\x02\x03",

            "#2109F嗯～气氛已经高涨起来了呢！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_4211")

    Jump("loc_4390")

    label("loc_4216")

    OP_4B(0x19, 0xFF)

    #C0227
    ChrTalk(
        0x101,
        (
            "#0000F格蕾丝小姐，\x01",
            "您正在收集游行的新闻素材吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x18,
        (
            "#2100F那还用说！\x01",
            "今年的游行规模大概是\x01",
            "有史以来最大的一次哦～\x02\x03",

            "#2104F从游行队伍的前面到后面，\x01",
            "所有角度的照片\x01",
            "全都要好好拍下来！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x19, 300)

    #C0229
    ChrTalk(
        0x18,
        "#2109F雷因兹，燃烧起干劲了吗？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 300)

    #C0230
    ChrTalk(
        0x19,
        "ＹＥＳ，ＭＡＤＡＭ！\x02",
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
    OP_93(0x19, 0x2D, 0x0)
    SetScenarioFlags(0x1, 3)
    OP_4C(0x19, 0xFF)

    label("loc_4390")

    TalkEnd(0xFE)
    Return()

    # Function_29_40E2 end

    def Function_30_4394(): pass

    label("Function_30_4394")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_43D0")

    #C0231
    ChrTalk(
        0xFE,
        (
            "（紧张）……\x01",
            "只剩三十分钟左右了吧！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4433")

    label("loc_43D0")


    #C0232
    ChrTalk(
        0xFE,
        "游、游行终于要开始了呀！\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "今天的照片会刊登在周边\x01",
            "诸国的新闻杂志上……\x01",
            "稍微有些紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_4433")

    TalkEnd(0xFE)
    Return()

    # Function_30_4394 end

    def Function_31_4437(): pass

    label("Function_31_4437")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_44CB")
    Jump("loc_4515")

    label("loc_44CB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_44EB")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4515")

    label("loc_44EB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_450B")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4515")

    label("loc_450B")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4515")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_45B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4555")
    Call(0, 35)
    Jump("loc_45B6")

    label("loc_4555")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4567")
    Call(0, 36)
    Jump("loc_45B6")

    label("loc_4567")


    #C0234
    ChrTalk(
        0x1A,
        (
            "#0804F纪念庆典刚刚开始……\x02\x03",

            "#0802F让我们齐心协力，\x01",
            "共同撑过这段忙碌期吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45B6")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_4437 end

    def Function_32_45BE(): pass

    label("Function_32_45BE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4652")
    Jump("loc_469C")

    label("loc_4652")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4672")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469C")

    label("loc_4672")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4692")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_469C")

    label("loc_4692")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_469C")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4760")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46DC")
    Call(0, 35)
    Jump("loc_4760")

    label("loc_46DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46EE")
    Call(0, 36)
    Jump("loc_4760")

    label("loc_46EE")


    #C0235
    ChrTalk(
        0x1B,
        (
            "#0903F这里不愧是国际性的贸易都市，\x01",
            "有很多国外的游客呢。\x02\x03",

            "#0908F为了将一切事故防患于未然，\x01",
            "有必要多加注意呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4760")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_45BE end

    def Function_33_4768(): pass

    label("Function_33_4768")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_48FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488B")

    #C0236
    ChrTalk(
        0xFE,
        (
            "我们为了对即将开始的游行活动\x01",
            "进行警备，正在这里待命。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "凭借游击士的威信，单是站在这里，\x01",
            "就已经能产生相当的震慑作用了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x104,
        (
            "#0303F游击士毕竟是战斗的专家，对吧。\x02\x03",

            "#0309F从某种意义上来说，\x01",
            "确实比警察更有威慑效果呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#0000F……倒、倒也无法否认呢。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_48FA")

    label("loc_488B")


    #C0240
    ChrTalk(
        0xFE,
        (
            "呵，不过警察也很值得信赖啊，\x01",
            "我觉得警察变得比以前\x01",
            "可靠多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#0006F（这到底能不能算是\x01",
            "  夸奖呢……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48FA")

    TalkEnd(0xFE)
    Return()

    # Function_33_4768 end

    def Function_34_48FE(): pass

    label("Function_34_48FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4966")

    #C0242
    ChrTalk(
        0xFE,
        (
            "啊……这不是警察局的各位嘛，\x01",
            "工作好像很努力啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "今天的人特别多，\x01",
            "你们也要小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4966")

    TalkEnd(0xFE)
    Return()

    # Function_34_48FE end

    def Function_35_496A(): pass

    label("Function_35_496A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4450, 3750, -13280, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15650, 0)
    SetChrPos(0x101, -4650, 2500, -14600, 0)
    SetChrPos(0x102, -3800, 2500, -14700, 0)
    SetChrPos(0x103, -4650, 2500, -15750, 0)
    SetChrPos(0x104, -3800, 2500, -15850, 0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_0D()

    #C0244
    ChrTalk(
        0x1A,
        (
            "#0809F#5P呀哈～！\x01",
            "这不是支援科的各位嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1B,
        "#0902F你们好，辛苦了呢。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0002F哈哈……\x01",
            "你们才是，辛苦了。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x103,
        (
            "#0202F艾丝蒂尔，你们\x01",
            "也在工作啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x1A,
        (
            "#0804F#5P嗯，不过现在正准备\x01",
            "稍微休息一下呢。\x02\x03",

            "#0802F话说回来，虽然早有心理准备，\x01",
            "但实在没想到纪念庆典会如此盛大啊。\x02\x03",

            "#0803F嗯～不管是人数还是规模，\x01",
            "或许都要在诞辰庆典之上呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0005F诞辰庆典……？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1B,
        (
            "#0904F是为了庆祝利贝尔王国的女王\x01",
            "艾莉茜雅Ⅱ世的生日而举办的庆典。\x02\x03",

            "#0900F在利贝尔应该算是\x01",
            "最盛大的庆典了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#0000F说起来，你们两位\x01",
            "正是从利贝尔来的哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#0104F我以前也曾去参加过\x01",
            "一次女王诞辰庆典呢。\x02\x03",

            "#0102F很有王国的传统风格，\x01",
            "是一场非常华丽优美的庆典哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x1A,
        (
            "#0809F#5P嘿嘿嘿……\x01",
            "听你这么说，我也很开心哦。\x02\x03",

            "#0802F不过，并不是只有华丽和优雅，\x01",
            "期间也会举办武术大会这样的活动呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#0305F是吗？那听上去\x01",
            "还真是很有意思啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 2500, -14600, 0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    EndChrThread(0xC, 0x0)
    SetChrPos(0xC, 8370, 2390, -14850, 90)
    BeginChrThread(0xC, 0, 0, 1)
    SetScenarioFlags(0xB3, 7)
    EventEnd(0x5)
    Return()

    # Function_35_496A end

    def Function_36_4D5A(): pass

    label("Function_36_4D5A")

    EventBegin(0x0)
    Fade(500)
    OP_68(-4450, 3750, -13280, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15650, 0)
    SetChrPos(0x101, -4650, 2500, -14600, 0)
    SetChrPos(0x102, -3800, 2500, -14700, 0)
    SetChrPos(0x103, -4650, 2500, -15750, 0)
    SetChrPos(0x104, -3800, 2500, -15850, 0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_0D()

    #C0255
    ChrTalk(
        0x1A,
        (
            "#0801F#5P啊，说起来！\x02\x03",

            "#0802F罗伊德，听说你们\x01",
            "立下了相当大的功劳吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#0002F啊……\x01",
            "是说暗杀市长未遂的事件吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        (
            "#0104F呵，最后能顺利解决，\x01",
            "或许也多亏了一连串的偶然……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x1B,
        (
            "#0904F即使如此，要不是你们将恶性事件\x01",
            "防患于未然，\x01",
            "现在恐怕也就无法举办庆典了。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1A,
        (
            "#0809F#5P嗯嗯！\x01",
            "所以说，现在能有这么热闹的庆典，\x01",
            "全都是你们的功劳，对吧¤\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#0012F哈哈……\x01",
            "（平时几乎都不会受到赞扬，突然被这么\x01",
            "  夸奖，倒觉得有些不好意思呢……）\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        "#0304F（算啦，大大方方地接受就好。）\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, -4250, 2500, -14600, 0)
    SetChrSubChip(0x1A, 0x0)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    EndChrThread(0xC, 0x0)
    SetChrPos(0xC, 8370, 2390, -14850, 90)
    BeginChrThread(0xC, 0, 0, 1)
    SetScenarioFlags(0xB4, 1)
    EventEnd(0x5)
    Return()

    # Function_36_4D5A end

    def Function_37_500A(): pass

    label("Function_37_500A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch02751.itc", 0x1E)
    LoadChrToIndex("chr/ch02702.itc", 0x1F)
    LoadChrToIndex("chr/ch09400.itc", 0x20)
    LoadChrToIndex("chr/ch00250.itc", 0x21)
    LoadChrToIndex("chr/ch00254.itc", 0x22)
    SoundLoad(840)
    OP_68(-18400, 3500, -300, 0)
    MoveCamera(90, 23, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -19000, 2500, -600, 45)
    SetChrPos(0x102, -18200, 2500, -1400, 45)
    SetChrPos(0x103, -20000, 2500, -1600, 45)
    SetChrPos(0x104, -19200, 2500, -2400, 45)
    OP_4B(0x23, 0xFF)
    SetChrFlags(0x23, 0x40)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -17700, 2500, 800, 180)
    OP_4B(0x24, 0xFF)
    SetChrFlags(0x24, 0x40)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -17150, 2600, 100, 270)
    SetChrChipByIndex(0x25, 0x1E)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, -17600, 500, -10200, 0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis056.itp")
    CreatePortrait(1, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis057.itp")
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
    TurnDirection(0x23, 0x101, 300)

    #C0262
    ChrTalk(
        0x23,
        "#3605F#5P各位……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)
    Sleep(300)

    #C0263
    ChrTalk(
        0x24,
        "#5P#3708F啊……！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0264
    ChrTalk(
        0x101,
        (
            "#12P#0001F真是好久不见了。\x02\x03",

            "那个，二位是不是在欣赏游行的时候\x01",
            "不小心和孩子走散了呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x24,
        (
            "#5P#3701F正、正是如此……！\x02\x03",

            "#3710F都因为我太不小心，\x01",
            "所以那孩子……柯林他才……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x24, 400)
    Sleep(150)

    #C0266
    ChrTalk(
        0x23,
        "#3608F索菲亚，冷静一点。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x101, 500)

    #C0267
    ChrTalk(
        0x23,
        (
            "#3603F#5P──不好意思，各位。\x02\x03",

            "#3601F我们和孩子走散，大概是在三小时之前……\x02\x03",

            "正好是游行队伍通过这个广场，\x01",
            "我们正在专心观看的时候。\x02\x03",

            "与孩子走散之后，妻子马上就察觉到了，\x01",
            "然后我们两个人在这附近仔细\x01",
            "搜索了一遍，但却毫无发现……\x02\x03",

            "#3610F不得已之下……\x01",
            "就只能来麻烦警察帮忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        "#0102F没那回事，您愿意来找我们商量，是我们的荣幸。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0269
    ChrTalk(
        0x102,
        (
            "#0101F#11P──在这种情况下，我们\x01",
            "显然还是分头搜寻比较好吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5486():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5486)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0270
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯，正在巡逻的警官\x01",
            "目前好像也很忙。\x02\x03",

            "#0001F既然如此……\x01",
            "确实是有必要考虑分工协作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x103,
        "#12P#0203F是啊……\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        (
            "#0300F好啦，大家分头搜寻，其间一定要\x01",
            "保持通讯联络，这是很重要的。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x24,
        (
            "#5P#3707F请、请让我也来帮忙吧！\x02\x03",

            "不然的话，那个孩子……柯林他……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x23,
        (
            "#3610F#5P……冷静一点啊。\x02\x03",

            "#3601F各位，我们就先返回\x01",
            "住宅街了。\x02\x03",

            "那一带的搜寻\x01",
            "就交给我们来负责吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_560D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_560D)
    Sleep(50)

    def lambda_561D():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_561D)
    Sleep(50)
    OP_93(0x104, 0x2D, 0x1F4)

    #C0275
    ChrTalk(
        0x101,
        (
            "#12P#0000F原来如此……\x01",
            "这确实是最有效率的做法。\x02\x03",

            "#0003F我们几个就分头行动，\x01",
            "把其它的街区全部搜寻一遍。\x02\x03",

            "#0001F另外……\x01",
            "您有没有带着什么能够当作\x01",
            "线索的东西呢？\x02\x03",

            "如果有照片自然最好。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0276
    ChrTalk(
        0x23,
        (
            "#3605F#5P啊，我们刚好将在纪念庆典中\x01",
            "拍的照片显像出来了！\x02\x03",

            "#3608F嗯，应该是放在这里……\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0277
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈罗德从怀中取出了\x01",
            "一枚装有照片的信封。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    #C0278
    ChrTalk(
        0x23,
        "#3601F#5P……就是这个！\x02",
    )

    CloseMessageWindow()

    def lambda_57D0():
        OP_9A(0xFE, 0x101, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_57D0)
    WaitChrThread(0x23, 1)

    def lambda_57E8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_57E8)

    def lambda_57F5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_57F5)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0279
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x327),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "共三张收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x327, 1)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    #A0280
    AnonymousTalk(
        0x102,
        "#0102F真可爱……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0281
    AnonymousTalk(
        0x103,
        (
            "#0202F#12P虽然是个男孩，\x01",
            "但长得好像女孩一样漂亮呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    def lambda_58D4():
        OP_96(0xFE, 0xFFFFBADC, 0x9C4, 0x320, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_58D4)
    WaitChrThread(0x23, 1)
    Sleep(300)
    SetChrSubChip(0x24, 0x0)
    Sleep(300)

    #C0282
    ChrTalk(
        0x24,
        "#5P#3710F呜呜……柯林……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x24, 500)

    #C0283
    ChrTalk(
        0x23,
        (
            "#3600F好啦，我们先回家，\x01",
            "然后等着柯林平安回来吧。\x02\x03",

            "说不定他会自己\x01",
            "回到家里呢……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x2)
    Sleep(300)

    #C0284
    ChrTalk(
        0x24,
        (
            "#11P#3707F可是……可是……！\x01",
            "如果再发生那时候的那种事……！\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x23,
        (
            "#3601F不会的……！\x01",
            "那种事情绝对不会再次发生的……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_59F9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_59F9)
    Sleep(50)
    OP_93(0x104, 0x2D, 0x1F4)

    #C0286
    ChrTalk(
        0x101,
        "#12P#0005F（那时候的事……？）\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x102,
        "#0108F（似乎有什么隐情呢……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x101, 300)

    #C0288
    ChrTalk(
        0x23,
        (
            "#3610F#5P……不好意思，\x01",
            "有些失态了。\x02\x03",

            "#3608F那个……\x01",
            "因为曾经发生过一些……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        "#12P#0004F哪里，请不用在意。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0290
    ChrTalk(
        0x101,
        (
            "#12P#0005F对了……除了照片之外，\x01",
            "还有没有什么柯林平时\x01",
            "经常使用的东西呢？\x02\x03",

            "#0000F我们那里还有警犬，\x01",
            "说不定能顺着气味找到他。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)

    #C0291
    ChrTalk(
        0x23,
        "#3605F#5P噢噢……！\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x24,
        (
            "#5P#3708F……那、那就请把这个拿去……！\x01",
            "这是那孩子经常带在身边的玩偶！\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0xFFFFD8F0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    Sleep(500)

    #A0293
    AnonymousTalk(
        0x103,
        (
            "#0205F#12P啊……\x01",
            "这不是『咪西』的玩偶吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0294
    AnonymousTalk(
        0x102,
        "#0103F那我们就先把这个借走啦。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0295
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x328),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x328, 1)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0296
    ChrTalk(
        0x104,
        (
            "#0303F好了，一味着急也没用。\x02\x03",

            "#0300F只要他还在市内，就肯定是安全的，\x01",
            "就把一切都放心交给我们吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x23,
        (
            "#3604F#5P是、是的，\x01",
            "非常感谢。\x02\x03",

            "#3601F那么，各位……\x01",
            "我儿子就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x23, 3, 0, 39)
    Sleep(200)
    Fade(250)
    SetChrChipByIndex(0x24, 0x20)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x1)
    SetChrPos(0x24, -17700, 2500, 100, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    BeginChrThread(0x24, 3, 0, 39)

    def lambda_5DAE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5DAE)
    Sleep(50)

    def lambda_5DBE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5DBE)
    Sleep(50)

    def lambda_5DCE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5DCE)
    Sleep(50)

    def lambda_5DDE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DDE)
    Sleep(3000)
    OP_68(-18350, 3500, -1750, 1200)

    def lambda_5DFF():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5DFF)
    Sleep(100)

    def lambda_5E0F():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5E0F)

    def lambda_5E1C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5E1C)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#0003F那么，接下来……\x01",
            "该怎么分工才好呢？\x02\x03",

            "#0000F在那之前……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#12P#0204F……嗯，\x01",
            "我把它叫来。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x23, 3)
    WaitChrThread(0x24, 3)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x103, 0x21)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sound(1205, 255, 95, 0)    #voice#Tio
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Sound(1206, 255, 95, 0)    #voice#Tio
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_24(0x348)
    Sound(820, 0, 100, 0)
    OP_0D()
    Sound(911, 0, 100, 0)
    Sleep(600)
    Sound(2054, 255, 100, 0)    #voice#Zeit
    Fade(500)
    OP_68(-18400, 3500, -2700, 0)
    MoveCamera(65, 29, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    OP_52(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x0, 0x25, 0x1E, 0xC8)

    def lambda_602F():
        OP_9D(0xFE, 0xFFFFB820, 0x9C4, 0xFFFFEF98, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_602F)
    Sound(854, 0, 100, 0)
    Sleep(600)
    SetChrSubChip(0x25, 0x1)
    Sound(43, 0, 100, 0)
    Sound(832, 0, 100, 0)
    Sleep(50)
    SetChrSubChip(0x25, 0x2)
    WaitChrThread(0x25, 1)
    SetChrChip(0x1, 0x25, 0x0, 0x0)
    SetChrChipByIndex(0x25, 0x1F)
    SetChrSubChip(0x25, 0x0)

    def lambda_6080():
        OP_93(0xFE, 0x154, 0x190)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_6080)

    def lambda_608D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_608D)

    def lambda_609A():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_609A)

    def lambda_60A7():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_60A7)

    def lambda_60B4():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_60B4)
    WaitChrThread(0x25, 2)
    BeginChrThread(0x25, 1, 0, 38)
    Sleep(500)
    Sound(2052, 255, 100, 0)    #voice#Zeit
    Sleep(800)

    #C0300
    ChrTalk(
        0x25,
        "#11P#1200F呜噜噜……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#5P#0002F蔡特，你来了啊。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        "#5P#0102F呵呵，辛苦啦。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x25,
        (
            "#11P#1203F呜噜噜噜……\x02\x03",

            "#1200F……呜噜噜噜噜……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        (
            "#6P#0204F『……既然我来了，\x01",
            "  你们就彻底放下心吧。』\x02\x03",

            "『那个孩子的气味，\x01",
            "  我一定能完美地嗅到。』\x02\x01",

            "#0202F  ──它这样说。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0305
    ChrTalk(
        0x101,
        (
            "#5P#0012F帮、帮大忙了呢。\x02\x03",

            "#0000F可是，话说回来，它不是刚刚才来的吗，\x01",
            "为什么对事情了解得如此详细……？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#5P#0300F哎呀呀，还是老样子，\x01",
            "真是个深不可测的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#5P#0104F算啦，这些都无所谓。\x02",
    )

    CloseMessageWindow()
    OP_68(-19100, 3500, -1700, 1000)
    MoveCamera(75, 27, 0, 1000)
    Sleep(500)
    TurnDirection(0x102, 0x101, 500)
    OP_6F(0x79)

    #C0308
    ChrTalk(
        0x102,
        (
            "#11P#0100F克洛斯贝尔如此广阔……\x01",
            "我们要如何分工搜索呢？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_635D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_635D)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0309
    ChrTalk(
        0x103,
        (
            "#12P#0204F我和蔡特同行。\x02\x03",

            "#0202F毕竟还是让能够和它沟通的人\x01",
            "与它一起行动比较好吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0310
    ChrTalk(
        0x101,
        (
            "#0003F#5P有道理……\x02\x03",

            "#0000F这样的话，这个玩偶\x01",
            "就交给缇欧吧。\x02\x03",

            "让蔡特通过它来\x01",
            "探寻柯林的气味吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        "#12P#0204F……了解。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0312
    ChrTalk(
        0x101,
        (
            "#0003F#5P我们三个人就来分配一下任务，\x01",
            "各自去不同的街区搜索吧。\x02\x03",

            "#0000F我负责的区域从欢乐街开始，然后是\x01",
            "后巷、中央广场、站前街道，最后是西街。\x02\x03",

            "#0004F兰迪负责东街和旧城区的全部区域。\x02\x03",

            "行政区和港湾区全部交给艾莉。\x02\x03",

            "#0000F──这样分如何？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        (
            "#11P#0105F啊呀，好像只有你负责\x01",
            "的区域相当广阔呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0002F#5P不，行政区和港湾区也很大，\x01",
            "旧城区的地形结构又比较复杂。\x02\x03",

            "相对的，我负责的这些区域\x01",
            "都是比较好走的地方，\x01",
            "总体来说，大家的难度都比较均衡。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#11P#0102F原来如此……\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#0304F好啦，那我们就赶快按照这种\x01",
            "分工方式开始搜寻吧。\x02\x03",

            "#0300F如果取得了什么进展，\x01",
            "只要使用导力通讯进行联络就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#0000F#5P嗯，就那么办。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        (
            "#12P#0202F那么，搜索柯林\x01",
            "的任务就正式开始了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    StopBGM(0xFA0)
    WaitBGM()
    ReplaceBGM("ed7000", "ed7000")
    ReplaceBGM("ed7100", "ed7103")
    ReplaceBGM("ed7101", "ed7103")
    RemoveParty(0x1, 0x0)
    RemoveParty(0x2, 0x0)
    RemoveParty(0x3, 0x0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x348)
    SetScenarioFlags(0x5C, 0)
    NewScene("c040C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_500A end

    def Function_38_6747(): pass

    label("Function_38_6747")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6765")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_38_6747")

    label("loc_6765")

    Return()

    # Function_38_6747 end

    def Function_39_6766(): pass

    label("Function_39_6766")

    OP_92(0xFE, 0xFFFFB7BC, 0x9C4, 0x1F4)

    def lambda_6778():
        OP_95(0xFE, -18500, 2500, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6778)
    WaitChrThread(0xFE, 1)

    def lambda_6796():
        OP_95(0xFE, -18500, 2500, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6796)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_6766 end

    def Function_40_67B0(): pass

    label("Function_40_67B0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(885)
    Sound(885, 2, 90, 0)
    FadeToBright(2000, 0)
    LoadEffect(0x7, "event\\ev308_00.eff")
    LoadEffect(0x1, "event\\ev308_01.eff")
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 10930, 2500, 15620, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 4860, 2410, 19070, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 14320, 2410, 9830, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 10930, 2500, 15620, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 4860, 2410, 19070, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x7, 0xFF, 0xFF, 0x0, 14320, 2410, 9830, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_68(-2080, 5260, 6650, 0)
    MoveCamera(58, -2, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(27500, 0)
    OP_68(-2080, 12900, 6650, 8000)
    MoveCamera(33, -15, 0, 8000)
    OP_6E(620, 8000)
    SetCameraDistance(27500, 8000)
    Sleep(1000)
    Sound(856, 0, 100, 0)
    Sleep(6000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x375)
    SetScenarioFlags(0x5C, 3)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_40_67B0 end

    def Function_41_69C5(): pass

    label("Function_41_69C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-18000, 3600, 26700, 0)
    MoveCamera(50, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x101, -18400, 3100, 31000, 180)
    SetChrPos(0x102, -17600, 3100, 31000, 180)
    SetChrPos(0x103, -18400, 3100, 31000, 180)
    SetChrPos(0x104, -17600, 3100, 31000, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_4B(0xC, 0xFF)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    SetCameraDistance(20000, 3000)
    FadeToBright(1000, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)

    def lambda_6AE4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6AE4)

    def lambda_6AF5():
        OP_96(0xFE, 0xFFFFB758, 0x9C4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AF5)
    Sleep(400)

    def lambda_6B12():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6B12)

    def lambda_6B23():
        OP_96(0xFE, 0xFFFFBC08, 0x9C4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6B23)
    Sleep(400)

    def lambda_6B40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6B40)

    def lambda_6B51():
        OP_96(0xFE, 0xFFFFB758, 0x9C4, 0x6B08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_6B51)
    Sleep(400)

    def lambda_6B6E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6B6E)

    def lambda_6B7F():
        OP_96(0xFE, 0xFFFFBC08, 0x9C4, 0x6B08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6B7F)
    WaitChrThread(0x101, 1)
    OP_71(0x1, 0xA, 0x0, 0x0, 0x0)
    Sound(107, 0, 100, 0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_6C1A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6C1A)
    Sleep(50)

    def lambda_6C2A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6C2A)

    #C0319
    ChrTalk(
        0x101,
        "#5P#0005F噢。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x102,
        (
            "#0105F#11P啊呀……\x01",
            "又有紧急请求了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        "#5P#0001F嗯～……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x7)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0322
    AnonymousTalk(
        0x101,
        "#0001F您好，我是罗伊德。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年的声音")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "噢，看来号码对啦。\x02\x03",

            "哎呀～\x01",
            "总之能打通就好。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0324
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F那个……您是哪位呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年的声音")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈……听了我的声音\x01",
            "难道还想不起来吗～\x02\x03",

            "我是约纳啦，约纳。\x01",
            "天才少年，约纳·塞克里德。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 42)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0326
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0014F#30W什么啊，是你吗─#800W─",
            "#0007F#20W#4S不对，等一下！\x02\x03",    #line#50

            "#3S#0007F为什么你会\x01",
            "知道这个号码啊！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0327
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，那还用说，自然是从\x01",
            "警察局的数据库里查到的啊。\x02\x03",

            "哈～警察局的安全系统\x01",
            "根本就是形同虚设吧？\x02\x03",

            "不过，关键的机密资料\x01",
            "倒是没有放在里面呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0328
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F你、你可真是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0329
    AnonymousTalk(
        0x104,
        "#0305F是谁啊，怎么了？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sleep(300)

    #C0330
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯……\x01",
            "就是那个黑客小鬼啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        "#0105F#11P哎？\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#0211F#5P那孩子还真是的……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0333
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F──那么，有什么事吗？\x02\x03",

            "#0001F该不会只是为了炫耀\x01",
            "一下你的黑客技术吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "也有一点这方面的想法啦，不过呢～\x02\x03",

            "主要还是想问问，你们是否\x01",
            "愿意接受我的委托～就是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0335
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F什么……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，准确地说，只是想\x01",
            "请缇欧帮个忙啦。\x02\x03",

            "所以觉得姑且也应该先\x01",
            "征求一下你们的同意。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0337
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0013F那个……\x01",
            "我们可是很忙的。\x02\x03",

            "如果是纯私人性质的委托，\x01",
            "可是会断然拒绝的。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，要说私人性质，\x01",
            "也确实是私人性质的委托，不过呢……\x02\x03",

            "报酬可是相当可观的哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0339
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F我们可不是游击士。\x02\x03",

            "并不打算直接收取\x01",
            "委托人的报酬。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，真是的，自命清高。\x02\x03",

            "不过，虽说是报酬，\x01",
            "但也并非米拉哦。\x02\x03",

            "如果是储存了你们所需情报的\x01",
            "『记录结晶』……\x02\x03",

            "又如何呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0341
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001F………………………………\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("约纳的声音")

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "哈，很好的反应。\x02\x03",

            "算啦，总而言之，\x01",
            "就先到我这里来吧。\x02\x03",

            "详细情况到时再说。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0343
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F……明白了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0344
    ChrTalk(
        0x102,
        "#0105F#11P那个，怎么了呢？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 500)

    #C0345
    ChrTalk(
        0x101,
        "#6P#0003F是这样的……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0346
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将约纳说的话转告了艾莉等人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0347
    ChrTalk(
        0x102,
        "#0103F#11P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#0306F真是的，好一个乱来的小鬼。\x02\x03",

            "#0301F而且，他的确是\x01",
            "掌握了我们的软肋呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x103,
        (
            "#0203F#5P……不过，我觉得\x01",
            "还是去一趟比较好呢。\x02\x03",

            "#0202F他似乎需要我的帮助，\x01",
            "反过来想的话，我们或许\x01",
            "也能借此发现他的软肋呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_75FC():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_75FC)
    Sleep(50)

    def lambda_760C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_760C)
    Sleep(50)

    def lambda_761C():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_761C)
    Sleep(300)

    #C0350
    ChrTalk(
        0x101,
        (
            "#12P#0012F啊，倒也没必要\x01",
            "这样算计来算计去的……\x02\x03",

            "#0005F话说回来，他为什么\x01",
            "不直接联络缇欧呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        (
            "#0204F#5P大概是因为不甘心吧。\x02\x03",

            "前天和我玩方块对战的时候，\x01",
            "他刚输了个落花流水。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0352
    ChrTalk(
        0x101,
        "#12P#0012F是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x102,
        (
            "#0102F#11P虽然不太了解\x01",
            "那个什么方块对战……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x104,
        (
            "#11P#0302F但那个小鬼在阿缇面前\x01",
            "根本就抬不起头，这是一定的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#0206F#5P因为他实在是太过天真了。\x02\x03",

            "#0202F总之，如果没有其它要事，\x01",
            "我们就去约纳那里看看吧。\x02\x03",

            "就我个人而言，也有些在意\x01",
            "他的委托内容呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#12P#0000F说得也是……去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -18000, 2500, 26000, 180)
    OP_4C(0xC, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    SetScenarioFlags(0xA0, 3)
    OP_29(0x44, 0x1, 0x4)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_41_69C5 end

    def Function_42_78A4(): pass

    label("Function_42_78A4")

    Sleep(900)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Return()

    # Function_42_78A4 end

    def Function_43_78B9(): pass

    label("Function_43_78B9")

    EventBegin(0x0)
    OP_4B(0xB, 0xFF)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(5880, 4740, -10040, 0)
    MoveCamera(7, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(12150, 0)
    SetChrPos(0x101, 5420, 2500, -7460, 45)
    SetChrPos(0x102, 5120, 2500, -9330, 45)
    SetChrPos(0x103, 6250, 2500, -8390, 45)
    SetChrPos(0x104, 4250, 2500, -8350, 45)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0357
    ChrTalk(
        0xB,
        (
            "#11P欢迎光临～\x01",
            "感谢您惠顾『库罗玛的果汁店』～\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#6P#0005F啊，这里……\x01",
            "好像是盗窃事件的受害店铺吧？\x02\x03",

            "#0001F可以向您打听一下，\x01",
            "事件的详细情况吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0359
    ChrTalk(
        0xB,
        (
            "#11P是、是这样的。\x01",
            "我只是稍微大意了一下，\x01",
            "然后就被盗了……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xB,
        "#11P唉，这下销售额可就……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x103,
        "#12P#0200F对犯人有没有什么印象？\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xB,
        (
            "#11P这个嘛，有些记不清了……\x01",
            "我当时正在专心接待客人呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xB,
        (
            "#11P然后来了一个态度轻浮的青年……\x01",
            "大概是从外国来的游客吧。\x01",
            "被他搭讪纠缠了半天。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xB,
        (
            "#11P然后，就在我努力回绝他的时候，\x01",
            "从后面传来了声音……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x104,
        "#6P#0303F大概就是趁着这个机会偷盗得手的吧……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xB,
        (
            "#11P嗯嗯，我当时虽然也\x01",
            "尽量小心了，但是……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x102,
        "#12P#0101F（看来是个很棘手的犯人呢……）\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DBF")
    OP_68(5210, 4740, -10040, 1200)
    MoveCamera(12, 25, 0, 1200)

    def lambda_7C45():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7C45)

    def lambda_7C52():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7C52)

    def lambda_7C5F():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7C5F)

    def lambda_7C6C():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7C6C)
    Sleep(1200)

    #C0368
    ChrTalk(
        0x101,
        "#5P#0003F询问工作就到此为止吧……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x104,
        (
            "#6P#0300F是啊，差不多也该回去\x01",
            "整理一下情报了。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_7DB9")

    #C0370
    ChrTalk(
        0x102,
        (
            "#12P#0100F工商协会那边也没有和我们联络，\x01",
            "看样子，似乎还没有\x01",
            "出现新的案情呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        (
            "#12P#0203F是啊。\x02\x03",

            "#0200F……慎重起见，\x01",
            "在回去的路上，顺便再留意\x01",
            "一下那些露天店铺吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7DB9")

    OP_29(0x20, 0x1, 0xD)

    label("loc_7DBF")

    OP_5A()
    SetChrPos(0x0, 5330, 2500, -8020, 56)
    OP_4C(0xB, 0xFF)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_43_78B9 end

    def Function_44_7DF6(): pass

    label("Function_44_7DF6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x28)
    SoundLoad(806)
    OP_68(-11530, 4730, 9500, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14790, 0)
    SetChrPos(0x101, -15600, 2500, -6960, 0)
    SetChrPos(0x102, -14420, 2500, -7260, 0)
    SetChrPos(0x103, -15590, 2500, -8090, 0)
    SetChrPos(0x104, -14590, 2500, -8690, 0)
    SetChrPos(0x26, -11470, 2500, 8720, 0)
    SetChrPos(0x27, 6590, 2500, 4100, 135)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0x26, 0xC)
    SetChrSubChip(0x26, 0x0)
    SetChrChipByIndex(0x27, 0x4)
    SetChrSubChip(0x27, 0x0)
    BeginChrThread(0x26, 0, 0, 0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrName("")

    #A0372
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人前往目标街区，\x01",
            "随后埋伏了下来。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-11530, 3730, 9500, 2800)
    PlayBGM("ed7111", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(2000, 0)
    BeginChrThread(0xE, 1, 0, 45)
    Sleep(150)
    BeginChrThread(0x26, 1, 0, 45)
    OP_0D()
    SoundDistance(0x7B, 0xFFFFB32A, 0x99C, 0xFFFFC324, 0x2710, 0x186A0, 0x64, 0x0)
    OP_6F(0x1)

    #A0373
    AnonymousTalk(
        0x101,
        (
            "#0001F………………………………\x02\x03",

            "看来不是这位客人呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x26, 0x1)
    OP_64(0xE)
    OP_64(0x26)
    Sleep(200)
    OP_95(0x26, -6710, 2390, 7920, 1500, 0x0)

    def lambda_7FC8():
        OP_95(0xFE, 600, 2500, 1580, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_7FC8)
    OP_95(0x27, -4270, 2390, 9110, 2000, 0x0)
    OP_95(0x27, -11420, 2500, 8680, 2000, 0x0)
    OP_93(0x27, 0x0, 0x190)
    BeginChrThread(0xE, 1, 0, 45)
    Sleep(150)
    BeginChrThread(0x27, 1, 0, 45)
    Sleep(2500)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x27, 0x1)
    OP_64(0xE)
    OP_64(0x27)
    Sleep(200)
    OP_95(0x27, -19340, 2420, 12410, 2000, 0x0)
    OP_95(0x27, -23170, 2390, 16300, 2000, 0x0)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)

    #A0374
    AnonymousTalk(
        0x104,
        "#0306F还不来啊……\x02",
    )

    CloseMessageWindow()

    #A0375
    AnonymousTalk(
        0x103,
        (
            "#0200F都已经在这里\x01",
            "埋伏了一个多小时了……\x02",
        )
    )

    CloseMessageWindow()

    #A0376
    AnonymousTalk(
        0x101,
        (
            "#0003F真奇怪啊，都这么久了，\x01",
            "也该来了吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sound(806, 2, 100, 0)
    Sleep(800)
    Fade(300)
    OP_68(-15360, 5070, -8180, 0)
    MoveCamera(37, 31, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(36070, 0)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    OP_0D()
    Sleep(500)
    OP_93(0x101, 0x10E, 0x190)
    Sleep(50)

    def lambda_813D():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_813D)

    def lambda_814A():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_814A)

    def lambda_8157():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8157)
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0377
    ChrTalk(
        0x101,
        (
            "#5P#0000F您好，我是罗伊德·班宁斯──\x02\x03",

            "#0005F哎，盗窃犯出现了……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0378
    ChrTalk(
        0x101,
        (
            "#5P#0001F好、好，是中央广场对吧。\x02\x03",

            "明白了，我们马上就过去！\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(807, 0, 100, 0)
    OP_0D()
    TurnDirection(0x101, 0x104, 400)
    Sleep(200)

    #C0379
    ChrTalk(
        0x101,
        (
            "#5P#0003F……抱歉，各位。\x01",
            "看来是我计算错误了。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        "#11P#0101F别说这些了，赶快出发吧，罗伊德！\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#5P#0001F也、也是啊。\x01",
            "当务之急是赶往现场！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8331():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8331)

    def lambda_833E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_833E)

    def lambda_834B():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_834B)

    def lambda_8358():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8358)
    Sleep(300)
    WaitChrThread(0x104, 1)

    def lambda_836C():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_836C)

    def lambda_8381():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8381)

    def lambda_8396():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8396)

    def lambda_83AB():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_83AB)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    ClearScenarioFlags(0x2, 0)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_7DF6 end

    def Function_45_83DB(): pass

    label("Function_45_83DB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8400")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_45_83DB")

    label("loc_8400")

    Return()

    # Function_45_83DB end

    def Function_46_8401(): pass

    label("Function_46_8401")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0382
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　※　新市政厅大楼建设中　※\x01",
            "除工程相关人员之外，一律禁止入内。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_8401 end

    def Function_47_847B(): pass

    label("Function_47_847B")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "国际研讨会\x01",
            "『～克洛斯贝尔的现状和未来～』\x01",
            "  八位有识之士共同探讨\x01",
            "           自治州的现在──\x02",
        )
    )

    CloseMessageWindow()

    #A0384
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　场所　：克洛斯贝尔市政厅\x01",
            "　　　　　宴会大厅\x01",
            "召开时间：纪念庆典第三日\x01",
            " 主办者 ：亨利·麦克道尔\x01",
            "※如欲旁听，需提前申请。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_847B end

    SaveToFile()

Try(main)
