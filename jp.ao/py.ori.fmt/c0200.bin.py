from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0200.bin",                # FileName
        "c0200",                    # MapName
        "c0200",                    # Location
        0x000A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c0200", "c1000_1", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 33140, -4000, -18370, 0, 0, 1, 10, 0, 11, 0, 12],
    )

    BuildStringList((
        "c0200",                  # 0
        "リュウ",                 # 1
        "アンリ",                 # 2
        "ポンス",                 # 3
        "ブリック",               # 4
        "モモ",                   # 5
        "エルサ",                 # 6
        "ルーヴィック老人",       # 7
        "カテリーナ",             # 8
        "チルル",                 # 9
        "オリガ夫人",             # 10
        "市民",                   # 11
        "警備隊員",               # 12
        "セルゲイ課長",           # 13
        "リース",                 # 14
        "ツァイト",               # 15
        "キーア",                 # 16
        "白ハヤブサ",             # 17
        "特務支援課導力車",       # 18
        "SE制御",                 # 19
        "bc0200",                 # 20
        "中央広場",               # 21
        "西通り",                 # 22
        "行政区",                 # 23
        "住宅街",                 # 24
        "歓楽街",                 # 25
        "東通り",                 # 26
        "旧市街",                 # 27
        "港湾区",                 # 28
        "ＩＢＣ",                 # 29
        "駅前通り",               # 30
        "裏通り",                 # 31
        "ウルスラ間道",           # 32
        "東クロスベル街道",       # 33
        "西クロスベル街道",       # 34
        "マインツ山道",           # 35
        "オルキスタワー",         # 36
    ))

    ATBonus("ATBonus_6D4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_B5FC", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_724", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_738", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_73C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_784", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_788", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_78C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_790", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_794", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_798", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_79C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_7A0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_704", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_708", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_70C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_710", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_714", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_718", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_7A4", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc0200", "Sepith_B5FC", 60, 25, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_724", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_704", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_724", "MonsterBattlePostion_784", "ed7450", "ed7453", "ATBonus_6D4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch20600.itc",                   # 00
        "chr/ch22200.itc",                   # 01
        "chr/ch20200.itc",                   # 02
        "chr/ch20402.itc",                   # 03
        "chr/ch20700.itc",                   # 04
        "chr/ch10400.itc",                   # 05
        "chr/ch21600.itc",                   # 06
        "chr/ch24500.itc",                   # 07
        "chr/ch20500.itc",                   # 08
        "chr/ch20100.itc",                   # 09
        "chr/ch49000.itc",                   # 0A
        "chr/ch48500.itc",                   # 0B
        "chr/ch31300.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
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

    DeclNpc(-1000,   0,       610,     90,   261,  0x0, 0,   0,   0,   0,   1,   0,   14,  255,  0)
    DeclNpc(449,     0,       610,     90,   261,  0x0, 0,   1,   0,   0,   1,   0,   18,  255,  0)
    DeclNpc(-15119,  0,       5829,    270,  261,  0x0, 0,   2,   0,   0,   2,   0,   19,  255,  0)
    DeclNpc(6570,    -150,    5119,    90,   325,  0x0, 0,   3,   0,   255, 255, 0,   20,  255,  0)
    DeclNpc(5360,    3000,    17690,   0,    261,  0x0, 0,   4,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(9159,    3000,    17489,   225,  261,  0x0, 0,   5,   0,   0,   0,   0,   22,  255,  0)
    DeclNpc(-6690,   0,       4460,    0,    389,  0x0, 0,   6,   0,   0,   0,   0,   23,  255,  0)
    DeclNpc(10800,   0,       -3480,   270,  389,  0x0, 0,   7,   0,   0,   0,   0,   24,  255,  0)
    DeclNpc(10729,   0,       -4780,   270,  389,  0x0, 0,   8,   0,   0,   0,   0,   25,  255,  0)
    DeclNpc(-5280,   0,       4489,    270,  389,  0x0, 0,   9,   0,   0,   0,   0,   26,  255,  0)
    DeclNpc(-850,    3000,    27399,   180,  385,  0x0, 0,   10,  0,   0,   10,  0,   27,  255,  0)
    DeclNpc(1360,    -300,    7380,    180,  385,  0x0, 0,   12,  0,   0,   0,   0,   28,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(250,     3470,    0,       0x10100E1,    "BattleInfo_7A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4800,    -9360,   0,       0x101013B,    "BattleInfo_7A4", 0,   16,  0xFFFF, 0,  1)

    DeclActor(33490,   -4000,   -16740,  1500,    33490,   -2000,   -16740,  0x007C, 0,  32, 0x0000)
    DeclActor(33490,   -4000,   -16740,  1500,    33490,   -2000,   -16740,  0x007C, 0,  32, 0x0000)
    DeclActor(37220,   -4000,   -19150,  1000,    37220,   -3000,   -19150,  0x007C, 0,  29, 0x0000)
    DeclActor(18220,   -210,    -11950,  1000,    18220,   1000,    -11950,  0x007C, 0,  29, 0x0000)
    DeclActor(14500,   -6500,   -13500,  1200,    14500,   -5500,   -13500,  0x007C, 0,  13, 0x0000)
    DeclActor(19330,   3000,    15550,   1200,    19330,   4500,    15550,   0x007C, 0,  30, 0x0000)
    DeclActor(40950,   -4000,   -19220,  1200,    40950,   -2500,   -19220,  0x007C, 0,  52, 0x0000)

    PlaceName(70.75, 0.0, -7.0, 0x0000, 0x0000, "中央広場")
    PlaceName(5.0, 0.0, -2.5, 0x0000, 0x0000, "西通り")
    PlaceName(97.75, 0.0, 82.0, 0x0000, 0x0000, "行政区")
    PlaceName(-56.0, 0.0, 72.0, 0x0000, 0x0000, "住宅街")
    PlaceName(17.0, 0.0, 64.0, 0x0000, 0x0000, "歓楽街")
    PlaceName(152.0, 0.0, -30.0, 0x0000, 0x0000, "東通り")
    PlaceName(187.5, 0.0, -85.0, 0x0000, 0x0000, "旧市街")
    PlaceName(180.0, 0.0, 36.0, 0x0000, 0x0000, "港湾区")
    PlaceName(154.0, 0.0, 130.0, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(82.0, 0.0, -76.0, 0x0000, 0x0000, "駅前通り")
    PlaceName(35.0, 0.0, 28.0, 0x0000, 0x0000, "裏通り")
    PlaceName(79.0, 0.0, -107.0, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(206.0, 0.0, -16.0, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-46.0, 0.0, -4.0, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-40.0, 0.0, 96.0, 0x0000, 0x0000, "マインツ山道")
    PlaceName(91.0, 0.0, 213.0, 0x0000, 0x0000, "オルキスタワー")
    PlaceName(48.75, 0.0, -21.0, 0x0000, 0x0051, "")
    PlaceName(102.5, 0.0, 5.0, 0x0000, 0x0054, "")
    PlaceName(73.25, 0.0, -29.0, 0x0000, 0x0057, "")
    PlaceName(48.0, 0.0, 8.0, 0x0000, 0x0053, "")
    PlaceName(68.5, 0.0, 32.0, 0x0000, 0x0053, "")
    PlaceName(17.75, 0.0, 3.0, 0x0000, 0x0053, "")
    PlaceName(8.0, 0.0, 24.0, 0x0000, 0x0053, "")
    PlaceName(32.0, 0.0, 56.0, 0x0000, 0x0052, "")
    PlaceName(36.75, 0.0, 43.0, 0x0000, 0x0053, "")
    PlaceName(45.5, 0.0, 34.5, 0x0000, 0x0053, "")
    PlaceName(74.0, 0.0, 105.5, 0x0000, 0x0051, "")
    PlaceName(186.0, 0.0, -30.0, 0x0000, 0x0052, "")
    PlaceName(169.0, 0.0, -120.5, 0x0000, 0x0053, "")
    PlaceName(156.0, 0.0, -102.0, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_92C",          # 00, 0
        "Function_1_9DC",          # 01, 1
        "Function_2_A3D",          # 02, 2
        "Function_3_A9E",          # 03, 3
        "Function_4_AC9",          # 04, 4
        "Function_5_B9D",          # 05, 5
        "Function_6_C71",          # 06, 6
        "Function_7_D45",          # 07, 7
        "Function_8_E19",          # 08, 8
        "Function_9_EED",          # 09, 9
        "Function_10_F18",         # 0A, 10
        "Function_11_F79",         # 0B, 11
        "Function_12_1B16",        # 0C, 12
        "Function_13_20E6",        # 0D, 13
        "Function_14_2237",        # 0E, 14
        "Function_15_2A49",        # 0F, 15
        "Function_16_2B08",        # 10, 16
        "Function_17_2BF6",        # 11, 17
        "Function_18_2D43",        # 12, 18
        "Function_19_3476",        # 13, 19
        "Function_20_4387",        # 14, 20
        "Function_21_4CB8",        # 15, 21
        "Function_22_4FBC",        # 16, 22
        "Function_23_5595",        # 17, 23
        "Function_24_5C47",        # 18, 24
        "Function_25_5C98",        # 19, 25
        "Function_26_5CE0",        # 1A, 26
        "Function_27_5D60",        # 1B, 27
        "Function_28_5E68",        # 1C, 28
        "Function_29_5FFB",        # 1D, 29
        "Function_30_607E",        # 1E, 30
        "Function_31_60D6",        # 1F, 31
        "Function_32_6477",        # 20, 32
        "Function_33_6A81",        # 21, 33
        "Function_34_6B42",        # 22, 34
        "Function_35_6BD6",        # 23, 35
        "Function_36_6C81",        # 24, 36
        "Function_37_71F8",        # 25, 37
        "Function_38_88C5",        # 26, 38
        "Function_39_891C",        # 27, 39
        "Function_40_89B1",        # 28, 40
        "Function_41_8A4A",        # 29, 41
        "Function_42_8A7E",        # 2A, 42
        "Function_43_8AB2",        # 2B, 43
        "Function_44_8AE6",        # 2C, 44
        "Function_45_8B1A",        # 2D, 45
        "Function_46_8B2A",        # 2E, 46
        "Function_47_A6AE",        # 2F, 47
        "Function_48_A6DE",        # 30, 48
        "Function_49_A71D",        # 31, 49
        "Function_50_AB99",        # 32, 50
        "Function_51_B252",        # 33, 51
        "Function_52_B513",        # 34, 52
    ))


    def Function_0_92C(): pass

    label("Function_0_92C")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_964"),
        (1, "loc_970"),
        (2, "loc_97C"),
        (3, "loc_988"),
        (4, "loc_994"),
        (5, "loc_9A0"),
        (6, "loc_9AC"),
        (SWITCH_DEFAULT, "loc_9B8"),
    )


    label("loc_964")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_970")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_97C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_988")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_994")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9A0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9AC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9B8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9C4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_9DB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_9C4")

    label("loc_9DB")

    Return()

    # Function_0_92C end

    def Function_1_9DC(): pass

    label("Function_1_9DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A3C")
    OP_95(0xFE, 7000, -300, 610, 6000, 0x0)
    OP_95(0xFE, 7000, 0, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, -10, -9140, 6000, 0x0)
    OP_95(0xFE, -1000, 0, 610, 6000, 0x0)
    Jump("Function_1_9DC")

    label("loc_A3C")

    Return()

    # Function_1_9DC end

    def Function_2_A3D(): pass

    label("Function_2_A3D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A9D")
    OP_95(0xFE, -10000, 0, 5750, 800, 0x0)
    OP_95(0xFE, -10000, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 2280, 800, 0x0)
    OP_95(0xFE, -27380, 0, 5750, 800, 0x0)
    Jump("Function_2_A3D")

    label("loc_A9D")

    Return()

    # Function_2_A3D end

    def Function_3_A9E(): pass

    label("Function_3_A9E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AC8")
    OP_94(0xFE, 0xFFFF8F3A, 0x9EC, 0xFFFFAD9E, 0x18EC, 0x3E8)
    Sleep(300)
    Jump("Function_3_A9E")

    label("loc_AC8")

    Return()

    # Function_3_A9E end

    def Function_4_AC9(): pass

    label("Function_4_AC9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B9C")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B08")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF40C, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B08")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B30")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF3A8, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B30")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B58")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF344, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_B80")
    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF2E0, 0x12C, 0x0)
    Jump("loc_B94")

    label("loc_B80")

    OP_96(0xFE, 0x1004, 0x0, 0xFFFFF27C, 0x12C, 0x0)

    label("loc_B94")

    Sleep(500)
    Jump("Function_4_AC9")

    label("loc_B9C")

    Return()

    # Function_4_AC9 end

    def Function_5_B9D(): pass

    label("Function_5_B9D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C70")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_BDC")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF40C, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_BDC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C04")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF3A8, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C04")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C2C")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF344, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C2C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C54")
    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF2E0, 0xC8, 0x0)
    Jump("loc_C68")

    label("loc_C54")

    OP_96(0xFE, 0xA14, 0x0, 0xFFFFF27C, 0xC8, 0x0)

    label("loc_C68")

    Sleep(600)
    Jump("Function_5_B9D")

    label("loc_C70")

    Return()

    # Function_5_B9D end

    def Function_6_C71(): pass

    label("Function_6_C71")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D44")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CB0")
    OP_96(0xFE, 0x11A8, 0x0, 0xFFFFF1AA, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_CB0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CD8")
    OP_96(0xFE, 0x11DA, 0x0, 0xFFFFF1DC, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_CD8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D00")
    OP_96(0xFE, 0x120C, 0x0, 0xFFFFF20E, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_D00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D28")
    OP_96(0xFE, 0x123E, 0x0, 0xFFFFF240, 0x12C, 0x0)
    Jump("loc_D3C")

    label("loc_D28")

    OP_96(0xFE, 0x1270, 0x0, 0xFFFFF272, 0x12C, 0x0)

    label("loc_D3C")

    Sleep(500)
    Jump("Function_6_C71")

    label("loc_D44")

    Return()

    # Function_6_C71 end

    def Function_7_D45(): pass

    label("Function_7_D45")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E18")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_D84")
    OP_96(0xFE, 0xE24, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_D84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DAC")
    OP_96(0xFE, 0xDF2, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DAC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DD4")
    OP_96(0xFE, 0xDC0, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DD4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_DFC")
    OP_96(0xFE, 0xD8E, 0x0, 0xFFFFF92A, 0xFA, 0x0)
    Jump("loc_E10")

    label("loc_DFC")

    OP_96(0xFE, 0xD5C, 0x0, 0xFFFFF92A, 0xFA, 0x0)

    label("loc_E10")

    Sleep(550)
    Jump("Function_7_D45")

    label("loc_E18")

    Return()

    # Function_7_D45 end

    def Function_8_E19(): pass

    label("Function_8_E19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_EEC")
    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E58")
    OP_96(0xFE, 0x910, 0x0, 0xFFFFF272, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_E58")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x28), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_E80")
    OP_96(0xFE, 0x942, 0x0, 0xFFFFF240, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_E80")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3C), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EA8")
    OP_96(0xFE, 0x974, 0x0, 0xFFFFF20E, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_EA8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_ED0")
    OP_96(0xFE, 0x9A6, 0x0, 0xFFFFF1DC, 0xC8, 0x0)
    Jump("loc_EE4")

    label("loc_ED0")

    OP_96(0xFE, 0x9D8, 0x0, 0xFFFFF1AA, 0xC8, 0x0)

    label("loc_EE4")

    Sleep(600)
    Jump("Function_8_E19")

    label("loc_EEC")

    Return()

    # Function_8_E19 end

    def Function_9_EED(): pass

    label("Function_9_EED")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F17")
    OP_94(0xFE, 0xFFFFFC18, 0xFFFFDCD8, 0x1B58, 0x0, 0x3E8)
    Sleep(300)
    Jump("Function_9_EED")

    label("loc_F17")

    Return()

    # Function_9_EED end

    def Function_10_F18(): pass

    label("Function_10_F18")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F78")
    OP_95(0xFE, -1630, 0, 5050, 2000, 0x0)
    OP_95(0xFE, 9840, 0, -6290, 2000, 0x0)
    OP_95(0xFE, 40380, 2060, -8580, 2000, 0x0)
    Sleep(500)
    SetChrPos(0xFE, -850, 3000, 27400, 180)
    Jump("Function_10_F18")

    label("loc_F78")

    Return()

    # Function_10_F18 end

    def Function_11_F79(): pass

    label("Function_11_F79")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E5")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1044")
    SetChrPos(0x0, 110, 3000, 22760, 180)
    SetChrPos(0x1, 110, 3000, 22760, 180)
    SetChrPos(0x2, 110, 3000, 22760, 180)
    SetChrPos(0x3, 110, 3000, 22760, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1017")
    SetChrPos(0x4, 110, 3000, 22760, 180)
    SetChrPos(0x5, 110, 3000, 22760, 180)
    Jump("loc_1036")

    label("loc_1017")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1036")
    SetChrPos(0x4, 110, 3000, 22760, 180)

    label("loc_1036")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_10E5")

    label("loc_1044")

    SetChrPos(0x0, 24460, 0, -8180, 270)
    SetChrPos(0x1, 24460, 0, -8180, 270)
    SetChrPos(0x2, 24460, 0, -8180, 270)
    SetChrPos(0x3, 24460, 0, -8180, 270)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10BD")
    SetChrPos(0x4, 24460, 0, -8180, 270)
    SetChrPos(0x5, 24460, 0, -8180, 270)
    Jump("loc_10DC")

    label("loc_10BD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10DC")
    SetChrPos(0x4, 24460, 0, -8180, 270)

    label("loc_10DC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_10E5")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1102")
    OP_C9(0x1, 0x1000)

    label("loc_1102")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118F")
    SetScenarioFlags(0x38, 0)

    label("loc_118F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A5")
    SetScenarioFlags(0x38, 1)

    label("loc_11A5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BB")
    SetScenarioFlags(0x38, 2)

    label("loc_11BB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D1")
    SetScenarioFlags(0x38, 3)

    label("loc_11D1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E7")
    SetScenarioFlags(0x38, 4)

    label("loc_11E7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FD")
    SetScenarioFlags(0x38, 5)

    label("loc_11FD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1213")
    SetScenarioFlags(0x38, 6)

    label("loc_1213")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1229")
    SetScenarioFlags(0x38, 7)

    label("loc_1229")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123F")
    SetScenarioFlags(0x39, 0)

    label("loc_123F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1255")
    SetScenarioFlags(0x39, 1)

    label("loc_1255")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_126B")
    SetScenarioFlags(0x39, 2)

    label("loc_126B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1281")
    SetScenarioFlags(0x39, 3)

    label("loc_1281")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1297")
    SetScenarioFlags(0x39, 4)

    label("loc_1297")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AD")
    SetScenarioFlags(0x39, 5)

    label("loc_12AD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C3")
    SetScenarioFlags(0x39, 6)

    label("loc_12C3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D9")
    SetScenarioFlags(0x39, 7)

    label("loc_12D9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12EF")
    SetScenarioFlags(0x3A, 0)

    label("loc_12EF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1305")
    SetScenarioFlags(0x3A, 1)

    label("loc_1305")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_131B")
    SetScenarioFlags(0x3A, 2)

    label("loc_131B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1331")
    SetScenarioFlags(0x3A, 3)

    label("loc_1331")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1347")
    SetScenarioFlags(0x3A, 4)

    label("loc_1347")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135D")
    SetScenarioFlags(0x3A, 5)

    label("loc_135D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1373")
    SetScenarioFlags(0x3A, 6)

    label("loc_1373")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1389")
    SetScenarioFlags(0x3A, 7)

    label("loc_1389")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139F")
    SetScenarioFlags(0x3B, 0)

    label("loc_139F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B5")
    SetScenarioFlags(0x3B, 1)

    label("loc_13B5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13CB")
    SetScenarioFlags(0x3B, 2)

    label("loc_13CB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13E1")
    SetScenarioFlags(0x3B, 3)

    label("loc_13E1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F7")
    SetScenarioFlags(0x3B, 4)

    label("loc_13F7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140D")
    SetScenarioFlags(0x3B, 5)

    label("loc_140D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1423")
    SetScenarioFlags(0x3B, 6)

    label("loc_1423")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1439")
    SetScenarioFlags(0x3B, 7)

    label("loc_1439")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144F")
    SetScenarioFlags(0x3D, 5)

    label("loc_144F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1465")
    SetScenarioFlags(0x3D, 6)

    label("loc_1465")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_147B")
    SetScenarioFlags(0x3D, 7)

    label("loc_147B")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14B6")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_15A6")

    label("loc_14B6")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D9")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_15A6")

    label("loc_14D9")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FC")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_15A6")

    label("loc_14FC")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_151F")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_15A6")

    label("loc_151F")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1542")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_15A6")

    label("loc_1542")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1565")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_15A6")

    label("loc_1565")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1588")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_15A6")

    label("loc_1588")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15A6")
    SetScenarioFlags(0x3C, 7)

    label("loc_15A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15BC")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_15BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15EE")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EE")
    SetChrPos(0x0, 33260, -4000, -18040, 278)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 34)

    label("loc_15EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1621")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1621")
    SetChrPos(0x0, 33490, -4000, -16740, 270)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_1621")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1635")
    ClearScenarioFlags(0x22, 0)
    Event(0, 35)
    Jump("loc_1644")

    label("loc_1635")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1644")
    ClearScenarioFlags(0x22, 1)
    Event(0, 37)

    label("loc_1644")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1655")
    Event(0, 36)

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1680")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1680")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1691")
    Event(0, 46)

    label("loc_1691")

    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1727")
    SetChrFlags(0xD, 0x80)
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16D6")
    SetChrFlags(0x8, 0x10)

    label("loc_16D6")

    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FC")
    SetChrFlags(0x9, 0x10)

    label("loc_16FC")

    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1722")
    SetChrFlags(0xC, 0x10)

    label("loc_1722")

    Jump("loc_1B15")

    label("loc_1727")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1753")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    Jump("loc_1B15")

    label("loc_1753")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_179E")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1B15")

    label("loc_179E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_17E9")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_1B15")

    label("loc_17E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_180E")
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 8)
    Jump("loc_1B15")

    label("loc_180E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_1879")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, -5710, 0, 1570, 180)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xA, 0xB)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1B15")

    label("loc_1879")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_18F1")
    SetChrPos(0x8, 30090, -4000, -15230, 225)
    BeginChrThread(0x8, 0, 0, 0)
    SetChrPos(0x9, 6330, -300, 1950, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xC, 4390, -40, 1630, 90)
    BeginChrThread(0xC, 0, 0, 0)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -6690, 0, 4460, 90)
    ClearChrFlags(0x11, 0x80)
    Jump("loc_1B15")

    label("loc_18F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_1953")
    SetChrPos(0x8, 30090, -4000, -15230, 225)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1920")
    SetChrFlags(0x8, 0x10)

    label("loc_1920")

    SetChrPos(0x9, 11110, -300, 5400, 270)
    BeginChrThread(0x9, 0, 0, 0)
    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 9)
    Jump("loc_1B15")

    label("loc_1953")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_19D5")
    SetChrPos(0x8, 4100, 0, -3260, 270)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1982")
    SetChrFlags(0x8, 0x10)

    label("loc_1982")

    SetChrPos(0x9, 2580, 0, -3260, 90)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A8")
    SetChrFlags(0x9, 0x10)

    label("loc_19A8")

    SetChrFlags(0xC, 0x80)
    SetChrPos(0xD, 8130, 3000, 13940, 180)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x161, 3)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19D0")
    SetChrFlags(0xB, 0x80)

    label("loc_19D0")

    Jump("loc_1B15")

    label("loc_19D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_19F7")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_1B15")

    label("loc_19F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_1A0F")
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jump("loc_1B15")

    label("loc_1A0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1A31")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)
    Jump("loc_1B15")

    label("loc_1A31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1AB1")
    SetChrPos(0x8, 4620, 0, -3570, 315)
    BeginChrThread(0x8, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A60")
    SetChrFlags(0x8, 0x10)

    label("loc_1A60")

    SetChrPos(0x9, 3520, 0, -1750, 180)
    BeginChrThread(0x9, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A86")
    SetChrFlags(0x9, 0x10)

    label("loc_1A86")

    SetChrPos(0xC, 2420, 0, -3570, 45)
    BeginChrThread(0xC, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AAC")
    SetChrFlags(0xC, 0x10)

    label("loc_1AAC")

    Jump("loc_1B15")

    label("loc_1AB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_1AF8")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrPos(0xA, -5710, 0, 1570, 180)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrChipByIndex(0xA, 0xB)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_1B15")

    label("loc_1AF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_1B15")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xE, 0x80)

    label("loc_1B15")

    Return()

    # Function_11_F79 end

    def Function_12_1B16(): pass

    label("Function_12_1B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BE2")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1BE2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C99")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)

    label("loc_1C99")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1D03")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)

    label("loc_1D03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D1B")
    ClearMapFlags(0x2000)
    Jump("loc_1D22")

    label("loc_1D1B")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_1D22")

    MiniGame(0x2F, 0x0, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x127, 7)), scpexpr(EXPR_END)), "loc_1DA0")
    SetMapObjFrame(0xFF, "tuika_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x0, 0x1)
    Jump("loc_1E2E")

    label("loc_1DA0")

    SetMapObjFrame(0xFF, "tuika_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x0, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x1, 0x1)
    SetMapObjFlags(0xA, 0x4)
    SetBarrier(0x0, 0x0, 0x1, 0x0, 18500, -1000, -11500, 5000, 5000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 37500, -5000, -19000, 5000, 5000, 90000)

    label("loc_1E2E")

    ClearMapObjFlags(0x7, 0x10)
    OP_70(0x7, 0x1E)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E4B")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E4B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E5E")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E71")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E84")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1E97")
    OP_1B(0x8, 0x0, 0x33)

    label("loc_1E97")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EB5")
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_1EB5")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED1")
    OP_66(0x5, 0x1)
    ClearMapObjFlags(0x3, 0x10)

    label("loc_1ED1")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1EED")
    OP_66(0x6, 0x1)
    ClearMapObjFlags(0x5, 0x10)

    label("loc_1EED")

    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_209D")
    Jump("loc_20AC")

    label("loc_209D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_20AC")
    SetMapObjFlags(0xC, 0x4)

    label("loc_20AC")

    MiniGame(0x2F, 0x0, 0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E1")
    OP_70(0xD, 0x0)
    Jump("loc_20E5")

    label("loc_20E1")

    OP_70(0xD, 0x1E)

    label("loc_20E5")

    Return()

    # Function_12_1B16 end

    def Function_13_20E6(): pass

    label("Function_13_20E6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21E6")
    Sound(14, 0, 100, 0)
    OP_74(0xD, 0x1E)
    OP_71(0xD, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x358, 1)"), scpexpr(EXPR_END)), "loc_216F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_21E1")

    label("loc_216F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x358),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xD, 0x1E, 0x0, 0x0, 0x0)

    label("loc_21E1")

    Jump("loc_222B")

    label("loc_21E6")

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

    label("loc_222B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_20E6 end

    def Function_14_2237(): pass

    label("Function_14_2237")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_22A3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2255")
    Call(0, 17)
    Jump("loc_229E")

    label("loc_2255")


    #C0004
    ChrTalk(
        0xFE,
        "あっ、兄ちゃんたち！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "クロスベル市のことは\x01",
            "俺たちに任せろよな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_229E")

    Jump("loc_2A45")

    label("loc_22A3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_22B1")
    Jump("loc_2A45")

    label("loc_22B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_23B7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2361")

    #C0006
    ChrTalk(
        0xFE,
        (
            "みんな、帝国と共和国がどうのとか\x01",
            "真剣に悩んでるみたいでさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "ドクリツがどうとかって、\x01",
            "よく分かんないけど……\x01",
            "嬉しいことじゃなかったのか？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_23B2")

    label("loc_2361")


    #C0008
    ChrTalk(
        0xFE,
        (
            "ドクリツって、\x01",
            "嬉しいことじゃなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        "俺にはよく分かんないよ……\x02",
    )

    CloseMessageWindow()

    label("loc_23B2")

    Jump("loc_2A45")

    label("loc_23B7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2437")

    #C0010
    ChrTalk(
        0xFE,
        (
            "モモを遊びに誘ったんだけど、\x01",
            "おばさんにダメって\x01",
            "言われたんだってさ……\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "はあ、なんだかしらけちゃうよな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A45")

    label("loc_2437")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_2465")

    #C0012
    ChrTalk(
        0xFE,
        "いやっほーい、待て待てー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A45")

    label("loc_2465")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2505")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24CB")

    #C0013
    ChrTalk(
        0xFE,
        "モモのやつ、おせーなー。\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "お使いくらい\x01",
            "早く終わらせたらいいのに。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2500")

    label("loc_24CB")


    #C0015
    ChrTalk(
        0xFE,
        (
            "モモのやつ、お使いくらい\x01",
            "早く終わらせろよなー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2500")

    Jump("loc_2A45")

    label("loc_2505")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_25E7")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2580")

    #C0016
    ChrTalk(
        0xFE,
        (
            "モモのやつ、ほんと探すの\x01",
            "へたくそだなあ……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "ふぁ～あ……\x01",
            "なんだか飽きてきちゃったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_25E2")

    label("loc_2580")


    #C0018
    ChrTalk(
        0xFE,
        (
            "じっとしてるのも\x01",
            "飽きてきちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "さっさと見つかって、\x01",
            "別の遊びをしたいんだけどな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_25E2")

    Jump("loc_2A45")

    label("loc_25E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_27A1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_273E")
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x8, 0x0, 500)

    #C0020
    ChrTalk(
        0xFE,
        (
            "おっと……\x01",
            "なんだよ、兄ちゃんたちか。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "あ～、ビックリした。\x01",
            "モモに見つかったかと\x01",
            "思ったじゃんか～。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#00006Fあのなぁ……\x01",
            "勝手にこんなところに\x01",
            "入り込むなよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "へへ、ケチくさいことは\x01",
            "言いっこなしだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xFE,
        (
            "オレがここに隠れてるのは\x01",
            "だまっててくれよな！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    OP_93(0xFE, 0xE1, 0x0)
    ClearChrFlags(0x8, 0x10)
    Jump("loc_279C")

    label("loc_273E")


    #C0025
    ChrTalk(
        0xFE,
        (
            "今、アンリたちと\x01",
            "かくれんぼしてんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xFE,
        (
            "オレがここに隠れてるのは\x01",
            "だまっててくれよな！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_279C")

    Jump("loc_2A45")

    label("loc_27A1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_281C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27BC")
    Call(0, 15)
    Jump("loc_2817")

    label("loc_27BC")


    #C0027
    ChrTalk(
        0xFE,
        (
            "そういや、キーアのやつ\x01",
            "最近元気なかったんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        "また今度遊びに誘ってやるか～。\x02",
    )

    CloseMessageWindow()

    label("loc_2817")

    Jump("loc_2A45")

    label("loc_281C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_282A")
    Jump("loc_2A45")

    label("loc_282A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_2989")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_292B")

    #C0029
    ChrTalk(
        0xFE,
        (
            "明日は、オルキスタワーで\x01",
            "ツーショーカイギってやつが\x01",
            "あるらしいじゃん。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "なんだかよく分からねーけど、\x01",
            "せっかくだからアンリたちと\x01",
            "見物に行くつもりなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "へへ、きっと楽しい\x01",
            "パーティか何かだよな。\x01",
            "明日が楽しみだぜ～♪\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_2984")

    label("loc_292B")


    #C0032
    ChrTalk(
        0xFE,
        (
            "ツーショーカイギってのは\x01",
            "多分パーティか何かだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "へへ、明日が楽しみだぜ～。\x02",
    )

    CloseMessageWindow()

    label("loc_2984")

    Jump("loc_2A45")

    label("loc_2989")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2997")
    Jump("loc_2A45")

    label("loc_2997")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2A2E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29B2")
    Call(0, 16)
    Jump("loc_2A29")

    label("loc_29B2")


    #C0034
    ChrTalk(
        0xFE,
        (
            "そういえば、キーアは今日\x01",
            "シズクって友達と\x01",
            "遊んでるんだっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "せっかくだし、そいつも\x01",
            "一緒に誘ってやるかな～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A29")

    Jump("loc_2A45")

    label("loc_2A2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2A3C")
    Jump("loc_2A45")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2A45")

    label("loc_2A45")

    TalkEnd(0xFE)
    Return()

    # Function_14_2237 end

    def Function_15_2A49(): pass

    label("Function_15_2A49")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)

    #C0036
    ChrTalk(
        0x8,
        (
            "今日はモモのやつ、\x01",
            "店の手伝いなんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "ちぇ、アンリと２人じゃ\x01",
            "遊びのハバがせまいよな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        (
            "リュウってば……\x01",
            "それはさすがに僕に\x01",
            "失礼じゃない？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    Return()

    # Function_15_2A49 end

    def Function_16_2B08(): pass

    label("Function_16_2B08")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0039
    ChrTalk(
        0x8,
        (
            "じゃあさー、明日はみんなで\x01",
            "オルキスタワーってやつを\x01",
            "見にいこうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "うん、いいね。\x01",
            "みんなでいこうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xC,
        "モ、モモもいくっ……！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "おっけー、\x01",
            "じゃあ朝イチで\x01",
            "百貨店前に集合な！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0xC, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_16_2B08 end

    def Function_17_2BF6(): pass

    label("Function_17_2BF6")

    OP_4B(0x8, 0xFF)
    OP_4B(0x9, 0xFF)
    OP_4B(0xC, 0xFF)

    #C0043
    ChrTalk(
        0x8,
        (
            "それじゃあみんなで\x01",
            "街のパトロールを始めるぞー！\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x8,
        "準備はいいか、アンリ、モモ！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        "はいっ、リュウ隊長！\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xC,
        "いこーっ！\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x8,
        (
            "よーし、そんじゃ行くか！\x01",
            "クロスベル少年特務支援課、出動ー！\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        "#00002F（はは、少年特務支援課って……）\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x102,
        "#00109F（何だか嬉しくなっちゃうわね。）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    SetScenarioFlags(0x0, 4)
    ClearChrFlags(0xC, 0x10)
    ClearChrFlags(0x9, 0x10)
    ClearChrFlags(0x8, 0x10)
    OP_4C(0x8, 0xFF)
    OP_4C(0x9, 0xFF)
    OP_4C(0xC, 0xFF)
    Return()

    # Function_17_2BF6 end

    def Function_18_2D43(): pass

    label("Function_18_2D43")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2DF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D61")
    Call(0, 17)
    Jump("loc_2DEC")

    label("loc_2D61")


    #C0050
    ChrTalk(
        0xFE,
        (
            "少年特務支援課か……\x01",
            "リュウもたまにはいいアイデアを\x01",
            "思いつきますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "やるからにはしっかりと\x01",
            "街のみなさんを助けていきたいです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DEC")

    Jump("loc_3472")

    label("loc_2DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2DFF")
    Jump("loc_3472")

    label("loc_2DFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2F61")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2ECB")

    #C0052
    ChrTalk(
        0xFE,
        (
            "ウチの父さんと母さんも、\x01",
            "昨日外国から戻ってきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "個人的にはうれしいんですけど、\x01",
            "みんなどこか複雑そうで……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "はあ、やっぱり独立って\x01",
            "大変なことなんでしょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_2F5C")

    label("loc_2ECB")


    #C0055
    ChrTalk(
        0xFE,
        (
            "父さんと母さんが帰ってきて\x01",
            "個人的にはうれしいんですけど、\x01",
            "みんなどこか複雑そうで……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "はあ、やっぱり独立って\x01",
            "大変なことなんでしょうか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F5C")

    Jump("loc_3472")

    label("loc_2F61")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FE0")

    #C0057
    ChrTalk(
        0xFE,
        (
            "モモのお母さんも、\x01",
            "心配なんだと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        (
            "仕方ないですよね……\x01",
            "襲撃事件なんてものが\x01",
            "あったんですから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3472")

    label("loc_2FE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3065")

    #C0059
    ChrTalk(
        0xFE,
        (
            "ちょ、ちょっと、リュウ！？\x01",
            "まだ何して遊ぶか\x01",
            "決まってないでしょ！\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "こんなの疲れるだけだから\x01",
            "ストップしてよ～！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3472")

    label("loc_3065")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3178")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3107")

    #C0061
    ChrTalk(
        0xFE,
        (
            "今朝いきなりリュウに誘われて、\x01",
            "タワー前の広場に行くことに\x01",
            "なったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "リュウったら、わざわざこんな\x01",
            "雨の日にしなくても……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_3173")

    label("loc_3107")


    #C0063
    ChrTalk(
        0xFE,
        (
            "も～、しかたないでしょ。\x01",
            "いきなり誘ったんだからさ。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "お使いが終わるまでは\x01",
            "ゆっくり待っていようよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3173")

    Jump("loc_3472")

    label("loc_3178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_3281")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_321D")

    #C0065
    ChrTalk(
        0xFE,
        "ふう、見つかっちゃいました。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "そういえばリュウは、\x01",
            "どこに隠れたんでしょう……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "また変なところに\x01",
            "入ってなきゃいいんですけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_327C")

    label("loc_321D")


    #C0068
    ChrTalk(
        0xFE,
        (
            "そういえば、さっきから\x01",
            "よく救急車が通るみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        "事故でもあったんでしょうか……？\x02",
    )

    CloseMessageWindow()

    label("loc_327C")

    Jump("loc_3472")

    label("loc_3281")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3305")

    #C0070
    ChrTalk(
        0xFE,
        (
            "この間かくれんぼをしたときは、\x01",
            "夕方までかかっちゃったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        (
            "モモ、ちゃんと\x01",
            "僕たちを見つけられるかなぁ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3472")

    label("loc_3305")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3320")
    Call(0, 15)
    Jump("loc_3391")

    label("loc_3320")


    #C0072
    ChrTalk(
        0xFE,
        (
            "モモがいたほうが、\x01",
            "出来る遊びも広がるし\x01",
            "楽しいんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        (
            "まあ、お手伝いがあるなら\x01",
            "仕方ありませんよね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3391")

    Jump("loc_3472")

    label("loc_3396")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_33A4")
    Jump("loc_3472")

    label("loc_33A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_33B2")
    Jump("loc_3472")

    label("loc_33B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_33C0")
    Jump("loc_3472")

    label("loc_33C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_345B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33DB")
    Call(0, 16)
    Jump("loc_3456")

    label("loc_33DB")


    #C0074
    ChrTalk(
        0xFE,
        (
            "噂じゃ、オルキスタワーは\x01",
            "高さ２５０アージュにも\x01",
            "なるらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xFE,
        (
            "一体どんな建物なんでしょう……\x01",
            "たのしみです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3456")

    Jump("loc_3472")

    label("loc_345B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3469")
    Jump("loc_3472")

    label("loc_3469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3472")

    label("loc_3472")

    TalkEnd(0xFE)
    Return()

    # Function_18_2D43 end

    def Function_19_3476(): pass

    label("Function_19_3476")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_3531")

    #C0076
    ChrTalk(
        0xFE,
        (
            "あんな大きくて、\x01",
            "しかも青白く光る大樹……\x01",
            "なんて物が現れたんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xFE,
        (
            "この先どうなるか分からないけど、\x01",
            "記録をしっかりととって\x01",
            "後世に伝えていかないといけないな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3531")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_353F")
    Jump("loc_4383")

    label("loc_353F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_35D8")

    #C0078
    ChrTalk(
        0xFE,
        (
            "ディーター大統領の言葉……\x01",
            "僕たち住民の心に強く響いたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xFE,
        (
            "２大国を敵に回すことに\x01",
            "なったとしても……\x01",
            "僕は彼を支持していきたいね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_35D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_3734")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36B9")

    #C0080
    ChrTalk(
        0xFE,
        (
            "復興活動をする人々や、\x01",
            "破壊されたＩＢＣなどの建物を\x01",
            "写真に収めているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xFE,
        (
            "二度とあんな恐ろしい事件を\x01",
            "起こさせてはいけない……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0xFE,
        (
            "それを忘れないためにも\x01",
            "きちんと記録をとっておかないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_372F")

    label("loc_36B9")


    #C0083
    ChrTalk(
        0xFE,
        (
            "二度とあんな恐ろしい事件を\x01",
            "起こさせてはいけない……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xFE,
        (
            "それを忘れないためにも\x01",
            "きちんと記録をとっておかないと。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_372F")

    Jump("loc_4383")

    label("loc_3734")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_3883")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3805")

    #C0085
    ChrTalk(
        0xFE,
        (
            "昨晩から、警備隊の装甲車が\x01",
            "何台もマインツ方面に\x01",
            "向かってるようなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xFE,
        (
            "これって、増援が向かってる\x01",
            "ってことだよね……\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0xFE,
        (
            "武装集団というのは\x01",
            "そこまで手強い相手なのか……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_387E")

    label("loc_3805")


    #C0088
    ChrTalk(
        0xFE,
        (
            "警備隊の増援が、\x01",
            "何台もマインツ方面に\x01",
            "向かってるようなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0xFE,
        (
            "武装集団というのは\x01",
            "そこまで手強い相手なのか……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_387E")

    Jump("loc_4383")

    label("loc_3883")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_3907")

    #C0090
    ChrTalk(
        0xFE,
        (
            "よく分からないが……\x01",
            "昨日の列車事故は得体の知れない\x01",
            "化物の仕業という話だね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xFE,
        "ふむ、また現れないか不安だよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_3907")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_395F")

    #C0092
    ChrTalk(
        0xFE,
        (
            "ふむ……\x01",
            "救急車のサイレンは苦手だよ。\x01",
            "なんだか不安になるというか……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_395F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3AFC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7A")

    #C0093
    ChrTalk(
        0xFE,
        (
            "クロスベル通信社が出版した\x01",
            "『クロスベル百景』という\x01",
            "観光ガイドを持っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0xFE,
        (
            "景観のいい場所がたくさん\x01",
            "掲載されていて、写真撮影に\x01",
            "大いに役立っているんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xFE,
        (
            "ただ、めぼしいスポットは\x01",
            "あらかた回ってしまってね。\x01",
            "次はどこで撮影しようかな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3AF7")

    label("loc_3A7A")


    #C0096
    ChrTalk(
        0xFE,
        (
            "今日はどこに写真を\x01",
            "撮りにいこうかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0xFE,
        (
            "『クロスベル百景』に\x01",
            "掲載されていたスポットは\x01",
            "あらかた回ってしまったしなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3AF7")

    Jump("loc_4383")

    label("loc_3AFC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_3C73")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BE1")

    #C0098
    ChrTalk(
        0xFE,
        (
            "この間、ウルスラ間道の中洲へ\x01",
            "写真を撮りに行ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xFE,
        (
            "そしたら、中州の奥のほうに\x01",
            "見慣れない道が出来ててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xFE,
        (
            "なんだか危なそうだったから\x01",
            "入りはしなかったけど……\x01",
            "あれってなんだったのかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3C6E")

    label("loc_3BE1")


    #C0101
    ChrTalk(
        0xFE,
        (
            "ウルスラ間道の中州の奥に\x01",
            "見慣れない道が出来ててね。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0xFE,
        (
            "なんだか危なそうだったから\x01",
            "入りはしなかったけど……\x01",
            "あれってなんだったのかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3C6E")

    Jump("loc_4383")

    label("loc_3C73")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3DC3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D42")

    #C0103
    ChrTalk(
        0xFE,
        (
            "今日はオルキスタワー周辺が\x01",
            "関係者以外立入禁止に\x01",
            "なってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0xFE,
        (
            "保安上しかたないとは思うけど、\x01",
            "ちょっと残念だなあ。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0xFE,
        (
            "昨日に続いて、\x01",
            "近くで写真を撮りたかったよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3DBE")

    label("loc_3D42")


    #C0106
    ChrTalk(
        0xFE,
        (
            "オルキスタワー周辺が\x01",
            "関係者以外立入禁止に\x01",
            "なってるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0xFE,
        (
            "まあ、今日は\x01",
            "百貨店の屋上から\x01",
            "撮影してみようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3DBE")

    Jump("loc_4383")

    label("loc_3DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_3ECF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E80")

    #C0108
    ChrTalk(
        0xFE,
        (
            "おっと……\x01",
            "感光クオーツが\x01",
            "切れてしまってるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xFE,
        (
            "昼間の除幕式で\x01",
            "写真を撮りすぎたみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xFE,
        (
            "オーバルストアが閉まる前に\x01",
            "新しいのを買いに行かないとね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_3ECA")

    label("loc_3E80")


    #C0111
    ChrTalk(
        0xFE,
        (
            "オーバルストアが閉まる前に\x01",
            "新しい感光クオーツを\x01",
            "買いに行かないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3ECA")

    Jump("loc_4383")

    label("loc_3ECF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4017")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3FA6")

    #C0112
    ChrTalk(
        0xFE,
        (
            "除幕式が終わってから、\x01",
            "オルキスタワーの写真を\x01",
            "沢山撮りに行ったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xFE,
        (
            "いや、それにしても\x01",
            "すごく大きな建物だったねえ。\x01",
            "地上４０階だったか……\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xFE,
        "うーん、現像するのが楽しみだよ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4012")

    label("loc_3FA6")


    #C0115
    ChrTalk(
        0xFE,
        (
            "オルキスタワーの写真を\x01",
            "沢山撮らせてもらったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xFE,
        (
            "あの建物はクロスベルの\x01",
            "新たな象徴になりそうだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4012")

    Jump("loc_4383")

    label("loc_4017")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4136")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_40CB")

    #C0117
    ChrTalk(
        0xFE,
        "通商会議が迫ってきたね。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0xFE,
        (
            "各国の偉い人が来るし、\x01",
            "新市庁ビルのお披露目をする\x01",
            "除幕式もある……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0xFE,
        (
            "シャッターチャンスを\x01",
            "逃さないようにしないと。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4131")

    label("loc_40CB")


    #C0120
    ChrTalk(
        0xFE,
        "各国のＶＩＰの来訪、除幕式……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0xFE,
        (
            "通商会議では\x01",
            "シャッターチャンスを\x01",
            "逃さないようにしないとね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4131")

    Jump("loc_4383")

    label("loc_4136")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_41E7")

    #C0122
    ChrTalk(
        0xFE,
        (
            "ふむ、やはり雨の景色というのも\x01",
            "普段とは趣きが違ってて良いねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xFE,
        (
            "雨天時のカメラ撮影はなかなかに\x01",
            "テクニックを要求されるんだが……\x01",
            "これがまた楽しいんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4383")

    label("loc_41E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4383")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_42D7")

    #C0124
    ChrTalk(
        0xFE,
        (
            "西クロスベル街道には\x01",
            "『ノックス森林地帯』という\x01",
            "場所があるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xFE,
        (
            "沢山の木々が生い茂って、\x01",
            "写真を撮るのによさそうな\x01",
            "ロケーションなんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0xFE,
        (
            "警察学校の敷地だから\x01",
            "一般人は立ち入り出来ないんだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_4383")

    label("loc_42D7")


    #C0127
    ChrTalk(
        0xFE,
        (
            "僕は写真撮影が趣味でね。\x01",
            "いい被写体を求めて\x01",
            "色々な場所に出かけているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xFE,
        (
            "『ノックス森林地帯』は\x01",
            "一般人は立ち入り出来ないけど、\x01",
            "いつか撮影に行きたいところだね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4383")

    TalkEnd(0xFE)
    Return()

    # Function_19_3476 end

    def Function_20_4387(): pass

    label("Function_20_4387")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_44CE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_445B")

    #C0129
    ChrTalk(
        0xFE,
        (
            "久しぶりに《モルジュ》に\x01",
            "コーヒーを飲みにきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0xFE,
        (
            "なんていうか……\x01",
            "これからクロスベルが徐々に\x01",
            "日常を取り戻せたらいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0xFE,
        (
            "……さすがにあの\x01",
            "巨大な樹のことは心配だけど。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_44C9")

    label("loc_445B")


    #C0132
    ChrTalk(
        0xFE,
        (
            "これからクロスベルが徐々に\x01",
            "日常を取り戻せたらいいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0xFE,
        (
            "……さすがにあの\x01",
            "巨大な樹のことは心配だけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_44C9")

    Jump("loc_4CB4")

    label("loc_44CE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_44DC")
    Jump("loc_4CB4")

    label("loc_44DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_45DF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_45AB")

    #C0134
    ChrTalk(
        0xFE,
        (
            "最近のクロスベルタイムズの\x01",
            "記事には僕も驚いてたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xFE,
        (
            "さすがにあそこまで\x01",
            "２大国を敵視した演説をするとは\x01",
            "思わなかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0xFE,
        (
            "これからのクロスベルの情勢が\x01",
            "心配だな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_45DA")

    label("loc_45AB")


    #C0137
    ChrTalk(
        0xFE,
        (
            "これからのクロスベルの情勢が\x01",
            "心配だな……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45DA")

    Jump("loc_4CB4")

    label("loc_45DF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4662")

    #C0138
    ChrTalk(
        0xFE,
        (
            "このあたりは\x01",
            "ほとんど被害がなかったのが\x01",
            "不幸中の幸いだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0xFE,
        (
            "行政区や港湾区は、\x01",
            "特に酷い有様だったからね……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4662")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_46AD")

    #C0140
    ChrTalk(
        0xFE,
        (
            "武装集団による占拠か……\x01",
            "マインツの人たちが心配だな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_46AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_46BB")
    Jump("loc_4CB4")

    label("loc_46BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_46F6")

    #C0141
    ChrTalk(
        0xFE,
        (
            "今日はずいぶんと\x01",
            "救急車を見かけるな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_46F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4768")

    #C0142
    ChrTalk(
        0xFE,
        (
            "かくれんぼか……\x01",
            "僕も昔、よくやったっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xFE,
        (
            "遊ぶ子供たちを見ると\x01",
            "ほほえましい気分になるね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4768")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_48B5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4844")

    #C0144
    ChrTalk(
        0xFE,
        (
            "市長の提唱する\x01",
            "クロスベル独立の是非……\x01",
            "難しい問題だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xFE,
        (
            "プルーナやリナリーにも\x01",
            "意見を聞いてみようかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0xFE,
        (
            "……やっぱやめた。\x01",
            "あの２人、あんまり深く\x01",
            "考えてなさそうだもんな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_48B0")

    label("loc_4844")


    #C0147
    ChrTalk(
        0xFE,
        (
            "クロスベル独立の是非……\x01",
            "難しい問題だよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0xFE,
        (
            "クロスベルタイムズを読んで\x01",
            "考えを巡らせてみるかなあ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_48B0")

    Jump("loc_4CB4")

    label("loc_48B5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4973")

    #C0149
    ChrTalk(
        0xFE,
        (
            "今日は『帝国時報社』や\x01",
            "レミフェリアの『アーデントプレス』も\x01",
            "会議の取材に行くらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xFE,
        (
            "どうせなら、書かれた記事を\x01",
            "クロスベルタイムズと\x01",
            "色々読み比べてみたいものだね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4A0A")

    #C0151
    ChrTalk(
        0xFE,
        (
            "カフェでぼーっと本を読んでたら\x01",
            "こんな時間になっちゃったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0xFE,
        (
            "ぶるっ……\x01",
            "夜はやっぱり冷えるねえ。\x01",
            "風邪を引かないうちに帰るかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4ABE")

    #C0153
    ChrTalk(
        0xFE,
        (
            "レミフェリアのアルバート大公は\x01",
            "ウルスラ医大に出資している\x01",
            "スポンサーの１人らしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0xFE,
        (
            "特にマクダエル議長は、\x01",
            "昔から大公と友好的な\x01",
            "付き合いがあるんだってさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CB4")

    label("loc_4ABE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4C4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BB6")

    #C0155
    ChrTalk(
        0xFE,
        (
            "西ゼムリア通商会議……\x01",
            "最近、よくクロスベルタイムズで\x01",
            "扱われているんだよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0xFE,
        (
            "経済関連の話し合いを\x01",
            "するということだけど、\x01",
            "どんな事が議題にあがるのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0xFE,
        (
            "うーん、今度マーブル先生に\x01",
            "詳しく質問してみようかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_4C45")

    label("loc_4BB6")


    #C0158
    ChrTalk(
        0xFE,
        (
            "西ゼムリア通商会議……\x01",
            "経済関連とは一口に言うけど\x01",
            "どんなことを話し合うのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xFE,
        (
            "うーん、今度マーブル先生に\x01",
            "詳しく質問してみようかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4C45")

    Jump("loc_4CB4")

    label("loc_4C4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4C58")
    Jump("loc_4CB4")

    label("loc_4C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4CB4")

    #C0160
    ChrTalk(
        0xFE,
        (
            "今日は夕方から\x01",
            "日曜学校の授業だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0xFE,
        "宿題、忘れずに持っていかないと。\x02",
    )

    CloseMessageWindow()

    label("loc_4CB4")

    TalkEnd(0xFE)
    Return()

    # Function_20_4387 end

    def Function_21_4CB8(): pass

    label("Function_21_4CB8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4D22")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4CD6")
    Call(0, 17)
    Jump("loc_4D1D")

    label("loc_4CD6")


    #C0162
    ChrTalk(
        0xFE,
        (
            "リュウくんたちといっしょに、\x01",
            "困ってる街のみんなを助けるのっ……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D1D")

    Jump("loc_4FB8")

    label("loc_4D22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4D30")
    Jump("loc_4FB8")

    label("loc_4D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4D3E")
    Jump("loc_4FB8")

    label("loc_4D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4D4C")
    Jump("loc_4FB8")

    label("loc_4D4C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_4D89")

    #C0163
    ChrTalk(
        0xFE,
        (
            "あ、あう……\x01",
            "おいかけっこはニガテなの……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4FB8")

    label("loc_4D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_4D97")
    Jump("loc_4FB8")

    label("loc_4D97")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_4E51")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E15")

    #C0164
    ChrTalk(
        0xFE,
        (
            "やっとアンリちゃんを\x01",
            "見つけたの……！\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xFE,
        (
            "よ、よーし……\x01",
            "つぎはリュウ君を\x01",
            "探さなくっちゃ……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4E4C")

    label("loc_4E15")


    #C0166
    ChrTalk(
        0xFE,
        (
            "でも、リュウ君の隠れ場所、\x01",
            "本当にわかんないの……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4E4C")

    Jump("loc_4FB8")

    label("loc_4E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_4F0C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4ED6")

    #C0167
    ChrTalk(
        0xFE,
        (
            "リュウ君たちと\x01",
            "かくれんぼしてるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0xFE,
        (
            "でも、全然みつけらんないの……\x01",
            "どこにかくれてるのかな……？\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_4F07")

    label("loc_4ED6")


    #C0169
    ChrTalk(
        0xFE,
        (
            "リュウ君たち、\x01",
            "どこにかくれてるのかな……？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4F07")

    Jump("loc_4FB8")

    label("loc_4F0C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_4F1A")
    Jump("loc_4FB8")

    label("loc_4F1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_4F28")
    Jump("loc_4FB8")

    label("loc_4F28")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_4F36")
    Jump("loc_4FB8")

    label("loc_4F36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_4F44")
    Jump("loc_4FB8")

    label("loc_4F44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_4FA1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F5F")
    Call(0, 16)
    Jump("loc_4F9C")

    label("loc_4F5F")


    #C0170
    ChrTalk(
        0xFE,
        (
            "明日はみんなで\x01",
            "百貨店に集合なの。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0xFE,
        "たのしみなの……\x02",
    )

    CloseMessageWindow()

    label("loc_4F9C")

    Jump("loc_4FB8")

    label("loc_4FA1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_4FAF")
    Jump("loc_4FB8")

    label("loc_4FAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_4FB8")

    label("loc_4FB8")

    TalkEnd(0xFE)
    Return()

    # Function_21_4CB8 end

    def Function_22_4FBC(): pass

    label("Function_22_4FBC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_4FCD")
    Jump("loc_5591")

    label("loc_4FCD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_4FDB")
    Jump("loc_5591")

    label("loc_4FDB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_4FE9")
    Jump("loc_5591")

    label("loc_4FE9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_4FF7")
    Jump("loc_5591")

    label("loc_4FF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_5068")

    #C0172
    ChrTalk(
        0xFE,
        "ま、まさか鉱山町の占拠だなんて……\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0xFE,
        (
            "なんだか不安だわ……\x01",
            "モモ、早く帰ってこないかしら……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5591")

    label("loc_5068")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5076")
    Jump("loc_5591")

    label("loc_5076")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_50D7")

    #C0174
    ChrTalk(
        0xFE,
        (
            "さっきから、救急車が\x01",
            "何度も行き来してるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0xFE,
        "何があったのかしら……？\x02",
    )

    CloseMessageWindow()
    Jump("loc_5591")

    label("loc_50D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_514D")

    #C0176
    ChrTalk(
        0xFE,
        (
            "イアン先生、とても忙しく\x01",
            "しているみたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0xFE,
        (
            "今日もたびたび、事務所を\x01",
            "出入りしているみたいよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5591")

    label("loc_514D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_51F9")

    #C0178
    ChrTalk(
        0xFE,
        (
            "通商会議以来、\x01",
            "独立について主人と真剣に\x01",
            "話す事が多くなったのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0xFE,
        (
            "私たちクロスベルの住民\x01",
            "全員に関係がある問題だもの。\x01",
            "しっかりと考えていかないとね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5591")

    label("loc_51F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_5207")
    Jump("loc_5591")

    label("loc_5207")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5215")
    Jump("loc_5591")

    label("loc_5215")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_5318")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52B7")

    #C0180
    ChrTalk(
        0xFE,
        "いらっしゃいませ～。\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0xFE,
        (
            "モモたち、今日は除幕式を\x01",
            "見に行ってるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xFE,
        (
            "ふふ、帰ってきたら\x01",
            "色々と話を\x01",
            "聞かせてもらわなくちゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5313")

    label("loc_52B7")


    #C0183
    ChrTalk(
        0xFE,
        (
            "モモたち、今日は除幕式を\x01",
            "見に行ってるのよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0xFE,
        (
            "ふふ、楽しんできて\x01",
            "くれるといいけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5313")

    Jump("loc_5591")

    label("loc_5318")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_54C6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5438")

    #C0185
    ChrTalk(
        0xFE,
        (
            "この間の雨の日、\x01",
            "モモがお使いからなかなか\x01",
            "帰らなくて、心配してたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0xFE,
        (
            "それで話を聞いてみたら、\x01",
            "失くした傘を捜してたんですって。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0xFE,
        (
            "モモったら、傘なんていくらでも\x01",
            "買い換えてあげるのに……\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0xFE,
        (
            "心配させるくらいだったら、\x01",
            "そのくらい安いものなんだから。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_54C1")

    label("loc_5438")


    #C0189
    ChrTalk(
        0xFE,
        (
            "でも、物を大事にするのは\x01",
            "とてもいい心がけよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0xFE,
        (
            "心配をかけたのはよくないけど、\x01",
            "モモにはその心をいつまでも\x01",
            "持っていてほしいわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_54C1")

    Jump("loc_5591")

    label("loc_54C6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_54D4")
    Jump("loc_5591")

    label("loc_54D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5591")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_553F")

    #C0191
    ChrTalk(
        0xFE,
        "いらっしゃいませ～。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0xFE,
        (
            "地域を支える\x01",
            "《タリーズ商店》は\x01",
            "こちらですよ～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_5591")

    label("loc_553F")


    #C0193
    ChrTalk(
        0xFE,
        (
            "モモも日曜学校に\x01",
            "行ったことだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0xFE,
        (
            "私たちは仕事を\x01",
            "がんばらなくちゃね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5591")

    TalkEnd(0xFE)
    Return()

    # Function_22_4FBC end

    def Function_23_5595(): pass

    label("Function_23_5595")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_55A6")
    Jump("loc_5C43")

    label("loc_55A6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_55B4")
    Jump("loc_5C43")

    label("loc_55B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_5640")

    #C0195
    ChrTalk(
        0xFE,
        (
            "今朝から国境門に向かっていく\x01",
            "導力車を多く見かけるぞい。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0xFE,
        (
            "どうやら、在留しとる外国人が\x01",
            "帰国していっているようじゃな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5C43")

    label("loc_5640")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_564E")
    Jump("loc_5C43")

    label("loc_564E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_565C")
    Jump("loc_5C43")

    label("loc_565C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_566A")
    Jump("loc_5C43")

    label("loc_566A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_57E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_575B")

    #C0197
    ChrTalk(
        0xFE,
        (
            "ベルガード門方面へのドライブから\x01",
            "帰ってきたところなのじゃが……\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0xFE,
        (
            "帰り道で見かけた\x01",
            "西クロスベル街道の事故現場は\x01",
            "大変な騒ぎになっておったぞい。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0xFE,
        (
            "ああまで豪快に脱線しておるとは\x01",
            "思いもよらんかったのう……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_57DC")

    label("loc_575B")


    #C0200
    ChrTalk(
        0xFE,
        (
            "帰り道で見かけた\x01",
            "西クロスベル街道の事故現場は\x01",
            "大変な騒ぎになっておった。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0xFE,
        (
            "警察や警備隊も大勢詰め掛けて\x01",
            "おったようじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_57DC")

    Jump("loc_5C43")

    label("loc_57E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_57EF")
    Jump("loc_5C43")

    label("loc_57EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_57FD")
    Jump("loc_5C43")

    label("loc_57FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_580B")
    Jump("loc_5C43")

    label("loc_580B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 0)), scpexpr(EXPR_END)), "loc_5819")
    Jump("loc_5C43")

    label("loc_5819")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_599D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5913")

    #C0202
    ChrTalk(
        0xFE,
        (
            "婆さんが怒っておってな、\x01",
            "ろくに口も利いてくれん。\x02",
        )
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0xFE,
        (
            "せっかく一緒に除幕式を\x01",
            "見に行こうというたのに、\x01",
            "無視しおったんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    #C0204
    ChrTalk(
        0xFE,
        (
            "花火を肴にあのワインを飲んだら、\x01",
            "最高じゃったろうに……\x01",
            "まったく、風情の分からん女じゃ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5998")

    label("loc_5913")


    #C0205
    ChrTalk(
        0xFE,
        (
            "ふん、なんじゃい。\x01",
            "高い買い物をしたくらいで\x01",
            "いつまでもぷりぷりと……\x02",
        )
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0xFE,
        (
            "婆さんがその気なら\x01",
            "わしだって知らんぷりしてやるわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5998")

    Jump("loc_5C43")

    label("loc_599D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_59AB")
    Jump("loc_5C43")

    label("loc_59AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_59B9")
    Jump("loc_5C43")

    label("loc_59B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_5C43")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5BD5")

    #C0207
    ChrTalk(
        0xFE,
        (
            "ほっほっほ、\x01",
            "やはり導力車はいいのう。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0xFE,
        (
            "婆さんはムダな浪費だと\x01",
            "抜かしおったが、\x01",
            "買って正解じゃったわい。\x02",
        )
    )

    CloseMessageWindow()

    #C0209
    ChrTalk(
        0x109,
        (
            "#10109Fヴェルヌ社製の導力車……\x01",
            "シックなデザインで\x01",
            "素敵だと思います！\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0xFE,
        (
            "ほお、これはこれは……\x01",
            "まだお若いのに話せるのう！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B0C")
    OP_63(0x109, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    label("loc_5B0C")

    Sleep(1000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B35")
    OP_63(0x0, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B5B")
    OP_63(0x1, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B5B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5B81")
    OP_63(0x2, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5B81")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5BA7")
    OP_63(0x3, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_5BA7")

    Sleep(1000)

    #C0211
    ChrTalk(
        0x101,
        "#00012F（意気投合してる……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_5C43")

    label("loc_5BD5")


    #C0212
    ChrTalk(
        0xFE,
        (
            "この導力車でのドライブは\x01",
            "本当に最高なんじゃよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0xFE,
        (
            "婆さんにも、そこのところを\x01",
            "分かって欲しいもんじゃ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C43")

    TalkEnd(0xFE)
    Return()

    # Function_23_5595 end

    def Function_24_5C47(): pass

    label("Function_24_5C47")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5C58")
    Jump("loc_5C94")

    label("loc_5C58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5C94")

    #C0214
    ChrTalk(
        0xFE,
        (
            "なんだか不安よね……\x01",
            "事故でもあったのかしら。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5C94")

    TalkEnd(0xFE)
    Return()

    # Function_24_5C47 end

    def Function_25_5C98(): pass

    label("Function_25_5C98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5CA9")
    Jump("loc_5CDC")

    label("loc_5CA9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_5CDC")

    #C0215
    ChrTalk(
        0xFE,
        "救急車の音は、あまり好きじゃない……\x02",
    )

    CloseMessageWindow()

    label("loc_5CDC")

    TalkEnd(0xFE)
    Return()

    # Function_25_5C98 end

    def Function_26_5CE0(): pass

    label("Function_26_5CE0")

    TalkBegin(0xFE)

    #C0216
    ChrTalk(
        0xFE,
        (
            "列車が脱線しているのを\x01",
            "見た時は、目を疑ったわよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0xFE,
        (
            "けが人も相当でていた\x01",
            "みたいだけれど、\x01",
            "大丈夫だったかしら……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_26_5CE0 end

    def Function_27_5D60(): pass

    label("Function_27_5D60")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_5DF8")

    #C0218
    ChrTalk(
        0xFE,
        (
            "もう、いつの間にか\x01",
            "靴の中がビッチョビチョの\x01",
            "グッチョグチョじゃない！\x02",
        )
    )

    CloseMessageWindow()

    #C0219
    ChrTalk(
        0xFE,
        (
            "だから雨って嫌いなの。\x01",
            "はやく用事を済ませて帰らなきゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5E64")

    label("loc_5DF8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_5E64")

    #C0220
    ChrTalk(
        0xFE,
        (
            "ああもう……雨のバカ！\x01",
            "うっとうしいったらありゃしない。\x02",
        )
    )

    CloseMessageWindow()

    #C0221
    ChrTalk(
        0xFE,
        "はやく用事を済ませて帰らなきゃ。\x02",
    )

    CloseMessageWindow()

    label("loc_5E64")

    TalkEnd(0xFE)
    Return()

    # Function_27_5D60 end

    def Function_28_5E68(): pass

    label("Function_28_5E68")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F6D")

    #C0222
    ChrTalk(
        0xFE,
        (
            "あんな事件が\x01",
            "起こってしまったからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0223
    ChrTalk(
        0xFE,
        (
            "微力ながらも、こうして\x01",
            "街を警戒させてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0xFE,
        (
            "仮に帝国が犯人だとして、\x01",
            "すぐまた襲撃してくる\x01",
            "可能性は低いとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0225
    ChrTalk(
        0xFE,
        (
            "とりあえず、\x01",
            "３日後の住民投票までは\x01",
            "気を抜けないよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_5FF7")

    label("loc_5F6D")


    #C0226
    ChrTalk(
        0xFE,
        (
            "仮に帝国が犯人だとして、\x01",
            "すぐまた襲撃してくる\x01",
            "可能性は低いとは思うけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0227
    ChrTalk(
        0xFE,
        (
            "とりあえず、\x01",
            "３日後の住民投票までは\x01",
            "気を抜けないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5FF7")

    TalkEnd(0xFE)
    Return()

    # Function_28_5E68 end

    def Function_29_5FFB(): pass

    label("Function_29_5FFB")

    TalkBegin(0xFF)

    #C0228
    ChrTalk(
        0x101,
        (
            "#00005Fセルゲイ課長が支援課に\x01",
            "何かを作ってるみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x102,
        (
            "#00104Fいずれにせよ、ここは\x01",
            "通らない方が良さそうね。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_29_5FFB end

    def Function_30_607E(): pass

    label("Function_30_607E")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされているようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CD, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BD, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x95, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D2")
    TalkEnd(0xFF)
    Call(0, 31)
    Return()

    label("loc_60D2")

    TalkEnd(0xFF)
    Return()

    # Function_30_607E end

    def Function_31_60D6(): pass

    label("Function_31_60D6")

    EventBegin(0x0)
    Fade(1000)
    OP_68(15530, 4300, 15700, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13270, 0)
    SetChrPos(0x101, 15530, 3000, 15700, 90)
    SetChrPos(0x102, 14820, 3000, 16800, 90)
    SetChrPos(0x103, 13710, 3000, 16700, 90)
    SetChrPos(0x104, 12510, 3000, 15490, 90)
    SetChrPos(0xF4, 13100, 3000, 14500, 90)
    SetChrPos(0xF5, 14690, 3000, 14290, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0231
    ChrTalk(
        0x101,
        (
            "#6P#00008F…………………………………………\x02\x03",

            "#00003F（さっきのピート君、クイントさん、\x01",
            "  そしてニールセンさんの話……）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6228")
    OP_63(0x0, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6228")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_624E")
    OP_63(0x1, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_624E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6274")
    OP_63(0x2, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_6274")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_629A")
    OP_63(0x3, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_629A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62C0")
    OP_63(0x4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_62C0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_62E6")
    OP_63(0x5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)

    label("loc_62E6")

    Sleep(1000)

    def lambda_62EE():
        TurnDirection(0x102, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_62EE)
    Sleep(50)

    def lambda_62FE():
        TurnDirection(0x103, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_62FE)

    def lambda_630B():
        TurnDirection(0x104, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_630B)
    Sleep(50)

    def lambda_631B():
        TurnDirection(0xF4, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_631B)
    Sleep(50)

    def lambda_632B():
        TurnDirection(0xF5, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xF5, 2, lambda_632B)
    WaitChrThread(0xF5, 2)

    #C0232
    ChrTalk(
        0x102,
        "#6P#00105Fロイド……どうかしたの？\x02",
    )

    CloseMessageWindow()

    #C0233
    ChrTalk(
        0x103,
        (
            "#6P#00200Fイアン先生の事務所に\x01",
            "何かあるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x104,
        "#6P#00301F今は留守みてぇだが……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(300)
    OP_93(0x101, 0x111, 0x1F4)

    #C0235
    ChrTalk(
        0x101,
        (
            "#11P#00006F……いや、なんでもない。\x01",
            "今は行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_6457")

    #C0236
    ChrTalk(
        0x10A,
        "#12P#00605F……………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_6457")

    OP_5A()
    SetScenarioFlags(0x1BE, 0)
    OP_2C(0xB1, 0x3)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_31_60D6 end

    def Function_32_6477(): pass

    label("Function_32_6477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_648E")
    Call(0, 49)
    Return()

    label("loc_648E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64A0")
    Call(0, 50)
    Return()

    label("loc_64A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64F2")

    #C0237
    ChrTalk(
        0x101,
        (
            "#00000F今は市外に出る用事はない。\x01",
            "車を使う必要もなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_64F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_65EA")
    CreatePortrait(0, 67, 20, 547, 276, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis241.itp")
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※支援課車両が使用可能になりました。\x02",
        )
    )

    CloseMessageWindow()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_57(0x3)
    OP_CB(0x0, 0x3, 0x80FFFFFF, 0x1F4, 0x0, 0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    SetScenarioFlags(0x12B, 2)
    SetScenarioFlags(0x31, 1)
    OP_C9(0x1, 0x200000)

    label("loc_65EA")

    SetMapFlags(0x80)
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6605")
    Jump("loc_6675")

    label("loc_6605")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6614")
    Jump("loc_6675")

    label("loc_6614")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_662F")
    SetScenarioFlags(0x31, 2)

    label("loc_662F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6675")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_666F")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6664")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_666A")

    label("loc_6664")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_666A")

    Jump("loc_6675")

    label("loc_666F")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_6675")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_668C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6A6B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_6705")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_66E5"),
        (SWITCH_DEFAULT, "loc_66F6"),
    )


    label("loc_66E5")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_6700")

    label("loc_66F6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6700")

    Jump("loc_6A66")

    label("loc_6705")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_6761")
    MenuCmd(1, 0, "導力車で休憩する")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_6761")

    MenuCmd(1, 0, "導力車のカスタマイズ")
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_69D1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6812")

    #C0239
    ChrTalk(
        0x101,
        (
            "#00003F導力車はこれで確保できた。\x02\x03",

            "#00001Fとりあえず、作戦の前に\x01",
            "駅に向かおう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69CC")

    label("loc_6812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_687A")

    #C0240
    ChrTalk(
        0x101,
        (
            "#00001F今はとにかく\x01",
            "ランディを追いかけないと――\x01",
            "まずは市内の調査を徹底しよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69CC")

    label("loc_687A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_68CD")

    #C0241
    ChrTalk(
        0x101,
        (
            "#00000F今は市外に出る用事はない。\x01",
            "車を使う必要もなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_69CC")

    label("loc_68CD")

    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_68FE")
    OP_70(0xA, 0x12C)
    OP_71(0xA, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_690E")

    label("loc_68FE")

    OP_70(0xA, 0xF0)
    OP_71(0xA, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_690E")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6964")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6964")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6987")
    Sound(461, 0, 100, 0)

    label("loc_6987")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_69A7")
    OP_70(0xA, 0x14A)
    OP_71(0xA, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_69B7")

    label("loc_69A7")

    OP_70(0xA, 0x10E)
    OP_71(0xA, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_69B7")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_70(0xA, 0x0)

    label("loc_69CC")

    Jump("loc_6A66")

    label("loc_69D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A47")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_6A0A")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_6A22")

    label("loc_6A0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_6A1D")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_6A22")

    label("loc_6A1D")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_6A22")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_6A66")

    label("loc_6A47")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A5C")
    Call(0, 33)
    Jump("loc_6A66")

    label("loc_6A5C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_6A66")

    Jump("loc_668C")

    label("loc_6A6B")

    SetMapObjFrame(0xA, "light", 0x1, 0x1)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_32_6477 end

    def Function_33_6A81(): pass

    label("Function_33_6A81")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_50(0x51, (scpexpr(EXPR_PUSH_LONG, 0xFF000000), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x0)
    SetChrFlags(0x0, 0x8)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AC7")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    label("loc_6AC7")

    SetMapObjFrame(0xFF, "main7", 0x0, 0x1)
    MiniGame(0x33, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetMapObjFrame(0xFF, "main7", 0x1, 0x1)
    ClearChrFlags(0x0, 0x8)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6B30")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_6B30")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    SetMapFlags(0x80)
    Return()

    # Function_33_6A81 end

    def Function_34_6B42(): pass

    label("Function_34_6B42")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_6B9D")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6B92")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_6B98")

    label("loc_6B92")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_6B98")

    Jump("loc_6BC1")

    label("loc_6B9D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_6BBB")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_6BC1")

    label("loc_6BBB")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_6BC1")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_34_6B42 end

    def Function_35_6BD6(): pass

    label("Function_35_6BD6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    OP_68(40100, -2850, -19150, 0)
    MoveCamera(50, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(18000, 0)
    OP_68(25400, -2250, -16450, 10000)
    MoveCamera(40, 30, 0, 10000)
    SetCameraDistance(24000, 10000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_35_6BD6 end

    def Function_36_6C81(): pass

    label("Function_36_6C81")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x105, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x109, 0x4)
    SetChrFlags(0x1A5, 0x4)
    SetChrPos(0x101, 43000, -4000, -18500, 270)
    SetChrPos(0x102, 43200, -4000, -19600, 270)
    SetChrPos(0x105, 44200, -4000, -18500, 270)
    SetChrPos(0x109, 44400, -4000, -19600, 270)
    SetChrPos(0x1A5, 46400, -4000, -19000, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x1A5, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_68(20000, -1500, -18000, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(28000, -1500, -18000, 6000)
    SetCameraDistance(23000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(103, 0, 100, 0)
    OP_79(0x5)
    Fade(500)
    OP_68(39500, -3100, -19000, 0)
    MoveCamera(53, 25, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(19000, 0)
    SetCameraDistance(18000, 2500)

    def lambda_6DE2():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6DE2)
    Sleep(100)

    def lambda_6DFF():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6DFF)
    Sleep(300)

    def lambda_6E1C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6E1C)
    Sleep(100)

    def lambda_6E30():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_6E30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x102, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_6E7D():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6E7D)
    Sleep(100)

    def lambda_6E9A():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6E9A)
    Sleep(100)

    def lambda_6EB7():
        OP_97(0x1A5, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A5, 0, lambda_6EB7)
    Sleep(800)

    def lambda_6ED4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_6ED4)
    Sleep(100)

    def lambda_6EE8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6EE8)
    Sleep(1000)

    def lambda_6EFC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1A5, 2, lambda_6EFC)
    OP_6F(0x79)

    #C0242
    ChrTalk(
        0x101,
        "#00005F#5Pこれって……\x02",
    )

    CloseMessageWindow()

    #C0243
    ChrTalk(
        0x102,
        "#11P#00105Fい、いつの間に？\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0244
    ChrTalk(
        0x109,
        (
            "#10105F#11Pあれ、支援課の裏口って\x01",
            "こんな感じでしたっけ？\x02",
        )
    )

    CloseMessageWindow()

    #C0245
    ChrTalk(
        0x105,
        (
            "#10302F#5Pへえ、いかにも\x01",
            "工事中って感じだけど。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x1A5, 0)

    #C0246
    ChrTalk(
        0x1A5,
        (
            "#11P#01105Fあ、そっか。\x01",
            "ロイドたちは知らないんだー。\x02\x03",

            "#01100Fえっとね、ロイドが出張したあと、\x01",
            "工事の人たちがやって来たの。\x02\x03",

            "かちょーが呼んだみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_706B():
        TurnDirection(0x101, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_706B)
    Sleep(50)

    def lambda_707B():
        TurnDirection(0x102, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_707B)
    Sleep(50)

    def lambda_708B():
        TurnDirection(0x105, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_708B)
    Sleep(50)

    def lambda_709B():
        TurnDirection(0x109, 0x1A5, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_709B)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0247
    ChrTalk(
        0x101,
        (
            "#6P#00006Fそうなのか……\x01",
            "昨日は気付かなかったな。\x02\x03",

            "#00001Fしかし課長、\x01",
            "一体どういうつもりなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x102,
        (
            "#6P#00103Fうーん、何か理由があっての\x01",
            "工事だと思うけど……\x02\x03",

            "#00100Fいずれにせよ、こっちの方は\x01",
            "通らない方が良さそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0249
    ChrTalk(
        0x101,
        "#6P#00000Fああ、１階の玄関から出よう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x1A5, 0x4)
    SetScenarioFlags(0x126, 3)
    EventEnd(0x5)
    NewScene("c0110", 108, 0, 0)
    IdleLoop()
    Return()

    # Function_36_6C81 end

    def Function_37_71F8(): pass

    label("Function_37_71F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch02500.itc", 0x1E)
    LoadChrToIndex("chr/ch02710.itc", 0x1F)
    LoadChrToIndex("apl/ch51107.itc", 0x20)
    SoundLoad(468)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01200.itp")
    OP_68(18000, 1660, -9000, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 19000, 0, -8600, 180)
    SetChrPos(0x102, 19000, 0, -8600, 180)
    SetChrPos(0x109, 19000, 0, -8600, 180)
    SetChrPos(0x105, 19000, 0, -8600, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x14, 0x1E)
    SetChrSubChip(0x14, 0x0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, 19000, 0, -8600, 180)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x15, 0x20)
    SetChrSubChip(0x15, 0x0)
    ClearChrFlags(0x15, 0x80)
    SetChrFlags(0x15, 0x8000)
    SetChrPos(0x15, 12500, 0, 500, 270)
    OP_A7(0x15, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrFlags(0x16, 0x20)
    SetChrFlags(0x16, 0x2)
    SetChrSubChip(0x16, 0x29)
    ClearChrFlags(0x16, 0x80)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x16, 42450, 2400, -22230, 315)
    SetChrFlags(0x16, 0x8)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 10050, 0, -8400, 90)
    SetChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 9350, 0, -6250, 90)
    SetChrFlags(0x9, 0x8)
    ClearChrFlags(0x19, 0x80)
    OP_78(0xA, 0x19)
    OP_49()
    SetChrPos(0x19, -36200, 0, 4000, 90)
    OP_D5(0x19, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xFF, 0xCF, 0xB5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "tuika_mul", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika", 0x1, 0x1)
    SetMapObjFrame(0xFF, "window01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "tuika2_mul", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kabuse", 0x0, 0x1)
    SetMapObjFlags(0xC, 0x4)
    SetChrFlags(0xB, 0x8)
    FadeToBright(1000, 0)
    Sound(468, 2, 80, 0)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 38)
    OP_68(-27750, 4250, 6400, 0)
    MoveCamera(69, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16000, 0)
    OP_68(-27750, 1250, 6400, 7500)
    OP_6F(0x79)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    EndChrThread(0x19, 0x3)
    Sound(459, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 39)
    BeginChrThread(0x1A, 1, 0, 45)
    OP_68(1950, 2350, -8400, 0)
    MoveCamera(22, 26, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(13650, 0)
    OP_68(18950, 2350, -8400, 7500)
    MoveCamera(22, 7, 0, 7500)
    OP_6F(0x79)
    WaitChrThread(0x19, 3)
    OP_0D()
    Sleep(500)

    #C0250
    ChrTalk(
        0x101,
        "#00005F#5Pあ……\x02",
    )

    CloseMessageWindow()
    OP_68(23200, 450, -21750, 3500)
    MoveCamera(30, 26, 0, 3500)
    OP_6E(700, 3500)
    SetCameraDistance(19850, 3500)
    OP_6F(0x79)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(462, 0, 100, 0)
    Sleep(1000)
    OP_68(19430, 800, -10000, 0)
    MoveCamera(30, 19, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(14350, 0)
    FadeToBright(1000, 0)
    OP_68(19430, 800, -8970, 2000)
    SetChrPos(0x101, 19600, 0, -10400, 180)
    SetChrPos(0x102, 20900, 0, -9500, 180)
    SetChrPos(0x109, 19600, 0, -9050, 180)
    SetChrPos(0x105, 18300, 0, -9950, 180)
    SetChrPos(0x14, 17550, 0, -8850, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_70(0xA, 0x10E)
    OP_6F(0x79)
    OP_0D()

    #C0251
    ChrTalk(
        0x14,
        "#01002F#5Pふむ、いい仕上がりだな。\x02",
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x101,
        "#00002F#5P課長、これって……\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x102,
        (
            "#00102F#5Pもしかして\x01",
            "この導力車のための？\x02",
        )
    )

    CloseMessageWindow()

    #C0254
    ChrTalk(
        0x14,
        (
            "#01004F#5Pああ、スロープ化と\x01",
            "駐車スペースの増設工事だ。\x02\x03",

            "#01004F予算は一応、警察本部から\x01",
            "ぶん取って来た。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x109,
        (
            "#10102F#5Pへえ……いいですね！\x02\x03",

            "#10109Fあれだけのスペースがあれば\x01",
            "整備とかも出来そうですし！\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、導力車のある生活か。\x01",
            "なかなか潤いがありそうだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0257
    ChrTalk(
        0x101,
        (
            "#00004F#5Pはは……キーアが\x01",
            "飛び上がって喜びそうだな。\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)

    #N0258
    NpcTalk(
        0x8,
        "男の子の声",
        "うわ～っ、何これ！？\x02",
    )

    CloseMessageWindow()

    #N0259
    NpcTalk(
        0x9,
        "男の子の声",
        "キレイな車……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x14, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_7929():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_7929)
    Sleep(50)

    def lambda_7939():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7939)
    Sleep(50)

    def lambda_7949():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7949)
    Sleep(50)

    def lambda_7959():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_7959)
    Sleep(50)

    def lambda_7969():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7969)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x14, 0)
    Fade(500)
    OP_68(13350, 800, -8750, 0)
    MoveCamera(30, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15800, 0)
    OP_68(18150, 800, -8750, 3000)
    SetCameraDistance(13800, 3000)

    def lambda_79DA():
        OP_96(0xFE, 0x3C8C, 0x0, 0xFFFFDAE4, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_79DA)

    def lambda_79F4():
        OP_96(0xFE, 0x3BC4, 0x0, 0xFFFFE08E, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_79F4)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_0D()

    #C0260
    ChrTalk(
        0x101,
        "#00002F#11Pやあ、リュウにアンリ。\x02",
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x102,
        "#00109F#11Pふふ、また会ったわね。\x02",
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x8,
        (
            "#6Pすっげー！\x01",
            "こんなクルマ見たことない！\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x8,
        (
            "#6Pもしかしてコレ、\x01",
            "兄ちゃんたちが買ったの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0264
    ChrTalk(
        0x101,
        (
            "#00004F#11Pはは、そんな訳ないって。\x02\x03",

            "#00002Fでも一応、支援課で\x01",
            "使えることになったんだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0265
    ChrTalk(
        0x9,
        "#6Pホ、ホントですか！？\x02",
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x8,
        (
            "#6P兄ちゃんたち、いつの間に\x01",
            "そんな出世したんだよっ！？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#00012F#11Pいや、別に出世したわけじゃ\x01",
            "ないんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0268
    ChrTalk(
        0x101,
        (
            "#00000F#11Pそういえば今日は\x01",
            "キーアと一緒じゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x102,
        (
            "#00100F#11Pひょっとして\x01",
            "モモちゃんと一緒かしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x9, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0270
    ChrTalk(
        0x8,
        "#6Pいや、わかんねーけど。\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x8,
        (
            "#6P日曜学校から一緒に\x01",
            "戻ってきたわけじゃねーし。\x02",
        )
    )

    CloseMessageWindow()

    #C0272
    ChrTalk(
        0x101,
        "#00005F#11Pえ、そうなのか？\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x9,
        (
            "#6Pキーアちゃん、マーブル先生に\x01",
            "用事があるって残ったんです。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x9,
        (
            "#6Pひょっとしたらまだ\x01",
            "大聖堂にいるのかも……\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x101,
        "#00001F#11Pそうなのか……\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x102,
        "#00108F#11Pどうしたのかしら……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)

    def lambda_7DF4():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_7DF4)
    Sleep(50)

    def lambda_7E04():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_7E04)
    Sleep(50)

    def lambda_7E14():
        TurnDirection(0x14, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_7E14)
    Sleep(50)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x14, 0)
    OP_64(0x101)
    OP_64(0x102)

    #C0277
    ChrTalk(
        0x105,
        (
            "#10302F#6Pやれやれ。\x01",
            "相変わらず過保護だねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x109,
        (
            "#10109F#5Pよっぽどキーアちゃんが\x01",
            "可愛くて仕方ないんですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#00012F#11Pい、いや～……\x01",
            "そんな事はないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x102,
        (
            "#00112F#11Pえ、ええ。\x01",
            "保護者として常識の範囲よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x14,
        (
            "#01004F#6Pクク、そんなに心配なら\x01",
            "大聖堂に迎えに行ったらどうだ？\x02\x03",

            "#01002Fせっかく足もあることだしな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x101,
        "#00000F#11Pあ、それもそうですね。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x109, 500)

    #C0283
    ChrTalk(
        0x102,
        "#00102F#11Pノエルさん、お願いできる？\x02",
    )

    CloseMessageWindow()

    def lambda_8004():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8004)
    Sleep(50)

    def lambda_8014():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8014)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    #C0284
    ChrTalk(
        0x109,
        "#10102F#5Pええ、お安い御用です。\x02",
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x8,
        (
            "#6Pえ、なに！？\x01",
            "キーアを迎えに行くの！？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x8,
        (
            "#6Pオレもオレも！\x01",
            "いっしょに乗せてくれよ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_80B0():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_80B0)
    Sleep(15)

    def lambda_80C0():
        OP_93(0x102, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_80C0)
    Sleep(15)

    def lambda_80D0():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_80D0)
    Sleep(15)

    def lambda_80E0():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_80E0)
    Sleep(15)

    def lambda_80F0():
        OP_93(0x14, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_80F0)
    Sleep(15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x14, 0)
    OP_63(0x9, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x9, 0x8, 500)

    #C0287
    ChrTalk(
        0x9,
        "#5Pちょ、ちょっとリュウ！\x02",
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x9,
        (
            "#5Pおじさんに早く帰って来いって\x01",
            "言われてたんじゃないの？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0289
    ChrTalk(
        0x8,
        "#12Pうぐっ、そうだった。\x02",
    )

    CloseMessageWindow()

    #C0290
    ChrTalk(
        0x8,
        (
            "#12P今日は珍しくねーちゃんが\x01",
            "帰ってるんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x101,
        (
            "#00004F#11Pはは、だったら早く\x01",
            "帰ってやらなくっちゃな。\x02\x03",

            "#00002Fまた今度、\x01",
            "２人とも乗せるからさ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_824C():
        OP_93(0x8, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_824C)
    Sleep(50)

    def lambda_825C():
        OP_93(0x9, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_825C)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    #C0292
    ChrTalk(
        0x8,
        "#6Pぜ、絶対だからな！\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x9,
        (
            "#6Pそれじゃあボクたち\x01",
            "これで失礼します。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x102,
        "#00109F#11Pふふ、気をつけて帰ってね。\x02",
    )

    CloseMessageWindow()

    def lambda_82E8():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_82E8)
    Sleep(50)

    def lambda_82F8():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_82F8)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)
    OP_68(19000, 800, -8750, 2500)

    def lambda_8321():
        OP_96(0xFE, 0x2742, 0x0, 0xFFFFDF30, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_8321)
    Sleep(50)

    def lambda_833E():
        OP_96(0xFE, 0x2486, 0x0, 0xFFFFE796, 0xDAC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_833E)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_6F(0x79)
    OP_93(0x14, 0x87, 0x1F4)

    #C0295
    ChrTalk(
        0x14,
        (
            "#01003F#5Pよし、そんじゃあ\x01",
            "とっとと行って来い。\x02\x03",

            "#01000F俺は一足先に戻るからな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_83C9():
        TurnDirection(0x101, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_83C9)
    Sleep(50)

    def lambda_83D9():
        TurnDirection(0x102, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_83D9)
    Sleep(50)

    def lambda_83E9():
        TurnDirection(0x109, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_83E9)
    Sleep(50)

    def lambda_83F9():
        TurnDirection(0x105, 0x14, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_83F9)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0296
    ChrTalk(
        0x101,
        "#00000F#12Pはい、了解しました。\x02",
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x102,
        "#00100F#11Pそれでは行って来ます。\x02",
    )

    CloseMessageWindow()
    OP_68(19000, 800, -9350, 2500)

    def lambda_8476():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_8476)

    def lambda_8483():
        OP_93(0xFE, 0xB4, 0xFA)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_8483)

    def lambda_8490():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8490)

    def lambda_849D():
        OP_93(0xFE, 0xB4, 0x96)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_849D)
    OP_93(0x14, 0xB4, 0x1F4)
    OP_96(0x14, 0x43C6, 0x0, 0xFFFFD27E, 0x9C4, 0x1)
    OP_96(0x14, 0x4A38, 0xFFFFF9C0, 0xFFFFC022, 0x9C4, 0x1)
    SetChrFlags(0x14, 0x80)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x109, 2)
    WaitChrThread(0x105, 2)
    OP_6F(0x79)

    #C0298
    ChrTalk(
        0x109,
        (
            "#10104F#5Pふふ、それじゃあ\x01",
            "大聖堂に向かいましょうか。\x02\x03",

            "#10100Fここからだと、中央広場から\x01",
            "歓楽街方面に抜けますね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_8567():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8567)
    Sleep(50)

    def lambda_8577():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8577)
    Sleep(50)

    def lambda_8587():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8587)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)

    #C0299
    ChrTalk(
        0x101,
        (
            "#00002F#12P分かった、お願いするよ。\x02\x03",

            "#00004F……うーん、キーアが\x01",
            "驚く顔が目に浮かぶなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x102,
        (
            "#00109F#12Pふふっ、あの子\x01",
            "導力車が大好きだものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x105,
        (
            "#10302F#6Pやれやれ。\x01",
            "ほんと親バカだなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(19000, 800, -6740, 6000)
    MoveCamera(45, 18, 0, 6000)
    Sleep(250)
    BeginChrThread(0x109, 3, 0, 44)
    Sleep(1000)
    BeginChrThread(0x105, 3, 0, 43)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 41)
    Sleep(1000)
    BeginChrThread(0x102, 3, 0, 42)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)
    Sound(461, 0, 100, 0)
    OP_71(0xA, 0x10F, 0x12C, 0x1, 0x8)
    Sleep(1000)
    Sleep(500)
    OP_68(11650, 1300, 450, 9000)
    MoveCamera(60, 21, 0, 9000)
    OP_6E(700, 9000)
    SetCameraDistance(16000, 9000)
    Sound(457, 0, 100, 0)
    BeginChrThread(0x19, 3, 0, 40)
    OP_6F(0x79)
    EndChrThread(0x19, 0x3)
    SetMapObjFlags(0xA, 0x4)
    Sound(100, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x4)
    Sleep(500)
    SetCameraDistance(20000, 8000)

    def lambda_8740():
        OP_9B(0x0, 0xFE, 0x0, 0x2EE0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_8740)

    def lambda_8755():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_8755)
    Sleep(1500)
    Sound(100, 0, 100, 0)
    OP_71(0x4, 0xA, 0x0, 0x0, 0x0)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x15, 2)
    SetChrFlags(0x15, 0x80)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Fade(1000)
    ClearChrFlags(0x16, 0x8)
    OP_68(41750, 3600, -21850, 0)
    MoveCamera(340, 30, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(16000, 3000)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    OP_63(0x16, 0xFFFFFE70, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x16)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    #Sound(3053, 255, 100, 0)    #voice#Zeit

    #A0302
    AnonymousTalk(
        0x16,
        "#30W…………グルル………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    FadeToDark(1000, 0, -1)
    SetCameraDistance(15500, 2000)
    OP_6F(0x79)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    WaitBGM()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x1D4)
    SetScenarioFlags(0x22, 1)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_37_71F8 end

    def Function_38_88C5(): pass

    label("Function_38_88C5")

    SetChrPos(0xFE, -36200, 0, 4000, 90)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -5850, 0, 4000)
    OP_9F(0x1, 800, 0, 1800)
    OP_9F(0x1, 8050, 0, -5950)
    OP_9F(0x1, 15500, 0, -6700)
    OP_9F(0x2, 0xFE, 5000, 0x6)
    Return()

    # Function_38_88C5 end

    def Function_39_891C(): pass

    label("Function_39_891C")

    SetChrPos(0xFE, 1250, 0, -1000, 180)
    OP_D5(0x19, 0x0, 0x2BF20, 0x0, 0x0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 5000, 0, -5500)
    OP_9F(0x1, 9000, 0, -6750)
    OP_9F(0x1, 16000, 0, -6750)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x3E8, 0x1)
    OP_71(0xA, 0x5B, 0x78, 0x1, 0x8)
    Return()

    # Function_39_891C end

    def Function_40_89B1(): pass

    label("Function_40_89B1")

    SetChrPos(0xFE, 19000, 0, -6740, 90)
    OP_D5(0xFE, 0x0, 0x15F90, 0x0, 0x0)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x3E8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x5DC, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0x9C4, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x190, 0xBB8, 0x1)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 27150, 50, -6740)
    OP_9F(0x1, 51600, 3950, -6740)
    OP_9F(0x2, 0xFE, 3500, 0x6)
    Return()

    # Function_40_89B1 end

    def Function_41_8A4A(): pass

    label("Function_41_8A4A")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_8A6D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8A6D)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_41_8A4A end

    def Function_42_8A7E(): pass

    label("Function_42_8A7E")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_8AA1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8AA1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_42_8A7E end

    def Function_43_8AB2(): pass

    label("Function_43_8AB2")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_8AD5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8AD5)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_43_8AB2 end

    def Function_44_8AE6(): pass

    label("Function_44_8AE6")

    OP_95(0xFE, 19000, 0, -8600, 2000, 0x0)
    OP_93(0xFE, 0x0, 0x1F4)
    Sleep(200)

    def lambda_8B09():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_8B09)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_44_8AE6 end

    def Function_45_8B1A(): pass

    label("Function_45_8B1A")

    Sleep(4500)
    StopSound(468, 1000, 80)
    Sound(492, 0, 80, 0)
    Return()

    # Function_45_8B1A end

    def Function_46_8B2A(): pass

    label("Function_46_8B2A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch13800.itc", 0x1E)
    LoadChrToIndex("chr/ch13801.itc", 0x1F)
    LoadChrToIndex("chr/ch13802.itc", 0x20)
    LoadChrToIndex("chr/ch08200.itc", 0x21)
    LoadChrToIndex("chr/ch08201.itc", 0x22)
    LoadChrToIndex("apl/ch50005.itc", 0x23)
    SoundLoad(847)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis244.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu08000.itp")
    OP_68(34500, -2900, -19000, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 38000, -4000, -19700, 270)
    SetChrPos(0x102, 38400, -4000, -18400, 270)
    SetChrPos(0x109, 39300, -4000, -19700, 270)
    SetChrPos(0x105, 39700, -4000, -18400, 270)
    SetChrPos(0x104, 40800, -4000, -19000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrFlags(0x18, 0x20)
    SetChrPos(0x18, 32700, 200, -36200, 0)
    OP_52(0x18, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrPos(0x17, 42000, -4000, -19000, 270)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0xA)
    SetCameraDistance(16500, 3000)

    def lambda_8CB0():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8CB0)
    Sleep(50)

    def lambda_8CCD():
        OP_97(0x102, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8CCD)
    Sleep(50)

    def lambda_8CEA():
        OP_97(0x105, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8CEA)
    Sleep(50)

    def lambda_8D07():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8D07)
    Sleep(50)

    def lambda_8D24():
        OP_97(0x104, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8D24)
    FadeToBright(2000, 0)
    Sleep(1000)
    Sound(104, 0, 100, 0)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x5)
    WaitChrThread(0x101, 0)
    Sound(846, 0, 100, 0)
    Sleep(300)
    StopBGM(0xBB8)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    def lambda_8DE9():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_8DE9)
    Sleep(50)

    def lambda_8DF9():
        OP_93(0x102, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_8DF9)
    Sleep(50)

    def lambda_8E09():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_8E09)
    Sleep(50)

    def lambda_8E19():
        OP_93(0x109, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_8E19)
    Sleep(50)

    def lambda_8E29():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_8E29)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    #C0303
    ChrTalk(
        0x101,
        "#5P#00005Fあれ……？\x02",
    )

    CloseMessageWindow()

    #C0304
    ChrTalk(
        0x102,
        "#00105F#5P鳥の鳴き声？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(10)
    WaitBGM()
    PlayBGM("ed7519", 0)
    Fade(250)
    OP_68(33700, -500, -27700, 0)
    MoveCamera(30, 27, 15, 0)
    OP_6E(700, 0)
    SetCameraDistance(12500, 0)
    OP_68(34700, -1000, -23700, 3000)
    MoveCamera(27, 27, 11, 3000)
    SetCameraDistance(15500, 3000)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 33200, -4000, -20000, 180)
    SetChrPos(0x102, 31800, -4000, -20300, 180)
    SetChrPos(0x109, 34600, -4000, -20000, 180)
    SetChrPos(0x104, 34700, -4000, -18700, 180)
    SetChrPos(0x105, 33300, -4000, -18700, 180)
    ClearChrFlags(0x18, 0x80)

    def lambda_8F61():

        label("loc_8F61")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_8F61")

    QueueWorkItem2(0x18, 2, lambda_8F61)

    def lambda_8F73():
        OP_96(0xFE, 0x7FBC, 0xFFFFF8F8, 0xFFFFAD30, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_8F73)
    Sound(847, 2, 70, 0)
    WaitChrThread(0x18, 1)
    BeginChrThread(0x18, 3, 0, 47)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8FB5():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8FB5)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_8FDD():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_8FDD)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9005():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9005)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_902D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_902D)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_9055():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_9055)
    Sleep(2000)
    Fade(500)
    OP_68(34300, -1800, -20900, 0)
    MoveCamera(40, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_52(0x18, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()

    #C0305
    ChrTalk(
        0x101,
        "#00011F#6Pな、なんだ！？\x02",
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x109,
        "#10111F#6Pし、白いタカ……？\x02",
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x105,
        (
            "#10305F#6P……いや\x01",
            "ハヤブサみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x104,
        (
            "#00301F#6Pおいおい、何だって\x01",
            "こんな街のど真ん中に……\x02",
        )
    )

    CloseMessageWindow()
    EndChrThread(0x18, 0x3)
    WaitChrThread(0x18, 1)
    EndChrThread(0x18, 0x0)
    OP_68(33300, -2800, -20900, 3000)
    MoveCamera(40, 21, 0, 3000)

    def lambda_918A():
        OP_9E(0xFE, 0x878C, 0xFFFFAD30, 0x50910, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_918A)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x73A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x76C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x79E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x802), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x834), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x866), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8CA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x92E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x992), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9F6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA28), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA5A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA8C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xABE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB22), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB54), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB86), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_930D():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_930D)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBEA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC4E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9356():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9356)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCB2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCE4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD16), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_939F():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_939F)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD7A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_93E8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_93E8)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE10), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE42), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xE74), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xEA6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)

    def lambda_9431():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_9431)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xED8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF0A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF3C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF6E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xFD2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(35)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x1004), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x18, 1)
    StopSound(847, 700, 60)
    Fade(250)
    EndChrThread(0x18, 0x2)
    SetChrPos(0x18, 33400, -3100, -21900, 0)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x0)
    ClearChrFlags(0x18, 0x1)

    def lambda_94D5():
        OP_96(0xFE, 0x8278, 0xFFFFF1F0, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_94D5)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x2)
    Sleep(300)
    WaitChrThread(0x18, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0309
    AnonymousTalk(
        0x18,
        (
            "ピューイ。\x02\x03",

            "ピュイ、ピュイ、ピューイ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0310
    ChrTalk(
        0x101,
        (
            "#00001F#5Pも、もしかして……\x01",
            "俺たちに何か用があるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x102,
        (
            "#5P#00108Fツァイトが話しかける時と\x01",
            "同じような感じだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0312
    ChrTalk(
        0x104,
        (
            "#5P#00306Fうーん、ティオすけがいたら\x01",
            "何喋ってんのか判りそうだが……\x02",
        )
    )

    CloseMessageWindow()
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x5, 0x10)
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x5)
    ClearChrFlags(0x17, 0x80)

    def lambda_9714():
        OP_96(0xFE, 0x9A4C, 0xFFFFF060, 0xFFFFB5C8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_9714)

    def lambda_972E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_972E)
    WaitChrThread(0x17, 1)
    Sound(104, 0, 100, 0)
    OP_71(0x5, 0xA, 0x0, 0x0, 0x0)

    #C0313
    ChrTalk(
        0x17,
        "#01105F#12Pあれー、どうしたのー？\x02",
    )

    OP_79(0x5)
    SetMapObjFlags(0x5, 0x10)
    CloseMessageWindow()
    OP_63(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    SetChrChipByIndex(0x17, 0x22)
    SetChrSubChip(0x17, 0x0)

    def lambda_97A8():
        OP_95(0xFE, 37500, -4000, -19000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_97A8)
    WaitChrThread(0x17, 1)

    def lambda_97C6():
        OP_95(0xFE, 34500, -4000, -21300, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_97C6)
    Sleep(300)

    def lambda_97E3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_97E3)
    Sleep(100)

    def lambda_97F3():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_97F3)
    Sleep(100)

    def lambda_9803():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_9803)
    Sleep(100)

    def lambda_9813():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_9813)
    WaitChrThread(0x17, 1)
    SetChrChipByIndex(0x17, 0x21)
    SetChrSubChip(0x17, 0x0)
    OP_93(0x17, 0xE1, 0x1F4)
    #Sound(3029, 255, 100, 0)    #voice#KeA

    #C0314
    ChrTalk(
        0x17,
        (
            "#01110F#11Pわぁ、白いトリだぁ！\x02\x03",

            "#01109Fクチバシも尖ってて\x01",
            "カッコイイー！\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x18, 0x20)
    SetChrSubChip(0x18, 0x0)
    TurnDirection(0x18, 0x17, 0)
    Sleep(300)

    #C0315
    ChrTalk(
        0x18,
        (
            "#6P#08009Fピューイ㈱\x02\x03",

            "ピュイイ、ピュイ、ピュイ♪\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x17,
        (
            "#01103F#11Pふむ、ふむ。\x02\x03",

            "#01102Fなるほど、そうなんだー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)

    #C0317
    ChrTalk(
        0x101,
        (
            "#00012F#5P（キーア……\x01",
            "  やっぱり判るのかな？）\x02",
        )
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x109,
        "#10112F#5P（ス、スゴイですね……）\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    def lambda_99ED():

        label("loc_99ED")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_99ED")

    QueueWorkItem2(0x17, 2, lambda_99ED)
    SetChrChipByIndex(0x18, 0x1F)
    SetChrSubChip(0x18, 0x2)

    #C0319
    ChrTalk(
        0x17,
        (
            "#01100F#11Pえっとね、この子、\x01",
            "『ジーク』っていうんだってー。\x02\x03",

            "ロイドたちに伝言があるから\x01",
            "受け取ってって言ってるよー？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9A82():
        TurnDirection(0x101, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_9A82)
    Sleep(50)

    def lambda_9A92():
        TurnDirection(0x104, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_9A92)
    Sleep(50)

    def lambda_9AA2():
        TurnDirection(0x109, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9AA2)
    Sleep(50)

    def lambda_9AB2():
        TurnDirection(0x105, 0x18, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_9AB2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0320
    ChrTalk(
        0x101,
        "#00011F#5Pそ、そうなのか……\x02",
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x104,
        (
            "#5P#00305Fお、確かに脚のところに\x01",
            "メモが括りつけてあるな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9B33():
        OP_95(0xFE, 33200, -4000, -21000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_9B33)
    TurnDirection(0x18, 0x101, 500)
    WaitChrThread(0x101, 1)
    EndChrThread(0x17, 0x2)
    SetChrName("")

    #A0322
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは白ハヤブサの脚に\x01",
            "括りつけてあったメモを取った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x23)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0323
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "拝啓　クロスベル警察、特務支援課様\x02\x03",

            "皆様の評判を耳にして\x01",
            "不躾#4Rぶしつけ#ですが連絡させていただきました。\x02\x03",

            "もしお時間があれば内密に\x01",
            "相談に乗っていただけないでしょうか。\x02\x03",

            "本日夕刻、クロスベル空港、\x01",
            "待合いテラスにてお待ちしております。\x02\x03",

            "追伸　もしご都合がつかない場合も\x01",
            "ご返答は頂かなくて結構です。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(150)

    #A0324
    AnonymousTalk(
        0x101,
        "#00005F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0325
    AnonymousTalk(
        0x102,
        "#00101Fこ、これって……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0326
    AnonymousTalk(
        0x109,
        (
            "#10106F内容といい、差出人不明といい\x01",
            "怪しすぎますけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0327
    AnonymousTalk(
        0x105,
        (
            "#10302Fでも、綺麗な筆跡だし、\x01",
            "文章も丁寧な感じだね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0328
    AnonymousTalk(
        0x104,
        (
            "#00301F何よりも、メモに押されてる\x01",
            "この白ハヤブサの紋章は……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0329
    AnonymousTalk(
        0x18,
        (
            "#08000Fピューイ。\x02\x03",

            "ピュイ、ピュイ、ピューイ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    Sound(847, 2, 70, 0)

    def lambda_9ED0():
        OP_96(0xFE, 0x8278, 0xFFFFF3E4, 0xFFFFAA74, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9ED0)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    Sleep(100)
    SetChrSubChip(0x18, 0x0)
    Sleep(100)
    SetChrSubChip(0x18, 0x1)
    WaitChrThread(0x18, 1)
    OP_68(33300, -1800, -24900, 5000)
    MoveCamera(46, 21, 0, 5000)
    SetCameraDistance(16000, 5000)
    Fade(250)
    SetChrPos(0x18, 33400, -3600, -21900, 0)
    SetChrChipByIndex(0x18, 0x1E)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x1)

    def lambda_9F56():

        label("loc_9F56")

        OP_A0(0xFE, 1500, 0x0, 0x4)
        Yield()
        Jump("loc_9F56")

    QueueWorkItem2(0x18, 2, lambda_9F56)
    BeginChrThread(0x18, 3, 0, 48)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDDE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xDAC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD7A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD48), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xD16), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCE4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xCB2), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC80), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC4E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBEA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB86), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB54), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xB22), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xAF0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xABE), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA8C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA5A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xA28), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9F6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x992), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x960), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x92E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8FC), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x8CA), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x898), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x866), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x834), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x802), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x79E), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x76C), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x73A), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(45)
    OP_52(0x18, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x708), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    WaitChrThread(0x18, 3)

    def lambda_A18B():
        OP_96(0xFE, 0x8278, 0xFFFFFED4, 0xFFFF7B94, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A18B)
    Sleep(300)

    def lambda_A1A8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_A1A8)
    Sleep(100)

    def lambda_A1B8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_A1B8)
    Sleep(100)

    def lambda_A1C8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_A1C8)
    Sleep(100)

    def lambda_A1D8():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_A1D8)
    StopSound(847, 2000, 60)
    WaitChrThread(0x18, 1)
    EndChrThread(0x18, 0xFF)
    SetChrFlags(0x18, 0x80)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1500)
    OP_6F(0x79)
    Fade(500)
    OP_68(33300, -2800, -20900, 0)
    MoveCamera(40, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_0D()
    TurnDirection(0x101, 0x17, 500)

    #C0330
    ChrTalk(
        0x101,
        (
            "#6P#00011Fえっと……\x01",
            "キーア、彼はなんて？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x101, 500)

    #C0331
    ChrTalk(
        0x17,
        (
            "#01111F#11Pんー、行くか行かないかは\x01",
            "ロイドたち次第だってー。\x02",
        )
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x101,
        "#6P#00003Fそうか……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    def lambda_A357():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_A357)
    Sleep(50)

    def lambda_A367():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_A367)
    Sleep(50)

    def lambda_A377():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_A377)
    Sleep(50)

    def lambda_A387():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_A387)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)

    #C0333
    ChrTalk(
        0x102,
        (
            "#6P#00108Fど、どうするの？\x02\x03",

            "#00101Fまさかそんな訳は\x01",
            "無いとは思うんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x104,
        "#5P#00306Fああ、さすがになぁ。\x02",
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x109,
        (
            "#10108F#11Pでも、白ハヤブサの紋章って……\x01",
            "今の子もそうだったみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x105,
        (
            "#10309F#5Pあはは、いやが上にも\x01",
            "期待しちゃうよねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(450)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(150)

    #C0337
    ChrTalk(
        0x101,
        (
            "#12P#00003F──せっかくのお誘いだ。\x01",
            "ここはお受けしておこう。\x02\x03",

            "#00000Fまだ夕方まで時間はあるから\x01",
            "用事を済ませてからでもいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x102,
        "#6P#00106Fわ、分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x109,
        "#10106F#11Pき、緊張してきました……\x02",
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x104,
        (
            "#5P#00309Fまあ、さすがに正装して\x01",
            "行く必要はないだろうが……\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x105,
        (
            "#10302F#5Pフフ、それじゃあ用が済んだら\x01",
            "南口のクロスベル空港に行こうか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x17, 0x13B, 0x1F4)
    Sleep(150)

    #C0342
    ChrTalk(
        0x17,
        (
            "#11P#01110Fよく分からないけど\x01",
            "みんな、がんばってねー。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    SetChrFlags(0x17, 0x80)
    OP_49()
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_D7(0x23)
    SetChrPos(0x0, 34000, -4000, -19000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x140, 7)
    OP_29(0xA3, 0x1, 0x11)
    OP_C9(0x1, 0x1000)
    OP_24(0x34F)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7150", 0)
    EventEnd(0x5)
    Return()

    # Function_46_8B2A end

    def Function_47_A6AE(): pass

    label("Function_47_A6AE")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A6DD")

    def lambda_A6BE():
        OP_9E(0xFE, 0x8980, 0xFFFFAD30, 0x57E40, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A6BE)
    WaitChrThread(0x18, 1)
    Jump("Function_47_A6AE")

    label("loc_A6DD")

    Return()

    # Function_47_A6AE end

    def Function_48_A6DE(): pass

    label("Function_48_A6DE")


    def lambda_A6E3():
        OP_9E(0xFE, 0x846C, 0xFFFFAA74, 0x2BF20, 0xED8, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A6E3)
    WaitChrThread(0x18, 1)

    def lambda_A702():
        OP_9E(0xFE, 0x8084, 0xFFFFAA74, 0x57E40, 0x1194, 0x1)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_A702)
    WaitChrThread(0x18, 1)
    Return()

    # Function_48_A6DE end

    def Function_49_A71D(): pass

    label("Function_49_A71D")

    EventBegin(0x0)
    Fade(500)
    OP_68(33500, -2700, -18100, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 32600, -4000, -19400, 0)
    SetChrPos(0x102, 31300, -4000, -18800, 45)
    SetChrPos(0x103, 34100, -4000, -19500, 315)
    SetChrPos(0x104, 35400, -4000, -18300, 270)
    SetChrPos(0x109, 33500, -4000, -17600, 0)
    SetChrPos(0x105, 31000, -4000, -17700, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Sleep(300)

    #C0343
    ChrTalk(
        0x103,
        (
            "#00206F#12Pそういえば……\x02\x03",

            "#00200Fノエルさんの運転も\x01",
            "今日が最後なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_A828():
        OP_93(0x109, 0xB3, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_A828)
    Sleep(400)

    #C0344
    ChrTalk(
        0x101,
        "#12P#00006Fそうか……そうだったな。\x02",
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x109,
        (
            "#10112F#5Pあはは……\x01",
            "あたしもすごく残念です。\x02\x03",

            "この子#2Rクルマ#、個人的にも\x01",
            "かなり気に入ってましたし。\x02\x03",

            "#10100Fでも、ロイドさんたちも\x01",
            "もうかなり運転できますよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x101,
        (
            "#12P#00004Fああ、休みの日なんか\x01",
            "ノエルに鍛えてもらったしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x102,
        (
            "#6P#00109Fふふっ、分かりやすくて\x01",
            "とっても助かっちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x105,
        (
            "#6P#10306Fうーん、\x01",
            "でも結構スパルタだったよね？\x02\x03",

            "#10302F曹長っていうより\x01",
            "鬼軍曹って感じだったかな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x109, 0x105, 500)
    Sleep(300)

    #C0349
    ChrTalk(
        0x109,
        (
            "#11P#10101Fそ、それは君が\x01",
            "減らず口ばかり叩くからでしょ？\x02\x03",

            "#10106Fやればちゃんと出来るのに\x01",
            "交通ルールも覚えてこないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x104,
        (
            "#00304F#11Pま、厳しく教えられるのも\x01",
            "軍人には必要な資質だからな。\x02\x03",

            "#00300Fとりあえず、今日一杯は\x01",
            "プロの運転を堪能させてもらおぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#12P#00002Fああ。\x01",
            "ノエル、よろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0352
    ChrTalk(
        0x109,
        "#10109F#5Pはい、お任せください！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 33500, -4000, -18000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x180, 4)
    EventEnd(0x5)
    Return()

    # Function_49_A71D end

    def Function_50_AB99(): pass

    label("Function_50_AB99")

    EventBegin(0x0)
    Fade(500)
    OP_68(33500, -2900, -17100, 0)
    MoveCamera(53, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 33500, -4000, -17600, 0)
    SetChrPos(0x102, 32600, -4000, -19400, 0)
    SetChrPos(0x103, 34100, -4000, -19500, 315)
    SetChrPos(0x104, 35400, -4000, -18300, 315)
    SetChrPos(0xF4, 31300, -4000, -18800, 45)
    SetChrPos(0xF5, 31000, -4000, -17700, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0353
    ChrTalk(
        0x101,
        (
            "#11P#00002F俺たちの車……\x01",
            "何とか無事みたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B058")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_ACD2")

    #C0354
    ChrTalk(
        0x109,
        "#6P#10109F良かった……一安心です。\x02",
    )

    CloseMessageWindow()

    label("loc_ACD2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AEBF")

    #C0355
    ChrTalk(
        0x105,
        (
            "#6P#10405Fしかしこれって確か、\x01",
            "ディーター市長にある程度、\x01",
            "融通してもらったんだよね？\x02\x03",

            "#10409Fフフ、それを使って\x01",
            "彼を逮捕しに行くなんて\x01",
            "皮肉が利いているじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AD90():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AD90)
    Sleep(50)

    def lambda_ADA0():
        TurnDirection(0x103, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_ADA0)
    Sleep(50)

    def lambda_ADB0():
        TurnDirection(0x101, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_ADB0)
    Sleep(50)

    def lambda_ADC0():
        TurnDirection(0x104, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_ADC0)
    Sleep(50)

    def lambda_ADD0():
        TurnDirection(0xF4, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_ADD0)
    Sleep(50)

    def lambda_ADE0():
        TurnDirection(0xF5, 0x105, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_ADE0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0356
    ChrTalk(
        0x102,
        "#12P#00106F……そうね、本当に。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE95")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0xF4, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_AE71")

    #C0357
    ChrTalk(
        0x109,
        "#12P#10101Fワジ君、あのねぇ……\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE95")

    label("loc_AE71")


    #C0358
    ChrTalk(
        0x109,
        "#6P#10101Fワジ君、あのねぇ……\x02",
    )

    CloseMessageWindow()

    label("loc_AE95")


    #C0359
    ChrTalk(
        0x103,
        "#00211F洒落になっていません……\x02",
    )

    CloseMessageWindow()
    Jump("loc_B053")

    label("loc_AEBF")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B053")

    #C0360
    ChrTalk(
        0x10A,
        (
            "#6P#00603Fふむ……\x01",
            "問題は無さそうだ。\x02\x03",

            "#00600Fしかし確か、この車は\x01",
            "ディーター元市長がある程度、\x01",
            "融通したと聞いているが？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_AF52():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_AF52)
    Sleep(50)

    def lambda_AF62():
        TurnDirection(0x103, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_AF62)
    Sleep(50)

    def lambda_AF72():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_AF72)
    Sleep(50)

    def lambda_AF82():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_AF82)
    Sleep(50)

    def lambda_AF92():
        TurnDirection(0xF4, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_AF92)
    Sleep(50)

    def lambda_AFA2():
        TurnDirection(0xF5, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_AFA2)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0361
    ChrTalk(
        0x102,
        "#12P#00108Fそ、そういえば……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B030")

    #C0362
    ChrTalk(
        0x109,
        (
            "#6P#10106F確かにセルゲイ課長が\x01",
            "そう仰ってましたね……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B030")


    #C0363
    ChrTalk(
        0x103,
        "#00211F……なんか皮肉的です。\x02",
    )

    CloseMessageWindow()

    label("loc_B053")

    Jump("loc_B190")

    label("loc_B058")


    #C0364
    ChrTalk(
        0x109,
        (
            "#6P#10104F良かった……一安心です。\x02\x03",

            "#10105F……そういえばこの車、\x01",
            "ディーター市長にある程度\x01",
            "融通してもらったんですよね。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B0DA():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_B0DA)
    Sleep(50)

    def lambda_B0EA():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_B0EA)
    Sleep(50)

    def lambda_B0FA():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_B0FA)
    Sleep(50)

    def lambda_B10A():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_B10A)
    Sleep(50)

    def lambda_B11A():
        TurnDirection(0xF4, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_B11A)
    Sleep(50)

    def lambda_B12A():
        TurnDirection(0xF5, 0x109, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_B12A)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0365
    ChrTalk(
        0x102,
        "#12P#00108Fそ、そういえば……\x02",
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x103,
        "#00211F……なんか皮肉的です。\x02",
    )

    CloseMessageWindow()

    label("loc_B190")

    OP_93(0x104, 0x13B, 0x1F4)
    Sleep(150)

    #C0367
    ChrTalk(
        0x104,
        (
            "#00304Fま、経緯はどうあれ、\x01",
            "こいつも支援課の一員だ。\x02\x03",

            "#00302Fちゃんと使えるかどうか、\x01",
            "中もチェックするとしようぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0368
    ChrTalk(
        0x101,
        "#11P#00000Fああ、そうだな。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x23, 1)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_50_AB99 end

    def Function_51_B252(): pass

    label("Function_51_B252")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B2D8")
    EventBegin(0x1)

    #C0369
    ChrTalk(
        0x101,
        (
            "#00000Fこの先は西クロスベル街道だな。\x02\x03",

            "手配魔獣がいるけど……\x01",
            "まずは市内の仕事を片付けよう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B2D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B3A0")
    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B350")

    #C0370
    ChrTalk(
        0x101,
        (
            "#00000Fこの先は西クロスベル街道だな。\x02\x03",

            "特に用事はないし、\x01",
            "出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_B38C")

    label("loc_B350")


    #C0371
    ChrTalk(
        0x101,
        (
            "#00000Fこちら方面に用事はない。\x01",
            "出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B38C")

    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B3A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B417")
    EventBegin(0x1)

    #C0372
    ChrTalk(
        0x101,
        (
            "#00001F今はとにかく\x01",
            "ランディを追いかけないと――\x01",
            "脇道にそれてる場合じゃない。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B417")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B47D")
    EventBegin(0x1)

    #C0373
    ChrTalk(
        0x101,
        (
            "#00001F今は市外に出ている場合じゃない。\x01",
            "大人しく引き返そう。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B47D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B512")
    EventBegin(0x1)

    #C0374
    ChrTalk(
        0x101,
        (
            "#00001Fここまで来て市内を\x01",
            "離れるわけにはいかない。\x02\x03",

            "オルキスタワー突入作戦――\x01",
            "何としても成功させなきゃな。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, -34230, 0, 4210, 90)
    EventEnd(0x4)
    Return()

    label("loc_B512")

    Return()

    # Function_51_B252 end

    def Function_52_B513(): pass

    label("Function_52_B513")

    TalkBegin(0xFF)
    Sound(807, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B576")

    #C0375
    ChrTalk(
        0x101,
        (
            "#00000F内側から鍵が\x01",
            "かかってるみたいだな。\x02\x03",

            "正面入り口から入るか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_B5D0")

    label("loc_B576")

    SetChrName("")

    #A0376
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵がかかっている。\x01",
            "どうやら内側から\x01",
            "ロックされているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_B5D0")

    TalkEnd(0xFF)
    Return()

    # Function_52_B513 end

    SaveToFile()

Try(main)
