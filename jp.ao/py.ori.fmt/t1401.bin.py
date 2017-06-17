from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "観光客",                 # 1
        "観光客",                 # 2
        "観光客",                 # 3
        "観光客",                 # 4
        "SE制御",                 # 5
        "bt1410",                 # 6
        "bt1420",                 # 7
        "bt1400",                 # 8
        "bt1400",                 # 9
    ))

    ATBonus("ATBonus_37C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_C3DA", 15,  5,   5,   5,   10,  5,   25)
    Sepith("Sepith_C3D2", 10,  6,   6,   6,   1,   4,   10)

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
        "BattleInfo_6A4", 0x0000, 78, 6, 60, 6, 1, 20, 0, "bt1400", "Sepith_C3DA", 40, 30, 20, 10,
        (
            ("ms79600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
            ("ms79600.dat", "ms82300.dat", "ms82300.dat", "ms82300.dat", 0, 0, 0, 0, "MonsterBattlePostion_3AC", "MonsterBattlePostion_42C", "ed7450", "ed7453", "ATBonus_37C"),
        )
    )

    BattleInfo(
        "BattleInfo_5DC", 0x0000, 78, 6, 45, 6, 1, 20, 0, "bt1400", "Sepith_C3D2", 40, 30, 20, 10,
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
        "Function_4_12FC",         # 04, 4
        "Function_5_144D",         # 05, 5
        "Function_6_1487",         # 06, 6
        "Function_7_14C3",         # 07, 7
        "Function_8_14FF",         # 08, 8
        "Function_9_1533",         # 09, 9
        "Function_10_1B7C",        # 0A, 10
        "Function_11_21AE",        # 0B, 11
        "Function_12_21BE",        # 0C, 12
        "Function_13_2564",        # 0D, 13
        "Function_14_25D3",        # 0E, 14
        "Function_15_2642",        # 0F, 15
        "Function_16_26AB",        # 10, 16
        "Function_17_271A",        # 11, 17
        "Function_18_43F2",        # 12, 18
        "Function_19_5126",        # 13, 19
        "Function_20_5168",        # 14, 20
        "Function_21_547F",        # 15, 21
        "Function_22_54B1",        # 16, 22
        "Function_23_55BE",        # 17, 23
        "Function_24_5628",        # 18, 24
        "Function_25_5648",        # 19, 25
        "Function_26_5661",        # 1A, 26
        "Function_27_567A",        # 1B, 27
        "Function_28_56D8",        # 1C, 28
        "Function_29_615B",        # 1D, 29
        "Function_30_6B01",        # 1E, 30
        "Function_31_7409",        # 1F, 31
        "Function_32_7420",        # 20, 32
        "Function_33_7E1A",        # 21, 33
        "Function_34_884C",        # 22, 34
        "Function_35_9037",        # 23, 35
        "Function_36_904E",        # 24, 36
        "Function_37_9A36",        # 25, 37
        "Function_38_A400",        # 26, 38
        "Function_39_AE2D",        # 27, 39
        "Function_40_B7D8",        # 28, 40
        "Function_41_C29F",        # 29, 41
        "Function_42_C2EC",        # 2A, 42
        "Function_43_C339",        # 2B, 43
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12AB")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1234")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FD, 0)
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
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

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

    # Function_3_11AB end

    def Function_4_12FC(): pass

    label("Function_4_12FC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FD, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13FC")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x650, 1)"), scpexpr(EXPR_END)), "loc_1385")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x650),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FD, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_13F7")

    label("loc_1385")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x650),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x650),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13F7")

    Jump("loc_1441")

    label("loc_13FC")

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

    label("loc_1441")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_12FC end

    def Function_5_144D(): pass

    label("Function_5_144D")

    TalkBegin(0xFE)

    #C0007
    ChrTalk(
        0xFE,
        (
            "ああ、綺麗すぎて\x01",
            "ついつい見入ってしまうよ……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_5_144D end

    def Function_6_1487(): pass

    label("Function_6_1487")

    TalkBegin(0xFE)

    #C0008
    ChrTalk(
        0xFE,
        (
            "あのプラネタリウム、\x01",
            "なんてキレイなのかしら……\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_6_1487 end

    def Function_7_14C3(): pass

    label("Function_7_14C3")

    TalkBegin(0xFE)

    #C0009
    ChrTalk(
        0xFE,
        (
            "ふふ、あわてなくても\x01",
            "『鏡』は逃げやしないわよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_7_14C3 end

    def Function_8_14FF(): pass

    label("Function_8_14FF")

    TalkBegin(0xFE)

    #C0010
    ChrTalk(
        0xFE,
        (
            "ママー、早く早く！\x01",
            "こっちが階段だよー！\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_8_14FF end

    def Function_9_1533(): pass

    label("Function_9_1533")

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

    def lambda_15FD():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_15FD)
    Sleep(50)

    def lambda_1615():
        OP_9B(0x0, 0x102, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1615)
    Sleep(50)

    def lambda_162D():
        OP_9B(0x0, 0x103, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_162D)
    Sleep(50)

    def lambda_1645():
        OP_9B(0x0, 0x104, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1645)
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
        "#00101F#6Pこの光は……\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x103,
        (
            "#00201F#12Pどうやら霊力の粒子が\x01",
            "上に登っているみたいですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1876")
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
        "#00013F正面の入口が……！\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    #A0014
    AnonymousTalk(
        0x104,
        (
            "#00306Fああ……塞がってやがるな。\x02\x03",

            "#00301F代わりに左右に\x01",
            "入口が現れてやがる……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jump("loc_19CF")

    label("loc_1876")

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
            "#00301Fチッ、内部の構造が\x01",
            "変わってやがるぞ……！\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 140, -1, -1)

    #A0016
    AnonymousTalk(
        0x101,
        "#00005Fそうなのか……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(200, 140, -1, -1)

    #A0017
    AnonymousTalk(
        0x104,
        (
            "#00303Fああ、前に入った時は\x01",
            "正面の入口が開いていたが……\x02\x03",

            "#00301F代わりに今は左右に\x01",
            "入口が現れてやがる……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    label("loc_19CF")

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
            "#00106F#6P何度か来たことがあったけど\x01",
            "あんな仕掛けがあったなんて……\x02\x03",

            "#00108Fこれも“彼女”の仕業……？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#00203F#12P……奥の方から\x01",
            "奇妙な稼動音も聞こえます。\x02\x03",

            "#00201F進むのなら警戒は必要かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00003F#5Pとにかく何としても\x01",
            "最上階に辿り着くしかない……\x02\x03",

            "#00013Fアリオスさんを問い詰め、\x01",
            "キーアを取り戻すためにも……！\x02",
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

    # Function_9_1533 end

    def Function_10_1B7C(): pass

    label("Function_10_1B7C")

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

    def lambda_1CA2():
        OP_93(0x101, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1CA2)
    Sleep(30)

    def lambda_1CB2():
        OP_93(0x102, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1CB2)
    Sleep(30)

    def lambda_1CC2():
        OP_93(0x103, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1CC2)
    Sleep(30)

    def lambda_1CD2():
        OP_93(0x104, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1CD2)
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
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DBA")
    SetMessageWindowPos(50, 140, -1, -1)

    #A0021
    AnonymousTalk(
        0x101,
        "#00013Fやっと着いたか……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    #A0022
    AnonymousTalk(
        0x104,
        "#00301Fああ……最上階だ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1E0F")

    label("loc_1DBA")

    SetMessageWindowPos(50, 140, -1, -1)

    #A0023
    AnonymousTalk(
        0x101,
        "#00013F着いたのか……？\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(230, 140, -1, -1)

    #A0024
    AnonymousTalk(
        0x104,
        (
            "#00301Fああ……\x01",
            "ここが最上階だ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E0F")

    SetMessageWindowPos(70, 140, -1, -1)

    #A0025
    AnonymousTalk(
        0x102,
        (
            "#00108Fで、でも……\x01",
            "キーアちゃんもアリオスさんも\x01",
            "いないみたいだけど……\x02",
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
            "#00206F#6P……前に訪れた時には\x01",
            "気付きませんでしたが……\x02\x03",

            "#00201Fあの光っている大鏡の奥に\x01",
            "隠された空間があるようです。\x02",
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

    def lambda_1F8E():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1F8E)
    Sleep(50)

    def lambda_1F9E():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1F9E)
    Sleep(50)

    def lambda_1FAE():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1FAE)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x104, 0)

    #C0027
    ChrTalk(
        0x101,
        "#00005F#11P本当か……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#00203F#6Pはい、かなりの霊力が\x01",
            "渦巻くよう流れています。\x02\x03",

            "#00201F恐らくそこが終点かと。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x102,
        "#00103F#5P……そう…………\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#00304F#6P……どうやら何とか\x01",
            "追いつけたみてぇだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x101,
        (
            "#00003F#11Pああ……\x02\x03",

            "#00007Fみんな──装備の確認を！\x01",
            "絶対にキーアを取り戻すぞ！\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20F5():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_20F5)
    Sleep(50)

    def lambda_2105():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2105)
    Sleep(50)

    def lambda_2115():
        TurnDirection(0x104, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_2115)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)

    #C0032
    ChrTalk(
        0x102,
        "#00107F#5Pええっ……！\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x103,
        "#00201F#6Pはい……！\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x104,
        "#00307F#6P合点承知だ！\x02",
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

    # Function_10_1B7C end

    def Function_11_21AE(): pass

    label("Function_11_21AE")

    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    Return()

    # Function_11_21AE end

    def Function_12_21BE(): pass

    label("Function_12_21BE")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23C9")
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "淡い光の粒子が鏡に吸い込まれて行っている。\x07\x00\x02",
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
            "#00006F#6P（どうやらこのまま\x01",
            "  鏡の中に入れそうだ……）\x02\x03",

            "#00013F（……キーア……今行くぞ！）\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x183, 3)
    Jump("loc_2420")

    label("loc_23C9")

    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "淡い光の粒子が鏡に吸い込まれて行っている。\x02\x03",

            "このまま鏡の中に入れそうだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_2420")

    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "鏡の中に足を踏み入れる\x01",      # 0
            "その場を離れる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2480"),
        (1, "loc_2539"),
        (SWITCH_DEFAULT, "loc_2563"),
    )


    label("loc_2480")

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
    Jump("loc_2563")

    label("loc_2539")

    FadeToDark(500, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_37()
    SetChrPos(0x0, 0, 44500, -4000, 180)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Jump("loc_2563")

    label("loc_2563")

    Return()

    # Function_12_21BE end

    def Function_13_2564(): pass

    label("Function_13_2564")


    def lambda_2569():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2569)
    Sleep(500)
    Sound(341, 0, 100, 0)

    def lambda_2587():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2587)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_2564 end

    def Function_14_25D3(): pass

    label("Function_14_25D3")


    def lambda_25D8():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_25D8)
    Sleep(1000)

    def lambda_25F0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_25F0)
    Sound(920, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_14_25D3 end

    def Function_15_2642(): pass

    label("Function_15_2642")


    def lambda_2647():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_2647)
    Sleep(1000)

    def lambda_265F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_265F)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_15_2642 end

    def Function_16_26AB(): pass

    label("Function_16_26AB")


    def lambda_26B0():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_26B0)
    Sleep(1500)

    def lambda_26C8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_26C8)
    Sound(920, 0, 60, 0)
    PlayEffect(0x0, 0xFF, 0xFE, 0x0, 0, 1000, 1000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    WaitChrThread(0xFE, 2)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_26AB end

    def Function_17_271A(): pass

    label("Function_17_271A")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_40F8")
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

    def lambda_2826():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2826)
    Sleep(50)

    def lambda_283E():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_283E)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00000Fこれが《鏡の城》か。\x02\x03",

            "テーマパークの象徴とも言える\x01",
            "アトラクションだそうだけど……\x02\x03",

            "#00006F……なんというか、\x01",
            "凄いとしか言いようがないな。\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_293D"),
        (1, "loc_2B77"),
        (2, "loc_2D97"),
        (3, "loc_2FBA"),
        (4, "loc_31DF"),
        (5, "loc_3407"),
        (6, "loc_361C"),
        (7, "loc_3857"),
        (8, "loc_3A73"),
        (9, "loc_3C68"),
        (10, "loc_3E68"),
        (SWITCH_DEFAULT, "loc_40F3"),
    )


    label("loc_293D")


    #C0039
    ChrTalk(
        0x102,
        (
            "#00104Fあそこにあるプラネタリウムで、\x01",
            "幻想的な雰囲気を作ってるみたいね。\x02\x03",

            "#00100Fリベールに留学していた頃に\x01",
            "王都のグランセル城を見学したけど、\x01",
            "雰囲気では引けを取らないと思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        (
            "#00000Fそれは本当に凄いな。\x01",
            "さすがＩＢＣってところか……\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x102,
        (
            "#00100Fええ、鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うと言われているわね。\x02\x03",

            "#00104F聞いた話では、城の最上階に\x01",
            "置かれているそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x102,
        "#00100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_2B77")


    #C0044
    ChrTalk(
        0x103,
        (
            "#00204F中央のプラネタリウムのおかげで、\x01",
            "幻想的なオーラが生まれていますね。\x02\x03",

            "#00200Fまるで、おとぎ話に出てくるような\x01",
            "お城みたいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x101,
        (
            "#00000Fああ、確かにそんな感じだな。\x01",
            "さすがＩＢＣってところか……\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x103,
        (
            "#00200Fエリィさんの話では、\x01",
            "鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うらしいですね。\x02\x03",

            "#00204Fなんでも、城の最上階に\x01",
            "置かれているそうですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#00200Fはい、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_2D97")


    #C0049
    ChrTalk(
        0x104,
        (
            "#00304F中央で回ってるプラネタリウムで、\x01",
            "幻想的な雰囲気を演出してるらしい。\x02\x03",

            "#00300Fハハ、ここまで本格的だと\x01",
            "本物の城みたいに見えてくるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00000Fああ、本当にそんな気がするよ。\x01",
            "さすがＩＢＣってところか……\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x104,
        (
            "#00300Fああ、鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うっていうアレだな。\x02\x03",

            "#00304F最上階に置いてあるから、\x01",
            "上ってみればすぐに分かると思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x104,
        "#00300Fおう、行ってみるか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_2FBA")


    #C0054
    ChrTalk(
        0x109,
        (
            "#10104F中央で回るプラネタリウムで、\x01",
            "幻想的な雰囲気を演出してるそうです。\x02\x03",

            "#10100Fここまで本格的だと\x01",
            "本物の城みたいに見えてきますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x101,
        (
            "#00000Fああ、本当にそんな気がするよ。\x01",
            "さすがＩＢＣってところか……\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x109,
        (
            "#10100Fはい、鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うって言われてますね。\x02\x03",

            "#10104F最上階に置いてあるので、\x01",
            "上ってみればすぐに分かると思います。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x109,
        "#10100Fはい、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_31DF")


    #C0059
    ChrTalk(
        0x105,
        (
            "#10304F中央のプラネタリウムで、\x01",
            "幻想的な雰囲気を演出してるわけか。\x02\x03",

            "#10302Fフフ、すごい凝り様だよね。\x01",
            "ここまでの建造物だと\x01",
            "相当ミラもかかってそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x101,
        (
            "#00000Fああ、つくづくＩＢＣの\x01",
            "資金力には驚かされるよ……\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x105,
        (
            "#10300Fああ、鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うって言うアレだね。\x02\x03",

            "#10304F最上階に置いてあるって話だし、\x01",
            "上ってみればすぐに分かるんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x105,
        "#10300Fフフ、了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3407")


    #C0064
    ChrTalk(
        0x153,
        (
            "#01111F真ん中でくるくる回ってるアレって、\x01",
            "何なのかなー？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        (
            "#00000Fああ、あれはプラネタリウムだな。\x01",
            "幻想的な雰囲気を演出するための\x01",
            "装置のようなものだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x153,
        "#01105Fへー……なんだかスゴイね。\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#00000Fああ、正直言葉もないくらいだよ。\x01",
            "さすがＩＢＣって所か……\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x153,
        (
            "#01100Fエリィが言ってたカガミのことー？\x01",
            "確か、お城のてっぺんにあるんだよねー。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        (
            "#00000Fああ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x153,
        "#01109Fさんせー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_361C")


    #C0071
    ChrTalk(
        0x156,
        (
            "#06404Fなんでも、中央のプラネタリウムで\x01",
            "幻想的な雰囲気を演出してるそうです～。\x02\x03",

            "#06400Fふふ、ここまで本格的だと\x01",
            "本物の城みたいに思えてきますよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#00000Fああ、本当にそんな気がするよ。\x01",
            "さすがＩＢＣってところか……\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x156,
        (
            "#06400Fはい、鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うって言われてますね～。\x02\x03",

            "#06404F最上階に置いてありますし、\x01",
            "上ってみればすぐに分かると思いますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x156,
        "#06409Fはい！　行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3857")


    #C0076
    ChrTalk(
        0x14C,
        (
            "#05904F中央にあるのはプラネタリウムかしら？\x01",
            "とても幻想的な雰囲気があるわね。\x02\x03",

            "#05902Fふふ、昔ロイドに読んであげた絵本にも\x01",
            "こんなお城が出てきたっけ。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#00000Fはは……\x01",
            "確かにおとぎ話の城みたいだね。\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x14C,
        (
            "#05900Fエリィさんは、\x01",
            "鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うって言ってたわね。\x02\x03",

            "#05904Fなんでも、城の最上階に\x01",
            "置かれているらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x14C,
        "#05900Fうん、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3A73")


    #C0081
    ChrTalk(
        0x134,
        (
            "#01704F中央にプラネタリウムで、\x01",
            "幻想的なオーラを作り出してるわけか……\x02\x03",

            "#01702Fふむ、今度アルカンシェルでも\x01",
            "使わせてもらえないかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00000Fはは……イリアさんらしいですね。\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話でしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x134,
        (
            "#01700Fああ、鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うっていうアレね。\x02\x03",

            "#01704F城の最上階に置いてるらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみましょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x134,
        "#01709Fオーケー、行ってみましょ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3C68")


    #C0086
    ChrTalk(
        0x135,
        (
            "#01804F中央にある天象儀で、\x01",
            "幻想的な雰囲気を作ってるんですね。\x02\x03",

            "#01802Fふふ、イリアさんが見たら\x01",
            "ステージ用に欲しがるかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x101,
        (
            "#00000Fはは……容易に想像できるな。\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x135,
        (
            "#01805Fああ、鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うっていう……\x02\x03",

            "#01804Fエリィさんの話では、城の最上階に\x01",
            "置いてあるということでしたが。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#00000Fじゃあ、ひとまず\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x135,
        "#01809Fはい、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_3E68")


    #C0091
    ChrTalk(
        0x166,
        (
            "#14005F真ん中でくるくる回ってるのは、\x01",
            "なんなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00000Fああ、あれはプラネタリウムだな。\x01",
            "幻想的な雰囲気を演出するための\x01",
            "装置のようなものだと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x166,
        (
            "#14000Fへえ……よく分かんないけど\x01",
            "なんだかすげえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        (
            "#00000Fああ、正直言葉もないくらいだよ。\x01",
            "さすがＩＢＣって所か……\x02\x03",

            "#00005Fそういえば、ここには\x01",
            "『願いを叶える鏡』ってものが\x01",
            "置かれているって話だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x166,
        (
            "#14000Fああ、さっき話してた、\x01",
            "鐘を鳴らして鏡の前に立つと\x01",
            "願い事が叶うっていうアレか。\x02\x03",

            "#14003F城の最上階にあるらしいけど……\x01",
            "そんなこと、信じてるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まだ分からないけど……\x01",
            "最上階まで上って探してみようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x166,
        "#14000Fフン、まあ付き合ってやるよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_40F3")

    label("loc_40F3")

    Jump("loc_43DC")

    label("loc_40F8")

    SetChrPos(0x101, -500, -950, -51000, 0)
    SetChrPos(0xEF, 500, -950, -51000, 0)
    OP_68(0, 1050, -46000, 0)
    MoveCamera(0, 10, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(13500, 3000)

    def lambda_415F():
        OP_9B(0x0, 0x101, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_415F)
    Sleep(50)

    def lambda_4177():
        OP_9B(0x0, 0xEF, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4177)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    OP_6F(0x79)
    OP_0D()

    #C0098
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、一緒に最上階にある\x01",
            "『願いを叶える鏡』を目指そう。\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_422A"),
        (1, "loc_424E"),
        (2, "loc_4278"),
        (3, "loc_429E"),
        (4, "loc_42C8"),
        (5, "loc_42E6"),
        (6, "loc_4302"),
        (7, "loc_432E"),
        (8, "loc_4358"),
        (9, "loc_4384"),
        (10, "loc_43AE"),
        (SWITCH_DEFAULT, "loc_43DC"),
    )


    label("loc_422A")


    #C0099
    ChrTalk(
        0x102,
        "#00100Fええ、分かったわ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_424E")


    #C0100
    ChrTalk(
        0x103,
        "#00200Fはい、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4278")


    #C0101
    ChrTalk(
        0x104,
        "#00300Fおう、行ってみるか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_429E")


    #C0102
    ChrTalk(
        0x109,
        "#10100Fはい、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_42C8")


    #C0103
    ChrTalk(
        0x105,
        "#10300Fフフ、了解。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_42E6")


    #C0104
    ChrTalk(
        0x153,
        "#01109Fさんせー！\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4302")


    #C0105
    ChrTalk(
        0x156,
        "#06409Fはい！　行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_432E")


    #C0106
    ChrTalk(
        0x14C,
        "#05900Fうん、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4358")


    #C0107
    ChrTalk(
        0x134,
        "#01709Fオーケー、行ってみましょ！\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_4384")


    #C0108
    ChrTalk(
        0x135,
        "#01802Fはい、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_43AE")


    #C0109
    ChrTalk(
        0x166,
        "#14000Fフン、まあ付き合ってやるよ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_43DC")

    label("loc_43DC")

    SetChrPos(0x0, 0, -1000, -46000, 0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_17_271A end

    def Function_18_43F2(): pass

    label("Function_18_43F2")

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

    def lambda_44AE():
        OP_9B(0x1, 0xFE, 0xFFFA, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44AE)

    def lambda_44C3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_44C3)
    Sleep(700)

    def lambda_44D7():
        OP_9B(0x1, 0xFE, 0x6, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_44D7)

    def lambda_44EC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 2, lambda_44EC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0xEF, 1)
    WaitChrThread(0xEF, 2)
    Sound(118, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x8)
    OP_79(0x4)
    SetMapObjFlags(0x4, 0x10)
    OP_6F(0x79)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4B50")

    #C0110
    ChrTalk(
        0x101,
        "#00000Fここが《鏡の城》の最上階か……\x02",
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
            "#00005Fどうやらあそこにあるのが、\x01",
            "話に出てた『鐘』みたいだな。\x02",
        )
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_462A"),
        (1, "loc_4698"),
        (2, "loc_4704"),
        (3, "loc_4742"),
        (4, "loc_4780"),
        (5, "loc_47EA"),
        (6, "loc_4852"),
        (7, "loc_4894"),
        (8, "loc_490A"),
        (9, "loc_497A"),
        (10, "loc_49E8"),
        (SWITCH_DEFAULT, "loc_4A54"),
    )


    label("loc_462A")


    #C0112
    ChrTalk(
        0x102,
        (
            "#00100F鳴らす為のヒモも\x01",
            "左右についているわね。\x02\x03",

            "#00104F話に聞いていたもので\x01",
            "間違いないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4698")


    #C0113
    ChrTalk(
        0x103,
        (
            "#00200F鳴らす為のヒモも\x01",
            "左右についています。\x02\x03",

            "#00204F話に聞いていたもので\x01",
            "間違いないでしょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4704")


    #C0114
    ChrTalk(
        0x104,
        (
            "#00300Fああ、鳴らす為のヒモも\x01",
            "左右についてるぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4742")


    #C0115
    ChrTalk(
        0x109,
        (
            "#10100Fええ、鳴らす為のヒモも\x01",
            "左右についてます。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4780")


    #C0116
    ChrTalk(
        0x105,
        (
            "#10300F鳴らす為のヒモも\x01",
            "左右についているね。\x02\x03",

            "#10304F話に聞いていたもので\x01",
            "間違いなさそうだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_47EA")


    #C0117
    ChrTalk(
        0x153,
        (
            "#01105F鳴らす為のヒモも\x01",
            "左右についてるねー。\x02\x03",

            "#01111Fエリィが言ってたのは\x01",
            "あれなのかなー？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4852")


    #C0118
    ChrTalk(
        0x156,
        (
            "#06400Fええ、鳴らす為のヒモも\x01",
            "左右についてますよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4894")


    #C0119
    ChrTalk(
        0x14C,
        (
            "#05900F鳴らす為のヒモも\x01",
            "左右についているわね。\x02\x03",

            "#05904F話に聞いていたもので\x01",
            "間違いないんじゃないかしら。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_490A")


    #C0120
    ChrTalk(
        0x134,
        (
            "#01700F鳴らす為のヒモも\x01",
            "左右についているわね。\x02\x03",

            "#01704F話に聞いていたもので\x01",
            "間違いないんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_497A")


    #C0121
    ChrTalk(
        0x135,
        (
            "#01802F鳴らす為のヒモも\x01",
            "左右についていますね。\x02\x03",

            "#01804F話に聞いていたもので\x01",
            "間違いなさそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_49E8")


    #C0122
    ChrTalk(
        0x166,
        (
            "#14000F鳴らす為のヒモも\x01",
            "左右についてるし……\x02\x03",

            "#14003F話に聞いていたので\x01",
            "間違いないんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_4A54")

    label("loc_4A54")


    def lambda_4A59():
        OP_93(0x101, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4A59)
    Sleep(50)

    def lambda_4A69():
        OP_93(0xEF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4A69)
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
            "#00002Fとすると、あの大きな鏡が\x01",
            "『願いを叶える鏡』か。\x02",
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

    def lambda_4B28():
        OP_93(0x101, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_4B28)
    Sleep(50)

    def lambda_4B38():
        OP_93(0xEF, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_4B38)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0xEF, 0)
    Jump("loc_4B75")

    label("loc_4B50")


    #C0124
    ChrTalk(
        0x101,
        "#00000Fふう、最上階に着いたな。\x02",
    )

    CloseMessageWindow()

    label("loc_4B75")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4BC0"),
        (1, "loc_4C37"),
        (2, "loc_4CAC"),
        (3, "loc_4D20"),
        (4, "loc_4D98"),
        (5, "loc_4E02"),
        (6, "loc_4E6E"),
        (7, "loc_4EE2"),
        (8, "loc_4F4E"),
        (9, "loc_4FB4"),
        (10, "loc_501A"),
        (SWITCH_DEFAULT, "loc_5074"),
    )


    label("loc_4BC0")


    #C0125
    ChrTalk(
        0x102,
        (
            "#00100F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うらしいけど……\x02\x03",

            "#00104Fいざとなると、\x01",
            "なんだか緊張してくるわね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4C37")


    #C0126
    ChrTalk(
        0x103,
        (
            "#00200F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うそうですが……\x02\x03",

            "#00204Fいざとなると、\x01",
            "なんだか緊張してきます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4CAC")


    #C0127
    ChrTalk(
        0x104,
        (
            "#00300F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うって言われてるが……\x02\x03",

            "#00304Fさて、どんな願い事にするかねえ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4D20")


    #C0128
    ChrTalk(
        0x109,
        (
            "#10100F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うって言われてますけど……\x02\x03",

            "#10104Fうーん、何をお願いしましょうか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4D98")


    #C0129
    ChrTalk(
        0x105,
        (
            "#10300F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うそうだけど……\x02\x03",

            "#10304Fはてさて、どうなることやら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4E02")


    #C0130
    ChrTalk(
        0x153,
        (
            "#01100F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うんだよねー。\x02\x03",

            "#01109Fキーア、何をお願いしようかなー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4E6E")


    #C0131
    ChrTalk(
        0x156,
        (
            "#06400F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うって言われてますね～。\x02\x03",

            "#06409F今回は何をお願いしようかな～。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4EE2")


    #C0132
    ChrTalk(
        0x14C,
        (
            "#05900F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うそうだけど……\x02\x03",

            "#05904Fふふ、何をお願いしようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4F4E")


    #C0133
    ChrTalk(
        0x134,
        (
            "#01700F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うそうね。\x02\x03",

            "#01702Fフフ、何をお願いしようかしら。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_4FB4")


    #C0134
    ChrTalk(
        0x135,
        (
            "#01803F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶うそうですね。\x02\x03",

            "#01808F（でも……願い事なんて。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_501A")


    #C0135
    ChrTalk(
        0x166,
        (
            "#14003F鐘を鳴らして鏡の前に立つと\x01",
            "願いが叶う、か……\x02\x03",

            "#14008F……本当なのかな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5074")

    label("loc_5074")

    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50C9")

    #C0136
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、まずは２人で\x01",
            "あの鐘を鳴らしてみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5107")

    label("loc_50C9")


    #C0137
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、まずは２人で\x01",
            "あの鐘を鳴らしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5107")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x40000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    SetChrPos(0x0, 0, 40550, -15500, 180)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_18_43F2 end

    def Function_19_5126(): pass

    label("Function_19_5126")

    TalkBegin(0xFF)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "鐘を鳴らす\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Sleep(200)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5164")
    Call(0, 20)
    Jump("loc_5164")

    label("loc_5164")

    TalkEnd(0xFF)
    Return()

    # Function_19_5126 end

    def Function_20_5168(): pass

    label("Function_20_5168")

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
            "#00000F#6P……よし、次は上にある\x01",
            "『鏡』の前に行こう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xEF, 0x101, 500)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5277"),
        (1, "loc_52A4"),
        (2, "loc_52D1"),
        (3, "loc_52FA"),
        (4, "loc_531F"),
        (5, "loc_5348"),
        (6, "loc_5371"),
        (7, "loc_539C"),
        (8, "loc_53C9"),
        (9, "loc_53F4"),
        (10, "loc_5425"),
        (SWITCH_DEFAULT, "loc_5452"),
    )


    label("loc_5277")


    #C0139
    ChrTalk(
        0x102,
        "#00100Fええ、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_52A4")


    #C0140
    ChrTalk(
        0x103,
        "#00200Fはい、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_52D1")


    #C0141
    ChrTalk(
        0x104,
        "#00300Fはは、いよいよだな。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_52FA")


    #C0142
    ChrTalk(
        0x109,
        "#10100Fいよいよですね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_531F")


    #C0143
    ChrTalk(
        0x105,
        "#10300Fフフ、いよいよだね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_5348")


    #C0144
    ChrTalk(
        0x153,
        "#01109Fうん、行ってみよー！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_5371")


    #C0145
    ChrTalk(
        0x156,
        "#06400Fふふ、楽しみですね～。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_539C")


    #C0146
    ChrTalk(
        0x14C,
        "#05900Fふふ、どうなるのかしら。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_53C9")


    #C0147
    ChrTalk(
        0x134,
        "#01700Fうん、行ってみましょ。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_53F4")


    #C0148
    ChrTalk(
        0x135,
        "#01802F……ええ、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_5425")


    #C0149
    ChrTalk(
        0x166,
        "#14000F……フン、行ってみるか。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_5452")

    label("loc_5452")

    OP_D2(0x4, (scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    SetScenarioFlags(0x0, 0)
    OP_1B(0xC, 0x0, 0x2A)
    SetChrPos(0x0, -7700, 40550, -25000, 315)
    EventEnd(0x5)
    Return()

    # Function_20_5168 end

    def Function_21_547F(): pass

    label("Function_21_547F")

    Sound(918, 0, 100, 0)
    Sleep(2000)
    Sound(918, 0, 80, 0)
    Sleep(2000)
    Sound(918, 0, 60, 0)

    label("loc_5497")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54B0")
    Sleep(2000)
    Sound(918, 0, 40, 0)
    Jump("loc_5497")

    label("loc_54B0")

    Return()

    # Function_21_547F end

    def Function_22_54B1(): pass

    label("Function_22_54B1")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x80000000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5505")

    #C0150
    ChrTalk(
        0x101,
        (
            "#00000Fおっと……\x01",
            "先に下にある鐘を鳴らさないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_55BA")

    label("loc_5505")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (0, "loc_5550"),
        (1, "loc_5558"),
        (2, "loc_5560"),
        (3, "loc_5568"),
        (4, "loc_5570"),
        (5, "loc_5578"),
        (6, "loc_5580"),
        (7, "loc_5588"),
        (8, "loc_5590"),
        (9, "loc_5598"),
        (10, "loc_55A0"),
        (SWITCH_DEFAULT, "loc_55A8"),
    )


    label("loc_5550")

    Call(0, 28)
    Jump("loc_55A8")

    label("loc_5558")

    Call(0, 29)
    Jump("loc_55A8")

    label("loc_5560")

    Call(0, 30)
    Jump("loc_55A8")

    label("loc_5568")

    Call(0, 32)
    Jump("loc_55A8")

    label("loc_5570")

    Call(0, 33)
    Jump("loc_55A8")

    label("loc_5578")

    Call(0, 34)
    Jump("loc_55A8")

    label("loc_5580")

    Call(0, 36)
    Jump("loc_55A8")

    label("loc_5588")

    Call(0, 37)
    Jump("loc_55A8")

    label("loc_5590")

    Call(0, 38)
    Jump("loc_55A8")

    label("loc_5598")

    Call(0, 39)
    Jump("loc_55A8")

    label("loc_55A0")

    Call(0, 40)
    Jump("loc_55A8")

    label("loc_55A8")

    StopBGM(0xFA0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1400", 0, 0, 0)
    IdleLoop()

    label("loc_55BA")

    TalkEnd(0xFF)
    Return()

    # Function_22_54B1 end

    def Function_23_55BE(): pass

    label("Function_23_55BE")

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

    # Function_23_55BE end

    def Function_24_5628(): pass

    label("Function_24_5628")

    Fade(800)
    EndChrThread(0xC, 0x1)
    SetMapObjFrame(0xFF, "Null_bell", 0x2, "stop")
    OP_0D()
    Sleep(2500)
    Return()

    # Function_24_5628 end

    def Function_25_5648(): pass

    label("Function_25_5648")


    def lambda_564D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_564D)
    OP_93(0xFE, 0x10E, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_25_5648 end

    def Function_26_5661(): pass

    label("Function_26_5661")


    def lambda_5666():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_5666)
    OP_93(0xFE, 0x0, 0x1F4)
    WaitChrThread(0x101, 2)
    Return()

    # Function_26_5661 end

    def Function_27_567A(): pass

    label("Function_27_567A")

    SetCameraDistance(14700, 3000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Jc((scpexpr(EXPR_23, 0x5), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_56BA")
    OP_63(0xFE, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Jump("loc_56CC")

    label("loc_56BA")

    OP_63(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)

    label("loc_56CC")

    Sleep(2500)
    OP_64(0x101)
    OP_64(0xFE)
    OP_6F(0x79)
    Return()

    # Function_27_567A end

    def Function_28_56D8(): pass

    label("Function_28_56D8")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x102, 3, 0, 25)
    WaitChrThread(0x102, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_57D4")

    #C0151
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0152
    ChrTalk(
        0x102,
        (
            "#00100F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいでいいと思うわ。\x02\x03",

            "それじゃあ、やってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_583D")

    label("loc_57D4")


    #C0153
    ChrTalk(
        0x101,
        (
            "#00000Fあとはこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#00100Fええ、やってみましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_583D")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0158
    ChrTalk(
        0x102,
        (
            "#00104Fええ、私も終わったわ。\x02\x03",

            "#00100Fところで……\x01",
            "ロイドは何をお願いしたの？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5A6F")

    #C0159
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、キーアやエリィたち\x01",
            "支援課の仲間も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0160
    ChrTalk(
        0x102,
        "#00100Fふふっ、あなたらしいわね。\x02",
    )

    CloseMessageWindow()

    #C0161
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fそういうエリィは、\x01",
            "何をお願いしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5B88")

    label("loc_5A6F")


    #C0162
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『エリィの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0163
    ChrTalk(
        0x102,
        "#00100Fふふっ、ありがとうロイド。\x02",
    )

    CloseMessageWindow()

    #C0164
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fそれで、エリィは\x01",
            "何をお願いしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5B88")

    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x102)

    #C0165
    ChrTalk(
        0x102,
        (
            "#00103F私は……『父と母が幸せに\x01",
            "過ごしてくれてますように』かな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0166
    ChrTalk(
        0x101,
        "#00005Fエリィのご両親って……\x02",
    )

    CloseMessageWindow()

    #C0167
    ChrTalk(
        0x102,
        (
            "#00100F……ふふ、前に話したわね。\x01",
            "１０年前に離婚して、それぞれ\x01",
            "共和国と帝国で暮らしているわ。\x02\x03",

            "#00104F今も手紙や導力通信で\x01",
            "ときどき連絡をとってはいるけど、\x01",
            "ほとんど顔は見れていないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0168
    ChrTalk(
        0x101,
        (
            "#00008F……やっぱり寂しいよな。\x02\x03",

            "#00003F俺も幼い頃に両親を亡くしたけど、\x01",
            "兄貴やセシル姉がいたから\x01",
            "そこまで寂しくなかったし……\x02",
        )
    )

    CloseMessageWindow()

    #C0169
    ChrTalk(
        0x102,
        (
            "#00100Fふふ、私にもおじいさまが\x01",
            "そばにいてくださったし、\x01",
            "寂しいという訳じゃないの。\x02\x03",

            "#00103F……どちらかというと……\x01",
            "心配っていうのが正しいかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0170
    ChrTalk(
        0x101,
        "#00005F心配……？\x02",
    )

    CloseMessageWindow()

    #C0171
    ChrTalk(
        0x102,
        (
            "#00103F父と母は、ときどき私の近況を\x01",
            "心配して連絡をくれるけれど……\x02\x03",

            "#00108Fそれが、私を置いて出ていったことを\x01",
            "未だに後悔しての行動だとしたら、\x01",
            "それはあまりに苦しい事だと思う。\x02\x03",

            "あの人たちはとても真面目だから、\x01",
            "過去を忘れて生きるなんてことは\x01",
            "決して出来ないタイプなのよね。\x02\x03",

            "#00104Fあれから１０年も経ったんだし、\x01",
            "そろそろ新しい人生を歩んで、\x01",
            "幸せになって欲しいなって思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0172
    ChrTalk(
        0x101,
        (
            "#00008F過去を忘れて新しい人生を、か……\x02\x03",

            "#00001Fでも、それが正しいとは\x01",
            "一概には言えないんじゃないか？\x02",
        )
    )

    CloseMessageWindow()

    #C0173
    ChrTalk(
        0x102,
        (
            "#00100Fうん……分かってる。\x01",
            "過去があるからこそ、\x01",
            "今の私があるわけだしね。\x02\x03",

            "#00104Fでも、父と母には\x01",
            "どんな形でもいいから\x01",
            "幸せであってほしいなって……\x02\x03",

            "#00100F……ふふ、ごめんなさい。\x01",
            "変な話をしちゃったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0174
    ChrTalk(
        0x101,
        (
            "#00004Fいや……そんなことないさ。\x02\x03",

            "#00000Fエリィのご両親の幸せ……\x01",
            "俺も願わせてもらうとするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0175
    ChrTalk(
        0x102,
        "#00109Fふふ、ありがとう。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_28_56D8 end

    def Function_29_615B(): pass

    label("Function_29_615B")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x103, 3, 0, 25)
    WaitChrThread(0x103, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6257")

    #C0176
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0177
    ChrTalk(
        0x103,
        (
            "#00200F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいでいいと思います。\x02\x03",

            "それでは、やってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_62C0")

    label("loc_6257")


    #C0178
    ChrTalk(
        0x101,
        (
            "#00000Fあとはこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0179
    ChrTalk(
        0x103,
        "#00200Fはい、やってみましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_62C0")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0183
    ChrTalk(
        0x103,
        (
            "#00204F……はい、わたしもです。\x02\x03",

            "#00200F参考程度にお聞きしたいのですが、\x01",
            "ロイドさんはどんなお願いを？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6515")

    #C0184
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、キーアやティオたち\x01",
            "支援課の仲間も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0185
    ChrTalk(
        0x103,
        (
            "#00200Fなるほど……\x01",
            "ロイドさんらしいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0186
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fそういうティオは、\x01",
            "何をお願いしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_663F")

    label("loc_6515")


    #C0187
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『ティオの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0188
    ChrTalk(
        0x103,
        (
            "#00200Fなるほど……\x01",
            "それはありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0189
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fそういうティオは、\x01",
            "何をお願いしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_663F")


    #C0190
    ChrTalk(
        0x103,
        (
            "#00203F……『ロバーツ主任のウザさが\x01",
            "もう少しマシになりますように』です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0191
    ChrTalk(
        0x101,
        "#00012Fさ、さすがに可哀想なんじゃ……\x02",
    )

    CloseMessageWindow()

    #C0192
    ChrTalk(
        0x103,
        (
            "#00202F……冗談です。\x02\x03",

            "#00203F本当は……\x01",
            "『わたしの生きる意味が\x01",
            "見つかりますように』です。\x02",
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
            "#00200F以前、ロイドさんたちにも\x01",
            "話した事がありましたね。\x02\x03",

            "#00203F３年前、ガイさんに聞こうとして\x01",
            "聞けなかった質問の答え……\x02\x03",

            "#00208Fそれは、教団事件を乗り超えた\x01",
            "今でもまだ見出せていません。\x02",
        )
    )

    CloseMessageWindow()

    #C0194
    ChrTalk(
        0x101,
        (
            "#00004F……ティオ、言っただろう？\x01",
            "そんなのが判ってる人間なんて\x01",
            "そうそういるもんじゃない。\x02\x03",

            "#00000F答えを探すのに焦る必要はないし、\x01",
            "一人で探す必要だってないんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0195
    ChrTalk(
        0x103,
        (
            "#00204Fええ、もちろん分かっています。\x02\x03",

            "#00200F焦ってなんていませんし、\x01",
            "皆さんが力になってくれる事も\x01",
            "今のわたしには理解できていますから。\x02\x03",

            "#00203Fでも、これはわたしの人生における\x01",
            "命題とも言える問いです。\x02\x03",

            "#00200Fだから、いつか絶対に答えを見つける。\x01",
            "……そういう意思表示も込めて、\x01",
            "『鏡』に願わせてもらいました。\x02",
        )
    )

    CloseMessageWindow()

    #C0196
    ChrTalk(
        0x101,
        (
            "#00000F……はは、そうか。\x01",
            "悪い、余計な心配だったみたいだ。\x02\x03",

            "#00004Fそういうことなら、俺も改めて\x01",
            "意思を示させてもらおうかな。\x02\x03",

            "#00000Fティオがいつかその答えを\x01",
            "見つけられるように……\x01",
            "俺たちも力を貸していくよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0197
    ChrTalk(
        0x103,
        (
            "#00209Fふふっ……\x01",
            "よろしくお願いします。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_29_615B end

    def Function_30_6B01(): pass

    label("Function_30_6B01")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x104, 3, 0, 25)
    WaitChrThread(0x104, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6BF7")

    #C0198
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0199
    ChrTalk(
        0x104,
        (
            "#00300F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいでいいと思うぜ。\x02\x03",

            "そんじゃ、やってみるか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_6C60")

    label("loc_6BF7")


    #C0200
    ChrTalk(
        0x101,
        (
            "#00000Fあとはこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0201
    ChrTalk(
        0x104,
        "#00300Fそんじゃ、やってみるか。\x02",
    )

    CloseMessageWindow()

    label("loc_6C60")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0205
    ChrTalk(
        0x104,
        (
            "#00304Fん、俺も終わったぜ。\x02\x03",

            "#00309Fんで、ロイド。\x01",
            "お前どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EE5")

    #C0206
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、キーアやランディたち\x01",
            "支援課の仲間も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0207
    ChrTalk(
        0x104,
        (
            "#00300Fはは、ホントお前って\x01",
            "真面目なヤツだよなあ。\x02\x03",

            "#00306Fもう少し自分の欲望に\x01",
            "正直な願い事をしても、\x01",
            "バチはあたんねえだろうによ。\x02",
        )
    )

    CloseMessageWindow()

    #C0208
    ChrTalk(
        0x101,
        (
            "#00005Fそ、そういうランディは\x01",
            "どんな願い事をしたんだよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7032")

    label("loc_6EE5")


    #C0209
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『ランディの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0210
    ChrTalk(
        0x104,
        (
            "#00305Fおお、マジでか！？\x02\x03",

            "#00309Fいや～さすがはロイド、\x01",
            "タイミングのいいヤツだぜ！\x02",
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
            "#00005Fえっ……ランディは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7032")


    #C0212
    ChrTalk(
        0x104,
        (
            "#00304F俺か？　そりゃあもちろん、\x01",
            "『クロスベルに、お姉さんたちとの\x01",
            "  ウハウハなハーレムを──』\x02",
        )
    )

    CloseMessageWindow()

    #C0213
    ChrTalk(
        0x101,
        (
            "#00003F──分かった、もういい。\x01",
            "聞いた俺がバカだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0214
    ChrTalk(
        0x104,
        (
            "#00305Fおいおい、男なら誰しもが\x01",
            "夢見る状況だろうが？\x02\x03",

            "#00304Fセシルさんたちナースさんに、\x01",
            "遊撃士のエオリアさん……\x02\x03",

            "#00309Fクロスベルには俺好みの\x01",
            "お姉さんが盛り沢山だからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0215
    ChrTalk(
        0x101,
        (
            "#00006Fあのなあ……そんな妄想に\x01",
            "セシル姉まで参加させるなよ。\x02\x03",

            "#00002F……まあ、ある意味安心したよ。\x01",
            "絶対に叶うわけない願い事だし。\x02",
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
            "#00306Fズ、ズバリ\x01",
            "言ってくれやがって……\x02\x03",

            "#00300F……ははーん、さてはお前、\x01",
            "羨ましいんだな？\x02\x03",

            "#00304F安心しておけ、\x01",
            "願いが叶った暁には\x01",
            "お前にもいい思いを……\x02",
        )
    )

    CloseMessageWindow()

    #C0217
    ChrTalk(
        0x101,
        (
            "#00011Fい、いつ誰が\x01",
            "そんな心配をしたんだよ！？\x02\x03",

            "#00006F……はあ、まったく。\x01",
            "願い事はしたんだしさっさと行くぞ。\x02",
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
            "#00308F（絶対に叶うわけない願い事……か。）\x02\x03",

            "#00303F（『このままずっと、仲間として』……\x01",
            "  俺にはムシが良すぎるわな。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_93(0x104, 0xE1, 0x1F4)
    OP_9B(0x0, 0x104, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    Return()

    # Function_30_6B01 end

    def Function_31_7409(): pass

    label("Function_31_7409")

    OP_93(0xFE, 0xE1, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1B58, 0x7D0, 0x0)
    Return()

    # Function_31_7409 end

    def Function_32_7420(): pass

    label("Function_32_7420")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x109, 3, 0, 25)
    WaitChrThread(0x109, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_751E")

    #C0219
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0220
    ChrTalk(
        0x109,
        (
            "#10100F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいでいいと思います。\x02\x03",

            "それじゃあ、やってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_75A4")

    label("loc_751E")


    #C0221
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "願い事をしてみよう。\x02\x03",

            "この鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0222
    ChrTalk(
        0x109,
        "#10100Fええ、やってみましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_75A4")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0226
    ChrTalk(
        0x109,
        (
            "#10104Fはい、あたしも終わりました。\x02\x03",

            "#10100F……えっと、ロイドさんは\x01",
            "どんな願い事を？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_77DB")

    #C0227
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、警備隊の人たちや\x01",
            "支援課の仲間も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0228
    ChrTalk(
        0x109,
        "#10100Fなるほど、ロイドさんらしいです。\x02",
    )

    CloseMessageWindow()

    #C0229
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "ノエルの方は、\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7905")

    label("loc_77DB")


    #C0230
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『ノエルの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0231
    ChrTalk(
        0x109,
        (
            "#10100Fあはは……\x01",
            "ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0232
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fそれで、ノエルの方は、\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7905")


    #C0233
    ChrTalk(
        0x109,
        (
            "#10100Fあたしの方は単純ですけど……\x01",
            "『立派な警備隊員になりたい』、\x01",
            "でしょうか。\x02",
        )
    )

    CloseMessageWindow()

    #C0234
    ChrTalk(
        0x101,
        (
            "#00009Fはは……\x01",
            "ノエルらしい率直な願いだな。\x02\x03",

            "#00000Fやっぱり、君のお父さんが\x01",
            "目標になってるのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0235
    ChrTalk(
        0x109,
        (
            "#10100Fあはは……前も言いましたけど、\x01",
            "そのあたりの自覚はあまりないです。\x02\x03",

            "#10104Fあたしも子供でしたし、\x01",
            "躾けの厳しい父のことは\x01",
            "むしろ苦手なくらいでしたから。\x02",
        )
    )

    CloseMessageWindow()

    #C0236
    ChrTalk(
        0x101,
        "#00005Fへえ、そうだったのか。\x02",
    )

    CloseMessageWindow()

    #C0237
    ChrTalk(
        0x109,
        (
            "#10102Fええ、本当に厳しい人でしたよ。\x02\x03",

            "#10104Fあたしやフランが\x01",
            "悪いイタズラをしたりすると、\x01",
            "容赦なく拳骨を飛ばすような人で……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0238
    ChrTalk(
        0x109,
        (
            "#10103F……そういえば、母に連れられて\x01",
            "一度だけ国境門で働く父を\x01",
            "見に行ったことがありました。\x02\x03",

            "#10108F当時の歪んだ体制を憂いつつも、\x01",
            "クロスベルを守る者として\x01",
            "全てに厳しくあろうとする姿……\x02\x03",

            "#10100F今考えると……\x01",
            "あたしはあの姿に尊敬の念を\x01",
            "抱いていたのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0239
    ChrTalk(
        0x101,
        (
            "#00002Fそっか……\x01",
            "ノエルの自分に厳しい性格には\x01",
            "やっぱり影響がありそうだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0240
    ChrTalk(
        0x109,
        (
            "#10109Fあはは、ですね。\x02\x03",

            "#10103Fそれはそれで、なんでフランが\x01",
            "あんなゆるやかな性格になったのか\x01",
            "納得いかないところですけど。\x02\x03",

            "#10101F……もしかして父さんって、\x01",
            "実はフランだけには\x01",
            "デレデレだったんでしょうか。\x02",
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
            "#00012Fいや、まあ……\x01",
            "厳しさの反動って可能性もあるし。\x02\x03",

            "#00000F……それじゃあ、願い事も済んだし\x01",
            "そろそろ行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0242
    ChrTalk(
        0x109,
        "#10100Fええ、そうですね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_32_7420 end

    def Function_33_7E1A(): pass

    label("Function_33_7E1A")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x105, 3, 0, 25)
    WaitChrThread(0x105, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F15")

    #C0243
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0244
    ChrTalk(
        0x105,
        (
            "#10300F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいで\x01",
            "いいんじゃない？\x02\x03",

            "それじゃ、やってみようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7FA4")

    label("loc_7F15")


    #C0245
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "願い事をしてみよう。\x02\x03",

            "#00004Fこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0246
    ChrTalk(
        0x105,
        "#10300Fそれじゃ、やってみようか。\x02",
    )

    CloseMessageWindow()

    label("loc_7FA4")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0250
    ChrTalk(
        0x105,
        (
            "#10304F僕も終わったよ。\x02\x03",

            "#10300Fそれで、君はどんな\x01",
            "願い事をしたんだい？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_81CE")

    #C0251
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、キーアやワジたち\x01",
            "支援課の仲間も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0252
    ChrTalk(
        0x105,
        "#10300Fフフ、君らしい願い事だね。\x02",
    )

    CloseMessageWindow()

    #C0253
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fそういうワジは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_82F4")

    label("loc_81CE")


    #C0254
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『ワジの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0255
    ChrTalk(
        0x105,
        (
            "#10300Fフフ、君ってヤツは\x01",
            "ほんとお人よしだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0256
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fそういうワジは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_82F4")


    #C0257
    ChrTalk(
        0x105,
        (
            "#10302Fフフ、強いて言うなら……\x02\x03",

            "#10304F『元喧嘩相手が自分の道を\x01",
            "みつけられるように』かな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0258
    ChrTalk(
        0x101,
        (
            "#00008F……噂で聞いたけど……\x01",
            "ヴァルド、最近はアジトにも\x01",
            "顔を出してないんだってな。\x02\x03",

            "#00003Fでも、それは別にワジのせいじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0259
    ChrTalk(
        0x105,
        (
            "#10309F別に、責任を感じたり\x01",
            "感傷に浸ってるわけじゃないさ。\x02\x03",

            "#10300Fあの雨の日の決闘の後、\x01",
            "彼が腐ったりヤケになるのは\x01",
            "僕にもある程度予想できたしね。\x02\x03",

            "#10304Fその後腐り続けるか、\x01",
            "全てを吹っ切って次に進むか……\x01",
            "結局はヴァルド自身の問題だ。\x02",
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
            "#00006Fそれはその、クールな意見だな……\x02\x03",

            "#00000Fでも、本当にそう思ってるんだったら\x01",
            "『ヴァルドが自分の道を……』だなんて\x01",
            "願わないんじゃないのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0261
    ChrTalk(
        0x105,
        (
            "#10304Fフフ、ごもっともだけど……\x01",
            "この願いは僕自身のためでもあるからね。\x02\x03",

            "#10300Fもし、今後彼が腐り続けるなら……\x01",
            "あの雨の日の決闘で僕が伝えるべきことが\x01",
            "何一つ伝わってなかったことになる。\x02\x03",

            "#10303Fそれは僕がケジメをつけ切れて\x01",
            "なかったという事実に他ならない……\x02\x03",

            "#10309Fさすがにそれはカッコ悪いだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0262
    ChrTalk(
        0x101,
        (
            "#00006F……はあ、やれやれ。\x01",
            "ワジって素直じゃないよな。\x02\x03",

            "#00000Fでも、ヴァルドたちや\x01",
            "バイパーの連中が道を見つける……\x01",
            "それは俺も願ってやまないよ。\x02\x03",

            "本当に、叶ってくれるといいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0263
    ChrTalk(
        0x105,
        (
            "#10303Fフフ、君って本当にお人よしだよね。\x02\x03",

            "#10309Fそういう所がたまらなく好きさ。\x02",
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
            "#00006Fああもう、折角きれいに\x01",
            "まとまりかけてたのに……\x01",
            "茶化すんじゃないっての！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_33_7E1A end

    def Function_34_884C(): pass

    label("Function_34_884C")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x153, 3, 0, 25)
    WaitChrThread(0x153, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8948")

    #C0265
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0266
    ChrTalk(
        0x153,
        (
            "#01100Fこのカガミの前で\x01",
            "お願い事を言えばいいのー？\x02",
        )
    )

    CloseMessageWindow()

    #C0267
    ChrTalk(
        0x101,
        (
            "#00000Fああ、多分頭の中で願い事を\x01",
            "思い浮かべるくらいでいいと思う。\x02\x03",

            "……それじゃ、やってみよう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_89C9")

    label("loc_8948")


    #C0268
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "願い事をしてみよう。\x02\x03",

            "#00004Fこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0269
    ChrTalk(
        0x153,
        "#01100Fわかったー。\x02",
    )

    CloseMessageWindow()

    label("loc_89C9")

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
        "#01103F……ん～…………………………\x02",
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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0273
    ChrTalk(
        0x153,
        (
            "#01109Fうん、キーアも終わったー！\x02\x03",

            "#01105Fねーねー、ロイドはどんな\x01",
            "お願い事をしたのー？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8BFF")

    #C0274
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、キーアたち\x01",
            "支援課の仲間も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0275
    ChrTalk(
        0x153,
        "#01109Fえへへ……さすがロイドだね。\x02",
    )

    CloseMessageWindow()

    #C0276
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fキーアのほうは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8D16")

    label("loc_8BFF")


    #C0277
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『キーアの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0278
    ChrTalk(
        0x153,
        "#01109Fえへへ……アリガトー。\x02",
    )

    CloseMessageWindow()

    #C0279
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fキーアのほうは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8D16")


    #C0280
    ChrTalk(
        0x153,
        (
            "#01106Fえっとね、お願いしたいのは\x01",
            "色々あったんだけどー……\x02\x03",

            "#01100Fやっぱり一番は、『シズクの目が\x01",
            "治りますように』かなー。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0281
    ChrTalk(
        0x101,
        (
            "#00003F……ああ、本当に治るといいよな。\x02\x03",

            "#00008Fシズクちゃんの目の手術は\x01",
            "やっぱり相当難しいらしいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0282
    ChrTalk(
        0x153,
        (
            "#01111Fでも、このカガミに\x01",
            "お願いしたら叶うんだよねー？\x02\x03",

            "#01101Fだったらキーア、\x01",
            "何回でもお願いする！\x02",
        )
    )

    CloseMessageWindow()

    #C0283
    ChrTalk(
        0x101,
        (
            "#00000Fはは……ああ。\x01",
            "俺も本気でお願いするよ。\x02\x03",

            "#00004F（本当に……奇跡でも\x01",
            "  起こればいいんだけどな。）\x02",
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
        "#00005Fどうした、キーア？\x02",
    )

    CloseMessageWindow()
    OP_93(0x153, 0x10E, 0x1F4)

    #C0286
    ChrTalk(
        0x153,
        (
            "#01103F……ん～ん、なんでもない。\x02\x03",

            "#01109Fそれよりロイド、\x01",
            "もっといっぱい鐘を鳴らそーよ！\x02",
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
            "#00009Fはは……\x01",
            "なんだか元気が有り余ってるな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_34_884C end

    def Function_35_9037(): pass

    label("Function_35_9037")

    OP_93(0xFE, 0x87, 0x1F4)
    OP_9B(0x0, 0xFE, 0x0, 0x1F40, 0xFA0, 0x0)
    Return()

    # Function_35_9037 end

    def Function_36_904E(): pass

    label("Function_36_904E")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x156, 3, 0, 25)
    WaitChrThread(0x156, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_914F")

    #C0288
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0289
    ChrTalk(
        0x156,
        (
            "#06400F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいで\x01",
            "いいと思いますよ～。\x02\x03",

            "それじゃ、やってみましょう！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_91E0")

    label("loc_914F")


    #C0290
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "願い事をしてみよう。\x02\x03",

            "#00004Fこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0291
    ChrTalk(
        0x156,
        "#06400Fそれじゃ、やってみましょう！\x02",
    )

    CloseMessageWindow()

    label("loc_91E0")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0295
    ChrTalk(
        0x156,
        (
            "#06400Fはい、わたしもお願いしました～。\x02\x03",

            "#06409Fちなみに、ロイドさんは\x01",
            "どんなお願い事をしたんですか～？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_942A")

    #C0296
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、フランたち\x01",
            "警察の仲間も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0297
    ChrTalk(
        0x156,
        "#06402Fふふ、ロイドさんらしいですね～。\x02",
    )

    CloseMessageWindow()

    #C0298
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fそういうフランは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9551")

    label("loc_942A")


    #C0299
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『フランの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0300
    ChrTalk(
        0x156,
        "#06402Fふふ、それはありがとうございます～。\x02",
    )

    CloseMessageWindow()

    #C0301
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fそういうフランは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9551")


    #C0302
    ChrTalk(
        0x156,
        (
            "#06409Fふふ、わたしはやっぱり\x01",
            "『お姉ちゃんみたいになりたい』\x01",
            "ですかね～。\x02\x03",

            "#06401Fお姉ちゃんみたいな\x01",
            "かっこよくて頼れる女性が、\x01",
            "わたしの永遠の目標ですから！\x02",
        )
    )

    CloseMessageWindow()

    #C0303
    ChrTalk(
        0x101,
        (
            "#00012Fノエルみたいな女性か……\x01",
            "はは、姉思いのフランらしい願いだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0304
    ChrTalk(
        0x101,
        (
            "#00005Fそういえば素朴な疑問だけど……\x01",
            "フランは警備隊を目指さなかったのか？\x02\x03",

            "#00000Fそんなにノエルを慕ってるなら、\x01",
            "同じ警備隊で働きたいと思っても\x01",
            "おかしくないと思うんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0305
    ChrTalk(
        0x156,
        (
            "#06400Fあはは、それはそれですよ～。\x01",
            "やっぱり、人ってそれぞれ\x01",
            "相応しい場所があるじゃないですか。\x02\x03",

            "#06403Fわたしは警察学校じゃ、訓練よりも\x01",
            "事務系の成績がよかったですから……\x02\x03",

            "#06400Fわたしはわたしに合った方法で、\x01",
            "クロスベルを守っていきたいと思って。\x02",
        )
    )

    CloseMessageWindow()

    #C0306
    ChrTalk(
        0x101,
        (
            "#00000F確かに、現場で働いている人だけが\x01",
            "クロスベルを守ってるんじゃないしな。\x02\x03",

            "#00004F作戦本部や、オペレーターの仕事が\x01",
            "あってこそ俺たちも活躍できる……\x02\x03",

            "#00009Fそういう意味では、フランが\x01",
            "受付にいるのはしっくりくるし……\x01",
            "やっぱり適任だったんだろうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0307
    ChrTalk(
        0x156,
        (
            "#06409Fえへへ……\x01",
            "そこまで言われると\x01",
            "照れちゃいますけど。\x02\x03",

            "#06400F『お姉ちゃんみたいになりたい』\x01",
            "っていう願い事も、\x01",
            "その範囲の中でってことですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0308
    ChrTalk(
        0x101,
        (
            "#00002Fはは、なるほど。\x02\x03",

            "#00000F……さてと、それじゃあ\x01",
            "願い事もしたことだし、\x01",
            "そろそろ行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0309
    ChrTalk(
        0x156,
        "#06409Fはいっ、行きましょう～！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_36_904E end

    def Function_37_9A36(): pass

    label("Function_37_9A36")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x14C, 3, 0, 25)
    WaitChrThread(0x14C, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9B3B")

    #C0310
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0311
    ChrTalk(
        0x14C,
        (
            "#05900F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいで\x01",
            "いいんじゃないかしら。\x02\x03",

            "それじゃあ、やってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9BC8")

    label("loc_9B3B")


    #C0312
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "願い事をしてみよう。\x02\x03",

            "#00004Fこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0313
    ChrTalk(
        0x14C,
        "#05900Fええ、やってみましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_9BC8")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0317
    ChrTalk(
        0x14C,
        (
            "#05904Fうん、私も大丈夫よ。\x02\x03",

            "#05900Fロイドはどんなお願い事を\x01",
            "したのかしら？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9DF4")

    #C0318
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、セシル姉や\x01",
            "支援課の仲間たちも含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0319
    ChrTalk(
        0x14C,
        "#05902Fふふ、ロイドらしいわ。\x02",
    )

    CloseMessageWindow()

    #C0320
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fそういうセシル姉は\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_9F13")

    label("loc_9DF4")


    #C0321
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『セシル姉の願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0322
    ChrTalk(
        0x14C,
        "#05902Fふふ、ありがとうロイド。\x02",
    )

    CloseMessageWindow()

    #C0323
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fそういうセシル姉は\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_9F13")


    #C0324
    ChrTalk(
        0x14C,
        (
            "#05900F私はやっぱり……\x01",
            "『ロイドたちがいつまでも\x01",
            "元気でありますように』かしら。\x02\x03",

            "#05904F私にとっては、\x01",
            "それが一番の願いだもの。\x02",
        )
    )

    CloseMessageWindow()

    #C0325
    ChrTalk(
        0x101,
        (
            "#00004F……そっか、ありがとうセシル姉。\x02\x03",

            "#00000F大怪我をして病院に運ばれたり\x01",
            "することのないように、\x01",
            "充分に気をつけるとするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0326
    ChrTalk(
        0x14C,
        (
            "#05909Fふふ、そうしてちょうだい。\x02\x03",

            "#05901Fもしそんなことになったら、\x01",
            "涙が出るほど痛いお注射を\x01",
            "何本も刺しちゃうんだから。\x02",
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
            "#00006F（それは、ランディあたりが\x01",
            "  結構喜びそうだな……）\x02\x03",

            "#00000F……セシル姉こそ、\x01",
            "無理して仕事ばかりしてないで\x01",
            "たまには休みをとってくれよ？\x02",
        )
    )

    CloseMessageWindow()

    #C0328
    ChrTalk(
        0x14C,
        (
            "#05905Fうーん、患者さんの事を考えると\x01",
            "やっぱり出来るかぎりは\x01",
            "仕事に出ておきたいのよね。\x02\x03",

            "#05909Fそれに、時々はこうして\x01",
            "休みをとってるし、大丈夫よ。\x02",
        )
    )

    CloseMessageWindow()

    #C0329
    ChrTalk(
        0x101,
        (
            "#00006Fいや、セシル姉の場合は\x01",
            "本当に時々しか\x01",
            "休んでないみたいだしさ……\x02\x03",

            "#00001F俺だって、セシル姉のことは\x01",
            "心配してるんだからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0330
    ChrTalk(
        0x14C,
        (
            "#05904Fうん……そうね、分かった。\x01",
            "無理はしないように\x01",
            "気をつけるとするわね。\x02\x03",

            "#05909Fふふ、それにしても\x01",
            "お姉ちゃんの心配なんて……\x01",
            "ロイドも大人になったわねえ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0xE, 0xF, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0331
    ChrTalk(
        0x101,
        "#00006Fまたそうやって子供扱いする……\x02",
    )

    CloseMessageWindow()

    #C0332
    ChrTalk(
        0x14C,
        "#05902Fふふ、ごめんごめん。\x02",
    )

    CloseMessageWindow()

    #C0333
    ChrTalk(
        0x101,
        (
            "#00002F（……セシル姉はやっぱり、\x01",
            "　どこまでも『セシル姉』なんだよな。）\x02\x03",

            "#00006F（……ちょっとだけ寂しい気はするけど。）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_37_9A36 end

    def Function_38_A400(): pass

    label("Function_38_A400")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x134, 3, 0, 25)
    WaitChrThread(0x134, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A500")

    #C0334
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみましょう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0335
    ChrTalk(
        0x134,
        (
            "#01700F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいでいいんじゃない？\x02\x03",

            "それじゃ、やってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A597")

    label("loc_A500")


    #C0336
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "願い事をしてみましょう。\x02\x03",

            "#00004Fこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0337
    ChrTalk(
        0x134,
        "#01700Fオッケー、やってみましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_A597")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0341
    ChrTalk(
        0x134,
        (
            "#01704Fうん、あたしも大丈夫よ。\x02\x03",

            "#01700Fちなみに、弟君は\x01",
            "どんなお願い事をしたの？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7F4")

    #C0342
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんですけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』ですね。\x02\x03",

            "#00000Fもちろん、イリアさんたち\x01",
            "アルカンシェルの皆さんも含めて。\x02",
        )
    )

    CloseMessageWindow()

    #C0343
    ChrTalk(
        0x134,
        (
            "#01702Fフフ、なるほど。\x01",
            "なかなか立派な事を言うじゃない。\x02",
        )
    )

    CloseMessageWindow()

    #C0344
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fイリアさんのほうは\x01",
            "どんな願い事をしたんですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_A938")

    label("loc_A7F4")


    #C0345
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃいましたから……\x02\x03",

            "#00004F同じ願い事をするのもなんですし、\x01",
            "『イリアさんの願いが叶いますように』\x01",
            "って願いにしましたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0346
    ChrTalk(
        0x134,
        (
            "#01702Fあら、弟君ったら\x01",
            "なかなか気が利くじゃないの。\x02",
        )
    )

    CloseMessageWindow()

    #C0347
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fイリアさんのほうは\x01",
            "どんな願い事をしたんですか？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A938")


    #C0348
    ChrTalk(
        0x134,
        (
            "#01704Fあたしはもちろん\x01",
            "『どんなことがあっても、\x01",
            "踊り続けられますように』ね。\x02\x03",

            "#01700Fまあ、わざわざ願わなくても、\x01",
            "あたしがステージを降りるなんて事は\x01",
            "絶対にありえないんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0349
    ChrTalk(
        0x101,
        (
            "#00000Fはは、さすがイリアさん。\x01",
            "ステージへの執念なら\x01",
            "誰にも負けない勢いですね。\x02\x03",

            "#00009Fそこまでのパワーが、\x01",
            "どこから湧いて来るのか、\x01",
            "いつも驚かされますよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0350
    ChrTalk(
        0x134,
        (
            "#01703Fうーん、そうね。\x01",
            "強いて言うなら……\x02\x03",

            "#01700Fあたしはどこの誰よりも\x01",
            "ステージで踊るのが『好き』だ、\x01",
            "ってところかしら。\x02\x03",

            "その点に関しては、大陸中の\x01",
            "誰にだって負けない自信があるし……\x02\x03",

            "#01709Fその気持ちがある限り、\x01",
            "あたしは死ぬまで踊り続けられるわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0351
    ChrTalk(
        0x101,
        (
            "#00005F『好き』ですか……\x01",
            "とてもシンプルですけど、\x01",
            "分かる気もします。\x02\x03",

            "#00004Fそう強く思えるのもある意味、\x01",
            "凄い事なのかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0352
    ChrTalk(
        0x134,
        (
            "#01700Fフフ、大したことじゃないわよ。\x01",
            "好きかどうかなんて\x01",
            "誰にでもある感情だしね。\x02\x03",

            "#01709F弟君も、大切な人のためなら\x01",
            "命だって賭けられるんじゃない？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0353
    ChrTalk(
        0x101,
        (
            "#00000Fええ……本当にそう思います。\x02\x03",

            "#00004F（あの教団事件を解決できたのも、\x01",
            "  キーアを守りたいという\x01",
            "  強い気持ちがあったから…… ）\x02\x03",

            "（人は大切なものの為なら、\x01",
            "  どこまでも強くなれるんだろうな。）\x02",
        )
    )

    CloseMessageWindow()

    #C0354
    ChrTalk(
        0x134,
        (
            "#01700Fふふ、納得してくれたみたいね。\x02\x03",

            "#01709F……さ、願い事もすんだ事だし\x01",
            "そろそろ行くとしましょ。\x02",
        )
    )

    CloseMessageWindow()

    #C0355
    ChrTalk(
        0x101,
        "#00000Fええ、そうですね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_38_A400 end

    def Function_39_AE2D(): pass

    label("Function_39_AE2D")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x135, 3, 0, 25)
    WaitChrThread(0x135, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AF3B")

    #C0356
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0357
    ChrTalk(
        0x135,
        (
            "#01802F多分、頭の中で願い事を\x01",
            "思い浮かべるくらいで\x01",
            "いいんじゃないでしょうか。\x02\x03",

            "#01803F……では、やってみましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_AFCC")

    label("loc_AF3B")


    #C0358
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "願い事をしてみよう。\x02\x03",

            "#00004Fこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0359
    ChrTalk(
        0x135,
        "#01803F……はい、やってみましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_AFCC")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0363
    ChrTalk(
        0x135,
        (
            "#01804Fはい、私も大丈夫です。\x02\x03",

            "#01802Fえっと、ロイドさんは\x01",
            "どんなお願い事をしましたか？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B21F")

    #C0364
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、リーシャたち\x01",
            "アルカンシェルの人も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0365
    ChrTalk(
        0x135,
        (
            "#01802F……そうですか。\x01",
            "ふふ、ロイドさんらしいです。\x02",
        )
    )

    CloseMessageWindow()

    #C0366
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fそういうリーシャは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B353")

    label("loc_B21F")


    #C0367
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『リーシャの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0368
    ChrTalk(
        0x135,
        (
            "#01802F……そうですか。\x01",
            "ふふ、ありがとうございます。\x02",
        )
    )

    CloseMessageWindow()

    #C0369
    ChrTalk(
        0x101,
        (
            "#00009Fはは、どういたしまして。\x02\x03",

            "#00000Fそういうリーシャは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B353")

    OP_63(0x135, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x135)

    #C0370
    ChrTalk(
        0x135,
        (
            "#01803F私の願いは……\x01",
            "『イリアさんのような\x01",
            "アーティストになりたい』です。\x02\x03",

            "#01802Fふふ、まだまだ新人の私が\x01",
            "おこがましいかもしれませんけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0371
    ChrTalk(
        0x101,
        (
            "#00000Fいや……\x01",
            "そんなことないんじゃないか？\x02\x03",

            "#00003Fアルカンシェルの公演も\x01",
            "かなり好評みたいだし……\x02\x03",

            "#00000F何より、君はあのイリアさんに\x01",
            "才能を認められてる。\x02\x03",

            "#00009Fこのまま努力を続ければ、\x01",
            "きっと将来はイリアさんみたいな\x01",
            "大スターにだってなれる気がするよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x135, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)

    #C0372
    ChrTalk(
        0x135,
        (
            "#01809Fそ、そんな……\x01",
            "私なんて本当にまだまだですよ。\x02\x03",

            "#01804F私なんかよりシュリちゃんの方が、\x01",
            "よっぽど才能があると思いますし。\x02",
        )
    )

    CloseMessageWindow()

    #C0373
    ChrTalk(
        0x101,
        (
            "#00004Fうーん、もう少し自信を持っても\x01",
            "いいとは思うんだけどな。\x02\x03",

            "#00000Fまあ、リーシャの願い事が叶うよう\x01",
            "俺も応援してるから……\x01",
            "これからも頑張ってくれよな。\x02",
        )
    )

    CloseMessageWindow()

    #C0374
    ChrTalk(
        0x135,
        "#01809Fは、はいっ、ありがとうございます。\x02",
    )

    CloseMessageWindow()

    #C0375
    ChrTalk(
        0x101,
        (
            "#00012Fはは、面とむかって言うのも\x01",
            "なんだか照れちゃうけどな。\x02\x03",

            "#00000F……それじゃ、願い事も済んだし\x01",
            "そろそろ行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0376
    ChrTalk(
        0x135,
        "#01802Fええ、そうですね。\x02",
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
            "#01803F#11P（絶対に叶わない願い\x01",
            "  だったとしても……）\x02\x03",

            "#01808F（思っているだけなら\x01",
            "  許されますよね……？）\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_9B(0x0, 0x135, 0x0, 0x7D0, 0x7D0, 0x0)
    OP_0D()
    EndChrThread(0x101, 0x3)
    Return()

    # Function_39_AE2D end

    def Function_40_B7D8(): pass

    label("Function_40_B7D8")

    EventBegin(0x0)
    Call(0, 23)
    BeginChrThread(0x166, 3, 0, 25)
    WaitChrThread(0x166, 3)
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B8D5")

    #C0378
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "さっそく願い事をしてみよう。\x02\x03",

            "#00005Fえっと……この鏡の前で\x01",
            "願いを言えばいいのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0379
    ChrTalk(
        0x166,
        (
            "#14000F頭の中で願い事を考えるくらいで\x01",
            "いいんじゃねーの。\x02\x03",

            "#14003Fやるならさっさとやっちまおうぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B973")

    label("loc_B8D5")


    #C0380
    ChrTalk(
        0x101,
        (
            "#00000Fそれじゃあ、\x01",
            "願い事をしてみよう。\x02\x03",

            "#00004Fこの鏡の前で、願い事を\x01",
            "思い浮かべればいいはずだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0381
    ChrTalk(
        0x166,
        (
            "#14003F……ま、やるならさっさと\x01",
            "やっちまおうぜ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B973")

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
        "#00000F……こんなところかな。\x02",
    )

    CloseMessageWindow()

    #C0385
    ChrTalk(
        0x166,
        (
            "#14003Fん、オレもいい。\x02\x03",

            "#14000F……で、アンタはどんな\x01",
            "願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7FF0000), scpexpr(EXPR_AND), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BBAE")

    #C0386
    ChrTalk(
        0x101,
        (
            "#00000Fはは、まあ普通すぎて\x01",
            "ちょっと照れるんだけど……\x02\x03",

            "#00004F『クロスベルをこれからも\x01",
            "守っていけますように』かな。\x02\x03",

            "#00000Fもちろん、シュリたち\x01",
            "アルカンシェルの人も含めてね。\x02",
        )
    )

    CloseMessageWindow()

    #C0387
    ChrTalk(
        0x166,
        (
            "#14000Fふーん……\x01",
            "まあ、別にいいんじゃねえの。\x02",
        )
    )

    CloseMessageWindow()

    #C0388
    ChrTalk(
        0x101,
        (
            "#00009Fはは、そりゃどうも。\x02\x03",

            "#00000Fそういうシュリは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BCD2")

    label("loc_BBAE")


    #C0389
    ChrTalk(
        0x101,
        (
            "#00000F俺は、最初に来たときに\x01",
            "一番の願い事はしちゃったからな。\x02\x03",

            "#00004F同じ願い事をするのもなんだし、\x01",
            "『シュリの願いが叶いますように』\x01",
            "って願いにしたよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0390
    ChrTalk(
        0x166,
        "#14006Fちぇっ、余計なお世話だっての。\x02",
    )

    CloseMessageWindow()

    #C0391
    ChrTalk(
        0x101,
        (
            "#00000Fはは……\x01",
            "お節介だったかな。\x02\x03",

            "#00000Fそういうシュリは\x01",
            "どんな願い事をしたんだ？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BCD2")

    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    #C0392
    ChrTalk(
        0x166,
        (
            "#14003Fオレは……\x01",
            "願い事なんて何にもしてない。\x02",
        )
    )

    CloseMessageWindow()

    #C0393
    ChrTalk(
        0x101,
        (
            "#00006Fガクッ……\x01",
            "なんだよ、人に言わせといて。\x02",
        )
    )

    CloseMessageWindow()

    #C0394
    ChrTalk(
        0x166,
        (
            "#14006F……もともと、願い事なんて\x01",
            "そうそう叶うもんじゃないだろ。\x02\x03",

            "#14008Fオレがいたスラムがそうだったしな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0395
    ChrTalk(
        0x166,
        (
            "#14000F……故郷のスラムには、\x01",
            "オレみたいな奴が\x01",
            "まだまだいっぱいいた。\x02\x03",

            "#14003Fオレはクロスベルに流れてきて、\x01",
            "イリアさんに拾ってもらえたけど……\x01",
            "それは単に運が良かっただけだ。\x02\x03",

            "#14008Fそれなのに、\x01",
            "これ以上願い事だなんて\x01",
            "やっぱりムシが良すぎるしな。\x02",
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
            "#00004Fシュリ……\x01",
            "……君は優しいんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0397
    ChrTalk(
        0x166,
        "#14005F……え……\x02",
    )

    CloseMessageWindow()

    #C0398
    ChrTalk(
        0x101,
        (
            "#00002F他の誰かのために、\x01",
            "そんなに考えられる人は\x01",
            "なかなかいないと思う。\x02\x03",

            "#00004Fそれは君がとても優しくて、\x01",
            "人を思いやれる心を持ってるからだ。\x02\x03",

            "#00000Fでも……だからといって\x01",
            "君が幸せになっちゃいけない\x01",
            "なんてことはないだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0399
    ChrTalk(
        0x166,
        "#14008Fで、でも……\x02",
    )

    CloseMessageWindow()

    #C0400
    ChrTalk(
        0x101,
        (
            "#00000Fそんなに難しく考えなくていい。\x01",
            "要するに、願い事を持つくらいは\x01",
            "いいんじゃないかなってことさ。\x02",
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
            "#14006Fあーもう、分かったよ……\x01",
            "説教臭くてうるさい兄さんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0402
    ChrTalk(
        0x101,
        "#00006Fわ、悪かったな、説教臭くて。\x02",
    )

    CloseMessageWindow()
    OP_63(0x166, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x166)

    #C0403
    ChrTalk(
        0x166,
        (
            "#14003F……将来の事なんて分からないけど、\x01",
            "確かにオレにも叶えたいことはある。\x02\x03",

            "#14000F『今度のリニューアル公演の成功』……\x01",
            "とりあえずこれだけは何とか叶えたい。\x02\x03",

            "#14009F……こんなもんでいいか？\x02",
        )
    )

    CloseMessageWindow()

    #C0404
    ChrTalk(
        0x101,
        (
            "#00002Fああ、充分じゃないか？\x02\x03",

            "俺も、それが叶う事を\x01",
            "心から願わせてもらうよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0405
    ChrTalk(
        0x166,
        (
            "#14012Fめ、面と向かって\x01",
            "恥ずかしいこと言うんじゃねーっつの。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Return()

    # Function_40_B7D8 end

    def Function_41_C29F(): pass

    label("Function_41_C29F")

    EventBegin(0x1)

    #C0406
    ChrTalk(
        0x101,
        (
            "#00000F目指すは最上階だ。\x01",
            "さっそく行ってみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, -950, -53650, 0)
    EventEnd(0x4)
    Return()

    # Function_41_C29F end

    def Function_42_C2EC(): pass

    label("Function_42_C2EC")

    EventBegin(0x1)

    #C0407
    ChrTalk(
        0x101,
        (
            "#00000F上にある『鏡』の前で\x01",
            "願い事をしてみよう。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 0, 40550, -13830, 180)
    EventEnd(0x4)
    Return()

    # Function_42_C2EC end

    def Function_43_C339(): pass

    label("Function_43_C339")

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
            scpstr(SCPSTR_CODE_ITEM, 0x394),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x394, 1)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x18A, 4)
    OP_65(0x6, 0x1)
    EventEnd(0x3)
    Return()

    # Function_43_C339 end

    SaveToFile()

Try(main)
