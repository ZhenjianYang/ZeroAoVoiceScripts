from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0302.bin",                # FileName
        "m0302",                    # MapName
        "m0302",                    # Location
        0x00A8,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 168, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0302",                  # 0
        "赛尔盖科长",             # 1
        "达德利搜查官",           # 2
        "雷蒙德搜查官",           # 3
        "艾玛搜查官",             # 4
        "罗伯兹主任",             # 5
        "接待小姐瑞贝卡",         # 6
        "乔里基科长",             # 7
        "凯特巡警",               # 8
        "研究员克雷",             # 9
        "警官",                   # 10
        "警官",                   # 11
        "搜查官",                 # 12
        "搜查官",                 # 13
        "诺艾尔",                 # 14
        "瓦吉",                   # 15
        "莉夏",                   # 16
        "三位一体攻击者ＲⅡ",     # 17
        "bm0300",                 # 18
        "bm0300",                 # 19
        "bm0300",                 # 20
        "bm0300",                 # 21
        "bm0300",                 # 22
    ))

    ATBonus("ATBonus_604", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_624", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_62A9", 5,   5,   5,   5,   10,  0,   0)

    MonsterBattlePostion("MonsterBattlePostion_664", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_668", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_66C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_670", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_674", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_678", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_680", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6C4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6C8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6CC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6D0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6D4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_6D8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_6DC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_644", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_660", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E4", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6E8", 10, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6EC", 3, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F0", 13, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F4", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 10, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_700", 0, 0, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_704", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_62A9", 35, 35, 30, 0,
        (
            ("ms84100.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84100.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7A0", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_62A9", 35, 35, 30, 0,
        (
            ("ms84200.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84200.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84100.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_62A9", 35, 35, 30, 0,
        (
            ("ms84300.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84300.dat", "ms84300.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84300.dat", "ms84200.dat", "ms84100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_91C", 0x0C40, 255, 6, 0, 0, 3, 0, 0, "bm0300", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80100.dat", "ms80100.dat", "ms80100.dat", "ms80100.dat", "ms80100.dat", "ms80100.dat", 0, 0, "MonsterBattlePostion_6E4", "MonsterBattlePostion_6C4", "ed7454", "ed7453", "ATBonus_624"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_8D8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm0300", 0x00000000, 100, 0, 0, 0,
        (
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7451", "ed7453", "ATBonus_604"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch02500.itc",                   # 00
        "chr/ch00900.itc",                   # 01
        "chr/ch30200.itc",                   # 02
        "chr/ch30500.itc",                   # 03
        "chr/ch29300.itc",                   # 04
        "chr/ch30400.itc",                   # 05
        "chr/ch30100.itc",                   # 06
        "chr/ch30600.itc",                   # 07
        "chr/ch32800.itc",                   # 08
        "chr/ch30000.itc",                   # 09
        "chr/ch27600.itc",                   # 0A
        "chr/ch27800.itc",                   # 0B
        "chr/ch02900.itc",                   # 0C
        "chr/ch03100.itc",                   # 0D
        "chr/ch03200.itc",                   # 0E
        "chr/ch00000.itc",                   # 0F
        "monster/ch84150.itc",               # 10
        "monster/ch84150.itc",               # 11
        "monster/ch84250.itc",               # 12
        "monster/ch84250.itc",               # 13
        "monster/ch84350.itc",               # 14
        "monster/ch84350.itc",               # 15
        "monster/ch80150.itc",               # 16
        "monster/ch80151.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   3,   0,   0,   0,   0,   15,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   4,   0,   0,   0,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   5,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   6,   0,   0,   0,   0,   16,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   7,   0,   0,   0,   0,   17,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   8,   0,   0,   0,   0,   19,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   20,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   9,   0,   0,   0,   0,   21,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   10,  0,   0,   0,   0,   22,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   11,  0,   0,   0,   0,   23,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   12,  0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   13,  0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   14,  0,   0,   0,   0,   10,  255,  0)
    DeclNpc(16000,   -5500,   338000,  0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(-6220,   183090,  -16000,  0x10100E1,    "BattleInfo_704", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(6460,    179480,  -16000,  0x101010E,    "BattleInfo_7A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-21250,  174340,  -16000,  0x101002D,    "BattleInfo_83C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-177920, 195000,  4000,    0x101010E,    "BattleInfo_83C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-197180, 201540,  6000,    0x1010059,    "BattleInfo_7A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(6220,    342630,  2000,    0x101013B,    "BattleInfo_704", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(26750,   342940,  2000,    0x10100E1,    "BattleInfo_83C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(22170,   199660,  -2000,   0x101002D,    "BattleInfo_7A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(341820,  99110,   6000,    0x10100E1,    "BattleInfo_704", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(327420,  77460,   0,       0x101010E,    "BattleInfo_7A0", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(349980,  198200,  0,       0x101010E,    "BattleInfo_83C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-500000, 500000,  0,       0x18500B4,    "BattleInfo_91C", 0,   22,  0xFFFF, 6,  7)

    DeclEvent(0x0040, 0, 26,  -500.0,                500.0,                 -1.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   62.5,                  -62.5,                 0.25,                  1.0])

    DeclActor(34000,   -2000,   190000,  1200,    34000,   -1000,   190000,  0x007C, 0,  4,  0x0000)
    DeclActor(16000,   -6000,   338000,  1200,    16000,   -5000,   338000,  0x007C, 0,  5,  0x0000)
    DeclActor(-2000,   -8000,   610000,  1200,    -2000,   -7000,   610000,  0x007C, 0,  6,  0x0000)
    DeclActor(350000,  0,       200000,  1200,    350000,  1000,    200000,  0x007C, 0,  7,  0x0000)
    DeclActor(-10600,  -16000,  193500,  1200,    -10600,  -15000,  193500,  0x007C, 0,  29, 0x0000)
    DeclActor(10000,   -8000,   193500,  1200,    10000,   -7000,   193500,  0x007C, 0,  30, 0x0000)
    DeclActor(-14000,  -8000,   192500,  1200,    -14000,  -7000,   192500,  0x007C, 0,  31, 0x0000)
    DeclActor(5500,    0,       748500,  1200,    5500,    1000,    748500,  0x007C, 0,  27, 0x0000)
    DeclActor(-6000,   -16000,  21660,   1200,    -6000,   -15000,  21660,   0x007C, 0,  25, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 7

    ScpFunction((
        "Function_0_A54",          # 00, 0
        "Function_1_B04",          # 01, 1
        "Function_2_B20",          # 02, 2
        "Function_3_BBD",          # 03, 3
        "Function_4_11AB",         # 04, 4
        "Function_5_12E6",         # 05, 5
        "Function_6_14E4",         # 06, 6
        "Function_7_161F",         # 07, 7
        "Function_8_1778",         # 08, 8
        "Function_9_198E",         # 09, 9
        "Function_10_1B5A",        # 0A, 10
        "Function_11_1D52",        # 0B, 11
        "Function_12_1FA2",        # 0C, 12
        "Function_13_2282",        # 0D, 13
        "Function_14_23FA",        # 0E, 14
        "Function_15_2580",        # 0F, 15
        "Function_16_2792",        # 10, 16
        "Function_17_28CD",        # 11, 17
        "Function_18_2A29",        # 12, 18
        "Function_19_2BFB",        # 13, 19
        "Function_20_2D44",        # 14, 20
        "Function_21_2E52",        # 15, 21
        "Function_22_2E94",        # 16, 22
        "Function_23_2EF6",        # 17, 23
        "Function_24_3011",        # 18, 24
        "Function_25_31F7",        # 19, 25
        "Function_26_32DB",        # 1A, 26
        "Function_27_3586",        # 1B, 27
        "Function_28_36E6",        # 1C, 28
        "Function_29_37F5",        # 1D, 29
        "Function_30_3958",        # 1E, 30
        "Function_31_3ABA",        # 1F, 31
        "Function_32_3C1C",        # 20, 32
        "Function_33_3CA8",        # 21, 33
        "Function_34_4178",        # 22, 34
        "Function_35_467B",        # 23, 35
        "Function_36_6175",        # 24, 36
    ))


    def Function_0_A54(): pass

    label("Function_0_A54")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_A8C"),
        (1, "loc_A98"),
        (2, "loc_AA4"),
        (3, "loc_AB0"),
        (4, "loc_ABC"),
        (5, "loc_AC8"),
        (6, "loc_AD4"),
        (SWITCH_DEFAULT, "loc_AE0"),
    )


    label("loc_A8C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_A98")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AA4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AB0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_ABC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AC8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AD4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AE0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_AEC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B03")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_AEC")

    label("loc_B03")

    Return()

    # Function_0_A54 end

    def Function_1_B04(): pass

    label("Function_1_B04")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B1F")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_B04")

    label("loc_B1F")

    Return()

    # Function_1_B04 end

    def Function_2_B20(): pass

    label("Function_2_B20")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B31")
    Call(0, 24)

    label("loc_B31")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B45")
    ClearScenarioFlags(0x22, 0)
    Event(0, 34)
    Jump("loc_B57")

    label("loc_B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_B57")
    ClearScenarioFlags(0x22, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 35)

    label("loc_B57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6E")
    Event(0, 28)

    label("loc_B6E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BBC")
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetScenarioFlags(0x151, 1)
    SetScenarioFlags(0x151, 2)
    SetScenarioFlags(0x151, 3)

    label("loc_BBC")

    Return()

    # Function_2_B20 end

    def Function_3_BBD(): pass

    label("Function_3_BBD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BE8")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BE3")
    ClearMapFlags(0x2000)
    Jump("loc_BE8")

    label("loc_BE3")

    SetMapFlags(0x2000)

    label("loc_BE8")

    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    SetMapObjFlags(0x2, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C32")
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x1, 0x4)

    label("loc_C32")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CA6")

    label("loc_C4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_C68")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)
    Jump("loc_CA6")

    label("loc_C68")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x143, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C81")
    OP_C9(0x0, 0x8)
    Jump("loc_CA6")

    label("loc_C81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C9D")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CA6")

    label("loc_C9D")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CA6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_CBF")
    OP_10(0x0, 0x0)
    OP_10(0x1A, 0x1)
    Jump("loc_CC5")

    label("loc_CBF")

    OP_10(0x0, 0x1)
    OP_10(0x1A, 0x0)

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x16B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_CD9")
    OP_1B(0x1, 0x0, 0x21)

    label("loc_CD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_END)), "loc_D3D")
    SetMapObjFrame(0x7, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x1, 0x1)
    SetMapObjFrame(0x7, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_2", 0x0, 0x1)
    Jump("loc_D93")

    label("loc_D3D")

    SetMapObjFrame(0x7, "moni_r", 0x1, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x1, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_2", 0x0, 0x1)

    label("loc_D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_END)), "loc_DF7")
    SetMapObjFrame(0x8, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x8, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x8, "light_g", 0x1, 0x1)
    SetMapObjFrame(0x8, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_2", 0x0, 0x1)
    Jump("loc_E4D")

    label("loc_DF7")

    SetMapObjFrame(0x8, "moni_r", 0x1, 0x1)
    SetMapObjFrame(0x8, "light_r", 0x1, 0x1)
    SetMapObjFrame(0x8, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x8, "light_g", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_2", 0x0, 0x1)

    label("loc_E4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_END)), "loc_EB1")
    SetMapObjFrame(0x9, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x9, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x9, "light_g", 0x1, 0x1)
    SetMapObjFrame(0x9, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_2", 0x0, 0x1)
    Jump("loc_F07")

    label("loc_EB1")

    SetMapObjFrame(0x9, "moni_r", 0x1, 0x1)
    SetMapObjFrame(0x9, "light_r", 0x1, 0x1)
    SetMapObjFrame(0x9, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x9, "light_g", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_2", 0x0, 0x1)

    label("loc_F07")

    ClearMapObjFlags(0x11, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F43")
    SetMapObjFrame(0x11, "lock_r", 0x0, 0x1)
    SetMapObjFrame(0x11, "lock_g", 0x1, 0x1)
    OP_70(0x11, 0x28)
    Jump("loc_F63")

    label("loc_F43")

    SetMapObjFrame(0x11, "lock_r", 0x1, 0x1)
    SetMapObjFrame(0x11, "lock_g", 0x0, 0x1)
    OP_70(0x11, 0x0)

    label("loc_F63")

    OP_10(0xF, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F9E")
    SetMapObjFrame(0x12, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)
    Jump("loc_1001")

    label("loc_F9E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDC")
    SetMapObjFrame(0x12, "Null_color", 0x0, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x1, 0x1)
    Jump("loc_1001")

    label("loc_FDC")

    SetMapObjFrame(0x12, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)

    label("loc_1001")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 16000, -6000, 343500, 4000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_104A")
    SetMapObjFrame(0xFF, "Null_door", 0x2, "close")
    SetMapObjFlags(0x14, 0x4)
    SetBarrier(0x3, 0x0, 0x1)
    Jump("loc_106F")

    label("loc_104A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_106F")
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetMapObjFlags(0x14, 0x4)
    SetBarrier(0x2, 0x0, 0x1)

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1088")
    ClearChrFlags(0x24, 0x80)
    ModifyEventFlags(1, 0, 0x80)
    SetChrFlags(0x24, 0x8000)

    label("loc_1088")

    OP_52(0x24, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1161")
    OP_70(0x3, 0x0)
    Jump("loc_1165")

    label("loc_1161")

    OP_70(0x3, 0x1E)

    label("loc_1165")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1178")
    OP_70(0x4, 0x0)
    Jump("loc_117C")

    label("loc_1178")

    OP_70(0x4, 0x1E)

    label("loc_117C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_118F")
    OP_70(0x5, 0x0)
    Jump("loc_1193")

    label("loc_118F")

    OP_70(0x5, 0x1E)

    label("loc_1193")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A6")
    OP_70(0x6, 0x0)
    Jump("loc_11AA")

    label("loc_11A6")

    OP_70(0x6, 0x1E)

    label("loc_11AA")

    Return()

    # Function_3_BBD end

    def Function_4_11AB(): pass

    label("Function_4_11AB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅱ', 1)"), scpexpr(EXPR_END)), "loc_122E")
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
    SetScenarioFlags(0x1F0, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1298")

    label("loc_122E")

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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1298")

    Jump("loc_12DA")

    label("loc_129D")

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

    label("loc_12DA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_11AB end

    def Function_5_12E6(): pass

    label("Function_5_12E6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A6")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13E3")
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x18, 0x0, 0)
    OP_98(0x18, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1343():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1343)

    def lambda_135D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_135D)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x18, 1)
    Battle("BattleInfo_8D8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x18, 0x80)
    ClearChrFlags(0x18, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_13C4"),
        (2, "loc_13D3"),
        (1, "loc_13E0"),
        (SWITCH_DEFAULT, "loc_13E3"),
    )


    label("loc_13C4")

    SetScenarioFlags(0x217, 1)
    OP_70(0x4, 0x1E)
    Sleep(500)
    Jump("loc_13E3")

    label("loc_13D3")

    OP_70(0x4, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13E0")

    OP_B9(0x0)
    Return()

    label("loc_13E3")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('命中３', 1)"), scpexpr(EXPR_END)), "loc_143A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_14A1")

    label("loc_143A")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '命中３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14A1")

    Jump("loc_14D8")

    label("loc_14A6")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_14D8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12E6 end

    def Function_6_14E4(): pass

    label("Function_6_14E4")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D6")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药', 1)"), scpexpr(EXPR_END)), "loc_1567")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_15D1")

    label("loc_1567")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_15D1")

    Jump("loc_1613")

    label("loc_15D6")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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

    label("loc_1613")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_14E4 end

    def Function_7_161F(): pass

    label("Function_7_161F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1749")
    Sound(14, 0, 100, 0)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x6, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×８０\x01\x07\x02",

            "#57I水之耀晶片×８０\x01\x07\x02",

            "#58I火之耀晶片×８０\x01\x07\x02",

            "#59I风之耀晶片×８０\x01\x07\x02",

            "#60I时之耀晶片×８０\x01\x07\x02",

            "#61I空之耀晶片×８０\x01\x07\x02",

            "#62I幻之耀晶片×８０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F1, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1766")

    label("loc_1749")


    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1766")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_161F end

    def Function_8_1778(): pass

    label("Function_8_1778")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1785")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_198A")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1937")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18C3")

    #C0013
    ChrTalk(
        0x15,
        (
            "#10103F突入兰花塔的作战……\x01",
            "想必会相当激烈。\x02\x03",

            "#10101F作战一旦开始，\x01",
            "恐怕就很难回头了……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#00103F是啊……\x01",
            "不知会发生什么情况，\x01",
            "一定要做好万全准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x15,
        (
            "#10100F最好趁现在\x01",
            "去市内的设施\x01",
            "补给一番哦。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1932")

    label("loc_18C3")


    #C0016
    ChrTalk(
        0x15,
        (
            "#10103F突入兰花塔的作战……\x01",
            "想必会相当激烈。\x02\x03",

            "#10100F最好趁现在\x01",
            "去市内的武器店、导力商店\x01",
            "等设施补给一番。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1932")

    Jump("loc_1985")

    label("loc_1937")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1985")

    #C0017
    ChrTalk(
        0x15,
        (
            "#10100F要编组队伍吗？\x01",
            "明白了！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 24)
    OP_0D()
    Jump("loc_1985")

    label("loc_1985")

    Jump("loc_1785")

    label("loc_198A")

    TalkEnd(0xFE)
    Return()

    # Function_8_1778 end

    def Function_9_198E(): pass

    label("Function_9_198E")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_199B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B56")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B06")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A79")

    #C0018
    ChrTalk(
        0x16,
        (
            "#10403F……说起来，从这里出去之后，\x01",
            "就是旧城区了呢。\x02\x03",

            "#10402F呵呵，机会难得，\x01",
            "顺便去『崔尼蒂』\x01",
            "露个面如何？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1B01")

    label("loc_1A79")


    #C0019
    ChrTalk(
        0x16,
        (
            "#10404F旧城区那边就交给圣书会，\x01",
            "应该不会有问题。\x02\x03",

            "#10400F我们还是集中精神，\x01",
            "专心准备作战吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B01")

    #C0020
    ChrTalk(
        0x101,
        "#00000F嗯……是啊。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1B01")

    Jump("loc_1B51")

    label("loc_1B06")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B51")

    #C0021
    ChrTalk(
        0x16,
        "#10400F呵呵，要编组队伍吗？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 24)
    OP_0D()
    Jump("loc_1B51")

    label("loc_1B51")

    Jump("loc_199B")

    label("loc_1B56")

    TalkEnd(0xFE)
    Return()

    # Function_9_198E end

    def Function_10_1B5A(): pass

    label("Function_10_1B5A")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B67")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D4E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFC")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CBD")

    #C0022
    ChrTalk(
        0x101,
        "#00005F莉夏，你在这里啊。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x17,
        (
            "#10702F嗯……\x01",
            "在作战开始之前，我想找个\x01",
            "安静的地方提升斗气。\x02\x03",

            "#10703F因为『血腥谢莉』\x01",
            "应该也在\x01",
            "兰花塔内……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#00301F嗯……她和叔叔他们\x01",
            "肯定会百般阻挠我们的。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x17,
        "#10701F……我绝对不会输的。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1CF7")

    label("loc_1CBD")


    #C0026
    ChrTalk(
        0x17,
        (
            "#10703F『血腥谢莉』……\x02\x03",

            "#10701F……我绝对不会输的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF7")

    Jump("loc_1D49")

    label("loc_1CFC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D49")

    #C0027
    ChrTalk(
        0x17,
        "#10700F好的，是要编组队伍吧？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 24)
    OP_0D()
    Jump("loc_1D49")

    label("loc_1D49")

    Jump("loc_1B67")

    label("loc_1D4E")

    TalkEnd(0xFE)
    Return()

    # Function_10_1B5A end

    def Function_11_1D52(): pass

    label("Function_11_1D52")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1D5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F9E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",          # 0
            "编组队伍\x01",      # 1
            "放弃\x01",          # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F45")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EDF")

    #C0028
    ChrTalk(
        0x9,
        (
            "#00603F我也会与你们一起\x01",
            "参加突入兰花塔的作战。\x02\x03",

            "#00600F你们要趁现在\x01",
            "做好充分准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#00000F嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，有达德利警官在，\x01",
            "真是让人信心百倍呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#00603F逮捕总统的任务\x01",
            "不能交给支援科独自处理……\x01",
            "仅此而已。\x02\x03",

            "#00600F如果听明白了，\x01",
            "就赶快出发吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1F40")

    label("loc_1EDF")


    #C0032
    ChrTalk(
        0x9,
        (
            "#00603F你们想必也明白……\x01",
            "逮捕总统可不像\x01",
            "嘴上说的那么简单。\x02\x03",

            "#00600F趁现在做好\x01",
            "充分准备吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F40")

    Jump("loc_1F99")

    label("loc_1F45")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F99")

    #C0033
    ChrTalk(
        0x9,
        (
            "#00600F要编组队伍吗？\x01",
            "……赶快决定。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_32(0xFF, 0xF9, 0x0)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    Fade(500)
    Call(0, 24)
    OP_0D()
    Jump("loc_1F99")

    label("loc_1F99")

    Jump("loc_1D5F")

    label("loc_1F9E")

    TalkEnd(0xFE)
    Return()

    # Function_11_1D52 end

    def Function_12_1FA2(): pass

    label("Function_12_1FA2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2148")

    #C0034
    ChrTalk(
        0x8,
        (
            "#01002F呵呵，话说回来……\x01",
            "你们几个好像都很有精神啊，\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#00202F科长才是呢……\x01",
            "您平安无事真让人高兴。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00000F科长，你们一直在市内\x01",
            "展开地下活动吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#01003F嗯，我们最近以此处为据点，\x01",
            "正准备慢慢商讨打开局面的对策……\x02\x03",

            "#01001F但既然现在情况变成这样，\x01",
            "便不能再\x01",
            "慢悠悠地研究了。\x02\x03",

            "你们无论如何也要在\x01",
            "这次的作战中取得成功。\x01",
            "……这也是为了夺回琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00000F嗯……交给我们吧！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 4)
    Jump("loc_227E")

    label("loc_2148")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221A")

    #C0039
    ChrTalk(
        0x8,
        (
            "#01003F既然现在情况变成这样，\x01",
            "便不能再慢悠悠地研究了。\x02\x03",

            "#01001F你们无论如何也要在\x01",
            "突入兰花塔的作战行动中\x01",
            "取得成功。\x02\x03",

            "#01002F这是为了广大市民……\x01",
            "更是为了你们和琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00000F是……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_227E")

    label("loc_221A")


    #C0041
    ChrTalk(
        0x8,
        (
            "#01004F我也仔细检修一下\x01",
            "我的霰弹枪吧。\x02\x03",

            "#01001F突入兰花塔的作战行动……\x01",
            "无论如何也要取得成功。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_227E")

    TalkEnd(0xFE)
    Return()

    # Function_12_1FA2 end

    def Function_13_2282(): pass

    label("Function_13_2282")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_239A")

    #C0042
    ChrTalk(
        0xA,
        (
            "好～在作战开始之前，\x01",
            "一定要仔细检查装备～\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "……对了，\x01",
            "听说你们去医院\x01",
            "探望了多诺邦警督啊～\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "怎么样？\x01",
            "他恢复得还好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00100F嗯，他的夫人也过去看护了，\x01",
            "现在好像已经接近痊愈了。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xA,
        "哈哈，那就好。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            "警督不在的时候，\x01",
            "我们必须要全力加油啊～\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_23F6")

    label("loc_239A")


    #C0048
    ChrTalk(
        0xA,
        (
            "好～在作战开始之前，\x01",
            "一定要仔细检查装备～\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xA,
        (
            "警督不在的时候，\x01",
            "我们必须要全力加油啊～\x02",
        )
    )

    CloseMessageWindow()

    label("loc_23F6")

    TalkEnd(0xFE)
    Return()

    # Function_13_2282 end

    def Function_14_23FA(): pass

    label("Function_14_23FA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24F4")

    #C0050
    ChrTalk(
        0xD,
        (
            "突入作战开始之后，\x01",
            "我们也要将市民的安全\x01",
            "摆在第一位。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xD,
        (
            "我的特长不是战斗，\x01",
            "到时我会在作战范围内引导\x01",
            "民众避难，以免他们遭到伤害。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        "#00100F那个任务也非常重要呢……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F我们也会多加小心的……\x01",
            "引导任务就拜托您了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_257C")

    label("loc_24F4")


    #C0054
    ChrTalk(
        0xD,
        (
            "我的特长不是战斗，\x01",
            "到时我会在作战范围内引导\x01",
            "民众避难，以免他们遭到伤害。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xD,
        (
            "即使在这种状况下，\x01",
            "我们也要将市民的安全\x01",
            "摆在第一位。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_257C")

    TalkEnd(0xFE)
    Return()

    # Function_14_23FA end

    def Function_15_2580(): pass

    label("Function_15_2580")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2677")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_263D")
    TurnDirection(0xB, 0x10A, 0)

    #C0056
    ChrTalk(
        0x10A,
        (
            "#00603F艾玛，这边的事情就交给你了。\x02\x03",

            "#00600F据点的周边\x01",
            "要重点警戒，\x01",
            "避免给作战行动造成妨碍。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "嗯，明白了。\x01",
            "……达德利长官，您也要小心。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2672")

    label("loc_263D")


    #C0058
    ChrTalk(
        0xB,
        (
            "这里就交给我们吧。\x01",
            "……达德利长官，您也要小心。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2672")

    Jump("loc_278E")

    label("loc_2677")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2745")

    #C0059
    ChrTalk(
        0xB,
        (
            "我们正在重新确认\x01",
            "作战的流程。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xB,
        (
            "你们也已经把作战步骤\x01",
            "牢记清楚了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#00000F嗯，当然。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xB,
        "……很好。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "作战能否成功，\x01",
            "很大程度上取决于你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        "准备工作一定要充分做好。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_278E")

    label("loc_2745")


    #C0065
    ChrTalk(
        0xB,
        (
            "作战能否成功，\x01",
            "很大程度上取决于你们。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        "准备工作一定要充分做好。\x02",
    )

    CloseMessageWindow()

    label("loc_278E")

    TalkEnd(0xFE)
    Return()

    # Function_15_2580 end

    def Function_16_2792(): pass

    label("Function_16_2792")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2880")

    #C0067
    ChrTalk(
        0xE,
        (
            "独立无效宣言发表之后，\x01",
            "总部的警官们也陆续集结，\x01",
            "前来协助我们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xE,
        (
            "弗兰茨主动担负起了\x01",
            "与他们联络的任务。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#00005F弗兰茨吗……？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xE,
        (
            "嗯，为了守护警察的荣耀，\x01",
            "大家都在拼命努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xE,
        "也拜托你们多多加油了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_28C9")

    label("loc_2880")


    #C0072
    ChrTalk(
        0xE,
        (
            "为了守护警察的荣耀，\x01",
            "大家都在拼命努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xE,
        "也拜托你们多多加油了。\x02",
    )

    CloseMessageWindow()

    label("loc_28C9")

    TalkEnd(0xFE)
    Return()

    # Function_16_2792 end

    def Function_17_28CD(): pass

    label("Function_17_28CD")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D6")

    #C0074
    ChrTalk(
        0xF,
        (
            "要想突破众多『魔导兵』的守卫，\x01",
            "靠警察局的警车也不是不行，\x01",
            "但性能实在是有些勉强。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xF,
        (
            "从马力与速度方面来考虑，\x01",
            "你们的车辆\x01",
            "是必不可少的。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00004F嗯，我们无论如何也会把车找到。\x02\x03",

            "#00000F凯特前辈，你们也要小心。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xF,
        "嗯，你们也要加油啊！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_2A25")

    label("loc_29D6")


    #C0078
    ChrTalk(
        0xF,
        (
            "在作战开始之前，\x01",
            "我们就在这里进行突入的准备。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xF,
        "罗伊德，你们要加油哦！\x02",
    )

    CloseMessageWindow()

    label("loc_2A25")

    TalkEnd(0xFE)
    Return()

    # Function_17_28CD end

    def Function_18_2A29(): pass

    label("Function_18_2A29")

    TalkBegin(0xFE)
    Fade(500)
    OP_6B(0xFF)
    OP_68(-12940, -13300, 188130, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B96")

    #C0080
    ChrTalk(
        0xC,
        (
            "如果向兰花塔发动的网络入侵能取得成功，\x01",
            "便可以解除妨碍通讯的干扰波了。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "你们乘坐的那艘飞艇\x01",
            "是叫梅尔卡瓦吧？\x01",
            "到时候也可以和那里取得联络哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#00203F嗯，那样的话，\x01",
            "似乎就可以随时\x01",
            "接受约纳的支援了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xC,
        (
            "嗯，约纳的协助\x01",
            "胜过百人之力啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        (
            "为此，我们一定要\x01",
            "成功完成\x01",
            "网络入侵！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_2BEA")

    label("loc_2B96")


    #C0085
    ChrTalk(
        0xC,
        (
            "网络入侵要想成功，\x01",
            "大概还需再花费些时间。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        (
            "缇欧，你们一定要\x01",
            "多加小心哦～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2BEA")

    Fade(500)
    OP_6B(0x0)
    OP_69(0xFF, 0x0)
    OP_0D()
    TalkEnd(0xFE)
    Return()

    # Function_18_2A29 end

    def Function_19_2BFB(): pass

    label("Function_19_2BFB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CCB")

    #C0087
    ChrTalk(
        0x10,
        (
            "我原本在ＩＢＣ的技术部任职，\x01",
            "但在听了独立无效宣言之后，\x01",
            "就从那里逃出来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x10,
        (
            "达比德那家伙说是\x01",
            "愿意相信玛丽亚贝尔小姐，\x01",
            "还留在兰花塔……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x10,
        (
            "如今发生了这样的情况，\x01",
            "他不要紧吧……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_2D40")

    label("loc_2CCB")


    #C0090
    ChrTalk(
        0x10,
        (
            "留在兰花塔的\x01",
            "达比德不要紧吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x10,
        (
            "我们分别的时候还吵了一架，\x01",
            "真是很担心他啊……\x01",
            "不过现在还是专心协助主任吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D40")

    TalkEnd(0xFE)
    Return()

    # Function_19_2BFB end

    def Function_20_2D44(): pass

    label("Function_20_2D44")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2DE2")

    #C0092
    ChrTalk(
        0x11,
        (
            "那些魔导兵\x01",
            "如今还没有\x01",
            "侵入室内的迹象……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x11,
        (
            "但如果这种状态长期持续下去，\x01",
            "谁也不知道它们会怎样。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x11,
        "要是能尽快打开局面就好了……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_2E4E")

    label("loc_2DE2")


    #C0095
    ChrTalk(
        0x11,
        (
            "虽说在外出禁止令下达之后，\x01",
            "市民们几乎都待在室内，\x01",
            "但情况仍然很危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x11,
        "要是能尽快打开局面就好了……\x02",
    )

    CloseMessageWindow()

    label("loc_2E4E")

    TalkEnd(0xFE)
    Return()

    # Function_20_2D44 end

    def Function_21_2E52(): pass

    label("Function_21_2E52")

    TalkBegin(0xFE)

    #C0097
    ChrTalk(
        0x12,
        (
            "呼……\x01",
            "实在是紧张啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x12,
        "希望突入作战能取得成功……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_2E52 end

    def Function_22_2E94(): pass

    label("Function_22_2E94")

    TalkBegin(0xFE)

    #C0099
    ChrTalk(
        0x13,
        (
            "魔导兵吗……\x01",
            "总统竟然还准备了\x01",
            "这么一张底牌啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x13,
        (
            "虽然很危险……\x01",
            "但我们也只能拼了。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_2E94 end

    def Function_23_2EF6(): pass

    label("Function_23_2EF6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FB5")

    #C0101
    ChrTalk(
        0x14,
        (
            "保存在这个区域的武器\x01",
            "是从某个渠道采购的。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x14,
        (
            "本来都属于违法的武器，\x01",
            "但在物资不足的状况下，\x01",
            "也顾不上那么多了。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x14,
        (
            "最重要的是，希望这些武器\x01",
            "能对魔导兵发挥作用……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_300D")

    label("loc_2FB5")


    #C0104
    ChrTalk(
        0x14,
        (
            "保存在这个区域的武器\x01",
            "是从某个渠道采购的。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x14,
        (
            "希望这些武器\x01",
            "能对魔导兵发挥作用……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_300D")

    TalkEnd(0xFE)
    Return()

    # Function_23_2EF6 end

    def Function_24_3011(): pass

    label("Function_24_3011")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, -8400, -8000, 606060, 90)
    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, -2170, -8000, 595370, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrPos(0xD, 7340, -16000, 184650, 180)
    ClearChrFlags(0xE, 0x80)
    SetChrPos(0xE, 7390, -16000, 191840, 270)
    ClearChrFlags(0xF, 0x80)
    SetChrPos(0xF, 6000, -16000, 191840, 90)
    ClearChrFlags(0xC, 0x80)
    SetChrPos(0xC, -9560, -16000, 190630, 17)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, -8410, -16000, 188790, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 7350, -16000, 183270, 0)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, -6040, -16000, 175740, 135)
    ClearChrFlags(0x14, 0x80)
    SetChrPos(0x14, -520, -8000, 606410, 90)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3127")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -6000, -8000, 595580, 0)

    label("loc_3127")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_314D")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -9520, -16000, 188860, 0)

    label("loc_314D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3173")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -5840, 0, 608620, 225)

    label("loc_3173")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_31CA")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 17080, -16000, 178000, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 135)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 45)
    Jump("loc_31F6")

    label("loc_31CA")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 0)

    label("loc_31F6")

    Return()

    # Function_24_3011 end

    def Function_25_31F7(): pass

    label("Function_25_31F7")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0106
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32CC")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x13, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x13, 0x0)
    OP_71(0x13, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x13)
    OP_71(0x13, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x13, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_32CC")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_25_31F7 end

    def Function_26_32DB(): pass

    label("Function_26_32DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_32E5")
    Return()

    label("loc_32E5")

    EventBegin(0x1)
    OP_52(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    SetChrSubChip(0x4, 0x0)
    SetChrSubChip(0x5, 0x0)
    SetChrSubChip(0x6, 0x0)
    SetChrSubChip(0x7, 0x0)
    SetChrName("")

    #A0107
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "蕴藏着强大力量的魔兽在此游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_33B9"),
        (SWITCH_DEFAULT, "loc_33D2"),
    )


    label("loc_33B9")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -499760, 0, 494390, 0)
    EventEnd(0x5)
    Return()

    label("loc_33D2")

    Battle("BattleInfo_91C", 0x0, 0x0, 0x100, 0xC, 0xFF)
    OP_E2(0x2)
    EventBegin(0x1)
    OP_68(-499760, 1000, 494390, 0)
    OP_90(0x0, -499760, 0, 494390, 0)
    OP_90(0x1, -499760, 0, 494390, 0)
    OP_90(0x2, -499760, 0, 494390, 0)
    OP_90(0x3, -499760, 0, 494390, 0)
    OP_90(0x4, -499760, 0, 494390, 0)
    OP_90(0x5, -499760, 0, 494390, 0)
    OP_90(0x6, -499760, 0, 494390, 0)
    OP_90(0x7, -499760, 0, 494390, 0)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_3494"),
        (1, "loc_3499"),
        (SWITCH_DEFAULT, "loc_349C"),
    )


    label("loc_3494")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_3499")

    OP_B9(0x0)
    Return()

    label("loc_349C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x24, 0x80)
    OP_E2(0x3)
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "击退了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0109
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21E, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_357C")
    Sound(629, 0, 100, 0)
    Sound(842, 0, 100, 0)
    Sleep(3000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0110
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "感觉到一股极其惊人的力量在某处苏醒了！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x21F, 0)

    label("loc_357C")

    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_26_32DB end

    def Function_27_3586(): pass

    label("Function_27_3586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3598")
    Call(0, 36)
    Return()

    label("loc_3598")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是升降机的控制面板。\x01",
            "要操作吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36DE")
    Fade(500)
    SetChrPos(0x0, 5000, 0, 747500, 0)
    SetChrPos(0x1, 6000, 0, 747500, 0)
    SetChrPos(0x2, 5000, 0, 746500, 0)
    SetChrPos(0x3, 6000, 0, 746500, 0)
    OP_68(5230, 0, 745110, 0)
    MoveCamera(25, 57, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_71(0x12, 0xA, 0xC8, 0x0, 0x0)
    Sleep(200)
    OP_68(6000, 2000, 762000, 3800)
    MoveCamera(22, 29, 0, 3800)
    Sleep(1800)
    Sound(150, 2, 100, 0)
    Sleep(200)
    FadeToDark(500, 0, -1)
    Sleep(4000)
    StopSound(150, 1000, 100)
    Sleep(1000)
    OP_0D()
    NewScene("m0309", 108, 0, 0)
    IdleLoop()

    label("loc_36DE")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_27_3586 end

    def Function_28_36E6(): pass

    label("Function_28_36E6")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_70(0x12, 0x64)
    Sleep(1)
    OP_68(4580, 2750, 757170, 0)
    MoveCamera(19, 37, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_90(0x0, 3500, 2750, 759000, 270)
    OP_90(0x1, 3500, 2750, 758000, 270)
    OP_90(0x2, 4500, 2750, 759000, 270)
    OP_90(0x3, 4500, 2750, 758000, 270)
    Sound(145, 0, 100, 0)
    OP_68(4030, 0, 745730, 3200)
    MoveCamera(53, 41, 0, 3200)
    OP_71(0x12, 0x64, 0xA, 0x0, 0x0)
    FadeToBright(500, 0)
    Sleep(3400)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x12)
    OP_6F(0x1)
    Sleep(500)
    SetMapObjFrame(0x12, "Null_color", 0x1, 0x1)
    SetMapObjFrame(0x12, "Null_color2", 0x0, 0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_28_36E6 end

    def Function_29_37F5(): pass

    label("Function_29_37F5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_END)), "loc_3830")
    TalkBegin(0xFF)
    SetChrName("")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开关已经按下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3957")

    label("loc_3830")

    EventBegin(0x1)

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个开关。\x01",
            "要操作吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3950")
    Fade(500)
    SetChrPos(0x0, -10890, -16000, 191940, 0)
    SetChrPos(0x1, -9900, -16000, 191760, 0)
    SetChrPos(0x2, -11180, -16000, 190380, 0)
    SetChrPos(0x3, -10290, -16000, 190460, 0)
    OP_68(-12300, -13300, 188960, 0)
    MoveCamera(34, 25, 0, 0)
    OP_6E(620, 0)
    SetCameraDistance(12500, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0x7, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x151, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3950")
    Call(0, 32)

    label("loc_3950")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_3957")

    Return()

    # Function_29_37F5 end

    def Function_30_3958(): pass

    label("Function_30_3958")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_END)), "loc_3993")
    TalkBegin(0xFF)
    SetChrName("")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开关已经按下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3AB9")

    label("loc_3993")

    EventBegin(0x1)

    #A0115
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个开关。\x01",
            "要操作吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AB2")
    Fade(500)
    SetChrPos(0x0, 9590, -8000, 192060, 0)
    SetChrPos(0x1, 10650, -8000, 191930, 0)
    SetChrPos(0x2, 9680, -8000, 190620, 0)
    SetChrPos(0x3, 10730, -8000, 190350, 0)
    OP_68(8740, -5300, 191340, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0x8, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x8, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x8, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x8, "light_g", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x151, 2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3AB2")
    Call(0, 32)

    label("loc_3AB2")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_3AB9")

    Return()

    # Function_30_3958 end

    def Function_31_3ABA(): pass

    label("Function_31_3ABA")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_END)), "loc_3AF5")
    TalkBegin(0xFF)
    SetChrName("")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开关已经按下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3C1B")

    label("loc_3AF5")

    EventBegin(0x1)

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个开关。\x01",
            "要操作吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C14")
    Fade(500)
    SetChrPos(0x0, -15480, -8000, 191340, 45)
    SetChrPos(0x1, -16480, -8000, 191930, 45)
    SetChrPos(0x2, -16830, -8000, 190290, 45)
    SetChrPos(0x3, -17830, -8000, 190910, 45)
    OP_68(-16450, -5300, 190460, 0)
    MoveCamera(39, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0x9, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x9, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x9, "moni_g", 0x1, 0x1)
    SetMapObjFrame(0x9, "light_g", 0x1, 0x1)
    OP_0D()
    Sleep(1000)
    SetScenarioFlags(0x151, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3C14")
    Call(0, 32)

    label("loc_3C14")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_3C1B")

    Return()

    # Function_31_3ABA end

    def Function_32_3C1C(): pass

    label("Function_32_3C1C")

    Fade(500)
    OP_68(-3140, -13300, 193070, 0)
    MoveCamera(41, 13, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0x11, "lock_r", 0x0, 0x1)
    SetMapObjFrame(0x11, "lock_g", 0x1, 0x1)
    OP_0D()
    Sleep(500)
    Sound(147, 0, 100, 0)
    OP_71(0x11, 0x0, 0x28, 0x0, 0x0)
    Sleep(1300)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    Return()

    # Function_32_3C1C end

    def Function_33_3CA8(): pass

    label("Function_33_3CA8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-19510, -11300, 175870, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x101, -2029, -14000, 165880, 0)
    SetChrPos(0x102, -3420, -14000, 165480, 0)
    SetChrPos(0x103, -650, -14000, 165410, 0)
    SetChrPos(0x104, -2060, -14000, 164380, 0)
    SetChrPos(0x109, -3340, -14000, 164200, 0)
    SetChrPos(0x105, -820, -14000, 164140, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(-1020, -11300, 176610, 8000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)

    def lambda_3D80():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D80)
    Sleep(50)

    def lambda_3D9D():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3D9D)
    Sleep(50)

    def lambda_3DBA():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3DBA)
    Sleep(50)

    def lambda_3DD7():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3DD7)
    Sleep(50)

    def lambda_3DF4():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3DF4)
    Sleep(50)

    def lambda_3E11():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3E11)
    OP_6F(0x1)
    OP_68(-4630, -11300, 167910, 5000)
    MoveCamera(45, 27, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(14590, 5000)
    OP_6F(0x79)

    #C0118
    ChrTalk(
        0x104,
        (
            "#12P#00305F唔，来到了一处相当辽阔的地方啊。\x02\x03",

            "#00303F在通商会议那起事件时，\x01",
            "我们从兰花塔下到地下后也曾见到过\x01",
            "类似的地方，当时真是大吃一惊呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00000F嗯，不过那个地方\x01",
            "和这里应该有很远的距离……\x02\x03",

            "#00006F没想到竟然连\x01",
            "旧城区的地下\x01",
            "都建有这么广阔的空间啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，从兰花塔的地下\x01",
            "一直通到旧城区的地下，\x01",
            "这到底要花费多少米拉啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#00200F另外，我以前听说\x01",
            "建造Ｄ区域的目的\x01",
            "是将其作为停车场……\x02\x03",

            "#00206F但根本就没有车\x01",
            "停在这里呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x102,
        (
            "#6P#00103F是啊……\x02\x03",

            "#00101F就算是导力车已经普及的共和国，\x01",
            "恐怕也用不上这么大面积的停车场。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x109,
        (
            "#12P#10106F更重要的是，把停车场\x01",
            "这种地方建造在旧城区的地下，\x01",
            "又有几个人能用得上呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#00006F的确有很多疑问……\x02\x03",

            "#00000F……但我们现在的首要任务\x01",
            "还是去驱逐通缉魔兽。\x02\x03",

            "继续向深处前进吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x16B, 3)
    OP_1B(0x1, 0xFF, 0xFFFF)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetChrPos(0x0, -2029, -14000, 168880, 0)
    EventEnd(0x5)
    Return()

    # Function_33_3CA8 end

    def Function_34_4178(): pass

    label("Function_34_4178")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x1)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -9600, -16000, 190500, 0)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -10400, -16000, 188100, 0)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, -11300, -16000, 189000, 0)
    OP_4B(0x9, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -12500, -16000, 188600, 0)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -10800, -16000, 190900, 0)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -12000, -16000, 190500, 0)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -13800, -16000, 189400, 45)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -13000, -16000, 190900, 45)
    OP_4B(0xE, 0xFF)
    SetMapObjFrame(0x7, "moni_1", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_2", 0x1, 0x1)
    SetMapObjFrame(0x7, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x1, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    OP_70(0x11, 0x28)
    OP_68(12000, -14000, 182000, 0)
    MoveCamera(60, 15, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(-8000, -14000, 187000, 7000)
    SetCameraDistance(23000, 7000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-10900, -14500, 193200, 0)
    MoveCamera(31, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(16000, 1500)
    OP_6F(0x79)
    Sleep(500)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("麦克道尔议长")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30W为了能让大家一起\x01",
            "思考这个问题……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("麦克道尔议长")

    #A0126
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S我以自治州代表之一的身份，\x01",
            "正式在此宣布──\x01",
            "『克洛斯贝尔独立宣言』无效！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-10900, -14900, 190900, 1000)
    MoveCamera(39, 21, 0, 1000)
    OP_6F(0x79)

    #C0127
    ChrTalk(
        0xA,
        "#11P哦哦！终于说出来了啊！\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "#12P这、这样一来，\x01",
            "我们的行动多少能宽松一些了……！\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        "#11P#00604F嗯……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0130
    ChrTalk(
        0x9,
        (
            "#5P#00602F赛尔盖长官，\x01",
            "这是在他们的协助下发表的吧？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0131
    ChrTalk(
        0x8,
        (
            "#11P#01004F呵呵……\x01",
            "除此之外，还能有其它可能吗？\x02\x03",

            "#01002F好，看来我们要开始忙了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(16500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    SetScenarioFlags(0x22, 6)
    NewScene("c1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_34_4178 end

    def Function_35_467B(): pass

    label("Function_35_467B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrPos(0x101, -9300, -16000, 188800, 0)
    SetChrPos(0x102, -9600, -16000, 187300, 0)
    SetChrPos(0x103, -10400, -16000, 189000, 0)
    SetChrPos(0x104, -10700, -16000, 187500, 0)
    SetChrPos(0x109, -11900, -16000, 188000, 45)
    SetChrPos(0x105, -11600, -16000, 186800, 0)
    SetChrPos(0x106, -10000, -16000, 186000, 0)
    SetChrPos(0x10A, -6900, -16000, 189300, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    ClearChrFlags(0x6, 0x80)
    ClearChrBattleFlags(0x6, 0x8000)
    ClearChrFlags(0x7, 0x80)
    ClearChrBattleFlags(0x7, 0x8000)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -7400, -16000, 188000, 270)
    OP_4B(0x8, 0xFF)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, -6600, -16000, 190700, 225)
    OP_4B(0xB, 0xFF)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xE, -7700, -16000, 190900, 225)
    OP_4B(0xE, 0xFF)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrPos(0xC, -9600, -16000, 190500, 180)
    OP_4B(0xC, 0xFF)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, -7100, -16000, 186600, 270)
    OP_4B(0xA, 0xFF)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xD, -5800, -16000, 188300, 270)
    OP_4B(0xD, 0xFF)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrPos(0xF, -5800, -16000, 187200, 270)
    OP_4B(0xF, 0xFF)
    ClearChrFlags(0x11, 0x80)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, -5250, -16000, 186150, 270)
    OP_4B(0x11, 0xFF)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)
    SetChrPos(0x12, -4460, -16000, 188480, 270)
    OP_4B(0x12, 0xFF)
    ClearChrFlags(0x13, 0x80)
    SetChrFlags(0x13, 0x8000)
    SetChrPos(0x13, -4570, -16000, 191320, 225)
    OP_4B(0x13, 0xFF)
    ClearChrFlags(0x14, 0x80)
    SetChrFlags(0x14, 0x8000)
    SetChrPos(0x14, -5780, -16000, 192400, 225)
    OP_4B(0x14, 0xFF)
    SetMapObjFrame(0x7, "moni_1", 0x1, 0x1)
    SetMapObjFrame(0x7, "moni_2", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_r", 0x0, 0x1)
    SetMapObjFrame(0x7, "moni_g", 0x0, 0x1)
    SetMapObjFrame(0x7, "light_g", 0x1, 0x1)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)
    ClearMapObjFlags(0x2, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    OP_70(0x11, 0x28)
    OP_68(-10000, -14900, 189500, 0)
    MoveCamera(55, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15000, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0132
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x18),
            "#1K同日９：３０──\x02",
        )
    )

    Sleep(2500)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    PlayBGM("ed7566", 0)
    OP_68(-9000, -7000, 188000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(25000, 0)
    OP_68(-9000, -14500, 188000, 8000)
    PlaceName2(340, 40, "c_plac53", 0x0, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(-10000, -14900, 189500, 0)
    MoveCamera(55, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(16000, 1000)
    OP_6F(0x79)

    #C0133
    ChrTalk(
        0xC,
        (
            "#5P啊啊……缇欧\x01",
            "终于平安回来了！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        (
            "#5P听说连约纳也\x01",
            "平安获救了！？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "#5P我、我再没有别的\x01",
            "挂怀之事了～！\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#12P#00206F主任……您太激动了。\x02\x03",

            "#00202F不过，您平安无事就好。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0137
    ChrTalk(
        0xC,
        (
            "#5P啊啊！\x01",
            "缇欧竟然会因为\x01",
            "我平安无事而高兴……！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        (
            "#5P我每天向女神\x01",
            "祈祷一百次，\x01",
            "终于起了作用啊～！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x103,
        "#12P#00211F真是烦死人了。\x02",
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
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x101, 0x8, 500)

    #C0140
    ChrTalk(
        0x101,
        (
            "#5P#00012F话、话说回来……\x01",
            "竟然聚集了这么多人啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-8300, -15000, 188100, 1000)
    MoveCamera(39, 22, 0, 1000)
    SetCameraDistance(15600, 1000)

    def lambda_4C99():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_4C99)
    Sleep(50)

    def lambda_4CA9():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4CA9)
    Sleep(50)

    def lambda_4CB9():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_4CB9)
    Sleep(50)

    def lambda_4CC9():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_4CC9)
    Sleep(50)

    def lambda_4CD9():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4CD9)
    Sleep(50)

    def lambda_4CE9():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4CE9)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0141
    ChrTalk(
        0x104,
        (
            "#6P#00305F看来大家对总统的\x01",
            "不满之情确实很严重呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#11P#01003F嗯，那当然。\x02\x03",

            "#01001F毕竟他昨天突然在全市范围内\x01",
            "颁布了戒严令与禁止外出令。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x10A,
        (
            "#11P#00603F之后，当大家发现有蓝色雾气升起时，\x01",
            "就变成现在这个样子了。\x02\x03",

            "#00610F……这已经完全不是可以\x01",
            "继续坐视不管的状况了。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        "虽然无法获得正式逮捕令……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "但我们现在也只能以处理现行犯\x01",
            "的名义将总统一派的人员拘捕了。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        "#6P#00106F…………是的。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#00008F是啊……\x01",
            "好像也只有这个办法了。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x109,
        (
            "#6P#10113F那个……\x01",
            "市民们的安全状况如何呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xD,
        (
            "#11P大家目前还在老老实实地遵守着\x01",
            "戒严令与禁止外出令。\x02\x03",

            "#11P我想在市外的战斗应该\x01",
            "也起到了一定影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "#11P不过，毕竟事发突然，\x01",
            "恐怕会有很多居民准备不足。\x02\x03",

            "#11P另外，好像还有一些人正在\x01",
            "市民会馆和酒店等场所避难，\x01",
            "肯定很难熬吧～\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#6P#00306F这样啊……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        "#00208F容不得片刻犹豫呢……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        (
            "#6P#10403F话说回来，如果想\x01",
            "逮捕总统一派的人员……\x02\x03",

            "#10401F就必须要攻占\x01",
            "兰花塔吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "#11P#01003F嗯，我们已经基本\x01",
            "制定好作战计划了。\x02\x03",

            "留在市内的游击士\x01",
            "也会与我们配合。\x02\x03",

            "#01002F万事俱备，\x01",
            "就等着你们回来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        "#6P#00102F科长……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        (
            "#00204F……感谢您一直\x01",
            "等着我们。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x106,
        (
            "#6P#10701F那么，具体作战计划\x01",
            "是怎样的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x10A,
        (
            "#11P#00603F如今似乎有大群\x01",
            "之前那样的『魔导兵』\x01",
            "牢牢驻守在兰花塔前。\x02\x03",

            "#00601F我们这里的全部人员\x01",
            "将会与众游击士一同发起强袭。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xF,
        (
            "到时候，突入队伍就驾驶车辆，\x01",
            "趁机闯入兰花塔……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xF,
        (
            "随后就可以开始\x01",
            "镇压塔内人员了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0161
    ChrTalk(
        0x109,
        "#6P#10112F那个……该怎么说呢……\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x104,
        (
            "#6P#00306F这作战方案似乎相当冒险啊，\x01",
            "我们真的有胜算吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#11P#01003F国防军的士兵基本\x01",
            "都前往市外了。\x02\x03",

            "#01000F留在塔内的，恐怕只有\x01",
            "以亚里欧斯为首的少数人员。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xE,
        (
            "#5P地下空间的通路\x01",
            "仍然被封锁着。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xE,
        (
            "#5P从目前的现状来看，\x01",
            "已经没有比这更妥善的作战计划了。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#00006F……原来如此。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        "#6P#00108F既然如此……\x02",
    )

    CloseMessageWindow()

    def lambda_544F():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_544F)

    def lambda_545C():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_545C)
    Sleep(30)

    def lambda_546C():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_546C)
    Sleep(30)

    def lambda_547C():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_547C)
    Sleep(30)

    def lambda_548C():
        TurnDirection(0x106, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_548C)
    Sleep(30)

    def lambda_549C():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_549C)
    Sleep(30)

    def lambda_54AC():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_54AC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1100)

    def lambda_54D4():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_54D4)

    def lambda_54E1():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_54E1)
    Sleep(30)

    def lambda_54F1():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_54F1)
    Sleep(30)

    def lambda_5501():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5501)
    Sleep(30)

    def lambda_5511():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5511)
    Sleep(30)

    def lambda_5521():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5521)
    Sleep(30)

    def lambda_5531():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5531)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0168
    ChrTalk(
        0x101,
        (
            "#00001F突入队伍的人选\x01",
            "已经确定了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x10A,
        (
            "#11P#00605F不，目前还没有……\x02\x03",

            "#00601F嗯？莫非你们……\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#00004F嗯，如果可以，\x01",
            "请把这个任务交给我们。\x02\x03",

            "#00013F我们想亲手夺回\x01",
            "兰花塔内的琪雅。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        (
            "#6P#00304F嗯，唯独这件事\x01",
            "是不能让给别人的。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        (
            "#00202F在应对兰花塔内的安全系统等方面，\x01",
            "我应该可以起到一些作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#6P#00103F我也……很想当面\x01",
            "质问贝尔和迪塔叔叔。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x109,
        (
            "#6P#10106F虽然我之前曾以国防军\x01",
            "士兵的身份支持他们……\x02\x03",

            "#10101F但正因如此，现在才更不能置身事外。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x105,
        (
            "#6P#10404F嗯，凭现在这种阵容，\x01",
            "再凶险的场面也有能力应付。\x02\x03",

            "#10402F而且，从团队配合的角度来考虑，\x01",
            "这也是最佳方案吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x106,
        "#6P#10704F我们一定会发挥作用的。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x10A,
        "#11P#00600F你们……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "#11P#01004F……呵呵，哎呀呀。\x02\x03",

            "#01002F当年那些稚气未脱的小家伙，\x01",
            "如今已经完全可以独当一面了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#00005F科长……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "#11P#01003F好吧，\x01",
            "突入任务就交给你们了。\x02\x03",

            "#01001F不过，准备工作\x01",
            "还没有全部就绪……\x02\x03",

            "你们再稍等一阵子吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x102,
        "#6P#00105F准备工作……？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "#5P目前正在向兰花塔\x01",
            "发动网络入侵。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "#5P大约再花一个小时左右，\x01",
            "应该就能顺利侵入了。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5942():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_5942)

    def lambda_594F():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_594F)
    Sleep(50)

    def lambda_595F():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_595F)
    Sleep(50)

    def lambda_596F():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_596F)
    Sleep(50)

    def lambda_597F():
        TurnDirection(0x106, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_597F)
    Sleep(50)

    def lambda_598F():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_598F)
    Sleep(50)

    def lambda_599F():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_599F)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0184
    ChrTalk(
        0x103,
        "#6P#00205F啊……\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        "#12P#00002F真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "#11P#01004F嗯，那样一来，\x01",
            "我们就能够向突入队伍提供支援，\x01",
            "通讯妨碍波应该也会随之解除。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x10A,
        (
            "#11P#00603F另外，我们还要再次\x01",
            "与协会和各方人员联络。\x02\x03",

            "#00600F总之，就在任命你们\x01",
            "担任突入任务的前提下，\x01",
            "开始最终阶段的商讨吧。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(15850, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetChrName("")

    #A0188
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "之后，罗伊德一行与\x01",
            "赛尔盖等人就突入作战\x01",
            "进行了最终阶段的讨论……\x02\x03",

            "讨论结束后，为了取回在突入时所需使用的导力车，\x01",
            "决定回一次支援科大楼。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x101, -2600, -16000, 176600, 0)
    SetChrPos(0x102, -1400, -16000, 176600, 0)
    SetChrPos(0x103, -3400, -16000, 175500, 0)
    SetChrPos(0x104, -600, -16000, 175500, 0)
    SetChrPos(0x109, -2000, -16000, 175500, 0)
    SetChrPos(0x105, -2900, -16000, 174500, 0)
    SetChrPos(0x106, -1100, -16000, 174500, 0)
    SetChrPos(0x10A, -2000, -16000, 179000, 180)
    SetChrPos(0x8, -2900, -16000, 179800, 180)
    PlayBGM("ed7566", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x236), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(-2000, -15000, 177700, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14000, 0)
    SetCameraDistance(15000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0189
    ChrTalk(
        0x101,
        (
            "#12P#00005F也就是说，\x01",
            "达德利警官也要加入突入队伍吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x10A,
        (
            "#5P#00603F嗯，我担任过通商会议\x01",
            "的警备任务，对兰花塔的构造\x01",
            "非常熟悉。\x02\x03",

            "#00600F如果要前往市区，\x01",
            "我也可以起到一定程度的向导作用。\x02\x03",

            "#00607F另外，逮捕总统的任务\x01",
            "绝不能只交给支援科来负责！\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        "#00306F哎呀呀，又来了。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x103,
        "#12P#00204F那就这么决定吧。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        "#00109F呵呵，真是帮了大忙呢。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x109,
        (
            "#10112F对了，说起突入时\x01",
            "要使用的导力车……\x02\x03",

            "#10100F真的要选用支援科的车？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "#01004F#5P嗯，目前来看，\x01",
            "它是兼具马力与速度\x01",
            "的最强车型。\x02\x03",

            "#01002F如果要在市区内强行突破，\x01",
            "正是最合适的选择。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        "#10102F的确……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x105,
        (
            "#12P#10404F嗯，如果那辆车还在支援科，\x01",
            "我们自然没有不用的理由。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x106,
        (
            "#10708F不过……\x01",
            "我们这么多人一起在市内行动，\x01",
            "未免也太显眼了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x10A,
        (
            "#5P#00603F既然如此，那就缩减\x01",
            "同行成员的人数吧。\x02\x03",

            "#00600F部分人员留在\x01",
            "此地待命即可。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#12P#00000F明白了。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(300)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0201
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "达德利加入队伍。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6004")
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)
    Jump("loc_600C")

    label("loc_6004")

    AddCraft(0x9, 0x196)
    AddCraft(0x0, 0x196)

    label("loc_600C")

    SetMessageWindowPos(-1, -1, -1, -1)

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德和达德利习得组合战技\x01\x07\x02",

            "『钢铁雄心』\x07\x05",
            "。\x02",
        )
    )

    CloseMessageWindow()

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "两人各自消耗１００点ＣＰ，\x01",
            "便可以施展威力强大的组合技攻击。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    ClearChrFlags(0x8, 0x8000)
    ClearChrFlags(0xB, 0x8000)
    ClearChrFlags(0xA, 0x8000)
    ClearChrFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x8000)
    ClearChrFlags(0xF, 0x8000)
    ClearChrFlags(0xE, 0x8000)
    ClearChrFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x8000)
    ClearChrFlags(0x13, 0x8000)
    ClearChrFlags(0x14, 0x8000)
    OP_4C(0x8, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_4C(0xE, 0xFF)
    OP_4C(0xC, 0xFF)
    OP_4C(0xA, 0xFF)
    OP_4C(0xD, 0xFF)
    OP_4C(0xF, 0xFF)
    OP_4C(0x11, 0xFF)
    OP_4C(0x12, 0xFF)
    OP_4C(0x13, 0xFF)
    OP_4C(0x14, 0xFF)
    OP_32(0xFF, 0xFE, 0x0)
    SetScenarioFlags(0x27, 1)
    PartySelect(1)
    ClearParty()
    PartySelect(0)
    PartySelect(2)
    SetChrPos(0x0, -1020, -16000, 175200, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    Call(0, 24)
    SetScenarioFlags(0x1A5, 3)
    OP_29(0xB1, 0x1, 0x7)
    ClearScenarioFlags(0x20, 5)
    OP_C9(0x0, 0x200000)
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7150", "ed7573")
    ReplaceBGM("ed7101", "ed7573")
    ReplaceBGM("ed7116", "ed7573")
    ReplaceBGM("ed7117", "ed7573")
    ReplaceBGM("ed7111", "ed7573")
    ReplaceBGM("ed7113", "ed7573")
    EventEnd(0x5)
    Return()

    # Function_35_467B end

    def Function_36_6175(): pass

    label("Function_36_6175")

    TalkBegin(0xFF)
    SetChrName("")

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "导力似乎已经停止了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_627D")

    #C0205
    ChrTalk(
        0x101,
        "#00003F……看来无法运转呢。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#00105F前方应该就连接着\x01",
            "兰花塔的地下区域……\x02\x03",

            "#00103F多半是总统他们\x01",
            "将导力停止的吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        "#00206F原来如此，很有可能。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        (
            "#00306F看来我们也只能\x01",
            "放弃从地下空间\x01",
            "侵入兰花塔了。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 5)

    label("loc_627D")

    TalkEnd(0xFF)
    Return()

    # Function_36_6175 end

    SaveToFile()

Try(main)
