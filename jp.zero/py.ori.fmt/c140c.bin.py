from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c140c.bin",                # FileName
        "c140c",                    # MapName
        "c140c",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1D,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 3, 0, 4],
    )

    BuildStringList((
        "c140c",                  # 0
        "ディーノ",               # 1
        "パオラ婆さん",           # 2
        "ヴァン",                 # 3
        "ルゼ",                   # 4
        "カノン",                 # 5
        "ヒューイ",               # 6
        "コウキ",                 # 7
        "キーンツ",               # 8
        "ベッセ",                 # 9
        "コロナ",                 # 10
        "リマ",                   # 11
        "メルスン",               # 12
        "見物客",                 # 13
        "見物客",                 # 14
        "エステル",               # 15
        "ヨシュア",               # 16
        "ワジ",                   # 17
        "ヴァルド",               # 18
        "アッバス",               # 19
        "グレイス",               # 20
        "カメラマン",             # 21
        "Ｓバイパー構成員",       # 22
        "Ｓバイパー構成員",       # 23
        "Ｓバイパー構成員",       # 24
        "Ｓバイパー構成員",       # 25
        "Ｓバイパー構成員",       # 26
        "テスタメンツ構成員",     # 27
        "テスタメンツ構成員",     # 28
        "テスタメンツ構成員",     # 29
        "テスタメンツ構成員",     # 30
        "イベント用タントス老人", # 31
        "イベント用ガイトナー",   # 32
        "イベント用見物客",       # 33
        "イベント用見物客",       # 34
        "ロイド",                 # 35
        "ランディ",               # 36
        "エリィ",                 # 37
        "ティオ",                 # 38
        "オブジェ用",             # 39
        "中央広場",               # 40
        "西通り",                 # 41
        "行政区",                 # 42
        "住宅街",                 # 43
        "歓楽街",                 # 44
        "東通り",                 # 45
        "旧市街",                 # 46
        "港湾区",                 # 47
        "ＩＢＣ",                 # 48
        "駅前通り",               # 49
        "裏通り",                 # 50
        "ウルスラ間道",           # 51
        "東クロスベル街道",       # 52
        "西クロスベル街道",       # 53
        "マインツ山道",           # 54
    ))

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch23302.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch24700.itc",                   # 03
        "chr/ch23800.itc",                   # 04
        "chr/ch31700.itc",                   # 05
        "chr/ch22700.itc",                   # 06
        "chr/ch20700.itc",                   # 07
        "chr/ch26200.itc",                   # 08
        "chr/ch23700.itc",                   # 09
        "chr/ch23600.itc",                   # 0A
        "chr/ch31800.itc",                   # 0B
        "chr/ch30900.itc",                   # 0C
        "chr/ch30800.itc",                   # 0D
    ))

    DeclNpc(44880,   -2500,   -20090,  225,  261,  0x0, 0,   0,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(15449,   100,     -19,     270,  261,  0x0, 0,   1,   0,   255, 255, 0,   7,   255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   2,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(10279,   0,       -550,    315,  261,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(34080,   -6500,   -38270,  45,   261,  0x0, 0,   4,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(2339,    0,       -2940,   315,  405,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(43650,   -2500,   -19120,  135,  389,  0x0, 0,   13,  0,   0,   0,   0,   15,  255,  0)
    DeclNpc(-140,    0,       3740,    135,  405,  0x0, 0,   11,  0,   0,   0,   0,   16,  255,  0)
    DeclNpc(920,     0,       2680,    315,  389,  0x0, 0,   12,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(9449,    0,       3140,    0,    277,  0x0, 0,   6,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(8350,    0,       4110,    90,   261,  0x0, 0,   7,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9560,    0,       4400,    225,  261,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-19489,  0,       -9409,   0,    261,  0x0, 0,   9,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(1950,    0,       140,     180,  261,  0x0, 0,   10,  0,   0,   0,   0,   24,  255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclActor(-28460,  2800,    -29590,  1200,    -28460,  3800,    -29590,  0x007C, 0,  5,  0x0000)
    DeclActor(34830,   2450,    -19780,  1500,    34830,   3950,    -19780,  0x007C, 0,  81, 0x0000)

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "中央広場")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "西通り")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "歓楽街")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "東通り")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "旧市街")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "駅前通り")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "裏通り")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-135.99000549316406, 0.0, 90.8499984741211, 0x0000, 0x0051, "")
    PlaceName(-74.18000030517578, 0.0, 120.75, 0x0000, 0x0054, "")
    PlaceName(-107.80999755859375, 0.0, 81.6500015258789, 0x0000, 0x0057, "")
    PlaceName(-136.85000610351562, 0.0, 124.19999694824219, 0x0000, 0x0053, "")
    PlaceName(-113.27999877929688, 0.0, 151.8000030517578, 0x0000, 0x0053, "")
    PlaceName(-171.63999938964844, 0.0, 118.44999694824219, 0x0000, 0x0053, "")
    PlaceName(-182.85000610351562, 0.0, 142.60000610351562, 0x0000, 0x0053, "")
    PlaceName(-155.25, 0.0, 179.39999389648438, 0x0000, 0x0052, "")
    PlaceName(-149.7899932861328, 0.0, 164.4499969482422, 0x0000, 0x0053, "")
    PlaceName(-139.72999572753906, 0.0, 154.67999267578125, 0x0000, 0x0053, "")
    PlaceName(-106.94999694824219, 0.0, 236.3300018310547, 0x0000, 0x0051, "")
    PlaceName(21.850000381469727, 0.0, 80.5, 0x0000, 0x0052, "")
    PlaceName(2.299999952316284, 0.0, -23.579999923706055, 0x0000, 0x0053, "")
    PlaceName(-12.649999618530273, 0.0, -2.299999952316284, 0x0000, 0x0053, "")

    ScpFunction((
        "Function_0_9D4",          # 00, 0
        "Function_1_A8C",          # 01, 1
        "Function_2_AB7",          # 02, 2
        "Function_3_B90",          # 03, 3
        "Function_4_EEE",          # 04, 4
        "Function_5_F60",          # 05, 5
        "Function_6_10AD",         # 06, 6
        "Function_7_1399",         # 07, 7
        "Function_8_16B9",         # 08, 8
        "Function_9_191C",         # 09, 9
        "Function_10_19C8",        # 0A, 10
        "Function_11_1A82",        # 0B, 11
        "Function_12_1C92",        # 0C, 12
        "Function_13_21F3",        # 0D, 13
        "Function_14_21FD",        # 0E, 14
        "Function_15_2370",        # 0F, 15
        "Function_16_24B7",        # 10, 16
        "Function_17_255A",        # 11, 17
        "Function_18_2673",        # 12, 18
        "Function_19_2771",        # 13, 19
        "Function_20_290C",        # 14, 20
        "Function_21_2ABF",        # 15, 21
        "Function_22_2B6E",        # 16, 22
        "Function_23_2DC6",        # 17, 23
        "Function_24_2E7B",        # 18, 24
        "Function_25_3035",        # 19, 25
        "Function_26_560C",        # 1A, 26
        "Function_27_569A",        # 1B, 27
        "Function_28_5702",        # 1C, 28
        "Function_29_5794",        # 1D, 29
        "Function_30_5800",        # 1E, 30
        "Function_31_58A3",        # 1F, 31
        "Function_32_5920",        # 20, 32
        "Function_33_59D3",        # 21, 33
        "Function_34_5A4D",        # 22, 34
        "Function_35_5A9F",        # 23, 35
        "Function_36_5AF1",        # 24, 36
        "Function_37_5B1E",        # 25, 37
        "Function_38_5B62",        # 26, 38
        "Function_39_5BCC",        # 27, 39
        "Function_40_5C4F",        # 28, 40
        "Function_41_5C9D",        # 29, 41
        "Function_42_5CEB",        # 2A, 42
        "Function_43_5D1C",        # 2B, 43
        "Function_44_5D6F",        # 2C, 44
        "Function_45_5EB5",        # 2D, 45
        "Function_46_5F78",        # 2E, 46
        "Function_47_5FC6",        # 2F, 47
        "Function_48_6014",        # 30, 48
        "Function_49_6066",        # 31, 49
        "Function_50_60C3",        # 32, 50
        "Function_51_616F",        # 33, 51
        "Function_52_61BB",        # 34, 52
        "Function_53_6226",        # 35, 53
        "Function_54_6294",        # 36, 54
        "Function_55_62F1",        # 37, 55
        "Function_56_6311",        # 38, 56
        "Function_57_636B",        # 39, 57
        "Function_58_63C6",        # 3A, 58
        "Function_59_6403",        # 3B, 59
        "Function_60_648C",        # 3C, 60
        "Function_61_651B",        # 3D, 61
        "Function_62_65AA",        # 3E, 62
        "Function_63_6633",        # 3F, 63
        "Function_64_6663",        # 40, 64
        "Function_65_6715",        # 41, 65
        "Function_66_6900",        # 42, 66
        "Function_67_69E0",        # 43, 67
        "Function_68_69ED",        # 44, 68
        "Function_69_69F8",        # 45, 69
        "Function_70_6A03",        # 46, 70
        "Function_71_6A0D",        # 47, 71
        "Function_72_B556",        # 48, 72
        "Function_73_B665",        # 49, 73
        "Function_74_B698",        # 4A, 74
        "Function_75_B6CB",        # 4B, 75
        "Function_76_B6E7",        # 4C, 76
        "Function_77_B703",        # 4D, 77
        "Function_78_B72F",        # 4E, 78
        "Function_79_B75B",        # 4F, 79
        "Function_80_B7E8",        # 50, 80
        "Function_81_EC38",        # 51, 81
    ))


    def Function_0_9D4(): pass

    label("Function_0_9D4")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A14"),
        (1, "loc_A20"),
        (2, "loc_A2C"),
        (3, "loc_A38"),
        (4, "loc_A44"),
        (5, "loc_A50"),
        (6, "loc_A5C"),
        (SWITCH_DEFAULT, "loc_A68"),
    )


    label("loc_A14")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A20")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A2C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A38")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A44")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A50")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A5C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A68")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A74")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A8B")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A74")

    label("loc_A8B")

    Return()

    # Function_0_9D4 end

    def Function_1_A8C(): pass

    label("Function_1_A8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AB6")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_1_A8C")

    label("loc_AB6")

    Return()

    # Function_1_A8C end

    def Function_2_AB7(): pass

    label("Function_2_AB7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B8F")
    OP_95(0xFE, 5840, 0, -6890, 5000, 0x0)
    OP_95(0xFE, 13450, -1420, -18510, 5000, 0x0)
    OP_95(0xFE, 21750, -2500, -24790, 5000, 0x0)
    OP_95(0xFE, 21750, -6500, -38390, 5000, 0x0)
    OP_95(0xFE, 7790, -6320, -37990, 5000, 0x0)
    OP_95(0xFE, -3730, -3830, -27600, 5000, 0x0)
    OP_95(0xFE, -12250, -3030, -23600, 5000, 0x0)
    OP_95(0xFE, -12250, 0, -12120, 5000, 0x0)
    OP_95(0xFE, -10970, 0, -11360, 5000, 0x0)
    OP_95(0xFE, -5510, 0, -7900, 5000, 0x0)
    Jump("Function_2_AB7")

    label("loc_B8F")

    Return()

    # Function_2_AB7 end

    def Function_3_B90(): pass

    label("Function_3_B90")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C6D")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C17")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_C36")

    label("loc_C17")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C36")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_C36")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C6D")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_C8A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 25)
    Jump("loc_CAD")

    label("loc_C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_C9E")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 71)
    Jump("loc_CAD")

    label("loc_C9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_CAD")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 80)

    label("loc_CAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_D61")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0x8, 4620, 0, -5320, 315)
    SetChrPos(0xF, 1100, 0, -1620, 135)
    SetChrPos(0x10, -310, 50, -1500, 135)
    SetChrPos(0xE, 44880, -2500, -20090, 225)
    OP_93(0x11, 0xE1, 0x0)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_EED")

    label("loc_D61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_DA5")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrPos(0xA, 1810, 0, 4550, 315)
    SetChrPos(0xB, 610, 0, 5750, 135)
    ClearChrFlags(0x11, 0x10)
    Jump("loc_EED")

    label("loc_DA5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_DDF")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    TurnDirection(0x11, 0x12, 0)
    TurnDirection(0x12, 0x11, 0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_EED")

    label("loc_DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_E93")
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xA, 4670, 0, -5500, 180)
    SetChrPos(0xB, 4710, 0, -7160, 0)
    SetChrPos(0x14, 43330, -2500, -20060, 90)
    SetChrPos(0x15, 42420, -2500, -19200, 135)
    OP_93(0x8, 0x10E, 0x0)
    TurnDirection(0x13, 0x12, 0)
    SetChrFlags(0x13, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x14, 0x10)
    SetChrFlags(0x15, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6C")
    SetChrFlags(0x8, 0x10)

    label("loc_E6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_E7F")
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)

    label("loc_E7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E8E")
    SetChrFlags(0x12, 0x10)

    label("loc_E8E")

    Jump("loc_EED")

    label("loc_E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_EB7")
    SetChrPos(0x15, -18810, 0, -10220, 315)
    SetChrFlags(0x8, 0x80)
    Jump("loc_EED")

    label("loc_EB7")

    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xA, 2740, 0, -770, 315)
    SetChrPos(0xB, 960, 0, 870, 135)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)

    label("loc_EED")

    Return()

    # Function_3_B90 end

    def Function_4_EEE(): pass

    label("Function_4_EEE")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F3D")
    OP_70(0x7, 0x0)
    Jump("loc_F41")

    label("loc_F3D")

    OP_70(0x7, 0x1E)

    label("loc_F41")

    OP_65(0x1, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5F")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_F5F")

    Return()

    # Function_4_EEE end

    def Function_5_F60(): pass

    label("Function_5_F60")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_105C")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x642, 1)"), scpexpr(EXPR_END)), "loc_FE5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x110, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1057")

    label("loc_FE5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x642),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1057")

    Jump("loc_10A1")

    label("loc_105C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_10A1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F60 end

    def Function_6_10AD(): pass

    label("Function_6_10AD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_113E")

    #C0004
    ChrTalk(
        0x8,
        (
            "はわわ……まさかこんな所で\x01",
            "テスタメンツの連中と……\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        "け、喧嘩するのかな！？\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x8,
        (
            "お、俺……\x01",
            "どうすりゃいいんだよっ！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1395")

    label("loc_113E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_11EB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_119A")

    #C0007
    ChrTalk(
        0x8,
        (
            "今日は観光客が\x01",
            "うろうろしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        "まったく、迷惑だなっ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_11E6")

    label("loc_119A")

    OP_4B(0x14, 0xFF)

    #C0009
    ChrTalk(
        0x8,
        "こら、ここは見世物じゃないぞ！\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x8,
        "あっちに行けよっ！\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 1)
    OP_4C(0x14, 0xFF)

    label("loc_11E6")

    Jump("loc_1395")

    label("loc_11EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_1263")

    #C0011
    ChrTalk(
        0x8,
        (
            "ヴァルドさんたちは\x01",
            "遊びに行っちまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "うう～、前に聞いてみた時は\x01",
            "興味なさそうだったのに……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1395")

    label("loc_1263")


    #C0013
    ChrTalk(
        0x8,
        (
            "ヴァルドさんたちは\x01",
            "遊びに行っちまうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x8,
        (
            "みんなお祭りに目が無くて、\x01",
            "毎年出店巡りしてるんだって……\x02",
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

    #C0015
    ChrTalk(
        0x102,
        (
            "#0106Fそ、それで\x01",
            "貴方はお留守番なのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            "仕方ないだろっ！\x01",
            "俺が一番下っ端なんだから！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_1395")

    TalkEnd(0xFE)
    Return()

    # Function_6_10AD end

    def Function_7_1399(): pass

    label("Function_7_1399")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_142D")
    Jump("loc_1477")

    label("loc_142D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_144D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1477")

    label("loc_144D")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_146D")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1477")

    label("loc_146D")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1477")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_14CA")

    #C0017
    ChrTalk(
        0x9,
        "あらあら、また喧嘩かしら。\x02",
    )

    CloseMessageWindow()
    Jump("loc_16B1")

    label("loc_14CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1546")

    #C0018
    ChrTalk(
        0x9,
        (
            "パレードはとても\x01",
            "華やかだったみたいですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x9,
        (
            "さて、今日はなにか\x01",
            "おいしい物でも食べましょうかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B1")

    label("loc_1546")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_15CF")

    #C0020
    ChrTalk(
        0x9,
        (
            "わたしは足が悪くて、\x01",
            "人ごみには入っていけないんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x9,
        (
            "でも平気ですよ。\x01",
            "パレードは毎年\x01",
            "音だけで楽しいんですもの。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B1")

    label("loc_15CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_164F")

    #C0022
    ChrTalk(
        0x9,
        (
            "旧市街にも観光の人が\x01",
            "ちらほら来ているみたいですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "ふふ、華やかになったみたいで\x01",
            "とても嬉しいですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_16B1")

    label("loc_164F")


    #C0024
    ChrTalk(
        0x9,
        (
            "きれいな紙ふぶき……\x01",
            "毎年記念祭は心が躍りますねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x9,
        (
            "見ているだけで\x01",
            "とても楽しくなるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16B1")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_7_1399 end

    def Function_8_16B9(): pass

    label("Function_8_16B9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1738")

    #C0026
    ChrTalk(
        0xA,
        (
            "クソオヤジをたたき起こして\x01",
            "ミラをせしめてやったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xA,
        (
            "ニシシ……今日は\x01",
            "うめーもん食っちまうぜーっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1918")

    label("loc_1738")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_17C8")

    #C0028
    ChrTalk(
        0xA,
        (
            "ちぇっ、人が多くて\x01",
            "よく見えなかったなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        (
            "やっぱパレードなんて\x01",
            "ダメダメだってーの。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        "見ても腹、ふくれねーんだもん。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1918")

    label("loc_17C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1828")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1820")

    #C0031
    ChrTalk(
        0xA,
        (
            "オヤジは今日も飲んだくれてるし、\x01",
            "オレたちだけで行こうぜ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1823")

    label("loc_1820")

    Call(0, 9)

    label("loc_1823")

    Jump("loc_1918")

    label("loc_1828")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1893")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_188B")

    #C0032
    ChrTalk(
        0xA,
        "おりゃー！　かかってこいやー！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xA,
        "オレの必殺クラフトで沈めてやらァ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_188E")

    label("loc_188B")

    Call(0, 10)

    label("loc_188E")

    Jump("loc_1918")

    label("loc_1893")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_18DA")

    #C0034
    ChrTalk(
        0xA,
        (
            "今日は不良の兄ちゃんたち、\x01",
            "どっかいっちまったぞ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1918")

    label("loc_18DA")

    OP_4B(0x15, 0xFF)

    #C0035
    ChrTalk(
        0xA,
        "かんこー客だ！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        "おい、なんか恵んでくれよな！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x15, 0xFF)

    label("loc_1918")

    TalkEnd(0xFE)
    Return()

    # Function_8_16B9 end

    def Function_9_191C(): pass

    label("Function_9_191C")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0037
    ChrTalk(
        0xA,
        "ルゼ、聞いたか？\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xA,
        (
            "東通りの方に\x01",
            "パレードがくるらしーぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xB,
        "パレード～？\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        "なにそれ～、うめーの？\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xA,
        "ばーか、食いもんじゃねえよ～。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_9_191C end

    def Function_10_19C8(): pass

    label("Function_10_19C8")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0042
    ChrTalk(
        0xA,
        "おりゃー！　かかってこいやー！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "オレの必殺クラフトで\x01",
            "沈めてやらァ！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xB,
        (
            "クスクス……じゃあ\x01",
            "あたしは遊撃士のお姉さんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xB,
        "いくわよっ、奥義・太極輪……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_10_19C8 end

    def Function_11_1A82(): pass

    label("Function_11_1A82")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1ABA")

    #C0046
    ChrTalk(
        0xB,
        (
            "キャハハッ！\x01",
            "今日はゴチソウだね！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8E")

    label("loc_1ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1B20")

    #C0047
    ChrTalk(
        0xB,
        (
            "オトナにぶつかって\x01",
            "頭うっちゃった……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "でもちょっと楽しかったな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C8E")

    label("loc_1B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1B82")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1B7A")

    #C0049
    ChrTalk(
        0xB,
        "パレードってなに～？\x02",
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "食いもん？　うめーの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B7D")

    label("loc_1B7A")

    Call(0, 9)

    label("loc_1B7D")

    Jump("loc_1C8E")

    label("loc_1B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_1BFA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1BF2")

    #C0051
    ChrTalk(
        0xB,
        (
            "クスクス……じゃあ\x01",
            "あたしは遊撃士のお姉さんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        "いくわよっ、奥義・太極輪……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1BF5")

    label("loc_1BF2")

    Call(0, 10)

    label("loc_1BF5")

    Jump("loc_1C8E")

    label("loc_1BFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_1C4D")

    #C0053
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "わたがし、もらったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xB,
        "ヴァンと山分けだね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C8E")

    label("loc_1C4D")


    #C0055
    ChrTalk(
        0xB,
        "かんこー客だ！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "恵んでくれないと\x01",
            "イタズラしちゃうぞ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1A82 end

    def Function_12_1C92(): pass

    label("Function_12_1C92")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_1D93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1D0E")

    #C0057
    ChrTalk(
        0xC,
        (
            "今朝ね、東の空に\x01",
            "きれいな鳥が飛んでいたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xC,
        (
            "ふふっ、君たちにも\x01",
            "幸せが訪れますように！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D8E")

    label("loc_1D0E")


    #C0059
    ChrTalk(
        0xC,
        (
            "今朝ね、東の空に\x01",
            "きれいな鳥が飛んでいたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xC,
        "ふふっ、何だか得しちゃった気分だ。\x02",
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xC,
        "今日もいい日になるといいな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1D8E")

    Jump("loc_21EF")

    label("loc_1D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_1E12")

    #C0062
    ChrTalk(
        0xC,
        "ふう、今日もお掃除頑張ったな。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xC,
        "明日も朝が早いし……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xC,
        (
            "暗くなる前に帰って、\x01",
            "ぐっすり眠らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EF")

    label("loc_1E12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_1F24")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1E7E")

    #C0065
    ChrTalk(
        0xC,
        "さっさっ、さっさっ……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xC,
        (
            "紙ふぶきって、きれいな\x01",
            "雪が降っているみたいだよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F1F")

    label("loc_1E7E")


    #C0067
    ChrTalk(
        0xC,
        "さっさっ、さっさっ……\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xC,
        (
            "紙ふぶきが積もっちゃうから\x01",
            "最近、はき掃除が増えたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xC,
        (
            "でも、紙ふぶきって楽しいね。\x01",
            "なんだか雪が降っているみたいだもの。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_1F1F")

    Jump("loc_21EF")

    label("loc_1F24")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_20DB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_1F92")

    #C0070
    ChrTalk(
        0xC,
        "おろおろ、早く片付けをしないと。\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xC,
        (
            "喧嘩なんて悲しいこと、\x01",
            "しないでほしいな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_20D6")

    label("loc_1F92")


    #C0072
    ChrTalk(
        0xC,
        (
            "ぼくがいない間に\x01",
            "また喧嘩があったみたいなんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xC,
        "おろおろ、早く片付けをしないと。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xC,
        (
            "この辺りもめちゃくちゃに\x01",
            "荒らされちゃったんだ……\x02",
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

    #C0075
    ChrTalk(
        0x101,
        "#0006Fす、すみませんでした……\x02",
    )


    #C0076
    ChrTalk(
        0x104,
        "#0306F#6Pす、すみませんでした……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_20D6")

    Jump("loc_21EF")

    label("loc_20DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_2153")

    #C0077
    ChrTalk(
        0xC,
        (
            "きれいに掃除をすれば\x01",
            "観光の人たちも気持ちがいいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xC,
        (
            "ぼく、記念祭の間も\x01",
            "頑張ってお掃除するよ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EF")

    label("loc_2153")


    #C0079
    ChrTalk(
        0xC,
        (
            "あ、君たちも\x01",
            "ゴミ拾いを手伝ってくれるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xC,
        (
            "きれいにお掃除すれば\x01",
            "観光の人たちも気持ちがいいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "みんなが楽しんでくれると\x01",
            "ぼくも嬉しいな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)

    label("loc_21EF")

    TalkEnd(0xFE)
    Return()

    # Function_12_1C92 end

    def Function_13_21F3(): pass

    label("Function_13_21F3")

    TalkBegin(0xFE)
    Call(0, 14)
    TalkEnd(0xFE)
    Return()

    # Function_13_21F3 end

    def Function_14_21FD(): pass

    label("Function_14_21FD")

    OP_4B(0x8, 0xFF)
    OP_4B(0xD, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0082
    ChrTalk(
        0xD,
        (
            "いつからここが\x01",
            "テメエらの縄張りになったんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xD,
        "いい気になってんじゃねえぞコラァ！！\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xF,
        "僕たちが先に通ろうとしたんだ。\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0xF,
        "そちらこそ身の程を弁えたまえ！\x02",
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

    #C0086
    ChrTalk(
        0x102,
        "#0106Fまた懲りずに喧嘩してる……\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        "#0003Fはいはい、抑えて抑えて。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_14_21FD end

    def Function_15_2370(): pass

    label("Function_15_2370")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_243A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_23DB")

    #C0088
    ChrTalk(
        0xE,
        "見張りは俺が引き受けてやった。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xE,
        (
            "ディーノも今日は\x01",
            "楽しんでくればいいさ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2435")

    label("loc_23DB")


    #C0090
    ChrTalk(
        0xE,
        (
            "今日だけディーノの\x01",
            "見張りを代わってやったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xE,
        "へっ、これも先輩の務めだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_2435")

    Jump("loc_24B3")

    label("loc_243A")

    OP_4B(0xE, 0xFF)
    OP_4B(0x8, 0xFF)

    #C0092
    ChrTalk(
        0xE,
        "俺、そろそろ行かねえと。\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xE,
        (
            "ディーノ、しっかりな！\x01",
            "あんま寂しがるんじゃねーぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x8,
        "う、うっす！\x02",
    )

    CloseMessageWindow()
    OP_4C(0xE, 0xFF)
    OP_4C(0x8, 0xFF)

    label("loc_24B3")

    TalkEnd(0xFE)
    Return()

    # Function_15_2370 end

    def Function_16_24B7(): pass

    label("Function_16_24B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_24CB")
    Call(0, 14)
    Jump("loc_2556")

    label("loc_24CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_2553")

    #C0095
    ChrTalk(
        0xF,
        (
            "家にチケットがあったのでね、\x01",
            "最終日は出かけようかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xF,
        (
            "フン……途中でバイパーの連中と\x01",
            "出くわさなきゃいいんだが。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2556")

    label("loc_2553")

    Call(0, 17)

    label("loc_2556")

    TalkEnd(0xFE)
    Return()

    # Function_16_24B7 end

    def Function_17_255A(): pass

    label("Function_17_255A")

    OP_4B(0xF, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0097
    ChrTalk(
        0x10,
        (
            "ア、アルカンシェルのチケットを\x01",
            "持ってるなんて、さすがだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xF,
        (
            "残念ながら今日じゃなくて\x01",
            "記念祭の最終日だけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xF,
        (
            "……それに、親父の\x01",
            "おこぼれってのが気に入らないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x10,
        (
            "そ、そう言うな。\x01",
            "オレは嬉しい。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x10,
        (
            "じゃあ最終日、\x01",
            "２人で見に行こう。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xF, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xF, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_17_255A end

    def Function_18_2673(): pass

    label("Function_18_2673")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_26DA")

    #C0102
    ChrTalk(
        0x10,
        (
            "バ、バイパーの連中から\x01",
            "絡んできたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x10,
        (
            "こ、ここは、\x01",
            "受けて立つのが、筋だ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_276D")

    label("loc_26DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_276A")

    #C0104
    ChrTalk(
        0x10,
        "キーンツの家は、金持ちなんだ。\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x10,
        (
            "ち、父親も、ウルスラ大で\x01",
            "医者をやっている。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x10,
        (
            "……い、いい友人を\x01",
            "持つと、得をするな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_276D")

    label("loc_276A")

    Call(0, 17)

    label("loc_276D")

    TalkEnd(0xFE)
    Return()

    # Function_18_2673 end

    def Function_19_2771(): pass

    label("Function_19_2771")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_27D1")

    #C0107
    ChrTalk(
        0x11,
        "あら困ったわ……\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x11,
        (
            "でも今は無理に通らない方が\x01",
            "いいんじゃないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2908")

    label("loc_27D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_282A")

    #C0109
    ChrTalk(
        0x11,
        "ふふ、娘も大喜びでした。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x11,
        (
            "今年は家族で回れて\x01",
            "本当に良かったです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2908")

    label("loc_282A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2873")
    OP_4B(0x12, 0xFF)

    #C0111
    ChrTalk(
        0x11,
        (
            "リマ、手を繋ぐのよ。\x01",
            "ぜったい離れちゃダメよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_2908")

    label("loc_2873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_28DC")
    OP_4B(0x13, 0xFF)

    #C0112
    ChrTalk(
        0x11,
        (
            "あなた、今日は少し\x01",
            "足を落としてくださいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x11,
        "リマはまだ小さいんですから。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    Jump("loc_2908")

    label("loc_28DC")

    OP_4B(0x13, 0xFF)

    #C0114
    ChrTalk(
        0x11,
        "あなた、どこに行きましょうか。\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)

    label("loc_2908")

    TalkEnd(0xFE)
    Return()

    # Function_19_2771 end

    def Function_20_290C(): pass

    label("Function_20_290C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2955")
    OP_4B(0x13, 0xFF)

    #C0115
    ChrTalk(
        0x12,
        "パパ、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x12,
        "はやくいこうよ～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x13, 0xFF)
    Jump("loc_2ABB")

    label("loc_2955")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_29A6")

    #C0117
    ChrTalk(
        0x12,
        (
            "きらきらの車がねー、\x01",
            "ゆっくり通っていったの！\x02",
        )
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x12,
        "すごーい！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2ABB")

    label("loc_29A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2A03")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0119
    ChrTalk(
        0x12,
        (
            "ねえねえ、どうしてお空から\x01",
            "花びらがふってるの～？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Jump("loc_2ABB")

    label("loc_2A03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2A66")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2A5E")

    #C0120
    ChrTalk(
        0x12,
        "リマ、どこでもいいんだー。\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x12,
        "パパと一緒ならどこでもいいの！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A61")

    label("loc_2A5E")

    Call(0, 21)

    label("loc_2A61")

    Jump("loc_2ABB")

    label("loc_2A66")


    #C0122
    ChrTalk(
        0x12,
        (
            "きょうはパパとママと\x01",
            "一緒におさんぽなの！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)

    #C0123
    ChrTalk(
        0x12,
        "わーい！\x02",
    )

    CloseMessageWindow()

    label("loc_2ABB")

    TalkEnd(0xFE)
    Return()

    # Function_20_290C end

    def Function_21_2ABF(): pass

    label("Function_21_2ABF")

    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0124
    ChrTalk(
        0x13,
        (
            "リマ、今日は\x01",
            "どこに行きたいんだい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 1700, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0x12)

    #C0125
    ChrTalk(
        0x12,
        "えっとねー、あっち！\x02",
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0126
    ChrTalk(
        0x13,
        "あっちは……街道の方だね。\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x10)
    SetScenarioFlags(0x0, 3)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_21_2ABF end

    def Function_22_2B6E(): pass

    label("Function_22_2B6E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_2BC8")

    #C0127
    ChrTalk(
        0x13,
        (
            "出かけようとしたら\x01",
            "不良たちが揉めはじめたんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x13,
        "困ったな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_2DC2")

    label("loc_2BC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xAA, 2)), scpexpr(EXPR_END)), "loc_2C27")

    #C0129
    ChrTalk(
        0x13,
        "パレードを見るのはタダ……\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x13,
        (
            "なんて素晴らしい\x01",
            "家族思いのイベントなんだ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DC2")

    label("loc_2C27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_2CC5")
    OP_4B(0x11, 0xFF)
    OP_4B(0x12, 0xFF)
    OP_4B(0x13, 0xFF)

    #C0131
    ChrTalk(
        0x13,
        (
            "大丈夫、パレードは街中の大通りを\x01",
            "ぐるっと巡回して来るんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x13,
        (
            "東通りは最後の方だから\x01",
            "まだまだ時間があるはずさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    Jump("loc_2DC2")

    label("loc_2CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2D39")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2D31")
    OP_4B(0x12, 0xFF)

    #C0133
    ChrTalk(
        0x13,
        (
            "リマ、今日は\x01",
            "東通りを回ってみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x13,
        "露店街はきっとたのしいぞ～！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x12, 0xFF)
    Jump("loc_2D34")

    label("loc_2D31")

    Call(0, 21)

    label("loc_2D34")

    Jump("loc_2DC2")

    label("loc_2D39")


    #C0135
    ChrTalk(
        0x13,
        (
            "普段は一日中仕事だからね……\x01",
            "娘には寂しい思いを\x01",
            "させてたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x13,
        (
            "よおし、今日は一緒に回ろう。\x01",
            "今までの分まで遊んでやるぞ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DC2")

    TalkEnd(0xFE)
    Return()

    # Function_22_2B6E end

    def Function_23_2DC6(): pass

    label("Function_23_2DC6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2E15")
    OP_4B(0x8, 0xFF)

    #C0137
    ChrTalk(
        0x14,
        "ねえ、なあにココー。\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x14,
        "ぼくぅ、何してるの～？\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    Jump("loc_2E77")

    label("loc_2E15")


    #C0139
    ChrTalk(
        0x14,
        (
            "ここのバーに\x01",
            "入ろうと思ったんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x14,
        (
            "なんか今日は臨時休業なんだって。\x01",
            "つまんないのー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2E77")

    TalkEnd(0xFE)
    Return()

    # Function_23_2DC6 end

    def Function_24_2E7B(): pass

    label("Function_24_2E7B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_2EE1")
    OP_4B(0x14, 0xFF)

    #C0141
    ChrTalk(
        0x15,
        "オイオイ、やばいんじゃねえの？\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x15,
        (
            "あんま旧市街の連中に\x01",
            "関わるなって。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0x14, 0xFF)
    Jump("loc_3031")

    label("loc_2EE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 1)), scpexpr(EXPR_END)), "loc_2F56")

    #C0143
    ChrTalk(
        0x15,
        (
            "旧市街なんざ\x01",
            "来るもんじゃないって\x01",
            "言ったんだけどな……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x15,
        (
            "祭りなら街の方で\x01",
            "楽しめばいいんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3031")

    label("loc_2F56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_2FC6")

    #C0145
    ChrTalk(
        0x15,
        (
            "オレの女、\x01",
            "この辺りでみなかったか？\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x15,
        (
            "あいつ１人でとっとこ\x01",
            "旧市街に入ってきやがって……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3031")

    label("loc_2FC6")


    #C0147
    ChrTalk(
        0x15,
        (
            "うおっ……変なガキどもに\x01",
            "絡まれちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x15,
        (
            "くっそー、あいつは見失うし……\x01",
            "今日は厄日だなぁ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)

    label("loc_3031")

    TalkEnd(0xFE)
    Return()

    # Function_24_2E7B end

    def Function_25_3035(): pass

    label("Function_25_3035")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00000.itc", 0x2D)
    LoadChrToIndex("chr/ch00100.itc", 0x2E)
    LoadChrToIndex("chr/ch00200.itc", 0x2F)
    LoadChrToIndex("chr/ch00300.itc", 0x30)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("chr/ch24000.itc", 0x23)
    LoadChrToIndex("chr/ch21000.itc", 0x24)
    LoadChrToIndex("chr/ch24500.itc", 0x25)
    LoadChrToIndex("chr/ch21300.itc", 0x26)
    ClearMapObjFlags(0x8, 0x20)
    ClearMapObjFlags(0x8, 0x4)
    OP_70(0x8, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xA, 9150, 0, -7800, 275)
    SetChrPos(0xB, 9350, 0, -8700, 275)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x14, 8000, 0, -12000, 310)
    SetChrPos(0x15, 8600, 0, -11200, 310)
    SetChrChipByIndex(0x26, 0x23)
    SetChrSubChip(0x26, 0x0)
    SetChrChipByIndex(0x27, 0x24)
    SetChrSubChip(0x27, 0x0)
    ClearChrFlags(0x26, 0x80)
    ClearChrBattleFlags(0x26, 0x8000)
    ClearChrFlags(0x27, 0x80)
    ClearChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x8000)
    SetChrPos(0x26, 12000, 0, -5900, 270)
    SetChrPos(0x27, 11700, 0, -4750, 270)
    SetChrChipByIndex(0x28, 0x25)
    SetChrSubChip(0x28, 0x0)
    SetChrChipByIndex(0x29, 0x26)
    SetChrSubChip(0x29, 0x0)
    ClearChrFlags(0x28, 0x80)
    ClearChrBattleFlags(0x28, 0x8000)
    ClearChrFlags(0x29, 0x80)
    ClearChrBattleFlags(0x29, 0x8000)
    SetChrFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x8000)
    SetChrPos(0x28, 7500, 0, 400, 230)
    SetChrPos(0x29, 8050, 0, -400, 230)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x2D)
    SetChrChipByIndex(0x2B, 0x30)
    SetChrChipByIndex(0x2C, 0x2E)
    SetChrChipByIndex(0x2D, 0x2F)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    SetChrPos(0x2B, 1820, 0, -7540, 359)
    SetChrPos(0x2A, 480, 0, -6970, 116)
    SetChrPos(0x2C, 4750, 0, -8590, 291)
    SetChrPos(0x2D, 4320, 0, -9580, 309)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    SetChrPos(0x16, 3500, 0, -4840, 214)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrPos(0x17, 4070, 0, -5920, 235)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    SetChrPos(0x18, 350, 0, -4510, 162)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    SetChrPos(0x19, 1980, 0, -2970, 183)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    SetChrPos(0x1A, -1100, 0, -4400, 125)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, 3900, 0, -1750, 225)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrPos(0x1E, 2100, 0, -1550, 170)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0x5)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 5000, 0, -2900, 250)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0xD)
    SetChrPos(0x20, 1400, 0, -650, 170)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, 4400, 0, -200, 225)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -2100, 0, -5550, 80)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -2100, 0, -3250, 125)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -3250, 0, -3000, 125)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, -3000, 0, -4600, 85)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    OP_68(1850, 1000, -5600, 0)
    MoveCamera(70, 31, 0, 0)
    OP_6E(670, 0)
    SetCameraDistance(17310, 0)
    FadeToBright(5000, 0)
    MoveCamera(110, 31, 0, 60000)
    SetCameraDistance(12810, 30000)
    OP_0D()

    #C0149
    ChrTalk(
        0x18,
        (
            "#6P#0404Fフフ……なるほどね。\x02\x03",

            "旧市街の地形を利用した\x01",
            "追いかけっこ#12Rチ ェ イ ス バ ト ル#か……\x02\x03",

            "#0402Fなかなか楽しめそうじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x19,
        (
            "#5P#1602Fハッ、いいじゃねえか！\x02\x03",

            "妨害アリ、何でもアリの\x01",
            "ケンカレースってわけだな！？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x17,
        (
            "#5P#0903F#Nスピード、パワー、テクニック、\x01",
            "それに駆け引き……\x02\x03",

            "#0900F一通りが必要になるわけですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x16,
        "#5P#0802F#Nへえ～、面白そうかも！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0153
    ChrTalk(
        0x2B,
        "#11P#0309Fハハ、だろ？\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x2A,
        (
            "#6P#0006Fだろって……\x01",
            "ランディ、あのなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x2C,
        (
            "#5P#0106F#N喧嘩にならないのはいいけど……\x02\x03",

            "#0101F結局、周りの人たちに\x01",
            "迷惑をかけるんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x2D,
        (
            "#11P#0202F#Nまあ、その割には\x01",
            "皆さん見物に集まってますけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0157
    ChrTalk(
        0x18,
        (
            "#6P#0404Fま、いいんじゃない？\x01",
            "なんかお祭りっぽくてさ。\x02\x03",

            "#0400Fそれで……\x01",
            "本当に君たちも参加するワケ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x18, 500)

    #C0158
    ChrTalk(
        0x2A,
        (
            "#11P#0003F……仕方ないだろ。\x02\x03",

            "#0001Fここまで関わっておいて\x01",
            "知らん顔はどうかと思うし……\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x2B,
        "#11P#0302Fやれやれ、真面目だねぇ。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 800)
    TurnDirection(0x17, 0x2A, 500)

    #C0160
    ChrTalk(
        0x2A,
        (
            "#6P#0011Fランディの提案だろ！？\x02\x03",

            "#0003Fその代わり、完全に試合形式にして\x01",
            "ルールから外れた事はしないこと！\x02\x03",

            "#0013F決着が付いたら遺恨は残さず、\x01",
            "それ以上は争わないこと！\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x16,
        (
            "#5P#0806F#Nうーん、あたしたちは\x01",
            "もちろん異存はないけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A4E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3A4E)
    Sleep(50)

    def lambda_3A5E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_3A5E)
    Sleep(50)

    def lambda_3A6E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3A6E)
    Sleep(50)

    def lambda_3A7E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_3A7E)
    Sleep(50)

    def lambda_3A8E():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A8E)
    Sleep(300)

    #C0162
    ChrTalk(
        0x19,
        (
            "#6P#1604Fハ、俺もそれでいいぜ。\x02\x03",

            "#1602Fこうなったら遊撃士も警察も\x01",
            "まとめて相手をしてやるよ……\x02\x03",

            "#1607F誰が一番か証明するためになぁ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x19, 500)
    Sleep(150)

    #C0163
    ChrTalk(
        0x16,
        (
            "#11P#0802Fあはは、それじゃあ\x01",
            "正々堂々と戦いましょ。\x02\x03",

            "#0806Fそれと、さっきは\x01",
            "あたしの態度も悪かったかも。\x02\x03",

            "#0800Fその、ゴメンなさい。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x19,
        "#1605F#6Pは……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x16, 800)
    TurnDirection(0x2C, 0x16, 800)
    TurnDirection(0x2D, 0x16, 800)
    OP_63(0x2A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)

    #C0165
    ChrTalk(
        0x2A,
        "#12P#0012F（ま、また……）\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x2B,
        "#12P#0302F（すげぇな、相変わらず……）\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x18,
        (
            "#6P#0409Fあはは！　すごいねお姉さん！\x02\x03",

            "#0402Fこのタイミングで謝ったら\x01",
            "レースの意味が無いじゃんか！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x18, 500)

    #C0168
    ChrTalk(
        0x16,
        (
            "#5P#0805Fでも、試合形式にするって時点で\x01",
            "何かどうでもいいって言うか……\x02\x03",

            "#0809Fお互い全力を尽くして\x01",
            "楽しめればいいんじゃないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x17,
        "#11P#0906F#Nはあ、君って子は……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x2B, 500)

    #C0170
    ChrTalk(
        0x19,
        (
            "#5P#1603F……ケッ、変な女だぜ。\x02\x03",

            "#1601Fまあいい。\x01",
            "赤毛、ルールを説明しろや。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x2B,
        "#11P#0301F誰が赤毛だ、誰が。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_3E65():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_3E65)

    def lambda_3E72():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3E72)

    def lambda_3E7F():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_3E7F)

    def lambda_3E8C():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3E8C)

    def lambda_3E99():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3E99)

    def lambda_3EA6():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3EA6)
    Fade(500)
    OP_68(1830, 1100, -6450, 0)
    MoveCamera(179, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17810, 0)
    SetChrPos(0x2A, 260, 0, -6350, 128)
    SetChrPos(0x2C, 3370, 0, -9330, 319)
    SetChrPos(0x2D, 2520, 0, -9890, 1)
    SetChrPos(0x19, 1190, 0, -3490, 172)
    TurnDirection(0x2B, 0x19, 0)
    Sleep(1000)

    #C0172
    ChrTalk(
        0x2B,
        (
            "#5P#0300F──さっきも言ったように\x01",
            "レースの基本は『追いかけっこ』だ。\x02\x03",

            "#0304Fワジ＆ヴァルドの旧市街チーム。\x02\x03",

            "エステル＆ヨシュアの遊撃士チーム。\x02\x03",

            "#0300Fそしてロイド＆俺の支援課チーム。\x02\x03",

            "この３チームで、旧市街を３周して\x01",
            "一番早くゴールしたチームが勝者となる。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(-21270, 1380, -10450, 0)
    MoveCamera(313, 42, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(21500, 0)
    MoveCamera(313, 29, 0, 10000)
    OP_6E(340, 10000)
    Sleep(500)
    SetMessageWindowPos(14, 280, 60, 3)

    #A0173
    AnonymousTalk(
        0x2B,
        (
            "#0301F──ただし、各チームには毎周、\x01",
            "３箇所のチェックポイントを押さえてもらう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(44450, -1060, -22490, 0)
    MoveCamera(53, 26, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(24500, 0)
    MoveCamera(53, 14, 0, 10000)
    OP_6E(460, 10000)
    SetCameraDistance(16000, 10000)
    Sleep(300)

    #A0174
    AnonymousTalk(
        0x2B,
        (
            "#0303Fチェックポイントは通りの奥にある路地。\x01",
            "衝撃を与えると点灯する装置が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(36420, -5060, -38470, 0)
    MoveCamera(28, 26, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(24500, 0)
    MoveCamera(53, 26, 0, 10000)
    OP_6E(300, 10000)
    Sleep(300)

    #A0175
    AnonymousTalk(
        0x2B,
        (
            "#0302Fこいつを３箇所ぶっ叩かないと\x01",
            "１周したとは見なされないわけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1820, 1100, -6000, 0)
    MoveCamera(180, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17810, 0)
    MoveCamera(160, 21, 0, 30000)
    Sleep(1000)

    #C0176
    ChrTalk(
        0x2B,
        (
            "#5P#0303Fこの地形を利用することで\x01",
            "一方的に逃げることは不可能になる。\x02\x03",

            "#0300Fレース中は相手の妨害も可……\x02\x03",

            "つまり、よほど先行していない限り、\x01",
            "相手から妨害を受ける事になるわけだ。\x02\x03",

            "#0304Fそれを迎撃するも、何とか躱#2Rかわ#すも\x01",
            "チームごとの戦術的判断になるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x18,
        (
            "#12P#0405Fふーん……\x01",
            "よく出来たルールじゃない。\x02\x03",

            "#0400Fちなみにトラップとかはアリなの？\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x2B,
        (
            "#5P#0303Fアリ、としておこう。\x02\x03",

            "#0300F直接やり合うだけじゃなくて\x01",
            "地形を活かした妨害なんかも\x01",
            "可能になるってわけだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x2A,
        "#12P#0001Fなるほど……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x17,
        "#6P#0905F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x17, 500)

    #C0181
    ChrTalk(
        0x16,
        "#6P#0805Fヨシュア、どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x17,
        (
            "#6P#0903Fいや……\x01",
            "大体ルールは分かりました。\x02\x03",

            "#0900Fスタート順はどうするんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x2B, 500)

    #C0183
    ChrTalk(
        0x2B,
        (
            "#5P#0300Fコイントスでいいだろ。\x02\x03",

            "ロイド、ヴァルド、エステルちゃん。\x01",
            "それぞれ１ミラ硬貨を出しな。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x2A,
        "#12P#0005Fああ……\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x19,
        "#6P#1602Fハッ……\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x16,
        "#6P#0804Fん、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x2B,
        (
            "#5P#0304Fそれぞれ弾いて手の甲に。\x02\x03",

            "#0300F表か裏か、揃わなかった方が\x01",
            "１番手のスタートとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x2A,
        "#0000F#12Pなるほど。\x02",
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x16,
        "#0800F#6Pそれじゃ、ほいっっと。\x02",
    )

    CloseMessageWindow()

    def lambda_4685():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_4685)

    def lambda_469E():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_469E)

    def lambda_46B7():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_46B7)
    Sound(860, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0190
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとエステル、ヴァルドは\x01",
            "それぞれコイントスをした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_6E(470, 5000)
    Sleep(1800)

    #C0191
    ChrTalk(
        0x2A,
        "#0001F#12P表。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x16,
        "#0800F#6P表よ。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x19,
        (
            "#6P#1604F裏──\x01",
            "ハッ、俺たちが一番手か。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x2A,
        "#0001F#12Pむっ……\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x16,
        "#0801F#6Pぬぬっ……\x02",
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x2B,
        (
            "#5P#0300Fよし、そんじゃあ\x01",
            "ワジにコイントスしてもらうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x18,
        "#12P#0404F了解。\x02",
    )

    CloseMessageWindow()

    def lambda_4819():
        OP_A6(0xFE, 0x0, 0x64, 0xFA, 0x5DC)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4819)
    Sound(860, 0, 100, 0)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0198
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジはコイントスをした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    TurnDirection(0x2B, 0x16, 500)
    Sleep(300)

    #C0199
    ChrTalk(
        0x2B,
        (
            "#11P#0300Fロイド、エステルちゃん。\x02\x03",

            "表か裏かを選んでくれ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x2A, 500)

    #C0200
    ChrTalk(
        0x16,
        "#0805F#5Pえっと……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x16, 500)

    #C0201
    ChrTalk(
        0x2A,
        "#0002F#11Pいいよ、先に選んで。\x02",
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x16,
        (
            "#0809F#5Pあはは……\x01",
            "それじゃあ、表で。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x2A,
        "#0000F#11P俺は裏だ。\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ワジは掌を開いた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sleep(1000)

    #C0205
    ChrTalk(
        0x18,
        "#12P#0404F裏──二番手はロイド達だね。\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x16, 0x17, 500)

    #C0206
    ChrTalk(
        0x16,
        (
            "#0806F#6Pうう……\x01",
            "ゴメン、ヨシュア。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x16, 500)

    #C0207
    ChrTalk(
        0x17,
        (
            "#0904F#5Pはは、いいよ。\x02\x03",

            "#0900F今回のルールだったら\x01",
            "最初の順番は重要じゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x2C, 3540, 0, -7660, 2000, 0x0)
    TurnDirection(0x2C, 0x18, 500)

    #C0208
    ChrTalk(
        0x2C,
        (
            "#0100F#5P──えっと、それじゃあ\x01",
            "これで一通り決まったのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x2B,
        "#0304F#11Pああ、そうだな。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x19, 500)

    def lambda_4ADE():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4ADE)
    Sleep(50)

    def lambda_4AEE():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4AEE)
    Sleep(50)

    def lambda_4AFE():
        TurnDirection(0xFE, 0x2B, 300)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_4AFE)
    Sleep(500)

    #C0210
    ChrTalk(
        0x2B,
        (
            "#0300F#5Pそれじゃあレース前に\x01",
            "各チーム作戦会議と行こう。\x02\x03",

            "一度レースが始まったら\x01",
            "タイムとかは無しだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0211
    ChrTalk(
        0x16,
        "#0809F#6Pあはは、そうね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x19, 500)

    #C0212
    ChrTalk(
        0x18,
        (
            "#0409F#11Pフフ、それじゃあヴァルド。\x01",
            "仲良く打ち合わせしようか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x18, 500)

    #C0213
    ChrTalk(
        0x19,
        "#1601F#5Pハッ……気色悪ぃんだよ。\x02",
    )

    CloseMessageWindow()

    def lambda_4C18():
        OP_95(0xFE, 9480, 0, -3490, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4C18)
    Sleep(50)

    def lambda_4C35():
        OP_95(0xFE, 2900, 0, -8940, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_4C35)
    Sleep(50)

    def lambda_4C52():

        label("loc_4C52")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4C52")

    QueueWorkItem2(0x1D, 2, lambda_4C52)

    def lambda_4C64():

        label("loc_4C64")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4C64")

    QueueWorkItem2(0x1E, 2, lambda_4C64)

    def lambda_4C76():

        label("loc_4C76")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4C76")

    QueueWorkItem2(0x1F, 2, lambda_4C76)

    def lambda_4C88():

        label("loc_4C88")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4C88")

    QueueWorkItem2(0x20, 2, lambda_4C88)

    def lambda_4C9A():

        label("loc_4C9A")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4C9A")

    QueueWorkItem2(0x21, 2, lambda_4C9A)

    def lambda_4CAC():
        OP_95(0xFE, -800, 0, 1900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_4CAC)
    Sleep(100)

    def lambda_4CC9():
        OP_95(0xFE, 9180, 50, -2440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_4CC9)
    Sleep(50)

    def lambda_4CE6():

        label("loc_4CE6")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_4CE6")

    QueueWorkItem2(0x22, 2, lambda_4CE6)

    def lambda_4CF8():

        label("loc_4CF8")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_4CF8")

    QueueWorkItem2(0x23, 2, lambda_4CF8)

    def lambda_4D0A():

        label("loc_4D0A")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_4D0A")

    QueueWorkItem2(0x24, 2, lambda_4D0A)

    def lambda_4D1C():

        label("loc_4D1C")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_4D1C")

    QueueWorkItem2(0x25, 2, lambda_4D1C)

    def lambda_4D2E():

        label("loc_4D2E")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_4D2E")

    QueueWorkItem2(0x1A, 2, lambda_4D2E)

    def lambda_4D40():
        OP_95(0xFE, -1540, 0, 790, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4D40)
    Sleep(50)

    def lambda_4D5D():
        OP_95(0xFE, -4280, 0, -10520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_4D5D)
    Sleep(50)

    def lambda_4D7A():
        OP_95(0xFE, -3260, 0, -10950, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_4D7A)
    Sleep(1000)
    Fade(500)
    OP_68(-4510, 3150, -11210, 0)
    MoveCamera(57, 21, 0, 0)
    OP_6E(280, 0)
    SetCameraDistance(29500, 0)
    OP_68(-4510, 1750, -11210, 3000)
    MoveCamera(74, 29, 0, 3000)
    OP_6E(280, 3000)
    SetCameraDistance(29500, 3000)
    Sleep(3000)

    #C0214
    ChrTalk(
        0x2B,
        (
            "#11P#0303Fさて……ロイド。\x02\x03",

            "#0301F気付いてるかもしれんが\x01",
            "このレース、俺たちが一番不利だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x2A,
        (
            "#0006F#5Pまあね……\x02\x03",

            "#0013Fワジとヴァルドのチームは\x01",
            "旧市街を知り尽くしている。\x02\x03",

            "一方エステルとヨシュアのチームは\x01",
            "ポテンシャルが半端なさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0216
    ChrTalk(
        0x2B,
        (
            "#11P#0306Fそういうこった。\x02\x03",

            "#0301F俺たちが勝つ可能性があるとすれば\x01",
            "運と役割分担と的確な状況判断……\x02\x03",

            "#0300F俺は後衛に回るから\x01",
            "お前は前衛に徹してくれ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2A, 0x2B, 500)
    Sleep(150)

    #C0217
    ChrTalk(
        0x2A,
        (
            "#0005F#6Pいいけど……\x01",
            "足はランディの方が速いだろ？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2A, 500)

    #C0218
    ChrTalk(
        0x2B,
        (
            "#11P#0304Fコンビの場合、速い方がフォローに\x01",
            "回った方が連携が取りやすい。\x02\x03",

            "#0300Fそれに、防御に関していえば\x01",
            "お前のトンファーは相当なもんだ。\x02\x03",

            "迎撃するにしても、躱#2Rかわ#すにしても\x01",
            "的確な判断が出来るだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x2A,
        (
            "#0003F#6Pうーん……\x01",
            "分かった、やってみるよ。\x02\x03",

            "#0000Fどっちも手強そうだけど……\x01",
            "参加するんなら勝ちに行こう！\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x2B,
        "#0309F#11Pハハ、その意気だぜ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0221
    ChrTalk(
        0x2B,
        (
            "#11P#0305F……そうだな。\x02\x03",

            "#0300Fせっかくだから\x01",
            "コンビネーションを使った戦技#4Rクラフト#も\x01",
            "このあたりで試しておくか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0222
    ChrTalk(
        0x2A,
        "#0005F#6Pええっ……いきなり大丈夫か？\x02",
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0x2B,
        (
            "#11P#0304Fなに、お互いのクセも\x01",
            "だいたい判ってるだろうしな。\x02\x03",

            "#0300Fぶっつけ本番にはなるが──\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF0, 4)), scpexpr(EXPR_END)), "loc_53D6")
    AddCraft(0x0, 0x156)
    AddCraft(0x3, 0x156)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0224
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとランディがコンビクラフト\x01\x07\x02",

            "『バーニングレイジⅡ』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0226
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※なお、このチェイスバトルでは\x01",
            "　敵チームへの行動として選択する事が可能です。\x01",
            "　（ＣＰ消費を心配する必要はありません。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    Jump("loc_5519")

    label("loc_53D6")

    AddCraft(0x0, 0x14C)
    AddCraft(0x3, 0x14C)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとランディがコンビクラフト\x01\x07\x02",

            "『バーニングレイジ』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0229
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※なお、このチェイスバトルでは\x01",
            "　敵チームへの行動として選択する事が可能です。\x01",
            "　（ＣＰ消費を心配する必要はありません。）\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    label("loc_5519")

    EndChrThread(0x1D, 0xFF)
    EndChrThread(0x1E, 0xFF)
    EndChrThread(0x1F, 0xFF)
    EndChrThread(0x20, 0xFF)
    EndChrThread(0x21, 0xFF)
    EndChrThread(0x22, 0xFF)
    EndChrThread(0x23, 0xFF)
    EndChrThread(0x24, 0xFF)
    EndChrThread(0x25, 0xFF)
    EndChrThread(0x1A, 0xFF)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x26, 0x80)
    SetChrBattleFlags(0x26, 0x8000)
    SetChrFlags(0x27, 0x80)
    SetChrBattleFlags(0x27, 0x8000)
    SetChrFlags(0x28, 0x80)
    SetChrBattleFlags(0x28, 0x8000)
    SetChrFlags(0x29, 0x80)
    SetChrBattleFlags(0x29, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    Call(0, 71)
    Return()

    # Function_25_3035 end

    def Function_26_560C(): pass

    label("Function_26_560C")

    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x29)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_26_560C end

    def Function_27_569A(): pass

    label("Function_27_569A")

    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_27_569A end

    def Function_28_5702(): pass

    label("Function_28_5702")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -14710, 0, -11410, 7000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_28_5702 end

    def Function_29_5794(): pass

    label("Function_29_5794")

    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_29_5794 end

    def Function_30_5800(): pass

    label("Function_30_5800")

    SetChrPos(0xFE, -980, 0, -8050, 272)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -8980, 0, -10190, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 7000, 0x0)
    Return()

    # Function_30_5800 end

    def Function_31_58A3(): pass

    label("Function_31_58A3")

    SetChrPos(0xFE, -1210, 0, -9240, 256)
    SetChrChipByIndex(0xFE, 0x2D)
    OP_95(0xFE, -8740, 0, -11240, 6000, 0x0)
    OP_95(0xFE, -17490, 0, -11470, 6000, 0x0)
    Sleep(500)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_31_58A3 end

    def Function_32_5920(): pass

    label("Function_32_5920")

    SetChrPos(0xFE, -980, 0, -8050, 272)
    SetChrChipByIndex(0xFE, 0x30)
    OP_95(0xFE, -8980, 0, -10190, 6000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x2F)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x2E)
    SetChrSubChip(0xFE, 0x0)
    OP_93(0xFE, 0x5A, 0x1F4)
    SetChrChipByIndex(0xFE, 0x30)
    SetChrSubChip(0xFE, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 6000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 6000, 0x0)
    Return()

    # Function_32_5920 end

    def Function_33_59D3(): pass

    label("Function_33_59D3")

    SetChrPos(0xFE, -1210, 0, -9240, 256)
    SetChrChipByIndex(0xFE, 0x2D)
    OP_95(0xFE, -8740, 0, -11240, 5000, 0x0)
    OP_95(0xFE, -18490, 0, -11470, 4000, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_33_59D3 end

    def Function_34_5A4D(): pass

    label("Function_34_5A4D")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrPos(0xFE, -9470, -3280, -24010, 7000)
    OP_95(0xFE, -3020, -3880, -27130, 7000, 0x0)
    OP_95(0xFE, 8500, -6390, -35860, 6000, 0x0)
    OP_95(0xFE, 26760, -6490, -37430, 6000, 0x0)
    Return()

    # Function_34_5A4D end

    def Function_35_5A9F(): pass

    label("Function_35_5A9F")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrPos(0xFE, -11390, -3080, -24680, 6000)
    OP_95(0xFE, -4560, -3800, -27110, 6000, 0x0)
    OP_95(0xFE, 5280, -5590, -36320, 6000, 0x0)
    OP_95(0xFE, 26700, -6490, -39330, 6000, 0x0)
    Return()

    # Function_35_5A9F end

    def Function_36_5AF1(): pass

    label("Function_36_5AF1")

    SetChrChipByIndex(0xFE, 0x27)
    OP_95(0xFE, 22720, -6500, -37590, 7000, 0x0)
    OP_95(0xFE, 21220, -2500, -25410, 7000, 0x0)
    Return()

    # Function_36_5AF1 end

    def Function_37_5B1E(): pass

    label("Function_37_5B1E")

    Sleep(500)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 30470, -6500, -37950, 6000, 0x0)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 22440, -2550, -25860, 6000, 0x0)
    Return()

    # Function_37_5B1E end

    def Function_38_5B62(): pass

    label("Function_38_5B62")

    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 32280, -6500, -38450, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x35)
    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 22440, -2550, -25860, 6000, 0x0)
    Return()

    # Function_38_5B62 end

    def Function_39_5BCC(): pass

    label("Function_39_5BCC")

    Sound(532, 0, 100, 0)
    OP_71(0xF, 0xA, 0x28, 0x0, 0x20)
    OP_9D(0x2E, 0x66BC, 0xFFFFE890, 0xFFFF6A96, 0x3E8, 0xFA0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(826, 0, 100, 0)
    OP_9D(0x2E, 0x61A8, 0xFFFFE890, 0xFFFF6A96, 0x190, 0xFA0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_95(0x2E, 8840, -6430, -36090, 6000, 0x0)
    SetMapObjFlags(0xF, 0x4)
    Return()

    # Function_39_5BCC end

    def Function_40_5C4F(): pass

    label("Function_40_5C4F")

    SetChrPos(0xFE, 21840, -6500, -37170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_40_5C4F end

    def Function_41_5C9D(): pass

    label("Function_41_5C9D")

    SetChrPos(0xFE, 21840, -6500, -40170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_41_5C9D end

    def Function_42_5CEB(): pass

    label("Function_42_5CEB")

    SetChrChipByIndex(0xFE, 0x27)
    SetChrPos(0xFE, 25590, -2500, -24700, 340)
    OP_95(0xFE, 41840, -2500, -24090, 7000, 0x0)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_42_5CEB end

    def Function_43_5D1C(): pass

    label("Function_43_5D1C")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrPos(0xFE, 27000, -2500, -23420, 0)
    OP_95(0xFE, 43180, -2500, -22300, 5000, 0x0)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x29)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_43_5D1C end

    def Function_44_5D6F(): pass

    label("Function_44_5D6F")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 43240, -2500, -22630, 5000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 37240, -2500, -22750, 7000, 0x0)
    OP_95(0xFE, 19890, -2500, -22930, 7000, 0x0)
    OP_95(0xFE, 8740, 0, -11540, 6000, 0x0)
    OP_95(0xFE, 4170, -10, -8870, 7000, 0x0)
    OP_95(0xFE, -4930, -10, -8640, 7000, 0x0)
    OP_95(0xFE, -10890, -10, -11230, 7000, 0x0)
    OP_95(0xFE, -20220, 0, -10520, 7000, 0x0)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, -18070, 0, -10380, 6000, 0x0)
    OP_95(0xFE, -14710, 0, -11410, 6000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_44_5D6F end

    def Function_45_5EB5(): pass

    label("Function_45_5EB5")

    Sleep(500)
    OP_95(0xFE, 34760, -2500, -23810, 5000, 0x0)
    OP_95(0xFE, 19890, -2500, -22930, 6000, 0x0)
    OP_95(0xFE, 8740, 0, -11540, 7000, 0x0)
    OP_95(0xFE, 4170, -10, -8870, 7000, 0x0)
    OP_95(0xFE, -4930, -10, -8640, 7000, 0x0)
    OP_95(0xFE, -10890, -10, -11230, 6000, 0x0)
    OP_95(0xFE, -18320, 0, -11470, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    Sleep(1000)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_45_5EB5 end

    def Function_46_5F78(): pass

    label("Function_46_5F78")

    SetChrPos(0xFE, 21840, -6500, -37170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_46_5F78 end

    def Function_47_5FC6(): pass

    label("Function_47_5FC6")

    SetChrPos(0xFE, 21840, -6500, -40170, 0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -24770, 5000, 0x0)
    OP_95(0xFE, 41360, -2510, -23000, 6000, 0x0)
    Return()

    # Function_47_5FC6 end

    def Function_48_6014(): pass

    label("Function_48_6014")

    SetChrChipByIndex(0xFE, 0x33)
    SetChrPos(0xFE, -9470, -3280, -24010, 9000)
    OP_95(0xFE, -3020, -3880, -27130, 9000, 0x0)
    OP_95(0xFE, 8500, -6390, -35860, 9000, 0x0)
    OP_95(0xFE, 35200, -6490, -38160, 9000, 0x0)
    Return()

    # Function_48_6014 end

    def Function_49_6066(): pass

    label("Function_49_6066")

    SetChrChipByIndex(0xFE, 0x36)
    SetChrPos(0xFE, -11390, -3080, -24680, 9000)
    OP_95(0xFE, -4560, -3800, -27110, 9000, 0x0)
    OP_95(0xFE, 5280, -5590, -36320, 9000, 0x0)
    OP_95(0xFE, 33860, -6490, -39150, 9000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_49_6066 end

    def Function_50_60C3(): pass

    label("Function_50_60C3")

    SetChrChipByIndex(0xFE, 0x2D)
    SetChrPos(0xFE, 23260, -6490, -37200, 99)
    OP_95(0xFE, 32750, -6490, -37340, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)

    def lambda_60F5():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_60F5)
    SetChrFlags(0xFE, 0x4)
    Sound(854, 0, 100, 0)
    OP_9D(0xFE, 0x8EB2, 0xFFFFEC78, 0xFFFF69C4, 0x7D0, 0xFA0)
    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_9D(0xFE, 0x7FEE, 0xFFFFE6A6, 0xFFFF6E24, 0x1F4, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    SetChrChipByIndex(0xFE, 0x2D)
    Sound(326, 0, 100, 0)
    Sleep(300)
    OP_95(0xFE, 22640, -6490, -36980, 7000, 0x0)
    Return()

    # Function_50_60C3 end

    def Function_51_616F(): pass

    label("Function_51_616F")

    SetChrPos(0xFE, 22340, -6490, -38660, 94)
    Sleep(500)
    OP_95(0xFE, 31530, -6490, -39340, 7000, 0x0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrSubChip(0x17, 0x0)
    Sleep(1300)
    SetChrChipByIndex(0x17, 0x30)
    OP_95(0xFE, 22640, -6490, -36980, 7000, 0x0)
    Return()

    # Function_51_616F end

    def Function_52_61BB(): pass

    label("Function_52_61BB")

    SetChrChipByIndex(0xFE, 0x33)
    OP_95(0xFE, 21840, -6500, -37170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -24500, 6000, 0x0)
    OP_95(0xFE, 31620, -2500, -22500, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x31)

    def lambda_6218():

        label("loc_6218")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_6218")

    QueueWorkItem2(0xFE, 2, lambda_6218)
    Return()

    # Function_52_61BB end

    def Function_53_6226(): pass

    label("Function_53_6226")

    Sleep(400)
    SetChrChipByIndex(0xFE, 0x36)
    OP_95(0xFE, 21840, -6500, -38170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 7000, 0x0)
    OP_95(0xFE, 30970, -2500, -24000, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x34)

    def lambda_6286():

        label("loc_6286")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_6286")

    QueueWorkItem2(0xFE, 2, lambda_6286)
    Return()

    # Function_53_6226 end

    def Function_54_6294(): pass

    label("Function_54_6294")

    SetChrChipByIndex(0xFE, 0x27)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, 42800, -2500, -23020, 7000, 0x0)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x26)
    Sound(532, 0, 100, 0)
    OP_A1(0xFE, 0xFA0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0xFE, 0x27)
    OP_95(0xFE, 23080, -2500, -23890, 7000, 0x0)
    Return()

    # Function_54_6294 end

    def Function_55_62F1(): pass

    label("Function_55_62F1")

    Sleep(2400)
    SetChrChipByIndex(0xFE, 0x2A)
    EndChrThread(0xFE, 0x2)
    OP_95(0xFE, 23080, -2500, -23890, 7000, 0x0)
    Return()

    # Function_55_62F1 end

    def Function_56_6311(): pass

    label("Function_56_6311")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrFlags(0xFE, 0x4)
    Sound(814, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFCB8A, 0x10CC, 0xFFFFE049, 0x3E8, 0xFA0)
    SetChrChipByIndex(0xFE, 0x29)

    def lambda_6340():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6340)
    Sound(854, 0, 100, 0)
    OP_9D(0xFE, 0xFFFFB438, 0x7D0, 0xFFFFD7A6, 0x7D0, 0xFA0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_56_6311 end

    def Function_57_636B(): pass

    label("Function_57_636B")

    OP_93(0xFE, 0x10E, 0x320)
    SetChrChipByIndex(0xFE, 0x29)
    OP_71(0xB, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(100)
    SetChrChipByIndex(0xFE, 0x2A)
    OP_95(0xFE, -14710, 0, -11410, 7000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 7000, 0x0)
    Return()

    # Function_57_636B end

    def Function_58_63C6(): pass

    label("Function_58_63C6")

    OP_95(0xFE, -14710, 0, -11410, 5000, 0x0)
    OP_95(0xFE, -12880, 0, -13440, 5000, 0x0)
    OP_95(0xFE, -13020, -3100, -19730, 5000, 0x0)
    Return()

    # Function_58_63C6 end

    def Function_59_6403(): pass

    label("Function_59_6403")

    SetChrPos(0xFE, 30590, -6500, -36930, 45)
    OP_95(0xFE, 21840, -6500, -37170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 5000, 0x0)
    OP_95(0xFE, 22800, -2510, -24000, 6000, 0x0)
    OP_95(0xFE, 33880, -2500, -23450, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x38)
    BeginChrThread(0xFE, 2, 0, 70)
    OP_9C(0xFE, 0x3E8, 0x0, 0x0, 0x64, 0xBB8)
    Sound(514, 0, 100, 0)
    Return()

    # Function_59_6403 end

    def Function_60_648C(): pass

    label("Function_60_648C")

    SetChrPos(0xFE, 32990, -6500, -39280, 315)
    OP_95(0xFE, 21840, -6500, -38170, 5000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 7000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 6000, 0x0)
    OP_95(0xFE, 33550, -2500, -25230, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x37)
    BeginChrThread(0xFE, 2, 0, 70)
    Sound(590, 0, 100, 0)
    OP_9C(0xFE, 0x960, 0x0, 0x0, 0x64, 0xFA0)
    Sound(819, 0, 100, 0)
    Return()

    # Function_60_648C end

    def Function_61_651B(): pass

    label("Function_61_651B")

    SetChrPos(0xFE, 27350, -6500, -39590, 210)
    OP_95(0xFE, 21840, -6500, -37170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 5000, 0x0)
    OP_95(0xFE, 22800, -2510, -24500, 6000, 0x0)
    OP_95(0xFE, 33770, -2500, -22910, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x39)
    BeginChrThread(0xFE, 2, 0, 70)
    Sound(590, 0, 100, 0)
    OP_9C(0xFE, 0xBB8, 0x0, 0x0, 0x64, 0xBB8)
    Sound(819, 0, 100, 0)
    Return()

    # Function_61_651B end

    def Function_62_65AA(): pass

    label("Function_62_65AA")

    SetChrPos(0xFE, 29850, -6500, -40680, 135)
    OP_95(0xFE, 21840, -6500, -38170, 6000, 0x0)
    OP_95(0xFE, 21770, -5620, -33150, 6000, 0x0)
    OP_95(0xFE, 22800, -2510, -25000, 6000, 0x0)
    OP_95(0xFE, 33350, -2500, -24540, 6000, 0x0)
    SetChrChipByIndex(0xFE, 0x3A)
    BeginChrThread(0xFE, 2, 0, 70)
    OP_9C(0xFE, 0x4E2, 0x0, 0x0, 0x64, 0xFA0)
    Sound(514, 0, 100, 0)
    Return()

    # Function_62_65AA end

    def Function_63_6633(): pass

    label("Function_63_6633")

    OP_95(0xFE, 30930, 2390, -21190, 6000, 0x0)
    OP_95(0xFE, 34310, 2450, -21190, 6000, 0x0)
    OP_93(0xFE, 0xB4, 0x2BC)
    Return()

    # Function_63_6633 end

    def Function_64_6663(): pass

    label("Function_64_6663")

    OP_95(0x2A, 40240, -1000, -27180, 7000, 0x0)
    Sound(814, 0, 100, 0)
    OP_9D(0x2A, 0xA028, 0xFFFFF63C, 0xFFFFA07E, 0x3E8, 0xFA0)
    Sound(42, 0, 100, 0)
    Sound(31, 0, 100, 0)
    OP_95(0x2A, 43620, -2500, -22910, 7000, 0x0)
    SetChrChipByIndex(0xFE, 0x32)
    OP_71(0x9, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    OP_A1(0xFE, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Sleep(150)
    SetChrChipByIndex(0xFE, 0x33)
    OP_A1(0xFE, 0x7D0, 0x4, 0x0, 0x0, 0x0, 0x0)
    Sleep(150)
    OP_95(0x2A, 41240, -2490, -22980, 4000, 0x0)
    SetChrChipByIndex(0xFE, 0x31)

    def lambda_6707():

        label("loc_6707")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_6707")

    QueueWorkItem2(0xFE, 2, lambda_6707)
    Return()

    # Function_64_6663 end

    def Function_65_6715(): pass

    label("Function_65_6715")

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
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    OP_D5(0x0)
    OP_D5(0x1)
    OP_D5(0x2)
    OP_D5(0x3)
    OP_D5(0x4)
    OP_D5(0x6)
    OP_D5(0x7)
    OP_D5(0x8)
    OP_D5(0x9)
    OP_D5(0xA)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("chr/ch06000.itc", 0x23)
    LoadChrToIndex("apl/ch50378.itc", 0x24)
    LoadChrToIndex("chr/ch02150.itc", 0x25)
    LoadChrToIndex("chr/ch02152.itc", 0x26)
    LoadChrToIndex("chr/ch02151.itc", 0x27)
    LoadChrToIndex("chr/ch00450.itc", 0x28)
    LoadChrToIndex("chr/ch00452.itc", 0x29)
    LoadChrToIndex("chr/ch00451.itc", 0x2A)
    LoadChrToIndex("chr/ch00650.itc", 0x2B)
    LoadChrToIndex("chr/ch00652.itc", 0x2C)
    LoadChrToIndex("chr/ch00651.itc", 0x2D)
    LoadChrToIndex("chr/ch00750.itc", 0x2E)
    LoadChrToIndex("chr/ch00752.itc", 0x2F)
    LoadChrToIndex("chr/ch00751.itc", 0x30)
    LoadChrToIndex("chr/ch00050.itc", 0x31)
    LoadChrToIndex("chr/ch00052.itc", 0x32)
    LoadChrToIndex("chr/ch00051.itc", 0x33)
    LoadChrToIndex("chr/ch00350.itc", 0x34)
    LoadChrToIndex("chr/ch00352.itc", 0x35)
    LoadChrToIndex("chr/ch00351.itc", 0x36)
    LoadChrToIndex("chr/ch02153.itc", 0x37)
    LoadChrToIndex("chr/ch00453.itc", 0x38)
    LoadChrToIndex("chr/ch00653.itc", 0x39)
    LoadChrToIndex("chr/ch00753.itc", 0x3A)
    LoadChrToIndex("chr/ch00053.itc", 0x3B)
    LoadChrToIndex("chr/ch00353.itc", 0x3C)
    LoadChrToIndex("chr/ch00357.itc", 0x3D)
    LoadChrToIndex("apl/ch50311.itc", 0x3E)
    LoadChrToIndex("apl/ch50314.itc", 0x3F)
    LoadChrToIndex("chr/ch00155.itc", 0x40)
    LoadChrToIndex("apl/ch50312.itc", 0x41)
    ClearMapObjFlags(0x8, 0x20)
    ClearMapObjFlags(0x8, 0x4)
    OP_70(0x8, 0x0)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    OP_52(0x2A, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_65_6715 end

    def Function_66_6900(): pass

    label("Function_66_6900")

    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    OP_D5(0x30)
    OP_D5(0x31)
    OP_D5(0x32)
    OP_D5(0x33)
    OP_D5(0x34)
    OP_D5(0x35)
    OP_D5(0x36)
    OP_D5(0x37)
    OP_D5(0x38)
    OP_D5(0x39)
    OP_D5(0x3A)
    OP_D5(0x3B)
    OP_D5(0x3C)
    OP_D5(0x3D)
    OP_D5(0x3E)
    OP_D5(0x3F)
    OP_D5(0x40)
    OP_D5(0x41)
    Return()

    # Function_66_6900 end

    def Function_67_69E0(): pass

    label("Function_67_69E0")

    OP_A1(0xFE, 0x6A4, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Return()

    # Function_67_69E0 end

    def Function_68_69ED(): pass

    label("Function_68_69ED")

    OP_A1(0xFE, 0x6A4, 0x4, 0x0, 0x1, 0x2, 0x3)
    Return()

    # Function_68_69ED end

    def Function_69_69F8(): pass

    label("Function_69_69F8")

    OP_A1(0xFE, 0x6A4, 0x4, 0x3, 0x2, 0x1, 0x0)
    Return()

    # Function_69_69F8 end

    def Function_70_6A03(): pass

    label("Function_70_6A03")

    OP_A1(0xFE, 0x6A4, 0x3, 0x1, 0x2, 0x3)
    Return()

    # Function_70_6A03 end

    def Function_71_6A0D(): pass

    label("Function_71_6A0D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrBattleFlags(0x101, 0x8000)
    SetChrFlags(0x104, 0x80)
    SetChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    SetChrFlags(0x2A, 0x80)
    SetChrBattleFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x80)
    SetChrBattleFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    OP_49()
    Call(0, 65)
    LoadChrToIndex("chr/ch00000.itc", 0x37)
    LoadChrToIndex("chr/ch00100.itc", 0x38)
    LoadChrToIndex("chr/ch00200.itc", 0x39)
    LoadChrToIndex("chr/ch00300.itc", 0x3A)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrChipByIndex(0x2D, 0x39)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1B, 0x4)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1B, 0x23)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1C, 0x4)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1C, 0x24)
    SetChrSubChip(0x1C, 0x0)
    SetChrPos(0x2C, -5340, 0, -6550, 122)
    SetChrPos(0x2D, -4410, 0, -5830, 122)
    SetChrPos(0x18, -3140, 0, -8130, 302)
    SetChrPos(0x19, -3080, 0, -9580, 302)
    SetChrPos(0x2A, -980, 0, -8050, 302)
    SetChrPos(0x2B, -1210, 0, -9240, 302)
    SetChrPos(0x16, 1080, 0, -9140, 302)
    SetChrPos(0x17, 1580, 0, -7990, 302)
    SetChrPos(0x1A, -3500, 0, -4500, 170)
    SetChrPos(0x1C, 2240, 0, 6890, 180)
    SetChrPos(0x1B, 1050, 0, 7050, 180)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    SetChrPos(0x1D, 1950, 0, -4050, 240)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrPos(0x1E, 3400, 0, -5700, 275)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0x5)
    SetChrSubChip(0x1F, 0x0)
    SetChrPos(0x1F, 3600, 0, -3700, 240)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0xD)
    SetChrPos(0x20, 2850, 0, -2050, 220)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    SetChrPos(0x21, 4850, 0, -4050, 240)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    SetChrPos(0x22, -4350, 0, -1800, 160)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    SetChrPos(0x23, -4900, 0, -3800, 140)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    SetChrPos(0x24, -2700, 0, -3200, 160)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    SetChrPos(0x25, -6000, 0, -2600, 140)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    FadeToBright(4000, 0)
    OP_68(1350, 2000, -8800, 0)
    MoveCamera(358, 31, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16000, 0)
    OP_68(-2710, 1320, -6940, 5000)
    MoveCamera(348, 30, 0, 5000)
    OP_6E(540, 5000)
    SetCameraDistance(15740, 5000)
    Sleep(5000)

    #C0230
    ChrTalk(
        0x2C,
        (
            "#5P#0104F──それじゃあ、号令は\x01",
            "私が務めさせてもらうわね。\x02\x03",

            "#0100F最初の空砲で第１チームがスタート。\x02\x03",

            "５秒後の空砲で第２チームがスタート。\x02\x03",

            "更に５秒後、\x01",
            "最後の空砲で第３チームがスタート。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x2D,
        (
            "#5P#0204F……タイムのカウントは\x01",
            "わたしが担当します。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x1A,
        (
            "#5Pでは、我々は見物人が\x01",
            "巻き込まれないよう配慮しよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0233
    ChrTalk(
        0x18,
        "#5P#0404Fフフ、舞台が整ったみたいだね。\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 10, -1, -1)
    SetChrName("女性の声")

    #A0234
    AnonymousTalk(
        0xFF,
        "いいえ、真打ちがまだよ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_70B5():

        label("loc_70B5")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_70B5")

    QueueWorkItem2(0x2A, 0, lambda_70B5)
    Sleep(50)

    def lambda_70CA():

        label("loc_70CA")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_70CA")

    QueueWorkItem2(0x2D, 0, lambda_70CA)
    Sleep(50)

    def lambda_70DF():

        label("loc_70DF")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_70DF")

    QueueWorkItem2(0x19, 0, lambda_70DF)

    def lambda_70F1():

        label("loc_70F1")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_70F1")

    QueueWorkItem2(0x16, 0, lambda_70F1)
    Sleep(50)

    def lambda_7106():

        label("loc_7106")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7106")

    QueueWorkItem2(0x17, 0, lambda_7106)
    Sleep(50)

    def lambda_711B():

        label("loc_711B")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_711B")

    QueueWorkItem2(0x1A, 0, lambda_711B)
    Sleep(50)

    def lambda_7130():

        label("loc_7130")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7130")

    QueueWorkItem2(0x2C, 0, lambda_7130)
    Sleep(50)

    def lambda_7145():

        label("loc_7145")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7145")

    QueueWorkItem2(0x2B, 0, lambda_7145)

    def lambda_7157():

        label("loc_7157")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7157")

    QueueWorkItem2(0x18, 0, lambda_7157)
    Sleep(50)

    def lambda_716C():

        label("loc_716C")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_716C")

    QueueWorkItem2(0x1D, 2, lambda_716C)

    def lambda_717E():

        label("loc_717E")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_717E")

    QueueWorkItem2(0x1E, 2, lambda_717E)

    def lambda_7190():

        label("loc_7190")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7190")

    QueueWorkItem2(0x1F, 2, lambda_7190)

    def lambda_71A2():

        label("loc_71A2")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_71A2")

    QueueWorkItem2(0x20, 2, lambda_71A2)

    def lambda_71B4():

        label("loc_71B4")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_71B4")

    QueueWorkItem2(0x21, 2, lambda_71B4)

    def lambda_71C6():

        label("loc_71C6")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_71C6")

    QueueWorkItem2(0x22, 2, lambda_71C6)

    def lambda_71D8():

        label("loc_71D8")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_71D8")

    QueueWorkItem2(0x23, 2, lambda_71D8)

    def lambda_71EA():

        label("loc_71EA")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_71EA")

    QueueWorkItem2(0x24, 2, lambda_71EA)

    def lambda_71FC():

        label("loc_71FC")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_71FC")

    QueueWorkItem2(0x25, 2, lambda_71FC)

    def lambda_720E():
        OP_95(0xFE, -1220, 0, -4550, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_720E)

    def lambda_7228():
        OP_95(0xFE, -50, 0, -4300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7228)
    Sleep(500)
    Fade(500)
    OP_68(130, 620, -370, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(12500, 0)
    OP_68(-1140, 1860, -7560, 5000)
    MoveCamera(0, 31, 0, 5000)
    OP_6E(620, 5000)
    SetCameraDistance(12500, 5000)
    Sleep(5000)

    #C0235
    ChrTalk(
        0x2A,
        "#6P#0005Fグ、グレイスさん！？\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x17,
        "#12P#0905F確かクロスベルタイムズの……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x1B,
        (
            "#5P#2109Fやっほー、ボーイズ＆ガールズ。\x02\x03",

            "#2102F何だか面白そうなことを\x01",
            "やろうとしてるみたいじゃない？\x02\x03",

            "お姉さんも一枚噛ませなさいよね！\x02",
        )
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x2A,
        "#6P#0011Fか、噛ませなさいって……\x02",
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x19,
        "#6P#1600F#Nハッ、何をしやがるつもりだ？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0240
    ChrTalk(
        0x1B,
        "#5P#2101F答えは──これよ！\x02",
    )

    CloseMessageWindow()
    VolumeBGM(0x50, 0xC8)
    Sleep(100)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0xF)
    OP_68(-1210, 2000, -6530, 500)
    OP_6E(580, 500)
    SetCameraDistance(10500, 500)
    OP_93(0x1B, 0xA, 0x2BC)
    OP_93(0x1B, 0xB4, 0x2BC)
    Sound(534, 0, 100, 0)
    Sound(882, 0, 100, 0)
    CancelBlur(100)
    Sound(896, 0, 100, 0)
    SetChrChipByIndex(0x1B, 0x3E)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1C, 0x3F)
    SetChrSubChip(0x1C, 0x0)
    Sleep(1600)
    VolumeBGM(0x64, 0xC8)

    #C0241
    ChrTalk(
        0x1B,
        (
            "#5P#2110Fレースといえばやはり実況！\x02\x03",

            "#2109Fカメラマンも連れてきたから\x01",
            "思いっきり盛り上げてあげるわ！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x1C, -6880, 1800, -14620, 45)
    SetChrPos(0x1B, -5740, 1800, -14060, 45)
    OP_68(-3900, 2000, -10810, 0)
    MoveCamera(87, 29, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(16000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x2A, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x19, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_63(0x17, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-4080, 2000, -8980, 5000)
    MoveCamera(65, 29, 0, 5000)
    SetCameraDistance(16000, 5000)
    Sleep(1000)
    EndChrThread(0x2A, 0x0)
    EndChrThread(0x2C, 0x0)
    EndChrThread(0x2D, 0x0)
    EndChrThread(0x2B, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x18, 0x0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)

    #C0242
    ChrTalk(
        0x2D,
        (
            "#5P#0211Fなんだか本当に\x01",
            "お祭り騒ぎになった気が……\x02",
        )
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x16,
        (
            "#11P#0809F#Nあはは、いいじゃない。\x01",
            "喧嘩より何倍も楽しいわよ♪\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2C, 500)
    Sleep(300)

    #C0244
    ChrTalk(
        0x2B,
        (
            "#11P#0304Fやれやれ……\x01",
            "せいぜい期待しときますか。\x02\x03",

            "#0300Fそんじゃあ、そろそろ始めよう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7742():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_7742)

    def lambda_774F():
        TurnDirection(0xFE, 0x19, 500)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_774F)
    Sleep(100)

    def lambda_775F():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_775F)

    def lambda_776C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_776C)
    Sleep(100)

    def lambda_777C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x19, 0, lambda_777C)

    def lambda_7789():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 0, lambda_7789)
    Sleep(100)

    def lambda_7799():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_7799)

    def lambda_77A6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_77A6)

    def lambda_77B3():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1D, 2, lambda_77B3)

    def lambda_77C0():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1E, 2, lambda_77C0)

    def lambda_77CD():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x1F, 2, lambda_77CD)

    def lambda_77DA():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x20, 2, lambda_77DA)

    def lambda_77E7():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x21, 2, lambda_77E7)

    def lambda_77F4():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x22, 2, lambda_77F4)

    def lambda_7801():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_7801)

    def lambda_780E():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_780E)

    def lambda_781B():
        TurnDirection(0xFE, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_781B)

    #C0245
    ChrTalk(
        0x18,
        (
            "#0404F#5Pフフ、そうだね。\x02\x03",

            "#0402Fヴァルド、用意はいいかい？\x02",
        )
    )

    CloseMessageWindow()
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x19, 0x25)
    OP_A0(0x19, 2000, 0x0, 0xFB)

    #C0246
    ChrTalk(
        0x19,
        "#1602F#11Pハッ、いつでもいいぜ。\x02",
    )

    CloseMessageWindow()
    OP_68(-5100, 1610, -9070, 3000)
    MoveCamera(72, 29, 0, 3000)
    OP_6E(540, 3000)
    SetCameraDistance(16000, 3000)
    SetChrChipByIndex(0x18, 0x2A)

    def lambda_78D2():

        label("loc_78D2")

        TurnDirection(0xFE, 0x18, 400)
        Yield()
        Jump("loc_78D2")

    QueueWorkItem2(0x2D, 2, lambda_78D2)

    def lambda_78E4():
        OP_95(0xFE, -5130, 0, -8590, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_78E4)
    Sleep(100)
    SetChrChipByIndex(0x19, 0x27)
    OP_95(0x19, -5050, 0, -9830, 2000, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_791D():

        label("loc_791D")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_791D")

    QueueWorkItem2(0x19, 2, lambda_791D)
    Sleep(1000)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_7936():

        label("loc_7936")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_7936")

    QueueWorkItem2(0x18, 2, lambda_7936)
    Sleep(1000)

    def lambda_794B():
        OP_96(0xFE, 0xFFFFEB60, 0x0, 0xFFFFE8D6, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_794B)
    WaitChrThread(0x2C, 1)
    SetChrChipByIndex(0x2C, 0x40)
    SetChrSubChip(0x2C, 0x0)
    Sound(531, 0, 100, 0)
    SetChrFlags(0x2C, 0x2)
    OP_A0(0x2C, 1500, 0x6, 0x0)
    Fade(250)
    ClearChrFlags(0x2C, 0x2)
    SetChrChipByIndex(0x2C, 0x41)
    SetChrSubChip(0x2C, 0x0)
    Sound(804, 0, 100, 0)
    EndChrThread(0x2D, 0x2)
    OP_0D()

    #C0247
    ChrTalk(
        0x2D,
        (
            "#0202F#5P……それでは\x01",
            "カウントを始めます。\x02",
        )
    )

    CloseMessageWindow()
    OP_E5()
    StopBGM(0xBB8)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6E(1060, 6000)
    SetCameraDistance(7000, 6000)
    Sound(844, 0, 100, 0)

    #C0248
    ChrTalk(
        0x2D,
        "#0203F#10A《３》#6Rドライ#\x02",
    )
    #Auto

    Sleep(1000)
    Sound(844, 0, 100, 0)

    #C0249
    ChrTalk(
        0x2D,
        "#0203F#10A《２》#6Rツヴァイ#\x02",
    )
    #Auto

    Sleep(1000)
    Sound(844, 0, 100, 0)

    #C0250
    ChrTalk(
        0x2D,
        "#0203F#10A《１》#6Rアイン#\x02",
    )
    #Auto

    Sleep(1000)
    FadeToDark(0, 16777215, -1)
    FadeToBright(500, 16777215)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayBGM("ed7507", 0)
    EndChrThread(0x18, 0x2)
    EndChrThread(0x19, 0x2)
    SetChrChipByIndex(0x19, 0x27)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 26)
    BeginChrThread(0x19, 3, 0, 27)

    Fade(500)
    OP_67(0x1)
    OP_68(-6020, 2000, -9720, 0)
    MoveCamera(74, 9, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(27150, 0)
    Sound(845, 0, 100, 0)
    Sound(901, 0, 100, 0)

    #N0251
    NpcTalk(
        0x2D,
        "ティオ",
        "#0207F#5A#N──《０》#6Rヌル#！\x02",
    )
    #Auto

    Sleep(1000)
    OP_5A()
    SetMessageWindowPos(14, -10, -1, 3)

    #A0252
    AnonymousTalk(
        0x1B,
        "#4A#30W#2110Fさあ、レースの開始です！\x02",
    )
    #Auto

    Sleep(1000)
    EndChrThread(0x18, 0x3)
    Sleep(400)
    EndChrThread(0x19, 0x3)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_93(0x1B, 0x12C, 0x0)
    OP_93(0x1C, 0x12C, 0x0)
    SetChrPos(0x18, -3140, 0, -8130, 302)
    SetChrPos(0x19, -3080, 0, -9580, 302)
    SetChrChipByIndex(0x19, 0x27)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 26)
    BeginChrThread(0x19, 3, 0, 27)
    OP_67(0x1)
    OP_68(-17450, 2000, -12010, 2500)
    MoveCamera(296, 19, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(27150, 0)

    #A0253
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2110F第１組、ワジ＆ヴァルドチーム、\x01",
            "素晴らしいスタートを切りました！\x02",
        )
    )
    #Auto

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    #A0254
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2110F今、第一チェックポイントを通過し、\x01",
            "第二チェックポイントへ向かいました！\x02",
        )
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrSubChip(0x2C, 0x0)
    ClearChrFlags(0x2C, 0x2)
    Sound(845, 0, 100, 0)
    Fade(500)
    BeginChrThread(0x2A, 3, 0, 28)
    BeginChrThread(0x2B, 3, 0, 29)
    OP_67(0x1)
    OP_68(-4540, 2000, -9070, 0)
    MoveCamera(83, 10, -1, 0)
    OP_6E(320, 0)
    SetCameraDistance(27150, 0)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0255
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2100F第２組、ロイド＆ランディチーム、\x01",
            "スタートしました！\x02",
        )
    )
    #Auto

    Sleep(2400)
    EndChrThread(0x2A, 0x3)
    EndChrThread(0x2B, 0x3)
    Sleep(800)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x2A, -980, 0, -8050, 302)
    SetChrPos(0x2B, -1210, 0, -9240, 302)
    BeginChrThread(0x2A, 3, 0, 28)
    BeginChrThread(0x2B, 3, 0, 29)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(-20730, 2000, -11460, 0)
    MoveCamera(59, 32, 0, 2500)
    OP_6E(340, 0)
    SetCameraDistance(25650, 0)

    #A0256
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2100Fランディ選手、軽快な走り！\x01",
            "ロイド選手もなかなかの早さです！\x02",
        )
    )
    #Auto

    Sleep(4000)
    OP_57(0x0)
    OP_5A()

    #A0257
    AnonymousTalk(
        0x1B,
        "#8A#30W#2100F今、第一チェックポイントを通過！\x02",
    )
    #Auto

    Sleep(1800)
    OP_57(0x0)
    OP_5A()
    Sound(845, 0, 100, 0)
    Fade(500)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 30)
    BeginChrThread(0x16, 3, 0, 31)
    BeginChrThread(0x2A, 3, 0, 34)
    BeginChrThread(0x2B, 3, 0, 35)
    SetChrPos(0x18, 33790, -6490, -39680, 270)
    SetChrPos(0x19, 32409, -6490, -38140, 270)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(-4720, 2000, -6290, 0)
    MoveCamera(211, 26, -1, 0)
    OP_6E(340, 0)
    SetCameraDistance(25650, 0)
    SetMessageWindowPos(290, 145, -1, -1)

    #A0258
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2104F第３組、エステル＆ヨシュアチーム、\x01",
            "スタートです！\x02",
        )
    )
    #Auto

    Sleep(200)
    EndChrThread(0x2A, 0x3)
    EndChrThread(0x2B, 0x3)
    Sleep(2200)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    Sleep(800)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x16, 1080, 0, -9140, 302)
    SetChrPos(0x17, 1580, 0, -7990, 302)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 30)
    BeginChrThread(0x16, 3, 0, 31)
    OP_67(0x1)
    OP_68(-10660, 2000, -12350, 0)
    MoveCamera(53, 36, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(12970, 0)
    OP_68(-10660, 2000, -12350, 0)
    MoveCamera(316, 36, 0, 3500)
    OP_6E(620, 0)
    SetCameraDistance(12970, 0)

    #A0259
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2100Fチームワークは折り紙付き！\x01",
            "遊撃士としての実力もＡクラス！\x02",
        )
    )
    #Auto

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    #A0260
    AnonymousTalk(
        0x1B,
        (
            "#6A#30W#2100F今、第一チェックポイントを通過！\x01",
            "先行チームの追撃を開始します！\x02",
        )
    )
    #Auto

    Sleep(3400)
    OP_57(0x0)
    OP_5A()
    Fade(1500)
    OP_6B(0x2A)
    BeginChrThread(0x2A, 3, 0, 34)
    BeginChrThread(0x2B, 3, 0, 35)
    OP_67(0x1)
    OP_68(-9470, -3280, -24010, 0)
    MoveCamera(20, 18, 0, 0)
    OP_6E(880, 0)
    SetCameraDistance(11000, 0)
    MoveCamera(65, 18, 0, 4000)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_785F():

        label("loc_785F")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_785F")

    QueueWorkItem2(0x18, 2, lambda_785F)
    SetChrPos(0x18, 33790, -6490, -39680, 270)
    SetChrPos(0x19, 32409, -6490, -38140, 270)
    SetChrPos(0x16, 1080, 0, -9140, 272)
    SetChrPos(0x17, 1580, 0, -7990, 267)
    EndChrThread(0x16, 0x3)
    EndChrThread(0x17, 0x3)
    SetChrFlags(0x2C, 0x80)
    SetChrBattleFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x80)
    SetChrBattleFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    OP_93(0x1D, 0xB4, 0x0)
    OP_93(0x1E, 0xB4, 0x0)
    OP_93(0x1F, 0xB4, 0x0)
    OP_93(0x20, 0xB4, 0x0)
    OP_93(0x21, 0xB4, 0x0)
    SetChrPos(0x2E, 32409, -4800, -38140, 180)
    SetMapObjFlags(0xF, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    OP_78(0xF, 0x2E)
    OP_D3(0x2E, 0x0, 0x15F90, 0x0, 0x0)
    OP_49()
    OP_74(0xF, 0xF)
    OP_70(0xF, 0xA)
    ClearChrFlags(0x2E, 0x80)
    SetChrFlags(0x2E, 0x1)
    Sleep(3500)
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6B(0xFF)
    Fade(1000)
    OP_68(33490, -4540, -38270, 1000)
    MoveCamera(70, 18, 0, 1000)
    OP_6E(360, 1000)
    SetCameraDistance(22500, 1000)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0261
    AnonymousTalk(
        0x1B,
        (
            "#7A#30W#2105Fおおっと～！\x01",
            "ヴァルド選手いきなり大技だ！\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_57(0x0)
    OP_5A()

    #A0262
    AnonymousTalk(
        0x1B,
        "#8A#30W#2101Fさあロイドチーム、どうする！？\x02",
    )
    #Auto

    Sleep(1800)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrPos(0x2A, 13000, -6490, -37180, 78)

    def lambda_7A79():
        OP_95(0x2A, 23760, -6490, -37430, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 3, lambda_7A79)
    SetChrPos(0x2B, 12600, -6490, -39220, 315)

    def lambda_7AA4():
        OP_95(0x2B, 23700, -6490, -39330, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 3, lambda_7AA4)
    OP_68(21660, -5040, -38440, 0)
    MoveCamera(80, 10, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_68(29470, -5040, -38330, 2500)
    MoveCamera(83, 10, 0, 2500)
    OP_6E(420, 2500)
    SetCameraDistance(21000, 2500)

    #C0263
    ChrTalk(
        0x2A,
        "#5P#8A#30W#0001F（くっ……）\x02",
    )
    #Auto

    Sleep(1000)

    #C0264
    ChrTalk(
        0x2B,
        "#11P#12A#30W#0301F（判断は任せた……！）\x02",
    )
    #Auto

    Sleep(1800)
    OP_E6()
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【何とかかわす】\x01",          # 0
            "【そのまま突っ込む】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_7BC6"),
        (1, "loc_7D73"),
        (SWITCH_DEFAULT, "loc_802F"),
    )


    label("loc_7BC6")


    #C0265
    ChrTalk(
        0x19,
        "#6A#30W#1607F#4S#5P#Nおらああっ！！\x02",
    )
    #Auto

    BeginChrThread(0x2E, 3, 0, 39)
    SetChrChipByIndex(0x19, 0x26)
    BeginChrThread(0x19, 3, 0, 67)
    Sleep(400)

    def lambda_7C04():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_7C04)

    def lambda_7C11():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_7C11)

    def lambda_7C1E():
        OP_9D(0xFE, 0x6428, 0xFFFFE69C, 0xFFFF728E, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7C1E)

    def lambda_7C3B():
        OP_9D(0xFE, 0x6554, 0xFFFFE69C, 0xFFFF60DC, 0x1F4, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_7C3B)
    Sound(814, 0, 100, 0)
    Sleep(600)

    #C0266
    ChrTalk(
        0x18,
        "#9A#30W#0402F#5Pお先～！\x02",
    )
    #Auto

    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    OP_9D(0x18, 0x76CA, 0xFFFFE69C, 0xFFFF6AB4, 0x320, 0x1770)
    Sound(814, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 36)
    OP_95(0x18, 22720, -6500, -37590, 7000, 0x0)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0267
    AnonymousTalk(
        0x1B,
        (
            "#4A#30W#2103Fロイド＆ランディ選手、\x01",
            "ドラム缶を何とか回避！\x02",
        )
    )
    #Auto

    BeginChrThread(0x2A, 3, 0, 37)
    BeginChrThread(0x2B, 3, 0, 38)
    OP_95(0x18, 21220, -2500, -25410, 7000, 0x0)
    Sleep(1400)
    OP_57(0x0)
    OP_5A()

    #A0268
    AnonymousTalk(
        0x1B,
        (
            "#4A#30W#2101Fしかし体勢を崩してしまい、\x01",
            "ややタイムロスでしょうか！？\x02",
        )
    )
    #Auto

    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    Jump("loc_802F")

    label("loc_7D73")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0269
    ChrTalk(
        0x19,
        "#6A#30W#1607F#4S#5P#Nおらああっ！！\x02",
    )
    #Auto

    BeginChrThread(0x2E, 3, 0, 39)
    SetChrChipByIndex(0x19, 0x26)
    BeginChrThread(0x19, 3, 0, 67)
    Sleep(300)
    SetChrChip(0x0, 0x2A, 0x64, 0x1F4)
    SetChrChip(0x0, 0x2B, 0x64, 0x1F4)

    def lambda_7DD4():
        OP_9D(0xFE, 0x6978, 0xFFFFE69C, 0xFFFF6C58, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7DD4)

    def lambda_7DF1():
        OP_9D(0xFE, 0x6978, 0xFFFFE69C, 0xFFFF66E0, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_7DF1)
    Sound(250, 0, 100, 0)
    Sleep(100)
    EndChrThread(0x18, 0x2)

    def lambda_7E1B():
        OP_9D(0xFE, 0x76CA, 0xFFFFE69C, 0xFFFF6AB4, 0x320, 0x7D0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7E1B)
    Sound(814, 0, 100, 0)
    OP_68(31000, -5040, -38330, 1500)
    MoveCamera(59, 6, 0, 1500)
    OP_6E(420, 1500)
    SetCameraDistance(21000, 1500)
    Sleep(600)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_7E73():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_7E73)
    Sleep(600)
    SetChrChipByIndex(0x18, 0x29)

    def lambda_7E87():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_7E87)
    Sleep(200)
    SetChrChip(0x0, 0x18, 0x64, 0x1F4)

    def lambda_7E9F():
        OP_9D(0xFE, 0x6860, 0xFFFFE69C, 0xFFFF6D2A, 0x64, 0x2BC)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_7E9F)
    Sound(250, 0, 100, 0)
    Sound(541, 0, 100, 0)

    def lambda_7EC8():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2A, 0, lambda_7EC8)

    def lambda_7ED5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_7ED5)

    def lambda_7EE2():
        OP_9D(0xFE, 0x7530, 0xFFFFE69C, 0xFFFF7040, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_7EE2)

    def lambda_7EFF():
        OP_9D(0xFE, 0x7530, 0xFFFFE69C, 0xFFFF62F8, 0x384, 0xBB8)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_7EFF)
    Sound(814, 0, 100, 0)
    Sleep(200)
    TurnDirection(0x18, 0x2A, 500)
    SetChrChip(0x1, 0x18, 0x0, 0x0)
    SetChrChip(0x1, 0x2A, 0x0, 0x0)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    BeginChrThread(0x19, 3, 0, 36)

    #C0270
    ChrTalk(
        0x18,
        "#5A#30W#0402F#5Pハハ、やるじゃない！\x02",
    )
    #Auto

    SetChrChipByIndex(0x18, 0x2A)
    Sleep(700)
    SetChrChip(0x1, 0x2A, 0x0, 0x0)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    BeginChrThread(0x2A, 3, 0, 37)
    BeginChrThread(0x2B, 3, 0, 38)
    OP_95(0x18, 21220, -2500, -25410, 7000, 0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, -10, -1, 3)

    #A0271
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2104Fロイド＆ランディ選手、\x01",
            "なかなかの度胸でドラム缶を回避！\x02",
        )
    )
    #Auto

    Sleep(4000)
    OP_57(0x0)
    OP_5A()
    
    #A0272
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2100Fワジ選手のアタックもかわし、\x01",
            "第２チェックポイントを通過します！\x02",
        )
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()
    Jump("loc_802F")

    label("loc_802F")

    Fade(500)
    BeginChrThread(0x2A, 3, 0, 40)
    BeginChrThread(0x2B, 3, 0, 41)
    SetChrPos(0x19, 43020, -2500, -21880, 135)
    SetChrPos(0x18, 42830, -2500, -23790, 45)
    OP_6B(0x2A)
    OP_68(21840, -4500, -37170, 0)
    MoveCamera(1, 20, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    MoveCamera(67, 12, 0, 5000)
    Sleep(1000)
    BeginChrThread(0x19, 3, 0, 42)
    BeginChrThread(0x18, 3, 0, 43)
    Sleep(1500)
    Sleep(500)

    #C0273
    ChrTalk(
        0x2B,
        "#5P#6A#30W#0301F（どうする……！？）\x02",
    )
    #Auto

    Sleep(800)

    #C0274
    ChrTalk(
        0x2A,
        "#5P#8A#30W#0007F（……仕掛けよう……！）\x02",
    )
    #Auto

    Sleep(1200)
    EndChrThread(0x2B, 0x3)
    EndChrThread(0x2A, 0x3)
    OP_6B(0xFF)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【各個撃破】\x01",            # 0
            "【コンビクラフト】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8166"),
        (1, "loc_83C2"),
        (SWITCH_DEFAULT, "loc_861D"),
    )


    label("loc_8166")

    OP_68(42290, -500, -23200, 700)

    def lambda_817C():
        OP_95(0xFE, 42100, -2500, -22410, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_817C)

    def lambda_8196():
        OP_9D(0xFE, 0xA154, 0xFFFFFE0C, 0xFFFFA20E, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8196)
    Sound(854, 0, 100, 0)
    Sleep(700)
    ClearScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    Call(0, 65)
    LoadEffect(0x3, "event\\ev301_00.eff")
    EventBegin(0x0)
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_822C():

        label("loc_822C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_822C")

    QueueWorkItem2(0x2A, 2, lambda_822C)

    def lambda_823E():

        label("loc_823E")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_823E")

    QueueWorkItem2(0x2B, 2, lambda_823E)
    SetChrPos(0x2A, 40970, -2500, -22390, 21)
    SetChrPos(0x2B, 41410, -2500, -24040, 135)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    SetChrChipByIndex(0x18, 0x28)
    SetChrChipByIndex(0x19, 0x37)

    def lambda_829C():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_829C)
    BeginChrThread(0x19, 3, 0, 68)
    Sound(514, 0, 100, 0)
    SetChrPos(0x18, 42120, -2500, -20350, 180)
    SetChrPos(0x19, 43290, -2500, -24680, 331)
    OP_6B(0x2A)
    OP_68(41050, -500, -22430, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    OP_E5()
    FadeToBright(500, 0)
    OP_0D()

    #C0275
    ChrTalk(
        0x19,
        "#11P#8A#30W#1607Fくっ……！？\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x18,
        "#5P#12A#30W#0404Fははっ、喰らったね。\x02",
    )
    #Auto

    Sleep(2000)
    OP_57(0x0)
    OP_5A()

    #C0277
    ChrTalk(
        0x2A,
        "#5P#8A#30W#0000Fお先に！\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x2A, 3, 0, 44)

    #C0278
    ChrTalk(
        0x2B,
        "#5P#8A#30W#0309Fはは、悪く思うなよ～！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x36)
    BeginChrThread(0x2B, 3, 0, 45)
    Jump("loc_861D")

    label("loc_83C2")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(42290, -500, -23200, 700)

    def lambda_83EB():
        OP_95(0xFE, 42100, -2500, -22410, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_83EB)

    def lambda_8405():
        OP_9D(0xFE, 0xA154, 0xFFFFFE0C, 0xFFFFA20E, 0x5DC, 0xFA0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8405)
    Sound(854, 0, 100, 0)
    Sleep(700)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x3, "event\\ev301_00.eff")
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_849B():

        label("loc_849B")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_849B")

    QueueWorkItem2(0x2A, 2, lambda_849B)

    def lambda_84AD():

        label("loc_84AD")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_84AD")

    QueueWorkItem2(0x2B, 2, lambda_84AD)
    SetChrPos(0x2A, 40970, -2500, -22390, 21)
    SetChrPos(0x2B, 41410, -2500, -24040, 135)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    SetChrChipByIndex(0x18, 0x38)
    SetChrChipByIndex(0x19, 0x37)
    BeginChrThread(0x18, 3, 0, 68)
    BeginChrThread(0x19, 3, 0, 68)
    SetChrPos(0x18, 42120, -2500, -20350, 180)
    SetChrPos(0x19, 43290, -2500, -24680, 331)
    OP_6B(0x2A)
    OP_68(41050, -500, -22430, 0)
    MoveCamera(44, 30, 0, 0)
    OP_6E(740, 0)
    SetCameraDistance(14500, 0)
    OP_E5()
    Sound(514, 0, 100, 0)
    FadeToBright(500, 0)
    OP_0D()

    #C0279
    ChrTalk(
        0x19,
        "#8A#30W#1605F#11Pなっ……！？\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x18,
        "#8A#30W#0410F#5Pへえ、やるねぇ……\x02",
    )
    #Auto

    Sleep(2500)
    OP_57(0x0)
    OP_5A()

    #C0281
    ChrTalk(
        0x2A,
        "#8A#30W#0001F#5P悪いな……！\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x2A, 3, 0, 44)

    #C0282
    ChrTalk(
        0x2B,
        "#8A#30W#0300F#5P先に行くぜっ！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x36)
    BeginChrThread(0x2B, 3, 0, 45)
    Jump("loc_861D")

    label("loc_861D")

    Sleep(1000)
    BeginChrThread(0x16, 3, 0, 46)
    BeginChrThread(0x17, 3, 0, 47)
    Sleep(2000)
    OP_57(0x0)
    OP_5A()
    Sleep(3000)
    Fade(1000)
    OP_6B(0xFF)
    OP_67(0x1)
    OP_68(9060, 1990, -12040, 0)
    MoveCamera(44, 31, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22150, 0)
    OP_67(0x0)
    OP_6B(0x2A)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0283
    AnonymousTalk(
        0x1B,
        "#18A#30W#2100Fさあ２周目です！\x02",
    )
    #Auto

    Sleep(1000)
    OP_57(0x0)
    OP_5A()

    #A0284
    AnonymousTalk(
        0x1B,
        (
            "#20A#50W#2100Fロイド＆ランディ選手、\x01",
            "順位を繰り上げて……\x02",
        )
    )
    #Auto

    Sleep(2400)
    OP_57(0x0)
    OP_5A()

    #A0285
    AnonymousTalk(
        0x1B,
        "#6A#20W#2109F第１チェックポイントを通過！\x02",
    )
    #Auto

    SetChrPos(0x16, 1080, 0, -9140, 272)
    SetChrPos(0x17, 1580, 0, -7990, 267)
    SetChrChipByIndex(0x17, 0x2A)
    SetChrChipByIndex(0x16, 0x27)
    BeginChrThread(0x17, 3, 0, 32)
    BeginChrThread(0x16, 3, 0, 33)
    Sleep(2200)
    OP_57(0x0)
    OP_5A()

    OP_6B(0xFF)
    OP_67(0x1)

    #A0286
    AnonymousTalk(
        0x1B,
        (
            "#15A#20W#2105Fおおっと！\x01",
            "ここでエステル＆ヨシュア選手が\x01",
            "とんでもないスピードで追い上げてきた！\x02",
        )
    )
    #Auto

    Sleep(4000)
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(-4680, -1840, -26700, 0)
    MoveCamera(51, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    BeginChrThread(0x2A, 3, 0, 48)
    BeginChrThread(0x2B, 3, 0, 49)
    OP_6B(0x2A)
    MoveCamera(359, 18, 0, 5000)
    Sleep(1000)

    #C0287
    ChrTalk(
        0x2A,
        "#6A#30W#0008F#5Pくっ……！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x2B,
        "#8A#30W#0301F#5Pチッ、追いつかれるな……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(2300)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x2A, 0x3)
    OP_95(0x2A, 35200, -6490, -38160, 7000, 0x0)

    #C0289
    ChrTalk(
        0x2B,
        "#6A#30W#0307F#5Pおい、ロイド！\x02",
    )
    #Auto

    OP_71(0xA, 0x0, 0xF, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    SetChrChipByIndex(0x2A, 0x32)
    OP_A1(0x2A, 0x7D0, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_889F():
        OP_A0(0xFE, 1500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_889F)
    Sleep(300)

    #C0290
    ChrTalk(
        0x2A,
        "#6A#30W#0005F#5Pえ……？\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_6B(0xFF)
    OP_68(36410, -4540, -38600, 5000)
    MoveCamera(339, 31, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(22500, 5000)
    PlayEffect(0x3, 0xFF, 0xFF, 0x40, 34000, -7000, -36000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(898, 0, 100, 0)
    OP_71(0x8, 0x0, 0x14, 0x0, 0x8)
    FadeToDark(300, 16777215, 100)
    Sleep(500)

    #C0291
    ChrTalk(
        0x2A,
        "#8A#30W#0007F#5Pなっ……！？\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x2B,
        "#8A#30W#0310F石灰か……！\x02",
    )
    #Auto

    CloseMessageWindow()
    SetMessageWindowPos(14, -10, -1, 3)

    #A0293
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2105Fおおっとお！？\x01",
            "何だ何だこの白い煙は～！？\x02",
        )
    )
    #Auto

    Sleep(2800)
    OP_57(0x0)
    OP_5A()

    #A0294
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2110Fひょっとして、エステルチームが\x01",
            "仕掛けたトラップだったのか～！？\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    BeginChrThread(0x16, 3, 0, 50)
    BeginChrThread(0x17, 3, 0, 51)

    #C0295
    ChrTalk(
        0x16,
        "#6A#30W#0802F#5P#Nゴメンね～！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(1500)

    #C0296
    ChrTalk(
        0x17,
        "#6A#30W#0900F#5Pお先に！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x2A,
        "#9A#30W#0013F#5Pくっ……\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x2B,
        "#9A#30W#0307F追いかけるぞ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    FadeToBright(1300, 16777215)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_8AAA():

        label("loc_8AAA")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8AAA")

    QueueWorkItem2(0x16, 2, lambda_8AAA)
    SetChrChipByIndex(0x17, 0x2E)

    def lambda_8AC0():

        label("loc_8AC0")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8AC0")

    QueueWorkItem2(0x17, 2, lambda_8AC0)
    SetChrPos(0x17, 37300, -2500, -22500, 270)
    SetChrPos(0x16, 37800, -2500, -24000, 270)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrPos(0x19, 28020, -2500, -23450, 308)
    SetChrPos(0x18, 28260, -2500, -24990, 128)
    BeginChrThread(0x2A, 3, 0, 52)
    BeginChrThread(0x2B, 3, 0, 53)
    Sleep(1500)
    OP_68(23210, -4540, -36350, 0)
    MoveCamera(48, 16, 0, 0)
    OP_6E(960, 0)
    SetCameraDistance(10000, 0)
    Sleep(2400)
    OP_68(22810, -500, -24060, 0)
    MoveCamera(120, 35, 0, 0)
    OP_6E(460, 0)
    SetCameraDistance(26000, 0)
    Sleep(1500)
    OP_68(34300, 50, -22710, 0)
    MoveCamera(0, 20, 0, 0)
    OP_6E(840, 0)
    SetCameraDistance(11000, 0)
    Sleep(50)
    OP_E6()

    #C0299
    ChrTalk(
        0x16,
        "#0800F#11P来たわね……！\x02",
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x17,
        "#0901F#11P突破するよ……！\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x2A,
        "#0013F#5P（くっ……！）\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x16, 0x2D)
    SetChrChipByIndex(0x17, 0x30)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChipByIndex(0x2A, 0x33)

    def lambda_8C34():
        OP_99(0xFE, 0x2B, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8C34)

    def lambda_8C48():
        OP_99(0xFE, 0x2A, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8C48)

    def lambda_8C5C():
        OP_99(0xFE, 0x16, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8C5C)

    def lambda_8C70():
        OP_99(0xFE, 0x17, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8C70)
    Sleep(150)
    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x2B, 0x2)
    EndChrThread(0x2A, 0x2)
    EndChrThread(0x16, 0x2)
    EndChrThread(0x17, 0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【各個撃破】\x01",            # 0
            "【コンビクラフト】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    def lambda_8CE5():
        OP_99(0xFE, 0x2B, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8CE5)

    def lambda_8CF9():
        OP_99(0xFE, 0x2A, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8CF9)

    def lambda_8D0D():
        OP_99(0xFE, 0x16, 0x3E8, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_8D0D)

    def lambda_8D21():
        OP_99(0xFE, 0x17, 0x3E8, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_8D21)
    Sleep(150)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_8D49"),
        (1, "loc_9295"),
        (SWITCH_DEFAULT, "loc_9685"),
    )


    label("loc_8D49")

    OP_2C(0x44, 0x1)
    RunExpression(0x3, (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    ClearScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x0, "battle\\cr003300.eff")
    LoadEffect(0x1, "event\\ev302_01.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    OP_68(35610, -500, -24250, 0)
    MoveCamera(38, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x2A, 0x31)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_8E3A():

        label("loc_8E3A")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8E3A")

    QueueWorkItem2(0x2A, 2, lambda_8E3A)

    def lambda_8E4C():

        label("loc_8E4C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8E4C")

    QueueWorkItem2(0x2B, 2, lambda_8E4C)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_8E66():

        label("loc_8E66")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8E66")

    QueueWorkItem2(0x17, 2, lambda_8E66)

    def lambda_8E78():

        label("loc_8E78")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_8E78")

    QueueWorkItem2(0x16, 2, lambda_8E78)
    SetChrPos(0x17, 34690, -2500, -22950, 89)
    SetChrPos(0x16, 33910, -2500, -24380, 89)
    SetChrPos(0x2A, 36880, -2500, -23410, 270)
    SetChrPos(0x2B, 37460, -2500, -24500, 270)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    FadeToBright(500, 0)
    OP_0D()

    #C0302
    ChrTalk(
        0x16,
        "#1P#30W#0809Fナイスファイト！\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x17,
        "#5P#30W#0902F先に行くよ！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x16, 0x2D)

    def lambda_8F3A():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8F3A)
    Sleep(300)
    SetChrChipByIndex(0x17, 0x30)

    def lambda_8F5B():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_8F5B)

    #C0304
    ChrTalk(
        0x2A,
        "#30W#0013F#11Pくっ……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x2B, 0x5A, 0x1F4)
    OP_68(36790, -500, -24050, 1000)

    #C0305
    ChrTalk(
        0x2B,
        (
            "#30W#0307F#5Pチェックポイントを押さえて\x01",
            "とっとと追いかけるぞ──\x02",
        )
    )

    Sleep(500)
    OP_93(0x2A, 0x5A, 0x1F4)
    CloseMessageWindow()
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    Sound(1431, 255, 100, 0)
    Sleep(1500)

    #C0306
    ChrTalk(
        0x18,
        "#8A#30W#0402F#2Pよそ見厳禁だね……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_93(0x2B, 0x10E, 0x320)
    Sleep(500)
    EndChrThread(0x2B, 0x2)
    MoveCamera(320, 27, 0, 2000)
    OP_93(0x2A, 0x10E, 0x320)
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x19, 0x27)

    def lambda_9090():
        OP_99(0xFE, 0x2B, 0xFFFFFC18, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9090)

    def lambda_90A4():
        OP_99(0xFE, 0x2A, 0xFFFFFC18, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_90A4)
    Sound(1791, 255, 100, 2)
    Sleep(1050)
    OP_49()
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    Sound(834, 0, 100, 0)
    OP_68(38120, -500, -23640, 500)
    MoveCamera(358, 27, 0, 500)
    OP_6E(400, 500)
    SetCameraDistance(24500, 500)
    OP_49()
    Sleep(30)
    SetChrChipByIndex(0x2A, 0x3B)
    BeginChrThread(0x2A, 3, 0, 68)
    Sound(514, 0, 100, 0)

    def lambda_911B():
        OP_9D(0xFE, 0x9CC2, 0xFFFFF63C, 0xFFFFA9D4, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_911B)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_913C():

        label("loc_913C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_913C")

    QueueWorkItem2(0x18, 2, lambda_913C)
    SetChrChipByIndex(0x2B, 0x3C)
    BeginChrThread(0x2B, 3, 0, 68)

    def lambda_9158():
        OP_9D(0xFE, 0x9D4E, 0xFFFFF63C, 0xFFFFA04C, 0x64, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9158)
    Sound(1318, 255, 100, 1)

    #C0307
    ChrTalk(
        0x2A,
        "#11P#6A#30W#0010Fぐはっ……\x02",
    )
    #Auto


    #C0308
    ChrTalk(
        0x2B,
        "#12P#6A#30W#0310Fがっ……\x02",
    )
    #Auto

    Sleep(200)
    BeginChrThread(0x19, 3, 0, 54)
    Sleep(200)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_91C7():

        label("loc_91C7")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_91C7")

    QueueWorkItem2(0x18, 2, lambda_91C7)
    BeginChrThread(0x18, 3, 0, 55)
    Sleep(1000)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0309
    AnonymousTalk(
        0x1B,
        (
            "#16A#30W#2105Fなんとなんと！\x01",
            "追いついたワジ＆ヴァルド選手、\x01",
            "ロイドチームへの奇襲成功！\x02",
        )
    )
    #Auto

    Sleep(5200)
    OP_57(0x0)
    OP_5A()

    #A0310
    AnonymousTalk(
        0x1B,
        (
            "#16A#30W#2110Fそして第３チェックポイントを押さえ、\x01",
            "エステルチームの追撃に移ります！\x02",
        )
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()
    Jump("loc_9685")

    label("loc_9295")

    EndChrThread(0x2B, 0x1)
    EndChrThread(0x2A, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    Call(0, 65)
    LoadEffect(0x0, "battle\\cr003300.eff")
    LoadEffect(0x1, "event\\ev302_01.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    OP_68(35610, -500, -24250, 0)
    MoveCamera(38, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x2A, 0x3B)
    SetChrChipByIndex(0x2B, 0x3C)
    BeginChrThread(0x2A, 3, 0, 68)
    BeginChrThread(0x2B, 3, 0, 68)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x19, 0x27)
    SetChrPos(0x17, 34690, -2500, -22950, 89)
    SetChrPos(0x16, 33910, -2500, -24380, 89)
    SetChrPos(0x2A, 40130, -2500, -22060, 270)
    SetChrPos(0x2B, 40270, -2500, -24500, 270)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    Sound(514, 0, 100, 0)
    OP_68(36790, -500, -24050, 1500)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)

    #C0311
    ChrTalk(
        0x16,
        "#0800F#1Pじゃあね～！\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x17,
        "#0901F#5Pこのまま先行する！\x02",
    )

    CloseMessageWindow()

    def lambda_9441():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9441)
    Sleep(300)

    def lambda_945E():
        OP_95(0xFE, 17660, -2500, -22500, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_945E)

    #C0313
    ChrTalk(
        0x2A,
        "#0010F#11Pぐっ……\x02",
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x2B,
        "#0310F#11Pチッ、やられたな……\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    Sound(1431, 255, 100, 0)
    Sleep(1500)

    #C0315
    ChrTalk(
        0x18,
        "#0409F#2P白熱してるじゃん！\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_951E():
        OP_99(0xFE, 0x2B, 0xBB8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_951E)
    OP_68(38120, -500, -23640, 3500)
    MoveCamera(358, 27, 0, 3500)
    OP_6E(400, 3500)
    SetCameraDistance(24500, 3500)
    ClearChrFlags(0x2A, 0x1000)
    ClearChrFlags(0x2B, 0x1000)
    OP_99(0x19, 0x2A, 0xBB8, 0xFA0, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_957C():

        label("loc_957C")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_957C")

    QueueWorkItem2(0x19, 2, lambda_957C)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_9592():

        label("loc_9592")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9592")

    QueueWorkItem2(0x18, 2, lambda_9592)

    #C0316
    ChrTalk(
        0x19,
        "#1602Fクク……無様だなぁ！\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x18,
        "#5P#0402Fま、仇は取ってあげるよ！\x02",
    )

    CloseMessageWindow()
    Sound(1809, 255, 100, 1)
    BeginChrThread(0x19, 3, 0, 54)
    Sleep(200)
    BeginChrThread(0x18, 3, 0, 55)
    Sleep(500)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0318
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2100Fワジ＆ヴァルド選手、\x01",
            "倒れたロイドチームをスルーして\x01",
            "第３チェックポイントを通過！\x02",
        )
    )
    #Auto

    Sleep(5200)
    OP_57(0x0)
    OP_5A()

    #A0319
    AnonymousTalk(
        0x1B,
        "#8A#30W#2100Fエステルチームの追撃に移ります！\x02",
    )
    #Auto

    Sleep(2400)
    OP_57(0x0)
    OP_5A()
    Jump("loc_9685")

    label("loc_9685")

    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_969D():

        label("loc_969D")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_969D")

    QueueWorkItem2(0x2A, 2, lambda_969D)
    Sound(804, 0, 100, 0)
    OP_A1(0x2B, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_96C2():

        label("loc_96C2")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_96C2")

    QueueWorkItem2(0x2B, 2, lambda_96C2)

    #C0320
    ChrTalk(
        0x2A,
        (
            "#0010F#11Pぐっ……\x02\x03",

            "#0008Fくそっ、このままじゃ……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_970A():
        OP_A6(0xFE, 0x0, 0x14, 0x12C, 0x7D0)
        ExitThread()

    QueueWorkItem(0x2B, 3, lambda_970A)
    Sleep(300)
    Sound(1370, 255, 100, 0)
    Sleep(150)
    EndChrThread(0x2B, 0x2)
    Sleep(1500)
    #Sound(1371, 255, 100, 0)
    Sleep(100)

    #C0321
    ChrTalk(
        0x2B,
        "#0312F#11P#60W#12A……ハハハハハハハハッ……！\x02",
    )
    #Auto

    Sleep(1000)

    def lambda_9775():
        TurnDirection(0xFE, 0x2B, 500)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_9775)
    Sleep(2000)
    Sound(1310, 255, 100, 0)
    SetChrChipByIndex(0x2B, 0x3D)
    OP_A1(0x2B, 0x7D0, 0x4, 0x0, 0x0, 0x0, 0x0)

    def lambda_9799():
        OP_A6(0xFE, 0x64, 0x0, 0x320, 0x5DC)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_9799)
    CloseMessageWindow()
    PlayEffect(0x0, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(197, 0, 100, 0)
    Sound(183, 0, 100, 0)
    OP_68(40200, -500, -24500, 1500)
    MoveCamera(45, 27, 0, 1500)
    OP_6E(240, 1500)
    SetCameraDistance(24500, 1500)
    Sleep(1500)
    OP_6E(350, 0)
    PlayEffect(0x1, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(256, 0, 100, 0)
    Sound(325, 0, 100, 0)
    OP_A1(0x2B, 0x7D0, 0x1, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    Sleep(800)

    #C0322
    ChrTalk(
        0x2A,
        "#0011F#5Pラ、ランディ？\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_98B0():

        label("loc_98B0")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_98B0")

    QueueWorkItem2(0x2B, 2, lambda_98B0)
    Sleep(500)

    #C0323
    ChrTalk(
        0x2B,
        (
            "#0312F#11Pいいねぇ！　熱くなってきたぜ！\x02\x03",

            "こうなりゃとことん、\x01",
            "楽しませてもらおうじゃねえか！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToBright(1000, 0)
    SetChrChipByIndex(0x17, 0x2E)
    SetChrChipByIndex(0x16, 0x2B)
    BeginChrThread(0x17, 3, 0, 32)
    BeginChrThread(0x16, 3, 0, 33)
    OP_68(-7310, 2000, -9830, 0)
    MoveCamera(317, 27, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    OP_68(-19630, 2000, -10660, 4000)
    MoveCamera(297, 27, 0, 4000)
    OP_6E(400, 4000)
    SetCameraDistance(23270, 4000)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0324
    AnonymousTalk(
        0x1B,
        (
            "#16A#30W#2103Fさあエステルチーム、\x01",
            "広場を通過して３周目に突入！\x02",
        )
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()

    #A0325
    AnonymousTalk(
        0x1B,
        (
            "#20A#30W#2101Fこのまま独走を許せば\x01",
            "彼女たちの勝利となりますが……\x02",
        )
    )
    #Auto

    Sleep(400)
    EndChrThread(0x16, 0x3)
    OP_93(0x16, 0x5A, 0x1F4)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_9A40():

        label("loc_9A40")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9A40")

    QueueWorkItem2(0x16, 2, lambda_9A40)
    Sleep(300)
    EndChrThread(0x17, 0x3)
    SetChrChipByIndex(0x17, 0x2E)

    def lambda_9A5D():

        label("loc_9A5D")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9A5D")

    QueueWorkItem2(0x17, 2, lambda_9A5D)
    OP_93(0x17, 0x5A, 0x1F4)
    Sleep(2500)
    OP_57(0x0)
    OP_5A()

    SetChrChipByIndex(0x19, 0x25)

    def lambda_9A7D():

        label("loc_9A7D")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9A7D")

    QueueWorkItem2(0x19, 2, lambda_9A7D)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_9A93():

        label("loc_9A93")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9A93")

    QueueWorkItem2(0x18, 2, lambda_9A93)
    SetChrPos(0x19, -13190, 0, -10450, 270)
    SetChrPos(0x18, -10130, 4300, -7240, 270)
    OP_68(-15530, 2000, -10670, 700)
    OP_6E(380, 700)
    SetCameraDistance(23500, 700)

    #A0326
    AnonymousTalk(
        0x1B,
        (
            "#20A#30W#2105Fおっと～、やはり\x01",
            "そうは問屋が卸さないようですっ！\x02",
        )
    )
    #Auto

    Sleep(3600)
    OP_57(0x0)
    OP_5A()

    #C0327
    ChrTalk(
        0x16,
        "#0801F#5P来たわね──って。\x02",
    )

    CloseMessageWindow()
    Sleep(700)

    #C0328
    ChrTalk(
        0x16,
        "#0805F#5Pえ、何で一人なの……！？\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0329
    ChrTalk(
        0x17,
        "#0907F#5P#Nまさか……！？\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(-13540, 3200, -8170, 0)
    MoveCamera(312, 32, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    Sleep(500)

    #C0330
    ChrTalk(
        0x18,
        "#0402F#16A──当たり。\x02",
    )
    #Auto

    Sleep(1500)
    OP_68(-19160, 1990, -9840, 2000)
    MoveCamera(312, 55, 0, 2000)
    OP_6E(1080, 2000)
    SetCameraDistance(9000, 2000)
    EndChrThread(0x18, 0x2)
    BeginChrThread(0x18, 3, 0, 56)
    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x19, 0x27)

    def lambda_9C37():
        OP_99(0xFE, 0x17, 0x3E8, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_9C37)
    Sleep(1400)
    EndChrThread(0x19, 0xFF)
    EndChrThread(0x18, 0xFF)
    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200002, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1FB, 0x8)
    ClearScenarioFlags(0x5C, 0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x4, "event\\ev303_00.eff")
    LoadEffect(0x2, "event\\ev302_00.eff")
    LoadEffect(0x5, "event\\ev311_00.eff")
    LoadEffect(0x6, "event\\eva01_00.eff")
    EventBegin(0x0)
    Call(0, 65)
    OP_68(-18550, 1810, -10400, 0)
    MoveCamera(37, 33, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_9D2F():

        label("loc_9D2F")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9D2F")

    QueueWorkItem2(0x19, 2, lambda_9D2F)
    SetChrChipByIndex(0x18, 0x28)

    def lambda_9D45():

        label("loc_9D45")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_9D45")

    QueueWorkItem2(0x18, 2, lambda_9D45)
    SetChrPos(0x16, -16760, 0, -9580, 270)
    SetChrPos(0x17, -16400, 0, -11240, 270)
    SetChrPos(0x19, -19960, 0, -11410, 90)
    SetChrPos(0x18, -20100, 0, -9630, 90)
    SetChrPos(0x102, -5280, 0, -5930, 122)
    SetChrPos(0x103, -4410, 0, -5830, 122)
    FadeToBright(500, 0)
    OP_0D()

    #C0331
    ChrTalk(
        0x16,
        "#0802F#11Pやるじゃない！\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x19,
        "#1602F#6P#Nハッ、そっちこそな！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0333
    ChrTalk(
        0x18,
        (
            "#0402F#5Pフフ……\x01",
            "相当やるね、お兄さん。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x17,
        (
            "#0904F#11P君の方こそ……\x02\x03",

            "#0901F──エステル、行くよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x16,
        "#0801F#5Pうんっ！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x16, 0x2)
    SetChrChipByIndex(0x16, 0x2D)

    def lambda_9E82():
        OP_95(0xFE, -11620, 0, -14190, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_9E82)
    Sleep(400)
    EndChrThread(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x30)

    def lambda_9EA7():
        OP_95(0xFE, -11250, -540, -15070, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9EA7)

    #C0336
    ChrTalk(
        0x18,
        "#0407F#5Pヴァルド、追撃だ！\x02",
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x19,
        "#1607F#6P#N言われるまでもねえ！\x02",
    )

    CloseMessageWindow()
    OP_E5()
    EndChrThread(0x18, 0x2)
    SetChrChipByIndex(0x18, 0x2A)
    BeginChrThread(0x18, 3, 0, 57)
    Sleep(100)
    EndChrThread(0x19, 0x2)
    SetChrChipByIndex(0x19, 0x27)
    BeginChrThread(0x19, 3, 0, 58)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0338
    AnonymousTalk(
        0x1B,
        "#8A#30W#2100F激しいデッドヒートを始めた両チーム！\x02",
    )
    #Auto

    Sleep(2400)
    OP_57(0x0)
    OP_5A()

    #A0339
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2100Fもうこれで、この２チームに\x01",
            "勝利は絞られてしまうのでしょうか──\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChipByIndex(0x2A, 0x33)
    SetChrPos(0x2B, -6110, 0, -10730, 127)
    SetChrPos(0x2A, -6110, 0, -10730, 5)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0340
    ChrTalk(
        0x2B,
        "#12A#30W#0307F#4Sおおおおおおっ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_95(0x2B, -16000, 0, -10700, 11000, 0x0)
    Sound(1295, 255, 100, 0)

    def lambda_A036():
        OP_95(0xFE, -15720, 0, -10810, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A036)
    SetChrChipByIndex(0x2B, 0x35)
    SetChrFlags(0x2B, 0x1000)

    def lambda_A059():
        OP_A0(0xFE, 4000, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A059)
    Sound(532, 0, 100, 0)
    OP_96(0x2B, 0xFFFFADF8, 0x0, 0xFFFFD544, 0x4E20, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)
    PlayEffect(0x5, 0xFF, 0xFF, 0x0, -21800, 1200, -10600, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0xFF, 0xFF, 0x0, -21300, 1200, -10600, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    OP_71(0xB, 0x10, 0x19, 0x0, 0x8)
    Sound(897, 0, 100, 0)
    Sound(899, 0, 100, 0)
    SetChrChipByIndex(0x2B, 0x36)
    OP_96(0x2B, 0xFFFFB5C8, 0x0, 0xFFFFD634, 0x2EE0, 0x0)

    def lambda_A12F():
        OP_95(0xFE, -11250, -540, -15070, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_A12F)
    Sleep(700)

    def lambda_A14C():
        OP_95(0xFE, -11620, 0, -14190, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A14C)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0341
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2105Fす、凄い……！\x01",
            "凄まじいパワーです、ランディ選手！\x02",
        )
    )
    #Auto

    Sleep(4200)
    OP_57(0x0)
    OP_5A()

    #A0342
    AnonymousTalk(
        0x1B,
        (
            "#8A#30W#2106Fというかあの装置……\x01",
            "完全に壊れちゃってない？\x02",
        )
    )
    #Auto

    Sleep(3200)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    ClearMapObjFlags(0xC, 0x4)
    OP_68(30200, -4540, -39130, 0)
    MoveCamera(330, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    OP_6B(0x17)
    MoveCamera(60, 27, 0, 5000)
    BeginChrThread(0x18, 3, 0, 59)
    BeginChrThread(0x19, 3, 0, 60)
    BeginChrThread(0x16, 3, 0, 61)
    BeginChrThread(0x17, 3, 0, 62)
    Sleep(5000)
    OP_6B(0xFF)
    OP_68(33400, -500, -24080, 0)
    MoveCamera(91, 25, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(16000, 0)
    SetCameraDistance(14000, 3000)
    MoveCamera(91, 25, 5, 3000)
    Sleep(1000)
    SetChrFlags(0x2A, 0x4)
    SetChrPos(0x2A, 25000, -1000, -27210, 90)

    #C0343
    ChrTalk(
        0x19,
        "#8A#30W#1605F#11Pな、なんだァ！？\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    #C0344
    ChrTalk(
        0x17,
        "#8A#30W#0901F#12Pワイヤートラップ……！\x02",
    )
    #Auto

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x2A,
        "#5P#8A#30W#0007F──引っかかったな！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_68(41380, -500, -22950, 3000)
    MoveCamera(80, 16, 5, 3000)
    OP_6E(700, 3000)
    SetCameraDistance(16000, 3000)
    BeginChrThread(0x2A, 3, 0, 64)
    Sleep(4000)
    OP_68(37090, -500, -23670, 3000)
    MoveCamera(72, 30, 5, 7000)

    #C0346
    ChrTalk(
        0x16,
        "#10A#30W#0801F#6P#Nくっ……！\x02",
    )
    #Auto

    OP_A1(0x16, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x16, 0x2D)
    OP_95(0x16, 38410, -2490, -22860, 6000, 0x0)
    SetChrChipByIndex(0x16, 0x2B)

    def lambda_A3C1():

        label("loc_A3C1")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A3C1")

    QueueWorkItem2(0x16, 2, lambda_A3C1)
    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x19,
        "#8A#1607F#12P#N行かせるか、こらああ！！\x02",
    )
    #Auto

    OP_A1(0x19, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    Sound(804, 0, 100, 0)
    SetChrChipByIndex(0x19, 0x27)
    OP_95(0x19, 38260, -2490, -24380, 6000, 0x0)
    SetChrChipByIndex(0x19, 0x25)

    def lambda_A427():

        label("loc_A427")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A427")

    QueueWorkItem2(0x19, 2, lambda_A427)
    CloseMessageWindow()
    OP_E6()
    Sound(804, 0, 100, 0)
    OP_A1(0x17, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x17, 0x2E)

    #C0348
    ChrTalk(
        0x17,
        "#0907F#11P待った……！\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x18, 0x3E8, 0x3, 0x3, 0x2, 0x1)
    SetChrChipByIndex(0x18, 0x28)

    #C0349
    ChrTalk(
        0x18,
        "#0410F#5Pもう一人は──！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1373, 255, 100, 0)
    Sleep(1000)

    def lambda_A4AC():

        label("loc_A4AC")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A4AC")

    QueueWorkItem2(0x19, 0, lambda_A4AC)
    Sleep(50)

    def lambda_A4C1():

        label("loc_A4C1")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A4C1")

    QueueWorkItem2(0x16, 0, lambda_A4C1)
    Sleep(100)

    def lambda_A4D6():

        label("loc_A4D6")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A4D6")

    QueueWorkItem2(0x17, 0, lambda_A4D6)
    Sleep(50)

    def lambda_A4EB():

        label("loc_A4EB")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A4EB")

    QueueWorkItem2(0x18, 0, lambda_A4EB)
    OP_68(33430, -500, -22930, 4000)
    MoveCamera(56, 30, 5, 4000)
    SetChrPos(0x2B, 24970, -2400, -21190, 0)

    #C0350
    ChrTalk(
        0x2B,
        "#14A#30W#0312F#5P#N油断大敵だぜ！！\x02",
    )
    #Auto

    CloseMessageWindow()
    BeginChrThread(0x2B, 3, 0, 63)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)
    Fade(500)
    OP_68(34310, 4450, -21190, 0)
    MoveCamera(39, 10, 5, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    Sleep(700)
    OP_6B(0x2B)
    SetChrChip(0x0, 0x2B, 0x64, 0x3E8)
    SetChrChipByIndex(0x2B, 0x35)

    def lambda_A5D8():
        OP_A0(0xFE, 500, 0x0, 0xFB)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A5D8)
    SetChrFlags(0x2B, 0x4)
    MoveCamera(317, 48, 5, 1000)
    OP_6E(700, 1000)
    SetCameraDistance(16000, 1000)
    Sound(1297, 255, 100, 0)
    Sound(854, 0, 100, 0)
    OP_9D(0x2B, 0x8E94, 0xFFFFF63C, 0xFFFFA236, 0xFA0, 0xFA0)
    Sound(808, 0, 100, 0)
    OP_82(0x0, 0xC8, 0xBB8, 0x1F4)
    SetMapObjFlags(0xC, 0x4)
    PlayEffect(0x4, 0xFF, 0x2B, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(834, 0, 100, 0)
    Sound(813, 0, 100, 0)
    EndChrThread(0x19, 0x0)
    EndChrThread(0x16, 0x0)
    EndChrThread(0x17, 0x0)
    EndChrThread(0x18, 0x0)
    TurnDirection(0x17, 0x2B, 0)
    TurnDirection(0x18, 0x2B, 0)
    TurnDirection(0x16, 0x2B, 0)
    TurnDirection(0x19, 0x2B, 0)
    SetChrChipByIndex(0x17, 0x3A)
    SetChrChipByIndex(0x18, 0x38)
    SetChrChipByIndex(0x16, 0x39)
    SetChrChipByIndex(0x19, 0x37)
    Sound(514, 0, 100, 0)
    BeginChrThread(0x17, 3, 0, 68)
    BeginChrThread(0x18, 3, 0, 68)
    BeginChrThread(0x16, 3, 0, 68)
    BeginChrThread(0x19, 3, 0, 68)
    Sound(1741, 255, 100, 1)

    def lambda_A6EA():
        OP_9D(0xFE, 0x8340, 0xFFFFF63C, 0xFFFF9EBC, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A6EA)
    Sound(1404, 255, 100, 2)

    def lambda_A70D():
        OP_9D(0xFE, 0x8322, 0xFFFFF63C, 0xFFFFA6D2, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_A70D)
    Sound(1669, 255, 100, 3)

    def lambda_A730():
        OP_9D(0xFE, 0x9970, 0xFFFFF63C, 0xFFFFA93E, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_A730)
    Sound(1800, 255, 100, 4)

    def lambda_A753():
        OP_9D(0xFE, 0x9A6A, 0xFFFFF63C, 0xFFFF9F52, 0x64, 0xFA0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_A753)
    BlurSwitch(0x64, 0xBBFFFFFF, 0x0, 0x1, 0xF)
    Sleep(100)
    SetChrChipByIndex(0x2B, 0x36)
    SetChrChip(0x1, 0x2B, 0x0, 0x0)
    Sleep(500)
    CancelBlur(1000)
    Sleep(1500)
    OP_6B(0xFF)
    OP_6E(500, 3000)
    EndChrThread(0x2A, 0x2)
    SetChrChipByIndex(0x2A, 0x33)
    OP_95(0x2A, 38500, -2500, -23850, 5000, 0x0)
    SetChrChipByIndex(0x2A, 0x31)

    def lambda_A7C8():

        label("loc_A7C8")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A7C8")

    QueueWorkItem2(0x2A, 2, lambda_A7C8)

    #C0351
    ChrTalk(
        0x2A,
        "#0000Fナイス、ランディ！\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x2B, 0x34)

    def lambda_A7FA():

        label("loc_A7FA")

        OP_A0(0xFE, 1500, 0x0, 0xFB)
        Yield()
        Jump("loc_A7FA")

    QueueWorkItem2(0x2B, 2, lambda_A7FA)
    TurnDirection(0x2B, 0x2A, 500)

    #C0352
    ChrTalk(
        0x2B,
        (
            "#0307F#5Pおお！\x01",
            "このままゴールするぞ！\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x2B, 0x2)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2A, 0x4)
    SetChrChipByIndex(0x2B, 0x36)

    def lambda_A851():
        OP_95(0xFE, 21840, -2500, -24140, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_A851)
    Sleep(300)
    SetChrChipByIndex(0x2A, 0x33)

    def lambda_A872():
        OP_95(0xFE, 21840, -2500, -24140, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_A872)
    Sleep(1500)
    Fade(500)
    OP_68(8660, 1940, -13150, 0)
    MoveCamera(51, 27, 0, 0)
    OP_6E(1000, 0)
    SetCameraDistance(7500, 0)
    SetChrPos(0x1D, 11600, -10, -9000, 135)
    SetChrPos(0x1E, 12950, -10, -8500, 135)
    SetChrPos(0x1F, 12350, -10, -7600, 135)
    SetChrPos(0x20, 11800, -10, -6250, 135)
    SetChrPos(0x21, 11200, -10, -7700, 135)
    SetChrPos(0x22, 7900, -10, -6300, 135)
    SetChrPos(0x23, 8700, -10, -6800, 135)
    SetChrPos(0x24, 10250, -10, -6200, 135)
    SetChrPos(0x25, 9500, -10, -5100, 135)
    SetChrPos(0x1A, 8700, -10, -8100, 135)
    SetChrPos(0x102, 10750, 0, -11000, 135)
    SetChrPos(0x103, 10100, 0, -10600, 135)

    def lambda_A98E():

        label("loc_A98E")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A98E")

    QueueWorkItem2(0x1D, 2, lambda_A98E)

    def lambda_A9A0():

        label("loc_A9A0")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A9A0")

    QueueWorkItem2(0x1E, 2, lambda_A9A0)

    def lambda_A9B2():

        label("loc_A9B2")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A9B2")

    QueueWorkItem2(0x1F, 2, lambda_A9B2)

    def lambda_A9C4():

        label("loc_A9C4")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A9C4")

    QueueWorkItem2(0x20, 2, lambda_A9C4)

    def lambda_A9D6():

        label("loc_A9D6")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_A9D6")

    QueueWorkItem2(0x21, 2, lambda_A9D6)

    def lambda_A9E8():

        label("loc_A9E8")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A9E8")

    QueueWorkItem2(0x22, 2, lambda_A9E8)

    def lambda_A9FA():

        label("loc_A9FA")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_A9FA")

    QueueWorkItem2(0x23, 2, lambda_A9FA)

    def lambda_AA0C():

        label("loc_AA0C")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA0C")

    QueueWorkItem2(0x24, 2, lambda_AA0C)

    def lambda_AA1E():

        label("loc_AA1E")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA1E")

    QueueWorkItem2(0x25, 2, lambda_AA1E)

    def lambda_AA30():

        label("loc_AA30")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA30")

    QueueWorkItem2(0x1A, 2, lambda_AA30)

    def lambda_AA42():

        label("loc_AA42")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA42")

    QueueWorkItem2(0x102, 2, lambda_AA42)

    def lambda_AA54():

        label("loc_AA54")

        TurnDirection(0xFE, 0x2B, 500)
        Yield()
        Jump("loc_AA54")

    QueueWorkItem2(0x103, 2, lambda_AA54)
    SetChrChipByIndex(0x17, 0x30)
    SetChrChipByIndex(0x18, 0x2A)
    SetChrChipByIndex(0x16, 0x2D)
    SetChrChipByIndex(0x19, 0x27)
    ClearMapObjFlags(0xD, 0x4)
    SetChrPos(0x1B, 4500, 1800, -14300, 90)
    SetChrPos(0x1C, 4059, 1800, -13820, 90)
    SetChrPos(0x2A, 16940, -2170, -20310, 0)

    def lambda_AAAF():
        OP_95(0xFE, 4080, 0, -5300, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_AAAF)
    SetChrPos(0x2B, 16290, -2310, -21940, 0)

    def lambda_AADA():
        OP_95(0xFE, 2660, 0, -6540, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_AADA)
    BeginChrThread(0x101, 3, 0, 72)
    Sleep(1500)
    Sound(874, 0, 100, 0)
    Sound(881, 0, 100, 0)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0353
    AnonymousTalk(
        0x1B,
        "#12A#30W#2110F#4Sゴールッ！！#3S\x02",
    )
    #Auto

    Sleep(1500)
    OP_57(0x0)
    OP_5A()

    #A0354
    AnonymousTalk(
        0x1B,
        (
            "#16A#30W#2102F激しいレースを最後に制したのは\x01",
            "ロイド＆ランディチームでした！\x02",
        )
    )
    #Auto

    Sleep(3800)
    ClearChrFlags(0x19, 0x4)
    ClearChrFlags(0x16, 0x4)
    SetChrPos(0x18, 16940, -2170, -20310, 0)

    def lambda_ABAD():
        OP_95(0xFE, 4080, 0, -5300, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_ABAD)
    Sleep(200)
    SetChrPos(0x17, 16290, -2310, -21940, 0)

    def lambda_ABDB():
        OP_95(0xFE, 2660, 0, -6540, 7000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_ABDB)
    Sleep(200)
    SetChrPos(0x19, 16620, -2270, -21350, 0)

    def lambda_AC09():
        OP_95(0xFE, 3270, 0, -5970, 5500, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_AC09)
    SetChrPos(0x16, 16290, -2310, -21940, 0)

    def lambda_AC34():
        OP_95(0xFE, 2660, 0, -6540, 6800, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_AC34)
    OP_57(0x0)
    OP_5A()
    Sound(876, 0, 100, 0)
    SetMessageWindowPos(14, -10, -1, 3)

    #A0355
    AnonymousTalk(
        0x1B,
        "#16A#30W#2100Fここで他の２チームもゴール！\x02",
    )
    #Auto

    Sleep(1800)
    OP_57(0x0)
    OP_5A()

    #A0356
    AnonymousTalk(
        0x1B,
        "#16A#30W#2105Fあら、どっちが先なのかしら……？\x02",
    )
    #Auto

    Sleep(1800)
    OP_57(0x0)
    OP_5A()

    #A0357
    AnonymousTalk(
        0x1B,
        (
            "#2109Fまあいいや！\x01",
            "#16A#30Wとにかくみんなお疲れさま～っ！\x02",
        )
    )
    #Auto

    Sleep(3400)
    OP_57(0x0)
    OP_5A()

    #A0358
    AnonymousTalk(
        0x1B,
        "#24A#30W#2109F観客の皆さん、惜しみない拍手を～！\x02",
    )
    #Auto
    
    Sleep(3600)
    OP_57(0x0)
    OP_5A()

    Sound(900, 0, 100, 0)
    Sound(874, 0, 100, 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x1388)
    WaitBGM()
    WaitChrThread(0x101, 3)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x1A, 0x2)
    Call(0, 66)
    Call(0, 80)
    Return()

    # Function_71_6A0D end

    def Function_72_B556(): pass

    label("Function_72_B556")

    Sleep(1800)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x1D, 0x2)
    EndChrThread(0x1E, 0x2)
    EndChrThread(0x1F, 0x2)
    EndChrThread(0x20, 0x2)
    EndChrThread(0x21, 0x2)
    EndChrThread(0x22, 0x2)
    EndChrThread(0x23, 0x2)
    EndChrThread(0x24, 0x2)
    EndChrThread(0x25, 0x2)
    EndChrThread(0x1A, 0x2)
    Sleep(4200)

    def lambda_B591():

        label("loc_B591")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B591")

    QueueWorkItem2(0x1D, 2, lambda_B591)

    def lambda_B5A3():

        label("loc_B5A3")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B5A3")

    QueueWorkItem2(0x1E, 2, lambda_B5A3)

    def lambda_B5B5():

        label("loc_B5B5")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B5B5")

    QueueWorkItem2(0x1F, 2, lambda_B5B5)

    def lambda_B5C7():

        label("loc_B5C7")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B5C7")

    QueueWorkItem2(0x20, 2, lambda_B5C7)

    def lambda_B5D9():

        label("loc_B5D9")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B5D9")

    QueueWorkItem2(0x21, 2, lambda_B5D9)

    def lambda_B5EB():

        label("loc_B5EB")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B5EB")

    QueueWorkItem2(0x22, 2, lambda_B5EB)

    def lambda_B5FD():

        label("loc_B5FD")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B5FD")

    QueueWorkItem2(0x23, 2, lambda_B5FD)

    def lambda_B60F():

        label("loc_B60F")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B60F")

    QueueWorkItem2(0x24, 2, lambda_B60F)

    def lambda_B621():

        label("loc_B621")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B621")

    QueueWorkItem2(0x25, 2, lambda_B621)

    def lambda_B633():

        label("loc_B633")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B633")

    QueueWorkItem2(0x1A, 2, lambda_B633)

    def lambda_B645():

        label("loc_B645")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B645")

    QueueWorkItem2(0x102, 2, lambda_B645)

    def lambda_B657():

        label("loc_B657")

        TurnDirection(0xFE, 0x19, 500)
        Yield()
        Jump("loc_B657")

    QueueWorkItem2(0x103, 2, lambda_B657)
    Return()

    # Function_72_B556 end

    def Function_73_B665(): pass

    label("Function_73_B665")

    OP_95(0xFE, 1490, 0, 7480, 2000, 0x0)
    OP_95(0xFE, 1490, 0, 30000, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_73_B665 end

    def Function_74_B698(): pass

    label("Function_74_B698")

    OP_95(0xFE, 2460, 0, 6790, 2000, 0x0)
    OP_95(0xFE, 2460, 0, 30000, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_74_B698 end

    def Function_75_B6CB(): pass

    label("Function_75_B6CB")

    OP_95(0xFE, 7050, 0, 3670, 2000, 0x0)
    TurnDirection(0xFE, 0x2A, 500)
    Return()

    # Function_75_B6CB end

    def Function_76_B6E7(): pass

    label("Function_76_B6E7")

    OP_95(0xFE, 7380, 0, 2610, 2000, 0x0)
    TurnDirection(0xFE, 0x2B, 500)
    Return()

    # Function_76_B6E7 end

    def Function_77_B703(): pass

    label("Function_77_B703")

    OP_92(0xFE, 0x251C, 0xFFFFC392, 0x1F4)
    OP_95(0xFE, 9500, -300, -15470, 3000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_77_B703 end

    def Function_78_B72F(): pass

    label("Function_78_B72F")

    OP_92(0xFE, 0xFFFFF038, 0xC10CA3D7, 0x1F4)
    OP_95(0xFE, -4040, 0, -8790, 2000, 0x0)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_78_B72F end

    def Function_79_B75B(): pass

    label("Function_79_B75B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B7E7")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B797")
    Sleep(50)
    Jump("loc_B7DF")

    label("loc_B797")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B7AE")
    Sleep(150)
    Jump("loc_B7DF")

    label("loc_B7AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B7C5")
    Sleep(200)
    Jump("loc_B7DF")

    label("loc_B7C5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B7DC")
    Sleep(300)
    Jump("loc_B7DF")

    label("loc_B7DC")

    Sleep(400)

    label("loc_B7DF")

    Sleep(50)
    Jump("Function_79_B75B")

    label("loc_B7E7")

    Return()

    # Function_79_B75B end

    def Function_80_B7E8(): pass

    label("Function_80_B7E8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
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
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)
    SetChrFlags(0x1E, 0x80)
    SetChrBattleFlags(0x1E, 0x8000)
    SetChrFlags(0x1F, 0x80)
    SetChrBattleFlags(0x1F, 0x8000)
    SetChrFlags(0x20, 0x80)
    SetChrBattleFlags(0x20, 0x8000)
    SetChrFlags(0x21, 0x80)
    SetChrBattleFlags(0x21, 0x8000)
    SetChrFlags(0x22, 0x80)
    SetChrBattleFlags(0x22, 0x8000)
    SetChrFlags(0x23, 0x80)
    SetChrBattleFlags(0x23, 0x8000)
    SetChrFlags(0x24, 0x80)
    SetChrBattleFlags(0x24, 0x8000)
    SetChrFlags(0x25, 0x80)
    SetChrBattleFlags(0x25, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    LoadChrToIndex("chr/ch00000.itc", 0x37)
    LoadChrToIndex("chr/ch00100.itc", 0x38)
    LoadChrToIndex("chr/ch00200.itc", 0x39)
    LoadChrToIndex("chr/ch00300.itc", 0x3A)
    LoadChrToIndex("chr/ch00600.itc", 0x1E)
    LoadChrToIndex("chr/ch00700.itc", 0x1F)
    LoadChrToIndex("chr/ch00400.itc", 0x20)
    LoadChrToIndex("chr/ch02100.itc", 0x21)
    LoadChrToIndex("chr/ch06700.itc", 0x22)
    LoadChrToIndex("apl/ch50317.itc", 0x23)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis163.itp")
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x96, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x104, 0x8)
    SetChrFlags(0x102, 0x80)
    SetChrBattleFlags(0x102, 0x8000)
    SetChrFlags(0x103, 0x80)
    SetChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x2A, 0x4)
    ClearChrFlags(0x2B, 0x4)
    ClearChrFlags(0x2C, 0x4)
    ClearChrFlags(0x2D, 0x4)
    SetChrFlags(0x2A, 0x8000)
    SetChrFlags(0x2B, 0x8000)
    SetChrFlags(0x2C, 0x8000)
    SetChrFlags(0x2D, 0x8000)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrChipByIndex(0x2C, 0x38)
    SetChrChipByIndex(0x2D, 0x39)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    SetChrSubChip(0x2C, 0x0)
    SetChrSubChip(0x2D, 0x0)
    ClearChrFlags(0x2A, 0x80)
    ClearChrBattleFlags(0x2A, 0x8000)
    ClearChrFlags(0x2B, 0x80)
    ClearChrBattleFlags(0x2B, 0x8000)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x16, 0x1E)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x4)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x4)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x21)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x2A, 8400, 0, 3900, 0)
    SetChrChipByIndex(0x2A, 0x23)
    SetChrSubChip(0x2A, 0x0)
    SetChrFlags(0x2A, 0x2)
    SetChrPos(0x2B, 9170, 0, 3280, 224)
    SetChrFlags(0x2B, 0x8)
    SetChrPos(0x2D, 8600, 0, 6160, 185)
    SetChrPos(0x2C, 7740, 0, 6270, 161)
    SetChrPos(0x18, 8610, 0, -7590, 68)
    SetChrPos(0x19, 7270, 0, -9110, 178)
    SetChrPos(0x16, -4080, 0, -8100, 195)
    SetChrPos(0x17, -3180, 0, -9070, 287)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_68(8800, 2000, 4470, 0)
    MoveCamera(79, 19, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(24500, 0)
    Sleep(1000)
    Sleep(1000)
    PlayBGM("ed7514", 0)
    OP_6E(400, 10000)
    BeginChrThread(0x2A, 2, 0, 79)
    FadeToBright(1000, 0)
    OP_0D()
    SetChrPos(0x101, 8400, -700, 4570, 0)
    SetChrPos(0x104, 8890, -700, 3750, 0)

    #C0337
    ChrTalk(
        0x101,
        "#0006F#5P#50Wはあっ、はあっ、はあっ……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x104,
        "#0303F#11P#50Wはっ、はっ、はっ、はっ……\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x2C,
        (
            "#0102Fふふっ。\x01",
            "２人とも、お疲れさま。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x2D,
        (
            "#0202F#5P……凄いレースでした。\x01",
            "おめでとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        (
            "#0002F#5P#40Wいや……全部……ランディの、\x01",
            "作戦勝ちだよ……はあっ、はあっ……\x02",
        )
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x104,
        (
            "#0302F#11P#40Wいや……お前がいなけりゃ……\x01",
            "最後の仕掛けは……成り立たねぇさ……\x02\x03",

            "#0306F……ぐうっ……\x01",
            "さ、さすがに飛ばしすぎたぜ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2C, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0343
    ChrTalk(
        0x2C,
        "#0106Fふう、これだから男の子は……\x02",
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x2D,
        (
            "#0203F#5P単純というか、意地っ張りというか……\x02\x03",

            "#0202Fまあ、女の子も一人いましたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x2C,
        (
            "#0109Fふふ、そうね。\x02\x03",

            "#0102Fそうだ……\x01",
            "私、冷たい飲み物買ってくるわね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2D, 0x2C, 500)

    #C0346
    ChrTalk(
        0x2D,
        (
            "#0202F#11Pあ、わたしも付き合います。\x02\x03",

            "東通りの屋台でいいですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x2C,
        (
            "#0104Fええ、そうね。\x02\x03",

            "#0100F二人とも、ちょっと待ってて。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2C, 0xE1, 0x1F4)
    BeginChrThread(0x2C, 3, 0, 73)
    Sleep(400)
    BeginChrThread(0x2D, 3, 0, 74)
    Sleep(3000)
    Fade(500)
    OP_68(8660, 2000, 3480, 0)
    MoveCamera(104, 28, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    Sleep(500)
    OP_68(8660, 2000, 3480, 40000)
    MoveCamera(88, 10, 0, 40000)
    OP_6E(520, 40000)
    SetCameraDistance(15500, 40000)
    EndChrThread(0x2A, 0xFF)
    SetChrSubChip(0x2A, 0x8)
    Sleep(1500)

    #C0348
    ChrTalk(
        0x101,
        (
            "#0006F#30Wあー……うー……\x02\x03",

            "#0008Fそういえば……何で俺たち\x01",
            "こんなことしたんだっけ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x104,
        (
            "#0304F#30Wはは……\x01",
            "どうでもよくなっちまったな……\x02\x03",

            "#0308F#40W…………………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sound(820, 0, 100, 0)
    OP_A0(0x2A, 1200, 0x8, 0xA)
    OP_63(0x2B, 0xFFFFFE3E, 1000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2B)
    OP_63(0x2A, 0xFFFFFDA8, 1100, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1200)
    OP_A1(0x2A, 0x4B0, 0x3, 0xA, 0xD, 0xE)

    #C0350
    ChrTalk(
        0x101,
        "#0005F#30W……ランディ……？\x02",
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x104,
        (
            "#0303F#30W──正直、引いただろ……\x02\x03",

            "あんな風にキレちまってよ……\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x101,
        (
            "#0005F#30Wあ……\x02\x03",

            "#0001F#30W………………………………\x02",
        )
    )

    CloseMessageWindow()
    Sleep(1500)

    #C0353
    ChrTalk(
        0x104,
        (
            "#0308F#30W自分でも……よく分からねぇんだ。\x02\x03",

            "いつもヘラヘラ笑っている俺が\x01",
            "“今”の本当の俺なのか……\x02\x03",

            "#0308Fそれともあんな風にキレちまうのが\x01",
            "俺の本質なのか……\x02\x03",

            "#0303Fこの２年間で……\x01",
            "すっかり分からなくなっちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x101,
        "#0001F#30Wランディ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0xFFFFFDA8, 1100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x2A)

    #C0355
    ChrTalk(
        0x101,
        (
            "#0008F……その、警備隊に入る前には\x01",
            "どこにいたんだ？\x02\x03",

            "クロスベル出身じゃないことは\x01",
            "聞いているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x104,
        (
            "#0304F#30Wクク……どこにいたか。\x02\x03",

            "#0312F……煉獄#4Rれんごく#のように熱く……\x01",
            "冥府のように寒いところかね。\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x101,
        "#0005Fえ……\x02",
    )

    CloseMessageWindow()

    #C0358
    ChrTalk(
        0x104,
        (
            "#0311F#30W血も魂も沸騰し……\x01",
            "凍りつくような世界……\x02\x03",

            "あらゆる生命#4Rいのち#の輝きと……\x01",
            "クソのような汚泥が\x01",
            "入り混じったようなところ……\x02\x03",

            "#0303F……それが、俺のいた場所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x101,
        "#0001Fランディ……\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x104,
        "#0300F──なーんてな。\x02",
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x3, 0xE, 0xF, 0x10)
    Sleep(1000)
    Sound(820, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x5, 0x11, 0x12, 0x13, 0x14, 0x15)
    Sleep(1000)
    SetChrPos(0x101, 8240, -400, 3940, 0)
    SetChrPos(0x104, 8490, -300, 3110, 0)

    #C0361
    ChrTalk(
        0x104,
        (
            "#0309F#5Pはは、それっぽかったろ？\x02\x03",

            "#0302F……俺の過去なんざ、\x01",
            "そんな大層なもんじゃねえさ。\x02\x03",

            "今はただの、夜遊びが大好きな\x01",
            "クールでハンサムなナイスガイだ。\x02\x03",

            "#0304Fそれ以上でも、以下でもねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Sound(804, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x3, 0x15, 0x16, 0x17)
    OP_A1(0x2A, 0x5DC, 0x2, 0x19, 0x1A)
    Sleep(500)

    #C0362
    ChrTalk(
        0x101,
        (
            "#0008F#5P…………………………………\x02\x03",

            "#0006Fあのさ、ランディ。\x02\x03",

            "#0002F前にも話したけど……\x01",
            "俺には兄貴がいたんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x5DC, 0x2, 0x1A, 0x19)
    OP_A1(0x2A, 0x5DC, 0x5, 0x19, 0x1B, 0x1C, 0x1D, 0x1E)

    #C0363
    ChrTalk(
        0x104,
        "#0305F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x101,
        (
            "#0004F#5Pガイ・バニングス……\x01",
            "捜査一課に所属していた捜査官。\x02\x03",

            "とんでもなく破天荒で、\x01",
            "あり得ないくらい前向きで……\x02\x03",

            "事故で両親を亡くした後、\x01",
            "男手一人で俺を養ってくれて……\x02\x03",

            "憧れてた女性#4Rひと#を取られても\x01",
            "嫉妬すら沸いてこないような……\x02\x03",

            "#0000Fとにかく“凄い男”だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x104,
        "#0300F#11Pそっか……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    OP_A1(0x2A, 0x4B0, 0x5, 0x17, 0x18, 0x19, 0x18, 0x17)
    Sleep(500)

    #C0366
    ChrTalk(
        0x104,
        (
            "#0304F#5Pはは、お前も大変だな。\x02\x03",

            "そんなスゲエ兄貴の背中を\x01",
            "追いかけてるってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x101,
        (
            "#0012F#5P……まあね。\x02\x03",

            "#0008Fでさ、少し白状すると……\x02\x03",

            "#0002Fランディってさ……\x01",
            "ちょっと兄貴に似てるんだよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x96, 1600, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_A1(0x2A, 0x708, 0x5, 0x19, 0x1B, 0x1C, 0x1D, 0x1E)

    #C0368
    ChrTalk(
        0x104,
        "#0305F#11Pへ……\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        (
            "#0004F#5Pもちろん顔とかは\x01",
            "全然、似てないんだけど……\x02\x03",

            "いつも俺とか、エリィやティオを\x01",
            "さり気なくフォローしてくれるだろ？\x02\x03",

            "#0002Fそんな所がちょっと似てるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        (
            "#0305F#11Pお、おいおい……\x01",
            "こっ恥ずかしいこと言うなよ。\x02\x03",

            "#0309Fお兄さん、顔が赤くなっちまうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#0009F#5Pはは、そういう照れ隠しも\x01",
            "ちょっと似てるかも。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x104,
        "#0301F#11Pうっ……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#0004F#5Pだから俺、ランディのことを\x01",
            "尊敬してる所があるんだよな。\x02\x03",

            "ちゃんと“自分”を判っていて\x01",
            "他人にも気を遣えるところ……\x02\x03",

            "#0000F同僚っていうより、\x01",
            "一人前の“男”としてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x104,
        "#0305F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#0008F#5P……正直、俺はまだまだだ。\x02\x03",

            "多分、ランディの話を聞いても\x01",
            "間の抜けた言葉しか\x01",
            "出てこないんじゃないかと思う。\x02\x03",

            "#0004F──だからさ。\x02\x03",

            "#0000Fいつか俺が、兄貴やランディと\x01",
            "肩を並べられるようになったら……\x02\x03",

            "その時は、聞かせてくれないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x104,
        "#0302F#11P……ロイド………\x02",
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x4B0, 0x3, 0x1E, 0x1F, 0x20)
    OP_63(0x2B, 0x96, 1600, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0x2B)
    Sleep(300)
    Sound(1374, 255, 85, 0)    #voice#Randy
    Sleep(1200)
    OP_A1(0x2A, 0x4B0, 0x5, 0x20, 0x21, 0x22, 0x23, 0x24)
    Sound(820, 0, 100, 0)
    OP_A1(0x2A, 0x5DC, 0x5, 0x24, 0x25, 0x26, 0x25, 0x24)

    #C0377
    ChrTalk(
        0x101,
        "#0011F#5Pラ、ランディ……？\x02",
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x104,
        (
            "#0304F#11Pいや～、参った参った！\x02\x03",

            "#0300Fお嬢もこぼしてたけど\x01",
            "お前、天性の女たらしかもな。\x02\x03",

            "#0305Fおっと、この場合\x01",
            "アニキたらしってところか？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x101,
        (
            "#0011F#5Pな、なんだそりゃ……\x02\x03",

            "#0013Fていうか、半人前なのは確かだけど\x01",
            "子ども扱いはさすがにやめてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(1376, 255, 100, 0)    #voice#Randy
    Sleep(150)
    OP_82(0x64, 0x0, 0x7D0, 0x12C)

    #C0380
    ChrTalk(
        0x104,
        (
            "#0309F#11Pククッ……\x01",
            "#4Sははははははっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_A1(0x2A, 0x5DC, 0x4, 0x24, 0x25, 0x26, 0x25)
    OP_A1(0x2A, 0x5DC, 0x4, 0x24, 0x25, 0x26, 0x25)
    OP_A1(0x2A, 0x5DC, 0x5, 0x24, 0x25, 0x26, 0x25, 0x24)
    SetChrPos(0x2C, 2300, 0, 7050, 194)
    SetChrPos(0x2D, 1700, 0, 5650, 135)
    ClearChrFlags(0x2C, 0x80)
    ClearChrBattleFlags(0x2C, 0x8000)
    ClearChrFlags(0x2D, 0x80)
    ClearChrBattleFlags(0x2D, 0x8000)

    #N0381
    NpcTalk(
        0x2C,
        "エリィの声",
        "はあ……何やってるんだか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 1500, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x64, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(8240, 1500, 2820, 0)
    MoveCamera(22, 27, 0, 0)
    OP_6E(380, 0)
    SetCameraDistance(24500, 0)
    BeginChrThread(0x2C, 3, 0, 75)
    Sleep(600)
    BeginChrThread(0x2D, 3, 0, 76)
    Sleep(1000)
    Fade(250)
    ClearChrFlags(0x2A, 0x2)
    SetChrPos(0x2A, 8440, 0, 4040, 240)
    SetChrPos(0x2B, 9170, 0, 3280, 240)
    SetChrChipByIndex(0x2A, 0x37)
    SetChrChipByIndex(0x2B, 0x3A)
    SetChrSubChip(0x2A, 0x0)
    SetChrSubChip(0x2B, 0x0)
    Sound(804, 0, 100, 0)
    ClearChrFlags(0x2B, 0x8)
    Sleep(1500)

    #C0382
    ChrTalk(
        0x2C,
        "#0106F#6Pはい、冷たい飲み物。\x02",
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x2C, 0x0, 0x320, 0x5DC, 0x0)
    Sleep(100)
    OP_96(0x2C, 0x1B8A, 0x0, 0xE56, 0x4B0, 0x0)
    WaitChrThread(0x2D, 3)

    #C0383
    ChrTalk(
        0x2D,
        (
            "#0202F#6Pラムネの屋台があったので\x01",
            "買って来ました。\x02",
        )
    )

    CloseMessageWindow()
    OP_9B(0x0, 0x2D, 0x0, 0x44C, 0x5DC, 0x0)
    Sleep(100)
    OP_96(0x2D, 0x1CD4, 0x0, 0xA32, 0x4B0, 0x0)

    #C0384
    ChrTalk(
        0x2B,
        "#0302F#11Pお、ありがたいねぇ。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x2A,
        "#0002F#5Pああ、マジで助かるよ。\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    #C0386
    ChrTalk(
        0x2A,
        "#0003F#11P#10A#70Wんくっ、んくっ、んくっ……\x02",
    )
    #Auto


    #C0387
    ChrTalk(
        0x2B,
        "#0303F#12P#10A#70Wんくっ、んくっ、んくっ……\x02",
    )
    #Auto

    Sound(887, 0, 100, 0)
    Sleep(800)
    Sound(887, 0, 100, 0)
    Sleep(800)
    Sound(887, 0, 100, 0)
    Sleep(900)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0388
    ChrTalk(
        0x2A,
        "#0014F#11P#1K#4Sぷはああああああっ！\x02",
    )


    #C0389
    ChrTalk(
        0x2B,
        "#0309F#12P#1K#4Sぷはああああああっ！\x02",
    )

    OP_57(0x1)
    OP_5A()
    Sleep(500)

    #C0390
    ChrTalk(
        0x2C,
        (
            "#0113F#6Pまったく男の子ときたら……\x02\x03",

            "#0111F消耗したばかりなんだから\x01",
            "あんまりジャレ合わないの。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2D, 0x2C, 500)

    #C0391
    ChrTalk(
        0x2D,
        "#0202F#12Pエリィさん、妬いてます？\x02",
    )

    CloseMessageWindow()
    OP_63(0x2C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(800)
    TurnDirection(0x2C, 0x2D, 800)
    OP_63(0x2C, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_96(0x2C, 0x1AC2, 0x0, 0x100E, 0xBB8, 0x0)
    Sleep(500)

    #C0392
    ChrTalk(
        0x2C,
        (
            "#0112F#5Pちょ、そんなわけ\x01",
            "あるはずないでしょう！？\x02\x03",

            "それにその……\x01",
            "男の子同士になんで……\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x2D,
        (
            "#0204F#12P聞いた話だと、そういう\x01",
            "特殊な趣向#4Rジャンル#もあるそうですし……\x02\x03",

            "#0202Fこれはもうフラグが立って\x01",
            "しまったのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x2C,
        "#0112F#5Pそ、そうなの……？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x2B, 0x2C, 500)

    #C0395
    ChrTalk(
        0x2B,
        (
            "#0302F#11Pフッ、悪いなお嬢……！\x02\x03",

            "#0309Fこの世界は弱肉強食！\x01",
            "喰うか喰われるかが全てなのさ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x2C, 0x2B, 500)

    #C0396
    ChrTalk(
        0x2C,
        "#0111F#5Pあ、あなたねぇ……\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x2A,
        (
            "#0006F#11Pはあ……\x01",
            "何の話をしてるんだか。\x02",
        )
    )

    CloseMessageWindow()

    #N0398
    NpcTalk(
        0x18,
        "少年の声",
        "──フフ、賑やかだねぇ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D33C():

        label("loc_D33C")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_D33C")

    QueueWorkItem2(0x2A, 0, lambda_D33C)

    def lambda_D34E():

        label("loc_D34E")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_D34E")

    QueueWorkItem2(0x2C, 0, lambda_D34E)

    def lambda_D360():

        label("loc_D360")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_D360")

    QueueWorkItem2(0x2D, 0, lambda_D360)

    def lambda_D372():

        label("loc_D372")

        TurnDirection(0xFE, 0x18, 500)
        Yield()
        Jump("loc_D372")

    QueueWorkItem2(0x2B, 0, lambda_D372)
    Fade(500)
    SetChrPos(0x2D, 6090, 0, 3190, 230)
    OP_68(7880, 1710, 1510, 0)
    MoveCamera(127, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(18500, 0)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x22, 0x4)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x22, 0xC)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    ClearChrBattleFlags(0x22, 0x8000)
    ClearChrFlags(0x23, 0x4)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x23, 0xB)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    ClearChrBattleFlags(0x23, 0x8000)
    ClearChrFlags(0x24, 0x4)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x24, 0xC)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    ClearChrBattleFlags(0x24, 0x8000)
    ClearChrFlags(0x25, 0x4)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x25, 0xC)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    ClearChrBattleFlags(0x25, 0x8000)
    ClearChrFlags(0x1A, 0x4)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1A, 0x22)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    SetChrPos(0x18, 7000, 0, -5000, 0)
    SetChrPos(0x1A, 6200, 0, -6000, 0)
    SetChrPos(0x22, 7000, 0, -7000, 0)
    SetChrPos(0x23, 7600, 0, -6000, 0)
    SetChrPos(0x24, 6700, 0, -8350, 0)
    SetChrPos(0x25, 5200, 0, -6900, 0)

    def lambda_D4C4():
        OP_95(0xFE, 7000, 0, -180, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 3, lambda_D4C4)

    def lambda_D4DE():
        OP_95(0xFE, 6200, 0, -1180, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 3, lambda_D4DE)

    def lambda_D4F8():
        OP_95(0xFE, 7000, 0, -2180, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 3, lambda_D4F8)

    def lambda_D512():
        OP_95(0xFE, 7600, 0, -1180, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 3, lambda_D512)

    def lambda_D52C():
        OP_95(0xFE, 6700, 0, -3350, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 3, lambda_D52C)

    def lambda_D546():
        OP_95(0xFE, 5200, 0, -1900, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 3, lambda_D546)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    ClearChrFlags(0x1D, 0x4)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1D, 0xD)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)
    ClearChrFlags(0x1E, 0x4)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1E, 0x5)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    ClearChrBattleFlags(0x1E, 0x8000)
    ClearChrFlags(0x1F, 0x4)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x1F, 0xD)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    ClearChrBattleFlags(0x1F, 0x8000)
    ClearChrFlags(0x20, 0x4)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x20, 0x5)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    ClearChrBattleFlags(0x20, 0x8000)
    ClearChrFlags(0x21, 0x4)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x21, 0xD)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    ClearChrBattleFlags(0x21, 0x8000)
    SetChrPos(0x19, 9500, 0, -5300, 0)
    SetChrPos(0x1D, 8700, 0, -6300, 0)
    SetChrPos(0x1E, 10300, 0, -6300, 0)
    SetChrPos(0x1F, 10300, 0, -7900, 0)
    SetChrPos(0x20, 8700, 0, -7900, 0)
    SetChrPos(0x21, 11400, 0, -7800, 0)

    def lambda_D65C():
        OP_95(0xFE, 9500, 0, -500, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 3, lambda_D65C)

    def lambda_D676():
        OP_95(0xFE, 8700, 0, -1500, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 3, lambda_D676)

    def lambda_D690():
        OP_95(0xFE, 10300, 0, -1500, 1300, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 3, lambda_D690)

    def lambda_D6AA():
        OP_95(0xFE, 10300, 0, -3100, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 3, lambda_D6AA)

    def lambda_D6C4():
        OP_95(0xFE, 8700, 0, -3100, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 3, lambda_D6C4)

    def lambda_D6DE():
        OP_95(0xFE, 11400, 0, -3000, 1100, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 3, lambda_D6DE)
    Sleep(1500)

    #C0399
    ChrTalk(
        0x2A,
        (
            "#0000F#6Pやあ……\x01",
            "そっちはもう回復したのか？\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x18, 3)

    #C0400
    ChrTalk(
        0x18,
        (
            "#0404F#11Pふふ、まあね。\x02\x03",

            "#0402F今日のところは\x01",
            "素直に負けを認めておこうかな。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x19, 3)
    TurnDirection(0x19, 0x2B, 500)

    #C0401
    ChrTalk(
        0x19,
        (
            "#1603F#11Pケッ……ふざけた結末だぜ。\x02\x03",

            "#1601F──おい、赤毛。\x01",
            "今度はガチで勝負しろよ……？\x02\x03",

            "あの最後の爆発力……\x01",
            "てめえ、猫かぶってやがったな？\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x2B,
        (
            "#0306F#6Pあー……\x01",
            "別にそういうわけじゃねえよ。\x02\x03",

            "#0300Fあんだけ一気に力を出すと\x01",
            "その分、消耗も激しくってな。\x02\x03",

            "奥の手みたいなもんだから、\x01",
            "あんま、やりたくねーだけさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0x19,
        (
            "#1600F#11Pチッ、あの黒髪の小僧といい……\x02\x03",

            "#1604Fまあいい、さすがに今日は疲れた。\x02\x03",

            "てめぇら、引き上げるぞ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(260, 20, -1, -1)
    SetChrName("サーベルバイパーたち")

    #A0404
    AnonymousTalk(
        0xFF,
        "#4Sウーッス！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_D98F():

        label("loc_D98F")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D98F")

    QueueWorkItem2(0x1D, 2, lambda_D98F)

    def lambda_D9A1():

        label("loc_D9A1")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D9A1")

    QueueWorkItem2(0x1E, 2, lambda_D9A1)

    def lambda_D9B3():

        label("loc_D9B3")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D9B3")

    QueueWorkItem2(0x1F, 2, lambda_D9B3)

    def lambda_D9C5():

        label("loc_D9C5")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D9C5")

    QueueWorkItem2(0x20, 2, lambda_D9C5)

    def lambda_D9D7():

        label("loc_D9D7")

        TurnDirection(0xFE, 0x19, 300)
        Yield()
        Jump("loc_D9D7")

    QueueWorkItem2(0x21, 2, lambda_D9D7)
    BeginChrThread(0x19, 3, 0, 77)
    Sleep(1500)
    EndChrThread(0x1F, 0x2)
    BeginChrThread(0x1F, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x20, 0x2)
    BeginChrThread(0x20, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x1D, 0x2)
    BeginChrThread(0x1D, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x21, 0x2)
    BeginChrThread(0x21, 3, 0, 77)
    Sleep(150)
    EndChrThread(0x1E, 0x2)
    BeginChrThread(0x1E, 3, 0, 77)

    #C0405
    ChrTalk(
        0x18,
        (
            "#0402F#11Pフフ、それじゃあ\x01",
            "僕たちも失礼しようかな。\x02\x03",

            "#0409Fアディオス。\x01",
            "なかなか楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0406
    ChrTalk(
        0x1A,
        "#11P──撤収だ。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(320, 60, -1, -1)
    SetChrName("テスタメンツたち")

    #A0407
    AnonymousTalk(
        0xFF,
        "#4S了解#4Rヤー#！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x24, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x25, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x22, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x1A, 3, 0, 78)
    Sleep(150)
    BeginChrThread(0x23, 3, 0, 78)
    Sleep(500)
    BeginChrThread(0x18, 3, 0, 78)
    Sleep(1000)

    #N0408
    NpcTalk(
        0x16,
        "娘の声",
        (
            "は～……\x01",
            "《レイヴン》たちよりも\x01",
            "ずいぶん統率されてるわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2C, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2B, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    def lambda_DBC6():

        label("loc_DBC6")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_DBC6")

    QueueWorkItem2(0x2A, 0, lambda_DBC6)

    def lambda_DBD8():

        label("loc_DBD8")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_DBD8")

    QueueWorkItem2(0x2C, 0, lambda_DBD8)

    def lambda_DBEA():

        label("loc_DBEA")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_DBEA")

    QueueWorkItem2(0x2D, 0, lambda_DBEA)

    def lambda_DBFC():

        label("loc_DBFC")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_DBFC")

    QueueWorkItem2(0x2B, 0, lambda_DBFC)
    Sleep(1000)
    Fade(500)
    OP_68(3990, 1500, 2440, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrPos(0x16, 3140, 0, 1400, 225)
    SetChrPos(0x17, 1830, 0, 1460, 90)

    def lambda_DC7A():
        OP_95(0xFE, 8300, 0, 1510, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_DC7A)

    def lambda_DC94():
        OP_95(0xFE, 6790, 0, 1680, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 3, lambda_DC94)
    OP_68(7460, 1500, 2790, 2000)
    Sleep(2000)

    def lambda_DCC2():

        label("loc_DCC2")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_DCC2")

    QueueWorkItem2(0x16, 0, lambda_DCC2)

    def lambda_DCD4():

        label("loc_DCD4")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_DCD4")

    QueueWorkItem2(0x17, 0, lambda_DCD4)

    #C0409
    ChrTalk(
        0x16,
        "#0809F#12Pえへへ、お疲れさま。\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x2A,
        (
            "#0002F#5Pははっ……\x01",
            "そっちこそお疲れ。\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0x2B,
        "#0300F#5Pなんだ、もう帰んのか？\x02",
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0x17,
        (
            "#0902F#6Pはい、元々仕事で\x01",
            "来ていたこともありますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x2D,
        (
            "#0203F#5Pそれを言うなら\x01",
            "わたしたちも同じですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x2C,
        (
            "#0106F#5Pふう……\x01",
            "もう夕方になっちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0x16,
        (
            "#0809F#12Pあはは。\x01",
            "楽しかったからいいじゃない。\x02\x03",

            "#0802Fせっかくのお祭りなんだし\x01",
            "ちょっとくらいは楽しまないとね！\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0x2A,
        "#0012F#5Pげ、元気だなぁ……\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0x17,
        (
            "#0909F#6Pはは、まあそれが\x01",
            "エステルの取り柄だから。\x02\x03",

            "#0908F──でも、ランディさん。\x02\x03",

            "#0901F身体の方は大丈夫なんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0418
    ChrTalk(
        0x2A,
        "#0005F#5Pえ……\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x2B,
        (
            "#0305F#5Pへえ……\x02\x03",

            "#0300F……同じ匂いはしなかったが\x01",
            "お前もそっち絡みなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x17,
        (
            "#0903F#6Pいえ、正確には違います。\x02\x03",

            "#0901Fですが多少、知識の方は……\x02",
        )
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x2B,
        (
            "#0300F#5Pそうか……\x02\x03",

            "#0304Fま、ガキの頃から\x01",
            "慣れっこにはなってるからな。\x02\x03",

            "後に残るダメージはねぇさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0422
    ChrTalk(
        0x17,
        (
            "#0904F#6Pそうですか……\x02\x03",

            "#0900Fすみません、差し出がましい事を。\x02",
        )
    )

    CloseMessageWindow()

    #C0423
    ChrTalk(
        0x2B,
        "#0302F#5Pいや、気にすんな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0424
    ChrTalk(
        0x2A,
        "#0001F#5Pランディ……？\x02",
    )

    CloseMessageWindow()

    def lambda_E131():

        label("loc_E131")

        TurnDirection(0xFE, 0x17, 500)
        Yield()
        Jump("loc_E131")

    QueueWorkItem2(0x16, 0, lambda_E131)
    Sleep(300)

    #C0425
    ChrTalk(
        0x16,
        (
            "#0801F#11Pちょっとちょっと。\x01",
            "なに２人で分かり合ってるのよ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_E187():

        label("loc_E187")

        TurnDirection(0xFE, 0x16, 500)
        Yield()
        Jump("loc_E187")

    QueueWorkItem2(0x17, 0, lambda_E187)
    Sleep(200)

    #C0426
    ChrTalk(
        0x17,
        (
            "#0904F#6Pはは、大した話じゃないよ。\x02\x03",

            "#0900Fそれよりエステル、そろそろ帰ろう。\x01",
            "アリオスさんも帰ってくるみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x16,
        "#0805F#11Pあ、うん……\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0428
    ChrTalk(
        0x16,
        (
            "#0801F#11Pそういえば……\x01",
            "ヨシュア、例の話！\x02",
        )
    )

    CloseMessageWindow()

    #C0429
    ChrTalk(
        0x17,
        (
            "#0905F#6Pああ……そうだね。\x02\x03",

            "#0901Fせっかくだから聞いてみようか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    def lambda_E320():

        label("loc_E320")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_E320")

    QueueWorkItem2(0x17, 0, lambda_E320)

    def lambda_E332():

        label("loc_E332")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_E332")

    QueueWorkItem2(0x16, 0, lambda_E332)
    Fade(1000)
    OP_68(7700, 1730, 3080, 0)
    MoveCamera(102, 32, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    OP_68(7280, 1730, 3440, 30000)
    MoveCamera(125, 32, 0, 30000)
    OP_6E(500, 30000)
    SetCameraDistance(16000, 30000)
    Sleep(1000)

    #C0430
    ChrTalk(
        0x2A,
        "#0005F#5P例の話……？\x02",
    )

    CloseMessageWindow()

    #C0431
    ChrTalk(
        0x2B,
        "#0305F#5Pなんだ、何かあんのか？\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x16,
        (
            "#0806F#11Pうん……あのね。\x02\x03",

            "#0801F《黒の競売会#10Rシュバルツオークション#》って知ってる？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2C, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2D, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x2B, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0433
    ChrTalk(
        0x2C,
        "#0105F#6P黒の#4Rシュバルツ#……\x02",
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x2D,
        "#0205F#6P#N競売会#6Rオークション#……ですか？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0435
    ChrTalk(
        0x16,
        (
            "#0806F#11Pどうやら、このクロスベルの\x01",
            "どこかで開かれる競売会らしいの。\x02\x03",

            "何でも毎年、記念祭の期間中に\x01",
            "開かれているらしくって……\x02\x03",

            "#0801F──で、ここが肝心なんだけど\x01",
            "盗品ばかり扱ってるって話なのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0436
    ChrTalk(
        0x2C,
        "#0101F#6Pと、盗品……！？\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x2A,
        "#0013F#6P本当なのか……！？\x02",
    )

    CloseMessageWindow()

    #C0438
    ChrTalk(
        0x17,
        (
            "#0903F#11Pいや、あくまでも噂だよ。\x02\x03",

            "#0908F途方もない価値のついた\x01",
            "表に出せない由来の品ばかりが\x01",
            "出品されるという話だけど……\x02\x03",

            "#0901F──でも、その様子だと\x01",
            "聞いたことはないみたいだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x2A,
        "#0006F#6Pああ……初めて聞いたよ。\x02",
    )

    CloseMessageWindow()

    #C0440
    ChrTalk(
        0x2D,
        (
            "#0201F#6P#N……警察のデータベースでも\x01",
            "見かけたことはありませんね。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0441
    ChrTalk(
        0x2B,
        (
            "#0303F#5P《黒の競売会#10Rシュバルツオークション#》か……\x01",
            "なかなか洒落た名前だけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0x2C,
        "#0108F#6P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0443
    ChrTalk(
        0x16,
        (
            "#0806F#11Pそっか～……あなた達なら\x01",
            "何か知ってると思ったんだけど。\x02\x03",

            "#0800Fやっぱりただの噂なのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0x17,
        (
            "#0903F#11Pうーん、そうだね……\x02\x03",

            "#0908Fナイアルさんの情報ソースだから\x01",
            "確かだとは思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0445
    ChrTalk(
        0x2A,
        "#0001F#6P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0446
    ChrTalk(
        0x16,
        (
            "#0809F#11Pあはは……\x01",
            "ゴメンね、変な事を聞いちゃって。\x02\x03",

            "#0802F今日は楽しかったわ！\x01",
            "負けちゃったのは悔しいけど。\x02\x03",

            "今度は同じ事件かなんかで\x01",
            "一緒に協力できるといいわね！\x02",
        )
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x2A,
        "#0002F#6Pはは……そうだな。\x02",
    )

    CloseMessageWindow()

    #C0448
    ChrTalk(
        0x17,
        (
            "#0904F#11Pそれじゃあ、僕たちはこれで。\x02\x03",

            "#0900F皆さん、お疲れさまでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0449
    ChrTalk(
        0x2B,
        "#0302F#5Pおう、そちらもお疲れさん。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0450
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "こうして……\x01",
            "記念祭２日目は過ぎて行った。\x02\x03",

            "支援課に戻ってきたロイドたちは\x01",
            "報告書をまとめ、皆で夕食を取ってから\x01",
            "明日のため早めに休むことにした。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    ClearChrFlags(0x101, 0x80)
    ClearChrBattleFlags(0x101, 0x8000)
    ClearChrFlags(0x104, 0x80)
    ClearChrBattleFlags(0x104, 0x8000)
    ClearChrFlags(0x102, 0x80)
    ClearChrBattleFlags(0x102, 0x8000)
    ClearChrFlags(0x103, 0x80)
    ClearChrBattleFlags(0x103, 0x8000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x104, 0x4)
    Sleep(500)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(2000)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EBF0")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC2B")

    label("loc_EBF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC10")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_EC2B")

    label("loc_EC10")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EC2B")
    OP_50(0x67, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x67), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_EC2B")

    SetScenarioFlags(0x5C, 0)
    NewScene("c011C", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_80_B7E8 end

    def Function_81_EC38(): pass

    label("Function_81_EC38")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0451
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アパート『メゾン・イメルダ』\x01\x01",
            "　～　現在運営休止中　～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECED")

    #C0452
    ChrTalk(
        0x101,
        (
            "#0000F大分すすけている……\x01",
            "長い間使われてないみたいだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)

    label("loc_ECED")

    TalkEnd(0xFF)
    Return()

    # Function_81_EC38 end

    SaveToFile()

Try(main)
