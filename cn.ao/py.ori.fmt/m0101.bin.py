from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m0101.bin",                # FileName
        "m0101",                    # MapName
        "m0101",                    # Location
        0x0068,                     # MapIndex
        "ed7300",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 104, 0, 2, 0, 3],
    )

    BuildStringList((
        "m0101",                  # 0
        "少年",                   # 1
        "缇欧",                   # 2
        "银",                     # 3
        "符术",                   # 4
        "噬光血鱼",               # 5
        "故障机体Ｂ",             # 6
        "SE控制",                 # 7
        "bm0101",                 # 8
        "bm0101",                 # 9
        "bm0101",                 # 10
        "bm0101",                 # 11
        "bm0100",                 # 12
        "bm0100",                 # 13
        "bm0100",                 # 14
        "bm0100",                 # 15
        "bm0100",                 # 16
        "bm0100",                 # 17
    ))

    ATBonus("ATBonus_434", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_792F", 11,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_791F", 0,   10,  5,   0,   6,   2,   4)
    Sepith("Sepith_7937", 0,   0,   0,   8,   6,   6,   6)
    Sepith("Sepith_7927", 6,   0,   11,  0,   0,   4,   6)

    MonsterBattlePostion("MonsterBattlePostion_4D4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 6, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 7, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F0", 6, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_514", 8, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_518", 8, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_51C", 5, 6, 45)
    MonsterBattlePostion("MonsterBattlePostion_520", 11, 10, 225)
    MonsterBattlePostion("MonsterBattlePostion_524", 11, 6, 315)
    MonsterBattlePostion("MonsterBattlePostion_528", 5, 10, 135)
    MonsterBattlePostion("MonsterBattlePostion_52C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 7, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 9, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 7, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 9, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_500", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_504", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_508", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_50C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_6C4", 0x0000, 62, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_792F", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_534", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_791F", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_AAC", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_7937", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_7937", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_5FC", 0x0000, 62, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_7927", 30, 45, 20, 5,
        (
            ("ms68700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms68700.dat", "ms68700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms68700.dat", "ms68700.dat", "ms63800.dat", "ms68700.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_B74", 0x0000, 62, 6, 60, 0, 1, 0, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "ms68700.dat", "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7451", "ed7453", "ATBonus_434"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BB8", 0x0000, 62, 6, 60, 0, 1, 0, 0, "bm0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7451", "ed7453", "ATBonus_434"),
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
        "monster/ch63850.itc",               # 10
        "monster/ch63851.itc",               # 11
        "monster/ch68750.itc",               # 12
        "monster/ch68750.itc",               # 13
        "monster/ch75850.itc",               # 14
        "monster/ch75851.itc",               # 15
        "monster/ch60550.itc",               # 16
        "monster/ch60550.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    452,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(109959,  -5500,   19,      0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(92000,   -8500,   90500,   0,    484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(99960,   100050,  -10000,  0x1010000,    "BattleInfo_6C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(100360,  200740,  0,       0x1010000,    "BattleInfo_534", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-290,    199690,  0,       0x1010000,    "BattleInfo_AAC", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(109910,  99810,   -7000,   0x1010000,    "BattleInfo_78C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(200810,  94840,   0,       0x1010000,    "BattleInfo_6C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(199760,  195940,  -10000,  0x1010000,    "BattleInfo_5FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(202350,  204410,  -10000,  0x1010000,    "BattleInfo_534", 0,   16,  0xFFFF, 0,  1)

    DeclActor(500000,  150,     208500,  1200,    500000,  1150,    208500,  0x007C, 0,  8,  0x0000)
    DeclActor(109960,  -6000,   20,      1200,    109960,  -5000,   20,      0x007C, 0,  4,  0x0000)
    DeclActor(109970,  -3000,   113430,  1200,    109970,  -2000,   113430,  0x007C, 0,  5,  0x0000)
    DeclActor(190010,  -4000,   200010,  1200,    190010,  -3000,   200010,  0x007C, 0,  6,  0x0000)
    DeclActor(92000,   -9000,   90500,   1200,    92000,   -8000,   90500,   0x007C, 0,  7,  0x0000)
    DeclActor(2000,    0,       0,       1200,    2500,    1000,    0,       0x007C, 0,  14, 0x0000)
    DeclActor(108000,  -6000,   2500,    2000,    108000,  -5000,   2500,    0x007C, 0,  10, 0x0000)
    DeclActor(85500,   -6000,   103000,  2000,    85500,   -5000,   103000,  0x007C, 0,  11, 0x0000)
    DeclActor(203430,  -6000,   184020,  2000,    203430,  -5000,   184020,  0x007C, 0,  12, 0x0000)
    DeclActor(320000,  -1000,   302800,  1200,    320000,  500,     302800,  0x007C, 0,  9,  0x0000)
    DeclActor(503490,  0,       199590,  1200,    503490,  1500,    199590,  0x007C, 0,  48, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_D20",          # 00, 0
        "Function_1_D3F",          # 01, 1
        "Function_2_D5E",          # 02, 2
        "Function_3_DEF",          # 03, 3
        "Function_4_148E",         # 04, 4
        "Function_5_168C",         # 05, 5
        "Function_6_17E5",         # 06, 6
        "Function_7_1920",         # 07, 7
        "Function_8_1B1E",         # 08, 8
        "Function_9_1B9E",         # 09, 9
        "Function_10_1C82",        # 0A, 10
        "Function_11_1C9E",        # 0B, 11
        "Function_12_1CBA",        # 0C, 12
        "Function_13_1CD6",        # 0D, 13
        "Function_14_21BE",        # 0E, 14
        "Function_15_2343",        # 0F, 15
        "Function_16_248A",        # 10, 16
        "Function_17_2755",        # 11, 17
        "Function_18_2774",        # 12, 18
        "Function_19_299F",        # 13, 19
        "Function_20_2CF4",        # 14, 20
        "Function_21_31C5",        # 15, 21
        "Function_22_7085",        # 16, 22
        "Function_23_70D6",        # 17, 23
        "Function_24_713F",        # 18, 24
        "Function_25_71A1",        # 19, 25
        "Function_26_7203",        # 1A, 26
        "Function_27_7258",        # 1B, 27
        "Function_28_72AD",        # 1C, 28
        "Function_29_7302",        # 1D, 29
        "Function_30_7375",        # 1E, 30
        "Function_31_73AF",        # 1F, 31
        "Function_32_73E9",        # 20, 32
        "Function_33_7441",        # 21, 33
        "Function_34_7499",        # 22, 34
        "Function_35_74D3",        # 23, 35
        "Function_36_74F2",        # 24, 36
        "Function_37_7532",        # 25, 37
        "Function_38_7572",        # 26, 38
        "Function_39_75EE",        # 27, 39
        "Function_40_7635",        # 28, 40
        "Function_41_76B8",        # 29, 41
        "Function_42_76DA",        # 2A, 42
        "Function_43_771E",        # 2B, 43
        "Function_44_7762",        # 2C, 44
        "Function_45_7785",        # 2D, 45
        "Function_46_77A8",        # 2E, 46
        "Function_47_785E",        # 2F, 47
        "Function_48_78BF",        # 30, 48
    ))


    def Function_0_D20(): pass

    label("Function_0_D20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D3E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_D20")

    label("loc_D3E")

    Return()

    # Function_0_D20 end

    def Function_1_D3F(): pass

    label("Function_1_D3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D5D")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_D3F")

    label("loc_D5D")

    Return()

    # Function_1_D3F end

    def Function_2_D5E(): pass

    label("Function_2_D5E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D86")
    Jc((scpexpr(EXPR_23, 0x0), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D86")
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)

    label("loc_D86")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_D9D")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 16)
    Jump("loc_DD4")

    label("loc_D9D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_DB1")
    ClearScenarioFlags(0x22, 1)
    Event(0, 19)
    Jump("loc_DD4")

    label("loc_DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_DC5")
    ClearScenarioFlags(0x22, 2)
    Event(0, 18)
    Jump("loc_DD4")

    label("loc_DC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 3)), scpexpr(EXPR_END)), "loc_DD4")
    ClearScenarioFlags(0x22, 3)
    Event(0, 46)

    label("loc_DD4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DEE")
    Event(0, 20)

    label("loc_DEE")

    Return()

    # Function_2_D5E end

    def Function_3_DEF(): pass

    label("Function_3_DEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_E04")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_E04")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E68")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E4B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x241), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x32, 0xC8)
    SetMapFlags(0x2)
    Jump("loc_E68")

    label("loc_E4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E68")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x241), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    VolumeBGM(0x64, 0xC8)

    label("loc_E68")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E84")
    ClearMapObjFlags(0x13, 0x10)
    OP_66(0x0, 0x1)

    label("loc_E84")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x85), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x86), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x8B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_EB9")
    SetMapFlags(0x2000)
    OP_E2(0x0)
    Jump("loc_EBE")

    label("loc_EB9")

    ClearMapFlags(0x2000)

    label("loc_EBE")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 106000, -6000, 0, 6000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 98000, -6000, 0, 6000, 2000, 90000)
    SetBarrier(0x0, 0x2, 0x1, 0x0, 100000, -7380, 89000, 4000, 2000, 0)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 100000, -7800, 110000, 4000, 2000, 0)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 96000, -7000, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 104000, -7000, 100000, 4000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 92000, -8000, 96000, 4000, 2000, 0)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 0, -7000, 100000, 4000, 2000, 0)
    SetBarrier(0x0, 0x8, 0x1, 0x0, 0, -7000, 92000, 4000, 2000, 0)
    SetBarrier(0x0, 0x9, 0x1, 0x0, 200000, -8000, 190000, 8000, 2000, 0)
    SetBarrier(0x0, 0xA, 0x1, 0x0, 200000, -8000, 210000, 8000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 0)), scpexpr(EXPR_END)), "loc_107A")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetMapObjFrame(0xE, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on_kp")
    SetMapObjFrame(0xFF, "Null", 0x2, "high")
    Jump("loc_10EB")

    label("loc_107A")

    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off_kp")
    SetMapObjFrame(0xFF, "Null", 0x2, "low")

    label("loc_10EB")

    SetMapObjFrame(0x11, "m00ele00", 0x2, "down_kp")
    SetMapObjFrame(0x0, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x0, "light01", 0x0, 0x1)
    SetMapObjFrame(0x1, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1, "light01", 0x0, 0x1)
    SetMapObjFrame(0x2, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x2, "light01", 0x0, 0x1)
    SetMapObjFrame(0x3, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x3, "light01", 0x0, 0x1)
    SetMapObjFrame(0x4, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x4, "light01", 0x0, 0x1)
    SetMapObjFrame(0x5, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x5, "light01", 0x0, 0x1)
    SetMapObjFrame(0x6, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x6, "light01", 0x0, 0x1)
    SetMapObjFrame(0x7, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x7, "light01", 0x0, 0x1)
    SetMapObjFrame(0x8, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x8, "light01", 0x0, 0x1)
    SetMapObjFrame(0x9, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x9, "light01", 0x0, 0x1)
    SetMapObjFrame(0xA, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xA, "light01", 0x0, 0x1)
    SetMapObjFrame(0xB, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xB, "light01", 0x0, 0x1)
    SetMapObjFrame(0xC, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xC, "light01", 0x0, 0x1)
    SetMapObjFrame(0xD, "sign01", 0x0, 0x1)
    SetMapObjFrame(0xD, "light01", 0x0, 0x1)
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1408")
    OP_70(0x14, 0x0)
    Jump("loc_140C")

    label("loc_1408")

    OP_70(0x14, 0x1E)

    label("loc_140C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141F")
    OP_70(0x15, 0x0)
    Jump("loc_1423")

    label("loc_141F")

    OP_70(0x15, 0x1E)

    label("loc_1423")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1436")
    OP_70(0x16, 0x0)
    Jump("loc_143A")

    label("loc_1436")

    OP_70(0x16, 0x1E)

    label("loc_143A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_144D")
    OP_70(0x17, 0x0)
    Jump("loc_1451")

    label("loc_144D")

    OP_70(0x17, 0x1E)

    label("loc_1451")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_1473")
    ClearMapObjFlags(0x1F, 0x4)
    SetMapObjFrame(0xFF, "koge00", 0x1, 0x1)
    Jump("loc_1487")

    label("loc_1473")

    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFrame(0xFF, "koge00", 0x0, 0x1)

    label("loc_1487")

    ClearMapObjFlags(0x18, 0x10)
    Return()

    # Function_3_DEF end

    def Function_4_148E(): pass

    label("Function_4_148E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_164E")
    Sound(14, 0, 100, 0)
    OP_74(0x14, 0x1E)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158B")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_14EB():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_14EB)

    def lambda_1505():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1505)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_B74", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_156C"),
        (2, "loc_157B"),
        (1, "loc_1588"),
        (SWITCH_DEFAULT, "loc_158B"),
    )


    label("loc_156C")

    SetScenarioFlags(0x216, 7)
    OP_70(0x14, 0x1E)
    Sleep(500)
    Jump("loc_158B")

    label("loc_157B")

    OP_70(0x14, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1588")

    OP_B9(0x0)
    Return()

    label("loc_158B")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x50, 1)"), scpexpr(EXPR_END)), "loc_15E2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1649")

    label("loc_15E2")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x14, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1649")

    Jump("loc_1680")

    label("loc_164E")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_1680")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_148E end

    def Function_5_168C(): pass

    label("Function_5_168C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17B6")
    Sound(14, 0, 100, 0)
    OP_74(0x15, 0x1E)
    OP_71(0x15, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x15, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 60)
    AddSepith(0x1, 60)
    AddSepith(0x2, 60)
    AddSepith(0x3, 60)
    AddSepith(0x4, 60)
    AddSepith(0x5, 60)
    AddSepith(0x6, 60)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×６０\x01\x07\x02",

            "#57I水之耀晶片×６０\x01\x07\x02",

            "#58I火之耀晶片×６０\x01\x07\x02",

            "#59I风之耀晶片×６０\x01\x07\x02",

            "#60I时之耀晶片×６０\x01\x07\x02",

            "#61I空之耀晶片×６０\x01\x07\x02",

            "#62I幻之耀晶片×６０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1EF, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_17D3")

    label("loc_17B6")


    #A0006
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

    label("loc_17D3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_168C end

    def Function_6_17E5(): pass

    label("Function_6_17E5")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18D7")
    Sound(14, 0, 100, 0)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_1868")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_18D2")

    label("loc_1868")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18D2")

    Jump("loc_1914")

    label("loc_18D7")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_1914")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_17E5 end

    def Function_7_1920(): pass

    label("Function_7_1920")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE0")
    Sound(14, 0, 100, 0)
    OP_74(0x17, 0x1E)
    OP_71(0x17, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1D")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_197D():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_197D)

    def lambda_1997():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1997)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xD, 1)
    Battle("BattleInfo_BB8", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_19FE"),
        (2, "loc_1A0D"),
        (1, "loc_1A1A"),
        (SWITCH_DEFAULT, "loc_1A1D"),
    )


    label("loc_19FE")

    SetScenarioFlags(0x217, 0)
    OP_70(0x17, 0x1E)
    Sleep(500)
    Jump("loc_1A1D")

    label("loc_1A0D")

    OP_70(0x17, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A1A")

    OP_B9(0x0)
    Return()

    label("loc_1A1D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xAF, 1)"), scpexpr(EXPR_END)), "loc_1A74")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1ADB")

    label("loc_1A74")

    FadeToDark(300, 0, 100)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x17, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1ADB")

    Jump("loc_1B12")

    label("loc_1AE0")

    FadeToDark(300, 0, 100)

    #A0013
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

    label("loc_1B12")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1920 end

    def Function_8_1B1E(): pass

    label("Function_8_1B1E")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "进入\x01",          # 0
            "离开此处\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1B68"),
        (1, "loc_1B85"),
        (SWITCH_DEFAULT, "loc_1B8A"),
    )


    label("loc_1B68")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x13, 0x10)
    OP_65(0x0, 0x1)
    Call(0, 21)
    Jump("loc_1B8A")

    label("loc_1B85")

    Jump("loc_1B8A")

    label("loc_1B8A")

    SetChrPos(0x0, 500000, 0, 205800, 180)
    EventEnd(0x5)
    Return()

    # Function_8_1B1E end

    def Function_9_1B9E(): pass

    label("Function_9_1B9E")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0014
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C73")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x12, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x12, 0x0)
    OP_71(0x12, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x12)
    OP_71(0x12, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x12, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_1C73")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_9_1B9E end

    def Function_10_1C82(): pass

    label("Function_10_1C82")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1C82 end

    def Function_11_1C9E(): pass

    label("Function_11_1C9E")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1C9E end

    def Function_12_1CBA(): pass

    label("Function_12_1CBA")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1CBA end

    def Function_13_1CD6(): pass

    label("Function_13_1CD6")


    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以调节水位的控制装置。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21BD")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DB4")
    SetChrPos(0x0, 107620, -6000, 200, 0)
    SetChrPos(0x1, 108620, -6000, -600, 0)
    SetChrPos(0x2, 106620, -6000, -600, 0)
    SetChrPos(0x3, 107620, -6000, -1900, 0)
    OP_68(107660, -5000, 850, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    Jump("loc_1EBB")

    label("loc_1DB4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3A")
    SetChrPos(0x0, 85000, -6000, 101000, 0)
    SetChrPos(0x1, 83800, -6000, 101000, 0)
    SetChrPos(0x2, 83800, -6000, 99800, 0)
    SetChrPos(0x3, 85000, -6000, 99800, 0)
    OP_68(84580, -5000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    Jump("loc_1EBB")

    label("loc_1E3A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EBB")
    SetChrPos(0x0, 201500, -6000, 184000, 90)
    SetChrPos(0x1, 200000, -6000, 185000, 90)
    SetChrPos(0x2, 200000, -6000, 183000, 90)
    SetChrPos(0x3, 198500, -6000, 184000, 90)
    OP_68(201500, -5000, 184020, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33500, 0)

    label("loc_1EBB")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 0)), scpexpr(EXPR_END)), "loc_2046")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F5F")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_1FDE")

    label("loc_1F5F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA1")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_1FDE")

    label("loc_1FA1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FDE")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_1FDE")

    OP_0D()
    Sound(157, 2, 100, 0)
    SetMapObjFrame(0xFF, "null", 0x2, "down")
    Sleep(4000)
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)
    SetBarrier(0x3, 0x8, 0x1)
    SetBarrier(0x2, 0x9, 0x1)
    SetBarrier(0x2, 0xA, 0x1)
    ClearScenarioFlags(0x150, 0)
    Jump("loc_21BD")

    label("loc_2046")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "on")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20DD")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_215C")

    label("loc_20DD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_211F")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_215C")

    label("loc_211F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_215C")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_215C")

    OP_0D()
    Sound(157, 2, 100, 0)
    SetMapObjFrame(0xFF, "null", 0x2, "up")
    Sleep(4000)
    OP_24(0x9D)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetBarrier(0x2, 0x8, 0x1)
    SetBarrier(0x3, 0x9, 0x1)
    SetBarrier(0x3, 0xA, 0x1)
    SetScenarioFlags(0x150, 0)

    label("loc_21BD")

    Return()

    # Function_13_1CD6 end

    def Function_14_21BE(): pass

    label("Function_14_21BE")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(144)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有可以操作导力梯的控制面板。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_233B")
    Fade(500)
    SetChrPos(0x0, 600, 0, 600, 90)
    SetChrPos(0x1, 600, 0, -600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_229B")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_22BA")

    label("loc_229B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_22BA")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_22BA")

    OP_68(600, 1000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(144, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_68(600, 6000, 0, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up")
    Sleep(2000)
    OP_D2(0x0, (scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    NewScene("m0100", 0, 0, 0)
    IdleLoop()

    label("loc_233B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_21BE end

    def Function_15_2343(): pass

    label("Function_15_2343")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    OP_6F(0x1)
    OP_69(0x2, 0x0)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "up_kp")
    Sleep(1)
    OP_68(600, 11000, 0, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    OP_90(0x0, 600, 30000, 600, 90)
    OP_90(0x1, 600, 30000, -600, 90)
    OP_90(0x2, -600, 30000, -600, 90)
    OP_90(0x3, -600, 30000, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2416")
    OP_90(0x4, -1800, 0, -600, 90)
    OP_90(0x5, -1800, 0, 600, 90)
    Jump("loc_2435")

    label("loc_2416")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2435")
    OP_90(0x4, -1800, 0, 0, 90)

    label("loc_2435")

    Sound(145, 0, 100, 0)
    OP_68(600, 1000, 0, 3000)
    SetMapObjFrame(0x11, "m00ele00", 0x2, "down")
    FadeToBright(500, 0)
    Sleep(3300)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(500)
    OP_79(0x11)
    OP_6F(0x1)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_15_2343 end

    def Function_16_248A(): pass

    label("Function_16_248A")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51207.itc", 0x1E)
    SoundLoad(938)
    SoundLoad(3706)
    SoundLoad(3707)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu04800.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 250, 302000, 0)
    BeginChrThread(0x8, 3, 0, 17)
    SetMapObjFlags(0x20, 0x1000)
    OP_70(0x20, 0x0)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    Sound(836, 0, 100, 0)
    Sleep(1000)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("少年的声音")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            "#3706V#30W──呵呵，原来如此。\x02\x03",

            "#3707V这终端还真是\x01",
            "方便易用呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE7B)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    PlayBGM("ed7580", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x244), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(499510, 1050, 296140, 0)
    MoveCamera(26, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    Sound(938, 2, 60, 0)
    OP_68(499320, 1050, 303000, 5000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(500)
    OP_68(499320, 1050, 303000, 0)
    MoveCamera(26, 20, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16640, 0)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0018
    AnonymousTalk(
        0x8,
        (
            "财团首屈一指的天才系统工程师，\x01",
            "名叫约纳·塞克里德的少年吗～\x02\x03",

            "虽说只是旧式网络，\x01",
            "但竟然能构筑起这样的环境。\x02\x03",

            "看来他能捕捉到玲，\x01",
            "并不是纯粹的偶然呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    StopSound(938, 2000, 60)
    SetCameraDistance(16140, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 0)
    NewScene("e4810", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_248A end

    def Function_17_2755(): pass

    label("Function_17_2755")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2773")
    SetChrSubChip(0x8, 0x0)
    Sleep(200)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)
    Jump("Function_17_2755")

    label("loc_2773")

    Return()

    # Function_17_2755 end

    def Function_18_2774(): pass

    label("Function_18_2774")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51207.itc", 0x1E)
    SoundLoad(938)
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis416.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 250, 302000, 0)
    SetMapObjFlags(0x20, 0x1000)
    OP_70(0x20, 0xB)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    OP_68(498250, 1050, 304800, 0)
    MoveCamera(0, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(16250, 0)
    SetCameraDistance(17250, 2000)
    FadeToBright(2000, 0)
    Sleep(1500)
    OP_63(0x8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    #C0019
    ChrTalk(
        0x8,
        (
            "#6P#04805F哦……\x01",
            "还做了防护措施啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    BeginChrThread(0x8, 3, 0, 17)
    Sound(938, 2, 60, 0)
    Sleep(800)

    #C0020
    ChrTalk(
        0x8,
        (
            "#6P#04802F呵呵……\x01",
            "有点本事嘛，小雀斑。\x02\x03",

            "不过，这机关应该不会立刻暴露，\x01",
            "至少能维持到明天吧。\x02\x03",

            "#04809F机会难得，\x01",
            "要让我玩得开心一点哦⊥\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(17750, 2000)
    FadeToDark(2000, 0, -1)
    Sleep(1000)
    StopSound(938, 2000, 60)
    OP_0D()
    OP_6F(0x79)
    StopBGM(0xFA0)
    WaitBGM()
    Sleep(1000)
    Sound(13, 0, 100, 0)
    Sleep(4000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(2000)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xFE, 0x0)
    ReplaceBGM(-1, -1)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 4)
    NewScene("c0100", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_2774 end

    def Function_19_299F(): pass

    label("Function_19_299F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51207.itc", 0x1E)
    SoundLoad(938)
    SoundLoad(3708)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis339.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis340.itp")
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 498200, 250, 302000, 0)
    SetMapObjFlags(0x20, 0x1000)
    OP_70(0x20, 0x15)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    OP_68(498200, 1900, 303600, 0)
    MoveCamera(29, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15000, 0)
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    FadeToBright(0, 0)
    Sleep(500)
    SetMessageWindowPos(15, 130, -1, -1)
    OP_C9(0x0, 0x80000000)
    SetChrName("少年的声音")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            "#3708V#40W命运之塔就此显现，\x01",
            "将无数因缘卷入其中，\x01",
            "描绘出螺旋般的绘卷──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE7C)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    BeginChrThread(0x8, 3, 0, 17)
    Sound(938, 2, 60, 0)
    OP_68(498200, 1400, 302600, 3000)
    MoveCamera(29, 14, 0, 3000)
    SetCameraDistance(16000, 3000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_6F(0x79)
    Sleep(300)

    #C0022
    ChrTalk(
        0x8,
        (
            "#12P#04804F呵呵，布卢布兰应该\x01",
            "很喜欢这种场面。\x02\x03",

            "#04800F呼，既然有这么重大的活动，\x01",
            "他应该会擅自前来观赏吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    StopSound(938, 500, 60)
    Sound(839, 0, 100, 0)
    Sleep(400)
    Sound(839, 0, 100, 0)
    Sleep(400)
    EndChrThread(0x8, 0x3)
    SetChrSubChip(0x8, 0x0)
    OP_63(0x8, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0023
    ChrTalk(
        0x8,
        "#12P#04805F哦，有了有了。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    #A0024
    AnonymousTalk(
        0x8,
        (
            "#04802F呵呵……\x01",
            "接下来，只需交给『他们』就可以了。\x02\x03",

            "#04809F那么……机会难得，\x01",
            "把愉快的余兴节目也准备好吧⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToDark(0, 0, -1)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x1, 0xFF, 0x0)
    OP_24(0x3AA)
    SetScenarioFlags(0x22, 2)
    NewScene("c0180", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_19_299F end

    def Function_20_2CF4(): pass

    label("Function_20_2CF4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(489500, 1150, 200000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33000, 0)
    OP_90(0x101, 491000, 0, 200600, 90)
    OP_90(0x102, 491000, 0, 199400, 90)
    OP_90(0x104, 490000, 0, 201100, 90)
    OP_90(0x109, 490000, 0, 198900, 90)
    OP_90(0x105, 489000, 0, 199400, 90)
    OP_90(0x10A, 489000, 0, 200600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_68(500000, 1300, 208000, 0)
    MoveCamera(23, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18000, 0)
    MoveCamera(35, 21, 0, 6000)
    OP_6E(500, 0)
    SetCameraDistance(20000, 6000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)
    Sleep(500)
    OP_68(492600, 1100, 200090, 3000)
    MoveCamera(33, 16, 0, 3000)
    OP_6E(500, 3000)
    SetCameraDistance(19000, 3000)
    OP_6F(0x79)

    #C0025
    ChrTalk(
        0x101,
        "#00011F#6P（这曲子是……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2E5A():
        OP_97(0x101, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2E5A)
    Sleep(100)

    def lambda_2E77():
        OP_97(0x102, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2E77)
    Sleep(100)

    def lambda_2E94():
        OP_97(0x104, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2E94)
    Sleep(100)

    def lambda_2EB1():
        OP_97(0x109, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2EB1)
    Sleep(100)

    def lambda_2ECE():
        OP_97(0x10A, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_2ECE)
    Sleep(100)

    def lambda_2EEB():
        OP_97(0x105, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2EEB)
    Sleep(2000)
    Fade(500)
    OP_68(500000, 1100, 204000, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    WaitChrThread(0x101, 0)

    def lambda_2F3F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2F3F)
    WaitChrThread(0x102, 0)

    def lambda_2F50():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2F50)
    WaitChrThread(0x104, 0)

    def lambda_2F61():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2F61)
    WaitChrThread(0x109, 0)

    def lambda_2F72():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2F72)
    WaitChrThread(0x10A, 0)

    def lambda_2F83():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_2F83)
    WaitChrThread(0x105, 0)

    def lambda_2F94():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2F94)
    Sleep(500)

    #C0026
    ChrTalk(
        0x102,
        (
            "#12P#00108F（是约纳房间中\x01",
            "  那个导力音响播放的……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00301F（怎么回事……？\x01",
            "  出故障了吗？）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x10A)

    #C0028
    ChrTalk(
        0x10A,
        (
            "#6P#00603F（也许是陷阱……\x01",
            "  谨慎起见，进去时要小心些。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)
    Sleep(200)

    #C0029
    ChrTalk(
        0x10A,
        (
            "#6P#00601F（班宁斯、奥兰多，\x01",
            "  我们三个人先闯进去。）\x02\x03",

            "（其他三人随后跟进，\x01",
            "  做好援助我们的准备。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_30D9():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_30D9)
    Sleep(50)

    def lambda_30E9():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_30E9)
    Sleep(50)

    def lambda_30F9():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_30F9)
    Sleep(50)

    def lambda_3109():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3109)
    Sleep(50)

    def lambda_3119():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3119)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0030
    ChrTalk(
        0x101,
        "#00013F#11P（明白了。）\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#00301F#11P（收到。）\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#12P#10101F（知道了！）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 499600, 0, 202400, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x141, 4)
    ClearMapObjFlags(0x13, 0x10)
    OP_66(0x0, 0x1)
    EventEnd(0x5)
    Return()

    # Function_20_2CF4 end

    def Function_21_31C5(): pass

    label("Function_21_31C5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00200.itc", 0x1E)
    LoadChrToIndex("chr/ch00500.itc", 0x1F)
    LoadChrToIndex("chr/ch00959.itc", 0x20)
    LoadChrToIndex("chr/ch00002.itc", 0x21)
    LoadChrToIndex("chr/ch00050.itc", 0x22)
    LoadChrToIndex("chr/ch00051.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00950.itc", 0x26)
    LoadChrToIndex("chr/ch00951.itc", 0x27)
    LoadChrToIndex("apl/ch51216.itc", 0x28)
    LoadChrToIndex("apl/ch51217.itc", 0x29)
    LoadChrToIndex("apl/ch51219.itc", 0x2A)
    LoadChrToIndex("apl/ch51220.itc", 0x2B)
    LoadChrToIndex("apl/ch51221.itc", 0x2C)
    LoadChrToIndex("apl/ch51223.itc", 0x2D)
    LoadChrToIndex("apl/ch50221.itc", 0x2E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis340.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00201.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00700.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis341.itp")
    LoadEffect(0x0, "event\\ev202_00.eff")
    LoadEffect(0x1, "event\\ev15020.eff")
    LoadEffect(0x2, "event\\ev12006.eff")
    LoadEffect(0x4, "event/ev15102.eff")
    SoundLoad(868)
    SoundLoad(825)
    SoundLoad(3709)
    SoundLoad(3710)
    SoundLoad(3711)
    SoundLoad(3712)
    SoundLoad(3713)
    SoundLoad(3714)
    SoundLoad(3715)
    SoundLoad(3453)
    SoundLoad(2669)
    SoundLoad(2670)
    SoundLoad(2671)
    SoundLoad(2672)
    SoundLoad(2673)
    OP_90(0x101, 499300, 0, 205000, 0)
    OP_90(0x104, 500600, 0, 204700, 0)
    OP_90(0x10A, 500000, 150, 206400, 0)
    OP_90(0x102, 500810, 0, 200440, 0)
    OP_90(0x109, 499230, 0, 200150, 0)
    OP_90(0x105, 497790, 0, 200360, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x101, 0x22)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    OP_68(500000, 1000, 207200, 0)
    MoveCamera(40, 17, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(23500, 0)
    SetCameraDistance(22500, 2000)
    FadeToBright(1000, 0)
    OP_0D()

    def lambda_3433():
        OP_95(0xFE, 500000, 150, 207400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3433)
    WaitChrThread(0x10A, 1)
    SetChrChipByIndex(0x10A, 0x26)
    SetChrSubChip(0x10A, 0x0)
    Sleep(300)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x10A)
    OP_93(0x10A, 0xB4, 0x1F4)
    Sleep(1000)
    OP_93(0x10A, 0x0, 0x3E8)
    Sound(121, 0, 100, 0)
    Sound(103, 0, 100, 0)
    OP_71(0x13, 0x0, 0xA, 0x0, 0x0)

    def lambda_349D():
        OP_95(0xFE, 500000, 150, 210400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_349D)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 22)
    Sleep(200)

    def lambda_34C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_34C3)
    Sleep(100)
    BeginChrThread(0x104, 3, 0, 22)
    WaitChrThread(0x10A, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x10A, 0xFF)
    SetChrPos(0x101, 499700, 150, 287400, 0)
    SetChrPos(0x102, 499700, 150, 287400, 0)
    SetChrPos(0x104, 499700, 150, 287400, 0)
    SetChrPos(0x109, 499700, 150, 287400, 0)
    SetChrPos(0x105, 499700, 150, 287400, 0)
    SetChrPos(0x10A, 499700, 150, 287400, 0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x20, 0x1000)
    OP_70(0x20, 0x1F)
    SetMapObjFrame(0xFF, "pizza", 0x0, 0x1)
    OP_71(0x1E, 0x0, 0x14, 0x0, 0x20)
    VolumeBGM(0x64, 0x3E8)
    OP_68(499700, 1000, 295500, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_68(499200, 1000, 297000, 3000)
    MoveCamera(55, 20, 0, 3000)
    SetCameraDistance(24000, 3000)
    BeginChrThread(0x10A, 3, 0, 23)
    Sleep(400)
    BeginChrThread(0x101, 3, 0, 24)
    Sleep(400)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)

    #C0033
    ChrTalk(
        0x101,
        "#12P#00008F一个人都没有……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#00301F#5P好像也没有藏着人……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x10A,
        (
            "#5P#00606F#11P……逃走了吗……\x02\x03",

            "#00600F可是，在我们前往这里的路上，\x01",
            "并没有遇到任何人……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(500700, 1300, 293900, 0)
    MoveCamera(47, 20, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(19500, 0)
    BeginChrThread(0x102, 3, 0, 26)
    Sleep(500)
    BeginChrThread(0x109, 3, 0, 27)
    Sleep(500)
    BeginChrThread(0x105, 3, 0, 28)
    WaitChrThread(0x105, 3)

    #C0036
    ChrTalk(
        0x102,
        "#12P#00108F已、已经逃走了吗？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    def lambda_3776():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3776)
    Sleep(50)

    def lambda_3786():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3786)
    Sleep(50)

    def lambda_3796():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3796)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x10A, 0)

    #C0037
    ChrTalk(
        0x101,
        "#00006F#5P嗯，好像是。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00001F#6P这音乐……\x01",
            "好像是那个装置发出的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3809():
        OP_92(0x101, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3809)
    Sleep(50)

    def lambda_381F():
        OP_92(0x102, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_381F)
    Sleep(50)

    def lambda_3835():
        OP_92(0x105, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3835)
    Sleep(50)

    def lambda_384B():
        OP_92(0x10A, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_384B)
    Sleep(50)

    def lambda_3861():
        OP_92(0x109, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3861)
    Sleep(50)

    def lambda_3877():
        OP_92(0x104, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3877)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    #C0039
    ChrTalk(
        0x10A,
        (
            "#6P#00601F实在是太吵了……\x01",
            "能关掉它吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00301F#6P嗯……\x01",
            "这个就是开关吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_38F6():
        OP_96(0xFE, 0x7AF94, 0x0, 0x4824C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_38F6)
    WaitChrThread(0x104, 1)
    Sleep(150)
    Sound(853, 0, 100, 0)
    SetMapObjFlags(0x1E, 0x4)
    StopBGM(0x1F4)
    Sleep(1000)

    #C0041
    ChrTalk(
        0x109,
        "#12P#10108F总觉得很诡异呢……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#6P#00106F是、是啊……\x01",
            "这里会响着音乐\x01",
            "也很奇怪……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#12P#10308F嗯，莫名地感觉到\x01",
            "一股恶意……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(150)

    #C0044
    ChrTalk(
        0x105,
        (
            "#12P#10305F另外，里面那个屏幕上\x01",
            "显示的东西是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_68(498200, 1300, 303700, 2500)
    MoveCamera(33, 20, 0, 2500)

    def lambda_3A75():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A75)
    Sleep(50)

    def lambda_3A85():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3A85)
    Sleep(50)

    def lambda_3A95():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3A95)
    Sleep(50)

    def lambda_3AA5():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3AA5)
    Sleep(50)

    def lambda_3AB5():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3AB5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)

    #C0045
    ChrTalk(
        0x101,
        "#00005F#N#12P构造图……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(498200, 1300, 302600, 3000)
    SetCameraDistance(21000, 3000)
    BeginChrThread(0x101, 3, 0, 29)
    BeginChrThread(0x10A, 3, 0, 30)
    BeginChrThread(0x104, 3, 0, 31)
    BeginChrThread(0x102, 3, 0, 32)
    BeginChrThread(0x105, 3, 0, 33)
    BeginChrThread(0x109, 3, 0, 34)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x10A, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x105, 3)
    WaitChrThread(0x109, 3)
    OP_6F(0x79)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0046
    ChrTalk(
        0x101,
        "#11P#00011F这、这是……！\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0047
    AnonymousTalk(
        0x102,
        (
            "#00105F这、这……\x01",
            "难道是兰花塔的……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0048
    AnonymousTalk(
        0x109,
        (
            "#10101F好像是记录着兰花塔\x01",
            "内部构造图的数据……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0049
    AnonymousTalk(
        0x10A,
        (
            "#00610F啧，为何会出现在\x01",
            "这种地方——\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_7D(0xFF, 0x64, 0x64, 0x0, 0x1F4)
    BeginChrThread(0xE, 1, 0, 44)
    Sleep(800)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    PlayBGM("ed7561", 0)

    #C0050
    ChrTalk(
        0x101,
        "#11P#00011F！？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x105,
        "#12P#10310F糟了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(504300, 900, 399700, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 498800, 200, 397200, 270)
    SetChrPos(0x102, 500400, 0, 397200, 270)
    SetChrPos(0x104, 499400, 0, 400300, 225)
    SetChrPos(0x109, 501100, 0, 399700, 270)
    SetChrPos(0x105, 501100, 0, 398700, 270)
    SetChrPos(0x10A, 499600, 0, 399200, 270)
    ClearMapObjFlags(0x19, 0x10)
    OP_70(0x19, 0xA)
    Sleep(500)
    Sound(104, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_71(0x19, 0xA, 0x0, 0x0, 0x0)
    OP_79(0x19)
    OP_82(0x32, 0x0, 0xBB8, 0x12C)

    def lambda_3E0A():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3E0A)
    Sleep(30)

    def lambda_3E1A():
        OP_93(0x10A, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3E1A)
    Sleep(30)

    def lambda_3E2A():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3E2A)
    Sleep(30)

    def lambda_3E3A():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3E3A)
    Sleep(30)

    def lambda_3E4A():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3E4A)
    Sleep(30)

    def lambda_3E5A():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3E5A)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    #C0052
    ChrTalk(
        0x102,
        "#00101F#6P#N唔！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0053
    ChrTalk(
        0x10A,
        "#00610F#6P啧，中圈套了吗！？\x02",
    )

    CloseMessageWindow()
    OP_68(505950, 900, 400300, 1500)
    MoveCamera(50, 17, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(21500, 1500)

    def lambda_3EE8():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3EE8)
    Sleep(300)

    def lambda_3F05():
        OP_95(0xFE, 502700, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F05)
    WaitChrThread(0x105, 1)

    def lambda_3F23():
        OP_95(0xFE, 508400, 0, 400700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F23)
    WaitChrThread(0x109, 1)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x109, 0x2B)
    SetChrSubChip(0x109, 0x0)
    WaitChrThread(0x105, 1)
    OP_93(0x105, 0x87, 0x1F4)
    OP_6F(0x79)
    Sleep(800)

    #C0054
    ChrTalk(
        0x109,
        (
            "#10110F#6P不、不行！\x01",
            "纹丝不动，打不开了！\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#6P#10308F#5P看来是被导力装置的\x01",
            "门锁给锁住了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(4113, 255, 100, 0)    #voice#Companella
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(500300, 1600, 297000, 0)
    MoveCamera(37, 13, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 497200, 200, 301200, 180)
    SetChrPos(0x102, 497100, 0, 299900, 180)
    SetChrPos(0x104, 500200, 0, 300600, 180)
    SetChrPos(0x109, 499700, 0, 290400, 180)
    SetChrPos(0x105, 501100, 0, 291200, 225)
    SetChrPos(0x10A, 498600, 200, 300600, 180)
    OP_0D()
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)

    def lambda_410F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_410F)

    def lambda_411C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_411C)
    Sleep(500)

    #C0056
    ChrTalk(
        0x101,
        "#5P#00010F刚才那是……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#5P#00307F喂，是谁……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("声音")

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3709V#30W呵呵呵……\x01",
            "初次见面，支援科的诸位。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(160, 100, -1, -1)
    SetChrName("声音")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3710V#30W如我所料，\x01",
            "你们果然来玩了呢。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("声音")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3711V#30W作为亲近的证明，\x01",
            "我给你们留下了一些礼物，\x01",
            "希望大家玩得开心哟⊥\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE7F)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)

    #C0061
    ChrTalk(
        0x101,
        "#5P#00011F什么……\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x0, 0x1F4)
    Sleep(150)

    #C0062
    ChrTalk(
        0x10A,
        "#00607F#11P可恶，声音是从终端传出的吗？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(498200, 1300, 302300, 2000)
    MoveCamera(33, 17, 0, 2000)
    SetCameraDistance(20500, 2000)

    def lambda_42E6():
        OP_95(0xFE, 499500, 0, 298400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_42E6)

    def lambda_4300():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4300)
    Sleep(30)

    def lambda_4310():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4310)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    def lambda_4328():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4328)
    Sleep(30)

    def lambda_4338():
        OP_95(0xFE, 499200, 0, 299300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_4338)
    WaitChrThread(0x105, 1)

    def lambda_4356():
        OP_95(0xFE, 498100, 0, 299300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4356)
    WaitChrThread(0x105, 1)

    def lambda_4374():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4374)
    WaitChrThread(0x109, 1)

    def lambda_4385():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4385)
    OP_6F(0x79)
    EndChrThread(0xE, 0x1)
    Fade(250)
    OP_70(0x20, 0x29)
    Sleep(500)
    Sound(72, 0, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(500)

    #A0063
    AnonymousTalk(
        0x109,
        "#10105F这、这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0064
    AnonymousTalk(
        0x102,
        (
            "#00101F罗伯兹主任给我们的\x01",
            "益智对战游戏……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 60, -1, -1)
    SetChrName("声音")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "如果你们能在三场游戏中取得两场胜利，\x01",
            "我就放你们出去。\x02\x03",

            "不过，如果你们输了，\x01",
            "可就要被烤焦了哟～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0066
    AnonymousTalk(
        0x101,
        "#00010F什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(499300, 1300, 297300, 3000)
    MoveCamera(53, 20, 0, 3000)
    OP_6E(600, 3000)
    SetCameraDistance(20000, 3000)
    BeginChrThread(0xE, 1, 0, 45)
    Sound(614, 0, 100, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4632():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4632)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_465A():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_465A)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_467F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_467F)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_46A7():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_46A7)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_46CC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_46CC)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_46F4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_46F4)
    Sleep(1000)
    OP_6F(0x79)

    #C0067
    ChrTalk(
        0x109,
        "#6P#10111F这……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#5P#00307F怎么可能……！\x01",
            "刚才并没有发现这种机关啊！！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    OP_68(498200, 1300, 302300, 0)
    MoveCamera(33, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    OP_0D()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声音")

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "呵呵，那我们就\x01",
            "立刻开始吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "时间已经不多了……\x01",
            "如果不快一点，可是会死的哟～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_93(0x10A, 0x0, 0x1F4)

    #C0071
    ChrTalk(
        0x10A,
        "#00610F你……！\x02",
    )

    CloseMessageWindow()

    def lambda_4823():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4823)

    def lambda_4830():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4830)
    Sleep(30)

    def lambda_4840():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4840)
    Sleep(30)

    def lambda_4850():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4850)
    Sleep(30)

    def lambda_4860():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4860)
    Sleep(30)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    #C0072
    ChrTalk(
        0x105,
        (
            "#12P#10307F罗伊德！\x01",
            "现在也只能试试看了！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#11P#00010F啧！我明白了！\x02",
    )

    CloseMessageWindow()
    StopSound(868, 1000, 40)
    StopSound(825, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0x20, 0x33)
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4940")
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4936")
    OP_2C(0xA3, 0x1)
    Jump("loc_493B")

    label("loc_4936")

    OP_2C(0xA3, 0x2)

    label("loc_493B")

    Jump("loc_4943")

    label("loc_4940")

    ClearScenarioFlags(0x0, 1)

    label("loc_4943")

    FadeToBright(0, -1)
    SetChrChipByIndex(0x101, 0x21)
    SetChrSubChip(0x101, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrPos(0x101, 498200, 250, 302000, 0)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 498500, 2000, 401200, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 501700, 1500, 404100, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 507700, 1000, 402700, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x1, 0xFF, 0xFF, 0x0, 507200, 500, 396600, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 1000)
    Sound(868, 2, 40, 0)
    Sound(825, 2, 40, 0)
    SetCameraDistance(20000, 0)
    SetCameraDistance(20500, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4C33")

    #C0074
    ChrTalk(
        0x101,
        "#11P#00000F好！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#12P#00102F罗伊德，好厉害！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        "#00309F干得不错嘛！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声音")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "唔，\x01",
            "我好像太手下留情了。\x02\x03",

            "那么，接下来就要用真本事了～\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4CE8")

    label("loc_4C33")


    #C0078
    ChrTalk(
        0x101,
        "#11P#00010F……唔………\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        "#10106F#12P啊啊……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x105,
        (
            "#12P#10306F嗯……真遗憾，\x01",
            "不过……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声音")

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "啊哈哈！\x01",
            "你们已经走投无路了。\x02\x03",

            "那么，接下来就是致命一击——\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4CE8")

    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("少女的声音")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2669V#30W适可而止吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA6D)
    OP_C9(0x1, 0x80000000)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声音")

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#4S ！？ \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7524", 0)

    #C0084
    ChrTalk(
        0x102,
        "#12P#00105F啊……！\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#11P#00005F这声音是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("少女的声音")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2670V#30W接下来由我\x01",
            "当你的对手。\x02",
        )
    )

    CloseMessageWindow()

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2671V#30W做好觉悟吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA6F)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    StopSound(868, 1000, 40)
    StopSound(825, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(0, -1, 0)
    Sleep(500)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_08a.pmf", 0x20C, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    Sound(868, 2, 60, 0)
    Sound(825, 2, 60, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_509A")
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 498500, 2000, 401200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 501700, 1500, 404100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507700, 1000, 402700, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507200, 500, 396600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)

    label("loc_509A")

    FadeToBright(0, -1)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_53CF")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声音")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3712V#30W哎……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE80)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("少女的声音")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2672V#30W继续。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xA70)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    StopSound(868, 1000, 60)
    StopSound(825, 1000, 60)
    FadeToDark(1000, 0, -1)
    OP_0D()
    FadeToDark(0, -1, 0)
    Sleep(500)
    OP_C9(0x0, 0x10)
    FadeToBright(0, 0)
    OP_0D()
    PlayMovie(0x0, "ed72_08b.pmf", 0x20C, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    FadeToDark(0, 0, -1)
    OP_0D()
    OP_C9(0x1, 0x10)
    Sound(868, 2, 60, 0)
    Sound(825, 2, 60, 0)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 498500, 2000, 401200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 501700, 1500, 404100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507700, 1000, 402700, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507200, 500, 396600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    FadeToBright(0, -1)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    label("loc_53CF")

    StopBGM(0xFA0)

    #C0090
    ChrTalk(
        0x101,
        "#11P#00002F成、成功了……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x2D, 0x1F4)
    Sleep(100)

    #C0091
    ChrTalk(
        0x104,
        (
            "#00310F#5P呜……\x01",
            "已经快来不及了吧！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声音")

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3713V#30W呵呵呵，干得漂亮。\x02",
        )
    )

    CloseMessageWindow()

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3714V#30W她好像也是你们的同伴，\x01",
            "那我就遵照约定，放你们出去吧。\x02",
        )
    )

    CloseMessageWindow()

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3715V#30W好啦，我们下次见⊥\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE83)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    Fade(250)
    OP_68(504300, 900, 399700, 0)
    MoveCamera(50, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 498300, 250, 398300, 270)
    SetChrPos(0x102, 500400, 0, 397200, 270)
    SetChrPos(0x104, 499400, 0, 400300, 225)
    SetChrPos(0x109, 501100, 0, 399700, 270)
    SetChrPos(0x105, 501100, 0, 398700, 270)
    SetChrPos(0x10A, 499600, 0, 399200, 270)
    Sleep(500)
    Sound(103, 0, 100, 0)
    Sound(121, 0, 100, 0)
    OP_71(0x19, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x19)
    OP_82(0x32, 0x0, 0xBB8, 0x12C)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    SetChrSubChip(0x101, 0x2)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_55EC():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_55EC)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5611():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_5611)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5639():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5639)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_565E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_565E)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5686():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_5686)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x109,
        "#10107F#5P门开了……！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x10A,
        "#00610F#5P快！要爆炸了！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(100)
    Sound(812, 0, 100, 0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x101, 498800, 200, 397200, 270)
    OP_0D()
    OP_93(0x101, 0x59, 0x1F4)

    #C0097
    ChrTalk(
        0x101,
        "#6P#00007F#N嗯！\x02",
    )

    CloseMessageWindow()
    OP_68(509000, 900, 399700, 4000)
    MoveCamera(57, 17, 0, 4000)
    SetCameraDistance(20500, 4000)
    BeginChrThread(0x109, 3, 0, 35)
    BeginChrThread(0x105, 3, 0, 36)
    BeginChrThread(0x104, 3, 0, 37)
    BeginChrThread(0x102, 3, 0, 38)
    BeginChrThread(0x10A, 3, 0, 39)
    BeginChrThread(0x101, 3, 0, 40)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    WaitChrThread(0x101, 3)
    OP_6F(0x79)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x104, 0xFF)
    EndChrThread(0x10A, 0xFF)
    EndChrThread(0x102, 0xFF)
    EndChrThread(0x105, 0xFF)
    EndChrThread(0x109, 0xFF)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x10A, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrPos(0x101, 500000, 150, 210400, 180)
    SetChrPos(0x102, 500000, 150, 207400, 180)
    SetChrPos(0x104, 500000, 0, 205000, 180)
    SetChrPos(0x109, 502000, 0, 200700, 315)
    SetChrPos(0x105, 502000, 0, 199600, 315)
    SetChrPos(0x10A, 498700, 0, 199200, 0)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 489200, 0, 198100, 0)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetMapObjFlags(0x1A, 0x1000)
    SetMapObjFlags(0x1B, 0x1000)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x1000)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x13, 0x4)
    OP_68(500000, 1000, 209400, 0)
    MoveCamera(27, 21, 5, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(500000, 1300, 204000, 2000)
    MoveCamera(45, 17, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(19500, 2000)
    BeginChrThread(0x104, 3, 0, 43)
    BeginChrThread(0x102, 3, 0, 42)
    BeginChrThread(0x101, 3, 0, 41)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x1E)
    FadeToBright(500, 0)
    OP_0D()
    OP_82(0xC8, 0x0, 0xBB8, 0x258)
    OP_C9(0x0, 0x80000000)

    #C0098
    ChrTalk(
        0x10A,
        "#12A#00607F#3453V#12P#N#4S趴下！\x02",
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x101, 3)
    SetChrSubChip(0x101, 0x1)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x102, 0x1)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x104, 0x1)
    SetChrChipByIndex(0x104, 0x2A)
    SetChrSubChip(0x109, 0x1)
    SetChrChipByIndex(0x109, 0x2B)
    SetChrSubChip(0x105, 0x1)
    SetChrChipByIndex(0x105, 0x2C)
    SetChrSubChip(0x10A, 0x1)
    SetChrChipByIndex(0x10A, 0x2D)
    Sound(2030, 255, 100, 0)    #voice#Lloyd
    Sound(2128, 255, 100, 1)    #voice#Elie
    Sound(2317, 255, 100, 2)    #voice#Randy
    Sound(2463, 255, 100, 3)    #voice#Noel
    Sound(2402, 255, 100, 4)    #voice#Lazy
    PlayEffect(0x2, 0xFF, 0xFF, 0x0, 500000, 400, 208000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(2500)
    SetMapObjFrame(0xFF, "koge00", 0x1, 0x1)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x7D0)
    Sound(200, 0, 100, 0)
    Sound(833, 0, 100, 0)
    StopSound(868, 2000, 30)
    StopSound(825, 2000, 30)
    Sleep(2500)

    def lambda_5A2F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5A2F)
    WaitChrThread(0x101, 2)
    Sleep(500)

    #C0099
    ChrTalk(
        0x101,
        "#5P#00006F#40W呼……呼……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        "#00306F#40W#11P呼，真是千钧一发啊……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        "#10106F#40W#11P我、我还以为这次死定了……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x10A,
        (
            "#00610F#40W#11P唔……\x01",
            "究竟是谁……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearChrFlags(0x9, 0x80)
    OP_C9(0x0, 0x80000000)

    #N0103
    NpcTalk(
        0x9,
        "少女的声音",
        (
            "#2673V#30W太好了，\x01",
            "你们好像没事呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xA71)
    OP_C9(0x1, 0x80000000)
    OP_63(0x101, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7565", 0)
    Fade(500)
    OP_68(501600, 1100, 506500, 0)
    MoveCamera(49, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18500, 0)
    OP_68(501900, 1100, 499900, 3000)
    MoveCamera(35, 23, 0, 3000)
    SetCameraDistance(17500, 3000)
    SetMapObjFrame(0x1C, "sign01", 0x0, 0x1)
    SetMapObjFrame(0x1C, "light01", 0x0, 0x1)
    ClearMapObjFlags(0x1C, 0x10)
    OP_70(0x1C, 0xA)
    SetChrPos(0x101, 502600, 0, 499800, 270)
    SetChrPos(0x102, 500400, 0, 500300, 90)
    SetChrPos(0x104, 500400, 0, 499000, 90)
    SetChrPos(0x109, 498900, 0, 498300, 45)
    SetChrPos(0x105, 499900, 0, 497600, 45)
    SetChrPos(0x10A, 498900, 0, 500000, 90)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x104, 0x1)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    SetChrSubChip(0x10A, 0x0)
    SetChrPos(0x9, 501600, 0, 507500, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    SetChrChipByIndex(0xA, 0x1F)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 500000, 150, 512000, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0xB, 0x2E)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrPos(0xB, 500000, 0, 504000, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_5D4F():
        OP_96(0xFE, 0x7AA1C, 0x0, 0x7A508, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5D4F)
    OP_0D()
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x104, 500)

    #C0104
    ChrTalk(
        0x101,
        "#12P#00002F缇欧！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        (
            "#00102F果、果然是\x01",
            "缇欧啊！\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#6P#00302F喂喂！\x01",
            "这到底是怎么回事！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2276, 255, 80, 0)    #voice#Tio
    Sleep(800)

    def lambda_5DE3():
        OP_95(0xFE, 502500, 0, 500400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5DE3)
    WaitChrThread(0x9, 1)

    def lambda_5E01():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5E01)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    def lambda_5E31():
        OP_96(0xFE, 0x7AA1C, 0x0, 0x7A508, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5E31)
    TurnDirection(0x101, 0x9, 500)
    WaitChrThread(0x9, 1)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0107
    AnonymousTalk(
        0x9,
        (
            "我是乘坐今天下午\x01",
            "开往克洛斯贝尔的\x01",
            "国际定期船回来的。\x02\x03",

            "听说最近发生了不少事情，\x01",
            "所以我就申请提前回来了。\x02",
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

    #C0108
    ChrTalk(
        0x101,
        "#12P#00000F这样啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    TurnDirection(0x102, 0x9, 0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    TurnDirection(0x104, 0x9, 0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    TurnDirection(0x109, 0x9, 0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    TurnDirection(0x105, 0x9, 0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    TurnDirection(0x10A, 0x9, 0)
    OP_0D()
    Sleep(150)

    #C0109
    ChrTalk(
        0x104,
        (
            "#6P#00309F哈哈……\x01",
            "回来得太是时候了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0110
    ChrTalk(
        0x105,
        (
            "#12P#N#10302F你是听科长说我们在这里，\x01",
            "就找过来了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TurnDirection(0x9, 0x104, 500)

    #C0111
    ChrTalk(
        0x9,
        (
            "#00204F嗯，用艾尼格玛联络时，\x01",
            "科长说你们来这里了。\x02\x03",

            "#00202F所以我就从空港直接过来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#00104F呵呵……\x01",
            "真是救了我们啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x109,
        "#6P#N#10109F太感谢你了，缇欧！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0114
    ChrTalk(
        0x9,
        "#00204F#5P哪里，及时赶到真是太好了。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    #C0115
    ChrTalk(
        0x9,
        (
            "#00201F#5P……话说回来，\x01",
            "对手似乎相当危险。\x02\x03",

            "不过总算是成功插入游戏，\x01",
            "把他击退了……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#12P#00005F插入游戏——哦，是指刚才啊。\x02",
    )

    CloseMessageWindow()
    OP_68(502700, 500, 508900, 2000)
    OP_93(0x9, 0x0, 0x190)
    OP_6F(0x79)

    #C0117
    ChrTalk(
        0x9,
        (
            "#12P#N#00202F嗯，我发现你们\x01",
            "都被关在里面，\x01",
            "所以就用预备线路接入了。\x02\x03",

            "#00206F对方应该是个\x01",
            "实力相当强的黑客。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0118
    ChrTalk(
        0x101,
        "#00006F#12P#N嗯，看来没错。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(501000, 1100, 500100, 0)
    MoveCamera(35, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    #C0119
    ChrTalk(
        0x10A,
        (
            "#6P#00601F哼，看样子，\x01",
            "犯人早已逃走了啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x10A,
        (
            "#6P#00605F对了，普拉托。\x02\x03",

            "你是一个人穿越地下空间，\x01",
            "追到这里的吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 500)
    Sleep(150)

    #C0121
    ChrTalk(
        0x9,
        (
            "#11P#00205F啊，不是的。\x02\x03",

            "#00203F……我们偶然相遇，\x01",
            "于是就一起过来了。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0122
    ChrTalk(
        0x101,
        "#12P#00005F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2629, 255, 100, 0)    #voice#Yin
    Sleep(800)
    ClearChrFlags(0xA, 0x80)

    #N0123
    NpcTalk(
        0xA,
        "声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#N真是在意想不到的\x01",
            "地方见面了呢。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7516", 0)
    OP_68(500140, 1100, 501660, 3000)
    MoveCamera(47, 15, 0, 3000)
    OP_6E(550, 3000)
    SetCameraDistance(15500, 3000)

    def lambda_647E():
        OP_96(0xFE, 0x7A120, 0x0, 0x7B0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_647E)

    def lambda_6498():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6498)

    def lambda_64A9():

        label("loc_64A9")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_64A9")

    QueueWorkItem2(0x101, 2, lambda_64A9)

    def lambda_64BB():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_64BB)

    def lambda_64C8():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_64C8)

    def lambda_64D5():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_64D5)

    def lambda_64E2():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_64E2)

    def lambda_64EF():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_64EF)

    def lambda_64FC():

        label("loc_64FC")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_64FC")

    QueueWorkItem2(0x9, 2, lambda_64FC)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    #C0124
    ChrTalk(
        0x101,
        "#00007F你是……！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x109,
        "#12P#10107F那、那时候的……！\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#12P#00101F『银』……！\x02",
    )

    CloseMessageWindow()
    Sound(2627, 255, 100, 0)    #voice#Yin
    Sleep(800)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)

    #A0127
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "……那家伙已经逃走了吗？\x02\x03",

            "虽然不知是从哪里来的老鼠，\x01",
            "但似乎相当狡猾啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0128
    ChrTalk(
        0x101,
        (
            "#00006F等、等一下！\x02\x03",

            "#00013F难道那个黑客\x01",
            "与『黑月』有关吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00700F非也，此人与『黑月』毫无关联。\x02\x03",

            "恐怕和『赤色星座』的人\x01",
            "也没什么关系。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        "#00005F什么……！？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#12P#00301F你为何会\x01",
            "知道这些？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702F呵呵，『黑月』和『赤色星座』\x01",
            "现在已经进入了互相监视的状态。\x02\x03",

            "目前至少可以肯定，\x01",
            "那名黑客并不从属于任何一方。\x02\x03",

            "#00700F看样子，似乎是对\x01",
            "通商会议有所图谋之辈。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x101,
        "#00013F……！\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    #C0134
    ChrTalk(
        0x102,
        (
            "#12P#00108F终端屏幕上所显示的\x01",
            "那张兰花塔构造图……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x105,
        (
            "#12P#10303F原来如此……\x01",
            "正是明天的会场啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x10A,
        "#12P#00608F#30W………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_68A6():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_68A6)
    WaitChrThread(0x10A, 1)
    Sleep(300)

    #C0137
    ChrTalk(
        0x10A,
        (
            "#12P#00603F似乎还是初次见面吧？\x02\x03",

            "#00600F我是克洛斯贝尔警察局\x01",
            "搜查一科的阿雷克斯·达德利。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702F呵呵……久闻大名。\x02\x03",

            "通商会议的警备工作\x01",
            "好像很辛苦吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x10A,
        (
            "#12P#00604F哼，还不是因为一群可疑的家伙\x01",
            "一直在蠢蠢欲动，其中尤以某个组织为最。\x02\x03",

            "看样子，你似乎了解不少\x01",
            "我们还没有掌握到的情报……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    Sound(531, 0, 50, 0)
    SetChrChipByIndex(0x10A, 0x26)
    SetChrSubChip(0x10A, 0x0)
    OP_0D()
    Sleep(300)

    #C0140
    ChrTalk(
        0x10A,
        (
            "#12P#00601F能否和我回警察局\x01",
            "仔细谈谈？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6A37():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6A37)
    Sleep(50)

    def lambda_6A47():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6A47)
    Sleep(50)

    def lambda_6A57():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6A57)
    Sleep(50)

    def lambda_6A67():
        TurnDirection(0x9, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6A67)
    Sleep(50)

    def lambda_6A77():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6A77)
    Sleep(50)

    def lambda_6A87():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6A87)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_6AAC():

        label("loc_6AAC")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6AAC")

    QueueWorkItem2(0x101, 2, lambda_6AAC)

    def lambda_6ABE():

        label("loc_6ABE")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6ABE")

    QueueWorkItem2(0x102, 2, lambda_6ABE)

    def lambda_6AD0():

        label("loc_6AD0")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6AD0")

    QueueWorkItem2(0x9, 2, lambda_6AD0)

    def lambda_6AE2():

        label("loc_6AE2")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6AE2")

    QueueWorkItem2(0x109, 2, lambda_6AE2)

    def lambda_6AF4():

        label("loc_6AF4")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6AF4")

    QueueWorkItem2(0x105, 2, lambda_6AF4)

    def lambda_6B06():

        label("loc_6B06")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6B06")

    QueueWorkItem2(0x104, 2, lambda_6B06)

    #C0141
    ChrTalk(
        0x101,
        "#00011F达德利警官……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#00305F喂喂……你是认真的吗？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702F呵呵，吾有何嫌疑？\x02\x03",

            "吾似乎并无触犯\x01",
            "克洛斯贝尔的刑法。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x10A,
        (
            "#12P#00602F言重了，只是普通的询问调查而已。\x02\x03",

            "#00607F如果你内心坦然，\x01",
            "还请务必赏光！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xA, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_6C38():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_6C38)
    ClearChrFlags(0xB, 0x80)

    def lambda_6C4E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_6C4E)
    Sleep(200)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    OP_68(500500, 1100, 504600, 1000)
    MoveCamera(59, 23, 0, 1000)
    SetCameraDistance(16500, 1000)
    SetChrFlags(0x10A, 0x20)
    SetChrFlags(0x10A, 0x1000)
    SetChrChipByIndex(0x10A, 0x20)
    SetChrSubChip(0x10A, 0x0)
    SetChrChip(0x0, 0x10A, 0x1E, 0x64)
    Sound(250, 0, 80, 0)

    def lambda_6CB3():
        OP_96(0xFE, 0x7A4A4, 0x0, 0x7B700, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6CB3)
    WaitChrThread(0x10A, 1)
    CancelBlur(0)
    SetChrChipByIndex(0x10A, 0x2D)
    SetChrSubChip(0x10A, 0x1)
    Sleep(1000)
    SetChrChip(0x1, 0x10A, 0x0, 0x0)
    ClearChrFlags(0x10A, 0x20)
    ClearChrFlags(0x10A, 0x1000)
    SetChrChipByIndex(0x10A, 0x26)
    SetChrSubChip(0x10A, 0x0)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x102, 0x2)
    EndChrThread(0x9, 0x2)
    EndChrThread(0x104, 0x2)
    EndChrThread(0x109, 0x2)
    EndChrThread(0x105, 0x2)
    OP_6F(0x79)
    Sleep(500)
    #Sound(2555, 255, 100, 0)    #voice#Dudley

    #C0145
    ChrTalk(
        0x10A,
        "#11P#00603F哼……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0146
    ChrTalk(
        0x9,
        "#00205F……什么时候离开的……\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x105,
        (
            "#10302F#12P#N嘿，是分身\x01",
            "符术吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(2628, 255, 100, 0)    #voice#Yin
    Sleep(800)
    SetMessageWindowPos(15, 10, -1, -1)
    SetChrName("银的声音")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#40W……今晚就此别过。\x02\x03",

            "#30W我们应该会于\x01",
            "近期再度相会的。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0xA, 0x80)
    OP_68(500000, 1500, 501500, 3000)
    MoveCamera(47, 15, 0, 3000)
    SetCameraDistance(17500, 3000)
    Sleep(1000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x10A, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x9, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x109)
    OP_64(0x105)
    OP_64(0x10A)
    OP_64(0x9)
    OP_6F(0x79)
    Sleep(300)
    TurnDirection(0x9, 0x101, 500)

    #C0149
    ChrTalk(
        0x9,
        (
            "#5P#00201F……罗伊德前辈，\x01",
            "要在附近搜索吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#11P#00006F不……没那个必要了。\x02\x03",

            "#00001F我们还是先回支援科\x01",
            "讨论一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    TurnDirection(0x10A, 0x101, 500)

    #C0151
    ChrTalk(
        0x10A,
        (
            "#5P#00606F嗯……\x01",
            "虽非本意，但也没办法了。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(500000, 2000, 501500, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_6F(0x79)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrFlags(0x9, 0x80)
    RemoveParty(0x9, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    OP_32(0x2, 0x0, 0x3F)
    OP_32(0x2, 0x5, 0x64)
    OP_42(0x2, 0x413, 0xFF)
    OP_42(0x2, 0x5E1, 0xFF)
    OP_42(0x2, 0x645, 0xFF)
    RemoveCraft(0x2, 0xFFFF)
    OP_38(0x2, 0x80, 0x2)
    OP_38(0x2, 0x81, 0x1)
    OP_38(0x2, 0x82, 0x1)
    OP_38(0x2, 0x83, 0x1)
    OP_38(0x2, 0x85, 0x1)
    OP_38(0x2, 0x86, 0x1)
    OP_42(0x2, 0xE3, 0x0)
    OP_42(0x2, 0x88, 0x1)
    OP_42(0x2, 0x78, 0x2)
    OP_42(0x2, 0x8F, 0x3)
    OP_42(0x2, 0x68, 0x5)
    OP_42(0x2, 0x74, 0x6)
    SetScenarioFlags(0x20, 3)
    AddCraft(0x2, 0xAA)
    AddCraft(0x2, 0xAC)
    AddCraft(0x2, 0xAD)
    AddCraft(0x2, 0xAE)
    AddCraft(0x2, 0xB0)
    AddCraft(0x2, 0x122)
    AddCraft(0x2, 0x123)
    SetChrChipPat(0x2, 0x6, 0x123)
    SetChrChipPat(0x2, 0x6, 0x125)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7040")
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)
    Jump("loc_705E")

    label("loc_7040")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_7056")
    AddCraft(0x2, 0x19B)
    AddCraft(0x0, 0x19B)
    Jump("loc_705E")

    label("loc_7056")

    AddCraft(0x2, 0x187)
    AddCraft(0x0, 0x187)

    label("loc_705E")

    AddCraft(0x2, 0x164)
    AddCraft(0x2, 0x189)
    AddCraft(0x1, 0x189)
    AddCraft(0x2, 0x18B)
    AddCraft(0x3, 0x18B)
    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 5)
    NewScene("c011B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_21_31C5 end

    def Function_22_7085(): pass

    label("Function_22_7085")


    def lambda_708A():
        OP_96(0xFE, 0x7A120, 0x96, 0x32A28, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_708A)
    WaitChrThread(0xFE, 1)

    def lambda_70A8():
        OP_96(0xFE, 0x7A120, 0x96, 0x335E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_70A8)
    Sleep(300)

    def lambda_70C5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_70C5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_7085 end

    def Function_23_70D6(): pass

    label("Function_23_70D6")


    def lambda_70DB():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_70DB)

    def lambda_70F5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_70F5)
    WaitChrThread(0xFE, 1)

    def lambda_710A():
        OP_95(0xFE, 501000, 0, 296900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_710A)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x3C, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_23_70D6 end

    def Function_24_713F(): pass

    label("Function_24_713F")


    def lambda_7144():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7144)

    def lambda_715E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_715E)
    WaitChrThread(0xFE, 1)

    def lambda_7173():
        OP_95(0xFE, 499700, 0, 295200, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7173)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_24_713F end

    def Function_25_71A1(): pass

    label("Function_25_71A1")


    def lambda_71A6():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_71A6)

    def lambda_71C0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_71C0)
    WaitChrThread(0xFE, 1)

    def lambda_71D5():
        OP_95(0xFE, 501700, 0, 294900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_71D5)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x3C, 0x1F4)
    Return()

    # Function_25_71A1 end

    def Function_26_7203(): pass

    label("Function_26_7203")


    def lambda_7208():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7208)

    def lambda_7222():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7222)
    WaitChrThread(0xFE, 1)

    def lambda_7237():
        OP_95(0xFE, 499300, 0, 293200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7237)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_7203 end

    def Function_27_7258(): pass

    label("Function_27_7258")


    def lambda_725D():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_725D)

    def lambda_7277():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7277)
    WaitChrThread(0xFE, 1)

    def lambda_728C():
        OP_95(0xFE, 501800, 0, 293000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_728C)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_27_7258 end

    def Function_28_72AD(): pass

    label("Function_28_72AD")


    def lambda_72B2():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72B2)

    def lambda_72CC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_72CC)
    WaitChrThread(0xFE, 1)

    def lambda_72E1():
        OP_95(0xFE, 500300, 0, 292400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_72E1)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_72AD end

    def Function_29_7302(): pass

    label("Function_29_7302")

    SetChrPos(0x101, 500300, 0, 296300, 0)

    def lambda_7318():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7318)
    WaitChrThread(0xFE, 1)

    def lambda_7336():
        OP_95(0xFE, 497200, 0, 299700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7336)
    WaitChrThread(0xFE, 1)

    def lambda_7354():
        OP_95(0xFE, 497200, 200, 301200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7354)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_29_7302 end

    def Function_30_7375(): pass

    label("Function_30_7375")

    SetChrPos(0x10A, 501300, 200, 295600, 0)
    Sleep(700)

    def lambda_738E():
        OP_95(0xFE, 498600, 200, 300600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_738E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_30_7375 end

    def Function_31_73AF(): pass

    label("Function_31_73AF")

    SetChrPos(0x10A, 501300, 200, 294600, 0)
    Sleep(1800)

    def lambda_73C8():
        OP_95(0xFE, 500200, 0, 300600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_73C8)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_73AF end

    def Function_32_73E9(): pass

    label("Function_32_73E9")

    SetChrPos(0x102, 500300, 0, 295300, 0)
    Sleep(1300)

    def lambda_7402():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7402)
    WaitChrThread(0xFE, 1)

    def lambda_7420():
        OP_95(0xFE, 497100, 0, 299900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7420)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_32_73E9 end

    def Function_33_7441(): pass

    label("Function_33_7441")

    SetChrPos(0x105, 500300, 0, 294300, 0)
    Sleep(1900)

    def lambda_745A():
        OP_95(0xFE, 499500, 0, 298400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_745A)
    WaitChrThread(0xFE, 1)

    def lambda_7478():
        OP_95(0xFE, 498100, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7478)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_7441 end

    def Function_34_7499(): pass

    label("Function_34_7499")

    SetChrPos(0x109, 500300, 0, 294300, 0)
    Sleep(2500)

    def lambda_74B2():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74B2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_34_7499 end

    def Function_35_74D3(): pass

    label("Function_35_74D3")


    def lambda_74D8():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_74D8)
    WaitChrThread(0x109, 1)
    Return()

    # Function_35_74D3 end

    def Function_36_74F2(): pass

    label("Function_36_74F2")

    Sleep(300)

    def lambda_74FA():
        OP_95(0xFE, 502700, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_74FA)
    WaitChrThread(0x105, 1)

    def lambda_7518():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7518)
    WaitChrThread(0x105, 1)
    Return()

    # Function_36_74F2 end

    def Function_37_7532(): pass

    label("Function_37_7532")

    Sleep(550)

    def lambda_753A():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_753A)
    WaitChrThread(0x104, 1)

    def lambda_7558():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7558)
    WaitChrThread(0x104, 1)
    Return()

    # Function_37_7532 end

    def Function_38_7572(): pass

    label("Function_38_7572")

    Sleep(200)

    def lambda_757A():
        OP_95(0xFE, 502500, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_757A)
    WaitChrThread(0xFE, 1)

    def lambda_7598():
        OP_95(0xFE, 505900, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7598)
    WaitChrThread(0xFE, 1)

    def lambda_75B6():
        OP_95(0xFE, 509000, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75B6)
    WaitChrThread(0xFE, 1)

    def lambda_75D4():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75D4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_7572 end

    def Function_39_75EE(): pass

    label("Function_39_75EE")

    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(900)

    def lambda_75FD():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_75FD)
    WaitChrThread(0x10A, 1)

    def lambda_761B():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_761B)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_39_75EE end

    def Function_40_7635(): pass

    label("Function_40_7635")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(850)

    def lambda_7644():
        OP_95(0xFE, 502500, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7644)
    WaitChrThread(0xFE, 1)

    def lambda_7662():
        OP_95(0xFE, 505900, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7662)
    WaitChrThread(0xFE, 1)

    def lambda_7680():
        OP_95(0xFE, 509000, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7680)
    WaitChrThread(0xFE, 1)

    def lambda_769E():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_769E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_7635 end

    def Function_41_76B8(): pass

    label("Function_41_76B8")

    Sleep(300)

    def lambda_76C0():
        OP_95(0xFE, 500000, 0, 202400, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76C0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_76B8 end

    def Function_42_76DA(): pass

    label("Function_42_76DA")


    def lambda_76DF():
        OP_95(0xFE, 500000, 0, 203700, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76DF)
    WaitChrThread(0xFE, 1)

    def lambda_76FD():
        OP_95(0xFE, 499400, 0, 200700, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76FD)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_76DA end

    def Function_43_771E(): pass

    label("Function_43_771E")


    def lambda_7723():
        OP_95(0xFE, 500000, 0, 204000, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7723)
    WaitChrThread(0xFE, 1)

    def lambda_7741():
        OP_95(0xFE, 500400, 0, 200000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7741)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_43_771E end

    def Function_44_7762(): pass

    label("Function_44_7762")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7784")
    Sound(840, 0, 100, 0)
    Sleep(1500)
    Sound(840, 0, 100, 0)
    Sleep(2000)
    Jump("Function_44_7762")

    label("loc_7784")

    Return()

    # Function_44_7762 end

    def Function_45_7785(): pass

    label("Function_45_7785")

    Sound(868, 2, 20, 0)
    Sound(825, 2, 20, 0)
    Sleep(200)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(300)
    OP_25(0x364, 0x28)
    OP_25(0x339, 0x28)
    Return()

    # Function_45_7785 end

    def Function_46_77A8(): pass

    label("Function_46_77A8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SoundLoad(931)
    SoundLoad(825)
    OP_68(295000, 1500, 300000, 0)
    MoveCamera(40, 10, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(25000, 0)
    ClearMapObjFlags(0xC, 0x10)
    OP_70(0xC, 0x1E)
    ClearMapObjFlags(0x1D, 0x4)
    OP_75(0x1D, 0x2, 0x1B58)
    OP_7D(0x7D, 0x9B, 0xFF, 0x0, 0x2328)
    Sound(930, 0, 100, 0)
    OP_68(315000, 1500, 300000, 9000)
    MoveCamera(57, 10, -10, 9000)
    SetCameraDistance(27000, 9000)
    FadeToBright(1000, 0)
    OP_0D()
    BeginChrThread(0xE, 1, 0, 47)
    Sleep(7000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m0301", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_46_77A8 end

    def Function_47_785E(): pass

    label("Function_47_785E")

    Sound(931, 2, 30, 0)
    Sound(825, 2, 30, 0)
    Sleep(400)
    OP_25(0x3A3, 0x28)
    OP_25(0x339, 0x28)
    Sleep(400)
    OP_25(0x3A3, 0x32)
    OP_25(0x339, 0x32)
    Sleep(400)
    OP_25(0x3A3, 0x3C)
    OP_25(0x339, 0x3C)
    Sleep(400)
    OP_25(0x3A3, 0x46)
    OP_25(0x339, 0x46)
    Sleep(400)
    OP_25(0x3A3, 0x50)
    OP_25(0x339, 0x50)
    Sleep(400)
    OP_25(0x339, 0x5A)
    Sleep(400)
    OP_25(0x339, 0x64)
    Sleep(4200)
    StopSound(931, 1000, 80)
    StopSound(825, 1000, 100)
    Return()

    # Function_47_785E end

    def Function_48_78BF(): pass

    label("Function_48_78BF")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "管道的入口\x01",
            "上着坚固的锁。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_48_78BF end

    SaveToFile()

Try(main)
