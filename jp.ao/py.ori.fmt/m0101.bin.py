from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ティオ",                 # 2
        "銀",                     # 3
        "符術",                   # 4
        "ブラッドモナド",         # 5
        "トルゾーＢ",             # 6
        "SE制御",                 # 7
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

    Sepith("Sepith_7DA1", 11,  1,   8,   0,   3,   7,   0)
    Sepith("Sepith_7D91", 0,   10,  5,   0,   6,   2,   4)
    Sepith("Sepith_7DA9", 0,   0,   0,   8,   6,   6,   6)
    Sepith("Sepith_7D99", 6,   0,   11,  0,   0,   4,   6)

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
        "BattleInfo_6C4", 0x0000, 62, 6, 60, 6, 1, 25, 0, "bm0101", "Sepith_7DA1", 30, 45, 20, 5,
        (
            ("ms75800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms75800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms75800.dat", "ms75800.dat", "ms68700.dat", "ms75800.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_534", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_7D91", 30, 45, 20, 5,
        (
            ("ms63800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms63800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms63800.dat", "ms63800.dat", "ms75800.dat", "ms63800.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_AAC", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0100", "Sepith_7DA9", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 62, 6, 60, 6, 1, 40, 0, "bm0101", "Sepith_7DA9", 30, 45, 20, 5,
        (
            ("ms60500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4D4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
            ("ms60500.dat", "ms60500.dat", "ms60500.dat", "ms60500.dat", 0, 0, 0, 0, "MonsterBattlePostion_4B4", "MonsterBattlePostion_514", "ed7450", "ed7453", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_5FC", 0x0000, 62, 6, 60, 6, 1, 30, 0, "bm0101", "Sepith_7D99", 30, 45, 20, 5,
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
        "Function_5_16A5",         # 05, 5
        "Function_6_180C",         # 06, 6
        "Function_7_195D",         # 07, 7
        "Function_8_1B74",         # 08, 8
        "Function_9_1C02",         # 09, 9
        "Function_10_1CFE",        # 0A, 10
        "Function_11_1D1A",        # 0B, 11
        "Function_12_1D36",        # 0C, 12
        "Function_13_1D52",        # 0D, 13
        "Function_14_2248",        # 0E, 14
        "Function_15_23DD",        # 0F, 15
        "Function_16_2524",        # 10, 16
        "Function_17_281B",        # 11, 17
        "Function_18_283A",        # 12, 18
        "Function_19_2A7D",        # 13, 19
        "Function_20_2E00",        # 14, 20
        "Function_21_3307",        # 15, 21
        "Function_22_74E3",        # 16, 22
        "Function_23_7534",        # 17, 23
        "Function_24_759D",        # 18, 24
        "Function_25_75FF",        # 19, 25
        "Function_26_7661",        # 1A, 26
        "Function_27_76B6",        # 1B, 27
        "Function_28_770B",        # 1C, 28
        "Function_29_7760",        # 1D, 29
        "Function_30_77D3",        # 1E, 30
        "Function_31_780D",        # 1F, 31
        "Function_32_7847",        # 20, 32
        "Function_33_789F",        # 21, 33
        "Function_34_78F7",        # 22, 34
        "Function_35_7931",        # 23, 35
        "Function_36_7950",        # 24, 36
        "Function_37_7990",        # 25, 37
        "Function_38_79D0",        # 26, 38
        "Function_39_7A4C",        # 27, 39
        "Function_40_7A93",        # 28, 40
        "Function_41_7B16",        # 29, 41
        "Function_42_7B38",        # 2A, 42
        "Function_43_7B7C",        # 2B, 43
        "Function_44_7BC0",        # 2C, 44
        "Function_45_7BE3",        # 2D, 45
        "Function_46_7C06",        # 2E, 46
        "Function_47_7CBC",        # 2F, 47
        "Function_48_7D1D",        # 30, 48
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_165F")
    Sound(14, 0, 100, 0)
    OP_74(0x14, 0x1E)
    OP_71(0x14, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_158D")
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
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_156E"),
        (2, "loc_157D"),
        (1, "loc_158A"),
        (SWITCH_DEFAULT, "loc_158D"),
    )


    label("loc_156E")

    SetScenarioFlags(0x216, 7)
    OP_70(0x14, 0x1E)
    Sleep(500)
    Jump("loc_158D")

    label("loc_157D")

    OP_70(0x14, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_158A")

    OP_B9(0x0)
    Return()

    label("loc_158D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x50, 1)"), scpexpr(EXPR_END)), "loc_15EA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_165A")

    label("loc_15EA")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x50),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x14, 0x1E, 0x0, 0x0, 0x0)

    label("loc_165A")

    Jump("loc_1699")

    label("loc_165F")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_1699")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_148E end

    def Function_5_16A5(): pass

    label("Function_5_16A5")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17D5")
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
            "#56I地のセピス×６０\x01\x07\x02",

            "#57I水のセピス×６０\x01\x07\x02",

            "#58I火のセピス×６０\x01\x07\x02",

            "#59I風のセピス×６０\x01\x07\x02",

            "#60I時のセピス×６０\x01\x07\x02",

            "#61I空のセピス×６０\x01\x07\x02",

            "#62I幻のセピス×６０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1EF, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_17FA")

    label("loc_17D5")


    #A0006
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

    label("loc_17FA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_16A5 end

    def Function_6_180C(): pass

    label("Function_6_180C")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_190C")
    Sound(14, 0, 100, 0)
    OP_74(0x16, 0x1E)
    OP_71(0x16, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_1895")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1907")

    label("loc_1895")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x16, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1907")

    Jump("loc_1951")

    label("loc_190C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_1951")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_180C end

    def Function_7_195D(): pass

    label("Function_7_195D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EF, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B2E")
    Sound(14, 0, 100, 0)
    OP_74(0x17, 0x1E)
    OP_71(0x17, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5C")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_19BA():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_19BA)

    def lambda_19D4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_19D4)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_1A3D"),
        (2, "loc_1A4C"),
        (1, "loc_1A59"),
        (SWITCH_DEFAULT, "loc_1A5C"),
    )


    label("loc_1A3D")

    SetScenarioFlags(0x217, 0)
    OP_70(0x17, 0x1E)
    Sleep(500)
    Jump("loc_1A5C")

    label("loc_1A4C")

    OP_70(0x17, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1A59")

    OP_B9(0x0)
    Return()

    label("loc_1A5C")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xAF, 1)"), scpexpr(EXPR_END)), "loc_1AB9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EF, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1B29")

    label("loc_1AB9")

    FadeToDark(300, 0, 100)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xAF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x17, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B29")

    Jump("loc_1B68")

    label("loc_1B2E")

    FadeToDark(300, 0, 100)

    #A0013
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

    label("loc_1B68")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_195D end

    def Function_8_1B74(): pass

    label("Function_8_1B74")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "中に踏み込む\x01",        # 0
            "その場を離れる\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BCC"),
        (1, "loc_1BE9"),
        (SWITCH_DEFAULT, "loc_1BEE"),
    )


    label("loc_1BCC")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapObjFlags(0x13, 0x10)
    OP_65(0x0, 0x1)
    Call(0, 21)
    Jump("loc_1BEE")

    label("loc_1BE9")

    Jump("loc_1BEE")

    label("loc_1BEE")

    SetChrPos(0x0, 500000, 0, 205800, 180)
    EventEnd(0x5)
    Return()

    # Function_8_1B74 end

    def Function_9_1C02(): pass

    label("Function_9_1C02")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0014
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CEF")
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

    label("loc_1CEF")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_9_1C02 end

    def Function_10_1CFE(): pass

    label("Function_10_1CFE")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_1CFE end

    def Function_11_1D1A(): pass

    label("Function_11_1D1A")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_1D1A end

    def Function_12_1D36(): pass

    label("Function_12_1D36")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 13)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_12_1D36 end

    def Function_13_1D52(): pass

    label("Function_13_1D52")


    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "水位調整用の制御装置がある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2247")
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E3E")
    SetChrPos(0x0, 107620, -6000, 200, 0)
    SetChrPos(0x1, 108620, -6000, -600, 0)
    SetChrPos(0x2, 106620, -6000, -600, 0)
    SetChrPos(0x3, 107620, -6000, -1900, 0)
    OP_68(107660, -5000, 850, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28500, 0)
    Jump("loc_1F45")

    label("loc_1E3E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1EC4")
    SetChrPos(0x0, 85000, -6000, 101000, 0)
    SetChrPos(0x1, 83800, -6000, 101000, 0)
    SetChrPos(0x2, 83800, -6000, 99800, 0)
    SetChrPos(0x3, 85000, -6000, 99800, 0)
    OP_68(84580, -5000, 101000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(27000, 0)
    Jump("loc_1F45")

    label("loc_1EC4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F45")
    SetChrPos(0x0, 201500, -6000, 184000, 90)
    SetChrPos(0x1, 200000, -6000, 185000, 90)
    SetChrPos(0x2, 200000, -6000, 183000, 90)
    SetChrPos(0x3, 198500, -6000, 184000, 90)
    OP_68(201500, -5000, 184020, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(33500, 0)

    label("loc_1F45")

    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 0)), scpexpr(EXPR_END)), "loc_20D0")
    SetMapObjFrame(0xE, "m01gim01", 0x2, "off")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "off")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "off")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FE9")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_2068")

    label("loc_1FE9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_202B")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_2068")

    label("loc_202B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2068")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_2068")

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
    Jump("loc_2247")

    label("loc_20D0")

    SetMapObjFrame(0xE, "m01gim01", 0x2, "on")
    SetMapObjFrame(0xF, "m01gim01", 0x2, "on")
    SetMapObjFrame(0x10, "m01gim01", 0x2, "on")
    Sound(138, 0, 100, 0)
    Sleep(1200)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    Fade(500)
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2167")
    OP_68(102040, -5000, 230, 0)
    MoveCamera(45, 43, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(38000, 0)
    Jump("loc_21E6")

    label("loc_2167")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21A9")
    OP_68(99810, -6000, 100090, 0)
    MoveCamera(45, 45, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(48000, 0)
    Jump("loc_21E6")

    label("loc_21A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E6")
    OP_68(200130, -9000, 198310, 0)
    MoveCamera(45, 42, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(42500, 0)

    label("loc_21E6")

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

    label("loc_2247")

    Return()

    # Function_13_1D52 end

    def Function_14_2248(): pass

    label("Function_14_2248")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    SoundLoad(144)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "エレベーターの制御パネルがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23D5")
    Fade(500)
    SetChrPos(0x0, 600, 0, 600, 90)
    SetChrPos(0x1, 600, 0, -600, 90)
    SetChrPos(0x2, -600, 0, -600, 90)
    SetChrPos(0x3, -600, 0, 600, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2335")
    SetChrPos(0x4, -1800, 0, -600, 90)
    SetChrPos(0x5, -1800, 0, 600, 90)
    Jump("loc_2354")

    label("loc_2335")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2354")
    SetChrPos(0x4, -1800, 0, 0, 90)

    label("loc_2354")

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

    label("loc_23D5")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_14_2248 end

    def Function_15_23DD(): pass

    label("Function_15_23DD")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xF), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24B0")
    OP_90(0x4, -1800, 0, -600, 90)
    OP_90(0x5, -1800, 0, 600, 90)
    Jump("loc_24CF")

    label("loc_24B0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_24CF")
    OP_90(0x4, -1800, 0, 0, 90)

    label("loc_24CF")

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

    # Function_15_23DD end

    def Function_16_2524(): pass

    label("Function_16_2524")

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
    SetChrName("少年の声")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            "#3706V#30W──ウフフ、なるほど。\x02\x03",

            "#3707Vなかなかどうして\x01",
            "使いやすい端末じゃないか。\x02",
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
            "財団きっての天才ＳＥ、\x01",
            "ヨナ・セイクリッド少年か。\x02\x03",

            "旧式のネットワークとはいえ\x01",
            "ここまでの環境を構築するとはね。\x02\x03",

            "レンが捕捉されたっていうのも\x01",
            "あながちマグレじゃなさそうだな。\x02",
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

    # Function_16_2524 end

    def Function_17_281B(): pass

    label("Function_17_281B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2839")
    SetChrSubChip(0x8, 0x0)
    Sleep(200)
    SetChrSubChip(0x8, 0x1)
    Sleep(200)
    Jump("Function_17_281B")

    label("loc_2839")

    Return()

    # Function_17_281B end

    def Function_18_283A(): pass

    label("Function_18_283A")

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
            "#6P#04805Fおっと……\x01",
            "こっちで踏んじゃったか。\x02",
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
            "#6P#04802Fウフフ……\x01",
            "やるねえ、ソバカス君。\x02\x03",

            "でも、この仕掛けだと\x01",
            "明日くらいまでバレないかな？\x02\x03",

            "#04809Fせっかくだから色々、\x01",
            "愉しませてもらおうっと㈱\x02",
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

    # Function_18_283A end

    def Function_19_2A7D(): pass

    label("Function_19_2A7D")

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
    SetChrName("少年の声")

    #A0021
    AnonymousTalk(
        0xFF,
        (
            "#3708V#40Wかくして運命の塔は顕れ、\x01",
            "数多の因縁を巻き込みながら\x01",
            "螺旋を描いてゆく──\x02",
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
            "#12P#04804Fフフ、ブルブランが\x01",
            "いかにも好きそうな場面#4Rシーン#だな。\x02\x03",

            "#04800Fまあこれだけのイベント、\x01",
            "彼なら勝手に見に来てそうだけど。\x02",
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
        "#12P#04805Fおっと、来た来た。\x02",
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(500)

    #A0024
    AnonymousTalk(
        0x8,
        (
            "#04802Fウフフ……\x01",
            "あとは“彼ら”に渡すだけか。\x02\x03",

            "#04809Fそれじゃあ、せっかくだから\x01",
            "お愉しみの準備もしとこうかな㈱\x02",
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

    # Function_19_2A7D end

    def Function_20_2E00(): pass

    label("Function_20_2E00")

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
        "#00011F#6P（この曲は……）\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    def lambda_2F66():
        OP_97(0x101, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F66)
    Sleep(100)

    def lambda_2F83():
        OP_97(0x102, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F83)
    Sleep(100)

    def lambda_2FA0():
        OP_97(0x104, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2FA0)
    Sleep(100)

    def lambda_2FBD():
        OP_97(0x109, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2FBD)
    Sleep(100)

    def lambda_2FDA():
        OP_97(0x10A, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_2FDA)
    Sleep(100)

    def lambda_2FF7():
        OP_97(0x105, 0x2710, 0x0, 0x5DC, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2FF7)
    Sleep(2000)
    Fade(500)
    OP_68(500000, 1100, 204000, 0)
    MoveCamera(35, 21, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20000, 0)
    WaitChrThread(0x101, 0)

    def lambda_304B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_304B)
    WaitChrThread(0x102, 0)

    def lambda_305C():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_305C)
    WaitChrThread(0x104, 0)

    def lambda_306D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_306D)
    WaitChrThread(0x109, 0)

    def lambda_307E():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_307E)
    WaitChrThread(0x10A, 0)

    def lambda_308F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_308F)
    WaitChrThread(0x105, 0)

    def lambda_30A0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_30A0)
    Sleep(500)

    #C0026
    ChrTalk(
        0x102,
        (
            "#12P#00108F（ヨナ君の部屋にかかっていた\x01",
            "  導力ステレオの曲……？）\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x104,
        (
            "#00301F（なんだ……？\x01",
            "  故障でもしてんのか。）\x02",
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
            "#6P#00603F（罠かもしれん……\x01",
            "  念のため慎重に踏み込むぞ。）\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 500)
    Sleep(200)

    #C0029
    ChrTalk(
        0x10A,
        (
            "#6P#00601F（バニングス、オルランド。\x01",
            "  まずは３人がかりで突入する。）\x02\x03",

            "（他の３人は後ろから\x01",
            "  フォローしつつ入って来い。）\x02",
        )
    )

    CloseMessageWindow()

    def lambda_320F():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_320F)
    Sleep(50)

    def lambda_321F():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_321F)
    Sleep(50)

    def lambda_322F():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_322F)
    Sleep(50)

    def lambda_323F():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_323F)
    Sleep(50)

    def lambda_324F():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_324F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0030
    ChrTalk(
        0x101,
        "#00013F#11P（了解です。）\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x104,
        "#00301F#11P（アイサー。）\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x109,
        "#12P#10101F（承知しました！）\x02",
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

    # Function_20_2E00 end

    def Function_21_3307(): pass

    label("Function_21_3307")

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

    def lambda_3575():
        OP_95(0xFE, 500000, 150, 207400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3575)
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

    def lambda_35DF():
        OP_95(0xFE, 500000, 150, 210400, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_35DF)
    Sleep(100)
    BeginChrThread(0x101, 3, 0, 22)
    Sleep(200)

    def lambda_3605():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_3605)
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
        "#12P#00008F誰もいない……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#00301F#5P隠れてる気配もねぇな……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x10A,
        (
            "#5P#00606F#11P……逃げられたか。\x02\x03",

            "#00600Fしかしここに来るまでの間、\x01",
            "誰ともすれ違わなかったが……\x02",
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
        "#12P#00108Fに、逃げられたの？\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    def lambda_38C2():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_38C2)
    Sleep(50)

    def lambda_38D2():
        OP_93(0x104, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_38D2)
    Sleep(50)

    def lambda_38E2():
        OP_93(0x10A, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_38E2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x10A, 0)

    #C0037
    ChrTalk(
        0x101,
        "#00006F#5Pああ、どうやらそうらしい。\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(300)

    #C0038
    ChrTalk(
        0x101,
        (
            "#00001F#6Pこの音楽は……\x01",
            "そっちの装置みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3969():
        OP_92(0x101, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3969)
    Sleep(50)

    def lambda_397F():
        OP_92(0x102, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_397F)
    Sleep(50)

    def lambda_3995():
        OP_92(0x105, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3995)
    Sleep(50)

    def lambda_39AB():
        OP_92(0x10A, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_39AB)
    Sleep(50)

    def lambda_39C1():
        OP_92(0x109, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_39C1)
    Sleep(50)

    def lambda_39D7():
        OP_92(0x104, 0x7B2B4, 0x4824C, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_39D7)
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
            "#6P#00601Fさすがにうるさいな……\x01",
            "停止させられるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#00301F#6Pああ……\x01",
            "こいつがスイッチだな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3A6A():
        OP_96(0xFE, 0x7AF94, 0x0, 0x4824C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3A6A)
    WaitChrThread(0x104, 1)
    Sleep(150)
    Sound(853, 0, 100, 0)
    SetMapObjFlags(0x1E, 0x4)
    StopBGM(0x1F4)
    Sleep(1000)

    #C0041
    ChrTalk(
        0x109,
        "#12P#10108F何だか不気味ですね……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        (
            "#6P#00106Fそ、そうね……\x01",
            "音楽が鳴っていたのも\x01",
            "不自然だし……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        (
            "#12P#10308Fフム、そこはかとなく\x01",
            "悪意を感じるけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(150)

    #C0044
    ChrTalk(
        0x105,
        (
            "#12P#10305Fとりあえず、奥のモニターに\x01",
            "映っているのはなんだい？\x02",
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

    def lambda_3C0F():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C0F)
    Sleep(50)

    def lambda_3C1F():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3C1F)
    Sleep(50)

    def lambda_3C2F():
        OP_93(0x10A, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3C2F)
    Sleep(50)

    def lambda_3C3F():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3C3F)
    Sleep(50)

    def lambda_3C4F():
        OP_93(0x104, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_3C4F)
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
        "#00005F#N#12P図面……\x02",
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
        "#11P#00011Fこ、これは……！\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)

    #A0047
    AnonymousTalk(
        0x102,
        (
            "#00105Fこ、これって……\x01",
            "まさかオルキスタワーの！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0048
    AnonymousTalk(
        0x109,
        (
            "#10101Fタワー内部の構成図が\x01",
            "記されたデータみたいですけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0049
    AnonymousTalk(
        0x10A,
        (
            "#00610Fクッ、どうしてそんなものが\x01",
            "こんな場所に──\x02",
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
        "#12P#10310Fしまった……！\x02",
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

    def lambda_3FCE():
        OP_93(0x102, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3FCE)
    Sleep(30)

    def lambda_3FDE():
        OP_93(0x10A, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3FDE)
    Sleep(30)

    def lambda_3FEE():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3FEE)
    Sleep(30)

    def lambda_3FFE():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3FFE)
    Sleep(30)

    def lambda_400E():
        OP_93(0x109, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_400E)
    Sleep(30)

    def lambda_401E():
        OP_93(0x104, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_401E)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x104, 0)

    #C0052
    ChrTalk(
        0x102,
        "#00101F#6P#Nっ！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0053
    ChrTalk(
        0x10A,
        "#00610F#6Pチッ、罠か！？\x02",
    )

    CloseMessageWindow()
    OP_68(505950, 900, 400300, 1500)
    MoveCamera(50, 17, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(21500, 1500)

    def lambda_40A8():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_40A8)
    Sleep(300)

    def lambda_40C5():
        OP_95(0xFE, 502700, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_40C5)
    WaitChrThread(0x105, 1)

    def lambda_40E3():
        OP_95(0xFE, 508400, 0, 400700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_40E3)
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
            "#10110F#6Pだ、駄目です！\x01",
            "ビクとも開きません！\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x105,
        (
            "#6P#10308F#5Pどうやら導力的な機構で\x01",
            "ロックされたみたいだね。\x02",
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

    def lambda_42E1():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_42E1)

    def lambda_42EE():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_42EE)
    Sleep(500)

    #C0056
    ChrTalk(
        0x101,
        "#5P#00010F今のは……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x104,
        "#5P#00307Fおい、誰だ……！？\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(200, 20, -1, -1)
    SetChrName("声")

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3709V#30Wウフフ……\x01",
            "初めまして、支援課の諸君。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(160, 100, -1, -1)
    SetChrName("声")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3710V#30W予想通り君たちが\x01",
            "遊びに来てくれたみたいだね。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(30, 50, -1, -1)
    SetChrName("声")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3711V#30Wお近づきの印に\x01",
            "置き土産を置いていくから\x01",
            "愉しんでくれると嬉しいな㈱\x07\x00\x02",
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
        "#5P#00011Fなっ……\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x0, 0x1F4)
    Sleep(150)

    #C0062
    ChrTalk(
        0x10A,
        "#00607F#11Pクッ、端末から喋ってるのか？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(498200, 1300, 302300, 2000)
    MoveCamera(33, 17, 0, 2000)
    SetCameraDistance(20500, 2000)

    def lambda_44C8():
        OP_95(0xFE, 499500, 0, 298400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_44C8)

    def lambda_44E2():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_44E2)
    Sleep(30)

    def lambda_44F2():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_44F2)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    def lambda_450A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_450A)
    Sleep(30)

    def lambda_451A():
        OP_95(0xFE, 499200, 0, 299300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_451A)
    WaitChrThread(0x105, 1)

    def lambda_4538():
        OP_95(0xFE, 498100, 0, 299300, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_4538)
    WaitChrThread(0x105, 1)

    def lambda_4556():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_4556)
    WaitChrThread(0x109, 1)

    def lambda_4567():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_4567)
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
        "#10105Fこ、これは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0064
    AnonymousTalk(
        0x102,
        (
            "#00101Fロバーツ主任から渡された\x01",
            "対戦パズルゲーム……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(230, 60, -1, -1)
    SetChrName("声")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "３本勝負で２本取ったら\x01",
            "君たちを解放してあげるよ。\x02\x03",

            "ただし、負けちゃった場合は\x01",
            "丸焦げになってもらおうかな？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #A0066
    AnonymousTalk(
        0x101,
        "#00010Fなに……！？\x02",
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

    def lambda_482A():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_482A)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4852():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_4852)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_4877():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4877)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_489F():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_489F)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_48C4():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_48C4)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_48EC():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_48EC)
    Sleep(1000)
    OP_6F(0x79)

    #C0067
    ChrTalk(
        0x109,
        "#6P#10111Fな……！\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x104,
        (
            "#5P#00307F馬鹿な……！\x01",
            "仕掛けの気配は無かったぞ！？\x02",
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
    SetChrName("声")

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "ウフフ、それじゃあ\x01",
            "始めるとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "あまり時間はない……\x01",
            "急がないと死んじゃうよ？\x07\x00\x02",
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
        "#00610F貴様……！\x02",
    )

    CloseMessageWindow()

    def lambda_4A21():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_4A21)

    def lambda_4A2E():
        OP_93(0x105, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_4A2E)
    Sleep(30)

    def lambda_4A3E():
        OP_93(0x109, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_4A3E)
    Sleep(30)

    def lambda_4A4E():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A4E)
    Sleep(30)

    def lambda_4A5E():
        OP_93(0x102, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4A5E)
    Sleep(30)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)

    #C0072
    ChrTalk(
        0x105,
        (
            "#12P#10307Fロイド！\x01",
            "とにかくやるしかない！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#11P#00010Fクッ──分かった！\x02",
    )

    CloseMessageWindow()
    StopSound(868, 1000, 40)
    StopSound(825, 1000, 40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_70(0x20, 0x33)
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "MiniGame(0x10, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4B44")
    SetScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B3A")
    OP_2C(0xA3, 0x1)
    Jump("loc_4B3F")

    label("loc_4B3A")

    OP_2C(0xA3, 0x2)

    label("loc_4B3F")

    Jump("loc_4B47")

    label("loc_4B44")

    ClearScenarioFlags(0x0, 1)

    label("loc_4B47")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_4E3B")

    #C0074
    ChrTalk(
        0x101,
        "#11P#00000Fよしっ！\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x102,
        "#12P#00102Fロイド、凄い！\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x104,
        "#00309Fやるじゃねえか！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "うーん。\x01",
            "手を抜きすぎたかな？\x02\x03",

            "それじゃあ次は本気を──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4EEE")

    label("loc_4E3B")


    #C0078
    ChrTalk(
        0x101,
        "#11P#00010F……くっ………\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        "#10106F#12Pああっ……\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x105,
        (
            "#12P#10306Fうーん。\x01",
            "惜しかったけど……\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声")

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "アハハ！\x01",
            "後が無くなったねぇ。\x02\x03",

            "それじゃあ止めを──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_4EEE")

    StopBGM(0x7D0)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("少女の声")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2669V#30W──いい加減にしてください。\x07\x00\x02",
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
    SetChrName("声")

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
        "#12P#00105Fあ……！\x02",
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#11P#00005Fこの声は……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("少女の声")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2670V#30Wここから先は\x01",
            "わたしがお相手します。\x02",
        )
    )

    CloseMessageWindow()

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2671V#30W──覚悟してください。\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_52C0")
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 496500, 500, 292600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502300, 2000, 292100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 493200, 2000, 299500, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 504000, 1500, 298100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 502000, 2500, 301100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 498500, 2000, 401200, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 501700, 1500, 404100, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507700, 1000, 402700, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)
    PlayEffect(0x4, 0xFF, 0xFF, 0x0, 507200, 500, 396600, 0, 0, 0, 1200, 1200, 1200, 0xFF, 0, 0, 0, 1000)

    label("loc_52C0")

    FadeToBright(0, -1)
    SetCameraDistance(20500, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55FD")
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声")

    #A0088
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3712V#30Wへえ……！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xE80)
    SetMessageWindowPos(150, 20, -1, -1)
    SetChrName("少女の声")

    #A0089
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2672V#30W続けて行きます。\x07\x00\x02",
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

    label("loc_55FD")

    StopBGM(0xFA0)

    #C0090
    ChrTalk(
        0x101,
        "#11P#00002Fや、やった……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x104, 0x2D, 0x1F4)
    Sleep(100)

    #C0091
    ChrTalk(
        0x104,
        (
            "#00310F#5Pくっ……\x01",
            "そろそろヤベエぞ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(80, 30, -1, -1)
    SetChrName("声")

    #A0092
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3713V#30Wウフフ、お見事。\x02",
        )
    )

    CloseMessageWindow()

    #A0093
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3714V#30W一応、お仲間みたいだし\x01",
            "約束どおり出してあげるよ。\x02",
        )
    )

    CloseMessageWindow()

    #A0094
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#3715V#30W──それじゃあ、またね㈱\x07\x00\x02",
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

    def lambda_581A():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_581A)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_583F():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_583F)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_5867():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_5867)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_588C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_588C)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_58B4():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_58B4)
    Sleep(1000)

    #C0095
    ChrTalk(
        0x109,
        "#10107F#5P開いた……！\x02",
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x10A,
        "#00610F#5P急げ、爆発するぞ！\x02",
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
        "#6P#00007F#Nはいっ！\x02",
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
        "#12A#00607F#3453V#12P#N#4S伏せろっ！\x02",
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

    def lambda_5C69():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5C69)
    WaitChrThread(0x101, 2)
    Sleep(500)

    #C0099
    ChrTalk(
        0x101,
        "#5P#00006F#40Wはあはあ……\x02",
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0x104,
        "#00306F#40W#11Pったく、危機一髪だな……\x02",
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x109,
        "#10106F#40W#11Pし、死ぬかと思いました……\x02",
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x10A,
        (
            "#00610F#40W#11Pクッ……\x01",
            "一体何者だ……！？\x02",
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
        "少女の声",
        (
            "#2673V#30W──よかった。\x01",
            "ご無事みたいですね。\x02",
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

    def lambda_5F97():
        OP_96(0xFE, 0x7AA1C, 0x0, 0x7A508, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5F97)
    OP_0D()
    WaitChrThread(0x9, 1)
    TurnDirection(0x9, 0x104, 500)

    #C0104
    ChrTalk(
        0x101,
        "#12P#00002Fティオ！\x02",
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x102,
        (
            "#00102Fや、やっぱり\x01",
            "ティオちゃんだったの！\x02",
        )
    )

    CloseMessageWindow()

    #C0106
    ChrTalk(
        0x104,
        (
            "#6P#00302Fおいおい！\x01",
            "一体どうなってんだ！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2276, 255, 80, 0)    #voice#Tio
    Sleep(800)

    def lambda_6043():
        OP_95(0xFE, 502500, 0, 500400, 1500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6043)
    WaitChrThread(0x9, 1)

    def lambda_6061():
        OP_A6(0xFE, 0x0, 0x1E, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_6061)
    Sleep(300)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    def lambda_6091():
        OP_96(0xFE, 0x7AA1C, 0x0, 0x7A508, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_6091)
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
            "──実は今日の午後、\x01",
            "クロスベル行きの\x01",
            "国際定期船に乗ったんです。\x02\x03",

            "色々、大変そうだったので\x01",
            "何とか帰国を早めてもらいました。\x02",
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
        "#12P#00000Fそうだったのか……\x02",
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
            "#6P#00309Fハハ……\x01",
            "まさにドンピシャじゃねえか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0110
    ChrTalk(
        0x105,
        (
            "#12P#N#10302Fじゃあ、課長さんから\x01",
            "話を聞いてここに来たんだ？\x02",
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
            "#00204Fええ、エニグマで連絡したら\x01",
            "こちらに向かったと聞いたので。\x02\x03",

            "#00202Fそれで空港から直接来ました。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x102,
        (
            "#00104Fふふ……\x01",
            "本当に助かっちゃったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0x109,
        "#6P#N#10109Fありがとう、ティオちゃん！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0114
    ChrTalk(
        0x9,
        "#00204F#5Pいえ、間に合って良かったです。\x02",
    )

    CloseMessageWindow()
    OP_93(0x9, 0x5A, 0x1F4)
    Sleep(300)

    #C0115
    ChrTalk(
        0x9,
        (
            "#00201F#5P……それにしても\x01",
            "厄介な相手だったみたいですね。\x02\x03",

            "何とか割り込みをかけて\x01",
            "撃退することができましたが……\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0x101,
        "#12P#00005F割り込みって──ああ、それか。\x02",
    )

    CloseMessageWindow()
    OP_68(502700, 500, 508900, 2000)
    OP_93(0x9, 0x0, 0x190)
    OP_6F(0x79)

    #C0117
    ChrTalk(
        0x9,
        (
            "#12P#N#00202Fええ、ロイドさんたちが\x01",
            "閉じ込められたと分かったので\x01",
            "予備回線から介入しました。\x02\x03",

            "#00206Fどうやら相当な腕前の\x01",
            "ハッカーだったようですね。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0118
    ChrTalk(
        0x101,
        "#00006F#12P#Nああ、そうみたいだな。\x02",
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
            "#6P#00601Fフン、どうやらとっくに\x01",
            "離脱されてしまったようだが……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0120
    ChrTalk(
        0x10A,
        (
            "#6P#00605Fそういえば、プラトー。\x02\x03",

            "一人でジオフロントを\x01",
            "ここまで追って来たのか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x10A, 500)
    Sleep(150)

    #C0121
    ChrTalk(
        0x9,
        (
            "#11P#00205Fあ、いえ。\x02\x03",

            "#00203F……たまたま居合わせたので\x01",
            "ここまで同行してもらいました。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)

    #C0122
    ChrTalk(
        0x101,
        "#12P#00005Fへ……\x02",
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
        "声",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#N──とんだ場面に\x01",
            "居合わせたようだな。\x07\x00\x02",
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

    def lambda_67B6():
        OP_96(0xFE, 0x7A120, 0x0, 0x7B0C0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_67B6)

    def lambda_67D0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_67D0)

    def lambda_67E1():

        label("loc_67E1")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_67E1")

    QueueWorkItem2(0x101, 2, lambda_67E1)

    def lambda_67F3():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_67F3)

    def lambda_6800():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_6800)

    def lambda_680D():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_680D)

    def lambda_681A():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_681A)

    def lambda_6827():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x10A, 2, lambda_6827)

    def lambda_6834():

        label("loc_6834")

        TurnDirection(0xFE, 0xA, 500)
        Yield()
        Jump("loc_6834")

    QueueWorkItem2(0x9, 2, lambda_6834)
    WaitChrThread(0xA, 1)
    EndChrThread(0x101, 0x2)
    EndChrThread(0x9, 0x2)
    OP_6F(0x79)

    #C0124
    ChrTalk(
        0x101,
        "#00007Fあんたは……！\x02",
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x109,
        "#12P#10107Fあ、あの時の……！\x02",
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x102,
        "#12P#00101F《銀#2Rイン#》……！\x02",
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
            "……取り逃がしたか。\x02\x03",

            "どこのネズミかは知らんが\x01",
            "相当、抜け目がないようだな。\x07\x00\x02",
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
            "#00006Fちょ、ちょっと待ってくれ！\x02\x03",

            "#00013Fここにいたハッカーは\x01",
            "《黒月》の関係者なのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00700Fいや、縁もゆかりもない者だ。\x02\x03",

            "おそらく《赤い星座》とも\x01",
            "関係があるわけではないだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x101,
        "#00005Fなに……！？\x02",
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x104,
        (
            "#12P#00301Fなんでアンタに\x01",
            "そんなことが判るってんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702Fフフ、《黒月》と《赤い星座》は\x01",
            "既にお互い監視体制に入っている。\x02\x03",

            "少なくとも、そのハッカーとやらは\x01",
            "どちらにも属していないはずだ。\x02\x03",

            "#00700F──どうやら通商会議に\x01",
            "何か思惑がある者のようだが。\x07\x00\x02",
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
            "#12P#00108F端末に映っていた\x01",
            "オルキスタワーの図面……\x02",
        )
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x105,
        (
            "#12P#10303Fなるほど……\x01",
            "まさに明日の会議の場所だね。\x02",
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

    def lambda_6C5C():
        OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_6C5C)
    WaitChrThread(0x10A, 1)
    Sleep(300)

    #C0137
    ChrTalk(
        0x10A,
        (
            "#12P#00603F──会うのはこれが初めてか。\x02\x03",

            "#00600Fクロスベル警察、捜査一課、\x01",
            "アレックス・ダドリーだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0138
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702Fフフ……噂はかねがね。\x02\x03",

            "通商会議の警備では\x01",
            "色々苦労しているようだな？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x10A,
        (
            "#12P#00604Fフン、どこぞの組織を始め、\x01",
            "怪しげな連中が跋扈#4Rばっこ#しているのでな。\x02\x03",

            "どうやらこちらの知らない動きに\x01",
            "色々と通じているようだし……\x02",
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
            "#12P#00601Fここは一つ、警察までご同行願って\x01",
            "話を聞かせてもらおうか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_6E33():
        TurnDirection(0x101, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_6E33)
    Sleep(50)

    def lambda_6E43():
        TurnDirection(0x104, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_6E43)
    Sleep(50)

    def lambda_6E53():
        TurnDirection(0x102, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_6E53)
    Sleep(50)

    def lambda_6E63():
        TurnDirection(0x9, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_6E63)
    Sleep(50)

    def lambda_6E73():
        TurnDirection(0x109, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_6E73)
    Sleep(50)

    def lambda_6E83():
        TurnDirection(0x105, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_6E83)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x9, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    def lambda_6EA8():

        label("loc_6EA8")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6EA8")

    QueueWorkItem2(0x101, 2, lambda_6EA8)

    def lambda_6EBA():

        label("loc_6EBA")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6EBA")

    QueueWorkItem2(0x102, 2, lambda_6EBA)

    def lambda_6ECC():

        label("loc_6ECC")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6ECC")

    QueueWorkItem2(0x9, 2, lambda_6ECC)

    def lambda_6EDE():

        label("loc_6EDE")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6EDE")

    QueueWorkItem2(0x109, 2, lambda_6EDE)

    def lambda_6EF0():

        label("loc_6EF0")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6EF0")

    QueueWorkItem2(0x105, 2, lambda_6EF0)

    def lambda_6F02():

        label("loc_6F02")

        TurnDirection(0xFE, 0x10A, 500)
        Yield()
        Jump("loc_6F02")

    QueueWorkItem2(0x104, 2, lambda_6F02)

    #C0141
    ChrTalk(
        0x101,
        "#00011Fダドリーさん……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x104,
        "#00305Fおいおい……マジかよ？\x02",
    )

    CloseMessageWindow()

    #C0143
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#5P#00702Fフフ、何の容疑で？\x02\x03",

            "クロスベルの刑事法に\x01",
            "抵触した覚えは無いのだが。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0144
    ChrTalk(
        0x10A,
        (
            "#12P#00602Fなに、任意の事情聴取だ。\x02\x03",

            "#00607F後ろめたい事がないなら\x01",
            "ぜひ来ていただこうか──！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(341, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xA, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    def lambda_704E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_704E)
    ClearChrFlags(0xB, 0x80)

    def lambda_7064():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_7064)
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

    def lambda_70C9():
        OP_96(0xFE, 0x7A4A4, 0x0, 0x7B700, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_70C9)
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
        "#11P#00603Fフン……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0146
    ChrTalk(
        0x9,
        "#00205F……いつの間に。\x02",
    )

    CloseMessageWindow()

    #C0147
    ChrTalk(
        0x105,
        (
            "#10302F#12P#Nへえ、符術を使った\x01",
            "分け身ってやつか。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)
    Sound(2628, 255, 100, 0)    #voice#Yin
    Sleep(800)
    SetMessageWindowPos(15, 10, -1, -1)
    SetChrName("銀の声")

    #A0148
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#40W……今宵はこれでさらばだ。\x02\x03",

            "#30Wまた近いうちに\x01",
            "会えそうな気もするがな。\x07\x00\x02",
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
            "#5P#00201F……ロイドさん。\x01",
            "付近をサーチしますか？\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x101,
        (
            "#11P#00006Fいや……その必要はないだろう。\x02\x03",

            "#00001Fとりあえず支援課に戻って\x01",
            "話し合う必要がありそうですね。\x02",
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
            "#5P#00606Fああ……\x01",
            "不本意だが仕方あるまい。\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x29, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_749E")
    AddCraft(0x2, 0x1AF)
    AddCraft(0x0, 0x1AF)
    Jump("loc_74BC")

    label("loc_749E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25, 4)), scpexpr(EXPR_END)), "loc_74B4")
    AddCraft(0x2, 0x19B)
    AddCraft(0x0, 0x19B)
    Jump("loc_74BC")

    label("loc_74B4")

    AddCraft(0x2, 0x187)
    AddCraft(0x0, 0x187)

    label("loc_74BC")

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

    # Function_21_3307 end

    def Function_22_74E3(): pass

    label("Function_22_74E3")


    def lambda_74E8():
        OP_96(0xFE, 0x7A120, 0x96, 0x32A28, 0x1388, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_74E8)
    WaitChrThread(0xFE, 1)

    def lambda_7506():
        OP_96(0xFE, 0x7A120, 0x96, 0x335E0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7506)
    Sleep(300)

    def lambda_7523():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7523)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_22_74E3 end

    def Function_23_7534(): pass

    label("Function_23_7534")


    def lambda_7539():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7539)

    def lambda_7553():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7553)
    WaitChrThread(0xFE, 1)

    def lambda_7568():
        OP_95(0xFE, 501000, 0, 296900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7568)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x3C, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x14A, 0x1F4)
    Sleep(1100)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_23_7534 end

    def Function_24_759D(): pass

    label("Function_24_759D")


    def lambda_75A2():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75A2)

    def lambda_75BC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_75BC)
    WaitChrThread(0xFE, 1)

    def lambda_75D1():
        OP_95(0xFE, 499700, 0, 295200, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_75D1)
    WaitChrThread(0xFE, 1)
    Sleep(500)
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x10E, 0x1F4)
    Return()

    # Function_24_759D end

    def Function_25_75FF(): pass

    label("Function_25_75FF")


    def lambda_7604():
        OP_95(0xFE, 499700, 0, 291400, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7604)

    def lambda_761E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_761E)
    WaitChrThread(0xFE, 1)

    def lambda_7633():
        OP_95(0xFE, 501700, 0, 294900, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7633)
    WaitChrThread(0xFE, 1)
    Sleep(300)
    OP_93(0xFE, 0x96, 0x1F4)
    Sleep(700)
    OP_93(0xFE, 0x3C, 0x1F4)
    Return()

    # Function_25_75FF end

    def Function_26_7661(): pass

    label("Function_26_7661")


    def lambda_7666():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7666)

    def lambda_7680():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_7680)
    WaitChrThread(0xFE, 1)

    def lambda_7695():
        OP_95(0xFE, 499300, 0, 293200, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7695)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_26_7661 end

    def Function_27_76B6(): pass

    label("Function_27_76B6")


    def lambda_76BB():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76BB)

    def lambda_76D5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_76D5)
    WaitChrThread(0xFE, 1)

    def lambda_76EA():
        OP_95(0xFE, 501800, 0, 293000, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_76EA)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_27_76B6 end

    def Function_28_770B(): pass

    label("Function_28_770B")


    def lambda_7710():
        OP_95(0xFE, 499700, 0, 291400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7710)

    def lambda_772A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_772A)
    WaitChrThread(0xFE, 1)

    def lambda_773F():
        OP_95(0xFE, 500300, 0, 292400, 3000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_773F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_28_770B end

    def Function_29_7760(): pass

    label("Function_29_7760")

    SetChrPos(0x101, 500300, 0, 296300, 0)

    def lambda_7776():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7776)
    WaitChrThread(0xFE, 1)

    def lambda_7794():
        OP_95(0xFE, 497200, 0, 299700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7794)
    WaitChrThread(0xFE, 1)

    def lambda_77B2():
        OP_95(0xFE, 497200, 200, 301200, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77B2)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_29_7760 end

    def Function_30_77D3(): pass

    label("Function_30_77D3")

    SetChrPos(0x10A, 501300, 200, 295600, 0)
    Sleep(700)

    def lambda_77EC():
        OP_95(0xFE, 498600, 200, 300600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_77EC)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_30_77D3 end

    def Function_31_780D(): pass

    label("Function_31_780D")

    SetChrPos(0x10A, 501300, 200, 294600, 0)
    Sleep(1800)

    def lambda_7826():
        OP_95(0xFE, 500200, 0, 300600, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7826)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x13B, 0x1F4)
    Return()

    # Function_31_780D end

    def Function_32_7847(): pass

    label("Function_32_7847")

    SetChrPos(0x102, 500300, 0, 295300, 0)
    Sleep(1300)

    def lambda_7860():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7860)
    WaitChrThread(0xFE, 1)

    def lambda_787E():
        OP_95(0xFE, 497100, 0, 299900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_787E)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_32_7847 end

    def Function_33_789F(): pass

    label("Function_33_789F")

    SetChrPos(0x105, 500300, 0, 294300, 0)
    Sleep(1900)

    def lambda_78B8():
        OP_95(0xFE, 499500, 0, 298400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78B8)
    WaitChrThread(0xFE, 1)

    def lambda_78D6():
        OP_95(0xFE, 498100, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_78D6)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_33_789F end

    def Function_34_78F7(): pass

    label("Function_34_78F7")

    SetChrPos(0x109, 500300, 0, 294300, 0)
    Sleep(2500)

    def lambda_7910():
        OP_95(0xFE, 499200, 0, 299300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7910)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_34_78F7 end

    def Function_35_7931(): pass

    label("Function_35_7931")


    def lambda_7936():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_7936)
    WaitChrThread(0x109, 1)
    Return()

    # Function_35_7931 end

    def Function_36_7950(): pass

    label("Function_36_7950")

    Sleep(300)

    def lambda_7958():
        OP_95(0xFE, 502700, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7958)
    WaitChrThread(0x105, 1)

    def lambda_7976():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_7976)
    WaitChrThread(0x105, 1)
    Return()

    # Function_36_7950 end

    def Function_37_7990(): pass

    label("Function_37_7990")

    Sleep(550)

    def lambda_7998():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_7998)
    WaitChrThread(0x104, 1)

    def lambda_79B6():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_79B6)
    WaitChrThread(0x104, 1)
    Return()

    # Function_37_7990 end

    def Function_38_79D0(): pass

    label("Function_38_79D0")

    Sleep(200)

    def lambda_79D8():
        OP_95(0xFE, 502500, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79D8)
    WaitChrThread(0xFE, 1)

    def lambda_79F6():
        OP_95(0xFE, 505900, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_79F6)
    WaitChrThread(0xFE, 1)

    def lambda_7A14():
        OP_95(0xFE, 509000, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A14)
    WaitChrThread(0xFE, 1)

    def lambda_7A32():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7A32)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_38_79D0 end

    def Function_39_7A4C(): pass

    label("Function_39_7A4C")

    OP_93(0x10A, 0x5A, 0x1F4)
    Sleep(900)

    def lambda_7A5B():
        OP_95(0xFE, 508900, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7A5B)
    WaitChrThread(0x10A, 1)

    def lambda_7A79():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_7A79)
    WaitChrThread(0x10A, 1)
    Return()

    # Function_39_7A4C end

    def Function_40_7A93(): pass

    label("Function_40_7A93")

    OP_93(0x101, 0x5A, 0x1F4)
    Sleep(850)

    def lambda_7AA2():
        OP_95(0xFE, 502500, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AA2)
    WaitChrThread(0xFE, 1)

    def lambda_7AC0():
        OP_95(0xFE, 505900, 0, 397400, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AC0)
    WaitChrThread(0xFE, 1)

    def lambda_7ADE():
        OP_95(0xFE, 509000, 0, 399700, 5000, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7ADE)
    WaitChrThread(0xFE, 1)

    def lambda_7AFC():
        OP_95(0xFE, 512900, 0, 399700, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7AFC)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_40_7A93 end

    def Function_41_7B16(): pass

    label("Function_41_7B16")

    Sleep(300)

    def lambda_7B1E():
        OP_95(0xFE, 500000, 0, 202400, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B1E)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_41_7B16 end

    def Function_42_7B38(): pass

    label("Function_42_7B38")


    def lambda_7B3D():
        OP_95(0xFE, 500000, 0, 203700, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B3D)
    WaitChrThread(0xFE, 1)

    def lambda_7B5B():
        OP_95(0xFE, 499400, 0, 200700, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B5B)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_42_7B38 end

    def Function_43_7B7C(): pass

    label("Function_43_7B7C")


    def lambda_7B81():
        OP_95(0xFE, 500000, 0, 204000, 4500, 0x1)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B81)
    WaitChrThread(0xFE, 1)

    def lambda_7B9F():
        OP_95(0xFE, 500400, 0, 200000, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_7B9F)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x0, 0x1F4)
    Return()

    # Function_43_7B7C end

    def Function_44_7BC0(): pass

    label("Function_44_7BC0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7BE2")
    Sound(840, 0, 100, 0)
    Sleep(1500)
    Sound(840, 0, 100, 0)
    Sleep(2000)
    Jump("Function_44_7BC0")

    label("loc_7BE2")

    Return()

    # Function_44_7BC0 end

    def Function_45_7BE3(): pass

    label("Function_45_7BE3")

    Sound(868, 2, 20, 0)
    Sound(825, 2, 20, 0)
    Sleep(200)
    OP_25(0x364, 0x1E)
    OP_25(0x339, 0x1E)
    Sleep(300)
    OP_25(0x364, 0x28)
    OP_25(0x339, 0x28)
    Return()

    # Function_45_7BE3 end

    def Function_46_7C06(): pass

    label("Function_46_7C06")

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

    # Function_46_7C06 end

    def Function_47_7CBC(): pass

    label("Function_47_7CBC")

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

    # Function_47_7CBC end

    def Function_48_7D1D(): pass

    label("Function_48_7D1D")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0152
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ダクトの入口には\x01",
            "頑丈な南京錠がかかっている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    # Function_48_7D1D end

    SaveToFile()

Try(main)
