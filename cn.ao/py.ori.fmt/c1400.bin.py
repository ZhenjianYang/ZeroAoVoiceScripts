from ScenarioHelper import *

def main():
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
        "迪诺",                   # 1
        "帕欧拉婆婆",             # 2
        "王",                     # 3
        "露茜",                   # 4
        "卡农",                   # 5
        "修伊",                   # 6
        "斯拉修",                 # 7
        "琴兹",                   # 8
        "贝赛",                   # 9
        "阿巴斯",                 # 10
        "莉丝修女",               # 11
        "巴克斯",                 # 12
        "利玛",                   # 13
        "梅尔斯",                 # 14
        "警官",                   # 15
        "瓦鲁多",                 # 16
        "奥利维尔",               # 17
        "金格",                   # 18
        "bc1400",                 # 19
        "中央广场",               # 20
        "西街",                   # 21
        "行政区",                 # 22
        "住宅街",                 # 23
        "欢乐街",                 # 24
        "东街",                   # 25
        "旧城区",                 # 26
        "港湾区",                 # 27
        "ＩＢＣ",                 # 28
        "站前街道",               # 29
        "后巷",                   # 30
        "乌尔斯拉间道",           # 31
        "东克洛斯贝尔街道",       # 32
        "西克洛斯贝尔街道",       # 33
        "玛因兹山道",             # 34
        "兰花塔",                 # 35
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

    PlaceName(-110.69000244140625, 0.0, 106.94999694824219, 0x0000, 0x0000, "中央广场")
    PlaceName(-186.3000030517578, 0.0, 112.12999725341797, 0x0000, 0x0000, "西街")
    PlaceName(-79.63999938964844, 0.0, 209.3000030517578, 0x0000, 0x0000, "行政区")
    PlaceName(-256.45001220703125, 0.0, 197.8000030517578, 0x0000, 0x0000, "住宅街")
    PlaceName(-172.5, 0.0, 188.60000610351562, 0x0000, 0x0000, "欢乐街")
    PlaceName(-17.25, 0.0, 80.5, 0x0000, 0x0000, "东街")
    PlaceName(23.579999923706055, 0.0, 17.25, 0x0000, 0x0000, "旧城区")
    PlaceName(14.949999809265137, 0.0, 156.39999389648438, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.949999809265137, 0.0, 264.5, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-97.75, 0.0, 27.600000381469727, 0x0000, 0x0000, "站前街道")
    PlaceName(-151.8000030517578, 0.0, 147.1999969482422, 0x0000, 0x0000, "后巷")
    PlaceName(-101.19999694824219, 0.0, -8.050000190734863, 0x0000, 0x0000, "乌尔斯拉间道")
    PlaceName(44.849998474121094, 0.0, 96.5999984741211, 0x0000, 0x0000, "东克洛斯贝尔街道")
    PlaceName(-244.9499969482422, 0.0, 110.4000015258789, 0x0000, 0x0000, "西克洛斯贝尔街道")
    PlaceName(-238.0500030517578, 0.0, 225.39999389648438, 0x0000, 0x0000, "玛因兹山道")
    PlaceName(-88.0, 0.0, 360.0, 0x0000, 0x0000, "兰花塔")
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
        "Function_7_1486",         # 07, 7
        "Function_8_19E1",         # 08, 8
        "Function_9_1F1D",         # 09, 9
        "Function_10_2368",        # 0A, 10
        "Function_11_265C",        # 0B, 11
        "Function_12_2EC7",        # 0C, 12
        "Function_13_2F2E",        # 0D, 13
        "Function_14_2FC5",        # 0E, 14
        "Function_15_2FCC",        # 0F, 15
        "Function_16_2FD6",        # 10, 16
        "Function_17_342F",        # 11, 17
        "Function_18_350D",        # 12, 18
        "Function_19_360D",        # 13, 19
        "Function_20_36B8",        # 14, 20
        "Function_21_3758",        # 15, 21
        "Function_22_3795",        # 16, 22
        "Function_23_37D3",        # 17, 23
        "Function_24_3853",        # 18, 24
        "Function_25_3895",        # 19, 25
        "Function_26_4049",        # 1A, 26
        "Function_27_40EE",        # 1B, 27
        "Function_28_40EF",        # 1C, 28
        "Function_29_455B",        # 1D, 29
        "Function_30_45CE",        # 1E, 30
        "Function_31_4641",        # 1F, 31
        "Function_32_46B4",        # 20, 32
        "Function_33_4727",        # 21, 33
        "Function_34_59EF",        # 22, 34
        "Function_35_609B",        # 23, 35
        "Function_36_6138",        # 24, 36
        "Function_37_6179",        # 25, 37
        "Function_38_69B8",        # 26, 38
        "Function_39_6A24",        # 27, 39
        "Function_40_6A90",        # 28, 40
        "Function_41_6AFC",        # 29, 41
        "Function_42_6B39",        # 2A, 42
        "Function_43_6B76",        # 2B, 43
        "Function_44_6BB3",        # 2C, 44
        "Function_45_7058",        # 2D, 45
        "Function_46_804A",        # 2E, 46
        "Function_47_9047",        # 2F, 47
        "Function_48_96C2",        # 30, 48
        "Function_49_9E19",        # 31, 49
        "Function_50_A2E5",        # 32, 50
        "Function_51_CA05",        # 33, 51
        "Function_52_CA55",        # 34, 52
        "Function_53_CA94",        # 35, 53
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_143D")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('珊瑚戒指', 1)"), scpexpr(EXPR_END)), "loc_13CE")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1438")

    label("loc_13CE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1438")

    Jump("loc_147A")

    label("loc_143D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)

    label("loc_147A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_134B end

    def Function_7_1486(): pass

    label("Function_7_1486")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14A6")
    Call(0, 48)
    Return()

    label("loc_14A6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1674")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18D, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1607")

    #C0004
    ChrTalk(
        0xFE,
        "啊，你们是特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x102,
        (
            "#00108F迪诺……\x01",
            "请问，其他成员现在……\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "嗯？啊……\x01",
            "伤情最重的寇奇前辈\x01",
            "也总算苏醒过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "至于其他前辈，也有几位已经出院，\x01",
            "回到了旧城区。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "虽然他们肯定不会\x01",
            "马上返回组织……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "不过，只要我一直在这里等，\x01",
            "他们总有一天会露面的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x102,
        "#00108F迪诺……\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0x101,
        "#00003F嗯……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x18D, 2)
    Jump("loc_166F")

    label("loc_1607")


    #C0012
    ChrTalk(
        0xFE,
        (
            "话说回来……\x01",
            "从一大早开始，市区那边就很吵闹啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "听说一直在讨论什么独立，\x01",
            "真希望他们能安静些。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_166F")

    Jump("loc_19DD")

    label("loc_1674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1682")
    Jump("loc_19DD")

    label("loc_1682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1690")
    Jump("loc_19DD")

    label("loc_1690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_169E")
    Jump("loc_19DD")

    label("loc_169E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_16AC")
    Jump("loc_19DD")

    label("loc_16AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_16BA")
    Jump("loc_19DD")

    label("loc_16BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_16C8")
    Jump("loc_19DD")

    label("loc_16C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_16D6")
    Jump("loc_19DD")

    label("loc_16D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_16E4")
    Jump("loc_19DD")

    label("loc_16E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1970")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1908")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18AD")

    #C0014
    ChrTalk(
        0xFE,
        "啊，你们是特别任务支援科的……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "那、那个……瓦吉，\x01",
            "听说你跟瓦鲁多大哥\x01",
            "一对一单挑……\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x105,
        (
            "#10303F……我可以回答你的问题，\x01",
            "但你真的想从我的口中听到那个答案吗？\x02",
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
        "不、不了，我什么都没问……！\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "瓦鲁多大哥是最强的，\x01",
            "我绝不会相信流言的！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#00303F（哦？这小子是打从心底\x01",
            "  敬爱着瓦鲁多那家伙啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00003F（是啊，对他来说，\x01",
            "  瓦鲁多就像英雄一样吧。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 6)
    Jump("loc_1903")

    label("loc_18AD")


    #C0021
    ChrTalk(
        0xFE,
        (
            "……无论什么时候，\x01",
            "瓦鲁多大哥都是最强的。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "没、没错！我怎么可以\x01",
            "不相信他呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1903")

    Jump("loc_196B")

    label("loc_1908")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1917")
    Jump("loc_196B")

    label("loc_1917")


    #C0023
    ChrTalk(
        0xFE,
        (
            "……真是的，\x01",
            "我不是已经把问诊表\x01",
            "交给你们了吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "赶快拿着\x01",
            "那东西\x01",
            "滚开吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_196B")

    Jump("loc_19DD")

    label("loc_1970")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_197E")
    Jump("loc_19DD")

    label("loc_197E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_19DD")

    #C0025
    ChrTalk(
        0xFE,
        (
            "……听懂了\x01",
            "就赶快滚吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "如果被瓦鲁多大哥发现了，\x01",
            "我可不知道会发生什么事啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19DD")

    TalkEnd(0xFE)
    Return()

    # Function_7_1486 end

    def Function_8_19E1(): pass

    label("Function_8_19E1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1A4B")

    #C0027
    ChrTalk(
        0xFE,
        (
            "虽然不了解详情，\x01",
            "但似乎发生了\x01",
            "相当严重的事态啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "看来暂时还是别出家门\x01",
            "为好呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F19")

    label("loc_1A4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1A59")
    Jump("loc_1F19")

    label("loc_1A59")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1ABA")

    #C0029
    ChrTalk(
        0xFE,
        (
            "听说玛因兹镇那边\x01",
            "发生了一场\x01",
            "大骚乱……\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "据说还有人受伤了……\x01",
            "真让人悲痛。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F19")

    label("loc_1ABA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1AC8")
    Jump("loc_1F19")

    label("loc_1AC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_1B26")

    #C0031
    ChrTalk(
        0xFE,
        (
            "说起来，今天没看到平时\x01",
            "那群小孩子呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "呵呵，他们是去\x01",
            "别的地方玩了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F19")

    label("loc_1B26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1B9E")

    #C0033
    ChrTalk(
        0xFE,
        (
            "听说在近期内，将会举行一场\x01",
            "调查独立意向的居民投票活动。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "虽然我搞不太懂，\x01",
            "但还是得好好思考一下。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F19")

    label("loc_1B9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1C93")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C36")

    #C0035
    ChrTalk(
        0xFE,
        (
            "最近有好多让人震惊的\x01",
            "大新闻啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "老实说，很多事情\x01",
            "我实在是搞不懂……\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "不管怎么说，希望大家\x01",
            "不要就此失去笑容啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1C8E")

    label("loc_1C36")


    #C0038
    ChrTalk(
        0xFE,
        (
            "老实说，我搞不懂\x01",
            "那些复杂的事情……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "不管怎么说，希望大家\x01",
            "不要就此失去笑容啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C8E")

    Jump("loc_1F19")

    label("loc_1C93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1CEE")

    #C0040
    ChrTalk(
        0xFE,
        "呵呵，今天也是个好天气呢。\x02",
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        (
            "孩子们也都很精神，\x01",
            "暖洋洋的感觉真幸福。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F19")

    label("loc_1CEE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x156, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D73")

    #C0042
    ChrTalk(
        0xFE,
        (
            "站在克洛斯贝尔市的\x01",
            "任何地方，大概都能看见\x01",
            "那座新市政厅大楼吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "呵呵，如果靠近了看，\x01",
            "该有多壮观呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1DEC")

    label("loc_1D73")


    #C0044
    ChrTalk(
        0xFE,
        (
            "刚才那个穿着白色大衣的人\x01",
            "是旅行音乐家吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "我的耳朵不大好，\x01",
            "听得不是很清楚，\x01",
            "呵呵，但那曲调还真是令人心情愉快。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DEC")

    Jump("loc_1F19")

    label("loc_1DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1EB9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5A")

    #C0046
    ChrTalk(
        0xFE,
        (
            "以前好像没见过\x01",
            "那位修女……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "呵呵，她可真擅长\x01",
            "和小朋友们打成一片啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EB4")

    label("loc_1E5A")


    #C0048
    ChrTalk(
        0xFE,
        (
            "那位修女真擅长\x01",
            "和小朋友们打成一片啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "呵呵，光是在一旁看着，\x01",
            "都觉得心里很温暖。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EB4")

    Jump("loc_1F19")

    label("loc_1EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1EC7")
    Jump("loc_1F19")

    label("loc_1EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1F19")

    #C0050
    ChrTalk(
        0xFE,
        (
            "呵呵，今天也暖洋洋的，\x01",
            "真是个好天气。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        "让我都迷迷糊糊地犯困了。\x02",
    )

    CloseMessageWindow()

    label("loc_1F19")

    TalkEnd(0xFE)
    Return()

    # Function_8_19E1 end

    def Function_9_1F1D(): pass

    label("Function_9_1F1D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F6E")

    #C0052
    ChrTalk(
        0xFE,
        (
            "嘿嘿，大街那边\x01",
            "很吵闹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "有人说，也许要\x01",
            "发生战争了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2364")

    label("loc_1F6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2037")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1FCC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F96")
    Call(0, 18)
    Jump("loc_1FC7")

    label("loc_1F96")


    #C0054
    ChrTalk(
        0xFE,
        (
            "哈哈哈，那个臭老爸～\x01",
            "看起来就像个正派人士。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FC7")

    Jump("loc_2032")

    label("loc_1FCC")


    #C0055
    ChrTalk(
        0xFE,
        (
            "嘿嘿，今天的赈济食物\x01",
            "也十分美味呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "如果每天都能吃到那么美味的东西，\x01",
            "一直重建下去也不错啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2032")

    Jump("loc_2364")

    label("loc_2037")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2093")

    #C0057
    ChrTalk(
        0xFE,
        (
            "不知为何，大人们今天\x01",
            "全都吵吵闹闹的～\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "嘻嘻，但我老爸\x01",
            "却还是老样子～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2364")

    label("loc_2093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_20C1")

    #C0059
    ChrTalk(
        0xFE,
        "哈哈，这可是天然的淋浴啊！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2364")

    label("loc_20C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_20CF")
    Jump("loc_2364")

    label("loc_20CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20DD")
    Jump("loc_2364")

    label("loc_20DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2133")

    #C0060
    ChrTalk(
        0xFE,
        (
            "哈哈～！\x01",
            "拿到钱啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "嘻嘻嘻……露茜，\x01",
            "咱们今天去吃肉哦，吃肉！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2364")

    label("loc_2133")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_21A5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_216F")

    #C0062
    ChrTalk(
        0xFE,
        (
            "让开让开～\x01",
            "王大人要过去～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_21A0")

    label("loc_216F")


    #C0063
    ChrTalk(
        0xFE,
        (
            "哈哈，那个臭老爸，\x01",
            "现在大概正喝着那东西呢！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A0")

    Jump("loc_2364")

    label("loc_21A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_21B3")
    Jump("loc_2364")

    label("loc_21B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_21C4")
    Call(0, 16)
    Jump("loc_2364")

    label("loc_21C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_221F")

    #C0064
    ChrTalk(
        0xFE,
        (
            "哇～！话说回来，\x01",
            "刚才的压迫感可真是可怕啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        "连我都流了一身冷汗！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2364")

    label("loc_221F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2276")

    #C0066
    ChrTalk(
        0xFE,
        "雨一直下个不停～\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "如果这全都是果汁的话，\x01",
            "倒是可以用来填填肚子～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2364")

    label("loc_2276")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2364")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2312")

    #C0068
    ChrTalk(
        0xFE,
        (
            "啊，我记得你们几个\x01",
            "是警察吧？\x01",
            "不良团伙的大哥哥也在一起啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "难道发生了什么案子吗……？\x01",
            "咦？没猜对吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xFE,
        "啧，真无趣～\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2364")

    label("loc_2312")


    #C0071
    ChrTalk(
        0xFE,
        (
            "不良团伙的大哥哥们\x01",
            "最近都不怎么闹事了～\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0xFE,
        (
            "哈哈，看来是\x01",
            "没什么干劲了吧～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2364")

    TalkEnd(0xFE)
    Return()

    # Function_9_1F1D end

    def Function_10_2368(): pass

    label("Function_10_2368")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2398")

    #C0073
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "那不是很糟糕吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2658")

    label("loc_2398")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_241B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23DF")

    #C0074
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "没想到王的爸爸还\x01",
            "挺靠得住呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2416")

    label("loc_23DF")


    #C0075
    ChrTalk(
        0xFE,
        (
            "傍晚还会分发一次\x01",
            "赈济餐。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0xFE,
        "这次能吃到什么呢？\x02",
    )

    CloseMessageWindow()

    label("loc_2416")

    Jump("loc_2658")

    label("loc_241B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_246A")

    #C0077
    ChrTalk(
        0xFE,
        (
            "听说有个叫玛因兹的地方\x01",
            "出了大事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xFE,
        "到底是什么大事呢？\x02",
    )

    CloseMessageWindow()
    Jump("loc_2658")

    label("loc_246A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_24A1")

    #C0079
    ChrTalk(
        0xFE,
        (
            "嘻嘻……待会找个地方\x01",
            "偷块肥皂好了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2658")

    label("loc_24A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_24AF")
    Jump("loc_2658")

    label("loc_24AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_24BD")
    Jump("loc_2658")

    label("loc_24BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_24EB")

    #C0080
    ChrTalk(
        0xFE,
        "哈哈，今天能吃得饱饱的了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2658")

    label("loc_24EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_255B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2526")

    #C0081
    ChrTalk(
        0xFE,
        "哈哈，露茜大人也要过去～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2556")

    label("loc_2526")


    #C0082
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "王的爸爸现在没准\x01",
            "已经昏过去了呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2556")

    Jump("loc_2658")

    label("loc_255B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2569")
    Jump("loc_2658")

    label("loc_2569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_257A")
    Call(0, 16)
    Jump("loc_2658")

    label("loc_257A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_25CF")

    #C0083
    ChrTalk(
        0xFE,
        (
            "那就是\x01",
            "大家常说的\x01",
            "一对一单挑吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "气势确实很惊人呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2658")

    label("loc_25CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_262B")

    #C0085
    ChrTalk(
        0xFE,
        (
            "但如果喝得太多，\x01",
            "肚子肯定会涨得鼓鼓的。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "就像王的爸爸一样。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2658")

    label("loc_262B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2658")

    #C0087
    ChrTalk(
        0xFE,
        (
            "嘻嘻……\x01",
            "王真是喜欢\x01",
            "看热闹啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2658")

    TalkEnd(0xFE)
    Return()

    # Function_10_2368 end

    def Function_11_265C(): pass

    label("Function_11_265C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2692")

    #C0088
    ChrTalk(
        0xFE,
        (
            "战、战争什么的……\x01",
            "千万不要啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC3")

    label("loc_2692")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27B4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x196, 0)), scpexpr(EXPR_END)), "loc_26F5")

    #C0089
    ChrTalk(
        0xFE,
        (
            "（翻动）……\x01",
            "唔，这个……不行呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xFE,
        (
            "那这个呢……\x01",
            "唔～这个也不行啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AF")

    label("loc_26F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274F")

    #C0091
    ChrTalk(
        0xFE,
        "大哥哥，太谢谢你们了。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0xFE,
        (
            "我会负责\x01",
            "拿这些废弃材料\x01",
            "去换取资金的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_27AF")

    label("loc_274F")


    #C0093
    ChrTalk(
        0xFE,
        (
            "好了，已经\x01",
            "吃得饱饱的了，\x01",
            "得继续努力工作～\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "大哥哥，你们帮了\x01",
            "我这么多，\x01",
            "真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AF")

    Jump("loc_2EC3")

    label("loc_27B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_28BD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2845")

    #C0095
    ChrTalk(
        0xFE,
        (
            "唔……因为昨天下了雨，\x01",
            "石板路的缝隙间有些泥污。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "而且缝隙间还有好多垃圾……\x01",
            "呵呵，在这种时候，就该祭出它了！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_28B8")

    label("loc_2845")


    #C0097
    ChrTalk(
        0xFE,
        (
            "看！这就是我的秘密武器——\x01",
            "『趁手小木棒』哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        (
            "好……用这个就能把塞在\x01",
            "缝隙间的垃圾挑出来了。\x01",
            "非常好用哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28B8")

    Jump("loc_2EC3")

    label("loc_28BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_28CB")
    Jump("loc_2EC3")

    label("loc_28CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_2964")

    #C0099
    ChrTalk(
        0xFE,
        (
            "（扫、扫）……\x01",
            "怎么样？我今天也把\x01",
            "这一带打扫得干干净净。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "呵呵，虽说清扫工作没有尽头，\x01",
            "但每次打扫干净之后的这种成就感真是太棒了。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC3")

    label("loc_2964")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_29BF")

    #C0101
    ChrTalk(
        0xFE,
        (
            "最近都没怎么看见那些\x01",
            "以前常在这附近闹事的人了。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        "呵呵，真是太好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2EC3")

    label("loc_29BF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2AEA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A73")

    #C0103
    ChrTalk(
        0xFE,
        (
            "大概是在上个星期吧，\x01",
            "有个不良团伙的大哥哥把一个东西\x01",
            "贴在自己耳边，一直对着它说话。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        "那到底是什么东西呢？\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x101,
        "#00005F（难道是艾尼格玛吗……？）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2AE5")

    label("loc_2A73")


    #C0106
    ChrTalk(
        0xFE,
        (
            "大概是在上个星期吧，\x01",
            "有个不良团伙的大哥哥把一个东西\x01",
            "贴在自己耳边，一直对着它说话。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        "那到底是什么东西呢？\x02",
    )

    CloseMessageWindow()

    label("loc_2AE5")

    Jump("loc_2EC3")

    label("loc_2AEA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2B3E")

    #C0108
    ChrTalk(
        0xFE,
        (
            "兰花塔\x01",
            "真高啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "听说有２５０亚矩……\x01",
            "那是我身高的多少倍呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2EC3")

    label("loc_2B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2C6E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF9")

    #C0110
    ChrTalk(
        0xFE,
        (
            "听说今天来了很多\x01",
            "外国的记者和\x01",
            "大人物。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0xFE,
        (
            "有人说那些人不可能\x01",
            "来旧城区这种地方，\x01",
            "但这可说不准呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0xFE,
        (
            "（扫、扫）……\x01",
            "我得把这里打扫得\x01",
            "比平时更干净才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_2C69")

    label("loc_2BF9")


    #C0113
    ChrTalk(
        0xFE,
        (
            "听说今天有很多外国的\x01",
            "记者和大人物要来\x01",
            "克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        (
            "（扫、扫）……\x01",
            "我得把这里打扫得\x01",
            "比平时更干净才行。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C69")

    Jump("loc_2EC3")

    label("loc_2C6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2C7F")
    Call(0, 16)
    Jump("loc_2EC3")

    label("loc_2C7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2C8D")
    Jump("loc_2EC3")

    label("loc_2C8D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2EC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x137, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E63")

    #C0115
    ChrTalk(
        0xFE,
        "（扫、扫）……\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "呼……还是老样子，\x01",
            "不管怎么努力清扫，\x01",
            "垃圾也不会彻底消失。\x02",
        )
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x105,
        (
            "#10300F早安，卡农，\x01",
            "今天还好吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xFE, 0x105, 0)

    #C0118
    ChrTalk(
        0xFE,
        "啊，瓦吉，早安。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "这个嘛……今天有很多\x01",
            "瓶子垃圾呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0xFE,
        (
            "虽说乱扔垃圾的行为不可原谅，\x01",
            "但各种各样的瓶子很有意思哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "你看这个，\x01",
            "瓶身中间收缩的\x01",
            "曲线多漂亮啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，确实很漂亮呢。\x02\x03",

            "#10300F不管怎么说，卡农，\x01",
            "你可要小心那些玻璃碎片哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        "嗯，谢谢你的关心。\x02",
    )

    CloseMessageWindow()
    OP_93(0xFE, 0xB4, 0x0)
    ClearChrFlags(0xC, 0x10)
    SetScenarioFlags(0x137, 3)
    Jump("loc_2EC3")

    label("loc_2E63")


    #C0124
    ChrTalk(
        0xFE,
        (
            "各种各样的瓶子\x01",
            "真的很有意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "你看，这一个看起来虽然破旧，\x01",
            "但在光线下却会闪闪发亮哦。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2EC3")

    TalkEnd(0xFE)
    Return()

    # Function_11_265C end

    def Function_12_2EC7(): pass

    label("Function_12_2EC7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F2A")

    #C0126
    ChrTalk(
        0xFE,
        (
            "呼……在第一线工作\x01",
            "果然很耗体力呀。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "不过，这也可以算是\x01",
            "不错的锻炼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F2A")

    label("loc_2F2A")

    TalkEnd(0xFE)
    Return()

    # Function_12_2EC7 end

    def Function_13_2F2E(): pass

    label("Function_13_2F2E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC1")

    #C0128
    ChrTalk(
        0x10,
        (
            "不、不管怎么说……\x01",
            "这栋公寓被破坏得\x01",
            "也太、太夸张了吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x10,
        (
            "幸好是栋废弃公寓，\x01",
            "如、如果里面还有人在……\x01",
            "想想都觉得后怕。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2FC1")

    label("loc_2FC1")

    TalkEnd(0xFE)
    Return()

    # Function_13_2F2E end

    def Function_14_2FC5(): pass

    label("Function_14_2FC5")

    TalkBegin(0xFE)
    TalkEnd(0xFE)
    Return()

    # Function_14_2FC5 end

    def Function_15_2FCC(): pass

    label("Function_15_2FCC")

    TalkBegin(0xFE)
    Call(0, 16)
    TalkEnd(0xFE)
    Return()

    # Function_15_2FCC end

    def Function_16_2FD6(): pass

    label("Function_16_2FD6")

    OP_4B(0x12, 0xFF)
    OP_4B(0xC, 0xFF)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x14C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31AB")

    #C0130
    ChrTalk(
        0x12,
        (
            "#04403F对了，先去找阿娜吧。\x02\x03",

            "既然她是魔女，肯定有办法\x01",
            "帮我找到罗恩的位置。\x02\x03",

            "顺着原路，玛尔克奔向阿娜的小屋。\x01",
            "突然，一阵震耳欲聋的吼声\x01",
            "传到玛尔克的耳中。\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    Sleep(300)

    #C0131
    ChrTalk(
        0xC,
        "(紧张紧张）……然后呢然后呢……？\x02",
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            "喂，还是赶快吃午饭吧。\x01",
            "你不是给我们拿了面包来吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xB,
        (
            "呵呵……\x01",
            "干脆偷偷拿过来吃掉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#00105F（莉丝修女……\x01",
            "  看来她今天被主日学校\x01",
            "  派到这里来授课呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00000F（她在给小朋友们念童话书啊……\x01",
            "  真是温馨的场面。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x14C, 7)
    Jump("loc_341E")

    label("loc_31AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_336A")

    #C0136
    ChrTalk(
        0x12,
        (
            "#04403F玛尔克战战兢兢地顺着\x01",
            "那可怕的吼声走去，只见……\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0xC,
        "嗯嗯……\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            "啧，真是石头脑子。\x01",
            "露茜，在她发面包之前睡一觉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xB,
        "嘻嘻……好吧。\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0x12)

    #C0140
    ChrTalk(
        0x12,
        (
            "#04400F我刚才忘了说，\x01",
            "在今天这堂课的最后，\x01",
            "会让大家写一篇关于本书的感想。\x02\x03",

            "#04400F如果有人什么都写不出来，\x01",
            "就视为没有来上课，\x01",
            "午饭也会被扣除哦。\x02",
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
            "哇哇，真的假的！？\x01",
            "这也太蛮横了吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "今天的修女姐姐还真严厉呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_341E")

    label("loc_336A")


    #C0143
    ChrTalk(
        0x12,
        (
            "#04403F玛尔克战战兢兢地顺着\x01",
            "那可怕的吼声走去，只见……\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xA,
        (
            "哇！等等！从头开始！\x01",
            "从头开始再讲一次吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "嘻嘻……\x01",
            "事到如今才慌起来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xC,
        "呵呵，大家能处得这么好，真开心。\x02",
    )

    CloseMessageWindow()

    label("loc_341E")

    OP_4C(0x12, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_16_2FD6 end

    def Function_17_342F(): pass

    label("Function_17_342F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_34BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3451")
    Call(0, 18)
    Jump("loc_34B9")

    label("loc_3451")


    #C0147
    ChrTalk(
        0xFE,
        (
            "真是的，虽说能领到赈济食物，\x01",
            "可居然让我大白天就白干活。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "真希望早点把事情干完，\x01",
            "然后来一杯啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34B9")

    Jump("loc_3509")

    label("loc_34BE")


    #C0149
    ChrTalk(
        0xFE,
        (
            "话说回来，\x01",
            "阳光也太刺眼了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        "对我这种夜行人来说，简直就是折磨啊。\x02",
    )

    CloseMessageWindow()

    label("loc_3509")

    TalkEnd(0xFE)
    Return()

    # Function_17_342F end

    def Function_18_350D(): pass

    label("Function_18_350D")

    OP_4B(0xA, 0xFF)
    OP_4B(0x13, 0xFF)
    TurnDirection(0xA, 0x0, 0)

    #C0151
    ChrTalk(
        0xA,
        (
            "哈哈，那个臭老爸～\x01",
            "居然在大白天就开始工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xA,
        (
            "听说房东对他说，\x01",
            "如果不帮忙重建旧城区，\x01",
            "就要把他赶出公寓呢～！\x02",
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
            "喂，王，\x01",
            "别说些多余的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x13,
        "闭上嘴巴，过来给我帮忙。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    SetScenarioFlags(0x0, 5)
    OP_93(0xA, 0x13B, 0x0)
    OP_93(0x13, 0x13B, 0x0)
    OP_4C(0xA, 0xFF)
    OP_4C(0x13, 0xFF)
    Return()

    # Function_18_350D end

    def Function_19_360D(): pass

    label("Function_19_360D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3663")

    #C0155
    ChrTalk(
        0xFE,
        (
            "好……今天也\x01",
            "干脆利落地搞定工作吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        "首先是测量尺寸……\x02",
    )

    CloseMessageWindow()
    Jump("loc_36B4")

    label("loc_3663")


    #C0157
    ChrTalk(
        0xFE,
        (
            "呼，虽然比别人晚了一点，\x01",
            "但总算可以歇一会了。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0xFE,
        "好……下午也要继续加油！\x02",
    )

    CloseMessageWindow()

    label("loc_36B4")

    TalkEnd(0xFE)
    Return()

    # Function_19_360D end

    def Function_20_36B8(): pass

    label("Function_20_36B8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3701")

    #C0159
    ChrTalk(
        0xFE,
        "爸爸正在为大家努力工作呢。\x02",
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xFE,
        "是不是很帅～¤\x02",
    )

    CloseMessageWindow()
    Jump("loc_3754")

    label("loc_3701")

    SetChrName("利玛")

    #C0161
    ChrTalk(
        0x14,
        "爸爸，这汤好美味啊～\x02",
    )

    CloseMessageWindow()
    SetChrName("梅尔斯")

    #C0162
    ChrTalk(
        0x15,
        (
            "是啊，真的很美味。\x01",
            "爸爸也充满力量了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3754")

    TalkEnd(0xFE)
    Return()

    # Function_20_36B8 end

    def Function_21_3758(): pass

    label("Function_21_3758")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_376D")
    Call(0, 23)
    Jump("loc_3791")

    label("loc_376D")


    #C0163
    ChrTalk(
        0xFE,
        "该怎么说呢，这可真是不得了……\x02",
    )

    CloseMessageWindow()

    label("loc_3791")

    TalkEnd(0xFE)
    Return()

    # Function_21_3758 end

    def Function_22_3795(): pass

    label("Function_22_3795")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37AA")
    Call(0, 23)
    Jump("loc_37CF")

    label("loc_37AA")


    #C0164
    ChrTalk(
        0xFE,
        (
            "真希望瓦鲁多大哥\x01",
            "也来看看啊……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_37CF")

    TalkEnd(0xFE)
    Return()

    # Function_22_3795 end

    def Function_23_37D3(): pass

    label("Function_23_37D3")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0165
    ChrTalk(
        0xD,
        "是叫兰花塔吧？\x02",
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0xD,
        (
            "真是的，还真是建了\x01",
            "一栋不得了的建筑物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xE,
        (
            "哈哈，是啊。\x01",
            "好想去塔顶上玩蹦极啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Return()

    # Function_23_37D3 end

    def Function_24_3853(): pass

    label("Function_24_3853")

    TalkBegin(0xFE)

    #C0168
    ChrTalk(
        0xFE,
        (
            "好……接下来该\x01",
            "巡视旧城区了。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0xFE,
        "……从哪里开始呢？\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_3853 end

    def Function_25_3895(): pass

    label("Function_25_3895")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_38A2")
    Call(0, 26)
    Return()

    label("loc_38A2")

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
        "#11P你们是……\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        (
            "#6P#00000F你好。\x01",
            "上次见面，还是在教团事件那时了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x102,
        (
            "#12P#00100F好久不见，迪诺。\x02\x03",

            "看来你已经\x01",
            "回到剑蛇帮了？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x8,
        "#11P嗯、嗯……是啊。\x02",
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x8,
        (
            "#11P之前跟瓦鲁多大哥他们打架的事……\x01",
            "因为是受了药物的影响，\x01",
            "他们已经原谅我了……\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x8,
        (
            "#11P……但还是挨了\x01",
            "一顿棍棒才算了事。\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x109,
        "#6P#10106F棍、棍棒吗……\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x105,
        (
            "#6P#10300F呵呵，不管怎么说，\x01",
            "能成功归队就好啦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0178
    ChrTalk(
        0x8,
        (
            "#11P瓦吉……\x01",
            "你还真的加入了\x01",
            "警察组织啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x8,
        "#11P都是因为你，瓦鲁多大哥他……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0180
    ChrTalk(
        0x101,
        (
            "#6P#00005F瓦鲁多……？\x01",
            "他怎么了？\x02",
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
            "#11P……教团事件时\x01",
            "受过你们的关照，\x01",
            "所以我就给你们一个忠告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x8,
        (
            "#11P瓦鲁多大哥最近的\x01",
            "心情简直糟到了极点。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x8,
        (
            "#11P如果还想留住自己的小命，\x01",
            "就别随便靠近这里。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        (
            "#12P#00105F心情糟到了极点……？\x01",
            "发生什么事情了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x8,
        "#11P……全都是因为瓦吉。\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "#11P那起事件结束之后，\x01",
            "圣书会的家伙们\x01",
            "变得安分了起来……\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x8,
        (
            "#11P接下来又轮到圣书会的首领瓦吉……\x01",
            "连声招呼都没打，\x01",
            "突然就去当警察的走狗了。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#6P#00003F……原来如此。\x02\x03",

            "#00001F也就是说，\x01",
            "因为没有了竞争对手，\x01",
            "所以情绪很焦躁吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x109,
        "#6P#10106F也不是不能理解他的心情……\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x105,
        "#6P#10308F……真是的。\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0x8,
        (
            "#11P还、还敢说什么『真是的』！！\x01",
            "你知道自己干了什么吗……！\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x8,
        (
            "#11P都怪你，瓦鲁多大哥\x01",
            "最近已经很少\x01",
            "在鬼火露面了！\x02",
        )
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x105,
        (
            "#6P#10303F……如果他想那样，\x01",
            "就随便他好了。\x02\x03",

            "#10300F呵呵，我也只是在做\x01",
            "自己想做的事。\x02\x03",

            "关于这一点，我可不想\x01",
            "被你们指指点点呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x8,
        "#11P唔……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xFFFF)

    #C0195
    ChrTalk(
        0x8,
        (
            "#11P……哼，既然如此，\x01",
            "你们就快滚吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x8,
        (
            "#11P如果被瓦鲁多大哥发现了，\x01",
            "不光是瓦吉，说不定连你们也\x01",
            "不会有什么好果子吃。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        (
            "#6P#00003F……看来今天还是\x01",
            "乖乖离开比较好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x102,
        (
            "#12P#00108F……是啊。\x02\x03",

            "#00100F那就再见了，迪诺。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x8,
        "#11P哼……！\x02",
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

    # Function_25_3895 end

    def Function_26_4049(): pass

    label("Function_26_4049")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_END)), "loc_40ED")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40B6")

    #C0201
    ChrTalk(
        0x101,
        (
            "#00008F……暂时还是不要\x01",
            "进入这里了。\x02",
        )
    )

    CloseMessageWindow()

    #C0202
    ChrTalk(
        0x105,
        (
            "#10303F嗯……\x01",
            "这样决定再好不过。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_40D7")

    label("loc_40B6")


    #C0203
    ChrTalk(
        0x101,
        "#00003F……还是别进鬼火了。\x02",
    )

    CloseMessageWindow()

    label("loc_40D7")

    Sleep(50)
    SetChrPos(0x0, 44540, -2500, -22490, 270)
    EventEnd(0x4)

    label("loc_40ED")

    Return()

    # Function_26_4049 end

    def Function_27_40EE(): pass

    label("Function_27_40EE")

    Return()

    # Function_27_40EE end

    def Function_28_40EF(): pass

    label("Function_28_40EF")

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
            "#12P#10108F交换店纳因瓦利……\x02\x03",

            "#10106F那位女老板的压迫感真是相当强，\x01",
            "把话题完全避开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x102,
        (
            "#00103F#5P没办法，从事那个行业的人\x01",
            "也有他们独有的道义规矩。\x02\x03",

            "#00100F能得到那么多情报，\x01",
            "我们就该感谢她了。\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x101,
        (
            "#11P#00006F是啊……\x02\x03",

            "#00008F……话说回来，\x01",
            "像食人虎一般的男人吗？\x02\x03",

            "#00001F如果不是恐怖分子，\x01",
            "那就很可能是猎兵了……\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x105,
        (
            "#6P#10303F但如果他是猎兵，\x01",
            "只身一人出现在那里就有点奇怪了。\x02\x03",

            "#10300F既然如此，就把这一点\x01",
            "也一并报告给科长吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4498")

    #C0208
    ChrTalk(
        0x101,
        (
            "#11P#00001F嗯，赞成。\x02\x03",

            "#00003F（如果跟猎兵有关，说不定\x01",
            "  兰迪会知道些什么……）\x02\x03",

            "#00000F（算了，反正支援请求也都解决了，\x01",
            "  先回一趟支援科吧……？）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4525")

    label("loc_4498")


    #C0209
    ChrTalk(
        0x101,
        (
            "#11P#00001F嗯，赞成。\x02\x03",

            "#00003F（如果跟猎兵有关，说不定\x01",
            "  兰迪会知道些什么……）\x02\x03",

            "#00000F（算了，还是赶紧把剩下的\x01",
            "  支援请求解决掉吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4525")

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

    # Function_28_40EF end

    def Function_29_455B(): pass

    label("Function_29_455B")


    def lambda_4560():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4560)

    def lambda_457A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_457A)
    WaitChrThread(0xFE, 1)

    def lambda_458F():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_458F)
    WaitChrThread(0xFE, 1)

    def lambda_45AD():
        OP_95(0xFE, -6500, 0, -9600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45AD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xFA, 0x1F4)
    Return()

    # Function_29_455B end

    def Function_30_45CE(): pass

    label("Function_30_45CE")


    def lambda_45D3():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45D3)

    def lambda_45ED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_45ED)
    WaitChrThread(0xFE, 1)

    def lambda_4602():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4602)
    WaitChrThread(0xFE, 1)

    def lambda_4620():
        OP_95(0xFE, -7700, 0, -9000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4620)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xC8, 0x1F4)
    Return()

    # Function_30_45CE end

    def Function_31_4641(): pass

    label("Function_31_4641")


    def lambda_4646():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4646)

    def lambda_4660():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4660)
    WaitChrThread(0xFE, 1)

    def lambda_4675():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4675)
    WaitChrThread(0xFE, 1)

    def lambda_4693():
        OP_95(0xFE, -7500, 0, -11200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4693)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x14, 0x1F4)
    Return()

    # Function_31_4641 end

    def Function_32_46B4(): pass

    label("Function_32_46B4")


    def lambda_46B9():
        OP_95(0xFE, -13000, 0, -10500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46B9)

    def lambda_46D3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_46D3)
    WaitChrThread(0xFE, 1)

    def lambda_46E8():
        OP_95(0xFE, -10000, 0, -11500, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_46E8)
    WaitChrThread(0xFE, 1)

    def lambda_4706():
        OP_95(0xFE, -8700, 0, -10600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4706)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x46, 0x1F4)
    Return()

    # Function_32_46B4 end

    def Function_33_4727(): pass

    label("Function_33_4727")

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

    def lambda_48A3():
        OP_97(0x101, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_48A3)
    Sleep(100)

    def lambda_48C0():
        OP_97(0x102, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_48C0)
    Sleep(100)

    def lambda_48DD():
        OP_97(0x109, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_48DD)
    Sleep(100)

    def lambda_48FA():
        OP_97(0x105, 0x0, 0x0, 0xFA0, 0x708, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_48FA)
    SetCameraDistance(19000, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 0)
    OP_C9(0x0, 0x80000000)

    #N0210
    NpcTalk(
        0x17,
        "凶恶的声音",
        "#3564V#30W站住，混账。\x02",
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

    def lambda_49E8():
        OP_93(0x105, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_49E8)
    Sleep(50)

    def lambda_49F8():
        OP_93(0x109, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_49F8)
    Sleep(50)

    def lambda_4A08():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4A08)
    Sleep(50)

    def lambda_4A18():
        OP_93(0x101, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A18)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x101, 0)
    Sleep(1000)

    def lambda_4A3B():
        OP_96(0xFE, 0x19DC, 0x0, 0xFFFFDEFE, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4A3B)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    #Sound(3306, 255, 80, 0)    #voice#Lloyd

    #C0211
    ChrTalk(
        0x101,
        "#00005F#30W#6P#N啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0212
    ChrTalk(
        0x105,
        "#10308F#2908V#40W#6P#N瓦鲁多。\x02",
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

    def lambda_4B53():
        OP_96(0xFE, 0x76C, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_4B53)
    OP_0D()
    WaitChrThread(0x17, 1)
    OP_93(0x17, 0x0, 0x1F4)

    #C0213
    ChrTalk(
        0x109,
        "#10105F（请问，这个人是……？）\x02",
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x102,
        (
            "#5P#00108F（他就是统领着名为剑蛇帮的\x01",
            "  团体的首领……）\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x105,
        (
            "#6P#10304F瓦鲁多，怎么了？\x02\x03",

            "#10300F听说你最近一直很少\x01",
            "在剑蛇帮露面呢。\x02",
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
            "#30W……少废话，\x01",
            "我的事不用多说。\x02\x03",

            "比起这些……\x01",
            "听说你这家伙当了警察的走狗啊？\x02\x03",

            "你这算什么意思……嗯？\x02",
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
            "#6P#10306F#30W也没什么意思啊……\x02\x03",

            "#10302F圣书会的各位都没有意见，\x01",
            "我这么做也不会给任何人\x01",
            "带来麻烦吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0218
    ChrTalk(
        0x17,
        (
            "#01601F#30W#11P混账……你是认真的吗？\x02\x03",

            "#01603F你还没跟本大爷……\x01",
            "瓦鲁多·瓦雷斯分出高下，\x01",
            "就想离开团体……\x02\x03",

            "#01607F你觉得我能接受吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0x105,
        "#6P#10308F#30W………………………………………\x02",
    )

    CloseMessageWindow()

    def lambda_4E31():
        OP_96(0xFE, 0x384, 0x0, 0x13EC, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4E31)
    WaitChrThread(0x101, 1)

    #C0220
    ChrTalk(
        0x101,
        "#6P#00011F瓦鲁多，别激动！\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0x102,
        "#00106F该怎么说呢，其实这也是有原因的……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x1F4)

    #C0222
    ChrTalk(
        0x17,
        (
            "#01607F#4S#11P少啰嗦！\x01",
            "外人都给我闭嘴！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0223
    ChrTalk(
        0x17,
        (
            "#01603F#11P瓦吉，我虽然不知道\x01",
            "你去当警察的目的……\x02\x03",

            "#01608F但是……\x02",
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
            "#01607F#11P……你该不会以为，\x01",
            "自己能完好无损地从这个旧城区\x01",
            "走出去吧！？\x02",
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
        "#6P#00001F唔……！\x02",
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0x102,
        "#5P#00106F这、这还真不妙啊……\x02",
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x105,
        "#6P#10303F#30W……瓦鲁多。\x02",
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(1680, 1300, 3250, 1200)

    def lambda_5043():
        OP_95(0xFE, 1900, 0, 4800, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5043)
    Sleep(500)

    def lambda_5060():
        TurnDirection(0xFE, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5060)

    def lambda_506D():
        OP_96(0xFE, 0x2BC, 0x0, 0x13EC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_506D)
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
        "#12P#00011F喂、喂！瓦吉！？\x02",
    )

    CloseMessageWindow()

    #C0230
    ChrTalk(
        0x105,
        (
            "#6P#10308F#30W没关系，交给我吧。\x02\x03",

            "#10306F……我说啊，瓦鲁多，\x01",
            "这不是理所当然的吗？\x02\x03",

            "无论是圣书会，\x01",
            "还是剑蛇帮……\x02\x03",

            "#10301F都不是永久的立足之地，\x01",
            "你应该也明白吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x17, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0231
    ChrTalk(
        0x17,
        "#11P#01605F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x105,
        (
            "#6P#10303F#30W我之所以组建圣书会，\x01",
            "只是为了结成一股能抑制你们\x01",
            "在这旧城区肆意妄为的力量。\x02\x03",

            "#10300F圣书会的各位在一开始还很弱小，\x01",
            "但如今已经成长起来了。\x02\x03",

            "就算我离开，\x01",
            "也能继续与你们对抗。\x02\x03",

            "所以我的任务已经完成了。\x02",
        )
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x17,
        "#11P#01607F#30W……你、你这家伙……\x02",
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x105,
        (
            "#6P#10304F#30W不仅如此……\x01",
            "其他成员迟早也都会\x01",
            "离开团体，走向独立。\x02\x03",

            "从懵懂不知前路的季节毕业，\x01",
            "去寻找只属于自己的道路……\x02\x03",

            "#10302F我相信他们能做到。\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x101,
        "#12P#00005F#30W瓦吉……\x02",
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x102,
        "#5P#00108F#30W瓦吉……\x02",
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
            "#6P#10304F#30W你们剑蛇帮也是一样。\x02\x03",

            "虽然多数成员都很粗暴，但仍然有着\x01",
            "拒绝黑手党邀请的气概与意志。\x02\x03",

            "#10300F所以啊，瓦鲁多……\x01",
            "你一定也能找到自己的道路的。\x02",
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
        "#11P#01604F#60W#10A……呵呵…………\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    #C0240
    ChrTalk(
        0x17,
        "#11P#01609F#2809V#4S#35A#40W哈哈哈哈哈哈哈哈哈哈！！！\x02",
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
            "#01611F#3565V#30W#11P真没想到啊，你居然会说出\x01",
            "这么天真又可笑的话！\x02\x03",

            "#01607F#3566V够了！不用再说下去了！\x02\x03",

            "#3561V你让这个『圣域』蒙上了污点！！\x01",
            "我绝对不能就这么饶了你！！\x02",
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
        "#6P#10303F#40W是吗……\x02",
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
        "#12P#00011F喂！瓦吉！\x02",
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x105,
        (
            "#6P#10303F#30W罗伊德，不要出手。\x02\x03",

            "#10301F这是一对一的对决，必须由\x01",
            "我一个人来做个了断。\x02",
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
            "#11P#01604F#30W呵呵，看来这点事理\x01",
            "你至少还是明白的啊……\x02\x03",

            "#01602F我会把你彻底打垮，\x01",
            "让你趴在地上站不起来……\x02\x03",

            "哼哼，那样一来，\x01",
            "你应该就能稍微清醒一点了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0246
    ChrTalk(
        0x105,
        "#6P#10303F#2909V#30W……闲话到此为止。\x02",
    )

    CloseMessageWindow()
    OP_24(0xB5D)
    OP_57(0x0)
    OP_5A()
    StopBGM(0xBB8)

    #C0247
    ChrTalk(
        0x17,
        "#11P#01601F#3567V啊……？\x02",
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

    def lambda_5818():
        OP_96(0xFE, 0x12C, 0x0, 0x13EC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5818)
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
        "#00005F（这是……！）\x02",
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
            "#5P#10301F#2910V#30W#20A瓦鲁多─#1600W─\x01",
            "#40W这次我会全力以赴。\x02",
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

    # Function_33_4727 end

    def Function_34_59EF(): pass

    label("Function_34_59EF")

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

    def lambda_5B53():
        OP_95(0xFE, 1900, 0, 2600, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5B53)
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

    def lambda_5BF3():
        OP_9D(0xFE, 0x76C, 0x0, 0xFFFFFE0C, 0x898, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5BF3)
    Sound(2800, 255, 100, 0)    #voice#Wald
    Sleep(500)
    CancelBlur(0)
    WaitChrThread(0x17, 1)
    Sound(862, 0, 100, 0)
    Sound(833, 0, 30, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x12C)
    SetChrSubChip(0x17, 0x3)

    def lambda_5C43():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x12C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_5C43)
    WaitChrThread(0x17, 1)
    Sound(811, 0, 100, 0)
    OP_82(0x0, 0x64, 0xBB8, 0x64)

    #C0251
    ChrTalk(
        0x17,
        "#01610F#13A#11P呜哇……！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(800)

    def lambda_5C9D():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_5C9D)
    Sleep(1200)

    #C0252
    ChrTalk(
        0x17,
        (
            "#11P#01611F#40W……唔唔……混账……\x02\x03",

            "难道你至今为止……\x01",
            "一直都在……手下留情……？\x02",
        )
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x105,
        (
            "#6P#10306F#30W……虽然和兰迪那招有所不同，\x01",
            "但刚才那也算是有些犯规的技巧。\x02\x03",

            "#10308F不过，面对今天的你，\x01",
            "我也只能毫不留情地拿出全力了。\x02\x03",

            "#10301F这就是……\x01",
            "我所能展现的最后的诚意。\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x17,
        (
            "#11P#01611F#50W唔……\x01",
            "……瓦吉……你……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(300)

    #C0255
    ChrTalk(
        0x105,
        (
            "#11P#10303F#30W再见了，瓦鲁多。\x02\x03",

            "#10300F这两年的时光……\x01",
            "我过得很愉快。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_5E50():

        label("loc_5E50")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5E50")

    QueueWorkItem2(0x101, 2, lambda_5E50)

    def lambda_5E62():

        label("loc_5E62")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5E62")

    QueueWorkItem2(0x102, 2, lambda_5E62)

    def lambda_5E74():

        label("loc_5E74")

        TurnDirection(0xFE, 0x105, 500)
        Yield()
        Jump("loc_5E74")

    QueueWorkItem2(0x109, 2, lambda_5E74)
    OP_68(1900, 1000, 3100, 5000)
    SetCameraDistance(17500, 5000)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)

    def lambda_5EA8():
        OP_95(0xFE, 1900, 0, 20000, 1800, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_5EA8)
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

    def lambda_5F0B():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_5F0B)
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
            "#11P#01611F#3568V#50W#45A别开玩笑了……\x01",
            "……我绝不接受……！\x02",
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
            "#11P#01610F#3569V#50W#65A我怎么能允许……\x01",
            "你一个人离开这里啊！！\x02",
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
        "#11P#01607F#3570V#5S#50W#20A瓦吉……！！！\x02",
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

    # Function_34_59EF end

    def Function_35_609B(): pass

    label("Function_35_609B")

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

    def lambda_60E1():
        OP_9C(0xFE, 0x0, 0x0, 0x0, 0x44C, 0x2BC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_60E1)
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

    # Function_35_609B end

    def Function_36_6138(): pass

    label("Function_36_6138")

    EndChrThread(0xFE, 0x2)

    def lambda_6141():
        OP_95(0xFE, 1900, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6141)
    WaitChrThread(0xFE, 1)

    def lambda_615F():
        OP_95(0xFE, 1900, 0, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_615F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_36_6138 end

    def Function_37_6179(): pass

    label("Function_37_6179")

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

    def lambda_63C3():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_63C3)
    Sleep(100)
    EndChrThread(0x109, 0xFF)
    SetChrPos(0x109, 18500, -2500, -23800, 315)

    def lambda_63F5():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_63F5)
    Sleep(100)
    EndChrThread(0x104, 0xFF)
    SetChrPos(0x104, 20000, -2500, -22300, 315)

    def lambda_6427():
        OP_97(0xFE, 0xFFFFCB44, 0x0, 0x34BC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_6427)
    Fade(500)
    OP_68(16200, 0, -20000, 0)
    MoveCamera(315, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_68(5200, 1000, -9000, 8500)
    MoveCamera(59, 27, 0, 8500)
    SetCameraDistance(19500, 8500)
    WaitChrThread(0x101, 1)

    def lambda_649D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_649D)
    WaitChrThread(0x109, 1)

    def lambda_64AE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_64AE)
    WaitChrThread(0x104, 1)

    def lambda_64BF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_64BF)
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
        "#6P#10308F……怎么样？\x02",
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0x101,
        (
            "#00006F#11P不行……\x01",
            "看来他们全不知情。\x02\x03",

            "#00013F这几天，谁也没有\x01",
            "见过瓦鲁多。\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x104,
        (
            "#00306F#11P看来他彻底疏远了\x01",
            "自己的小弟们……\x02\x03",

            "#00301F他们还反过来质问我，\x01",
            "知不知道瓦鲁多的行踪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x109,
        "#12P#10106F嗯……看来他们也在拼命找他呢。\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x105,
        "#6P#10303F……是吗。\x02",
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x102,
        (
            "#00106F#6P我们去询问了\x01",
            "圣书会的那些孩子……\x02\x03",

            "#00108F最近这段时间，没有任何人\x01",
            "见到过瓦鲁多呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0265
    ChrTalk(
        0x103,
        (
            "#6P#00206F是的……之前倒是有一段时间，\x01",
            "经常有人能看到他烂醉如泥的样子。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x101,
        (
            "#00001F#11P是吗……果然没法看出\x01",
            "他背后的人到底是谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x104,
        (
            "#00303F#11P那个混蛋，到底是从哪里得到\x01",
            "『真知』那种东西的……\x02",
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
            "#12P#10113F……瓦吉，你没事吧？\x02\x03",

            "脸色好像不太好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0x105,
        (
            "#6P#10304F呵呵，可能是因为雨天阴冷吧。\x02\x03",

            "#10300F总之，我已经拜托阿巴斯他们\x01",
            "帮忙收集情报了。\x02\x03",

            "瓦鲁多的事情就先放在一边，\x01",
            "我们回支援科吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x101,
        (
            "#00006F#11P……说的也是，\x01",
            "琪雅大概正在给我们\x01",
            "准备早餐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x102,
        (
            "#00102F#6P呵呵，总觉得最近\x01",
            "让那孩子操了不少心呢。\x02",
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

    # Function_37_6179 end

    def Function_38_69B8(): pass

    label("Function_38_69B8")


    def lambda_69BD():
        OP_95(0xFE, 45000, -2500, -22500, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_69BD)

    def lambda_69D7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_69D7)
    WaitChrThread(0xFE, 1)

    def lambda_69EC():
        OP_95(0xFE, 38500, -2500, -23800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_69EC)
    WaitChrThread(0xFE, 1)

    def lambda_6A0A():
        OP_95(0xFE, 27500, -2500, -23800, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A0A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_69B8 end

    def Function_39_6A24(): pass

    label("Function_39_6A24")


    def lambda_6A29():
        OP_95(0xFE, 45000, -2500, -23300, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A29)

    def lambda_6A43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6A43)
    WaitChrThread(0xFE, 1)

    def lambda_6A58():
        OP_95(0xFE, 38500, -2500, -24600, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A58)
    WaitChrThread(0xFE, 1)

    def lambda_6A76():
        OP_95(0xFE, 27500, -2500, -24600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A76)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_39_6A24 end

    def Function_40_6A90(): pass

    label("Function_40_6A90")


    def lambda_6A95():
        OP_95(0xFE, 45000, -2500, -21700, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6A95)

    def lambda_6AAF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_6AAF)
    WaitChrThread(0xFE, 1)

    def lambda_6AC4():
        OP_95(0xFE, 38500, -2500, -23000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AC4)
    WaitChrThread(0xFE, 1)

    def lambda_6AE2():
        OP_95(0xFE, 27500, -2500, -23000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6AE2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_6A90 end

    def Function_41_6AFC(): pass

    label("Function_41_6AFC")


    def lambda_6B01():
        OP_95(0xFE, -9500, 0, -10400, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B01)
    WaitChrThread(0xFE, 1)

    def lambda_6B1F():
        OP_95(0xFE, -3500, 0, -9000, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B1F)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_6AFC end

    def Function_42_6B39(): pass

    label("Function_42_6B39")


    def lambda_6B3E():
        OP_95(0xFE, -9500, 0, -9800, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B3E)
    WaitChrThread(0xFE, 1)

    def lambda_6B5C():
        OP_95(0xFE, -3500, 0, -8400, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B5C)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_42_6B39 end

    def Function_43_6B76(): pass

    label("Function_43_6B76")


    def lambda_6B7B():
        OP_95(0xFE, -9500, 0, -11000, 2200, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B7B)
    WaitChrThread(0xFE, 1)

    def lambda_6B99():
        OP_95(0xFE, -3500, 0, -9600, 2200, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_6B99)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_43_6B76 end

    def Function_44_6BB3(): pass

    label("Function_44_6BB3")

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
            "#12P#00000F这里就是处理通缉魔兽的委托中\x01",
            "提到的地下空间Ｄ区域的入口吗……\x02\x03",

            "#00003F这里以前堆放着\x01",
            "不少材料，看来是因为\x01",
            "这个委托，已经全都搬开了。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x103,
        (
            "#12P#00203F唔，我有点疑问……\x02\x03",

            "#00200F为什么并未被导力网络\x01",
            "覆盖的旧城区会有\x01",
            "地下空间的入口？\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x104,
        "#12P#00305F啊，如此说来，确实有点奇怪。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x109,
        (
            "#12P#10105F如果没记错，旧城区是在\x01",
            "都市开发中被遗留的区域吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0x102,
        (
            "#12P#00103F是的……\x01",
            "以前和大家说过，Ｄ区域是在议员和\x01",
            "官员们的暗中推动下建造而成的……\x02\x03",

            "#00108F结果使地下工程无休止地扩展推进，\x01",
            "最后甚至扩张到了这种地方。\x02\x03",

            "#00106F据说当时那些议员和官员捏造了很多完全没有\x01",
            "根据的理由，开始了这项毫无计划可言的工程。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x105,
        (
            "#12P#10300F哦……原来如此。\x02\x03",

            "#10304F总之就是腐败政治下的\x01",
            "利益产物吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#12P#00006F嗯，是啊……\x02\x03",

            "#00000F不过，自迪塔先生成为市长之后，\x01",
            "这方面似乎已经有所改善了。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x104,
        (
            "#12P#00300F先不说这些了，既然要去处理通缉魔兽，\x01",
            "我们就赶快进去吧。\x02",
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

    # Function_44_6BB3 end

    def Function_45_7058(): pass

    label("Function_45_7058")

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
            "#12P#00101F……我们已经掌握到兰迪\x01",
            "从昨夜至今早的行动了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x101,
        "#5P#00003F嗯，简单整理一下吧。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_71C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7460")
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
            "#1K兰迪最先前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7265")
    ClearScenarioFlags(0x1, 1)

    label("loc_7265")

    SetChrName("")

    #A0284
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K兰迪随后前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_72E2")
    ClearScenarioFlags(0x1, 1)

    label("loc_72E2")

    SetChrName("")

    #A0285
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K兰迪最后前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7368")
    ClearScenarioFlags(0x1, 1)

    label("loc_7368")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73EA")

    #C0286
    ChrTalk(
        0x101,
        (
            "#5P#00003F（不对……\x01",
            "  应该不是这个顺序。）\x02\x03",

            "#00001F（再整理一次吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_73E5")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_73E5")

    Jump("loc_745B")

    label("loc_73EA")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_73FA"),
        (SWITCH_DEFAULT, "loc_742C"),
    )


    label("loc_73FA")

    OP_2C(0xAA, 0x1)

    #C0287
    ChrTalk(
        0x101,
        "#5P#00000F（不错，就是这个顺序。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_745B")

    label("loc_742C")


    #C0288
    ChrTalk(
        0x101,
        "#5P#00003F（……多半是这个顺序吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_745B")

    label("loc_745B")

    Jump("loc_71C7")

    label("loc_7460")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "三点～四点　『巴鲁卡』\x01",
            "五点～六点　改造店『基约姆工房』\x01",
            "六点～　　　交换店『纳因瓦利』\x07\x00\x02",
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
            "#5P#00006F兰迪应该先去了『巴鲁卡』，\x01",
            "取走了寄存在\x01",
            "多雷克老板那里的手提箱。\x02\x03",

            "#00008F而箱子中的东西则是\x01",
            "兰迪在猎兵时代所使用的武器……\x02\x03",

            "#00001F我想，多半是攻击力\x01",
            "超群的导力来复枪。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x103,
        (
            "#6P#00203F像那样的来复枪，\x01",
            "在平时应该会以分解的状态来携带。\x02\x03",

            "#00201F由于已经有两年左右没使用过了，\x01",
            "所以兰迪前辈便将那些分解的部件\x01",
            "拿到修理工房检修……\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x109,
        (
            "#11P#10103F嗯，应该就是这样。\x02\x03",

            "#10108F在战场上，武器的检修\x01",
            "往往可以左右战士的生死……\x02\x03",

            "#10101F像兰迪前辈这种经验丰富的人，\x01",
            "一定会在事先做好精密的检查工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x105,
        (
            "#10303F最后，就是前往交换店，\x01",
            "采购各种物品了……\x02\x03",

            "#10301F他还购买了火药式弹药，\x01",
            "看来那支来复枪是相当特殊的型号啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x102,
        (
            "#12P#00108F听说莱恩福尔特公司\x01",
            "制造过可以切换导力模式\x01",
            "与火药模式的来复枪……\x02\x03",

            "#00101F每一种都是经过特殊强化的\x01",
            "来复枪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        (
            "#5P#00006F嗯，赤色星座的\x01",
            "那些猎兵所使用的也都是\x01",
            "从未见过的巨大来复枪。\x02\x03",

            "#00013F好，这样一来，\x01",
            "我们已经大体上掌握兰迪的行动了……\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x103,
        (
            "#6P#00206F兰迪前辈最后出现在交换店的时间\x01",
            "是在今天早上六点之后……\x02\x03",

            "#00208F现在是十点左右，\x01",
            "已经过去快四个小时了。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x109,
        (
            "#11P#10106F如果现在才出发，\x01",
            "恐怕已经很难追到兰迪前辈了……\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#5P#00003F……不，无论兰迪再怎么强健，\x01",
            "毕竟也是有极限的。\x02\x03",

            "#00001F如果想对『赤色星座』出手，\x01",
            "终究还是要先休息一下的。\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0x105,
        (
            "#10304F在精力充沛的境况下，活用地形优势，\x01",
            "一口气将敌人歼灭……\x02\x03",

            "#10302F只要他没有抱着玉石俱焚的想法，\x01",
            "准备与对方同归于尽，\x01",
            "还是那种做法比较妥当。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#12P#00101F……即使如此，\x01",
            "我们也没有多余的时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#5P#00013F嗯，现在也只能\x01",
            "先去玛因兹……\x02",
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

    def lambda_7AE5():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_7AE5)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_7B0A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_7B0A)
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
        "#5P#00011F难道是……\x02",
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x103,
        "#6P#00205F兰迪前辈打来的……？\x02",
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
            "#00007F这里是特别任务支援科！\x01",
            "我是罗伊德·班宁斯！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0305
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呀，罗伊德警官。\x02\x03",

            "……呵呵，听你的口气，\x01",
            "似乎误以为是其他人打去的吧？\x02",
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
            "#00005F这、这声音是……\x02\x03",

            "#00013F……您为何会知道这个号码？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0307
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，以前不是说过吗？\x01",
            "我可是你们的支持者啊。\x02\x03",

            "我在『时代』百货店。\x02\x03",

            "如果有空，\x01",
            "请一定来楼顶一趟。\x07\x00\x02",
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
            "#6P#00201F……罗伊德前辈，\x01",
            "刚才的通讯是……\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x102,
        "#12P#00108F到、到底是谁？\x02",
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
            "#5P#00003F……『黑月』的曹。\x02\x03",

            "#00013F他似乎正在中央广场\x01",
            "百货店的楼顶等我们。\x02",
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
        "#11P#10111F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x105,
        (
            "#10301F竟在这种时候……\x01",
            "他到底有什么目的？\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x101,
        (
            "#5P#00006F……不知道。\x01",
            "不过，我不认为那个男人\x01",
            "会无缘无故地发来联络。\x02\x03",

            "#00001F在前往山道之前，\x01",
            "还是过去见见他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0314
    ChrTalk(
        0x102,
        "#12P#00101F明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x103,
        "#6P#00201F总之，我们赶快过去吧。\x02",
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

    # Function_45_7058 end

    def Function_46_804A(): pass

    label("Function_46_804A")

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
            "#12P#00101F……我们已经掌握到兰迪\x01",
            "从昨夜至今早的行动了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x101,
        "#5P#00003F嗯，简单整理一下吧。\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x1, 1)

    label("loc_81BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8456")
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
            "#1K兰迪最先前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_825B")
    ClearScenarioFlags(0x1, 1)

    label("loc_825B")

    SetChrName("")

    #A0319
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K兰迪随后前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_82D8")
    ClearScenarioFlags(0x1, 1)

    label("loc_82D8")

    SetChrName("")

    #A0320
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K兰迪最后前往的地方是？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "交换店『纳因瓦利』\x01",        # 0
            "改造店『基约姆工房』\x01",      # 1
            "『巴鲁卡』\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_835E")
    ClearScenarioFlags(0x1, 1)

    label("loc_835E")

    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83E0")

    #C0321
    ChrTalk(
        0x101,
        (
            "#5P#00003F（不对……\x01",
            "  应该不是这个顺序。）\x02\x03",

            "#00001F（再整理一次吧。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_83DB")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_83DB")

    Jump("loc_8451")

    label("loc_83E0")

    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_83F0"),
        (SWITCH_DEFAULT, "loc_8422"),
    )


    label("loc_83F0")

    OP_2C(0xAA, 0x1)

    #C0322
    ChrTalk(
        0x101,
        "#5P#00000F（不错，就是这个顺序。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8451")

    label("loc_8422")


    #C0323
    ChrTalk(
        0x101,
        "#5P#00003F（……多半是这个顺序吧。）\x02",
    )

    CloseMessageWindow()
    Jump("loc_8451")

    label("loc_8451")

    Jump("loc_81BD")

    label("loc_8456")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "三点～四点　『巴鲁卡』\x01",
            "五点～六点　改造店『基约姆工房』\x01",
            "六点～　　　交换店『纳因瓦利』\x07\x00\x02",
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
            "#5P#00006F兰迪应该先去了『巴鲁卡』，\x01",
            "取走了寄存在\x01",
            "多雷克老板那里的手提箱。\x02\x03",

            "#00008F而箱子中的东西则是\x01",
            "兰迪在猎兵时代所使用的武器……\x02\x03",

            "#00001F我想，多半是攻击力\x01",
            "超群的导力来复枪。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x103,
        (
            "#6P#00203F像那样的来复枪，\x01",
            "在平时应该会以分解的状态来携带。\x02\x03",

            "#00201F由于已经有两年左右没使用过了，\x01",
            "所以兰迪前辈便将那些分解的部件\x01",
            "拿到修理工房检修……\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x109,
        (
            "#10103F#11P嗯，应该就是这样。\x02\x03",

            "#10108F在战场上，武器的检修\x01",
            "往往可以左右战士的生死……\x02\x03",

            "#10101F像兰迪前辈这种经验丰富的人，\x01",
            "一定会在事先做好精密的检查工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x105,
        (
            "#12P#10303F最后，就是前往交换店，\x01",
            "采购各种物品了……\x02\x03",

            "#10301F他还购买了火药式弹药，\x01",
            "看来那支来复枪是相当特殊的型号啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x102,
        (
            "#12P#00108F听说莱恩福尔特公司\x01",
            "制造过可以切换导力模式\x01",
            "与火药模式的来复枪……\x02\x03",

            "#00101F每一种都是经过特殊强化的\x01",
            "来复枪呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x101,
        (
            "#5P#00006F嗯，赤色星座的\x01",
            "那些猎兵所使用的也都是\x01",
            "从未见过的巨大来复枪。\x02\x03",

            "#00013F好，这样一来，\x01",
            "我们已经大体上掌握兰迪的行动了……\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x103,
        (
            "#6P#00206F兰迪前辈最后出现在交换店的时间\x01",
            "是今天早上六点之后……\x02\x03",

            "#00208F现在是十点左右，\x01",
            "已经过去快四个小时了。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x109,
        (
            "#10106F#11P如果现在才出发，\x01",
            "恐怕已经很难追到兰迪前辈了……\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#5P#00003F……不，无论兰迪再怎么强健，\x01",
            "毕竟也是有极限的。\x02\x03",

            "#00001F如果想对『赤色星座』出手，\x01",
            "终究还是要先休息一下的。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x105,
        (
            "#12P#10304F在精力充沛的境况下，活用地形优势，\x01",
            "一口气将敌人歼灭……\x02\x03",

            "#10302F只要他没有抱着玉石俱焚的想法，\x01",
            "准备与对方同归于尽，\x01",
            "还是那种做法比较妥当。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x102,
        (
            "#12P#00101F……即使如此，\x01",
            "我们也没有多余的时间了。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x101,
        (
            "#5P#00013F嗯，现在也只能\x01",
            "先去玛因兹……\x02",
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

    def lambda_8AE1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_8AE1)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8B06():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8B06)
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
        "#5P#00011F难道是……\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x103,
        "#6P#00205F兰迪前辈打来的……？\x02",
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
            "#00007F这里是特别任务支援科！\x01",
            "我是罗伊德·班宁斯！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0340
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呀，罗伊德警官。\x02\x03",

            "……呵呵，听你的口气，\x01",
            "似乎误以为是其他人打去的吧？\x02",
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
            "#00005F这、这声音是……\x02\x03",

            "#00013F……您为何会知道这个号码？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男性的声音")

    #A0342
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "呵呵，以前不是说过吗？\x01",
            "我可是你们的支持者啊。\x02\x03",

            "我在『时代』百货店。\x02\x03",

            "如果有空，\x01",
            "请一定来楼顶一趟。\x07\x00\x02",
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
            "#6P#00201F……罗伊德前辈，\x01",
            "刚才的通讯是……\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x102,
        "#12P#00108F到、到底是谁？\x02",
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
            "#5P#00003F……『黑月』的曹。\x02\x03",

            "#00013F他似乎正在中央广场\x01",
            "百货店的楼顶等我们。\x02",
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
        "#10111F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x105,
        (
            "#12P#10301F竟在这种时候……\x01",
            "他到底有什么目的？\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        (
            "#5P#00006F……不知道。\x01",
            "不过，我不认为那个男人\x01",
            "会无缘无故地发来联络。\x02\x03",

            "#00001F在前往山道之前，\x01",
            "还是过去见见他吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x102,
        "#12P#00101F明、明白了。\x02",
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x103,
        "#6P#00201F总之，我们赶快过去吧。\x02",
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

    # Function_46_804A end

    def Function_47_9047(): pass

    label("Function_47_9047")

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

    def lambda_9122():
        OP_95(0x101, 8630, 0, 4260, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9122)

    def lambda_913C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_913C)
    Sleep(500)

    def lambda_9150():
        OP_95(0x102, 9430, 0, 3460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9150)

    def lambda_916A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_916A)
    Sleep(500)

    def lambda_917E():
        OP_95(0x109, 9830, 0, 5460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_917E)

    def lambda_9198():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9198)
    Sleep(500)

    def lambda_91AC():
        OP_95(0x105, 10630, 0, 4460, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_91AC)

    def lambda_91C6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_91C6)
    Sleep(50)
    WaitChrThread(0x101, 1)

    def lambda_91DE():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_91DE)
    WaitChrThread(0x102, 1)

    def lambda_91EF():
        OP_93(0x102, 0x168, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_91EF)
    WaitChrThread(0x109, 1)

    def lambda_9200():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9200)
    WaitChrThread(0x105, 1)

    def lambda_9211():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9211)
    SetMapObjFlags(0x3, 0x0)
    WaitChrThread(0x101, 1)

    #C0351
    ChrTalk(
        0x102,
        (
            "#12P#00103F话说回来……\x02\x03",

            "#00108F在那些被撤职的议员之中，\x01",
            "盖巴尔议员的境遇\x01",
            "恐怕还算不错了。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x109,
        (
            "#10101F是啊，那些因教团事件\x01",
            "被捕的议员们，\x01",
            "现在的状况可比他严苛得多。\x02\x03",

            "#10103F虽说是应有此报，\x01",
            "但他们毕竟只是被操纵的一方，\x01",
            "所以一定觉得很难接受吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0353
    ChrTalk(
        0x101,
        (
            "#6P#00003F是啊，但结局\x01",
            "还是恶有恶报……\x01",
            "这就是世间常理。\x02\x03",

            "#00000F反过来说，只要努力重新振作，\x01",
            "也总有一天会有回报的。\x02\x03",

            "#00004F不管是那位盖巴尔议员，\x01",
            "还是被捕的那些议员……\x01",
            "真希望他们能有这么一天啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x102,
        (
            "#12P#00103F是啊……\x01",
            "（希望阿奈斯特先生也能有这么一天……）\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，真不愧是队长啊，\x01",
            "说出来的话特别有道理。\x02\x03",

            "#10302F不如一起去『崔尼蒂』\x01",
            "继续探讨这个话题，\x01",
            "顺便喝一杯吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x101,
        (
            "#6P#00006F我说你啊，现在可是在工作呢，\x01",
            "怎么可能干那种事。\x02\x03",

            "#00000F……总之，\x01",
            "旧城区这边已经调查完了。\x02",
        )
    )

    CloseMessageWindow()
    OP_29(0x6A, 0x1, 0x5)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95EB")
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
            "◆「调查状况？（测试用）\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【还有剩余】\x01",          # 0
            "【六处确认完毕】\x01",      # 1
            "【未变更】\x01",            # 2
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
        (0, "loc_95BE"),
        (1, "loc_95D2"),
        (2, "loc_95E6"),
        (SWITCH_DEFAULT, "loc_95EB"),
    )


    label("loc_95BE")

    ClearScenarioFlags(0x131, 5)
    ClearScenarioFlags(0x131, 6)
    ClearScenarioFlags(0x131, 7)
    ClearScenarioFlags(0x132, 0)
    ClearScenarioFlags(0x132, 1)
    Jump("loc_95EB")

    label("loc_95D2")

    SetScenarioFlags(0x131, 5)
    SetScenarioFlags(0x131, 6)
    SetScenarioFlags(0x131, 7)
    SetScenarioFlags(0x132, 0)
    SetScenarioFlags(0x132, 1)
    Jump("loc_95EB")

    label("loc_95E6")

    Jump("loc_95EB")

    label("loc_95EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9640")

    #C0358
    ChrTalk(
        0x101,
        (
            "#6P#00000F接下来，我们就继续去\x01",
            "调查剩下的地方吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_968A")

    label("loc_9640")

    OP_29(0x6A, 0x1, 0x6)

    #C0359
    ChrTalk(
        0x101,
        (
            "#6P#00000F好，已经全部调查完毕了。\x02\x03",

            "这就去市民会馆汇报结果吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_968A")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x3, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x10)
    SetScenarioFlags(0x132, 2)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 9630, 0, 4460, 225)
    EventEnd(0x5)
    Return()

    # Function_47_9047 end

    def Function_48_96C2(): pass

    label("Function_48_96C2")

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
            "#11P啊，是你们……\x01",
            "到底有什么事？\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x8,
        (
            "#11P而且那边那个是……\x01",
            "瓦、瓦吉！？\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x8,
        (
            "#11P唔……！\x01",
            "滚一边去，混蛋！\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x105,
        (
            "#6P#10308F哎呀呀……\x01",
            "看来我被人讨厌了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x101,
        (
            "#6P#00003F……抱歉，我明白你的心情，\x01",
            "但请你听我们说几句。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0365
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德将接受教授的委托，\x01",
            "前来收取问诊表的事情做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0366
    ChrTalk(
        0x8,
        "#11P问诊表……？\x02",
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x8,
        (
            "#11P……啊，就是去乌尔斯拉医院\x01",
            "治疗时拿到的那张表格吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x104,
        "#12P#00305F怎么，原来你并没有忘记啊？\x02",
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x8,
        (
            "#11P哼，我现在已经完全\x01",
            "不受药物的影响了。\x02",
        )
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x8,
        (
            "#11P既然已经痊愈了，\x01",
            "谁还会特意跑到医院去。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x102,
        (
            "#12P#00101F迪诺……\x01",
            "不可以擅自判断病情哦。\x02\x03",

            "#00103F万一症状还有所残留，\x01",
            "说不定会给剑蛇帮的各位\x01",
            "带来麻烦呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x8,
        "#11P唔……你说的也没错……\x02",
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x8,
        (
            "#11P……啊啊，真是的，我知道啦！\x01",
            "你们在这里稍等一下。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x8,
        (
            "#11P我应该随手把那表格放在什么地方了，\x01",
            "我现在就去填了拿给你们。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A76():
        OP_95(0xFE, 44930, -2500, -22750, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9A76)
    WaitChrThread(0x8, 1)

    def lambda_9A94():
        OP_95(0xFE, 47960, -2100, -22440, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9A94)
    Sleep(50)

    def lambda_9AB1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9AB1)
    Sleep(50)

    def lambda_9AC1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9AC1)
    Sleep(50)

    def lambda_9AD1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9AD1)
    Sleep(50)

    def lambda_9AE1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_9AE1)
    Sleep(50)

    def lambda_9AF1():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_9AF1)
    WaitChrThread(0x8, 1)
    Sound(116, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    Sleep(700)

    def lambda_9B20():
        OP_97(0xFE, 0x7D0, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_9B20)

    def lambda_9B3A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_9B3A)
    WaitChrThread(0x8, 2)
    SetChrFlags(0x8, 0x80)
    OP_0D()

    #C0375
    ChrTalk(
        0x109,
        "#6P#10106F呼，看来可以成功回收表格呢。\x02",
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x101,
        "#6P#00000F是啊，站在这里等等吧。\x02",
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
        "#11P……给，这样就行了吧？\x02",
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
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('迪诺的问诊表', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0379
    ChrTalk(
        0x101,
        "#6P#00000F没错，那我就收下了。\x02",
    )

    CloseMessageWindow()

    #C0380
    ChrTalk(
        0x102,
        "#12P#00100F谢谢你的配合，迪诺。\x02",
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x8,
        (
            "#11P……哼，没什么\x01",
            "可谢的。\x02",
        )
    )

    CloseMessageWindow()

    #C0382
    ChrTalk(
        0x8,
        (
            "#11P好了，赶快带着\x01",
            "那个瓦吉滚远一点吧！！\x02",
        )
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x101,
        "#6P#00006F我、我知道了。\x02",
    )

    CloseMessageWindow()

    #C0384
    ChrTalk(
        0x105,
        "#6P#10303F……真是打扰了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x152, 3)
    OP_29(0x70, 0x1, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x70, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x152, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DEC")

    #A0385
    AnonymousTalk(
        0x101,
        (
            "#00000F好，我们已经把所有\x01",
            "问诊表都收回来了。\x02\x03",

            "赶快给赛兰德教授\x01",
            "送去吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_29(0x70, 0x1, 0x5)

    label("loc_9DEC")

    OP_93(0x8, 0xE1, 0x0)
    OP_4C(0x8, 0xFF)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 43610, -2500, -21900, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_48_96C2 end

    def Function_49_9E19(): pass

    label("Function_49_9E19")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_9E93")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_9ED2")

    label("loc_9E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_9EB5")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_9ED2")

    label("loc_9EB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_9ED2")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_9ED2")

    OP_68(-2990, 1930, -22180, 5000)
    MoveCamera(44, 22, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(49730, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_9FDE")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x104, 910, 0, 24450, 180)

    def lambda_9F70():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_9F70)

    def lambda_9F8A():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_9F8A)
    Sleep(100)

    def lambda_9FA7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9FA7)
    Sleep(50)

    def lambda_9FC4():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_9FC4)
    Jump("loc_A181")

    label("loc_9FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_A0B2")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x109, 910, 0, 24450, 180)

    def lambda_A044():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_A044)

    def lambda_A05E():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A05E)
    Sleep(100)

    def lambda_A07B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A07B)
    Sleep(50)

    def lambda_A098():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A098)
    Jump("loc_A181")

    label("loc_A0B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_A181")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, 2260, 0, 22750, 180)
    SetChrPos(0x102, 1410, 0, 22750, 180)
    SetChrPos(0x101, 2900, 0, 24450, 180)
    SetChrPos(0x105, 910, 0, 24450, 180)

    def lambda_A118():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_A118)

    def lambda_A132():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A132)
    Sleep(100)

    def lambda_A14F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A14F)
    Sleep(50)

    def lambda_A16C():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFB1E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A16C)

    label("loc_A181")

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
            "这里……\x01",
            "还真是个萧条的地方啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x102,
        (
            "#00103F……这里是旧城区，\x01",
            "在城市开发计划中被遗留的地方。\x02",
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
            "哼……不管哪个国家\x01",
            "都有这样的地方啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0389
    ChrTalk(
        0x1A2,
        "#12P够了，我们回东街去吧。\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x101,
        "#00005F好、好的……我明白了。\x02",
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

    # Function_49_9E19 end

    def Function_50_A2E5(): pass

    label("Function_50_A2E5")

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

    def lambda_A3D5():
        OP_95(0xFE, 2450, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A3D5)
    Sleep(10)

    def lambda_A3F2():
        OP_95(0xFE, 1250, 0, 8000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A3F2)
    Sleep(20)

    def lambda_A40F():
        OP_95(0xFE, 2260, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A40F)
    Sleep(10)

    def lambda_A42C():
        OP_95(0xFE, 3460, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A42C)
    Sleep(20)

    def lambda_A449():
        OP_95(0xFE, 1060, 0, 9650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A449)
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
        "男人的声音",
        "#4S……你说什么！？\x02",
    )

    CloseMessageWindow()

    #N0392
    NpcTalk(
        0xE,
        "男人的声音",
        (
            "#4S啊！？别光知道\x01",
            "在那里抱怨啊！\x02",
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
        "#00005F这声音是……\x02",
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x102,
        "#00105F罗伊德，你看！\x02",
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
            "#6P混蛋，斯拉修……\x01",
            "你有没有好好在想啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0xD,
        (
            "#6P如果瓦鲁多大哥继续每日酗酒，\x01",
            "搞坏了身体可怎么办啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0xE,
        (
            "为了避免那种情况，我这不是在\x01",
            "努力思考可行的办法吗！！\x02",
        )
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0xE,
        (
            "别因为自己什么都想不出来，\x01",
            "就在那里大吼大叫的！\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0xD,
        (
            "#6P你的办法就是刚才说的那种烂点子吗！？\x01",
            "什么叫『只要在塔顶看看风景，\x01",
            "说不定就能舒坦些』！？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0xD,
        (
            "#6P如果跑到高处看看风景\x01",
            "就能让瓦鲁多大哥的心情转好，\x01",
            "那我们还用这么辛苦吗！！\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0xD,
        (
            "#6P#4S别拿我跟你这种白痴\x01",
            "相提并论啊，白痴！\x01",
            "你这个白痴！！\x02",
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
            "#4S混、混账～～～！！\x01",
            "你竟敢连续说我白痴三次！！\x02",
        )
    )

    CloseMessageWindow()

    #C0403
    ChrTalk(
        0xE,
        (
            "#4S跟你这种连根毛都想不出来的\x01",
            "家伙相比，我可要强一百倍呢！\x02",
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
        "#6P你说什么……！！\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0xD,
        "#6P#4S要跟我打一架吗！？\x02",
    )

    CloseMessageWindow()
    Sleep(100)

    #C0406
    ChrTalk(
        0x101,
        "#5P#N#4S#00007F快住手，你们两个！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_68(280, 2000, -1490, 3000)
    MoveCamera(36, 20, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(15650, 3000)

    def lambda_A918():
        OP_95(0xFE, 2450, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A918)
    Sleep(10)

    def lambda_A935():
        OP_95(0xFE, 1250, 0, 500, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_A935)
    Sleep(20)

    def lambda_A952():
        OP_95(0xFE, 2260, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_A952)
    Sleep(10)

    def lambda_A96F():
        OP_95(0xFE, 3460, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A96F)
    Sleep(20)

    def lambda_A98C():
        OP_95(0xFE, 1060, 0, 2150, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_A98C)
    Sleep(200)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_A9D0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_A9D0)
    Sleep(10)

    def lambda_A9E0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_A9E0)
    WaitChrThread(0x105, 1)
    WaitChrThread(0xD, 1)
    OP_6F(0x79)

    #C0407
    ChrTalk(
        0xE,
        "#12P你、你们是……\x02",
    )

    CloseMessageWindow()

    #C0408
    ChrTalk(
        0x104,
        (
            "#5P#00301F喂喂，你们可是同伴啊，\x01",
            "把武器亮出来就\x01",
            "太不像话了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0xD,
        (
            "#12P哼……\x01",
            "这跟你们没关系吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0xD,
        (
            "#12P说到底……瓦吉！\x01",
            "还不都是因为你这混账\x01",
            "做了那种事……！！\x02",
        )
    )

    CloseMessageWindow()

    #C0411
    ChrTalk(
        0xE,
        (
            "#12P就是啊……！\x01",
            "瓦鲁多大哥会变成那样，\x01",
            "全都怪瓦吉！\x02",
        )
    )

    CloseMessageWindow()

    #C0412
    ChrTalk(
        0xE,
        "#12P都是你不好，瓦吉！\x02",
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
            "#5P#10105F等、等等！\x01",
            "瓦吉他并没有……\x02",
        )
    )

    CloseMessageWindow()

    #C0415
    ChrTalk(
        0xD,
        (
            "#12P总之，可不能就此收手……\x01",
            "首先得把你们几个狠揍一顿！\x02",
        )
    )

    CloseMessageWindow()

    #C0416
    ChrTalk(
        0xE,
        "#12P哈哈，说的没错！\x02",
    )

    CloseMessageWindow()

    #C0417
    ChrTalk(
        0xE,
        (
            "#12P嘿～等教训过他们之后，\x01",
            "再好好修理你！\x02",
        )
    )

    CloseMessageWindow()

    #C0418
    ChrTalk(
        0x102,
        "#5P#00101F（怎、怎么办？罗伊德……）\x02",
    )

    CloseMessageWindow()

    #C0419
    ChrTalk(
        0x104,
        "#5P#00301F（他们的情绪已经完全失控了啊。）\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        (
            "#11P#00010F（唔，事到如今，\x01",
            "  我们也只能出手制服他们了……）\x02",
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
        "青年的声音",
        (
            "唉……\x01",
            "真是可悲啊。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x64, 0x7D0)
    OP_68(-7930, 6500, -5030, 6000)
    MoveCamera(41, 31, 0, 6000)
    OP_6E(500, 6000)
    SetCameraDistance(14890, 6000)
    Sleep(500)

    def lambda_ADAC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_ADAC)
    Sleep(10)

    def lambda_ADBC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_ADBC)
    Sleep(20)

    def lambda_ADCC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_ADCC)
    Sleep(10)

    def lambda_ADDC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_ADDC)
    Sleep(20)

    def lambda_ADEC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_ADEC)
    Sleep(10)

    def lambda_ADFC():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_ADFC)
    Sleep(10)

    def lambda_AE0C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_AE0C)
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
        "金发青年",
        (
            "#5P#13904F纷争无法蕴育任何事物……\x01",
            "只能编织出愚蠢又可憎的连锁。\x02\x03",

            "#13902F就让我为冲动的你们献上一曲吧。\x02\x03",

            "为了化解你们那已经浑沌的心灵，\x01",
            "为了让各位的心彼此相连，\x01",
            "我特此献上这首优美而伤感的歌曲…………\x02",
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
        "金发青年",
        "#70A#50W滑过天边#1500W　#50W星之#1000W　#50W轨迹……  \x05\x02",
    )
    #Auto

    Sleep(7000)

    #N0424
    NpcTalk(
        0x18,
        "金发青年",
        "#70A#50W仿如路标#1000W　#50W引导向你……\x05\x02",
    )
    #Auto

    Sleep(7000)

    #N0425
    NpcTalk(
        0x18,
        "金发青年",
        "#70A#50W急切的#1500W　#50W思念#1000W　#50W满溢胸怀……\x05\x02",
    )
    #Auto

    Sleep(7000)

    #N0426
    NpcTalk(
        0x18,
        "金发青年",
        "#70A#50W月亮也嘲笑#1000W　#50W这份痛苦……\x05\x02",
    )
    #Auto

    Sleep(7000)

    #N0427
    NpcTalk(
        0x18,
        "金发青年",
        "#70A#50W若无法实现#3000W　#50W这份空想……\x05\x02",
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
        "#4S……喂！死金毛！吵死人了！！\x02",
    )

    CloseMessageWindow()

    #N0429
    NpcTalk(
        0x18,
        "金发青年",
        "#12P#13911F唔哇……！？\x02",
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
        "金发青年",
        (
            "#11P#13909F怎、怎么了？\x01",
            "我可爱的小猫咪。\x02\x03",

            "#13902F如你所见，我正在演奏呢。\x01",
            "抱歉，如果想要签名，请等到演奏之后。\x02\x03",

            "#13910F还有啊，在这种地方踢人\x01",
            "实在是太危——\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x19, 0x0, 1700, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0431
    ChrTalk(
        0x19,
        "#6P少在那里啰嗦个没完……！\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x19,
        (
            "#6P竟敢在我们店的屋顶上折腾，\x01",
            "真是烦死了，赶紧给我下去！\x02",
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
        "金发青年",
        (
            "#13911F我、我知道了！\x01",
            "已经知道了，所以别再……\x02",
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
        "#12P快·下·去！\x02",
    )

    CloseMessageWindow()

    def lambda_B47D():
        OP_95(0xFE, -17240, 5400, -1780, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B47D)
    Sleep(800)
    OP_95(0x19, -16880, 5400, -1950, 4000, 0x0)
    Sleep(1000)
    Sound(1013, 0, 100, 0)

    #N0435
    NpcTalk(
        0x18,
        "青年的声音",
        "#2S哇……！？\x02",
    )

    CloseMessageWindow()
    Sound(833, 0, 40, 0)
    Sound(992, 0, 40, 0)
    Sleep(50)
    Sound(811, 0, 100, 0)

    #C0436
    ChrTalk(
        0x19,
        "#2S……啊，掉下去了。\x02",
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x19,
        "#2S金毛～你还活着吗～？\x02",
    )

    CloseMessageWindow()

    #N0438
    NpcTalk(
        0x18,
        "青年的声音",
        "#2S呜……\x02",
    )

    CloseMessageWindow()

    #C0439
    ChrTalk(
        0x19,
        "#2S……原来还活着嘛～\x02",
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
        "#12P这……这个……\x02",
    )

    CloseMessageWindow()

    def lambda_B652():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B652)
    Sleep(10)

    def lambda_B662():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B662)
    Sleep(20)

    def lambda_B672():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B672)
    Sleep(10)

    def lambda_B682():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B682)
    Sleep(20)

    def lambda_B692():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B692)

    #C0441
    ChrTalk(
        0xD,
        "#12P不知为何，突然没有继续的欲望了，我要回去了。\x02",
    )

    CloseMessageWindow()

    #C0442
    ChrTalk(
        0xE,
        "#12P#5A可恶，那个金毛是怎么回事……\x02",
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
        "#12P真是的。\x02",
    )

    CloseMessageWindow()

    #C0444
    ChrTalk(
        0xD,
        "#6P……好了，快回去吧。\x02",
    )

    CloseMessageWindow()

    def lambda_B757():
        OP_95(0xFE, 6640, 0, -7350, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B757)
    Sleep(800)

    def lambda_B774():
        OP_95(0xFE, 7700, 0, -7010, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_B774)

    def lambda_B78E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B78E)
    Sleep(50)

    def lambda_B79E():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B79E)
    Sleep(50)

    def lambda_B7AE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B7AE)
    Sleep(50)

    def lambda_B7BE():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B7BE)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)

    #C0445
    ChrTalk(
        0x101,
        "#5P#00012F他、他们走了……\x02",
    )

    CloseMessageWindow()

    #C0446
    ChrTalk(
        0x105,
        (
            "#5P#10306F……呼，这也算是\x01",
            "得救了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x18, -3400, 0, -6690, 0)

    #N0447
    NpcTalk(
        0x18,
        "青年的声音",
        (
            "呵、呵呵……\x01",
            "我成功摘除了一株即将在\x01",
            "魔都绽放的斗争之芽呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B884():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B884)
    Sleep(50)

    def lambda_B894():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B894)
    Sleep(50)

    def lambda_B8A4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B8A4)
    Sleep(50)

    def lambda_B8B4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_B8B4)
    Sleep(50)

    def lambda_B8C4():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_B8C4)

    #N0448
    NpcTalk(
        0x18,
        "青年的声音",
        (
            "全靠我这以爱与真心来\x01",
            "追求和平的鲁特琴演奏……\x02",
        )
    )

    CloseMessageWindow()

    #N0449
    NpcTalk(
        0x18,
        "青年的声音",
        (
            "有时真为自己这惊人的\x01",
            "才华而感到恐惧啊。\x02",
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

    def lambda_B9B8():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B9B8)
    OP_96(0x18, 0xFFFFFD4E, 0x0, 0xFFFFECB4, 0x3E8, 0x0)

    def lambda_B9D9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B9D9)
    OP_96(0x18, 0xFFFFFC68, 0x0, 0xFFFFF330, 0x7D0, 0x0)

    def lambda_B9FA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_B9FA)
    OP_96(0x18, 0x320, 0x0, 0xFFFFF416, 0x5DC, 0x0)

    def lambda_BA1B():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BA1B)
    OP_96(0x18, 0x654, 0x0, 0xFFFFFA10, 0x3E8, 0x0)

    def lambda_BA3C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_BA3C)
    Sleep(50)

    def lambda_BA4C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_BA4C)
    Sleep(50)

    def lambda_BA5C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_BA5C)
    Sleep(50)

    def lambda_BA6C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_BA6C)
    Sleep(50)

    def lambda_BA7C():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_BA7C)
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
            "#6P#00105F请、请问……您没事吧？\x01",
            "刚才听到了\x01",
            "很大的落地声呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0451
    NpcTalk(
        0x18,
        "金发青年",
        (
            "#11P#13904F呵呵，请不必为我担心，\x01",
            "尊敬的小姐。\x02\x03",

            "#13902F对翱翔在大陆苍穹的我来说，\x01",
            "这点微不足道的高度\x01",
            "实在是不值一提。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x104,
        "#6P#00306F听不懂他在说什么……\x02",
    )

    CloseMessageWindow()

    #N0453
    NpcTalk(
        0x18,
        "金发青年",
        (
            "#11P#13903F刚才发生了一点\x01",
            "小小的意外……\x02\x03",

            "#13900F接下来就重整心情，\x01",
            "继续为各位演奏我的名曲吧。\x02\x03",

            "#13904F呵呵，请大家尽情享受。\x02",
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
        "#6P#00011F不、不必了！\x02",
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x109,
        (
            "#6P#10106F（罗、罗伊德警官，\x01",
            "  难道这个人就是……）\x02",
        )
    )

    CloseMessageWindow()

    #C0456
    ChrTalk(
        0x101,
        (
            "#12P#00001F（没错，金发与白色大衣……）\x02\x03",

            "#00006F（虽然穆拉先生说过\x01",
            "  他是个棘手人物……\x01",
            "  但还真是超乎想象啊。）\x02",
        )
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x101,
        (
            "#6P#00001F……咳咳。\x01",
            "您应该就是\x01",
            "奥利维尔先生吧？\x02",
        )
    )

    CloseMessageWindow()

    #N0458
    NpcTalk(
        0x18,
        "金发青年",
        "#11P#13904F呵呵……不错。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("金发青年")

    #A0459
    AnonymousTalk(
        0xFF,
        (
            "我正是为了寻求爱而踏上旅程的\x01",
            "稀世天才、漂泊的演奏家——\x01",
            "奥利维尔·朗海姆。\x02",
        )
    )

    CloseMessageWindow()

    #A0460
    AnonymousTalk(
        0x18,
        (
            "呵呵，你们的运气真好，\x01",
            "居然有幸欣赏我这个天才的\x01",
            "即兴演奏会。\x02\x03",

            "请把今天这个日子永刻心中，\x01",
            "将其当作铭记一生的宝贵回忆吧。\x02",
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
        "#6P#00006F……哦……\x02",
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
            "#11P#13905F啊，说起来……\x01",
            "你们为何会知道我的名字呢？\x02\x03",

            "#13902F我来到克洛斯贝尔之后，\x01",
            "好像还没对任何人说过自己的名字呢。\x01",
            "……我们曾在哪里见过吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0463
    ChrTalk(
        0x101,
        (
            "#6P#00000F我们是克洛斯贝尔警察局·\x01",
            "特别任务支援科的成员。\x02\x03",

            "受穆拉先生所托，\x01",
            "正在寻找您。\x02",
        )
    )

    CloseMessageWindow()

    #C0464
    ChrTalk(
        0x102,
        (
            "#6P#00100F请问您是否\x01",
            "认识他？\x02",
        )
    )

    CloseMessageWindow()

    #C0465
    ChrTalk(
        0x18,
        (
            "#11P#13905F哦？原来你们就是传闻中的……\x02\x03",

            "#13904F呵呵……\x01",
            "穆拉还是老样子，这么爱乱操心。\x02\x03",

            "#13912F只不过是分开了\x01",
            "这么一点点时间而已，\x01",
            "我们之间的爱并不会因此而淡化啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0466
    ChrTalk(
        0x109,
        (
            "#6P#10105F咦咦！？\x01",
            "你、你们是那种关系吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0467
    ChrTalk(
        0x104,
        "#6P#00306F……不不不，多半只是他胡言乱语。\x02",
    )

    CloseMessageWindow()

    #C0468
    ChrTalk(
        0x101,
        (
            "#6P#00006F总、总之……\x01",
            "您能和我们一起回去\x01",
            "见穆拉先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x18,
        (
            "#11P#13903F……实在抱歉，\x01",
            "我无法答应你们这个请求。\x02\x03",

            "#13900F到了明天，无论如何都会忙碌起来，\x01",
            "所以必须得趁现在，\x01",
            "在克洛斯贝尔尽情游览一番。\x02",
        )
    )

    CloseMessageWindow()

    #C0470
    ChrTalk(
        0x102,
        "#6P#00105F忙碌起来……？\x02",
    )

    CloseMessageWindow()

    #C0471
    ChrTalk(
        0x18,
        (
            "#11P#13904F呵呵，只是我的个人问题而已。\x02\x03",

            "如果你们\x01",
            "不能就此\x01",
            "放过我的话……\x02\x03",

            "#13902F我无论动用什么手段，\x01",
            "也要让你们放我走。\x02",
        )
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x105,
        (
            "#6P#10302F哎……？\x01",
            "你这是什么意思？\x02",
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
            "#12P#13907F#4S哇……！\x01",
            "站在那边的是尤莉亚准校！？\x02",
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

    def lambda_C497():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C497)
    Sleep(10)

    def lambda_C4A7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C4A7)
    Sleep(20)

    def lambda_C4B7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C4B7)
    Sleep(10)

    def lambda_C4C7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C4C7)
    Sleep(20)

    def lambda_C4D7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C4D7)
    Sleep(500)

    #C0474
    ChrTalk(
        0x101,
        "#00011F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0475
    ChrTalk(
        0x102,
        "#12P#00105F咦咦……！？\x02",
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x109,
        "#6P#10107F#4S在、在哪里！？\x02",
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
            "#10105F咦？奇、奇怪……\x01",
            "根本没人啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x101,
        "#00005F……啊！\x02",
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

    def lambda_C67C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C67C)
    Sleep(10)

    def lambda_C68C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_C68C)
    Sleep(20)

    def lambda_C69C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_C69C)
    Sleep(10)

    def lambda_C6AC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_C6AC)
    Sleep(20)

    def lambda_C6BC():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C6BC)
    Sleep(500)

    #C0479
    ChrTalk(
        0x18,
        (
            "#5P#13902F呵呵，期待与你们\x01",
            "重逢的那一天哦！\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_93(0x18, 0x0, 0x1F4)

    def lambda_C71B():
        OP_95(0xFE, 1900, 0, 20650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_C71B)
    Sleep(500)

    #C0480
    ChrTalk(
        0x101,
        "#12P#00011F等、等一下……！\x02",
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
        "#12P#00106F让、让他逃了呢……\x02",
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x109,
        (
            "#11P#10101F居然中了这么\x01",
            "老套的伎俩……\x02\x03",

            "#10106F仔细想想，\x01",
            "尤莉亚准校怎么可能\x01",
            "会来这种地方嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x104,
        (
            "#5P#00306F哎呀呀，和雷克特有所不同，\x01",
            "是另一种类型的棘手老兄呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x101,
        (
            "#12P#00000F总、总之，\x01",
            "我们赶快追吧。\x02\x03",

            "#00003F不过，\x01",
            "他到底去了哪里呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x105,
        (
            "#6P#10303F还是先去刚才\x01",
            "提到的那几个地方\x01",
            "看看吧。\x02\x03",

            "#10300F既然已经在旧城区找到他了，\x01",
            "剩下的地点……\x01",
            "也就是后巷和港湾区了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x109,
        "#11P#10100F总之，去找找看吧！\x02",
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

    # Function_50_A2E5 end

    def Function_51_CA05(): pass

    label("Function_51_CA05")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CA54")
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
    Jump("Function_51_CA05")

    label("loc_CA54")

    Return()

    # Function_51_CA05 end

    def Function_52_CA55(): pass

    label("Function_52_CA55")

    Sleep(23000)
    OP_95(0xFE, -12870, 5400, -2670, 1000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(4000)
    OP_9D(0xFE, 0xFFFFD4AE, 0x1900, 0xFFFFF466, 0x4B0, 0xBB8)
    Sound(50, 0, 100, 0)
    Return()

    # Function_52_CA55 end

    def Function_53_CA94(): pass

    label("Function_53_CA94")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0487
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "公寓『伊梅尔达馆』\x01\x01",
            "　～　暂时停止出租　～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('伊梅尔达馆的钥匙', 0x0)"), scpexpr(EXPR_END)), "loc_CB89")
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0488
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是否使用伊梅尔达馆的钥匙？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CB84")
    OP_5A()
    Sleep(500)
    Sound(806, 0, 100, 0)
    Sleep(1000)

    #A0489
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『伊梅尔达馆』的门锁被打开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_29(0x67, 0x1, 0x1)
    SetScenarioFlags(0x133, 1)
    SetMapObjFlags(0x1, 0x10)
    OP_65(0x1, 0x1)

    label("loc_CB84")

    Jump("loc_CCF1")

    label("loc_CB89")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC7D")

    #C0490
    ChrTalk(
        0x101,
        "#00000F……看来被锁上了呢。\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x102,
        (
            "#00105F在那件处理魔兽的委托中\x01",
            "提及的地点应该就是这栋公寓。\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x101,
        (
            "#00003F我记得这里的所有人\x01",
            "是古董店的店主\x01",
            "『伊梅尔达夫人』。\x02\x03",

            "#00000F这就去后巷的古董店，\x01",
            "向夫人借用\x01",
            "公寓的钥匙吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_CCF1")

    label("loc_CC7D")


    #C0493
    ChrTalk(
        0x101,
        (
            "#00000F在那件处理魔兽的委托中\x01",
            "提及的地点\x01",
            "就是这栋公寓。\x02\x03",

            "#00000F这就去后巷的古董店，\x01",
            "向夫人借用\x01",
            "公寓的钥匙吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CCF1")

    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_53_CA94 end

    SaveToFile()

Try(main)
