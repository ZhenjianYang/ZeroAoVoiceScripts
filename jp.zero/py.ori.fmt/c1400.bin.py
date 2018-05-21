from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1400.bin",                # FileName
        "c1400",                    # MapName
        "c1400",                    # Location
        0x002E,                     # MapIndex
        "ed7101",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 46, 0, 4, 0, 5],
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
        "シスター・ハティナ",     # 9
        "コウキ",                 # 10
        "青装束の青年",           # 11
        "青装束の青年",           # 12
        "青装束の青年",           # 13
        "青装束の青年",           # 14
        "赤ジャージの青年",       # 15
        "赤ジャージの青年",       # 16
        "赤ジャージの青年",       # 17
        "赤ジャージの青年",       # 18
        "ワジ",                   # 19
        "ヴァルド",               # 20
        "アッバス",               # 21
        "グレイス",               # 22
        "リャン",                 # 23
        "ベッセ",                 # 24
        "アゼル",                 # 25
        "ジェド",                 # 26
        "BC1400",                 # 27
        "BC1400",                 # 28
        "BC1400",                 # 29
        "BC1400",                 # 30
        "中央広場",               # 31
        "西通り",                 # 32
        "行政区",                 # 33
        "住宅街",                 # 34
        "歓楽街",                 # 35
        "東通り",                 # 36
        "旧市街",                 # 37
        "港湾区",                 # 38
        "ＩＢＣ",                 # 39
        "駅前通り",               # 40
        "裏通り",                 # 41
        "ウルスラ間道",           # 42
        "東クロスベル街道",       # 43
        "西クロスベル街道",       # 44
        "マインツ山道",           # 45
    ))

    ATBonus("ATBonus_708", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    MonsterBattlePostion("MonsterBattlePostion_7C8", 7, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_7CC", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D0", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7D8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7DC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7E4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_7AC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_7B0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_7B4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_7B8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_7BC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_7C0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7C4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_7E8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_7EC", 8, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F4", 11, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_7F8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_7FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_800", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_804", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_808", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_80C", 5, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_810", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_814", 11, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_818", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_81C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_820", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_824", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_828", 10, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_82C", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_830", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_834", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_838", 4, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_83C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_840", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_844", 3, 10, 180)

    # monster count: 0

    # event battle count: 4

    BattleInfo(
        "BattleInfo_848", 0x0002, 3, 6, 180, 0, 0, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms30800.dat", "ms31700.dat", "ms30900.dat", "ms31800.dat", 0, 0, 0, 0, "MonsterBattlePostion_7C8", "MonsterBattlePostion_7A8", "ed7401", "ed7403", "ATBonus_708"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_88C", 0x0002, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31801.dat", "ms30901.dat", "ms30902.dat", "ms30903.dat", 0, 0, 0, 0, "MonsterBattlePostion_7E8", "MonsterBattlePostion_7A8", "ed7401", "ed7403", "ATBonus_708"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8D0", 0x0002, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31701.dat", "ms30801.dat", "ms31702.dat", "ms30802.dat", 0, 0, 0, 0, "MonsterBattlePostion_808", "MonsterBattlePostion_7A8", "ed7401", "ed7403", "ATBonus_708"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_914", 0x0022, 26, 6, 180, 0, 1, 0, 0, "BC1400", 0x00000000, 100, 0, 0, 0,
        (
            ("ms31801.dat", "ms30901.dat", "ms30902.dat", "ms30903.dat", "ms31701.dat", "ms30801.dat", "ms31702.dat", "ms30802.dat", "MonsterBattlePostion_828", "MonsterBattlePostion_7A8", "ed7402", "ed7403", "ATBonus_708"),
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
        "chr/ch25500.itc",                   # 08
    ))

    DeclNpc(44880,   -2500,   -20090,  225,  261,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(15449,   100,     -19,     270,  261,  0x0, 0,   1,   0,   255, 255, 0,   11,  255,  0)
    DeclNpc(9640,    0,       850,     180,  261,  0x0, 0,   2,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(10279,   0,       -550,    315,  261,  0x0, 0,   3,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(34080,   -6500,   -38270,  45,   261,  0x0, 0,   4,   0,   0,   1,   0,   18,  255,  0)
    DeclNpc(45090,   -2500,   -21969,  180,  405,  0x0, 0,   5,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(45099,   -2500,   -23700,  0,    405,  0x0, 0,   6,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(-17750,  0,       -9270,   225,  405,  0x0, 0,   7,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(1590,    0,       6789,    180,  389,  0x0, 0,   8,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(43650,   -2500,   -19120,  135,  389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
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

    DeclEvent(0x0000, 0, 37,  -19.450000762939453,   -6.659999847412109,    -0.7099999785423279,   16.0,                  [0.25,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.5,                   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   4.862500190734863,     3.3299999237060547,    0.1420000046491623,    1.0])

    DeclActor(-28460,  2800,    -29590,  1200,    -28460,  3800,    -29590,  0x007C, 0,  6,  0x0000)
    DeclActor(-13130,  0,       -7750,   1500,    -13130,  1500,    -7750,   0x007C, 0,  39, 0x0000)
    DeclActor(48640,   -2100,   -22590,  1500,    48640,   -600,    -22590,  0x007C, 0,  38, 0x0000)
    DeclActor(34830,   2450,    -19780,  1500,    34830,   3950,    -19780,  0x007C, 0,  40, 0x0000)

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
    PlaceName(-97.75, 0.0, 93.1500015258789, 0x0000, 0x0056, "")

    ScpFunction((
        "Function_0_A50",          # 00, 0
        "Function_1_B08",          # 01, 1
        "Function_2_B33",          # 02, 2
        "Function_3_C0C",          # 03, 3
        "Function_4_C55",          # 04, 4
        "Function_5_11B8",         # 05, 5
        "Function_6_12F1",         # 06, 6
        "Function_7_143E",         # 07, 7
        "Function_8_2189",         # 08, 8
        "Function_9_2303",         # 09, 9
        "Function_10_2545",        # 0A, 10
        "Function_11_29CA",        # 0B, 11
        "Function_12_326B",        # 0C, 12
        "Function_13_3BBE",        # 0D, 13
        "Function_14_3C99",        # 0E, 14
        "Function_15_3D47",        # 0F, 15
        "Function_16_3E9C",        # 10, 16
        "Function_17_3F8A",        # 11, 17
        "Function_18_45D1",        # 12, 18
        "Function_19_5254",        # 13, 19
        "Function_20_53BA",        # 14, 20
        "Function_21_55BB",        # 15, 21
        "Function_22_561E",        # 16, 22
        "Function_23_5A69",        # 17, 23
        "Function_24_5BB4",        # 18, 24
        "Function_25_6001",        # 19, 25
        "Function_26_743B",        # 1A, 26
        "Function_27_A6C9",        # 1B, 27
        "Function_28_A6FF",        # 1C, 28
        "Function_29_A735",        # 1D, 29
        "Function_30_A790",        # 1E, 30
        "Function_31_A7F5",        # 1F, 31
        "Function_32_A83B",        # 20, 32
        "Function_33_A885",        # 21, 33
        "Function_34_A8C6",        # 22, 34
        "Function_35_B827",        # 23, 35
        "Function_36_CD23",        # 24, 36
        "Function_37_D94C",        # 25, 37
        "Function_38_DA56",        # 26, 38
        "Function_39_DB8A",        # 27, 39
        "Function_40_DBE1",        # 28, 40
        "Function_41_DCBD",        # 29, 41
        "Function_42_E33A",        # 2A, 42
        "Function_43_E5D1",        # 2B, 43
        "Function_44_EA11",        # 2C, 44
        "Function_45_EDDE",        # 2D, 45
        "Function_46_101A7",       # 2E, 46
        "Function_47_10E1A",       # 2F, 47
        "Function_48_10E32",       # 30, 48
        "Function_49_10E4A",       # 31, 49
        "Function_50_1158A",       # 32, 50
        "Function_51_11F15",       # 33, 51
        "Function_52_1262F",       # 34, 52
        "Function_53_12644",       # 35, 53
        "Function_54_12659",       # 36, 54
        "Function_55_1266E",       # 37, 55
        "Function_56_12683",       # 38, 56
        "Function_57_126A9",       # 39, 57
        "Function_58_126FA",       # 3A, 58
        "Function_59_1274B",       # 3B, 59
        "Function_60_1279C",       # 3C, 60
        "Function_61_127ED",       # 3D, 61
    ))


    def Function_0_A50(): pass

    label("Function_0_A50")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A90"),
        (1, "loc_A9C"),
        (2, "loc_AA8"),
        (3, "loc_AB4"),
        (4, "loc_AC0"),
        (5, "loc_ACC"),
        (6, "loc_AD8"),
        (SWITCH_DEFAULT, "loc_AE4"),
    )


    label("loc_A90")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_A9C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AA8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AB4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AC0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_ACC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AD8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AE4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_AF0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B07")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AF0")

    label("loc_B07")

    Return()

    # Function_0_A50 end

    def Function_1_B08(): pass

    label("Function_1_B08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B32")
    OP_94(0xFE, 0x8D04, 0xFFFF6E7E, 0x7800, 0xFFFF612C, 0x3E8)
    Sleep(300)
    Jump("Function_1_B08")

    label("loc_B32")

    Return()

    # Function_1_B08 end

    def Function_2_B33(): pass

    label("Function_2_B33")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C0B")
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
    Jump("Function_2_B33")

    label("loc_C0B")

    Return()

    # Function_2_B33 end

    def Function_3_C0C(): pass

    label("Function_3_C0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C54")
    Sleep(4000)
    OP_95(0xFE, -6960, -3800, -27910, 1000, 0x0)
    Sleep(4000)
    OP_95(0xFE, -13650, -3010, -25240, 1000, 0x0)
    OP_93(0xFE, 0xE1, 0x12C)
    Sleep(1900)
    Jump("Function_3_C0C")

    label("loc_C54")

    Return()

    # Function_3_C0C end

    def Function_4_C55(): pass

    label("Function_4_C55")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D32")
    SetChrPos(0x0, 2050, 0, 14590, 180)
    SetChrPos(0x1, 2050, 0, 14590, 180)
    SetChrPos(0x2, 2050, 0, 14590, 180)
    SetChrPos(0x3, 2050, 0, 14590, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CDC")
    SetChrPos(0x4, 2050, 0, 14590, 180)
    SetChrPos(0x5, 2050, 0, 14590, 180)
    Jump("loc_CFB")

    label("loc_CDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFB")
    SetChrPos(0x4, 2050, 0, 14590, 180)

    label("loc_CFB")

    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D32")

    OP_D0(0x7, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xCD, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D51")
    Event(0, 41)
    Jump("loc_D9B")

    label("loc_D51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D67")
    Event(0, 35)
    Jump("loc_D9B")

    label("loc_D67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D82")
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_D9B")

    label("loc_D82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9B")
    Event(0, 36)

    label("loc_D9B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_DAF")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 26)
    Jump("loc_DBE")

    label("loc_DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_DBE")
    ClearScenarioFlags(0x5C, 1)
    Event(0, 43)

    label("loc_DBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_DDB")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_11A0")

    label("loc_DDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_E26")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_11A0")

    label("loc_E26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_E4C")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 0)), scpexpr(EXPR_END)), "loc_E47")
    SetChrFlags(0x8, 0x80)

    label("loc_E47")

    Jump("loc_11A0")

    label("loc_E4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_E5F")
    SetChrFlags(0x8, 0x80)
    Jump("loc_11A0")

    label("loc_E5F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_E77")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    Jump("loc_11A0")

    label("loc_E77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_E99")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jump("loc_11A0")

    label("loc_E99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_EFA")
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 11340, 0, 1320, 225)
    OP_93(0x8, 0x2D, 0x0)
    TurnDirection(0xA, 0x10, 0)
    TurnDirection(0xB, 0x10, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDC")
    SetChrFlags(0x8, 0x10)

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EF5")
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    SetChrFlags(0x10, 0x10)

    label("loc_EF5")

    Jump("loc_11A0")

    label("loc_EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_F75")
    ClearChrFlags(0x10, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_F38")
    SetChrPos(0xA, -10970, 0, -9240, 135)
    SetChrPos(0xB, -11920, 0, -9620, 45)
    Jump("loc_F70")

    label("loc_F38")

    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)

    label("loc_F70")

    Jump("loc_11A0")

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_FB4")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xD, 2820, 0, -2350, 45)
    SetChrPos(0xE, 3020, 0, -950, 45)
    Jump("loc_11A0")

    label("loc_FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_FF7")
    SetChrPos(0xA, 1220, 0, -1610, 135)
    SetChrPos(0xB, 2410, 0, -2740, 315)
    SetChrFlags(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_FF2")
    SetChrFlags(0xA, 0x10)

    label("loc_FF2")

    Jump("loc_11A0")

    label("loc_FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1058")
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xA, 0x10)
    SetChrPos(0xA, -11120, -220, -14560, 45)
    SetChrPos(0xB, -11150, -820, -15530, 45)
    SetChrPos(0xD, 5010, 0, -7740, 0)
    SetChrPos(0xE, 4090, 0, -6750, 45)
    Jump("loc_11A0")

    label("loc_1058")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_10BD")
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    OP_93(0x8, 0x13B, 0x0)
    SetChrFlags(0x8, 0x10)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_10B8")
    SetChrFlags(0x11, 0x10)

    label("loc_10B8")

    Jump("loc_11A0")

    label("loc_10BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_1112")
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0xA, 0x4)
    ClearChrFlags(0xB, 0x4)
    SetChrPos(0xA, 5840, 0, -6890, 135)
    SetChrPos(0xB, 4760, 0, -5890, 135)
    SetChrFlags(0xA, 0x10)
    SetChrFlags(0xB, 0x10)
    BeginChrThread(0xA, 0, 0, 2)
    BeginChrThread(0xB, 0, 0, 2)
    Jump("loc_11A0")

    label("loc_1112")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_1172")
    SetChrPos(0xA, 8620, 0, 8810, 180)
    SetChrPos(0xB, 7900, 0, 9630, 135)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_115C")
    SetChrPos(0x8, 44880, -2500, -20090, 225)
    Jump("loc_116D")

    label("loc_115C")

    SetChrPos(0x8, 48000, -2100, -22500, 270)

    label("loc_116D")

    Jump("loc_11A0")

    label("loc_1172")

    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0x8, 48000, -2100, -22500, 270)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_11A0")
    SetChrFlags(0xA, 0x10)

    label("loc_11A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x45, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11B7")
    SetMapFlags(0x10000000)
    Event(0, 24)

    label("loc_11B7")

    Return()

    # Function_4_C55 end

    def Function_5_11B8(): pass

    label("Function_5_11B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CF")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_11CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x81, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F9")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_122C")

    label("loc_11F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_121E")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Jump("loc_122C")

    label("loc_121E")

    SetMapObjFrame(0xFF, "sd_mul", 0x1, 0x1)

    label("loc_122C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123F")
    OP_70(0x7, 0x0)
    Jump("loc_1243")

    label("loc_123F")

    OP_70(0x7, 0x1E)

    label("loc_1243")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_125B")

    OP_65(0x2, 0x1)
    SetMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x41, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1279")
    ClearMapObjFlags(0x4, 0x10)

    label("loc_1279")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1291")
    OP_66(0x1, 0x1)
    ClearMapObjFlags(0x2, 0x10)

    label("loc_1291")

    OP_65(0x3, 0x1)
    SetMapObjFlags(0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AF")
    OP_66(0x3, 0x1)
    ClearMapObjFlags(0x1, 0x10)

    label("loc_12AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12CB")
    Jump("loc_12D0")

    label("loc_12CB")

    OP_16(0x3, 0x1D, 0x1, 0x0)

    label("loc_12D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_12F0")
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_12F0")

    Return()

    # Function_5_11B8 end

    def Function_6_12F1(): pass

    label("Function_6_12F1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x110, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13ED")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x642, 1)"), scpexpr(EXPR_END)), "loc_1376")
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
    Jump("loc_13E8")

    label("loc_1376")

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

    label("loc_13E8")

    Jump("loc_1432")

    label("loc_13ED")

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

    label("loc_1432")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_12F1 end

    def Function_7_143E(): pass

    label("Function_7_143E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1454")
    Call(0, 34)
    Jump("loc_2188")

    label("loc_1454")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_146F")
    Call(0, 10)
    Jump("loc_2188")

    label("loc_146F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_156E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_14F3")

    #C0004
    ChrTalk(
        0x8,
        (
            "……入るか？\x01",
            "中の連中、今ごろビビッてるぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x8,
        (
            "ハハハ、これで明日からは\x01",
            "俺がバイパーの大幹部だな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1569")

    label("loc_14F3")


    #C0006
    ChrTalk(
        0x8,
        "ハハッ、すかっとしたぜ。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x8,
        "あいつ前から気に入らなかったんだ。\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x8,
        (
            "人に雑用ばっか\x01",
            "押し付けやがってよォ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1569")

    Jump("loc_2185")

    label("loc_156E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_1706")
    OP_64(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16B0")

    #C0009
    ChrTalk(
        0xFE,
        (
            "俺……祭りの最終日に\x01",
            "ガラの悪い観光客に絡まれちまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "頑張ってケンカしたのに……\x01",
            "ま、負けちまったんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "俺、バイパーのメンバーなのに……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A5")

    #C0012
    ChrTalk(
        0x101,
        (
            "#0003Fそ、そうか。\x01",
            "（この子、喧嘩弱そうだしな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x153,
        (
            "#1111F？？？\x01",
            "（へんなカッコウ～。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16A5")

    SetScenarioFlags(0xD8, 2)
    SetScenarioFlags(0x0, 0)
    Jump("loc_16EF")

    label("loc_16B0")


    #C0014
    ChrTalk(
        0xFE,
        (
            "………………………………\x01",
            "俺、バイパーのメンバーなのに……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16EF")

    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_2185")

    label("loc_1706")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_174A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1742")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 0)), scpexpr(EXPR_END)), "loc_172C")
    Call(0, 8)
    Jump("loc_173D")

    label("loc_172C")

    TurnDirection(0x8, 0x0, 0)
    Call(0, 9)
    OP_93(0x8, 0x2D, 0x0)

    label("loc_173D")

    Jump("loc_1745")

    label("loc_1742")

    Call(0, 8)

    label("loc_1745")

    Jump("loc_2185")

    label("loc_174A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1824")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_17A0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x91, 0)), scpexpr(EXPR_END)), "loc_1798")

    #C0015
    ChrTalk(
        0x8,
        (
            "お、俺もいつか\x01",
            "喧嘩に参加するんだ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179B")

    label("loc_1798")

    Call(0, 9)

    label("loc_179B")

    Jump("loc_181F")

    label("loc_17A0")


    #C0016
    ChrTalk(
        0x8,
        (
            "いいなぁ、俺も\x01",
            "朝稽古に参加したかったなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x8,
        (
            "へへ……そんでもって\x01",
            "いつかヴァルドさんみたいに\x01",
            "強い男になるんだ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181F")

    Jump("loc_2185")

    label("loc_1824")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_1976")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_18BB")

    #C0018
    ChrTalk(
        0xFE,
        (
            "俺もバイパーのメンバーなんだし。\x01",
            "今年からはお祭りも遊ばないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "……言っとくけど、別に\x01",
            "残念なんかじゃないからな！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1971")

    label("loc_18BB")


    #C0020
    ChrTalk(
        0xFE,
        (
            "記念祭が近いからって、\x01",
            "浮かれてるヤツを見かけるけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        "フ、フン、そんなのガキ臭いよな。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "サーベルバイパーは硬派なんだ。\x01",
            "お祭りだからって\x01",
            "喜んだりしないんだからな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1971")

    Jump("loc_2185")

    label("loc_1976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_19E2")

    #C0023
    ChrTalk(
        0x8,
        "もう騙されないぞ。\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "しっしっ、あっちに行けよ！\x01",
            "先輩たちの邪魔になるだろっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A8C")

    label("loc_19E2")


    #C0025
    ChrTalk(
        0x8,
        "オッス、お疲れ様です！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0026
    ChrTalk(
        0x8,
        "って、またお前たちじゃないか！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "もう……\x01",
            "わざとやってるだろっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0006Fいや、わざとじゃ\x01",
            "ないんだけどな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1A8C")

    Jump("loc_2185")

    label("loc_1A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1CE5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1B7C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1B08")

    #C0029
    ChrTalk(
        0x8,
        (
            "オレ、ちゃんと挨拶できたんだ！\x01",
            "ヴァルドさんは\x01",
            "オウって言っただけだったけどな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B77")

    label("loc_1B08")


    #C0030
    ChrTalk(
        0x8,
        (
            "さっきヴァルドさんが\x01",
            "戻ってきたんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "オッス、お疲れ様です！\x01",
            "……オレ、ちゃんと挨拶できたんだ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1B77")

    Jump("loc_1CE0")

    label("loc_1B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1C63")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x2)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6F, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C2F")

    #C0032
    ChrTalk(
        0xFE,
        (
            "そういや、なんだかドタンバタンって\x01",
            "変な音がするなぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "イグニスからじゃないみたいだけど……\x01",
            "どこから聞こえてくるんだろ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C5E")

    label("loc_1C2F")


    #C0034
    ChrTalk(
        0x8,
        (
            "先輩たちは忙しいんだぞ！\x01",
            "邪魔すんなよっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C5E")

    Jump("loc_1CE0")

    label("loc_1C63")


    #C0035
    ChrTalk(
        0x8,
        "オッス、お疲れ様です！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0036
    ChrTalk(
        0x8,
        "って、お前たちじゃないか！\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "もう……\x01",
            "紛らわしい真似すんなよっ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1CE0")

    Jump("loc_2185")

    label("loc_1CE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_1D53")
    OP_4B(0x11, 0xFF)

    #C0038
    ChrTalk(
        0x8,
        "うっす！\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x11,
        "うっすじゃなくてオッスだ！\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0040
    ChrTalk(
        0x8,
        "オ、オッス！\x02",
    )

    CloseMessageWindow()
    OP_64(0x8)
    OP_4C(0x11, 0xFF)
    Jump("loc_2185")

    label("loc_1D53")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_1E40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1DC2")

    #C0041
    ChrTalk(
        0x8,
        (
            "俺、今度病院まで\x01",
            "お見舞いに行くんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "……じゃ、邪魔したら\x01",
            "許さないからな！？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E3B")

    label("loc_1DC2")


    #C0043
    ChrTalk(
        0x8,
        (
            "テスタメンツの\x01",
            "連中にやられたのは\x01",
            "コウキっていう先輩だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        (
            "俺のこと、一番\x01",
            "可愛がってくれてたのに\x01",
            "……ぐす……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1E3B")

    Jump("loc_2185")

    label("loc_1E40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 3)), scpexpr(EXPR_END)), "loc_1FDE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_1E92")

    #C0045
    ChrTalk(
        0x8,
        (
            "と、とっとと帰れよっ！\x01",
            "もう信用してやらないからな！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FD9")

    label("loc_1E92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4E, 6)), scpexpr(EXPR_END)), "loc_1EFF")

    #C0046
    ChrTalk(
        0x8,
        "ヴァ、ヴァルドさんをよくも……\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "と、とっとと帰れよっ！\x01",
            "もう信用してやらないからな！！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F71")

    label("loc_1EFF")


    #C0048
    ChrTalk(
        0x8,
        (
            "あ、あのヴァルドさんと\x01",
            "引き分けるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        (
            "お前、さては何かズルしただろっ！\x01",
            "俺は知ってるんだからな！！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F71")


    #C0050
    ChrTalk(
        0x101,
        "#0003F（うーん、この子……）\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#0300F（ああ、ヴァルドって奴に\x01",
            "  憧れちゃってるみたいだな。）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)

    label("loc_1FD9")

    Jump("loc_2185")

    label("loc_1FDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 2)), scpexpr(EXPR_END)), "loc_2050")

    #C0052
    ChrTalk(
        0x8,
        "ヴァルドさんがお呼びだ！\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        (
            "入ってもいいけど……\x01",
            "変なことをしたら\x01",
            "タダじゃ済まさないからな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2185")

    label("loc_2050")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_2109")

    #N0054
    NpcTalk(
        0xFE,
        "赤ジャージの少年",
        (
            "こらっ、警察が\x01",
            "何見てるんだよっ！\x02",
        )
    )

    CloseMessageWindow()

    #N0055
    NpcTalk(
        0xFE,
        "赤ジャージの少年",
        "とっとと帰れよなっ！\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#0001F（仕方ない……\x01",
            "  先にもう一方のグループを\x01",
            "  訪ねてみるか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2185")

    label("loc_2109")


    #N0057
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        (
            "な、何だよおまえら！\x01",
            "何見てるんだよっ！\x02",
        )
    )

    CloseMessageWindow()

    #N0058
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "とっととあっちへ行けよっ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2185")
    SetScenarioFlags(0x53, 4)

    label("loc_2185")

    TalkEnd(0xFE)

    label("loc_2188")

    Return()

    # Function_7_143E end

    def Function_8_2189(): pass

    label("Function_8_2189")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_2218")

    #C0059
    ChrTalk(
        0x8,
        (
            "俺だって、いずれは\x01",
            "木刀をもらえるハズなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x8,
        (
            "そしたらお前たちだって\x01",
            "テスタメンツだって\x01",
            "ボコボコにしてやるんだからな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2302")

    label("loc_2218")


    #C0061
    ChrTalk(
        0x8,
        (
            "しゅっ、しゅっ……！\x01",
            "おりゃ～！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x0, 500)

    #C0062
    ChrTalk(
        0x8,
        "な、なんだよ！\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x8,
        (
            "ケンカの稽古をしてるんだ。\x01",
            "邪魔すんなよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#0305Fケンカの稽古って……\x01",
            "イメージトレーニングか？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x8,
        (
            "ぼ、木刀持ってないんだから\x01",
            "仕方ないだろっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x2D, 0x0)
    ClearChrFlags(0x8, 0x10)
    SetScenarioFlags(0x0, 0)

    label("loc_2302")

    Return()

    # Function_8_2189 end

    def Function_9_2303(): pass

    label("Function_9_2303")


    #C0066
    ChrTalk(
        0x8,
        (
            "こ、こらお前ら！\x01",
            "どのツラさげて来たんだよっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x8,
        "ぶ、ぶ、ぶ……ぶっ飛ばすぞっ！？\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#0002Fえっと、いつも見張りご苦労様。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x8,
        "ううっ、馬鹿にするなよっ！\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x8,
        (
            "お、俺だって次の喧嘩には\x01",
            "参加させてもらうんだからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x103,
        (
            "#0205Fそういえば……あなたは稽古に\x01",
            "来ていませんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x8,
        (
            "……ジェド先輩、俺だけ置いて\x01",
            "喧嘩に行っちまってたんだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x8,
        (
            "あ、でももう帰ってきたからな！\x01",
            "寂しくなんかないぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x104,
        (
            "#0303Fあー、なんだその、\x01",
            "悪かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        (
            "#0100Fまた一緒に\x01",
            "稽古ができるといいわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(500)

    #C0076
    ChrTalk(
        0x8,
        (
            "な、なんだよ！\x01",
            "馬鹿にするなって言ってるだろっ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x8)
    SetScenarioFlags(0x91, 0)
    Return()

    # Function_9_2303 end

    def Function_10_2545(): pass

    label("Function_10_2545")

    EventBegin(0x0)
    Fade(500)
    OP_68(45000, -1500, -22500, 0)
    MoveCamera(37, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 43700, -2500, -23300, 90)
    SetChrPos(0x102, 43700, -2500, -21900, 90)
    SetChrPos(0x103, 42600, -2500, -23100, 90)
    SetChrPos(0x104, 42600, -2500, -21700, 90)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 47500, -2100, -22500, 270)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #N0077
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "お、お前らは……！\x02",
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x101,
        (
            "#6P#0005Fその格好……\x02\x03",

            "#0001Fひょっとしてここが\x01",
            "『サーベルバイパー』の？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        (
            "#3P#0200Fライブハウス『イグニス』……\x02\x03",

            "元々、倉庫だった場所を\x01",
            "改装した店のようですね。\x02\x03",

            "#0203F税金が払われていないので\x01",
            "詳細は判りませんが……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2703():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2703)
    WaitChrThread(0x8, 1)

    #N0080
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "む、無視すんなよ！\x02",
    )

    CloseMessageWindow()

    #N0081
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        (
            "いくら俺が新米だからって\x01",
            "サーベルバイパーの一員なんだぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#6P#0005Fああ……ゴメン。\x02\x03",

            "#0000Fその、君たちのヘッドに\x01",
            "話を聞きたくて来たんだけど……\x02\x03",

            "取り次いでもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    #N0083
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "ヴァルドさんに？\x02",
    )

    CloseMessageWindow()

    #N0084
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        (
            "フン、お前らみたいな警察と\x01",
            "ヴァルドさんが話をするもんか！\x02",
        )
    )

    CloseMessageWindow()

    #N0085
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "ほら、とっとと帰れよなっ！\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x101,
        (
            "#6P#0003F（うーん、簡単には\x01",
            "  入れてくれなさそうだな……）\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x104,
        (
            "#0300F（腕ずくっつーのも\x01",
            "  大人げねえしな。）\x02\x03",

            "（先にもう一方のグループを\x01",
            "  訪ねてみるか？）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x102,
        (
            "#0101F（そうね……その後で\x01",
            "  もう一度寄ってみましょう。）\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 48000, -2100, -22500, 270)
    SetChrPos(0x0, 43000, -2500, -22500, 90)
    SetScenarioFlags(0x52, 7)
    EventEnd(0x5)
    Return()

    # Function_10_2545 end

    def Function_11_29CA(): pass

    label("Function_11_29CA")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A5E")
    Jump("loc_2AA8")

    label("loc_2A5E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2A7E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AA8")

    label("loc_2A7E")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A9E")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AA8")

    label("loc_2A9E")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AA8")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_2B44")

    #C0089
    ChrTalk(
        0x9,
        (
            "あら、日が暮れてきた\x01",
            "みたいですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x9,
        (
            "わたしもそろそろ、\x01",
            "おうちに帰らなくちゃ\x01",
            "いけませんねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2B44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2BA3")

    #C0091
    ChrTalk(
        0x9,
        "あ、あら……なにかしら。\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x9,
        (
            "わたしは耳が遠くて、\x01",
            "よく聞こえないんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2BA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2C17")

    #C0093
    ChrTalk(
        0x9,
        (
            "さっき、そこにチョウチョが\x01",
            "飛んでいたのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x9,
        (
            "うふふ……すっかり\x01",
            "暖かくなったみたいですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2C17")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_2CFE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C9C")

    #C0095
    ChrTalk(
        0xFE,
        (
            "最近不良の子達の\x01",
            "様子がおかしいですねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xFE,
        (
            "はて……わたしは耳が遠いので\x01",
            "よくは知りませんけれど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2CF9")

    label("loc_2C9C")


    #C0097
    ChrTalk(
        0xFE,
        (
            "赤ジャージの子達の様子が\x01",
            "どことなくおかしいですねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xFE,
        "何かあったんでしょうかねぇ。\x02",
    )

    CloseMessageWindow()

    label("loc_2CF9")

    Jump("loc_3263")

    label("loc_2CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_2D37")

    #C0099
    ChrTalk(
        0x9,
        (
            "うとうと……\x01",
            "今日もいい天気ですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2D37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_2D9E")

    #C0100
    ChrTalk(
        0x9,
        "うとうと……あらいけない。\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x9,
        (
            "暖かくなってくると\x01",
            "つい居眠りをしてしまいますねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2D9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_2E18")

    #C0102
    ChrTalk(
        0x9,
        (
            "わたしは足が悪いんです、\x01",
            "遠くへは歩いていけないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x9,
        (
            "その分、子供達が元気だと\x01",
            "嬉しくなるんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2E18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_2E80")

    #C0104
    ChrTalk(
        0x9,
        (
            "今日の晩御飯は\x01",
            "なににしようかしら……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x9,
        (
            "たまにはおいしいものを\x01",
            "食べたいですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_2EF8")

    #C0106
    ChrTalk(
        0x9,
        "あら……何かご用かしら？\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x9,
        (
            "さっきも何か聞いてきた人が\x01",
            "いたんだけど……\x01",
            "わたしは耳が遠いんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2EF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_2F57")

    #C0108
    ChrTalk(
        0x9,
        "あらあら、ジャージの子が……\x02",
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x9,
        (
            "最近よく見るけれど、\x01",
            "何かあるのかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_2F57")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_3020")

    #C0110
    ChrTalk(
        0x9,
        (
            "クロスベルに駅ができたのは\x01",
            "２０年ほど前のことだったかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x9,
        (
            "あの時は街中浮かれてしまって\x01",
            "大騒ぎだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x9,
        (
            "いまでは空港までできて、昔と比べると\x01",
            "本当に便利になりましたねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_3020")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_308B")

    #C0113
    ChrTalk(
        0x9,
        "子供たちは今日も元気ですねぇ。\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x9,
        (
            "お日様もぽかぽかだし、\x01",
            "いい一日になりそうですねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_308B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_3118")

    #C0115
    ChrTalk(
        0x9,
        (
            "ジャージの子達は\x01",
            "よくここを通りがかるんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x9,
        (
            "わたしは耳が遠くて、\x01",
            "よく判らないけれど……\x01",
            "みんな元気がいいわねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_3118")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_31AA")

    #C0117
    ChrTalk(
        0x9,
        "おや、何かあったのかしら。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x9,
        (
            "若い子たちが\x01",
            "集まっていたみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x9,
        (
            "わたしは耳が遠くて、\x01",
            "よく聞き取れないんですよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_31AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3210")

    #C0120
    ChrTalk(
        0x9,
        (
            "あ、あら……\x01",
            "わたしに何か用かしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x9,
        (
            "ごめんなさいねぇ、\x01",
            "わたし、耳が遠くって。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3263")

    label("loc_3210")


    #C0122
    ChrTalk(
        0x9,
        (
            "ああ、今日も\x01",
            "いい天気ですねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x9,
        (
            "また日向ぼっこでも\x01",
            "しましょうかねぇ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)

    label("loc_3263")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_11_29CA end

    def Function_12_326B(): pass

    label("Function_12_326B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_334A")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_32EC")

    #C0124
    ChrTalk(
        0xFE,
        "ニシシ……またなんかの喧嘩か～？\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "シスターの授業より\x01",
            "そっちの方がおもしれーっ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xFE, 0x5A, 0x0)
    Jump("loc_3345")

    label("loc_32EC")


    #C0126
    ChrTalk(
        0xFE,
        "ニシシ……またなんかの喧嘩か～？\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xFE,
        (
            "シスターの授業より\x01",
            "こっちの方がおもしれーっ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3345")

    Jump("loc_3BBA")

    label("loc_334A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_33D5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_33CD")
    OP_4B(0xB, 0xFF)

    #C0128
    ChrTalk(
        0xA,
        (
            "クソオヤジは一日じゅー\x01",
            "飲んだくれてんもんなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            "しょーがねー、\x01",
            "残飯でももらいに行くか～？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_33D0")

    label("loc_33CD")

    Call(0, 13)

    label("loc_33D0")

    Jump("loc_3BBA")

    label("loc_33D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_342E")

    #C0130
    ChrTalk(
        0xA,
        (
            "今日は不良の兄ちゃんたち、\x01",
            "見かけねーなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xA,
        "キャハ、つまんねー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BBA")

    label("loc_342E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_34C2")
    OP_4B(0xB, 0xFF)

    #C0132
    ChrTalk(
        0xA,
        (
            "あの不良の兄ちゃん、\x01",
            "ちょーおっかねえよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xA,
        "薄気味悪いしよぉ～……\x02",
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xA,
        (
            "ルゼ、ああいうのには\x01",
            "ぜってー近づくなよ？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_3BBA")

    label("loc_34C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_3534")

    #C0135
    ChrTalk(
        0xFE,
        (
            "あのシスター、ジンゴんとこに\x01",
            "行ったみたいだなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "ニシシ……今のうちに\x01",
            "隠れちまおうぜっ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BBA")

    label("loc_3534")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_3545")
    Call(0, 14)
    Jump("loc_3BBA")

    label("loc_3545")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_359B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3593")

    #C0137
    ChrTalk(
        0xA,
        (
            "ニヒヒ、授業なんか\x01",
            "またひっかきまわしてやるぜー！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3596")

    label("loc_3593")

    Call(0, 15)

    label("loc_3596")

    Jump("loc_3BBA")

    label("loc_359B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_3644")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_35F3")

    #C0138
    ChrTalk(
        0xA,
        (
            "オーレのオヤジーは\x01",
            "酒飲みで～い……♪\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xA,
        "キャハハハハハ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_363F")

    label("loc_35F3")


    #C0140
    ChrTalk(
        0xA,
        (
            "キャハハ！\x01",
            "ルゼ、今日は何して遊ぶ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0xA,
        "木箱くずしでもやっか～？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_363F")

    Jump("loc_3BBA")

    label("loc_3644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_36BA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_36B2")
    OP_4B(0xB, 0xFF)

    #C0142
    ChrTalk(
        0xA,
        (
            "でもオヤジ、\x01",
            "いつも飲んだくれてっからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        "たたいても起きっかなー。\x02",
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_36B5")

    label("loc_36B2")

    Call(0, 16)

    label("loc_36B5")

    Jump("loc_3BBA")

    label("loc_36BA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_3772")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_370A")
    OP_4B(0xB, 0xFF)

    #C0144
    ChrTalk(
        0xA,
        (
            "二ヒヒ……次はネズミでも\x01",
            "捕まえてくっか～？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_376D")

    label("loc_370A")


    #C0145
    ChrTalk(
        0xA,
        (
            "ここの下水に\x01",
            "イモリを落としてんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xA,
        (
            "ボチャン、ボチャ～ン！\x01",
            "キャハハハハ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0x87, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_376D")

    Jump("loc_3BBA")

    label("loc_3772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_37E0")
    OP_4B(0xB, 0xFF)

    #C0147
    ChrTalk(
        0xA,
        (
            "やべーぞルゼ、\x01",
            "ちょっと隠れろっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xA,
        (
            "二ヒヒ……また\x01",
            "乱闘の相談でもしてんのか～？\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xB, 0xFF)
    Jump("loc_3BBA")

    label("loc_37E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_38D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3877")

    #C0149
    ChrTalk(
        0xA,
        (
            "オレのオヤジ、まだ部屋で\x01",
            "飲んだくれてやがんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        "もう昼間だってのによ。\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0xA,
        (
            "キャハハ、酒しか飲まねー\x01",
            "ダメ人間～！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_38D1")

    label("loc_3877")


    #C0152
    ChrTalk(
        0xA,
        (
            "オヤジ、まだ\x01",
            "飲んだくれてるみたいだなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0xA,
        (
            "キャハハ、酒しか飲まねー\x01",
            "ダメ人間～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_38D1")

    Jump("loc_3BBA")

    label("loc_38D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_3918")

    #C0154
    ChrTalk(
        0xA,
        "オレのオヤジは酒飲みで～い！\x02",
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0xA,
        "ひゃっほ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3BBA")

    label("loc_3918")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_39E0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3984")

    #C0156
    ChrTalk(
        0xA,
        (
            "不良のにーちゃんたち、\x01",
            "やけにガマン強いなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xA,
        "……乱闘、やんねーのかなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_39DB")

    label("loc_3984")


    #C0158
    ChrTalk(
        0xA,
        (
            "うりー……？\x01",
            "今日こそ乱闘だと思ったのになー。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xA,
        "どうしちまったんだー？\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_39DB")

    Jump("loc_3BBA")

    label("loc_39E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_3AD1")
    OP_4B(0xB, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A6C")
    OP_93(0xFE, 0xB4, 0x0)

    #C0160
    ChrTalk(
        0xA,
        (
            "ニヒヒ、あっぶねー。\x01",
            "今日はいよいよってカンジだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xA,
        (
            "ルゼ、おめー\x01",
            "絶対前に出るんじゃねーぞ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AC8")

    label("loc_3A6C")


    #C0162
    ChrTalk(
        0xFE,
        (
            "あの兄ちゃんら、\x01",
            "ぜってーすぐに戻ってくんぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0xFE,
        (
            "ニシシッ……\x01",
            "今日はちょーやべーぞ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AC8")

    OP_4C(0xB, 0xFF)
    Jump("loc_3BBA")

    label("loc_3AD1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_3B32")

    #C0164
    ChrTalk(
        0xA,
        "んで次は何して遊ぶ～？\x02",
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xA,
        (
            "キャハハ、水道管に穴あけて\x01",
            "水浸しにしちまうか～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3BBA")

    label("loc_3B32")


    #C0166
    ChrTalk(
        0xA,
        "お、市街の連中だ。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0xA,
        "キャハ、オメーら気をつけろよー。\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xA,
        (
            "この辺りの不良グループ、\x01",
            "今すげーピリピリしてっから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0xA, 0xB4, 0x0)
    SetChrFlags(0xA, 0x10)
    SetScenarioFlags(0x0, 2)

    label("loc_3BBA")

    TalkEnd(0xFE)
    Return()

    # Function_12_326B end

    def Function_13_3BBE(): pass

    label("Function_13_3BBE")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0169
    ChrTalk(
        0xB,
        "今日も何も食べなかったね。\x02",
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0xB,
        (
            "クスクス……あたし\x01",
            "おなか減っちゃったな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xA,
        (
            "しょーがねー、\x01",
            "残飯でももらいに行くか～？\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0xA,
        (
            "オラオラァ……\x01",
            "メシ食わせろ～っ！\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xB,
        "キャハハ、メシ食わせろ～！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_13_3BBE end

    def Function_14_3C99(): pass

    label("Function_14_3C99")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0174
    ChrTalk(
        0xA,
        (
            "最近シスターのヤロー、\x01",
            "ウゼエよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xA,
        "なんで毎週くるんだ～？\x02",
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0xB,
        "クスクス……知らな～い。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xB,
        (
            "ヴァンが追い返しちゃうから\x01",
            "何でもいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_14_3C99 end

    def Function_15_3D47(): pass

    label("Function_15_3D47")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_4B(0x10, 0xFF)

    #C0178
    ChrTalk(
        0xA,
        "んだよ、また来たのかー？\x02",
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xB,
        (
            "クスクス……しすたーの\x01",
            "懲りないおねーさんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x10,
        "ええ、懲りませんとも。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x10,
        (
            "……さぁ、早速\x01",
            "場所を移動しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x10,
        (
            "今日こそはきちんと授業を\x01",
            "受けてもらいますからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xA,
        "ニヒヒ、ナマイキな女だなー。\x02",
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x10,
        (
            "ふう……まずは言葉遣いから\x01",
            "教えないといけませんね。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    ClearChrFlags(0x10, 0x10)
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0x10, 0xFF)
    Return()

    # Function_15_3D47 end

    def Function_16_3E9C(): pass

    label("Function_16_3E9C")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0185
    ChrTalk(
        0xA,
        "きねんさい～？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xA,
        "ルゼ、おめーアテでもあんのか～？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xB,
        "ううん、なんにもないよ。\x02",
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "ヴァンがいるだけだもん。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0xA,
        "ちぇっ、つまんねーなー。\x02",
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xA,
        (
            "オヤジをたたき起こして\x01",
            "どっか連れてってもらうか～？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Return()

    # Function_16_3E9C end

    def Function_17_3F8A(): pass

    label("Function_17_3F8A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_407B")
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_4017")

    #C0191
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "お兄ちゃんたち強いんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "もし……あたしが危ない目にあったら\x01",
            "助けてほしいなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4066")

    label("loc_4017")


    #C0193
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "お兄ちゃんたち結構強いんだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        "最後は負けちゃったけど。\x02",
    )

    CloseMessageWindow()

    label("loc_4066")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4076")
    OP_93(0xFE, 0x2D, 0x0)

    label("loc_4076")

    Jump("loc_45CD")

    label("loc_407B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4106")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_40FE")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0195
    ChrTalk(
        0xB,
        (
            "りゅーろーの店なら\x01",
            "おねーちゃん優しいものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "メシ分けてもらおっと。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_4101")

    label("loc_40FE")

    Call(0, 13)

    label("loc_4101")

    Jump("loc_45CD")

    label("loc_4106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_4164")

    #C0197
    ChrTalk(
        0xB,
        (
            "あたし、青い人たちの\x01",
            "ヘッドなら見たよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "何してたのかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CD")

    label("loc_4164")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_41A5")
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0199
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "うん、わかった。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    Jump("loc_45CD")

    label("loc_41A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_421B")

    #C0200
    ChrTalk(
        0xFE,
        (
            "ジンゴちゃんね、まだ一度も\x01",
            "シスターの授業受けてないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "クスクス……\x01",
            "シスターも大変だね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CD")

    label("loc_421B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_422C")
    Call(0, 14)
    Jump("loc_45CD")

    label("loc_422C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_42BE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_42B6")

    #C0202
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "しすたーのおねーさん、\x01",
            "ほんとに懲りないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xB,
        (
            "いつもヴァンに\x01",
            "ムチャクチャにされちゃうのに～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_42B9")

    label("loc_42B6")

    Call(0, 15)

    label("loc_42B9")

    Jump("loc_45CD")

    label("loc_42BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4311")

    #C0204
    ChrTalk(
        0xB,
        "キャハハッ！\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0xB,
        (
            "走りながらしゃべると、\x01",
            "いき、きれちゃうよぅ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45CD")

    label("loc_4311")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4370")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_4368")

    #C0206
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "きねんさい、兄ちゃんたちは\x01",
            "なにして遊ぶの～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_436B")

    label("loc_4368")

    Call(0, 16)

    label("loc_436B")

    Jump("loc_45CD")

    label("loc_4370")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_43C5")

    #C0207
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "イモリ、これで最後だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xB,
        "ボチャン、ボチャ～ン！\x02",
    )

    CloseMessageWindow()
    Jump("loc_45CD")

    label("loc_43C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4416")

    #C0209
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "お腹すいてきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xB,
        "何かおちてねーかな？\x02",
    )

    CloseMessageWindow()
    Jump("loc_45CD")

    label("loc_4416")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4473")

    #C0211
    ChrTalk(
        0xB,
        (
            "クスクス……ヴァンは\x01",
            "いいよね、お父さんがいてさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0212
    ChrTalk(
        0xB,
        "飲んだくれだけど。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45CD")

    label("loc_4473")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_44A5")

    #C0213
    ChrTalk(
        0xB,
        "キャハハッ！　待って待って～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_45CD")

    label("loc_44A5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_44FE")

    #C0214
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "もう飽きてきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0xB,
        "そろそろ遊びに行きたいなー。\x02",
    )

    CloseMessageWindow()
    Jump("loc_45CD")

    label("loc_44FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_455A")
    OP_4B(0xA, 0xFF)
    OP_93(0xFE, 0x87, 0x0)

    #C0216
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "ねえ、どんな感じ？\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xB,
        "どんくらいやべーの？\x02",
    )

    CloseMessageWindow()
    OP_4C(0xA, 0xFF)
    Jump("loc_45CD")

    label("loc_455A")


    #C0218
    ChrTalk(
        0xB,
        (
            "不良の兄ちゃんたちね、\x01",
            "最近すっごくイラついてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xB,
        (
            "クスクス……\x01",
            "市街の兄ちゃんたちも\x01",
            "気をつけてね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45CD")

    TalkEnd(0xFE)
    Return()

    # Function_17_3F8A end

    def Function_18_45D1(): pass

    label("Function_18_45D1")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_4663")

    #C0220
    ChrTalk(
        0xC,
        "ふう、眠くなってきちゃったな……\x02",
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xC,
        (
            "今日もお仕事たくさんしたし、\x01",
            "暗くなる前に帰らなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0xC,
        "また明日も早いものね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5250")

    label("loc_4663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_473D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_46B5")

    #C0223
    ChrTalk(
        0xC,
        (
            "業者さん、喜んでくれるかな。\x01",
            "ふふっ、楽しみだなぁ～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4738")

    label("loc_46B5")


    #C0224
    ChrTalk(
        0xC,
        "お掃除、お掃除……\x02",
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xC,
        (
            "今日は鉄くずを集めて\x01",
            "業者さんに買い取ってもらうんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0xC,
        (
            "ふふっ、業者さん\x01",
            "喜んでくれるかなぁ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4738")

    Jump("loc_5250")

    label("loc_473D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_47D9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_478E")

    #C0227
    ChrTalk(
        0xC,
        (
            "最近怒鳴り声が\x01",
            "聞こえてきたりするんだ。\x01",
            "心配だな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47D4")

    label("loc_478E")


    #C0228
    ChrTalk(
        0xC,
        (
            "不良の人たち、\x01",
            "どうしたんだろう……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0xC,
        "なんだか心配だな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_47D4")

    Jump("loc_5250")

    label("loc_47D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_4863")

    #C0230
    ChrTalk(
        0xC,
        (
            "石畳って、なんだか落ち着くよね。\x01",
            "いろんな形があってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0xC,
        (
            "石畳を見ながら掃除していると\x01",
            "毎日でも全然飽きないんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5250")

    label("loc_4863")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_497F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_48C1")
    TurnDirection(0xC, 0x153, 0)

    #C0232
    ChrTalk(
        0xC,
        "お掃除はぼくに任せて。\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0xC,
        "慣れてるからへっちゃらだよっ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_497A")

    label("loc_48C1")


    #C0234
    ChrTalk(
        0xC,
        (
            "こんにちは！\x01",
            "今日もいい天気だね！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xC, 0x153, 0)

    #C0235
    ChrTalk(
        0xC,
        (
            "あれ……見かけない女の子……\x01",
            "君もお掃除、手伝ってくれるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0xC,
        (
            "ふふっ、うれしいけどダメダメ。\x01",
            "ガラスの欠片とかも落ちてるからね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_497A")

    Jump("loc_5250")

    label("loc_497F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_4A8C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_49E3")

    #C0237
    ChrTalk(
        0xC,
        "ぼく、お祭り大好きなんだ。\x02",
    )

    CloseMessageWindow()

    #C0238
    ChrTalk(
        0xC,
        (
            "ワクワク……\x01",
            "記念祭、早くこないかなぁ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4A87")

    label("loc_49E3")


    #C0239
    ChrTalk(
        0xC,
        (
            "記念祭って言葉を聞くと、\x01",
            "それだけでワクワクするよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0xC,
        "ワクワク、ワクワク……！\x02",
    )

    CloseMessageWindow()

    #C0241
    ChrTalk(
        0xC,
        "ぼく、お祭り大好きなんだ。\x02",
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0xC,
        "だってみんなが笑顔になるんだもの。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4A87")

    Jump("loc_5250")

    label("loc_4A8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_4BA9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4AFF")

    #C0243
    ChrTalk(
        0xC,
        (
            "ぼく、難しいことは\x01",
            "よく分からないや……\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0xC,
        (
            "せっせっ……\x01",
            "お掃除なら得意なんだけどね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4BA4")

    label("loc_4AFF")


    #C0245
    ChrTalk(
        0xC,
        (
            "せっせっ……\x01",
            "今朝はテスタメンツの人が\x01",
            "挨拶してくれたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0xC,
        (
            "最近、この辺りの\x01",
            "見回りをしてるんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0247
    ChrTalk(
        0xC,
        (
            "マフィアが入ってこないように\x01",
            "って言っていたよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4BA4")

    Jump("loc_5250")

    label("loc_4BA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_4CD9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4C2E")

    #C0248
    ChrTalk(
        0xC,
        "あれ、お役人の人じゃないの？\x02",
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0xC,
        (
            "ごめんなさい、\x01",
            "最近お役人さんが来たりするから\x01",
            "間違えてしまったみたい。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD4")

    label("loc_4C2E")


    #C0250
    ChrTalk(
        0xC,
        (
            "こんにちは！\x01",
            "……お役人の人？\x02",
        )
    )

    CloseMessageWindow()

    #C0251
    ChrTalk(
        0xC,
        (
            "ここはぼくが毎日\x01",
            "お掃除してるからきれいですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0xC,
        "ふふっ、今日もぴかぴかです！\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0xC,
        (
            "ごろんって\x01",
            "横になっても平気ですよ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4CD4")

    Jump("loc_5250")

    label("loc_4CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_4DF8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4D47")

    #C0254
    ChrTalk(
        0xC,
        (
            "ぼく、あの狼さんに\x01",
            "毎朝挨拶をしてるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0xC,
        "だって、とっても賢そうなんだもの。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4DF3")

    label("loc_4D47")


    #C0256
    ChrTalk(
        0xC,
        (
            "朝早くにね、この辺りを\x01",
            "大きな白い狼が通りがかるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0xC,
        (
            "立派なたてがみを持っていて\x01",
            "とっても賢そうなんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0258
    ChrTalk(
        0xC,
        (
            "ふふ、この辺りの\x01",
            "見回りをしてくれているのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4DF3")

    Jump("loc_5250")

    label("loc_4DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_4ECC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4E69")

    #C0259
    ChrTalk(
        0xC,
        (
            "朝からずっと\x01",
            "この通りを掃除していたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0260
    ChrTalk(
        0xC,
        (
            "ふふっ、とっても\x01",
            "綺麗になったでしょ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EC7")

    label("loc_4E69")


    #C0261
    ChrTalk(
        0xC,
        "あ、こんにちは！\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0xC,
        "ふふっ、見て見て！\x02",
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0xC,
        (
            "この通り、\x01",
            "とっても綺麗になったでしょ？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4EC7")

    Jump("loc_5250")

    label("loc_4ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 1)), scpexpr(EXPR_END)), "loc_4FC0")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_4F21")

    #C0264
    ChrTalk(
        0xC,
        (
            "釘とか金属はね、\x01",
            "買い取ってくれる\x01",
            "業者さんがいるんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FBB")

    label("loc_4F21")


    #C0265
    ChrTalk(
        0xC,
        (
            "釘とか金属はね、\x01",
            "こうして袋に集めるんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0xC,
        (
            "分別して持っていくと\x01",
            "買い取ってくれる業者さんがいるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0xC,
        (
            "街も綺麗になるし\x01",
            "一石二鳥だよね？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_4FBB")

    Jump("loc_5250")

    label("loc_4FC0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_END)), "loc_507F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_500E")

    #C0268
    ChrTalk(
        0xC,
        (
            "さっさっ、さっさっ……\x01",
            "今日もお掃除頑張ろうっと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_507A")

    label("loc_500E")


    #C0269
    ChrTalk(
        0xC,
        "こんにちは、とってもいい朝だね！\x02",
    )

    CloseMessageWindow()

    #C0270
    ChrTalk(
        0xC,
        (
            "ぼく、朝日を見ると思うんだ。\x01",
            "よーし、今日も一日頑張ろうって。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_507A")

    Jump("loc_5250")

    label("loc_507F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 5)), scpexpr(EXPR_END)), "loc_518F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_50FA")

    #C0271
    ChrTalk(
        0xC,
        (
            "何日か前、この辺りで\x01",
            "喧嘩があったみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0xC,
        (
            "……どうして\x01",
            "喧嘩なんてするんだろうね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_518A")

    label("loc_50FA")


    #C0273
    ChrTalk(
        0xC,
        (
            "何日か前、この辺りで\x01",
            "喧嘩があったみたいなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0xC,
        (
            "たくさんの破片に\x01",
            "血の跡が残ってた……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0xC,
        (
            "見てるだけで\x01",
            "何だか胸が苦しくなったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)

    label("loc_518A")

    Jump("loc_5250")

    label("loc_518F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x42, 0)), scpexpr(EXPR_END)), "loc_51DE")

    #C0276
    ChrTalk(
        0xC,
        (
            "あっちの通りが\x01",
            "騒がしかったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0277
    ChrTalk(
        0xC,
        "何かあったのかな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_5250")

    label("loc_51DE")


    #C0278
    ChrTalk(
        0xC,
        (
            "えっと……あなたたちも\x01",
            "ゴミ拾いを手伝ってくれるの？\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0xC,
        (
            "ふふっ、ありがとう。\x01",
            "やっぱり街は綺麗にしないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5250")

    TalkEnd(0xFE)
    Return()

    # Function_18_45D1 end

    def Function_19_5254(): pass

    label("Function_19_5254")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_52E9")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0280
    ChrTalk(
        0xD,
        "……シャア、広場は異常なしだぜ。\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0xD,
        (
            "おいスラッシュ、\x01",
            "そろそろいいだろうが。\x01",
            "戻ってヴァルドさんに報告すんぞ！\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_53B6")

    label("loc_52E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_534C")

    #C0282
    ChrTalk(
        0xD,
        "あの女、今日はいねえのかな。\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0xD,
        (
            "チッ、折角声かけて\x01",
            "やろうと思ったのによォ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53B6")

    label("loc_534C")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0284
    ChrTalk(
        0xD,
        "ああ、俺も同感だぜ。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0xD,
        (
            "あんな連中、今すぐ\x01",
            "ブチ殺してやんねえとなァ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53AE")
    SetScenarioFlags(0x53, 4)

    label("loc_53AE")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_53B6")

    TalkEnd(0xFE)
    Return()

    # Function_19_5254 end

    def Function_20_53BA(): pass

    label("Function_20_53BA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 7)), scpexpr(EXPR_END)), "loc_5470")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0286
    ChrTalk(
        0xE,
        (
            "そういやあの女、\x01",
            "最近見ねえよなァ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0xE,
        (
            "ひゃひゃ、練習が忙しいとか\x01",
            "言ってやがったが、そのせいかァ？\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x101,
        (
            "#0005F（…………？\x01",
            "  誰の事だろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_55B7")

    label("loc_5470")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_5543")
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_54C2")

    #C0289
    ChrTalk(
        0xE,
        (
            "ちぇっ、あの女～……\x01",
            "今日は通んねえのかァ～？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5536")

    label("loc_54C2")


    #C0290
    ChrTalk(
        0xE,
        "通んねえなァ～……\x02",
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0xE,
        (
            "そういやあの女、\x01",
            "いっつも練習とか叫んでんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0xE,
        "ひゃひゃ、何の練習なんだろーな！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)

    label("loc_5536")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    Jump("loc_55B7")

    label("loc_5543")

    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)

    #C0293
    ChrTalk(
        0xE,
        "ヒャハ！　構うもんか！\x02",
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0xE,
        (
            "ヴァルドさんだって腹の底じゃ\x01",
            "イラついてんだからよォ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55AF")
    SetScenarioFlags(0x53, 4)

    label("loc_55AF")

    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)

    label("loc_55B7")

    TalkEnd(0xFE)
    Return()

    # Function_20_53BA end

    def Function_21_55BB(): pass

    label("Function_21_55BB")

    TalkBegin(0xFE)

    #C0295
    ChrTalk(
        0xF,
        (
            "くっ、こんな事が\x01",
            "許されるものか……！\x02",
        )
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0xF,
        "だが……ワジがそう言うなら……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x53, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_561A")
    SetScenarioFlags(0x53, 4)

    label("loc_561A")

    TalkEnd(0xFE)
    Return()

    # Function_21_55BB end

    def Function_22_561E(): pass

    label("Function_22_561E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x12, 0x0, 0x10)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x94, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_58A9")
    TurnDirection(0xFE, 0x0, 0)

    #C0297
    ChrTalk(
        0xFE,
        (
            "まあ、警察官が不良たちと\x01",
            "一緒になって乱闘だなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#0005Fいえ今のは喧嘩ではなく、\x01",
            "護身術の稽古で……\x02",
        )
    )

    CloseMessageWindow()

    #C0299
    ChrTalk(
        0xFE,
        (
            "どんな理由があろうと\x01",
            "暴力はいけません！\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#0104F彼らとの交流試合を通じて\x01",
            "スポーツマンシップを\x01",
            "学んでもらっているんです。\x02\x03",

            "#0100F彼らの更生のために\x01",
            "定期的に来ているんですよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0301
    ChrTalk(
        0xFE,
        (
            "まあそうだったんですか……\x01",
            "これは失礼しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0302
    ChrTalk(
        0xFE,
        (
            "それにしてもあんな乱暴な子達の\x01",
            "心を開かせようとするなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0xFE,
        (
            "素晴らしいですわ！\x01",
            "私も教育者として見習わなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x103,
        (
            "#0200F（さすがエリィさん、\x01",
            "  説得はお手のものですね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x104,
        "#0300F（ハハ、正直助かったぜ。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x94, 5)
    SetScenarioFlags(0x0, 7)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_58A4")
    OP_93(0xFE, 0xE1, 0x0)

    label("loc_58A4")

    Jump("loc_5A65")

    label("loc_58A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_593E")
    TurnDirection(0xFE, 0x0, 0)

    #C0306
    ChrTalk(
        0xFE,
        (
            "あの乱暴な子達の\x01",
            "心を開かせようとするなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0xFE,
        (
            "素晴らしいですわ！\x01",
            "私も教育者として見習わなくっちゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_5939")
    OP_93(0xFE, 0xE1, 0x0)

    label("loc_5939")

    Jump("loc_5A65")

    label("loc_593E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_END)), "loc_59F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_59ED")

    #C0308
    ChrTalk(
        0x10,
        (
            "……この子たちときたら、\x01",
            "勉強しようとする気が\x01",
            "全く感じられないのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x10,
        (
            "日曜学校に来ないなら、\x01",
            "こういう場でしっかりと\x01",
            "学んで欲しいのですが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_59F0")

    label("loc_59ED")

    Call(0, 15)

    label("loc_59F0")

    Jump("loc_5A65")

    label("loc_59F5")


    #C0310
    ChrTalk(
        0x10,
        (
            "大聖堂から日曜学校の\x01",
            "出張授業に来たのです。\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x10,
        (
            "さて……今日はちゃんと\x01",
            "お話を聞いてくれると良いのですが。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5A65")

    TalkEnd(0xFE)
    Return()

    # Function_22_561E end

    def Function_23_5A69(): pass

    label("Function_23_5A69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_5AD8")

    #C0312
    ChrTalk(
        0x11,
        "いいか、まずは挨拶だ。\x02",
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x11,
        (
            "ヴァルドさんや\x01",
            "幹部の人たちに会ったら\x01",
            "オッスって言うんだぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5BB0")

    label("loc_5AD8")

    OP_4B(0x8, 0xFF)

    #C0314
    ChrTalk(
        0x11,
        "ディーノは新入りだからな。\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x11,
        (
            "俺たちのルールを\x01",
            "一つ一つ教えてやんねえと。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x11, 0x8, 500)

    #C0316
    ChrTalk(
        0x11,
        "いいか、まずは挨拶だ。\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x11,
        (
            "ヴァルドさんや\x01",
            "幹部の人たちに会ったら\x01",
            "オッスって言うんだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x8,
        "オ、オッス！\x02",
    )

    CloseMessageWindow()
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x11, 0x10)
    SetScenarioFlags(0x0, 5)

    label("loc_5BB0")

    TalkEnd(0xFE)
    Return()

    # Function_23_5A69 end

    def Function_24_5BB4(): pass

    label("Function_24_5BB4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearMapFlags(0x10000000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(-4950, -1840, -23330, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    SetMapObjFlags(0x5, 0x1000)
    FadeToBright(1000, 0)
    OP_68(-14810, 2000, -9650, 5000)
    MoveCamera(44, 27, 0, 5000)
    OP_6E(500, 5000)
    SetCameraDistance(24500, 5000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(11430, 2000, 960, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(29500, 0)
    ClearMapObjFlags(0x5, 0x1000)
    OP_68(38910, 2200, -19760, 7000)
    MoveCamera(32, 17, 0, 7000)
    OP_6E(500, 7000)
    SetCameraDistance(30920, 7000)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(2190, 2000, -10020, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(35000, 0)
    SetCameraDistance(48000, 5000)
    OP_0D()
    PlaceName2(340, 200, "c_plac10", 0x0, 0)
    OP_6F(0x10)
    Sleep(500)

    #A0319
    AnonymousTalk(
        0x104,
        (
            "#0305F随分寂れた場所だな……\x01",
            "本当にクロスベル市の中なのか？\x02",
        )
    )

    CloseMessageWindow()

    #A0320
    AnonymousTalk(
        0x102,
        "#0108F……そう、ここが旧市街ね。\x02",
    )

    CloseMessageWindow()

    #A0321
    AnonymousTalk(
        0x101,
        (
            "#0001Fああ……俺もここには\x01",
            "ほとんど来たことが無かったな。\x02\x03",

            "随分前に、都市開発から\x01",
            "取り残された区画みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #A0322
    AnonymousTalk(
        0x103,
        (
            "#0200Fデータベースによると\x01",
            "現在でもそれなりの数の住民が\x01",
            "普通に暮らしているみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #A0323
    AnonymousTalk(
        0x101,
        (
            "#0003Fそうか……\x02\x03",

            "#0000Fということは、警察の管轄には違いないな。\x01",
            "一通り回ってみることにしよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    Sound(828, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0324
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "旧市街は、街の外れに位置する寂れた街区です。\x02",
        )
    )

    CloseMessageWindow()

    #A0325
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いくつかの便利な施設が存在しますが、\x01",
            "序盤では入る事はできません。\x02",
        )
    )

    CloseMessageWindow()

    #A0326
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "物語の進行に合わせて\x01",
            "立ち寄ってみると良いでしょう。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_68(2050, 2000, 14590, 0)
    MoveCamera(45, 34, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetScenarioFlags(0x45, 1)
    EventEnd(0x5)
    Return()

    # Function_24_5BB4 end

    def Function_25_6001(): pass

    label("Function_25_6001")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1F)
    LoadChrToIndex("chr/ch30900.itc", 0x20)
    LoadChrToIndex("chr/ch30950.itc", 0x21)
    LoadChrToIndex("chr/ch31750.itc", 0x23)
    LoadChrToIndex("chr/ch31850.itc", 0x25)
    LoadChrToIndex("chr/ch00050.itc", 0x26)
    LoadChrToIndex("chr/ch00150.itc", 0x27)
    LoadChrToIndex("chr/ch00250.itc", 0x28)
    LoadChrToIndex("chr/ch00350.itc", 0x29)
    LoadChrToIndex("apl/ch50014.itc", 0x2A)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_68(1700, 1000, 8700, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    SetChrPos(0x101, 1100, 0, 8000, 180)
    SetChrPos(0x102, 2300, 0, 8000, 180)
    SetChrPos(0x103, 1100, 0, 9400, 180)
    SetChrPos(0x104, 2300, 0, 9400, 180)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -1000, 0, -5200, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -1500, 0, -3700, 90)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -1500, 0, -6700, 90)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, -2600, 0, -5600, 90)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 3100, 0, -5200, 270)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 3600, 0, -3700, 270)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrPos(0x18, 3600, 0, -6700, 270)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, 4600, 0, -5400, 270)
    ClearMapFlags(0x10000000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00001.itp")
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light", 0x0, 0x1)
    FadeToBright(1000, 0)
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
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0327
    ChrTalk(
        0x101,
        "#5P#0013Fあれは……！\x02",
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x104,
        (
            "#5P#0305Fおーおー。\x01",
            "一触即発みたいだな。\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7517", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x205), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(1100, 900, -5200, 3000)
    MoveCamera(55, 23, 0, 3000)
    SetCameraDistance(18000, 3000)
    OP_6F(0x79)

    #C0329
    ChrTalk(
        0x16,
        "#2Pおうおう、青坊主ども……\x02",
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x16,
        (
            "#2Pあんまり調子コイてると\x01",
            "マジでブチ殺すぞ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x17,
        (
            "#11Pヒャハ、とっくに\x01",
            "ネタは上がってんだよォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x17,
        (
            "#11Pテメエらが\x01",
            "クソ汚い真似をしたってよォ！\x02",
        )
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x12,
        (
            "#6Pフン……\x01",
            "これだから低脳な連中は。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x12,
        (
            "#6P君たちごときチンピラに\x01",
            "卑怯な真似をするまでもない。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x13,
        (
            "#3Pそ、そちらこそよくも\x01",
            "仲間を病院送りにしてくれたな……\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x13,
        (
            "#3P目には目を、歯には歯を……\x01",
            "……か、覚悟してもらうぞ……\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x16,
        "#2P上等だよ、この青坊主ども！\x02",
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x16,
        "#2Pヴァルドさんが出るまでもねぇ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0339
    ChrTalk(
        0x12,
        (
            "#6Pこちらこそワジの\x01",
            "手を煩#2Rわずら#わせるまでもない……\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x12,
        (
            "#6P総員、聖戦の準備！\x01",
            "バイパーどもを殲滅する！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(300)
    #Sound(1086, 255, 100, 0)    #voice#Lloyd
    OP_82(0x96, 0x0, 0xBB8, 0x12C)

    #N0341
    NpcTalk(
        0x101,
        "声",
        "#4S──待った！\x02",
    )

    CloseMessageWindow()
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x20)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x20)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    OP_0D()
    Fade(500)
    OP_68(1100, 1000, 800, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, 600, 0, 7000, 180)
    SetChrPos(0x102, 1800, 0, 9300, 180)
    SetChrPos(0x103, 600, 0, 9300, 180)
    SetChrPos(0x104, 1800, 0, 7000, 180)
    OP_68(1100, 1000, -3200, 2500)
    SetCameraDistance(17500, 2500)

    def lambda_67BE():
        OP_95(0xFE, 600, 0, -1800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_67BE)
    Sleep(50)

    def lambda_67DB():
        OP_95(0xFE, 1800, 0, -1800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_67DB)
    Sleep(50)

    def lambda_67F8():
        OP_96(0xFE, 0x258, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_67F8)
    Sleep(50)

    def lambda_6815():
        OP_96(0xFE, 0x708, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6815)
    OP_0D()

    def lambda_6830():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_6830)

    def lambda_683D():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_683D)
    Sleep(50)

    def lambda_684D():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_684D)

    def lambda_685A():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_685A)

    def lambda_6867():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_6867)

    def lambda_6874():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x19, 2, lambda_6874)
    Sleep(50)

    def lambda_6884():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x14, 2, lambda_6884)

    def lambda_6891():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_6891)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x11)

    #C0342
    ChrTalk(
        0x16,
        "#2Pなんだァ……？\x02",
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x12,
        "#6P見かけない顔だな……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)

    #A0344
    AnonymousTalk(
        0x101,
        (
            "双方、喧嘩を中止してくれ！\x02\x03",

            "ここは公共の広場だ！\x01",
            "他の住民が迷惑している！\x02",
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

    #C0345
    ChrTalk(
        0x17,
        "#11Pハァ……？\x02",
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x13,
        (
            "#6Pな、なんだお前……\x01",
            "いきなり現れて口出しを……\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x104,
        "#5P#0306F（まあ、普通そうだわな。）\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x102,
        "#5P#0108F（……どうするの？）\x02",
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        "#5P#0003F（ああ……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【まず捜査手帳を見せる】\x01",          # 0
            "【明かさないで仲裁を続ける】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_6AB0"),
        (1, "loc_6B57"),
        (SWITCH_DEFAULT, "loc_6DB9"),
    )


    label("loc_6AB0")

    OP_2C(0x3E, 0x1)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    def lambda_6AC3():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFF704, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6AC3)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0350
    ChrTalk(
        0x101,
        (
            "#5P#0007Fクロスベル警察、特務支援課の者だ。\x02\x03",

            "付近住民の要請により\x01",
            "君たちの喧嘩を止めにきた。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DB9")

    label("loc_6B57")

    OP_63(0x12, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0351
    ChrTalk(
        0x12,
        (
            "#6Pそうか君たち……\x01",
            "遊撃士協会の連中だな？\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x12,
        (
            "#6P見かけない顔だが\x01",
            "新米といったところか。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6BE9():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6BE9)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x101,
        "#5P#0011Fい、いや……\x02",
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x103,
        "#5P#0206F……またですか。\x02",
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x16,
        (
            "#2Pケッ、毎度のことながら\x01",
            "小うるさい連中だぜ……\x02",
        )
    )

    CloseMessageWindow()

    #C0356
    ChrTalk(
        0x16,
        (
            "#2Pだが、今度ばかりは邪魔される\x01",
            "わけにはいかねぇんだよォ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6CA9():
        TurnDirection(0xFE, 0x16, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6CA9)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0357
    ChrTalk(
        0x101,
        "#5P#0013Fちょ、ちょっと待ってくれ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)

    def lambda_6CFE():
        OP_96(0xFE, 0x1F4, 0x0, 0xFFFFF704, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6CFE)
    WaitChrThread(0x101, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x2A)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0358
    ChrTalk(
        0x101,
        (
            "#5P#0007F俺たちは遊撃士じゃない。\x02\x03",

            "クロスベル警察、\x01",
            "『特務支援課』に所属している。\x02\x03",

            "付近住民の要請により\x01",
            "君たちの喧嘩を止めにきた。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6DB9")

    label("loc_6DB9")

    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0359
    ChrTalk(
        0x16,
        "#2P#4Sハアアアッ、警察だァ！？\x02",
    )

    CloseMessageWindow()

    #C0360
    ChrTalk(
        0x17,
        (
            "#11Pひゃはははは！\x01",
            "フカシこいてんじゃねーぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x13,
        (
            "#6P殆んど警官も寄り付かないのに\x01",
            "そ、そんなわけがあるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0362
    ChrTalk(
        0x12,
        (
            "#6Pまったく……吐#2Rつ#くなら\x01",
            "もっとマシな嘘を吐きたまえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sleep(300)

    #C0363
    ChrTalk(
        0x101,
        (
            "#5P#0003F……と、とにかく！\x02\x03",

            "#0013F君たちがしている喧嘩は\x01",
            "他の住民にとって迷惑なんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0364
    ChrTalk(
        0x104,
        (
            "#5P#0300Fそんなに喧嘩がしたけりゃ\x01",
            "街の外でやってきたらどうだ？\x02\x03",

            "いい運動になるだろうぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x16,
        "#2Pハッ、上等だ……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x16,
        (
            "#2Pこの旧市街で俺たちに\x01",
            "そんな口が利けるとはなァ……\x02",
        )
    )

    CloseMessageWindow()

    #C0367
    ChrTalk(
        0x12,
        "#6P旧市街#6Rこ  こ#には旧市街#6Rこ  こ#のルールがある。\x02",
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x12,
        (
            "#6P興味本位で口を出すつもりなら\x01",
            "痛い目に遭ってもらおうか。\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x16, 0x23)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x23)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    Sound(808, 0, 100, 0)
    SetChrChipByIndex(0x12, 0x25)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #C0369
    ChrTalk(
        0x101,
        "#5P#0013Fくっ……\x02",
    )

    CloseMessageWindow()

    #C0370
    ChrTalk(
        0x104,
        "#5P#0306Fダメだな、これは。\x02",
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x103,
        (
            "#5P#0211F……結局、\x01",
            "こうなるわけですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0372
    ChrTalk(
        0x102,
        "#5P#0101Fふう……仕方ないわね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0x26)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0373
    ChrTalk(
        0x16,
        (
            "#2Pなんだなんだ、よく見たら\x01",
            "可愛い子ちゃんたちと一緒かよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x16,
        (
            "#2P彼女にカッコいいとこを\x01",
            "見せてやろうってつもりかァ？\x02",
        )
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x17,
        (
            "#11Pなあなあ、そんな連中放って\x01",
            "俺たちとデートでもしねぇ～？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x12, 0x16, 500)
    Sleep(200)

    #C0376
    ChrTalk(
        0x12,
        (
            "#6P阿呆だな、君たちは……\x01",
            "ナンパなんかしてる場合か。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x13, 0x17, 500)
    Sleep(200)

    #C0377
    ChrTalk(
        0x13,
        (
            "#6Pじゃ、邪魔者を追っ払ったら\x01",
            "改めて戦闘を開始する……\x02",
        )
    )

    CloseMessageWindow()

    #C0378
    ChrTalk(
        0x13,
        "#6Pい、いいな、赤マムシども……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x16, 0x12, 500)
    Sleep(200)

    #C0379
    ChrTalk(
        0x16,
        "#2Pおお、上等だよ！\x02",
    )

    CloseMessageWindow()
    OP_93(0x16, 0x13B, 0x1F4)
    Sleep(200)

    #C0380
    ChrTalk(
        0x16,
        (
            "#2Pそんじゃサクッっと\x01",
            "ボコボコにすっかなァ～！！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7402():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7402)
    Sleep(50)
    OP_93(0x13, 0x2D, 0x1F4)
    StopBGM(0x3E8)
    Battle("BattleInfo_848", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_CA(0x1, 0xFF, 0x0)
    Call(0, 26)
    Return()

    # Function_25_6001 end

    def Function_26_743B(): pass

    label("Function_26_743B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30850.itc", 0x1F)
    LoadChrToIndex("chr/ch30853.itc", 0x20)
    LoadChrToIndex("chr/ch30900.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch30953.itc", 0x23)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch31753.itc", 0x26)
    LoadChrToIndex("chr/ch31850.itc", 0x28)
    LoadChrToIndex("chr/ch31853.itc", 0x29)
    LoadChrToIndex("chr/ch00400.itc", 0x2A)
    LoadChrToIndex("chr/ch02100.itc", 0x2B)
    LoadChrToIndex("chr/ch06700.itc", 0x2C)
    LoadChrToIndex("chr/ch00050.itc", 0x2D)
    LoadChrToIndex("chr/ch00150.itc", 0x2E)
    LoadChrToIndex("chr/ch00250.itc", 0x2F)
    LoadChrToIndex("chr/ch00350.itc", 0x30)
    LoadChrToIndex("apl/ch50015.itc", 0x31)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    OP_68(1100, 1000, -4200, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17500, 0)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x2E)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2F)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x30)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 600, 0, -1800, 180)
    SetChrPos(0x102, 1800, 0, 0, 180)
    SetChrPos(0x103, 600, 0, 0, 180)
    SetChrPos(0x104, 1800, 0, -1800, 180)
    SetChrChipByIndex(0x12, 0x29)
    SetChrSubChip(0x12, 0x3)
    SetChrChipByIndex(0x13, 0x23)
    SetChrSubChip(0x13, 0x3)
    SetChrChipByIndex(0x14, 0x22)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x22)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x80)
    ClearChrBattleFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x80)
    ClearChrBattleFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x80)
    ClearChrBattleFlags(0x15, 0x8000)
    SetChrPos(0x12, -1000, 0, -5200, 45)
    SetChrPos(0x13, -1500, 0, -3700, 45)
    SetChrPos(0x14, -1500, 0, -6700, 45)
    SetChrPos(0x15, -2600, 0, -5600, 45)
    SetChrChipByIndex(0x16, 0x26)
    SetChrSubChip(0x16, 0x3)
    SetChrChipByIndex(0x17, 0x20)
    SetChrSubChip(0x17, 0x3)
    SetChrChipByIndex(0x18, 0x25)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x1F)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x16, 0x80)
    ClearChrBattleFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x80)
    ClearChrBattleFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x80)
    ClearChrBattleFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x80)
    ClearChrBattleFlags(0x19, 0x8000)
    SetChrPos(0x16, 3100, 0, -5200, 315)
    SetChrPos(0x17, 3600, 0, -3700, 315)
    SetChrPos(0x18, 3600, 0, -6700, 315)
    SetChrPos(0x19, 4600, 0, -5400, 315)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrSubChip(0x1B, 0x0)
    SetChrChipByIndex(0x1A, 0x2A)
    SetChrSubChip(0x1A, 0x0)
    SetChrChipByIndex(0x1C, 0x2C)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x8000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00400.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu01600.itp")
    OP_63(0x14, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x15, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x19, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    SetMapObjFrame(0xFF, "h_kage", 0x0, 0x1)
    SetMapObjFrame(0xFF, "light", 0x0, 0x1)
    OP_68(1100, 1000, -3200, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)

    def lambda_778B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_778B)
    WaitChrThread(0x13, 2)

    #C0381
    ChrTalk(
        0x13,
        (
            "#6Pこ、こいつら……\x01",
            "ただの素人じゃない……？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_77DA():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_77DA)
    WaitChrThread(0x16, 2)

    #C0382
    ChrTalk(
        0x16,
        (
            "お、女どもも……\x01",
            "ただの連れかと思ったが……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7828():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7828)
    WaitChrThread(0x12, 2)

    #C0383
    ChrTalk(
        0x12,
        (
            "#6Pあの杖はなんだ……？\x01",
            "………ビリビリきたぞ………\x02",
        )
    )

    CloseMessageWindow()

    def lambda_787D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_787D)
    WaitChrThread(0x17, 2)

    #C0384
    ChrTalk(
        0x17,
        (
            "#2Pクソが……！\x01",
            "やっぱ遊撃士じゃねえか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x101,
        (
            "#5P#0006Fいや、だからさっきから\x01",
            "警察だって言ってるし……\x02",
        )
    )

    CloseMessageWindow()

    #C0386
    ChrTalk(
        0x102,
        (
            "#1P#0106Fふう……\x01",
            "よっぽど信用ないのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x16,
        "チッ、上等だ……\x02",
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x16,
        (
            "こうなったら全員で\x01",
            "ブチのめしてやらぁ……！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_797D():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_797D)
    SetChrSubChip(0x16, 0x2)
    Sound(808, 0, 100, 0)
    Sleep(80)
    BeginChrThread(0x17, 3, 0, 27)
    SetChrSubChip(0x16, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x16, 0x25)
    SetChrSubChip(0x16, 0x0)
    OP_64(0x18)
    OP_64(0x19)
    OP_0D()
    WaitChrThread(0x17, 3)

    #C0389
    ChrTalk(
        0x12,
        "#6P我々も遅れを取るな……！\x02",
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x12,
        (
            "#6Pたとえ相手が遊撃士でも\x01",
            "テスタメンツの誇りを見せろ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_7A25():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_7A25)
    SetChrSubChip(0x12, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(80)
    BeginChrThread(0x13, 3, 0, 28)
    SetChrSubChip(0x12, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x12, 0x28)
    SetChrSubChip(0x12, 0x0)
    OP_64(0x14)
    OP_64(0x15)
    OP_0D()
    WaitChrThread(0x13, 3)

    #C0391
    ChrTalk(
        0x101,
        "#5P#0013Fくっ……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrPos(0x1B, 15500, -1000, -10500, 315)
    SetChrPos(0x1A, -8300, 0, -10800, 60)
    ClearChrFlags(0x1B, 0x80)
    ClearChrBattleFlags(0x1B, 0x8000)
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)
    StopBGM(0xBB8)
    #Sound(1804, 255, 100, 0)    #voice#Wald

    #N0392
    NpcTalk(
        0x1B,
        "獰猛そうな声",
        "#1Pおいおい……何やってやがる。\x02",
    )

    CloseMessageWindow()
    #Sound(1427, 255, 100, 0)    #voice#Lazy

    #N0393
    NpcTalk(
        0x1A,
        "涼しげな声",
        "#5Pその辺にしときなよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x13, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x14, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x15, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_63(0x19, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    Fade(500)
    OP_68(8300, 900, -12000, 0)
    MoveCamera(173, 27, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(17500, 0)
    ClearChrFlags(0x1A, 0x8)
    SetChrPos(0x1A, -8300, 0, -10800, 60)
    ClearChrFlags(0x1B, 0x4)
    ClearChrFlags(0x1B, 0x8)
    OP_90(0x1B, 12500, -1000, -16500, 315)
    ClearChrFlags(0x1C, 0x80)
    ClearChrBattleFlags(0x1C, 0x8000)
    SetChrPos(0x1C, -9100, 0, -11800, 60)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, 700, 0, -2300, 180)
    SetChrPos(0x104, 1700, 0, -2300, 180)
    SetChrPos(0x102, 2000, 0, -700, 180)
    SetChrPos(0x103, 400, 0, -700, 180)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x6)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x5)
    SetChrSubChip(0x18, 0x0)
    SetChrChipByIndex(0x19, 0x6)
    SetChrSubChip(0x19, 0x0)
    SetChrChipByIndex(0x12, 0x7)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x21)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x21)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x21)
    SetChrSubChip(0x15, 0x0)
    SetChrPos(0x12, -1600, 0, -4700, 45)
    SetChrPos(0x13, -2400, 0, -3100, 45)
    SetChrPos(0x14, -3700, 0, -4300, 45)
    SetChrPos(0x15, -2700, 0, -5500, 45)
    SetChrPos(0x16, 4000, 0, -4700, 315)
    SetChrPos(0x17, 4800, 0, -3100, 315)
    SetChrPos(0x18, 6100, 0, -4300, 315)
    SetChrPos(0x19, 5100, 0, -5500, 315)

    def lambda_7DD5():

        label("loc_7DD5")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7DD5")

    QueueWorkItem2(0x16, 2, lambda_7DD5)

    def lambda_7DE7():

        label("loc_7DE7")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7DE7")

    QueueWorkItem2(0x17, 2, lambda_7DE7)

    def lambda_7DF9():

        label("loc_7DF9")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7DF9")

    QueueWorkItem2(0x18, 2, lambda_7DF9)

    def lambda_7E0B():

        label("loc_7E0B")

        TurnDirection(0xFE, 0x1B, 500)
        Yield()
        Jump("loc_7E0B")

    QueueWorkItem2(0x19, 2, lambda_7E0B)

    def lambda_7E1D():

        label("loc_7E1D")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_7E1D")

    QueueWorkItem2(0x12, 2, lambda_7E1D)

    def lambda_7E2F():

        label("loc_7E2F")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_7E2F")

    QueueWorkItem2(0x13, 2, lambda_7E2F)

    def lambda_7E41():

        label("loc_7E41")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_7E41")

    QueueWorkItem2(0x14, 2, lambda_7E41)

    def lambda_7E53():

        label("loc_7E53")

        TurnDirection(0xFE, 0x1A, 500)
        Yield()
        Jump("loc_7E53")

    QueueWorkItem2(0x15, 2, lambda_7E53)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetMapObjFrame(0xFF, "light", 0x1, 0x1)
    MoveCamera(163, 27, 0, 3000)
    SetCameraDistance(16500, 3000)

    def lambda_7EAE():
        OP_95(0xFE, 8300, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7EAE)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1B, 0x4)
    OP_6F(0x40)
    OP_6F(0x10)

    #C0394
    ChrTalk(
        0x16,
        "#1Pヴァ、ヴァルドさん……！！\x02",
    )

    CloseMessageWindow()

    def lambda_7EF8():
        OP_95(0xFE, 2900, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_7EF8)
    Sleep(2000)
    Fade(500)
    OP_68(-5700, 900, -9300, 0)
    MoveCamera(210, 30, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(16000, 0)
    EndChrThread(0x1B, 0x1)
    MoveCamera(200, 30, 0, 1500)
    SetCameraDistance(15000, 1500)

    def lambda_7F60():
        OP_95(0xFE, -5700, 0, -9300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_7F60)

    def lambda_7F7A():
        OP_95(0xFE, -6500, 0, -10300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_7F7A)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1C, 1)
    OP_6F(0x40)
    OP_6F(0x10)

    #C0395
    ChrTalk(
        0x12,
        "#2Pワジ……来てたのか。\x02",
    )

    CloseMessageWindow()

    #C0396
    ChrTalk(
        0x101,
        "#0005F（……もしかして。）\x02",
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x104,
        (
            "#0301F（両チームの頭#2Rヘッド#の\x01",
            "  お出ましのようだな……）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_801E():
        OP_95(0xFE, -500, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_801E)
    Sleep(50)

    def lambda_803B():
        OP_95(0xFE, -1100, 0, -6500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_803B)
    Sleep(1000)

    def lambda_8058():
        OP_95(0xFE, 2900, 0, -5500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_8058)
    Sleep(1000)
    Fade(500)
    OP_68(1200, 800, -4800, 0)
    MoveCamera(180, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16500, 1500)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    WaitChrThread(0x1B, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1C, 1)
    WaitChrThread(0x1C, 2)
    OP_6F(0x10)

    #N0398
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        (
            "#5P#1604Fクク、人が昼寝をしてる間に\x01",
            "楽しそうな事をしてるじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x16, 500)
    Sleep(300)

    #N0399
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        (
            "#11P#1602Fなあ、お前ら……\x01",
            "こいつは一体どういうつもりだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x16,
        (
            "#3Pいや……\x01",
            "へへ、なんと言いますか。\x02",
        )
    )

    CloseMessageWindow()

    #C0401
    ChrTalk(
        0x16,
        (
            "#3P青坊主どもに\x01",
            "お仕置きをしようとしたら\x01",
            "この変な連中がですね……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_820D():
        OP_9B(0x1, 0xFE, 0x0, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_820D)
    WaitChrThread(0x1B, 1)
    Fade(250)
    SetChrChipByIndex(0x1B, 0x31)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_8248():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_8248)

    def lambda_8261():
        OP_96(0xFE, 0xFA0, 0x1C2, 0xFFFFEDA4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_8261)
    Sound(804, 0, 100, 0)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x16, 2)
    ClearChrFlags(0x16, 0x20)

    #C0402
    ChrTalk(
        0x16,
        "#3Pひっ……！\x02",
    )

    CloseMessageWindow()

    #N0403
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        (
            "#11P#1601F……タコが。\x01",
            "先走るなって言ったろうが？\x02\x03",

            "てめえら前座がしゃしゃり出て\x01",
            "俺様の顔を潰すつもりかよ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x16,
        "#3Pめ、め、滅相もない！\x02",
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x16,
        (
            "#3Pヴァルドさんの顔を潰すなんて\x01",
            "そんな事はこれっぽっちも……！\x02",
        )
    )

    CloseMessageWindow()

    #N0406
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        "#11P#1600Fフン……\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1B, 0x2B)
    SetChrSubChip(0x1B, 0x0)

    def lambda_83B4():
        OP_96(0xFE, 0xB54, 0x0, 0xFFFFEA84, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_83B4)

    def lambda_83CE():
        OP_A6(0xFE, 0x0, 0x64, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_83CE)

    def lambda_83E7():
        OP_9D(0xFE, 0xFA0, 0x0, 0xFFFFEDA4, 0x0, 0x1388)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_83E7)
    Sound(819, 0, 100, 0)
    WaitChrThread(0x16, 1)
    SetChrChipByIndex(0x16, 0x26)
    SetChrSubChip(0x16, 0x3)
    WaitChrThread(0x16, 2)
    ClearChrFlags(0x16, 0x4)
    OP_52(0x16, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    #C0407
    ChrTalk(
        0x16,
        "#3Pゴホッ、ゴホッ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x1B, 1)

    def lambda_8449():
        TurnDirection(0xFE, 0x12, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_8449)
    Sleep(100)

    def lambda_8459():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_8459)
    WaitChrThread(0x1C, 2)

    #N0408
    NpcTalk(
        0x1A,
        "涼しげな少年",
        (
            "#5P#0403F君たちも……\x01",
            "一体どういうつもりかな？\x02\x03",

            "#0400F僕の言ったことが\x01",
            "聞けないっていうわけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0409
    ChrTalk(
        0x12,
        "#4Pだが、ワジ……\x02",
    )

    CloseMessageWindow()

    #C0410
    ChrTalk(
        0x14,
        (
            "#4Pこ、こいつらが\x01",
            "絡んでくるから、つい……\x02",
        )
    )

    CloseMessageWindow()

    #N0411
    NpcTalk(
        0x1C,
        "禿の大男",
        "#5P言い訳はいい。\x02",
    )

    CloseMessageWindow()

    #N0412
    NpcTalk(
        0x1C,
        "禿の大男",
        (
            "#5P俺たちはワジの手足。\x01",
            "余計な気を回す必要はない。\x02",
        )
    )

    CloseMessageWindow()

    #C0413
    ChrTalk(
        0x12,
        "#4P……分かった……\x02",
    )

    CloseMessageWindow()

    #C0414
    ChrTalk(
        0x14,
        "#4P……も、猛省する……\x02",
    )

    CloseMessageWindow()

    #N0415
    NpcTalk(
        0x1A,
        "涼しげな少年",
        (
            "#5P#0404Fま、判ってくれれば\x01",
            "それでいいけどね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_85F9():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x16, 2, lambda_85F9)
    Sleep(160)
    Fade(250)
    SetChrChipByIndex(0x16, 0x5)
    SetChrSubChip(0x16, 0x0)
    OP_0D()
    TurnDirection(0x1B, 0x1A, 500)

    #N0416
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        (
            "#5P#1602Fクク……\x01",
            "相変わらず気色の悪い連中だぜ。\x02\x03",

            "舎弟にそんな格好をさせて……\x01",
            "どこぞの宗教家気取りかよ？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_86A8():
        TurnDirection(0xFE, 0x1B, 500)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_86A8)
    Sleep(100)

    def lambda_86B8():
        TurnDirection(0xFE, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_86B8)
    WaitChrThread(0x1C, 2)

    #N0417
    NpcTalk(
        0x1A,
        "涼しげな少年",
        (
            "#11P#0402Fフフ、別に僕がその格好を\x01",
            "強制してるわけじゃないけどね。\x02\x03",

            "そっちの方こそ、\x01",
            "手下に当り散らしてばかりだと\x01",
            "お山の大将が知れるってもんだよ？\x02",
        )
    )

    CloseMessageWindow()

    #N0418
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        "#5P#1602Fククク……\x02",
    )

    CloseMessageWindow()

    #N0419
    NpcTalk(
        0x1A,
        "涼しげな少年",
        "#11P#0404Fフフフ……\x02",
    )

    CloseMessageWindow()

    #C0420
    ChrTalk(
        0x101,
        "#12P#0001F（な、なんだ……？）\x02",
    )

    CloseMessageWindow()

    #C0421
    ChrTalk(
        0x102,
        "#0101F#6P#N（どういう関係なのかしら……）\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #N0422
    NpcTalk(
        0x1A,
        "涼しげな少年",
        "#2P#0404F──まあ、それはともかく。\x02",
    )

    CloseMessageWindow()

    def lambda_8846():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A, 2, lambda_8846)
    Sleep(50)

    def lambda_8856():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1B, 2, lambda_8856)
    Sleep(50)

    def lambda_8866():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1C, 2, lambda_8866)
    WaitChrThread(0x1C, 2)
    Sleep(300)

    #N0423
    NpcTalk(
        0x1A,
        "涼しげな少年",
        (
            "#11P#0402F君たち、警察の人って本当？\x02\x03",

            "フフ……\x01",
            "とてもそうは見えないけど。\x02",
        )
    )

    CloseMessageWindow()

    #N0424
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        (
            "#5P#1604Fフン、そこそこやりそうだがな。\x02\x03",

            "#1602F特にそこの赤毛……\x01",
            "いいガタイしてんじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0425
    ChrTalk(
        0x104,
        (
            "#6P#0306Fそりゃどうも……\x01",
            "アンタほどじゃないけどな。\x02",
        )
    )

    CloseMessageWindow()

    #N0426
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        (
            "#5P#1602Fまあ、そっちの姉ちゃんたちは\x01",
            "とても警察には見えねぇけどなァ。\x02\x03",

            "クク……\x01",
            "なかなかの上玉じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0427
    ChrTalk(
        0x102,
        "#0103F#6P#N……それはどうも。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0428
    ChrTalk(
        0x103,
        "#0211F#12P#N………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0429
    ChrTalk(
        0x101,
        (
            "#12P#0003F……新人だけど\x01",
            "一応全員、警察の人間だ。\x02\x03",

            "#0001F『特務支援課』……\x01",
            "発足されたばかりの\x01",
            "新部署に所属している。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x1A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #N0430
    NpcTalk(
        0x1A,
        "涼しげな少年",
        (
            "#11P#0405Fへえ、今日出た\x01",
            "クロスベルタイムズに\x01",
            "載っていたアレか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_8B9A")

    #C0431
    ChrTalk(
        0x101,
        "#12P#0011Fうっ……\x02",
    )

    CloseMessageWindow()

    #C0432
    ChrTalk(
        0x102,
        (
            "#0106F#6P#Nさすがクロスベルタイムズ……\x01",
            "早速広まったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8C6F")

    label("loc_8B9A")

    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0433
    ChrTalk(
        0x101,
        (
            "#12P#0005Fクロスベルタイムズに\x01",
            "載っていたって……\x02",
        )
    )

    CloseMessageWindow()

    #C0434
    ChrTalk(
        0x102,
        (
            "#6P#0105F#Nまさか……\x01",
            "子供たちを助けた時の？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8C6F")

    TurnDirection(0x1B, 0x1A, 500)
    Sleep(300)

    #N0435
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        (
            "#5P#1605Fなんだァ？\x01",
            "コイツら何かやったのか？\x02",
        )
    )

    CloseMessageWindow()

    #N0436
    NpcTalk(
        0x1A,
        "涼しげな少年",
        (
            "#11P#0404Fああ、ギルドの噛ませ犬として\x01",
            "大活躍だったみたいだよ。\x02\x03",

            "#0402Fいや、ゴメンゴメン。\x01",
            "一応少しは役立ったんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0437
    ChrTalk(
        0x101,
        "#12P#0013Fぐっ……\x02",
    )

    CloseMessageWindow()

    #N0438
    NpcTalk(
        0x1A,
        "涼しげな少年",
        (
            "#11P#0404Fフフ、イジめるのは\x01",
            "このくらいにしておいて……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(450)
    #Sound(1435, 255, 100, 0)    #voice#Lazy
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("涼しげな少年")

    #A0439
    AnonymousTalk(
        0xFF,
        (
            "──僕はワジ。\x01",
            "ワジ・ヘミスフィア。\x02\x03",

            "一応、『テスタメンツ』の\x01",
            "頭#2Rヘッド#をしてるみたいだよ？\x02",
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

    #N0440
    NpcTalk(
        0x1C,
        "禿の大男",
        "#11P……なぜ疑問形を使う？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x1C, 500)

    #C0441
    ChrTalk(
        0x1A,
        (
            "#6P#0402Fだって君の方が\x01",
            "いかにもヘッドじゃないか。\x02\x03",

            "#0409Fフフ、禿頭だけに\x01",
            "ヘッドが光ってるしね。\x02",
        )
    )

    CloseMessageWindow()

    #N0442
    NpcTalk(
        0x1C,
        "禿の大男",
        "#11P…………………………\x02",
    )

    CloseMessageWindow()

    #N0443
    NpcTalk(
        0x1B,
        "獰猛そうな青年",
        "#5P#1603Fフン……戯言はそこまでだ。\x02",
    )

    CloseMessageWindow()
    OP_93(0x1B, 0x13B, 0x1F4)
    Sleep(300)
    #Sound(1805, 255, 100, 0)    #voice#Wald
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("獰猛そうな青年")

    #A0444
    AnonymousTalk(
        0xFF,
        (
            "──ヴァルド。\x01",
            "ヴァルド・ヴァレスだ。\x02\x03",

            "『サーベルバイパー』の頭#2Rヘッド#をやってる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    OP_93(0x1A, 0x2D, 0x1F4)
    Sleep(300)

    #C0445
    ChrTalk(
        0x101,
        (
            "#12P#0003Fワジにヴァルドか……\x02\x03",

            "#0000F改めて──\x01",
            "クロスベル警察・特務支援課の\x01",
            "ロイド・バニングスだ。\x02\x03",

            "２人とも、どうやらこれ以上\x01",
            "事を構えるつもりはなさそうだし……\x02\x03",

            "ここは任せてもいいのかな？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    #C0446
    ChrTalk(
        0x1B,
        "#5P#1604Fククク……\x02",
    )

    CloseMessageWindow()

    #C0447
    ChrTalk(
        0x1A,
        "#11P#0404Fフフフ……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    SetCameraDistance(17500, 1000)
    #Sound(1809, 255, 100, 0)    #voice#Wald
    #Sound(1431, 255, 100, 1)    #voice#Lazy

    #C0448
    ChrTalk(
        0x1B,
        (
            "#1P#1609F#4S#1Kハハハハハ\x01",
            "ハハハッ！\x02",
        )
    )


    #C0449
    ChrTalk(
        0x1A,
        (
            "#2P#0409F#4S#1Kあはははは\x01",
            "はははっ！\x02",
        )
    )

    OP_57(0x1)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0450
    ChrTalk(
        0x101,
        "#12P#0013Fな、何がおかしい？\x02",
    )

    CloseMessageWindow()

    #C0451
    ChrTalk(
        0x1A,
        (
            "#11P#0404Fいやいや。\x01",
            "おめでたいなーと思ってさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0452
    ChrTalk(
        0x1B,
        (
            "#5P#1602F事を構えるつもりがない？\x02\x03",

            "クク……\x01",
            "なに寝ぼけた事を言ってんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0453
    ChrTalk(
        0x101,
        "#12P#0005F……なに………\x02",
    )

    CloseMessageWindow()

    #C0454
    ChrTalk(
        0x1A,
        (
            "#11P#0404Fこの場で手を引くのは\x01",
            "単に準備が済んでないから……\x02\x03",

            "#0402F──準備が終わりしだい、\x01",
            "徹底的にやり合うつもりだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0455
    ChrTalk(
        0x1B,
        (
            "#5P#1602Fそれも今までみたいな\x01",
            "セコイ小競り合いじゃねえ……\x02\x03",

            "どちらが生き残るか、\x01",
            "お互い潰し合うつもりでなァ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0456
    ChrTalk(
        0x101,
        "#12P#0007Fなっ！？\x02",
    )

    CloseMessageWindow()

    #C0457
    ChrTalk(
        0x104,
        (
            "#6P#0301Fおいおい……\x01",
            "殺し合いでもするつもりかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0458
    ChrTalk(
        0x1B,
        (
            "#5P#1604Fクク、そうなっても\x01",
            "不思議じゃねえだろうなァ。\x02\x03",

            "#1602Fま、どちらが血ヘドを吐くかは\x01",
            "分かりきってるけどよォ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0459
    ChrTalk(
        0x1A,
        (
            "#11P#0400Fフフ……言ってなよ。\x02\x03",

            "#0404Fまあ、どっちにしても\x01",
            "お呼びじゃないってことさ。\x02\x03",

            "#0402F腰抜けの警察──\x01",
            "まして君たちみたいな若造はね。\x02",
        )
    )

    CloseMessageWindow()

    #C0460
    ChrTalk(
        0x101,
        "#12P#0013Fっ……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1B, 0x16, 500)
    Sleep(300)
    #Sound(1807, 255, 100, 0)    #voice#Wald
    Sleep(500)

    #C0461
    ChrTalk(
        0x1B,
        (
            "#11P#1602Fクク……\x01",
            "行くぞ、てめえら！\x02",
        )
    )

    CloseMessageWindow()

    #C0462
    ChrTalk(
        0x16,
        "#3Pオ、オッス！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A, 0x12, 500)
    Sleep(300)
    #Sound(1429, 255, 100, 0)    #voice#Lazy
    Sleep(500)

    #C0463
    ChrTalk(
        0x1A,
        (
            "#5P#0400Fフフ……\x01",
            "こちらも引き上げるよ。\x02",
        )
    )

    CloseMessageWindow()

    #N0464
    NpcTalk(
        0x1C,
        "禿の大男",
        "#5P……了解だ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18500, 10000)
    BeginChrThread(0x1B, 3, 0, 29)
    BeginChrThread(0x1A, 3, 0, 30)
    OP_6F(0x10)
    WaitChrThread(0x1B, 3)
    WaitChrThread(0x1A, 3)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    SetChrFlags(0x17, 0x80)
    SetChrBattleFlags(0x17, 0x8000)
    SetChrFlags(0x18, 0x80)
    SetChrBattleFlags(0x18, 0x8000)
    SetChrFlags(0x19, 0x80)
    SetChrBattleFlags(0x19, 0x8000)
    SetChrFlags(0x1B, 0x80)
    SetChrBattleFlags(0x1B, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    SetChrFlags(0x1C, 0x80)
    SetChrBattleFlags(0x1C, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x8000)
    ClearChrFlags(0x17, 0x8000)
    ClearChrFlags(0x18, 0x8000)
    ClearChrFlags(0x19, 0x8000)
    ClearChrFlags(0x1B, 0x8000)
    ClearChrFlags(0x1A, 0x8000)
    ClearChrFlags(0x1C, 0x8000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7103", 0)
    ReplaceBGM("ed7101", "ed7103")
    ReplaceBGM("ed7100", "ed7103")
    Fade(1000)
    OP_68(1200, 900, -1500, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 500, 0, -2200, 180)
    SetChrPos(0x104, 1900, 0, -2200, 180)
    SetChrPos(0x102, 1900, 0, -800, 180)
    SetChrPos(0x103, 500, 0, -800, 180)
    OP_0D()

    #C0465
    ChrTalk(
        0x101,
        "#5P#0001F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)
    Sleep(300)

    #C0466
    ChrTalk(
        0x102,
        (
            "#5P#0106F……困った人たちね。\x02\x03",

            "#0101Fそれにどちらも\x01",
            "かなり本気みたいだったわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0x13B, 0x1F4)

    #C0467
    ChrTalk(
        0x104,
        (
            "#2P#0301Fああ、あの調子だと\x01",
            "数日中にやり合うつもりだろ。\x02\x03",

            "血を見るぞ、あの様子じゃ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x103, 0x87, 0x1F4)
    Sleep(300)

    #C0468
    ChrTalk(
        0x103,
        (
            "#1P#0206Fでも、課長からの任務は\x01",
            "一応終えた形にはなりますし……\x02\x03",

            "#0200Fこれ以上は任務外なのでは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0469
    ChrTalk(
        0x101,
        "#5P#0003F…………いや。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0470
    ChrTalk(
        0x101,
        (
            "#6P#0001Fそれじゃあ本当の意味で\x01",
            "任務を終わらせた事にはならない。\x02\x03",

            "ここで放置したら……\x01",
            "警察に対する市民の信頼は\x01",
            "いつまでも回復できないだろう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_99BD():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_99BD)

    def lambda_99CA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_99CA)

    def lambda_99D7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_99D7)
    WaitChrThread(0x104, 2)

    #C0471
    ChrTalk(
        0x103,
        "#1P#0203F……まあ、確かに。\x02",
    )

    CloseMessageWindow()

    #C0472
    ChrTalk(
        0x102,
        (
            "#5P#0103Fそうね……\x02\x03",

            "#0101F知ってしまった以上は\x01",
            "何とかして止めるべきだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0473
    ChrTalk(
        0x104,
        (
            "#2P#0306Fでもよ、そいつは\x01",
            "結構難しいんじゃないか？\x02\x03",

            "#0301Fお互い仲良くしろなんて\x01",
            "聞くような連中じゃないだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0474
    ChrTalk(
        0x101,
        "#6P#0008Fそうだな……\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【本部の応援を頼む】\x01",          # 0
            "【本部の応援は頼めない】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_9B4A"),
        (1, "loc_9D82"),
        (SWITCH_DEFAULT, "loc_A089"),
    )


    label("loc_9B4A")


    #C0475
    ChrTalk(
        0x101,
        (
            "#6P#0006F……本部に状況を報告して\x01",
            "旧市街の巡回強化を\x01",
            "提案するしかなさそうだな。\x02\x03",

            "#0001Fあの数が衝突したら\x01",
            "俺たちだけで何とかなるとは\x01",
            "ちょっと思えない。\x02",
        )
    )

    CloseMessageWindow()

    #C0476
    ChrTalk(
        0x102,
        (
            "#5P#0100F確かに、警官隊の巡回なら\x01",
            "抑止力はあるかもしれないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0477
    ChrTalk(
        0x104,
        "#2P#0306Fうーん、そう上手く行くかねぇ。\x02",
    )

    CloseMessageWindow()

    #C0478
    ChrTalk(
        0x103,
        (
            "#1P#0203F……データベースによれば、\x01",
            "ここ最近、旧市街での巡回が\x01",
            "大幅に減らされているようです。\x02\x03",

            "#0200F予算の削減が名目らしいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0479
    ChrTalk(
        0x101,
        (
            "#6P#0005Fそ、そうなのか！？\x02\x03",

            "#0008Fクソ、完全に放置することに\x01",
            "決めたって感じだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0480
    ChrTalk(
        0x102,
        (
            "#5P#0106Fそうなると提案するだけ\x01",
            "無駄かもしれないわね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A089")

    label("loc_9D82")

    OP_2C(0x3E, 0x2)
    OP_D0(0x6, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    #C0481
    ChrTalk(
        0x101,
        (
            "#6P#0008F……本部に報告したところで\x01",
            "頼りになるとは思えない。\x02\x03",

            "ここは自分たちで\x01",
            "何とかするしかなさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0482
    ChrTalk(
        0x102,
        (
            "#5P#0105Fあら……\x01",
            "報告するだけしてみたらどう？\x02\x03",

            "もしかした旧市街の巡回を\x01",
            "強化してくれるかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0483
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいや……たぶん難しいだろう。\x02\x03",

            "あれだけ騒ぎを起こしているのに\x01",
            "彼らは警察を気にもしてなかった。\x02\x03",

            "#0001F多分、この旧市街は意図的に\x01",
            "放置されてるんじゃないかと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0484
    ChrTalk(
        0x102,
        "#5P#0101Fあ……\x02",
    )

    CloseMessageWindow()

    #C0485
    ChrTalk(
        0x103,
        (
            "#1P#0203F確かにデータベースによれば、\x01",
            "ここ最近、旧市街での巡回が\x01",
            "大幅に減らされているようです。\x02\x03",

            "#0200F予算の削減が名目らしいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0486
    ChrTalk(
        0x104,
        (
            "#2P#0301Fフン、ビンゴってわけか。\x02\x03",

            "#0306Fしかし……それなら尚更、\x01",
            "打つ手ナシなんじゃねえか？\x02\x03",

            "#0300Fいっそ俺たちが、\x01",
            "両チームにケンカを売って\x01",
            "言うことを聞かせちまうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0487
    ChrTalk(
        0x101,
        "#6P#0006Fあのな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_A089")

    label("loc_A089")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0488
    ChrTalk(
        0x101,
        "#6P#0005F──待てよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0489
    ChrTalk(
        0x101,
        (
            "#6P#0008Fそういえば……\x01",
            "どうしてあの２チームは\x01",
            "“潰し合う”つもりなんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0490
    ChrTalk(
        0x102,
        "#5P#0105Fどうしてって……\x02",
    )

    CloseMessageWindow()

    #C0491
    ChrTalk(
        0x104,
        (
            "#2P#0305Fそりゃ、縄張り争いだの、\x01",
            "意地の張り合いってやつだろ？\x02",
        )
    )

    CloseMessageWindow()

    #C0492
    ChrTalk(
        0x101,
        (
            "#6P#0003Fいや、それだけじゃ普通、\x01",
            "本気の潰し合いにはならない。\x02\x03",

            "#0008F利害が絡んでいるならともかく\x01",
            "街の不良同士のいざこざだ。\x02\x03",

            "#0013Fどうして念入りに準備してまで\x01",
            "徹底的に潰し合う必要がある？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1300)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0493
    ChrTalk(
        0x103,
        "#1P#0205F……驚きました。\x02",
    )

    CloseMessageWindow()

    #C0494
    ChrTalk(
        0x102,
        "#5P#0100Fええ、私も。\x02",
    )

    CloseMessageWindow()

    #C0495
    ChrTalk(
        0x104,
        "#2P#0302Fふーん、なるほどねぇ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x101)

    #C0496
    ChrTalk(
        0x101,
        (
            "#6P#0011Fな、なんだよ……\x01",
            "そんなに変なこと言ったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0497
    ChrTalk(
        0x102,
        (
            "#5P#0104Fううん、さすが捜査官の資格を\x01",
            "持っているだけはあるなって。\x02",
        )
    )

    CloseMessageWindow()

    #C0498
    ChrTalk(
        0x104,
        (
            "#2P#0300Fいいとこ突いてると思うぜ。\x02\x03",

            "見たところ、ヘッド同士が\x01",
            "そこまで険悪な関係って\x01",
            "雰囲気でもなかったしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0499
    ChrTalk(
        0x103,
        (
            "#1P#0203F……多分、\x01",
            "理由があるのではないかと。\x02\x03",

            "#0201F当事者以外は知らない、\x01",
            "本気で争うだけの理由が。\x02",
        )
    )

    CloseMessageWindow()

    #C0500
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあ、ああ。\x01",
            "まさに俺もそう思ってさ。\x02\x03",

            "だったら──\x01",
            "やるべきことは一つだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0501
    ChrTalk(
        0x104,
        "#2P#0304Fだな。\x02",
    )

    CloseMessageWindow()

    #C0502
    ChrTalk(
        0x102,
        (
            "#5P#0100F『サーベルバイパー』に\x01",
            "『テスタメンツ』……\x02\x03",

            "まずはどちらに\x01",
            "話を聞きに行くべきかしら？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x25)
    OP_D5(0x26)
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
    SetMapObjFrame(0xFF, "h_kage", 0x1, 0x1)
    OP_68(1200, 2000, -1500, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 1200, 0, -1500, 180)
    SetChrPos(0x1, 1200, 0, -1500, 180)
    SetChrPos(0x2, 1200, 0, -1500, 180)
    SetChrPos(0x3, 1200, 0, -1500, 180)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrPos(0xA, 8620, 0, 8810, 180)
    SetChrPos(0xB, 7900, 0, 9630, 135)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetScenarioFlags(0x42, 0)
    OP_29(0x3E, 0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_26_743B end

    def Function_27_A6C9(): pass

    label("Function_27_A6C9")


    def lambda_A6CE():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A6CE)
    SetChrSubChip(0x17, 0x2)
    Sleep(80)
    SetChrSubChip(0x17, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x17, 0x1F)
    SetChrSubChip(0x17, 0x0)
    OP_0D()
    Return()

    # Function_27_A6C9 end

    def Function_28_A6FF(): pass

    label("Function_28_A6FF")


    def lambda_A704():
        OP_A6(0xFE, 0x0, 0x32, 0x190, 0xBB8)
        ExitThread()

    QueueWorkItem(0x13, 2, lambda_A704)
    SetChrSubChip(0x13, 0x2)
    Sleep(80)
    SetChrSubChip(0x13, 0x1)
    Sleep(80)
    Fade(250)
    SetChrChipByIndex(0x13, 0x22)
    SetChrSubChip(0x13, 0x0)
    OP_0D()
    Return()

    # Function_28_A6FF end

    def Function_29_A735(): pass

    label("Function_29_A735")

    OP_93(0x1B, 0x87, 0x1F4)
    ClearChrFlags(0x1B, 0x4)

    def lambda_A746():
        OP_95(0xFE, 15100, -1600, -17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_A746)
    Sleep(1600)
    BeginChrThread(0x19, 3, 0, 31)
    Sleep(400)
    BeginChrThread(0x18, 3, 0, 31)
    Sleep(900)
    BeginChrThread(0x16, 3, 0, 31)
    Sleep(500)
    BeginChrThread(0x17, 3, 0, 31)
    WaitChrThread(0x16, 3)
    WaitChrThread(0x17, 3)
    WaitChrThread(0x18, 3)
    WaitChrThread(0x19, 3)
    Return()

    # Function_29_A735 end

    def Function_30_A790(): pass

    label("Function_30_A790")

    BeginChrThread(0x1C, 3, 0, 32)
    OP_93(0x1A, 0xF0, 0x1F4)

    def lambda_A7A2():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_A7A2)
    Sleep(2400)
    BeginChrThread(0x15, 3, 0, 33)
    Sleep(500)
    BeginChrThread(0x14, 3, 0, 33)
    Sleep(800)
    BeginChrThread(0x12, 3, 0, 33)
    Sleep(400)
    BeginChrThread(0x13, 3, 0, 33)
    StopBGM(0x1F40)
    WaitChrThread(0x1C, 3)
    WaitChrThread(0x12, 3)
    WaitChrThread(0x13, 3)
    WaitChrThread(0x14, 3)
    WaitChrThread(0x15, 3)
    Return()

    # Function_30_A790 end

    def Function_31_A7F5(): pass

    label("Function_31_A7F5")

    EndChrThread(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x4)

    def lambda_A803():
        OP_95(0xFE, 6100, 0, -7700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A803)
    WaitChrThread(0xFE, 1)

    def lambda_A821():
        OP_95(0xFE, 15100, -1600, -17800, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A821)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_31_A7F5 end

    def Function_32_A83B(): pass

    label("Function_32_A83B")

    OP_93(0x1C, 0x14A, 0x1F4)

    def lambda_A847():
        OP_96(0xFE, 0xFFFFFCE0, 0x0, 0xFFFFE4A8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A847)
    WaitChrThread(0x1C, 1)
    Sleep(400)
    OP_93(0x1C, 0xF0, 0x1F4)

    def lambda_A86F():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_A86F)
    Return()

    # Function_32_A83B end

    def Function_33_A885(): pass

    label("Function_33_A885")

    EndChrThread(0xFE, 0x2)

    def lambda_A88E():
        OP_95(0xFE, -3700, 0, -7400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A88E)
    WaitChrThread(0xFE, 1)

    def lambda_A8AC():
        OP_95(0xFE, -11600, 0, -12000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_A8AC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_33_A885 end

    def Function_34_A8C6(): pass

    label("Function_34_A8C6")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    LoadChrToIndex("chr/ch00150.itc", 0x1E)
    LoadChrToIndex("apl/ch50017.itc", 0x1F)
    OP_68(45000, -1500, -22500, 0)
    MoveCamera(37, 30, 0, 0)
    OP_6E(480, 0)
    SetCameraDistance(20500, 0)
    SetChrPos(0x101, 43700, -2500, -23300, 90)
    SetChrPos(0x102, 43700, -2500, -21900, 90)
    SetChrPos(0x103, 42600, -2500, -23100, 90)
    SetChrPos(0x104, 42600, -2500, -21700, 90)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x8, 0x4)
    SetChrPos(0x8, 47500, -2100, -22500, 270)
    FadeToBright(1000, 0)
    OP_0D()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x52, 7)), scpexpr(EXPR_END)), "loc_AA5A")

    #N0503
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "#11Pま、また来たのかよ！？\x02",
    )

    CloseMessageWindow()

    def lambda_A9E2():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_A9E2)
    WaitChrThread(0x8, 1)

    #N0504
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        (
            "#11Pだから、お前らみたいな警察と\x01",
            "ヴァルドさんが話をするもんか！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AD50")

    label("loc_AA5A")


    #N0505
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "#11Pお、お前らは……！\x02",
    )

    CloseMessageWindow()

    #C0506
    ChrTalk(
        0x101,
        (
            "#6P#0005Fその格好……\x02\x03",

            "#0001Fひょっとしてここが\x01",
            "『サーベルバイパー』の？\x02",
        )
    )

    CloseMessageWindow()

    #C0507
    ChrTalk(
        0x103,
        (
            "#6P#0203Fライブハウス『イグニス』……\x02\x03",

            "#0200F元々、倉庫だった場所を\x01",
            "改装した店のようですね。\x02\x03",

            "税金が払われていないので\x01",
            "詳細は判りませんが……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AB6D():
        OP_96(0xFE, 0xB4DC, 0xFFFFF704, 0xFFFFA81C, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_AB6D)
    WaitChrThread(0x8, 1)

    #N0508
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "#11Pむ、無視すんなよ！\x02",
    )

    CloseMessageWindow()

    #N0509
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        (
            "#11Pいくらオレが新米だからって\x01",
            "サーベルバイパーの一員なんだぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0510
    ChrTalk(
        0x101,
        (
            "#6P#0006Fああ……ゴメン。\x02\x03",

            "#0001Fその、君たちのヘッドに\x01",
            "話を聞きたくて来たんだけど……\x02\x03",

            "取り次いでもらえるかな？\x02",
        )
    )

    CloseMessageWindow()

    #N0511
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "#11Pヴァルドさんに？\x02",
    )

    CloseMessageWindow()

    #N0512
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        (
            "#11Pフン、お前らみたいな警察と\x01",
            "ヴァルドさんが話をするもんか！\x02",
        )
    )

    CloseMessageWindow()

    #C0513
    ChrTalk(
        0x101,
        "#6P#0011Fいや、でも……\x02",
    )

    CloseMessageWindow()

    #N0514
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "#11Pダメだったら、ダメだ！\x02",
    )

    CloseMessageWindow()

    label("loc_AD50")


    #N0515
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "#11Pとっとと帰れよなっ！\x02",
    )

    CloseMessageWindow()

    #C0516
    ChrTalk(
        0x101,
        "#6P#0001F（困ったな……）\x02",
    )

    CloseMessageWindow()

    #C0517
    ChrTalk(
        0x104,
        (
            "#0300F#6P（と言うか、不良にしては\x01",
            "  ずいぶん可愛らしい小僧だな……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    #C0518
    ChrTalk(
        0x102,
        (
            "#0102F#5P──ねえ。\x01",
            "あなた、お名前は？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_AE7C():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_AE7C)

    def lambda_AE89():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_AE89)

    def lambda_AE96():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_AE96)
    WaitChrThread(0x101, 2)

    #N0519
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "#11Pオ、オレ？\x02",
    )

    CloseMessageWindow()

    #N0520
    NpcTalk(
        0x8,
        "赤ジャージの少年",
        "#11Pディ、ディーノだけど。\x02",
    )

    CloseMessageWindow()

    #C0521
    ChrTalk(
        0x102,
        (
            "#0104F#5Pそう、ディーノ君ね。\x02\x03",

            "#0100Fディーノ君は、ここで不審な人間を\x01",
            "見張っているのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0522
    ChrTalk(
        0x8,
        "#11Pそ、そうさ！\x02",
    )

    CloseMessageWindow()

    #C0523
    ChrTalk(
        0x8,
        (
            "#11Pヴァルドさんに頼まれて\x01",
            "テスタメンツどもが入らないよう\x01",
            "ここで見張りをしてるんだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0524
    ChrTalk(
        0x8,
        (
            "#11Pべ、別に他の先輩たちに\x01",
            "押し付けられたんじゃないからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0525
    ChrTalk(
        0x102,
        (
            "#0103F#5Pなるほど、立派な役目ね。\x02\x03",

            "#0101Fでも、私たちは\x01",
            "テスタメンツの一員じゃないわ。\x02\x03",

            "だったら案内してくれても\x01",
            "いいんじゃないかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0526
    ChrTalk(
        0x8,
        "#11Pだ、だけど……\x02",
    )

    CloseMessageWindow()

    #C0527
    ChrTalk(
        0x8,
        (
            "#11Pさっき先輩たちと戦ってたし、\x01",
            "そんな奴らを案内したら……\x02",
        )
    )

    CloseMessageWindow()

    #C0528
    ChrTalk(
        0x102,
        (
            "#0109F#5Pふふ、戦ったといっても、\x01",
            "あのくらい貴方たちにとったら\x01",
            "挨拶みたいなものでしょう？\x02\x03",

            "#0102F貴方たちのリーダーだって\x01",
            "気にしていないみたいだったし。\x02",
        )
    )

    CloseMessageWindow()

    #C0529
    ChrTalk(
        0x8,
        "#11Pで、でも……\x02",
    )

    CloseMessageWindow()

    #C0530
    ChrTalk(
        0x102,
        (
            "#0106F#5Pうーん、それでも\x01",
            "信用できないのなら──\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B1E0():

        label("loc_B1E0")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_B1E0")

    QueueWorkItem2(0x101, 2, lambda_B1E0)

    def lambda_B1F2():

        label("loc_B1F2")

        TurnDirection(0xFE, 0x102, 500)
        Yield()
        Jump("loc_B1F2")

    QueueWorkItem2(0x103, 2, lambda_B1F2)
    OP_68(45330, -1500, -22310, 1000)

    def lambda_B215():
        OP_96(0xFE, 0xB02C, 0xFFFFF63C, 0xFFFFA81C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B215)
    WaitChrThread(0x102, 1)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x102, 0x1E)
    SetChrSubChip(0x102, 0x0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    #C0531
    ChrTalk(
        0x8,
        "#11Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0532
    ChrTalk(
        0x101,
        "#6P#0005Fお、おい……！？\x02",
    )

    CloseMessageWindow()

    #C0533
    ChrTalk(
        0x103,
        "#6P#0205Fエリィさん……？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(300)
    #Sound(1174, 255, 100, 0)    #voice#Elie
    Fade(250)
    SetChrFlags(0x102, 0x10)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sleep(800)

    #C0534
    ChrTalk(
        0x102,
        (
            "#5P#0100F──私の銃を\x01",
            "貴方に預けてもいいわ。\x02\x03",

            "大切にしているものだから\x01",
            "ちゃんと返して欲しいけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0535
    ChrTalk(
        0x8,
        "#11P……～～っ～～……！\x02",
    )

    CloseMessageWindow()

    #C0536
    ChrTalk(
        0x8,
        (
            "#11Pい、いいよ！\x01",
            "そこまでしなくてもさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0537
    ChrTalk(
        0x8,
        (
            "#11Pヴァルドさんに聞いてくる！\x01",
            "絶対に入ってくんなよな！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_B43B():
        OP_95(0xFE, 48000, -2100, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B43B)
    Sleep(800)
    Fade(100)
    ClearChrFlags(0x102, 0x10)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    WaitChrThread(0x8, 1)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xF, 0x0, 0x0)
    Sound(116, 0, 100, 0)
    OP_79(0x4)

    def lambda_B48F():
        OP_95(0xFE, 50000, -2100, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B48F)

    def lambda_B4A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B4A9)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)
    OP_79(0x4)
    OP_68(44610, -1500, -22020, 1200)

    def lambda_B4E8():
        OP_96(0xFE, 0xAAB4, 0xFFFFF63C, 0xFFFFAA74, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B4E8)
    WaitChrThread(0x102, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x1)

    #C0538
    ChrTalk(
        0x104,
        "#0302F#6Pやれやれ、大胆だねぇ。\x02",
    )

    CloseMessageWindow()

    #C0539
    ChrTalk(
        0x103,
        "#6P#0206Fびっくりしました……\x02",
    )

    CloseMessageWindow()

    #C0540
    ChrTalk(
        0x101,
        (
            "#12P#0004F……凄いな、エリィは。\x02\x03",

            "#0002Fあんな交渉の仕方、\x01",
            "俺にはとても無理だよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    #C0541
    ChrTalk(
        0x102,
        (
            "#0104F#5Pふふ、こういった交渉は\x01",
            "結構慣れているから任せて。\x02\x03",

            "#0108Fでも、あのヴァルドって人には\x01",
            "通用しないと思うわ。\x02\x03",

            "#0101Fワジ君の時みたいに\x01",
            "貴方が話した方がいいと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0542
    ChrTalk(
        0x101,
        "#12P#0000F……ああ、判ってる。\x02",
    )

    CloseMessageWindow()
    OP_71(0x4, 0x0, 0xF, 0x0, 0x0)
    Sound(116, 0, 100, 0)
    OP_79(0x4)

    def lambda_B6A3():
        OP_95(0xFE, 46200, -2400, -22500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B6A3)

    def lambda_B6BD():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_B6BD)

    def lambda_B6CE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B6CE)
    Sleep(50)

    def lambda_B6DE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B6DE)
    Sleep(50)

    def lambda_B6EE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B6EE)
    Sleep(50)

    def lambda_B6FE():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B6FE)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x8, 2)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)

    #C0543
    ChrTalk(
        0x8,
        "#11Pヴァルドさんがお呼びだ！\x02",
    )

    CloseMessageWindow()

    #C0544
    ChrTalk(
        0x8,
        (
            "#11P入ってもいいけど……\x01",
            "変なことをしたら\x01",
            "タダじゃ済まないからな！\x02",
        )
    )

    CloseMessageWindow()

    #C0545
    ChrTalk(
        0x102,
        "#0109F#6Pふふ、ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0546
    ChrTalk(
        0x101,
        "#6P#0002Fそれじゃあ、失礼するよ。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(20750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_4C(0x8, 0xFF)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 44880, -2500, -20090, 225)
    SetChrPos(0x0, 43000, -2500, -22500, 90)
    SetScenarioFlags(0x42, 2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_34_A8C6 end

    def Function_35_B827(): pass

    label("Function_35_B827")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06000.itc", 0x1E)
    LoadChrToIndex("apl/ch50010.itc", 0x1F)
    LoadEffect(0x0, "event\\eva02_00.eff")
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    OP_68(40100, -1300, -23900, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 44400, -2500, -23600, 270)
    SetChrPos(0x102, 44400, -2500, -22200, 270)
    SetChrPos(0x103, 45800, -2500, -23600, 270)
    SetChrPos(0x104, 45800, -2500, -22200, 270)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    OP_52(0x1D, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu02100.itp")

    def lambda_B932():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B932)
    Sleep(50)

    def lambda_B94F():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B94F)
    Sleep(50)

    def lambda_B96C():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B96C)
    Sleep(50)

    def lambda_B989():
        OP_98(0xFE, 0xFFFFEC78, 0x0, 0xFFFFFC18, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B989)
    SetCameraDistance(19500, 3000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)

    def lambda_B9B9():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_B9B9)
    WaitChrThread(0x102, 1)

    def lambda_B9CA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_B9CA)
    WaitChrThread(0x103, 1)

    def lambda_B9DB():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_B9DB)
    WaitChrThread(0x104, 1)

    def lambda_B9EC():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_B9EC)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)

    #C0547
    ChrTalk(
        0x102,
        (
            "#1P#0108F……どういう事かしら。\x02\x03",

            "#0101Fどちらのメンバーも\x01",
            "闇討ちに遭っているなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0548
    ChrTalk(
        0x103,
        (
            "#2P#0203Fどちらかが嘘を付いている……\x01",
            "そういう訳でも無さそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0549
    ChrTalk(
        0x101,
        "#6P#0008F…………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_BB23():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BB23)

    def lambda_BB30():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BB30)

    def lambda_BB3D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BB3D)
    WaitChrThread(0x103, 2)

    #C0550
    ChrTalk(
        0x102,
        "#1P#0105F……どうしたの？\x02",
    )

    CloseMessageWindow()

    #C0551
    ChrTalk(
        0x104,
        (
            "#5P#0301Fまさか、さっきのタイマンで\x01",
            "どこかやられちまったか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0552
    ChrTalk(
        0x101,
        (
            "#6P#0000Fああ、いや……\x02\x03",

            "向こうも手加減してたし、\x01",
            "大したことはないさ。\x02\x03",

            "#0003Fただ、少し妙だと思ってね。\x02",
        )
    )

    CloseMessageWindow()

    #C0553
    ChrTalk(
        0x103,
        "#2P#0205F妙……ですか？\x02",
    )

    CloseMessageWindow()

    #C0554
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ……\x02\x03",

            "#0008Fどちらも５日前の夜……\x01",
            "違う場所で同時に襲われている。\x02\x03",

            "お互いが偶然、相手のメンバーを\x01",
            "闇討ちするつもりだったとしても……\x02\x03",

            "#0001F同時にそれだけの人数が動いてたら\x01",
            "お互いに気付かないって事があるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0555
    ChrTalk(
        0x102,
        "#1P#0101Fあ……\x02",
    )

    CloseMessageWindow()

    #C0556
    ChrTalk(
        0x104,
        (
            "#5P#0303F……確かにそうだな。\x02\x03",

            "#0301F戦闘のプロ同士でもない限り、\x01",
            "普通なら考えられない状況だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0557
    ChrTalk(
        0x103,
        (
            "#2P#0201Fでは、どちらかが先にやられて\x01",
            "その報復のため動いたというのは？\x02",
        )
    )

    CloseMessageWindow()

    #C0558
    ChrTalk(
        0x102,
        (
            "#1P#0103Fううん、それもおかしいわ。\x02\x03",

            "#0108F当然、先に闇討ちした方は\x01",
            "相手の報復を警戒するはず……\x02\x03",

            "なのにどちらのメンバーも\x01",
            "あっけなく不意を突かれている……\x02\x03",

            "#0101F……そういう事よね、ロイド？\x02",
        )
    )

    CloseMessageWindow()

    #C0559
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ……\x01",
            "この事件、何かがおかしい。\x02\x03",

            "#0008F必要なパズルのピースが\x01",
            "欠けてしまっているみたいな……\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x1D, 31700, -2500, -23600, 90)
    SetChrFlags(0x1D, 0x8)
    ClearChrFlags(0x1D, 0x80)
    ClearChrBattleFlags(0x1D, 0x8000)

    #N0560
    NpcTalk(
        0x1D,
        "女性の声",
        "フフン、お困りのようね？\x02",
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
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_BFCE():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_BFCE)

    def lambda_BFDB():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_BFDB)

    def lambda_BFE8():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_BFE8)

    def lambda_BFF5():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_BFF5)
    WaitChrThread(0x101, 2)
    Fade(500)
    OP_68(33700, -1400, -23600, 0)
    MoveCamera(313, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, 39300, -2500, -24200, 270)
    SetChrPos(0x102, 39300, -2500, -23000, 270)
    SetChrPos(0x103, 40800, -2500, -24200, 270)
    SetChrPos(0x104, 40800, -2500, -23000, 270)
    ClearChrFlags(0x1D, 0x8)
    SetChrPos(0x1D, 31700, -2500, -23600, 90)
    OP_68(38200, -1400, -23600, 2500)
    SetCameraDistance(20500, 2500)

    def lambda_C0AD():
        OP_95(0xFE, 36700, -2500, -23600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C0AD)
    WaitChrThread(0x1D, 1)
    OP_6F(0x11)

    #C0561
    ChrTalk(
        0x101,
        "#12P#0005Fあ、あなたは……！？\x02",
    )

    CloseMessageWindow()

    #C0562
    ChrTalk(
        0x102,
        "#0105Fクロスベルタイムズの……\x02",
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("女性")

    #A0563
    AnonymousTalk(
        0xFF,
        (
            "ハロハロー。\x01",
            "また会っちゃったわね。\x02\x03",

            "おっと、いい構図！\x02",
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

    def lambda_C1B9():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA1DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C1B9)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)

    def lambda_C22A():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA5C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C22A)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)

    def lambda_C29B():
        OP_96(0xFE, 0x8F5C, 0xFFFFF63C, 0xFFFFA3D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C29B)
    WaitChrThread(0x1D, 1)
    SetChrChipByIndex(0x1D, 0x1F)
    SetChrSubChip(0x1D, 0x0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x1D, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(817, 0, 100, 0)

    #C0564
    ChrTalk(
        0x101,
        "#12P#0001Fっ……\x02",
    )

    CloseMessageWindow()

    #C0565
    ChrTalk(
        0x103,
        "#12P#0211F……肖像権侵害です。\x02",
    )

    CloseMessageWindow()

    #N0566
    NpcTalk(
        0x1D,
        "女性",
        (
            "#2109F#5Pいや～、職業柄、\x01",
            "いい画#2Rえ#が撮れそうだと\x01",
            "反射的にやっちゃうのよねぇ。\x02\x03",

            "#2102Fまあ、記事の写真に\x01",
            "使うかもしれないんだし。\x02\x03",

            "ケチケチしないで欲しいなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0567
    ChrTalk(
        0x101,
        "#12P#0001Fあ、あのですね……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x48, 0)), scpexpr(EXPR_END)), "loc_C452")

    #C0568
    ChrTalk(
        0x102,
        (
            "#0101Fまた、あんな記事を書いて\x01",
            "笑い者にするつもりですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C4C6")

    label("loc_C452")


    #C0569
    ChrTalk(
        0x102,
        (
            "#0103F何だか面白い記事を\x01",
            "書かれたみたいですけど……\x02\x03",

            "#0101Fまた、そんな記事を書いて\x01",
            "笑い者にするつもりですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C4C6")

    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    OP_0D()
    Sleep(300)

    #N0570
    NpcTalk(
        0x1D,
        "女性",
        (
            "#2109F#5Pあはは、おかげであの記事、\x01",
            "結構評判みたいでね～。\x02\x03",

            "#2100Fそれよりも、何だか今度は\x01",
            "面白いネタに絡んでるみたいね？\x02\x03",

            "ちょっとお姉さんの取材に\x01",
            "協力してくれないかしら？\x02\x03",

            "この前の記事のお礼として\x01",
            "お姉さんが奢ってあげるからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0571
    ChrTalk(
        0x101,
        (
            "#12P#0003Fくっ……\x02\x03",

            "#0001F捜査中の情報を、部外者に\x01",
            "簡単に洩らせるわけないでしょう。\x02\x03",

            "それもマスコミの人間なんかに。\x02",
        )
    )

    CloseMessageWindow()

    #N0572
    NpcTalk(
        0x1D,
        "女性",
        (
            "#2106F#5Pもう、つれないなぁ。\x02\x03",

            "せっかく美味しい東方料理を\x01",
            "ご馳走してあげるのにぃ……\x02\x03",

            "#2102F……デザートとして、\x01",
            "『欠けたパズルのピース』もね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0573
    ChrTalk(
        0x101,
        "#12P#0005Fなっ……\x02",
    )

    CloseMessageWindow()

    #C0574
    ChrTalk(
        0x104,
        (
            "#0303Fなるほど……\x01",
            "情報交換ってことか。\x02",
        )
    )

    CloseMessageWindow()

    #N0575
    NpcTalk(
        0x1D,
        "女性",
        (
            "#2104F#5Pうふふん……♪\x02\x03",

            "#2100Fその気があるなら\x01",
            "東通りに出たところにある\x01",
            "『龍老飯店』にいらっしゃい。\x02\x03",

            "お姉さん、先に一人で\x01",
            "飲んで待っててあげるから。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x10E, 0x1F4)

    def lambda_C83B():
        OP_95(0xFE, 35700, -2500, -23600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C83B)
    WaitChrThread(0x1D, 1)
    OP_63(0x1D, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x1D, 0x5A, 0x1F4)

    #N0576
    NpcTalk(
        0x1D,
        "女性",
        (
            "#5P#2105F──そうそう。\x01",
            "まだ名乗ってなかったわね。\x02\x03",

            "#2100F《クロスベルタイムズ》の記者、\x01",
            "グレイス・リンよ。\x02\x03",

            "#2109Fグレイスお姉さんって呼んでね♪\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1D, 0x10E, 0x1F4)

    def lambda_C918():
        OP_95(0xFE, 25700, -2500, -23600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_C918)
    Sleep(3000)
    Fade(1000)
    OP_68(40100, -1300, -23900, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 39400, -2500, -24600, 270)
    SetChrPos(0x102, 39400, -2500, -23200, 270)
    SetChrPos(0x103, 40800, -2500, -24600, 270)
    SetChrPos(0x104, 40800, -2500, -23200, 270)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    WaitChrThread(0x1D, 1)
    ClearChrFlags(0x1D, 0x8000)
    SetChrFlags(0x1D, 0x80)
    SetChrBattleFlags(0x1D, 0x8000)

    #C0577
    ChrTalk(
        0x101,
        (
            "#11P#0001Fグレイス・リン……\x01",
            "クロスベルタイムズの記者か。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x104, 0xE1, 0x190)

    #C0578
    ChrTalk(
        0x104,
        (
            "#5P#0300Fウサン臭そうな姉さんだが\x01",
            "色々と情報は持ってそうだな。\x02\x03",

            "ここは誘いに乗ってみるか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_CABD():
        OP_93(0xFE, 0x2D, 0x190)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CABD)
    Sleep(100)

    def lambda_CACD():
        OP_93(0xFE, 0x87, 0x190)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_CACD)
    Sleep(50)

    def lambda_CADD():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_CADD)
    WaitChrThread(0x101, 2)

    #C0579
    ChrTalk(
        0x101,
        (
            "#6P#0006Fう、うーん……\x02\x03",

            "#0001Fご馳走になるかはともかく、\x01",
            "話を聞くだけは聞いてみよう。\x02\x03",

            "本部がアテにならない以上、\x01",
            "少しでも多く情報が欲しい所だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0580
    ChrTalk(
        0x102,
        (
            "#1P#0103F……そうね。\x01",
            "記者なら情報通でしょうし。\x02\x03",

            "#0101Fただ、話しすぎないよう、\x01",
            "こちらも気をつけておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0581
    ChrTalk(
        0x103,
        (
            "#2P#0203F……同感です。\x02\x03",

            "#0211F気を抜いたらどこまでも\x01",
            "図々しくしてくるタイプかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0582
    ChrTalk(
        0x101,
        (
            "#6P#0002F（うーん……\x01",
            "  散々な言われようだな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_68(40100, -500, -23900, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 40100, -2500, -23900, 270)
    SetChrPos(0x1, 40100, -2500, -23900, 270)
    SetChrPos(0x2, 40100, -2500, -23900, 270)
    SetChrPos(0x3, 40100, -2500, -23900, 270)
    OP_4C(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetScenarioFlags(0x42, 4)
    OP_29(0x3E, 0x1, 0x4)
    EventEnd(0x5)
    Return()

    # Function_35_B827 end

    def Function_36_CD23(): pass

    label("Function_36_CD23")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    OP_68(-19000, 1000, -10300, 0)
    MoveCamera(60, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, -19700, 0, -11000, 45)
    SetChrPos(0x102, -18300, 0, -11000, 315)
    SetChrPos(0x103, -19700, 0, -9600, 135)
    SetChrPos(0x104, -18300, 0, -9600, 225)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    MoveCamera(70, 30, 0, 3000)
    SetCameraDistance(17500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0583
    ChrTalk(
        0x102,
        (
            "#0106F……まさか全員、\x01",
            "行方不明になってるなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0584
    ChrTalk(
        0x104,
        (
            "#5P#0303F嫌な予感、的中だな……\x02\x03",

            "#0301F自発的に消えちまったのか、\x01",
            "それとも拉致されちまったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0585
    ChrTalk(
        0x103,
        (
            "#6P#0206F現時点では情報が少なすぎて\x01",
            "どちらの可能性も考えられますね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC8, 3)), scpexpr(EXPR_END)), "loc_CF96")

    #C0586
    ChrTalk(
        0x101,
        (
            "#12P#0003F……失踪した５人については\x01",
            "氷山の一角かもしれない。\x02\x03",

            "#0001Fクロスベル市全体では\x01",
            "かなりの人数が失踪している\x01",
            "可能性が高そうだな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D027")

    label("loc_CF96")


    #C0587
    ChrTalk(
        0x101,
        (
            "#12P#0003F……失踪した４人については\x01",
            "氷山の一角かもしれない。\x02\x03",

            "#0001Fクロスベル市全体では\x01",
            "かなりの人数が失踪している\x01",
            "可能性が高そうだな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D027")


    #C0588
    ChrTalk(
        0x102,
        (
            "#0108Fええ……\x01",
            "一体どれだけの人たちが\x01",
            "消えてしまったのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0589
    ChrTalk(
        0x104,
        (
            "#5P#0301Fどうする、ロイド。\x02\x03",

            "一人一人を捜すってのは\x01",
            "さすがに難しそうだぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0590
    ChrTalk(
        0x101,
        (
            "#12P#0006Fああ……こちらの手が\x01",
            "圧倒的に不足している。\x02\x03",

            "#0008Fこうなると上からの圧力で\x01",
            "一課が動けないのが痛いな……\x02",
        )
    )

    CloseMessageWindow()

    #C0591
    ChrTalk(
        0x103,
        (
            "#6P#0202Fでしたら二課のドノバン警部に\x01",
            "相談してみてはどうでしょう？\x02\x03",

            "以前、手伝った貸しもありますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0592
    ChrTalk(
        0x101,
        (
            "#12P#0003Fいや……難しいと思う。\x02\x03",

            "#0001Fダドリー捜査官がわざわざ、\x01",
            "支援課を頼ってきている以上、\x01",
            "二課にも圧力が掛かっているはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0593
    ChrTalk(
        0x103,
        "#6P#0206Fなるほど……確かに。\x02",
    )

    CloseMessageWindow()

    #C0594
    ChrTalk(
        0x102,
        (
            "#0108Fとなると広域防犯課も\x01",
            "状況は同じでしょうね……\x02\x03",

            "#0106F警官隊のマンパワーが使えれば\x01",
            "すごく助かるのだけど……\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_D312():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_D312)
    Sleep(50)

    def lambda_D322():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_D322)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x2)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x3)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0595
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0001Fはい、特務支援課、\x01",
            "ロイド・バニングスです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("男の声")

    #A0596
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "おい、新米ども……！\x02\x03",

            "まさか何かしでかしたんじゃ\x01",
            "ないだろうな……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0597
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011Fへ……\x02\x03",

            "#0001Fもしかしてその声は\x01",
            "ダドリー捜査官ですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0598
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もしかしても何もない！\x02\x03",

            "お前たち、ルバーチェに何か\x01",
            "ちょっかいをかけなかったか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0599
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fい、いえ別に……\x02\x03",

            "#0003F現在は薬物捜査の方に\x01",
            "専念していますから。\x02\x03",

            "#0001F……何かあったんですか？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ダドリーの声")

    #A0600
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "あったも何も！\x01",
            "連中の事務所が……\x02\x03",

            "……ゴホン、何でもない。\x02\x03",

            "何もしてないなら構わん。\x01",
            "そのまま捜査を続けていろ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(825, 0, 100, 0)
    Sleep(500)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0601
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005Fあ……\x02",
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
    SetChrSubChip(0x101, 0x2)
    Sound(807, 0, 100, 0)
    Sleep(300)

    #C0602
    ChrTalk(
        0x101,
        "#12P#0013F………………………………\x02",
    )

    CloseMessageWindow()

    #C0603
    ChrTalk(
        0x102,
        (
            "#0101Fダドリー捜査官から？\x01",
            "何かあったの？\x02",
        )
    )

    CloseMessageWindow()

    #C0604
    ChrTalk(
        0x101,
        "#12P#0006Fいや……\x02",
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
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0605
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドはエリィたちに\x01",
            "ダドリーとのやり取りを伝えた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)

    #C0606
    ChrTalk(
        0x104,
        "#5P#0301Fなんだそりゃ……\x02",
    )

    CloseMessageWindow()

    #C0607
    ChrTalk(
        0x103,
        (
            "#6P#0206F……露骨に怪しいですね。\x02\x03",

            "#0201Fルバーチェ商会で\x01",
            "何かあったんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0608
    ChrTalk(
        0x101,
        "#12P#0003F可能性は高そうだな……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0609
    ChrTalk(
        0x104,
        (
            "#5P#0300Fこりゃ、行ってみるしか\x01",
            "ねえんじゃねえのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0610
    ChrTalk(
        0x102,
        (
            "#0103Fそうね……抗争には関わるなって\x01",
            "釘は刺されているけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0611
    ChrTalk(
        0x103,
        (
            "#6P#0202F失踪者にマフィアが絡んでいるなら\x01",
            "大義名分は立つのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0612
    ChrTalk(
        0x101,
        (
            "#12P#0001Fああ……\x01",
            "ルバーチェ商会に急ごう！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    SetChrPos(0x0, -19000, 0, -10000, 180)
    SetScenarioFlags(0xC3, 7)
    OP_29(0x4C, 0x1, 0xC)
    OP_24(0x326)
    EventEnd(0x5)
    Return()

    # Function_36_CD23 end

    def Function_37_D94C(): pass

    label("Function_37_D94C")

    EventBegin(0x1)
    OP_4B(0xF, 0xFF)
    TurnDirection(0xF, 0x0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D9F3")

    #C0613
    ChrTalk(
        0xF,
        "……待ちたまえ。\x02",
    )

    CloseMessageWindow()

    #C0614
    ChrTalk(
        0xF,
        (
            "悪いが我々は取り込み中でね。\x01",
            "ワジの話の邪魔を\x01",
            "させるわけにはいかない。\x02",
        )
    )

    CloseMessageWindow()

    #C0615
    ChrTalk(
        0xF,
        "部外者は立ち去ってもらいたいな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_DA34")

    label("loc_D9F3")


    #C0616
    ChrTalk(
        0xF,
        "…………………………\x02",
    )

    CloseMessageWindow()

    #C0617
    ChrTalk(
        0xF,
        (
            "客ならまた\x01",
            "後日にしてくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DA34")

    Sleep(50)
    SetChrPos(0x0, -19660, 0, -10600, 180)
    OP_93(0xF, 0xE1, 0x0)
    OP_4C(0xF, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_37_D94C end

    def Function_38_DA56(): pass

    label("Function_38_DA56")

    TalkBegin(0xFF)
    OP_4B(0x8, 0xFF)
    SetChrName("")

    #A0618
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中からは騒がしい音楽が\x01",
            "漏れ聞こえてくる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x8, 0x0, 500)

    #C0619
    ChrTalk(
        0x8,
        (
            "こ、こら！\x01",
            "ここはヨソ者は入れないぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0620
    ChrTalk(
        0x8,
        "とっととあっちへ行けよっ！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DB7B")
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0621
    ChrTalk(
        0x101,
        "#0001F（何だか妙な具合だな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 0)

    label("loc_DB7B")

    OP_93(0x8, 0xE1, 0x1F4)
    OP_4C(0x8, 0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_38_DA56 end

    def Function_39_DB8A(): pass

    label("Function_39_DB8A")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0622
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《ナインヴァリ》\x01",
            "　　　　本日臨時休業。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_39_DB8A end

    def Function_40_DBE1(): pass

    label("Function_40_DBE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0xA, 0x1, 0x1)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC04")
    Call(0, 42)
    Jump("loc_DCBC")

    label("loc_DC04")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0623
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x47, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DCB9")

    #C0624
    ChrTalk(
        0x101,
        (
            "#0001F大分すすけている……\x01",
            "長い間使われてないみたいだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x47, 7)

    label("loc_DCB9")

    TalkEnd(0xFF)

    label("loc_DCBC")

    Return()

    # Function_40_DBE1 end

    def Function_41_DCBD(): pass

    label("Function_41_DCBD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00400.itc", 0x1E)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    OP_71(0x4, 0xF, 0xF, 0x0, 0x0)
    OP_68(43800, -490, -23000, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 49400, -2500, -23600, 270)
    SetChrPos(0x102, 49400, -2500, -22200, 270)
    SetChrPos(0x103, 50800, -2500, -23600, 270)
    SetChrPos(0x104, 50800, -2500, -22200, 270)
    SetChrPos(0x1A, 34870, -2490, -22900, 90)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_DD9C():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DD9C)

    def lambda_DDB6():
        OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DDB6)
    Sleep(50)

    def lambda_DDCA():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DDCA)

    def lambda_DDE4():
        OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DDE4)
    Sleep(50)

    def lambda_DDF8():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DDF8)

    def lambda_DE12():
        OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DE12)
    Sleep(50)

    def lambda_DE26():
        OP_97(0xFE, 0xFFFFE890, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DE26)

    def lambda_DE40():
        OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DE40)
    SetCameraDistance(20000, 3000)
    FadeToBright(2000, 0)
    WaitChrThread(0x101, 1)

    def lambda_DE67():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_DE67)
    WaitChrThread(0x102, 1)

    def lambda_DE78():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_DE78)
    WaitChrThread(0x103, 1)

    def lambda_DE89():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_DE89)
    WaitChrThread(0x104, 1)

    def lambda_DE9A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_DE9A)
    WaitChrThread(0x104, 2)
    OP_6F(0x10)
    OP_71(0x4, 0xF, 0x0, 0x0, 0x0)
    Sound(117, 0, 100, 0)

    #C0625
    ChrTalk(
        0x104,
        "#0301Fどうなってんだ、ありゃあ……\x02",
    )

    CloseMessageWindow()

    #C0626
    ChrTalk(
        0x102,
        (
            "#0108F状況は判らないけれど、\x01",
            "リストにあったディーノ君は\x01",
            "見当たらなかったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0627
    ChrTalk(
        0x101,
        (
            "#0003F#6Pああ、それに連中の様子も\x01",
            "普通じゃなかったし……\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x1A, 0x80)
    ClearChrBattleFlags(0x1A, 0x8000)

    #N0628
    NpcTalk(
        0x1A,
        "涼しげな声",
        "──やあ、ちょっといいかな。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(42800, -490, -23000, 2000)

    def lambda_E00C():
        OP_97(0xFE, 0x1770, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_E00C)

    def lambda_E026():
        TurnDirection(0x101, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E026)
    Sleep(50)

    def lambda_E036():
        TurnDirection(0x102, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E036)
    Sleep(50)

    def lambda_E046():
        TurnDirection(0x103, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E046)
    Sleep(50)

    def lambda_E056():
        TurnDirection(0x104, 0x1A, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E056)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x1A, 1)

    #C0629
    ChrTalk(
        0x103,
        (
            "#0205F#11Pワジさん。\x01",
            "どうしてこんな所に……\x02",
        )
    )

    CloseMessageWindow()

    #C0630
    ChrTalk(
        0x1A,
        (
            "#0404Fバイパーの様子が気になってさ。\x02\x03",

            "#0400F新入りの例の子、\x01",
            "今朝から居ないみたいじゃない。\x02\x03",

            "#0406Fま、あんな事やっちゃった後だし、\x01",
            "まさかとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0631
    ChrTalk(
        0x104,
        "#0305F#11Pお前……何か知ってるのか？\x02",
    )

    CloseMessageWindow()

    #C0632
    ChrTalk(
        0x1A,
        (
            "#0402Fまあね。\x02\x03",

            "#0409Fここじゃ何だし\x01",
            "トリニティにおいでよ。\x02\x03",

            "僕の知ってる範囲でよければ\x01",
            "教えてあげるからさ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1A, 0x10E, 0x1F4)
    OP_97(0x1A, 0xFFFFE890, 0x0, 0x0, 0xBB8, 0x0)
    SetChrFlags(0x1A, 0x80)
    SetChrBattleFlags(0x1A, 0x8000)
    ClearChrFlags(0x1A, 0x8000)

    #C0633
    ChrTalk(
        0x101,
        (
            "#0006F#11P……サーベルバイパーの\x01",
            "情報については\x01",
            "ワジに頼るしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0634
    ChrTalk(
        0x102,
        (
            "#0101F#11Pそうね……\x01",
            "何かあったことだけは\x01",
            "確かみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D5(0x1E)
    OP_71(0x4, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFlags(0x4, 0x10)
    OP_68(43500, -490, -22900, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x0, 43500, -2490, -22900, 270)
    SetChrPos(0x1, 43500, -2490, -22900, 270)
    SetChrPos(0x2, 43500, -2490, -22900, 270)
    SetChrPos(0x3, 43500, -2490, -22900, 270)
    SetScenarioFlags(0xD0, 5)
    OP_29(0x4C, 0x1, 0x8)
    EventEnd(0x5)
    Return()

    # Function_41_DCBD end

    def Function_42_E33A(): pass

    label("Function_42_E33A")

    EventBegin(0x0)
    Fade(500)
    OP_68(34400, 3600, -20130, 0)
    MoveCamera(35, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19680, 0)
    SetChrPos(0x101, 34840, 2450, -21150, 0)
    SetChrPos(0x102, 35840, 2450, -21150, 315)
    SetChrPos(0x103, 33840, 2450, -21150, 45)
    SetChrPos(0x104, 32840, 2450, -21150, 45)
    OP_0D()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0635
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

    #C0636
    ChrTalk(
        0x101,
        (
            "#11P#0000Fここがイメルダさんの言っていた\x01",
            "アパートみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0637
    ChrTalk(
        0x102,
        (
            "#11P#0100F現在運営休止中……\x01",
            "随分とすすけちゃってるわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0638
    ChrTalk(
        0x103,
        (
            "#5P#0200Fとりあえず\x01",
            "中へ入ってみましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0639
    ChrTalk(
        0x101,
        "#11P#0000Fああ、ちょっと待ってくれ。\x02",
    )

    CloseMessageWindow()
    OP_97(0x101, 0x0, 0x0, 0x3E8, 0x7D0, 0x0)
    Sleep(200)
    Sound(809, 0, 100, 0)
    Sleep(500)
    OP_93(0x101, 0xE1, 0x1F4)

    #C0640
    ChrTalk(
        0x101,
        (
            "#5P#0003Fよし、開いたぞ。\x02\x03",

            "#0001F魔獣が出るということだから\x01",
            "油断しないようにしないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0641
    ChrTalk(
        0x104,
        (
            "#5P#0300Fうっし、んじゃあ\x01",
            "気合入れて行くか！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 34840, 2450, -20500, 0)
    OP_65(0x3, 0x1)
    SetMapObjFlags(0x1, 0x10)
    SetScenarioFlags(0x6E, 6)
    EventEnd(0x5)
    Return()

    # Function_42_E33A end

    def Function_43_E5D1(): pass

    label("Function_43_E5D1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_4B(0xD, 0xFF)
    OP_4B(0xE, 0xFF)
    OP_4B(0xF, 0xFF)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x40)
    SetChrFlags(0xD, 0x40)
    SetChrFlags(0xE, 0x40)
    SetChrFlags(0x11, 0x40)
    ClearChrFlags(0x21, 0x4)
    ClearChrFlags(0xD, 0x4)
    ClearChrFlags(0xE, 0x4)
    ClearChrFlags(0x11, 0x4)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    Call(0, 44)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30953.itc", 0x2A)
    LoadChrToIndex("chr/ch31853.itc", 0x2B)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 45)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    LoadChrToIndex("chr/ch30951.itc", 0x32)
    LoadChrToIndex("chr/ch31851.itc", 0x33)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 46)
    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E80E")
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch30953.itc", 0x2A)
    LoadChrToIndex("chr/ch31853.itc", 0x2B)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_29(0x12, 0x1, 0x4)
    OP_2C(0x12, 0x5)
    Call(0, 49)
    Jump("loc_E8B7")

    label("loc_E80E")

    OP_32(0x0, 0xFC, 0x1)
    OP_32(0x1, 0xFC, 0x1)
    OP_32(0x2, 0xFC, 0x1)
    OP_32(0x3, 0xFC, 0x1)
    OP_32(0x0, 0x2, 0x1)
    OP_32(0x1, 0x2, 0x1)
    OP_32(0x2, 0x2, 0x1)
    OP_32(0x3, 0x2, 0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch30950.itc", 0x22)
    LoadChrToIndex("chr/ch31850.itc", 0x23)
    LoadChrToIndex("chr/ch30850.itc", 0x24)
    LoadChrToIndex("chr/ch31750.itc", 0x25)
    LoadChrToIndex("chr/ch00153.itc", 0x27)
    LoadChrToIndex("chr/ch00253.itc", 0x28)
    LoadChrToIndex("chr/ch00353.itc", 0x29)
    LoadChrToIndex("chr/ch30853.itc", 0x2C)
    LoadChrToIndex("chr/ch31753.itc", 0x2D)
    LoadChrToIndex("chr/ch30900.itc", 0x2E)
    LoadChrToIndex("chr/ch06700.itc", 0x2F)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_29(0x12, 0x1, 0x3)
    Call(0, 50)

    label("loc_E8B7")

    Call(0, 51)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0642
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "クエスト【テスタメンツの稽古依頼】\x07\x00",
            "を達成した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E940")
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x2A)
    OP_D5(0x2B)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)
    Jump("loc_E95E")

    label("loc_E940")

    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_D5(0x2E)
    OP_D5(0x2F)

    label("loc_E95E")

    SetChrPos(0x0, 130, 0, -5310, 0)
    OP_4C(0xD, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    SetChrFlags(0x21, 0x4)
    SetChrFlags(0xD, 0x4)
    SetChrFlags(0xE, 0x4)
    SetChrFlags(0x11, 0x4)
    ClearChrFlags(0x21, 0x40)
    ClearChrFlags(0xD, 0x40)
    ClearChrFlags(0xE, 0x40)
    ClearChrFlags(0x11, 0x40)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E9FD")
    SetChrPos(0xA, -10970, 0, -9240, 135)
    SetChrPos(0xB, -11920, 0, -9620, 45)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xB, 0, 0, 0)

    label("loc_E9FD")

    OP_29(0x12, 0x4, 0x10)
    OP_29(0x12, 0x1, 0x5)
    SetScenarioFlags(0x0, 6)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_43_E5D1 end

    def Function_44_EA11(): pass

    label("Function_44_EA11")

    OP_68(830, 1200, -3860, 0)
    MoveCamera(176, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22640, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3150, 0, -4000, 270)
    SetChrPos(0x1F, 4080, 0, -4770, 270)
    SetChrPos(0x20, 4550, 0, -3310, 270)
    SetChrPos(0x1E, 5260, 0, -4350, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetCameraDistance(20640, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0643
    ChrTalk(
        0x1C,
        "#5P形式は４対４の戦闘。\x02",
    )

    CloseMessageWindow()

    #C0644
    ChrTalk(
        0x1C,
        (
            "#5Pテスタメンツは全力を以って\x01",
            "特務支援課を攻撃すべし！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(50, 40, -1, -1)
    SetChrName("メンバーたち")

    #A0645
    AnonymousTalk(
        0xFF,
        "#5S  ヤーッ！  \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    #C0646
    ChrTalk(
        0x1F,
        (
            "け、警察の護身術とやら、\x01",
            "見せてもらうぞ……\x02",
        )
    )

    CloseMessageWindow()

    #C0647
    ChrTalk(
        0xF,
        (
            "フン、こちらは\x01",
            "全力で行かせてもらう……\x02",
        )
    )

    CloseMessageWindow()

    #C0648
    ChrTalk(
        0xF,
        (
            "君達が不甲斐ないようなら\x01",
            "このまま倒してやるつもりだ。\x01",
            "覚悟するんだな！\x02",
        )
    )

    CloseMessageWindow()

    #C0649
    ChrTalk(
        0x104,
        (
            "#12P#0300Fおーおー、\x01",
            "活気があっていいこった。\x02",
        )
    )

    CloseMessageWindow()

    #C0650
    ChrTalk(
        0x101,
        (
            "#12P#0003F一応こちらの戦いぶりを見せつつ\x01",
            "彼らを制圧すれば完了だけど……\x02\x03",

            "#0001Fここで手加減したら\x01",
            "訓練にならないからな。\x02\x03",

            "みんな、遠慮はいらない。\x01",
            "本気で行こう！\x02",
        )
    )

    CloseMessageWindow()

    #C0651
    ChrTalk(
        0x102,
        "#11P#0101Fええ！\x02",
    )

    CloseMessageWindow()

    #C0652
    ChrTalk(
        0x103,
        "#12P#0201F了解です！\x02",
    )

    CloseMessageWindow()

    #C0653
    ChrTalk(
        0x1C,
        "#5P#4S──それでは戦闘開始！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x3E8)
    Battle("BattleInfo_88C", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_44_EA11 end

    def Function_45_EDDE(): pass

    label("Function_45_EDDE")

    OP_68(830, 1200, -3860, 0)
    MoveCamera(176, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20640, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3150, 0, -4000, 270)
    SetChrPos(0x1F, 4080, 0, -4770, 270)
    SetChrPos(0x20, 4550, 0, -3310, 270)
    SetChrPos(0x1E, 5260, 0, -4350, 270)
    SetChrPos(0x21, 10500, -230, -14120, 314)
    SetChrPos(0xD, 11110, -680, -15910, 314)
    SetChrPos(0xE, 12100, -550, -14490, 314)
    SetChrPos(0x11, 13530, -1180, -16690, 314)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x3)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xF, 0x3)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrSubChip(0x1F, 0x3)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrSubChip(0x1E, 0x3)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x3)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0654
    ChrTalk(
        0x101,
        (
            "#12P#0003Fふう、こんな所か……\x02\x03",

            "#0000F君たち、大丈夫か？\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_95(0x101, -880, 0, -4000, 1000, 0x0)
    Sleep(300)

    #C0655
    ChrTalk(
        0x1F,
        "#5Pや、や、やられたな……\x02",
    )

    CloseMessageWindow()

    #C0656
    ChrTalk(
        0xF,
        "#5Pああ、やはり強い……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0657
    ChrTalk(
        0x20,
        (
            "#5Pあれだけ攻めたのに……\x01",
            "なんで仕留めきれないんだ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0658
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれが警察流の制圧術だな。\x02\x03",

            "これは上級カリキュラムになるけど\x01",
            "４人相手の組手なんかもやるんだ。\x02\x03",

            "#0003F警察官は自分だけじゃなくて\x01",
            "背後にいる人たちを\x01",
            "守らなくちゃいけない。\x02\x03",

            "負けるわけには行かない……\x01",
            "そんな訓練を積んできているのさ。\x02\x03",

            "#0000F……まあ、君たちはまず\x01",
            "自分の身を守る事かな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x20, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1E, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0xF)
    OP_64(0x20)
    OP_64(0x1E)
    OP_64(0x1F)
    Sleep(300)

    #C0659
    ChrTalk(
        0xF,
        (
            "#5P……警察も\x01",
            "伊達じゃないってわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0660
    ChrTalk(
        0xF,
        "#5P学ぶ事は多そうだな。\x02",
    )

    CloseMessageWindow()

    #C0661
    ChrTalk(
        0x1E,
        (
            "#5Pうん、今回は完敗だけど……\x01",
            "次に生かせそうな気がするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0662
    ChrTalk(
        0x104,
        (
            "#12P#0300Fへっ、こうして闘#2Rや#りあってみりゃあ\x01",
            "意外と素直な連中じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0663
    ChrTalk(
        0x102,
        (
            "#12P#0100F少し手ひどく\x01",
            "やってしまったけれど……\x01",
            "良かったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0664
    ChrTalk(
        0x103,
        (
            "#12P#0200Fあの様子なら\x01",
            "問題なさそうかと思……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(10, 10, -1, -1)
    SetChrName("青年の声")

    #A0665
    AnonymousTalk(
        0xFF,
        "#4P──クソが。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    def lambda_F405():

        label("loc_F405")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F405")

    QueueWorkItem2(0x0, 1, lambda_F405)

    def lambda_F417():

        label("loc_F417")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F417")

    QueueWorkItem2(0x1, 1, lambda_F417)

    def lambda_F429():

        label("loc_F429")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F429")

    QueueWorkItem2(0x2, 1, lambda_F429)

    def lambda_F43B():

        label("loc_F43B")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F43B")

    QueueWorkItem2(0x3, 1, lambda_F43B)

    def lambda_F44D():

        label("loc_F44D")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F44D")

    QueueWorkItem2(0xF, 1, lambda_F44D)

    def lambda_F45F():

        label("loc_F45F")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F45F")

    QueueWorkItem2(0x1F, 1, lambda_F45F)

    def lambda_F471():

        label("loc_F471")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F471")

    QueueWorkItem2(0x1E, 1, lambda_F471)

    def lambda_F483():

        label("loc_F483")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F483")

    QueueWorkItem2(0x20, 1, lambda_F483)

    def lambda_F495():

        label("loc_F495")

        TurnDirection(0xFE, 0x21, 500)
        Yield()
        Jump("loc_F495")

    QueueWorkItem2(0x1C, 1, lambda_F495)
    Sleep(800)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7517", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x205), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(500)
    OP_68(8710, 2000, -11680, 0)
    MoveCamera(136, 22, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x11, 0x80)
    OP_0D()

    #C0666
    ChrTalk(
        0x101,
        "#11P#0005F#Nあれ、サーベルバイパー？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0667
    ChrTalk(
        0x102,
        "#11P#0105F#Nどうしたのかしら……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    BeginChrThread(0x21, 0, 0, 52)
    BeginChrThread(0xD, 0, 0, 53)
    BeginChrThread(0xE, 0, 0, 54)
    BeginChrThread(0x11, 0, 0, 55)
    OP_68(3520, 2000, -6230, 4000)
    MoveCamera(152, 19, 0, 4000)

    #C0668
    ChrTalk(
        0xE,
        "#5Pヒャハ、何やってやがんだ～？\x02",
    )

    CloseMessageWindow()

    #C0669
    ChrTalk(
        0xD,
        (
            "#11Pハッ、サツのくせに\x01",
            "旧市街で喧嘩かよ！\x02",
        )
    )

    CloseMessageWindow()

    #C0670
    ChrTalk(
        0x11,
        (
            "#5P青坊主が負けたみたいだけど。\x01",
            "アハハハ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(10)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(12)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0671
    ChrTalk(
        0xF,
        "#12Pな、なんだと……？\x02",
    )

    CloseMessageWindow()

    #C0672
    ChrTalk(
        0x20,
        (
            "#6Pお、お前たちにだけは\x01",
            "言われたくないな……！\x02",
        )
    )

    CloseMessageWindow()

    #C0673
    ChrTalk(
        0x1E,
        "#6P何だったら……この場でやる？\x02",
    )

    CloseMessageWindow()

    #C0674
    ChrTalk(
        0x21,
        (
            "#11P待てや。\x01",
            "その前に正すことがある。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x21, 0)
    OP_68(1780, 700, -7220, 3500)
    MoveCamera(172, 22, 0, 3500)
    OP_95(0x21, 4910, -10, -7940, 2000, 0x0)
    OP_95(0x21, 2029, -10, -7760, 2000, 0x0)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1C, 0x1)
    OP_93(0xF, 0xE1, 0x1F4)

    #C0675
    ChrTalk(
        0x21,
        (
            "#5Pどういう事だコラ。\x01",
            "果し合いに呼び出しやがったのは\x01",
            "テメエの方だろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0676
    ChrTalk(
        0x21,
        (
            "#5P両チームトップ抜きの\x01",
            "４対４勝負……\x02",
        )
    )

    CloseMessageWindow()

    #C0677
    ChrTalk(
        0x21,
        (
            "#5Pデカい顔で抜かしておいて\x01",
            "サツとお遊戯か？\x02",
        )
    )

    CloseMessageWindow()

    #C0678
    ChrTalk(
        0x1C,
        "#11P……予定通り来たようだな。\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x12C)
    Sleep(400)

    #C0679
    ChrTalk(
        0x1C,
        (
            "#11Pではこれより、特務支援課と\x01",
            "サーベルバイパーの訓練試合を開始する！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x20, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x21, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(200)

    def lambda_F9D5():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_F9D5)

    def lambda_F9E2():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_F9E2)

    def lambda_F9EF():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_F9EF)

    def lambda_F9FC():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_F9FC)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x21, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    OP_63(0x11, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_FA99():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_FA99)

    def lambda_FAAE():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_FAAE)

    def lambda_FAC3():
        OP_9B(0x1, 0xFE, 0x0, 0x9C4, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_FAC3)
    Sleep(1500)
    OP_64(0x0)
    OP_64(0x1)
    OP_64(0x2)
    OP_64(0x3)
    OP_64(0x21)
    OP_64(0xD)
    OP_64(0xE)
    OP_64(0x11)
    Sleep(100)

    #C0680
    ChrTalk(
        0xD,
        "#5Pはァ……！？\x02",
    )

    CloseMessageWindow()

    #C0681
    ChrTalk(
        0x101,
        "#12P#0011Fちょ……えええ！？\x02",
    )

    CloseMessageWindow()

    #C0682
    ChrTalk(
        0x21,
        "#5Pど、どういう事だコラァ！！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x5A, 0x190)
    Sleep(400)

    #C0683
    ChrTalk(
        0x1C,
        (
            "#11Pお前たちもこの機会に\x01",
            "護身の術を学んでおく事だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0684
    ChrTalk(
        0x1C,
        (
            "#11Pマフィアに備えねばならんのは\x01",
            "お前たちも同様……\x02",
        )
    )

    CloseMessageWindow()

    #C0685
    ChrTalk(
        0x1C,
        (
            "#11Pそしてお前たちもまた\x01",
            "実戦で覚えるのが一番早かろう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    SetMessageWindowPos(130, 115, -1, -1)
    SetChrName("一同")

    #A0686
    AnonymousTalk(
        0xFF,
        "#40W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)

    #C0687
    ChrTalk(
        0x11,
        (
            "#6Pつまり……サツが俺たちに\x01",
            "稽古をつけようってことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0688
    ChrTalk(
        0xE,
        (
            "#5Pヒャハ、こいつの言ってること、\x01",
            "いつもイミ判んねェ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0689
    ChrTalk(
        0xE,
        "#5Pなんでサツが稽古つけるんだ～？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0xD, 500)
    TurnDirection(0x101, 0x21, 500)
    Sleep(300)

    #C0690
    ChrTalk(
        0x21,
        (
            "#12Pフン……うろたえんな。\x01",
            "能無し警官に\x01",
            "教わることなんざねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0691
    ChrTalk(
        0x21,
        "#12P稽古だと？　ふざけてんのか。\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x2BC)

    #C0692
    ChrTalk(
        0x21,
        (
            "#4S#12P……要は俺たちバイパーが\x01",
            "サツより強い所を\x01",
            "見せればいいんだろうがァッ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(8)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(5)
    OP_63(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1200)

    #C0693
    ChrTalk(
        0xD,
        (
            "#5Pハッ、やってやろうじゃねか！\x01",
            "サツを潰せばいいんだなァ？\x02",
        )
    )

    CloseMessageWindow()

    #C0694
    ChrTalk(
        0x11,
        (
            "#5Pシャア……\x01",
            "ボコボコにしてやんぜぇ！！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x21, 0x101, 400)
    BeginChrThread(0x21, 2, 0, 56)
    Sleep(10)
    BeginChrThread(0xD, 2, 0, 56)
    Sleep(8)
    BeginChrThread(0xE, 2, 0, 56)
    Sleep(12)
    BeginChrThread(0x11, 2, 0, 56)
    Fade(250)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()
    OP_68(750, 700, -5890, 3000)
    OP_93(0x1C, 0x0, 0x1F4)

    def lambda_FEFA():
        OP_9B(0x1, 0xFE, 0xB4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_FEFA)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    OP_6F(0x1)

    #C0695
    ChrTalk(
        0x101,
        (
            "#12P#0011F待ってくれ、\x01",
            "予定とまったく違うんだが……\x02\x03",

            "#0006Fって、ああもう……\x01",
            "誰も話を聞いてくれない……！\x02",
        )
    )

    CloseMessageWindow()

    #C0696
    ChrTalk(
        0x104,
        (
            "#12P#0301Fおいロイド、こっちは連戦だぜ。\x01",
            "……どうする。\x02",
        )
    )

    CloseMessageWindow()

    #C0697
    ChrTalk(
        0x101,
        "#12P#0006Fし、仕方がない……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0698
    ChrTalk(
        0x101,
        "#12P#0001Fエリィ、ティオ、大丈夫か？\x02",
    )

    CloseMessageWindow()

    #C0699
    ChrTalk(
        0x102,
        "#12P#0101Fええ、こっちは何とか。\x02",
    )

    CloseMessageWindow()

    #C0700
    ChrTalk(
        0x103,
        (
            "#12P#0201Fこうなったら\x01",
            "全力で行くしかありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0701
    ChrTalk(
        0x101,
        (
            "#12P#0001Fああ、さすがに\x01",
            "負けるわけには行かない……\x01",
            "全力で戦おう！\x02",
        )
    )

    CloseMessageWindow()

    #C0702
    ChrTalk(
        0x1C,
        (
            "#11Pそれでは特務支援課対\x01",
            "サーベルバイパー……\x02",
        )
    )

    CloseMessageWindow()

    #C0703
    ChrTalk(
        0x1C,
        "#11P#4S──戦闘開始！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x21, 0x2)
    EndChrThread(0xD, 0x2)
    EndChrThread(0xE, 0x2)
    EndChrThread(0x11, 0x2)
    StopBGM(0x3E8)
    Battle("BattleInfo_8D0", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_45_EDDE end

    def Function_46_101A7(): pass

    label("Function_46_101A7")

    OP_68(-360, 2000, -2190, 0)
    MoveCamera(154, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0x21, 3150, 0, -4000, 270)
    SetChrPos(0xD, 4080, 0, -4770, 270)
    SetChrPos(0xE, 4550, 0, -3310, 270)
    SetChrPos(0x11, 5260, 0, -4350, 270)
    SetChrPos(0xF, 4610, 0, -8510, 315)
    SetChrPos(0x1F, 5940, 0, -10170, 315)
    SetChrPos(0x20, 5790, 0, -8490, 315)
    SetChrPos(0x1E, 4910, 0, -10200, 315)
    SetChrChipByIndex(0x21, 0x2D)
    SetChrSubChip(0x21, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x3)
    OP_29(0x12, 0x1, 0x2)
    FadeToBright(1000, 0)
    OP_0D()

    #C0704
    ChrTalk(
        0x101,
        "#12P#0006Fふう……さすがに危なかったな。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0705
    ChrTalk(
        0xD,
        "#5Pハァ、畜生がァ……！\x02",
    )

    CloseMessageWindow()

    #C0706
    ChrTalk(
        0x21,
        "#5P野郎……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0707
    ChrTalk(
        0x21,
        (
            "#5Pクソが、４対４で負けただと……？\x01",
            "舐めてやがんのか！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)

    #C0708
    ChrTalk(
        0x21,
        (
            "#5P#4Sこれじゃあ青坊主どもと\x01",
            "一緒じゃねえか！\x02",
        )
    )

    CloseMessageWindow()

    #C0709
    ChrTalk(
        0xE,
        "#5Pヒャハ、ありえねェ～ッ！！\x02",
    )

    CloseMessageWindow()

    #C0710
    ChrTalk(
        0xE,
        (
            "#5Pオレらの方がつえーに\x01",
            "決まってんじゃん！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(15)
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(12)
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0711
    ChrTalk(
        0x102,
        (
            "#12P#0106Fそういう所で\x01",
            "突っかかるのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0712
    ChrTalk(
        0x104,
        "#12P#0300F長年の宿敵らしいからな……\x02",
    )

    CloseMessageWindow()
    Fade(500)
    OP_68(2040, 2000, -6710, 0)
    MoveCamera(98, 32, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(32390, 0)
    OP_0D()

    #C0713
    ChrTalk(
        0xF,
        "#11Pい、言わせておけば……\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    Sound(808, 0, 100, 0)
    OP_0D()

    #C0714
    ChrTalk(
        0xF,
        (
            "#11P僕たちテスタメンツが\x01",
            "バイパーなんかに\x01",
            "劣るわけが無いだろう！\x02",
        )
    )

    CloseMessageWindow()

    #C0715
    ChrTalk(
        0xF,
        (
            "#11Pその低脳をフルに使って\x01",
            "考えてみる事だな！\x02",
        )
    )

    CloseMessageWindow()

    #C0716
    ChrTalk(
        0x1F,
        (
            "#11Pそ、その通りだ。\x01",
            "オレたちが、同レベルなわけが、ない！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1067B():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1067B)
    Sleep(8)

    def lambda_1068B():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1068B)
    Sleep(2)

    def lambda_1069B():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_1069B)
    Sleep(5)

    def lambda_106AB():
        OP_93(0xFE, 0xAA, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_106AB)
    Sleep(200)

    #C0717
    ChrTalk(
        0x11,
        "#6Pんだとコラァ！！\x02",
    )

    CloseMessageWindow()

    #C0718
    ChrTalk(
        0xD,
        "#6P潰すぞテメエらァ！！\x02",
    )

    CloseMessageWindow()

    #C0719
    ChrTalk(
        0x101,
        "#12P#0005F#N待ってくれ、喧嘩はダメだぞ！\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0720
    ChrTalk(
        0x103,
        "#12P#0206F#N沸点の低い人たちばかりです。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0721
    ChrTalk(
        0x1C,
        (
            "#12Pふむ……\x01",
            "双方、まだまだ元気が\x01",
            "有り余っているようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0722
    ChrTalk(
        0x1C,
        "#12Pそれでは最終戦に入るとしよう。\x02",
    )

    CloseMessageWindow()
    OP_63(0xF, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x20, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1E, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1F, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x21, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x11, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_10892():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10892)

    def lambda_1089F():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_1089F)

    def lambda_108AC():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_108AC)

    def lambda_108B9():
        TurnDirection(0xFE, 0x1C, 500)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_108B9)

    def lambda_108C6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_108C6)

    def lambda_108D3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_108D3)

    def lambda_108E0():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_108E0)

    def lambda_108ED():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_108ED)

    def lambda_108FA():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_108FA)

    def lambda_10907():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10907)

    def lambda_10914():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_10914)

    def lambda_10921():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_10921)
    Sleep(300)

    #C0723
    ChrTalk(
        0x101,
        "#12P#0011F#Nへ……？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0724
    ChrTalk(
        0x11,
        "#5P最終戦……？\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x190)
    Sleep(200)

    #C0725
    ChrTalk(
        0x1C,
        "#12Pルールは簡単だ。\x02",
    )

    CloseMessageWindow()
    OP_68(660, 2000, -3670, 3000)
    MoveCamera(173, 31, 0, 3000)
    OP_6E(340, 3000)
    SetCameraDistance(33840, 3000)
    OP_6F(0x79)

    #C0726
    ChrTalk(
        0x1C,
        (
            "#11Pこの警察の護身術の達人を\x01",
            "どちらが先に仕留めるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0727
    ChrTalk(
        0x1C,
        (
            "#11Pそれで優劣を付ける、\x01",
            "というのはどうだ？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(10, 0, -1, -1)
    SetChrName("テスタメンツ")

    #A0728
    AnonymousTalk(
        0xFF,
        "#60W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)
    SetMessageWindowPos(20, 150, -1, -1)
    SetChrName("サーベルバイパー")

    #A0729
    AnonymousTalk(
        0xFF,
        "#60W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(100)

    #C0730
    ChrTalk(
        0x101,
        (
            "#12P#0011Fな、何を言い出すんだあんた……\x01",
            "いくらなんでも無茶だろ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x13B, 0x190)
    Sleep(300)

    #C0731
    ChrTalk(
        0x1C,
        "#5P……そうか？\x02",
    )

    CloseMessageWindow()

    #C0732
    ChrTalk(
        0x1C,
        (
            "#5P危機感があった方が\x01",
            "お前たちも本気になれるのではないか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10B75():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_10B75)

    def lambda_10B82():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_10B82)

    def lambda_10B8F():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_10B8F)

    def lambda_10B9C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_10B9C)
    Sleep(200)
    OP_82(0xC8, 0x0, 0xBB8, 0xC8)

    #C0733
    ChrTalk(
        0x21,
        "#6P#5Sいくぞコラァ！！\x02",
    )

    CloseMessageWindow()

    def lambda_10BD9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_10BD9)

    def lambda_10BE6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_10BE6)

    def lambda_10BF3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_10BF3)

    def lambda_10C00():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_10C00)
    SetChrChipByIndex(0xF, 0x33)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x32)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x32)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x32)
    SetChrSubChip(0x20, 0x0)
    BeginChrThread(0xF, 1, 0, 48)
    BeginChrThread(0x1F, 1, 0, 47)
    BeginChrThread(0x1E, 1, 0, 47)
    BeginChrThread(0x20, 1, 0, 47)

    #C0734
    ChrTalk(
        0xF,
        "#5S#5P連中に遅れをとるなっ！\x02",
    )

    CloseMessageWindow()

    #C0735
    ChrTalk(
        0xE,
        "#6P#4Sシャア！！\x02",
    )

    CloseMessageWindow()

    #C0736
    ChrTalk(
        0x20,
        "#5P#4Sいくぞッ……！！\x02",
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(640, 2000, -2860, 2000)
    MoveCamera(171, 26, 0, 2000)
    OP_6E(300, 2000)
    SetCameraDistance(34010, 2000)
    OP_63(0x0, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x1, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x2, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_63(0x3, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_6F(0x79)
    WaitChrThread(0xF, 1)
    WaitChrThread(0x1F, 1)
    WaitChrThread(0x1E, 1)
    WaitChrThread(0x20, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0737
    ChrTalk(
        0x101,
        (
            "#12P#0003Fだ、だめだ。\x01",
            "止められない……！\x02",
        )
    )

    CloseMessageWindow()

    #C0738
    ChrTalk(
        0x104,
        "#12P#0301Fやるしかねえみたいだな……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x190)
    Sleep(300)

    #C0739
    ChrTalk(
        0x1C,
        "#5P#4S──よし#500W、#20W最終戦開始！！\x02",
    )

    CloseMessageWindow()
    Battle("BattleInfo_914", 0x0, 0x0, 0x4, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Return()

    # Function_46_101A7 end

    def Function_47_10E1A(): pass

    label("Function_47_10E1A")

    OP_9B(0x0, 0xFE, 0x28, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x22)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_47_10E1A end

    def Function_48_10E32(): pass

    label("Function_48_10E32")

    OP_9B(0x0, 0xFE, 0x28, 0x7D0, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0x23)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_48_10E32 end

    def Function_49_10E4A(): pass

    label("Function_49_10E4A")

    OP_68(3950, 2000, -4170, 0)
    MoveCamera(127, 27, -1, 0)
    OP_6E(500, 0)
    SetCameraDistance(18720, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3020, 0, -5730, 270)
    SetChrPos(0x1F, 3960, 0, -7270, 270)
    SetChrPos(0x20, 4520, 0, -5070, 270)
    SetChrPos(0x1E, 5330, 0, -6480, 270)
    SetChrPos(0x21, 3310, 0, -2870, 270)
    SetChrPos(0xD, 3950, 0, -4170, 270)
    SetChrPos(0xE, 4270, 50, -1940, 270)
    SetChrPos(0x11, 5080, 0, -3400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x2B)
    SetChrSubChip(0xF, 0x3)
    SetChrChipByIndex(0x1F, 0x2A)
    SetChrSubChip(0x1F, 0x3)
    SetChrChipByIndex(0x1E, 0x2A)
    SetChrSubChip(0x1E, 0x3)
    SetChrChipByIndex(0x20, 0x2A)
    SetChrSubChip(0x20, 0x3)
    SetChrChipByIndex(0x21, 0x2D)
    SetChrSubChip(0x21, 0x2)
    SetChrChipByIndex(0xD, 0x2D)
    SetChrSubChip(0xD, 0x2)
    SetChrChipByIndex(0xE, 0x2C)
    SetChrSubChip(0xE, 0x3)
    SetChrChipByIndex(0x11, 0x2C)
    SetChrSubChip(0x11, 0x3)
    SetCameraDistance(23720, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x10)
    Fade(500)
    OP_68(-500, 2000, -2270, 0)
    MoveCamera(150, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(34010, 0)
    OP_0D()

    #C0740
    ChrTalk(
        0x101,
        "#12P#0006Fハア、ハア……\x02",
    )

    CloseMessageWindow()

    #C0741
    ChrTalk(
        0x104,
        "#12P#0301F……終わったか。\x02",
    )

    CloseMessageWindow()

    #C0742
    ChrTalk(
        0x103,
        "#12P#0200F何とか勝てましたけど……\x02",
    )

    CloseMessageWindow()

    #C0743
    ChrTalk(
        0x102,
        "#12P#0103F無茶苦茶ね……\x02",
    )

    CloseMessageWindow()
    OP_A6(0xF, 0xC8, 0x0, 0x3, 0xBB8)

    #C0744
    ChrTalk(
        0xF,
        (
            "#5Pりょ、両チーム相手に\x01",
            "凌ぐなんて……\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0xC8, 0x0, 0x3, 0xBB8)

    #C0745
    ChrTalk(
        0x21,
        (
            "#5Pぐは……\x01",
            "こんなの認めねえぞ……\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(200)
    SetChrSubChip(0x21, 0x1)
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)
    Sleep(500)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    Sound(804, 0, 100, 0)
    OP_95(0x1C, 1780, 0, -3880, 1500, 0x0)
    TurnDirection(0x1C, 0x21, 500)
    TurnDirection(0x21, 0x1C, 500)
    Sleep(300)

    #C0746
    ChrTalk(
        0x1C,
        (
            "#11Pこれで分かったか？\x01",
            "お前たちの戦闘は\x01",
            "力に頼る単純なもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0747
    ChrTalk(
        0x1C,
        (
            "#11Pいまだ自らの身を守る術すら\x01",
            "持ち合わせていないという事を。\x02",
        )
    )

    CloseMessageWindow()

    #C0748
    ChrTalk(
        0x1C,
        (
            "#11Pつまりは、まだまだ\x01",
            "未熟という事だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)

    #C0749
    ChrTalk(
        0x21,
        "#5Pぐっ……！？\x02",
    )

    CloseMessageWindow()
    Fade(200)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(200)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    OP_93(0xF, 0x13B, 0x0)
    Sleep(500)
    Fade(200)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    OP_93(0xE, 0xE1, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    OP_93(0x1F, 0x13B, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(250)
    Fade(200)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    OP_93(0x1E, 0x13B, 0x0)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    OP_93(0x20, 0x13B, 0x0)
    Sleep(500)

    #C0750
    ChrTalk(
        0x11,
        (
            "#5Pよ、よく分かんねえけど\x01",
            "イキナリ説教された……\x02",
        )
    )

    CloseMessageWindow()

    #C0751
    ChrTalk(
        0xE,
        "#6Pイミ判んねェ～……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0752
    ChrTalk(
        0x101,
        (
            "#12P#0004Fまあ、君たちは十分強いよ。\x01",
            "一般人レベルなら文句ないと思う。\x02\x03",

            "#0000F良かったら護身術くらい\x01",
            "教えてやるけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x1F4)
    Sleep(300)

    #C0753
    ChrTalk(
        0x21,
        (
            "#5P……クソが。\x01",
            "サツに教わることなんざねえんだよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x5A, 0x190)
    Sleep(300)

    #C0754
    ChrTalk(
        0x21,
        "#5Pお前ら、引き上げるぞ！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("バイパーたち")

    #A0755
    AnonymousTalk(
        0xFF,
        "#4S う、うーっす！ \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_1147A():

        label("loc_1147A")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1147A")

    QueueWorkItem2(0x0, 1, lambda_1147A)

    def lambda_1148C():

        label("loc_1148C")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1148C")

    QueueWorkItem2(0x1, 1, lambda_1148C)

    def lambda_1149E():

        label("loc_1149E")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1149E")

    QueueWorkItem2(0x2, 1, lambda_1149E)

    def lambda_114B0():

        label("loc_114B0")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_114B0")

    QueueWorkItem2(0x3, 1, lambda_114B0)

    def lambda_114C2():

        label("loc_114C2")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_114C2")

    QueueWorkItem2(0xF, 1, lambda_114C2)

    def lambda_114D4():

        label("loc_114D4")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_114D4")

    QueueWorkItem2(0x1F, 1, lambda_114D4)

    def lambda_114E6():

        label("loc_114E6")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_114E6")

    QueueWorkItem2(0x1E, 1, lambda_114E6)

    def lambda_114F8():

        label("loc_114F8")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_114F8")

    QueueWorkItem2(0x20, 1, lambda_114F8)

    def lambda_1150A():

        label("loc_1150A")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_1150A")

    QueueWorkItem2(0x1C, 1, lambda_1150A)
    BeginChrThread(0x21, 1, 0, 57)
    Sleep(1200)
    BeginChrThread(0xD, 1, 0, 58)
    Sleep(800)
    BeginChrThread(0x11, 1, 0, 60)
    Sleep(400)
    BeginChrThread(0xE, 1, 0, 59)

    #C0756
    ChrTalk(
        0xE,
        (
            "#6Pあの大男、いっつも\x01",
            "イミ判かんねえぞ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0757
    ChrTalk(
        0xD,
        "#4Pちっ、やってられるかァ！\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_49_10E4A end

    def Function_50_1158A(): pass

    label("Function_50_1158A")

    OP_68(810, 1500, -4230, 0)
    MoveCamera(150, 27, 0, 0)
    OP_6E(300, 0)
    SetCameraDistance(34010, 0)
    SetChrPos(0x101, -1400, 0, -4000, 90)
    SetChrPos(0x102, -2500, 0, -4700, 90)
    SetChrPos(0x103, -2050, 0, -2950, 90)
    SetChrPos(0x104, -3160, 0, -3320, 90)
    SetChrPos(0x1C, 990, 0, -7830, 0)
    SetChrPos(0xF, 3020, 0, -5730, 270)
    SetChrPos(0x1F, 3960, 0, -7270, 270)
    SetChrPos(0x20, 4520, 0, -5070, 270)
    SetChrPos(0x1E, 5330, 0, -6480, 270)
    SetChrPos(0x21, 3310, 0, -2870, 270)
    SetChrPos(0xD, 3950, 0, -4170, 270)
    SetChrPos(0xE, 4270, 50, -1940, 270)
    SetChrPos(0x11, 5080, 0, -3400, 270)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x27)
    SetChrSubChip(0x102, 0x3)
    SetChrChipByIndex(0x103, 0x28)
    SetChrSubChip(0x103, 0x3)
    SetChrChipByIndex(0x104, 0x29)
    SetChrSubChip(0x104, 0x3)
    SetChrChipByIndex(0x1C, 0x2F)
    SetChrSubChip(0x1C, 0x0)
    SetChrChipByIndex(0xF, 0x23)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x22)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x22)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x22)
    SetChrSubChip(0x20, 0x0)
    SetChrChipByIndex(0x21, 0x25)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x25)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x24)
    SetChrSubChip(0x11, 0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0758
    ChrTalk(
        0x101,
        "#12P#0010Fハア、ハア、ハア……\x02",
    )

    CloseMessageWindow()

    #C0759
    ChrTalk(
        0x104,
        "#12P#0310F#Nくそっ……しくじったか。\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0760
    ChrTalk(
        0x21,
        "#6Pはっ……\x02",
    )

    CloseMessageWindow()
    OP_82(0xC8, 0x0, 0xBB8, 0x2BC)

    #C0761
    ChrTalk(
        0xE,
        (
            "#6P#4Sヒャハハ、ざまあ見ろォ！\x01",
            "倒してやったぜェ～！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x21, 0x5)
    SetChrSubChip(0x21, 0x0)
    SetChrChipByIndex(0xD, 0x5)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x6)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0x11, 0x6)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0xF, 0x7)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x1F, 0x2E)
    SetChrSubChip(0x1F, 0x0)
    SetChrChipByIndex(0x1E, 0x2E)
    SetChrSubChip(0x1E, 0x0)
    SetChrChipByIndex(0x20, 0x2E)
    SetChrSubChip(0x20, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_63(0x21, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xD, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0xE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    OP_63(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(800)
    OP_93(0xF, 0x0, 0x190)
    Sleep(400)

    #C0762
    ChrTalk(
        0xF,
        (
            "#11P待ちたまえ！\x01",
            "あれは僕の一撃が効いたからだ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11892():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_11892)
    Sleep(10)

    def lambda_118A2():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_118A2)
    Sleep(5)

    def lambda_118B2():
        OP_93(0xFE, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_118B2)
    Sleep(180)

    def lambda_118C2():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_118C2)
    Sleep(14)

    def lambda_118D2():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_118D2)
    Sleep(8)

    def lambda_118E2():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_118E2)
    Sleep(12)

    def lambda_118F2():
        OP_93(0xFE, 0xB4, 0x190)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_118F2)

    #C0763
    ChrTalk(
        0x1F,
        (
            "#11Pそ、そうだ。\x01",
            "俺たちも、加勢していた。\x02",
        )
    )

    CloseMessageWindow()

    #C0764
    ChrTalk(
        0x1F,
        (
            "#11Pお前達の実力なんかじゃ、\x01",
            "全然、ない！\x02",
        )
    )

    CloseMessageWindow()

    #C0765
    ChrTalk(
        0x11,
        (
            "#6Pなんだと！？\x01",
            "そ、そりゃあ……\x01",
            "確かに手は借りたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0766
    ChrTalk(
        0x1C,
        "#11P──それでは勝利とは言えんな。\x02",
    )

    CloseMessageWindow()

    def lambda_119C2():

        label("loc_119C2")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_119C2")

    QueueWorkItem2(0x101, 1, lambda_119C2)

    def lambda_119D4():

        label("loc_119D4")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_119D4")

    QueueWorkItem2(0xF, 1, lambda_119D4)

    def lambda_119E6():

        label("loc_119E6")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_119E6")

    QueueWorkItem2(0x1F, 1, lambda_119E6)

    def lambda_119F8():

        label("loc_119F8")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_119F8")

    QueueWorkItem2(0x1E, 1, lambda_119F8)

    def lambda_11A0A():

        label("loc_11A0A")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_11A0A")

    QueueWorkItem2(0x20, 1, lambda_11A0A)

    def lambda_11A1C():

        label("loc_11A1C")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_11A1C")

    QueueWorkItem2(0x21, 1, lambda_11A1C)

    def lambda_11A2E():

        label("loc_11A2E")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_11A2E")

    QueueWorkItem2(0xD, 1, lambda_11A2E)

    def lambda_11A40():

        label("loc_11A40")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_11A40")

    QueueWorkItem2(0xE, 1, lambda_11A40)

    def lambda_11A52():

        label("loc_11A52")

        TurnDirection(0xFE, 0x1C, 300)
        Yield()
        Jump("loc_11A52")

    QueueWorkItem2(0x11, 1, lambda_11A52)
    OP_95(0x1C, 1780, 0, -3880, 1500, 0x0)
    TurnDirection(0x1C, 0x21, 500)
    TurnDirection(0x21, 0x1C, 500)
    Sleep(300)
    EndChrThread(0x101, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0x11, 0x1)

    #C0767
    ChrTalk(
        0x1C,
        (
            "#11Pそもそも特務支援課は\x01",
            "３度の連戦……\x01",
            "ここまで戦い抜いたのは見事だろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0768
    ChrTalk(
        0x1C,
        "#11Pお前たちに同じ真似ができるか？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("サーベルバイパー")

    #A0769
    AnonymousTalk(
        0xFF,
        "#30W……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(200)

    #C0770
    ChrTalk(
        0x1C,
        (
            "#11P分かったか？\x01",
            "お前たちの戦闘は\x01",
            "力に頼る単純なもの……\x02",
        )
    )

    CloseMessageWindow()

    #C0771
    ChrTalk(
        0x1C,
        (
            "#11Pいまだ自らの身を守る術すら\x01",
            "持ち合わせていないという事を。\x02",
        )
    )

    CloseMessageWindow()

    #C0772
    ChrTalk(
        0x1C,
        (
            "#11Pつまりは、まだまだ\x01",
            "未熟という事だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_A6(0x21, 0x0, 0x32, 0x1F4, 0xBB8)

    #C0773
    ChrTalk(
        0x21,
        "#5Pぐっ……！？\x02",
    )

    CloseMessageWindow()

    #C0774
    ChrTalk(
        0x11,
        (
            "#5Pよ、よく分かんねえけど\x01",
            "すげー説教された……\x02",
        )
    )

    CloseMessageWindow()

    #C0775
    ChrTalk(
        0xE,
        "#6Pイミ判んねェ～……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0776
    ChrTalk(
        0x101,
        (
            "#12P#0004Fまあ、君たちは十分強いよ。\x01",
            "一般人レベルなら文句ないと思う。\x02\x03",

            "#12P#0000F最後は負けたけど、\x01",
            "良かったら護身術くらい\x01",
            "教えてあげようか……？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x10E, 0x1F4)
    Sleep(300)

    #C0777
    ChrTalk(
        0x21,
        (
            "#5P……クソが。\x01",
            "サツに教わることなんざねえんだよ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x21, 0x5A, 0x190)
    Sleep(300)

    #C0778
    ChrTalk(
        0x21,
        "#5Pお前ら、引き上げるぞ！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(20, 40, -1, -1)
    SetChrName("バイパーたち")

    #A0779
    AnonymousTalk(
        0xFF,
        "#4S うーっす！ \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_11E04():

        label("loc_11E04")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E04")

    QueueWorkItem2(0x0, 1, lambda_11E04)

    def lambda_11E16():

        label("loc_11E16")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E16")

    QueueWorkItem2(0x1, 1, lambda_11E16)

    def lambda_11E28():

        label("loc_11E28")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E28")

    QueueWorkItem2(0x2, 1, lambda_11E28)

    def lambda_11E3A():

        label("loc_11E3A")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E3A")

    QueueWorkItem2(0x3, 1, lambda_11E3A)

    def lambda_11E4C():

        label("loc_11E4C")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E4C")

    QueueWorkItem2(0xF, 1, lambda_11E4C)

    def lambda_11E5E():

        label("loc_11E5E")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E5E")

    QueueWorkItem2(0x1F, 1, lambda_11E5E)

    def lambda_11E70():

        label("loc_11E70")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E70")

    QueueWorkItem2(0x1E, 1, lambda_11E70)

    def lambda_11E82():

        label("loc_11E82")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E82")

    QueueWorkItem2(0x20, 1, lambda_11E82)

    def lambda_11E94():

        label("loc_11E94")

        TurnDirection(0xFE, 0xD, 300)
        Yield()
        Jump("loc_11E94")

    QueueWorkItem2(0x1C, 1, lambda_11E94)
    BeginChrThread(0x21, 1, 0, 57)
    Sleep(1200)
    BeginChrThread(0xD, 1, 0, 58)
    Sleep(800)
    BeginChrThread(0x11, 1, 0, 60)
    Sleep(400)
    BeginChrThread(0xE, 1, 0, 59)

    #C0780
    ChrTalk(
        0xE,
        (
            "#6Pあの大男、いっつも\x01",
            "イミ判かんねえぞ～？\x02",
        )
    )

    CloseMessageWindow()

    #C0781
    ChrTalk(
        0xD,
        "#12Pちっ、やってられるかァ！\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_50_1158A end

    def Function_51_11F15(): pass

    label("Function_51_11F15")

    Sleep(2500)
    WaitChrThread(0xE, 1)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x11, 0x80)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x1E, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x1C, 0x1)

    #C0782
    ChrTalk(
        0xF,
        (
            "#11Pフン……相変わらず\x01",
            "低脳な連中だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0783
    ChrTalk(
        0x1F,
        (
            "#12Pあ、あいつらが護身術なんて、\x01",
            "一生かかっても、無理だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0784
    ChrTalk(
        0x20,
        "#5Pだね、僕もそう思う。\x02",
    )

    CloseMessageWindow()

    #C0785
    ChrTalk(
        0x1E,
        "#6P折角いい経験をしたのにね。\x02",
    )

    CloseMessageWindow()

    def lambda_12005():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_12005)

    def lambda_12012():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_12012)
    Sleep(20)

    def lambda_12022():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_12022)
    Sleep(10)

    def lambda_12032():
        OP_93(0xFE, 0x5A, 0x190)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_12032)
    Sleep(100)

    def lambda_12042():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_12042)
    Sleep(20)

    def lambda_12052():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12052)

    def lambda_1205F():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1205F)
    Sleep(18)

    def lambda_1206F():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_1206F)

    def lambda_1207C():
        OP_93(0xFE, 0x10E, 0x190)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1207C)
    Sleep(300)

    #C0786
    ChrTalk(
        0x101,
        (
            "#12P#0003Fまあ、君たちだけでも\x01",
            "判ってくれたみたいで良かった。\x01",
            "付き合った甲斐があったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0787
    ChrTalk(
        0x102,
        "#12P#0103Fそうね、とても疲れたけれど。\x02",
    )

    CloseMessageWindow()

    #C0788
    ChrTalk(
        0x1C,
        (
            "#5Pでは、我らも\x01",
            "引き上げるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0789
    ChrTalk(
        0x1C,
        (
            "#5P……特務支援課、休息が必要ならば\x01",
            "後ほどバーに顔を出すとよい。\x02",
        )
    )

    CloseMessageWindow()

    #C0790
    ChrTalk(
        0x1C,
        (
            "#5Pフ……お前たちも\x01",
            "いい訓練になったろう？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x87, 0x190)
    Sleep(400)
    OP_63(0x0, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x1, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x2, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x3, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)

    #C0791
    ChrTalk(
        0x104,
        "#12P#0305Fへ……！？\x02",
    )

    CloseMessageWindow()

    #C0792
    ChrTalk(
        0x101,
        "#12P#0005F……………………？\x02",
    )

    CloseMessageWindow()

    def lambda_12247():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_12247)
    Sleep(10)

    def lambda_12257():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_12257)

    def lambda_12264():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_12264)
    Sleep(12)

    def lambda_12274():
        OP_93(0xFE, 0x13B, 0x190)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_12274)
    Sleep(400)

    #C0793
    ChrTalk(
        0x1C,
        "#5P#4S──戦闘終了、撤収！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 10, -1, -1)
    SetChrName("テスタメンツたち")

    #A0794
    AnonymousTalk(
        0xFF,
        "#5S  ヤーッ！  \x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()

    def lambda_122E0():

        label("loc_122E0")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_122E0")

    QueueWorkItem2(0x0, 1, lambda_122E0)

    def lambda_122F2():

        label("loc_122F2")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_122F2")

    QueueWorkItem2(0x1, 1, lambda_122F2)

    def lambda_12304():

        label("loc_12304")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_12304")

    QueueWorkItem2(0x2, 1, lambda_12304)

    def lambda_12316():

        label("loc_12316")

        TurnDirection(0xFE, 0xF, 300)
        Yield()
        Jump("loc_12316")

    QueueWorkItem2(0x3, 1, lambda_12316)
    OP_68(-4030, 2000, -6480, 5500)
    MoveCamera(228, 29, -1, 5500)
    OP_6E(500, 5500)
    SetCameraDistance(21190, 5500)
    BeginChrThread(0x1C, 1, 0, 61)
    Sleep(1100)
    BeginChrThread(0xF, 1, 0, 61)
    Sleep(700)
    BeginChrThread(0x1F, 1, 0, 61)
    Sleep(400)
    BeginChrThread(0x20, 1, 0, 61)
    Sleep(700)
    BeginChrThread(0x1E, 1, 0, 61)
    Sleep(3800)
    StopBGM(0x1388)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(3000)
    EndChrThread(0x0, 0x1)
    EndChrThread(0x1, 0x1)
    EndChrThread(0x2, 0x1)
    EndChrThread(0x3, 0x1)
    Fade(800)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x20, 0x80)
    OP_68(-1140, 2000, -2670, 0)
    MoveCamera(228, 29, -1, 0)
    OP_6E(520, 0)
    SetCameraDistance(16580, 0)
    OP_0D()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7101", 0)

    #C0795
    ChrTalk(
        0x101,
        (
            "#6P#0005Fあのアッバスってやつ……\x01",
            "初めからこのつもりだったのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0796
    ChrTalk(
        0x102,
        (
            "#5P#0106F結局両チームとも\x01",
            "稽古に巻き込んじゃったのよね。\x02\x03",

            "#0100F確かに予め\x01",
            "考えがあったみたいだわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0797
    ChrTalk(
        0x104,
        (
            "#11P#0306Fまんまと踊らされたってわけか。\x01",
            "……食えねえやつだぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0798
    ChrTalk(
        0x103,
        (
            "#12P#0206Fですね……大変疲れました。\x02\x03",

            "#0200Fでも、あのお説教のお陰で\x01",
            "不良さんたちも\x01",
            "大人しくなってくれそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0799
    ChrTalk(
        0x101,
        (
            "#6P#0000Fそうだな、当初の目的も\x01",
            "果たせたわけだし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1259D():
        TurnDirection(0xFE, 0x104, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1259D)

    def lambda_125AA():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_125AA)

    def lambda_125B7():
        TurnDirection(0xFE, 0x103, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_125B7)

    def lambda_125C4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_125C4)
    Sleep(400)

    #C0800
    ChrTalk(
        0x101,
        (
            "#6P#0000Fよし、俺たちもそろそろ\x01",
            "引き上げるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0801
    ChrTalk(
        0x102,
        "#5P#0100Fええ、そうしましょう。\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_51_11F15 end

    def Function_52_1262F(): pass

    label("Function_52_1262F")

    OP_95(0x21, 5880, -10, -9390, 2000, 0x0)
    Return()

    # Function_52_1262F end

    def Function_53_12644(): pass

    label("Function_53_12644")

    OP_95(0xD, 6450, 0, -11270, 2000, 0x0)
    Return()

    # Function_53_12644 end

    def Function_54_12659(): pass

    label("Function_54_12659")

    OP_95(0xE, 7550, 0, -9860, 2000, 0x0)
    Return()

    # Function_54_12659 end

    def Function_55_1266E(): pass

    label("Function_55_1266E")

    OP_95(0x11, 7860, 0, -11350, 2000, 0x0)
    Return()

    # Function_55_1266E end

    def Function_56_12683(): pass

    label("Function_56_12683")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_126A8")
    OP_63(0xFE, 0xC8, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_56_12683")

    label("loc_126A8")

    Return()

    # Function_56_12683 end

    def Function_57_126A9(): pass

    label("Function_57_126A9")

    OP_95(0xFE, 4400, 0, -3520, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_57_126A9 end

    def Function_58_126FA(): pass

    label("Function_58_126FA")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_58_126FA end

    def Function_59_1274B(): pass

    label("Function_59_1274B")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_59_1274B end

    def Function_60_1279C(): pass

    label("Function_60_1279C")

    OP_95(0xFE, 5830, 0, -5010, 2000, 0x0)
    OP_95(0xFE, 7480, 0, -8260, 2000, 0x0)
    OP_95(0xFE, 9280, -10, -12350, 2000, 0x0)
    OP_95(0xFE, 17170, -2310, -21070, 2000, 0x0)
    Return()

    # Function_60_1279C end

    def Function_61_127ED(): pass

    label("Function_61_127ED")

    OP_95(0xFE, 390, 0, -7500, 2000, 0x0)
    OP_95(0xFE, -5110, 0, -8500, 2000, 0x0)
    OP_95(0xFE, -10460, 0, -11450, 2000, 0x0)
    OP_95(0xFE, -15990, 0, -11600, 2000, 0x0)
    Return()

    # Function_61_127ED end

    SaveToFile()

Try(main)
