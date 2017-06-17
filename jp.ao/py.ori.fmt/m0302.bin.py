from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "セルゲイ課長",           # 1
        "ダドリー捜査官",         # 2
        "レイモンド捜査官",       # 3
        "エマ捜査官",             # 4
        "ロバーツ主任",           # 5
        "受付嬢レベッカ",         # 6
        "ジョーリッジ課長",       # 7
        "ケイト巡査長",           # 8
        "研究員クレイ",           # 9
        "警官",                   # 10
        "警官",                   # 11
        "捜査官",                 # 12
        "捜査官",                 # 13
        "ノエル",                 # 14
        "ワジ",                   # 15
        "リーシャ",               # 16
        "トライアタッカーＲⅡ",   # 17
        "bm0300",                 # 18
        "bm0300",                 # 19
        "bm0300",                 # 20
        "bm0300",                 # 21
        "bm0300",                 # 22
    ))

    ATBonus("ATBonus_604", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_624", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_6CCE", 5,   5,   5,   5,   10,  0,   0)

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
        "BattleInfo_704", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_6CCE", 35, 35, 30, 0,
        (
            ("ms84100.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84100.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84100.dat", "ms84200.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_7A0", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_6CCE", 35, 35, 30, 0,
        (
            ("ms84200.dat", "ms81800.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84200.dat", "ms81800.dat", "ms81800.dat", 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            ("ms84200.dat", "ms84100.dat", "ms84300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_664", "MonsterBattlePostion_6C4", "ed7450", "ed7453", "ATBonus_604"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_83C", 0x0000, 64, 6, 45, 6, 1, 30, 0, "bm0300", "Sepith_6CCE", 35, 35, 30, 0,
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
        "Function_5_12FC",         # 05, 5
        "Function_6_1513",         # 06, 6
        "Function_7_1664",         # 07, 7
        "Function_8_17CB",         # 08, 8
        "Function_9_1A77",         # 09, 9
        "Function_10_1C79",        # 0A, 10
        "Function_11_1EE1",        # 0B, 11
        "Function_12_21B7",        # 0C, 12
        "Function_13_2527",        # 0D, 13
        "Function_14_26F7",        # 0E, 14
        "Function_15_28EB",        # 0F, 15
        "Function_16_2B79",        # 10, 16
        "Function_17_2D10",        # 11, 17
        "Function_18_2EA8",        # 12, 18
        "Function_19_30CA",        # 13, 19
        "Function_20_323B",        # 14, 20
        "Function_21_3377",        # 15, 21
        "Function_22_33C9",        # 16, 22
        "Function_23_343B",        # 17, 23
        "Function_24_358E",        # 18, 24
        "Function_25_3774",        # 19, 25
        "Function_26_3870",        # 1A, 26
        "Function_27_3B2F",        # 1B, 27
        "Function_28_3CA1",        # 1C, 28
        "Function_29_3DB0",        # 1D, 29
        "Function_30_3F33",        # 1E, 30
        "Function_31_40B5",        # 1F, 31
        "Function_32_4237",        # 20, 32
        "Function_33_42C3",        # 21, 33
        "Function_34_481F",        # 22, 34
        "Function_35_4D62",        # 23, 35
        "Function_36_6B56",        # 24, 36
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AB")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1234")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F0, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_12A6")

    label("loc_1234")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12A6")

    Jump("loc_12F0")

    label("loc_12AB")

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

    label("loc_12F0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_11AB end

    def Function_5_12FC(): pass

    label("Function_5_12FC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14CD")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FB")
    OP_A7(0x18, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x18, 0x0, 0)
    OP_98(0x18, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1359():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1359)

    def lambda_1373():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x18, 2, lambda_1373)
    ClearChrFlags(0x18, 0x80)
    SetChrFlags(0x18, 0x8000)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_13DC"),
        (2, "loc_13EB"),
        (1, "loc_13F8"),
        (SWITCH_DEFAULT, "loc_13FB"),
    )


    label("loc_13DC")

    SetScenarioFlags(0x217, 1)
    OP_70(0x4, 0x1E)
    Sleep(500)
    Jump("loc_13FB")

    label("loc_13EB")

    OP_70(0x4, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13F8")

    OP_B9(0x0)
    Return()

    label("loc_13FB")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x7E, 1)"), scpexpr(EXPR_END)), "loc_1458")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_14C8")

    label("loc_1458")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x7E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14C8")

    Jump("loc_1507")

    label("loc_14CD")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_1507")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12FC end

    def Function_6_1513(): pass

    label("Function_6_1513")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1613")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_159C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_160E")

    label("loc_159C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_160E")

    Jump("loc_1658")

    label("loc_1613")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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

    label("loc_1658")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1513 end

    def Function_7_1664(): pass

    label("Function_7_1664")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1794")
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
            "#56I地のセピス×８０\x01\x07\x02",

            "#57I水のセピス×８０\x01\x07\x02",

            "#58I火のセピス×８０\x01\x07\x02",

            "#59I風のセピス×８０\x01\x07\x02",

            "#60I時のセピス×８０\x01\x07\x02",

            "#61I空のセピス×８０\x01\x07\x02",

            "#62I幻のセピス×８０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F1, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_17B9")

    label("loc_1794")


    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_17B9")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1664 end

    def Function_8_17CB(): pass

    label("Function_8_17CB")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A73")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話す\x01",              # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A14")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1972")

    #C0013
    ChrTalk(
        0x15,
        (
            "#10103Fオルキスタワーへの突入……\x01",
            "かなり激しい戦いが予想されます。\x02\x03",

            "#10101F一度作戦を開始したら、\x01",
            "戻ってくるのは難しいでしょうし……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        (
            "#00103Fそうね……\x01",
            "何が起こるか分からないし\x01",
            "万全にしておかないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x15,
        (
            "#10100F今のうちに、市内の施設にも\x01",
            "立ち寄っておいた方が\x01",
            "いいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A0F")

    label("loc_1972")


    #C0016
    ChrTalk(
        0x15,
        (
            "#10103Fオルキスタワーへの突入……\x01",
            "かなり激しい戦いが予想されます。\x02\x03",

            "#10100F今のうちに、市内の武器屋や\x01",
            "オーバルストアにも\x01",
            "立ち寄った方がよさそうですね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A0F")

    Jump("loc_1A6E")

    label("loc_1A14")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6E")

    #C0017
    ChrTalk(
        0x15,
        (
            "#10100Fメンバー編成ですね、\x01",
            "了解しました！\x02",
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
    Jump("loc_1A6E")

    label("loc_1A6E")

    Jump("loc_17D8")

    label("loc_1A73")

    TalkEnd(0xFE)
    Return()

    # Function_8_17CB end

    def Function_9_1A77(): pass

    label("Function_9_1A77")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C75")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話す\x01",              # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C1B")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BE, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B7C")

    #C0018
    ChrTalk(
        0x16,
        (
            "#10403F……そういえば、ここを出ると\x01",
            "すぐに旧市街だったね。\x02\x03",

            "#10402Fフフ、せっかくだから\x01",
            "《トリニティ》に\x01",
            "顔を出しておこうかな？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1C16")

    label("loc_1B7C")


    #C0019
    ChrTalk(
        0x16,
        (
            "#10404F旧市街の方はテスタメンツに\x01",
            "任せておいて大丈夫だろう。\x02\x03",

            "#10400F僕たちは作戦に\x01",
            "集中するとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C16")

    #C0020
    ChrTalk(
        0x101,
        "#00000Fああ……そうだな。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_1C16")

    Jump("loc_1C70")

    label("loc_1C1B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C70")

    #C0021
    ChrTalk(
        0x16,
        "#10400Fフフ、メンバーを代えるのかい？\x02",
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
    Jump("loc_1C70")

    label("loc_1C70")

    Jump("loc_1A84")

    label("loc_1C75")

    TalkEnd(0xFE)
    Return()

    # Function_9_1A77 end

    def Function_10_1C79(): pass

    label("Function_10_1C79")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1C86")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EDD")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話す\x01",              # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E7F")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E32")

    #C0022
    ChrTalk(
        0x101,
        "#00005Fリーシャ、こんな所にいたのか。\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x17,
        (
            "#10702Fええ……\x01",
            "作戦が開始するまで、静かな所で\x01",
            "気を高めておこうと思いまして。\x02\x03",

            "#10703Fあのオルキスタワーには、\x01",
            "《血染めのシャーリィ》が\x01",
            "いるはずですから……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#00301Fああ……叔父貴たちと同様、\x01",
            "立ちはだかってくるだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x17,
        "#10701F……負けません、絶対に。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1E7A")

    label("loc_1E32")


    #C0026
    ChrTalk(
        0x17,
        (
            "#10703F《血染めのシャーリィ》……\x02\x03",

            "#10701F……負けません、絶対に。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E7A")

    Jump("loc_1ED8")

    label("loc_1E7F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED8")

    #C0027
    ChrTalk(
        0x17,
        "#10700Fはい、メンバーを変更するんですね。\x02",
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
    Jump("loc_1ED8")

    label("loc_1ED8")

    Jump("loc_1C86")

    label("loc_1EDD")

    TalkEnd(0xFE)
    Return()

    # Function_10_1C79 end

    def Function_11_1EE1(): pass

    label("Function_11_1EE1")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1EEE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B3")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話す\x01",              # 0
            "パーティ編成\x01",      # 1
            "やめる\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2144")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20B6")

    #C0028
    ChrTalk(
        0x9,
        (
            "#00603Fタワーへの突入作戦には\x01",
            "私も同行させてもらう。\x02\x03",

            "#00600Fお前たちも、今のうちに\x01",
            "しっかりと準備を整えておけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#00000Fええ、了解しました。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、ダドリーさんが\x01",
            "いてくれると心強いわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        (
            "#00603F大統領の逮捕を\x01",
            "支援課だけに任せてはおけん……\x01",
            "ただそれだけのことだ。\x02\x03",

            "#00600F分かったら、さっさと\x01",
            "行ってくるがいい。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_213F")

    label("loc_20B6")


    #C0032
    ChrTalk(
        0x9,
        (
            "#00603F大統領の逮捕……\x01",
            "口で言うほど簡単ではないのは\x01",
            "お前達にも分かっているはずだ。\x02\x03",

            "#00600F今のうちにしっかりと\x01",
            "準備を整えておけ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213F")

    Jump("loc_21AE")

    label("loc_2144")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21AE")

    #C0033
    ChrTalk(
        0x9,
        (
            "#00600Fメンバーを変更するんだな？\x01",
            "……さっさと選ぶがいい。\x02",
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
    Jump("loc_21AE")

    label("loc_21AE")

    Jump("loc_1EEE")

    label("loc_21B3")

    TalkEnd(0xFE)
    Return()

    # Function_11_1EE1 end

    def Function_12_21B7(): pass

    label("Function_12_21B7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23A9")

    #C0034
    ChrTalk(
        0x8,
        (
            "#01002Fクク、それにしても……\x01",
            "どいつもこいつも\x01",
            "元気そうでなによりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x103,
        (
            "#00202F課長こそ……\x01",
            "無事でよかったです。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00000F課長たちはずっと市内で\x01",
            "地下活動をしていたんですよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x8,
        (
            "#01003Fああ、しばらくはここを拠点にして、\x01",
            "打開策を話し合ったりしていたが……\x02\x03",

            "#01001Fこうなってしまった以上、\x01",
            "そんな悠長な真似をしている\x01",
            "暇もないだろう。\x02\x03",

            "お前たちにはなんとしても、\x01",
            "今回の作戦を成功させてもらうぞ。\x01",
            "……キーアを取り戻すためにもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        "#00000Fええ……任せてください！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 4)
    Jump("loc_2523")

    label("loc_23A9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A9")

    #C0039
    ChrTalk(
        0x8,
        (
            "#01003Fこうなってしまった以上、\x01",
            "悠長な真似をしている暇もない。\x02\x03",

            "#01001Fお前たちにはなんとしても、\x01",
            "オルキスタワーの突入作戦を\x01",
            "成功させてもらうぞ。\x02\x03",

            "#01002F市民のために……なにより、\x01",
            "お前たちとキーアの為にもな。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#00000Fはい……！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_2523")

    label("loc_24A9")


    #C0041
    ChrTalk(
        0x8,
        (
            "#01004F俺もショットガンの\x01",
            "メンテナンスをしておこう。\x02\x03",

            "#01001Fオルキスタワーの突入作戦……\x01",
            "なんとしても成功させるぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2523")

    TalkEnd(0xFE)
    Return()

    # Function_12_21B7 end

    def Function_13_2527(): pass

    label("Function_13_2527")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_267B")

    #C0042
    ChrTalk(
        0xA,
        (
            "さ～て、作戦の開始前に\x01",
            "武装の点検をしとかなくちゃな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            "……そういえば君たち、\x01",
            "病院でドノバン警部に\x01",
            "会ったらしいね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xA,
        (
            "どうだい、\x01",
            "元気そうにしてたかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x102,
        (
            "#00100Fええ、奥さんの看病もあって\x01",
            "全快も近いみたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0xA,
        "はは、それはよかったよ。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xA,
        (
            "警部のいない間、僕たちで\x01",
            "何とかやっていかないとね～。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 6)
    Jump("loc_26F3")

    label("loc_267B")


    #C0048
    ChrTalk(
        0xA,
        (
            "さ～て、作戦の開始前に\x01",
            "武装の点検をしとかなくちゃな～。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xA,
        (
            "警部のいない間、僕たちで\x01",
            "何とかやっていかないとね～。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_26F3")

    TalkEnd(0xFE)
    Return()

    # Function_13_2527 end

    def Function_14_26F7(): pass

    label("Function_14_26F7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2835")

    #C0050
    ChrTalk(
        0xD,
        (
            "突入作戦を開始するにしても、\x01",
            "市民の安全は最優先にする\x01",
            "必要がありますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xD,
        (
            "私は戦闘には向きませんし、\x01",
            "作戦範囲内で被害が及ばないように\x01",
            "避難誘導にあたりたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x102,
        "#00100Fそういう役目も重要そうですね……\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x101,
        (
            "#00003F俺たちの方でも気をつけますが……\x01",
            "そちらはよろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 7)
    Jump("loc_28E7")

    label("loc_2835")


    #C0054
    ChrTalk(
        0xD,
        (
            "私は戦闘には向きませんし、\x01",
            "作戦範囲内で被害が及ばないように\x01",
            "避難誘導にあたりたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xD,
        (
            "たとえこんな状況といえども、\x01",
            "市民の安全は最優先にする\x01",
            "必要がありますから。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28E7")

    TalkEnd(0xFE)
    Return()

    # Function_14_26F7 end

    def Function_15_28EB(): pass

    label("Function_15_28EB")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A1C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D0")
    TurnDirection(0xB, 0x10A, 0)

    #C0056
    ChrTalk(
        0x10A,
        (
            "#00603Fエマ君、この場は君に任せる。\x02\x03",

            "#00600F作戦行動に支障が出ないよう、\x01",
            "拠点周辺の警戒にも\x01",
            "十分に気を配ってくれたまえ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "ええ、了解しました。\x01",
            "……ダドリーさんもお気をつけて。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 0)
    Jump("loc_2A17")

    label("loc_29D0")


    #C0058
    ChrTalk(
        0xB,
        (
            "この場は私たちにお任せください。\x01",
            "……ダドリーさんもお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A17")

    Jump("loc_2B75")

    label("loc_2A1C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B20")

    #C0059
    ChrTalk(
        0xB,
        (
            "改めて、作戦の段取りを\x01",
            "確認している所です。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xB,
        (
            "あなたたちも、流れはちゃんと\x01",
            "頭に入っていますね？\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#00000Fええ、もちろんです。\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xB,
        "……よろしい。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xB,
        (
            "作戦の成功は\x01",
            "あなたたちにかかっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0xB,
        "くれぐれも準備を怠らないように。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 1)
    Jump("loc_2B75")

    label("loc_2B20")


    #C0065
    ChrTalk(
        0xB,
        (
            "作戦の成功は\x01",
            "あなたたちにかかっています。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xB,
        "くれぐれも準備を怠らないように。\x02",
    )

    CloseMessageWindow()

    label("loc_2B75")

    TalkEnd(0xFE)
    Return()

    # Function_15_28EB end

    def Function_16_2B79(): pass

    label("Function_16_2B79")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CA7")

    #C0067
    ChrTalk(
        0xE,
        (
            "無効宣言から、本部にも\x01",
            "我々に協力してくれる警官が\x01",
            "少しずつ集まりだしてなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xE,
        (
            "フランツ君が彼らとの連絡役を\x01",
            "買って出てくれているんだー。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#00005Fフランツが……？\x02",
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0xE,
        (
            "うむ、みな警察としての誇りを\x01",
            "守るために、頑張っているわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xE,
        "君たちのほうもよろしく頼んだぞー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 2)
    Jump("loc_2D0C")

    label("loc_2CA7")


    #C0072
    ChrTalk(
        0xE,
        (
            "みな警察としての誇りを\x01",
            "守るために、頑張っているわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xE,
        "君たちのほうもよろしく頼んだぞー。\x02",
    )

    CloseMessageWindow()

    label("loc_2D0C")

    TalkEnd(0xFE)
    Return()

    # Function_16_2B79 end

    def Function_17_2D10(): pass

    label("Function_17_2D10")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E51")

    #C0074
    ChrTalk(
        0xF,
        (
            "『魔導兵』たちの守りを\x01",
            "突破するには、警察のパトカーじゃ\x01",
            "とてもじゃないけど力不足なのよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0xF,
        (
            "馬力とスピードを考えても、\x01",
            "ロイド君たちの車両が\x01",
            "絶対に必要になると思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            "#00004Fええ、何としても回収してきます。\x02\x03",

            "#00000Fケイト先輩たちもお気をつけて。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0xF,
        "うん、ロイド君たちもがんばってね！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 3)
    Jump("loc_2EA4")

    label("loc_2E51")


    #C0078
    ChrTalk(
        0xF,
        (
            "私たちは作戦まで\x01",
            "突入の準備を整えておくわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0xF,
        "ロイド君たちもがんばってね！\x02",
    )

    CloseMessageWindow()

    label("loc_2EA4")

    TalkEnd(0xFE)
    Return()

    # Function_17_2D10 end

    def Function_18_2EA8(): pass

    label("Function_18_2EA8")

    TalkBegin(0xFE)
    Fade(500)
    OP_6B(0xFF)
    OP_68(-12940, -13300, 188130, 0)
    MoveCamera(45, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3049")

    #C0080
    ChrTalk(
        0xC,
        (
            "タワーへのハッキングが成功すれば\x01",
            "通信妨害も解除できる。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0xC,
        (
            "君たちの乗ってきたという\x01",
            "メルカバ、だったかな？\x01",
            "そちらとも通信が可能になるはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x103,
        (
            "#00203Fふむ、そうなると\x01",
            "ヨナのバックアップも\x01",
            "受けられそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xC,
        (
            "ああ、ヨナ君の協力があれば\x01",
            "きっと百人力だよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xC,
        (
            "そのためにも、\x01",
            "なんとしてもハッキングを\x01",
            "成功させなくちゃね！！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 4)
    Jump("loc_30B9")

    label("loc_3049")


    #C0085
    ChrTalk(
        0xC,
        (
            "ハッキングが成功するまで、\x01",
            "もう少し時間がかかりそうなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0xC,
        (
            "ティオ君たちのほうも\x01",
            "気をつけてくれよ～！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30B9")

    Fade(500)
    OP_6B(0x0)
    OP_69(0xFF, 0x0)
    OP_0D()
    TalkEnd(0xFE)
    Return()

    # Function_18_2EA8 end

    def Function_19_30CA(): pass

    label("Function_19_30CA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31BA")

    #C0087
    ChrTalk(
        0x10,
        (
            "僕はＩＢＣの技術部にいたんだけど、\x01",
            "この間の無効宣言を見て、\x01",
            "逃げ出してきちゃったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x10,
        (
            "ダビッドの奴は\x01",
            "マリアベルお嬢さんを信じたいって\x01",
            "タワーに残ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x10,
        (
            "こんな事になってしまって、\x01",
            "大丈夫かな……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 5)
    Jump("loc_3237")

    label("loc_31BA")


    #C0090
    ChrTalk(
        0x10,
        (
            "タワーに残った\x01",
            "ダビッドは大丈夫かな……\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x10,
        (
            "別れ際にケンカもしちゃって\x01",
            "心配だけど……今はとにかく、\x01",
            "主任の手伝いだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3237")

    TalkEnd(0xFE)
    Return()

    # Function_19_30CA end

    def Function_20_323B(): pass

    label("Function_20_323B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32F1")

    #C0092
    ChrTalk(
        0x11,
        (
            "今のところ、魔導兵も\x01",
            "屋内までは入ってきて\x01",
            "いないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x11,
        (
            "この状態が長引けば、\x01",
            "どうなるか分かりません。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x11,
        "早く事態を打開できるといいですね……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 6)
    Jump("loc_3373")

    label("loc_32F1")


    #C0095
    ChrTalk(
        0x11,
        (
            "外出禁止令で、市民はほとんど\x01",
            "屋内にいる状態とはいえ、\x01",
            "危険なのに違いはありません。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x11,
        "早く事態を打開できるといいですね……\x02",
    )

    CloseMessageWindow()

    label("loc_3373")

    TalkEnd(0xFE)
    Return()

    # Function_20_323B end

    def Function_21_3377(): pass

    label("Function_21_3377")

    TalkBegin(0xFE)

    #C0097
    ChrTalk(
        0x12,
        (
            "はあ……\x01",
            "どうにも緊張してきたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x12,
        "突入作戦、成功するといいな……\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_3377 end

    def Function_22_33C9(): pass

    label("Function_22_33C9")

    TalkBegin(0xFE)

    #C0099
    ChrTalk(
        0x13,
        (
            "魔導兵か……\x01",
            "大統領はこんなカードを\x01",
            "用意していたとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x13,
        (
            "厄介だが……\x01",
            "なんとかするしかあるまい。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_33C9 end

    def Function_23_343B(): pass

    label("Function_23_343B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3518")

    #C0101
    ChrTalk(
        0x14,
        (
            "このエリアに保存してある武器は、\x01",
            "あるルートから仕入れたものでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x14,
        (
            "本来なら違法な武器だが、\x01",
            "物資の足りない状況では\x01",
            "背に腹は代えられない。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x14,
        (
            "なにより、あの魔導兵に\x01",
            "通用するといいんだが……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1, 7)
    Jump("loc_358A")

    label("loc_3518")


    #C0104
    ChrTalk(
        0x14,
        (
            "このエリアに保存してある武器は、\x01",
            "あるルートから仕入れたものでな。\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x14,
        (
            "あの魔導兵に\x01",
            "通用するといいんだが……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_358A")

    TalkEnd(0xFE)
    Return()

    # Function_23_343B end

    def Function_24_358E(): pass

    label("Function_24_358E")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_36A4")
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x15, -6000, -8000, 595580, 0)

    label("loc_36A4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_36CA")
    ClearChrFlags(0x16, 0x80)
    SetChrPos(0x16, -9520, -16000, 188860, 0)

    label("loc_36CA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_36F0")
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x17, -5840, 0, 608620, 225)

    label("loc_36F0")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_3747")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 17080, -16000, 178000, 270)
    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 135)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 45)
    Jump("loc_3773")

    label("loc_3747")

    ClearChrFlags(0xB, 0x80)
    SetChrPos(0xB, 15200, -16000, 178850, 180)
    ClearChrFlags(0x13, 0x80)
    SetChrPos(0x13, 15200, -16000, 177140, 0)

    label("loc_3773")

    Return()

    # Function_24_358E end

    def Function_25_3774(): pass

    label("Function_25_3774")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0106
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3861")
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

    label("loc_3861")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_25_3774 end

    def Function_26_3870(): pass

    label("Function_26_3870")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_387A")
    Return()

    label("loc_387A")

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
            "強大な力を秘めた魔物がいる。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【退治する】\x01",      # 0
            "【やめる】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3952"),
        (SWITCH_DEFAULT, "loc_396B"),
    )


    label("loc_3952")

    Sleep(500)
    OP_E2(0x2)
    OP_90(0x0, -499760, 0, 494390, 0)
    EventEnd(0x5)
    Return()

    label("loc_396B")

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
        (2, "loc_3A2D"),
        (1, "loc_3A32"),
        (SWITCH_DEFAULT, "loc_3A35"),
    )


    label("loc_3A2D")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    label("loc_3A32")

    OP_B9(0x0)
    Return()

    label("loc_3A35")

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
            "魔獣を退治した！\x02",
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
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x21E, 6)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B25")
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
            "途方もない力が、どこかで目覚めるのを感じた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x21F, 0)

    label("loc_3B25")

    OP_E2(0x2)
    ModifyEventFlags(0, 0, 0x80)
    EventEnd(0x5)
    Return()

    # Function_26_3870 end

    def Function_27_3B2F(): pass

    label("Function_27_3B2F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3B41")
    Call(0, 36)
    Return()

    label("loc_3B41")

    SetMapFlags(0x8000000)
    EventBegin(0x1)
    SoundLoad(144)
    SoundLoad(150)

    #A0111
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "リフトの制御パネルがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C99")
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

    label("loc_3C99")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_27_3B2F end

    def Function_28_3CA1(): pass

    label("Function_28_3CA1")

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

    # Function_28_3CA1 end

    def Function_29_3DB0(): pass

    label("Function_29_3DB0")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_END)), "loc_3DF9")
    TalkBegin(0xFF)
    SetChrName("")

    #A0112
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは切られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_3F32")

    label("loc_3DF9")

    EventBegin(0x1)

    #A0113
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2B")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3F2B")
    Call(0, 32)

    label("loc_3F2B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_3F32")

    Return()

    # Function_29_3DB0 end

    def Function_30_3F33(): pass

    label("Function_30_3F33")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_END)), "loc_3F7C")
    TalkBegin(0xFF)
    SetChrName("")

    #A0114
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは切られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_40B4")

    label("loc_3F7C")

    EventBegin(0x1)

    #A0115
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40AD")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_40AD")
    Call(0, 32)

    label("loc_40AD")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_40B4")

    Return()

    # Function_30_3F33 end

    def Function_31_40B5(): pass

    label("Function_31_40B5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_END)), "loc_40FE")
    TalkBegin(0xFF)
    SetChrName("")

    #A0116
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは切られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_4236")

    label("loc_40FE")

    EventBegin(0x1)

    #A0117
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_422F")
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x151, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_422F")
    Call(0, 32)

    label("loc_422F")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_4236")

    Return()

    # Function_31_40B5 end

    def Function_32_4237(): pass

    label("Function_32_4237")

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

    # Function_32_4237 end

    def Function_33_42C3(): pass

    label("Function_33_42C3")

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

    def lambda_439B():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_439B)
    Sleep(50)

    def lambda_43B8():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43B8)
    Sleep(50)

    def lambda_43D5():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43D5)
    Sleep(50)

    def lambda_43F2():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43F2)
    Sleep(50)

    def lambda_440F():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_440F)
    Sleep(50)

    def lambda_442C():
        OP_97(0xFE, 0x0, 0x0, 0xBB8, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_442C)
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
            "#12P#00305Fふむ、随分広い場所に出やがったな。\x02\x03",

            "#00303F通商会議の事件で\x01",
            "オルキスタワーから降りた時にも\x01",
            "面食らったもんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        (
            "#00000Fああ、あそことは場所的にも\x01",
            "結構離れているみたいだけど……\x02\x03",

            "#00006F旧市街の地下にまで、\x01",
            "こんな広大なスペースが\x01",
            "作られていたなんてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、オルキスタワーの地下から\x01",
            "旧市街まで到達するまでに、\x01",
            "どれだけのミラがかかったことやら。\x02",
        )
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#00200Fそれに、以前聞いた話では、\x01",
            "Ｄ区画は導力車の駐車場として\x01",
            "建造されたそうですが……\x02\x03",

            "#00206Fやっぱり、車なんて\x01",
            "まったく停められていませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x102,
        (
            "#6P#00103Fそうね……\x02\x03",

            "#00101F導力車の普及している共和国ですら、\x01",
            "ここまでのものは必要ないはずよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0123
    ChrTalk(
        0x109,
        (
            "#12P#10106Fそもそも、駐車場なんてものを\x01",
            "旧市街の地下に用意されていても、\x01",
            "どれだけの人が利用するか疑問ですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x101,
        (
            "#00006F色々思うところはあるけど……\x02\x03",

            "#00000F……とにかく手配魔獣を\x01",
            "退治しに行かなきゃな。\x02\x03",

            "奥の方に進んでみるとしようか。\x02",
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

    # Function_33_42C3 end

    def Function_34_481F(): pass

    label("Function_34_481F")

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
    SetChrName("マクダエル議長")

    #A0125
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#30Wそれを皆さんに共に考えて頂く\x01",
            "きっかけとするためにも……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(500)
    OP_82(0x64, 0x0, 0xBB8, 0x320)
    SetMessageWindowPos(-1, 10, -1, -1)
    SetChrName("マクダエル議長")

    #A0126
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#4S──自治州代表の１人として\x01",
            "私はここに『クロスベル独立国』が\x01",
            "無効である事を宣言いたします！\x07\x00\x02",
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
        "#11Pおお、言っちゃったよ！？\x02",
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0xB,
        (
            "#12Pで、でもこれで少しは\x01",
            "動きやすくなります……！\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        "#11P#00604Fああ……\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x8, 500)

    #C0130
    ChrTalk(
        0x9,
        (
            "#5P#00602F──セルゲイさん。\x01",
            "連中#4Rあいつら#の協力でしょうか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x9, 500)

    #C0131
    ChrTalk(
        0x8,
        (
            "#11P#01004Fクク……\x01",
            "それ以外にはあり得ねぇだろ。\x02\x03",

            "#01002Fさぁて──忙しくなりそうだな。\x02",
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

    # Function_34_481F end

    def Function_35_4D62(): pass

    label("Function_35_4D62")

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
            "#1K同日、９：３０──\x02",
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
            "#5Pああ……ティオ君が\x01",
            "無事でいてくれたなんて！\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0xC,
        (
            "#5Pしかもヨナ君も無事、\x01",
            "解放されたんだって！？\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0xC,
        (
            "#5Pも、もうこれで\x01",
            "思い残すことはないよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x103,
        (
            "#12P#00206F主任……感激しすぎです。\x02\x03",

            "#00202Fでも、ご無事で何よりでした。\x02",
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
            "#5Pああっ！\x01",
            "ティオ君が僕の無事を\x01",
            "喜んでくれるなんて……！\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xC,
        (
            "#5P１日１００回以上、\x01",
            "女神#4Rエイドス#にお祈りを奉げた甲斐が\x01",
            "あったよ～！\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x103,
        "#12P#00211Fさすがにウザすぎです。\x02",
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
            "#5P#00012Fそ、それにしても……\x01",
            "よくこんなに集まりましたね。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-8300, -15000, 188100, 1000)
    MoveCamera(39, 22, 0, 1000)
    SetCameraDistance(15600, 1000)

    def lambda_53E8():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_53E8)
    Sleep(50)

    def lambda_53F8():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_53F8)
    Sleep(50)

    def lambda_5408():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5408)
    Sleep(50)

    def lambda_5418():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5418)
    Sleep(50)

    def lambda_5428():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5428)
    Sleep(50)

    def lambda_5438():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5438)
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
            "#6P#00305Fやっぱり大統領への反感が\x01",
            "高まってるってことか？\x02",
        )
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x8,
        (
            "#11P#01003Fま、当然だろう。\x02\x03",

            "#01001F昨日だって、いきなり全市内に\x01",
            "戒厳令と外出禁止令が出されてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0x10A,
        (
            "#11P#00603Fその後、青白いモヤが立ち込めたと\x01",
            "思ったらあの有様だ。\x02\x03",

            "#00610F……もはや断じて\x01",
            "見過ごせる状況ではない。\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0xB,
        "さすがに逮捕令状は取れませんが……\x02",
    )

    CloseMessageWindow()

    #C0145
    ChrTalk(
        0xB,
        (
            "現行犯逮捕という形で大統領一派を\x01",
            "押さえるしかないでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x102,
        "#6P#00106F…………はい。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x101,
        (
            "#00008Fそうですね……\x01",
            "それしか方法は無さそうです。\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x109,
        (
            "#6P#10113Fあの……\x01",
            "市民の安全はどうですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0xD,
        (
            "#11P今の所、戒厳令と外出禁止令に\x01",
            "大人しく従っているようです。\x02\x03",

            "#11P街の外で戦闘が起きているのも\x01",
            "影響しているのではないかと。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0xA,
        (
            "#11Pでも、いきなりだったから\x01",
            "備えのない市民も多いみたいでね。\x02\x03",

            "#11P市民会館やホテルなんかに\x01",
            "避難している人もいるみたいだし\x01",
            "かなり困ってるんじゃないかな～？\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x104,
        "#6P#00306Fなるほどな……\x02",
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x103,
        "#00208F一刻の猶予もありませんね……\x02",
    )

    CloseMessageWindow()

    #C0153
    ChrTalk(
        0x105,
        (
            "#6P#10403Fしかし、大統領一派を\x01",
            "押さえるとなると……\x02\x03",

            "#10401Fオルキスタワーを攻略する必要が\x01",
            "あるってわけだね？\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x8,
        (
            "#11P#01003Fああ、既に大まかな段取りは\x01",
            "出来ている。\x02\x03",

            "市内に残った遊撃士たちと\x01",
            "連携も出来そうだしな。\x02\x03",

            "#01002Fあとはお前らが来るのを\x01",
            "今か今かと待ってたってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0155
    ChrTalk(
        0x102,
        "#6P#00102F課長……\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x103,
        (
            "#00204F……待っててくれて\x01",
            "感謝です。\x02",
        )
    )

    CloseMessageWindow()

    #C0157
    ChrTalk(
        0x106,
        (
            "#6P#10701Fそれで、具体的な段取りは\x01",
            "どのような……？\x02",
        )
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x10A,
        (
            "#11P#00603F現在、タワー前には\x01",
            "先ほどの“魔導兵”の大群が\x01",
            "守りを固めているようだ。\x02\x03",

            "#00601Fそれを、ここにいる全員と\x01",
            "遊撃士たちで強襲する。\x02",
        )
    )

    CloseMessageWindow()

    #C0159
    ChrTalk(
        0xF,
        (
            "その隙に、突入チームが\x01",
            "車輌でオルキスタワーに突入……\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0xF,
        (
            "そのままタワーの制圧を\x01",
            "開始するっていう段取りね。\x02",
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
        "#6P#10112Fえっと……何ていうか。\x02",
    )

    CloseMessageWindow()

    #C0162
    ChrTalk(
        0x104,
        (
            "#6P#00306Fかなり強引な段取りだが\x01",
            "勝算はあるのかよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x8,
        (
            "#11P#01003Fどうやら国防軍の殆んどは\x01",
            "市外に回されているらしい。\x02\x03",

            "#01000Fおそらくタワー内にいるのは\x01",
            "アリオスを始め少数のはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0xE,
        (
            "#5Pジオフロントからのルートは\x01",
            "相変わらず封鎖されとるからなー。\x02",
        )
    )

    CloseMessageWindow()

    #C0165
    ChrTalk(
        0xE,
        (
            "#5Pこのあたりが現状で取れる\x01",
            "最善の策といったところだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0166
    ChrTalk(
        0x101,
        "#00006F……なるほど。\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        "#6P#00108Fそうなると……\x02",
    )

    CloseMessageWindow()

    def lambda_5CB8():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5CB8)

    def lambda_5CC5():
        TurnDirection(0x101, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_5CC5)
    Sleep(30)

    def lambda_5CD5():
        TurnDirection(0x102, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5CD5)
    Sleep(30)

    def lambda_5CE5():
        TurnDirection(0x103, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5CE5)
    Sleep(30)

    def lambda_5CF5():
        TurnDirection(0x106, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5CF5)
    Sleep(30)

    def lambda_5D05():
        TurnDirection(0x109, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5D05)
    Sleep(30)

    def lambda_5D15():
        TurnDirection(0x105, 0x104, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5D15)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Sleep(1100)

    def lambda_5D3D():
        TurnDirection(0xFE, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5D3D)

    def lambda_5D4A():
        TurnDirection(0x104, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_5D4A)
    Sleep(30)

    def lambda_5D5A():
        TurnDirection(0x102, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_5D5A)
    Sleep(30)

    def lambda_5D6A():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_5D6A)
    Sleep(30)

    def lambda_5D7A():
        TurnDirection(0x106, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_5D7A)
    Sleep(30)

    def lambda_5D8A():
        TurnDirection(0x109, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_5D8A)
    Sleep(30)

    def lambda_5D9A():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_5D9A)
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
            "#00001Fその突入チームというのは\x01",
            "もう決まってるんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x10A,
        (
            "#11P#00605Fいや、これからだが……\x02\x03",

            "#00601F──お前たち、まさか。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        (
            "#00004Fええ、できれば突入チームは\x01",
            "俺たちに任せてください。\x02\x03",

            "#00013Fタワーにいるキーアを\x01",
            "この手で取り戻すためにも。\x02",
        )
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x104,
        (
            "#6P#00304Fああ、そいつばかりは\x01",
            "他の連中には譲れねぇな。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x103,
        (
            "#00202Fタワー内のセキュリティなら\x01",
            "わたしがいれば役立ちます。\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#6P#00103F私も……ベルやおじさまを\x01",
            "直接問い詰めたいと思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x109,
        (
            "#6P#10106F一度、国防軍として彼らに\x01",
            "加担した身ですけれど……\x02\x03",

            "#10101Fだからこそ放っておけません。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x105,
        (
            "#6P#10404Fまあ、このメンツだったら\x01",
            "修羅場も潜り抜けてるしね。\x02\x03",

            "#10402Fチームワークのことを考えると\x01",
            "打ってつけなんじゃないかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0176
    ChrTalk(
        0x106,
        "#6P#10704Fきっとお役に立ってみせます。\x02",
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x10A,
        "#11P#00600Fお前たち……\x02",
    )

    CloseMessageWindow()

    #C0178
    ChrTalk(
        0x8,
        (
            "#11P#01004F……クク、やれやれ。\x02\x03",

            "#01002Fあのヒヨッ子どもが、すっかり\x01",
            "一丁前の顔になったもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x101,
        "#00005F課長……\x02",
    )

    CloseMessageWindow()

    #C0180
    ChrTalk(
        0x8,
        (
            "#11P#01003Fま、いいだろ。\x01",
            "突入チームはお前らに任せる。\x02\x03",

            "#01001Fだが、全ての段取りが\x01",
            "整ってるわけじゃなくてな。\x02\x03",

            "もう少し待ってもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x102,
        "#6P#00105Fと言うと……？\x02",
    )

    CloseMessageWindow()

    #C0182
    ChrTalk(
        0xC,
        (
            "#5Pオルキスタワーへのハッキングを\x01",
            "進めている最中なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0xC,
        (
            "#5Pあと１時間ちょいで\x01",
            "アクセスが可能になるはずさ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_624F():
        TurnDirection(0xFE, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_624F)

    def lambda_625C():
        TurnDirection(0x101, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_625C)
    Sleep(50)

    def lambda_626C():
        TurnDirection(0x102, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_626C)
    Sleep(50)

    def lambda_627C():
        TurnDirection(0x104, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_627C)
    Sleep(50)

    def lambda_628C():
        TurnDirection(0x106, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_628C)
    Sleep(50)

    def lambda_629C():
        TurnDirection(0x109, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_629C)
    Sleep(50)

    def lambda_62AC():
        TurnDirection(0x105, 0xC, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_62AC)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x106, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0184
    ChrTalk(
        0x103,
        "#6P#00205Fあ……\x02",
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x101,
        "#12P#00002F本当ですか……！？\x02",
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x8,
        (
            "#11P#01004Fああ、そうなれば突入チームへの\x01",
            "バックアップもしやすくなるし、\x01",
            "通信妨害も解除できるだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0187
    ChrTalk(
        0x10A,
        (
            "#11P#00603Fそれと、ギルドや各方面にも\x01",
            "改めて連絡を入れる必要がある。\x02\x03",

            "#00600Fとにかく、お前たちが\x01",
            "突入チームに回るという前提で\x01",
            "最終的な段取りを詰めるぞ。\x02",
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
            "その後、ロイドたちは\x01",
            "突入作戦の最終的な段取りを\x01",
            "セルゲイたちと話し合った後……\x02\x03",

            "突入に使う導力車を確保するため\x01",
            "一度、支援課ビルに戻ることにした。\x07\x00\x02",
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
            "#12P#00005F──それじゃあ、\x01",
            "ダドリーさんも突入チームに？\x02",
        )
    )

    CloseMessageWindow()

    #C0190
    ChrTalk(
        0x10A,
        (
            "#5P#00603Fああ、通商会議の警備で\x01",
            "オルキスタワーの構造にも\x01",
            "通じているからな。\x02\x03",

            "#00600F市街地を行くなら\x01",
            "ある程度案内もできるだろう。\x02\x03",

            "#00607Fそれに大統領の逮捕ともなれば\x01",
            "支援課だけに任せてはおけん！\x02",
        )
    )

    CloseMessageWindow()

    #C0191
    ChrTalk(
        0x104,
        "#00306Fやれやれ、またかよ。\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x103,
        "#12P#00204Fもはやお約束ですね。\x02",
    )

    CloseMessageWindow()

    #C0193
    ChrTalk(
        0x102,
        "#00109Fふふ、でも助かります。\x02",
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x109,
        (
            "#10112Fえっと、突入に使用する\x01",
            "導力車ですけど……\x02\x03",

            "#10100F本当に支援課の車輌を？\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x8,
        (
            "#01004F#5Pああ、現時点で一番、\x01",
            "馬力とスピードの双方を\x01",
            "併せ持っている車種だ。\x02\x03",

            "#01002F市街地を強行突破するには\x01",
            "まさに打ってつけだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x109,
        "#10102F確かに……\x02",
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x105,
        (
            "#12P#10404Fまあ支援課に残っているなら\x01",
            "利用しない手はないよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0198
    ChrTalk(
        0x106,
        (
            "#10708Fですが……\x01",
            "この数で市街地を動くと\x01",
            "さすがに目立ちそうですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x10A,
        (
            "#5P#00603Fならば同行するメンバーを\x01",
            "絞り込むがいい。\x02\x03",

            "#00600Fそれ以外の者はここで\x01",
            "待機していればいいだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0200
    ChrTalk(
        0x101,
        "#12P#00000F了解しました。\x02",
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
            "ダドリーがパーティに加入しました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(500)
    Sound(517, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_69B9")
    AddCraft(0x9, 0x1AA)
    AddCraft(0x0, 0x1AA)
    Jump("loc_69C1")

    label("loc_69B9")

    AddCraft(0x9, 0x196)
    AddCraft(0x0, 0x196)

    label("loc_69C1")

    SetMessageWindowPos(-1, -1, -1, -1)

    #A0202
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドとダドリーがコンビクラフト\x01\x07\x02",

            "『ハーツオブアイアン』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()

    #A0203
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ＣＰを１００ずつ消費することで\x01",
            "強力なコンビネーション攻撃が繰り出せます。\x07\x00\x02",
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

    # Function_35_4D62 end

    def Function_36_6B56(): pass

    label("Function_36_6B56")

    TalkBegin(0xFF)
    SetChrName("")

    #A0204
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力が落ちているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1BF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6CA2")

    #C0205
    ChrTalk(
        0x101,
        "#00003F……動かないみたいだな。\x02",
    )

    CloseMessageWindow()

    #C0206
    ChrTalk(
        0x102,
        (
            "#00105Fこの先はオルキスタワーの基部に\x01",
            "繋がっているはずだし……\x02\x03",

            "#00103F多分、大統領たちが\x01",
            "止めているんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x103,
        "#00206Fなるほど、考えられそうです。\x02",
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x104,
        (
            "#00306Fジオフロントから\x01",
            "タワーに侵入するのは\x01",
            "諦めた方がよさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x1BF, 5)

    label("loc_6CA2")

    TalkEnd(0xFF)
    Return()

    # Function_36_6B56 end

    SaveToFile()

Try(main)
