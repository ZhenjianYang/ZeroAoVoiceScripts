from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c120d.bin",                # FileName
        "c120d",                    # MapName
        "c120d",                    # Location
        0x001A,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 1, 0, 4, 0, 5],
    )

    BuildStringList((
        "c120d",                  # 0
        "ヨナ",                   # 1
        "警官",                   # 2
        "警備隊員",               # 3
        "警備隊員",               # 4
        "クーニャ",               # 5
        "オーゼル",               # 6
        "ビショップ",             # 7
        "クワイン老人",           # 8
        "アミサ",                 # 9
        "警官",                   # 10
        "国防軍兵士",             # 11
        "装甲車",                 # 12
        "ニールセン",             # 13
        "マリアベル",             # 14
        "警備員ビルス",           # 15
        "車",                     # 16
        "車",                     # 17
        "bc1200",                 # 18
        "中央広場",               # 19
        "西通り",                 # 20
        "行政区",                 # 21
        "住宅街",                 # 22
        "歓楽街",                 # 23
        "東通り",                 # 24
        "旧市街",                 # 25
        "港湾区",                 # 26
        "ＩＢＣ",                 # 27
        "駅前通り",               # 28
        "裏通り",                 # 29
        "ウルスラ間道",           # 30
        "東クロスベル街道",       # 31
        "西クロスベル街道",       # 32
        "マインツ山道",           # 33
        "オルキスタワー",         # 34
    ))

    ATBonus("ATBonus_674", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_7159", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_6C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_728", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_72C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_730", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_734", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_738", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_73C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_740", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C0", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_744", 0x0000, 99, 6, 60, 4, 1, 25, 0, "bc1200", "Sepith_7159", 60, 25, 10, 5,
        (
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_674"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_674"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_6C4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_674"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, "MonsterBattlePostion_6A4", "MonsterBattlePostion_724", "ed7450", "ed7453", "ATBonus_674"),
        )
    )

    AddCharChip((
        "chr/ch06100.itc",                   # 00
        "chr/ch30000.itc",                   # 01
        "chr/ch31200.itc",                   # 02
        "chr/ch31300.itc",                   # 03
        "chr/ch22100.itc",                   # 04
        "chr/ch25200.itc",                   # 05
        "chr/ch26000.itc",                   # 06
        "chr/ch24000.itc",                   # 07
        "chr/ch21500.itc",                   # 08
        "chr/ch30000.itc",                   # 09
        "chr/ch41400.itc",                   # 0A
        "chr/ch45102.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
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

    DeclNpc(75500,   -2500,   20000,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(22079,   0,       15050,   180,  389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(3130,    2000,    25149,   180,  389,  0x0, 0,   2,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(5530,    2000,    25000,   180,  389,  0x0, 0,   3,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(-13199,  0,       11500,   90,   385,  0x0, 0,   4,   0,   0,   1,   0,   12,  255,  0)
    DeclNpc(-10470,  0,       13340,   180,  385,  0x0, 0,   5,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-52470,  2000,    21149,   90,   385,  0x0, 0,   6,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(39669,   -2500,   -19379,  135,  385,  0x0, 0,   7,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(40919,   -2500,   -18989,  135,  385,  0x0, 0,   8,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(-17799,  0,       13369,   180,  389,  0x0, 0,   9,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(-18479,  0,       12000,   180,  389,  0x0, 0,   10,  0,   0,   0,   0,   18,  255,  0)
    DeclNpc(-21239,  0,       14350,   90,   196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(7820,    -400,    3200,    180,  389,  0x0, 0,   11,  0,   255, 255, 0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(3140,    -1200,   -700,    0x10100E1,    "BattleInfo_744", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(38750,   1370,    -2500,   0x10100E1,    "BattleInfo_744", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-16760,  9670,    -10,     0x10100E1,    "BattleInfo_744", 0,   16,  0xFFFF, 0,  1)

    DeclActor(16750,   -1000,   -15740,  1200,    16750,   0,       -15740,  0x007C, 0,  6,  0x0000)
    DeclActor(82470,   -2500,   15010,   1200,    79890,   -3500,   8810,    0x007C, 0,  20, 0x0000)
    DeclActor(20620,   10,      15670,   2000,    20620,   1500,    15670,   0x007C, 0,  35, 0x0000)
    DeclActor(4550,    2000,    25990,   2000,    4550,    3000,    25990,   0x007C, 0,  36, 0x0000)
    DeclActor(77220,   -2500,   20290,   2000,    77220,   -1000,   20290,   0x007C, 0,  21, 0x0000)

    PlaceName(-123.13999938964844, 0.0, -85.1500015258789, 0x0000, 0x0000, "中央広場")
    PlaceName(-209.27000427246094, 0.0, -79.26000213623047, 0x0000, 0x0000, "西通り")
    PlaceName(-87.7699966430664, 0.0, 31.440000534057617, 0x0000, 0x0000, "行政区")
    PlaceName(-289.17999267578125, 0.0, 18.34000015258789, 0x0000, 0x0000, "住宅街")
    PlaceName(-193.5500030517578, 0.0, 7.860000133514404, 0x0000, 0x0000, "歓楽街")
    PlaceName(-16.700000762939453, 0.0, -115.27999877929688, 0x0000, 0x0000, "東通り")
    PlaceName(29.799999237060547, 0.0, -187.3300018310547, 0x0000, 0x0000, "旧市街")
    PlaceName(19.979999542236328, 0.0, -28.81999969482422, 0x0000, 0x0000, "港湾区")
    PlaceName(-14.079999923706055, 0.0, 94.31999969482422, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-108.4000015258789, 0.0, -175.5399932861328, 0x0000, 0x0000, "駅前通り")
    PlaceName(-169.97000122070312, 0.0, -39.29999923706055, 0x0000, 0x0000, "裏通り")
    PlaceName(-112.33000183105469, 0.0, -216.14999389648438, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(54.040000915527344, 0.0, -96.94000244140625, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-276.0799865722656, 0.0, -81.22000122070312, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-268.2200012207031, 0.0, 49.779998779296875, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-96.5, 0.0, 203.75, 0x0000, 0x0000, "オルキスタワー")
    PlaceName(-151.9600067138672, 0.0, -103.48999786376953, 0x0000, 0x0051, "")
    PlaceName(-81.55000305175781, 0.0, -69.43000030517578, 0x0000, 0x0054, "")
    PlaceName(-119.87000274658203, 0.0, -113.97000122070312, 0x0000, 0x0057, "")
    PlaceName(-152.94000244140625, 0.0, -65.5, 0x0000, 0x0053, "")
    PlaceName(-126.08999633789062, 0.0, -34.060001373291016, 0x0000, 0x0053, "")
    PlaceName(-192.57000732421875, 0.0, -72.05000305175781, 0x0000, 0x0053, "")
    PlaceName(-205.33999633789062, 0.0, -44.540000915527344, 0x0000, 0x0053, "")
    PlaceName(-173.89999389648438, 0.0, -2.619999885559082, 0x0000, 0x0052, "")
    PlaceName(-167.67999267578125, 0.0, -19.649999618530273, 0x0000, 0x0053, "")
    PlaceName(-156.22000122070312, 0.0, -30.790000915527344, 0x0000, 0x0053, "")
    PlaceName(-118.87999725341797, 0.0, 62.22999954223633, 0x0000, 0x0051, "")
    PlaceName(27.84000015258789, 0.0, -115.27999877929688, 0x0000, 0x0052, "")
    PlaceName(5.570000171661377, 0.0, -233.83999633789062, 0x0000, 0x0053, "")
    PlaceName(-11.460000038146973, 0.0, -209.60000610351562, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_8B8",          # 00, 0
        "Function_1_968",          # 01, 1
        "Function_2_A19",          # 02, 2
        "Function_3_B00",          # 03, 3
        "Function_4_B28",          # 04, 4
        "Function_5_EC7",          # 05, 5
        "Function_6_1512",         # 06, 6
        "Function_7_1663",         # 07, 7
        "Function_8_1676",         # 08, 8
        "Function_9_168C",         # 09, 9
        "Function_10_17D6",        # 0A, 10
        "Function_11_1873",        # 0B, 11
        "Function_12_191D",        # 0C, 12
        "Function_13_1D1A",        # 0D, 13
        "Function_14_204F",        # 0E, 14
        "Function_15_22EE",        # 0F, 15
        "Function_16_255A",        # 10, 16
        "Function_17_27B2",        # 11, 17
        "Function_18_28A1",        # 12, 18
        "Function_19_293E",        # 13, 19
        "Function_20_2A10",        # 14, 20
        "Function_21_2AE4",        # 15, 21
        "Function_22_2C69",        # 16, 22
        "Function_23_413F",        # 17, 23
        "Function_24_43DA",        # 18, 24
        "Function_25_4465",        # 19, 25
        "Function_26_44AD",        # 1A, 26
        "Function_27_5A63",        # 1B, 27
        "Function_28_5AA0",        # 1C, 28
        "Function_29_5AF5",        # 1D, 29
        "Function_30_5B4A",        # 1E, 30
        "Function_31_5B9F",        # 1F, 31
        "Function_32_5BF4",        # 20, 32
        "Function_33_5C49",        # 21, 33
        "Function_34_5C9E",        # 22, 34
        "Function_35_704D",        # 23, 35
        "Function_36_70B7",        # 24, 36
    ))


    def Function_0_8B8(): pass

    label("Function_0_8B8")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_8F0"),
        (1, "loc_8FC"),
        (2, "loc_908"),
        (3, "loc_914"),
        (4, "loc_920"),
        (5, "loc_92C"),
        (6, "loc_938"),
        (SWITCH_DEFAULT, "loc_944"),
    )


    label("loc_8F0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_8FC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_908")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_914")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_920")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_92C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_938")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_944")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_950")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_967")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_950")

    label("loc_967")

    Return()

    # Function_0_8B8 end

    def Function_1_968(): pass

    label("Function_1_968")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_A18")
    OP_95(0xFE, 14600, 0, 11500, 1000, 0x0)
    OP_95(0xFE, 20200, 0, 8200, 1000, 0x0)
    OP_95(0xFE, 20200, 0, -6200, 1000, 0x0)
    OP_95(0xFE, 14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -14000, 0, -11700, 1000, 0x0)
    OP_95(0xFE, -20000, 0, -6400, 1000, 0x0)
    OP_95(0xFE, -20000, 0, 6000, 1000, 0x0)
    OP_95(0xFE, -13200, 0, 11500, 1000, 0x0)
    Jump("Function_1_968")

    label("loc_A18")

    Return()

    # Function_1_968 end

    def Function_2_A19(): pass

    label("Function_2_A19")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AFF")
    Sleep(3000)
    OP_95(0xFE, -13000, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -13000, 2000, 24150, 5000, 0x0)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_A0(0xFE, 5000, 0x0, 0xFB)
    OP_A0(0xFE, 4000, 0x0, 0xFB)
    OP_95(0xFE, -13000, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -22020, 0, -46700, 5000, 0x0)
    Sleep(3000)
    OP_95(0xFE, -22130, 0, 5860, 5000, 0x0)
    OP_95(0xFE, -15540, 0, 14240, 5000, 0x0)
    OP_95(0xFE, -15540, 2000, 21150, 5000, 0x0)
    OP_95(0xFE, -52470, 2000, 21150, 5000, 0x0)
    Jump("Function_2_A19")

    label("loc_AFF")

    Return()

    # Function_2_A19 end

    def Function_3_B00(): pass

    label("Function_3_B00")

    SetMapObjFlags(0xB, 0x2000000)
    SetMapObjFlags(0xC, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B27")
    SetMapObjFlags(0x4, 0x2000000)
    ClearMapObjFlags(0xB, 0x2000000)
    ClearMapObjFlags(0xC, 0x2000000)

    label("loc_B27")

    Return()

    # Function_3_B00 end

    def Function_4_B28(): pass

    label("Function_4_B28")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D63")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEA")
    SetChrPos(0x0, 4870, 3350, 31570, 180)
    SetChrPos(0x1, 4870, 3350, 31570, 180)
    SetChrPos(0x2, 4870, 3350, 31570, 180)
    SetChrPos(0x3, 4870, 3350, 31570, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BBD")
    SetChrPos(0x4, 4870, 3350, 31570, 180)
    SetChrPos(0x5, 4870, 3350, 31570, 180)
    Jump("loc_BDC")

    label("loc_BBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BDC")
    SetChrPos(0x4, 4870, 3350, 31570, 180)

    label("loc_BDC")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D63")

    label("loc_BEA")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CC2")
    SetChrPos(0x0, -28110, 2000, 23520, 90)
    SetChrPos(0x1, -28110, 2000, 23520, 90)
    SetChrPos(0x2, -28110, 2000, 23520, 90)
    SetChrPos(0x3, -28110, 2000, 23520, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C95")
    SetChrPos(0x4, -28110, 2000, 23520, 90)
    SetChrPos(0x5, -28110, 2000, 23520, 90)
    Jump("loc_CB4")

    label("loc_C95")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CB4")
    SetChrPos(0x4, -28110, 2000, 23520, 90)

    label("loc_CB4")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D63")

    label("loc_CC2")

    SetChrPos(0x0, -19600, 0, -27950, 0)
    SetChrPos(0x1, -19600, 0, -27950, 0)
    SetChrPos(0x2, -19600, 0, -27950, 0)
    SetChrPos(0x3, -19600, 0, -27950, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D3B")
    SetChrPos(0x4, -19600, 0, -27950, 0)
    SetChrPos(0x5, -19600, 0, -27950, 0)
    Jump("loc_D5A")

    label("loc_D3B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D5A")
    SetChrPos(0x4, -19600, 0, -27950, 0)

    label("loc_D5A")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_D63")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7F")
    ClearChrFlags(0x8, 0x80)

    label("loc_D7F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D9C")
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_DD2")
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x10)
    ClearChrFlags(0x14, 0x4)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    Jump("loc_E94")

    label("loc_DD2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_DE0")
    Jump("loc_E94")

    label("loc_DE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E34")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, -16840, 0, -5150, 180)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, -16810, 0, -6100, 0)
    ClearChrFlags(0x12, 0x80)
    Jump("loc_E94")

    label("loc_E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E94")
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, 21190, 0, 1100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, 22390, 0, 1100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -17800, 0, 13370, 180)

    label("loc_E94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EA3")
    ClearScenarioFlags(0x22, 0)
    Event(0, 23)

    label("loc_EA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_EB2")
    ClearScenarioFlags(0x22, 1)
    Event(0, 8)

    label("loc_EB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EC6")
    SetScenarioFlags(0x0, 6)
    Event(0, 34)

    label("loc_EC6")

    Return()

    # Function_4_B28 end

    def Function_5_EC7(): pass

    label("Function_5_EC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_EDC")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 6)

    label("loc_EDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_EF5")
    OP_10(0x1, 0x0)
    OP_10(0x8, 0x1)
    Jump("loc_EFB")

    label("loc_EF5")

    OP_10(0x1, 0x1)
    OP_10(0x8, 0x0)

    label("loc_EFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F8F")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x190, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_F8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_FD6")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x2D, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_FD6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FEE")
    ClearMapFlags(0x2000)
    Jump("loc_FF5")

    label("loc_FEE")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_FF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_106B")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x1, 0x1)
    Jump("loc_1149")

    label("loc_106B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_10E1")
    SetMapObjFrame(0xFF, "koge2", 0x0, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x0, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x0, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x1, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x1, 0x1)
    Jump("loc_1149")

    label("loc_10E1")

    SetMapObjFrame(0xFF, "koge2", 0x1, 0x1)
    SetMapObjFrame(0xFF, "koge", 0x1, 0x1)
    SetMapObjFrame(0xFF, "syugeki01", 0x1, 0x1)
    SetMapObjFrame(0xFF, "body03", 0x1, 0x1)
    SetMapObjFrame(0xFF, "keepout", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sakutoka", 0x0, 0x1)
    SetMapObjFrame(0xFF, "atokabuse", 0x0, 0x1)

    label("loc_1149")

    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 79890, -3500, 8810, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1419")
    OP_70(0x7, 0x0)
    Jump("loc_141D")

    label("loc_1419")

    OP_70(0x7, 0x1E)

    label("loc_141D")

    SetMapObjFlags(0x4, 0x4)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1440")
    OP_70(0x8, 0x0)
    Jump("loc_145A")

    label("loc_1440")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1456")
    OP_70(0x8, 0x28)
    OP_65(0x4, 0x1)
    Jump("loc_145A")

    label("loc_1456")

    OP_66(0x4, 0x1)

    label("loc_145A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14AE")
    ClearChrFlags(0x13, 0x80)
    OP_78(0xA, 0x13)
    SetChrPos(0x13, -20340, 0, 14300, 90)
    OP_D5(0x13, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)

    label("loc_14AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_14C2")
    SetMapObjFlags(0x5, 0x4)

    label("loc_14C2")

    SoundDistance(0x7E, 0x13E3E, 0x0, 0xFFFF8972, 0x13880, 0xC350, 0x64, 0x0)
    OP_E3(0x13DE4, 0x0, 0x71E8)
    OP_E3(0x13C54, 0x0, 0xD1B0)
    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1511")
    OP_66(0x2, 0x1)
    OP_66(0x3, 0x1)

    label("loc_1511")

    Return()

    # Function_5_EC7 end

    def Function_6_1512(): pass

    label("Function_6_1512")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1612")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1D7, 1)"), scpexpr(EXPR_END)), "loc_159B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_160D")

    label("loc_159B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1D7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_160D")

    Jump("loc_1657")

    label("loc_1612")

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

    label("loc_1657")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1512 end

    def Function_7_1663(): pass

    label("Function_7_1663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1675")
    Call(0, 26)
    Return()

    label("loc_1675")

    Return()

    # Function_7_1663 end

    def Function_8_1676(): pass

    label("Function_8_1676")

    EventBegin(0x0)
    SetChrPos(0x0, 75710, -2500, 20230, 270)
    EventEnd(0x5)
    Return()

    # Function_8_1676 end

    def Function_9_168C(): pass

    label("Function_9_168C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175F")

    #C0004
    ChrTalk(
        0xFE,
        (
            "黒月の連中は、\x01",
            "未だに見つかってない。\x02",
        )
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0xFE,
        (
            "倒壊した建物の中にも\x01",
            "手がかりがなくてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "自治州内に潜伏しているのか、\x01",
            "国外へ逃亡したのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "一体どこに行って\x01",
            "しまったんだろうな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_17D2")

    label("loc_175F")


    #C0008
    ChrTalk(
        0xFE,
        (
            "黒月の連中は、\x01",
            "自治州内に潜伏しているのか、\x01",
            "国外へ逃亡したのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "一体どこに行って\x01",
            "しまったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D2")

    TalkEnd(0xFE)
    Return()

    # Function_9_168C end

    def Function_10_17D6(): pass

    label("Function_10_17D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17E8")
    Call(0, 22)
    Jump("loc_1872")

    label("loc_17E8")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "倒壊したＩＢＣビルは、\x01",
            "まさに瓦礫の山といった状態でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "あれだけ壊れてしまっていると、\x01",
            "再建するのは正直難しいだろうな……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_1872")

    Return()

    # Function_10_17D6 end

    def Function_11_1873(): pass

    label("Function_11_1873")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1885")
    Call(0, 22)
    Jump("loc_191C")

    label("loc_1885")

    TalkBegin(0xFE)

    #C0012
    ChrTalk(
        0xFE,
        (
            "ＩＢＣのご令嬢の視察も、\x01",
            "あまり成果はなかったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "銀行のシステムが\x01",
            "オルキスタワーに移せたのは、\x01",
            "不幸中の幸いというところだろう。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)

    label("loc_191C")

    Return()

    # Function_11_1873 end

    def Function_12_191D(): pass

    label("Function_12_191D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_19AF")

    #C0014
    ChrTalk(
        0xFE,
        (
            "やっとモヤが晴れて\x01",
            "空を眺められると思ったら……\x01",
            "あの樹は一体なに？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "兵器、には見えないけど……\x01",
            "あれも大統領の仕業なの？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D16")

    label("loc_19AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_19BD")
    Jump("loc_1D16")

    label("loc_19BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1B71")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ADF")

    #C0016
    ChrTalk(
        0xFE,
        (
            "流石に急な展開でビックリしたけど……\x01",
            "このくらい強く出て言わないと、\x01",
            "２大国に舐められるだけなんだよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "だったら私、断固として\x01",
            "ディーター大統領を支持するわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "アリオス長官だっているんだし……\x01",
            "もういつまでも２大国に\x01",
            "勝手なことばかりさせたくないもの！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B6C")

    label("loc_1ADF")


    #C0019
    ChrTalk(
        0xFE,
        (
            "もちろん不安もあるけど……\x01",
            "私は断固として\x01",
            "ディーター大統領を支持するわ！\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "もういつまでも２大国に\x01",
            "勝手なことばかりさせたくないもの！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B6C")

    Jump("loc_1D16")

    label("loc_1B71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_1D16")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C6A")

    #C0021
    ChrTalk(
        0xFE,
        (
            "公園近くの全壊した会社……\x01",
            "共和国政府に雇われてたって噂ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "それが判ったから帝国の雇った\x01",
            "猟兵団に襲われたとか……\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        (
            "そんな事情はどうでもいいけど……\x01",
            "とにかく、このクロスベルで\x01",
            "余計な事をしないで欲しいわよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1D16")

    label("loc_1C6A")


    #C0024
    ChrTalk(
        0xFE,
        (
            "こんな事態になっちゃったのは\x01",
            "クロスベルがいつまでも\x01",
            "従属州だから……なんだよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "だったらやっぱり、\x01",
            "私たちは独立の意志をはっきりと\x01",
            "周辺諸国に示すべきだと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D16")

    TalkEnd(0xFE)
    Return()

    # Function_12_191D end

    def Function_13_1D1A(): pass

    label("Function_13_1D1A")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D27")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_204B")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D85")
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_1D85")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DA5")
    OP_AF(0x7B)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2046")

    label("loc_1DA5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DB9")
    Jump("loc_2046")

    label("loc_1DB9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2046")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_1EFF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E99")

    #C0026
    ChrTalk(
        0xFE,
        (
            "苦難は乗り越えるために存在する……\x01",
            "そして乗り越えられない苦難はない！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        "２大国が何だ、不気味な樹がなんだ！\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "なにがあろうと、\x01",
            "私はここで麺を振舞い続けるだけだ！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1EFA")

    label("loc_1E99")


    #C0029
    ChrTalk(
        0xFE,
        "２大国が何だ、不気味な樹がなんだ！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xFE,
        (
            "なにがあろうと、\x01",
            "私はここで麺を振舞い続けるだけだ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1EFA")

    Jump("loc_2046")

    label("loc_1EFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_1F0D")
    Jump("loc_2046")

    label("loc_1F0D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1F88")

    #C0031
    ChrTalk(
        0xFE,
        "ふむ、ついにここまで来たか……\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xFE,
        (
            "私もそれなりに覚悟はしたつもりだ。\x01",
            "こうなれば徹底抗戦するだけだな！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2046")

    label("loc_1F88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2046")

    #C0033
    ChrTalk(
        0xFE,
        (
            "長年、苦楽を共にしてきた屋台が\x01",
            "壊された時は相当ショックだったが……\x01",
            "前を向かないことにはしょうがない！\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "この新しく購入した屋台と一緒に\x01",
            "また心機一転、頑張って行くつもりだ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2046")

    Jump("loc_1D27")

    label("loc_204B")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D1A end

    def Function_14_204F(): pass

    label("Function_14_204F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2106")

    #C0035
    ChrTalk(
        0xFE,
        (
            "ふう、忙しい忙しい……\x01",
            "戒厳令の影響で配達の仕事が\x01",
            "久しぶりに大忙しなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        (
            "へへっ、でもやっぱ配達屋は\x01",
            "こうでなくっちゃな。\x01",
            "生きてるって感じがすげえするよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_22EA")

    label("loc_2106")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_2114")
    Jump("loc_22EA")

    label("loc_2114")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_225F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_21EF")

    #C0037
    ChrTalk(
        0xFE,
        (
            "今朝から鉄道便が止まってるせいで、\x01",
            "配達できる数もかなり減っているんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        (
            "……というより、このまま行くと\x01",
            "クロスベルは本当にどうなるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        "仕事のことよりそっちが重要だよな……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_225A")

    label("loc_21EF")


    #C0040
    ChrTalk(
        0xFE,
        (
            "ホント、このまま行くと\x01",
            "クロスベルは本当にどうなるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xFE,
        "仕事のことよりそっちが重要だよな……\x02",
    )

    CloseMessageWindow()

    label("loc_225A")

    Jump("loc_22EA")

    label("loc_225F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_22EA")

    #C0042
    ChrTalk(
        0xFE,
        (
            "襲撃事件から早くも１週間か……\x01",
            "この辺もやっと落ち着いて来たかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xFE,
        (
            "とにかく、あんな事件は\x01",
            "もう二度と起きて欲しくないよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_22EA")

    TalkEnd(0xFE)
    Return()

    # Function_14_204F end

    def Function_15_22EE(): pass

    label("Function_15_22EE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2399")

    #C0044
    ChrTalk(
        0xFE,
        (
            "大統領の行いといい、\x01",
            "あの大樹といい、まったく\x01",
            "得体の知れんことばかりじゃな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "じゃが、この先も\x01",
            "何が起ころうとわしは\x01",
            "アミサのことを守るだけじゃ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2556")

    label("loc_2399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_23A7")
    Jump("loc_2556")

    label("loc_23A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_24DD")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_246A")

    #C0046
    ChrTalk(
        0xFE,
        (
            "何という愚かな演説じゃ……\x01",
            "世間は騙せても、\x01",
            "このワシは騙されんぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        (
            "何が独立国、何が国防軍じゃ！\x01",
            "本当に２大国の脅威から我々を\x01",
            "守り切れるとでも思っておるのか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_24D8")

    label("loc_246A")


    #C0048
    ChrTalk(
        0xFE,
        (
            "女神よ……\x01",
            "ワシのことなど、どうでもいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "じゃから、どうか孫娘を、\x01",
            "アミサのことをお救い下され……！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24D8")

    Jump("loc_2556")

    label("loc_24DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2556")

    #C0050
    ChrTalk(
        0xFE,
        (
            "あの時、少しでも逃げ遅れておったら\x01",
            "ワシもアミサも……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xFE,
        (
            "……そう考えると\x01",
            "今でも恐ろしくて仕方ないわい。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2556")

    TalkEnd(0xFE)
    Return()

    # Function_15_22EE end

    def Function_16_255A(): pass

    label("Function_16_255A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_26E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2655")

    #C0052
    ChrTalk(
        0xFE,
        (
            "まだまだこれから色んなことが\x01",
            "起こるかもしれないって、\x01",
            "おじいちゃんが言ってたの。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0xFE,
        (
            "もし前の時みたいに街が\x01",
            "襲われたりしたら怖いけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "それでも、大好きな\x01",
            "おじいちゃんと一緒なら\x01",
            "何でも耐えられる気がするんだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_26DC")

    label("loc_2655")


    #C0055
    ChrTalk(
        0xFE,
        (
            "もし前の時みたいに街が\x01",
            "襲われたりしたら怖いけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xFE,
        (
            "それでも、大好きな\x01",
            "おじいちゃんと一緒なら\x01",
            "何でも耐えられる気がするんだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26DC")

    Jump("loc_27AE")

    label("loc_26E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_26EF")
    Jump("loc_27AE")

    label("loc_26EF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2764")

    #C0057
    ChrTalk(
        0xFE,
        (
            "おじいちゃんが言うみたいに\x01",
            "本当に戦争になっちゃうのかな……\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xFE,
        "……そんなのヤダよ、怖いよ………\x02",
    )

    CloseMessageWindow()
    Jump("loc_27AE")

    label("loc_2764")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_27AE")

    #C0059
    ChrTalk(
        0xFE,
        (
            "あそこにあった東方風の建物……\x01",
            "すっかりなくなっちゃったね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_27AE")

    TalkEnd(0xFE)
    Return()

    # Function_16_255A end

    def Function_17_27B2(): pass

    label("Function_17_27B2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_289D")

    #C0060
    ChrTalk(
        0xFE,
        (
            "黒月の事務所は全壊したが、\x01",
            "１週間でこの辺りも\x01",
            "大分落ち着いたみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xFE,
        (
            "近々行われる住民投票の\x01",
            "おかげか、落ち込んでいる市民も\x01",
            "比較的少ないようだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xFE,
        (
            "何かこう、土壇場の人間の\x01",
            "力強さみたいなものを感じるぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_289D")

    TalkEnd(0xFE)
    Return()

    # Function_17_27B2 end

    def Function_18_28A1(): pass

    label("Function_18_28A1")

    TalkBegin(0xFE)

    #C0063
    ChrTalk(
        0xFE,
        (
            "何ていうか、こうして\x01",
            "新しい制服に袖を通すと\x01",
            "身も心も引き締まるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xFE,
        (
            "とにかく、これからは\x01",
            "クロスベル独立国のために\x01",
            "全力を尽くさせてもらうぜ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_28A1 end

    def Function_19_293E(): pass

    label("Function_19_293E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2A0C")

    #C0065
    ChrTalk(
        0xFE,
        "蒼い光を放つ大樹、ですか……\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "まるでリベールで起きたという\x01",
            "リベル＝アークの出現を\x01",
            "連想させる出来事ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xFE,
        (
            "あちらは古代都市だったという\x01",
            "話を聞きましたが、\x01",
            "果たして大樹とは一体……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A0C")

    TalkEnd(0xFE)
    Return()

    # Function_19_293E end

    def Function_20_2A10(): pass

    label("Function_20_2A10")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0068
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(75920, 0, 7460, 1500)
    MoveCamera(45, 24, 0, 1500)
    OP_6E(600, 1500)
    SetCameraDistance(11500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0069
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ADF")
    OP_E2(0x2)
    MiniGame(0x6, 0x1, 0x14226, 0xFFFFF63C, 0x3AA2, 0xB4, 0x13812, 0xFFFFF254, 0x226A)

    label("loc_2ADF")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_20_2A10 end

    def Function_21_2AE4(): pass

    label("Function_21_2AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B69")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　《ルピナス川・第一灯台》\x01\x01",
            "関係者以外の立ち入りを禁ずる。\x01",
            "　　　　　～クロスベル市～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Jump("loc_2C68")

    label("loc_2B69")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ジオフロントＣへの扉がある。\x01",
            "開きますか？\x02",
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
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C5D")
    Fade(500)
    OP_68(75060, 800, 20060, 0)
    MoveCamera(43, 14, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20250, 0)
    OP_0D()
    Sleep(500)
    Sound(100, 0, 70, 0)
    OP_71(0x8, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x8)
    Sleep(500)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    Sleep(500)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x0, 7)

    label("loc_2C5D")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_2C68")

    Return()

    # Function_21_2AE4 end

    def Function_22_2C69(): pass

    label("Function_22_2C69")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x109, 4330, 2000, 23330, 0)
    SetChrPos(0x102, 2900, 2000, 23240, 0)
    SetChrPos(0x101, 5350, 2000, 22780, 0)
    SetChrPos(0x103, 3280, 2000, 22060, 0)
    SetChrPos(0x104, 4150, 2000, 21040, 0)
    SetChrPos(0x105, 5950, 2000, 21600, 0)
    OP_68(4530, 3000, 23340, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15800, 0)
    LoadChrToIndex("chr/ch05500.itc", 0x1E)
    LoadChrToIndex("chr/ch28600.itc", 0x1F)
    SetChrChipByIndex(0x15, 0x1E)
    SetChrChipByIndex(0x16, 0x1F)
    SetChrSubChip(0x15, 0x0)
    SetChrSubChip(0x16, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x15, 0x4)
    SetChrFlags(0x15, 0x8000)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x16, 0x4)
    SetChrFlags(0x16, 0x8000)
    SetChrPos(0x15, 4700, 6500, 42400, 180)
    SetChrPos(0x16, 5750, 6500, 43250, 180)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02900.itp")
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    #C0072
    ChrTalk(
        0x109,
        "#10100Fお疲れ様です、皆さん。\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xA,
        (
            "おや、ノエル曹長……\x01",
            "お疲れ様です！\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0xB,
        (
            "曹長が一緒にいるということは、\x01",
            "君たちが例の特務支援課か。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xB,
        "こちらに何か仕事でも？\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00000Fいえ、そういうわけでは\x01",
            "ないんですが……\x02\x03",

            "#00003FＩＢＣビルが爆破された時、\x01",
            "現場の近くにいましたから\x01",
            "状況が気になっていまして。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x102,
        (
            "#12P#00101F……やっぱり、\x01",
            "そちらは酷い状況なんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0xA,
        (
            "ああ……まさに\x01",
            "瓦礫の山といった状態でね。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xA,
        (
            "ビルを再建するのは\x01",
            "正直難しそうだと感じたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0xB,
        (
            "今、丁度あの人が\x01",
            "視察をしているところだが……\x02",
        )
    )

    CloseMessageWindow()

    #N0081
    NpcTalk(
        0x15,
        "女性の声",
        (
            "あら、エリィに皆さん……\x01",
            "こんな所で何を\x01",
            "しているのかしら？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(700)

    def lambda_30BA():
        OP_93(0xA, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_30BA)
    Sleep(50)

    def lambda_30CA():
        OP_93(0xB, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_30CA)
    Sleep(300)
    SetChrPos(0x15, 3900, 5000, 37400, 180)
    SetChrPos(0x16, 4950, 5000, 39500, 180)
    OP_68(4640, 3200, 24370, 2000)
    MoveCamera(45, 15, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(19450, 2000)

    def lambda_312A():
        OP_95(0x15, 3900, 5000, 27400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_312A)
    Sleep(200)

    def lambda_3147():
        OP_95(0x16, 4950, 5000, 28000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3147)
    Sleep(3000)

    #C0082
    ChrTalk(
        0x102,
        "#00105F#12Pベル……！\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x103,
        "#00200F#12Pマリアベルさんでしたか。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0084
    AnonymousTalk(
        0x15,
        (
            "ええ、丁度ＩＢＣの視察に\x01",
            "来ていた所なのです。\x02\x03",

            "うふふ、よかったら\x01",
            "お話でもしましょうか？\x02",
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
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0x0, 0x0)
    SetChrPos(0x15, 1350, 2000, 22900, 90)
    SetChrPos(0x16, 700, 2000, 24100, 90)
    OP_93(0x101, 0x10E, 0x0)
    OP_93(0x102, 0x10E, 0x0)
    OP_93(0x104, 0x10E, 0x0)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x109, 0x10E, 0x0)
    OP_93(0x105, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_93(0xB, 0x10E, 0x0)
    OP_68(4570, 2700, 23870, 0)
    MoveCamera(45, 15, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16720, 0)
    Sleep(500)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    #C0085
    ChrTalk(
        0x101,
        (
            "#00000Fマリアベルさん……\x01",
            "お久しぶりですね。\x02\x03",

            "#00004F前にミシュラムに\x01",
            "招待していただいて\x01",
            "以来でしたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x15,
        (
            "#02900F#3Pそういえば\x01",
            "顔を合わせるのは\x01",
            "久しぶりでしたわね。\x02\x03",

            "#02904FＩＢＣの倒壊の現場に\x01",
            "居合わせたそうですが、\x01",
            "無事でなによりでしたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#11P#00100Fベルも……事件当時は丁度、\x01",
            "ミシュラムにいたらしいわね。\x02\x03",

            "#00104F本当に無事でよかった……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x15,
        (
            "#02900F#3Pうふふ、エリィったら……\x01",
            "そこまで私のことを\x01",
            "心配してくれていましたのね？\x02\x03",

            "#02909Fああ、これぞまさしく\x01",
            "愛の為せる業ですわ！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0089
    ChrTalk(
        0x102,
        (
            "#11P#00106Fも、もうベルったら……\x01",
            "心配するのは当たり前じゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x104,
        (
            "#00300Fしかしなんつーか……\x01",
            "ＩＢＣが破壊されたってのに\x01",
            "なんだか余裕ッスね。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#00000Fああ、そうだよな。\x01",
            "おかげでなんだか安心しました。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x15,
        (
            "#02904F#3Pふう……そう見えるかしら？\x02\x03",

            "#02901Fこれでもかなり深刻なのですが。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x105,
        (
            "#10305Fやっぱり、状況は相当悪いのかい？\x02\x03",

            "#10303F瓦礫の山になってしまったと\x01",
            "聞いたばかりだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x15,
        (
            "#02901F#3P悪いなんてものじゃないですわ！\x02\x03",

            "#02903F全く、よりにもよってＩＢＣビルを\x01",
            "爆破されてしまうなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x16,
        (
            "お嬢様の護衛に付き添ったけど\x01",
            "正直ひどい有様だったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x16,
        (
            "地下に保存されていた\x01",
            "セピスインゴットや金庫保管物の回収を\x01",
            "検討するための視察だったんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x15,
        (
            "#02906F#3P正直、今の所はお手上げですわね。\x02\x03",

            "#02901F全壊したビルの再建は困難ですし、\x01",
            "瓦礫の撤去にも時間がかかるでしょう。\x02\x03",

            "#02906F緊急措置として銀行の機能を\x01",
            "オルキスタワーに移せたのは\x01",
            "幸いでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x103,
        (
            "#00204F#2Pその話は聞きました。\x01",
            "バックアップをしていたデータを\x01",
            "速やかに復活させたとか。\x02\x03",

            "#00200F緊急時の対策は万全だったと\x01",
            "諸国からの評価も\x01",
            "高かったそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x15,
        (
            "#02902F#3Pシステム管理者として\x01",
            "当然の事をしたまでですわ。\x02\x03",

            "#02906Fまあ、当面はオルキスタワーで\x01",
            "顧客の対応をできるので\x01",
            "結果オーライにはなったのですが……\x02\x03",

            "#02901Fあの《赤い星座》とかいう\x01",
            "猟兵団には本当に腹が立ちますわ。\x02\x03",

            "#02903Fただでさえ忙しいというのに、\x01",
            "余計な仕事を増やしてくれて……\x02\x03",

            "#02901Fもし今後見かけることがあったら、\x01",
            "ありとあらゆる手を使って\x01",
            "八つ裂きにしてやりますわ！！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x102,
        (
            "#11P#00103F（うーん、怒り心頭と\x01",
            "  いった感じね……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0101
    ChrTalk(
        0x102,
        (
            "#11P#00105Fそういえば……ベル。\x02\x03",

            "あなたの大事にしていた\x01",
            "ローゼンベルク人形は\x01",
            "どうなったの？\x02\x03",

            "#00103Fまさか、瓦礫に巻き込まれて\x01",
            "しまったんじゃ……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x15, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    #C0102
    ChrTalk(
        0x15,
        (
            "#02903F#3Pうふふ、それが聞いてくださいな。\x02\x03",

            "#02903F実は、部屋の掃除を頼んだメイドに\x01",
            "緊急の際はトランクに入れて\x01",
            "持ち出すよう指示していましたの。\x02\x03",

            "#02900Fおかげであの子達は\x01",
            "誰一人として無傷でしたわ。\x02\x03",

            "#02909Fうふふ、日ごろの行いが\x01",
            "良かったのかしら。\x01",
            "不幸中の幸いというやつですわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x101,
        (
            "#00009F（はは、人形の話になると\x01",
            "  途端に嬉しそうになったな。）\x02\x03",

            "#00006F（……俺にもこれくらい\x01",
            "  優しく接してもらえると\x01",
            "  助かるんだけど。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x16, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0x16, 0x15, 500)

    #C0104
    ChrTalk(
        0x16,
        (
            "あの、マリアベルお嬢様、\x01",
            "もうそろそろお時間ですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x15,
        (
            "#02905F#3Pあら……少々話に\x01",
            "花が咲いてしまいましたわね。\x02\x03",

            "#02900Fそれではエリィ、皆さん。\x01",
            "わたくしはこれで失礼しますわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x101,
        (
            "#00005Fあ、お忙しいのに\x01",
            "引き止めてしまって\x01",
            "すみませんでした。\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x102,
        "#11P#00100Fそれじゃあまたね、ベル。\x02",
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x15,
        "#02902F#3Pふふ、ごきげんよう。\x02",
    )

    CloseMessageWindow()
    OP_93(0x15, 0x10E, 0x1F4)

    def lambda_4069():
        OP_95(0x15, -20000, 2000, 22900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4069)
    OP_68(2500, 2700, 23800, 5000)

    def lambda_4094():

        label("loc_4094")

        TurnDirection(0x16, 0x15, 500)
        Yield()
        Jump("loc_4094")

    QueueWorkItem2(0x16, 2, lambda_4094)
    Sleep(1050)
    EndChrThread(0x16, 0x2)

    def lambda_40AD():
        OP_95(0x16, -20000, 2000, 24100, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_40AD)
    Sleep(1000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_68(2500, 2700, 23800, 0)
    Sleep(500)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrChipByIndex(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0xA, 0xB4, 0x0)
    OP_93(0xB, 0xB4, 0x0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x0, 4320, 2000, 22960, 0)
    SetScenarioFlags(0x191, 3)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_22_2C69 end

    def Function_23_413F(): pass

    label("Function_23_413F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0xF, 21190, 0, 1100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, 22390, 0, 1100, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 7310, 0, 14850, 225)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    ClearChrFlags(0x17, 0x80)
    OP_78(0xB, 0x17)
    OP_49()
    ClearMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xB, 0x1000)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    ClearChrFlags(0x18, 0x80)
    OP_78(0xC, 0x18)
    OP_49()
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    SetMapObjFrame(0xC, "light", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x17, 3000, 2000, 21500, 0)
    OP_D5(0x17, 0x0, 0x0, 0x0, 0x0)
    SetChrPos(0x18, 6000, 5300, 40000, 180)
    OP_D5(0x18, 0x2710, 0x2BF20, 0x0, 0x0)
    OP_68(19250, 2500, 10000, 0)
    MoveCamera(30, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    OP_68(21000, 1000, 19800, 8000)
    MoveCamera(35, 15, 0, 8000)
    SetCameraDistance(20000, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(5000)
    Sound(459, 0, 50, 0)
    OP_6F(0x79)
    Fade(500)
    SetMapObjFrame(0xFF, "keepout", 0x0, 0x1)
    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)
    OP_68(4450, 3200, 25750, 0)
    MoveCamera(35, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(23000, 0)
    MoveCamera(40, 30, 0, 7000)
    SetCameraDistance(25000, 7000)

    def lambda_435F():
        OP_95(0xFE, 500, 2000, 25450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_435F)

    def lambda_4379():
        OP_95(0xFE, 8100, 2000, 25450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4379)
    BeginChrThread(0x17, 1, 0, 24)
    OP_0D()
    WaitChrThread(0xA, 1)
    OP_93(0xA, 0xB4, 0x1F4)
    WaitChrThread(0xB, 1)
    OP_93(0xB, 0x10E, 0x1F4)
    BeginChrThread(0x18, 1, 0, 25)
    Sleep(3500)
    Sound(459, 0, 100, 0)
    OP_6F(0x79)
    StopSound(459, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("c140D", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_413F end

    def Function_24_43DA(): pass

    label("Function_24_43DA")

    Sound(492, 0, 50, 0)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x8)
    OP_96(0xFE, 0xBB8, 0x7D0, 0x57E4, 0x3E8, 0x0)
    OP_79(0xB)
    Sleep(1000)
    Sound(493, 0, 100, 0)
    StopSound(459, 200, 40)
    OP_71(0xB, 0x3C, 0x5A, 0x0, 0x8)
    OP_79(0xB)
    OP_71(0xB, 0x79, 0xB4, 0x0, 0x20)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 3000, 2000, 23500)
    OP_9F(0x1, 3000, 2200, 25500)
    OP_9F(0x1, 3000, 6700, 45500)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_24_43DA end

    def Function_25_4465(): pass

    label("Function_25_4465")

    OP_71(0xC, 0x5B, 0x78, 0x0, 0x8)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, 6000, 6700, 45500)
    OP_9F(0x1, 6000, 2500, 27500)
    OP_9F(0x2, 0xFE, 4000, 0x6)
    OP_79(0xC)
    OP_71(0xC, 0x3C, 0x5A, 0x0, 0x8)
    OP_79(0xC)
    Return()

    # Function_25_4465 end

    def Function_26_44AD(): pass

    label("Function_26_44AD")

    EventBegin(0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu02300.itp")
    Fade(500)
    OP_68(74500, -1600, 20000, 0)
    MoveCamera(41, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17500, 0)
    SetChrPos(0x101, 73000, -2500, 19300, 90)
    SetChrPos(0x102, 73400, -2500, 20700, 90)
    SetChrPos(0x103, 72600, -2500, 18000, 45)
    SetChrPos(0x104, 72300, -2500, 21100, 90)
    SetChrPos(0x109, 71600, -2500, 18500, 90)
    SetChrPos(0x105, 71300, -2500, 20000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_4B(0x8, 0xFF)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x181, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_542E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x93, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_4657")
    OP_63(0x8, 0x0, 1700, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0109
    AnonymousTalk(
        0x8,
        (
            "なんだよ、随分と\x01",
            "遅かったじゃねーか。\x02\x03",

            "まあいっか。\x01",
            "とっとと行くとしようぜ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_46E9")

    label("loc_4657")

    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0110
    AnonymousTalk(
        0x8,
        (
            "よう、待ってたぜ。\x02\x03",

            "そんじゃあ\x01",
            "とっとと行くとしようぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_46E9")

    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    Sleep(150)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1200)

    #C0111
    ChrTalk(
        0x101,
        (
            "#6P#00011Fちょっと待て……\x01",
            "いきなり訳わかんないぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00306Fったく、相変わらず\x01",
            "マイペースな小僧だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x8,
        (
            "#02305F#11Pっと、そっか。\x01",
            "ちゃんと話してなかったな。\x02\x03",

            "#02309Fいや、実はさー。\x01",
            "ジオフロントの端末室まで\x01",
            "ボクを連れてって欲しいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x109,
        "#6P#10105Fジオフロントの端末室って……\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x105,
        "#6P#10301F前に爆破されたあの部屋かい？\x02",
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x8,
        (
            "#02303F#11Pあれはジオフロントの\x01",
            "Ｂ区画にある『第８制御端末』。\x02\x03",

            "#02300F連れてって欲しいのは\x01",
            "Ｃ区画にある『第４制御端末』さ。\x02\x03",

            "#02309Fいや～、他の制御端末だと\x01",
            "あんま自由が効かないんだよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0117
    ChrTalk(
        0x103,
        "#6P#00211Fヨナ、また凝りもせず……\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x102,
        (
            "#00106F『導力ネット基本法』は\x01",
            "既に施行されているんだし。\x02\x03",

            "#00101Fさすがに違法占拠を\x01",
            "手伝うわけにはいかないわよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#6P#00013Fていうか、話を聞いた時点で\x01",
            "止めざるを得ないんだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 1700, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0120
    ChrTalk(
        0x8,
        (
            "#02305F#11Pい、いや、一応は\x01",
            "違法じゃないんだって！\x02\x03",

            "#02303Fボクの今の立場は\x01",
            "財団のエンジニアなんだから！\x02\x03",

            "#02301Fジオフロントの制御端末の\x01",
            "管理資格も持ってるんだっての！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 500)
    Sleep(150)

    #C0121
    ChrTalk(
        0x101,
        "#5P#00001F……ティオ、どうなんだ？\x02",
    )

    CloseMessageWindow()

    def lambda_4C3B():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4C3B)
    Sleep(50)

    def lambda_4C4B():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4C4B)
    Sleep(50)

    def lambda_4C5B():
        TurnDirection(0x105, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4C5B)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x105, 0)

    #C0122
    ChrTalk(
        0x103,
        (
            "#6P#00206F管理資格は本当ですが\x01",
            "それでもグレーな感じですね。\x02\x03",

            "#00200F導力ネット基本法も\x01",
            "もう少し整備されるべきかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x102,
        "#5P#00108Fうーん……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#00301Fさすがに\x01",
            "ちょいと微妙じゃねえか？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x109,
        (
            "#6P#10106Fそうですね、グレーゾーンの\x01",
            "行為を手伝うわけにも……\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x8,
        (
            "#02311F#11Pああもう、アタマ固すぎだっての！\x02\x03",

            "#02310F《結社》だったか？\x01",
            "あの変な連中が導力ネットにも\x01",
            "色々仕掛けてたんだろ？\x02\x03",

            "今も何かされてない保証が\x01",
            "どこにあるんだっつーの？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4E2E():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4E2E)
    Sleep(50)

    def lambda_4E3E():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4E3E)
    Sleep(50)

    def lambda_4E4E():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4E4E)
    Sleep(50)

    def lambda_4E5E():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4E5E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0127
    ChrTalk(
        0x101,
        "#6P#00005Fそれは……\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x105,
        (
            "#6P#10303F……確かにそれは\x01",
            "言えてるかもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x8,
        (
            "#02303F#11P主任#4Rオッサン#も気にはしてたけど\x01",
            "忙しくて手が回ってねーし。\x02\x03",

            "動きやすいボクがわざわざ\x01",
            "援護射撃してやろーってんじゃん。\x02\x03",

            "#02301F感謝こそされ、\x01",
            "渋られるのはおかしくね？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x104,
        (
            "#00306Fったく。\x01",
            "口だけは達者な小僧だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x103,
        (
            "#6P#00203F……でも確かに\x01",
            "気になるといえば気になります。\x02\x03",

            "#00208Fあの《道化師》の少年……\x01",
            "ノバルティスという博士……\x02\x03",

            "#00201F財団を超えるネットワーク技術を\x01",
            "確かに持っているようでしたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x101,
        "#6P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0133
    ChrTalk(
        0x101,
        (
            "#6P#00001F──分かった、手伝おう。\x02\x03",

            "#00003Fただし、明らかに違法な\x01",
            "ハッキングは控えてもらうぞ？\x02\x03",

            "それと地下で何日も過ごさないで\x01",
            "部屋のベッドで寝ること。\x02\x03",

            "#00000Fそれが条件だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x8,
        (
            "#02306F#11Pおいおい、勘弁してくれよ～？\x02\x03",

            "#02302Fなんでこの天才ヨナ様が\x01",
            "そんなリアルに合わせないと──\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        "#6P#00013Fジロッ……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x8,
        "#02305F#11Pうっ……\x02",
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x102,
        (
            "#00109Fふふっ、そういうのは\x01",
            "ロイドは厳しいものね。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x103,
        (
            "#6P#00204Fまあ、そのくらいの条件は\x01",
            "呑んだ方が無難かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x8,
        (
            "#02311F#11Pあーもう、分かったよ！\x02\x03",

            "その条件でいいから\x01",
            "とっとと連れてってくれ！\x02\x03",

            "#02307F制限ガチガチの\x01",
            "オルキスタワーの端末なんて\x01",
            "もう耐えられないんだってば！\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x104,
        "#00302Fま、本音はそんなトコか。\x02",
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x109,
        (
            "#6P#10108Fうーん……\x01",
            "やっぱり少し不健全だなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#02306F#11Pう、うっせーな。\x02\x03",

            "#02300FそれでＣ区画だけど……\x01",
            "もう準備はいいのかよ？\x02\x03",

            "他のジオフロント区画と同じく、\x01",
            "魔獣とかいると思うぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x101,
        "#6P#00008Fそうだな……\x02",
    )

    CloseMessageWindow()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x181, 3)
    Jump("loc_54B5")

    label("loc_542E")


    #C0144
    ChrTalk(
        0x8,
        (
            "#02305F#11Pなに、もう準備はいいのかよ？\x02\x03",

            "#02300F他のジオフロント区画と同じく、\x01",
            "魔獣とかいると思うぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#6P#00008Fそうだな……\x02",
    )

    CloseMessageWindow()

    label("loc_54B5")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "準備はできている\x01",          # 0
            "一度準備を整えてくる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    SoundLoad(145)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5518"),
        (1, "loc_59D2"),
        (SWITCH_DEFAULT, "loc_5A62"),
    )


    label("loc_5518")


    #C0146
    ChrTalk(
        0x8,
        (
            "#02309F#11Pへへ、そんじゃ\x01",
            "とっとと降りようぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0147
    ChrTalk(
        0x109,
        "#6P#10105F降りるって……\x02",
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x104,
        "#00305Fどういうことだよ？\x02",
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x8,
        (
            "#02304F#11Pああ、Ｃ区画の入口は\x01",
            "この灯台にあるんだぜ？\x02\x03",

            "#02302F知らなかったのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        "#6P#00011Fそ、そうなのか？\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x8,
        "#02309F#11Pフフン、見てなって。\x02",
    )

    CloseMessageWindow()
    OP_68(77500, -1000, 20000, 1500)
    MoveCamera(49, 15, 0, 1500)
    SetCameraDistance(21000, 1500)
    OP_93(0x8, 0x5A, 0x1F4)

    def lambda_56EF():
        OP_95(0xFE, 76400, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_56EF)
    WaitChrThread(0x8, 1)
    OP_6F(0x79)
    Sound(100, 0, 70, 0)
    OP_71(0x8, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x8)
    Sleep(1000)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_82(0x32, 0x32, 0xBB8, 0x3E8)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0152
    ChrTalk(
        0x102,
        "#00105Fこんな所に……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        (
            "#6P#N#10302Fやれやれ。\x01",
            "趣味全開な造りだねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_93(0x8, 0x10E, 0x1F4)

    #C0154
    ChrTalk(
        0x8,
        (
            "#11P#02302F#11Pよし、そんじゃあ\x01",
            "とっとと入るとしようぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x5A, 0x1F4)
    OP_63(0x8, 0x0, 1700, 0x8, 0x9, 0xFA, 0x2)
    Sound(27, 0, 100, 0)

    def lambda_58AD():
        OP_95(0xFE, 77500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58AD)
    WaitChrThread(0x8, 1)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)

    def lambda_58E6():
        OP_95(0xFE, 80500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_58E6)
    BeginChrThread(0x101, 3, 0, 27)
    Sleep(900)
    BeginChrThread(0x102, 3, 0, 27)
    Sleep(300)
    BeginChrThread(0x103, 3, 0, 27)
    Sleep(800)
    BeginChrThread(0x104, 3, 0, 27)
    Sleep(600)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(600)
    BeginChrThread(0x105, 3, 0, 27)
    StopSound(126, 1000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0155
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ヨナが護衛対象に加わりました。\x01",
            "ＨＰが０になるとゲームオーバーになります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    AddParty(0x3D, 0xFF, 0xFF)
    SetScenarioFlags(0x181, 4)
    OP_29(0xAC, 0x1, 0x8)
    StopBGM(0xFA0)
    WaitBGM()
    EventEnd(0x5)
    NewScene("m0200", 100, 0, 0)
    IdleLoop()
    Jump("loc_5A62")

    label("loc_59D2")


    #C0156
    ChrTalk(
        0x8,
        (
            "#02303F#11Pあっそ、だったら\x01",
            "とっとと準備してきなよ。\x02\x03",

            "#02300Fここで待っててやっからさ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 72500, -2500, 20000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_24(0x91)
    EventEnd(0x5)
    Jump("loc_5A62")

    label("loc_5A62")

    Return()

    # Function_26_44AD end

    def Function_27_5A63(): pass

    label("Function_27_5A63")


    def lambda_5A68():
        OP_95(0xFE, 76000, -2500, 20000, 2000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A68)
    WaitChrThread(0xFE, 1)

    def lambda_5A86():
        OP_95(0xFE, 80500, -2500, 20000, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5A86)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_27_5A63 end

    def Function_28_5AA0(): pass

    label("Function_28_5AA0")


    def lambda_5AA5():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AA5)

    def lambda_5ABF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5ABF)
    WaitChrThread(0xFE, 1)

    def lambda_5AD4():
        OP_95(0xFE, 66900, -2500, 17100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AD4)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_28_5AA0 end

    def Function_29_5AF5(): pass

    label("Function_29_5AF5")


    def lambda_5AFA():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5AFA)

    def lambda_5B14():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B14)
    WaitChrThread(0xFE, 1)

    def lambda_5B29():
        OP_95(0xFE, 69300, -2500, 18400, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B29)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_29_5AF5 end

    def Function_30_5B4A(): pass

    label("Function_30_5B4A")


    def lambda_5B4F():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B4F)

    def lambda_5B69():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5B69)
    WaitChrThread(0xFE, 1)

    def lambda_5B7E():
        OP_95(0xFE, 68500, -2500, 17300, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5B7E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_30_5B4A end

    def Function_31_5B9F(): pass

    label("Function_31_5B9F")


    def lambda_5BA4():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BA4)

    def lambda_5BBE():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5BBE)
    WaitChrThread(0xFE, 1)

    def lambda_5BD3():
        OP_95(0xFE, 69800, -2500, 16600, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BD3)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_31_5B9F end

    def Function_32_5BF4(): pass

    label("Function_32_5BF4")


    def lambda_5BF9():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5BF9)

    def lambda_5C13():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C13)
    WaitChrThread(0xFE, 1)

    def lambda_5C28():
        OP_95(0xFE, 70600, -2500, 17700, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C28)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_32_5BF4 end

    def Function_33_5C49(): pass

    label("Function_33_5C49")


    def lambda_5C4E():
        OP_95(0xFE, 74000, -2500, 20000, 2500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C4E)

    def lambda_5C68():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_5C68)
    WaitChrThread(0xFE, 1)

    def lambda_5C7D():
        OP_95(0xFE, 68300, 0, 19100, 2500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_5C7D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0xB4, 0x1F4)
    Return()

    # Function_33_5C49 end

    def Function_34_5C9E(): pass

    label("Function_34_5C9E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51522.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    SoundLoad(145)
    SoundLoad(3520)
    SoundLoad(3521)
    SoundLoad(3522)
    SetChrPos(0x101, 79000, -2500, 20000, 270)
    SetChrPos(0x102, 79000, -2500, 20000, 270)
    SetChrPos(0x103, 79000, -2500, 20000, 270)
    SetChrPos(0x104, 79000, -2500, 20000, 270)
    SetChrPos(0x109, 79000, -2500, 20000, 270)
    SetChrPos(0x105, 79000, -2500, 20000, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xEE, 0x98, 0x84, 0x2D, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    PlayBGM("ed7514", 0)
    OP_68(79000, -1500, 20000, 0)
    MoveCamera(59, 25, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(26500, 0)
    OP_70(0x8, 0xB)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    ClearMapObjFlags(0x8, 0x10)
    OP_71(0x8, 0xB, 0x28, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    Sound(102, 0, 100, 0)
    ClearMapObjFlags(0x2, 0x10)
    OP_71(0x2, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x2)
    OP_68(69000, -1500, 17600, 7500)
    MoveCamera(59, 17, 0, 7500)
    SetCameraDistance(22500, 7500)
    BeginChrThread(0x101, 3, 0, 28)
    Sleep(700)
    BeginChrThread(0x103, 3, 0, 30)
    Sleep(700)
    BeginChrThread(0x102, 3, 0, 29)
    Sleep(700)
    BeginChrThread(0x104, 3, 0, 31)
    Sleep(700)
    BeginChrThread(0x109, 3, 0, 33)
    Sleep(700)
    BeginChrThread(0x105, 3, 0, 32)
    Sleep(1500)
    Sound(102, 0, 100, 0)
    OP_71(0x2, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x2)
    Sound(454, 0, 100, 0)
    Sound(145, 2, 100, 0)
    OP_71(0x8, 0x28, 0x47, 0x0, 0x0)
    OP_79(0x8)
    Sound(143, 0, 100, 0)
    OP_24(0x91)
    OP_6F(0x79)

    #C0157
    ChrTalk(
        0x101,
        "#5P#00008Fちょうど夕方か……\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#5P#00106F今夜は外食だし……\x01",
            "仕事もここまでかしら。\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0x109, 3)

    #C0159
    ChrTalk(
        0x109,
        "#10108F#5Pはい……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x105)
    OP_64(0x109)
    Sleep(500)
    Fade(2000)
    OP_68(79000, 3000, 10000, 0)
    MoveCamera(55, 0, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(45000, 0)
    MoveCamera(75, 0, 0, 12000)
    SetCameraDistance(40000, 12000)
    OP_6F(0x79)
    Fade(500)
    OP_68(68300, -1500, 18500, 0)
    MoveCamera(59, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    SetCameraDistance(24000, 2000)

    def lambda_6081():
        OP_96(0xFE, 0x10ACC, 0xFFFFF63C, 0x4C2C, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6081)
    WaitChrThread(0x109, 1)
    OP_6F(0x79)
    OP_C9(0x0, 0x80000000)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0160
    AnonymousTalk(
        0x109,
        (
            "#3520V#30W──皆さん。\x01",
            "色々とお世話になりました。\x02\x03",

            "#3521V短い間でしたけど……\x01",
            "本当に勉強になりました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xDC1)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_C9(0x1, 0x80000000)

    def lambda_6188():
        TurnDirection(0x101, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6188)
    Sleep(50)

    def lambda_6198():
        TurnDirection(0x102, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6198)
    Sleep(50)

    def lambda_61A8():
        TurnDirection(0x104, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_61A8)
    Sleep(50)

    def lambda_61B8():
        TurnDirection(0x103, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_61B8)
    Sleep(50)

    def lambda_61C8():
        TurnDirection(0x105, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_61C8)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    Sleep(150)

    #C0161
    ChrTalk(
        0x101,
        (
            "#12P#00004Fノエル……\x01",
            "こちらの台詞だよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x102,
        (
            "#00102F#12P……ちょうど\x01",
            "３ヶ月くらいだったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x103,
        (
            "#12P#00206Fわたしと一緒だったのは\x01",
            "２ヶ月くらいですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x104,
        (
            "#12P#00302Fなんつーか……\x01",
            "寂しくなっちまうよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x109,
        (
            "#10112F#5Pあはは……\x01",
            "あたしも名残惜しいです。\x02\x03",

            "#10108Fそれに結社や猟兵団……\x01",
            "幻獣とか蒼い花の問題も……\x02\x03",

            "#10106F全然解決していないのに\x01",
            "離れるのが申し訳なくって……\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#12P#00008Fノエル……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x105,
        (
            "#10304F#11P──まあ、立場は違っても\x01",
            "クロスベルを想う気持ちが\x01",
            "同じならいいんじゃない？\x02\x03",

            "#10302Fって、僕が言うと\x01",
            "胡散臭いかもしれないけどさ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x105, 500)
    Sleep(150)

    #C0168
    ChrTalk(
        0x109,
        "#10102F#5Pワジ君……\x02",
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x105,
        (
            "#10304F#11Pそれに一段落付いたら\x01",
            "また戻ってくればいいじゃない。\x02\x03",

            "#10302F君、一応#4R㈲　㈲#将来を\x01",
            "期待されてる身なんだよね？\x02\x03",

            "#10309F警備隊でドンパチやってるだけより\x01",
            "確かに視野は広げられるし\x01",
            "勉強にもなると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x109,
        (
            "#10101F#5Pも、もう……\x01",
            "最後まで生意気なんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x101,
        "#12P#00012Fはは……\x02",
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x104,
        (
            "#12P#00304Fま、確かにソーニャ司令も\x01",
            "そのつもりでお前を\x01",
            "出向させたんだろうしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#00102F#12Pノエルさんさえ良かったら\x01",
            "是非、また一緒に働きましょう。\x02\x03",

            "#00109Fそうでなくても休日とか\x01",
            "一緒に遊びに行ってもいいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x103,
        (
            "#12P#00204F……わたしも車の運転とか\x01",
            "教えてもらいたいです。\x02\x03",

            "#00202F年齢制限のせいで\x01",
            "今回は教われませんでしたし。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0175
    ChrTalk(
        0x109,
        (
            "#10112F#5Pあはは……グス。\x01",
            "よろこんで！\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x101,
        "#12P#00008F………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0177
    ChrTalk(
        0x101,
        (
            "#12P#00004F──ありがとう、ノエル。\x02\x03",

            "君の運転と、戦闘技術と\x01",
            "行動力には何度も助けられたけど……\x02\x03",

            "#00000F何よりもその真っ直ぐなところに\x01",
            "いつも勇気付けてもらったと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x109,
        "#10105F#5Pロイドさん……\x02",
    )

    CloseMessageWindow()
    OP_68(68400, -1400, 18800, 1800)
    MoveCamera(44, 13, 0, 1800)
    SetCameraDistance(22500, 1800)

    def lambda_681C():

        label("loc_681C")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_681C")

    QueueWorkItem2(0x109, 2, lambda_681C)

    def lambda_682E():
        OP_95(0xFE, 67300, -2500, 19200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_682E)
    WaitChrThread(0x101, 1)
    TurnDirection(0x101, 0x109, 500)
    EndChrThread(0x109, 0x2)
    OP_6F(0x79)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x10)
    SetChrFlags(0x101, 0x2)
    SetChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x109, 0x1E)
    SetChrSubChip(0x109, 0x8)
    SetChrFlags(0x109, 0x10)
    SetChrFlags(0x109, 0x2)
    SetChrFlags(0x109, 0x20)
    Sound(802, 0, 100, 0)
    Sleep(110)
    SetChrSubChip(0x101, 0x1)
    Sleep(110)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0179
    ChrTalk(
        0x101,
        (
            "#6P#00002F離れてても俺たちは仲間だ。\x02\x03",

            "警備隊で困った事があったら\x01",
            "是非、俺たちを呼んでくれ。\x02\x03",

            "#00009F俺たちもノエルの助けが必要な時は\x01",
            "遠慮なく頼らせてもらうから。\x02",
        )
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x109,
        "#11P#10114F……あ…………\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(802, 0, 100, 0)
    SetChrSubChip(0x109, 0xB)
    Sleep(130)
    SetChrSubChip(0x109, 0xC)
    Sleep(800)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0181
    ChrTalk(
        0x109,
        "#11P#10112Fはい──喜んで！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1300)

    #C0182
    ChrTalk(
        0x105,
        "#10302F#11P（フフ、さすがリーダー。）\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#12P#00211F（一瞬で良い所を\x01",
            "  持っていきましたね……）\x02",
        )
    )

    CloseMessageWindow()

    #C0184
    ChrTalk(
        0x102,
        "#11P#00113F（ま、まったくもう……）\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x104,
        (
            "#12P#00302F（ハハ、こりゃお嬢も\x01",
            "  もう少し頑張らないとなぁ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x102,
        "#11P#00112F（わ、私は別に……）\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x6)
    Sleep(50)
    SetChrSubChip(0x109, 0xE)
    Sleep(200)

    #C0187
    ChrTalk(
        0x101,
        "#5P#00005F？　どうしたんだ？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)

    #C0188
    ChrTalk(
        0x109,
        "#5P#10114F#3522V#12A#30Wって、ああっ……！\x02",
    )
    #Auto

    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x10)
    ClearChrFlags(0x101, 0x2)
    ClearChrFlags(0x101, 0x20)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    ClearChrFlags(0x109, 0x10)
    ClearChrFlags(0x109, 0x2)
    ClearChrFlags(0x109, 0x20)
    OP_63(0x109, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_6C02():
        OP_93(0xFE, 0xB4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_6C02)

    def lambda_6C0F():

        label("loc_6C0F")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6C0F")

    QueueWorkItem2(0x102, 2, lambda_6C0F)

    def lambda_6C21():

        label("loc_6C21")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6C21")

    QueueWorkItem2(0x105, 2, lambda_6C21)

    def lambda_6C33():

        label("loc_6C33")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6C33")

    QueueWorkItem2(0x104, 2, lambda_6C33)
    OP_68(69100, -1400, 18800, 650)
    SetCameraDistance(23000, 650)

    def lambda_6C5F():
        OP_96(0xFE, 0x10D88, 0xFFFFF63C, 0x4DBC, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_6C5F)
    WaitChrThread(0x109, 1)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    OP_6F(0x79)

    #C0189
    ChrTalk(
        0x109,
        (
            "#10112F#5Pす、すみません。\x01",
            "別にそういうわけじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x104,
        (
            "#12P#00309Fんー、そういうわけって\x01",
            "どういうわけかねぇ？\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x105,
        (
            "#10309Fフフ、そういう意味でも\x01",
            "支援課に戻ってきてもらって\x01",
            "続きが見たい気がするね。\x02",
        )
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x109,
        "#10114F#5Pせ、先輩、ワジ君！\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        "#11P#00113Fはぁ……まったくもう。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#6P#00011F？？？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(69290, -1400, 18560, 1800)

    def lambda_6DCA():

        label("loc_6DCA")

        TurnDirection(0xFE, 0x109, 500)
        Yield()
        Jump("loc_6DCA")

    QueueWorkItem2(0x101, 2, lambda_6DCA)

    def lambda_6DDC():
        OP_96(0xFE, 0x10810, 0xFFFFF63C, 0x4394, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_6DDC)
    WaitChrThread(0x101, 1)
    EndChrThread(0x101, 0x2)
    OP_6F(0x79)

    #C0195
    ChrTalk(
        0x101,
        "#6P#00008F（……ティオ、何の話だ？）\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x66), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_6E9C")

    #C0196
    ChrTalk(
        0x103,
        (
            "#12P#00211F（……さあ？\x01",
            "  自分で考えてみてください。）\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#6P#00006F（なんか怒ってるし……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_6F06")

    label("loc_6E9C")


    #C0198
    ChrTalk(
        0x103,
        (
            "#12P#00204F（まあ、ロイドさんも\x01",
            "  まだまだ未熟という事かと。）\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x101,
        "#6P#00006F（ダメ出しされた……）\x02",
    )

    CloseMessageWindow()

    label("loc_6F06")

    SetCameraDistance(23500, 2000)
    StopSound(126, 1000, 100)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    SetChrName("")

    #A0200
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "その夜、ロイドたちは中央広場のレストランで\x01",
            "ノエルの送別会を開いた。\x02\x03",

            "セルゲイやキーアはもちろん、\x01",
            "ツァイトも特別に入店させてもらい、\x01",
            "楽しくも名残惜しい夜は過ぎて行き……\x02\x03",

            "そして翌朝──荷物をまとめたノエルは\x01",
            "特務支援課のビルを去って行った。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_32(0xFF, 0xFE, 0x0)
    RemoveParty(0x8, 0xFF)
    RemoveParty(0x4, 0xFF)
    OP_BC(0x8)
    OP_BC(0x4)
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x91)
    SetScenarioFlags(0x22, 2)
    NewScene("m0209", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_5C9E end

    def Function_35_704D(): pass

    label("Function_35_704D")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　　 ～　売り地　～ 　　\x01",
            "クロスベル市・都市整備課\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_35_704D end

    def Function_36_70B7(): pass

    label("Function_36_70B7")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "　 ＜立入禁止区域＞\x01",
            "危険ですので敷地内には\x01",
            "立ち入らないで下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_36_70B7 end

    SaveToFile()

Try(main)
