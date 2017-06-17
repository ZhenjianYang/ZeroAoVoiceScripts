from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1000.bin",                # FileName
        "c1000",                    # MapName
        "c1000",                    # Location
        0x0010,                     # MapIndex
        "ed7150",
        0x00002000,                 # Flags
        ("c1000", "c1000_1", "c1000_2", "", "", ""),   # include
        0x1E,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 16, 0, 8, 0, 9],
    )

    BuildStringList((
        "c1000",                  # 0
        "クロンク",               # 1
        "ディンズ",               # 2
        "リリィ",                 # 3
        "マルテ",                 # 4
        "ダナン",                 # 5
        "アンネ",                 # 6
        "ルノー爺さん",           # 7
        "ロイ",                   # 8
        "メイリン",               # 9
        "スーザン",               # 10
        "ジレ",                   # 11
        "クータ",                 # 12
        "モルス老人",             # 13
        "捜査官",                 # 14
        "車",                     # 15
        "暴走車",                 # 16
        "パトカー",               # 17
        "セルダン支部長",         # 18
        "コパン",                 # 19
        "ペーター",               # 20
        "シャーリィ",             # 21
        "国防軍兵士",             # 22
        "国防軍兵士",             # 23
        "市民１",                 # 24
        "市民２",                 # 25
        "市民３",                 # 26
        "市民４",                 # 27
        "市民５",                 # 28
        "市民６",                 # 29
        "市民７",                 # 30
        "警官",                   # 31
        "警官",                   # 32
        "警官",                   # 33
        "警官",                   # 34
        "パオラ婆さん",           # 35
        "bc1000",                 # 36
        "中央広場",               # 37
        "西通り",                 # 38
        "行政区",                 # 39
        "住宅街",                 # 40
        "歓楽街",                 # 41
        "東通り",                 # 42
        "旧市街",                 # 43
        "港湾区",                 # 44
        "ＩＢＣ",                 # 45
        "駅前通り",               # 46
        "裏通り",                 # 47
        "ウルスラ間道",           # 48
        "東クロスベル街道",       # 49
        "西クロスベル街道",       # 50
        "マインツ山道",           # 51
        "オルキスタワー",         # 52
    ))

    ATBonus("ATBonus_950", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_C605", 8,   8,   8,   8,   11,  11,  11)

    MonsterBattlePostion("MonsterBattlePostion_9A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_9A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_9A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_9AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_9B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_9BC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_A00", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_A04", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_A08", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_A0C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_A10", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_A14", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_A18", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_A1C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_980", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_984", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_988", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_98C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_990", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_994", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_998", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_99C", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_A20", 0x0000, 93, 6, 60, 4, 1, 25, 0, "bc1000", "Sepith_C605", 60, 30, 10, 0,
        (
            ("ms85100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_9A0", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            ("ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_980", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            ("ms85100.dat", "ms85100.dat", "ms85100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_9A0", "MonsterBattlePostion_A00", "ed7450", "ed7453", "ATBonus_950"),
            (),
        )
    )

    AddCharChip((
        "chr/ch23500.itc",                   # 00
        "chr/ch20400.itc",                   # 01
        "chr/ch24800.itc",                   # 02
        "chr/ch24900.itc",                   # 03
        "chr/ch21100.itc",                   # 04
        "chr/ch24000.itc",                   # 05
        "chr/ch21200.itc",                   # 06
        "chr/ch21500.itc",                   # 07
        "chr/ch10300.itc",                   # 08
        "chr/ch26200.itc",                   # 09
        "chr/ch21400.itc",                   # 0A
        "chr/ch20800.itc",                   # 0B
        "chr/ch49800.itc",                   # 0C
        "chr/ch49600.itc",                   # 0D
        "chr/ch49700.itc",                   # 0E
        "chr/ch49900.itc",                   # 0F
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "chr/ch27600.itc",                   # 12
        "chr/ch24200.itc",                   # 13
    ))

    DeclNpc(-24409,  -3000,   5239,    180,  261,  0x0, 0,   1,   0,   0,   0,   2,   0,   255,  0)
    DeclNpc(-13039,  -3000,   -810,    225,  261,  0x0, 0,   2,   0,   0,   0,   2,   1,   255,  0)
    DeclNpc(-16500,  -3000,   2920,    45,   261,  0x0, 0,   3,   0,   0,   7,   2,   2,   255,  0)
    DeclNpc(-4559,   -3000,   -8949,   180,  261,  0x0, 0,   0,   0,   0,   0,   2,   3,   255,  0)
    DeclNpc(-5559,   -3000,   -8949,   180,  389,  0x0, 0,   19,  0,   0,   0,   2,   15,  255,  0)
    DeclNpc(26200,   -300,    -1049,   270,  261,  0x0, 0,   4,   0,   0,   1,   2,   7,   255,  0)
    DeclNpc(-40490,  -300,    15850,   90,   261,  0x0, 0,   5,   0,   0,   6,   2,   8,   255,  0)
    DeclNpc(-18200,  -300,    18139,   270,  261,  0x0, 0,   6,   0,   0,   0,   2,   9,   255,  0)
    DeclNpc(-22280,  -300,    18370,   225,  261,  0x0, 0,   7,   0,   0,   2,   2,   10,  255,  0)
    DeclNpc(-8470,   -3000,   -7349,   45,   261,  0x0, 0,   8,   0,   0,   0,   2,   12,  255,  0)
    DeclNpc(-7420,   -3000,   -8600,   45,   261,  0x0, 0,   9,   0,   0,   0,   2,   13,  255,  0)
    DeclNpc(-15939,  -3000,   -600,    45,   261,  0x0, 0,   10,  0,   0,   3,   2,   14,  255,  0)
    DeclNpc(-18200,  -300,    18139,   270,  389,  0x0, 0,   11,  0,   0,   0,   2,   11,  255,  0)
    DeclNpc(-3049,   -3000,   -13779,  315,  385,  0x0, 0,   18,  0,   0,   0,   2,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-17640,  14650,   -310,    0x10100E1,    "BattleInfo_A20", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(530,     -13160,  -3000,   0x101013B,    "BattleInfo_A20", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 12,  -26.8700008392334,     4.059999942779541,     -4.0,                  20.25,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   8.956666946411133,     -1.3533333539962769,   0.800000011920929,     1.0])
    DeclEvent(0x0000, 0, 13,  -15.1899995803833,     -5.800000190734863,    -6.5,                  37.515625,             [0.20203045010566711,  0.20203058421611786,   -0.0,                  0.0,                   -0.20203058421611786,  0.20203045010566711,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   1.8970650434494019,    4.240621089935303,     1.3000000715255737,    1.0])

    DeclActor(-30000,  -5500,   4000,    1200,    -30000,  -4500,   4000,    0x007C, 0,  10, 0x0000)
    DeclActor(-23010,  -14900,  -4830,   1200,    -23010,  -13900,  -4830,   0x007C, 0,  11, 0x0000)
    DeclActor(-190,    340,     6410,    2000,    -190,    1540,    6410,    0x007C, 0,  35, 0x0000)
    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  17, 0x0000)
    DeclActor(-15920,  240,     24020,   2000,    -15920,  1540,    24020,   0x007C, 0,  36, 0x0000)
    DeclActor(17360,   -300,    4630,    1200,    17530,   1500,    5120,    0x007C, 0,  37, 0x0000)
    DeclActor(12360,   250,     5680,    1200,    12360,   1540,    5680,    0x007C, 0,  41, 0x0000)
    DeclActor(-33350,  -5500,   9380,    1200,    -33350,  -4000,   9380,    0x007C, 0,  14, 0x0000)

    PlaceName(-111.26000213623047, 0.0, 15.239999771118164, 0x0000, 0x0000, "中央広場")
    PlaceName(-186.8800048828125, 0.0, 20.40999984741211, 0x0000, 0x0000, "西通り")
    PlaceName(-80.20999908447266, 0.0, 117.58999633789062, 0x0000, 0x0000, "行政区")
    PlaceName(-257.0299987792969, 0.0, 106.08999633789062, 0x0000, 0x0000, "住宅街")
    PlaceName(-173.0800018310547, 0.0, 96.88999938964844, 0x0000, 0x0000, "歓楽街")
    PlaceName(-17.829999923706055, 0.0, -11.210000038146973, 0x0000, 0x0000, "東通り")
    PlaceName(23.0, 0.0, -74.45999908447266, 0x0000, 0x0000, "旧市街")
    PlaceName(14.380000114440918, 0.0, 64.69000244140625, 0x0000, 0x0000, "港湾区")
    PlaceName(-15.529999732971191, 0.0, 172.7899932861328, 0x0000, 0x0000, "ＩＢＣ")
    PlaceName(-98.33000183105469, 0.0, -64.11000061035156, 0x0000, 0x0000, "駅前通り")
    PlaceName(-152.3800048828125, 0.0, 55.4900016784668, 0x0000, 0x0000, "裏通り")
    PlaceName(-101.77999877929688, 0.0, -99.76000213623047, 0x0000, 0x0000, "ウルスラ間道")
    PlaceName(44.279998779296875, 0.0, 4.889999866485596, 0x0000, 0x0000, "東クロスベル街道")
    PlaceName(-245.52999877929688, 0.0, 18.690000534057617, 0x0000, 0x0000, "西クロスベル街道")
    PlaceName(-238.6300048828125, 0.0, 133.69000244140625, 0x0000, 0x0000, "マインツ山道")
    PlaceName(-88.0, 0.0, 269.0, 0x0000, 0x0000, "オルキスタワー")
    PlaceName(-136.55999755859375, 0.0, -0.8600000143051147, 0x0000, 0x0051, "")
    PlaceName(-74.75, 0.0, 29.040000915527344, 0x0000, 0x0054, "")
    PlaceName(-108.38999938964844, 0.0, -10.0600004196167, 0x0000, 0x0057, "")
    PlaceName(-137.42999267578125, 0.0, 32.4900016784668, 0x0000, 0x0053, "")
    PlaceName(-113.8499984741211, 0.0, 60.09000015258789, 0x0000, 0x0053, "")
    PlaceName(-172.2100067138672, 0.0, 26.739999771118164, 0x0000, 0x0053, "")
    PlaceName(-183.42999267578125, 0.0, 50.88999938964844, 0x0000, 0x0053, "")
    PlaceName(-155.8300018310547, 0.0, 87.69000244140625, 0x0000, 0x0052, "")
    PlaceName(-150.36000061035156, 0.0, 72.73999786376953, 0x0000, 0x0053, "")
    PlaceName(-140.3000030517578, 0.0, 62.959999084472656, 0x0000, 0x0053, "")
    PlaceName(-107.52999877929688, 0.0, 144.61000061035156, 0x0000, 0x0051, "")
    PlaceName(21.280000686645508, 0.0, -11.210000038146973, 0x0000, 0x0052, "")
    PlaceName(1.7300000190734863, 0.0, -115.29000091552734, 0x0000, 0x0053, "")
    PlaceName(-13.229999542236328, 0.0, -94.01000213623047, 0x0000, 0x0053, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1

    ScpFunction((
        "Function_0_B94",          # 00, 0
        "Function_1_C44",          # 01, 1
        "Function_2_CDD",          # 02, 2
        "Function_3_D08",          # 03, 3
        "Function_4_D7D",          # 04, 4
        "Function_5_E1A",          # 05, 5
        "Function_6_E67",          # 06, 6
        "Function_7_F28",          # 07, 7
        "Function_8_F75",          # 08, 8
        "Function_9_169B",         # 09, 9
        "Function_10_1C33",        # 0A, 10
        "Function_11_1D84",        # 0B, 11
        "Function_12_1ED5",        # 0C, 12
        "Function_13_20FC",        # 0D, 13
        "Function_14_2356",        # 0E, 14
        "Function_15_2B9E",        # 0F, 15
        "Function_16_2C89",        # 10, 16
        "Function_17_2EA9",        # 11, 17
        "Function_18_2EAA",        # 12, 18
        "Function_19_32EF",        # 13, 19
        "Function_20_34E2",        # 14, 20
        "Function_21_3849",        # 15, 21
        "Function_22_38ED",        # 16, 22
        "Function_23_3DAA",        # 17, 23
        "Function_24_4129",        # 18, 24
        "Function_25_4673",        # 19, 25
        "Function_26_49C9",        # 1A, 26
        "Function_27_4E77",        # 1B, 27
        "Function_28_52E5",        # 1C, 28
        "Function_29_5B4D",        # 1D, 29
        "Function_30_6E13",        # 1E, 30
        "Function_31_6E2F",        # 1F, 31
        "Function_32_6E4B",        # 20, 32
        "Function_33_6E67",        # 21, 33
        "Function_34_6E83",        # 22, 34
        "Function_35_6E9F",        # 23, 35
        "Function_36_759B",        # 24, 36
        "Function_37_7706",        # 25, 37
        "Function_38_9AAA",        # 26, 38
        "Function_39_9D0D",        # 27, 39
        "Function_40_9EE0",        # 28, 40
        "Function_41_B57D",        # 29, 41
        "Function_42_B6EC",        # 2A, 42
        "Function_43_C0FB",        # 2B, 43
        "Function_44_C132",        # 2C, 44
        "Function_45_C18D",        # 2D, 45
        "Function_46_C258",        # 2E, 46
        "Function_47_C50E",        # 2F, 47
    ))


    def Function_0_B94(): pass

    label("Function_0_B94")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_BCC"),
        (1, "loc_BD8"),
        (2, "loc_BE4"),
        (3, "loc_BF0"),
        (4, "loc_BFC"),
        (5, "loc_C08"),
        (6, "loc_C14"),
        (SWITCH_DEFAULT, "loc_C20"),
    )


    label("loc_BCC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BD8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BE4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BF0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_BFC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C08")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C14")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C20")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C2C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C43")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_C2C")

    label("loc_C43")

    Return()

    # Function_0_B94 end

    def Function_1_C44(): pass

    label("Function_1_C44")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CDC")
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -40270, -300, 12170, 2000, 0x0)
    Sleep(2500)
    OP_95(0xFE, -15670, -300, 12310, 2000, 0x0)
    OP_95(0xFE, -1180, -300, -1100, 2000, 0x0)
    OP_95(0xFE, 26200, -300, -1050, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    Jump("Function_1_C44")

    label("loc_CDC")

    Return()

    # Function_1_C44 end

    def Function_2_CDD(): pass

    label("Function_2_CDD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D07")
    OP_94(0xFE, 0xFFFFB000, 0x4ECA, 0xFFFFA8EE, 0x3F01, 0x3E8)
    Sleep(300)
    Jump("Function_2_CDD")

    label("loc_D07")

    Return()

    # Function_2_CDD end

    def Function_3_D08(): pass

    label("Function_3_D08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D7C")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_3_D08")

    label("loc_D7C")

    Return()

    # Function_3_D08 end

    def Function_4_D7D(): pass

    label("Function_4_D7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E19")
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -22610, -3000, 3390, 1000, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -19740, -3000, 3190, 1000, 0x0)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_95(0xFE, -8470, -3000, -7350, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    Jump("Function_4_D7D")

    label("loc_E19")

    Return()

    # Function_4_D7D end

    def Function_5_E1A(): pass

    label("Function_5_E1A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E66")
    OP_95(0xFE, -15940, -3000, -600, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    OP_95(0xFE, -9950, -3000, -6670, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(1500)
    Jump("Function_5_E1A")

    label("loc_E66")

    Return()

    # Function_5_E1A end

    def Function_6_E67(): pass

    label("Function_6_E67")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F27")
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, 26030, -300, 2230, 2000, 0x0)
    Sleep(200)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(300)
    OP_95(0xFE, -1180, -300, 2190, 2000, 0x0)
    OP_95(0xFE, -13780, -300, 14160, 2000, 0x0)
    OP_95(0xFE, -16760, -300, 15130, 2000, 0x0)
    OP_95(0xFE, -40490, -300, 15850, 2000, 0x0)
    Sleep(2400)
    Jump("Function_6_E67")

    label("loc_F27")

    Return()

    # Function_6_E67 end

    def Function_7_F28(): pass

    label("Function_7_F28")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F74")
    OP_95(0xFE, -15130, -3000, 1420, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    OP_95(0xFE, -16500, -3000, 2920, 1000, 0x0)
    OP_93(0xFE, 0x2D, 0x12C)
    Sleep(3000)
    Jump("Function_7_F28")

    label("loc_F74")

    Return()

    # Function_7_F28 end

    def Function_8_F75(): pass

    label("Function_8_F75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1195")
    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1040")
    SetChrPos(0x0, -20760, -310, 33300, 180)
    SetChrPos(0x1, -20760, -310, 33300, 180)
    SetChrPos(0x2, -20760, -310, 33300, 180)
    SetChrPos(0x3, -20760, -310, 33300, 180)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1013")
    SetChrPos(0x4, -20760, -310, 33300, 180)
    SetChrPos(0x5, -20760, -310, 33300, 180)
    Jump("loc_1032")

    label("loc_1013")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1032")
    SetChrPos(0x4, -20760, -310, 33300, 180)

    label("loc_1032")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1195")

    label("loc_1040")

    Jc((scpexpr(EXPR_23, 0x7), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F4")
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    SetChrPos(0x1, 1910, -3000, -35980, 0)
    SetChrPos(0x2, 1910, -3000, -35980, 0)
    SetChrPos(0x3, 1910, -3000, -35980, 0)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10C7")
    SetChrPos(0x4, 1910, -3000, -35980, 0)
    SetChrPos(0x5, 1910, -3000, -35980, 0)
    Jump("loc_10E6")

    label("loc_10C7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E6")
    SetChrPos(0x4, 1910, -3000, -35980, 0)

    label("loc_10E6")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1195")

    label("loc_10F4")

    SetChrPos(0x0, -29790, -330, 13830, 90)
    SetChrPos(0x1, -29790, -330, 13830, 90)
    SetChrPos(0x2, -29790, -330, 13830, 90)
    SetChrPos(0x3, -29790, -330, 13830, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_116D")
    SetChrPos(0x4, -29790, -330, 13830, 90)
    SetChrPos(0x5, -29790, -330, 13830, 90)
    Jump("loc_118C")

    label("loc_116D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_118C")
    SetChrPos(0x4, -29790, -330, 13830, 90)

    label("loc_118C")

    OP_50(0x0, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1195")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_11B1")
    ClearChrFlags(0xC, 0x80)
    Jump("loc_154F")

    label("loc_11B1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_END)), "loc_11F6")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_154F")

    label("loc_11F6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_1237")
    SetChrPos(0x10, -22760, -3000, 5010, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -21950, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_1237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_124F")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x12, 0x80)
    Jump("loc_154F")

    label("loc_124F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_1290")
    SetChrPos(0x10, -14890, -300, 9170, 225)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_1290")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_12C3")
    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xE)
    SetChrChipByIndex(0xD, 0xC)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x13, 0xF)
    BeginChrThread(0x13, 0, 0, 4)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_12C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_12F2")
    SetChrPos(0xF, -23170, -3000, 5100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x14, 0x80)
    Jump("loc_154F")

    label("loc_12F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_133D")
    SetChrPos(0x10, -19280, -320, 18240, 90)
    BeginChrThread(0x10, 0, 0, 0)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x10, 0x10)
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x12, 0x80)
    Jump("loc_154F")

    label("loc_133D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_1383")
    SetChrPos(0x10, -14890, -300, 9170, 225)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrPos(0xF, -26620, -3000, 5100, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x13, 0x80)
    Jump("loc_154F")

    label("loc_1383")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_13C3")
    SetChrPos(0xF, -23170, -3000, 5100, 270)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x8, -24410, -3000, 5240, 90)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_154F")

    label("loc_13C3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_1413")
    SetChrPos(0xF, -22760, -3000, 5010, 0)
    BeginChrThread(0xF, 0, 0, 0)
    SetChrPos(0x10, -21950, -3000, 5010, 0)
    BeginChrThread(0x10, 0, 0, 0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jump("loc_154F")

    label("loc_1413")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_1489")
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x15, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1484")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1484")
    SetChrFlags(0x8, 0x10)

    label("loc_1484")

    Jump("loc_154F")

    label("loc_1489")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_14FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 3)), scpexpr(EXPR_END)), "loc_14AA")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    Jump("loc_14DC")

    label("loc_14AA")

    SetChrChipByIndex(0xF, 0xD)
    SetChrChipByIndex(0x10, 0xE)
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    SetChrFlags(0x10, 0x10)

    label("loc_14DC")

    SetChrChipByIndex(0xD, 0xC)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrChipByIndex(0x13, 0xF)
    BeginChrThread(0x13, 0, 0, 4)
    SetChrFlags(0x11, 0x80)
    Jump("loc_154F")

    label("loc_14FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_154F")
    SetChrFlags(0x11, 0x80)
    SetChrPos(0x10, -17150, -300, 16600, 315)
    BeginChrThread(0x10, 0, 0, 0)
    TurnDirection(0x10, 0xF, 0)
    TurnDirection(0xF, 0x10, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x130, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_154F")
    SetChrFlags(0x10, 0x10)

    label("loc_154F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_1563")
    ClearScenarioFlags(0x22, 0)
    Event(0, 18)
    Jump("loc_162A")

    label("loc_1563")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_1577")
    ClearScenarioFlags(0x22, 1)
    Event(0, 19)
    Jump("loc_162A")

    label("loc_1577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_158B")
    ClearScenarioFlags(0x22, 2)
    Event(0, 20)
    Jump("loc_162A")

    label("loc_158B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_159F")
    ClearScenarioFlags(0x22, 3)
    Event(0, 23)
    Jump("loc_162A")

    label("loc_159F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 4)), scpexpr(EXPR_END)), "loc_15B3")
    ClearScenarioFlags(0x22, 4)
    Event(0, 24)
    Jump("loc_162A")

    label("loc_15B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 5)), scpexpr(EXPR_END)), "loc_15C7")
    ClearScenarioFlags(0x22, 5)
    Event(0, 27)
    Jump("loc_162A")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 6)), scpexpr(EXPR_END)), "loc_15E0")
    ClearScenarioFlags(0x22, 6)
    SetMapFlags(0x10000000)
    Event(0, 25)
    Jump("loc_162A")

    label("loc_15E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 7)), scpexpr(EXPR_END)), "loc_15F4")
    ClearScenarioFlags(0x22, 7)
    Event(0, 42)
    Jump("loc_162A")

    label("loc_15F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 0)), scpexpr(EXPR_END)), "loc_161B")
    ClearScenarioFlags(0x23, 0)
    OP_1B(0x2, 0x0, 0x2C)
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    Jump("loc_162A")

    label("loc_161B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x23, 1)), scpexpr(EXPR_END)), "loc_162A")
    ClearScenarioFlags(0x23, 1)
    Event(0, 16)

    label("loc_162A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 6)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1655")
    SetMapFlags(0x10000000)
    Event(1, 0)

    label("loc_1655")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_EXEC_OP, "OP_2A(0x74, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_166D")
    Event(0, 22)

    label("loc_166D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_169A")
    SetMapFlags(0x10000000)
    Event(0, 28)

    label("loc_169A")

    Return()

    # Function_8_F75 end

    def Function_9_169B(): pass

    label("Function_9_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1744")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xF, 0x64, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    Sound(128, 1, 100, 0)

    label("loc_1744")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17D8")
    LoadEffect(0x9, "map/mpmoya.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0x78, 0x96, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xFF, 0xD, 0x5F, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_17D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_181F")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)

    label("loc_181F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1837")
    ClearMapFlags(0x2000)
    Jump("loc_183E")

    label("loc_1837")

    SetMapFlags(0x2000)
    OP_E2(0x1)

    label("loc_183E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_185A")
    SetMapObjFrame(0xFF, "turi00", 0x0, 0x1)
    Jump("loc_1868")

    label("loc_185A")

    SetMapObjFrame(0xFF, "turi01", 0x0, 0x1)

    label("loc_1868")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1881")
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_1887")

    label("loc_1881")

    SetMapObjFlags(0x9, 0x4)

    label("loc_1887")

    ClearMapObjFlags(0x5, 0x10)
    OP_70(0x5, 0x1E)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18C8")
    OP_1B(0x8, 0x0, 0x2D)
    OP_66(0x4, 0x1)
    ClearMapObjFlags(0x2, 0x10)
    OP_70(0x2, 0x0)

    label("loc_18C8")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_18FB")
    OP_66(0x6, 0x1)
    ClearMapObjFlags(0x3, 0x10)
    OP_70(0x3, 0x0)

    label("loc_18FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1920")
    OP_1B(0x2, 0x0, 0x2C)

    label("loc_1920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_192E")
    OP_1B(0x2, 0x0, 0x2F)

    label("loc_192E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_193D")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_193D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1950")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1963")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1976")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1976")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1989")
    OP_1B(0x8, 0x0, 0x2E)

    label("loc_1989")

    OP_52(0x2B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2C, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B3E")
    OP_70(0x6, 0x0)
    Jump("loc_1B42")

    label("loc_1B3E")

    OP_70(0x6, 0x1E)

    label("loc_1B42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B55")
    OP_70(0x7, 0x0)
    Jump("loc_1B59")

    label("loc_1B55")

    OP_70(0x7, 0x1E)

    label("loc_1B59")

    OP_65(0x2, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B7F")
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)
    OP_66(0x2, 0x1)
    Jump("loc_1BAD")

    label("loc_1B7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BAD")
    OP_66(0x2, 0x1)
    ClearMapObjFlags(0x0, 0x10)
    OP_70(0x0, 0x0)

    label("loc_1BAD")

    OP_65(0x3, 0x1)
    OP_65(0x7, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BCB")
    OP_66(0x7, 0x1)

    label("loc_1BCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BDC")
    OP_66(0x7, 0x1)

    label("loc_1BDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1BFB")
    OP_10(0x2, 0x0)
    OP_10(0xB, 0x1)
    OP_10(0x1, 0x0)
    OP_10(0xC, 0x1)
    Jump("loc_1C07")

    label("loc_1BFB")

    OP_10(0x2, 0x1)
    OP_10(0xB, 0x0)
    OP_10(0x1, 0x1)
    OP_10(0xC, 0x0)

    label("loc_1C07")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C32")
    ModifyEventFlags(1, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1C32")

    Return()

    # Function_9_169B end

    def Function_10_1C33(): pass

    label("Function_10_1C33")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D33")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_1CBC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1D2E")

    label("loc_1CBC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D2E")

    Jump("loc_1D78")

    label("loc_1D33")

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

    label("loc_1D78")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1C33 end

    def Function_11_1D84(): pass

    label("Function_11_1D84")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EB, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E84")
    Sound(14, 0, 100, 0)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x98, 1)"), scpexpr(EXPR_END)), "loc_1E0D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EB, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1E7F")

    label("loc_1E0D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x98),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E7F")

    Jump("loc_1EC9")

    label("loc_1E84")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_1EC9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_1D84 end

    def Function_12_1ED5(): pass

    label("Function_12_1ED5")

    EventBegin(0x0)
    Fade(500)
    OP_68(-25670, -1400, 3480, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_E2(0x3)
    SetChrPos(0x101, -24530, -3000, 3820, 270)
    SetChrPos(0x102, -24620, -3000, 4610, 270)
    SetChrPos(0x103, -26670, -3000, 3480, 270)
    SetChrPos(0x104, -23080, -3000, 4470, 270)
    SetChrPos(0xF4, -23280, -3000, 3480, 270)
    SetChrPos(0xF5, -23030, -3000, 2550, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0007
    ChrTalk(
        0x103,
        "#11P#00205F……………………\x02",
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#00005F……ティオ？\x02",
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x102,
        "#11P#00105F気になることでもあった？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_68(-32299, -1400, 3240, 3000)
    OP_6F(0x79)

    #C0010
    ChrTalk(
        0x103,
        (
            "#11P#00200Fこちらの方角からちょっとした\x01",
            "気配を感じたのですが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0011
    ChrTalk(
        0x103,
        (
            "#6P#00203F……すみません、おそらく\x01",
            "気にするほどの事ではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x101,
        "#00005Fそうか……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0x1BF, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -24530, -3000, 3820, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_12_1ED5 end

    def Function_13_20FC(): pass

    label("Function_13_20FC")

    EventBegin(0x0)
    Fade(500)
    OP_68(-16840, -3900, -5030, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_E2(0x3)
    SetChrPos(0x101, -15840, -5500, -6030, 315)
    SetChrPos(0x102, -15430, -5500, -4830, 270)
    SetChrPos(0x103, -16840, -5500, -5030, 315)
    SetChrPos(0x104, -14440, -5500, -5410, 270)
    SetChrPos(0xF4, -14440, -5500, -6610, 315)
    SetChrPos(0xF5, -14850, -5500, -7820, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0013
    ChrTalk(
        0x103,
        "#11P#00205F……………………\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x101,
        "#00005F……ティオ？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#00105F気になることでもあった？\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)
    OP_68(-30570, -3900, 4350, 5000)
    OP_6F(0x79)
    Sleep(2000)
    Fade(500)
    OP_68(-16840, -3900, -5030, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_0D()

    #C0016
    ChrTalk(
        0x103,
        (
            "#11P#00200Fこちらの方角からちょっとした\x01",
            "気配を感じたのですが……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)

    #C0017
    ChrTalk(
        0x103,
        (
            "#6P#00203F……すみません、おそらく\x01",
            "気にするほどの事ではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#00005Fそうか……\x02",
    )

    CloseMessageWindow()
    OP_5A()
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    SetScenarioFlags(0x1BF, 1)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -15840, -5500, -6030, 315)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_13_20FC end

    def Function_14_2356(): pass

    label("Function_14_2356")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_2363")
    Call(0, 15)
    Return()

    label("loc_2363")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-33380, -3950, 5900, 0)
    MoveCamera(25, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15420, 0)
    SetChrPos(0x101, -33000, -5500, 6670, 0)
    SetChrPos(0x102, -32000, -5500, 5870, 0)
    SetChrPos(0x103, -34000, -5500, 5660, 0)
    SetChrPos(0x104, -33000, -5500, 5160, 0)
    SetChrPos(0xF4, -34400, -5500, 4450, 0)
    SetChrPos(0xF5, -31790, -5500, 4570, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A42")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2870")
    SetScenarioFlags(0x2, 2)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁に立てかけられた\x01",
            "木の板の隙間から暗闇が見える。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        (
            "#12P#00005Fこれは……\x01",
            "どこかに通じているみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#12P#00105F場所的にジオフロントかしら？\x02\x03",

            "#00103Fどうやら、\x01",
            "板を動かせそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x104,
        (
            "#12P#00305Fもしかして、さっき\x01",
            "ティオすけが反応したのは……？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#6P#00200Fええ、この場所だと思います。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_25CE")

    #C0024
    ChrTalk(
        0x10A,
        "#12P#00603Fふむ……少々気になるな。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_264F")

    label("loc_25CE")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_260F")

    #C0025
    ChrTalk(
        0x109,
        "#12P#10105F……誰かいるんでしょうか？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_264F")

    label("loc_260F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_264F")

    #C0026
    ChrTalk(
        0x105,
        "#12P#10405F……誰かさんが迷い込んだかな？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_264F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_268A")

    #C0027
    ChrTalk(
        0x106,
        "#12P#10701F入って確かめますか？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2703")

    label("loc_268A")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26C9")

    #C0028
    ChrTalk(
        0x105,
        "#12P#10400F入って確かめてみるかい？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Jump("loc_2703")

    label("loc_26C9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2703")

    #C0029
    ChrTalk(
        0x109,
        "#12P#10101F入って確かめてみますか？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    label("loc_2703")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【中の様子を探ってみる】\x01",      # 0
            "【やめておく】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2800")

    #C0030
    ChrTalk(
        0x101,
        (
            "#12P#00001Fそうだな……\x01",
            "念のため確認しておくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x103,
        "#6P#00200Fでは早速、入りましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("m0304", 0, 0, 0)
    IdleLoop()
    Jump("loc_286B")

    label("loc_2800")


    #C0032
    ChrTalk(
        0x101,
        (
            "#12P#00003F……いや、今は無理に\x01",
            "寄り道することもないだろう。\x02\x03",

            "#00000Fとりあえず、ここは放っておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_286B")

    Jump("loc_2A3D")

    label("loc_2870")

    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁に木の板が立てかけられており、\x01",
            "隙間から暗闇が見える。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【中の様子を探る】\x01",      # 0
            "【やめておく】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29D8")

    #C0034
    ChrTalk(
        0x101,
        (
            "#12P#00003Fやっぱり……\x01",
            "念のため確認しておくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x102,
        "#12P#00101Fそうね、何だか気になるし。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        "#6P#00200Fでは早速、入りましょう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(10)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("m0304", 0, 0, 0)
    IdleLoop()
    Jump("loc_2A3D")

    label("loc_29D8")


    #C0037
    ChrTalk(
        0x101,
        (
            "#12P#00003F……今は無理に\x01",
            "寄り道することもないだろう。\x02\x03",

            "#00000Fとりあえず、ここは放っておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A3D")

    Jump("loc_2B67")

    label("loc_2A42")

    SetChrName("")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁に木の板が立てかけられており、\x01",
            "隙間から暗闇が見える。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0039
    ChrTalk(
        0x101,
        (
            "#12P#00003F（レインズさんか……\x01",
            "  まさか調査会社の\x01",
            "  人間だったなんてな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【レインズの潜伏場所に行く】\x01",      # 0
            "【やめておく】\x01",                    # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B67")
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("m0304", 100, 0, 0)
    IdleLoop()
    Jump("loc_2B67")

    label("loc_2B67")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -33410, -5500, 5850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_14_2356 end

    def Function_15_2B9E(): pass

    label("Function_15_2B9E")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C3B")
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁に木の板が立てかけられており、\x01",
            "しっかりと固定されている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0041
    ChrTalk(
        0x101,
        (
            "#00005Fレインズさん、あれから\x01",
            "しっかり塞いだみたいだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 2)
    Jump("loc_2C85")

    label("loc_2C3B")

    SetChrName("")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壁に木の板が立てかけられており、\x01",
            "しっかりと固定されている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2C85")

    TalkEnd(0xFF)
    Return()

    # Function_15_2B9E end

    def Function_16_2C89(): pass

    label("Function_16_2C89")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-33310, -3750, 5030, 0)
    MoveCamera(57, 31, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14690, 0)
    SetChrPos(0x101, -33000, -5500, 6670, 180)
    SetChrPos(0x102, -31600, -5500, 6070, 225)
    SetChrPos(0x103, -31790, -5500, 5070, 270)
    SetChrPos(0x104, -33000, -5500, 3860, 0)
    SetChrPos(0xF4, -34400, -5500, 4450, 45)
    SetChrPos(0xF5, -34400, -5500, 5660, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0043
    ChrTalk(
        0x103,
        (
            "#00203Fそれにしても\x01",
            "Ｒ＆Ａリサーチ、ですか……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x104,
        (
            "#12P#00301Fああ、なんつうか\x01",
            "相当優秀な組織みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#5P#00100Fええ、何といっても\x01",
            "あのリシャール元大佐の会社だから。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#00003Fまあ、とりあえず\x01",
            "必要以上に勘ぐっても仕方ない。\x02\x03",

            "#00001Fとにかく今は\x01",
            "タワー突入の準備を進めよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -33410, -5500, 5850, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1BF, 3)
    OP_2C(0xB1, 0x2)
    EventEnd(0x5)
    Return()

    # Function_16_2C89 end

    def Function_17_2EA9(): pass

    label("Function_17_2EA9")

    Return()

    # Function_17_2EA9 end

    def Function_18_2EAA(): pass

    label("Function_18_2EAA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(1600, -900, -42250, 0)
    MoveCamera(47, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(26000, 0)
    SetChrPos(0x101, 1600, -3000, -47000, 0)
    SetChrPos(0x102, 2500, -3000, -47900, 0)
    SetChrPos(0x109, 700, -3000, -48500, 0)
    SetChrPos(0x105, 1600, -3000, -40500, 0)

    def lambda_2F2D():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF88DC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2F2D)
    Sleep(50)

    def lambda_2F4A():
        OP_96(0xFE, 0x640, 0xFFFFF448, 0xFFFF7B30, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F4A)
    Sleep(50)

    def lambda_2F67():
        OP_96(0xFE, 0x9C4, 0xFFFFF448, 0xFFFF77AC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F67)
    Sleep(50)

    def lambda_2F84():
        OP_96(0xFE, 0x2BC, 0xFFFFF448, 0xFFFF7554, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2F84)
    OP_68(1600, -1900, -32250, 7000)
    MoveCamera(40, 15, 0, 7000)
    SetCameraDistance(15000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x105, 1)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x101, 1)

    #C0047
    ChrTalk(
        0x101,
        "#12P#00008F#30Wワジ……\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 1)
    WaitChrThread(0x109, 1)

    #C0048
    ChrTalk(
        0x109,
        "#12P#10106F#30Wワジ君、その……\x02",
    )

    CloseMessageWindow()
    OP_64(0x105)
    Sleep(500)
    OP_93(0x105, 0xB4, 0x190)
    Sleep(150)

    #C0049
    ChrTalk(
        0x105,
        (
            "#5P#10304F#30W……ハハ。\x01",
            "みっともない所を見せたね。\x02\x03",

            "#10302Fちょっと僕らしくもなく\x01",
            "熱くなっちゃったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#12P#00006Fいや……\x02\x03",

            "#00000F……何ていうか\x01",
            "男なんてそんなもんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x102,
        (
            "#00103F男の子の気持ちは\x01",
            "ちょっと判らないけど……\x02\x03",

            "#00100Fあなたが彼に、誠意をもって\x01",
            "向き合ったのは判ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x109,
        (
            "#12P#10112Fうんうん……！\x02\x03",

            "#10100Fいつかきっと彼にも\x01",
            "判ってもらえると思うよ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x6A, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6B, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x6C, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3241")

    #C0053
    ChrTalk(
        0x105,
        (
            "#5P#10304F#30Wフフ……\x01",
            "そうだといいけどね。\x02\x03",

            "#10300F──時間を取らせた。\x01",
            "とにかく別の場所に行こう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32AC")

    label("loc_3241")


    #C0054
    ChrTalk(
        0x105,
        (
            "#5P#10304F#30Wフフ……\x01",
            "そうだといいけどね。\x02\x03",

            "#10300F──時間を取らせた。\x01",
            "残りの支援要請を片付けよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32AC")

    SetCameraDistance(15500, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetChrPos(0x0, 1530, -3000, -23230, 0)
    SetScenarioFlags(0x128, 6)
    SetScenarioFlags(0x2, 6)
    OP_1B(0x2, 0x0, 0x2F)
    OP_32(0xFF, 0xFE, 0x0)
    OP_C9(0x1, 0x1000)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_18_2EAA end

    def Function_19_32EF(): pass

    label("Function_19_32EF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-10500, 2000, -1000, 0)
    MoveCamera(65, 3, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 27600, -300, -2700, 0)
    SetChrPos(0x1, 27600, -300, -2700, 0)
    SetChrPos(0x2, 27600, -300, -2700, 0)
    SetChrPos(0x3, 27600, -300, -2700, 0)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF7, 0xCD, 0xB7, 0x23, 0x96, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sky1", 0x1, 0x1)
    SetMapObjFrame(0xFF, "sd_mul", 0x0, 0x1)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    BeginChrThread(0xA, 0, 0, 0)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x15, 0x8000)
    SetChrFlags(0xE, 0x8000)
    BeginChrThread(0xE, 0, 0, 0)
    SetChrPos(0xE, -4200, -300, -500, 315)
    SetChrFlags(0xD, 0x8000)
    BeginChrThread(0xD, 0, 0, 0)
    SetChrPos(0xD, -5200, -300, 500, 135)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -13300, -300, 12700, 135)

    def lambda_3427():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_3427)
    SetChrFlags(0x10, 0x8000)
    SetChrPos(0x10, -14300, -300, 11700, 135)

    def lambda_3457():
        OP_98(0xFE, 0x2AF8, 0x0, 0xFFFFD508, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_3457)
    OP_68(-10500, 1000, -1000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(1000)
    OP_68(-7500, 2100, 14100, 0)
    MoveCamera(75, 23, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(21500, 0)
    SetCameraDistance(17500, 4000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6F(0x10)
    SetScenarioFlags(0x22, 0)
    NewScene("c1010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_32EF end

    def Function_20_34E2(): pass

    label("Function_20_34E2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30000.itc", 0x1E)
    SoundLoad(835)
    SoundLoad(821)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xD, 0, 0, 0)
    BeginChrThread(0xE, 0, 0, 0)
    BeginChrThread(0x10, 0, 0, 0)
    BeginChrThread(0x13, 0, 0, 0)
    SetChrChipByIndex(0x26, 0x1E)
    ClearChrFlags(0x26, 0x80)
    SetChrFlags(0x26, 0x8000)
    BeginChrThread(0x26, 0, 0, 0)
    SetChrChipByIndex(0x27, 0x1E)
    ClearChrFlags(0x27, 0x80)
    SetChrFlags(0x27, 0x8000)
    BeginChrThread(0x27, 0, 0, 0)
    SetChrChipByIndex(0x28, 0x1E)
    ClearChrFlags(0x28, 0x80)
    SetChrFlags(0x28, 0x8000)
    BeginChrThread(0x28, 0, 0, 0)
    SetChrChipByIndex(0x29, 0x1E)
    ClearChrFlags(0x29, 0x80)
    SetChrFlags(0x29, 0x8000)
    BeginChrThread(0x29, 0, 0, 0)
    ClearMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xC, 0x1000)
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x26, -23200, -340, 16500, 180)
    SetChrPos(0x27, -18350, -300, 16500, 180)
    SetChrPos(0x28, -18150, -300, 11450, 0)
    SetChrPos(0x29, 1900, -300, -2300, 0)
    SetChrPos(0xF, -19750, -300, 18450, 180)
    SetChrPos(0x10, -18650, -300, 18900, 180)
    SetChrPos(0xE, -20200, -300, 19900, 180)
    SetChrPos(0xD, -22800, -300, 18500, 180)
    SetChrPos(0x13, -21300, -300, 20900, 180)
    SetChrPos(0x11, -18200, -300, 21250, 180)
    SetChrPos(0x8, -18600, -600, 9150, 0)
    SetChrPos(0x9, -17550, -830, 8850, 0)
    SetChrPos(0xA, 1250, -580, -4500, 0)
    SetChrPos(0xB, 2600, -310, -4150, 0)
    SetChrPos(0x12, 2150, -1030, -5050, 0)
    BeginChrThread(0xF, 3, 0, 21)
    BeginChrThread(0xE, 3, 0, 21)
    BeginChrThread(0xD, 3, 0, 21)
    BeginChrThread(0x11, 3, 0, 21)
    BeginChrThread(0x8, 3, 0, 21)
    BeginChrThread(0x9, 3, 0, 21)
    BeginChrThread(0xA, 3, 0, 21)
    BeginChrThread(0xB, 3, 0, 21)
    BeginChrThread(0x12, 3, 0, 21)
    OP_68(-24900, 1000, 12950, 0)
    MoveCamera(55, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_68(-19900, 1000, 12950, 5000)
    MoveCamera(50, 30, 0, 5000)
    SetCameraDistance(15000, 5000)
    Sound(835, 2, 100, 0)
    Sound(821, 2, 50, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    SetChrPos(0x11, 3160, -950, -4950, 0)
    SetChrPos(0xE, 2160, -1250, -5340, 0)
    SetChrPos(0xD, 550, -350, -4150, 0)
    OP_68(-850, 1000, -7900, 0)
    MoveCamera(40, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13000, 0)
    OP_68(11450, 1750, -350, 5000)
    MoveCamera(60, 20, 0, 5000)
    SetCameraDistance(15000, 5000)
    Sleep(4000)
    StopSound(835, 1000, 100)
    StopSound(821, 1000, 50)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("r0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_34E2 end

    def Function_21_3849(): pass

    label("Function_21_3849")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_3881"),
        (1, "loc_3889"),
        (2, "loc_3891"),
        (3, "loc_3899"),
        (4, "loc_38A1"),
        (5, "loc_38A9"),
        (6, "loc_38B1"),
        (SWITCH_DEFAULT, "loc_38B9"),
    )


    label("loc_3881")

    Sleep(100)
    Jump("loc_38C1")

    label("loc_3889")

    Sleep(200)
    Jump("loc_38C1")

    label("loc_3891")

    Sleep(300)
    Jump("loc_38C1")

    label("loc_3899")

    Sleep(400)
    Jump("loc_38C1")

    label("loc_38A1")

    Sleep(500)
    Jump("loc_38C1")

    label("loc_38A9")

    Sleep(600)
    Jump("loc_38C1")

    label("loc_38B1")

    Sleep(700)
    Jump("loc_38C1")

    label("loc_38B9")

    Sleep(800)
    Jump("loc_38C1")

    label("loc_38C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38EC")
    OP_63(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)
    OP_64(0xFE)
    Sleep(500)
    Jump("loc_38C1")

    label("loc_38EC")

    Return()

    # Function_21_3849 end

    def Function_22_38ED(): pass

    label("Function_22_38ED")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(-19500, 1020, 24400, 0)
    MoveCamera(39, 29, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18500, 0)
    SetChrPos(0x101, -20800, -320, 24400, 90)
    SetChrPos(0x102, -20000, -320, 23100, 45)
    SetChrPos(0x104, -18400, -320, 25100, 270)
    SetChrPos(0x109, -20000, -320, 25700, 135)
    SetChrPos(0x105, -18400, -320, 23700, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    MoveCamera(49, 25, 0, 3000)
    SetCameraDistance(16500, 3000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0055
    ChrTalk(
        0x101,
        (
            "#6P#00012Fふう……\x01",
            "何だかどっと疲れたな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x102,
        (
            "#12P#00102Fそうね……\x01",
            "無事、マリーちゃんが\x01",
            "見つかってよかったけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        (
            "#00306F……すまねぇな。\x01",
            "不肖のイトコが迷惑をかけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x109,
        (
            "#5P#10112Fあはは……\x01",
            "先輩のせいじゃないですよ。\x02\x03",

            "#10100Fそれに結構、\x01",
            "いい子みたいじゃないですか。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        (
            "#12P#00100Fそうね、何だかんだ言って\x01",
            "親身になって協力してくれたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#00302Fはは……\x01",
            "ま、確かに悪気はねえんだ。\x02\x03",

            "#00306Fそれだけに結構厄介でな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#6P#00008Fなるほど……\x01",
            "色々あるみたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#11P#10304Fフフ、女の子の気まぐれに\x01",
            "振り回されるのも\x01",
            "男の甲斐性だと思うけど。\x02\x03",

            "#10300Fそれで、どうするんだい？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x72, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x76, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x77, 0x0, 0x10)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C9D")

    #C0063
    ChrTalk(
        0x101,
        (
            "#6P#00004Fそうだな……\x01",
            "支援要請も一通り終わったし。\x02\x03",

            "#00000F一度、支援課に戻って\x01",
            "休憩してもいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3D10")

    label("loc_3C9D")


    #C0064
    ChrTalk(
        0x101,
        (
            "#6P#00003Fそうだな……\x01",
            "まだ支援要請は残ってるけど。\x02\x03",

            "#00000F一度、支援課に戻って\x01",
            "休憩してもいいかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3D10")


    #C0065
    ChrTalk(
        0x102,
        (
            "#12P#00104Fそうね……\x01",
            "そうしましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#00300Fそんじゃ、中休みに\x01",
            "支援課に戻るとすっか。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -18400, -310, 24400, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x140, 5)
    OP_29(0xA3, 0x1, 0xF)
    EventEnd(0x5)
    Return()

    # Function_22_38ED end

    def Function_23_3DAA(): pass

    label("Function_23_3DAA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch41400.itc", 0x1E)
    LoadChrToIndex("chr/ch41500.itc", 0x1F)
    SoundLoad(821)
    SoundLoad(835)
    ClearChrFlags(0x16, 0x80)
    OP_78(0x8, 0x16)
    OP_49()
    SetChrPos(0x16, -18400, -300, 16800, 225)
    OP_D5(0x16, 0x0, 0x4CE78, 0x0, 0x0)
    SetMapObjFlags(0x8, 0x1000)
    ClearMapObjFlags(0x8, 0x4)
    OP_74(0x8, 0x1E)
    OP_70(0x8, 0x2)
    SetChrChipByIndex(0x1D, 0x1E)
    SetChrSubChip(0x1D, 0x0)
    ClearChrFlags(0x1D, 0x80)
    SetChrFlags(0x1D, 0x8000)
    SetChrPos(0x1D, -20800, -320, 16200, 225)
    SetChrChipByIndex(0x1E, 0x1F)
    SetChrSubChip(0x1E, 0x0)
    ClearChrFlags(0x1E, 0x80)
    SetChrFlags(0x1E, 0x8000)
    SetChrPos(0x1E, -17500, -310, 12900, 225)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrChipByIndex(0x1F, 0x2)
    SetChrSubChip(0x1F, 0x0)
    ClearChrFlags(0x1F, 0x80)
    SetChrFlags(0x1F, 0x8000)
    SetChrPos(0x1F, -22000, -300, 12900, 90)
    SetChrChipByIndex(0x20, 0x3)
    SetChrSubChip(0x20, 0x0)
    ClearChrFlags(0x20, 0x80)
    SetChrFlags(0x20, 0x8000)
    SetChrPos(0x20, -22650, -300, 13500, 90)
    SetChrChipByIndex(0x21, 0x4)
    SetChrSubChip(0x21, 0x0)
    ClearChrFlags(0x21, 0x80)
    SetChrFlags(0x21, 0x8000)
    SetChrPos(0x21, -20200, -300, 12100, 45)
    SetChrChipByIndex(0x22, 0x5)
    SetChrSubChip(0x22, 0x0)
    ClearChrFlags(0x22, 0x80)
    SetChrFlags(0x22, 0x8000)
    SetChrPos(0x22, -21700, -300, 11300, 45)
    SetChrChipByIndex(0x23, 0x6)
    SetChrSubChip(0x23, 0x0)
    ClearChrFlags(0x23, 0x80)
    SetChrFlags(0x23, 0x8000)
    SetChrPos(0x23, -19200, -300, 11300, 45)
    SetChrChipByIndex(0x24, 0x8)
    SetChrSubChip(0x24, 0x0)
    ClearChrFlags(0x24, 0x80)
    SetChrFlags(0x24, 0x8000)
    SetChrPos(0x24, -22500, -300, 15200, 90)
    SetChrChipByIndex(0x25, 0xB)
    SetChrSubChip(0x25, 0x0)
    ClearChrFlags(0x25, 0x80)
    SetChrFlags(0x25, 0x8000)
    SetChrPos(0x25, -24100, -300, 12850, 90)
    OP_63(0x1F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x21, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(50)
    OP_63(0x25, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_68(-20000, 3300, 13800, 0)
    MoveCamera(33, 21, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(15500, 0)
    OP_68(-20000, 1300, 13800, 10000)
    Sound(821, 2, 60, 0)
    Sound(835, 2, 80, 0)
    FadeToBright(1500, 0)
    OP_0D()
    SetMessageWindowPos(120, 90, -1, -1)
    SetChrName("ディーター大統領")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "──もちろん、お気づきの通り、\x01",
            "邪悪な意志は１つではありません。\x02\x03",

            "『カルバード共和国政府』……\x02\x03",

            "狡猾な犯罪組織と手を結んでいた\x01",
            "彼らもまた、クロスベルの平和と\x01",
            "尊厳を踏みにじろうとしているのです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0x22, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    StopSound(851, 1500, 60)
    StopSound(835, 1500, 80)
    FadeToDark(1500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0000", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_23_3DAA end

    def Function_24_4129(): pass

    label("Function_24_4129")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(13890, -1330, -14740, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(13890, -1330, -14740, 0)
    MoveCamera(45, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, 16400, -2500, -15030, 270)
    SetChrPos(0x102, 18400, -2500, -15030, 270)
    SetChrPos(0x109, 20400, -2500, -15030, 270)
    SetChrPos(0x105, 22400, -2500, -15030, 270)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Sound(103, 0, 100, 0)
    ClearMapObjFlags(0x4, 0x10)
    OP_71(0x4, 0x0, 0x10, 0x0, 0x0)
    OP_79(0x0)
    OP_68(1120, -1400, -15440, 3000)
    MoveCamera(45, 13, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(12000, 3000)
    OP_0D()

    def lambda_4293():
        OP_95(0x101, 1000, -3000, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4293)

    def lambda_42AD():
        OP_95(0x102, 2600, -3000, -13540, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_42AD)

    def lambda_42C7():
        OP_95(0x109, 2000, -3000, -15940, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_42C7)

    def lambda_42E1():
        OP_95(0x105, 3600, -2930, -14740, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42E1)

    def lambda_42FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_42FB)
    Sleep(300)

    def lambda_430F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_430F)
    Sleep(300)

    def lambda_4323():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4323)
    Sleep(300)

    def lambda_4337():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x320)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4337)
    Sleep(1500)
    SetMapObjFlags(0x4, 0x0)
    WaitChrThread(0x101, 1)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    WaitChrThread(0x102, 1)

    def lambda_4385():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4385)
    Sleep(300)

    def lambda_4395():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4395)
    Sleep(300)

    def lambda_43A5():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43A5)
    Sleep(300)

    def lambda_43B5():
        OP_93(0x105, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43B5)
    Sleep(300)

    def lambda_43C5():
        OP_93(0x101, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_43C5)
    Sleep(300)

    def lambda_43D5():
        OP_93(0x102, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43D5)
    Sleep(300)

    def lambda_43E5():
        OP_93(0x109, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_43E5)
    Sleep(300)

    def lambda_43F5():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_43F5)
    Sleep(300)
    OP_0D()

    def lambda_4406():
        OP_93(0x101, 0x5A, 0x5DC)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4406)

    def lambda_4413():
        OP_93(0x102, 0xB4, 0x5DC)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4413)

    def lambda_4420():
        OP_93(0x109, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4420)

    def lambda_442D():
        OP_93(0x105, 0x10E, 0x5DC)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_442D)
    OP_0D()
    WaitChrThread(0x101, 1)

    #C0068
    ChrTalk(
        0x101,
        "#6P#00001F駄目だ……見失った。\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x109,
        (
            "#12P#10106Fと、とんでもない人ですね。\x02\x03",

            "#10101Fまるであたしたちが来るのを\x01",
            "分かってて引っ掛けたような……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x102,
        (
            "#00103Fまあ、あれくらいのことは\x01",
            "朝飯前なんでしょうね……\x02\x03",

            "#00101Fさすがは情報機関の\x01",
            "大尉を務めるだけはあるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、とても軍人とは\x01",
            "思えないような方法だけど。\x02\x03",

            "#10302Fで、ここで諦めるのかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#6P#00003Fいや……\x01",
            "とにかく後を追ってみよう。\x02\x03",

            "#00000F今なら通りの人に聞けば\x01",
            "行方が掴めるかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x102,
        "#00100F分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x109,
        "#12P#10100F行きましょう！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x4, 0x10)
    SetScenarioFlags(0x130, 3)
    OP_29(0x66, 0x1, 0x3)
    SetChrPos(0x0, 1000, -3000, -14740, 225)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_24_4129 end

    def Function_25_4673(): pass

    label("Function_25_4673")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(975)
    OP_68(-23060, 4740, 24030, 0)
    MoveCamera(63, 44, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(17480, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x105, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrFlags(0x17, 0x8000)
    SetMapObjFlags(0xB, 0x1000)
    ClearMapObjFlags(0xB, 0x4)
    OP_78(0xB, 0x17)
    SetMapObjFrame(0xB, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x17, -20760, -310, 40300, 180)
    OP_A7(0x17, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_D5(0x17, 0x0, 0x2BF20, 0x0, 0x0)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)
    OP_78(0xA, 0x18)
    OP_49()
    SetChrPos(0x18, -13070, -300, 11900, 315)
    OP_D5(0x18, 0x0, 0x4CE78, 0x0, 0x0)
    ClearMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xA, 0x1000)
    SetMapObjFrame(0xA, "light", 0x0, 0x1)
    OP_74(0xA, 0x1E)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    Sound(486, 0, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_68(-25830, 4740, 8470, 1500)
    MoveCamera(42, 17, 0, 1500)
    OP_6E(700, 1500)
    SetCameraDistance(14250, 1500)

    def lambda_47D6():
        OP_9B(0x1, 0xFE, 0x0, 0x61A8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_47D6)

    def lambda_47EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x17, 2, lambda_47EB)
    OP_71(0xB, 0xB5, 0xF0, 0x0, 0x20)
    Sleep(1000)
    Sound(492, 0, 100, 0)
    StopSound(486, 300, 100)
    WaitChrThread(0x17, 1)
    OP_6F(0x79)
    OP_63(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x17, 1)
    OP_0D()

    #N0075
    NpcTalk(
        0x17,
        "サイクス",
        "ハハッ、待ち伏せかよ！\x02",
    )

    CloseMessageWindow()

    #N0076
    NpcTalk(
        0x17,
        "ユーリ",
        "フン、浅知恵だな。\x02",
    )

    CloseMessageWindow()

    #N0077
    NpcTalk(
        0x17,
        "ユーリ",
        "レジー、振り切れるな？\x02",
    )

    CloseMessageWindow()

    #N0078
    NpcTalk(
        0x17,
        "レジー",
        (
            "トーゼン、\x01",
            "あんなの敵じゃねーっつの！\x02",
        )
    )

    CloseMessageWindow()
    Sound(493, 0, 100, 0)
    OP_9B(0x1, 0x17, 0x0, 0xFFFFF830, 0x1388, 0x0)
    OP_71(0xB, 0x5B, 0x78, 0x0, 0x20)
    Sleep(200)
    OP_71(0xB, 0xB5, 0xF0, 0x0, 0x20)
    OP_9F(0x0, 0x17)
    OP_9F(0x1, -22600, -330, 15200)
    OP_9F(0x1, -28560, -330, 14320)
    OP_9F(0x2, 0x17, 11000, 0x6)

    def lambda_493B():
        OP_9B(0x1, 0x17, 0x0, 0x2710, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_493B)
    Sleep(50)
    Sound(494, 0, 100, 0)
    Sound(975, 2, 100, 0)
    OP_71(0xA, 0x79, 0xB4, 0x0, 0x20)
    OP_96(0x18, 0xFFFFC6A8, 0xFFFFFED4, 0x35DE, 0x1388, 0x0)
    WaitChrThread(0x18, 1)
    OP_9F(0x0, 0x18)
    OP_9F(0x1, -15680, -300, 13790)
    OP_9F(0x1, -18990, -300, 13910)
    OP_9F(0x2, 0x18, 11000, 0x6)
    OP_9B(0x1, 0x18, 0x0, 0x3A98, 0x3A98, 0x0)
    StopSound(975, 300, 100)
    SetScenarioFlags(0x24, 2)
    NewScene("c0100", 101, 0, 0)
    IdleLoop()
    Return()

    # Function_25_4673 end

    def Function_26_49C9(): pass

    label("Function_26_49C9")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    ClearChrFlags(0x1A, 0x80)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrPos(0x1A, 1200, 0, 7800, 225)
    ClearChrFlags(0x1B, 0x80)
    SetChrChipByIndex(0x1B, 0x1E)
    SetChrPos(0x1B, 1200, 0, 7800, 225)
    OP_68(-790, 690, 5800, 0)
    MoveCamera(44, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16700, 0)
    SetChrPos(0x101, -1400, -300, 4400, 45)
    SetChrPos(0x102, -2150, -300, 5100, 45)
    SetChrPos(0x109, -1700, -300, 3200, 45)
    SetChrPos(0x105, -3400, -300, 4800, 45)
    FadeToBright(1000, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_END)), "loc_4C08")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0079
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～只今、準備中～　　\x01",
            "　　　――釣皇#4Rちょうおう#倶楽部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0080
    ChrTalk(
        0x101,
        "#12P#00003Fう～ん、前回見た時と同じだな……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#6P#00105Fねえ、ロイド。\x01",
            "本当に心当たりはないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#12P#00001Fああ、正直\x01",
            "何が起こっているのか\x01",
            "さっぱりだよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0083
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあれ……でもどうやら\x01",
            "鍵は開いているみたいだな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4D03")

    label("loc_4C08")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～只今、準備中～　　\x01",
            "　　　――釣皇#4Rちょうおう#倶楽部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0085
    ChrTalk(
        0x101,
        (
            "#12P#00003F準備中、か。\x01",
            "でも釣皇倶楽部って一体……？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0086
    ChrTalk(
        0x101,
        (
            "#12P#00005Fあれ……でもどうやら\x01",
            "鍵は開いているみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4D03")


    #N0087
    NpcTalk(
        0x1A,
        "青年の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5Pあ、あんた……\x01",
            "それでも釣り人なんスか！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0088
    NpcTalk(
        0x1B,
        "男の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11Pそ、そうですよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #N0089
    NpcTalk(
        0x1B,
        "男の声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#11Pそんな強引なやり方、\x01",
            "私は絶対に認めませんよ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0090
    ChrTalk(
        0x102,
        "#6P#00105Fロイド、今のは？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x101,
        (
            "#12P#00001Fああ、知っている声だ。\x01",
            "中に入らせてもらおう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    SetScenarioFlags(0x22, 0)
    NewScene("c1020", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_26_49C9 end

    def Function_27_4E77(): pass

    label("Function_27_4E77")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch23600.itc", 0x1E)
    LoadChrToIndex("chr/ch24200.itc", 0x1F)
    SetChrChipByIndex(0x1A, 0x1E)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -2600, -300, 4800, 225)
    SetChrChipByIndex(0x1B, 0x1F)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1800, -300, 4000, 225)
    SetChrFlags(0xD, 0x80)
    EndChrThread(0xD, 0x0)
    OP_68(-1990, 90, 4670, 0)
    MoveCamera(44, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15630, 0)
    SetChrPos(0x101, -3300, 0, 2500, 45)
    SetChrPos(0x102, -4100, 0, 3300, 45)
    SetChrPos(0x109, -3300, 0, 1400, 45)
    SetChrPos(0x105, -5200, 0, 3300, 45)
    FadeToBright(1000, 0)
    OP_0D()

    #C0092
    ChrTalk(
        0x1A,
        (
            "#5P何でこんなことに……\x01",
            "オレ、納得いかないッスよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x1B,
        (
            "#11Pええ、まさか支部が\x01",
            "奪われてしまうなんてねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x1B,
        (
            "#11Pとりあえず、改めて\x01",
            "セルダン支部長と相談しないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x101,
        (
            "#12P#00006Fあの、ペーターさん。\x01",
            "まだいまいち、\x01",
            "話が見えて来ないのですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x1B,
        (
            "#11Pああ、ロイド君はしばらく\x01",
            "お休みしていましたからねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x1B,
        (
            "#11Pとにかく、一度みんなで\x01",
            "集まって話をしましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x1B,
        (
            "#11P今から支部長に声を掛けて、\x01",
            "裏通りにあるジャズバー\x01",
            "《ガランテ》に来てもらいます。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0x1B,
        "#11Pロイド君も来て下さい。\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x1A,
        (
            "#5Pじゃあ、オレたちは\x01",
            "先に行ってるッスから。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_517E():
        OP_9B(0x0, 0x1A, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_517E)
    Sleep(50)

    def lambda_5196():
        OP_93(0x101, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5196)
    Sleep(50)

    def lambda_51A6():
        OP_93(0x102, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51A6)
    Sleep(50)
    WaitChrThread(0x1B, 1)

    def lambda_51BA():
        OP_9B(0x0, 0x1B, 0x5A, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_51BA)
    Sleep(50)

    def lambda_51D2():
        OP_93(0x109, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_51D2)
    Sleep(50)

    def lambda_51E2():
        OP_93(0x105, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_51E2)
    Sleep(50)
    WaitChrThread(0x1B, 1)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    #C0101
    ChrTalk(
        0x102,
        "#5P#00105F本当に何があったのかしらね。\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x101,
        (
            "#11P#00003Fよく分からないけど\x01",
            "とにかく経緯を確認しないと。\x02\x03",

            "#00000F俺たちもジャズバーに向かおう。\x02",
        )
    )

    CloseMessageWindow()
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x2, 0x1)
    SetMapObjFlags(0x0, 0x10)
    OP_D7(0x1E)
    OP_D7(0x1F)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 1, 0, 1)
    SetScenarioFlags(0x132, 0)
    OP_29(0x6A, 0x1, 0x3)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -4200, 0, 2400, 225)
    EventEnd(0x5)
    Return()

    # Function_27_4E77 end

    def Function_28_52E5(): pass

    label("Function_28_52E5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(4570, 40, -12620, 0)
    MoveCamera(44, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(33000, 0)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x8000)
    SetChrFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x8000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5382")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x104, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_53C1")

    label("loc_5382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_53A4")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x1A2, 0x80)
    Jump("loc_53C1")

    label("loc_53A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_53C1")
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0x105, 0x80)
    SetChrFlags(0x1A2, 0x80)

    label("loc_53C1")

    OP_68(4570, 40, -12620, 5000)
    MoveCamera(44, 13, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(37220, 5000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_68(-23840, 1240, 8210, 7000)
    MoveCamera(33, 13, 0, 7000)
    OP_6E(600, 7000)
    SetCameraDistance(37220, 7000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-20080, 1440, 21740, 0)
    MoveCamera(45, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16560, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5535")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x104, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x104, -20350, -310, 27200, 180)

    def lambda_54C7():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_54C7)

    def lambda_54E1():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54E1)
    Sleep(100)

    def lambda_54FE():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54FE)
    Sleep(50)

    def lambda_551B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_551B)
    Jump("loc_56D8")

    label("loc_5535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5609")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x109, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x109, -20350, -310, 27200, 180)

    def lambda_559B():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_559B)

    def lambda_55B5():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_55B5)
    Sleep(100)

    def lambda_55D2():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_55D2)
    Sleep(50)

    def lambda_55EF():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_55EF)
    Jump("loc_56D8")

    label("loc_5609")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_56D8")
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x105, 0x80)
    ClearChrFlags(0x1A2, 0x80)
    SetChrPos(0x1A2, -19400, -310, 26000, 180)
    SetChrPos(0x102, -20100, -310, 26000, 180)
    SetChrPos(0x101, -19150, -310, 27200, 180)
    SetChrPos(0x105, -20350, -310, 27200, 180)

    def lambda_566F():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A2, 1, lambda_566F)

    def lambda_5689():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF060, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5689)
    Sleep(100)

    def lambda_56A6():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_56A6)
    Sleep(50)

    def lambda_56C3():
        OP_97(0xFE, 0x0, 0x0, 0xFFFFF31C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_56C3)

    label("loc_56D8")

    SetCameraDistance(14560, 3000)
    OP_6F(0x79)

    #C0103
    ChrTalk(
        0x1A2,
        "ここが東通り……\x02",
    )

    CloseMessageWindow()

    #C0104
    ChrTalk(
        0x1A2,
        (
            "こうして、ゆっくり\x01",
            "眺めるのは初めてだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0105
    ChrTalk(
        0x102,
        (
            "#6P#00100Fふふ、ここは故郷に似ていて\x01",
            "落ち着くんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0106
    ChrTalk(
        0x1A2,
        "#11Pええ、そうかもしれません。\x02",
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x1A2,
        (
            "#11Pフフ、といっても\x01",
            "本場・東方人街の活気は\x01",
            "こんなものではありませんが。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x1A2,
        (
            "#11Pもし機会があれば、\x01",
            "こんどはボクがお姉さんに\x01",
            "共和国を案内したい。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0x1A2,
        "#11Pというか、クニにつれて帰りたい！\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_5939")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0110
    ChrTalk(
        0x102,
        "#6P#00112Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x101,
        "#00006Fほんと、大したアプローチだな。\x02",
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#00300Fああ、洒落っ気も\x01",
            "へったくれもねえけどな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD7")

    label("loc_5939")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_5A0E")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0113
    ChrTalk(
        0x102,
        "#00112Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0x101,
        "#00006Fほんと、大したアプローチだな。\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x109,
        (
            "#10109Fあはは、ある意味\x01",
            "うらやましいかもですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5AD7")

    label("loc_5A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_5AD7")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x102,
        "#00112Fえ、えっと……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x101,
        "#00006Fほんと、大したアプローチだな。\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x105,
        "#10300Fフフ、ド直球もいいところだけどね。\x02",
    )

    CloseMessageWindow()

    label("loc_5AD7")

    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    ClearChrFlags(0x15, 0x8000)
    OP_1B(0x8, 0x0, 0x2D)
    SetScenarioFlags(0x153, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -19750, -310, 26000, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_28_52E5 end

    def Function_29_5B4D(): pass

    label("Function_29_5B4D")

    EventBegin(0x0)
    Fade(500)
    LoadChrToIndex("chr/ch03400.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04600.itp")
    SoundLoad(3949)
    OP_68(-5300, -1400, -11050, 0)
    MoveCamera(44, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(13490, 0)
    SetChrPos(0x101, -5200, -3000, -10840, 0)
    SetChrPos(0x102, -3970, -3000, -10800, 0)
    SetChrPos(0x109, -6270, -3000, -10440, 45)
    SetChrPos(0x104, -2970, -3000, -11500, 315)
    SetChrPos(0x105, -3950, -3000, -12150, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_4B(0xB, 0xFF)
    OP_0D()

    #C0119
    ChrTalk(
        0xB,
        "おや、何か用事かい？\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x101,
        (
            "#12P#00000Fええ、ちょっと\x01",
            "お聞きしたいことがありまして。\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0121
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドは事情を説明し、\x01",
            "仔猫のマリーが来ていないか尋ねた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0122
    ChrTalk(
        0xB,
        (
            "ああ、ボンドさん一家の仔猫だね。\x01",
            "警察が捜してくれるなら安心だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0xB,
        (
            "でも、あいにく\x01",
            "今日はまだ見ていなくてねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0xB,
        (
            "念のために置いてあった\x01",
            "あの子の好物の干物も\x01",
            "そのままだったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xB,
        (
            "少なくとも昨晩からここには\x01",
            "来ていないんじゃないかねえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#12P#00103Fそうですか……\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0xB,
        (
            "あのご家族にはいつも\x01",
            "贔屓#5R  ひいき #にしてもらっているし、\x01",
            "力になってあげたいんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        "何とか見つけてあげて頂戴ね。\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        "#12P#00000Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x102,
        "#12P#00100Fご協力ありがとうございました。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 32)
    Sleep(100)
    BeginChrThread(0x105, 3, 0, 34)
    Sleep(100)
    BeginChrThread(0x102, 3, 0, 31)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 30)
    Sleep(100)
    BeginChrThread(0x109, 3, 0, 33)
    OP_68(2580, -1400, -13440, 5000)
    MoveCamera(32, 28, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(15530, 5000)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)

    #C0131
    ChrTalk(
        0x104,
        "#00303Fまずは空振り、か。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0132
    ChrTalk(
        0x109,
        (
            "#12P#10105Fロイドさん、\x01",
            "この後はどうするんですか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)
    Sleep(300)

    #C0133
    ChrTalk(
        0x101,
        (
            "#00000Fああ、とりあえずは周辺で\x01",
            "一通り聞き込みを行って……\x02\x03",

            "#00003F後は捜索範囲が広がってしまうけど、\x01",
            "ツァイトの鼻に頼るしかないかもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x102,
        (
            "#11P#00105Fそれはいいんだけど……\x02\x03",

            "#00106F……ティオちゃんがいない状況で\x01",
            "ちゃんと意思疎通できるかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x101,
        (
            "#00006Fそうなんだよな……\x02\x03",

            "#00000Fでもまあ、そこは何とか\x01",
            "身振り手振りで――\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x1C, 0x1E)
    SetChrSubChip(0x1C, 0x0)
    ClearChrFlags(0x1C, 0x80)
    SetChrFlags(0x1C, 0x8000)
    SetChrPos(0x1C, 2270, -220, -3590, 180)
    OP_C9(0x0, 0x80000000)

    #N0136
    NpcTalk(
        0x1C,
        "少女の声",
        "#3949Vあれー、なにしてんの？\x02",
    )

    CloseMessageWindow()
    OP_24(0xF6D)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(-1420, 800, -15420, 3000)
    MoveCamera(35, 19, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(13050, 3000)

    def lambda_61AB():

        label("loc_61AB")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61AB")

    QueueWorkItem2(0x101, 1, lambda_61AB)

    def lambda_61BD():

        label("loc_61BD")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61BD")

    QueueWorkItem2(0x104, 1, lambda_61BD)

    def lambda_61CF():

        label("loc_61CF")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61CF")

    QueueWorkItem2(0x102, 1, lambda_61CF)

    def lambda_61E1():

        label("loc_61E1")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61E1")

    QueueWorkItem2(0x109, 1, lambda_61E1)

    def lambda_61F3():

        label("loc_61F3")

        TurnDirection(0xFE, 0x1C, 500)
        Yield()
        Jump("loc_61F3")

    QueueWorkItem2(0x105, 1, lambda_61F3)
    OP_6F(0x79)
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
    Sleep(1000)

    #C0137
    ChrTalk(
        0x101,
        "#12P#00011Fな……！\x02",
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0x102,
        "#00105Fランディの……\x02",
    )

    CloseMessageWindow()
    OP_68(870, -1400, -12100, 4000)
    MoveCamera(53, 30, 0, 4000)
    OP_6E(600, 4000)
    SetCameraDistance(14790, 4000)
    OP_95(0x1C, 1340, -3000, -9310, 2000, 0x0)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    WaitChrThread(0x1C, 1)
    OP_6F(0x79)
    Sleep(300)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0139
    AnonymousTalk(
        0x1C,
        (
            "ランディ兄#2Rにい#に……\x01",
            "お兄さんとお姉さんたちじゃん。\x02\x03",

            "こんな所で何してんのさー？\x02",
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

    #C0140
    ChrTalk(
        0x104,
        (
            "#00303F……どうでもいいだろうが。\x01",
            "とっとと失せろ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1C, 0x104, 500)
    Sleep(300)

    #C0141
    ChrTalk(
        0x1C,
        (
            "#04606Fむー、つれないなぁ。\x02\x03",

            "#04600Fそれじゃあ、そっちのお姉さんの\x01",
            "身体に聞いちゃおうかな？\x02\x03",

            "#04609Fまた思いっきり揉んでみたいし㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        "#00112Fちょ、ちょっと……！\x02",
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_9B(0x1, 0x102, 0xB4, 0x1F4, 0x5DC, 0x0)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    OP_64(0x102)

    #C0143
    ChrTalk(
        0x101,
        (
            "#12P#00003F……見ての通り、\x01",
            "特務支援課のお仕事でね。\x02\x03",

            "#00001F君たちに関係のある話じゃないから\x01",
            "絡まないでくれないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0xB4, 0x1F4)
    Sleep(300)

    #C0144
    ChrTalk(
        0x1C,
        (
            "#04606Fんー、別に絡んでる\x01",
            "つもりはないんだけど。\x02\x03",

            "#04600Fちなみにどんな仕事なの？\x02",
        )
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0x101,
        "#12P#00006Fふう……仕方ないな。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0146
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "仔猫の件について\x01",
            "かいつまんで内容を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0147
    ChrTalk(
        0x1C,
        (
            "#04605Fふ～ん、なるほどね。\x02\x03",

            "#04600Fそれで、そのマリーってコ、\x01",
            "これからどうやって捜すの？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x101,
        (
            "#12P#00000Fああ、これから警察犬の\x01",
            "力を頼って匂いを辿ろうと――\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x1C,
        "#04609Fあはは、それじゃダメだよ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0150
    ChrTalk(
        0x101,
        "#12P#00005Fえ……！？\x02",
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x1C,
        (
            "#04602Fお兄さん、犬は詳しそうだけど\x01",
            "ネコについてはまだまだだねー？\x02\x03",

            "#04604Fもっとさ、マリーってコの\x01",
            "気持ちになって考えてあげないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x101,
        "#12P#00006Fど、どういうことだ？\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x1C,
        (
            "#04600F詳しいことは知らないけど、\x01",
            "その家族、最近引っ越したんでしょ？\x02\x03",

            "#04604Fだったら答えは一つだと思うけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0154
    ChrTalk(
        0x102,
        (
            "#00105Fそうか、どうして\x01",
            "気付かなかったのかしら。\x02\x03",

            "#00100F住宅街だわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x1C,
        "#04600Fふ～ん、そこに前の家があるんだ？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0156
    ChrTalk(
        0x101,
        (
            "#12P#00005Fそうか、マリーは始めから\x01",
            "家に帰ろうとしていたんだ……！\x02\x03",

            "#00001Fただし、新しい家ではなく、\x01",
            "前に暮らしてた住宅街の家の方に。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x109,
        (
            "#12P#10103Fなるほど、確かに\x01",
            "それなら筋は通りますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x105,
        (
            "#12P#10303Fどちらかというと犬は人に、\x01",
            "猫は家に馴染むというからね。\x02\x03",

            "#10300F飼い主とはぐれた後の\x01",
            "猫の行動パターンを考えれば\x01",
            "すぐに分かるわけか。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0x104,
        (
            "#00303F……確かにコッペなんかも\x01",
            "支援課のビルから離れねぇしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x1C,
        (
            "#04609Fあはは、そういうコト。\x02\x03",

            "#04602Fそれじゃ、先に行ってるからね♪\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x1C, 0x0, 0x1F4)
    Sleep(300)

    def lambda_6B5C():
        OP_95(0xFE, 2270, -220, -3590, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_6B5C)
    Sleep(1000)
    OP_68(1440, -1400, -13650, 3000)
    MoveCamera(27, 27, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(14300, 3000)
    OP_6F(0x79)
    SetChrFlags(0x1C, 0x80)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0161
    ChrTalk(
        0x101,
        (
            "#00005Fま、まさか……\x01",
            "首を突っ込むつもりなのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x105,
        (
            "#12P#10304Fフフ、みたいだね。\x02\x03",

            "#10300Fまさに気まぐれな仔猫……\x01",
            "いや、虎の子というべきかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x109,
        "#6P#10106F洒落になってないんだけど……\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x102,
        (
            "#00106Fう、うーん……\x01",
            "どうしたものかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0x104,
        (
            "#00303F……ま、ドンパチが絡まなきゃ\x01",
            "そこまで危険なヤツじゃねぇ。\x02\x03",

            "#00300Fすぐに飽きるかもしれねぇし、\x01",
            "様子を見てみるとしようぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        (
            "#00000F分かった……\x01",
            "俺たちも早く住宅街に行こう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_4C(0xB, 0xFF)
    SetScenarioFlags(0x155, 1)
    OP_29(0x74, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, 2000, -3000, -11920, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_29_5B4D end

    def Function_30_6E13(): pass

    label("Function_30_6E13")

    OP_95(0x101, 750, -3000, -12700, 2000, 0x0)
    OP_93(0x101, 0x5A, 0x1F4)
    Return()

    # Function_30_6E13 end

    def Function_31_6E2F(): pass

    label("Function_31_6E2F")

    OP_95(0x102, 2530, -3000, -11630, 2000, 0x0)
    OP_93(0x102, 0xB4, 0x1F4)
    Return()

    # Function_31_6E2F end

    def Function_32_6E4B(): pass

    label("Function_32_6E4B")

    OP_95(0x104, 3790, -3000, -12940, 2000, 0x0)
    OP_93(0x104, 0x10E, 0x1F4)
    Return()

    # Function_32_6E4B end

    def Function_33_6E67(): pass

    label("Function_33_6E67")

    OP_95(0x109, 1400, -3000, -14510, 2000, 0x0)
    OP_93(0x109, 0x2D, 0x1F4)
    Return()

    # Function_33_6E67 end

    def Function_34_6E83(): pass

    label("Function_34_6E83")

    OP_95(0x105, 3200, -3000, -14560, 2000, 0x0)
    OP_93(0x105, 0x13B, 0x1F4)
    Return()

    # Function_34_6E83 end

    def Function_35_6E9F(): pass

    label("Function_35_6E9F")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72D2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7298")

    #C0167
    ChrTalk(
        0x1A2,
        "つりおう倶楽部……？\x02",
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#00000Fああ、それは\x01",
            "釣皇#4Rちょうおう#倶楽部って読むんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x1A2,
        (
            "フンッ、よく分からないけど\x01",
            "釣りバカどものあつまりってワケか。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x1A2,
        (
            "クロスベルにも、\x01",
            "おなじようなジンシュがいるんだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x1A2, 500)
    Sleep(300)

    #C0171
    ChrTalk(
        0x102,
        "#00105Fということは、共和国にも？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x1A2, 0x102, 500)
    Sleep(300)

    #C0172
    ChrTalk(
        0x1A2,
        "ええ、これがいるんですよ。\x02",
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x1A2,
        (
            "ちなみにおじいさまも\x01",
            "釣りをたしなむのですが、\x01",
            "正直ボクには理解できません。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x1A2,
        (
            "だってサカナをとるなら\x01",
            "アミをつかうのが\x01",
            "イチバン効率的ですからね。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 6)), scpexpr(EXPR_END)), "loc_713D")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_70EE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_70EE)
    Sleep(50)

    def lambda_70FE():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_70FE)
    Sleep(50)

    def lambda_710E():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_710E)
    Sleep(300)

    #C0175
    ChrTalk(
        0x104,
        "#00306F身も蓋もねえな……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7290")

    label("loc_713D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C4, 7)), scpexpr(EXPR_END)), "loc_71E9")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7196():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7196)
    Sleep(50)

    def lambda_71A6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_71A6)
    Sleep(50)

    def lambda_71B6():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_71B6)
    Sleep(300)

    #C0176
    ChrTalk(
        0x109,
        "#10106F身も蓋もないですね……\x02",
    )

    CloseMessageWindow()
    Jump("loc_7290")

    label("loc_71E9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 0)), scpexpr(EXPR_END)), "loc_7290")
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_7242():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_7242)
    Sleep(50)

    def lambda_7252():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_7252)
    Sleep(50)

    def lambda_7262():
        TurnDirection(0xFE, 0x1A2, 500)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7262)
    Sleep(300)

    #C0177
    ChrTalk(
        0x105,
        "#10304Fフフ、身も蓋もないね。\x02",
    )

    CloseMessageWindow()

    label("loc_7290")

    SetScenarioFlags(0x1, 6)
    Jump("loc_72CD")

    label("loc_7298")


    #C0178
    ChrTalk(
        0x1A2,
        (
            "こんなトコロに興味はないぞ。\x01",
            "他の場所に行こう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_72CD")

    Jump("loc_7597")

    label("loc_72D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x131, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x132, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_72E8")
    Call(0, 26)
    Jump("loc_7597")

    label("loc_72E8")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x13F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_74DD")
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0179
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっており、\x01",
            "メッセージプレートが付いている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0180
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～只今、準備中～　　\x01",
            "　　　――釣皇#4Rちょうおう#倶楽部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0181
    ChrTalk(
        0x101,
        (
            "#00005F準備中、か。\x01",
            "でも《釣皇倶楽部》って……？\x02",
        )
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0x102,
        (
            "#00105Fここって、ロイドが入ってた\x01",
            "《釣公師団》の建物よね。\x02\x03",

            "#00100F他のメンバーの方たちからは\x01",
            "何も聞かされていないの？\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x101,
        (
            "#00003Fああ、最近忙しくて\x01",
            "釣りどころじゃなかったからさ。\x02\x03",

            "#00000F鍵も閉まってるみたいだし、\x01",
            "改めて出直すか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x13F, 5)
    Jump("loc_7597")

    label("loc_74DD")

    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0184
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉には鍵が掛かっており、\x01",
            "メッセージプレートが付いている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0185
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "～只今、準備中～　　\x01",
            "　　　――釣皇#4Rちょうおう#倶楽部\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_7597")

    TalkEnd(0xFF)
    Return()

    # Function_35_6E9F end

    def Function_36_759B(): pass

    label("Function_36_759B")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7702")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_768E")

    #C0186
    ChrTalk(
        0x1A2,
        "ん、ここはアパートか？\x02",
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x1A2,
        (
            "何か面白いものでも\x01",
            "あったりするのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x101,
        (
            "#00000Fいや、別にそういう\x01",
            "わけじゃないんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x1A2,
        (
            "フン、なら入る意味はないだろう。\x01",
            "さっさと次へ行ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_7702")

    label("loc_768E")


    #C0190
    ChrTalk(
        0x1A2,
        (
            "ボクには、とくに用事もなく\x01",
            "他人の住居にズカズカ\x01",
            "押しはいるシュミはないぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x1A2,
        "ほら、さっさと次へ行ってくれ。\x02",
    )

    CloseMessageWindow()

    label("loc_7702")

    TalkEnd(0xFF)
    Return()

    # Function_36_759B end

    def Function_37_7706(): pass

    label("Function_37_7706")

    EventBegin(0x2)
    SetChrName("")

    #A0192
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東方風の地蔵が奉られている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7886")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1DC, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7883")

    #C0193
    ChrTalk(
        0x1A2,
        (
            "地蔵か――\x01",
            "ほんと、まるで東方人街だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        "#00005Fやはり、そっちには沢山あるのか？\x02",
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x1A2,
        (
            "まあな、火焼け地蔵やら、\x01",
            "とげぬき地蔵やら、ご利益に応じて\x01",
            "いろんな種類があるぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x1A2,
        (
            "ま、ボクはそんな\x01",
            "目にみえないご利益なんてモノは\x01",
            "信じちゃいないけどな。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x101,
        "#00006Fそ、そうか……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1DC, 4)
    EventEnd(0x3)
    Return()

    label("loc_7883")

    EventEnd(0x3)
    Return()

    label("loc_7886")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B01")

    #C0198
    ChrTalk(
        0x101,
        (
            "#00000Fここの地蔵……\x01",
            "いつも丁寧に掃除されてるよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x102,
        (
            "#00100F誰かが熱心にお参りされて\x01",
            "いるみたいよね。\x02\x03",

            "せっかくだし、私たちも\x01",
            "作ったお料理を供えてみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_79D0")

    #C0200
    ChrTalk(
        0x105,
        (
            "#10300Fへえ、支援課って\x01",
            "そんな事までするんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x101,
        (
            "#00000Fはは……いつもって訳じゃないけど。\x01",
            "料理の練習にもなりそうだろ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7A08")

    label("loc_79D0")


    #C0202
    ChrTalk(
        0x104,
        (
            "#00300Fま、やってみるか。\x01",
            "料理の練習にもなんだろ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7A08")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_7A9B")

    #C0203
    ChrTalk(
        0x109,
        (
            "#10100Fいいですね、賛成です！\x01",
            "目標があった方が\x01",
            "上達できそうですし……\x02\x03",

            "上手にできた料理があれば\x01",
            "持ってきてみましょうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7AFE")

    label("loc_7A9B")


    #C0204
    ChrTalk(
        0x103,
        (
            "#00200F目標があった方が\x01",
            "上達が早いものです。\x02\x03",

            "上手にできた料理があれば\x01",
            "持ってきてみましょう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7AFE")

    SetScenarioFlags(0x20B, 0)

    label("loc_7B01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AA7")
    Call(0, 38)
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B6F")

    #C0205
    ChrTalk(
        0x101,
        (
            "#0000Fお供えするのに良さそうな\x01",
            "料理は今は無いな。\x02\x03",

            "今度持ってきてみよう。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_7B6F")

    Call(0, 39)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_END)), "loc_7B92")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B8D")
    Call(0, 40)
    Return()

    label("loc_7B8D")

    Jump("loc_9AA7")

    label("loc_7B92")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7FBE")
    SetChrName("")

    #A0206
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "小包と共に、手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0207
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いつも料理を供えて下さる方、\x01",
            "このお地蔵様にたくさんの料理を供えていただいて、\x01",
            "本当にありがとうございました。\x02",
        )
    )

    CloseMessageWindow()

    #A0208
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "実は私は、幼い頃父とこの辺りに暮らしておりまして、\x01",
            "その時分より毎日手を合わせていたものですから\x01",
            "このお地蔵様にはとても思い入れがあったのです。\x01",
            "今ではお参りしてくださる方も\x01",
            "めっきり居なくなってしまいましたが、\x01",
            "あなた様のような心温かい方がいらっしゃった事に\x01",
            "密かに嬉しく思い、何か救われた気持ちすら致しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0209
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自分以外にも同じ志をもった誰かがいるというのは\x01",
            "とても心強いことなのですね。\x01",
            "また長々と失礼いたしました。\x01",
            "ほんの粗品ですが、どうか感謝の品を\x01",
            "お受け取り下さい。\x02",
        )
    )

    CloseMessageWindow()

    #A0210
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いまだあなた様に直接お会いできていないことが\x01",
            "残念ですが、私もまだまだ健康らしく、\x01",
            "こうして毎日欠かさずお参りに来ることができます。\x01",
            "あなた様とも、いずれ会えるかもしれませんね。\x01\x01",
            "　　　　　　～見知らぬあなた様の隣人より\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrName("")

    #A0211
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "小包の中からはティアラルの薬が出てきた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0212
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "２個を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F6, 2)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 6)
    SetScenarioFlags(0x2, 0)
    Jump("loc_9AA7")

    label("loc_7FBE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x16), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_839D")
    SetChrName("")

    #A0213
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティアラの薬と共に、\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0214
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "強い日差しに青草がぐんぐんと伸び、\x01",
            "いよいよ夏の気配がやってきたように思います。\x01",
            "いつも料理を供えて下さる方も\x01",
            "日々ご健勝のこととお慶び申し上げます。\x02",
        )
    )

    CloseMessageWindow()

    #A0215
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "私の方はと言いますと、先日役所に立ち寄った折、\x01",
            "偶然に学生時代の知己と会う機会がありました。\x01",
            "彼女は長くクロスベルを離れていたのですが\x01",
            "息子夫婦の転勤を機に戻ってきたとの事で、\x01",
            "本当にばったりと出会ったものですから、２人して\x01",
            "もう大いに驚いた次第です。\x02",
        )
    )

    CloseMessageWindow()

    #A0216
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "若い頃に気心が通じていると、年をとっても\x01",
            "変わらないものですね。長く音信普通だったことも忘れ\x01",
            "あの年はあれが流行った、戦争もあって大変だったと、\x01",
            "思い出話に花を咲かせてしまいました。\x02",
        )
    )

    CloseMessageWindow()

    #A0217
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "偶然にこのような幸運にめぐり合えたのは\x01",
            "これもお地蔵様の計らいかもしれませんね。\x01",
            "またつまらない話に付き合わせてしまいましたが、\x01",
            "あなた様のご健康を祈りつつ、\x01",
            "筆を置かせていただきたいと思います。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0218
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 5)
    Jump("loc_9AA7")

    label("loc_839D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8729")
    SetChrName("")

    #A0219
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティアラの薬と共に、\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0220
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いつも料理を供えて下さる方、\x01",
            "本日はいかがお過ごしでしょうか。\x01",
            "またお地蔵様のお参りに来てくださったようで\x01",
            "本当に、いつもありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #A0221
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "先日、台所に立った段になって\x01",
            "いつも供えられている美味しそうな料理のことを\x01",
            "思い出し、あの品を作ってみよう、と\x01",
            "不意に思い立ってしまった次第です。\x02",
        )
    )

    CloseMessageWindow()

    #A0222
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "料理は幼き頃から母に厳しく躾けられましたし、\x01",
            "平気だろうと意気込んだはよかったのですが\x01",
            "やはり物事、そう上手くは運ばないものですね。\x01",
            "大騒ぎした挙句できたのは、いつもと少し味付けのちがう\x01",
            "クリームシチューのようなものでした。\x01",
            "家の者は美味しいと言ってくれたのですが。\x02",
        )
    )

    CloseMessageWindow()

    #A0223
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "事件の絶えない世の中ですが、\x01",
            "こうして毎日を暮らしていけることを\x01",
            "深く感謝したいものです。\x01",
            "どうかあなた様にも穏やかな日々が訪れますように。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0224
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 4)
    Jump("loc_9AA7")

    label("loc_8729")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8AB3")
    SetChrName("")

    #A0225
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティアラの薬と共に、\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0226
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "この季節、少し雨の多い日々が続きますが\x01",
            "いかがお過ごしでしょうか。\x01",
            "いつも料理を供えて下さる方なら\x01",
            "きっと読んでくださるだろうと思い、\x01",
            "また勝手ながら筆をとらせて頂いた次第です。\x02",
        )
    )

    CloseMessageWindow()

    #A0227
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "先日の日中、賑やかな通りに目をやりますと\x01",
            "元気な子供たちが楽しそうに駆け回っているのを\x01",
            "見ることがありました。\x01",
            "この辺りではよく見る子達なのですが、\x01",
            "毎日仲がよく、ほほえましく思ってしまいます。\x02",
        )
    )

    CloseMessageWindow()

    #A0228
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "世間では何かと耳目を集めるクロスベルですが、\x01",
            "子供たちの健やかな成長こそが\x01",
            "この街のなによりの宝物ではないか、などと\x01",
            "徒然と考えを巡らせた次第でした。\x01",
            "本当に、穏やかな日々がいつまでも続けばよいですね。\x02",
        )
    )

    CloseMessageWindow()

    #A0229
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "最後になってしまいましたが、\x01",
            "また勝手ながら粗品を用意させて頂きました。\x01",
            "どうか何かのお役に立てていただければ幸いです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0230
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 3)
    Jump("loc_9AA7")

    label("loc_8AB3")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_8CAE")
    SetChrName("")

    #A0231
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティアラの薬と共に、\x01",
            "手紙が添えられている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0232
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "いつも料理を供えて下さる方、\x01",
            "ありがとうございます。\x01",
            "私以外にも熱心にお参りしてくださる\x01",
            "方がいて、美味しそうなお供え物を見るたび\x01",
            "ほっと心温まる日々が続いておりました。\x02",
        )
    )

    CloseMessageWindow()

    #A0233
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "どこのどなたか存じませんが、\x01",
            "本日は勝手ながら粗品を用意させて頂きました。\x01",
            "日頃のご篤信によるものと思って\x01",
            "どうかお受け取りください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0234
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x1F5, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x20B, 2)
    Jump("loc_9AA7")

    label("loc_8CAE")

    SetChrName("")

    #A0235
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "上手にできた料理を供えますか？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_8CE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AA7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D38")
    MenuCmd(1, 1, "天上麺≪日輪≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_8D2E")
    Call(2, 6)

    label("loc_8D2E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8D71")
    MenuCmd(1, 1, "神仙麻婆≪麒麟≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_8D67")
    Call(2, 6)

    label("loc_8D67")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8D71")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DA4")
    MenuCmd(1, 1, "天下一炒飯")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_8D9A")
    Call(2, 6)

    label("loc_8D9A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DA4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8DDF")
    MenuCmd(1, 1, "極上ステーキ≪剛≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_8DD5")
    Call(2, 6)

    label("loc_8DD5")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8DDF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E1A")
    MenuCmd(1, 1, "三日煮込みシチュー")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_8E10")
    Call(2, 6)

    label("loc_8E10")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E1A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E51")
    MenuCmd(1, 1, "大地鍋≪爛漫≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_8E47")
    Call(2, 6)

    label("loc_8E47")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8E88")
    MenuCmd(1, 1, "天河鍋≪瑞雲≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_8E7E")
    Call(2, 6)

    label("loc_8E7E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8E88")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EC1")
    MenuCmd(1, 1, "特急フライ≪疾≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_8EB7")
    Call(2, 6)

    label("loc_8EB7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8EFA")
    MenuCmd(1, 1, "メガ盛オムライス")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_8EF0")
    Call(2, 6)

    label("loc_8EF0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8EFA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F31")
    MenuCmd(1, 1, "翠玉麺≪癒し≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_8F27")
    Call(2, 6)

    label("loc_8F27")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8F68")
    MenuCmd(1, 1, "ダブルバーガー")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_8F5E")
    Call(2, 6)

    label("loc_8F5E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8F68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FA3")
    MenuCmd(1, 1, "クワトロチーズピザ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_8F99")
    Call(2, 6)

    label("loc_8F99")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8FDA")
    MenuCmd(1, 1, "パワフルサンド")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_8FD0")
    Call(2, 6)

    label("loc_8FD0")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_8FDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9011")
    MenuCmd(1, 1, "真心弁当≪誠≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_9007")
    Call(2, 6)

    label("loc_9007")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9011")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_904C")
    MenuCmd(1, 1, "ブリリアントスープ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_9042")
    Call(2, 6)

    label("loc_9042")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_904C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9087")
    MenuCmd(1, 1, "ワンダーキャンディ")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_907D")
    Call(2, 6)

    label("loc_907D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9087")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90BC")
    MenuCmd(1, 1, "天菓≪夜月≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_90B2")
    Call(2, 6)

    label("loc_90B2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90BC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_90F1")
    MenuCmd(1, 1, "宝菓≪白雪≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_90E7")
    Call(2, 6)

    label("loc_90E7")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_90F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9126")
    MenuCmd(1, 1, "氷菓≪七彩≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_911C")
    Call(2, 6)

    label("loc_911C")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9126")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_915B")
    MenuCmd(1, 1, "絶菓≪瞬動≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_9151")
    Call(2, 6)

    label("loc_9151")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_915B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9190")
    MenuCmd(1, 1, "玉露≪緑風≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_9186")
    Call(2, 6)

    label("loc_9186")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9190")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91C5")
    MenuCmd(1, 1, "甘露≪紫紺≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_91BB")
    Call(2, 6)

    label("loc_91BB")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_91FE")
    MenuCmd(1, 1, "黒茶≪夢魔殺し≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_91F4")
    Call(2, 6)

    label("loc_91F4")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_91FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9235")
    MenuCmd(1, 1, "秘水≪桃源郷≫")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_922B")
    Call(2, 6)

    label("loc_922B")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9235")

    MenuCmd(1, 1, "やめる")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_GE), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9279")
    Sleep(500)
    Jump("loc_9AA2")

    label("loc_9279")

    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92E4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92DA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x190, 1)
    SetScenarioFlags(0x208, 0)

    #A0236
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x190),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_92DA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_92E4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9330")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9326")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x193, 1)
    SetScenarioFlags(0x208, 1)

    #A0237
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x193),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9326")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9330")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_937C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9372")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x196, 1)
    SetScenarioFlags(0x208, 2)

    #A0238
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x196),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9372")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_937C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_93C8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93BE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x199, 1)
    SetScenarioFlags(0x208, 3)

    #A0239
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x199),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_93BE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_93C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9414")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_940A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19C, 1)
    SetScenarioFlags(0x208, 4)

    #A0240
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_940A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9460")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9456")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x19F, 1)
    SetScenarioFlags(0x208, 5)

    #A0241
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x19F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9456")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9460")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94AC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94A2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A2, 1)
    SetScenarioFlags(0x208, 6)

    #A0242
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_94A2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_94F8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_94EE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A5, 1)
    SetScenarioFlags(0x208, 7)

    #A0243
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_94EE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_94F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9544")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_953A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1A8, 1)
    SetScenarioFlags(0x209, 0)

    #A0244
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_953A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9544")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9590")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9586")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AB, 1)
    SetScenarioFlags(0x209, 1)

    #A0245
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9586")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9590")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_95DC")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_95D2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1AE, 1)
    SetScenarioFlags(0x209, 2)

    #A0246
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AE),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_95D2")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_95DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9628")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_961E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B1, 1)
    SetScenarioFlags(0x209, 3)

    #A0247
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_961E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9628")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9674")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_966A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B4, 1)
    SetScenarioFlags(0x209, 4)

    #A0248
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B4),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_966A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9674")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_96C0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96B6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1B7, 1)
    SetScenarioFlags(0x209, 5)

    #A0249
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_96B6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_96C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_970C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9702")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BA, 1)
    SetScenarioFlags(0x209, 6)

    #A0250
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9702")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_970C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9758")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_974E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1BD, 1)
    SetScenarioFlags(0x209, 7)

    #A0251
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1BD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_974E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9758")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97A4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_979A")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C0, 1)
    SetScenarioFlags(0x20A, 0)

    #A0252
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C0),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_979A")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_97F0")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C3, 1)
    SetScenarioFlags(0x20A, 1)

    #A0253
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_97E6")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_97F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_983C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9832")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C6, 1)
    SetScenarioFlags(0x20A, 2)

    #A0254
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9832")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_983C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9888")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_987E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1C9, 1)
    SetScenarioFlags(0x20A, 3)

    #A0255
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1C9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_987E")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9888")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_98D4")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98CA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CC, 1)
    SetScenarioFlags(0x20A, 4)

    #A0256
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_98CA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_98D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9920")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9916")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1CF, 1)
    SetScenarioFlags(0x20A, 5)

    #A0257
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1CF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9916")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9920")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_996C")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9962")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D2, 1)
    SetScenarioFlags(0x20A, 6)

    #A0258
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D2),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_9962")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_996C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_99B8")
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_99AE")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SubItemNumber(0x1D5, 1)
    SetScenarioFlags(0x20A, 7)

    #A0259
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1D5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を供えた。\x02",
        )
    )


    label("loc_99AE")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_99B8")

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9AA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20B, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A9F")

    #C0260
    ChrTalk(
        0x101,
        (
            "#00000Fこれでよし、と。\x01",
            "……また持ってきてみようかな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_9A9C")

    #C0261
    ChrTalk(
        0x102,
        (
            "#00100Fあまり同じ料理ばかりだと\x01",
            "失礼でしょうし、\x01",
            "一品一回くらいが良さそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        "#00000Fああ、そうするか。\x02",
    )

    CloseMessageWindow()

    label("loc_9A9C")

    SetScenarioFlags(0x20B, 1)

    label("loc_9A9F")

    SetScenarioFlags(0x2, 0)

    label("loc_9AA2")

    Jump("loc_8CE5")

    label("loc_9AA7")

    EventEnd(0x3)
    Return()

    # Function_37_7706 end

    def Function_38_9AAA(): pass

    label("Function_38_9AAA")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x190, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9ACD")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9ACD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x193, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AE6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x196, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9AFF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9AFF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x199, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B18")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B18")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19C, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B31")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x19F, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B4A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B63")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B7C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1A8, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9B95")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9B95")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AB, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BAE")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1AE, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BC7")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B1, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BE0")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BE0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B4, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9BF9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9BF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1B7, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C12")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C12")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BA, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C2B")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C2B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1BD, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C44")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C44")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C0, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C5D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C3, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C76")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C6, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9C8F")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9C8F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1C9, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CA8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CA8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CC, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CC1")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CC1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1CF, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CDA")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CDA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D2, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9CF3")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x1D5, 0x0)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_9D0C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D0C")

    Return()

    # Function_38_9AAA end

    def Function_39_9D0D(): pass

    label("Function_39_9D0D")

    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 0)), scpexpr(EXPR_END)), "loc_9D2A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 1)), scpexpr(EXPR_END)), "loc_9D3D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 2)), scpexpr(EXPR_END)), "loc_9D50")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 3)), scpexpr(EXPR_END)), "loc_9D63")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 4)), scpexpr(EXPR_END)), "loc_9D76")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D76")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 5)), scpexpr(EXPR_END)), "loc_9D89")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D89")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 6)), scpexpr(EXPR_END)), "loc_9D9C")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9D9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x208, 7)), scpexpr(EXPR_END)), "loc_9DAF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DAF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 0)), scpexpr(EXPR_END)), "loc_9DC2")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 1)), scpexpr(EXPR_END)), "loc_9DD5")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 2)), scpexpr(EXPR_END)), "loc_9DE8")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 3)), scpexpr(EXPR_END)), "loc_9DFB")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9DFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 4)), scpexpr(EXPR_END)), "loc_9E0E")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 5)), scpexpr(EXPR_END)), "loc_9E21")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 6)), scpexpr(EXPR_END)), "loc_9E34")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E34")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x209, 7)), scpexpr(EXPR_END)), "loc_9E47")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 0)), scpexpr(EXPR_END)), "loc_9E5A")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 1)), scpexpr(EXPR_END)), "loc_9E6D")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E6D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 2)), scpexpr(EXPR_END)), "loc_9E80")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 3)), scpexpr(EXPR_END)), "loc_9E93")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9E93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 4)), scpexpr(EXPR_END)), "loc_9EA6")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EA6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 5)), scpexpr(EXPR_END)), "loc_9EB9")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EB9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 6)), scpexpr(EXPR_END)), "loc_9ECC")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9ECC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20A, 7)), scpexpr(EXPR_END)), "loc_9EDF")
    RunExpression(0x1, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_9EDF")

    Return()

    # Function_39_9D0D end

    def Function_40_9EE0(): pass

    label("Function_40_9EE0")

    EventBegin(0x0)
    Fade(1000)
    OP_68(14950, 1450, 2880, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14180, 0)
    SetChrPos(0x101, 16200, -300, 2570, 0)
    SetChrPos(0x102, 17600, -300, 2700, 0)
    SetChrPos(0x103, 15750, -300, 1260, 0)
    SetChrPos(0x104, 17570, -300, 1120, 0)
    SetChrPos(0xF4, 15720, -300, 20, 0)
    SetChrPos(0xF5, 16940, -300, 30, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xD, 0x80)
    LoadChrToIndex("chr/ch23300.itc", 0x1E)
    SetChrChipByIndex(0x2A, 0x1E)
    SetChrSubChip(0x2A, 0x0)
    ClearChrFlags(0x2A, 0x80)
    SetChrFlags(0x2A, 0x8000)
    SetChrPos(0x2A, -3400, -300, 1670, 0)
    OP_0D()

    #C0263
    ChrTalk(
        0x101,
        (
            "#00000F（……料理をお供えしてた地蔵か……\x01",
            "  願掛けってわけじゃないけど……）\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_93(0x101, 0xB4, 0x1F4)

    #C0264
    ChrTalk(
        0x101,
        (
            "#00002Fなあみんな、折角だし\x01",
            "出かける前にお参りしていかないか？\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)

    #C0265
    ChrTalk(
        0x102,
        "#00100Fあら、いいんじゃない？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A0DD")

    #C0266
    ChrTalk(
        0x109,
        (
            "#10100Fキーアちゃんの救出祈願ですね。\x01",
            "……自分も賛成です！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A0DD")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A127")

    #C0267
    ChrTalk(
        0x10A,
        (
            "#00606Fフン、寄り道をしているヒマは\x01",
            "無いはずだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A127")


    #C0268
    ChrTalk(
        0x103,
        (
            "#00202Fまあ、時間も取りませんし。\x01",
            "こういう事は気持ちの問題ですから。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x104,
        (
            "#00300F今後の士気を考えると\x01",
            "精神統一ってのも悪くないだろ。\x02\x03",

            "#00309Fうっし、やってみようぜ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0x0, 0x1F4)

    #C0270
    ChrTalk(
        0x102,
        (
            "#00100F東方の風習だと、こうやって\x01",
            "手を合わせるのよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x0, 0x1F4)

    #C0271
    ChrTalk(
        0x101,
        "#00005Fおっと、こうか……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A28D")

    #C0272
    ChrTalk(
        0x105,
        (
            "#10402Fフフ、肩を落として\x01",
            "４５度くらいに作るといいらしいよ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A28D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A33A")

    #C0273
    ChrTalk(
        0x106,
        (
            "#10702F本当は色々としきたりが\x01",
            "あるんですけど……\x02\x03",

            "#10704F今は七耀教会でお祈りをするのと\x01",
            "同じ要領でいいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0274
    ChrTalk(
        0x101,
        "#00000Fわかった、やってみるよ。\x02",
    )

    CloseMessageWindow()

    label("loc_A33A")

    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF4, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0xF5, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(1000)
    SetChrName("")

    #A0275
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイド達は両手を合わせて目を閉じ、\x01",
            "地蔵に祈りを捧げた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(1000)
    Sound(491, 0, 100, 0)
    Sleep(300)
    Sound(491, 0, 80, 0)
    Sleep(500)

    #N0276
    NpcTalk(
        0x2A,
        "声",
        (
            "あらあら、ごめんなさいね。\x01",
            "私ったら耳が遠くって。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    Sleep(500)
    OP_68(-3070, 1450, 2110, 0)
    MoveCamera(44, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14180, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    OP_93(0x2A, 0x5A, 0x1F4)
    Sleep(100)

    def lambda_A498():
        OP_95(0xFE, 12120, -300, 1430, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A498)
    Sleep(1000)
    OP_68(12510, 1450, 1570, 8000)
    MoveCamera(57, 25, 0, 8000)
    Sleep(4000)
    WaitChrThread(0x2A, 1)
    Sleep(500)

    #C0277
    ChrTalk(
        0x2A,
        "あら、あなたたち……\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0xF4)
    OP_64(0xF5)
    Sleep(500)

    def lambda_A50D():

        label("loc_A50D")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A50D")

    QueueWorkItem2(0x101, 2, lambda_A50D)
    Sleep(50)

    def lambda_A522():

        label("loc_A522")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A522")

    QueueWorkItem2(0x102, 2, lambda_A522)
    Sleep(50)

    def lambda_A537():

        label("loc_A537")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A537")

    QueueWorkItem2(0x103, 2, lambda_A537)
    Sleep(50)

    def lambda_A54C():

        label("loc_A54C")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A54C")

    QueueWorkItem2(0x104, 2, lambda_A54C)
    Sleep(50)

    def lambda_A561():

        label("loc_A561")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A561")

    QueueWorkItem2(0xF4, 2, lambda_A561)
    Sleep(50)

    def lambda_A576():

        label("loc_A576")

        TurnDirection(0xFE, 0x2A, 400)
        Yield()
        Jump("loc_A576")

    QueueWorkItem2(0xF5, 2, lambda_A576)
    Sleep(50)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0278
    ChrTalk(
        0x102,
        "#00105F……え？\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x2A,
        (
            "もしかしてだけれど……お地蔵様に\x01",
            "料理をお供えしてくれていたのは、\x01",
            "あなた達かしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0280
    ChrTalk(
        0x101,
        "#00005Fあっ……ってことは……！？\x02",
    )

    CloseMessageWindow()

    #C0281
    ChrTalk(
        0x103,
        "#00205Fもしかして、あの手紙の主は……\x02",
    )

    CloseMessageWindow()
    OP_63(0x2A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0282
    ChrTalk(
        0x2A,
        "あらまあ、じゃあそうなのね！？\x02",
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x2A,
        (
            "でもこんなに可愛らしい子達が\x01",
            "大勢だったなんて……てっきり\x01",
            "私くらいの年の人かと思っていたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0284
    ChrTalk(
        0x101,
        (
            "#00002Fあはは、実は料理の練習ついでに\x01",
            "みんなでお供えをしていまして……\x02",
        )
    )

    CloseMessageWindow()

    #C0285
    ChrTalk(
        0x104,
        (
            "#00300Fいやー、こっちこそ驚きッス。\x01",
            "確か……旧市街で時々見かける\x01",
            "お婆さんっすよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0286
    ChrTalk(
        0x102,
        (
            "#00104Fお手紙がとても上品で\x01",
            "達筆でいらっしゃるから\x01",
            "年配の方かもとは思っていたけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0287
    ChrTalk(
        0x2A,
        (
            "うふふ、いつもお手紙を書くのが\x01",
            "遅くてごめんなさいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0288
    ChrTalk(
        0x2A,
        (
            "でも、そうだったの……\x01",
            "本当に世の中、\x01",
            "色んなことがあるものねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    def lambda_A903():
        OP_95(0xFE, 14600, -300, 3080, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A903)
    Sleep(800)
    EndChrThread(0x101, 0x2)
    OP_93(0x101, 0x0, 0x12C)

    def lambda_A92B():
        OP_96(0xFE, 0x3F34, 0xFFFFFED4, 0x898, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A92B)
    Sleep(50)
    EndChrThread(0x103, 0x2)
    OP_93(0x103, 0x0, 0x0)

    def lambda_A953():
        OP_96(0xFE, 0x3B92, 0xFFFFFED4, 0x3E8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_A953)
    FadeToDark(2000, 0, -1)
    Sleep(50)
    EndChrThread(0xF4, 0x2)

    def lambda_A97E():
        OP_96(0xFE, 0x3D68, 0xFFFFFED4, 0xFFFFFF9C, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 1, lambda_A97E)
    WaitChrThread(0x2A, 1)

    def lambda_A99C():
        OP_95(0xFE, 17260, -300, 3820, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_A99C)
    OP_0D()
    Sleep(1000)
    OP_68(14150, 1450, 840, 0)
    MoveCamera(62, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(12970, 0)
    SetChrPos(0x2A, 17260, -300, 3820, 0)
    SetChrPos(0x101, 16000, -300, 1250, 0)
    SetChrPos(0x102, 18000, -300, 1340, 0)
    SetChrPos(0x103, 14800, -300, 50, 0)
    SetChrPos(0x104, 18800, -300, 370, 0)
    SetChrPos(0xF4, 16400, -300, -650, 0)
    SetChrPos(0xF5, 18200, -300, -730, 0)
    SetChrName("")

    #A0289
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "パオラは地蔵に向かって静かに手を合わせた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetCameraDistance(12770, 1000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_63(0x2A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x1)
    Sleep(2000)

    #C0290
    ChrTalk(
        0x2A,
        (
            "このお地蔵様はね、クロスベルの\x01",
            "動乱の時代をずっと経験していらっしゃって\x01",
            "一度は取り壊された事もあったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x2A,
        (
            "それでも、この街の人たちの手で\x01",
            "何度も立ち直っていらっしゃるの。\x02",
        )
    )

    CloseMessageWindow()

    #C0292
    ChrTalk(
        0x2A,
        (
            "……最近はお参りする人も\x01",
            "めっきり減ってしまったけど……\x01",
            "ふふっ、心配なんていらなかったようねぇ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0xB4, 0x190)

    #C0293
    ChrTalk(
        0x2A,
        (
            "そうだわ、私、\x01",
            "ちょうどいい物を持っているの。\x02",
        )
    )

    CloseMessageWindow()

    #C0294
    ChrTalk(
        0x2A,
        (
            "頂き物で悪いんだけど……\x01",
            "よかったら受け取ってくれないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x101,
        "#00005Fええと、ですが……\x02",
    )

    CloseMessageWindow()

    #C0296
    ChrTalk(
        0x2A,
        (
            "ふふっ、いいのよ。\x01",
            "ほんの気持ちばかりの品だから。\x02",
        )
    )

    CloseMessageWindow()
    OP_95(0x2A, 16010, -300, 2000, 1500, 0x0)
    TurnDirection(0x2A, 0x101, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0xEC, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AD24")
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0297
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xEC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xEC, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x2, 7)
    Jump("loc_AD71")

    label("loc_AD24")

    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0298
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x86),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x86, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_AD71")


    def lambda_AD76():
        OP_96(0xFE, 0x3E80, 0xFFFFFED4, 0xA00, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_AD76)

    def lambda_AD90():

        label("loc_AD90")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_AD90")

    QueueWorkItem2(0x101, 2, lambda_AD90)

    def lambda_ADA2():

        label("loc_ADA2")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADA2")

    QueueWorkItem2(0x102, 2, lambda_ADA2)

    def lambda_ADB4():

        label("loc_ADB4")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADB4")

    QueueWorkItem2(0x103, 2, lambda_ADB4)

    def lambda_ADC6():

        label("loc_ADC6")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADC6")

    QueueWorkItem2(0x104, 2, lambda_ADC6)

    def lambda_ADD8():

        label("loc_ADD8")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADD8")

    QueueWorkItem2(0xF4, 2, lambda_ADD8)

    def lambda_ADEA():

        label("loc_ADEA")

        TurnDirection(0xFE, 0x2A, 500)
        Yield()
        Jump("loc_ADEA")

    QueueWorkItem2(0xF5, 2, lambda_ADEA)
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
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0299
    ChrTalk(
        0x2A,
        (
            "後輩の子がくれたのだけれど、\x01",
            "私には飾っておくしかないし……\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x2A,
        (
            "……うふふ、イメルダったら。\x01",
            "本当にいつまでたっても\x01",
            "気がきかないんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x2A,
        (
            "それじゃあねぇ、あなた達。\x01",
            "また気が向いたらで構わないから、\x01",
            "お地蔵様にお参りしてあげて頂戴ね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x2A, 0x10E, 0x1F4)

    def lambda_AF9A():
        OP_95(0xFE, -1050, -300, 2150, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_AF9A)
    Sleep(5000)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x103, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0xF4, 0x2)
    EndChrThread(0xF5, 0x2)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B03C")

    #C0302
    ChrTalk(
        0x109,
        (
            "#10102Fうーん、どういうお婆ちゃん\x01",
            "だったんでしょうか。\x01",
            "随分と颯爽とした人でしたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B087")

    label("loc_B03C")


    #C0303
    ChrTalk(
        0x104,
        (
            "#00302Fはー……\x01",
            "何がどうなのかサッパリだが、\x01",
            "また颯爽としたヒトだぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B087")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B159")

    #C0304
    ChrTalk(
        0x106,
        (
            "#10702Fよく私のアパートの近くで\x01",
            "日向ぼっこをしているお婆ちゃんです。\x02\x03",

            "#10704F今は旧市街にいらっしゃいますが、\x01",
            "元は別の場所に住んでいたみたいで……\x01",
            "綺麗な方だなとは思っていましたけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B193")

    label("loc_B159")


    #C0305
    ChrTalk(
        0x103,
        (
            "#00202Fかなり高齢の方ですけど、\x01",
            "お元気そうでしたね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 7)), scpexpr(EXPR_END)), "loc_B206")

    #C0306
    ChrTalk(
        0x101,
        (
            "#00005Fこれってマスタークオーツ……\x01",
            "それにイメルダさんの名前を出して\x01",
            "後輩だって言ってたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B26D")

    label("loc_B206")


    #C0307
    ChrTalk(
        0x101,
        (
            "#00005Fこれってレアな上位クオーツ……\x01",
            "それにイメルダさんの名前を出して\x01",
            "後輩だって言ってたけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B26D")


    #C0308
    ChrTalk(
        0x102,
        (
            "#00100F本当に心優しくて\x01",
            "不思議な人だったわね。\x02\x03",

            "#00103F（そういえば……お祖父様の１つ上の世代に\x01",
            "  伝説の『社交界の華』と呼ばれる\x01",
            "  素敵な女性がいたそうだけど……）\x02\x03",

            "（……ま、まさかね。）\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B3A9")

    #C0309
    ChrTalk(
        0x10A,
        (
            "#00606F（……知らんのか、ヒヨッコどもが。\x01",
            "  その昔クロスベルで一世を風靡した\x01",
            "  有名なレディーだぞ。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B3A9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_B481")

    #C0310
    ChrTalk(
        0x105,
        (
            "#10404Fフフ、たまには願掛けも\x01",
            "してみるものだね。\x02\x03",

            "#10400Fでもリーダー、そろそろ\x01",
            "いい時間じゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x101,
        (
            "#00005Fおっと、そうだな。\x01",
            "気合も入ったことだし……\x02\x03",

            "#00000Fよし、それじゃあ行こうか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B504")

    label("loc_B481")


    #C0312
    ChrTalk(
        0x101,
        (
            "#00004Fお参りするつもりが\x01",
            "思わぬ事になったけど……\x01",
            "気合も入ったみたいだ。\x02\x03",

            "#00000Fよし、そろそろ行こうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x104,
        "#00300Fおう！\x02",
    )

    CloseMessageWindow()

    label("loc_B504")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 17130, -300, 2670, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 1, 0, 1)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, -40490, -300, 15850, 90)
    BeginChrThread(0xE, 1, 0, 6)
    EndChrThread(0x2A, 0xFF)
    SetChrFlags(0x2A, 0x80)
    OP_D7(0x1E)
    SetScenarioFlags(0x20B, 7)
    EventEnd(0x5)
    Return()

    # Function_40_9EE0 end

    def Function_41_B57D(): pass

    label("Function_41_B57D")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B6E8")
    OP_63(0x1A2, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0314
    ChrTalk(
        0x1A2,
        "ここは……？\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x102,
        (
            "#00100Fええ、クロスベル商工会の\x01",
            "会長さんのご自宅よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0316
    ChrTalk(
        0x101,
        (
            "#00000Fちょっとした縁があって\x01",
            "親しくさせてもらってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x1A2,
        "ふむ、そうだったのか。\x02",
    )

    CloseMessageWindow()

    #C0318
    ChrTalk(
        0x1A2,
        (
            "商工会の会長ともなれば、\x01",
            "当然ツァオたちも\x01",
            "一目置いているだろうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x1A2,
        (
            "何だったら、\x01",
            "挨拶しておくのもいいかもな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1C5, 3)
    OP_65(0x6, 0x1)
    SetMapObjFlags(0x3, 0x10)

    label("loc_B6E8")

    TalkEnd(0xFF)
    Return()

    # Function_41_B57D end

    def Function_42_B6EC(): pass

    label("Function_42_B6EC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch32200.itc", 0x1E)
    LoadChrToIndex("chr/ch23600.itc", 0x1F)
    LoadChrToIndex("chr/ch24200.itc", 0x20)
    SetChrChipByIndex(0x19, 0x1E)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x80)
    SetChrFlags(0x19, 0x8000)
    SetChrPos(0x19, -2200, -300, 4400, 225)
    SetChrChipByIndex(0x1A, 0x1F)
    SetChrSubChip(0x1A, 0x0)
    ClearChrFlags(0x1A, 0x80)
    SetChrFlags(0x1A, 0x8000)
    SetChrPos(0x1A, -3000, -300, 5200, 225)
    SetChrChipByIndex(0x1B, 0x20)
    SetChrSubChip(0x1B, 0x0)
    ClearChrFlags(0x1B, 0x80)
    SetChrFlags(0x1B, 0x8000)
    SetChrPos(0x1B, -1400, -300, 3600, 225)
    OP_68(-4790, 1690, 1740, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetChrPos(0x101, -3700, -300, 2600, 45)
    SetChrPos(0x102, -4650, -300, 1000, 45)
    SetChrPos(0x104, -5350, -300, 1750, 45)
    SetChrPos(0x109, -4650, -300, -100, 45)
    SetChrPos(0x105, -6350, -300, 1750, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00003F《爆釣勝負》か……\x01",
            "何だか話が大きくなりましたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0321
    ChrTalk(
        0x1A,
        "へへっ、でも楽勝ッスよ。\x02",
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x1A,
        (
            "４人の内の誰かが、\x01",
            "最終的にあのレイクロードを\x01",
            "倒せばいいんスからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x1B,
        (
            "う、う～ん……\x01",
            "正直、私は戦力にならないと\x01",
            "思いますが。\x02",
        )
    )

    CloseMessageWindow()

    #C0324
    ChrTalk(
        0x19,
        (
            "あと気になるのは、\x01",
            "『釣傑四天王』だな……\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x19,
        (
            "リトライ無制限のルールもある。\x01",
            "もちろんいつかは勝てると\x01",
            "踏んではいるが……\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x19,
        (
            "少なくとも、コパンが言うほど\x01",
            "楽な勝負ではないと思うぜ？\x02",
        )
    )

    CloseMessageWindow()

    #C0327
    ChrTalk(
        0x19,
        (
            "噂では、それぞれが\x01",
            "ウチで言う『特級釣師』以上の\x01",
            "実力を持っているらしいからなァ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0328
    ChrTalk(
        0x101,
        "#00005Fそ、そうなんですか……\x02",
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x1B,
        (
            "は、はあ……\x01",
            "やっぱり私には無理ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x1A,
        (
            "へへっ、なるほど……\x01",
            "面白くなって来たじゃないッスか。\x02",
        )
    )

    CloseMessageWindow()

    #C0331
    ChrTalk(
        0x19,
        (
            "まあ、とにかく一旦、\x01",
            "新支部に戻って作戦会議だな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0332
    ChrTalk(
        0x101,
        "#00005F新支部、ですか？\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x1B,
        (
            "ああ、ロイド君には\x01",
            "まだ言っていませんでしたね。\x02",
        )
    )

    CloseMessageWindow()

    #C0334
    ChrTalk(
        0x1B,
        (
            "実は東クロスベル街道の方で\x01",
            "支部長が新しい事務所となる建物を\x01",
            "見つけたんですよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x1B,
        (
            "数年前に打ち捨てられて以来、\x01",
            "ずっと使われていなかった\x01",
            "貸しボート小屋なんですけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0336
    ChrTalk(
        0x1A,
        (
            "狭くてボロっちいッスけど\x01",
            "近くの川で釣りだって出来るし、\x01",
            "なかなか快適な所ッスよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x19,
        (
            "ああ、まさに再出発する\x01",
            "俺たちにあつらえ向きって\x01",
            "感じの場所でなァ。\x02",
        )
    )

    CloseMessageWindow()

    #C0338
    ChrTalk(
        0x19,
        (
            "東クロスベル街道の三叉路を\x01",
            "タングラム門方面に抜けると、\x01",
            "看板が見えると思うんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x19,
        (
            "後はそいつに従って、\x01",
            "ちょいと南に下った先に\x01",
            "あるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0340
    ChrTalk(
        0x19,
        (
            "ロイド団員も、\x01",
            "暇があったら顔を出してくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x101,
        "#00000Fはい、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0342
    ChrTalk(
        0x19,
        (
            "それからロイド団員、\x01",
            "爆釣勝負は一応俺たちの方で\x01",
            "何とかするつもりだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x19,
        (
            "数は少しでも\x01",
            "多いほうがいいからな。\x01",
            "ロイド団員も頼んだぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00004Fはい、俺も好きな場所で\x01",
            "釣りが出来なくなるのは\x01",
            "御免ですからね。\x02\x03",

            "#00000F出来る限り、努力してみます。\x02",
        )
    )

    CloseMessageWindow()

    #C0345
    ChrTalk(
        0x1A,
        (
            "へへっ、ロイド団員。\x01",
            "オレも負けないッスよ～。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x1B,
        "それでは我々はこれで。\x02",
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x19,
        "そんじゃな、健闘を祈るぜ！\x02",
    )

    CloseMessageWindow()

    #C0348
    ChrTalk(
        0x101,
        "#00000Fええ、支部長たちも！\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x1B, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x19, 3, 0, 43)
    Sleep(200)
    BeginChrThread(0x1A, 3, 0, 43)
    Sleep(1000)

    def lambda_BF70():

        label("loc_BF70")

        TurnDirection(0x101, 0x1A, 500)
        Yield()
        Jump("loc_BF70")

    QueueWorkItem2(0x101, 2, lambda_BF70)

    def lambda_BF82():

        label("loc_BF82")

        TurnDirection(0x102, 0x1A, 500)
        Yield()
        Jump("loc_BF82")

    QueueWorkItem2(0x102, 2, lambda_BF82)

    def lambda_BF94():

        label("loc_BF94")

        TurnDirection(0x109, 0x1A, 500)
        Yield()
        Jump("loc_BF94")

    QueueWorkItem2(0x109, 2, lambda_BF94)

    def lambda_BFA6():

        label("loc_BFA6")

        TurnDirection(0x105, 0x1A, 500)
        Yield()
        Jump("loc_BFA6")

    QueueWorkItem2(0x105, 2, lambda_BFA6)

    def lambda_BFB8():

        label("loc_BFB8")

        TurnDirection(0x104, 0x1A, 500)
        Yield()
        Jump("loc_BFB8")

    QueueWorkItem2(0x104, 2, lambda_BFB8)
    WaitChrThread(0x1B, 3)

    #C0349
    ChrTalk(
        0x102,
        (
            "#00109F（う～ん、ロイドったら\x01",
            "  何気にノリノリね。）\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x109,
        (
            "#10100F（釣り、か……\x01",
            "  よく分からないけど熱い人たちが\x01",
            "  沢山いるんですね。）\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    EndChrThread(0x104, 0x2)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    SetScenarioFlags(0x1C0, 2)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrPos(0xD, 26200, -300, -1050, 270)
    BeginChrThread(0xD, 0, 0, 1)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrPos(0xE, -40490, -300, 15850, 90)
    BeginChrThread(0xE, 0, 0, 6)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -3700, -300, 2600, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    EventEnd(0x5)
    Return()

    # Function_42_B6EC end

    def Function_43_C0FB(): pass

    label("Function_43_C0FB")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_95(0xFE, 110, -300, 1300, 2000, 0x0)
    OP_93(0xFE, 0x5A, 0x0)
    OP_95(0xFE, 14590, -300, 1300, 2000, 0x0)
    Return()

    # Function_43_C0FB end

    def Function_44_C132(): pass

    label("Function_44_C132")

    EventBegin(0x1)
    TurnDirection(0x1A2, 0x101, 500)
    Sleep(300)

    #C0351
    ChrTalk(
        0x1A2,
        (
            "こっちを案内する必要はないぞ。\x01",
            "他の場所に行ってくれ。\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1910, -3000, -35980, 0)
    EventEnd(0x4)
    Return()

    # Function_44_C132 end

    def Function_45_C18D(): pass

    label("Function_45_C18D")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C208")

    #C0352
    ChrTalk(
        0x1A2,
        (
            "おい、こっちは\x01",
            "街の外なんじゃないか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x1A2, 500)
    Sleep(300)

    #C0353
    ChrTalk(
        0x101,
        (
            "#00000Fああ、確かにそうだ。\x01",
            "街の方に戻ろう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 1)
    Jump("loc_C244")

    label("loc_C208")


    #C0354
    ChrTalk(
        0x101,
        (
            "#00000F街道に出るわけにはいかないな。\x01",
            "街の方に戻ろう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C244")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_45_C18D end

    def Function_46_C258(): pass

    label("Function_46_C258")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C308")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C2CC")

    #C0355
    ChrTalk(
        0x101,
        (
            "#00000Fこの先は東クロスベル街道だな。\x02\x03",

            "特に用事はないし、\x01",
            "出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_C308")

    label("loc_C2CC")


    #C0356
    ChrTalk(
        0x101,
        (
            "#00000Fこっち方面に用事はない。\x01",
            "出るのは止めておこう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C308")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C3CA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C384")

    #C0357
    ChrTalk(
        0x101,
        (
            "#00001Fこの先は東クロスベル街道だな。\x02\x03",

            "今は寄り道せずに、\x01",
            "事故関連の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x2, 5)
    Jump("loc_C3CA")

    label("loc_C384")


    #C0358
    ChrTalk(
        0x101,
        (
            "#00001Fこっち方面に用事はない。\x01",
            "今は事故関連の捜査に集中しよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C42B")

    #C0359
    ChrTalk(
        0x101,
        (
            "#00001F今はとにかく\x01",
            "ランディを追いかけないと――\x01",
            "脇道にそれてる場合じゃない。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C42B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C47B")

    #C0360
    ChrTalk(
        0x101,
        (
            "#00001F今は市外に出ている場合じゃない。\x01",
            "大人しく引き返そう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C47B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C4FA")

    #C0361
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

    label("loc_C4FA")

    SetChrPos(0x0, 29390, -300, 500, 270)
    EventEnd(0x4)
    Return()

    # Function_46_C258 end

    def Function_47_C50E(): pass

    label("Function_47_C50E")

    EventBegin(0x1)

    #C0362
    ChrTalk(
        0x105,
        (
            "#10303F……ロイド、悪いけど\x01",
            "旧市街に戻るなら少しだけ\x01",
            "時間を置いてくれないか。\x02\x03",

            "#10308Fほんの少しでいいんだ。\x01",
            "流石にすぐに引き返すのは\x01",
            "ちょっと、ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x101,
        "#00003Fああ……分かった。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 1610, -3000, -35150, 0)
    EventEnd(0x4)
    Return()

    # Function_47_C50E end

    SaveToFile()

Try(main)
