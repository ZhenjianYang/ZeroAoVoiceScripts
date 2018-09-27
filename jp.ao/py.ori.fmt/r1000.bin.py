from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1000.bin",                # FileName
        "r1000",                    # MapName
        "r1000",                    # Location
        0x005F,                     # MapIndex
        "ed7205",
        0x00000000,                 # Flags
        ("r1000", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x05,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 95, 0, 2, 0, 3],
    )

    BuildStringList((
        "r1000",                  # 0
        "バス",                   # 1
        "バス",                   # 2
        "バス",                   # 3
        "車",                     # 4
        "SE制御",                 # 5
        "クロベルガ蟲",           # 6
        "クロベルガ蟲",           # 7
        "ガンテ",                 # 8
        "ガンテ",                 # 9
        "br1000",                 # 10
        "br1000",                 # 11
        "br1000",                 # 12
        "br1000",                 # 13
        "br1000",                 # 14
        "br1000",                 # 15
        "br1000",                 # 16
        "クロスベル市方面",       # 17
        "ベルガード門方面",       # 18
    ))

    ATBonus("ATBonus_4E4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_4112", 4,   2,   3,   0,   3,   0,   0)
    Sepith("Sepith_411A", 2,   0,   3,   4,   0,   0,   3)
    Sepith("Sepith_415A", 2,   1,   4,   1,   0,   2,   2)
    Sepith("Sepith_4152", 5,   5,   0,   3,   0,   0,   0)
    Sepith("Sepith_416A", 11,  7,   4,   3,   6,   12,  7)

    MonsterBattlePostion("MonsterBattlePostion_544", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_548", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_54C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_550", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_554", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_558", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_55C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_560", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_524", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_528", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_52C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_534", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_538", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_53C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_540", 2, 13, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_5C4", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_4112", 30, 40, 20, 10,
        (
            ("ms60900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms60900.dat", "ms60900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms60900.dat", "ms70400.dat", "ms60900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms60900.dat", "ms60900.dat", "ms74800.dat", "ms60900.dat", 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
        )
    )

    BattleInfo(
        "BattleInfo_68C", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_411A", 30, 40, 20, 10,
        (
            ("ms74800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms74800.dat", "ms74800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms74800.dat", "ms70400.dat", "ms74800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms74800.dat", "ms74800.dat", "ms60900.dat", "ms74800.dat", 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
        )
    )

    BattleInfo(
        "BattleInfo_754", 0x0000, 50, 6, 60, 8, 1, 25, 0, "br1000", "Sepith_415A", 30, 40, 20, 10,
        (
            ("ms71900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms71900.dat", "ms71900.dat", "ms71900.dat", "ms71900.dat", 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
        )
    )

    BattleInfo(
        "BattleInfo_81C", 0x0000, 50, 6, 60, 8, 1, 30, 0, "br1000", "Sepith_4152", 30, 40, 20, 10,
        (
            ("ms71500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms71500.dat", "ms71500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms71500.dat", "ms71900.dat", "ms71500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms71500.dat", "ms71500.dat", "ms70400.dat", "ms71500.dat", 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
        )
    )

    BattleInfo(
        "BattleInfo_8E4", 0x0000, 84, 6, 60, 6, 1, 30, 0, "br1000", "Sepith_416A", 40, 35, 25, 0,
        (
            ("ms60701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_544", "MonsterBattlePostion_5A4", "ed7450", "ed7453", "ATBonus_4E4"),
            (),
        )
    )

    # event battle count: 4

    BattleInfo(
        "BattleInfo_980", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "ms60900.dat", "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7453", "ed7453", "ATBonus_4E4"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_9C4", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", "ms60701.dat", 0, 0, "MonsterBattlePostion_524", "MonsterBattlePostion_5A4", "ed7453", "ed7453", "ATBonus_4E4"),
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
        "monster/ch60950.itc",               # 10
        "monster/ch60951.itc",               # 11
        "monster/ch74850.itc",               # 12
        "monster/ch74851.itc",               # 13
        "monster/ch71950.itc",               # 14
        "monster/ch71950.itc",               # 15
        "monster/ch71550.itc",               # 16
        "monster/ch71551.itc",               # 17
        "monster/ch60750.itc",               # 18
        "monster/ch60750.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-98569,  -2000,   46880,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-85819,  -2000,   14609,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-98569,  -2000,   46880,   270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-85819,  -2000,   14609,   270,  484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(-36920,  25180,   -2000,   0x1010000,    "BattleInfo_5C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-27400,  39160,   -2000,   0x1010000,    "BattleInfo_68C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-61100,  16450,   -2000,   0x1010000,    "BattleInfo_754", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-82360,  38870,   -2000,   0x1010000,    "BattleInfo_81C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-76380,  52370,   -2000,   0x1010000,    "BattleInfo_5C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-99040,  47600,   -2000,   0x1010000,    "BattleInfo_68C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-93520,  16270,   -2000,   0x1010000,    "BattleInfo_754", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-30170,  11920,   -2000,   0x1010000,    "BattleInfo_8E4", 0,   24,  0xFFFF, 10, 11)
    DeclMonster(-103540, 6520,    -1080,   0x1010000,    "BattleInfo_8E4", 0,   24,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 19,  -98.0,                 12.0,                  -3.0,                  15625.0,               [0.07071083039045334,  -0.028284205123782158, 0.0,                   0.0,                   0.07071051746606827,   0.028284333646297455,  -0.0,                  0.0,                   -0.0,                  -0.0,                  0.20000000298023224,   0.0,                   6.081135272979736,     -3.1112639904022217,   0.6000000238418579,    1.0])

    DeclActor(-4330,   -2000,   5700,    1200,    -4330,   -1000,   5700,    0x007C, 0,  15, 0x0000)
    DeclActor(-74580,  -2000,   56210,   1200,    -74580,  -1000,   56210,   0x007C, 0,  4,  0x0000)
    DeclActor(-23140,  -2000,   37630,   1200,    -23140,  -1000,   37630,   0x007C, 0,  5,  0x0000)
    DeclActor(-98570,  -2000,   46880,   1200,    -98570,  -2000,   46880,   0x007C, 0,  6,  0x0000)
    DeclActor(-85820,  -2000,   14610,   1200,    -85820,  -2000,   14610,   0x007C, 0,  7,  0x0000)
    DeclActor(-7010,   -2000,   11560,   1200,    -7010,   0,       11560,   0x007C, 0,  14, 0x0000)
    DeclActor(-6500,   -2000,   13000,   1200,    -6500,   0,       13000,   0x007C, 0,  14, 0x0000)
    DeclActor(-11530,  -2000,   5320,    1500,    -11530,  -300,    5320,    0x007C, 0,  27, 0x0000)

    PlaceName(23.0, 0.0, 4.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-137.0, 0.0, -28.0, 0x0000, 0x0000, "ベルガード門方面")
    PlaceName(-4.0, 0.0, 5.900000095367432, 0x0000, 0x0055, "")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_B08",          # 00, 0
        "Function_1_B27",          # 01, 1
        "Function_2_B46",          # 02, 2
        "Function_3_157C",         # 03, 3
        "Function_4_1C9D",         # 04, 4
        "Function_5_1DEE",         # 05, 5
        "Function_6_1F3F",         # 06, 6
        "Function_7_229D",         # 07, 7
        "Function_8_25FB",         # 08, 8
        "Function_9_2614",         # 09, 9
        "Function_10_2618",        # 0A, 10
        "Function_11_26D8",        # 0B, 11
        "Function_12_280B",        # 0C, 12
        "Function_13_285C",        # 0D, 13
        "Function_14_28F0",        # 0E, 14
        "Function_15_2C33",        # 0F, 15
        "Function_16_2E43",        # 10, 16
        "Function_17_3351",        # 11, 17
        "Function_18_3475",        # 12, 18
        "Function_19_34CC",        # 13, 19
        "Function_20_3B68",        # 14, 20
        "Function_21_3BCD",        # 15, 21
        "Function_22_3C32",        # 16, 22
        "Function_23_3C97",        # 17, 23
        "Function_24_3CB0",        # 18, 24
        "Function_25_3F7C",        # 19, 25
        "Function_26_401B",        # 1A, 26
        "Function_27_4084",        # 1B, 27
    ))


    def Function_0_B08(): pass

    label("Function_0_B08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B26")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_B08")

    label("loc_B26")

    Return()

    # Function_0_B08 end

    def Function_1_B27(): pass

    label("Function_1_B27")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B45")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_B27")

    label("loc_B45")

    Return()

    # Function_1_B27 end

    def Function_2_B46(): pass

    label("Function_2_B46")

    OP_D2(0x7, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B63")
    ClearScenarioFlags(0x22, 0)
    Event(0, 17)
    Jump("loc_B83")

    label("loc_B63")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_B77")
    ClearScenarioFlags(0x22, 1)
    Event(0, 24)
    Jump("loc_B83")

    label("loc_B77")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 2)), scpexpr(EXPR_END)), "loc_B83")
    ClearScenarioFlags(0x22, 2)

    label("loc_B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B94")
    Event(0, 16)

    label("loc_B94")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1038")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C21")
    SetScenarioFlags(0x38, 0)

    label("loc_C21")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C37")
    SetScenarioFlags(0x38, 1)

    label("loc_C37")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C4D")
    SetScenarioFlags(0x38, 2)

    label("loc_C4D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C63")
    SetScenarioFlags(0x38, 3)

    label("loc_C63")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C79")
    SetScenarioFlags(0x38, 4)

    label("loc_C79")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C8F")
    SetScenarioFlags(0x38, 5)

    label("loc_C8F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CA5")
    SetScenarioFlags(0x38, 6)

    label("loc_CA5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CBB")
    SetScenarioFlags(0x38, 7)

    label("loc_CBB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CD1")
    SetScenarioFlags(0x39, 0)

    label("loc_CD1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE7")
    SetScenarioFlags(0x39, 1)

    label("loc_CE7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CFD")
    SetScenarioFlags(0x39, 2)

    label("loc_CFD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D13")
    SetScenarioFlags(0x39, 3)

    label("loc_D13")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D29")
    SetScenarioFlags(0x39, 4)

    label("loc_D29")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D3F")
    SetScenarioFlags(0x39, 5)

    label("loc_D3F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D55")
    SetScenarioFlags(0x39, 6)

    label("loc_D55")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D6B")
    SetScenarioFlags(0x39, 7)

    label("loc_D6B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D81")
    SetScenarioFlags(0x3A, 0)

    label("loc_D81")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D97")
    SetScenarioFlags(0x3A, 1)

    label("loc_D97")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DAD")
    SetScenarioFlags(0x3A, 2)

    label("loc_DAD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DC3")
    SetScenarioFlags(0x3A, 3)

    label("loc_DC3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DD9")
    SetScenarioFlags(0x3A, 4)

    label("loc_DD9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DEF")
    SetScenarioFlags(0x3A, 5)

    label("loc_DEF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E05")
    SetScenarioFlags(0x3A, 6)

    label("loc_E05")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E1B")
    SetScenarioFlags(0x3A, 7)

    label("loc_E1B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E31")
    SetScenarioFlags(0x3B, 0)

    label("loc_E31")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E47")
    SetScenarioFlags(0x3B, 1)

    label("loc_E47")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5D")
    SetScenarioFlags(0x3B, 2)

    label("loc_E5D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E73")
    SetScenarioFlags(0x3B, 3)

    label("loc_E73")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E89")
    SetScenarioFlags(0x3B, 4)

    label("loc_E89")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E9F")
    SetScenarioFlags(0x3B, 5)

    label("loc_E9F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB5")
    SetScenarioFlags(0x3B, 6)

    label("loc_EB5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECB")
    SetScenarioFlags(0x3B, 7)

    label("loc_ECB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EE1")
    SetScenarioFlags(0x3D, 5)

    label("loc_EE1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF7")
    SetScenarioFlags(0x3D, 6)

    label("loc_EF7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F0D")
    SetScenarioFlags(0x3D, 7)

    label("loc_F0D")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F48")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1038")

    label("loc_F48")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6B")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1038")

    label("loc_F6B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8E")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1038")

    label("loc_F8E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB1")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1038")

    label("loc_FB1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD4")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1038")

    label("loc_FD4")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF7")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1038")

    label("loc_FF7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101A")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1038")

    label("loc_101A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1038")
    SetScenarioFlags(0x3C, 7)

    label("loc_1038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x35, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_104E")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_104E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1080")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1080")
    SetChrPos(0x0, -7000, -2000, 10900, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    Event(0, 13)

    label("loc_1080")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_10B3")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B3")
    SetChrPos(0x0, -6500, -2000, 13000, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_10B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3E, 0)), scpexpr(EXPR_END)), "loc_10C2")
    ClearScenarioFlags(0x3E, 0)
    Event(0, 12)

    label("loc_10C2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1578")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1161")
    SetScenarioFlags(0x38, 0)

    label("loc_1161")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1177")
    SetScenarioFlags(0x38, 1)

    label("loc_1177")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_118D")
    SetScenarioFlags(0x38, 2)

    label("loc_118D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A3")
    SetScenarioFlags(0x38, 3)

    label("loc_11A3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11B9")
    SetScenarioFlags(0x38, 4)

    label("loc_11B9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11CF")
    SetScenarioFlags(0x38, 5)

    label("loc_11CF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11E5")
    SetScenarioFlags(0x38, 6)

    label("loc_11E5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11FB")
    SetScenarioFlags(0x38, 7)

    label("loc_11FB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1211")
    SetScenarioFlags(0x39, 0)

    label("loc_1211")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1227")
    SetScenarioFlags(0x39, 1)

    label("loc_1227")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123D")
    SetScenarioFlags(0x39, 2)

    label("loc_123D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1253")
    SetScenarioFlags(0x39, 3)

    label("loc_1253")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1269")
    SetScenarioFlags(0x39, 4)

    label("loc_1269")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_127F")
    SetScenarioFlags(0x39, 5)

    label("loc_127F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1295")
    SetScenarioFlags(0x39, 6)

    label("loc_1295")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12AB")
    SetScenarioFlags(0x39, 7)

    label("loc_12AB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12C1")
    SetScenarioFlags(0x3A, 0)

    label("loc_12C1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D7")
    SetScenarioFlags(0x3A, 1)

    label("loc_12D7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12ED")
    SetScenarioFlags(0x3A, 2)

    label("loc_12ED")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1303")
    SetScenarioFlags(0x3A, 3)

    label("loc_1303")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1319")
    SetScenarioFlags(0x3A, 4)

    label("loc_1319")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132F")
    SetScenarioFlags(0x3A, 5)

    label("loc_132F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1345")
    SetScenarioFlags(0x3A, 6)

    label("loc_1345")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_135B")
    SetScenarioFlags(0x3A, 7)

    label("loc_135B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1371")
    SetScenarioFlags(0x3B, 0)

    label("loc_1371")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1387")
    SetScenarioFlags(0x3B, 1)

    label("loc_1387")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_139D")
    SetScenarioFlags(0x3B, 2)

    label("loc_139D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13B3")
    SetScenarioFlags(0x3B, 3)

    label("loc_13B3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13C9")
    SetScenarioFlags(0x3B, 4)

    label("loc_13C9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13DF")
    SetScenarioFlags(0x3B, 5)

    label("loc_13DF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13F5")
    SetScenarioFlags(0x3B, 6)

    label("loc_13F5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_140B")
    SetScenarioFlags(0x3B, 7)

    label("loc_140B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1421")
    SetScenarioFlags(0x3D, 5)

    label("loc_1421")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1437")
    SetScenarioFlags(0x3D, 6)

    label("loc_1437")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_144D")
    SetScenarioFlags(0x3D, 7)

    label("loc_144D")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1488")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1578")

    label("loc_1488")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AB")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1578")

    label("loc_14AB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CE")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1578")

    label("loc_14CE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14F1")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1578")

    label("loc_14F1")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1514")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1578")

    label("loc_1514")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1537")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1578")

    label("loc_1537")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155A")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1578")

    label("loc_155A")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1578")
    SetScenarioFlags(0x3C, 7)

    label("loc_1578")

    Call(0, 8)
    Return()

    # Function_2_B46 end

    def Function_3_157C(): pass

    label("Function_3_157C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_158E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_158E")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_15A6")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_15A6")

    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1AB5")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1AB5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1B31")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    Jump("loc_1B73")

    label("loc_1B31")

    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)

    label("loc_1B73")

    MiniGame(0x2F, 0x5, 0x6, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetMapObjFlags(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BB3")
    OP_70(0x1, 0x0)
    Jump("loc_1BB7")

    label("loc_1BB3")

    OP_70(0x1, 0x1E)

    label("loc_1BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BCA")
    OP_70(0x2, 0x0)
    Jump("loc_1BCE")

    label("loc_1BCA")

    OP_70(0x2, 0x1E)

    label("loc_1BCE")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C2F")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -98570, -2000, 46880, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1C2F")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1C7B")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -85820, -2000, 14610, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1C7B")

    OP_1C(0x0, 0x13, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    OP_1C(0x0, 0x14, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    OP_1C(0x0, 0x15, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    Return()

    # Function_3_157C end

    def Function_4_1C9D(): pass

    label("Function_4_1C9D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D9D")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_1D26")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_1D98")

    label("loc_1D26")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D98")

    Jump("loc_1DE2")

    label("loc_1D9D")

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

    label("loc_1DE2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1C9D end

    def Function_5_1DEE(): pass

    label("Function_5_1DEE")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EEE")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_1E77")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E2, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1EE9")

    label("loc_1E77")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1EE9")

    Jump("loc_1F33")

    label("loc_1EEE")

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

    label("loc_1F33")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1DEE end

    def Function_6_1F3F(): pass

    label("Function_6_1F3F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20F7")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_END)), "loc_20D8")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20D3")
    ClearScenarioFlags(0x3A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_20D0")
    ClearScenarioFlags(0x38, 0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1FF9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1FF9)
    TurnDirection(0xD, 0x0, 0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    PlayEffect(0x7, 0x1, 0xD, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_980", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20CB")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20B2")
    Call(1, 5)
    Jump("loc_20CB")

    label("loc_20B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20C8")
    Call(1, 4)
    Jump("loc_20CB")

    label("loc_20C8")

    Call(1, 3)

    label("loc_20CB")

    Jump("loc_20D3")

    label("loc_20D0")

    Call(1, 1)

    label("loc_20D3")

    Jump("loc_20EE")

    label("loc_20D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_20EE")
    ClearScenarioFlags(0x38, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_20EE")

    TalkEnd(0xFF)
    Return()

    label("loc_20F7")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 0)), scpexpr(EXPR_END)), "loc_2282")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_227D")
    ClearScenarioFlags(0x3A, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_227A")
    ClearScenarioFlags(0x38, 0)
    OP_A7(0xF, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_21A3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_21A3)
    TurnDirection(0xF, 0x0, 0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    PlayEffect(0x7, 0x1, 0xF, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_9C4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xF, 0x80)
    ClearChrFlags(0xF, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2275")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_225C")
    Call(1, 5)
    Jump("loc_2275")

    label("loc_225C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2272")
    Call(1, 4)
    Jump("loc_2275")

    label("loc_2272")

    Call(1, 3)

    label("loc_2275")

    Jump("loc_227D")

    label("loc_227A")

    Call(1, 1)

    label("loc_227D")

    Jump("loc_2298")

    label("loc_2282")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 0)), scpexpr(EXPR_END)), "loc_2298")
    ClearScenarioFlags(0x38, 0)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2298")

    TalkEnd(0xFF)
    Return()

    # Function_6_1F3F end

    def Function_7_229D(): pass

    label("Function_7_229D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2455")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_2436")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2431")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_242E")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2357():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_2357)
    TurnDirection(0xE, 0x0, 0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    PlayEffect(0x7, 0x1, 0xE, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_980", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2429")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2410")
    Call(1, 5)
    Jump("loc_2429")

    label("loc_2410")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2426")
    Call(1, 4)
    Jump("loc_2429")

    label("loc_2426")

    Call(1, 3)

    label("loc_2429")

    Jump("loc_2431")

    label("loc_242E")

    Call(1, 1)

    label("loc_2431")

    Jump("loc_244C")

    label("loc_2436")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_244C")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_244C")

    TalkEnd(0xFF)
    Return()

    label("loc_2455")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 1)), scpexpr(EXPR_END)), "loc_25E0")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "何かが埋まっているようだ。\x01",
            "掘り出しますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は  い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25DB")
    ClearScenarioFlags(0x3A, 1)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_25D8")
    ClearScenarioFlags(0x38, 1)
    OP_A7(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2501():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_2501)
    TurnDirection(0x10, 0x0, 0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    PlayEffect(0x7, 0x1, 0x10, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_9C4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    ClearChrFlags(0x10, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25D3")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_25BA")
    Call(1, 5)
    Jump("loc_25D3")

    label("loc_25BA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_25D0")
    Call(1, 4)
    Jump("loc_25D3")

    label("loc_25D0")

    Call(1, 3)

    label("loc_25D3")

    Jump("loc_25DB")

    label("loc_25D8")

    Call(1, 1)

    label("loc_25DB")

    Jump("loc_25F6")

    label("loc_25E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 1)), scpexpr(EXPR_END)), "loc_25F6")
    ClearScenarioFlags(0x38, 1)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_25F6")

    TalkEnd(0xFF)
    Return()

    # Function_7_229D end

    def Function_8_25FB(): pass

    label("Function_8_25FB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2613")
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)

    label("loc_2613")

    Return()

    # Function_8_25FB end

    def Function_9_2614(): pass

    label("Function_9_2614")

    Call(1, 6)
    Return()

    # Function_9_2614 end

    def Function_10_2618(): pass

    label("Function_10_2618")

    EventBegin(0x2)
    SetMapFlags(0x8000000)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1Kバス停がある。\x01",
            "バスで移動しますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ベルガード門\x01",                # 0
            "停留所（警察学校付近）\x01",      # 1
            "やめる\x01",                      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26B0")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("t2000", 0, 0, 0)
    IdleLoop()
    Jump("loc_26D0")

    label("loc_26B0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D0")
    Call(0, 11)
    ClearMapFlags(0x8000000)
    NewScene("r1030", 0, 0, 0)
    IdleLoop()

    label("loc_26D0")

    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Return()

    # Function_10_2618 end

    def Function_11_26D8(): pass

    label("Function_11_26D8")

    ClearMapFlags(0x1)
    SetEventSkip(0x0, "loc_2807")
    Fade(500)
    OP_68(-9910, -1400, 11630, 0)
    MoveCamera(39, 32, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(24500, 0)
    OP_E2(0x1)
    SetChrPos(0x0, -5700, -2000, 5500, 0)
    SetChrPos(0x1, -7000, -2000, 5500, 0)
    SetChrPos(0x2, -8300, -2000, 5500, 0)
    SetChrPos(0x3, -9600, -2000, 5500, 0)
    ClearChrFlags(0x8, 0x80)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x0, 0x2)
    OP_78(0x0, 0x8)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0x8, -21340, -2000, 9000, 0)
    OP_D5(0x8, 0x0, 0x15F90, 0x0, 0x0)
    SetMapObjFlags(0x0, 0x1000)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x79, 0xB4, 0x0, 0x20)

    def lambda_27BE():
        OP_95(0xFE, -8200, -2000, 9000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27BE)
    OP_0D()
    Sound(466, 0, 100, 0)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x8, 1)
    OP_71(0x0, 0x5B, 0x78, 0x0, 0x0)
    OP_79(0x0)
    Sleep(300)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetEventSkip(0x1, 0x0)

    label("loc_2807")

    SetScenarioFlags(0x3E, 0)
    Return()

    # Function_11_26D8 end

    def Function_12_280B(): pass

    label("Function_12_280B")

    EventBegin(0x1)
    FadeToDark(0, 0, -1)
    OP_0D()
    SetChrPos(0x0, -5770, -2000, 5580, 270)
    OP_31(0x1)
    OP_68(-5770, -1400, 5580, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24500, 0)
    EventEnd(0x5)
    Return()

    # Function_12_280B end

    def Function_13_285C(): pass

    label("Function_13_285C")

    EventBegin(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(0, 0, -1)
    Sleep(100)
    Sound(459, 0, 100, 0)
    Sleep(2000)
    StopSound(459, 1000, 100)
    Sound(492, 0, 70, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_28B7")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28AC")
    Sound(2502, 255, 100, 0)    #voice#Noel
    Jump("loc_28B2")

    label("loc_28AC")

    Sound(2503, 255, 100, 0)    #voice#Noel

    label("loc_28B2")

    Jump("loc_28DB")

    label("loc_28B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_28D5")
    Sound(3347, 255, 100, 0)    #voice#Lloyd
    Jump("loc_28DB")

    label("loc_28D5")

    Sound(3348, 255, 100, 0)    #voice#Lloyd

    label("loc_28DB")

    Sleep(500)
    FadeToBright(500, 0)
    OP_0D()
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_13_285C end

    def Function_14_28F0(): pass

    label("Function_14_28F0")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2922")
    SetScenarioFlags(0x31, 2)

    label("loc_2922")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2968")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_2962")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2957")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_295D")

    label("loc_2957")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_295D")

    Jump("loc_2968")

    label("loc_2962")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_2968")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C25")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_29E1")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "メルカバに乗り込む")
    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29C1"),
        (SWITCH_DEFAULT, "loc_29D2"),
    )


    label("loc_29C1")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_29DC")

    label("loc_29D2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_29DC")

    Jump("loc_2C20")

    label("loc_29E1")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "導力車で移動する")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2A15")
    MenuCmd(1, 0, "導力車で休憩する")

    label("loc_2A15")

    MenuCmd(1, 0, "やめる")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2A49"),
        (1, "loc_2B4D"),
        (2, "loc_2BDE"),
        (SWITCH_DEFAULT, "loc_2C16"),
    )


    label("loc_2A49")

    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A7A")
    OP_70(0x3, 0x12C)
    OP_71(0x3, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_2A8A")

    label("loc_2A7A")

    OP_70(0x3, 0xF0)
    OP_71(0x3, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_2A8A")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2AE0")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B03")
    Sound(461, 0, 100, 0)

    label("loc_2B03")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B23")
    OP_70(0x3, 0x14A)
    OP_71(0x3, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_2B33")

    label("loc_2B23")

    OP_70(0x3, 0x10E)
    OP_71(0x3, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_2B33")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x3, "light", 0x1, 0x1)
    OP_70(0x3, 0x0)
    Jump("loc_2968")

    label("loc_2B4D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_2BBF")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_2B82")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_2B9A")

    label("loc_2B82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2B95")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_2B9A")

    label("loc_2B95")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_2B9A")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BD9")

    label("loc_2BBF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2BCF")
    OP_AF(0xFB)
    Jump("loc_2BD9")

    label("loc_2BCF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2BD9")

    Jump("loc_2C20")

    label("loc_2BDE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BF7")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C11")

    label("loc_2BF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_2C07")
    OP_AF(0xFB)
    Jump("loc_2C11")

    label("loc_2C07")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C11")

    Jump("loc_2C20")

    label("loc_2C16")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C20")

    Jump("loc_2968")

    label("loc_2C25")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_14_28F0 end

    def Function_15_2C33(): pass

    label("Function_15_2C33")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D84")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0017
    ChrTalk(
        0x101,
        (
            "#00000F警察学校までは歩いて行こう。\x01",
            "いい運動にもなりそうだしな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12D, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D81")
    Sound(814, 0, 100, 0)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ストーリーが進行すると、\x01",
            "各地の停留所からバスを\x01",
            "利用できるようになります。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #A0019
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "街道の行き来に便利ですので、\x01",
            "時期が来た後にご活用ください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x12D, 5)

    label("loc_2D81")

    EventEnd(0x3)
    Return()

    label("loc_2D84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DF7")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0020
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "バス停がある。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0021
    ChrTalk(
        0x101,
        (
            "#00001F事故のこともあるし、\x01",
            "バスを待ってる時間はないな。\x02",
        )
    )

    CloseMessageWindow()
    EventEnd(0x3)
    Return()

    label("loc_2DF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_2E3F")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力バスは運行を見合わせているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    EventEnd(0x3)
    Return()

    label("loc_2E3F")

    Call(0, 10)
    Return()

    # Function_15_2C33 end

    def Function_16_2E43(): pass

    label("Function_16_2E43")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    OP_68(10470, 1300, -500, 0)
    MoveCamera(44, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17850, 0)
    SetChrPos(0x101, 16000, 0, 0, 270)
    SetChrPos(0x102, 17500, 0, -1000, 270)
    SetChrPos(0x109, 17500, 0, 750, 270)
    SetChrPos(0x105, 18500, 0, 250, 270)
    FadeToBright(1000, 0)
    SetCameraDistance(16350, 3000)

    def lambda_2EDA():
        OP_9B(0x0, 0x101, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2EDA)
    Sleep(0)

    def lambda_2EF2():
        OP_9B(0x0, 0x102, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2EF2)
    Sleep(0)

    def lambda_2F0A():
        OP_9B(0x0, 0x109, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F0A)
    Sleep(0)

    def lambda_2F22():
        OP_9B(0x0, 0x105, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2F22)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)
    OP_0D()
    TurnDirection(0x101, 0x105, 500)
    Sleep(50)

    def lambda_2F57():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_2F57)
    Sleep(100)

    def lambda_2F67():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2F67)
    Sleep(100)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0023
    ChrTalk(
        0x101,
        (
            "#00000F#6Pさてと……\x01",
            "みんな、どうする？\x02\x03",

            "警察学校まで行くとしたら\x01",
            "徒歩かバスになるけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        (
            "#00105F#11Pそうね……\x01",
            "私はどちらでもいいわ。\x02\x03",

            "#00100F最近、歩いてなかったから\x01",
            "ちょっと身体を動かしたいし。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x109,
        (
            "#10100F#5Pそれに確か、西クロスベル街道に\x01",
            "手配魔獣が出ていましたよね。\x02\x03",

            "だったらついでですし、\x01",
            "歩いた方がいいかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        (
            "#10306F#11Pおいおい、本気かい？\x02\x03",

            "#10301Fさすがに徒歩なんて\x01",
            "ダルすぎる気がするけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_312A():
        TurnDirection(0x109, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_312A)
    Sleep(50)

    def lambda_313A():
        TurnDirection(0x102, 0x105, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_313A)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x102, 0)

    #C0027
    ChrTalk(
        0x109,
        (
            "#10106F#5Pもう、いい若者が\x01",
            "そんなことじゃ情けないよ？\x02\x03",

            "#10101F普段、夜遊びばかりしてるんだから\x01",
            "こういう時に身体を動かさないと！\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x105,
        (
            "#10306F#11P体育会系のノリは\x01",
            "あまり趣味じゃないんだけどな。\x02\x03",

            "#10302Fま、いっか。\x02\x03",

            "#10309F疲れたら優しいリーダーに\x01",
            "負ぶってもらえばいいんだし㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#00003F#6P負ぶらないから。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0030
    ChrTalk(
        0x102,
        (
            "#00102F#11Pふふ、それじゃあ徒歩で\x01",
            "出発する事にしましょうか。\x02\x03",

            "#00100F手配魔獣が出るかもしれないから\x01",
            "気をつけないとね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)

    #C0031
    ChrTalk(
        0x109,
        "#10102F#5P了解しました！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 9500, 0, 0, 270)
    SetScenarioFlags(0x126, 6)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_16_2E43 end

    def Function_17_3351(): pass

    label("Function_17_3351")

    EventBegin(0x0)
    OP_E2(0x1)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    SoundLoad(468)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x3, 0xB)
    OP_49()
    SetChrPos(0xB, -25550, -1850, 10450, 90)
    OP_D5(0xB, 0x0, 0x15F90, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x1, 0x20)
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xD5, 0x8F, 0x7B, 0x5A, 0x78, 0x0)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    FadeToBright(1000, 0)
    Sound(468, 2, 100, 0)
    Sound(458, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 18)
    OP_68(-17300, -1500, 0, 0)
    MoveCamera(48, 23, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28650, 0)
    OP_68(7250, 1000, 0, 9500)
    Sleep(9000)
    OP_0D()
    StopSound(468, 1000, 100)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 1)
    NewScene("c0200", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3351 end

    def Function_18_3475(): pass

    label("Function_18_3475")

    SetChrPos(0xFE, -25550, -1850, 10450, 90)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -16149, -1850, 450)
    OP_9F(0x1, -950, -1600, 0)
    OP_9F(0x1, 8050, 0, 0)
    OP_9F(0x1, 35200, 0, 0)
    OP_9F(0x2, 0xFE, 6000, 0x6)
    Return()

    # Function_18_3475 end

    def Function_19_34CC(): pass

    label("Function_19_34CC")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    SoundLoad(469)
    OP_68(-99750, -1400, 10300, 0)
    MoveCamera(45, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23950, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -94100, -2000, 15900, 225)
    SetChrPos(0x102, -92460, -2000, 16149, 225)
    SetChrPos(0x103, -92860, -2000, 18300, 225)
    SetChrPos(0x104, -90900, -2000, 18350, 225)
    SetChrPos(0x109, -90150, -2000, 20400, 225)
    SetChrPos(0x105, -88650, -2000, 19200, 225)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x5, 0x8)
    OP_49()
    SetChrPos(0x8, -135050, 500, -25100, 45)
    OP_D5(0x8, 0x0, 0xAFC8, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x6, 0x9)
    OP_49()
    SetChrPos(0x9, -145050, 500, -35100, 45)
    OP_D5(0x9, 0x0, 0xAFC8, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x7, 0xA)
    OP_49()
    SetChrPos(0xA, -155050, 500, -45100, 45)
    OP_D5(0xA, 0x0, 0xAFC8, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x1, 0x20)
    FadeToBright(1000, 0)
    OP_68(-97150, -1400, 12900, 4000)
    MoveCamera(45, 18, 0, 4000)
    SetCameraDistance(19800, 4000)

    def lambda_36D1():
        OP_95(0xFE, -98100, -2000, 11900, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36D1)

    def lambda_36EB():
        OP_95(0xFE, -96960, -2000, 11650, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_36EB)

    def lambda_3705():
        OP_95(0xFE, -97860, -2000, 13300, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3705)

    def lambda_371F():
        OP_95(0xFE, -96400, -2000, 12850, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_371F)

    def lambda_3739():
        OP_95(0xFE, -96150, -2000, 14400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_3739)

    def lambda_3753():
        OP_95(0xFE, -95150, -2000, 12700, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3753)
    Sleep(2500)
    Sound(467, 0, 100, 0)
    WaitChrThread(0x101, 1)
    Sound(469, 2, 100, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    EndChrThread(0x109, 0x1)
    EndChrThread(0x105, 0x1)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    Fade(1000)
    SetChrPos(0x101, -91200, -2000, 12420, 261)
    SetChrPos(0x102, -90230, -2000, 13370, 261)
    SetChrPos(0x103, -91090, -2000, 11380, 261)
    SetChrPos(0x104, -88810, -2000, 12920, 261)
    SetChrPos(0x109, -88260, -2000, 14040, 261)
    SetChrPos(0x105, -88570, -2000, 12010, 261)
    OP_68(-131770, 1650, -15610, 0)
    MoveCamera(57, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21400, 0)
    OP_68(-131770, 6350, -15610, 14000)
    BeginChrThread(0xC, 1, 0, 23)
    BeginChrThread(0x8, 3, 0, 20)
    BeginChrThread(0x9, 3, 0, 21)
    BeginChrThread(0xA, 3, 0, 22)
    Sleep(13000)
    OP_0D()
    Fade(1000)
    OP_68(-96670, 400, 10000, 0)
    MoveCamera(350, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17250, 0)
    SetCameraDistance(15750, 2500)
    SetChrPos(0x101, -98100, -2000, 11900, 45)
    SetChrPos(0x102, -96960, -2000, 11650, 45)
    SetChrPos(0x103, -97860, -2000, 13300, 45)
    SetChrPos(0x104, -96400, -2000, 12850, 45)
    SetChrPos(0x109, -96150, -2000, 14400, 45)
    SetChrPos(0x105, -95150, -2000, 12700, 45)
    ClearChrFlags(0x101, 0x8)
    ClearChrFlags(0x102, 0x8)
    ClearChrFlags(0x103, 0x8)
    ClearChrFlags(0x104, 0x8)
    ClearChrFlags(0x109, 0x8)
    ClearChrFlags(0x105, 0x8)
    EndChrThread(0x8, 0x3)
    EndChrThread(0x9, 0x3)
    EndChrThread(0xA, 0x3)
    SetChrPos(0x8, 26700, -2000, -11460, 0)
    SetChrPos(0x9, 30110, -2000, -11480, 0)
    SetChrPos(0xA, 33470, -2000, -11600, 0)
    OP_D5(0x8, 0x0, 0x0, 0x0, 0x0)
    OP_D5(0x9, 0x0, 0x0, 0x0, 0x0)
    OP_D5(0xA, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_6F(0x79)
    OP_0D()

    #C0032
    ChrTalk(
        0x101,
        "#00001F#6P今のバスは……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x109,
        (
            "#10108F#5P共和国方面への行き来に\x01",
            "使われている旅客バスですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        (
            "#00103F#6P多分、列車に乗っていた乗客を\x01",
            "振替#4Rふりかえ#輸送しているんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#00306F#6Pやれやれ、大変だな。\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x103,
        (
            "#00208F#5P……事故の規模は\x01",
            "どの程度なんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -98000, -2000, 12000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x162, 7)
    ModifyEventFlags(0, 0, 0x80)
    OP_24(0x1D5)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_34CC end

    def Function_20_3B68(): pass

    label("Function_20_3B68")

    SetChrPos(0xFE, -135050, 500, -25100, 45)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -110800, 500, -1130)
    OP_9F(0x1, -105900, -350, 4220)
    OP_9F(0x1, -98460, -1750, 11450)
    OP_9F(0x1, -82910, -1750, 26520)
    OP_9F(0x1, -65770, -1750, 31700)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_20_3B68 end

    def Function_21_3BCD(): pass

    label("Function_21_3BCD")

    SetChrPos(0xFE, -145050, 500, -35100, 45)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -110800, 500, -1130)
    OP_9F(0x1, -105900, -350, 4220)
    OP_9F(0x1, -98460, -1750, 11450)
    OP_9F(0x1, -82910, -1750, 26520)
    OP_9F(0x1, -65770, -1750, 31700)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_21_3BCD end

    def Function_22_3C32(): pass

    label("Function_22_3C32")

    SetChrPos(0xFE, -155050, 500, -45100, 45)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -110800, 500, -1130)
    OP_9F(0x1, -105900, -350, 4220)
    OP_9F(0x1, -98460, -1750, 11450)
    OP_9F(0x1, -82910, -1750, 26520)
    OP_9F(0x1, -65770, -1750, 31700)
    OP_9F(0x2, 0xFE, 6500, 0x6)
    Return()

    # Function_22_3C32 end

    def Function_23_3C97(): pass

    label("Function_23_3C97")

    Sound(465, 0, 100, 0)
    Sleep(5000)
    Sound(471, 0, 100, 0)
    Sleep(3000)
    StopSound(469, 4000, 100)
    Return()

    # Function_23_3C97 end

    def Function_24_3CB0(): pass

    label("Function_24_3CB0")

    EventBegin(0x0)
    OP_E2(0x1)
    FadeToDark(0, 0, -1)
    SoundLoad(469)
    SetChrFlags(0x101, 0x8)
    SetChrFlags(0x102, 0x8)
    SetChrFlags(0x109, 0x8)
    SetChrFlags(0x105, 0x8)
    ClearChrFlags(0xB, 0x80)
    OP_78(0x3, 0xB)
    OP_49()
    SetChrPos(0xB, -57790, -2000, 29140, 270)
    OP_D5(0xB, 0x0, 0x41EB0, 0x0, 0x0)
    ClearMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0x8, 0x80)
    OP_78(0x5, 0x8)
    OP_49()
    SetChrPos(0x8, -135050, 500, -25100, 45)
    OP_D5(0x8, 0x0, 0xAFC8, 0x0, 0x0)
    ClearMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x5, 0x1000)
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0x9, 0x80)
    OP_78(0x6, 0x9)
    OP_49()
    SetChrPos(0x9, -145050, 500, -35100, 45)
    OP_D5(0x9, 0x0, 0xAFC8, 0x0, 0x0)
    ClearMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x6, 0x1000)
    SetMapObjFrame(0x6, "light", 0x0, 0x1)
    OP_74(0x6, 0x1E)
    OP_71(0x6, 0x79, 0xB4, 0x1, 0x20)
    ClearChrFlags(0xA, 0x80)
    OP_78(0x7, 0xA)
    OP_49()
    SetChrPos(0xA, -155050, 500, -45100, 45)
    OP_D5(0xA, 0x0, 0xAFC8, 0x0, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x7, 0x1000)
    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_74(0x7, 0x1E)
    OP_71(0x7, 0x79, 0xB4, 0x1, 0x20)
    FadeToBright(1000, 0)
    BeginChrThread(0xB, 3, 0, 25)
    OP_68(-93200, 1300, 13900, 0)
    MoveCamera(60, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(36850, 0)
    OP_68(-93200, -2000, 13900, 4500)
    OP_6F(0x79)
    Sound(467, 0, 100, 0)
    OP_0D()
    WaitChrThread(0xB, 3)
    BeginChrThread(0xC, 1, 0, 26)
    Sleep(1500)
    Fade(1000)
    SetChrPos(0xB, -88650, -2000, 12450, 225)
    OP_70(0x3, 0x78)
    BeginChrThread(0xC, 1, 0, 23)
    BeginChrThread(0x8, 3, 0, 20)
    BeginChrThread(0x9, 3, 0, 21)
    BeginChrThread(0xA, 3, 0, 22)
    OP_68(-131770, 1650, -15610, 0)
    MoveCamera(57, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21400, 0)
    OP_68(-131770, 6350, -15610, 14000)
    Sleep(13000)
    OP_0D()
    Sound(469, 2, 70, 0)
    Sound(471, 0, 100, 0)
    Fade(1000)
    OP_68(-90850, 400, 13250, 0)
    MoveCamera(0, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(24500, 0)
    SetCameraDistance(22000, 5000)
    OP_6F(0x79)
    OP_0D()
    StopSound(469, 500, 70)
    StopSound(471, 1000, 100)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 7)
    NewScene("e2010", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_24_3CB0 end

    def Function_25_3F7C(): pass

    label("Function_25_3F7C")

    SetChrPos(0xFE, -57790, -2000, 29140, 270)
    Sound(458, 0, 100, 0)
    OP_9F(0x0, 0xFE)
    OP_9F(0x1, -64860, -2000, 31710)
    OP_9F(0x1, -74690, -2000, 31380)
    OP_9F(0x1, -80190, -2000, 29170)
    OP_9F(0x1, -88190, -2000, 21170)
    OP_9F(0x2, 0xFE, 7500, 0x6)
    Sound(492, 0, 60, 0)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x1770, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0xBB8, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x3E8, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x3E8, 0x1)
    Return()

    # Function_25_3F7C end

    def Function_26_401B(): pass

    label("Function_26_401B")

    Sound(469, 2, 30, 0)
    Sleep(150)
    OP_25(0x1D5, 0x23)
    Sleep(150)
    OP_25(0x1D5, 0x28)
    Sleep(150)
    OP_25(0x1D5, 0x2D)
    Sleep(150)
    OP_25(0x1D5, 0x32)
    Sleep(150)
    OP_25(0x1D5, 0x37)
    Sleep(150)
    OP_25(0x1D5, 0x3C)
    Sleep(150)
    OP_25(0x1D5, 0x41)
    Sleep(150)
    OP_25(0x1D5, 0x46)
    Sleep(150)
    OP_25(0x1D5, 0x4B)
    Sleep(150)
    OP_25(0x1D5, 0x50)
    Sleep(150)
    OP_25(0x1D5, 0x55)
    Sleep(150)
    OP_25(0x1D5, 0x5A)
    Sleep(150)
    OP_25(0x1D5, 0x5F)
    Sleep(150)
    OP_25(0x1D5, 0x64)
    Return()

    # Function_26_401B end

    def Function_27_4084(): pass

    label("Function_27_4084")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東・クロスベル市\x01",
            "西・ベルガード門　１９８セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_27_4084 end

    SaveToFile()

Try(main)
