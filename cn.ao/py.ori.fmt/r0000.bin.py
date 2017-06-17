from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r0000.bin",                # FileName
        "r0000",                    # MapName
        "r0000",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0000", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x01,                       # PreInitFunctionIndex
        b'\x00\xff\x03',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 4, 0, 5],
    )

    BuildStringList((
        "r0000",                  # 0
        "达德利搜查官",           # 1
        "曹",                     # 2
        "刘",                     # 3
        "黑月成员",               # 4
        "黑月成员",               # 5
        "黑月成员",               # 6
        "黑月成员",               # 7
        "黑月成员",               # 8
        "黑月成员",               # 9
        "黑月成员",               # 10
        "黑月成员",               # 11
        "黑月成员",               # 12
        "黑月成员",               # 13
        "黑月成员",               # 14
        "黑月成员",               # 15
        "黑月成员",               # 16
        "黑月成员",               # 17
        "猎兵加雷斯",             # 18
        "猎兵",                   # 19
        "猎兵",                   # 20
        "猎兵",                   # 21
        "猎兵",                   # 22
        "猎兵",                   # 23
        "猎兵",                   # 24
        "猎兵",                   # 25
        "猎兵",                   # 26
        "猎兵",                   # 27
        "猎兵",                   # 28
        "狮兽",                   # 29
        "狮兽",                   # 30
        "狮兽",                   # 31
        "偃月轮",                 # 32
        "偃月轮",                 # 33
        "巴士",                   # 34
        "黑色轿车",               # 35
        "黑色轿车",               # 36
        "黑色轿车",               # 37
        "黑色轿车",               # 38
        "黑色轿车",               # 39
        "黑色轿车",               # 40
        "总统的高级轿车",         # 41
        "凯特巡警",               # 42
        "警官",                   # 43
        "警官",                   # 44
        "警官",                   # 45
        "警官",                   # 46
        "警官",                   # 47
        "警官",                   # 48
        "警官",                   # 49
        "警官",                   # 50
        "警官",                   # 51
        "警官",                   # 52
        "SE控制",                 # 53
        "迟缓虫",                 # 54
        "凶暴角牛",               # 55
        "br0000",                 # 56
        "br0000",                 # 57
        "br0000",                 # 58
        "br0000",                 # 59
        "克洛斯贝尔市方向",       # 60
        "阿尔摩利卡村·唐古拉姆门方向",# 61
    ))

    ATBonus("ATBonus_878", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_58E8", 7,   4,   5,   0,   0,   5,   0)
    Sepith("Sepith_5900", 7,   0,   3,   9,   0,   0,   2)

    MonsterBattlePostion("MonsterBattlePostion_8D8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_8DC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8E8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8EC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8F4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_938", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_93C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_940", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_944", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_948", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_94C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_950", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_954", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_8B8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_8BC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_8C8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_8CC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_8D4", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_958", 0x0000, 59, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_58E8", 50, 50, 0, 0,
        (
            ("ms66500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8D8", "MonsterBattlePostion_938", "ed7450", "ed7453", "ATBonus_878"),
            ("ms66500.dat", "ms66500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8B8", "MonsterBattlePostion_938", "ed7450", "ed7453", "ATBonus_878"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9C8", 0x0000, 59, 6, 45, 6, 1, 75, 0, "br0000", "Sepith_5900", 30, 45, 25, 0,
        (
            ("ms61000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8D8", "MonsterBattlePostion_938", "ed7450", "ed7453", "ATBonus_878"),
            ("ms61000.dat", "ms61000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_8B8", "MonsterBattlePostion_938", "ed7450", "ed7453", "ATBonus_878"),
            ("ms61000.dat", "ms61000.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_8D8", "MonsterBattlePostion_938", "ed7450", "ed7453", "ATBonus_878"),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_A64", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66500.dat", "ms66500.dat", "ms66500.dat", "ms66500.dat", "ms66500.dat", "ms66500.dat", "ms66500.dat", "ms66500.dat", "MonsterBattlePostion_8D8", "MonsterBattlePostion_938", "ed7453", "ed7453", "ATBonus_878"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AA8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "ms63701.dat", "MonsterBattlePostion_8D8", "MonsterBattlePostion_938", "ed7453", "ed7453", "ATBonus_878"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00000.itc",                   # 00
        "chr/ch00000.itc",                   # 01
        "chr/ch00000.itc",                   # 02
        "chr/ch00000.itc",                   # 03
        "chr/ch00000.itc",                   # 04
        "chr/ch00000.itc",                   # 05
        "chr/ch00000.itc",                   # 06
        "chr/ch00000.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch00000.itc",                   # 0D
        "chr/ch00000.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch66550.itc",               # 10
        "monster/ch66551.itc",               # 11
        "monster/ch61050.itc",               # 12
        "monster/ch61050.itc",               # 13
        "monster/ch63750.itc",               # 14
        "monster/ch63751.itc",               # 15
    ))

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
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    487,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    487,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
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
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(121569,  3000,    68819,   270,  484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(121569,  3000,    68819,   270,  484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)

    DeclMonster(130449,  38270,   2000,    0x1010000,    "BattleInfo_958", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(133810,  75570,   3000,    0x1010000,    "BattleInfo_9C8", 0,   18,  0xFFFF, 2,  3)

    DeclActor(550,     0,       4660,    1200,    550,     1000,    4660,    0x007C, 0,  15, 0x0000)
    DeclActor(111510,  -2000,   78150,   1200,    111510,  -1000,   78150,   0x007C, 0,  6,  0x0000)
    DeclActor(118170,  3000,    85350,   1200,    118170,  4000,    85350,   0x007C, 0,  7,  0x0000)
    DeclActor(121570,  3000,    68820,   1200,    121570,  3000,    68820,   0x007C, 0,  8,  0x0000)
    DeclActor(14350,   0,       4400,    1200,    14350,   2000,    4400,    0x007C, 0,  14, 0x0000)
    DeclActor(15000,   0,       6000,    1200,    15000,   2000,    6000,    0x007C, 0,  14, 0x0000)
    DeclActor(4010,    0,       6840,    1500,    4010,    1700,    6840,    0x007C, 0,  59, 0x0000)

    PlaceName(-17.0, 0.0, -7.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(203.0, 0.0, 27.5, 0x0000, 0x0000, "阿尔摩利卡村·唐古拉姆门方向")
    PlaceName(0.5899999737739563, 0.0, 4.840000152587891, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_C0C",          # 00, 0
        "Function_1_CBB",          # 01, 1
        "Function_2_CDA",          # 02, 2
        "Function_3_CF9",          # 03, 3
        "Function_4_D63",          # 04, 4
        "Function_5_1788",         # 05, 5
        "Function_6_1BEC",         # 06, 6
        "Function_7_1D27",         # 07, 7
        "Function_8_1E62",         # 08, 8
        "Function_9_218C",         # 09, 9
        "Function_10_2190",        # 0A, 10
        "Function_11_22A7",        # 0B, 11
        "Function_12_23D4",        # 0C, 12
        "Function_13_2425",        # 0D, 13
        "Function_14_24B9",        # 0E, 14
        "Function_15_27E6",        # 0F, 15
        "Function_16_2820",        # 10, 16
        "Function_17_2D96",        # 11, 17
        "Function_18_2DB2",        # 12, 18
        "Function_19_304E",        # 13, 19
        "Function_20_4313",        # 14, 20
        "Function_21_4386",        # 15, 21
        "Function_22_439E",        # 16, 22
        "Function_23_43D5",        # 17, 23
        "Function_24_442D",        # 18, 24
        "Function_25_445F",        # 19, 25
        "Function_26_4491",        # 1A, 26
        "Function_27_44C3",        # 1B, 27
        "Function_28_44F5",        # 1C, 28
        "Function_29_454D",        # 1D, 29
        "Function_30_4571",        # 1E, 30
        "Function_31_4595",        # 1F, 31
        "Function_32_48F2",        # 20, 32
        "Function_33_4B50",        # 21, 33
        "Function_34_4E03",        # 22, 34
        "Function_35_4E1E",        # 23, 35
        "Function_36_4E39",        # 24, 36
        "Function_37_4E54",        # 25, 37
        "Function_38_4ED3",        # 26, 38
        "Function_39_5084",        # 27, 39
        "Function_40_5223",        # 28, 40
        "Function_41_52CC",        # 29, 41
        "Function_42_5375",        # 2A, 42
        "Function_43_54DE",        # 2B, 43
        "Function_44_5587",        # 2C, 44
        "Function_45_5630",        # 2D, 45
        "Function_46_5653",        # 2E, 46
        "Function_47_5673",        # 2F, 47
        "Function_48_5696",        # 30, 48
        "Function_49_56B5",        # 31, 49
        "Function_50_56D4",        # 32, 50
        "Function_51_56F3",        # 33, 51
        "Function_52_5712",        # 34, 52
        "Function_53_5731",        # 35, 53
        "Function_54_5760",        # 36, 54
        "Function_55_5783",        # 37, 55
        "Function_56_57DD",        # 38, 56
        "Function_57_5800",        # 39, 57
        "Function_58_5823",        # 3A, 58
        "Function_59_583D",        # 3B, 59
    ))


    def Function_0_C0C(): pass

    label("Function_0_C0C")

    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C2A")
    SetScenarioFlags(0x31, 2)

    label("loc_C2A")

    OutputDebugInt(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C72")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_C6C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C61")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_C67")

    label("loc_C61")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_C67")

    Jump("loc_C72")

    label("loc_C6C")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_C72")

    OutputDebugInt(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_CB4")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_CA9")
    Sound(2500, 255, 100, 0)    #voice#Noel
    Jump("loc_CAF")

    label("loc_CA9")

    Sound(3538, 255, 100, 0)    #voice#Noel

    label("loc_CAF")

    Jump("loc_CBA")

    label("loc_CB4")

    Sound(3345, 255, 100, 0)    #voice#Lloyd

    label("loc_CBA")

    Return()

    # Function_0_C0C end

    def Function_1_CBB(): pass

    label("Function_1_CBB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CD9")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_CBB")

    label("loc_CD9")

    Return()

    # Function_1_CBB end

    def Function_2_CDA(): pass

    label("Function_2_CDA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF8")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_2_CDA")

    label("loc_CF8")

    Return()

    # Function_2_CDA end

    def Function_3_CF9(): pass

    label("Function_3_CF9")

    SetMapObjFlags(0xD, 0x2000000)
    SetMapObjFlags(0xE, 0x2000000)
    SetMapObjFlags(0xF, 0x2000000)
    SetMapObjFlags(0x10, 0x2000000)
    SetMapObjFlags(0x11, 0x2000000)
    SetMapObjFlags(0x12, 0x2000000)
    SetMapObjFlags(0x13, 0x2000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D62")
    ClearMapObjFlags(0xD, 0x2000000)
    ClearMapObjFlags(0xE, 0x2000000)
    ClearMapObjFlags(0xF, 0x2000000)
    ClearMapObjFlags(0x10, 0x2000000)
    ClearMapObjFlags(0x11, 0x2000000)
    ClearMapObjFlags(0x12, 0x2000000)
    ClearMapObjFlags(0x13, 0x2000000)
    SetMapObjFlags(0x0, 0x2000000)
    SetMapObjFlags(0x5, 0x2000000)

    label("loc_D62")

    Return()

    # Function_3_CF9 end

    def Function_4_D63(): pass

    label("Function_4_D63")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D80")
    ClearScenarioFlags(0x22, 0)
    Event(0, 16)
    Jump("loc_DA3")

    label("loc_D80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_D94")
    ClearScenarioFlags(0x22, 1)
    Event(0, 18)
    Jump("loc_DA3")

    label("loc_D94")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_DA3")
    ClearScenarioFlags(0x22, 2)
    Event(0, 19)

    label("loc_DA3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1247")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E30")
    SetScenarioFlags(0x38, 0)

    label("loc_E30")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E46")
    SetScenarioFlags(0x38, 1)

    label("loc_E46")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5C")
    SetScenarioFlags(0x38, 2)

    label("loc_E5C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E72")
    SetScenarioFlags(0x38, 3)

    label("loc_E72")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E88")
    SetScenarioFlags(0x38, 4)

    label("loc_E88")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9E")
    SetScenarioFlags(0x38, 5)

    label("loc_E9E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB4")
    SetScenarioFlags(0x38, 6)

    label("loc_EB4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECA")
    SetScenarioFlags(0x38, 7)

    label("loc_ECA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE0")
    SetScenarioFlags(0x39, 0)

    label("loc_EE0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF6")
    SetScenarioFlags(0x39, 1)

    label("loc_EF6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0C")
    SetScenarioFlags(0x39, 2)

    label("loc_F0C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F22")
    SetScenarioFlags(0x39, 3)

    label("loc_F22")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F38")
    SetScenarioFlags(0x39, 4)

    label("loc_F38")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F4E")
    SetScenarioFlags(0x39, 5)

    label("loc_F4E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F64")
    SetScenarioFlags(0x39, 6)

    label("loc_F64")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F7A")
    SetScenarioFlags(0x39, 7)

    label("loc_F7A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F90")
    SetScenarioFlags(0x3A, 0)

    label("loc_F90")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FA6")
    SetScenarioFlags(0x3A, 1)

    label("loc_FA6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FBC")
    SetScenarioFlags(0x3A, 2)

    label("loc_FBC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD2")
    SetScenarioFlags(0x3A, 3)

    label("loc_FD2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE8")
    SetScenarioFlags(0x3A, 4)

    label("loc_FE8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFE")
    SetScenarioFlags(0x3A, 5)

    label("loc_FFE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1014")
    SetScenarioFlags(0x3A, 6)

    label("loc_1014")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_102A")
    SetScenarioFlags(0x3A, 7)

    label("loc_102A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1040")
    SetScenarioFlags(0x3B, 0)

    label("loc_1040")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1056")
    SetScenarioFlags(0x3B, 1)

    label("loc_1056")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_106C")
    SetScenarioFlags(0x3B, 2)

    label("loc_106C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1082")
    SetScenarioFlags(0x3B, 3)

    label("loc_1082")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1098")
    SetScenarioFlags(0x3B, 4)

    label("loc_1098")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AE")
    SetScenarioFlags(0x3B, 5)

    label("loc_10AE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10C4")
    SetScenarioFlags(0x3B, 6)

    label("loc_10C4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10DA")
    SetScenarioFlags(0x3B, 7)

    label("loc_10DA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F0")
    SetScenarioFlags(0x3D, 5)

    label("loc_10F0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1106")
    SetScenarioFlags(0x3D, 6)

    label("loc_1106")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111C")
    SetScenarioFlags(0x3D, 7)

    label("loc_111C")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1157")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1247")

    label("loc_1157")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117A")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1247")

    label("loc_117A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_119D")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1247")

    label("loc_119D")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C0")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1247")

    label("loc_11C0")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E3")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1247")

    label("loc_11E3")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1206")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1247")

    label("loc_1206")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1229")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1247")

    label("loc_1229")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1247")
    SetScenarioFlags(0x3C, 7)

    label("loc_1247")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_125D")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_125D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_128F")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_128F")
    SetChrPos(0x0, 14840, 0, 3570, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 13)

    label("loc_128F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_12C2")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C2")
    SetChrPos(0x0, 15000, 0, 6000, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_12C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_12D1")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 12)

    label("loc_12D1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1787")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1370")
    SetScenarioFlags(0x38, 0)

    label("loc_1370")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1386")
    SetScenarioFlags(0x38, 1)

    label("loc_1386")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139C")
    SetScenarioFlags(0x38, 2)

    label("loc_139C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B2")
    SetScenarioFlags(0x38, 3)

    label("loc_13B2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C8")
    SetScenarioFlags(0x38, 4)

    label("loc_13C8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DE")
    SetScenarioFlags(0x38, 5)

    label("loc_13DE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F4")
    SetScenarioFlags(0x38, 6)

    label("loc_13F4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140A")
    SetScenarioFlags(0x38, 7)

    label("loc_140A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1420")
    SetScenarioFlags(0x39, 0)

    label("loc_1420")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1436")
    SetScenarioFlags(0x39, 1)

    label("loc_1436")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144C")
    SetScenarioFlags(0x39, 2)

    label("loc_144C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1462")
    SetScenarioFlags(0x39, 3)

    label("loc_1462")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1478")
    SetScenarioFlags(0x39, 4)

    label("loc_1478")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_148E")
    SetScenarioFlags(0x39, 5)

    label("loc_148E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14A4")
    SetScenarioFlags(0x39, 6)

    label("loc_14A4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14BA")
    SetScenarioFlags(0x39, 7)

    label("loc_14BA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14D0")
    SetScenarioFlags(0x3A, 0)

    label("loc_14D0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E6")
    SetScenarioFlags(0x3A, 1)

    label("loc_14E6")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14FC")
    SetScenarioFlags(0x3A, 2)

    label("loc_14FC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1512")
    SetScenarioFlags(0x3A, 3)

    label("loc_1512")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1528")
    SetScenarioFlags(0x3A, 4)

    label("loc_1528")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_153E")
    SetScenarioFlags(0x3A, 5)

    label("loc_153E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1554")
    SetScenarioFlags(0x3A, 6)

    label("loc_1554")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_156A")
    SetScenarioFlags(0x3A, 7)

    label("loc_156A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1580")
    SetScenarioFlags(0x3B, 0)

    label("loc_1580")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1596")
    SetScenarioFlags(0x3B, 1)

    label("loc_1596")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15AC")
    SetScenarioFlags(0x3B, 2)

    label("loc_15AC")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C2")
    SetScenarioFlags(0x3B, 3)

    label("loc_15C2")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15D8")
    SetScenarioFlags(0x3B, 4)

    label("loc_15D8")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EE")
    SetScenarioFlags(0x3B, 5)

    label("loc_15EE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1604")
    SetScenarioFlags(0x3B, 6)

    label("loc_1604")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_161A")
    SetScenarioFlags(0x3B, 7)

    label("loc_161A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1630")
    SetScenarioFlags(0x3D, 5)

    label("loc_1630")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1646")
    SetScenarioFlags(0x3D, 6)

    label("loc_1646")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165C")
    SetScenarioFlags(0x3D, 7)

    label("loc_165C")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1697")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1787")

    label("loc_1697")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16BA")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1787")

    label("loc_16BA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16DD")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1787")

    label("loc_16DD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1700")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1787")

    label("loc_1700")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1723")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1787")

    label("loc_1723")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1746")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1787")

    label("loc_1746")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1769")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1787")

    label("loc_1769")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1787")
    SetScenarioFlags(0x3C, 7)

    label("loc_1787")

    Return()

    # Function_4_D63 end

    def Function_5_1788(): pass

    label("Function_5_1788")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_179A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_179A")

    OP_52(0x40, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x40, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_19A7")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_19A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_19F9")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    Jump("loc_1A11")

    label("loc_19F9")

    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)

    label("loc_1A11")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B08")
    OP_11(0x38, 0x97, 0xF5, 0x0, 0x96, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x258, 0x0, 0x20)
    OP_C3(0x0, 0x1, 0x3, 0x0, 0x0, 0x1, 173490, -500, 11820, 2000, 2000, 0)
    OP_C3(0x1, 0x1, 0x3, 0x0, 0x0, 0x1, 174860, -500, 9700, 2000, 2000, 0)
    OP_C3(0x2, 0x1, 0x3, 0x0, 0x0, 0x1, 176430, -500, 7380, 2000, 2000, 0)
    OP_C3(0x3, 0x1, 0x3, 0x0, 0x0, 0x1, 177860, -500, 5310, 2000, 2000, 0)
    OP_C3(0x4, 0x1, 0x3, 0x0, 0x0, 0x1, 179420, -500, 2990, 2000, 2000, 0)
    LoadEffect(0x11, "eff\\\\trapdmg2.eff")
    Jump("loc_1B0E")

    label("loc_1B08")

    SetMapObjFlags(0x5, 0x4)

    label("loc_1B0E")

    MiniGame(0x2F, 0x4, 0x5, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x29, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B4E")
    OP_70(0x1, 0x0)
    Jump("loc_1B52")

    label("loc_1B4E")

    OP_70(0x1, 0x1E)

    label("loc_1B52")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B65")
    OP_70(0x2, 0x0)
    Jump("loc_1B69")

    label("loc_1B65")

    OP_70(0x2, 0x1E)

    label("loc_1B69")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1BCA")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 121570, 3000, 68820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1BCA")

    OP_1C(0x0, 0xA, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    OP_1C(0x0, 0xB, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    OP_1C(0x0, 0xC, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    Return()

    # Function_5_1788 end

    def Function_6_1BEC(): pass

    label("Function_6_1BEC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CDE")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅱ', 1)"), scpexpr(EXPR_END)), "loc_1C6F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1CD9")

    label("loc_1C6F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅱ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1CD9")

    Jump("loc_1D1B")

    label("loc_1CDE")

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

    label("loc_1D1B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1BEC end

    def Function_7_1D27(): pass

    label("Function_7_1D27")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E8, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E19")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('叮当耳环', 1)"), scpexpr(EXPR_END)), "loc_1DAA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '叮当耳环'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E8, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_1E14")

    label("loc_1DAA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '叮当耳环'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '叮当耳环'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E14")

    Jump("loc_1E56")

    label("loc_1E19")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_1E56")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1D27 end

    def Function_8_1E62(): pass

    label("Function_8_1E62")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2000")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_END)), "loc_1FE1")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FDC")
    ClearScenarioFlags(0x3A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_1FD9")
    ClearScenarioFlags(0x38, 0)
    OP_A7(0x3D, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F04():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3D, 2, lambda_1F04)
    TurnDirection(0x3D, 0x0, 0)
    ClearChrFlags(0x3D, 0x80)
    SetChrFlags(0x3D, 0x8000)
    PlayEffect(0x7, 0x1, 0x3D, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_A64", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x3D, 0x80)
    ClearChrFlags(0x3D, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FD4")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FBB")
    Call(1, 5)
    Jump("loc_1FD4")

    label("loc_1FBB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FD1")
    Call(1, 4)
    Jump("loc_1FD4")

    label("loc_1FD1")

    Call(1, 3)

    label("loc_1FD4")

    Jump("loc_1FDC")

    label("loc_1FD9")

    Call(1, 1)

    label("loc_1FDC")

    Jump("loc_1FF7")

    label("loc_1FE1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_1FF7")
    ClearScenarioFlags(0x38, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1FF7")

    TalkEnd(0xFF)
    Return()

    label("loc_2000")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_END)), "loc_2171")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_216C")
    ClearScenarioFlags(0x3A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_2169")
    ClearScenarioFlags(0x38, 0)
    OP_A7(0x3E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2094():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x3E, 2, lambda_2094)
    TurnDirection(0x3E, 0x0, 0)
    ClearChrFlags(0x3E, 0x80)
    SetChrFlags(0x3E, 0x8000)
    PlayEffect(0x7, 0x1, 0x3E, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_AA8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x3E, 0x80)
    ClearChrFlags(0x3E, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2164")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_214B")
    Call(1, 5)
    Jump("loc_2164")

    label("loc_214B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2161")
    Call(1, 4)
    Jump("loc_2164")

    label("loc_2161")

    Call(1, 3)

    label("loc_2164")

    Jump("loc_216C")

    label("loc_2169")

    Call(1, 1)

    label("loc_216C")

    Jump("loc_2187")

    label("loc_2171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_2187")
    ClearScenarioFlags(0x38, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2187")

    TalkEnd(0xFF)
    Return()

    # Function_8_1E62 end

    def Function_9_218C(): pass

    label("Function_9_218C")

    Call(1, 6)
    Return()

    # Function_9_218C end

    def Function_10_2190(): pass

    label("Function_10_2190")

    EventBegin(0x2)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21CA")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "有一个巴士车站。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    label("loc_21CA")


    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K有一个巴士车站。\x01",
            "要乘坐巴士吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "阿尔摩利卡村\x01",          # 0
            "唐古拉姆门\x01",            # 1
            "停靠站（三岔路）\x01",      # 2
            "放弃\x01",                  # 3
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_225A")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("t0000", 0, 0, 0)
    IdleLoop()
    Jump("loc_229F")

    label("loc_225A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_227F")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("t2500", 0, 0, 0)
    IdleLoop()
    Jump("loc_229F")

    label("loc_227F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_229F")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("r0030", 0, 0, 0)
    IdleLoop()

    label("loc_229F")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_10_2190 end

    def Function_11_22A7(): pass

    label("Function_11_22A7")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_23D0")
    Fade(500)
    OP_68(-620, 600, 4110, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(27000, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -1000, 0, 4500, 180)
    SetChrPos(0x1, -1000, 0, 5600, 180)
    SetChrPos(0x2, -1000, 0, 6700, 180)
    SetChrPos(0x3, -1000, 0, 7800, 180)
    ClearChrFlags(0x29, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    OP_78(0x0, 0x29)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x29, 12000, 0, 0, 0)
    OP_D5(0x29, 0x0, 0x41EB0, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_2387():
        OP_98(0xFE, 0xFFFFD120, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x29, 1, lambda_2387)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x29, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_23D0")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_11_22A7 end

    def Function_12_23D4(): pass

    label("Function_12_23D4")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -1000, 0, 4500, 180)
    OP_31(0x1)
    OP_68(-1000, 600, 4500, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(25000, 0)
    EventEnd(0x5)
    Return()

    # Function_12_23D4 end

    def Function_13_2425(): pass

    label("Function_13_2425")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2480")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2475")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_247B")

    label("loc_2475")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_247B")

    Jump("loc_24A4")

    label("loc_2480")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_249E")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_24A4")

    label("loc_249E")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_24A4")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_2425 end

    def Function_14_24B9(): pass

    label("Function_14_24B9")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24EB")
    SetScenarioFlags(0x31, 2)

    label("loc_24EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2531")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_252B")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2520")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_2526")

    label("loc_2520")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_2526")

    Jump("loc_2531")

    label("loc_252B")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_2531")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27D8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_25A2")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2582"),
        (SWITCH_DEFAULT, "loc_2593"),
    )


    label("loc_2582")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_259D")

    label("loc_2593")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_259D")

    Jump("loc_27D3")

    label("loc_25A2")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_25D2")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_25D2")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_25FC"),
        (1, "loc_2700"),
        (2, "loc_2791"),
        (SWITCH_DEFAULT, "loc_27C9"),
    )


    label("loc_25FC")

    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_262D")
    OP_70(0x3, 0x12C)
    OP_71(0x3, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_263D")

    label("loc_262D")

    OP_70(0x3, 0xF0)
    OP_71(0x3, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_263D")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2693")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2693")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26B6")
    Sound(461, 0, 100, 0)

    label("loc_26B6")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_26D6")
    OP_70(0x3, 0x14A)
    OP_71(0x3, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_26E6")

    label("loc_26D6")

    OP_70(0x3, 0x10E)
    OP_71(0x3, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_26E6")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x3, "light", 0x1, 0x1)
    OP_70(0x3, 0x0)
    Jump("loc_2531")

    label("loc_2700")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2772")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2735")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_274D")

    label("loc_2735")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2748")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_274D")

    label("loc_2748")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_274D")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_278C")

    label("loc_2772")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2782")
    OP_AF(0xFB)
    Jump("loc_278C")

    label("loc_2782")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_278C")

    Jump("loc_27D3")

    label("loc_2791")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27AA")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27C4")

    label("loc_27AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_27BA")
    OP_AF(0xFB)
    Jump("loc_27C4")

    label("loc_27BA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27C4")

    Jump("loc_27D3")

    label("loc_27C9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27D3")

    Jump("loc_2531")

    label("loc_27D8")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_24B9 end

    def Function_15_27E6(): pass

    label("Function_15_27E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_281C")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力巴士已经停运了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_281C")

    Call(0, 10)
    Return()

    # Function_15_27E6 end

    def Function_16_2820(): pass

    label("Function_16_2820")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch30600.itc", 0x1E)
    LoadChrToIndex("chr/ch30000.itc", 0x1F)
    LoadChrToIndex("apl/ch51231.itc", 0x20)
    SoundLoad(835)
    SoundLoad(468)
    SoundLoad(924)
    SetChrChipByIndex(0x31, 0x1E)
    SetChrSubChip(0x31, 0x0)
    ClearChrFlags(0x31, 0x80)
    SetChrFlags(0x31, 0x8000)
    SetChrChipByIndex(0x32, 0x1F)
    SetChrSubChip(0x32, 0x0)
    ClearChrFlags(0x32, 0x80)
    SetChrFlags(0x32, 0x8000)
    SetChrChipByIndex(0x33, 0x1F)
    SetChrSubChip(0x33, 0x0)
    ClearChrFlags(0x33, 0x80)
    SetChrFlags(0x33, 0x8000)
    SetChrChipByIndex(0x34, 0x1F)
    SetChrSubChip(0x34, 0x0)
    ClearChrFlags(0x34, 0x80)
    SetChrFlags(0x34, 0x8000)
    SetChrChipByIndex(0x35, 0x1F)
    SetChrSubChip(0x35, 0x0)
    ClearChrFlags(0x35, 0x80)
    SetChrFlags(0x35, 0x8000)
    SetChrChipByIndex(0x36, 0x1F)
    SetChrSubChip(0x36, 0x0)
    ClearChrFlags(0x36, 0x80)
    SetChrFlags(0x36, 0x8000)
    SetChrChipByIndex(0x37, 0x1F)
    SetChrSubChip(0x37, 0x0)
    ClearChrFlags(0x37, 0x80)
    SetChrFlags(0x37, 0x8000)
    SetChrChipByIndex(0x38, 0x1F)
    SetChrSubChip(0x38, 0x0)
    ClearChrFlags(0x38, 0x80)
    SetChrFlags(0x38, 0x8000)
    SetChrChipByIndex(0x39, 0x1F)
    SetChrSubChip(0x39, 0x0)
    ClearChrFlags(0x39, 0x80)
    SetChrFlags(0x39, 0x8000)
    SetChrChipByIndex(0x3A, 0x1F)
    SetChrSubChip(0x3A, 0x0)
    ClearChrFlags(0x3A, 0x80)
    SetChrFlags(0x3A, 0x8000)
    SetChrChipByIndex(0x3B, 0x1F)
    SetChrSubChip(0x3B, 0x0)
    ClearChrFlags(0x3B, 0x80)
    SetChrFlags(0x3B, 0x8000)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0xD, 0x2A)
    OP_49()
    ClearMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xD, 0x1000)
    ClearChrFlags(0x2B, 0x80)
    OP_78(0xE, 0x2B)
    OP_49()
    ClearMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xE, 0x1000)
    ClearChrFlags(0x2C, 0x80)
    OP_78(0xF, 0x2C)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    ClearChrFlags(0x2D, 0x80)
    OP_78(0x10, 0x2D)
    OP_49()
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x10, 0x1000)
    ClearChrFlags(0x2E, 0x80)
    OP_78(0x11, 0x2E)
    OP_49()
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x11, 0x1000)
    ClearChrFlags(0x2F, 0x80)
    OP_78(0x12, 0x2F)
    OP_49()
    ClearMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x12, 0x1000)
    ClearChrFlags(0x30, 0x80)
    OP_78(0x13, 0x30)
    OP_49()
    ClearMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x13, 0x1000)
    SetMapObjFrame(0x13, "light", 0x0, 0x1)
    SetChrFlags(0x0, 0x80)
    SetChrBattleFlags(0x0, 0x8000)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    SetChrPos(0x31, 17750, 0, 4750, 90)
    SetChrPos(0x32, 16500, 0, 4750, 180)
    SetChrPos(0x33, 15250, 0, 4750, 180)
    SetChrPos(0x34, 14000, 0, 4750, 180)
    SetChrPos(0x35, 12750, 0, 4750, 180)
    SetChrPos(0x36, 11500, 0, 4750, 180)
    SetChrPos(0x37, 16500, 0, -5000, 0)
    SetChrPos(0x38, 15250, 0, -5000, 0)
    SetChrPos(0x39, 14000, 0, -5000, 0)
    SetChrPos(0x3A, 12750, 0, -5000, 0)
    SetChrPos(0x3B, 11500, 0, -5000, 0)
    SetChrPos(0x2A, 90000, 0, 0, 270)
    OP_D5(0x2A, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2B, 97500, 0, 2000, 270)
    OP_D5(0x2B, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2C, 97500, 0, -2000, 270)
    OP_D5(0x2C, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x30, 107500, 0, 0, 270)
    OP_D5(0x30, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2D, 117500, 0, 2000, 270)
    OP_D5(0x2D, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2E, 117500, 0, -2000, 270)
    OP_D5(0x2E, 0x0, 0x41EB0, 0x0, 0x0)
    SetChrPos(0x2F, 125000, 0, 0, 270)
    OP_D5(0x2F, 0x0, 0x41EB0, 0x0, 0x0)
    OP_68(14000, 600, 0, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(25000, 3000)
    Sound(835, 2, 100, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    OP_93(0x31, 0xE1, 0x1F4)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x32, 0x20)
    SetChrSubChip(0x32, 0x0)
    SetChrChipByIndex(0x33, 0x20)
    SetChrSubChip(0x33, 0x0)
    SetChrChipByIndex(0x34, 0x20)
    SetChrSubChip(0x34, 0x0)
    SetChrChipByIndex(0x35, 0x20)
    SetChrSubChip(0x35, 0x0)
    SetChrChipByIndex(0x36, 0x20)
    SetChrSubChip(0x36, 0x0)
    SetChrChipByIndex(0x37, 0x20)
    SetChrSubChip(0x37, 0x0)
    SetChrChipByIndex(0x38, 0x20)
    SetChrSubChip(0x38, 0x0)
    SetChrChipByIndex(0x39, 0x20)
    SetChrSubChip(0x39, 0x0)
    SetChrChipByIndex(0x3A, 0x20)
    SetChrSubChip(0x3A, 0x0)
    SetChrChipByIndex(0x3B, 0x20)
    SetChrSubChip(0x3B, 0x0)
    SetCameraDistance(24500, 200)
    OP_0D()
    Sleep(500)
    MoveCamera(60, 20, 0, 1500)
    OP_68(30500, 600, 0, 1500)
    Sleep(1000)
    Fade(500)
    SetChrPos(0x31, 17750, 0, 4750, 180)
    BeginChrThread(0x3C, 1, 0, 17)

    def lambda_2C8E():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_2C8E)

    def lambda_2CA3():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_2CA3)

    def lambda_2CB8():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_2CB8)

    def lambda_2CCD():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_2CCD)

    def lambda_2CE2():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x2E, 1, lambda_2CE2)

    def lambda_2CF7():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x2F, 1, lambda_2CF7)

    def lambda_2D0C():
        OP_9B(0x1, 0xFE, 0x0, 0x30D40, 0x2328, 0x0)
        ExitThread()

    QueueWorkItem(0x30, 1, lambda_2D0C)
    OP_68(85000, 600, 0, 0)
    MoveCamera(80, 20, 2, 0)
    OP_6E(450, 0)
    SetCameraDistance(28500, 0)
    OP_68(-2750, 600, 0, 14250)
    MoveCamera(35, 25, 2, 14250)
    SetCameraDistance(29500, 14250)
    Sleep(12750)
    StopSound(924, 1000, 30)
    StopSound(468, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("e2110", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2820 end

    def Function_17_2D96(): pass

    label("Function_17_2D96")

    Sound(468, 2, 100, 0)
    Sound(924, 2, 30, 0)
    Sleep(6000)
    StopSound(835, 1000, 100)
    Sound(458, 0, 80, 0)
    Return()

    # Function_17_2D96 end

    def Function_18_2DB2(): pass

    label("Function_18_2DB2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51258.itc", 0x1E)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    SoundLoad(3463)
    SoundLoad(3464)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x5)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x8, 0x2)
    SetChrPos(0x8, 13500, -5000, -9500, 90)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFlags(0x9, 0x4)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_68(176300, 3000, 7600, 0)
    MoveCamera(25, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26000, 0)
    MoveCamera(45, 21, 0, 7000)
    SetCameraDistance(23000, 7000)
    OP_71(0x5, 0x208, 0x2BC, 0x0, 0x0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(700)
    Sound(202, 0, 100, 0)
    Sleep(100)
    Sound(223, 0, 100, 0)
    Sleep(1200)
    FadeToDark(1000, 16777215, -1)
    Sound(181, 0, 100, 0)
    Sleep(1500)
    FadeToBright(1000, 16777215)
    OP_6F(0x79)
    Sleep(500)
    OP_68(156300, 1000, -1000, 5000)
    MoveCamera(29, 19, 0, 5000)
    SetCameraDistance(19000, 5000)
    Sleep(4000)
    Fade(1000)
    OP_68(33500, 1100, -9500, 0)
    MoveCamera(29, 19, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_68(13500, -3900, -9500, 5000)
    SetCameraDistance(16500, 5000)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(14, 280, -1, 3)

    #A0014
    AnonymousTalk(
        0x8,
        (
            "#3463V#30W我是达德利，\x01",
            "『结界』已经消失，确认完毕。\x02\x03",

            "#3464V接下来，准备尝试与教会的梅尔卡瓦联络。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xD88)
    OP_C9(0x1, 0x80000000)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    SetCameraDistance(16000, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 1)
    NewScene("c1560", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2DB2 end

    def Function_19_304E(): pass

    label("Function_19_304E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_D7(0x10)
    OP_D7(0x11)
    OP_D7(0x12)
    OP_D7(0x13)
    OP_D7(0x14)
    OP_D7(0x15)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("monster/ch82052.itc", 0x20)
    LoadChrToIndex("monster/ch86150.itc", 0x22)
    LoadChrToIndex("monster/ch86151.itc", 0x23)
    LoadChrToIndex("monster/ch86152.itc", 0x24)
    LoadChrToIndex("apl/ch51709.itc", 0x26)
    LoadChrToIndex("apl/ch51708.itc", 0x27)
    LoadChrToIndex("chr/ch41950.itc", 0x28)
    LoadChrToIndex("chr/ch41951.itc", 0x29)
    LoadChrToIndex("chr/ch41952.itc", 0x2A)
    LoadChrToIndex("chr/ch42050.itc", 0x2D)
    LoadChrToIndex("chr/ch42051.itc", 0x2E)
    LoadChrToIndex("chr/ch42052.itc", 0x2F)
    LoadChrToIndex("chr/ch42056.itc", 0x31)
    LoadChrToIndex("chr/ch06300.itc", 0x32)
    LoadChrToIndex("apl/ch50237.itc", 0x33)
    LoadChrToIndex("chr/ch31400.itc", 0x37)
    LoadChrToIndex("chr/ch31500.itc", 0x3C)
    LoadChrToIndex("chr/ch31551.itc", 0x3D)
    LoadChrToIndex("chr/ch31552.itc", 0x3E)
    LoadChrToIndex("chr/ch31556.itc", 0x3F)
    LoadChrToIndex("chr/ch12500.itc", 0x41)
    LoadChrToIndex("chr/ch12551.itc", 0x42)
    LoadChrToIndex("chr/ch12552.itc", 0x43)
    LoadChrToIndex("chr/ch12556.itc", 0x44)
    LoadEffect(0x0, "battle/btgun00.eff")
    LoadEffect(0x1, "battle/sp003000.eff")
    LoadEffect(0x2, "battle/ms00000.eff")
    LoadEffect(0x3, "event/ev15036.eff")
    SoundLoad(865)
    SoundLoad(863)
    SoundLoad(861)
    SetChrChipByIndex(0x9, 0x32)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x37)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x3C)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x41)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x3C)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x41)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x3C)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x41)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x3C)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x41)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetChrChipByIndex(0x13, 0x3C)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x41)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x3C)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x41)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x3C)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x41)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x27, 0x3F)
    SetChrSubChip(0x27, 0x0)
    SetChrFlags(0x27, 0x8000)
    SetChrChipByIndex(0x28, 0x44)
    SetChrSubChip(0x28, 0x0)
    SetChrFlags(0x28, 0x8000)
    SetChrFlags(0x19, 0x2)
    SetChrChipByIndex(0x19, 0x27)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x28)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x28)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0x1C, 0x28)
    SetChrSubChip(0x1C, 0x0)
    SetChrFlags(0x1C, 0x8000)
    SetChrChipByIndex(0x1D, 0x28)
    SetChrSubChip(0x1D, 0x0)
    SetChrFlags(0x1D, 0x8000)
    SetChrChipByIndex(0x1E, 0x28)
    SetChrSubChip(0x1E, 0x0)
    SetChrFlags(0x1E, 0x8000)
    SetChrChipByIndex(0x1F, 0x2D)
    SetChrSubChip(0x1F, 0x0)
    SetChrFlags(0x1F, 0x8000)
    SetChrChipByIndex(0x20, 0x2D)
    SetChrSubChip(0x20, 0x0)
    SetChrFlags(0x20, 0x8000)
    SetChrChipByIndex(0x21, 0x2D)
    SetChrSubChip(0x21, 0x0)
    SetChrFlags(0x21, 0x8000)
    SetChrChipByIndex(0x22, 0x2D)
    SetChrSubChip(0x22, 0x0)
    SetChrFlags(0x22, 0x8000)
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)
    SetChrFlags(0x23, 0x8000)
    SetChrChipByIndex(0x24, 0x1E)
    SetChrSubChip(0x24, 0x0)
    SetChrFlags(0x24, 0x8000)
    SetChrChipByIndex(0x25, 0x22)
    SetChrSubChip(0x25, 0x0)
    SetChrFlags(0x25, 0x8000)
    SetChrChipByIndex(0x26, 0x1E)
    SetChrSubChip(0x26, 0x0)
    SetChrFlags(0x26, 0x8000)
    ClearChrFlags(0x2A, 0x80)
    OP_78(0x14, 0x2A)
    OP_49()
    ClearMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x14, 0x1000)
    SetMapObjFrame(0x14, "light", 0x0, 0x1)
    ClearMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x15, 0x1000)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetChrFlags(0x1, 0x80)
    SetChrBattleFlags(0x1, 0x8000)
    SetChrFlags(0x2, 0x80)
    SetChrBattleFlags(0x2, 0x8000)
    SetChrFlags(0x3, 0x80)
    SetChrBattleFlags(0x3, 0x8000)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x26, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x2A, 20000, 0, 6000, 90)
    OP_D5(0x2A, 0x0, 0x15F90, 0x0, 0x0)
    SetChrPos(0x24, 25000, 0, 2500, 90)
    SetChrPos(0x25, 26000, 0, 0, 90)
    SetChrPos(0x26, 25000, 0, -2500, 90)
    SetChrPos(0x1F, 22500, 0, 3000, 90)
    SetChrPos(0x20, 22000, 0, 1500, 90)
    SetChrPos(0x21, 22500, 0, 0, 90)
    SetChrPos(0x22, 22000, 0, -1500, 90)
    SetChrPos(0x23, 22500, 0, -3000, 90)
    SetChrPos(0x1A, 19500, 0, 3000, 90)
    SetChrPos(0x1B, 19000, 0, 1500, 90)
    SetChrPos(0x1C, 19500, 0, 0, 90)
    SetChrPos(0x1D, 19000, 0, -1500, 90)
    SetChrPos(0x1E, 19500, 0, -3000, 90)
    SetChrPos(0x19, 20700, 2700, 5850, 90)
    BeginChrThread(0x24, 0, 0, 26)
    Sleep(50)
    BeginChrThread(0x26, 0, 0, 26)
    Sleep(50)
    BeginChrThread(0x25, 0, 0, 27)
    OP_68(26560, 3600, -970, 0)
    MoveCamera(315, 35, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(20300, 0)
    OP_68(20700, 3600, 5850, 4000)
    MoveCamera(315, 27, 0, 4000)
    SetCameraDistance(18350, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(250)
    Sound(531, 0, 100, 0)
    Sound(358, 0, 50, 0)
    SetChrChipByIndex(0x19, 0x26)
    SetChrSubChip(0x19, 0x0)
    ClearChrFlags(0x19, 0x2)
    OP_0D()
    Sleep(300)

    #C0015
    ChrTalk(
        0x19,
        "#5P来了……\x02",
    )

    CloseMessageWindow()
    OP_68(30000, 3600, 5850, 2000)
    Sleep(1000)
    Fade(500)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    SetChrPos(0x9, 139000, 0, 500, 270)
    SetChrPos(0xA, 140000, 0, -500, 270)
    SetChrPos(0xB, 135000, 0, 1200, 270)
    SetChrPos(0xC, 134500, 0, 0, 270)
    SetChrPos(0xD, 135000, 0, -1200, 270)
    SetChrPos(0xE, 137000, 0, 1200, 270)
    SetChrPos(0xF, 136500, 0, 0, 270)
    SetChrPos(0x10, 137000, 0, -1200, 270)
    SetChrPos(0x11, 136000, 0, 2400, 270)
    SetChrPos(0x12, 136000, 0, -2400, 270)
    SetChrPos(0x13, 137500, 0, -2900, 270)
    SetChrPos(0x14, 138500, 0, -2400, 270)
    SetChrPos(0x15, 140000, 0, -2900, 270)
    SetChrPos(0x16, 137500, 0, 2900, 270)
    SetChrPos(0x17, 138500, 0, 2400, 270)
    SetChrPos(0x18, 140000, 0, 2900, 270)
    OP_68(137000, 600, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24000, 0)
    OP_68(127000, 600, 0, 6000)

    def lambda_3728():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3728)

    def lambda_373D():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_373D)
    Sleep(5)

    def lambda_3755():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3755)

    def lambda_376A():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_376A)
    Sleep(5)

    def lambda_3782():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3782)

    def lambda_3797():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3797)
    Sleep(5)

    def lambda_37AF():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_37AF)

    def lambda_37C4():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_37C4)
    Sleep(5)

    def lambda_37DC():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_37DC)

    def lambda_37F1():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_37F1)
    Sleep(5)

    def lambda_3809():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_3809)

    def lambda_381E():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_381E)
    Sleep(5)

    def lambda_3836():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3836)

    def lambda_384B():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_384B)
    Sleep(5)

    def lambda_3863():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3863)

    def lambda_3878():
        OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3878)
    OP_0D()
    Sleep(3000)
    Fade(500)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    OP_68(19650, 3600, 1510, 0)
    MoveCamera(55, 21, 5, 0)
    OP_6E(440, 0)
    SetCameraDistance(20250, 0)
    OP_0D()
    OP_6F(0x79)

    #C0016
    ChrTalk(
        0x19,
        "#5P开始迎击。\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x19,
        (
            "#5P对手是肉搏战的达人，\x01",
            "出动狮兽，与他们保持距离。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(280, 120, -1, -1)
    SetChrName("众猎兵")

    #A0018
    AnonymousTalk(
        0xFF,
        "#5S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(28000, 600, 0, 3000)
    SetCameraDistance(23250, 3000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sound(948, 0, 50, 0)
    BeginChrThread(0x3C, 1, 0, 58)
    BeginChrThread(0x25, 0, 0, 25)

    def lambda_39C8():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 1, lambda_39C8)
    Sleep(50)
    BeginChrThread(0x24, 0, 0, 24)

    def lambda_39E6():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 1, lambda_39E6)
    Sleep(50)
    BeginChrThread(0x26, 0, 0, 24)

    def lambda_3A04():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 1, lambda_3A04)
    Sleep(50)
    SetChrChipByIndex(0x1F, 0x2E)

    def lambda_3A20():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_3A20)
    SetChrChipByIndex(0x23, 0x2E)

    def lambda_3A39():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x23, 1, lambda_3A39)
    Sleep(50)
    SetChrChipByIndex(0x20, 0x2E)

    def lambda_3A55():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_3A55)
    SetChrChipByIndex(0x22, 0x2E)

    def lambda_3A6E():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_3A6E)
    Sleep(50)
    SetChrChipByIndex(0x21, 0x2E)

    def lambda_3A8A():
        OP_9B(0x0, 0xFE, 0x0, 0x4E20, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_3A8A)
    Sleep(100)
    SetChrChipByIndex(0x1A, 0x29)

    def lambda_3AA6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3AA6)
    SetChrChipByIndex(0x1E, 0x29)

    def lambda_3ABF():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_3ABF)
    Sleep(50)
    SetChrChipByIndex(0x1B, 0x29)

    def lambda_3ADB():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3ADB)
    SetChrChipByIndex(0x1D, 0x29)

    def lambda_3AF4():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_3AF4)
    Sleep(50)
    SetChrChipByIndex(0x1C, 0x29)

    def lambda_3B10():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_3B10)
    WaitChrThread(0x1A, 1)
    Sound(865, 2, 100, 0)
    Sound(861, 2, 60, 0)
    BeginChrThread(0x1A, 0, 0, 23)
    BeginChrThread(0x1A, 3, 0, 22)
    WaitChrThread(0x1E, 1)
    BeginChrThread(0x1E, 0, 0, 23)
    BeginChrThread(0x1E, 3, 0, 22)
    WaitChrThread(0x1B, 1)
    BeginChrThread(0x1B, 0, 0, 23)
    BeginChrThread(0x1B, 3, 0, 22)
    WaitChrThread(0x1D, 1)
    BeginChrThread(0x1D, 0, 0, 23)
    BeginChrThread(0x1D, 3, 0, 22)
    WaitChrThread(0x1C, 1)
    BeginChrThread(0x1C, 0, 0, 23)
    BeginChrThread(0x1C, 3, 0, 22)
    OP_6F(0x79)
    StopSound(865, 1000, 90)
    StopSound(861, 1000, 50)
    Sound(863, 2, 80, 0)
    CancelBlur(0)
    Fade(500)
    EndChrThread(0x3C, 0x1)
    EndChrThread(0x24, 0x1)
    EndChrThread(0x25, 0x1)
    EndChrThread(0x26, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x23, 0x1)
    EndChrThread(0x1A, 0x0)
    EndChrThread(0x1A, 0x3)
    EndChrThread(0x1B, 0x0)
    EndChrThread(0x1B, 0x3)
    EndChrThread(0x1C, 0x0)
    EndChrThread(0x1C, 0x3)
    EndChrThread(0x1D, 0x0)
    EndChrThread(0x1D, 0x3)
    EndChrThread(0x1E, 0x0)
    EndChrThread(0x1E, 0x3)
    SetChrChipByIndex(0xB, 0x3E)
    SetChrSubChip(0xB, 0x0)
    SetChrChipByIndex(0xC, 0x43)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x3E)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x43)
    SetChrSubChip(0xE, 0x0)
    SetChrChipByIndex(0xF, 0x3E)
    SetChrSubChip(0xF, 0x0)
    SetChrChipByIndex(0x10, 0x43)
    SetChrSubChip(0x10, 0x0)
    SetChrChipByIndex(0x11, 0x3E)
    SetChrSubChip(0x11, 0x0)
    SetChrChipByIndex(0x12, 0x43)
    SetChrSubChip(0x12, 0x0)
    SetChrChipByIndex(0x13, 0x3E)
    SetChrSubChip(0x13, 0x0)
    SetChrChipByIndex(0x14, 0x43)
    SetChrSubChip(0x14, 0x0)
    SetChrChipByIndex(0x15, 0x3E)
    SetChrSubChip(0x15, 0x0)
    SetChrChipByIndex(0x16, 0x43)
    SetChrSubChip(0x16, 0x0)
    SetChrChipByIndex(0x17, 0x3E)
    SetChrSubChip(0x17, 0x0)
    SetChrChipByIndex(0x18, 0x43)
    SetChrSubChip(0x18, 0x0)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrPos(0x9, 109000, 0, 500, 270)
    SetChrPos(0xA, 110000, 0, -500, 270)
    SetChrPos(0xB, 105000, 0, 1200, 270)
    SetChrPos(0xC, 104500, 0, 0, 270)
    SetChrPos(0xD, 105000, 0, -1200, 270)
    SetChrPos(0xE, 107000, 0, 1200, 270)
    SetChrPos(0xF, 106500, 0, 0, 270)
    SetChrPos(0x10, 107000, 0, -1200, 270)
    SetChrPos(0x11, 106000, 0, 2400, 270)
    SetChrPos(0x12, 106000, 0, -2400, 270)
    SetChrPos(0x13, 107500, 0, -2900, 270)
    SetChrPos(0x14, 108500, 0, -2400, 270)
    SetChrPos(0x15, 110000, 0, -2900, 270)
    SetChrPos(0x16, 107500, 0, 2900, 270)
    SetChrPos(0x17, 108500, 0, 2400, 270)
    SetChrPos(0x18, 110000, 0, 2900, 270)
    OP_68(108500, 800, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(23000, 0)
    PlayEffect(0x1, 0x0, 0xFF, 0x0, 98000, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    SetChrChipByIndex(0x9, 0x33)
    Sound(318, 0, 100, 0)
    OP_A0(0x9, 1000, 0x0, 0x3)
    Sleep(300)

    #C0019
    ChrTalk(
        0x9,
        (
            "#03209F#11P呵呵……\x01",
            "真是让人热血沸腾的场面啊。\x02\x03",

            "#03210F那就赶快开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xA,
        "#11P明白了。\x02",
    )

    CloseMessageWindow()
    OP_A0(0x9, 1000, 0x2, 0x0)
    SetChrChipByIndex(0x9, 0x32)
    Sleep(300)

    #C0021
    ChrTalk(
        0xA,
        (
            "#11P在驱散兽群的同时\x01",
            "与猎兵团游斗。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xA,
        (
            "#11P注意他们的狙击，\x01",
            "努力杀入敌阵！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x1F4)
    SetMessageWindowPos(120, 50, -1, -1)
    SetChrName("众拳士")

    #A0023
    AnonymousTalk(
        0xFF,
        "#5S是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_68(103500, 800, 0, 1000)
    BlurSwitch(0x0, 0x77FFFFFF, 0x0, 0x1, 0x0)
    Sound(250, 0, 80, 0)
    BeginChrThread(0xB, 1, 0, 29)
    Sleep(30)
    BeginChrThread(0xC, 1, 0, 30)
    Sleep(30)
    BeginChrThread(0xD, 1, 0, 29)
    Sleep(30)
    BeginChrThread(0xE, 1, 0, 30)
    Sleep(30)
    BeginChrThread(0xF, 1, 0, 29)
    Sleep(30)
    BeginChrThread(0x10, 1, 0, 30)
    Sleep(30)
    BeginChrThread(0x11, 1, 0, 29)
    BeginChrThread(0x12, 1, 0, 30)
    Sleep(30)
    BeginChrThread(0x13, 1, 0, 29)
    BeginChrThread(0x16, 1, 0, 30)
    Sleep(30)
    BeginChrThread(0x14, 1, 0, 30)
    BeginChrThread(0x17, 1, 0, 29)
    Sleep(30)
    BeginChrThread(0x15, 1, 0, 29)
    BeginChrThread(0x18, 1, 0, 30)
    Sleep(1000)
    StopSound(863, 1000, 70)
    CancelBlur(2000)
    Fade(500)
    StopEffect(0x0, 0x0)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x14, 0x1)
    EndChrThread(0x15, 0x1)
    EndChrThread(0x16, 0x1)
    EndChrThread(0x17, 0x1)
    EndChrThread(0x18, 0x1)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrChip(0x1, 0xC, 0x0, 0x0)
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    SetChrChip(0x1, 0xE, 0x0, 0x0)
    SetChrChip(0x1, 0xF, 0x0, 0x0)
    SetChrChip(0x1, 0x10, 0x0, 0x0)
    SetChrChip(0x1, 0x11, 0x0, 0x0)
    SetChrChip(0x1, 0x12, 0x0, 0x0)
    SetChrChip(0x1, 0x13, 0x0, 0x0)
    SetChrChip(0x1, 0x14, 0x0, 0x0)
    SetChrChip(0x1, 0x15, 0x0, 0x0)
    SetChrChip(0x1, 0x16, 0x0, 0x0)
    SetChrChip(0x1, 0x17, 0x0, 0x0)
    SetChrChip(0x1, 0x18, 0x0, 0x0)
    SetChrPos(0xB, 87000, 0, 3500, 270)
    SetChrPos(0xE, 89000, 0, 2500, 270)
    SetChrPos(0xC, 86500, 0, 500, 270)
    SetChrPos(0xF, 88500, 0, -500, 270)
    SetChrPos(0xD, 87000, 0, -3500, 270)
    SetChrPos(0x10, 89000, 0, -2500, 270)
    SetChrPos(0x11, 88000, 0, 2400, 270)
    SetChrPos(0x16, 89500, 0, 2900, 270)
    SetChrPos(0x12, 88000, 0, -2400, 270)
    SetChrPos(0x13, 89500, 0, -2900, 270)
    SetChrPos(0x14, 89500, 0, -1400, 270)
    SetChrPos(0x15, 91000, 0, -1900, 270)
    SetChrPos(0x17, 89500, 0, 1400, 270)
    SetChrPos(0x18, 91000, 0, 1900, 270)
    SetChrPos(0x24, 65000, 0, 3000, 90)
    SetChrPos(0x25, 66000, 0, 0, 90)
    SetChrPos(0x26, 65000, 0, -3000, 90)
    SetChrPos(0x1F, 62500, 0, 3000, 90)
    SetChrPos(0x20, 62000, 0, 1500, 90)
    SetChrPos(0x21, 62500, 0, 0, 90)
    SetChrPos(0x22, 62000, 0, -1500, 90)
    SetChrPos(0x23, 62500, 0, -3000, 90)
    SetChrPos(0x1A, 59500, 0, 3000, 90)
    SetChrPos(0x1B, 59000, 0, 1500, 90)
    SetChrPos(0x1C, 59500, 0, 0, 90)
    SetChrPos(0x1D, 59000, 0, -1500, 90)
    SetChrPos(0x1E, 59500, 0, -3000, 90)
    BeginChrThread(0xA, 1, 0, 20)
    BeginChrThread(0xB, 1, 0, 31)
    BeginChrThread(0xC, 1, 0, 32)
    BeginChrThread(0xD, 1, 0, 33)
    BeginChrThread(0xE, 1, 0, 34)
    BeginChrThread(0xF, 1, 0, 35)
    BeginChrThread(0x10, 1, 0, 36)
    BeginChrThread(0x11, 1, 0, 37)
    BeginChrThread(0x12, 1, 0, 38)
    BeginChrThread(0x13, 1, 0, 39)
    BeginChrThread(0x14, 1, 0, 40)
    BeginChrThread(0x15, 1, 0, 41)
    BeginChrThread(0x16, 1, 0, 42)
    BeginChrThread(0x17, 1, 0, 43)
    BeginChrThread(0x18, 1, 0, 44)
    BeginChrThread(0x24, 1, 0, 45)
    BeginChrThread(0x25, 1, 0, 46)
    BeginChrThread(0x26, 1, 0, 47)
    BeginChrThread(0x1F, 1, 0, 48)
    BeginChrThread(0x20, 1, 0, 49)
    BeginChrThread(0x21, 1, 0, 50)
    BeginChrThread(0x22, 1, 0, 51)
    BeginChrThread(0x23, 1, 0, 52)
    BeginChrThread(0x1A, 1, 0, 53)
    BeginChrThread(0x1B, 1, 0, 54)
    BeginChrThread(0x1C, 1, 0, 55)
    BeginChrThread(0x1D, 1, 0, 56)
    BeginChrThread(0x1E, 1, 0, 57)
    Sleep(8000)
    StopSound(865, 1000, 50)
    StopSound(861, 1000, 30)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    EndChrThread(0x11, 0x1)
    EndChrThread(0x12, 0x1)
    EndChrThread(0x13, 0x1)
    EndChrThread(0x1F, 0x1)
    EndChrThread(0x20, 0x1)
    EndChrThread(0x21, 0x1)
    EndChrThread(0x22, 0x1)
    EndChrThread(0x23, 0x1)
    OP_24(0x361)
    OP_24(0x35F)
    OP_24(0x35D)
    Sleep(500)
    SetScenarioFlags(0x23, 0)
    NewScene("c1600", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_304E end

    def Function_20_4313(): pass

    label("Function_20_4313")

    OP_68(85000, 800, 0, 0)
    MoveCamera(90, 20, 5, 0)
    OP_6E(450, 0)
    SetCameraDistance(20000, 0)
    OP_68(77000, 800, 0, 1000)
    MoveCamera(90, 25, 5, 1000)
    Sleep(800)
    OP_68(75000, 800, 0, 10000)
    MoveCamera(40, 25, 5, 10000)
    SetCameraDistance(32000, 10000)
    Return()

    # Function_20_4313 end

    def Function_21_4386(): pass

    label("Function_21_4386")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_439D")
    OP_A0(0xFE, 5000, 0x10, 0x17)
    Jump("Function_21_4386")

    label("loc_439D")

    Return()

    # Function_21_4386 end

    def Function_22_439E(): pass

    label("Function_22_439E")

    Sleep(30)

    label("loc_43A1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_43D4")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43C8")
    OP_4C(0xFE, 0x0)
    Jump("loc_43CC")

    label("loc_43C8")

    OP_4B(0xFE, 0x0)

    label("loc_43CC")

    Sleep(500)
    Jump("loc_43A1")

    label("loc_43D4")

    Return()

    # Function_22_439E end

    def Function_23_43D5(): pass

    label("Function_23_43D5")

    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x0)

    label("loc_43DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_442C")
    PlayEffect(0x0, 0xFF, 0xFE, 0x3, 100, 950, 1700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_A1(0xFE, 0xBB8, 0x2, 0x2, 0x1)
    Jump("loc_43DD")

    label("loc_442C")

    Return()

    # Function_23_43D5 end

    def Function_24_442D(): pass

    label("Function_24_442D")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4447")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_445E")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_4447")

    label("loc_445E")

    Return()

    # Function_24_442D end

    def Function_25_445F(): pass

    label("Function_25_445F")

    SetChrChipByIndex(0xFE, 0x23)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4479")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4490")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_4479")

    label("loc_4490")

    Return()

    # Function_25_445F end

    def Function_26_4491(): pass

    label("Function_26_4491")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44AB")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44C2")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_44AB")

    label("loc_44C2")

    Return()

    # Function_26_4491 end

    def Function_27_44C3(): pass

    label("Function_27_44C3")

    SetChrChipByIndex(0xFE, 0x22)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44DD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_44F4")
    OP_A0(0xFE, 1500, 0x0, 0x5)
    Jump("loc_44DD")

    label("loc_44F4")

    Return()

    # Function_27_44C3 end

    def Function_28_44F5(): pass

    label("Function_28_44F5")

    SetChrFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x0)
    PlayEffect(0x2, 0xFF, 0xFE, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
    SetChrSubChip(0xFE, 0x3)
    Return()

    # Function_28_44F5 end

    def Function_29_454D(): pass

    label("Function_29_454D")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_29_454D end

    def Function_30_4571(): pass

    label("Function_30_4571")

    SetChrChip(0x0, 0xFE, 0x1E, 0xC8)
    SetChrChipByIndex(0xFE, 0x42)
    OP_9B(0x0, 0xFE, 0x0, 0x3A98, 0x2710, 0x0)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    Return()

    # Function_30_4571 end

    def Function_31_4595(): pass

    label("Function_31_4595")

    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1B58, 0x0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)

    label("loc_45B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_48F1")
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xE, 0x20)
    WaitChrThread(0x24, 1)
    SetChrChip(0x0, 0xB, 0x1E, 0xC8)
    OP_9A(0xB, 0x24, 0x3E8, 0x4E20, 0x0)
    SetChrChip(0x1, 0xB, 0x0, 0x0)
    SetChrSubChip(0xB, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(815, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x24, 0x0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0x24, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_465B():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_465B)
    OP_9B(0x1, 0x24, 0x0, 0xFFFFFE70, 0x2710, 0x0)
    BeginChrThread(0x24, 0, 0, 26)
    Sleep(300)
    SetChrSubChip(0xB, 0x0)

    def lambda_4690():
        OP_96(0xFE, 0x13498, 0x0, 0xDAC, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4690)
    Sleep(500)
    SetChrSubChip(0xE, 0x2)
    SetChrChip(0x0, 0xE, 0x1E, 0xC8)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(251, 0, 50, 0)
    OP_9D(0xE, 0x12BCE, 0x0, 0xA5A, 0x1F4, 0x3A98)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xE, 0x0, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(815, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x24, 0x0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0x24, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_475D():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_475D)
    OP_9B(0x1, 0x24, 0x0, 0xFFFFFE70, 0x2710, 0x0)
    BeginChrThread(0x24, 0, 0, 26)
    Sleep(300)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xE, 0x13880, 0x0, 0x9C4, 0x3E8, 0x2710)
    OP_52(0xE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    BeginChrThread(0x3C, 1, 0, 58)
    BeginChrThread(0x24, 0, 0, 24)
    OP_96(0x24, 0x128E0, 0x0, 0xBB8, 0x1B58, 0x0)
    EndChrThread(0x24, 0x0)
    EndChrThread(0x3C, 0x1)
    SetChrChipByIndex(0x24, 0x20)
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4804():
        OP_A0(0xFE, 1500, 0x0, 0x7)
        ExitThread()

    QueueWorkItem(0x24, 0, lambda_4804)

    def lambda_4811():
        OP_9B(0x1, 0xFE, 0x0, 0x7D0, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_4811)

    def lambda_4826():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_4826)

    def lambda_483B():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_483B)
    WaitChrThread(0x24, 0)
    WaitChrThread(0x24, 2)
    SetChrChipByIndex(0x24, 0x1F)
    SetChrSubChip(0x24, 0x0)
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(809, 0, 100, 0)
    OP_9D(0x24, 0x128E0, 0x0, 0xBB8, 0x1F4, 0x2710)
    OP_52(0x24, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x24, 0, 0, 26)
    Sleep(500)

    def lambda_48B2():
        OP_96(0xFE, 0x13498, 0x0, 0xDAC, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_48B2)
    Sleep(100)

    def lambda_48CF():
        OP_96(0xFE, 0x13880, 0x0, 0x9C4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_48CF)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xE, 2)
    Jump("loc_45B2")

    label("loc_48F1")

    Return()

    # Function_31_4595 end

    def Function_32_48F2(): pass

    label("Function_32_48F2")

    Sleep(30)
    OP_9B(0x0, 0xFE, 0x0, 0x1964, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)

    label("loc_490C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B4F")
    SetChrFlags(0xC, 0x20)
    SetChrFlags(0xF, 0x20)
    WaitChrThread(0x25, 1)
    Sound(948, 0, 60, 0)
    SetChrChipByIndex(0x25, 0x24)
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_494A():
        OP_A0(0xFE, 1500, 0x0, 0x5)
        ExitThread()

    QueueWorkItem(0x25, 0, lambda_494A)

    def lambda_4957():
        OP_9B(0x1, 0xFE, 0x0, 0x3E8, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x25, 2, lambda_4957)
    Sound(533, 0, 30, 0)

    def lambda_4972():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4972)
    Sleep(30)

    def lambda_498A():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFC18, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_498A)
    WaitChrThread(0x25, 0)
    WaitChrThread(0x25, 2)
    Sleep(100)
    BeginChrThread(0x25, 0, 0, 27)
    Sleep(200)
    SetChrChipByIndex(0x25, 0x23)
    SetChrSubChip(0x25, 0x0)
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0x25, 0x12CC8, 0x0, 0x0, 0x1F4, 0x2710)
    OP_52(0x25, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x25, 0, 0, 27)
    Sleep(1000)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xF, 2)
    SetChrChip(0x0, 0xC, 0x1E, 0xC8)
    OP_9A(0xC, 0x25, 0x7D0, 0x4E20, 0x0)
    SetChrChip(0x1, 0xC, 0x0, 0x0)
    SetChrSubChip(0xC, 0x1)
    Sound(815, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x25, 0x0)
    OP_A6(0x25, 0x0, 0x32, 0x1F4, 0xBB8)
    BeginChrThread(0x25, 0, 0, 27)
    Sleep(300)
    SetChrSubChip(0xF, 0x2)
    SetChrChip(0x0, 0xF, 0x1E, 0xC8)
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(534, 0, 40, 0)
    OP_9D(0xF, 0x1336C, 0x0, 0xFFFFFEA2, 0x1F4, 0x3A98)
    OP_52(0xF, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xF, 0x0, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(815, 0, 100, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x25, 0x0)
    OP_A6(0x25, 0x0, 0x32, 0x1F4, 0xBB8)
    BeginChrThread(0x25, 0, 0, 27)
    Sleep(300)
    SetChrSubChip(0xC, 0x0)

    def lambda_4B0C():
        OP_96(0xFE, 0x13880, 0x0, 0x1F4, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_4B0C)
    Sleep(30)
    SetChrSubChip(0xF, 0x0)

    def lambda_4B2D():
        OP_96(0xFE, 0x13C68, 0x0, 0xFFFFFE0C, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_4B2D)
    WaitChrThread(0xC, 2)
    WaitChrThread(0xF, 2)
    Jump("loc_490C")

    label("loc_4B4F")

    Return()

    # Function_32_48F2 end

    def Function_33_4B50(): pass

    label("Function_33_4B50")

    Sleep(60)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0x1B58, 0x0)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)

    label("loc_4B70")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4E02")
    SetChrFlags(0xD, 0x20)
    SetChrFlags(0x10, 0x20)
    WaitChrThread(0x26, 1)
    SetChrSubChip(0xD, 0x2)
    SetChrChip(0x0, 0xD, 0x1E, 0xC8)
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(250, 0, 40, 0)
    OP_9D(0xD, 0x12D90, 0x0, 0xFFFFF2EA, 0x1F4, 0x3A98)
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChip(0x1, 0xD, 0x0, 0x0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(600, 0, 40, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    EndChrThread(0x26, 0x0)
    Sound(501, 0, 100, 0)
    PlayEffect(0x2, 0xFF, 0x26, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_4C3E():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_4C3E)
    OP_9B(0x1, 0x26, 0x0, 0xFFFFFC18, 0x2710, 0x0)
    BeginChrThread(0x26, 0, 0, 26)
    Sleep(300)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4C7E():
        OP_9D(0xFE, 0x13498, 0x0, 0xFFFFF254, 0x3E8, 0x2710)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_4C7E)
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x26, 0, 0, 24)

    def lambda_4CAC():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x26, 2, lambda_4CAC)
    Sleep(300)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x10, 0x44)
    SetChrSubChip(0x10, 0x0)
    Sleep(300)
    SetChrSubChip(0x10, 0x1)
    SetChrPos(0x27, 80000, 0, -2500, 0)
    BeginChrThread(0x27, 3, 0, 21)
    ClearChrFlags(0x27, 0x80)
    Sound(538, 0, 80, 0)
    Sound(637, 0, 100, 0)
    PlayEffect(0x3, 0x1, 0x27, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x27, 0x26, 0x3E8, 0x7530, 0x0)
    StopEffect(0x1, 0x0)
    EndChrThread(0x26, 0x0)
    EndChrThread(0x26, 0x2)
    PlayEffect(0x2, 0xFF, 0x26, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_4D88():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x26, 0, lambda_4D88)
    OP_9B(0x1, 0x26, 0x0, 0xFFFFFA24, 0x4E20, 0x0)
    BeginChrThread(0x26, 0, 0, 26)
    OP_9A(0x27, 0x10, 0x0, 0x3A98, 0x0)
    EndChrThread(0x27, 0x3)
    Sound(308, 0, 100, 0)
    SetChrFlags(0x27, 0x80)
    SetChrSubChip(0x10, 0x0)
    Sleep(300)
    BeginChrThread(0x26, 0, 0, 24)
    OP_96(0x26, 0x128E0, 0x0, 0xFFFFF448, 0x1388, 0x0)
    BeginChrThread(0x26, 0, 0, 26)
    SetChrChipByIndex(0x10, 0x43)
    SetChrSubChip(0x10, 0x0)
    Jump("loc_4B70")

    label("loc_4E02")

    Return()

    # Function_33_4B50 end

    def Function_34_4E03(): pass

    label("Function_34_4E03")

    Sleep(90)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_34_4E03 end

    def Function_35_4E1E(): pass

    label("Function_35_4E1E")

    Sleep(120)
    OP_9B(0x0, 0xFE, 0x0, 0x1D4C, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_35_4E1E end

    def Function_36_4E39(): pass

    label("Function_36_4E39")

    Sleep(150)
    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_36_4E39 end

    def Function_37_4E54(): pass

    label("Function_37_4E54")

    Sleep(180)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1800)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 81600, 0, 4900, 6000, 0x0)
    OP_95(0xFE, 72250, 0, 4900, 6000, 0x0)
    OP_93(0xFE, 0x87, 0x3E8)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0x20, 1)
    OP_93(0xFE, 0xB4, 0x3E8)
    OP_95(0x20, 72250, 0, 2500, 6000, 0x0)
    TurnDirection(0x20, 0x11, 1000)
    Return()

    # Function_37_4E54 end

    def Function_38_4ED3(): pass

    label("Function_38_4ED3")

    Sleep(210)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)
    Sleep(1900)
    SetChrChipByIndex(0xFE, 0x42)
    OP_95(0xFE, 81600, 0, -4900, 6000, 0x0)
    OP_95(0xFE, 73250, 0, -4900, 6000, 0x0)
    OP_93(0xFE, 0x13B, 0x3E8)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)

    label("loc_4F2B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5083")
    WaitChrThread(0x1F, 1)
    SetChrFlags(0x12, 0x20)
    SetChrFlags(0x23, 0x20)
    OP_93(0x23, 0x2D, 0x3E8)
    Sound(540, 0, 70, 0)
    SetChrChipByIndex(0x23, 0x31)
    OP_A0(0x23, 1500, 0x0, 0x1)

    def lambda_4F61():
        OP_A0(0xFE, 1500, 0x2, 0x4)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_4F61)
    OP_99(0x23, 0x12, 0x1F4, 0x1388, 0x0)
    Sound(533, 0, 30, 0)

    def lambda_4F82():
        OP_9B(0x1, 0xFE, 0x0, 0xFFFFFD12, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 3, lambda_4F82)
    WaitChrThread(0x23, 2)
    WaitChrThread(0x12, 3)
    Sleep(300)
    TurnDirection(0x12, 0x23, 0)
    Sleep(300)
    OP_9A(0x12, 0x23, 0x1F4, 0x2710, 0x0)
    SetChrSubChip(0x12, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(862, 0, 60, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    TurnDirection(0x23, 0x12, 0)
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)
    PlayEffect(0x2, 0xFF, 0x23, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_502C():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x23, 0, lambda_502C)
    OP_96(0x23, 0x11B34, 0x0, 0xFFFFF448, 0x2710, 0x0)
    WaitChrThread(0x23, 0)
    SetChrChipByIndex(0x23, 0x2D)
    SetChrSubChip(0x23, 0x0)
    Sleep(500)
    SetChrSubChip(0x12, 0x0)
    OP_96(0x12, 0x11E22, 0x0, 0xFFFFECDC, 0x2710, 0x0)
    Sleep(1000)
    Jump("loc_4F2B")

    label("loc_5083")

    Return()

    # Function_38_4ED3 end

    def Function_39_5084(): pass

    label("Function_39_5084")

    Sleep(240)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(2000)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 81600, 0, -4900, 6000, 0x0)
    OP_95(0xFE, 74950, 0, -4500, 6000, 0x0)
    OP_93(0xFE, 0x13B, 0x3E8)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)

    label("loc_50DC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5222")
    Sound(531, 0, 30, 0)
    SetChrFlags(0x13, 0x20)
    SetChrFlags(0x22, 0x20)
    WaitChrThread(0x22, 1)
    SetChrChipByIndex(0x13, 0x3F)
    SetChrSubChip(0x13, 0x0)
    Sleep(300)
    SetChrSubChip(0x13, 0x1)
    SetChrPos(0x28, 74950, 0, -4500, 0)
    BeginChrThread(0x28, 3, 0, 21)
    ClearChrFlags(0x28, 0x80)
    Sound(538, 0, 50, 0)
    PlayEffect(0x3, 0x2, 0x28, 0x1, 0, 1000, 0, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_9A(0x28, 0x22, 0x3E8, 0x7530, 0x0)
    StopEffect(0x2, 0x0)
    TurnDirection(0x22, 0x13, 0)
    PlayEffect(0x2, 0xFF, 0x22, 0x1, 0, 1000, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)

    def lambda_51B7():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x22, 0, lambda_51B7)
    OP_9B(0x1, 0x22, 0x0, 0xFFFFFC18, 0x4E20, 0x0)
    OP_9A(0x28, 0x13, 0x0, 0x3A98, 0x0)
    EndChrThread(0x28, 0x3)
    Sound(308, 0, 100, 0)
    SetChrFlags(0x28, 0x80)
    SetChrSubChip(0x13, 0x0)
    Sleep(300)
    OP_96(0x22, 0x11940, 0x0, 0xFFFFFA24, 0x1388, 0x0)
    SetChrChipByIndex(0x13, 0x43)
    SetChrSubChip(0x13, 0x0)
    Sleep(1000)
    Jump("loc_50DC")

    label("loc_5222")

    Return()

    # Function_39_5084 end

    def Function_40_5223(): pass

    label("Function_40_5223")

    Sleep(270)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)
    Sleep(4000)
    SetChrChipByIndex(0xFE, 0x42)
    OP_95(0xFE, 81600, 0, -4900, 6000, 0x0)
    OP_95(0xFE, 77350, 0, -4900, 6000, 0x0)
    OP_95(0xFE, 76350, 0, -6000, 6000, 0x0)
    OP_95(0xFE, 73450, 0, -6000, 6000, 0x0)
    OP_95(0xFE, 72750, 0, -4900, 6000, 0x0)
    OP_95(0xFE, 69750, 0, -4900, 6000, 0x0)
    OP_93(0xFE, 0x0, 0x3E8)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_40_5223 end

    def Function_41_52CC(): pass

    label("Function_41_52CC")

    Sleep(300)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(4000)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 81600, 0, -4900, 6000, 0x0)
    OP_95(0xFE, 77350, 0, -4900, 6000, 0x0)
    OP_95(0xFE, 76350, 0, -6000, 6000, 0x0)
    OP_95(0xFE, 73450, 0, -6000, 6000, 0x0)
    OP_95(0xFE, 72450, 0, -4900, 6000, 0x0)
    OP_95(0xFE, 70750, 0, -4900, 6000, 0x0)
    OP_93(0xFE, 0x13B, 0x3E8)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_41_52CC end

    def Function_42_5375(): pass

    label("Function_42_5375")

    Sleep(330)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1B58, 0x0)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)
    Sleep(2100)
    SetChrChipByIndex(0xFE, 0x42)
    OP_95(0xFE, 81600, 0, 4900, 6000, 0x0)
    OP_95(0xFE, 74250, 0, 4900, 6000, 0x0)
    OP_93(0xFE, 0xE1, 0x3E8)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)

    label("loc_53CD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54DD")
    WaitChrThread(0x1F, 1)
    OP_93(0x1F, 0x2D, 0x3E8)
    SetChrChipByIndex(0x1F, 0x2F)
    SetChrSubChip(0x1F, 0x2)
    OP_52(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0x1F, 0x1207A, 0x0, 0x1130, 0x7D0, 0x1388)
    OP_52(0x1F, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_541D():
        OP_9B(0x1, 0xFE, 0x2D, 0xFFFFFD12, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 3, lambda_541D)
    SetChrSubChip(0x1F, 0x3)
    Sleep(50)
    SetChrSubChip(0x1F, 0x4)
    WaitChrThread(0x16, 3)
    Sleep(300)
    TurnDirection(0x16, 0x1F, 0)
    Sleep(300)
    SetChrSubChip(0x16, 0x1)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    TurnDirection(0x1F, 0xFE, 0)
    SetChrSubChip(0x1F, 0x0)

    def lambda_547F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x1F, 0, lambda_547F)
    OP_96(0x1F, 0x11B34, 0x0, 0xBB8, 0x2710, 0x0)
    WaitChrThread(0x1F, 0)
    SetChrChipByIndex(0x1F, 0x2D)
    SetChrSubChip(0x1F, 0x0)
    Sleep(500)
    SetChrSubChip(0x16, 0x0)
    OP_96(0x16, 0x1220A, 0x0, 0x1324, 0x2710, 0x0)
    OP_93(0x16, 0xD7, 0x3E8)
    Sleep(1000)
    Jump("loc_53CD")

    label("loc_54DD")

    Return()

    # Function_42_5375 end

    def Function_43_54DE(): pass

    label("Function_43_54DE")

    Sleep(360)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1F40, 0x0)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)
    Sleep(4000)
    SetChrChipByIndex(0xFE, 0x3D)
    OP_95(0xFE, 81600, 0, 4900, 6000, 0x0)
    OP_95(0xFE, 77350, 0, 4900, 6000, 0x0)
    OP_95(0xFE, 76350, 0, 6000, 6000, 0x0)
    OP_95(0xFE, 73450, 0, 6000, 6000, 0x0)
    OP_95(0xFE, 72750, 0, 4900, 6000, 0x0)
    OP_95(0xFE, 69750, 0, 4900, 6000, 0x0)
    OP_93(0xFE, 0xB4, 0x3E8)
    SetChrChipByIndex(0xFE, 0x3E)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_43_54DE end

    def Function_44_5587(): pass

    label("Function_44_5587")

    Sleep(390)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x1F40, 0x0)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)
    Sleep(4000)
    SetChrChipByIndex(0xFE, 0x42)
    OP_95(0xFE, 81600, 0, 4900, 6000, 0x0)
    OP_95(0xFE, 77350, 0, 4900, 6000, 0x0)
    OP_95(0xFE, 76350, 0, 6000, 6000, 0x0)
    OP_95(0xFE, 73450, 0, 6000, 6000, 0x0)
    OP_95(0xFE, 72450, 0, 4900, 6000, 0x0)
    OP_95(0xFE, 70750, 0, 4900, 6000, 0x0)
    OP_93(0xFE, 0xD7, 0x3E8)
    SetChrChipByIndex(0xFE, 0x43)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_44_5587 end

    def Function_45_5630(): pass

    label("Function_45_5630")

    Sleep(200)
    BeginChrThread(0xFE, 0, 0, 24)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1B58, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 26)
    Return()

    # Function_45_5630 end

    def Function_46_5653(): pass

    label("Function_46_5653")

    BeginChrThread(0xFE, 0, 0, 25)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1B58, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 27)
    Return()

    # Function_46_5653 end

    def Function_47_5673(): pass

    label("Function_47_5673")

    Sleep(400)
    BeginChrThread(0xFE, 0, 0, 24)
    OP_9B(0x0, 0xFE, 0x0, 0x2AF8, 0x1B58, 0x0)
    EndChrThread(0xFE, 0x0)
    BeginChrThread(0xFE, 0, 0, 26)
    Return()

    # Function_47_5673 end

    def Function_48_5696(): pass

    label("Function_48_5696")

    Sleep(3100)
    SetChrChipByIndex(0xFE, 0x2E)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_48_5696 end

    def Function_49_56B5(): pass

    label("Function_49_56B5")

    Sleep(3050)
    SetChrChipByIndex(0xFE, 0x2E)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_49_56B5 end

    def Function_50_56D4(): pass

    label("Function_50_56D4")

    Sleep(3000)
    SetChrChipByIndex(0xFE, 0x2E)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_50_56D4 end

    def Function_51_56F3(): pass

    label("Function_51_56F3")

    Sleep(3050)
    SetChrChipByIndex(0xFE, 0x2E)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_51_56F3 end

    def Function_52_5712(): pass

    label("Function_52_5712")

    Sleep(3100)
    SetChrChipByIndex(0xFE, 0x2E)
    OP_9B(0x0, 0xFE, 0x0, 0x2710, 0x1388, 0x0)
    SetChrChipByIndex(0xFE, 0x2D)
    SetChrSubChip(0xFE, 0x0)
    Return()

    # Function_52_5712 end

    def Function_53_5731(): pass

    label("Function_53_5731")

    Sleep(5100)
    SetChrChipByIndex(0xFE, 0x29)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1388, 0x0)
    Sound(865, 2, 60, 0)
    Sound(861, 2, 40, 0)
    BeginChrThread(0xFE, 0, 0, 23)
    BeginChrThread(0xFE, 3, 0, 22)
    Return()

    # Function_53_5731 end

    def Function_54_5760(): pass

    label("Function_54_5760")

    Sleep(5050)
    SetChrChipByIndex(0xFE, 0x29)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 23)
    BeginChrThread(0xFE, 3, 0, 22)
    Return()

    # Function_54_5760 end

    def Function_55_5783(): pass

    label("Function_55_5783")

    Sleep(5000)
    SetChrChipByIndex(0xFE, 0x29)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 23)
    BeginChrThread(0xFE, 3, 0, 22)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 79500, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_55_5783 end

    def Function_56_57DD(): pass

    label("Function_56_57DD")

    Sleep(5050)
    SetChrChipByIndex(0xFE, 0x29)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 23)
    BeginChrThread(0xFE, 3, 0, 22)
    Return()

    # Function_56_57DD end

    def Function_57_5800(): pass

    label("Function_57_5800")

    Sleep(5100)
    SetChrChipByIndex(0xFE, 0x29)
    OP_9B(0x0, 0xFE, 0x0, 0x251C, 0x1388, 0x0)
    BeginChrThread(0xFE, 0, 0, 23)
    BeginChrThread(0xFE, 3, 0, 22)
    Return()

    # Function_57_5800 end

    def Function_58_5823(): pass

    label("Function_58_5823")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_583C")
    Sound(845, 0, 100, 0)
    Sleep(500)
    Jump("Function_58_5823")

    label("loc_583C")

    Return()

    # Function_58_5823 end

    def Function_59_583D(): pass

    label("Function_59_583D")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0024
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "西·克洛斯贝尔市\x01",
            "东·阿尔摩利卡村　２７４赛尔矩\x01",
            "　　唐古拉姆门　　２０６赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_59_583D end

    SaveToFile()

Try(main)
