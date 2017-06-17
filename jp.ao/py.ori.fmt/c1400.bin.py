from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1400.bin",                # FileName
        "c1400",                    # MapName
        "c1400",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("c1400", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 4, 0, 5],
    )

    BuildStringList((
        "c1400",                  # 0
        "ディーノ",               # 1
        "パオラ婆さん",           # 2
        "ヴァン",                 # 3
        "ルゼ",                   # 4
        "カノン",                 # 5
        "ヒューイ",               # 6
        "スラッシュ",             # 7
        "キーンツ",               # 8
        "ベッセ",                 # 9
        "アッバス",               # 10
        "シスター・リース",       # 11
        "バッカス",               # 12
        "リマ",                   # 13
        "メルスン",               # 14
        "警官",                   # 15
        "ヴァルド",               # 16
        "オリビエ",               # 17
        "ジンゴ",                 # 18
        "bc1400",                 # 19
        "中央広場",               # 20
        "西通り",                 # 21
        "行政区",                 # 22
        "住宅街",                 # 23
        "歓楽街",                 # 24
        "東通り",                 # 25
        "旧市街",                 # 26
        "港湾区",                 # 27
        "ＩＢＣ",                 # 28
        "駅前通り",               # 29
        "裏通り",                 # 30
        "ウルスラ間道",           # 31
        "東クロスベル街道",       # 32
        "西クロスベル街道",       # 33
        "マインツ山道",           # 34
        "オルキスタワー",         # 35
    ))

    ATBonus("ATBonus_6E8", 100, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_7D8", 8, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F4", 0, 0, 180)

    # monster count: 0

    # event battle count: 1

    BattleInfo(
        "BattleInfo_7F8", 0x008A, 0, 6, 0, 0, 255, 0, 0, "bc1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02102.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_7D8", "MonsterBattlePostion_7D8", "ed7452", "ed7453", "ATBonus_6E8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch06800.itc",                   # 00
        "chr/ch23302.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch24700.itc",                   # 03
        "chr/ch23800.itc",                   # 04
        "chr/ch31700.itc",                   # 05
        "chr/ch30800.itc",                   # 06
        "chr/ch31800.itc",                   # 07
        "chr/ch14000.itc",                   # 08
        "chr/ch23400.itc",                   # 09
        "chr/ch06700.itc",                   # 0A
        "chr/ch30900.itc",                   # 0B
        "chr/ch20700.itc",                   # 0C
        "chr/ch26200.itc",                   # 0D
        "chr/ch30000.itc",                   # 0E
    ))

    DeclNpc(44880,   -2500,   -20090,  225,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(15449,   100,     -19,     270,  261,  0x0, 0,   1,   0,   255, 255, 0,   8,   255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   2,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(10279,   0,       -550,    315,  261,  0x0, 0,   3,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(34080,   -6500,   -38270,  45,   261,  0x0, 0,   4,   0,   0,   1,   0,   11,  255,  0)
    DeclNpc(2369,    0,       -2210,   315,  389,  0x0, 0,   5,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(3700,    0,       -1070,   315,  389,  0x0, 0,   6,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   14,  255,  0)
    DeclNpc(11460,   0,       -6909,   135,  389,  0x0, 0,   8,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(32799,   -6500,   -36950,  315,  389,  0x0, 0,   9,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(10270,   3500,    11050,   135,  389,  0x0, 0,   12,  0,   0,   0,   0,   20,  255,  0)
    DeclNpc(9609,    3500,    13869,   135,  389,  0x0, 0,   13,  0,   0,   0,   0,   19,  255,  0)
    DeclNpc(4940,    0,       5250,    180,  389,  0x0, 0,   14,  0,   0,   0,   0,   24,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclEvent(0x0000, 0, 25,  46.5,                  -22.5,                 -3.0,                  20.25,                 [0.5,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.2222222238779068,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -23.25,                5.0,                   0.6000000238418579,    1.0])
    DeclEvent(0x0040, 0, 27,  1.6399999856948853,    0.0,                   -1.0,                  4.0,                   [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.4099999964237213,   -0.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 33,  1.899999976158142,     10.0,                  -1.0,                  100.0,                 [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -0.37999996542930603,  -2.5,                  0.19999998807907104,   1.0])
    DeclEvent(0x0000, 0, 44,  10.039999961853027,    -37.459999084472656,   -6.409999847412109,    400.0,                 [0.19999998807907104,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.19999998807907104,   0.0,                   -2.007999897003174,    4.682499885559082,     1.281999945640564,     1.0])

    DeclActor(47720,   -1100,   -33160,  1200,    47720,   100,     -33160,  0x007C, 0,  6,  0x0000)
    DeclActor(34830,   2450,    -19780,  1500,    34830,   3950,    -19780,  0x007C, 0,  53, 0x0000)

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
    PlaceName(-88.0, 0.0, 360.0, 0x0000, 0x0000, "オルキスタワー")
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

    ChipFrameInfo(2324, 0)                                       # 0

    ScpFunction((
        "Function_0_914",          # 00, 0
        "Function_1_9C4",          # 01, 1
        "Function_2_9EF",          # 02, 2
        "Function_3_AC8",          # 03, 3
        "Function_4_B11",          # 04, 4
        "Function_5_1105",         # 05, 5
        "Function_6_134B",         # 06, 6
        "Function_7_149C",         # 07, 7
        "Function_8_1AAD",         # 08, 8
        "Function_9_2131",         # 09, 9
        "Function_10_2654",        # 0A, 10
        "Function_11_29FE",        # 0B, 11
        "Function_12_33F7",        # 0C, 12
        "Function_13_3468",        # 0D, 13
        "Function_14_3511",        # 0E, 14
        "Function_15_3518",        # 0F, 15
        "Function_16_3522",        # 10, 16
        "Function_17_3A2E",        # 11, 17
        "Function_18_3B26",        # 12, 18
        "Function_19_3C60",        # 13, 19
        "Function_20_3D23",        # 14, 20
        "Function_21_3DE5",        # 15, 21
        "Function_22_3E22",        # 16, 22
        "Function_23_3E68",        # 17, 23
        "Function_24_3F0A",        # 18, 24
        "Function_25_3F5E",        # 19, 25
        "Function_26_4842",        # 1A, 26
        "Function_27_4913",        # 1B, 27
        "Function_28_4914",        # 1C, 28
        "Function_29_4DDA",        # 1D, 29
        "Function_30_4E4D",        # 1E, 30
        "Function_31_4EC0",        # 1F, 31
        "Function_32_4F33",        # 20, 32
        "Function_33_4FA6",        # 21, 33
        "Function_34_63F7",        # 22, 34
        "Function_35_6AD1",        # 23, 35
        "Function_36_6B6E",        # 24, 36
        "Function_37_6BAF",        # 25, 37
        "Function_38_7474",        # 26, 38
        "Function_39_74E0",        # 27, 39
        "Function_40_754C",        # 28, 40
        "Function_41_75B8",        # 29, 41
        "Function_42_75F5",        # 2A, 42
        "Function_43_7632",        # 2B, 43
        "Function_44_766F",        # 2C, 44
        "Function_45_7B82",        # 2D, 45
        "Function_46_8D16",        # 2E, 46
        "Function_47_9EB7",        # 2F, 47
        "Function_48_A5EE",        # 30, 48
        "Function_49_AE11",        # 31, 49
        "Function_50_B2F5",        # 32, 50
        "Function_51_DCEF",        # 33, 51
        "Function_52_DD3F",        # 34, 52
        "Function_53_DD7E",        # 35, 53
    ))


    def Function_0_914(): pass

    label("Function_0_914")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_94C"),
        (1, "loc_958"),
        (2, "loc_964"),
        (3, "loc_970"),
        (4, "loc_97C"),
        (5, "loc_988"),
        (6, "loc_994"),
        (SWITCH_DEFAULT, "loc_9A0"),
    )


    label("loc_94C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_958")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_964")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_970")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_97C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_988")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_994")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_9A0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_9AC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9C3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9AC")

    label("loc_9C3")

    Return()

    # Function_0_914 end

    def Function_1_9C4(): pass

    label("Function_1_9C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9EE")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_1_9C4")

    label("loc_9EE")

    Return()

    # Function_1_9C4 end

    def Function_2_9EF(): pass

    label("Function_2_9EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC7")
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
    Jump("Function_2_9EF")

    label("loc_AC7")

    Return()

    # Function_2_9EF end

    def Function_3_AC8(): pass

    label("Function_3_AC8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B10")
    Sleep(4000)
    OP_95(0xFE, -6960, -3800, -27910, 1000, 0x0)
    Sleep(4000)
    OP_95(0xFE, -13650, -3010, -25240, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x12C)
    Sleep(1900)
    Jump("Function_3_AC8")

    label("loc_B10")

    Return()

    # Function_3_AC8 end

    def Function_4_B11(): pass

    label("Function_4_B11")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEE")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B98")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_BB7")

    label("loc_B98")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BB7")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_BB7")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BEE")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x1)
    SetChrSubChip(0x9, 0x0)
    EndChrThread(0x9, 0x0)
    SetChrBattleFlags(0x9, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_C4F")
    SetChrPos(0xC, 8290, 0, -1190, 45)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrPos(0xA, 9640, 0, 850, 180)
    SetChrPos(0xB, 10280, 0, -550, 315)
    Jump("loc_FE5")

    label("loc_C4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_D83")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD4")
    SetChrPos(0xF, -200, 0, -8460, 180)
    SetChrPos(0x10, 30390, -2500, -21970, 0)
    SetChrPos(0x15, 6500, 0, 5410, 0)
    SetChrPos(0x14, 5490, 0, 5600, 0)
    Jump("loc_D2E")

    label("loc_CD4")

    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 2520, -10, -4059, 225)
    SetChrPos(0xF, 2120, -10, -6060, 315)
    SetChrPos(0x10, 310, -10, -4250, 90)
    SetChrPos(0x15, 6500, 0, 5410, 0)
    SetChrPos(0x14, 5490, 0, 5600, 0)

    label("loc_D2E")

    SetChrFlags(0x9, 0x80)
    SetChrPos(0xA, 34490, -6500, -37750, 315)
    SetChrPos(0xB, 34490, -6500, -38950, 315)
    SetChrPos(0xC, 34840, -2220, -19610, 0)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7E")
    SetChrFlags(0xC, 0x10)

    label("loc_D7E")

    Jump("loc_FE5")

    label("loc_D83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_D96")
    SetChrFlags(0x8, 0x80)
    Jump("loc_FE5")

    label("loc_D96")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_DEB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_FE5")

    label("loc_DEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E08")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_FE5")

    label("loc_E08")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E25")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_FE5")

    label("loc_E25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E38")
    SetChrFlags(0x8, 0x80)
    Jump("loc_FE5")

    label("loc_E38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E83")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_FE5")

    label("loc_E83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EBE")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EB9")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x10)
    SetChrFlags(0xE, 0x10)

    label("loc_EB9")

    Jump("loc_FE5")

    label("loc_EBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_F34")
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 11460, 0, -6910, 270)
    SetChrPos(0xA, 9710, 0, -5240, 135)
    SetChrPos(0xB, 9190, 0, -6190, 90)
    SetChrPos(0xC, 8940, 0, -7660, 45)
    BeginChrThread(0xC, 0, 0, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0xC, 0x10)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0x16, 0x80)
    Jump("loc_FE5")

    label("loc_F34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_F7D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, 14710, 0, -5170, 180)
    SetChrPos(0xB, 14710, 0, -6450, 0)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_FE5")

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_FBC")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, 14710, 0, -5170, 270)
    SetChrPos(0xB, 14710, 0, -6450, 270)
    Jump("loc_FE5")

    label("loc_FBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_FE5")
    SetChrPos(0x8, 47930, -2100, -22760, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE5")
    SetChrFlags(0xC, 0x10)

    label("loc_FE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_FF9")
    ClearScenarioFlags(0x22, 0)
    Event(0, 28)
    Jump("loc_1036")

    label("loc_FF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1010")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x1, 2)
    Event(0, 34)
    Jump("loc_1036")

    label("loc_1010")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_1027")
    ClearScenarioFlags(0x22, 2)
    SetScenarioFlags(0x1, 3)
    Event(0, 37)
    Jump("loc_1036")

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_1036")
    ClearScenarioFlags(0x22, 3)
    Event(0, 47)

    label("loc_1036")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1061")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1061")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_109E")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108D")
    Event(0, 45)
    Jump("loc_109E")

    label("loc_108D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_109E")
    Event(0, 46)

    label("loc_109E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_10D4")
    SetMapFlags(0x10000000)
    Event(0, 49)

    label("loc_10D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1104")
    SetMapFlags(0x10000000)
    SetScenarioFlags(0x1, 4)
    Event(0, 50)

    label("loc_1104")

    Return()

    # Function_4_B11 end

    def Function_5_1105(): pass

    label("Function_5_1105")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_111F")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 2)
    Jump("loc_114E")

    label("loc_111F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_END)), "loc_1139")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 3)
    Jump("loc_114E")

    label("loc_1139")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_END)), "loc_114E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 4)

    label("loc_114E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_11EF")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sentaku", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_11EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x133, 1)), scpexpr(EXPR_END)), "loc_1207")
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x1, 0x1)
    Jump("loc_120D")

    label("loc_1207")

    ClearMapObjFlags(0x1, 0x10)

    label("loc_120D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1220")
    OP_70(0x7, 0x0)
    Jump("loc_1224")

    label("loc_1220")

    OP_70(0x7, 0x1E)

    label("loc_1224")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    ModifyEventFlags(0, 3, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1246")
    Jump("loc_1298")

    label("loc_1246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1254")
    Jump("loc_1298")

    label("loc_1254")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_1267")
    ModifyEventFlags(1, 0, 0x80)
    Jump("loc_1298")

    label("loc_1267")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_127A")
    ModifyEventFlags(1, 0, 0x80)
    Jump("loc_1298")

    label("loc_127A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1298")
    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x138, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1298")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12AB")
    ModifyEventFlags(1, 2, 0x80)

    label("loc_12AB")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 11000, -6500, -34510, 4000, 2000, 7000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_131C")
    SetBarrier(0x2, 0x0, 0x1)
    SetMapObjFrame(0xFF, "kusari", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kakusi01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kakusi02", 0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1317")
    ModifyEventFlags(1, 3, 0x80)

    label("loc_1317")

    Jump("loc_134A")

    label("loc_131C")

    SetMapObjFrame(0xFF, "kusari", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kakusi01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kakusi02", 0x0, 0x1)

    label("loc_134A")

    Return()

    # Function_5_1105 end

    def Function_6_134B(): pass

    label("Function_6_134B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144B")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_13D4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1446")

    label("loc_13D4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1446")

    Jump("loc_1490")

    label("loc_144B")

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

    label("loc_1490")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_134B end

    def Function_7_149C(): pass

    label("Function_7_149C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14BC")
    Call(0, 48)
    Return()

    label("loc_14BC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_16F0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1675")

    #C0004
    ChrTalk(
        0xFE,
        "あ、特務支援課……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00108Fディーノ君……\x01",
            "えっと、他のメンバーはその……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "ん、ああ……おかげ様で\x01",
            "一番重症だったコウキ先輩も\x01",
            "何とか意識を取り戻してさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "他の先輩方も、何人かは退院して\x01",
            "旧市街の方に戻って来ているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "まあ流石に、すぐにチームへ\x01",
            "復帰ってのは難しいと思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "でも、ここで待っていれば、\x01",
            "必ず顔を出してくれるはずだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        "#00108Fディーノ君……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#00003Fそうか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_16EB")

    label("loc_1675")


    #C0012
    ChrTalk(
        0xFE,
        (
            "それにしても……\x01",
            "朝から街の方が騒がしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "独立がどうのとかって聞いたけど、\x01",
            "もっと静かにやって欲しいよな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EB")

    Jump("loc_1AA9")

    label("loc_16F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_16FE")
    Jump("loc_1AA9")

    label("loc_16FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_170C")
    Jump("loc_1AA9")

    label("loc_170C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_171A")
    Jump("loc_1AA9")

    label("loc_171A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1728")
    Jump("loc_1AA9")

    label("loc_1728")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1736")
    Jump("loc_1AA9")

    label("loc_1736")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1744")
    Jump("loc_1AA9")

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1752")
    Jump("loc_1AA9")

    label("loc_1752")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1760")
    Jump("loc_1AA9")

    label("loc_1760")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1A2A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19B6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1951")

    #C0014
    ChrTalk(
        0xFE,
        "あ、特務支援課……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "な、なあ、ワジ。\x01",
            "何でもヴァルドさん相手に\x01",
            "タイマン張ったって話だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        (
            "#10303F……質問があれば答えるけど。\x01",
            "僕の口からそれを聞きたいかい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xFE)

    #C0017
    ChrTalk(
        0xFE,
        "い、いや、何でもない……！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "ヴァ、ヴァルドさんは最強なんだ。\x01",
            "俺は絶対に信じないからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#00303F（へっ、ヴァルドの野郎、\x01",
            "  心底好かれてやがんのな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00003F（ああ、彼にとっては\x01",
            "  ヒーローみたいなものなんだろうな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 6)
    Jump("loc_19B1")

    label("loc_1951")


    #C0021
    ChrTalk(
        0xFE,
        (
            "……いつだって\x01",
            "ヴァルドさんは最強なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "そ、そうだ、俺が\x01",
            "信じないでどうするんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19B1")

    Jump("loc_1A25")

    label("loc_19B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19C5")
    Jump("loc_1A25")

    label("loc_19C5")


    #C0023
    ChrTalk(
        0xFE,
        (
            "……もう、\x01",
            "モンシンヒョウは\x01",
            "渡しただろ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "それ持って\x01",
            "さっさとどっかに\x01",
            "行っちゃえよ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A25")

    Jump("loc_1AA9")

    label("loc_1A2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1A38")
    Jump("loc_1AA9")

    label("loc_1A38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1AA9")

    #C0025
    ChrTalk(
        0xFE,
        (
            "……分かったら\x01",
            "さっさと行っちまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "ヴァルドさんに見つかったら、\x01",
            "どうなっても知らないからな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AA9")

    TalkEnd(0xFE)
    Return()

    # Function_7_149C end

    def Function_8_1AAD(): pass

    label("Function_8_1AAD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B3B")

    #C0027
    ChrTalk(
        0xFE,
        (
            "よく分からないけど、\x01",
            "大変な事態になっている\x01",
            "みたいですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "しばらく家からは出ない方が\x01",
            "よいのかもしれませんねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1B3B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1B49")
    Jump("loc_212D")

    label("loc_1B49")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1BD6")

    #C0029
    ChrTalk(
        0xFE,
        (
            "マインツの町の方で、\x01",
            "大変な騒ぎが起こっている\x01",
            "そうですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "怪我人も出ていると言いますが……\x01",
            "本当に悲しいことです。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1BD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1BE4")
    Jump("loc_212D")

    label("loc_1BE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1C62")

    #C0031
    ChrTalk(
        0xFE,
        (
            "そういえば、今日はいつもの\x01",
            "子供たちの姿を見かけませんねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "ふふ、どこかへ\x01",
            "遊びに行ったのでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1C62")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1CFE")

    #C0033
    ChrTalk(
        0xFE,
        (
            "何でも近々、独立の是非について\x01",
            "住民投票が行われるらしいですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "わたしにはよく分からないけど、\x01",
            "ちゃんと考えないといけませんねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1E2F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DBC")

    #C0035
    ChrTalk(
        0xFE,
        (
            "最近、世間を騒がせる\x01",
            "大きなニュースが多いですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "わたしには分からないことも\x01",
            "多いのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "とにかくみんなの笑顔を\x01",
            "絶やしたくないものですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E2A")

    label("loc_1DBC")


    #C0038
    ChrTalk(
        0xFE,
        (
            "わたしには難しい話は\x01",
            "よく分からないのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "とにかくみんなの笑顔を\x01",
            "絶やしたくないものですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E2A")

    Jump("loc_212D")

    label("loc_1E2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1E94")

    #C0040
    ChrTalk(
        0xFE,
        "ふふ、今日も良い日和ですねぇ。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "子供たちも元気だし、\x01",
            "ほのぼのと幸せですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_212D")

    label("loc_1E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1FC5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F29")

    #C0042
    ChrTalk(
        0xFE,
        (
            "新しい市役所のビルは\x01",
            "クロスベル市のどこからでも\x01",
            "見えるみたいですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "ふふ、近くで見たら\x01",
            "どれだけ立派なのかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FC0")

    label("loc_1F29")


    #C0044
    ChrTalk(
        0xFE,
        (
            "さっきいた白いコートを着た人は\x01",
            "旅の音楽家さんなんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "わたしは耳が遠くて\x01",
            "よくは聴こえませんでしたが、\x01",
            "ふふ、心地良い調べでしたねぇ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC0")

    Jump("loc_212D")

    label("loc_1FC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_20C3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2046")

    #C0046
    ChrTalk(
        0xFE,
        (
            "あのシスターさん、\x01",
            "あまり見ない顔だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "ふふ、子供たちと\x01",
            "仲良くなるのがお上手なのねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_20BE")

    label("loc_2046")


    #C0048
    ChrTalk(
        0xFE,
        (
            "あのシスターさん、子供たちと\x01",
            "仲良くなるのがお上手なのねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "ふふ、見ているだけで\x01",
            "何だか気持ちが暖かくなるわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20BE")

    Jump("loc_212D")

    label("loc_20C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_20D1")
    Jump("loc_212D")

    label("loc_20D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_212D")

    #C0050
    ChrTalk(
        0xFE,
        (
            "ふふ、今日もポカポカして\x01",
            "いい天気ですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "つい、ウトウトしてしまうわ。\x02",
    )

    CloseMessageWindow()

    label("loc_212D")

    TalkEnd(0xFE)
    Return()

    # Function_8_1AAD end

    def Function_9_2131(): pass

    label("Function_9_2131")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_21AA")

    #C0052
    ChrTalk(
        0xFE,
        (
            "へへっ、何だか街の方が\x01",
            "スゲエ騒ぎになってんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "誰かが戦争になるかも\x01",
            "しれねえって言ってたぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_21AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_227B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_220A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21D2")
    Call(0, 18)
    Jump("loc_2205")

    label("loc_21D2")


    #C0054
    ChrTalk(
        0xFE,
        (
            "キャハハ、オヤジのやろー、\x01",
            "まるで真人間だな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2205")

    Jump("loc_2276")

    label("loc_220A")


    #C0055
    ChrTalk(
        0xFE,
        (
            "へへっ、今日の炊き出しも\x01",
            "うまかったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "あんなのが毎日食えんなら、\x01",
            "ずっとフッコーしててもいいぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2276")

    Jump("loc_2650")

    label("loc_227B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_22F1")

    #C0057
    ChrTalk(
        0xFE,
        (
            "何か今日は、オトナたちが\x01",
            "ザワザワしてやがんな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "ヒヒ、ウチのオヤジは\x01",
            "相変わらずだけどな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_22F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2329")

    #C0059
    ChrTalk(
        0xFE,
        "キャハハ、天然のシャワーだシャワー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_2329")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2337")
    Jump("loc_2650")

    label("loc_2337")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2345")
    Jump("loc_2650")

    label("loc_2345")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_23B5")

    #C0060
    ChrTalk(
        0xFE,
        (
            "ひゃっほ～！\x01",
            "りんじしゅーにゅー、ゲットだぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "ニシシ……ルゼ、\x01",
            "今日はニク食うぞ、ニク。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_23B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2441")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23FD")

    #C0062
    ChrTalk(
        0xFE,
        (
            "そらそらぁ～、\x01",
            "ヴァン様のお通りで～い！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_243C")

    label("loc_23FD")


    #C0063
    ChrTalk(
        0xFE,
        (
            "キャハハ、オヤジのやろー、\x01",
            "今頃あれを飲んだトコかもな～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_243C")

    Jump("loc_2650")

    label("loc_2441")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_244F")
    Jump("loc_2650")

    label("loc_244F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2460")
    Call(0, 16)
    Jump("loc_2650")

    label("loc_2460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_24BF")

    #C0064
    ChrTalk(
        0xFE,
        (
            "くは～！　にしても\x01",
            "スゲエ迫力だったよな～！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "思わずアセかいちまったぜ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_24BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_252C")

    #C0066
    ChrTalk(
        0xFE,
        "雨、シトシト降ってんなー。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "これ全部ジュースだったら\x01",
            "ちっとはハラふくれんだけどな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2650")

    label("loc_252C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2650")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25D8")

    #C0068
    ChrTalk(
        0xFE,
        (
            "お、確かオメーら\x01",
            "ケーサツのヤツらだな。\x01",
            "それに不良の兄ちゃんまで。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "なんか事件でも……\x01",
            "って、ん？　違うのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "ちぇ、つまんねーの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2650")

    label("loc_25D8")


    #C0071
    ChrTalk(
        0xFE,
        (
            "最近、不良チームの兄ちゃんたち、\x01",
            "あんま騒がなくなったんだよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "キャハハ、気合い\x01",
            "入ってねぇんじゃねえの～？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2650")

    TalkEnd(0xFE)
    Return()

    # Function_9_2131 end

    def Function_10_2654(): pass

    label("Function_10_2654")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2694")

    #C0073
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "それってヤベーんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_2694")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_273B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26EF")

    #C0074
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "ヴァンのお父さんって\x01",
            "意外と頼りになるんだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2736")

    label("loc_26EF")


    #C0075
    ChrTalk(
        0xFE,
        (
            "炊き出しは、\x01",
            "夕方にもう一回あるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "次は何食えんのかな？\x02",
    )

    CloseMessageWindow()

    label("loc_2736")

    Jump("loc_29FA")

    label("loc_273B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_278E")

    #C0077
    ChrTalk(
        0xFE,
        (
            "マインツって場所が\x01",
            "何かヤベーらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        "どうヤベーんだろ？\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_278E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_27D5")

    #C0079
    ChrTalk(
        0xFE,
        (
            "クスクス……どっかで\x01",
            "セッケンかっぱらってこよっか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_27D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_27E3")
    Jump("loc_29FA")

    label("loc_27E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27F1")
    Jump("loc_29FA")

    label("loc_27F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2829")

    #C0080
    ChrTalk(
        0xFE,
        "キャハハ、今日は腹イッパイ食えるね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_2829")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_28AD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_286C")

    #C0081
    ChrTalk(
        0xFE,
        "キャハハッ、ルゼ様もお通りで～い！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_28A8")

    label("loc_286C")


    #C0082
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "ヴァンのお父さん、\x01",
            "モンゼツしてるかもね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28A8")

    Jump("loc_29FA")

    label("loc_28AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_28BB")
    Jump("loc_29FA")

    label("loc_28BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_28CC")
    Call(0, 16)
    Jump("loc_29FA")

    label("loc_28CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_293F")

    #C0083
    ChrTalk(
        0xFE,
        (
            "ああいうのを、\x01",
            "タイマンしょーぶって\x01",
            "言うんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "確かにスゲエ迫力だったね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_293F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_29B5")

    #C0085
    ChrTalk(
        0xFE,
        (
            "でもそれだと、おなか\x01",
            "たぷんたぷんになっちゃいそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "ヴァンのお父さんみたいに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_29FA")

    label("loc_29B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_29FA")

    #C0087
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "ヴァンったら本当に\x01",
            "騒ぎが好きなんだから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_29FA")

    TalkEnd(0xFE)
    Return()

    # Function_10_2654 end

    def Function_11_29FE(): pass

    label("Function_11_29FE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2A46")

    #C0088
    ChrTalk(
        0xFE,
        (
            "せ、戦争だなんて……\x01",
            "そんなのゼッタイにダメだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_2A46")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2BAA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_2ABF")

    #C0089
    ChrTalk(
        0xFE,
        (
            "ガサゴソ……\x01",
            "えっと、これは……ダメか。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "それじゃこっちは……\x01",
            "う～ん、これもハズレだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_2ABF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B31")

    #C0091
    ChrTalk(
        0xFE,
        "お兄ちゃんたち、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "もらった廃材は\x01",
            "僕が責任を持って\x01",
            "換金させてもらうからね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2BA5")

    label("loc_2B31")


    #C0093
    ChrTalk(
        0xFE,
        (
            "さてと、お腹も\x01",
            "一杯になったことだし、\x01",
            "また頑張るぞ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "お兄ちゃんたち、\x01",
            "色々手伝ってくれて\x01",
            "ありがとうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BA5")

    Jump("loc_33F3")

    label("loc_2BAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2CDD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C49")

    #C0095
    ChrTalk(
        0xFE,
        (
            "う～ん、昨日の雨のせいで\x01",
            "石畳の隙間が少しぬかるんでるね。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "それに隙間にゴミが沢山……\x01",
            "ふふ、こんな時こそアレの出番だよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2CD8")

    label("loc_2C49")


    #C0097
    ChrTalk(
        0xFE,
        (
            "じゃ～ん、これが僕の秘密兵器\x01",
            "“手ごろな木の棒”さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "うんしょ……これをこうして\x01",
            "隙間に溜まったゴミを掻き出すんだ。\x01",
            "けっこう楽しいよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2CD8")

    Jump("loc_33F3")

    label("loc_2CDD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2CEB")
    Jump("loc_33F3")

    label("loc_2CEB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2D7A")

    #C0099
    ChrTalk(
        0xFE,
        (
            "さっさっ、さっさっ……\x01",
            "どう、今日もこの辺りは\x01",
            "ピカピカだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "ふふ、お掃除に終わりはないけど、\x01",
            "この達成感は最高だよね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_2D7A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2DEF")

    #C0101
    ChrTalk(
        0xFE,
        (
            "最近、この辺りで喧嘩してる人を\x01",
            "あまり見かけなくなったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "ふふっ、とっても良いことだよね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_2DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2F30")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2EB3")

    #C0103
    ChrTalk(
        0xFE,
        (
            "先週だったかな、不良の\x01",
            "お兄さんが耳元に何かを当てて\x01",
            "ブツブツ喋ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "アレって一体、何だったんだろうね？\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#00005F（もしかしてエニグマのことか……？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2F2B")

    label("loc_2EB3")


    #C0106
    ChrTalk(
        0xFE,
        (
            "先週だったかな、不良の\x01",
            "お兄さんが耳元に何かを当てて\x01",
            "ブツブツ喋ってたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "アレって一体、何だったんだろうね？\x02",
    )

    CloseMessageWindow()

    label("loc_2F2B")

    Jump("loc_33F3")

    label("loc_2F30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2FB6")

    #C0108
    ChrTalk(
        0xFE,
        (
            "オルキスタワーって、\x01",
            "すごく背が高いらしいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "２５０アージュって聞いたけど……\x01",
            "僕の身長の何倍くらいだろう？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_33F3")

    label("loc_2FB6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3144")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30B1")

    #C0110
    ChrTalk(
        0xFE,
        (
            "何でも今日は、外国から\x01",
            "記者さんやえらい人たちが\x01",
            "いっぱい来てるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "誰かがこんな場所には\x01",
            "来ないって言ってたけど、\x01",
            "そんな事は分からないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "さっさっ、さっさっ……\x01",
            "いつもより余計に\x01",
            "綺麗にしておかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_313F")

    label("loc_30B1")


    #C0113
    ChrTalk(
        0xFE,
        (
            "何でも今日は、外国から\x01",
            "すごくエライ人たちが\x01",
            "いっぱい来てるらしいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "さっさっ、さっさっ……\x01",
            "いつもより余計に\x01",
            "綺麗にしておかないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_313F")

    Jump("loc_33F3")

    label("loc_3144")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3155")
    Call(0, 16)
    Jump("loc_33F3")

    label("loc_3155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3163")
    Jump("loc_33F3")

    label("loc_3163")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_33F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3375")

    #C0115
    ChrTalk(
        0xFE,
        "せっせ、せっせ……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "ふう、相変わらず\x01",
            "いくらお掃除しても\x01",
            "ゴミはなくならないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x105,
        (
            "#10300Fおはよう、カノン。\x01",
            "今日の調子はどうだい？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    #C0118
    ChrTalk(
        0xFE,
        "あ、ワジさん、おはよう。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "う～んとね、今日は\x01",
            "ビンのゴミが多いかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "マナー違反は許せないけど、\x01",
            "色んな形があって面白いよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "ほら、これなんか\x01",
            "真ん中がキュッとくびれていて\x01",
            "キレイでしょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x105,
        (
            "#10304Fふふ、確かに綺麗な形だね。\x02\x03",

            "#10300Fとりあえずカノン、\x01",
            "破片なんかには気を付けなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "うん、ありがとう。\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x137, 3)
    Jump("loc_33F3")

    label("loc_3375")


    #C0124
    ChrTalk(
        0xFE,
        (
            "ビンはね、色んな形があって\x01",
            "眺めていると面白いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "ほら、コレなんかボコボコしてて\x01",
            "光に当てるとキラキラ光るんだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33F3")

    TalkEnd(0xFE)
    Return()

    # Function_11_29FE end

    def Function_12_33F7(): pass

    label("Function_12_33F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3464")

    #C0126
    ChrTalk(
        0xFE,
        (
            "ふう、やはり\x01",
            "現場作業は体力を使うな。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "でもまあ、これも\x01",
            "良いトレーニングだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3464")

    label("loc_3464")

    TalkEnd(0xFE)
    Return()

    # Function_12_33F7 end

    def Function_13_3468(): pass

    label("Function_13_3468")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_350D")

    #C0128
    ChrTalk(
        0x10,
        (
            "そ、それにしても……\x01",
            "このアパートの\x01",
            "破壊ぶりは、す、凄まじいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x10,
        (
            "廃アパートで良かったが、\x01",
            "な、中に人がいたらと思うと、\x01",
            "ぞっとするぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_350D")

    label("loc_350D")

    TalkEnd(0xFE)
    Return()

    # Function_13_3468 end

    def Function_14_3511(): pass

    label("Function_14_3511")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_3511 end

    def Function_15_3518(): pass

    label("Function_15_3518")

    TalkBegin(0xFE)
    Call(0, 16)
    TalkEnd(0xFE)
    Return()

    # Function_15_3518 end

    def Function_16_3522(): pass

    label("Function_16_3522")

    OP_4B(0x12, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_375E")

    #C0130
    ChrTalk(
        0x12,
        (
            "#04403F『そうだ、アナの所に行ってみよう。』\x02\x03",

            "魔女である彼女なら、きっとロンのいる\x01",
            "場所をさがしてくれるはずです。\x02\x03",

            "来た道を辿ってアナの小屋に向かいます。\x01",
            "ふと、走るマルクの耳に、\x01",
            "けたたましい獣の声が聞こえてきました。\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    Sleep(300)

    #C0131
    ChrTalk(
        0xC,
        "わくわく……それでそれで……？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "つーか、早く昼メシにしようぜ。\x01",
            "パン持ってきてくれたんだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "こっそりもらって食べちゃおうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#00105F（リースさん……\x01",
            "  今日は日曜学校の出張に\x01",
            "  来ているみたいね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00000F（童話を読み聞かせているのか……\x01",
            "  なんていうか暖かい光景だな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 7)
    Jump("loc_3A1D")

    label("loc_375E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3961")

    #C0136
    ChrTalk(
        0x12,
        (
            "#04403F恐る恐る声のした方に近づくと、\x01",
            "そこには……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        "うんうん……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "ちぇっ、かったりーなあ。\x01",
            "ルゼ、パンがもらえるまで寝ちまうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        "クスクス……そうすっか。\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x12)

    #C0140
    ChrTalk(
        0x12,
        (
            "#04400F言い忘れていましたが、\x01",
            "今日の授業の最後に\x01",
            "本の感想文を書いていただきます。\x02\x03",

            "#04400F何も書けなかった場合は\x01",
            "授業不参加とみなし、\x01",
            "昼食は抜きとしますからそのつもりで。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0xA)

    #C0141
    ChrTalk(
        0xA,
        (
            "ゲゲッ、マジかよ！？\x01",
            "そんなの横暴だろー！\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "今日のシスターはなかなかキビしいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_3A1D")

    label("loc_3961")


    #C0143
    ChrTalk(
        0x12,
        (
            "#04403F恐る恐る声のした方に近づくと、\x01",
            "そこには……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "わー待て待て、最初から！\x01",
            "最初から読んでくれよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "いまごろアセッてきたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        "ふふ、みんな仲良しで楽しいな。\x02",
    )

    CloseMessageWindow()

    label("loc_3A1D")

    OP_4C(0x12, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_16_3522 end

    def Function_17_3A2E(): pass

    label("Function_17_3A2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3ACD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A50")
    Call(0, 18)
    Jump("loc_3AC8")

    label("loc_3A50")


    #C0147
    ChrTalk(
        0xFE,
        (
            "ったく、炊き出しがあるとは言え、\x01",
            "まっ昼間からタダ働きとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "さっさと終わらせて、\x01",
            "早く一杯やりてえモンだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC8")

    Jump("loc_3B22")

    label("loc_3ACD")


    #C0149
    ChrTalk(
        0xFE,
        (
            "しっかし、太陽ってヤツは\x01",
            "どんだけ眩しいんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "夜型人間には毒だぜ、こりゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_3B22")

    TalkEnd(0xFE)
    Return()

    # Function_17_3A2E end

    def Function_18_3B26(): pass

    label("Function_18_3B26")

    OP_4B(0xA, 0xFF)
    OP_4B(0x13, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    #C0151
    ChrTalk(
        0xA,
        (
            "キャハハ、オヤジのやろー、\x01",
            "珍しく昼間から仕事してやがる。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "何でもフッコーを手伝わねえと、\x01",
            "アパートから追い出すって\x01",
            "大家に言われたらしいぜ～？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x13, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x13, 0xA, 0)

    #C0153
    ChrTalk(
        0x13,
        (
            "おらぁ、ヴァン。\x01",
            "余計なこと喋ってんじゃねえぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x13,
        "黙って仕事を手伝いやがれ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 5)
    OP_93(0xA, 0x13B, 0x0)
    OP_93(0x13, 0x13B, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_18_3B26 end

    def Function_19_3C60(): pass

    label("Function_19_3C60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3CC2")

    #C0155
    ChrTalk(
        0xFE,
        (
            "さてと、今日も\x01",
            "ちゃっちゃと片付けるか。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "まずは寸法を測って、と……\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D1F")

    label("loc_3CC2")


    #C0157
    ChrTalk(
        0xFE,
        (
            "ふう、一足遅くなっちゃったけど\x01",
            "やっと一息付けたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        "よしと……午後からも頑張るぞ！\x02",
    )

    CloseMessageWindow()

    label("loc_3D1F")

    TalkEnd(0xFE)
    Return()

    # Function_19_3C60 end

    def Function_20_3D23(): pass

    label("Function_20_3D23")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D80")

    #C0159
    ChrTalk(
        0xFE,
        "パパ、みんなのためにお仕事してるの。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "とっても、かっこいいの♪\x02",
    )

    CloseMessageWindow()
    Jump("loc_3DE1")

    label("loc_3D80")

    SetChrName("リマ")

    #C0161
    ChrTalk(
        0x14,
        "パパ、このお汁おいしーねー。\x02",
    )

    CloseMessageWindow()
    SetChrName("メルスン")

    #C0162
    ChrTalk(
        0x15,
        (
            "ああ、本当だね。\x01",
            "パパも力が湧いてくるよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DE1")

    TalkEnd(0xFE)
    Return()

    # Function_20_3D23 end

    def Function_21_3DE5(): pass

    label("Function_21_3DE5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DFA")
    Call(0, 23)
    Jump("loc_3E1E")

    label("loc_3DFA")


    #C0163
    ChrTalk(
        0xFE,
        "なんつうか、とんでもねえな……\x02",
    )

    CloseMessageWindow()

    label("loc_3E1E")

    TalkEnd(0xFE)
    Return()

    # Function_21_3DE5 end

    def Function_22_3E22(): pass

    label("Function_22_3E22")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E37")
    Call(0, 23)
    Jump("loc_3E64")

    label("loc_3E37")


    #C0164
    ChrTalk(
        0xFE,
        (
            "ヴァルドさんも\x01",
            "見に来りゃいいのにな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3E64")

    TalkEnd(0xFE)
    Return()

    # Function_22_3E22 end

    def Function_23_3E68(): pass

    label("Function_23_3E68")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0165
    ChrTalk(
        0xD,
        "オルキスタワーっつったっけ？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xD,
        (
            "まったく、\x01",
            "とんでもねえモンを造りやがるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        (
            "ヒャハッ、確かにな。\x01",
            "屋上からバンジーしてみてえぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_3E68 end

    def Function_24_3F0A(): pass

    label("Function_24_3F0A")

    TalkBegin(0xFE)

    #C0168
    ChrTalk(
        0xFE,
        (
            "さてと、これから旧市街を\x01",
            "巡回する所なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "……どこから回るかな。\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3F0A end

    def Function_25_3F5E(): pass

    label("Function_25_3F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3F6B")
    Call(0, 26)
    Return()

    label("loc_3F6B")

    EventBegin(0x0)
    Fade(500)
    OP_68(44710, -500, -23880, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(17000, 0)
    OP_4B(0x8, 0xFF)
    SetChrPos(0x101, 45140, -2500, -22290, 90)
    SetChrPos(0x102, 45040, -2500, -24290, 90)
    SetChrPos(0x109, 43640, -2500, -22090, 90)
    SetChrPos(0x105, 43950, -2500, -23790, 90)
    TurnDirection(0x101, 0x8, 0)
    TurnDirection(0x102, 0x8, 0)
    TurnDirection(0x109, 0x8, 0)
    TurnDirection(0x105, 0x8, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0170
    ChrTalk(
        0x8,
        "#11Pお前ら……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#6P#00000Fこんにちは。\x01",
            "教団事件の時に会って以来かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#12P#00100F久しぶりね、ディーノ君。\x02\x03",

            "その様子を見ると、\x01",
            "チームに復帰できたみたいね？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        "#11Pあ、ああ……まあな。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x8,
        (
            "#11Pヴァルドさんたちに\x01",
            "喧嘩を売っちゃった件は\x01",
            "薬のせいだって認めてくれたし……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "#11P……ケジメにけつバットを\x01",
            "食らっちゃったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x109,
        "#6P#10106Fけ、けつバットって……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#6P#10300Fフフ、まあ復帰できて\x01",
            "よかったじゃない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0178
    ChrTalk(
        0x8,
        (
            "#11Pワジ……\x01",
            "警察に入ったってのは\x01",
            "本当だったんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x8,
        "#11Pお前のせいでヴァルドさんは……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0180
    ChrTalk(
        0x101,
        (
            "#6P#00005Fヴァルド……？\x01",
            "彼がどうかしたのか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0181
    ChrTalk(
        0x8,
        (
            "#11P……お前らには\x01",
            "事件の時に世話になったから\x01",
            "一つだけ忠告してやる。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "#11Pヴァルドさんは近頃、\x01",
            "最悪に機嫌が悪いんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "#11P命が惜しかったら\x01",
            "ここに近づくんじゃねーぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#12P#00105F機嫌が悪いって……\x01",
            "何があったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        "#11P……全部、そこにいるワジのせいだ。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "#11Pあの事件からしばらくして\x01",
            "テスタメンツの連中が\x01",
            "大人しくなってきて……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "#11P今度はそのヘッドのワジが、\x01",
            "ロクなケジメをつけもしないで\x01",
            "いきなり警察のイヌになったんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#6P#00003F……なるほどな。\x02\x03",

            "#00001F要は、張り合いのある\x01",
            "喧嘩相手がいなくなって、\x01",
            "イライラが募ってるわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x109,
        "#6P#10106F気持ちは分からなくもないけど……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x105,
        "#6P#10308F……やれやれ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0x8,
        (
            "#11Pな、何がやれやれだ！！\x01",
            "てめー、自分が何をやったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "#11Pおかげでヴァルドさん、\x01",
            "最近はイグニスにもあまり\x01",
            "顔を出してくれなくなったんだぞ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x105,
        (
            "#6P#10303F……彼がそうしたいなら\x01",
            "そうすればいいさ。\x02\x03",

            "#10300Fフフ、僕も自分のやりたいように\x01",
            "やってるってだけの事だしね。\x02\x03",

            "その点において、君たちに\x01",
            "非難されるいわれはないつもりだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        "#11Pぐっ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0195
    ChrTalk(
        0x8,
        (
            "#11P……ふん、だったら\x01",
            "さっさと行っちまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "#11Pヴァルドさんに見つかったら\x01",
            "ワジだけじゃなく、お前らも\x01",
            "どうなっても知らないからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#6P#00003F……今日の所はおとなしく\x01",
            "退散した方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        (
            "#12P#00108F……そうね。\x02\x03",

            "#00100Fそれじゃあね、ディーノ君。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        "#11Pフンッ……\x02",
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x105,
        "#6P#10308F………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x138, 0)
    OP_93(0x8, 0x10E, 0x0)
    OP_4C(0x8, 0xFF)
    ModifyEventFlags(0, 0, 0x80)
    SetChrPos(0x0, 44540, -2500, -22490, 270)
    EventEnd(0x5)
    Return()

    # Function_25_3F5E end

    def Function_26_4842(): pass

    label("Function_26_4842")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_4912")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_48CB")

    #C0201
    ChrTalk(
        0x101,
        (
            "#00008F……しばらくここには\x01",
            "入らない方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#10303Fああ……\x01",
            "そうしてくれると助かるよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_48FC")

    label("loc_48CB")


    #C0203
    ChrTalk(
        0x101,
        "#00003F……イグニスに入るのは止めておこう。\x02",
    )

    CloseMessageWindow()

    label("loc_48FC")

    Sleep(50)
    SetChrPos(0x0, 44540, -2500, -22490, 270)
    EventEnd(0x4)

    label("loc_4912")

    Return()

    # Function_26_4842 end

    def Function_27_4913(): pass

    label("Function_27_4913")

    Return()

    # Function_27_4913 end

    def Function_28_4914(): pass

    label("Function_28_4914")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -13000, 0, -7000, 0)
    SetChrPos(0x102, -13000, 0, -7000, 0)
    SetChrPos(0x109, -13000, 0, -7000, 0)
    SetChrPos(0x105, -13000, 0, -7000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-13000, 1200, -8000, 0)
    MoveCamera(39, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0x5, 0x0, 0x0)
    OP_79(0x2)
    OP_68(-7600, 1200, -10100, 6500)
    MoveCamera(53, 29, 0, 6500)
    SetCameraDistance(19000, 6500)
    BeginChrThread(0x101, 3, 0, 29)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 30)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 31)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(1100)
    Sound(104, 0, 100, 0)
    OP_71(0x2, 0x5, 0x0, 0x0, 0x0)
    OP_79(0x2)
    SetMapObjFlags(0x2, 0x10)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)

    #C0204
    ChrTalk(
        0x109,
        (
            "#12P#10108F交換屋ナインヴァリ……\x02\x03",

            "#10106Fさすがの迫力でしたけど\x01",
            "はぐらかされてしまいましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        (
            "#00103F#5Pまあ、ああいう業界には\x01",
            "独自の仁義があるはずだから。\x02\x03",

            "#00100Fあそこまで教えてくれただけでも\x01",
            "感謝しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#11P#00006Fそうだな……\x02\x03",

            "#00008F……それにしても\x01",
            "人喰い虎みたいな男か。\x02\x03",

            "#00001Fテロリストでないとすると\x01",
            "猟兵の可能性が高そうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x105,
        (
            "#6P#10303Fま、猟兵の場合１人ってのは\x01",
            "ちょっと不自然だけどね。\x02\x03",

            "#10300Fそのあたりも含めて\x01",
            "課長さんに報告しておけば？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4D01")

    #C0208
    ChrTalk(
        0x101,
        (
            "#11P#00001Fああ、そうしよう。\x02\x03",

            "#00003F（猟兵関係なら、ランディが\x01",
            "  何か知っていそうだけど……）\x02\x03",

            "#00000F（まあいい、支援要請も片付けたし\x01",
            "  いったん支援課に戻るか……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DA4")

    label("loc_4D01")


    #C0209
    ChrTalk(
        0x101,
        (
            "#11P#00001Fああ、そうしよう。\x02\x03",

            "#00003F（猟兵関係なら、ランディが\x01",
            "  何か知っていそうだけど……）\x02\x03",

            "#00000F（まあいい、今は残っている\x01",
            "  支援要請を片付けよう。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DA4")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -9830, 0, -10560, 90)
    SetScenarioFlags(0x128, 5)
    OP_29(0xA1, 0x1, 0xE)
    ModifyEventFlags(1, 2, 0x80)
    OP_C9(0x0, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_28_4914 end

    def Function_29_4DDA(): pass

    label("Function_29_4DDA")


    def lambda_4DDF():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4DDF)

    def lambda_4DF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4DF9)
    WaitChrThread(0xFE, 1)

    def lambda_4E0E():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E0E)
    WaitChrThread(0xFE, 1)

    def lambda_4E2C():
        OP_95(0xFE, -6500, 0, -9600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E2C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xFA, 0x1F4)
    Return()

    # Function_29_4DDA end

    def Function_30_4E4D(): pass

    label("Function_30_4E4D")


    def lambda_4E52():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E52)

    def lambda_4E6C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4E6C)
    WaitChrThread(0xFE, 1)

    def lambda_4E81():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E81)
    WaitChrThread(0xFE, 1)

    def lambda_4E9F():
        OP_95(0xFE, -7700, 0, -9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4E9F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xC8, 0x1F4)
    Return()

    # Function_30_4E4D end

    def Function_31_4EC0(): pass

    label("Function_31_4EC0")


    def lambda_4EC5():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4EC5)

    def lambda_4EDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4EDF)
    WaitChrThread(0xFE, 1)

    def lambda_4EF4():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4EF4)
    WaitChrThread(0xFE, 1)

    def lambda_4F12():
        OP_95(0xFE, -7500, 0, -11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F12)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x14, 0x1F4)
    Return()

    # Function_31_4EC0 end

    def Function_32_4F33(): pass

    label("Function_32_4F33")


    def lambda_4F38():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F38)

    def lambda_4F52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4F52)
    WaitChrThread(0xFE, 1)

    def lambda_4F67():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F67)
    WaitChrThread(0xFE, 1)

    def lambda_4F85():
        OP_95(0xFE, -8700, 0, -10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4F85)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x46, 0x1F4)
    Return()

    # Function_32_4F33 end

    def Function_33_4FA6(): pass

    label("Function_33_4FA6")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01600.itp")
    LoadChrToIndex("chr/ch02100.itc", 0x1E)
    LoadChrToIndex("chr/ch02150.itc", 0x1F)
    LoadChrToIndex("apl/ch50019.itc", 0x20)
    LoadChrToIndex("apl/ch50030.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    LoadEffect(0x0, "event\\ev17004.eff")
    LoadEffect(0x1, "event\\ev17005.eff")
    SoundLoad(832)
    SoundLoad(2908)
    SoundLoad(2909)
    SoundLoad(2910)
    SoundLoad(3564)
    SoundLoad(3565)
    SoundLoad(3566)
    SoundLoad(3561)
    SoundLoad(3567)
    SoundLoad(2807)
    SoundLoad(2809)
    OP_68(1900, 1100, 9700, 0)
    MoveCamera(53, 29, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 1900, 0, 6800, 0)
    SetChrPos(0x102, 1100, 0, 5700, 0)
    SetChrPos(0x109, 2700, 0, 5700, 0)
    SetChrPos(0x105, 1900, 0, 4600, 0)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrPos(0x17, 9470, -60, -13170, 327)
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)

    def lambda_5122():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5122)
    Sleep(100)

    def lambda_513F():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_513F)
    Sleep(100)

    def lambda_515C():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_515C)
    Sleep(100)

    def lambda_5179():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5179)
    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0)
    OP_C9(0x0, 0x80000000)

    #N0210
    NpcTalk(
        0x17,
        "獰猛な声",
        "#3564V#30W──待てや、コラ。\x02",
    )

    CloseMessageWindow()
    OP_24(0xDEC)
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(4430, 2000, -7760, 3500)
    MoveCamera(96, 23, 0, 3500)
    OP_6E(500, 3500)
    SetCameraDistance(16990, 3500)

    def lambda_526B():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_526B)
    Sleep(50)

    def lambda_527B():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_527B)
    Sleep(50)

    def lambda_528B():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_528B)
    Sleep(50)

    def lambda_529B():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_529B)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    Sleep(1000)

    def lambda_52BE():
        OP_96(0xFE, 0x19DC, 0x0, 0xFFFFDEFE, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_52BE)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    #Sound(3306, 255, 80, 0)    #voice#Lloyd

    #C0211
    ChrTalk(
        0x101,
        "#00005F#30W#6P#Nあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0212
    ChrTalk(
        0x105,
        "#10308F#2908V#40W#6P#Nヴァルドか。\x02",
    )

    CloseMessageWindow()
    OP_24(0xB5C)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(1770, 1300, 3460, 0)
    MoveCamera(137, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15700, 0)
    SetMapObjFrame(0xFF, "light2", 0x0, 0x1)
    EndChrThread(0x17, 0x1)
    SetChrPos(0x17, 3800, 0, -2200, 315)
    SetChrPos(0x101, 500, 0, 6200, 180)
    SetChrPos(0x102, 3900, 0, 5200, 225)
    SetChrPos(0x109, 4200, 0, 6000, 225)
    SetChrPos(0x105, 1900, 0, 6200, 180)

    def lambda_53DA():
        OP_96(0xFE, 0x76C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_53DA)
    OP_0D()
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0x0, 0x1F4)

    #C0213
    ChrTalk(
        0x109,
        "#10105F（えっと、この人は……？）\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#5P#00108F（サーベルバイパーというチームを\x01",
            "  まとめている人だけど……）\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x105,
        (
            "#6P#10304Fヴァルド、どうしたんだい？\x02\x03",

            "#10300Fあんまりチームの方にも\x01",
            "顔を出してないそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0216
    AnonymousTalk(
        0x17,
        (
            "#30W……るせえ。\x01",
            "俺のことはどうだっていい。\x02\x03",

            "それよりも、てめえ……\x01",
            "サツの犬になりやがったらしいな？\x02\x03",

            "どういうつもりだ……アア？\x02",
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

    #C0217
    ChrTalk(
        0x105,
        (
            "#6P#10306F#30Wどういうつもりも何も……\x02\x03",

            "#10302Fテスタメンツのみんなは\x01",
            "納得してくれたし、他の誰にも\x01",
            "迷惑は掛けていないけど？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x17,
        (
            "#01601F#30W#11Pてめえ……本気で言ってんのか？\x02\x03",

            "#01603Fこのオレ様と……\x01",
            "ヴァルド・ヴァレスと決着付けずに\x01",
            "チームを抜けようなんざ……\x02\x03",

            "#01607F許されると思ってんのか、アア！？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x105,
        "#6P#10308F#30W………………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_573A():
        OP_96(0xFE, 0x384, 0x0, 0x13EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_573A)
    WaitChrThread(0x101, 1)

    #C0220
    ChrTalk(
        0x101,
        "#6P#00011Fヴァルド、待ってくれ！\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        "#00106Fその、これには事情が……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0222
    ChrTalk(
        0x17,
        (
            "#01607F#4S#11Pるせえ！\x01",
            "外野はすっこんでろ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0223
    ChrTalk(
        0x17,
        (
            "#01603F#11Pワジ、てめえがどんな狙いで\x01",
            "サツに入ったのかは知らねぇ……\x02\x03",

            "#01608Fだがな──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(500)
    SetCameraDistance(15200, 300)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    Sound(805, 0, 100, 0)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    #C0224
    ChrTalk(
        0x17,
        (
            "#01607F#11P──まさか五体満足で\x01",
            "旧市街#6Rこ　こ#から抜けられるとは\x01",
            "思ってねえだろうなァ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0x109,
        "#10101F……！\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x101,
        "#6P#00001Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x102,
        "#5P#00106Fこ、困ったわね……\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x105,
        "#6P#10303F#30W──ヴァルド。\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1680, 1300, 3250, 1200)

    def lambda_5974():
        OP_95(0xFE, 1900, 0, 4800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5974)
    Sleep(500)

    def lambda_5991():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5991)

    def lambda_599E():
        OP_96(0xFE, 0x2BC, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_599E)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x5A, 0x0)
    OP_6F(0x79)
    SetCameraDistance(14700, 30000)
    MoveCamera(138, 22, 0, 30000)

    #C0229
    ChrTalk(
        0x101,
        "#12P#00011Fお、おい、ワジ！？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x105,
        (
            "#6P#10308F#30Wいいから任せて。\x02\x03",

            "#10306F……ねえ、ヴァルド。\x01",
            "ひどく当たり前のことさ。\x02\x03",

            "テスタメンツにしろ\x01",
            "サーベルバイパーにしろ……\x02\x03",

            "#10301Fずっと居られる場所じゃないのは\x01",
            "君にも判っているんだろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0231
    ChrTalk(
        0x17,
        "#11P#01605F#11Pなにィ……！？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x105,
        (
            "#6P#10303F#30W僕がテスタメンツを結成したのは\x01",
            "旧市街#6Rこ　こ#で好き勝手をしていた\x01",
            "君たちへの抑止力になるためだ。\x02\x03",

            "#10300Fだが、最初はひ弱だった\x01",
            "テスタメンツのみんなも成長した。\x02\x03",

            "僕一人が抜けたって、\x01",
            "君たちに対抗できるくらいにね。\x02\x03",

            "僕の役目はもう終わってるのさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x17,
        "#11P#01607F#30W……て、てめえ……\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x105,
        (
            "#6P#10304F#30Wそして……\x01",
            "いつかきっと他のメンバーも\x01",
            "チームから巣立っていくはずだ。\x02\x03",

            "モラトリアムの季節を卒業して\x01",
            "自分だけの道を見つけていく……\x02\x03",

            "#10302F僕はそう信じている。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#12P#00005F#30Wワジ……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        "#5P#00108F#30Wワジ君……\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x17,
        "#11P#01608F#30W……………………………………\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0x105,
        (
            "#6P#10304F#30W君たちサーベルバイパーも同じだ。\x02\x03",

            "乱暴者は多いけど、マフィアの誘いに\x01",
            "乗らないだけの気概と根性を持っている。\x02\x03",

            "#10300Fだからヴァルド……\x01",
            "きっと君も道を見つけられるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    Sleep(300)
    #Sound(2807, 255, 100, 0)    #voice#Wald

    #C0239
    ChrTalk(
        0x17,
        "#11P#01604F#60W#10A……クク………\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    #C0240
    ChrTalk(
        0x17,
        "#11P#01609F#2809V#4S#35A#40Wハハハハハハハハハッ！！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrFlags(0x17, 0x10)
    SetChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x1)
    Sound(805, 0, 100, 0)
    Sleep(500)
    Fade(500)
    OP_68(1470, 1300, 3040, 700)
    MoveCamera(144, 22, 0, 700)
    OP_6E(600, 700)
    SetCameraDistance(13720, 700)
    Sound(533, 0, 60, 0)
    Sound(532, 0, 70, 0)
    SetChrSubChip(0x17, 0x2)
    Sleep(60)
    SetChrSubChip(0x17, 0x3)
    Sleep(500)
    OP_6F(0x79)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0241
    ChrTalk(
        0x17,
        (
            "#01611F#3565V#30W#11Pまさかてめぇがそんな\x01",
            "甘ッちょろい事を抜かすとはなァ！\x02\x03",

            "#01607F#3566Vもういい、それ以上喋るな！\x02\x03",

            "#3561Vてめえはこの『聖域』を汚した！\x01",
            "絶対に許すわけにはいかねえッ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xDE9)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Sleep(300)

    #C0242
    ChrTalk(
        0x105,
        "#6P#10303F#40Wそうかい……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0243
    ChrTalk(
        0x101,
        "#12P#00011Fおい、ワジ！\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x105,
        (
            "#6P#10303F#30Wロイド、手出し無用だ。\x02\x03",

            "#10301Fこのタイマンは僕一人で\x01",
            "ケリを付けなくちゃならない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Fade(250)
    ClearChrFlags(0x17, 0x10)
    ClearChrFlags(0x17, 0x2)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Sleep(300)

    #C0245
    ChrTalk(
        0x17,
        (
            "#11P#01604F#30Wクク、そのくらいは\x01",
            "判ってるみてぇだな……\x02\x03",

            "#01602F徹底的に叩き潰して\x01",
            "地面に這いつくばらせてやる……\x02\x03",

            "クク、そうすりゃ\x01",
            "てめぇも少しは目が覚めるだろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0246
    ChrTalk(
        0x105,
        "#6P#10303F#2909V#30W──お喋りは終わりだ。\x02",
    )

    CloseMessageWindow()
    OP_24(0xB5D)
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)

    #C0247
    ChrTalk(
        0x17,
        "#11P#01601F#3567Vあ……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDEF)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    Fade(500)
    MoveCamera(153, 25, 0, 2500)
    SetCameraDistance(15500, 2500)

    def lambda_6205():
        OP_96(0xFE, 0x12C, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6205)
    PlayEffect(0x1, 0x2, 0x105, 0x1, 0, 0, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sound(832, 2, 50, 0)
    Sleep(1000)
    OP_6F(0x79)
    Fade(500)
    OP_68(1900, 1100, 4100, 0)
    MoveCamera(38, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14790, 0)
    SetMapObjFrame(0xFF, "light2", 0x1, 0x1)
    OP_68(1900, 1100, 3100, 1500)
    SetCameraDistance(15790, 1500)
    SetChrPos(0x109, 4000, 0, 6000, 225)
    OP_93(0x101, 0x87, 0x0)
    OP_0D()
    OP_6F(0x79)

    #C0248
    ChrTalk(
        0x17,
        "#12P#01605F！？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 1)

    #C0249
    ChrTalk(
        0x101,
        "#00005F（これは……！）\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7452", 0)
    OP_C9(0x0, 0x80000000)

    #C0250
    ChrTalk(
        0x105,
        (
            "#5P#10301F#2910V#30W#20Aヴァルド─#1600W─\x01",
            "#40W本気で行くよ#12R㈲　㈲　㈲　㈲　㈲　㈲#。\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetScenarioFlags(0x1, 2)
    SetChrBattleFlags(0x101, 0x8)
    SetChrBattleFlags(0x102, 0x8)
    SetChrBattleFlags(0x109, 0x8)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x5B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_32(0x4, 0x0, 0x46)
    OP_32(0x4, 0xFB, 0x0)
    OP_32(0x4, 0xD, 0x32)
    Battle("BattleInfo_7F8", 0x30200011, 0x0, 0x0, 0x12, 0xFF)
    FadeToDark(0, 0, -1)
    MiniGame(0x32, 0x4, 0x3, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_32(0x4, 0xFE, 0x0)
    StopEffect(0x0, 0x0)
    StopEffect(0x1, 0x0)
    OP_CC(0x1, 0xFF, 0x0)
    Call(0, 34)
    Return()

    # Function_33_4FA6 end

    def Function_34_63F7(): pass

    label("Function_34_63F7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02153.itc", 0x1E)
    LoadChrToIndex("chr/ch02150.itc", 0x1F)
    LoadChrToIndex("chr/ch03050.itc", 0x20)
    LoadChrToIndex("chr/ch03051.itc", 0x21)
    LoadChrToIndex("apl/ch51111.itc", 0x22)
    LoadEffect(0x0, "battle\\ms00000.eff")
    SoundLoad(3568)
    SoundLoad(3569)
    SoundLoad(3570)
    OP_68(1900, 1000, 4100, 0)
    MoveCamera(135, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16500, 0)
    SetChrPos(0x101, 300, 0, 5100, 135)
    SetChrPos(0x102, 3900, 0, 5200, 225)
    SetChrPos(0x109, 4000, 0, 6000, 225)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x2)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    ClearChrFlags(0x17, 0x4)
    SetChrPos(0x17, 1900, 0, 1500, 0)
    OP_52(0x17, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x105, 1900, 0, 5800, 180)
    SetMapObjFrame(0xFF, "light2", 0x0, 0x1)
    StopBGM(0xFA0)
    WaitBGM()
    FadeToBright(250, 0)
    OP_68(1900, 1000, 2150, 700)
    SetCameraDistance(15500, 700)
    SetChrChip(0x0, 0x105, 0x32, 0xC8)

    def lambda_655B():
        OP_95(0xFE, 1900, 0, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_655B)
    WaitChrThread(0x105, 1)
    BeginChrThread(0x105, 3, 0, 35)
    Sleep(400)
    OP_68(1900, 1000, 1100, 1500)
    MoveCamera(130, 21, 0, 1500)
    OP_6E(550, 1500)
    SetCameraDistance(16500, 1500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    PlayEffect(0x0, 0x1, 0x105, 0x5, 0, 1100, 1000, 0, 0, 0, 200, 200, 200, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x17, 0x1E)
    SetChrSubChip(0x17, 0x0)

    def lambda_65FB():
        OP_9D(0xFE, 0x76C, 0x0, 0xFFFFFE0C, 0x898, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_65FB)
    Sound(2800, 255, 100, 0)    #voice#Wald
    Sleep(500)
    CancelBlur(0)
    WaitChrThread(0x17, 1)
    Sound(862, 0, 100, 0)
    Sound(833, 0, 30, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    SetChrSubChip(0x17, 0x3)

    def lambda_664B():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_664B)
    WaitChrThread(0x17, 1)
    Sound(811, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x64)

    #C0251
    ChrTalk(
        0x17,
        "#01610F#13A#11Pカハッ……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(800)

    def lambda_66A7():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_66A7)
    Sleep(1200)

    #C0252
    ChrTalk(
        0x17,
        (
            "#11P#01611F#40W……ググ……てめぇ……\x02\x03",

            "まさか今まで……\x01",
            "ずっと……手を抜いて……？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x105,
        (
            "#6P#10306F#30W……ランディじゃないけど\x01",
            "今のはちょっとした反則技さ。\x02\x03",

            "#10308Fでも、今日の君には\x01",
            "手加減抜きで行かせてもらった。\x02\x03",

            "#10301Fこれが……\x01",
            "僕が見せられる最後の誠意さ。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x17,
        (
            "#11P#01611F#50Wぎいッ……\x01",
            "……ワジ……てめえっ……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    #C0255
    ChrTalk(
        0x105,
        (
            "#11P#10303F#30Wさよなら、ヴァルド。\x02\x03",

            "#10300Fこの２年……\x01",
            "けっこう楽しかったよ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_6868():

        label("loc_6868")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_6868")

    QueueWorkItem2(0x101, 2, lambda_6868)

    def lambda_687A():

        label("loc_687A")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_687A")

    QueueWorkItem2(0x102, 2, lambda_687A)

    def lambda_688C():

        label("loc_688C")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_688C")

    QueueWorkItem2(0x109, 2, lambda_688C)
    OP_68(1900, 1000, 3100, 5000)
    SetCameraDistance(17500, 5000)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    def lambda_68C0():
        OP_95(0xFE, 1900, 0, 20000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_68C0)
    Sleep(3000)
    BeginChrThread(0x101, 3, 0, 36)
    Sleep(1000)
    BeginChrThread(0x109, 3, 0, 36)
    Sleep(800)
    BeginChrThread(0x102, 3, 0, 36)
    WaitChrThread(0x105, 1)
    OP_6F(0x79)
    OP_68(1900, 1000, -500, 2000)
    MoveCamera(140, 23, 0, 2000)
    SetCameraDistance(16500, 2000)
    Sleep(500)

    def lambda_6923():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_6923)
    Sleep(1200)
    OP_6F(0x79)
    OP_68(1900, 1000, -500, 50000)
    MoveCamera(136, 34, 0, 50000)
    OP_6E(550, 50000)
    SetCameraDistance(39710, 50000)
    OP_C9(0x0, 0x80000000)

    #C0256
    ChrTalk(
        0x17,
        (
            "#11P#01611F#3568V#50W#45Aふざけろ……\x01",
            "……絶対に認めねぇぞ……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)

    #C0257
    ChrTalk(
        0x17,
        (
            "#11P#01610F#3569V#50W#65Aてめぇ一人抜けるなんて……\x01",
            "認めてたまるかよおおおっ！！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_68(1900, 1000, -500, 6000)
    MoveCamera(136, 34, 0, 6000)
    OP_6E(550, 6000)
    SetCameraDistance(39710, 6000)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    EndChrThread(0x17, 0x2)
    Sleep(1500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)

    #C0258
    ChrTalk(
        0x17,
        "#11P#01607F#3570V#5S#50W#20Aワジイイイイイイッ！！！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x109, 0xFF)
    EndChrThread(0x105, 0xFF)
    Sleep(500)
    SetScenarioFlags(0x22, 0)
    NewScene("c1000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_63F7 end

    def Function_35_6AD1(): pass

    label("Function_35_6AD1")

    SetChrFlags(0x105, 0x10)
    SetChrFlags(0x105, 0x2)
    SetChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    Sleep(60)
    Sound(802, 0, 100, 0)
    Sound(3093, 255, 100, 0)    #voice#Lazy
    SetChrSubChip(0x105, 0x0)
    Sleep(240)
    Sound(534, 0, 40, 0)
    Sound(809, 0, 80, 0)
    SetChrChip(0x1, 0x105, 0x0, 0x0)

    def lambda_6B17():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_6B17)
    SetChrSubChip(0x105, 0x1)
    Sound(815, 0, 100, 0)
    Sound(195, 0, 100, 0)
    Sound(501, 0, 100, 0)
    Sleep(300)
    Sound(833, 0, 40, 0)
    SetChrSubChip(0x105, 0x1)
    WaitChrThread(0x105, 1)
    ClearChrFlags(0x105, 0x10)
    ClearChrFlags(0x105, 0x2)
    ClearChrFlags(0x105, 0x20)
    SetChrChipByIndex(0x105, 0x20)
    SetChrSubChip(0x105, 0x0)
    Return()

    # Function_35_6AD1 end

    def Function_36_6B6E(): pass

    label("Function_36_6B6E")

    EndChrThread(0xFE, 0x2)

    def lambda_6B77():
        OP_95(0xFE, 1900, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B77)
    WaitChrThread(0xFE, 1)

    def lambda_6B95():
        OP_95(0xFE, 1900, 0, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B95)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_6B6E end

    def Function_37_6BAF(): pass

    label("Function_37_6BAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 50000, -2100, -22500, 270)
    SetChrPos(0x104, 50000, -2100, -21700, 270)
    SetChrPos(0x109, 50000, -2100, -23300, 270)
    SetChrPos(0x105, -17300, 0, -10400, 90)
    SetChrPos(0x102, -18500, 0, -9800, 90)
    SetChrPos(0x103, -19700, 0, -11000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x8C, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sentaku", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    ClearMapObjFlags(0x8, 0x4)
    SoundLoad(128)
    Sound(128, 2, 100, 0)
    PlayBGM("ed7560", 0)
    OP_68(18500, 500, -25000, 0)
    MoveCamera(32, 4, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(40500, 0)
    MoveCamera(27, 4, 0, 6000)
    SetCameraDistance(45500, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x6E, 0x0)
    OP_68(47000, -600, -22500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    Sound(116, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xF, 0x0, 0x0)
    OP_79(0x4)
    OP_68(38500, -600, -23800, 5500)
    BeginChrThread(0x101, 3, 0, 38)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 39)
    Sleep(600)
    BeginChrThread(0x104, 3, 0, 40)
    Sleep(1300)
    Sound(117, 0, 100, 0)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    WaitChrThread(0x101, 3)
    SetChrPos(0x101, 18500, -2500, -22300, 315)

    def lambda_6DF9():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DF9)
    Sleep(100)
    EndChrThread(0x109, 0xFF)
    SetChrPos(0x109, 18500, -2500, -23800, 315)

    def lambda_6E2B():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6E2B)
    Sleep(100)
    EndChrThread(0x104, 0xFF)
    SetChrPos(0x104, 20000, -2500, -22300, 315)

    def lambda_6E5D():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6E5D)
    Fade(500)
    OP_68(16200, 0, -20000, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_68(5200, 1000, -9000, 8500)
    MoveCamera(59, 27, 0, 8500)
    SetCameraDistance(19500, 8500)
    WaitChrThread(0x101, 1)

    def lambda_6ED3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6ED3)
    WaitChrThread(0x109, 1)

    def lambda_6EE4():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6EE4)
    WaitChrThread(0x104, 1)

    def lambda_6EF5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6EF5)
    OP_6F(0x79)
    Sleep(300)
    OP_68(-11500, 1000, -10400, 3000)
    MoveCamera(55, 31, 0, 3000)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 41)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 42)
    Sleep(100)
    BeginChrThread(0x103, 3, 0, 43)
    Sleep(2500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x103, 0xFF)
    EndChrThread(0x105, 0xFF)
    OP_68(1200, 1100, -8000, 0)
    MoveCamera(37, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 2900, 0, -7750, 270)
    SetChrPos(0x104, 2250, 0, -6700, 270)
    SetChrPos(0x109, 2250, 0, -9350, 270)
    SetChrPos(0x105, -500, 0, -8250, 90)
    SetChrPos(0x102, 200, 0, -6700, 90)
    SetChrSubChip(0x102, 0x0)
    SetChrPos(0x103, -100, 0, -9350, 90)
    SetChrSubChip(0x103, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    SetCameraDistance(16500, 1500)
    OP_0D()
    OP_6F(0x79)

    #C0259
    ChrTalk(
        0x105,
        "#6P#10308F……どうだった？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#00006F#11P駄目だ……\x01",
            "まったく知らないらしい。\x02\x03",

            "#00013Fここ数日、ヴァルドの姿は\x01",
            "誰も見ていないみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        (
            "#00306F#11Pどうやら徹底的に舎弟どもを\x01",
            "遠ざけてたみてぇだからな……\x02\x03",

            "#00301F逆に行方を知らないか\x01",
            "喰ってかかられちまったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x109,
        "#12P#10106Fええ……必死そうでしたね。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x105,
        "#6P#10303F……そうか。\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#00106F#6Pこちらもテスタメンツの子たちに\x01",
            "改めて聞いてみたけど……\x02\x03",

            "#00108F誰も最近、ヴァルドさんの姿を\x01",
            "見かけた人はいないみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#6P#00206Fはい……泥酔して潰れた姿を\x01",
            "一時期よく見かけたそうですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#00001F#11Pそうか……やっぱり\x01",
            "背後関係は見えて来ないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x104,
        (
            "#00303F#11Pあの野郎、一体どこから\x01",
            "《グノーシス》なんぞを……\x02",
        )
    )

    CloseMessageWindow()

    #C0268
    ChrTalk(
        0x105,
        "#6P#10308F…………………………………\x02",
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x109,
        (
            "#12P#10113F……ワジ君、大丈夫？\x02\x03",

            "何だか顔色が良くないよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x105,
        (
            "#6P#10304Fフフ、雨で冷えたせいかな。\x02\x03",

            "#10300Fとりあえず、アッバスたちに\x01",
            "情報収集は頼んでおいた。\x02\x03",

            "ヴァルドのことは置いておいて\x01",
            "僕らも一度支援課に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#00006F#11P……そうだな。\x01",
            "キーアが朝食を用意して\x01",
            "くれているみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        (
            "#00102F#6Pふふ、何だか最近、\x01",
            "お世話になりっぱなしね。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    ReplaceBGM("ed7150", "ed7560")
    StopSound(128, 1000, 100)
    Sleep(1000)
    Sleep(1000)
    SetScenarioFlags(0x23, 1)
    NewScene("c0110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_6BAF end

    def Function_38_7474(): pass

    label("Function_38_7474")


    def lambda_7479():
        OP_95(0xFE, 45000, -2500, -22500, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7479)

    def lambda_7493():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7493)
    WaitChrThread(0xFE, 1)

    def lambda_74A8():
        OP_95(0xFE, 38500, -2500, -23800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74A8)
    WaitChrThread(0xFE, 1)

    def lambda_74C6():
        OP_95(0xFE, 27500, -2500, -23800, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74C6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_7474 end

    def Function_39_74E0(): pass

    label("Function_39_74E0")


    def lambda_74E5():
        OP_95(0xFE, 45000, -2500, -23300, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74E5)

    def lambda_74FF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_74FF)
    WaitChrThread(0xFE, 1)

    def lambda_7514():
        OP_95(0xFE, 38500, -2500, -24600, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7514)
    WaitChrThread(0xFE, 1)

    def lambda_7532():
        OP_95(0xFE, 27500, -2500, -24600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7532)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_74E0 end

    def Function_40_754C(): pass

    label("Function_40_754C")


    def lambda_7551():
        OP_95(0xFE, 45000, -2500, -21700, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7551)

    def lambda_756B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_756B)
    WaitChrThread(0xFE, 1)

    def lambda_7580():
        OP_95(0xFE, 38500, -2500, -23000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7580)
    WaitChrThread(0xFE, 1)

    def lambda_759E():
        OP_95(0xFE, 27500, -2500, -23000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_759E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_754C end

    def Function_41_75B8(): pass

    label("Function_41_75B8")


    def lambda_75BD():
        OP_95(0xFE, -9500, 0, -10400, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75BD)
    WaitChrThread(0xFE, 1)

    def lambda_75DB():
        OP_95(0xFE, -3500, 0, -9000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75DB)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_75B8 end

    def Function_42_75F5(): pass

    label("Function_42_75F5")


    def lambda_75FA():
        OP_95(0xFE, -9500, 0, -9800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75FA)
    WaitChrThread(0xFE, 1)

    def lambda_7618():
        OP_95(0xFE, -3500, 0, -8400, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7618)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_42_75F5 end

    def Function_43_7632(): pass

    label("Function_43_7632")


    def lambda_7637():
        OP_95(0xFE, -9500, 0, -11000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7637)
    WaitChrThread(0xFE, 1)

    def lambda_7655():
        OP_95(0xFE, -3500, 0, -9600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7655)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_7632 end

    def Function_44_766F(): pass

    label("Function_44_766F")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(8090, -4470, -37870, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16540, 0)
    SetChrFlags(0xA, 0x80)
    EndChrThread(0xA, 0x0)
    SetChrFlags(0xB, 0x80)
    EndChrThread(0xB, 0x0)
    SetChrPos(0x101, 9720, -6420, -37340, 0)
    SetChrPos(0x102, 8270, -6390, -37670, 0)
    SetChrPos(0x103, 10420, -6420, -38430, 0)
    SetChrPos(0x104, 9060, -6390, -39050, 0)
    SetChrPos(0x109, 11890, -6440, -37730, 310)
    SetChrPos(0x105, 11080, -6420, -39330, 310)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0273
    ChrTalk(
        0x101,
        (
            "#12P#00000Fここが手配魔獣の退治依頼が出ていた、\x01",
            "ジオフロントＤ区画の入り口か……\x02\x03",

            "#00003F以前は資材なんかが\x01",
            "置いてあったはずだけど、\x01",
            "依頼のために撤去されたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x103,
        (
            "#12P#00203Fふむ、少し疑問なのですが……\x02\x03",

            "#00200Fどうして導力ネットが\x01",
            "引かれていない旧市街に、\x01",
            "ジオフロントの入り口が？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x104,
        "#12P#00305Fああ、そういやそうだな。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x109,
        (
            "#12P#10105F確か旧市街は、都市開発から\x01",
            "取り残された場所のはずですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x102,
        (
            "#12P#00103Fええ……\x01",
            "以前、Ｄ区画は議員と役人たちの思惑で\x01",
            "建造されたということは話したけど……\x02\x03",

            "#00108F地下の工事が際限なく進められるうちに\x01",
            "こんな所まで拡大してしまったみたいね。\x02\x03",

            "#00106Fありもしない需要がでっちあげられて、\x01",
            "無計画に建造が始まったみたいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x105,
        (
            "#12P#10300Fふうん、なるほどね。\x02\x03",

            "#10304F要するに、腐敗した行政による\x01",
            "利権の産物って感じかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#12P#00006Fああ、確かにな……\x02\x03",

            "#00000Fディーターさんが市長になってから\x01",
            "改善はされてきてるみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#12P#00300Fま、手配魔獣の退治にいくなら\x01",
            "さっさと入ってみるとしようや。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x16B, 2)
    ModifyEventFlags(0, 3, 0x80)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xB, 0, 0, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 10220, -6440, -36310, 0)
    EventEnd(0x5)
    Return()

    # Function_44_766F end

    def Function_45_7B82(): pass

    label("Function_45_7B82")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-13300, 1100, -10600, 0)
    MoveCamera(60, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -13300, 0, -9400, 200)
    SetChrPos(0x102, -14000, 0, -11600, 20)
    SetChrPos(0x103, -14600, 0, -10500, 110)
    SetChrPos(0x109, -12000, 0, -10500, 290)
    SetChrPos(0x105, -12600, 0, -11600, 340)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    MoveCamera(70, 30, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0281
    ChrTalk(
        0x102,
        (
            "#12P#00101F……昨夜から今朝にかけての\x01",
            "ランディの動きが見えてきたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        "#5P#00003Fああ、軽く整理してみよう。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_7D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FF2")
    SetScenarioFlags(0x1, 1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0283
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K最初にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7DB7")
    ClearScenarioFlags(0x1, 1)

    label("loc_7DB7")

    SetChrName("")

    #A0284
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K次にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7E48")
    ClearScenarioFlags(0x1, 1)

    label("loc_7E48")

    SetChrName("")

    #A0285
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K最後にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7EE4")
    ClearScenarioFlags(0x1, 1)

    label("loc_7EE4")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F76")

    #C0286
    ChrTalk(
        0x101,
        (
            "#5P#00003F（いや……\x01",
            "  この順番じゃないはずだ。）\x02\x03",

            "#00001F（もう一度整理してみよう。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F71")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_7F71")

    Jump("loc_7FED")

    label("loc_7F76")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_7F86"),
        (SWITCH_DEFAULT, "loc_7FBC"),
    )


    label("loc_7F86")

    OP_2C(0xAA, 0x1)

    #C0287
    ChrTalk(
        0x101,
        "#5P#00000F（間違いない、この順番だ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FED")

    label("loc_7FBC")


    #C0288
    ChrTalk(
        0x101,
        "#5P#00003F（……多分、この順番だな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_7FED")

    label("loc_7FED")

    Jump("loc_7D03")

    label("loc_7FF2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３時～４時　カジノバー《バルカ》\x01",
            "５時～６時　修理屋《ギヨーム工房》\x01",
            "６時～　　　交換屋《ナインヴァリ》\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    #C0290
    ChrTalk(
        0x101,
        (
            "#5P#00006F──おそらく最初に\x01",
            "ドレイク・オーナーに預けていた\x01",
            "トランクを受け取ったんだろう。\x02\x03",

            "#00008Fそのトランクに入っていたのは\x01",
            "ランディの猟兵時代の得物……\x02\x03",

            "#00001F多分、かなりの攻撃力を誇る\x01",
            "導力ライフルじゃないかと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x103,
        (
            "#6P#00203F普通、そうしたライフルは\x01",
            "分解した状態で持ち運ぶはずです。\x02\x03",

            "#00201F２年ほど使っていなかったため、\x01",
            "ランディさんは分解されたユニットを\x01",
            "修理工房で整備してもらった……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x109,
        (
            "#11P#10103F──うん、間違いないと思う。\x02\x03",

            "#10108F武装の整備は、戦場での生死を\x01",
            "左右するものだから……\x02\x03",

            "#10101Fランディ先輩なら絶対に\x01",
            "綿密にチェックしたはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        (
            "#10303F最後に、交換屋に寄って\x01",
            "色々と仕入れたみたいだけど……\x02\x03",

            "#10301F火薬の弾薬も仕入れたってことは\x01",
            "かなり特殊なライフルなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x102,
        (
            "#12P#00108Fラインフォルト社の中には\x01",
            "導力式と火薬式を切り替えられる\x01",
            "ラインナップもあるそうだけど……\x02\x03",

            "#00101Fいずれにしても、相当特殊で\x01",
            "強化されたライフルでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#5P#00006Fああ、赤い星座の猟兵たちも\x01",
            "見たことのない巨大なライフルを\x01",
            "使っていたからな。\x02\x03",

            "#00013F──よし、これで大体、\x01",
            "ランディの状況は掴めたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#6P#00206F最後にランディさんが交換屋を\x01",
            "訪れたのが今朝の６時過ぎ……\x02\x03",

            "#00208F現在、１０時くらいですから\x01",
            "４時間近くも経っていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x109,
        (
            "#11P#10106F今から先輩の足に追いつくのは\x01",
            "かなり難しそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#00003F……いや、ランディだって\x01",
            "いくらタフでも限度があるはずだ。\x02\x03",

            "#00001F《赤い星座》に仕掛けるなら\x01",
            "さすがに仮眠くらいは取るだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x105,
        (
            "#10304Fその上で、地形の利を活かして\x01",
            "一気に仕掛けてケリを付ける……\x02\x03",

            "#10302Fま、玉砕覚悟で\x01",
            "特攻するつもりじゃなければ\x01",
            "そのあたりが妥当だろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#12P#00101F……いずれにしても\x01",
            "もうそんなに余裕がないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#5P#00013Fああ、こうなったら駄目元で\x01",
            "マインツ方面に行くしか──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    def lambda_8767():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8767)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_878C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_878C)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0302
    ChrTalk(
        0x101,
        "#5P#00011Fまさか……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x103,
        "#6P#00205Fランディさんから……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0304
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F──はい、特務支援課、\x01",
            "ロイド・バニングスです！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0305
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "やあ、ロイドさん。\x02\x03",

            "……フフ、どうやら別の誰かと\x01",
            "カン違いさせてしまったようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0306
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00005Fそ、その声は……\x02\x03",

            "#00013F……どうしてこの番号が？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("青年の声")

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、言ったでしょう。\x01",
            "ロイドさんたちのファンだと。\x02\x03",

            "──タイムズ百貨店。\x02\x03",

            "お暇でしたら是非、\x01",
            "屋上までいらしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    Sleep(400)
    Sound(894, 2, 100, 0)
    Sleep(1200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_24(0x37E)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    #C0308
    ChrTalk(
        0x103,
        (
            "#6P#00201F……ロイドさん。\x01",
            "今の通信は……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x102,
        "#12P#00108Fい、一体誰だったの？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_64(0x101)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0310
    ChrTalk(
        0x101,
        (
            "#5P#00003F……《黒月》のツァオだ。\x02\x03",

            "#00013F中央広場のデパートの\x01",
            "屋上で待っているらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0311
    ChrTalk(
        0x109,
        "#11P#10111Fええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x105,
        (
            "#10301Fこんな時に……\x01",
            "いったい何のつもりだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#5P#00006F……分からない。\x01",
            "ただ、あの男が意味もなく\x01",
            "連絡してくるとも思えない。\x02\x03",

            "#00001F山道に出る前に\x01",
            "寄るだけ寄ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        "#12P#00101Fわ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x103,
        "#6P#00201Fとにかく急ぎましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -13220, 0, -9320, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 1)
    OP_29(0xAA, 0x1, 0x4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    OP_24(0x323)
    OP_24(0x37E)
    EventEnd(0x5)
    Return()

    # Function_45_7B82 end

    def Function_46_8D16(): pass

    label("Function_46_8D16")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(803)
    SoundLoad(894)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis007.itp")
    OP_68(-6100, -2500, -25800, 0)
    MoveCamera(65, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x101, -5500, -3800, -24600, 215)
    SetChrPos(0x102, -6900, -3800, -26100, 35)
    SetChrPos(0x103, -7200, -3650, -25050, 125)
    SetChrPos(0x109, -4900, -3800, -26300, 305)
    SetChrPos(0x105, -6100, -3800, -26800, 35)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    MoveCamera(75, 25, 0, 3000)
    SetCameraDistance(17000, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0316
    ChrTalk(
        0x102,
        (
            "#12P#00101F……昨夜から今朝にかけての\x01",
            "ランディの動きが見えてきたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#5P#00003Fああ、軽く整理してみよう。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_8E9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_918A")
    SetScenarioFlags(0x1, 1)
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0318
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K最初にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8F4F")
    ClearScenarioFlags(0x1, 1)

    label("loc_8F4F")

    SetChrName("")

    #A0319
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K次にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8FE0")
    ClearScenarioFlags(0x1, 1)

    label("loc_8FE0")

    SetChrName("")

    #A0320
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K最後にランディが訪れたのは？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交換屋《ナインヴァリ》\x01",      # 0
            "修理屋《ギヨーム工房》\x01",      # 1
            "カジノバー《バルカ》\x01",        # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_907C")
    ClearScenarioFlags(0x1, 1)

    label("loc_907C")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_910E")

    #C0321
    ChrTalk(
        0x101,
        (
            "#5P#00003F（いや……\x01",
            "  この順番じゃないはずだ。）\x02\x03",

            "#00001F（もう一度整理してみよう。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9109")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_9109")

    Jump("loc_9185")

    label("loc_910E")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_911E"),
        (SWITCH_DEFAULT, "loc_9154"),
    )


    label("loc_911E")

    OP_2C(0xAA, 0x1)

    #C0322
    ChrTalk(
        0x101,
        "#5P#00000F（間違いない、この順番だ。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_9154")


    #C0323
    ChrTalk(
        0x101,
        "#5P#00003F（……多分、この順番だな。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_9185")

    label("loc_9185")

    Jump("loc_8E9B")

    label("loc_918A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３時～４時　カジノバー《バルカ》\x01",
            "５時～６時　修理屋《ギヨーム工房》\x01",
            "６時～　　　交換屋《ナインヴァリ》\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_0D()

    #C0325
    ChrTalk(
        0x101,
        (
            "#5P#00006F──おそらく最初に\x01",
            "ドレイク・オーナーに預けていた\x01",
            "トランクを受け取ったんだろう。\x02\x03",

            "#00008Fそのトランクに入っていたのは\x01",
            "ランディの猟兵時代の得物……\x02\x03",

            "#00001F多分、かなりの攻撃力を誇る\x01",
            "導力ライフルじゃないかと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        (
            "#6P#00203F普通、そうしたライフルは\x01",
            "分解した状態で持ち運ぶはずです。\x02\x03",

            "#00201F２年ほど使っていなかったため、\x01",
            "ランディさんは分解されたユニットを\x01",
            "修理工房で整備してもらった……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x109,
        (
            "#10103F#11P──うん、間違いないと思う。\x02\x03",

            "#10108F武装の整備は、戦場での生死を\x01",
            "左右するものだから……\x02\x03",

            "#10101Fランディ先輩なら絶対に\x01",
            "綿密にチェックしたはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x105,
        (
            "#12P#10303F最後に、交換屋に寄って\x01",
            "色々と仕入れたみたいだけど……\x02\x03",

            "#10301F火薬の弾薬も仕入れたってことは\x01",
            "かなり特殊なライフルなのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        (
            "#12P#00108Fラインフォルト社の中には\x01",
            "導力式と火薬式を切り替えられる\x01",
            "ラインナップもあるそうだけど……\x02\x03",

            "#00101Fいずれにしても、相当特殊で\x01",
            "強化されたライフルでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        (
            "#5P#00006Fああ、赤い星座の猟兵たちも\x01",
            "見たことのない巨大なライフルを\x01",
            "使っていたからな。\x02\x03",

            "#00013F──よし、これで大体、\x01",
            "ランディの状況は掴めたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x103,
        (
            "#6P#00206F最後にランディさんが交換屋を\x01",
            "訪れたのが今朝の６時過ぎ……\x02\x03",

            "#00208F現在、１０時くらいですから\x01",
            "４時間近くも経っていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x109,
        (
            "#10106F#11P今から先輩の足に追いつくのは\x01",
            "かなり難しそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#5P#00003F……いや、ランディだって\x01",
            "いくらタフでも限度があるはずだ。\x02\x03",

            "#00001F《赤い星座》に仕掛けるなら\x01",
            "さすがに仮眠くらいは取るだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x105,
        (
            "#12P#10304Fその上で、地形の利を活かして\x01",
            "一気に仕掛けてケリを付ける……\x02\x03",

            "#10302Fま、玉砕覚悟で\x01",
            "特攻するつもりじゃなければ\x01",
            "そのあたりが妥当だろうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#12P#00101F……いずれにしても\x01",
            "もうそんなに余裕がないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#5P#00013Fああ、こうなったら駄目元で\x01",
            "マインツ方面に行くしか──\x02",
        )
    )

    CloseMessageWindow()
    Sound(803, 2, 100, 0)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)

    def lambda_9907():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_9907)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_992C():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_992C)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x6)
    Sound(802, 0, 100, 0)
    Sleep(500)

    #C0337
    ChrTalk(
        0x101,
        "#5P#00011Fまさか……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x103,
        "#6P#00205Fランディさんから……？\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x101, 0x7)
    OP_24(0x323)
    Sound(804, 0, 100, 0)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0339
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#00007F──はい、特務支援課、\x01",
            "ロイド・バニングスです！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性の声")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "やあ、ロイドさん。\x02\x03",

            "……フフ、どうやら別の誰かと\x01",
            "カン違いさせてしまったようですね。\x02",
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
            "#00005Fそ、その声は……\x02\x03",

            "#00013F……どうしてこの番号が？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性の声")

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "フフ、言ったでしょう。\x01",
            "ロイドさんたちのファンだと。\x02\x03",

            "──タイムズ百貨店。\x02\x03",

            "お暇でしたら是非、\x01",
            "屋上までいらしてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(813, 0, 70, 0)
    Sleep(400)
    Sound(894, 2, 100, 0)
    Sleep(1200)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    OP_CC(0x0, 0x0, 0x3)
    SetChrSubChip(0x101, 0x6)
    Sound(804, 0, 100, 0)
    OP_24(0x37E)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    #C0343
    ChrTalk(
        0x103,
        (
            "#6P#00201F……ロイドさん。\x01",
            "今の通信は……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        "#12P#00108Fい、一体誰だったの？\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(300)
    Fade(250)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(802, 0, 100, 0)
    OP_0D()

    #C0345
    ChrTalk(
        0x101,
        (
            "#5P#00003F……《黒月》のツァオだ。\x02\x03",

            "#00013F中央広場のデパートの\x01",
            "屋上で待っているらしい。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0346
    ChrTalk(
        0x109,
        "#10111F#11Pええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x105,
        (
            "#12P#10301Fこんな時に……\x01",
            "いったい何のつもりだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#5P#00006F……分からない。\x01",
            "ただ、あの男が意味もなく\x01",
            "連絡してくるとも思えない。\x02\x03",

            "#00001F山道に出る前に\x01",
            "寄るだけ寄ってみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#12P#00101Fわ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x103,
        "#6P#00201Fとにかく急ぎましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    SetChrPos(0x0, -5500, -3800, -24330, 207)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 1)
    OP_29(0xAA, 0x1, 0x4)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7151", 0)
    OP_24(0x323)
    OP_24(0x37E)
    EventEnd(0x5)
    Return()

    # Function_46_8D16 end

    def Function_47_9EB7(): pass

    label("Function_47_9EB7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(9630, 1300, 4460, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16210, 0)
    SetChrPos(0x101, 13000, 0, 7800, 225)
    SetChrPos(0x102, 13000, 0, 7800, 225)
    SetChrPos(0x109, 13000, 0, 7800, 225)
    SetChrPos(0x105, 13000, 0, 7800, 225)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x3, 0x10)
    OP_71(0x3, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    OP_0D()
    Sleep(500)

    def lambda_9F92():
        OP_95(0x101, 8630, 0, 4260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9F92)

    def lambda_9FAC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_9FAC)
    Sleep(500)

    def lambda_9FC0():
        OP_95(0x102, 9430, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9FC0)

    def lambda_9FDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9FDA)
    Sleep(500)

    def lambda_9FEE():
        OP_95(0x109, 9830, 0, 5460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9FEE)

    def lambda_A008():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A008)
    Sleep(500)

    def lambda_A01C():
        OP_95(0x105, 10630, 0, 4460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A01C)

    def lambda_A036():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_A036)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_A04E():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A04E)
    WaitChrThread(0x102, 1)

    def lambda_A05F():
        OP_93(0x102, 0x168, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A05F)
    WaitChrThread(0x109, 1)

    def lambda_A070():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A070)
    WaitChrThread(0x105, 1)

    def lambda_A081():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A081)
    SetMapObjFlags(0x3, 0x0)
    WaitChrThread(0x101, 1)

    #C0351
    ChrTalk(
        0x102,
        (
            "#12P#00103Fでも、ゲバル議員か……\x02\x03",

            "#00108F職を追われることになった\x01",
            "議員たちの中では、\x01",
            "まだマシな方かもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x109,
        (
            "#10101Fええ、教団事件をきっかけに\x01",
            "逮捕された議員たちは\x01",
            "もっと厳しい状況にあると思います。\x02\x03",

            "#10103F当然の報いだとは思いますが、\x01",
            "踊らされた側の人間は、どこかで\x01",
            "納得はいっていないでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#6P#00003Fああ、でも結局のところ、\x01",
            "悪事はいつか自分に跳ね返る……\x01",
            "それが世の常ってものだろう。\x02\x03",

            "#00000F逆に立ち直ろうと努力していれば、\x01",
            "必ず報われる日は来るはずだ。\x02\x03",

            "#00004Fあのゲバルさんにしても\x01",
            "捕まった議員たちにしても、\x01",
            "いつかそうなれるといいんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        (
            "#12P#00103Fそうね……\x01",
            "（アーネストさんもいつかは……）\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、さすがリーダー。\x01",
            "言うことがオツじゃないか。\x02\x03",

            "#10302Fどうだい、今の話をツマミに\x01",
            "このままトリニティで\x01",
            "一杯引っかけて行くというのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#6P#00006Fはぁ、勤務中に\x01",
            "そんなこと出来るわけないだろう。\x02\x03",

            "#00000F……とにかく。\x01",
            "これで旧市街の調査は終了だ。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A50F")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0357
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "◆「調査状況は？（テスト用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まだ残りがある】\x01",              # 0
            "【６箇所の確認が終わった】\x01",      # 1
            "【変更しない】\x01",                  # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_A4E2"),
        (1, "loc_A4F6"),
        (2, "loc_A50A"),
        (SWITCH_DEFAULT, "loc_A50F"),
    )


    label("loc_A4E2")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    Jump("loc_A50F")

    label("loc_A4F6")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    Jump("loc_A50F")

    label("loc_A50A")

    Jump("loc_A50F")

    label("loc_A50F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A564")

    #C0358
    ChrTalk(
        0x101,
        (
            "#6P#00000Fよし、それじゃ\x01",
            "引き続き調査にあたろう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A5B6")

    label("loc_A564")

    OP_29(0x6A, 0x1, 0x6)

    #C0359
    ChrTalk(
        0x101,
        (
            "#6P#00000Fよし、これで一通り調査は済んだな。\x02\x03",

            "市民会館へ報告に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A5B6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x132, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 9630, 0, 4460, 225)
    EventEnd(0x5)
    Return()

    # Function_47_9EB7 end

    def Function_48_A5EE(): pass

    label("Function_48_A5EE")

    EventBegin(0x0)
    Fade(500)
    OP_68(43660, -1700, -21280, 0)
    MoveCamera(37, 21, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(21420, 0)
    SetChrPos(0x101, 42460, -2500, -21980, 45)
    SetChrPos(0x102, 43410, -2500, -23070, 45)
    SetChrPos(0x104, 43290, -2500, -24550, 45)
    SetChrPos(0x109, 41320, -2500, -22550, 45)
    SetChrPos(0x105, 41680, -2500, -23920, 45)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0360
    ChrTalk(
        0x8,
        (
            "#11Pあっ、おまえら……\x01",
            "一体なんの用だよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x8,
        (
            "#11Pそれにそこにいるのは……\x01",
            "ワ、ワジ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#11Pくっ……！\x01",
            "あっちいけ、この野郎！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x105,
        (
            "#6P#10308Fやれやれ……\x01",
            "どうにも嫌われているね。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x101,
        (
            "#6P#00003F……気持ちは判るけど\x01",
            "ちょっと話をさせてくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは教授の依頼で\x01",
            "問診表を回収している事情を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0366
    ChrTalk(
        0x8,
        "#11Pモンシンヒョウ……？\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#11P……ってああ、ウルスラ病院に\x01",
            "通ってた頃に渡されたアレか。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x104,
        "#12P#00305Fなんだ、忘れてたわけじゃないのか？\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x8,
        (
            "#11Pふん、クスリの影響なんか\x01",
            "もう全然残ってないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        (
            "#11Pそれなのにわざわざ\x01",
            "病院に行くなんてかったるいしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#12P#00101Fディーノくん……\x01",
            "自己判断はよくないわ。\x02\x03",

            "#00103F万が一にも症状が残ってたら、\x01",
            "バイパーの皆にも迷惑を\x01",
            "かけてしまうかもしれないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        "#11Pう……確かにそうだけど……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#11P……ああもう、わかったよ！\x01",
            "ちょっとそこで待っててくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "#11Pどっかにしまってたから、\x01",
            "急いで書いて持ってくる。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AA0C():
        OP_95(0xFE, 44930, -2500, -22750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AA0C)
    WaitChrThread(0x8, 1)

    def lambda_AA2A():
        OP_95(0xFE, 47960, -2100, -22440, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AA2A)
    Sleep(50)

    def lambda_AA47():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AA47)
    Sleep(50)

    def lambda_AA57():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AA57)
    Sleep(50)

    def lambda_AA67():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AA67)
    Sleep(50)

    def lambda_AA77():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_AA77)
    Sleep(50)

    def lambda_AA87():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_AA87)
    WaitChrThread(0x8, 1)
    Sound(116, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(700)

    def lambda_AAB6():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AAB6)

    def lambda_AAD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_AAD0)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    OP_0D()

    #C0375
    ChrTalk(
        0x109,
        "#6P#10106Fふう、何とか回収できそうですね。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        "#6P#00000Fああ、少し待ってるとするか。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x80)
    OP_71(0x4, 0x10, 0x0, 0x0, 0x0)
    OP_79(0x0)
    SetMapObjFlags(0x4, 0x10)
    SetChrPos(0x8, 44880, -2500, -20090, 225)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_93(0x101, 0x2D, 0x0)
    OP_93(0x102, 0x2D, 0x0)
    OP_93(0x104, 0x2D, 0x0)
    OP_93(0x109, 0x2D, 0x0)
    OP_93(0x105, 0x2D, 0x0)
    Sleep(1000)
    Sound(117, 0, 100, 0)
    Sleep(1000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0377
    ChrTalk(
        0x8,
        "#11P……ホラ、これでいいんだろ？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0378
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x32E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x32E, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0379
    ChrTalk(
        0x101,
        "#6P#00000Fああ、確かに受け取ったよ。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        "#12P#00100Fありがとう、ディーノくん。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11P……ふん、お礼を言われる\x01",
            "スジアイなんかないだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#11Pほら、さっさとワジを連れて\x01",
            "どっかにいっちまえ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#6P#00006Fわ、分かったから。\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x105,
        "#6P#10303F……邪魔したね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 3)
    OP_29(0x70, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ADE4")

    #A0385
    AnonymousTalk(
        0x101,
        (
            "#00000Fこれで全ての問診表を\x01",
            "回収し終わったな。\x02\x03",

            "さっそくセイランド教授に\x01",
            "届けにいくとしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_ADE4")

    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 43610, -2500, -21900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_48_A5EE end

    def Function_49_AE11(): pass

    label("Function_49_AE11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-2990, 1930, -22180, 0)
    MoveCamera(44, 22, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(40910, 0)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x16, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_AE8B")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_AECA")

    label("loc_AE8B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_AEAD")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_AECA")

    label("loc_AEAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_AECA")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_AECA")

    OP_68(-2990, 1930, -22180, 5000)
    MoveCamera(44, 22, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(49730, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_AFD6")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x104, 910, 0, 24450, 180)

    def lambda_AF68():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_AF68)

    def lambda_AF82():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_AF82)
    Sleep(100)

    def lambda_AF9F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_AF9F)
    Sleep(50)

    def lambda_AFBC():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_AFBC)
    Jump("loc_B179")

    label("loc_AFD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_B0AA")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x109, 910, 0, 24450, 180)

    def lambda_B03C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B03C)

    def lambda_B056():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B056)
    Sleep(100)

    def lambda_B073():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B073)
    Sleep(50)

    def lambda_B090():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B090)
    Jump("loc_B179")

    label("loc_B0AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_B179")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x105, 910, 0, 24450, 180)

    def lambda_B110():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_B110)

    def lambda_B12A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B12A)
    Sleep(100)

    def lambda_B147():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B147)
    Sleep(50)

    def lambda_B164():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B164)

    label("loc_B179")

    OP_6F(0x79)
    OP_68(2000, 1930, 2050, 7000)
    MoveCamera(41, 21, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(17730, 7000)
    OP_6F(0x79)

    #C0386
    ChrTalk(
        0x1A2,
        (
            "ここは……\x01",
            "またずい分さびれた場所だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#00103F……旧市街よ。\x01",
            "開発から取り残された場所なの。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A2, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x1A2)

    #C0388
    ChrTalk(
        0x1A2,
        (
            "フン……こういうのは\x01",
            "ホントどこの国にもあるんだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0389
    ChrTalk(
        0x1A2,
        "#12Pもう十分だ、東通りに戻るぞ。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        "#00005Fあ、ああ……分かった。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    SetScenarioFlags(0x1C5, 4)
    OP_29(0x73, 0x1, 0x8)
    SetScenarioFlags(0x23, 0)
    NewScene("c1000", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_49_AE11 end

    def Function_50_B2F5(): pass

    label("Function_50_B2F5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch46500.itc", 0x1E)
    LoadChrToIndex("apl/ch51270.itc", 0x1F)
    LoadChrToIndex("apl/ch51271.itc", 0x20)
    LoadChrToIndex("chr/ch30850.itc", 0x21)
    LoadChrToIndex("chr/ch31750.itc", 0x22)
    LoadChrToIndex("chr/ch23900.itc", 0x23)
    SoundLoad(849)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu13900.itp")
    OP_68(960, 2000, 7700, 0)
    MoveCamera(37, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16940, 0)
    SetChrPos(0x101, 2450, 0, 12000, 180)
    SetChrPos(0x102, 1250, 0, 12000, 180)
    SetChrPos(0x104, 2260, 0, 13650, 180)
    SetChrPos(0x109, 3460, 0, 13650, 180)
    SetChrPos(0x105, 1060, 0, 13650, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_B3E5():
        OP_95(0xFE, 2450, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B3E5)
    Sleep(10)

    def lambda_B402():
        OP_95(0xFE, 1250, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B402)
    Sleep(20)

    def lambda_B41F():
        OP_95(0xFE, 2260, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B41F)
    Sleep(10)

    def lambda_B43C():
        OP_95(0xFE, 3460, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B43C)
    Sleep(20)

    def lambda_B459():
        OP_95(0xFE, 1060, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B459)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x18, 0x1F)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0x18, -9420, 6230, -3210, 90)
    SetChrPos(0xD, 380, 0, -2000, 90)
    SetChrPos(0xE, 3610, 0, -2000, 270)
    StopBGM(0xBB8)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)

    #N0391
    NpcTalk(
        0xD,
        "男の声",
        "#4S……んだと、コラァ！\x02",
    )

    CloseMessageWindow()

    #N0392
    NpcTalk(
        0xE,
        "男の声",
        (
            "#4Sアア！？　文句ばっか\x01",
            "言ってんじゃねえよ！\x02",
        )
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
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7517", 0)

    #C0393
    ChrTalk(
        0x101,
        "#00005Fこの声は……\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x102,
        "#00105Fロイド、あれ！\x02",
    )

    CloseMessageWindow()
    OP_68(850, 2000, -2600, 3000)
    MoveCamera(39, 25, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(16810, 3000)
    OP_6F(0x79)

    #C0395
    ChrTalk(
        0xD,
        (
            "#6Pてめえ、スラッシュ……\x01",
            "マジメに考えてんのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xD,
        (
            "#6Pあのままヴァルドさんが酒に溺れて\x01",
            "体でも壊したらどうすんだ、ア！？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xE,
        (
            "だから、オレはそうならないように\x01",
            "色々とアイデアを考えてるだろうが！！\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xE,
        (
            "何にも思いつかねえからって\x01",
            "カリカリすんなっつーの！\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xD,
        (
            "#6Pさっき『タワーの上で景色でも見れば、\x01",
            "キゲン直るんじゃねーの』とか、\x01",
            "軽く抜かしてやがったあれの事か！？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xD,
        (
            "#6Pヴァルドさんの機嫌が\x01",
            "高い所に上るくらいで直るんだったら\x01",
            "誰も苦労しねえんだよ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xD,
        (
            "#6P#4Sお前みたいなバカと\x01",
            "一緒にすんじゃねえ、バカ！\x01",
            "このバカ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xE, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0xE, 0x21)
    SetChrSubChip(0xE, 0x0)
    OP_0D()

    #C0402
    ChrTalk(
        0xE,
        (
            "#4Sて、てめェ～～～ッ！！\x01",
            "３回も言いやがったな、コラァ！！\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xE,
        (
            "#4S一つもいいアイデアをださねえ\x01",
            "お前なんかの百倍はマシなんだよ！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xD, 0x22)
    SetChrSubChip(0xD, 0x0)
    OP_0D()

    #C0404
    ChrTalk(
        0xD,
        "#6Pんだと……！！\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xD,
        "#6P#4Sやろうってのか、アア！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    #C0406
    ChrTalk(
        0x101,
        "#5P#N#4S#00007Fやめろ、お前たち！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(280, 2000, -1490, 3000)
    MoveCamera(36, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15650, 3000)

    def lambda_B986():
        OP_95(0xFE, 2450, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B986)
    Sleep(10)

    def lambda_B9A3():
        OP_95(0xFE, 1250, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B9A3)
    Sleep(20)

    def lambda_B9C0():
        OP_95(0xFE, 2260, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B9C0)
    Sleep(10)

    def lambda_B9DD():
        OP_95(0xFE, 3460, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B9DD)
    Sleep(20)

    def lambda_B9FA():
        OP_95(0xFE, 1060, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B9FA)
    Sleep(200)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BA3E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BA3E)
    Sleep(10)

    def lambda_BA4E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BA4E)
    WaitChrThread(0x105, 1)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)

    #C0407
    ChrTalk(
        0xE,
        "#12Pて、てめえらは……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x104,
        (
            "#5P#00301Fおいおい、仲間同士で\x01",
            "武器まで持ち出すなんて、\x01",
            "らしくねえんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xD,
        (
            "#12Pハッ……\x01",
            "てめえらには関係ねえだろ！\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xD,
        (
            "#12P元はといえば……ワジ！！\x01",
            "てめえがハンパなマネを\x01",
            "やらかしたせいで……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xE,
        (
            "#12Pそうだ……！\x01",
            "ヴァルドさんがあんなことに\x01",
            "なっちまったのはワジのせいだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xE,
        "#12P全部てめえが悪いんだよ、ワジィ！\x02",
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x105,
        "#5P#10303F………………………………\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x109,
        (
            "#5P#10105Fちょ、ちょっと待って！\x01",
            "ワジ君はそんな……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xD,
        (
            "#12Pとにかく、このままじゃ収まらねえ……\x01",
            "まずはてめえらをブチのめしてやる！！\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xE,
        "#12Pヒャハ、そうだなァ！\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xE,
        (
            "#12Pヒューイ、てめえを\x01",
            "のしてやんのはその後だぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x102,
        "#5P#00101F（ど、どうするのロイド……？）\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x104,
        "#5P#00301F（完全に頭に血が上ってやがるぜ？）\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#11P#00010F（くっ、こうなったら\x01",
            "  俺たちで制圧するしか……）\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x3C, 0x1F4)
    Sound(849, 0, 100, 0)
    Sleep(1000)
    OP_63(0xE, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(10)
    OP_63(0xD, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(20)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(10)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #N0421
    NpcTalk(
        0x18,
        "青年の声",
        (
            "フッ……\x01",
            "哀しいことだね。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x7D0)
    OP_68(-7930, 6500, -5030, 6000)
    MoveCamera(41, 31, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(14890, 6000)
    Sleep(500)

    def lambda_BEA8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BEA8)
    Sleep(10)

    def lambda_BEB8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BEB8)
    Sleep(20)

    def lambda_BEC8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BEC8)
    Sleep(10)

    def lambda_BED8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BED8)
    Sleep(20)

    def lambda_BEE8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BEE8)
    Sleep(10)

    def lambda_BEF8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_BEF8)
    Sleep(10)

    def lambda_BF08():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_BF08)
    OP_6F(0x79)
    Sleep(1000)
    Fade(1000)
    OP_68(-9650, 6900, -3210, 0)
    MoveCamera(305, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(13930, 0)
    OP_0D()
    StopBGM(0xFA0)

    #N0422
    NpcTalk(
        0x18,
        "金髪の青年",
        (
            "#5P#13904F争いは何も生み出さない……\x01",
            "愚かな憎しみの連鎖を紡ぐだけさ。\x02\x03",

            "#13902Fそんな君たちに、歌を贈ろう。\x02\x03",

            "混沌とした心を解きほぐし\x01",
            "やがて人々を結びつけるような、\x01",
            "そんな優しくも切ない歌を……\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Fade(500)
    SetChrFlags(0x18, 0x2)
    SetChrFlags(0x18, 0x10)
    SetChrFlags(0x18, 0x20)
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    BeginChrThread(0x18, 0, 0, 51)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x19, 0x23)
    SetChrPos(0x19, -17200, 5400, -6800, 45)
    BeginChrThread(0x19, 0, 0, 52)
    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    Sleep(10)
    PlayBGM("ed7578", 1)
    Sleep(1000)

    #N0423
    NpcTalk(
        0x18,
        "金髪の青年",
        "#70A#50W流れ行く#1500W　#50W星の#1000W　#50W軌跡は……\x05\x02",
    )
    #Auto

    Sleep(7000)

    #N0424
    NpcTalk(
        0x18,
        "金髪の青年",
        "#70A#50W道しるべ#1000W　#50W君へ続く……\x05\x02",
    )
    #Auto

    Sleep(7000)

    #N0425
    NpcTalk(
        0x18,
        "金髪の青年",
        "#70A#50W焦がれれば#1500W　#50W想い#1000W　#50W胸を裂き……\x05\x02",
    )
    #Auto

    Sleep(7000)

    #N0426
    NpcTalk(
        0x18,
        "金髪の青年",
        "#70A#50W苦しさを#1000W　#50W月が笑う……\x05\x02",
    )
    #Auto

    Sleep(7000)

    #N0427
    NpcTalk(
        0x18,
        "金髪の青年",
        "#70A#50W叶うことなどない#3000W　#50Wはかない望みなら……\x05\x02",
    )
    #Auto

    WaitChrThread(0x19, 1)
    Sleep(1000)
    OP_57(0x0)
    OP_5A()
    OP_99(0x19, 0x18, 0xFA, 0x2710, 0x0)
    Sound(809, 0, 30, 0)
    OP_9B(0x1, 0x19, 0xB4, 0x3E8, 0x2710, 0x0)
    Sound(811, 0, 100, 0)
    StopBGM(0x3E8)
    Sleep(500)
    Fade(500)
    EndChrThread(0x18, 0x0)
    ClearChrFlags(0x18, 0x2)
    ClearChrFlags(0x18, 0x10)
    ClearChrFlags(0x18, 0x20)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    SetChrPos(0xD, 1000, 0, -2000, 270)
    SetChrPos(0xE, 2400, 0, -2000, 270)
    OP_0D()
    WaitBGM()
    PlayBGM("ed7518", 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0428
    ChrTalk(
        0x19,
        "#4S……おい、うるせーぞキンパツ！！\x02",
    )

    CloseMessageWindow()

    #N0429
    NpcTalk(
        0x18,
        "金髪の青年",
        "#12P#13911Fむおっ……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(-9170, 6600, -2680, 0)
    MoveCamera(42, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16370, 0)
    OP_0D()
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)
    OP_93(0x18, 0x10E, 0x1F4)
    Sleep(1000)
    OP_64(0x18)

    #N0430
    NpcTalk(
        0x18,
        "金髪の青年",
        (
            "#11P#13909Fど、どうしたんだい、\x01",
            "可愛い仔猫ちゃん。\x02\x03",

            "#13902Fフッ、見ての通り演奏中でね。\x01",
            "悪いがサインなら後でお願いするよ。\x02\x03",

            "#13910Fというか、こんな所で蹴られたら\x01",
            "さすがに危な──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0431
    ChrTalk(
        0x19,
        "#6Pゴチャゴチャいってんじゃねー！\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x19,
        (
            "#6P店の上でメーワクだから、\x01",
            "さっさとおりろ！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_99(0x19, 0x18, 0xFA, 0x2710, 0x0)
    Sound(809, 0, 30, 0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_9B(0x1, 0x19, 0xB4, 0x3E8, 0x2710, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(500)
    OP_93(0x18, 0x13B, 0x0)
    OP_9D(0x18, 0xFFFFD814, 0x1900, 0xFFFFF8B2, 0x15E, 0x7D0)
    Sound(50, 0, 100, 0)
    Sleep(500)
    OP_93(0x18, 0x10E, 0x0)
    OP_9D(0x18, 0xFFFFCFB8, 0x1518, 0xFFFFFCA4, 0xFA, 0xBB8)
    Sound(30, 0, 100, 0)
    Sleep(500)
    OP_93(0x18, 0xB4, 0x1F4)

    #N0433
    NpcTalk(
        0x18,
        "金髪の青年",
        (
            "#13911Fわ、分かった、\x01",
            "分かったからもう──\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x19, 0x10E, 0x1F4)
    OP_9D(0x19, 0xFFFFCFB8, 0x1518, 0xFFFFF4A2, 0xFA, 0xBB8)
    Sound(30, 0, 100, 0)
    OP_93(0x19, 0x0, 0x1F4)
    OP_99(0x19, 0x18, 0xFA, 0x2710, 0x0)
    Sound(809, 0, 30, 0)
    OP_9B(0x1, 0x19, 0xB4, 0x3E8, 0x2710, 0x0)
    Sound(811, 0, 100, 0)
    Sleep(500)

    #C0434
    ChrTalk(
        0x19,
        "#12Pおーりーろー！\x02",
    )

    CloseMessageWindow()

    def lambda_C5A9():
        OP_95(0xFE, -17240, 5400, -1780, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C5A9)
    Sleep(800)
    OP_95(0x19, -16880, 5400, -1950, 4000, 0x0)
    Sleep(1000)
    Sound(1013, 0, 100, 0)

    #N0435
    NpcTalk(
        0x18,
        "青年の声",
        "#2Sわー……！？\x02",
    )

    CloseMessageWindow()
    Sound(833, 0, 40, 0)
    Sound(992, 0, 40, 0)
    Sleep(50)
    Sound(811, 0, 100, 0)

    #C0436
    ChrTalk(
        0x19,
        "#2S……あ、落ちた。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x19,
        "#2S生きてるかー、キンパツー。\x02",
    )

    CloseMessageWindow()

    #N0438
    NpcTalk(
        0x18,
        "青年の声",
        "#2Sきゅう……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x19,
        "#2S……生きてるなー。\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x80)
    OP_64(0x18)
    Sleep(500)
    Fade(1000)
    OP_68(280, 2000, -1490, 0)
    MoveCamera(36, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(15650, 0)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    SetChrFlags(0x9, 0x8000)
    OP_0D()
    Sleep(1000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0xD)
    OP_64(0xE)
    OP_93(0xD, 0x0, 0x1F4)

    #C0440
    ChrTalk(
        0xD,
        "#12Pあー……その、なんだ。\x02",
    )

    CloseMessageWindow()

    def lambda_C78C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C78C)
    Sleep(10)

    def lambda_C79C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C79C)
    Sleep(20)

    def lambda_C7AC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C7AC)
    Sleep(10)

    def lambda_C7BC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C7BC)
    Sleep(20)

    def lambda_C7CC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C7CC)

    #C0441
    ChrTalk(
        0xD,
        "#12Pなんか白けちまったし、帰るわ。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xE,
        "#12P#5Aヒャハッ、なんだよあの金髪……\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_93(0xD, 0x5A, 0x1F4)
    OP_99(0xD, 0xE, 0x1F4, 0x1388, 0x0)
    Sound(811, 0, 60, 0)
    OP_9B(0x1, 0xD, 0xB4, 0xC8, 0x1388, 0x0)

    #C0443
    ChrTalk(
        0xE,
        "#12Pもががっ。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xD,
        "#6P……いいから、帰るぞ。\x02",
    )

    CloseMessageWindow()

    def lambda_C889():
        OP_95(0xFE, 6640, 0, -7350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_C889)
    Sleep(800)

    def lambda_C8A6():
        OP_95(0xFE, 7700, 0, -7010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_C8A6)

    def lambda_C8C0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C8C0)
    Sleep(50)

    def lambda_C8D0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C8D0)
    Sleep(50)

    def lambda_C8E0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C8E0)
    Sleep(50)

    def lambda_C8F0():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C8F0)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    #C0445
    ChrTalk(
        0x101,
        "#5P#00012Fに、逃げた……\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x105,
        (
            "#5P#10306F……ふう、ある意味\x01",
            "助けられちゃったかな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x18, -3400, 0, -6690, 0)

    #N0447
    NpcTalk(
        0x18,
        "青年の声",
        (
            "フ、フッ……\x01",
            "魔都に咲かんとする\x01",
            "争いの芽を摘んでしまった。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_C9C0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C9C0)
    Sleep(50)

    def lambda_C9D0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C9D0)
    Sleep(50)

    def lambda_C9E0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C9E0)
    Sleep(50)

    def lambda_C9F0():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C9F0)
    Sleep(50)

    def lambda_CA00():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CA00)

    #N0448
    NpcTalk(
        0x18,
        "青年の声",
        (
            "愛と真心で平和をもたらす\x01",
            "我がリュートの調べ……\x02",
        )
    )

    CloseMessageWindow()

    #N0449
    NpcTalk(
        0x18,
        "青年の声",
        (
            "自分の才能が\x01",
            "ときどき恐ろしくなるよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(980, 2000, 1730, 0)
    MoveCamera(142, 31, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(16810, 0)
    OP_0D()
    OP_96(0x18, 0xFFFFF132, 0x0, 0xFFFFE624, 0x7D0, 0x0)
    OP_96(0x18, 0xFFFFF772, 0x0, 0xFFFFE570, 0x7D0, 0x0)
    OP_96(0x18, 0xFFFFF646, 0x0, 0xFFFFEC96, 0x7D0, 0x0)

    def lambda_CAF0():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CAF0)
    OP_96(0x18, 0xFFFFFD4E, 0x0, 0xFFFFECB4, 0x3E8, 0x0)

    def lambda_CB11():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CB11)
    OP_96(0x18, 0xFFFFFC68, 0x0, 0xFFFFF330, 0x7D0, 0x0)

    def lambda_CB32():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CB32)
    OP_96(0x18, 0x320, 0x0, 0xFFFFF416, 0x5DC, 0x0)

    def lambda_CB53():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CB53)
    OP_96(0x18, 0x654, 0x0, 0xFFFFFA10, 0x3E8, 0x0)

    def lambda_CB74():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_CB74)
    Sleep(50)

    def lambda_CB84():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_CB84)
    Sleep(50)

    def lambda_CB94():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_CB94)
    Sleep(50)

    def lambda_CBA4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_CBA4)
    Sleep(50)

    def lambda_CBB4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_CBB4)
    OP_93(0x18, 0x0, 0x1F4)
    EndChrThread(0x18, 0x1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0450
    ChrTalk(
        0x102,
        (
            "#6P#00105Fあ、あの……大丈夫ですか？\x01",
            "さっきはなんだか\x01",
            "鈍い音が聞こえましたけど。\x02",
        )
    )

    CloseMessageWindow()

    #N0451
    NpcTalk(
        0x18,
        "金髪の青年",
        (
            "#11P#13904Fフッ、心配はいらないよ、\x01",
            "マドモアゼル。\x02\x03",

            "#13902Fあの程度の高さなど、\x01",
            "今まさに大陸の空を駆けんとする\x01",
            "ボクには恐るるに足らずさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x104,
        "#6P#00306F意味が分からねえ……\x02",
    )

    CloseMessageWindow()

    #N0453
    NpcTalk(
        0x18,
        "金髪の青年",
        (
            "#11P#13903F少しばかりトラブルに\x01",
            "見舞われてしまったが……\x02\x03",

            "#13900F気を取り直して、続きを\x01",
            "披露させていただくとしよう。\x02\x03",

            "#13904Fフッ、存分に楽しんでくれたまえ。\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    #C0454
    ChrTalk(
        0x101,
        "#6P#00011Fけ、結構です！\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x109,
        (
            "#6P#10106F（ロ、ロイドさん。\x01",
            "  もしかしてこの人って……）\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#12P#00001F（ああ、金髪に白いコート……）\x02\x03",

            "#00006F（ミュラーさんは\x01",
            "  厄介な人物だって言ってたけど……\x01",
            "  正直、予想以上だな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        (
            "#6P#00001F……コホン。\x01",
            "あなたは、オリビエさんで\x01",
            "間違いありませんね？\x02",
        )
    )

    CloseMessageWindow()

    #N0458
    NpcTalk(
        0x18,
        "金髪の青年",
        "#11P#13904Fフッ……いかにも。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("金髪の青年")

    #A0459
    AnonymousTalk(
        0xFF,
        (
            "愛を求めて旅をする\x01",
            "不世出の天才にして漂泊の演奏家、\x01",
            "オリビエ・レンハイムだ。\x02",
        )
    )

    CloseMessageWindow()

    #A0460
    AnonymousTalk(
        0x18,
        (
            "フッ、君たちは運がいい。\x01",
            "この天才のゲリラ・リサイタルに\x01",
            "遭遇する事が出来たのだからね。\x02\x03",

            "どうか今日という日をその心に刻み、\x01",
            "一生の思い出としてくれたまえ。\x02",
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
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0461
    ChrTalk(
        0x101,
        "#6P#00006F……は、はあ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x18, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x18)
    OP_63(0x18, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    OP_0D()

    #C0462
    ChrTalk(
        0x18,
        (
            "#11P#13905Fアレッ、そういえば……\x01",
            "なんでその名を知っているんだい？\x02\x03",

            "#13902Fクロスベル入りしてから\x01",
            "名乗った覚えはないつもりだったが。\x01",
            "……どこかでお会いしたかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#6P#00000F俺たちはクロスベル警察、\x01",
            "特務支援課の者です。\x02\x03",

            "ミュラーさんという方の依頼で\x01",
            "あなたを探していました。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x102,
        (
            "#6P#00100Fお知り合いに\x01",
            "間違いありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x18,
        (
            "#11P#13905Fほう、君たちが噂の……\x02\x03",

            "#13904Fフッ……\x01",
            "ミュラーの心配性も相変わらずだな。\x02\x03",

            "#13912Fこの程度の時を\x01",
            "別々に過ごしたところで、\x01",
            "僕らの愛は薄れはしないのに。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x109,
        (
            "#6P#10105Fええっ！\x01",
            "そ、そんな関係なんですか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        "#6P#00306F……いやいや、多分違うだろ。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x101,
        (
            "#6P#00006Fと、とにかく……\x01",
            "ミュラーさんのもとへ\x01",
            "戻っていただけますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x18,
        (
            "#11P#13903F……悪いが、その頼みを\x01",
            "聞くわけにはいかないな。\x02\x03",

            "#13900Fどうせ、明日には忙しくなる。\x01",
            "今のうちにこのクロスベルを\x01",
            "十分に堪能しておきたいしね。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x102,
        "#6P#00105F忙しくなる……？\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x18,
        (
            "#11P#13904Fフッ、こちらの話さ。\x02\x03",

            "もし、キミたちが\x01",
            "ボクを見逃してくれないと\x01",
            "言うのならば……\x02\x03",

            "#13902Fどんな手を使っても\x01",
            "見逃してもらうとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x105,
        (
            "#6P#10302Fへえ……？\x01",
            "一体どうするつもりなんだい？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x18, 0x87, 0x1F4)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0473
    ChrTalk(
        0x18,
        (
            "#12P#13907F#4Sハッ……！\x01",
            "あそこにいるのはユリア准佐ッ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_D6F5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D6F5)
    Sleep(10)

    def lambda_D705():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D705)
    Sleep(20)

    def lambda_D715():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D715)
    Sleep(10)

    def lambda_D725():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D725)
    Sleep(20)

    def lambda_D735():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D735)
    Sleep(500)

    #C0474
    ChrTalk(
        0x101,
        "#00011Fなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x102,
        "#12P#00105Fええっ……！？\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x109,
        "#6P#10107F#4Sど、どこですかっ！？\x02",
    )

    CloseMessageWindow()
    OP_68(8520, 2000, -12850, 3000)
    MoveCamera(45, 27, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(24500, 3000)
    OP_6F(0x79)

    #C0477
    ChrTalk(
        0x109,
        (
            "#10105Fって、あ、あれ……\x01",
            "誰もいませんけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        "#00005F……はっ！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(1000)
    OP_68(1810, 1560, 4120, 0)
    MoveCamera(49, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21950, 0)
    SetChrPos(0x18, 1900, 0, 8440, 180)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(500)

    def lambda_D8EC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8EC)
    Sleep(10)

    def lambda_D8FC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_D8FC)
    Sleep(20)

    def lambda_D90C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_D90C)
    Sleep(10)

    def lambda_D91C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_D91C)
    Sleep(20)

    def lambda_D92C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_D92C)
    Sleep(500)

    #C0479
    ChrTalk(
        0x18,
        (
            "#5P#13902Fフッ、また会える日を\x01",
            "楽しみにしているよ！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x18, 0x0, 0x1F4)

    def lambda_D993():
        OP_95(0xFE, 1900, 0, 20650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_D993)
    Sleep(500)

    #C0480
    ChrTalk(
        0x101,
        "#12P#00011Fちょ、ちょっと……！\x02",
    )

    CloseMessageWindow()
    OP_68(1070, 1560, 2280, 3000)
    SetCameraDistance(17880, 3000)
    WaitChrThread(0x18, 1)
    OP_64(0x18)
    SetChrFlags(0x18, 0x80)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7101", 0)

    #C0481
    ChrTalk(
        0x102,
        "#12P#00106Fに、逃げられてしまったわね……\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x109,
        (
            "#11P#10101Fあんな古典的な手に\x01",
            "ひっかかるなんて……\x02\x03",

            "#10106Fあのユリア准佐が\x01",
            "こんなところに\x01",
            "いるわけないんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        (
            "#5P#00306Fやれやれ、レクターとは\x01",
            "別の意味で厄介そうな兄さんだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        (
            "#12P#00000Fと、とにかく\x01",
            "追いかけてみるか。\x02\x03",

            "#00003Fと言っても、\x01",
            "どこに行ったんだろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x105,
        (
            "#6P#10303Fやっぱり、さっき言ってた場所を\x01",
            "一通りあたってみるのが\x01",
            "いいかもしれないね。\x02\x03",

            "#10300F旧市街で見つけたから、\x01",
            "他に候補が挙げられるとしたら……\x01",
            "裏通りか港湾区、かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x109,
        "#11P#10100Fとにかく、探してみましょう！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 2029, 0, 250, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    ClearChrFlags(0x9, 0x8000)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x156, 2)
    OP_29(0x76, 0x1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_50_B2F5 end

    def Function_51_DCEF(): pass

    label("Function_51_DCEF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD3E")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    Jump("Function_51_DCEF")

    label("loc_DD3E")

    Return()

    # Function_51_DCEF end

    def Function_52_DD3F(): pass

    label("Function_52_DD3F")

    Sleep(23000)
    OP_95(0xFE, -12870, 5400, -2670, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(4000)
    OP_9D(0xFE, 0xFFFFD4AE, 0x1900, 0xFFFFF466, 0x4B0, 0xBB8)
    Sound(50, 0, 100, 0)
    Return()

    # Function_52_DD3F end

    def Function_53_DD7E(): pass

    label("Function_53_DD7E")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0487
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x321, 0x0)"), scpexpr(EXPR_END)), "loc_DE93")
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0488
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "メゾン・イメルダの鍵を使いますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DE8E")
    OP_5A()
    Sleep(500)
    Sound(806, 0, 100, 0)
    Sleep(1000)

    #A0489
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『メゾン・イメルダ』の鍵を開けた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_29(0x67, 0x1, 0x1)
    SetScenarioFlags(0x133, 1)
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x1, 0x1)

    label("loc_DE8E")

    Jump("loc_E02B")

    label("loc_DE93")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DFA7")

    #C0490
    ChrTalk(
        0x101,
        "#00000F……鍵がかかってるみたいだ。\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x102,
        (
            "#00105Fこのアパートに魔獣退治の\x01",
            "支援要請が入っていたわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x101,
        (
            "#00003F確か、管理人は\x01",
            "アンティークショップの店主\x01",
            "『イメルダ夫人』だったな。\x02\x03",

            "#00000F裏通りにある\x01",
            "アンティークショップに\x01",
            "鍵を借りにいこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_E02B")

    label("loc_DFA7")


    #C0493
    ChrTalk(
        0x101,
        (
            "#00000Fこのアパートには\x01",
            "魔獣退治の支援要請が\x01",
            "入っていたはずだ。\x02\x03",

            "#00000F裏通りにある\x01",
            "アンティークショップに\x01",
            "鍵を借りにいこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_E02B")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_53_DD7E end

    SaveToFile()

Try(main)
