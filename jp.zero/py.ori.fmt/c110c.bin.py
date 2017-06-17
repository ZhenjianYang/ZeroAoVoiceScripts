from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "フランツ巡査",           # 1
        "シャーナ",               # 2
        "アビー",                 # 3
        "クロマ",                 # 4
        "オットー",               # 5
        "タジク",                 # 6
        "デリック",               # 7
        "シーリィ",               # 8
        "ドノバン警部",           # 9
        "レイモンド捜査官",       # 10
        "ジョーリッジ課長",       # 11
        "アレサ",                 # 12
        "ステファン",             # 13
        "警官",                   # 14
        "セルゲイ課長",           # 15
        "ケイト巡査",             # 16
        "グレイス",               # 17
        "レインズ",               # 18
        "エステル",               # 19
        "ヨシュア",               # 20
        "遊撃士リン",             # 21
        "遊撃士エオリア",         # 22
        "見物客",                 # 23
        "見物客",                 # 24
        "見物客",                 # 25
        "見物客",                 # 26
        "警官",                   # 27
        "ハロルド",               # 28
        "ソフィア",               # 29
        "ツァイト",               # 30
        "客",                     # 31
        "客",                     # 32
        "中央広場",               # 33
        "西通り",                 # 34
        "行政区",                 # 35
        "住宅街",                 # 36
        "歓楽街",                 # 37
        "東通り",                 # 38
        "旧市街",                 # 39
        "港湾区",                 # 40
        "ＩＢＣ",                 # 41
        "駅前通り",               # 42
        "裏通り",                 # 43
        "ウルスラ間道",           # 44
        "東クロスベル街道",       # 45
        "西クロスベル街道",       # 46
        "マインツ山道",           # 47
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

    PlaceName(-31.530000686645508, 0.0, -107.9000015258789, 0x0000, 0x0000, "中央広場")
    PlaceName(-117.0, 0.0, -102.05000305175781, 0x0000, 0x0000, "西通り")
    PlaceName(3.5799999237060547, 0.0, 7.800000190734863, 0x0000, 0x0000, "行政区")
    PlaceName(-196.3000030517578, 0.0, -5.199999809265137, 0x0000, 0x0000, "住宅街")
    PlaceName(-101.4000015258789, 0.0, -15.600000381469727, 0x0000, 0x0000, "歓楽街")
    PlaceName(74.0999984741211, 0.0, -137.8000030517578, 0x0000, 0x0000, "東通り")
    PlaceName(120.25, 0.0, -209.3000030517578, 0x0000, 0x0000, "旧市街")
    PlaceName(110.5, 0.0, -52.0, 0x0000, 0x0000, "港湾区")
    PlaceName(76.69999694824219, 0.0, 70.19999694824219, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-16.899999618530273, 0.0, -197.60000610351562, 0x0000, 0x0000, "駅前通り")
    PlaceName(-78.0, 0.0, -62.400001525878906, 0x0000, 0x0000, "裏通り")
    PlaceName(-20.799999237060547, 0.0, -237.89999389648438, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(144.3000030517578, 0.0, -119.5999984741211, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-183.3000030517578, 0.0, -104.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-175.5, 0.0, 26.0, 0x0000, 0x0000, "マインツ山道")
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
        "Function_7_10B2",         # 07, 7
        "Function_8_13F0",         # 08, 8
        "Function_9_1463",         # 09, 9
        "Function_10_158C",        # 0A, 10
        "Function_11_1B6A",        # 0B, 11
        "Function_12_1FDB",        # 0C, 12
        "Function_13_2129",        # 0D, 13
        "Function_14_298D",        # 0E, 14
        "Function_15_30B1",        # 0F, 15
        "Function_16_3261",        # 10, 16
        "Function_17_35E6",        # 11, 17
        "Function_18_36C4",        # 12, 18
        "Function_19_3782",        # 13, 19
        "Function_20_3905",        # 14, 20
        "Function_21_39CF",        # 15, 21
        "Function_22_3BB1",        # 16, 22
        "Function_23_3C22",        # 17, 23
        "Function_24_3E17",        # 18, 24
        "Function_25_3FBF",        # 19, 25
        "Function_26_418E",        # 1A, 26
        "Function_27_4353",        # 1B, 27
        "Function_28_4588",        # 1C, 28
        "Function_29_4678",        # 1D, 29
        "Function_30_4946",        # 1E, 30
        "Function_31_4A0F",        # 1F, 31
        "Function_32_4BA0",        # 20, 32
        "Function_33_4D5E",        # 21, 33
        "Function_34_4F02",        # 22, 34
        "Function_35_4F8A",        # 23, 35
        "Function_36_53A8",        # 24, 36
        "Function_37_5662",        # 25, 37
        "Function_38_6F27",        # 26, 38
        "Function_39_6F46",        # 27, 39
        "Function_40_6F90",        # 28, 40
        "Function_41_71A5",        # 29, 41
        "Function_42_81E8",        # 2A, 42
        "Function_43_81FD",        # 2B, 43
        "Function_44_875C",        # 2C, 44
        "Function_45_8D6F",        # 2D, 45
        "Function_46_8D95",        # 2E, 46
        "Function_47_8E0F",        # 2F, 47
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_F60")

    #C0001
    ChrTalk(
        0xFE,
        "駅の方は大変混雑しています。\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "落し物、迷子などには\x01",
            "お気をつけくださ～い！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AE")

    label("loc_F60")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_FD0")

    #C0003
    ChrTalk(
        0xFE,
        (
            "パレードの誘導のために\x01",
            "街中を走り回ってきた所なんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "ぜえ、ぜえ……\x01",
            "つ、疲れたぜ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AE")

    label("loc_FD0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1051")

    #C0005
    ChrTalk(
        0xFE,
        (
            "パレードの警備は\x01",
            "オレたち広域防犯課が\x01",
            "一手に担ってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "……この人ごみだし\x01",
            "道を確保するのも大変だよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_10AE")

    label("loc_1051")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_105F")
    Jump("loc_10AE")

    label("loc_105F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_10AE")

    #C0007
    ChrTalk(
        0xFE,
        "ぴっぴー！　押さないで下さい！\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        "車の前に飛び出さないように！\x02",
    )

    CloseMessageWindow()

    label("loc_10AE")

    TalkEnd(0xFE)
    Return()

    # Function_6_EFC end

    def Function_7_10B2(): pass

    label("Function_7_10B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_11D3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1158")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    #C0009
    ChrTalk(
        0xFE,
        (
            "アビーったら……\x01",
            "もう疲れちゃったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "よーしっ、それなら\x01",
            "ママがおんぶしてあげる！\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xA,
        (
            "ほ、ほんと～？\x01",
            "わーい！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    SetScenarioFlags(0x0, 0)
    Jump("loc_11CE")

    label("loc_1158")


    #C0012
    ChrTalk(
        0xFE,
        (
            "記念祭を毎日遊んでいたら\x01",
            "疲れてしまったみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "無理もないですね……\x01",
            "私もはしゃぎすぎたかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11CE")

    Jump("loc_13EC")

    label("loc_11D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_125F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11EE")
    Call(0, 8)
    Jump("loc_125A")

    label("loc_11EE")


    #C0014
    ChrTalk(
        0xFE,
        (
            "今年はいい思い出が\x01",
            "できたみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "ふふっ、クロスベルの記念祭って\x01",
            "とっても楽しいお祭りですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_125A")

    Jump("loc_13EC")

    label("loc_125F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_12C9")
    TurnDirection(0xFE, 0xA, 0)

    #C0016
    ChrTalk(
        0xFE,
        "ほら、あれがパレードよ。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "パッパーって音楽を流しながら\x01",
            "街中を回るんだから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13EC")

    label("loc_12C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_136A")
    OP_4B(0xA, 0xFF)
    TurnDirection(0xFE, 0xA, 0)

    #C0018
    ChrTalk(
        0xFE,
        "アビー、おいしい？\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "ママにも少し\x01",
            "わけてくれないかな～？\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        "うん、わけてあげるっ！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "ママぁ、いっしょに\x01",
            "たべようよ～！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_13EC")

    label("loc_136A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_13EC")

    #C0022
    ChrTalk(
        0xFE,
        (
            "私、今年に入って\x01",
            "引っ越してきたばかりなので\x01",
            "記念祭って初めてなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "すごいものですね……\x01",
            "驚いてしまいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13EC")

    TalkEnd(0xFE)
    Return()

    # Function_7_10B2 end

    def Function_8_13F0(): pass

    label("Function_8_13F0")

    OP_4B(0x9, 0xFF)
    OP_4B(0xA, 0xFF)
    TurnDirection(0x9, 0xA, 0)
    TurnDirection(0xA, 0x9, 0)

    #C0024
    ChrTalk(
        0x9,
        "パレード楽しかったねー！\x02",
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0025
    ChrTalk(
        0xA,
        "うんっ、たのしかったー！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_4C(0x9, 0xFF)
    OP_4C(0xA, 0xFF)
    Return()

    # Function_8_13F0 end

    def Function_9_1463(): pass

    label("Function_9_1463")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_149F")
    TurnDirection(0xFE, 0x9, 0)

    #C0026
    ChrTalk(
        0xFE,
        "ママぁ、なんだかねむいよぅ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_149F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_14B0")
    Call(0, 8)
    Jump("loc_1588")

    label("loc_14B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_14E1")

    #C0027
    ChrTalk(
        0xFE,
        (
            "ぱれーどぉ？\x01",
            "なあに、それー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_14E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_153C")

    #C0028
    ChrTalk(
        0xFE,
        (
            "ママにね、アイスクリーム\x01",
            "かってもらったんだ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "えへへ、おいしー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1588")

    label("loc_153C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1588")
    TurnDirection(0xFE, 0x9, 0)

    #C0030
    ChrTalk(
        0xFE,
        "すごーい、かみふぶき～！\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        "ねえママ、すごいねーっ！\x02",
    )

    CloseMessageWindow()

    label("loc_1588")

    TalkEnd(0xFE)
    Return()

    # Function_9_1463 end

    def Function_10_158C(): pass

    label("Function_10_158C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15B6")
    Call(0, 43)
    Return()

    label("loc_15B6")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15C3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B66")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1621")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1621")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1641")
    OP_AF(0x80)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1B61")

    label("loc_1641")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1655")
    Jump("loc_1B61")

    label("loc_1655")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B61")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17C4")

    #C0032
    ChrTalk(
        0xFE,
        (
            "窃盗犯が捕まったって\x01",
            "本当ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "よかった……これで\x01",
            "盗られたミラも戻ってきますね！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "あの、お礼にこれを\x01",
            "持って行ってください。\x02",
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
            "を貰った。\x02",
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
        "#0300Fおう、サンキュー。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "お世話になりました。\x01",
            "今度はお客さんとして来てくださいね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xBC, 7)
    Jump("loc_1B61")

    label("loc_17C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1894")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1837")

    #C0038
    ChrTalk(
        0xFE,
        (
            "今日も警察の人が\x01",
            "ドタバタしていますね……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "あ、そうか。\x01",
            "閉会式があるんですね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_188F")

    label("loc_1837")


    #C0040
    ChrTalk(
        0xFE,
        (
            "最終日も観光客の人が\x01",
            "多いみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "みなさん閉会式を\x01",
            "見に来たんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_188F")

    Jump("loc_1B61")

    label("loc_1894")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1950")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1920")

    #C0042
    ChrTalk(
        0xFE,
        (
            "あ、いけない……\x01",
            "オレンジカフェが\x01",
            "売り切れそうです……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "すみません、ご注文でしたら\x01",
            "お急ぎくださいませ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_194B")

    label("loc_1920")


    #C0044
    ChrTalk(
        0xFE,
        (
            "今日はホントに\x01",
            "大忙しでしたものね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_194B")

    Jump("loc_1B61")

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1A74")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_19CC")

    #C0045
    ChrTalk(
        0xFE,
        (
            "丁度お客さんの対応中で……\x01",
            "油断してしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xFE,
        "はあ、売り上げが……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A6F")

    label("loc_19CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A35")

    #C0047
    ChrTalk(
        0xFE,
        (
            "そろそろパレードの車が\x01",
            "到着するそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xFE,
        "わ、私もドキドキしてきました。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A6F")

    label("loc_1A35")


    #C0049
    ChrTalk(
        0xFE,
        (
            "パレード、そろそろ\x01",
            "始まっちゃいますね、\x01",
            "ドキドキ……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A6F")

    Jump("loc_1B61")

    label("loc_1A74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1AF0")

    #C0050
    ChrTalk(
        0xFE,
        (
            "今日は市庁舎の方で\x01",
            "催し物があるそうなんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "ちょっとインテリな人たちが\x01",
            "朝から集まってきてますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B61")

    label("loc_1AF0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1B61")

    #C0052
    ChrTalk(
        0xFE,
        (
            "いらっしゃいませ、\x01",
            "いらっしゃいませー！\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "本当にお客さんが多い……\x01",
            "私もびっくりしてしまいます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B61")

    Jump("loc_15C3")

    label("loc_1B66")

    TalkEnd(0xFE)
    Return()

    # Function_10_158C end

    def Function_11_1B6A(): pass

    label("Function_11_1B6A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1BF6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BBE")

    #C0054
    ChrTalk(
        0xFE,
        "今日で最終日だな……\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        "遊びつくさねば……！！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1BF1")

    label("loc_1BBE")


    #C0056
    ChrTalk(
        0xFE,
        (
            "さあ、今日はどこを回る。\x01",
            "どこから回るんだ！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BF1")

    Jump("loc_1FD7")

    label("loc_1BF6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1CCB")

    #C0057
    ChrTalk(
        0xFE,
        "市長、ナイスな演説だった。\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "そしてナイス《みっしぃ》！\x02",
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
        "#0003F（な、なんの事だ……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1FD7")

    label("loc_1CCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1D91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D54")

    #C0060
    ChrTalk(
        0xFE,
        (
            "祭りだからと言って、\x01",
            "はしゃぎすぎは良くないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "人間、やはり自制心だ！\x01",
            "自制の心を忘れず、楽しめよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1D8C")

    label("loc_1D54")


    #C0062
    ChrTalk(
        0xFE,
        "……カメラは持ったかね？\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        "そろそろ始まるぞ！！\x02",
    )

    CloseMessageWindow()

    label("loc_1D8C")

    Jump("loc_1FD7")

    label("loc_1D91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1EE1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E6C")

    #C0064
    ChrTalk(
        0xFE,
        (
            "うおっほん、今日は市庁舎で\x01",
            "国際シンポジウムが開かれるのだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "市長の呼びかけに応え\x01",
            "国内外から集まった識者たち……！\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "彼らの討論は\x01",
            "必ずやクロスベルに\x01",
            "一筋の光をもたらすであろう！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1EDC")

    label("loc_1E6C")


    #C0067
    ChrTalk(
        0xFE,
        (
            "今日は市庁舎で\x01",
            "国際シンポジウムが開かれるのだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "……私はお堅いのは駄目でな。\x01",
            "直接傍聴はしないのだが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EDC")

    Jump("loc_1FD7")

    label("loc_1EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_1FD7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F65")

    #C0069
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の\x01",
            "出張オムライス……だと？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        (
            "そう言われると\x01",
            "食べてみないわけには\x01",
            "いかんではないか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1FD7")

    label("loc_1F65")


    #C0071
    ChrTalk(
        0xFE,
        (
            "私はこう、目の前で\x01",
            "ブラブラと気になる物が\x01",
            "垂れ下がっているのは嫌いなのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        "これはぜひ食べてみなければ。\x02",
    )

    CloseMessageWindow()

    label("loc_1FD7")

    TalkEnd(0xFE)
    Return()

    # Function_11_1B6A end

    def Function_12_1FDB(): pass

    label("Function_12_1FDB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1FEC")
    Jump("loc_2125")

    label("loc_1FEC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1FFA")
    Jump("loc_2125")

    label("loc_1FFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2008")
    Jump("loc_2125")

    label("loc_2008")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2016")
    Jump("loc_2125")

    label("loc_2016")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2125")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20D1")

    #C0073
    ChrTalk(
        0xFE,
        (
            "仕事の合間に\x01",
            "休憩に出たんだが……\x01",
            "ちっ、えらい騒ぎだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xFE,
        (
            "記念祭が終わって一週間もすれば\x01",
            "予算議会が始まるんだぜ？\x01",
            "こっちは浮かれてる場合じゃねえよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2125")

    label("loc_20D1")


    #C0075
    ChrTalk(
        0xFE,
        (
            "あー、くそ、腹が立ってきたぜ。\x01",
            "こっちは浮かれてる場合じゃ\x01",
            "ないってのによ～……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2125")

    TalkEnd(0xFE)
    Return()

    # Function_12_1FDB end

    def Function_13_2129(): pass

    label("Function_13_2129")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2136")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2989")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2194")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_2194")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B4")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2984")

    label("loc_21B4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21C8")
    Jump("loc_2984")

    label("loc_21C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2984")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_229D")

    #C0076
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "どうやらこれ以上の村への集客は\x01",
            "見込めなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "今年はもう潮時かもしれんな。\x01",
            "そろそろ店をたたむか……\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        (
            "君たち、何か欲しいなら\x01",
            "今のうちに言ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2984")

    label("loc_229D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2336")

    #C0079
    ChrTalk(
        0xFE,
        (
            "最終日に向けてのラストスパート……\x01",
            "今のうちに持ってきた分を\x01",
            "売り切ってしまおう。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xFE,
        (
            "君たちも何か買っていくか？\x01",
            "是非申し付けてくれ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2984")

    label("loc_2336")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2711")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_244A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FE")

    #C0081
    ChrTalk(
        0xFE,
        (
            "さっき連絡があってな、\x01",
            "連続窃盗犯が捕まったらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "クロスベル警察も\x01",
            "意外と頼りになるんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xFE,
        (
            "こんなに頼もしく感じたのは\x01",
            "はっきり言って初めてだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2445")

    label("loc_23FE")


    #C0084
    ChrTalk(
        0xFE,
        "これで店が続けられる……\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xFE,
        (
            "村の振興のためにも\x01",
            "頑張らないとな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2445")

    Jump("loc_270C")

    label("loc_244A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_268B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25F3")

    #C0086
    ChrTalk(
        0x101,
        (
            "#0001Fすみません、少しお話を\x01",
            "伺ってもいいですか？\x02\x03",

            "窃盗事件について\x01",
            "捜査をしているんですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        "ドキドキ……\x02",
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xFE,
        (
            "し、心配ない。\x01",
            "この店は警察本部のすぐ前だしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "しかし、近くの\x01",
            "店舗がやられたとなると\x01",
            "緊張するな……\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x102,
        (
            "#0101F（ここの屋台の人は\x01",
            "  大分警戒しているみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#0003F（犯人に心当たりもなさそうだし、\x01",
            "  あまり話しかけないであげようか。）\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x9)
    Jump("loc_2686")

    label("loc_25F3")


    #C0092
    ChrTalk(
        0xFE,
        (
            "ドキドキ……\x01",
            "この店は警察本部のすぐ前なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xFE,
        (
            "し、心配ない。\x01",
            "絶対大丈夫だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#0003F（確かに本部の前なら\x01",
            "  犯人も狙えないよな……？）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2686")

    Jump("loc_270C")

    label("loc_268B")


    #C0095
    ChrTalk(
        0xFE,
        (
            "アルモリカ村の方から\x01",
            "連絡があってな。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "向こうにも観光客が\x01",
            "訪れているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "このまま村が\x01",
            "賑やかになればいいな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_270C")

    Jump("loc_2984")

    label("loc_2711")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2852")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27DD")

    #C0098
    ChrTalk(
        0xFE,
        "村の特産品の売り上げは上々だな。\x02",
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "村の方に向かう観光客も\x01",
            "ちらほら見かける。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "まだ記念祭は２日間残っているが、\x01",
            "村を活性化させる目的は\x01",
            "充分果たせたといえるだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_284D")

    label("loc_27DD")


    #C0101
    ChrTalk(
        0xFE,
        (
            "村の特産品を売り、\x01",
            "観光客を集める……\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "記念祭は２日間残っているが、\x01",
            "目的は充分果たせたといえるだろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_284D")

    Jump("loc_2984")

    label("loc_2852")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_2984")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_290F")

    #C0103
    ChrTalk(
        0xFE,
        (
            "こちら、アルモリカ名物の\x01",
            "高純度ハチミツです。\x01",
            "よろしければ試食してみてください。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "このハチミツを作っている\x01",
            "アルモリカ村へは\x01",
            "東口の導力バスで行けますよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2984")

    label("loc_290F")


    #C0105
    ChrTalk(
        0xFE,
        (
            "アルモリカ村は\x01",
            "広大な自然に囲まれた\x01",
            "のどかな村です。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0xFE,
        (
            "記念祭の喧騒に疲れたら、\x01",
            "是非足を運んでみてください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2984")

    Jump("loc_2136")

    label("loc_2989")

    TalkEnd(0xFE)
    Return()

    # Function_13_2129 end

    def Function_14_298D(): pass

    label("Function_14_298D")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_299A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30AD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",          # 0
            "買い物をする\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F8")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_29F8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A18")
    OP_AF(0x81)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_30A8")

    label("loc_2A18")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A2C")
    Jump("loc_30A8")

    label("loc_2A2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30A8")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2B6D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AE1")

    #C0107
    ChrTalk(
        0xFE,
        (
            "昨日よりは大分ラクになったけど、\x01",
            "まだまだ忙しいわね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0xFE,
        (
            "ま、今日を乗り切れば\x01",
            "村に帰れるんだし。\x01",
            "一丁、ふんばりますか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2B68")

    label("loc_2AE1")


    #C0109
    ChrTalk(
        0xFE,
        (
            "にしても、もう最終日かぁ……\x01",
            "あっという間の\x01",
            "都会生活だったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "ミシュラムに遊びに行けないのは\x01",
            "心残りだけど……ま、いっか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B68")

    Jump("loc_30A8")

    label("loc_2B6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2BF5")

    #C0111
    ChrTalk(
        0xFE,
        (
            "村の店の心配なんて\x01",
            "とりあえずどうでもいっか！\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "あっちはあっち！　こっちはこっち！\x01",
            "そして、あたしの担当はこっち！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30A8")

    label("loc_2BF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2E68")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_2CEF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C88")

    #C0113
    ChrTalk(
        0xFE,
        (
            "アルモリカ村名物、\x01",
            "特製オムライスはいかがっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "……ふう、頑張って\x01",
            "売り上げを挽回しなくっちゃね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2CEA")

    label("loc_2C88")


    #C0115
    ChrTalk(
        0xFE,
        (
            "……村の方は\x01",
            "今頃どうしてるかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "相変わらずキースくんあたりが\x01",
            "居座ってそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CEA")

    Jump("loc_2E63")

    label("loc_2CEF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D81")

    #C0117
    ChrTalk(
        0xFE,
        "じろっ……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "あなたたち、\x01",
            "怪しい人間じゃないわよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "ウ、ウチの店で何かしたら\x01",
            "すぐに捕まえるわよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2E63")

    label("loc_2D81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E01")

    #C0120
    ChrTalk(
        0xFE,
        "はぁ～疲れたっ！\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "お父さんに教えてもらったレシピで\x01",
            "なんとかやってたけど、\x01",
            "やっぱ一人はツラいわね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2E63")

    label("loc_2E01")


    #C0122
    ChrTalk(
        0xFE,
        (
            "……村の方は\x01",
            "今頃どうしてるかなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "相変わらずキースくんあたりが\x01",
            "居座ってそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E63")

    Jump("loc_30A8")

    label("loc_2E68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2FBE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F3B")

    #C0124
    ChrTalk(
        0xFE,
        (
            "今日も賑わってるわねぇ\x01",
            "クロスベル市は。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "びっくりしたのが、\x01",
            "ちょっと目を放した隙に\x01",
            "行列が出来てたことね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "はぁ、並んでまで御飯を食べるなんて\x01",
            "都会の人って変わってるなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2FB9")

    label("loc_2F3B")


    #C0127
    ChrTalk(
        0xFE,
        (
            "並んでまで御飯を食べるなんて\x01",
            "都会の人っておもしろいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "あたしだったらすぐ諦めて、\x01",
            "別のところ行っちゃうけどなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2FB9")

    Jump("loc_30A8")

    label("loc_2FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_30A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_304E")

    #C0129
    ChrTalk(
        0xFE,
        (
            "アルモリカ村名物、\x01",
            "宿酒場《トネリコ亭》の\x01",
            "料理ですよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "何かのついででいいので\x01",
            "是非食べてってくださいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_30A8")

    label("loc_304E")


    #C0131
    ChrTalk(
        0xFE,
        (
            "ふぅ、まさか私まで\x01",
            "駆り出されるとは\x01",
            "思わなかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xFE,
        "ま、楽しいからいっか。\x02",
    )

    CloseMessageWindow()

    label("loc_30A8")

    Jump("loc_299A")

    label("loc_30AD")

    TalkEnd(0xFE)
    Return()

    # Function_14_298D end

    def Function_15_30B1(): pass

    label("Function_15_30B1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_30C2")
    Jump("loc_325D")

    label("loc_30C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_30D0")
    Jump("loc_325D")

    label("loc_30D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_31EF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3184")

    #C0133
    ChrTalk(
        0xFE,
        (
            "遊撃士も、今日は市内に\x01",
            "人員を裂いているらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "そう来られちゃ仕方ねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "せめてパレードだけでも\x01",
            "俺たちが混乱なく進めねえとな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_31EA")

    label("loc_3184")


    #C0136
    ChrTalk(
        0xFE,
        (
            "遊撃士の目の前で\x01",
            "無様な真似は出来ねえからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xFE,
        (
            "制服警官と連携とって\x01",
            "混乱なく進めねえとなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31EA")

    Jump("loc_325D")

    label("loc_31EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_31FD")
    Jump("loc_325D")

    label("loc_31FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_325D")

    #C0138
    ChrTalk(
        0xFE,
        "よお、凄い人出だな。\x02",
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "あちこちでいざこざが起きてる。\x01",
            "お前らも注意しておけよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_325D")

    TalkEnd(0xFE)
    Return()

    # Function_15_30B1 end

    def Function_16_3261(): pass

    label("Function_16_3261")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3272")
    Jump("loc_35E2")

    label("loc_3272")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_32FB")

    #C0140
    ChrTalk(
        0xFE,
        (
            "パレードに付き添って\x01",
            "港湾区まで行ってきた\x01",
            "トコなんだよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xFE,
        (
            "あー、疲れた……\x01",
            "ジュースでも飲みたいトコだよね～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_35E2")

    label("loc_32FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3443")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33C8")

    #C0142
    ChrTalk(
        0xFE,
        "やあ、昨日は助かったよ～。\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "さすが、例の事件で\x01",
            "一課を出し抜いただけの\x01",
            "事はあるな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x101,
        (
            "#0012Fはは、いえ。\x01",
            "その事はもう……\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "なんだよ～、\x01",
            "照れることないのにさ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_343E")

    label("loc_33C8")


    #C0146
    ChrTalk(
        0xFE,
        (
            "オレたちもパレードの\x01",
            "警備に駆り出されたんだよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0xFE,
        (
            "やれやれ、しばらくは\x01",
            "忙しさから逃れられそうにないよ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_343E")

    Jump("loc_35E2")

    label("loc_3443")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3451")
    Jump("loc_35E2")

    label("loc_3451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_35E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3572")

    #C0148
    ChrTalk(
        0xFE,
        (
            "窃盗犯を追ってる所なんだよ。\x01",
            "毎年お祭り騒ぎに乗じて\x01",
            "悪さする奴が後を絶たないんだよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xFE,
        (
            "やれやれ、オレが\x01",
            "お仕置きしちゃうぞ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#0000Fな、なぜか楽しそうですね。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xFE,
        "あはは、そりゃまあね～。\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "お祭り中の窃盗犯なんて\x01",
            "ただの単純犯罪だからね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_35E2")

    label("loc_3572")


    #C0153
    ChrTalk(
        0xFE,
        (
            "こういう気兼ねのない\x01",
            "事件って好きなんだよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "議員とか背後関係とか\x01",
            "難しいことを考えなくていいし～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_35E2")

    TalkEnd(0xFE)
    Return()

    # Function_16_3261 end

    def Function_17_35E6(): pass

    label("Function_17_35E6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3689")

    #C0155
    ChrTalk(
        0xFE,
        (
            "そうか、今年は\x01",
            "パレードの車が多いんだったなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "えー、ひいふうみい……\x02",
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "うーむ、全然揃っとらんなぁ。\x01",
            "たしか７台あるはずだぞー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_36C0")

    label("loc_3689")


    #C0158
    ChrTalk(
        0xFE,
        (
            "パレードの車が揃わんと\x01",
            "警備体制が確認できんぞー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_36C0")

    TalkEnd(0xFE)
    Return()

    # Function_17_35E6 end

    def Function_18_36C4(): pass

    label("Function_18_36C4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36E2")
    Call(0, 19)
    Jump("loc_371D")

    label("loc_36E2")


    #C0159
    ChrTalk(
        0xFE,
        (
            "最終日は混むでしょうから\x01",
            "早めに引き上げるとしますか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_371D")

    Jump("loc_377E")

    label("loc_3722")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_377E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_373D")
    Call(0, 19)
    Jump("loc_377E")

    label("loc_373D")


    #C0160
    ChrTalk(
        0xFE,
        (
            "アルモリカ村のハチミツってすごいのね。\x01",
            "なんだか感動だわ～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_377E")

    TalkEnd(0xFE)
    Return()

    # Function_18_36C4 end

    def Function_19_3782(): pass

    label("Function_19_3782")

    OP_4B(0x13, 0xFF)
    OP_4B(0x14, 0xFF)
    TurnDirection(0x13, 0x14, 0)
    TurnDirection(0x14, 0x13, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3809")

    #C0161
    ChrTalk(
        0x13,
        (
            "さてと、パレードも堪能したし。\x01",
            "そろそろ村に帰りましょっか。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x14,
        "……うん、そうだねお母さん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_38F6")

    label("loc_3809")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_38F6")

    #C0163
    ChrTalk(
        0x13,
        (
            "まぁまぁ！　村の特産品、\x01",
            "結構売れてるみたいじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x13,
        (
            "ほらステファン、見てみなさい。\x01",
            "お家の隣でやってる\x01",
            "商店で売ってたハチミツよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x14,
        "へぇ～……すごいね。\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x13,
        (
            "もう、この子ったら\x01",
            "反応が薄いんだからっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x13, 0x0, 0x0)
    OP_93(0x14, 0x0, 0x0)

    label("loc_38F6")

    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    SetScenarioFlags(0x1, 1)
    SetScenarioFlags(0x1, 2)
    Return()

    # Function_19_3782 end

    def Function_20_3905(): pass

    label("Function_20_3905")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3957")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3923")
    Call(0, 19)
    Jump("loc_3952")

    label("loc_3923")


    #C0167
    ChrTalk(
        0xFE,
        (
            "なんだか村に\x01",
            "帰りたくなってきちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3952")

    Jump("loc_39CB")

    label("loc_3957")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_39CB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3972")
    Call(0, 19)
    Jump("loc_39CB")

    label("loc_3972")


    #C0168
    ChrTalk(
        0xFE,
        (
            "あのハチミツが売れてるの\x01",
            "初めて見たかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "……よく見たら結構美味しそうだよね。\x02",
    )

    CloseMessageWindow()

    label("loc_39CB")

    TalkEnd(0xFE)
    Return()

    # Function_20_3905 end

    def Function_21_39CF(): pass

    label("Function_21_39CF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3A5B")

    #C0170
    ChrTalk(
        0xFE,
        (
            "閉会式もここの\x01",
            "セレモニーホールで\x01",
            "執り行われる予定なのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        (
            "会場の警備に市民の誘導……\x01",
            "今日も仕事が山ほどあるぞ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BAD")

    label("loc_3A5B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3A69")
    Jump("loc_3BAD")

    label("loc_3A69")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3B10")

    #C0172
    ChrTalk(
        0xFE,
        (
            "出発が１０：００で\x01",
            "歓楽街到着は３０分後……\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "課長、アルカンシェル前は\x01",
            "特に人が多いはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0xFE,
        (
            "パレードを止めないよう\x01",
            "指示をお願いしますよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BAD")

    label("loc_3B10")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3BA4")

    #C0175
    ChrTalk(
        0xFE,
        (
            "今日は市庁舎のセレモニーホールで\x01",
            "シンポジウムが開かれるのだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xFE,
        (
            "あのマクダエル市長も参加なさる。\x01",
            "我々もしっかり警備せんとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BAD")

    label("loc_3BA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3BAD")

    label("loc_3BAD")

    TalkEnd(0xFE)
    Return()

    # Function_21_39CF end

    def Function_22_3BB1(): pass

    label("Function_22_3BB1")

    TalkBegin(0xFE)

    #C0177
    ChrTalk(
        0xFE,
        "今日はパレードがあるのよ。\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0xFE,
        (
            "ゆっくり徐行するとはいえ\x01",
            "人ごみの中を走るんだもの。\x01",
            "気が抜けないわ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_3BB1 end

    def Function_23_3C22(): pass

    label("Function_23_3C22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9F")

    #C0179
    ChrTalk(
        0xFE,
        (
            "#1006Fったく俺まで\x01",
            "呼び出すとはどういう了見だ。\x02\x03",

            "#1000F……おいお前ら、\x01",
            "俺の代わりに仕事しろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x101,
        (
            "#0003Fいや、こっちも\x01",
            "支援要請で忙しいので……\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x104,
        (
            "#0300Fつーかこんな時くらい\x01",
            "普通に働いたらどうよ。\x02",
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
            "#1000Fお前らはパレード整理の\x01",
            "面倒さが分かってねえから\x01",
            "そんな事が言えるんだ。\x02\x03",

            "#1006Fったく……\x01",
            "雑用ってレベルじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_3E13")

    label("loc_3D9F")


    #C0183
    ChrTalk(
        0xFE,
        (
            "#1003Fすぱー……\x01",
            "裏技使って抜け出すか。\x02\x03",

            "面倒すぎるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x103,
        (
            "#0203F課長、たまには大人らしく\x01",
            "仕事してください。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E13")

    TalkEnd(0xFE)
    Return()

    # Function_23_3C22 end

    def Function_24_3E17(): pass

    label("Function_24_3E17")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_3E53")

    #C0185
    ChrTalk(
        0xFE,
        (
            "今日で最終日か……\x01",
            "名残惜しいのう……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBB")

    label("loc_3E53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_3EBA")

    #C0186
    ChrTalk(
        0xFE,
        (
            "中央広場に行けば\x01",
            "たくさん店があったはずじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        "そう心配せんでもええはずじゃよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3FBB")

    label("loc_3EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_3F15")

    #C0188
    ChrTalk(
        0xFE,
        "今日は一大行事じゃよ。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xFE,
        (
            "これを見るために\x01",
            "田舎から出てきたんじゃー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBB")

    label("loc_3F15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_3F7F")

    #C0190
    ChrTalk(
        0xFE,
        (
            "『クロスベルの現在と未来』\x01",
            "……だったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0xFE,
        (
            "そんなシンポジウムが\x01",
            "開かれるらしいぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3FBB")

    label("loc_3F7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_3FBB")

    #C0192
    ChrTalk(
        0xFE,
        (
            "さすがクロスベルの市庁舎だ。\x01",
            "壮観、壮観……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3FBB")

    TalkEnd(0xFE)
    Return()

    # Function_24_3E17 end

    def Function_25_3FBF(): pass

    label("Function_25_3FBF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_4033")

    #C0193
    ChrTalk(
        0xFE,
        "最後に出店を回っておかなくちゃ。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "まずは特別おいしいっていう\x01",
            "何とか村のオムライスからね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_418A")

    label("loc_4033")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4092")

    #C0195
    ChrTalk(
        0xFE,
        (
            "カメラの感光クオーツが\x01",
            "切れちゃったのよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        "どこで買えばいいのかしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_418A")

    label("loc_4092")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_40E2")

    #C0197
    ChrTalk(
        0xFE,
        "先頭の車が出てきたわ～。\x02",
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        "ばっちり写真に収めなくっちゃ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_418A")

    label("loc_40E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4152")

    #C0199
    ChrTalk(
        0xFE,
        (
            "今日は市庁舎で\x01",
            "催し物があるそうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0xFE,
        (
            "さっきから職員さんたちが\x01",
            "沢山出入りしているみたい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_418A")

    label("loc_4152")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_418A")

    #C0201
    ChrTalk(
        0xFE,
        (
            "写真に撮っておかなくちゃ\x01",
            "いけないわねー！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_418A")

    TalkEnd(0xFE)
    Return()

    # Function_25_3FBF end

    def Function_26_418E(): pass

    label("Function_26_418E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_41F5")

    #C0202
    ChrTalk(
        0xFE,
        (
            "いや、ちょっと待て。\x01",
            "ミラに余裕が……\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "仕方ない、\x01",
            "ＩＢＣで下ろして来るか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434F")

    label("loc_41F5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4236")

    #C0204
    ChrTalk(
        0xFE,
        (
            "さすがクロスベルの祭りだ！\x01",
            "大したもんだなぁ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434F")

    label("loc_4236")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4297")

    #C0205
    ChrTalk(
        0xFE,
        (
            "俺の勘によると\x01",
            "パレードはこっちから来る。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        "おいお前、カメラを構えるんだ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_434F")

    label("loc_4297")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_42F3")

    #C0207
    ChrTalk(
        0xFE,
        (
            "今日は警察の人が\x01",
            "ウロウロしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "ハッハーッ！\x01",
            "何かあるのか～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_434F")

    label("loc_42F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_434F")

    #C0209
    ChrTalk(
        0xFE,
        "さあて、遊ぶぜ～い！\x02",
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "祭りだ！　クロスベルだ！\x01",
            "とことん楽しまねえとなぁ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_434F")

    TalkEnd(0xFE)
    Return()

    # Function_26_418E end

    def Function_27_4353(): pass

    label("Function_27_4353")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_43B5")

    #C0211
    ChrTalk(
        0xFE,
        "今日はショッピングに行くのよ。\x02",
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xFE,
        (
            "絶対行くの！\x01",
            "これだけは譲れないから！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4584")

    label("loc_43B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_4430")

    #C0213
    ChrTalk(
        0xFE,
        (
            "お祭りに来たのはいいけど\x01",
            "まだ一度も\x01",
            "ショッピングしてないわ……\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0xFE,
        (
            "むきぃ！\x01",
            "私はお買い物がしたいの！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4584")

    label("loc_4430")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_449C")

    #C0215
    ChrTalk(
        0xFE,
        (
            "ああん、午前中に\x01",
            "百貨店に行きたかったのに～。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0xFE,
        (
            "もうパレードが\x01",
            "始まっちゃうじゃない！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4584")

    label("loc_449C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_4518")

    #C0217
    ChrTalk(
        0xFE,
        (
            "あんたね～、ショッピングに\x01",
            "連れてってくれる約束じゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0xFE,
        (
            "どうして出店を回ってる\x01",
            "だけなのよ～っ！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4584")

    label("loc_4518")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4584")

    #C0219
    ChrTalk(
        0xFE,
        "ショッピングよ、ショッピング！\x02",
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0xFE,
        (
            "観光なんて後回しでいいの！\x01",
            "記念祭セールを楽しまなくちゃ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4584")

    TalkEnd(0xFE)
    Return()

    # Function_27_4353 end

    def Function_28_4588(): pass

    label("Function_28_4588")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_45E8")

    #C0221
    ChrTalk(
        0xFE,
        "本日も大忙し、であります！\x02",
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xFE,
        (
            "皆さんも任務、\x01",
            "頑張って下さいであります！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4674")

    label("loc_45E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_45F6")
    Jump("loc_4674")

    label("loc_45F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4604")
    Jump("loc_4674")

    label("loc_4604")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_466B")

    #C0223
    ChrTalk(
        0xFE,
        (
            "本日は先輩と２人で\x01",
            "警備を行う事になったのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        "気が引き締まる思いであります！\x02",
    )

    CloseMessageWindow()
    Jump("loc_4674")

    label("loc_466B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4674")

    label("loc_4674")

    TalkEnd(0xFE)
    Return()

    # Function_28_4588 end

    def Function_29_4678(): pass

    label("Function_29_4678")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_47BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_470D")

    #C0225
    ChrTalk(
        0x18,
        (
            "#2100Fあ、そうそう。\x01",
            "写真の方は十分撮れたら\x01",
            "通信社の受付に渡しちゃって。\x02\x03",

            "よろしく頼んだからね～♪\x02",
        )
    )

    CloseMessageWindow()
    ClearScenarioFlags(0x1, 4)
    Jump("loc_47B9")

    label("loc_470D")


    #C0226
    ChrTalk(
        0x18,
        (
            "#2100F今年のパレードは\x01",
            "過去最大の人出になるはずよ。\x02\x03",

            "#2104F表側から裏側まで\x01",
            "あらゆる角度から迫って\x01",
            "ぜんぶ晒しちゃうんだから！\x02\x03",

            "#2109Fう～ん、盛り上がってきたわね！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)

    label("loc_47B9")

    Jump("loc_4942")

    label("loc_47BE")

    OP_4B(0x19, 0xFF)

    #C0227
    ChrTalk(
        0x101,
        (
            "#0000Fグレイスさん。\x01",
            "パレードの取材ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x18,
        (
            "#2100Fモチ！\x01",
            "今年は過去最大の\x01",
            "人出になりそうだからね～。\x02\x03",

            "#2104Fパレードの表側から裏側まで\x01",
            "あらゆる角度から迫って\x01",
            "ぜんぶ晒しちゃうんだから！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x19, 300)

    #C0229
    ChrTalk(
        0x18,
        "#2109Fレインズ君、気合いは入れたっ？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 300)

    #C0230
    ChrTalk(
        0x19,
        "イエス・マム！\x02",
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

    label("loc_4942")

    TalkEnd(0xFE)
    Return()

    # Function_29_4678 end

    def Function_30_4946(): pass

    label("Function_30_4946")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_END)), "loc_4988")

    #C0231
    ChrTalk(
        0xFE,
        (
            "ドキドキ……\x01",
            "あと３０分くらいでしょうか！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A0B")

    label("loc_4988")


    #C0232
    ChrTalk(
        0xFE,
        "い、いよいよパレードですね！\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xFE,
        (
            "今日の写真は周辺諸国のニュース誌にも\x01",
            "流されるはずなので……\x01",
            "ちょっと緊張してきましたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)

    label("loc_4A0B")

    TalkEnd(0xFE)
    Return()

    # Function_30_4946 end

    def Function_31_4A0F(): pass

    label("Function_31_4A0F")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4AA3")
    Jump("loc_4AED")

    label("loc_4AA3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4AC3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AED")

    label("loc_4AC3")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4AE3")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4AED")

    label("loc_4AE3")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AED")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4B98")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B2D")
    Call(0, 35)
    Jump("loc_4B98")

    label("loc_4B2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4B3F")
    Call(0, 36)
    Jump("loc_4B98")

    label("loc_4B3F")


    #C0234
    ChrTalk(
        0x1A,
        (
            "#0804F記念祭は始まったばかり……\x02\x03",

            "#0802Fここはお互い、\x01",
            "力を合わせて乗り切りましょ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4B98")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_31_4A0F end

    def Function_32_4BA0(): pass

    label("Function_32_4BA0")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4C34")
    Jump("loc_4C7E")

    label("loc_4C34")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C54")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C7E")

    label("loc_4C54")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4C74")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_4C7E")

    label("loc_4C74")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C7E")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_4D56")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CBE")
    Call(0, 35)
    Jump("loc_4D56")

    label("loc_4CBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xB4, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD0")
    Call(0, 36)
    Jump("loc_4D56")

    label("loc_4CD0")


    #C0235
    ChrTalk(
        0x1B,
        (
            "#0903F国際的な貿易都市だけあって\x01",
            "外国の観光客も多いみたいだね。\x02\x03",

            "#0908Fトラブルを未然に防げるよう、\x01",
            "注意する必要がありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D56")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_32_4BA0 end

    def Function_33_4D5E(): pass

    label("Function_33_4D5E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4EFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E75")

    #C0236
    ChrTalk(
        0xFE,
        (
            "これから始まるパレードの\x01",
            "警備のために待機してるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0xFE,
        (
            "遊撃士が立ってるだけで\x01",
            "結構な抑止力になるものだからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x104,
        (
            "#0303F遊撃士は戦闘のプロ、だもんなぁ。\x02\x03",

            "#0309Fある意味警察より\x01",
            "睨みが効いてたりして。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        "#0000F……ひ、否定できないから。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_4EFE")

    label("loc_4E75")


    #C0240
    ChrTalk(
        0xFE,
        (
            "まぁ、警察も頼りにしてるよ。\x01",
            "前よりは大分使えるように\x01",
            "なったと思うしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0x101,
        (
            "#0006F（果たしてこれは\x01",
            "  褒められてるんだろうか……）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EFE")

    TalkEnd(0xFE)
    Return()

    # Function_33_4D5E end

    def Function_34_4F02(): pass

    label("Function_34_4F02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_4F86")

    #C0242
    ChrTalk(
        0xFE,
        (
            "あら……警察のみんなじゃない。\x01",
            "お仕事頑張ってるみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0xFE,
        (
            "今日は特別に人が多いから、\x01",
            "あなた達も気をつけてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F86")

    TalkEnd(0xFE)
    Return()

    # Function_34_4F02 end

    def Function_35_4F8A(): pass

    label("Function_35_4F8A")

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
            "#0809F#5Pやっほー。\x01",
            "支援課のみんなじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x1B,
        "#0902Fやあ、お疲れさま。\x02",
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x101,
        (
            "#0002Fはは……\x01",
            "そちらこそお疲れさま。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0x103,
        (
            "#0202Fエステルさんたちも\x01",
            "お仕事中みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x1A,
        (
            "#0804F#5Pうん、ちょっと\x01",
            "休憩を入れてるところなの。\x02\x03",

            "#0802Fそれにしても、まさかここまで\x01",
            "大きなお祭りとは思わなかったわ。\x02\x03",

            "#0803Fうーん、人出と規模だけなら\x01",
            "生誕祭以上かも。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#0005F生誕祭……？\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x1B,
        (
            "#0904Fリベール女王、アリシアⅡ世の\x01",
            "生誕をお祝いする祭りだよ。\x02\x03",

            "#0900Fリベールでは一番、\x01",
            "大きなお祭りになるかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0x101,
        (
            "#0000Fそういや２人は\x01",
            "リベールから来たんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x102,
        (
            "#0104F私も女王生誕祭には\x01",
            "前に一度行ったことがあるわ。\x02\x03",

            "#0102F伝統ある王国のお祭りらしく、\x01",
            "とても華やかで優美なお祭りよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x1A,
        (
            "#0809F#5Pえへへ……\x01",
            "そう言ってくれると嬉しいな。\x02\x03",

            "#0802Fもっとも華やかだけじゃなくて\x01",
            "武術大会なんかもあるんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x104,
        (
            "#0305Fへえ、そいつは\x01",
            "なかなか面白そうだな。\x02",
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

    # Function_35_4F8A end

    def Function_36_53A8(): pass

    label("Function_36_53A8")

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
            "#0801F#5Pあ、そういえば！\x02\x03",

            "#0802Fロイド君たち、すっごく\x01",
            "お手柄だったみたいね！？\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#0002Fあ、ああ……\x01",
            "市長暗殺未遂事件のことか。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x102,
        (
            "#0104Fまあ、色々な偶然が重なって\x01",
            "解決できたのだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0x1B,
        (
            "#0904Fそれでも、もし君たちが\x01",
            "事件を未然に防げなかったら\x01",
            "祭りどころじゃなかったと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x1A,
        (
            "#0809F#5Pうんうん！\x01",
            "言わば、このお祭りの賑わいも\x01",
            "ロイド君たちのお陰ってわけね♪\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#0012Fはは……\x01",
            "（普段あまり誉められないから\x01",
            "  こそばゆいな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        "#0304F（ま、素直に受け取っとこうぜ。）\x02",
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

    # Function_36_53A8 end

    def Function_37_5662(): pass

    label("Function_37_5662")

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
        "#3605F#5P皆さん……！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)
    Sleep(300)

    #C0263
    ChrTalk(
        0x24,
        "#5P#3708Fあ……！\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7111", 0)

    #C0264
    ChrTalk(
        0x101,
        (
            "#12P#0001Fどうもお久しぶりです。\x02\x03",

            "その、パレードを見物していたら\x01",
            "お子さんとはぐれてしまったとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x24,
        (
            "#5P#3701Fそ、そうなんです……！\x02\x03",

            "#3710F私がしっかりしていなかったから\x01",
            "あの子が……コリンが……！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x24, 400)
    Sleep(150)

    #C0266
    ChrTalk(
        0x23,
        "#3608Fソフィア、落ち着きなさい。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x101, 500)

    #C0267
    ChrTalk(
        0x23,
        (
            "#3603F#5P──すみません、皆さん。\x02\x03",

            "#3601F息子とはぐれたのは３時間ほど前……\x02\x03",

            "この広場でパレードが通過するのを\x01",
            "ちょうど見物している最中でした。\x02\x03",

            "すぐに妻が気付いて、\x01",
            "２人でこのあたりを一通り\x01",
            "捜したんですが見つからなくて……\x02\x03",

            "#3610F思い余って……\x01",
            "警察を頼らせていただきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x102,
        "#0102Fいえ、よく相談してくれました。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(150)

    #C0269
    ChrTalk(
        0x102,
        (
            "#0101F#11P──どうやら私たちで\x01",
            "手分けして捜した方がよさそうね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5AFE():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5AFE)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0270
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ、巡回中の警官も\x01",
            "今日ばかりは忙しそうだしな。\x02\x03",

            "#0001Fそうなると……\x01",
            "割り振りを考える必要がありそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x103,
        "#12P#0203Fそうですね……\x02",
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x104,
        (
            "#0300Fま、別々に探して\x01",
            "通信で連絡を取るのが一番だろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x24,
        (
            "#5P#3707Fわ、私もお手伝いさせてください！\x02\x03",

            "でないとあの子が……コリンが……\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x23,
        (
            "#3610F#5P……落ち着きなさい。\x02\x03",

            "#3601F皆さん、私たちはいったん、\x01",
            "住宅街にある自宅に戻ります。\x02\x03",

            "その近辺の捜索は\x01",
            "私の方で一通り行いますので。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5CC9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5CC9)
    Sleep(50)

    def lambda_5CD9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5CD9)
    Sleep(50)
    OP_93(0x104, 0x2D, 0x1F4)

    #C0275
    ChrTalk(
        0x101,
        (
            "#12P#0000Fなるほど……\x01",
            "その方が効率的でしょうね。\x02\x03",

            "#0003F自分たちは手分けして、\x01",
            "他の街区を一通り捜してみます。\x02\x03",

            "#0001Fそれから……\x01",
            "息子さんの手がかりになるものを\x01",
            "何かお持ちではないですか？\x02\x03",

            "写真があれば一番ですけど。\x02",
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
            "#3605F#5Pああ、ちょうど記念祭で撮った\x01",
            "写真を現像してもらってたんです！\x02\x03",

            "#3608Fえっと、確かここに……\x02",
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
            "ハロルド氏は懐から\x01",
            "写真の入った封筒を取り出した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    #C0278
    ChrTalk(
        0x23,
        "#3601F#5P……これです！\x02",
    )

    CloseMessageWindow()

    def lambda_5EC8():
        OP_9A(0xFE, 0x101, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5EC8)
    WaitChrThread(0x23, 1)

    def lambda_5EE0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_5EE0)

    def lambda_5EED():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5EED)
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
            "を３枚受け取った。\x02",
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
        "#0102F可愛い……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0281
    AnonymousTalk(
        0x103,
        (
            "#0202F#12P男の子なのに\x01",
            "美人さんですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)

    def lambda_5FC4():
        OP_96(0xFE, 0xFFFFBADC, 0x9C4, 0x320, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_5FC4)
    WaitChrThread(0x23, 1)
    Sleep(300)
    SetChrSubChip(0x24, 0x0)
    Sleep(300)

    #C0282
    ChrTalk(
        0x24,
        "#5P#3710Fううっ……コリン……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x24, 500)

    #C0283
    ChrTalk(
        0x23,
        (
            "#3600Fほら、いったん家に戻って\x01",
            "コリンが帰ってくるのを待とう。\x02\x03",

            "ひょっとしたら家の方に\x01",
            "戻ってくるかもしれないし……\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x2)
    Sleep(300)

    #C0284
    ChrTalk(
        0x24,
        (
            "#11P#3707Fでも……でも……！\x01",
            "あの時みたいな事があったら……！\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x23,
        (
            "#3601F大丈夫だ……！\x01",
            "もう絶対にあんなことは……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_610F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_610F)
    Sleep(50)
    OP_93(0x104, 0x2D, 0x1F4)

    #C0286
    ChrTalk(
        0x101,
        "#12P#0005F（あの時……？）\x02",
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x102,
        "#0108F（何か事情があるみたいね……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x23, 0x101, 300)

    #C0288
    ChrTalk(
        0x23,
        (
            "#3610F#5P……すみません。\x01",
            "取り乱してしまって。\x02\x03",

            "#3608Fその……\x01",
            "ちょっと事情がありまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x101,
        "#12P#0004Fいや、気にしないでください。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0290
    ChrTalk(
        0x101,
        (
            "#12P#0005Fそうだ……写真の他に、\x01",
            "普段コリン君が持っているような\x01",
            "品物はお持ちではないですか？\x02\x03",

            "#0000Fうちには警察犬もいますので\x01",
            "匂いで辿れるかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x24, 0x1)

    #C0291
    ChrTalk(
        0x23,
        "#3605F#5Pおお……！\x02",
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x24,
        (
            "#5P#3708F……じゃ、じゃあこれを……！\x01",
            "あの子の持っていたぬいぐるみです！\x02",
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
            "#0205F#12Pあ……\x01",
            "《みっしぃ》のぬいぐるみですか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0294
    AnonymousTalk(
        0x102,
        "#0103Fそれではお借りしておきます。\x02",
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
            "を受け取った。\x02",
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
            "#0303Fま、焦ったって仕方ねぇ。\x02\x03",

            "#0300F街の中にいる限りは安全だろうし\x01",
            "俺たちにドンと任せてくださいよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x23,
        (
            "#3604F#5Pは、はい。\x01",
            "ありがとうございます。\x02\x03",

            "#3601Fそれでは皆さん……\x01",
            "息子をよろしくお願いします。\x02",
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

    def lambda_6532():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6532)
    Sleep(50)

    def lambda_6542():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6542)
    Sleep(50)

    def lambda_6552():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6552)
    Sleep(50)

    def lambda_6562():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6562)
    Sleep(3000)
    OP_68(-18350, 3500, -1750, 1200)

    def lambda_6583():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6583)
    Sleep(100)

    def lambda_6593():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6593)

    def lambda_65A0():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_65A0)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    OP_6F(0x1)

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#0003Fさてと……\x01",
            "どう手分けするかだけど。\x02\x03",

            "#0000Fその前に……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x103,
        (
            "#12P#0204F……はい。\x01",
            "呼んでみます。\x02",
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

    def lambda_67B7():
        OP_9D(0xFE, 0xFFFFB820, 0x9C4, 0xFFFFEF98, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_67B7)
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

    def lambda_6808():
        OP_93(0xFE, 0x154, 0x190)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_6808)

    def lambda_6815():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6815)

    def lambda_6822():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6822)

    def lambda_682F():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_682F)

    def lambda_683C():
        TurnDirection(0xFE, 0x25, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_683C)
    WaitChrThread(0x25, 2)
    BeginChrThread(0x25, 1, 0, 38)
    Sleep(500)
    Sound(2052, 255, 100, 0)    #voice#Zeit
    Sleep(800)

    #C0300
    ChrTalk(
        0x25,
        "#11P#1200Fグルル……\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        "#5P#0002Fツァイト、来てくれたか。\x02",
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0x102,
        "#5P#0102Fふふ、お疲れさま。\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x25,
        (
            "#11P#1203Fグルルル……ウォン。\x02\x03",

            "#1200F……グルルルル……\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        (
            "#6P#0204F『……自分が来たからには\x01",
            "  大船に乗った気分でいるといい。』\x02\x03",

            "『その幼子の匂いは\x01",
            "  完璧に嗅ぎ当ててみせよう。』\x02\x01",

            "#0202F──だそうです。\x02",
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
            "#5P#0012Fた、助かるよ。\x02\x03",

            "#0000Fっていうか、来たばかりなのに\x01",
            "なんでそんなに詳しいんだ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x104,
        (
            "#5P#0300Fやれやれ。\x01",
            "相変わらずとんでもねぇヤツだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x102,
        "#5P#0104Fまあ、それはともかく。\x02",
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
            "#11P#0100Fこの広いクロスベル……\x01",
            "どう分担して捜索しましょうか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6B0B():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_6B0B)
    Sleep(50)
    TurnDirection(0x104, 0x101, 500)

    #C0309
    ChrTalk(
        0x103,
        (
            "#12P#0204Fわたしはツァイトに同行します。\x02\x03",

            "#0202F彼の言葉を判る人間が\x01",
            "付いていた方がいいでしょう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)

    #C0310
    ChrTalk(
        0x101,
        (
            "#0003F#5Pそうだな……\x02\x03",

            "#0000Fだったらティオには\x01",
            "このぬいぐるみを渡しておく。\x02\x03",

            "ツァイトにコリン君の匂いを\x01",
            "探ってもらってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x103,
        "#12P#0204F……了解です。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 500)
    Sleep(300)

    #C0312
    ChrTalk(
        0x101,
        (
            "#0003F#5P俺たち３人は\x01",
            "手分けして街区を担当しよう。\x02\x03",

            "#0000F俺は歓楽街から裏通り、中央広場、\x01",
            "駅前通り、それから西通り。\x02\x03",

            "#0004Fランディは東通りと旧市街全般。\x02\x03",

            "エリィは行政区と、港湾区全般。\x02\x03",

            "#0000F──そんな分担でどうかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x102,
        (
            "#11P#0105Fあら、あなたの担当だけ\x01",
            "相当広い気がするけど……？\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x101,
        (
            "#0002F#5Pいや、行政区も港湾区も広いし、\x01",
            "旧市街だって入り組んでいる。\x02\x03",

            "その点、俺の担当は\x01",
            "よく通る場所ばかりだから\x01",
            "丁度いいバランスのはずだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        "#11P#0102Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x104,
        (
            "#0304Fま、とりあえず\x01",
            "その分担で始めてみようぜ。\x02\x03",

            "#0300F進展があったらお互い\x01",
            "通信で連絡を取ればいいんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#0000F#5Pああ、そうしよう。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x103,
        (
            "#12P#0202Fそれではコリン君の捜索、\x01",
            "ミッションスタートですね。\x02",
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

    # Function_37_5662 end

    def Function_38_6F27(): pass

    label("Function_38_6F27")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F45")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_38_6F27")

    label("loc_6F45")

    Return()

    # Function_38_6F27 end

    def Function_39_6F46(): pass

    label("Function_39_6F46")

    OP_92(0xFE, 0xFFFFB7BC, 0x9C4, 0x1F4)

    def lambda_6F58():
        OP_95(0xFE, -18500, 2500, 2500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F58)
    WaitChrThread(0xFE, 1)

    def lambda_6F76():
        OP_95(0xFE, -18500, 2500, 10500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6F76)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_6F46 end

    def Function_40_6F90(): pass

    label("Function_40_6F90")

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

    # Function_40_6F90 end

    def Function_41_71A5(): pass

    label("Function_41_71A5")

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

    def lambda_72C4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_72C4)

    def lambda_72D5():
        OP_96(0xFE, 0xFFFFB758, 0x9C4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_72D5)
    Sleep(400)

    def lambda_72F2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_72F2)

    def lambda_7303():
        OP_96(0xFE, 0xFFFFBC08, 0x9C4, 0x6590, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7303)
    Sleep(400)

    def lambda_7320():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7320)

    def lambda_7331():
        OP_96(0xFE, 0xFFFFB758, 0x9C4, 0x6B08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_7331)
    Sleep(400)

    def lambda_734E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_734E)

    def lambda_735F():
        OP_96(0xFE, 0xFFFFBC08, 0x9C4, 0x6B08, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_735F)
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

    def lambda_73FA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_73FA)
    Sleep(50)

    def lambda_740A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_740A)

    #C0319
    ChrTalk(
        0x101,
        "#5P#0005Fおっと。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x102,
        (
            "#0105F#11Pあら……\x01",
            "また緊急要請かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x101,
        "#5P#0001Fうーん……\x02",
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
        "#0001Fはい、ロイドです。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年の声")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "お、ビンゴだな。\x02\x03",

            "いや～。\x01",
            "合ってて何よりだぜ。\x02",
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
            "#0005Fえっと……どちらさま？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("少年の声")

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハッ……ボクの声を\x01",
            "聞いて分かんねーのかよ。\x02\x03",

            "ヨナだよ、ヨナ。\x01",
            "天才ヨナ・セイクリッド。\x02",
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
            "#0014F#30Wなんだ君か─#800W─",
            "#0007F#20W#4Sっておい！\x02\x03",    #line#50

            "#3S#0007Fどうして君が\x01",
            "この番号を知ってるんだ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0327
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハッ、警察のデータベースから\x01",
            "調べたに決まってるじゃん。\x02\x03",

            "いや～、警察のセキュリティって\x01",
            "ちょっとザルすぎるんじゃん？\x02\x03",

            "まあトップシークレットなんかは\x01",
            "データベースには無いみたいだけどさ。\x02",
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
            "#0011Fお、お前な……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(50, 30, -1, -1)

    #A0329
    AnonymousTalk(
        0x104,
        "#0305F誰からなんだ？\x02",
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
            "#6P#0006Fああ……\x01",
            "あのハッカーの坊主だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x102,
        "#0105F#11Pええっ？\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x103,
        "#0211F#5Pまったくあの子は……\x02",
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
            "#0003F──それで、何の用なんだ？\x02\x03",

            "#0001Fハッキングの腕を\x01",
            "自慢したいんじゃないだろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0334
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "それなんだけどさ～。\x02\x03",

            "ちょっとボクからの依頼を\x01",
            "請けてくんないかな～って思ってさ。\x02",
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
            "#0005Fなに……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0336
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ま、正確にはティオの助けが\x01",
            "借りたいだけなんだけど。\x02\x03",

            "一応、アンタたちにも\x01",
            "話を通しておこうと思ってさ。\x02",
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
            "#0013Fあのな……\x01",
            "こっちは忙しいんだ。\x02\x03",

            "プライベートな話だったら\x01",
            "さすがに断らせてもらうぞ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0338
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ま、プライベートっちゃあ\x01",
            "プライベートな用事だけど……\x02\x03",

            "報酬はたんまり弾むぜ？\x02",
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
            "#0006F俺たちは遊撃士じゃない。\x02\x03",

            "直接、そうした報酬を\x01",
            "受け取るつもりはないんだが。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ヨナの声")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハッ、お高くとまっちゃって。\x02\x03",

            "ただまあ、報酬といっても\x01",
            "直接ミラってわけじゃないさ。\x02\x03",

            "あんた達の欲しがってる情報を\x01",
            "パックした記録結晶#8Rメモリークオーツ#……\x02\x03",

            "それだったらどうよ？\x02",
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
    SetChrName("ヨナの声")

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハッ、いい反応じゃん。\x02\x03",

            "ま、とにかく\x01",
            "ボクんとこに来てくれよ。\x02\x03",

            "詳しい話はその時にするからさ。\x02",
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
            "#0006F……分かった。\x02",
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
        "#0105F#11Pえっと、何だったの？\x02",
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
        "#6P#0003Fああ……\x02",
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
            "ロイドはヨナからの話をエリィたちに説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0347
    ChrTalk(
        0x102,
        "#0103F#11Pなるほど……\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x104,
        (
            "#0306Fったく、ふざけたガキだぜ。\x02\x03",

            "#0301Fしかも確実に\x01",
            "こっちの足元を見てやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x103,
        (
            "#0203F#5P……でも、とりあえず\x01",
            "行ってみた方が良さそうですね。\x02\x03",

            "#0202Fわたしの助けが欲しいみたいですし\x01",
            "逆にこちらが彼の足元を\x01",
            "見ることもできるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7EDE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_7EDE)
    Sleep(50)

    def lambda_7EEE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_7EEE)
    Sleep(50)

    def lambda_7EFE():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_7EFE)
    Sleep(300)

    #C0350
    ChrTalk(
        0x101,
        (
            "#12P#0012Fいや、別にそんな駆け引きは\x01",
            "しなくてもいいんだけど……\x02\x03",

            "#0005Fというか、どうして彼は\x01",
            "ティオに直接連絡しないんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x103,
        (
            "#0204F#5Pおそらく悔しいんだと思います。\x02\x03",

            "おととい、落ちゲーの対戦で\x01",
            "徹底的に負かしたばかりですから。\x02",
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
        "#12P#0012Fそ、そうなのか……\x02",
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x102,
        (
            "#0102F#11Pその落ちゲーっていうのは\x01",
            "よく分からないけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x104,
        (
            "#11P#0302Fあの小僧が、ティオすけには\x01",
            "頭が上がらないのは確かみてぇだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x103,
        (
            "#0206F#5P基本的に甘ったれですから。\x02\x03",

            "#0202Fとにかく、他に用事が無ければ\x01",
            "ヨナの所に行ってみましょう。\x02\x03",

            "わたしとしても、\x01",
            "彼の依頼内容は気になりますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        "#12P#0000Fそうだな……行ってみるか。\x02",
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

    # Function_41_71A5 end

    def Function_42_81E8(): pass

    label("Function_42_81E8")

    Sleep(900)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Return()

    # Function_42_81E8 end

    def Function_43_81FD(): pass

    label("Function_43_81FD")

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
            "#11Pいらっしゃいませー。\x01",
            "『クロマのジュース屋』へようこそー。\x02",
        )
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあ、確か……\x01",
            "窃盗被害に遭われた店舗ですよね？\x02\x03",

            "#0001F詳しい状況を\x01",
            "お聞きしてよろしいですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0359
    ChrTalk(
        0xB,
        (
            "#11Pそ、そうなんです。\x01",
            "少し油断したスキに\x01",
            "盗られてしまったみたいで……\x02",
        )
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0xB,
        "#11Pはあ、売り上げが……\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x103,
        "#12P#0200F何か犯人の心当たりは？\x02",
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0xB,
        (
            "#11Pそれはちょっと……\x01",
            "お客さんの応対中だったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0xB,
        (
            "#11P軽い感じの青年……\x01",
            "たぶん外国からの観光客ですね。\x01",
            "そんな人にナンパされちゃいまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0xB,
        (
            "#11Pで、何とか断ってる最中に\x01",
            "後ろで物音が……\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x104,
        "#6P#0303Fその隙に盗られたってワケか……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0xB,
        (
            "#11Pええ、私も気をつけては\x01",
            "いたんですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x102,
        "#12P#0101F（中々手強い相手みたいね……）\x02",
    )

    CloseMessageWindow()
    OP_29(0x20, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x6)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8725")
    OP_68(5210, 4740, -10040, 1200)
    MoveCamera(12, 25, 0, 1200)

    def lambda_85A1():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_85A1)

    def lambda_85AE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_85AE)

    def lambda_85BB():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_85BB)

    def lambda_85C8():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_85C8)
    Sleep(1200)

    #C0368
    ChrTalk(
        0x101,
        "#5P#0003F聞き込みはこんな所かな……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x104,
        (
            "#6P#0300Fだな、そろそろ戻って\x01",
            "整理してみようぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xB)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_2A(0x20, 0x1, 0xC)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_871F")

    #C0370
    ChrTalk(
        0x102,
        (
            "#12P#0100F商工会から連絡もないし、\x01",
            "まだ次の犯行は\x01",
            "行われてないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        (
            "#12P#0203Fですね。\x02\x03",

            "#0200F……念のため、\x01",
            "出店を見て回りながら戻った方が\x01",
            "いいかもしれませんが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_871F")

    OP_29(0x20, 0x1, 0xD)

    label("loc_8725")

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

    # Function_43_81FD end

    def Function_44_875C(): pass

    label("Function_44_875C")

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
            "ロイド達は目星をつけた街区へ向かい\x01",
            "張り込みを行う事にした。\x07\x00\x02",
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

            "この客じゃなさそうだな……\x02",
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

    def lambda_8944():
        OP_95(0xFE, 600, 2500, 1580, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_8944)
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
        "#0306F来ねえな……\x02",
    )

    CloseMessageWindow()

    #A0375
    AnonymousTalk(
        0x103,
        (
            "#0200Fもう１時間以上\x01",
            "張り込んでいますが……\x02",
        )
    )

    CloseMessageWindow()

    #A0376
    AnonymousTalk(
        0x101,
        (
            "#0003Fおかしいな、もう来ても\x01",
            "いいはずなんだが……\x02",
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

    def lambda_8AC1():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_8AC1)

    def lambda_8ACE():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_8ACE)

    def lambda_8ADB():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_8ADB)
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
            "#5P#0000Fはい、ロイド・バニングス──\x02\x03",

            "#0005Fえっ、窃盗犯が現れた……！？\x02",
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
            "#5P#0001Fはい、はい、中央広場ですね。\x02\x03",

            "判りました、すぐに急行します！\x02",
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
            "#5P#0003F……みんなゴメン。\x01",
            "読みが外れたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        "#11P#0101Fいいから急ぎましょう、ロイド！\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x101,
        (
            "#5P#0001Fそ、そうだな。\x01",
            "今は現場に急ごう！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8CC5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8CC5)

    def lambda_8CD2():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8CD2)

    def lambda_8CDF():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8CDF)

    def lambda_8CEC():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8CEC)
    Sleep(300)
    WaitChrThread(0x104, 1)

    def lambda_8D00():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_8D00)

    def lambda_8D15():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_8D15)

    def lambda_8D2A():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_8D2A)

    def lambda_8D3F():
        OP_9B(0x0, 0xFE, 0x0, 0x1194, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_8D3F)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x28)
    ClearScenarioFlags(0x2, 0)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 5)
    NewScene("c010C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_44_875C end

    def Function_45_8D6F(): pass

    label("Function_45_8D6F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_8D94")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_45_8D6F")

    label("loc_8D94")

    Return()

    # Function_45_8D6F end

    def Function_46_8D95(): pass

    label("Function_46_8D95")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0382
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　※　新市庁舎ビル建設中　※\x01",
            "工事関係者以外、立ち入りを禁ずる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_46_8D95 end

    def Function_47_8E0F(): pass

    label("Function_47_8E0F")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0383
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "国際シンポジウム\x01",
            "『～クロスベルの現在と未来～』\x01",
            "  有識者８名が語る\x01",
            "           自治州の現在──\x02",
        )
    )

    CloseMessageWindow()

    #A0384
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　場所　：クロスベル市庁舎\x01",
            "          レセプションホール\x01",
            "開催期間：記念祭３日目\x01",
            " 主催者 ：ヘンリー・マクダエル\x01",
            "※傍聴には事前申し込みが必要です。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_47_8E0F end

    SaveToFile()

Try(main)
