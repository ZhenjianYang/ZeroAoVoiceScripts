from ScenarioHelper import *

def main():
    CreateScenaFile(
        "t1401.bin",                # FileName
        "t1401",                    # MapName
        "t1401",                    # Location
        0x00BB,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x1A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 187, 0, 1, 0, 2],
    )

    BuildStringList((
        "t1401",                  # 0
        "游客",                   # 1
        "游客",                   # 2
        "游客",                   # 3
        "游客",                   # 4
        "SE控制",                 # 5
        "bt1410",                 # 6
        "bt1420",                 # 7
        "bt1400",                 # 8
        "bt1400",                 # 9
    ))

    ATBonus("ATBonus_37C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_AA8C", 15,  5,   5,   5,   10,  5,   25)
    Sepith("Sepith_AA84", 10,  6,   6,   6,   1,   4,   10)

    MonsterBattlePostion("MonsterBattlePostion_3CC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_430", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_434", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_438", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_43C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_440", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_444", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 2, 13, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_6A4", 0x0000, 78, 6, 60, 6, 1, 20, 0, "bt1400", "Sepith_AA8C", 40, 30, 20, 10,
        (
            ("ms79600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
        )
    )

    BattleInfo(
        "BattleInfo_5DC", 0x0000, 78, 6, 45, 6, 1, 20, 0, "bt1400", "Sepith_AA84", 40, 30, 20, 10,
        (
            ("ms82300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms82300.dat", "ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
        )
    )

    AddCharChip((
        "chr/ch22000.itc",                   # 00
        "chr/ch22100.itc",                   # 01
        "chr/ch24300.itc",                   # 02
        "chr/ch22200.itc",                   # 03
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
        "monster/ch82150.itc",               # 10
        "monster/ch82150.itc",               # 11
        "monster/ch82250.itc",               # 12
        "monster/ch82250.itc",               # 13
        "monster/ch82350.itc",               # 14
        "monster/ch82350.itc",               # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "monster/ch79650.itc",               # 18
        "monster/ch79650.itc",               # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
        "chr/ch00000.itc",                   # 1E
        "chr/ch00000.itc",                   # 1F
    ))

    DeclNpc(12500,   -3000,   -40400,  270,  389,  0x0, 0,   0,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(12560,   -3000,   -38650,  270,  389,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-3180,   -1000,   -13220,  45,   389,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-2279,   -1000,   -12399,  225,  389,  0x0, 0,   3,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(13840,   -28530,  20500,   0x10100B4,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(-13800,  -29380,  20550,   0x1010168,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(509320,  -20070,  0,       0x101010E,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(488860,  -19170,  0,       0x101005A,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(499240,  -6620,   50,      0x10100B4,    "BattleInfo_6A4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(481090,  -2890,   16000,   0x10100B4,    "BattleInfo_5DC", 0,   20,  0xFFFF, 4,  5)

    DeclActor(515500,  8000,    -12000,  1200,    515500,  9000,    -12000,  0x007C, 0,  3,  0x0000)
    DeclActor(0,       44500,   -500,    1500,    0,       46500,   -500,    0x007C, 0,  12, 0x0000)
    DeclActor(512000,  0,       -19000,  1200,    512000,  1000,    -19000,  0x007C, 0,  4,  0x0000)
    DeclActor(-2220,   40500,   -26430,  2000,    0,       44000,   -28050,  0x007C, 0,  19, 0x0000)
    DeclActor(2250,    40500,   -28050,  2000,    0,       44000,   -28050,  0x007C, 0,  19, 0x0000)
    DeclActor(0,       44500,   -540,    2000,    0,       46000,   -540,    0x007C, 0,  22, 0x0000)
    DeclActor(0,       44550,   -5470,   1500,    0,       44550,   -5470,   0x007C, 0,  43, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_87C",          # 00, 0
        "Function_1_934",          # 01, 1
        "Function_2_A5D",          # 02, 2
        "Function_3_11AB",         # 03, 3
        "Function_4_12E6",         # 04, 4
        "Function_5_1421",         # 05, 5
        "Function_6_1457",         # 06, 6
        "Function_7_147F",         # 07, 7
        "Function_8_14B3",         # 08, 8
        "Function_9_14E1",         # 09, 9
        "Function_10_1AD2",        # 0A, 10
        "Function_11_20BC",        # 0B, 11
        "Function_12_20CC",        # 0C, 12
        "Function_13_2446",        # 0D, 13
        "Function_14_24B5",        # 0E, 14
        "Function_15_2524",        # 0F, 15
        "Function_16_258D",        # 10, 16
        "Function_17_25FC",        # 11, 17
        "Function_18_3CE0",        # 12, 18
        "Function_19_4882",        # 13, 19
        "Function_20_48C0",        # 14, 20
        "Function_21_4BA5",        # 15, 21
        "Function_22_4BD7",        # 16, 22
        "Function_23_4CDA",        # 17, 23
        "Function_24_4D44",        # 18, 24
        "Function_25_4D64",        # 19, 25
        "Function_26_4D7D",        # 1A, 26
        "Function_27_4D96",        # 1B, 27
        "Function_28_4DF4",        # 1C, 28
        "Function_29_5713",        # 1D, 29
        "Function_30_5F0D",        # 1E, 30
        "Function_31_66D1",        # 1F, 31
        "Function_32_66E8",        # 20, 32
        "Function_33_6F86",        # 21, 33
        "Function_34_7818",        # 22, 34
        "Function_35_7EE9",        # 23, 35
        "Function_36_7F00",        # 24, 36
        "Function_37_8742",        # 25, 37
        "Function_38_8F96",        # 26, 38
        "Function_39_97F1",        # 27, 39
        "Function_40_A016",        # 28, 40
        "Function_41_A965",        # 29, 41
        "Function_42_A9AE",        # 2A, 42
        "Function_43_A9F1",        # 2B, 43
    ))


    def Function_0_87C(): pass

    label("Function_0_87C")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_8BC"),
        (1, "loc_8C8"),
        (2, "loc_8D4"),
        (3, "loc_8E0"),
        (4, "loc_8EC"),
        (5, "loc_8F8"),
        (6, "loc_904"),
        (SWITCH_DEFAULT, "loc_910"),
    )


    label("loc_8BC")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8C8")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8D4")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8E0")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8EC")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_8F8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_904")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_910")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_91C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_933")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_91C")

    label("loc_933")

    Return()

    # Function_0_87C end

    def Function_1_934(): pass

    label("Function_1_934")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x146, 0)), scpexpr(EXPR_END)), "loc_942")
    Jump("loc_9D5")

    label("loc_942")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 7)), scpexpr(EXPR_END)), "loc_950")
    Jump("loc_9D5")

    label("loc_950")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_END)), "loc_95E")
    Jump("loc_9D5")

    label("loc_95E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_END)), "loc_994")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x10)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x10)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x10)
    Jump("loc_9D5")

    label("loc_994")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 2)), scpexpr(EXPR_END)), "loc_9A2")
    Jump("loc_9D5")

    label("loc_9A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 1)), scpexpr(EXPR_END)), "loc_9B0")
    Jump("loc_9D5")

    label("loc_9B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 0)), scpexpr(EXPR_END)), "loc_9BE")
    Jump("loc_9D5")

    label("loc_9BE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 5)), scpexpr(EXPR_END)), "loc_9CC")
    Jump("loc_9D5")

    label("loc_9CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x144, 0)), scpexpr(EXPR_END)), "loc_9D5")

    label("loc_9D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EB")
    Event(0, 9)
    Jump("loc_A05")

    label("loc_9EB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A05")
    Event(0, 10)

    label("loc_A05")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_A14")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)

    label("loc_A14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A42")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A42")
    Event(0, 18)

    label("loc_A42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_A5C")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A5C")
    SetScenarioFlags(0x194, 3)

    label("loc_A5C")

    Return()

    # Function_1_934 end

    def Function_2_A5D(): pass

    label("Function_2_A5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A79")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_A8B")

    label("loc_A79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_END)), "loc_A8B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_A8B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_ACB")
    SetMapFlags(0x80000000)

    label("loc_ACB")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x12), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_FD9")
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xC, 0x4)

    label("loc_FD9")

    ClearMapObjFlags(0x1, 0x10)
    ClearMapObjFlags(0x5, 0x10)
    ClearMapObjFlags(0x6, 0x10)
    ClearMapObjFlags(0x7, 0x10)
    ClearMapObjFlags(0x8, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 5)), scpexpr(EXPR_END)), "loc_1031")
    OP_70(0x1, 0x0)
    OP_70(0x5, 0x1E)
    OP_70(0x6, 0x1E)
    ClearMapObjFlags(0x5, 0x2)
    ClearMapObjFlags(0x6, 0x2)
    OP_70(0x7, 0x1E)
    OP_70(0x8, 0x1E)
    ClearMapObjFlags(0x7, 0x2)
    ClearMapObjFlags(0x8, 0x2)
    Jump("loc_103B")

    label("loc_1031")

    OP_70(0x1, 0x1E)
    ClearMapObjFlags(0x1, 0x2)

    label("loc_103B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x194, 3)), scpexpr(EXPR_END)), "loc_104E")
    OP_70(0x1, 0x1E)
    ClearMapObjFlags(0x1, 0x2)

    label("loc_104E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1082")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1082")
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "move")

    label("loc_1082")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1095")
    OP_1B(0x0, 0x0, 0x29)

    label("loc_1095")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_10AD")
    SetMapFlags(0x2000)
    Jump("loc_10B2")

    label("loc_10AD")

    ClearMapFlags(0x2000)

    label("loc_10B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_10C5")
    OP_1B(0xC, 0x0, 0x2A)
    Jump("loc_10CA")

    label("loc_10C5")

    OP_1B(0xC, 0xFF, 0xFFFF)

    label("loc_10CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DD")
    OP_70(0x0, 0x0)
    Jump("loc_10E1")

    label("loc_10DD")

    OP_70(0x0, 0x1E)

    label("loc_10E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F4")
    OP_70(0x2, 0x0)
    Jump("loc_10F8")

    label("loc_10F4")

    OP_70(0x2, 0x1E)

    label("loc_10F8")

    OP_65(0x1, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_110E")
    OP_66(0x1, 0x1)

    label("loc_110E")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x145, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1148")
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1144")
    OP_66(0x3, 0x1)
    OP_66(0x4, 0x1)

    label("loc_1144")

    OP_66(0x5, 0x1)

    label("loc_1148")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11AA")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, 0, 44550, -5470, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_11AA")

    Return()

    # Function_2_A5D end

    def Function_3_11AB(): pass

    label("Function_3_11AB")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_129D")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药·改', 1)"), scpexpr(EXPR_END)), "loc_122E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FD, 0)
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
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药·改'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

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

    # Function_3_11AB end

    def Function_4_12E6(): pass

    label("Function_4_12E6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D8")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('柔光凉鞋', 1)"), scpexpr(EXPR_END)), "loc_1369")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '柔光凉鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FD, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_13D3")

    label("loc_1369")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '柔光凉鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '柔光凉鞋'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13D3")

    Jump("loc_1415")

    label("loc_13D8")

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

    label("loc_1415")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_12E6 end

    def Function_5_1421(): pass

    label("Function_5_1421")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "是啊，漂亮得会让人\x01",
            "不知不觉就看入神了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_1421 end

    def Function_6_1457(): pass

    label("Function_6_1457")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        (
            "那个天象仪\x01",
            "实在是太美了……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1457 end

    def Function_7_147F(): pass

    label("Function_7_147F")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "呵呵，不用这么着急，\x01",
            "镜子是不会跑掉的。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_147F end

    def Function_8_14B3(): pass

    label("Function_8_14B3")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "妈妈～快点快点！\x01",
            "楼梯在这边呢～！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_14B3 end

    def Function_9_14E1(): pass

    label("Function_9_14E1")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, -1000, -51000, 0)
    SetChrPos(0x102, -1000, -1000, -51500, 0)
    SetChrPos(0x103, 1000, -1000, -52500, 0)
    SetChrPos(0x104, 0, -1000, -53500, 0)
    OP_68(0, 0, -30000, 0)
    MoveCamera(27, 52, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(49130, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1000, -34000, 12000)
    MoveCamera(330, 16, 0, 12000)
    SetCameraDistance(47500, 12000)
    Sleep(7000)
    PlaceName2(340, 200, "c_plac47", 0x0, 0)
    Sleep(2000)

    def lambda_15AB():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15AB)
    Sleep(50)

    def lambda_15C3():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_15C3)
    Sleep(50)

    def lambda_15DB():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_15DB)
    Sleep(50)

    def lambda_15F3():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_15F3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    OP_6F(0x79)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_68(0, 3200, -47500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 100, -1000, -46000, 0)
    SetChrPos(0x102, -1150, -1000, -46900, 0)
    SetChrPos(0x103, 1200, -1000, -47100, 0)
    SetChrPos(0x104, -100, -1000, -48000, 0)
    OP_68(0, 1200, -47500, 3000)
    OP_6F(0x79)
    OP_0D()

    #C0011
    ChrTalk(
        0x102,
        "#00101F#6P这些光是……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#00201F#12P灵力粒子似乎\x01",
            "正在不断向上方飘浮……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1806")
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1700, -40000, 1800)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 3000, -13000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(39000, 0)
    SetCameraDistance(37500, 5000)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(100, 140, -1, -1)

    #A0013
    AnonymousTalk(
        0x101,
        "#00013F正面入口被……！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    #A0014
    AnonymousTalk(
        0x104,
        (
            "#00306F嗯……被封死了。\x02\x03",

            "#00301F不过，左右两边却\x01",
            "出现了新的入口……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_1943")

    label("loc_1806")

    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(0, 1700, -40000, 1800)
    Sleep(1000)
    Fade(1000)
    OP_68(0, 3000, -13000, 0)
    MoveCamera(0, 26, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(39000, 0)
    SetCameraDistance(37500, 5000)
    OP_0D()
    Sleep(500)
    SetMessageWindowPos(200, 140, -1, -1)

    #A0015
    AnonymousTalk(
        0x104,
        (
            "#00301F啧，竟然连内部构造\x01",
            "都改变了……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 140, -1, -1)

    #A0016
    AnonymousTalk(
        0x101,
        "#00005F是吗……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    #A0017
    AnonymousTalk(
        0x104,
        (
            "#00303F没错，上次来的时候，\x01",
            "正面入口是开着的……\x02\x03",

            "#00301F但现在却在左右两侧\x01",
            "出现了新入口……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_1943")

    Fade(1000)
    OP_68(0, 1200, -47500, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(540, 0)
    SetCameraDistance(18000, 0)
    OP_0D()

    #C0018
    ChrTalk(
        0x102,
        (
            "#00106F#6P我之前来过好几次了，\x01",
            "真没想到还有这种设计……\x02\x03",

            "#00108F这也是『她』做的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#00203F#12P……从深处传来了\x01",
            "奇怪的运转声……\x02\x03",

            "#00201F如果要继续前进，一定要保持警戒。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00003F#5P总之，我们也只能\x01",
            "想办法抵达最顶层了……\x02\x03",

            "#00013F必须要问清楚亚里欧斯先生的目的，\x01",
            "并夺回琪雅……！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 0, -1000, -46000, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 1)
    OP_29(0xAD, 0x1, 0x4)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_14E1 end

    def Function_10_1AD2(): pass

    label("Function_10_1AD2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, -19000, 40500, -33500, 90)
    SetChrPos(0x102, -20150, 40500, -33500, 90)
    SetChrPos(0x103, -19500, 40500, -34650, 90)
    SetChrPos(0x104, -20650, 40500, -34650, 90)
    OP_68(-14500, 42000, -34000, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(17500, 0)
    SetCameraDistance(17000, 3000)
    FadeToBright(1000, 0)
    BeginChrThread(0x101, 3, 0, 11)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 11)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 11)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 11)
    WaitChrThread(0x101, 3)
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

    def lambda_1BF8():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1BF8)
    Sleep(30)

    def lambda_1C08():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C08)
    Sleep(30)

    def lambda_1C18():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C18)
    Sleep(30)

    def lambda_1C28():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1C28)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    Fade(1000)
    OP_68(0, 43500, -30500, 0)
    MoveCamera(36, 33, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(36000, 0)
    OP_68(0, 45900, -14500, 12000)
    MoveCamera(24, 6, 0, 12000)
    OP_6E(640, 12000)
    SetCameraDistance(26000, 12000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D0A")
    SetMessageWindowPos(50, 140, -1, -1)

    #A0021
    AnonymousTalk(
        0x101,
        "#00013F终于到了啊……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    #A0022
    AnonymousTalk(
        0x104,
        "#00301F嗯……到顶层了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D53")

    label("loc_1D0A")

    SetMessageWindowPos(50, 140, -1, -1)

    #A0023
    AnonymousTalk(
        0x101,
        "#00013F到了吗……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    #A0024
    AnonymousTalk(
        0x104,
        (
            "#00301F嗯……\x01",
            "到顶层了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D53")

    SetMessageWindowPos(70, 140, -1, -1)

    #A0025
    AnonymousTalk(
        0x102,
        (
            "#00108F可、可是……\x01",
            "并没有看到小琪雅\x01",
            "和亚里欧斯先生啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Fade(500)
    OP_68(-14500, 42000, -34250, 0)
    MoveCamera(0, 21, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(14580, 0)
    OP_0D()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0026
    ChrTalk(
        0x103,
        (
            "#00206F#6P……之前来这里的时候，\x01",
            "我并没有察觉到……\x02\x03",

            "#00201F在那面发光大镜子的里面，\x01",
            "似乎还隐藏着一个秘密空间。\x02",
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
    Sleep(1000)

    def lambda_1EBE():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1EBE)
    Sleep(50)

    def lambda_1ECE():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1ECE)
    Sleep(50)

    def lambda_1EDE():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1EDE)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0027
    ChrTalk(
        0x101,
        "#00005F#11P真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#00203F#6P是的，相当大量的灵力\x01",
            "呈漩涡状流动。\x02\x03",

            "#00201F那里恐怕就是终点了。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#00103F#5P……原来如此…………\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#00304F#6P……看来我们总算是\x01",
            "追上了啊……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00003F#11P是啊……\x02\x03",

            "#00007F各位！检查一下自己的装备！\x01",
            "我们绝对要夺回琪雅！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_200D():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_200D)
    Sleep(50)

    def lambda_201D():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_201D)
    Sleep(50)

    def lambda_202D():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_202D)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0032
    ChrTalk(
        0x102,
        "#00107F#5P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#00201F#6P好的……！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#00307F#6P明白！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -14000, 40500, -34000, 45)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x183, 2)
    OP_29(0xAD, 0x1, 0x5)
    OP_66(0x1, 0x1)
    EventEnd(0x5)
    Return()

    # Function_10_1AD2 end

    def Function_11_20BC(): pass

    label("Function_11_20BC")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    Return()

    # Function_11_20BC end

    def Function_12_20CC(): pass

    label("Function_12_20CC")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    SetChrPos(0x101, 100, 44500, -2000, 0)
    SetChrPos(0x102, -1000, 44500, -3000, 0)
    SetChrPos(0x103, 1000, 44500, -3000, 0)
    SetChrPos(0x104, -100, 44500, -4000, 0)
    LoadChrToIndex("apl/ch51779.itc", 0x1E)
    LoadEffect(0x0, "event\\ev15050.eff")
    OP_68(0, 49700, -2200, 0)
    MoveCamera(0, 11, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(15480, 0)
    FadeToBright(1000, 0)
    OP_68(-150, 46800, -2200, 3000)
    OP_6F(0x79)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22CB")
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "散发着淡淡光芒的粒子正被吸入到镜中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    Sleep(500)
    OP_9B(0x0, 0x101, 0x0, 0x1F4, 0x3E8, 0x0)
    Sleep(300)
    Fade(250)
    Sound(812, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    OP_0D()
    Sound(920, 0, 50, 0)
    Sound(935, 0, 40, 0)
    PlayEffect(0x0, 0xFF, 0x101, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(2500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    OP_0D()

    #C0036
    ChrTalk(
        0x101,
        (
            "#00006F#6P（看来我们可以\x01",
            "  直接进入镜中……）\x02\x03",

            "#00013F（……琪雅……我们马上就来了！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183, 3)
    Jump("loc_2316")

    label("loc_22CB")

    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "散发着淡淡光芒的粒子正被吸入到镜中。\x02\x03",

            "看来可以直接进入镜中。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2316")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "踏入镜中\x01",      # 0
            "离开此处\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2362"),
        (1, "loc_241B"),
        (SWITCH_DEFAULT, "loc_2445"),
    )


    label("loc_2362")

    SetChrPos(0x101, 0, 44500, -2000, 0)
    Fade(1000)
    OP_68(0, 47500, -2000, 0)
    MoveCamera(0, 15, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(14700, 0)
    OP_68(0, 47500, -2000, 5000)
    MoveCamera(0, 35, 0, 5000)
    SetCameraDistance(17000, 5000)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(200)
    BeginChrThread(0x102, 3, 0, 14)
    Sleep(200)
    BeginChrThread(0x103, 3, 0, 15)
    Sleep(200)
    BeginChrThread(0x104, 3, 0, 16)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    OP_6F(0x79)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_37()
    NewScene("t1490", 0, 0, 0)
    IdleLoop()
    Jump("loc_2445")

    label("loc_241B")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 0, 44500, -4000, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_2445")

    label("loc_2445")

    Return()

    # Function_12_20CC end

    def Function_13_2446(): pass

    label("Function_13_2446")


    def lambda_244B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_244B)
    Sleep(500)
    Sound(341, 0, 100, 0)

    def lambda_2469():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2469)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_2446 end

    def Function_14_24B5(): pass

    label("Function_14_24B5")


    def lambda_24BA():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24BA)
    Sleep(1000)

    def lambda_24D2():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24D2)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_24B5 end

    def Function_15_2524(): pass

    label("Function_15_2524")


    def lambda_2529():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2529)
    Sleep(1000)

    def lambda_2541():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2541)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_2524 end

    def Function_16_258D(): pass

    label("Function_16_258D")


    def lambda_2592():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2592)
    Sleep(1500)

    def lambda_25AA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25AA)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_258D end

    def Function_17_25FC(): pass

    label("Function_17_25FC")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3A46")
    SetChrPos(0x101, -500, -950, -51000, 0)
    SetChrPos(0xEF, 500, -950, -51000, 0)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0xEF, 0x8)
    OP_68(0, 18000, -30000, 0)
    MoveCamera(330, 48, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(40000, 0)
    FadeToBright(1000, 0)
    OP_68(0, 0, -30000, 15000)
    MoveCamera(345, 18, 0, 15000)
    SetCameraDistance(40000, 15000)
    Sleep(9000)
    PlaceName2(340, 200, "c_plac47", 0x0, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0xEF, 0x8)
    OP_68(0, 1050, -46000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    SetCameraDistance(13500, 3000)

    def lambda_2708():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2708)
    Sleep(50)

    def lambda_2720():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_2720)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00000F这就是『镜之城』啊。\x02\x03",

            "据说是这座主题公园的\x01",
            "代表性游乐设施……\x02\x03",

            "#00006F……呼，真是只能用\x01",
            "惊人来形容它了。\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_27FF"),
        (1, "loc_29AB"),
        (2, "loc_2B37"),
        (3, "loc_2CD8"),
        (4, "loc_2E77"),
        (5, "loc_302F"),
        (6, "loc_31D0"),
        (7, "loc_3363"),
        (8, "loc_34FD"),
        (9, "loc_367E"),
        (10, "loc_381E"),
        (SWITCH_DEFAULT, "loc_3A41"),
    )


    label("loc_27FF")


    #C0039
    ChrTalk(
        0x102,
        (
            "#00104F这种梦幻般的气氛似乎是用\x01",
            "那个天象仪营造出来的。\x02\x03",

            "#00100F我在利贝尔留学的时候，\x01",
            "参观过王都格兰赛尔的王城，\x01",
            "这里的气氛完全可以与之媲美。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00000F那真是很厉害了，\x01",
            "不愧是ＩＢＣ啊……\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#00100F是的，据说只要在摇响大钟之后\x01",
            "站在镜子前，许下的愿望就会实现。\x02\x03",

            "#00104F那面镜子好像在\x01",
            "城堡的最顶层……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        "#00100F嗯，好的。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_29AB")


    #C0044
    ChrTalk(
        0x103,
        (
            "#00204F多亏有中央那台天象仪，\x01",
            "才能营造出这种梦幻般的气氛。\x02\x03",

            "#00200F简直就像在童话中\x01",
            "出现的城堡。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00000F是啊，确实有这种感觉，\x01",
            "真不愧是ＩＢＣ……\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#00200F听艾莉前辈说，\x01",
            "只要在摇响大钟之后站在镜子前，\x01",
            "许下的愿望就会实现。\x02\x03",

            "#00204F那面镜子好像在\x01",
            "城堡的最顶层……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#00200F好的，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_2B37")


    #C0049
    ChrTalk(
        0x104,
        (
            "#00304F这种梦幻般的气氛好像是那台\x01",
            "在中央转动的天象仪营造出来的。\x02\x03",

            "#00300F哈哈，做得这么逼真，\x01",
            "看起来就像一座真正的城堡啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00000F是啊，确实有这种感觉，\x01",
            "真不愧是ＩＢＣ……\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#00300F哦，就是那个摇响大钟后\x01",
            "站在镜子前就能实现愿望的传说吧？\x02\x03",

            "#00304F那镜子在最顶层，\x01",
            "只要爬上去就能看到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        "#00300F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_2CD8")


    #C0054
    ChrTalk(
        0x109,
        (
            "#10104F这种梦幻般的气氛似乎是那台\x01",
            "在中央转动的天象仪营造出来的。\x02\x03",

            "#10100F做得如此逼真，\x01",
            "简直就像一座真正的城堡呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00000F是啊，确实有这种感觉，\x01",
            "真不愧是ＩＢＣ……\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x109,
        (
            "#10100F是的，据说只要摇响大钟，\x01",
            "然后站在镜子前，就能实现愿望。\x02\x03",

            "#10104F那面镜子就在最顶层，\x01",
            "只要爬上去就能看到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x109,
        "#10100F好的，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_2E77")


    #C0059
    ChrTalk(
        0x105,
        (
            "#10304F这种梦幻般的气氛就是靠\x01",
            "中央那台天象仪营造出来的呢。\x02\x03",

            "#10302F呵呵，设计还真精致。\x01",
            "建造这种规模的建筑物，\x01",
            "肯定花费了巨额的米拉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00000F嗯，ＩＢＣ的财力\x01",
            "总能让人大吃一惊……\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x105,
        (
            "#10300F哦，就是那个摇响大钟后，\x01",
            "站在镜子前就能实现愿望的传说吧？\x02\x03",

            "#10304F听说那面镜子在最顶层，\x01",
            "我们只要上去就可以看到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        "#10300F呵呵，好啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_302F")


    #C0064
    ChrTalk(
        0x153,
        (
            "#01111F在正中央咕噜噜地转个不停的\x01",
            "那个东西是什么呢～？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00000F哦，那是天象仪。\x01",
            "就是那个装置营造出了\x01",
            "这种梦幻般的气氛。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x153,
        "#01105F哇……听起来好厉害。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00000F是啊，简直无法用语言来形容，\x01",
            "真不愧是ＩＢＣ……\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x153,
        (
            "#01100F就是艾莉说过的那个镜子吗～？\x01",
            "我记得她说那面镜子在城堡的顶层～\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00000F嗯，那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x153,
        "#01109F赞成～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_31D0")


    #C0071
    ChrTalk(
        0x156,
        (
            "#06404F看来是中央那台天象仪\x01",
            "营造出了这种梦幻般的气氛～\x02\x03",

            "#06400F呵呵，做得如此逼真，\x01",
            "简直就像是真正的城堡呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00000F是啊，确实有这种感觉，\x01",
            "真不愧是ＩＢＣ……\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x156,
        (
            "#06400F嗯，据说摇响大钟后\x01",
            "站在镜子前，就可以实现愿望了～\x02\x03",

            "#06404F那面镜子就在最顶层，\x01",
            "只要爬上去就能看到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x156,
        "#06409F好的！走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_3363")


    #C0076
    ChrTalk(
        0x14C,
        (
            "#05904F中央那台设备是天象仪吧？\x01",
            "给人一种梦幻般的感觉呢。\x02\x03",

            "#05902F呵呵，我以前给你讲的图画书里\x01",
            "好像也出现过这样的城堡。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……\x01",
            "确实很像童话中的城堡呢。\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x14C,
        (
            "#05900F嗯，艾莉小姐说过，\x01",
            "只要在摇响大钟后站在镜子前，\x01",
            "许下的愿望就会实现。\x02\x03",

            "#05904F那面镜子好像在\x01",
            "城堡的最顶层……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x14C,
        "#05900F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_34FD")


    #C0081
    ChrTalk(
        0x134,
        (
            "#01704F这种梦幻般的感觉就是靠\x01",
            "中央那台天象仪营造出来的吧……\x02\x03",

            "#01702F唔……下次能不能让\x01",
            "彩虹剧团借用一下呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……伊莉娅小姐还是老样子啊。\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x134,
        (
            "#01700F嗯，就是那个摇响大钟后，\x01",
            "站在镜子前就能实现愿望的传说吧？\x02\x03",

            "#01704F那面镜子好像在城堡最顶层……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x134,
        "#01709F好，走吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_367E")


    #C0086
    ChrTalk(
        0x135,
        (
            "#01804F这种梦幻的气氛就是靠\x01",
            "中央那台天象仪营造出来的吧……\x02\x03",

            "#01802F呵呵，伊莉娅小姐要是看到它，\x01",
            "说不定会产生用在舞台上的想法呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……确实不难想象。\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x135,
        (
            "#01805F嗯，听说只要在摇响大钟之后\x01",
            "站在镜子前，就能实现许下的愿望。\x02\x03",

            "#01804F据艾莉小姐所说，\x01",
            "那面镜子在城堡的最顶层。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00000F那我们就去最顶层\x01",
            "找找看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x135,
        "#01809F好的，那就走吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_381E")


    #C0091
    ChrTalk(
        0x166,
        (
            "#14005F在正中央转个不停的\x01",
            "那个东西是什么？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00000F哦，那是天象仪。\x01",
            "就是那个装置营造出了\x01",
            "这种梦幻般的气氛。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x166,
        (
            "#14000F嘿……虽然不太明白，\x01",
            "但感觉好厉害啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00000F是啊，简直无法用语言来形容，\x01",
            "真不愧是ＩＢＣ……\x02\x03",

            "#00005F对了，\x01",
            "听说这里有一面\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x166,
        (
            "#14000F哦，就是刚才听他们说的那个，\x01",
            "摇响大钟之后站在镜子前许愿，\x01",
            "愿望就可以实现的传说吧？\x02\x03",

            "#14003F那面镜子好像在城堡的最顶层……\x01",
            "话说回来，那种传闻真的可信吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，我也不知道……\x01",
            "但我们还是去最顶层看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x166,
        "#14000F哼，那我就陪你去看看好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_3A41")

    Jump("loc_3CCA")

    label("loc_3A46")

    SetChrPos(0x101, -500, -950, -51000, 0)
    SetChrPos(0xEF, 500, -950, -51000, 0)
    OP_68(0, 1050, -46000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13500, 3000)

    def lambda_3AAD():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3AAD)
    Sleep(50)

    def lambda_3AC5():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_3AC5)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00000F目标是最顶层的\x01",
            "『实现愿望的镜子』。\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3B5E"),
        (1, "loc_3B7C"),
        (2, "loc_3B9A"),
        (3, "loc_3BBA"),
        (4, "loc_3BDC"),
        (5, "loc_3BFC"),
        (6, "loc_3C16"),
        (7, "loc_3C38"),
        (8, "loc_3C58"),
        (9, "loc_3C78"),
        (10, "loc_3C9E"),
        (SWITCH_DEFAULT, "loc_3CCA"),
    )


    label("loc_3B5E")


    #C0099
    ChrTalk(
        0x102,
        "#00100F嗯，明白了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3B7C")


    #C0100
    ChrTalk(
        0x103,
        "#00200F好，出发吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3B9A")


    #C0101
    ChrTalk(
        0x104,
        "#00300F哦，去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3BBA")


    #C0102
    ChrTalk(
        0x109,
        "#10100F好的，去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3BDC")


    #C0103
    ChrTalk(
        0x105,
        "#10300F呵呵，知道了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3BFC")


    #C0104
    ChrTalk(
        0x153,
        "#01109F赞成～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3C16")


    #C0105
    ChrTalk(
        0x156,
        "#06409F好的！去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3C38")


    #C0106
    ChrTalk(
        0x14C,
        "#05900F嗯，去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3C58")


    #C0107
    ChrTalk(
        0x134,
        "#01709F好，去看看吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3C78")


    #C0108
    ChrTalk(
        0x135,
        "#01802F好的，我们去看看吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3C9E")


    #C0109
    ChrTalk(
        0x166,
        "#14000F哼，那我就陪你去看看好了。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3CCA")

    label("loc_3CCA")

    SetChrPos(0x0, 0, -1000, -46000, 0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_17_25FC end

    def Function_18_3CE0(): pass

    label("Function_18_3CE0")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    SetChrPos(0x101, 0, 40500, -10450, 180)
    SetChrPos(0xEF, 0, 40500, -10450, 180)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xEF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearMapObjFlags(0x4, 0x10)
    OP_70(0x4, 0x0)
    OP_68(0, 41500, -10450, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(18000, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(118, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x8)
    OP_79(0x4)
    OP_68(0, 41500, -15400, 3000)
    SetCameraDistance(14000, 3000)

    def lambda_3D9C():
        OP_9B(0x1, 0xFE, 0xFFFA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D9C)

    def lambda_3DB1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3DB1)
    Sleep(700)

    def lambda_3DC5():
        OP_9B(0x1, 0xFE, 0x6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_3DC5)

    def lambda_3DDA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_3DDA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xEF, 2)
    Sound(118, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x8)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4336")

    #C0110
    ChrTalk(
        0x101,
        "#00000F这里就是『镜之城』的最顶层……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 42700, -27500, 0)
    MoveCamera(27, 12, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(19500, 0)
    OP_0D()

    #C0111
    ChrTalk(
        0x101,
        (
            "#00005F看样子，那个就是传闻中的\x01",
            "那口『大钟』了。\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3F0A"),
        (1, "loc_3F58"),
        (2, "loc_3FA6"),
        (3, "loc_3FE0"),
        (4, "loc_4018"),
        (5, "loc_4066"),
        (6, "loc_40C2"),
        (7, "loc_40FC"),
        (8, "loc_414C"),
        (9, "loc_419A"),
        (10, "loc_41E8"),
        (SWITCH_DEFAULT, "loc_423A"),
    )


    label("loc_3F0A")


    #C0112
    ChrTalk(
        0x102,
        (
            "#00100F用来摇响它的粗绳\x01",
            "就在左右两边。\x02\x03",

            "#00104F应该不会\x01",
            "有错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_3F58")


    #C0113
    ChrTalk(
        0x103,
        (
            "#00200F用来摇响它的粗绳\x01",
            "就在左右两边。\x02\x03",

            "#00204F应该不会\x01",
            "有错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_3FA6")


    #C0114
    ChrTalk(
        0x104,
        (
            "#00300F嗯，左右两边还有\x01",
            "用来摇响它的粗绳呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_3FE0")


    #C0115
    ChrTalk(
        0x109,
        (
            "#10100F嗯，用来摇响它的粗绳\x01",
            "就在左右两边。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_4018")


    #C0116
    ChrTalk(
        0x105,
        (
            "#10300F用于摇响它的粗绳\x01",
            "就在左右两边。\x02\x03",

            "#10304F应该不会\x01",
            "有错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_4066")


    #C0117
    ChrTalk(
        0x153,
        (
            "#01105F用来摇响它的粗绳子\x01",
            "就在左右两边呢。\x02\x03",

            "#01111F艾莉说的大钟\x01",
            "就是它了吧～？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_40C2")


    #C0118
    ChrTalk(
        0x156,
        (
            "#06400F嗯，用来摇响它的粗绳\x01",
            "就在左右两边呢～\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_40FC")


    #C0119
    ChrTalk(
        0x14C,
        (
            "#05900F用来摇响它的粗绳\x01",
            "就在左右两边呢。\x02\x03",

            "#05904F应该不会\x01",
            "有错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_414C")


    #C0120
    ChrTalk(
        0x134,
        (
            "#01700F用来摇响它的粗绳\x01",
            "就在左右两边。\x02\x03",

            "#01704F应该不会\x01",
            "有错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_419A")


    #C0121
    ChrTalk(
        0x135,
        (
            "#01802F用于摇响它的粗绳\x01",
            "就在左右两边。\x02\x03",

            "#01804F应该不会\x01",
            "有错了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_41E8")


    #C0122
    ChrTalk(
        0x166,
        (
            "#14000F用来摇响它的粗绳\x01",
            "就在左右两边……\x02\x03",

            "#14003F应该就是\x01",
            "这东西了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_423A")

    label("loc_423A")


    def lambda_423F():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_423F)
    Sleep(50)

    def lambda_424F():
        OP_93(0xEF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_424F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Fade(500)
    OP_68(0, 45500, -12000, 0)
    MoveCamera(30, 12, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(30000, 0)
    OP_0D()

    #C0123
    ChrTalk(
        0x101,
        (
            "#00002F也就是说，那面大镜子\x01",
            "就是『实现愿望的镜子』啦？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, 41500, -15400, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(14000, 0)
    OP_0D()

    def lambda_430E():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_430E)
    Sleep(50)

    def lambda_431E():
        OP_93(0xEF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_431E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jump("loc_435B")

    label("loc_4336")


    #C0124
    ChrTalk(
        0x101,
        "#00000F呼……终于爬到最顶层了。\x02",
    )

    CloseMessageWindow()

    label("loc_435B")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_43A6"),
        (1, "loc_441D"),
        (2, "loc_448E"),
        (3, "loc_44F0"),
        (4, "loc_4552"),
        (5, "loc_45B0"),
        (6, "loc_460C"),
        (7, "loc_4668"),
        (8, "loc_46CA"),
        (9, "loc_472A"),
        (10, "loc_4796"),
        (SWITCH_DEFAULT, "loc_47F0"),
    )


    label("loc_43A6")


    #C0125
    ChrTalk(
        0x102,
        (
            "#00100F只要在摇响大钟之后站在镜子前，\x01",
            "就可以实现许下的愿望……\x02\x03",

            "#00104F亲身来到这里之后，\x01",
            "不由得有些紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_441D")


    #C0126
    ChrTalk(
        0x103,
        (
            "#00200F只要在摇响大钟之后站在\x01",
            "镜子前，就可以实现愿望……\x02\x03",

            "#00204F亲身来到这里之后，\x01",
            "总觉得有些紧张呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_448E")


    #C0127
    ChrTalk(
        0x104,
        (
            "#00300F只要摇响大钟，然后站在\x01",
            "镜子前，就能实现愿望……\x02\x03",

            "#00304F嗯，我该许个什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_44F0")


    #C0128
    ChrTalk(
        0x109,
        (
            "#10100F只要在摇响大钟后站在\x01",
            "镜子前，就可以实现愿望……\x02\x03",

            "#10104F唔……我该许什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_4552")


    #C0129
    ChrTalk(
        0x105,
        (
            "#10300F只要在摇响大钟之后站在\x01",
            "镜子前，就能实现愿望……\x02\x03",

            "#10304F嗯，究竟是真是假呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_45B0")


    #C0130
    ChrTalk(
        0x153,
        (
            "#01100F只要在摇响大钟之后站在\x01",
            "镜子前，就能实现愿望了吧～\x02\x03",

            "#01109F该许个什么愿呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_460C")


    #C0131
    ChrTalk(
        0x156,
        (
            "#06400F只要在摇响大钟之后站在\x01",
            "镜子前，就能实现愿望了～\x02\x03",

            "#06409F这次许个什么愿呢～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_4668")


    #C0132
    ChrTalk(
        0x14C,
        (
            "#05900F只要在摇响大钟后站在\x01",
            "镜子前，就能实现愿望了……\x02\x03",

            "#05904F呵呵，我许个什么愿好呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_46CA")


    #C0133
    ChrTalk(
        0x134,
        (
            "#01700F只要在摇响大钟后站在\x01",
            "镜子前，就能实现愿望了。\x02\x03",

            "#01702F呵呵，我该许个什么愿呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_472A")


    #C0134
    ChrTalk(
        0x135,
        (
            "#01803F只要在摇响大钟后站在\x01",
            "镜子前，就能使愿望成真了。\x02\x03",

            "#01808F（但对我来说……愿望这种事情……）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_4796")


    #C0135
    ChrTalk(
        0x166,
        (
            "#14003F只要在摇响大钟之后站在\x01",
            "镜子前，就能使愿望成真……\x02\x03",

            "#14008F……是真的吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_47F0")

    label("loc_47F0")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4833")

    #C0136
    ChrTalk(
        0x101,
        (
            "#00000F总之，我们一起\x01",
            "去把那个大钟摇响吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4863")

    label("loc_4833")


    #C0137
    ChrTalk(
        0x101,
        (
            "#00000F总之，我们一起\x01",
            "去把那个大钟摇响吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4863")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x0, 0, 40550, -15500, 180)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_18_3CE0 end

    def Function_19_4882(): pass

    label("Function_19_4882")

    TalkBegin(0xFF)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "摇响大钟\x01",      # 0
            "放弃\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Sleep(200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48BC")
    Call(0, 20)
    Jump("loc_48BC")

    label("loc_48BC")

    TalkEnd(0xFF)
    Return()

    # Function_19_4882 end

    def Function_20_48C0(): pass

    label("Function_20_48C0")

    EventBegin(0x0)
    Fade(500)
    OP_68(0, 42000, -27500, 0)
    MoveCamera(48, 28, 0, 0)
    OP_6E(640, 0)
    SetCameraDistance(13500, 0)
    SetCameraDistance(18500, 5000)
    SetChrPos(0x101, -2450, 40500, -27300, 0)
    SetChrPos(0xEF, 2090, 40500, -28590, 0)
    BeginChrThread(0xC, 1, 0, 21)
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "move")
    OP_6F(0x79)
    OP_0D()
    TurnDirection(0x101, 0xEF, 500)

    #C0138
    ChrTalk(
        0x101,
        (
            "#00000F#6P……好，接下来就要去\x01",
            "上边那面镜子前了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_49CB"),
        (1, "loc_49EA"),
        (2, "loc_4A0B"),
        (3, "loc_4A3A"),
        (4, "loc_4A63"),
        (5, "loc_4A92"),
        (6, "loc_4AB3"),
        (7, "loc_4ADC"),
        (8, "loc_4B05"),
        (9, "loc_4B28"),
        (10, "loc_4B51"),
        (SWITCH_DEFAULT, "loc_4B78"),
    )


    label("loc_49CB")


    #C0139
    ChrTalk(
        0x102,
        "#00100F嗯，走吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_49EA")


    #C0140
    ChrTalk(
        0x103,
        "#00200F好的，走吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4A0B")


    #C0141
    ChrTalk(
        0x104,
        "#00300F哈哈，终于要到关键时刻了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4A3A")


    #C0142
    ChrTalk(
        0x109,
        "#10100F终于要到关键时刻了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4A63")


    #C0143
    ChrTalk(
        0x105,
        "#10300F呵呵，终于要到关键时刻了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4A92")


    #C0144
    ChrTalk(
        0x153,
        "#01109F嗯，走吧～！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4AB3")


    #C0145
    ChrTalk(
        0x156,
        "#06400F呵呵，真让人期待啊～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4ADC")


    #C0146
    ChrTalk(
        0x14C,
        "#05900F呵呵，究竟会如何呢～\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4B05")


    #C0147
    ChrTalk(
        0x134,
        "#01700F嗯，我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4B28")


    #C0148
    ChrTalk(
        0x135,
        "#01802F……好的，我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4B51")


    #C0149
    ChrTalk(
        0x166,
        "#14000F……哼，那就走吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4B78")

    label("loc_4B78")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x0, 0)
    OP_1B(0xC, 0x0, 0x2A)
    SetChrPos(0x0, -7700, 40550, -25000, 315)
    EventEnd(0x5)
    Return()

    # Function_20_48C0 end

    def Function_21_4BA5(): pass

    label("Function_21_4BA5")

    Sound(918, 0, 100, 0)
    Sleep(2000)
    Sound(918, 0, 80, 0)
    Sleep(2000)
    Sound(918, 0, 60, 0)

    label("loc_4BBD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BD6")
    Sleep(2000)
    Sound(918, 0, 40, 0)
    Jump("loc_4BBD")

    label("loc_4BD6")

    Return()

    # Function_21_4BA5 end

    def Function_22_4BD7(): pass

    label("Function_22_4BD7")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C21")

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000F不对……\x01",
            "得先摇响下面的大钟才行。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4CD6")

    label("loc_4C21")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4C6C"),
        (1, "loc_4C74"),
        (2, "loc_4C7C"),
        (3, "loc_4C84"),
        (4, "loc_4C8C"),
        (5, "loc_4C94"),
        (6, "loc_4C9C"),
        (7, "loc_4CA4"),
        (8, "loc_4CAC"),
        (9, "loc_4CB4"),
        (10, "loc_4CBC"),
        (SWITCH_DEFAULT, "loc_4CC4"),
    )


    label("loc_4C6C")

    Call(0, 28)
    Jump("loc_4CC4")

    label("loc_4C74")

    Call(0, 29)
    Jump("loc_4CC4")

    label("loc_4C7C")

    Call(0, 30)
    Jump("loc_4CC4")

    label("loc_4C84")

    Call(0, 32)
    Jump("loc_4CC4")

    label("loc_4C8C")

    Call(0, 33)
    Jump("loc_4CC4")

    label("loc_4C94")

    Call(0, 34)
    Jump("loc_4CC4")

    label("loc_4C9C")

    Call(0, 36)
    Jump("loc_4CC4")

    label("loc_4CA4")

    Call(0, 37)
    Jump("loc_4CC4")

    label("loc_4CAC")

    Call(0, 38)
    Jump("loc_4CC4")

    label("loc_4CB4")

    Call(0, 39)
    Jump("loc_4CC4")

    label("loc_4CBC")

    Call(0, 40)
    Jump("loc_4CC4")

    label("loc_4CC4")

    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()

    label("loc_4CD6")

    TalkEnd(0xFF)
    Return()

    # Function_22_4BD7 end

    def Function_23_4CDA(): pass

    label("Function_23_4CDA")

    SetChrPos(0x101, -500, 44550, -2500, 0)
    SetChrPos(0xEF, 500, 44550, -2500, 0)
    Fade(500)
    OP_68(0, 47500, -1500, 0)
    OP_68(0, 46000, -1500, 4000)
    MoveCamera(0, 15, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15700, 0)
    OP_6F(0x79)
    OP_0D()
    Return()

    # Function_23_4CDA end

    def Function_24_4D44(): pass

    label("Function_24_4D44")

    Fade(800)
    EndChrThread(0xC, 0x1)
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "stop")
    OP_0D()
    Sleep(2500)
    Return()

    # Function_24_4D44 end

    def Function_25_4D64(): pass

    label("Function_25_4D64")


    def lambda_4D69():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D69)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_25_4D64 end

    def Function_26_4D7D(): pass

    label("Function_26_4D7D")


    def lambda_4D82():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4D82)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_26_4D7D end

    def Function_27_4D96(): pass

    label("Function_27_4D96")

    SetCameraDistance(14700, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DD6")
    OP_63(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_4DE8")

    label("loc_4DD6")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_4DE8")

    Sleep(2500)
    OP_64(0x101)
    OP_64(0xFE)
    OP_6F(0x79)
    Return()

    # Function_27_4D96 end

    def Function_28_4DF4(): pass

    label("Function_28_4DF4")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x102, 3, 0, 25)
    WaitChrThread(0x102, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4EC0")

    #C0151
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        (
            "#00100F只要在脑中暗想一下自己的愿望，\x01",
            "应该就可以了。\x02\x03",

            "我们试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4F19")

    label("loc_4EC0")


    #C0153
    ChrTalk(
        0x101,
        (
            "#00000F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#00100F嗯，我们试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_4F19")

    BeginChrThread(0x102, 3, 0, 26)
    WaitChrThread(0x102, 3)

    #C0155
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0156
    ChrTalk(
        0x102,
        "#00103F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x102, 3, 0, 27)
    WaitChrThread(0x102, 3)
    Call(0, 24)
    BeginChrThread(0x102, 3, 0, 25)
    WaitChrThread(0x102, 3)

    #C0157
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#00104F嗯，我也许完愿了。\x02\x03",

            "#00100F对了……\x01",
            "罗伊德，你许了什么愿？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_511D")

    #C0159
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括琪雅、你，\x01",
            "还有支援科的同伴们。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        "#00100F呵呵，真符合你的作风啊。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢称赞。\x02\x03",

            "#00000F对了，艾莉，\x01",
            "你许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5218")

    label("loc_511D")


    #C0162
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望艾莉的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        "#00100F呵呵，谢谢你，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，不用客气。\x02\x03",

            "#00000F对了，艾莉，\x01",
            "你许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5218")

    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    #C0165
    ChrTalk(
        0x102,
        (
            "#00103F我的愿望是……\x01",
            "『希望爸爸和妈妈都幸福快乐』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x101,
        "#00005F记得你的父母已经……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#00100F……呵呵，嗯，以前和你说过。\x01",
            "他们在十年前就离婚了，\x01",
            "分别生活在共和国和帝国。\x02\x03",

            "#00104F虽然现在时常用\x01",
            "书信、导力通讯等方式和他们联系，\x01",
            "但几乎见不到面。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#00008F……你肯定很寂寞吧。\x02\x03",

            "#00003F我和你一样，也是自幼与父母离别。\x01",
            "他们在我很小的时候就过世了，但因为还有大哥\x01",
            "和塞茜尔姐姐陪着我，所以并没有感到很寂寞……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#00100F呵呵，我也还有\x01",
            "外公这个亲人啊，\x01",
            "所以并不是寂寞的问题……\x02\x03",

            "#00103F……准确地说……\x01",
            "我是在担心他们。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#00005F担心……？\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00103F爸爸和妈妈都很关心我，\x01",
            "会经常和我联系……\x02\x03",

            "#00108F如果这只是因为当年抛下我而去，\x01",
            "所以一直后悔至今，\x01",
            "那未免也太过痛苦了。\x02\x03",

            "他们都是非常正派的人，\x01",
            "无论如何也无法将过去\x01",
            "彻底遗忘。\x02\x03",

            "#00104F但那些都已经是十年前的事情了，\x01",
            "我希望他们能走上崭新的人生道路，\x01",
            "幸福轻松地生活下去。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00008F希望他们忘记过去，开始新生活吗……\x02\x03",

            "#00001F但也不能断言\x01",
            "那就是正确的选择吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#00100F嗯……我明白。\x01",
            "正是因为有着那样的过去，\x01",
            "才造就了现在的自己。\x02\x03",

            "#00104F但是，无论以哪种形式都好，\x01",
            "我只希望爸爸和妈妈\x01",
            "都能幸福快乐……\x02\x03",

            "#00100F……呵呵，对不起，\x01",
            "和你说了些奇怪的话。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#00004F不……没有的事。\x02\x03",

            "#00000F我也来许愿吧……\x01",
            "希望艾莉的父母能获得幸福。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#00109F呵呵，谢谢。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_4DF4 end

    def Function_29_5713(): pass

    label("Function_29_5713")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57D7")

    #C0176
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#00200F我觉得只要在脑海中\x01",
            "暗想一下就可以了。\x02\x03",

            "我们试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5832")

    label("loc_57D7")


    #C0178
    ChrTalk(
        0x101,
        (
            "#00000F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        "#00200F好的，我们试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_5832")

    BeginChrThread(0x103, 3, 0, 26)
    WaitChrThread(0x103, 3)

    #C0180
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0181
    ChrTalk(
        0x103,
        "#00203F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x103, 3, 0, 27)
    WaitChrThread(0x103, 3)
    Call(0, 24)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)

    #C0182
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#00204F……嗯，我也许好了。\x02\x03",

            "#00200F作为参考，我想问问\x01",
            "罗伊德前辈许了什么愿望。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A51")

    #C0184
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括琪雅、你，\x01",
            "还有支援科的同伴们。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#00200F原来如此……\x01",
            "真符合罗伊德前辈的风格。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢称赞。\x02\x03",

            "#00000F对了，缇欧，\x01",
            "你许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B53")

    label("loc_5A51")


    #C0187
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望缇欧的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        (
            "#00200F原来如此……\x01",
            "那真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，不用客气。\x02\x03",

            "#00000F对了，缇欧，\x01",
            "你许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B53")


    #C0190
    ChrTalk(
        0x103,
        (
            "#00203F……『希望罗伯兹主任\x01",
            "以后别再那么烦人』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0x101,
        "#00012F主、主任好可怜……\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x103,
        (
            "#00202F……开个玩笑而已。\x02\x03",

            "#00203F我的愿望是……\x01",
            "『希望能找到自己的\x01",
            "　生存意义』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0193
    ChrTalk(
        0x103,
        (
            "#00200F以前告诉过\x01",
            "大家。\x02\x03",

            "#00203F三年前，我想询问盖伊先生，\x01",
            "但最终却没能问成这个问题……\x02\x03",

            "#00208F如今虽然已经彻底解决了教团事件，\x01",
            "但我仍然没有找到答案。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#00004F……缇欧，我不是说过吗？\x01",
            "没有多少人能答出\x01",
            "那个问题。\x02\x03",

            "#00000F你不必如此焦虑地寻找答案，\x01",
            "更不必独自寻找。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        (
            "#00204F嗯，我明白。\x02\x03",

            "#00200F我并没有焦虑，\x01",
            "而且现在已经知道\x01",
            "大家都会帮助我了。\x02\x03",

            "#00203F但这个问题可以说是\x01",
            "关乎我整个人生的一大命题。\x02\x03",

            "#00200F所以总有一天要找到答案。\x01",
            "……我向『镜子』许的愿，\x01",
            "也包含着表明决心的意思。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#00000F……哈哈，原来如此，\x01",
            "抱歉，看来是我多虑了。\x02\x03",

            "#00004F既然如此，那我也再次\x01",
            "表明自己的意愿吧。\x02\x03",

            "#00000F希望你有朝一日\x01",
            "找到那个问题的答案……\x01",
            "而我们也会帮助你一起前进的。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x103,
        (
            "#00209F呵呵……\x01",
            "那就先谢谢大家了。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_5713 end

    def Function_30_5F0D(): pass

    label("Function_30_5F0D")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FCF")

    #C0198
    ChrTalk(
        0x101,
        (
            "#00000F好，我们这就\x01",
            "开始许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        (
            "#00300F我觉得只要在脑子里\x01",
            "想想就行了。\x02\x03",

            "好，试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6028")

    label("loc_5FCF")


    #C0200
    ChrTalk(
        0x101,
        (
            "#00000F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x104,
        "#00300F那我们就试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6028")

    BeginChrThread(0x104, 3, 0, 26)
    WaitChrThread(0x104, 3)

    #C0202
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0203
    ChrTalk(
        0x104,
        "#00303F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x104, 3, 0, 27)
    WaitChrThread(0x104, 3)
    Call(0, 24)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)

    #C0204
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x104,
        (
            "#00304F嗯，我也许完了。\x02\x03",

            "#00309F对了，罗伊德，\x01",
            "你许了个什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_624B")

    #C0206
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括琪雅、你，\x01",
            "还有支援科的同伴们。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        (
            "#00300F哈哈，你真是个\x01",
            "一本正经的家伙。\x02\x03",

            "#00306F就算许个比较\x01",
            "注重私欲的愿望，\x01",
            "也不会遭天谴啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#00005F那、那你许了\x01",
            "什么愿呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6374")

    label("loc_624B")


    #C0209
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望兰迪的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        (
            "#00305F哦哦，真的吗！？\x02\x03",

            "#00309F哎呀～不愧是罗伊德，\x01",
            "你这愿望许得太是时候了！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0211
    ChrTalk(
        0x101,
        (
            "#00005F哎……？你许了\x01",
            "什么愿呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6374")


    #C0212
    ChrTalk(
        0x104,
        (
            "#00304F我吗？那还用问，当然是\x01",
            "『把克洛斯贝尔的大姐姐\x01",
            "  全都收进我的──』\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#00003F明白了，不用再说下去了，\x01",
            "我根本就不该问啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x104,
        (
            "#00305F喂喂，每个男人\x01",
            "都会有这种梦想吧？\x02\x03",

            "#00304F塞茜尔小姐等护士姐姐，\x01",
            "还有游击士艾欧莉娅小姐……\x02\x03",

            "#00309F克洛斯贝尔有着很多\x01",
            "我喜欢的大姐姐呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00006F喂……不要把塞茜尔姐姐\x01",
            "也放到你的妄想中啊。\x02\x03",

            "#00002F……不过，这倒是让我放心了，\x01",
            "反正那种愿望绝对不可能实现。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0216
    ChrTalk(
        0x104,
        (
            "#00306F居、居然说得\x01",
            "这么过分……\x02\x03",

            "#00300F……嘿嘿～我明白啦，\x01",
            "其实你是在羡慕吧？\x02\x03",

            "#00304F放心吧，\x01",
            "等我实现愿望之后，\x01",
            "也会让你开心一下的……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00011F我、我才没有\x01",
            "那种想法呢！\x02\x03",

            "#00006F……呼，真是的。\x01",
            "反正已经许过愿了，我们这就走吧。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 31)
    OP_93(0x104, 0xE1, 0x1F4)
    Sleep(1500)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    WaitChrThread(0x101, 3)
    OP_64(0x104)

    #C0218
    ChrTalk(
        0x104,
        (
            "#00308F（绝对不可能实现吗……）\x02\x03",

            "#00303F（『永远都是大家的同伴』……\x01",
            "  对我来说，这个愿望终究是奢求吧。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_93(0x104, 0xE1, 0x1F4)
    OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    Return()

    # Function_30_5F0D end

    def Function_31_66D1(): pass

    label("Function_31_66D1")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    Return()

    # Function_31_66D1 end

    def Function_32_66E8(): pass

    label("Function_32_66E8")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_67AC")

    #C0219
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x109,
        (
            "#10100F我觉得只要在脑海中\x01",
            "想一想就可以了。\x02\x03",

            "好啦，试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6816")

    label("loc_67AC")


    #C0221
    ChrTalk(
        0x101,
        (
            "#00000F好，我们来\x01",
            "许愿吧。\x02\x03",

            "只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x109,
        "#10100F嗯，试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_6816")

    BeginChrThread(0x109, 3, 0, 26)
    WaitChrThread(0x109, 3)

    #C0223
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0224
    ChrTalk(
        0x109,
        "#10103F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x109, 3, 0, 27)
    WaitChrThread(0x109, 3)
    Call(0, 24)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)

    #C0225
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x109,
        (
            "#10104F嗯，我也许完了。\x02\x03",

            "#10100F……请问，罗伊德警官\x01",
            "许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6A23")

    #C0227
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括警备队的成员们，\x01",
            "还有支援科的同伴们。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x109,
        "#10100F原来如此，真符合罗伊德警官的作风啊。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢称赞。\x02\x03",

            "诺艾尔，\x01",
            "你许了什么愿呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6B1F")

    label("loc_6A23")


    #C0230
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望诺艾尔的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        (
            "#10100F哈哈……\x01",
            "非常感谢。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，不用客气。\x02\x03",

            "#00000F对了，诺艾尔，\x01",
            "你许了什么愿呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6B1F")


    #C0233
    ChrTalk(
        0x109,
        (
            "#10100F我的愿望很简单。\x01",
            "那就是……\x01",
            "『希望能成为出色的警备队员』。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……真是个率直的愿望，\x01",
            "很符合你的风格啊。\x02\x03",

            "#00000F你是不是把父亲视为了\x01",
            "自己的目标？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x109,
        (
            "#10100F哈哈……之前也说过，\x01",
            "关于那方面的事情，其实我并没有特别明确的想法。\x02\x03",

            "#10104F爸爸在世时，我年纪还小，\x01",
            "他对我们的管教十分严厉，\x01",
            "老实说，我对他其实有些害怕。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        "#00005F哦？这样啊。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x109,
        (
            "#10102F嗯，他是个非常严厉的人。\x02\x03",

            "#10104F只要我和芙兰\x01",
            "做了什么恶作剧，他就会\x01",
            "毫不留情地一拳挥下来……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0238
    ChrTalk(
        0x109,
        (
            "#10103F……说起来，妈妈曾带我\x01",
            "探望过在边境大门工作的爸爸，\x01",
            "不过只有一次而已。\x02\x03",

            "#10108F他虽然对当时的扭曲体制深感忧虑，\x01",
            "但身为一名克洛斯贝尔的守卫者，\x01",
            "始终都严于律己……\x02\x03",

            "#10100F如今想想……\x01",
            "我似乎一直都对恪尽职守\x01",
            "的爸爸抱有尊敬呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        (
            "#00002F这样啊……\x01",
            "看来你那严于律己的性格\x01",
            "果然是因为受他的影响。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x109,
        (
            "#10109F哈哈，我想也是。\x02\x03",

            "#10103F话说回来，\x01",
            "我直到现在都不明白芙兰的\x01",
            "性格为何会那么散漫随意。\x02\x03",

            "#10101F……难道爸爸\x01",
            "在暗地里只对芙兰\x01",
            "一个人很宽容吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0241
    ChrTalk(
        0x101,
        (
            "#00012F这个嘛……也有可能是\x01",
            "过于严厉的管教造成了反效果吧。\x02\x03",

            "#00000F……我们已经许完愿了，\x01",
            "差不多也该走啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x109,
        "#10100F嗯，说的也是。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_66E8 end

    def Function_33_6F86(): pass

    label("Function_33_6F86")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_704B")

    #C0243
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x105,
        (
            "#10300F只要在脑海中\x01",
            "暗想一下就\x01",
            "可以了吧？\x02\x03",

            "我们赶快试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_70BC")

    label("loc_704B")


    #C0245
    ChrTalk(
        0x101,
        (
            "#00000F好，我们来\x01",
            "许愿吧。\x02\x03",

            "#00004F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x105,
        "#10300F嗯，试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_70BC")

    BeginChrThread(0x105, 3, 0, 26)
    WaitChrThread(0x105, 3)

    #C0247
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0248
    ChrTalk(
        0x105,
        "#10303F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x105, 3, 0, 27)
    WaitChrThread(0x105, 3)
    Call(0, 24)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)

    #C0249
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x105,
        (
            "#10304F我也好了。\x02\x03",

            "#10300F对了，你许了\x01",
            "什么愿？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_72AC")

    #C0251
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括琪雅、你，\x01",
            "还有支援科的同伴们。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x105,
        "#10300F呵呵，真符合你的作风。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢称赞。\x02\x03",

            "#00000F对了，瓦吉，\x01",
            "你许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73AE")

    label("loc_72AC")


    #C0254
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望瓦吉的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x105,
        (
            "#10300F呵呵，你可真是个\x01",
            "老好人啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，哪里哪里。\x02\x03",

            "#00000F对了，瓦吉，\x01",
            "你许了个什么愿望？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_73AE")


    #C0257
    ChrTalk(
        0x105,
        (
            "#10302F呵呵，简单来说就是……\x02\x03",

            "#10304F『希望我以前的打架对手\x01",
            "能找到自己的道路』。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0258
    ChrTalk(
        0x101,
        (
            "#00008F……我也听到传闻了……\x01",
            "据说瓦鲁多最近已经\x01",
            "很少在他们的据点露面了。\x02\x03",

            "#00003F不过，那不是你的错吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x105,
        (
            "#10309F我并没有因自责\x01",
            "而沉浸在伤感之中。\x02\x03",

            "#10300F他在雨天的那场决斗\x01",
            "之后会萎靡颓废，\x01",
            "也在我的预料之中。\x02\x03",

            "#10304F今后会一直颓废下去，\x01",
            "还是放开一切，继续前进……\x01",
            "终究是瓦鲁多自己的问题。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0260
    ChrTalk(
        0x101,
        (
            "#00006F这种想法真是有点冷漠啊……\x02\x03",

            "#00000F不过，如果你真的这样想，\x01",
            "也就不会许下『希望瓦鲁多找到\x01",
            "自己的道路』这种愿望了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x105,
        (
            "#10304F呵呵，你说的没错……\x01",
            "但这个愿望也关系到我自己。\x02\x03",

            "#10300F如果他今后一直颓废下去……\x01",
            "就说明我在雨天的那场决斗中\x01",
            "并没有将想要传达的意思传达给他。\x02\x03",

            "#10303F换句话说，也就是我根本\x01",
            "没能做出了断……\x02\x03",

            "#10309F这未免也太丢人了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#00006F……唉，真是的，\x01",
            "瓦吉，你太不坦率了。\x02\x03",

            "#00000F不过，瓦鲁多和剑蛇帮的\x01",
            "成员们能找到自己的道路……\x01",
            "也是我希望看到的结果。\x02\x03",

            "但愿这个愿望能实现。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x105,
        (
            "#10303F呵呵，你果然是个老好人。\x02\x03",

            "#10309F我太喜欢你这种性格了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0264
    ChrTalk(
        0x101,
        (
            "#00006F真是的，我好不容易\x01",
            "才做了个总结性发言……\x01",
            "你就别再开玩笑了！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_6F86 end

    def Function_34_7818(): pass

    label("Function_34_7818")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_78DC")

    #C0265
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x153,
        (
            "#01100F只要在这面镜子前\x01",
            "说出愿望就可以了吧～？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#00000F哦，我觉得只要在\x01",
            "脑中想想就可以了。\x02\x03",

            "……我们这就试试吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7949")

    label("loc_78DC")


    #C0268
    ChrTalk(
        0x101,
        (
            "#00000F好，我们来\x01",
            "许愿吧。\x02\x03",

            "#00004F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x153,
        "#01100F我知道了～\x02",
    )

    CloseMessageWindow()

    label("loc_7949")

    BeginChrThread(0x153, 3, 0, 26)
    WaitChrThread(0x153, 3)

    #C0270
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0271
    ChrTalk(
        0x153,
        "#01103F……嗯…………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 27)
    WaitChrThread(0x153, 3)
    Call(0, 24)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)

    #C0272
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x153,
        (
            "#01109F嗯！我也许好啦～！\x02\x03",

            "#01105F罗伊德，\x01",
            "你许了什么愿望～？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7B3D")

    #C0274
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括琪雅，\x01",
            "还有支援科的同伴们。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x153,
        "#01109F嘿嘿……不愧是罗伊德啊。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢夸奖。\x02\x03",

            "#00000F那你呢？\x01",
            "许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7C2C")

    label("loc_7B3D")


    #C0277
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望琪雅的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x153,
        "#01109F嘿嘿……谢谢～\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，不用客气。\x02\x03",

            "#00000F琪雅，你许了\x01",
            "什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7C2C")


    #C0280
    ChrTalk(
        0x153,
        (
            "#01106F嗯……其实我有很多\x01",
            "想许的愿望……\x02\x03",

            "#01100F但最大的愿望还是\x01",
            "『希望小滴的眼睛痊愈』～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x101,
        (
            "#00003F……嗯，真希望她能痊愈啊。\x02\x03",

            "#00008F听说小滴的眼部手术\x01",
            "是个难度相当高的手术……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x153,
        (
            "#01111F但是，只要对着这面镜子许愿，\x01",
            "就可以成真了吧～？\x02\x03",

            "#01101F所以我会不断许愿的，\x01",
            "无论多少次都可以！\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……说的对，\x01",
            "我也来认真地许愿吧。\x02\x03",

            "#00004F（真希望……能发生\x01",
            "  奇迹啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x153, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_93(0x153, 0x0, 0x1F4)

    #C0284
    ChrTalk(
        0x153,
        "#01111F…………………………？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0285
    ChrTalk(
        0x101,
        "#00005F怎么了？琪雅。\x02",
    )

    CloseMessageWindow()
    OP_93(0x153, 0x10E, 0x1F4)

    #C0286
    ChrTalk(
        0x153,
        (
            "#01103F……嗯，没什么～\x02\x03",

            "#01109F不说这个啦，罗伊德，\x01",
            "我们再去摇响大钟吧～！\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x153, 3, 0, 35)
    OP_93(0x101, 0x87, 0x1F4)
    WaitChrThread(0x153, 3)
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0287
    ChrTalk(
        0x101,
        (
            "#00009F哈哈……\x01",
            "你真是精力过剩啊。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_7818 end

    def Function_35_7EE9(): pass

    label("Function_35_7EE9")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
    Return()

    # Function_35_7EE9 end

    def Function_36_7F00(): pass

    label("Function_36_7F00")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7FC9")

    #C0288
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x156,
        (
            "#06400F我觉得只要在脑中\x01",
            "想一想那个愿望\x01",
            "就可以了～\x02\x03",

            "这就试试看吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8044")

    label("loc_7FC9")


    #C0290
    ChrTalk(
        0x101,
        (
            "#00000F好，我们开始\x01",
            "许愿吧。\x02\x03",

            "#00004F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x156,
        "#06400F好，我们赶快试试看吧！\x02",
    )

    CloseMessageWindow()

    label("loc_8044")

    BeginChrThread(0x156, 3, 0, 26)
    WaitChrThread(0x156, 3)

    #C0292
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0293
    ChrTalk(
        0x156,
        "#06403F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x156, 3, 0, 27)
    WaitChrThread(0x156, 3)
    Call(0, 24)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)

    #C0294
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x156,
        (
            "#06400F嗯，我也许愿完毕了～\x02\x03",

            "#06409F对了，罗伊德警官\x01",
            "许了什么愿望呢～？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8250")

    #C0296
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括你，\x01",
            "还有警察局的其他同伴。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x156,
        "#06402F呵呵，果然很符合罗伊德警官的作风～\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，多谢夸奖。\x02\x03",

            "#00000F芙兰，你许了\x01",
            "什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8347")

    label("loc_8250")


    #C0299
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望芙兰的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x156,
        "#06402F呵呵，那真是太感谢啦～\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，不用客气。\x02\x03",

            "#00000F芙兰，你许了\x01",
            "什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8347")


    #C0302
    ChrTalk(
        0x156,
        (
            "#06409F呵呵，\x01",
            "我的愿望自然是\x01",
            "『希望变得像姐姐那样』～\x02\x03",

            "#06401F成为姐姐那种\x01",
            "又帅气又可靠的女性，\x01",
            "是我永远的目标！\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#00012F像诺艾尔一样的女性吗……\x01",
            "哈哈，真不愧是最爱姐姐的芙兰啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0304
    ChrTalk(
        0x101,
        (
            "#00005F对了，我有个小问题……\x01",
            "你有没有想过加入警备队？\x02\x03",

            "#00000F既然那么喜欢诺艾尔，\x01",
            "应该很想和她一起\x01",
            "在警备队工作吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x156,
        (
            "#06400F哈哈，这倒是没错～\x01",
            "但每个人都有自己\x01",
            "最适合的岗位。\x02\x03",

            "#06403F我在警察学校读书时，\x01",
            "事务系的成绩就明显比训练成绩好……\x02\x03",

            "#06400F所以我当时就在想，要用最适合\x01",
            "自己的方法来守护克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00000F嗯，确实如你所说，守护克洛斯贝尔的人\x01",
            "并不是只有在第一线工作的成员。\x02\x03",

            "#00004F正是因为有作战总部和联络员的支援，\x01",
            "我们才能在任务现场大展身手……\x02\x03",

            "#00009F从这层意义上说，\x01",
            "你的确最适合在接待处工作……\x01",
            "这份工作很适合你呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x156,
        (
            "#06409F嘿嘿……\x01",
            "受到如此称赞，\x01",
            "还真有些不好意思呢。\x02\x03",

            "#06400F总之，『希望变得像姐姐那样』\x01",
            "这个愿望，也是以保持自我\x01",
            "特点为前提条件的。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        (
            "#00002F哈哈，原来如此。\x02\x03",

            "#00000F……好啦，我们已经\x01",
            "许愿完毕，\x01",
            "差不多也该走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x156,
        "#06409F好的，我们走吧～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_36_7F00 end

    def Function_37_8742(): pass

    label("Function_37_8742")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_880D")

    #C0310
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x14C,
        (
            "#05900F我觉得只要在头脑中\x01",
            "想一想那个愿望\x01",
            "就可以了。\x02\x03",

            "这就试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_887E")

    label("loc_880D")


    #C0312
    ChrTalk(
        0x101,
        (
            "#00000F好，我们来\x01",
            "许愿吧。\x02\x03",

            "#00004F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x14C,
        "#05900F嗯，试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_887E")

    BeginChrThread(0x14C, 3, 0, 26)
    WaitChrThread(0x14C, 3)

    #C0314
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0315
    ChrTalk(
        0x14C,
        "#05903F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x14C, 3, 0, 27)
    WaitChrThread(0x14C, 3)
    Call(0, 24)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)

    #C0316
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x14C,
        (
            "#05904F嗯，我也许好啦。\x02\x03",

            "#05900F罗伊德，\x01",
            "你许了什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8A86")

    #C0318
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括塞茜尔姐姐，\x01",
            "还有支援科的同伴们。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x14C,
        "#05902F呵呵，很符合你的作风呢。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢夸奖。\x02\x03",

            "#00000F对了，塞茜尔姐姐，\x01",
            "你许了什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8B8B")

    label("loc_8A86")


    #C0321
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望塞茜尔姐姐的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x14C,
        "#05902F呵呵，谢谢，罗伊德。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，不用客气。\x02\x03",

            "#00000F对了，塞茜尔姐姐你\x01",
            "许了个什么愿呢？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8B8B")


    #C0324
    ChrTalk(
        0x14C,
        (
            "#05900F我的愿望自然是……\x01",
            "『希望罗伊德和大家\x01",
            "永远健康精神』。\x02\x03",

            "#05904F对我来说，\x01",
            "这就是最大的愿望了。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#00004F……谢谢，塞茜尔姐姐。\x02\x03",

            "#00000F我们一定多加注意，\x01",
            "绝不会身负重伤，\x01",
            "被送到医院去的。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x14C,
        (
            "#05909F呵呵，一定要说到做到哦。\x02\x03",

            "#05901F如果不遵守约定，\x01",
            "我到时一定会给你们多扎几管\x01",
            "疼得能让人掉眼泪的针。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0327
    ChrTalk(
        0x101,
        (
            "#00006F（若是如此，兰迪也许会\x01",
            "  很高兴吧……）\x02\x03",

            "#00000F……塞茜尔姐姐，你也一样，\x01",
            "工作时别太拼命，\x01",
            "偶尔也要休息一下哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x14C,
        (
            "#05905F唔……只要一想到患者们，\x01",
            "我就想竭尽全力地\x01",
            "投身于工作中。\x02\x03",

            "#05909F不过，我时常也会像现在\x01",
            "这样适当休息的，不用担心。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#00006F哪有，你明明只在\x01",
            "很偶尔的情况下才会\x01",
            "稍微休息一下……\x02\x03",

            "#00001F我一直都很担心\x01",
            "塞茜尔姐姐啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x14C,
        (
            "#05904F嗯……说的也是，我明白了。\x01",
            "我以后一定注意一些，\x01",
            "不会太勉强自己的。\x02\x03",

            "#05909F呵呵，话说回来，\x01",
            "你居然担心起姐姐了……\x01",
            "还真是长大了呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0331
    ChrTalk(
        0x101,
        "#00006F你又把我当小孩子看待了……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x14C,
        "#05902F呵呵，抱歉抱歉。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#00002F（……塞茜尔姐姐果然\x01",
            "　还是『姐姐』啊。）\x02\x03",

            "#00006F（……总觉得有些失落。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_37_8742 end

    def Function_38_8F96(): pass

    label("Function_38_8F96")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9054")

    #C0334
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x134,
        (
            "#01700F我看只要在脑子里\x01",
            "想一想就行了。\x02\x03",

            "赶快试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_90CB")

    label("loc_9054")


    #C0336
    ChrTalk(
        0x101,
        (
            "#00000F好，我们开始\x01",
            "许愿吧。\x02\x03",

            "#00004F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x134,
        "#01700F好，赶快试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_90CB")

    BeginChrThread(0x134, 3, 0, 26)
    WaitChrThread(0x134, 3)

    #C0338
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0339
    ChrTalk(
        0x134,
        "#01703F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x134, 3, 0, 27)
    WaitChrThread(0x134, 3)
    Call(0, 24)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)

    #C0340
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x134,
        (
            "#01704F嗯，我也已经许好了。\x02\x03",

            "#01700F对了，警察弟弟，\x01",
            "你许了什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_92E0")

    #C0342
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括伊莉娅小姐，\x01",
            "还有彩虹剧团的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x134,
        (
            "#01702F呵呵，原来如此，\x01",
            "这愿望很不错呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，多谢夸奖。\x02\x03",

            "#00000F伊莉娅小姐，\x01",
            "您许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_93E6")

    label("loc_92E0")


    #C0345
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望伊莉娅小姐的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x134,
        (
            "#01702F哎呀，警察弟弟\x01",
            "还真懂事啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，谢谢夸奖。\x02\x03",

            "#00000F伊莉娅小姐，\x01",
            "您许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_93E6")


    #C0348
    ChrTalk(
        0x134,
        (
            "#01704F我的愿望当然是\x01",
            "『无论发生什么事\x01",
            "都可以继续跳舞』。\x02\x03",

            "#01700F不过，其实也不用特地来许愿，\x01",
            "反正我是绝对不可能\x01",
            "离开舞台的。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，真不愧是伊莉娅小姐，\x01",
            "对舞台的执著\x01",
            "真是无人能及呢。\x02\x03",

            "#00009F这种热情一直都让我\x01",
            "感到很吃惊，\x01",
            "它究竟是从哪里涌出来的呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x134,
        (
            "#01703F唔……这个嘛，\x01",
            "简单来说……\x02\x03",

            "#01700F那就是因为我\x01",
            "比任何人都『喜欢』\x01",
            "在舞台上跳舞。\x02\x03",

            "单论这一点，我有自信不会\x01",
            "输给整个大陆的任何人……\x02\x03",

            "#01709F只要这种感情不变，\x01",
            "我可以一直起舞到生命的终点。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00005F『喜欢』吗……\x01",
            "听起来很单纯，\x01",
            "但我似乎可以理解。\x02\x03",

            "#00004F能有如此强烈的感情，\x01",
            "恐怕也是您的过人之处啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x134,
        (
            "#01700F呵呵，这不算什么。\x01",
            "所谓的『喜欢』，\x01",
            "是每个人都有的感情啊。\x02\x03",

            "#01709F警察弟弟也一样，为了重要的人，\x01",
            "你也可以赌上性命吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x101,
        (
            "#00000F嗯……是啊。\x02\x03",

            "#00004F（当时正是因为有着\x01",
            "  想要保护琪雅的强烈感情，\x01",
            "  才能将教团事件解决…… ）\x02\x03",

            "（人类这种生物，为了重要的事物，\x01",
            "  就可以变得无比强大。）\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x134,
        (
            "#01700F呵呵，看来你已经理解了呢。\x02\x03",

            "#01709F……好啦，已经许愿完毕，\x01",
            "我们差不多也该走了。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x101,
        "#00000F嗯，说的也是。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_38_8F96 end

    def Function_39_97F1(): pass

    label("Function_39_97F1")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98D3")

    #C0356
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x135,
        (
            "#01802F我觉得，只要在脑海中\x01",
            "暗想一下自己的愿望\x01",
            "就可以了。\x02\x03",

            "#01803F……好了，这就试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_994E")

    label("loc_98D3")


    #C0358
    ChrTalk(
        0x101,
        (
            "#00000F好，我们开始\x01",
            "许愿吧。\x02\x03",

            "#00004F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x135,
        "#01803F……嗯，这就试试看吧。\x02",
    )

    CloseMessageWindow()

    label("loc_994E")

    BeginChrThread(0x135, 3, 0, 26)
    WaitChrThread(0x135, 3)

    #C0360
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0361
    ChrTalk(
        0x135,
        "#01803F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x135, 3, 0, 27)
    WaitChrThread(0x135, 3)
    Call(0, 24)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)

    #C0362
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x135,
        (
            "#01804F嗯，我也已经许好了。\x02\x03",

            "#01802F对了，罗伊德警官，\x01",
            "你许了什么愿望呢？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B6B")

    #C0364
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括你，\x01",
            "还有彩虹剧团的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x135,
        (
            "#01802F……原来如此。\x01",
            "呵呵，真符合罗伊德警官的作风呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，多谢夸奖。\x02\x03",

            "#00000F莉夏，你呢？\x01",
            "你许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9C67")

    label("loc_9B6B")


    #C0367
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望莉夏的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x135,
        (
            "#01802F……这样啊。\x01",
            "呵呵，真是太感谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，不用客气。\x02\x03",

            "#00000F那你许了\x01",
            "什么愿望？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9C67")

    OP_63(0x135, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x135)

    #C0370
    ChrTalk(
        0x135,
        (
            "#01803F我的愿望是……\x01",
            "『成为一名像伊莉娅小姐\x01",
            "那样的舞蹈演员』。\x02\x03",

            "#01802F呵呵，其实我只是个新人而已，\x01",
            "许这种愿望或许有些不自量力。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#00000F不……\x01",
            "没有的事。\x02\x03",

            "#00003F你的表演已经得到了\x01",
            "观众们的高度评价……\x02\x03",

            "#00000F更重要的是，连伊莉娅小姐\x01",
            "都承认你的才能。\x02\x03",

            "#00009F你只要继续努力下去，\x01",
            "将来一定能成为像伊莉娅小姐\x01",
            "那样的超级大明星。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0372
    ChrTalk(
        0x135,
        (
            "#01809F太、太过奖了……\x01",
            "我真的还差得很远。\x02\x03",

            "#01804F而且我觉得修利的才能\x01",
            "要比我强得多。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#00004F唔……你应该再\x01",
            "自信些才对。\x02\x03",

            "#00000F总之，希望你的愿望早日实现，\x01",
            "我会一直支持你的……\x01",
            "今后也要继续努力哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x135,
        "#01809F好、好的，谢谢。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#00012F哈哈，当面说这样的话，\x01",
            "还真有点不好意思呢。\x02\x03",

            "#00000F……好，我们已经许过愿了，\x01",
            "差不多也该走啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x135,
        "#01802F嗯，是啊。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x101, 3, 0, 31)
    Sleep(150)
    OP_93(0x135, 0xE1, 0x1F4)
    Sleep(650)
    OP_9B(0x0, 0x135, 0x0, 0x4B0, 0x7D0, 0x0)
    OP_63(0x135, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x135)

    #C0377
    ChrTalk(
        0x135,
        (
            "#01803F#11P（虽然是个绝对\x01",
            "  不可能实现的愿望……）\x02\x03",

            "#01808F（但只是幻想一下\x01",
            "  总可以吧……？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_9B(0x0, 0x135, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    EndChrThread(0x101, 0x3)
    Return()

    # Function_39_97F1 end

    def Function_40_A016(): pass

    label("Function_40_A016")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A0D5")

    #C0378
    ChrTalk(
        0x101,
        (
            "#00000F好，这就开始\x01",
            "许愿吧。\x02\x03",

            "#00005F嗯……只要在这面镜子前\x01",
            "把愿望说出来就可以了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x166,
        (
            "#14000F在脑子里想想\x01",
            "就行啦。\x02\x03",

            "#14003F要试的话就赶快吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A155")

    label("loc_A0D5")


    #C0380
    ChrTalk(
        0x101,
        (
            "#00000F好，我们开始\x01",
            "许愿吧。\x02\x03",

            "#00004F只要在这面镜子前\x01",
            "暗想一下自己的愿望就可以了。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x166,
        (
            "#14003F……嗯，要试的话\x01",
            "就赶快吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A155")

    BeginChrThread(0x166, 3, 0, 26)
    WaitChrThread(0x166, 3)

    #C0382
    ChrTalk(
        0x101,
        "#00003F……………………………………\x02",
    )

    CloseMessageWindow()

    #C0383
    ChrTalk(
        0x166,
        "#14008F……………………………………\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x166, 3, 0, 27)
    WaitChrThread(0x166, 3)
    Call(0, 24)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)

    #C0384
    ChrTalk(
        0x101,
        "#00000F……我已经许好了。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x166,
        (
            "#14003F嗯，我也许完了。\x02\x03",

            "#14000F……对了，你许了\x01",
            "什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A352")

    #C0386
    ChrTalk(
        0x101,
        (
            "#00000F哈哈，那愿望太过普通了，\x01",
            "说出来还真有点不好意思……\x02\x03",

            "#00004F『希望今后也能继续守护\x01",
            "　克洛斯贝尔』。\x02\x03",

            "#00000F当然，这其中也包括你，\x01",
            "还有彩虹剧团的各位。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x166,
        (
            "#14000F哼、哼……\x01",
            "这愿望还算不错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        (
            "#00009F哈哈，多谢夸奖。\x02\x03",

            "#00000F修利，你呢？\x01",
            "你许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A450")

    label("loc_A352")


    #C0389
    ChrTalk(
        0x101,
        (
            "#00000F其实我第一次来的时候，\x01",
            "就已经许下了最想实现的愿望。\x02\x03",

            "#00004F同样的愿望总不能再许一次，\x01",
            "所以我这次许的愿望是\x01",
            "『希望修利的愿望能够实现』。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x166,
        "#14006F啧，不用你瞎操心。\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#00000F哈哈……\x01",
            "是我太多事了。\x02\x03",

            "#00000F修利，你呢？\x01",
            "你许了什么愿望？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A450")

    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    #C0392
    ChrTalk(
        0x166,
        (
            "#14003F我……\x01",
            "我根本就没有愿望。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#00006F喂……这算什么啊。\x01",
            "问完别人之后，自己却不说。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x166,
        (
            "#14006F……愿望这种东西，\x01",
            "原本就不是可以轻易实现的。\x02\x03",

            "#14008F在我以前待的贫民窟就是这样。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0395
    ChrTalk(
        0x166,
        (
            "#14000F……我的故乡\x01",
            "还有很多像我\x01",
            "这样的人。\x02\x03",

            "#14003F虽然我流浪到了克洛斯贝尔，\x01",
            "还在机缘巧合下被伊莉娅小姐发现……\x01",
            "但这只是运气好而已。\x02\x03",

            "#14008F和别人相比，我已经有了如此好运，\x01",
            "如果再祈求更多的愿望，\x01",
            "未免也太过贪心了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0396
    ChrTalk(
        0x101,
        (
            "#00004F修利……\x01",
            "……你真善良啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x166,
        "#14005F……哎……？\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#00002F很少人能像你这样，\x01",
            "为他人考虑\x01",
            "这么多。\x02\x03",

            "#00004F这说明你有一颗温柔善良，\x01",
            "懂得为他人着想的心。\x02\x03",

            "#00000F不过……\x01",
            "这并不意味着你没有\x01",
            "获得幸福的权利吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x166,
        "#14008F可、可是……\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        (
            "#00000F你不必想得那么复杂。\x01",
            "让自己拥有一个愿望，\x01",
            "不也是一件很好的事吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0401
    ChrTalk(
        0x166,
        (
            "#14006F啊啊，好了好了，我知道啦……\x01",
            "你可真是个爱讲大道理的烦人老兄啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        "#00006F抱、抱歉，惹你心烦了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    #C0403
    ChrTalk(
        0x166,
        (
            "#14003F……虽然我没有预想过久远的将来，\x01",
            "但现在确实有一个很想实现的愿望。\x02\x03",

            "#14000F『希望这次的新版公演能取得成功』……\x01",
            "这就是我现在唯一的愿望。\x02\x03",

            "#14009F……这样的愿望也可以吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#00002F当然，这不是很好嘛。\x02\x03",

            "我也会发自内心地为你祈祷，\x01",
            "希望你的愿望能顺利实现。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x166,
        (
            "#14012F不、不要面对面地\x01",
            "说这种让人难为情的话！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_40_A016 end

    def Function_41_A965(): pass

    label("Function_41_A965")

    EventBegin(0x1)

    #C0406
    ChrTalk(
        0x101,
        (
            "#00000F我们的目标是最顶层，\x01",
            "赶快上去看看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, -950, -53650, 0)
    EventEnd(0x4)
    Return()

    # Function_41_A965 end

    def Function_42_A9AE(): pass

    label("Function_42_A9AE")

    EventBegin(0x1)

    #C0407
    ChrTalk(
        0x101,
        (
            "#00000F赶快到顶层的镜子前\x01",
            "许下愿望吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 40550, -13830, 180)
    EventEnd(0x4)
    Return()

    # Function_42_A9AE end

    def Function_43_A9F1(): pass

    label("Function_43_A9F1")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    StopEffect(0x9, 0x0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0408
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '塞姆里亚石碎片'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('塞姆里亚石碎片', 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 4)
    OP_65(0x6, 0x1)
    EventEnd(0x3)
    Return()

    # Function_43_A9F1 end

    SaveToFile()

Try(main)
