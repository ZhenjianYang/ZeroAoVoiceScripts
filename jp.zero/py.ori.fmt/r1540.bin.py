from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1540.bin",                # FileName
        "r1540",                    # MapName
        "r1540",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1540", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 96, 0, 1, 0, 2],
    )

    BuildStringList((
        "r1540",                  # 0
        "チルル",                 # 1
        "br1530",                 # 2
        "br1530",                 # 3
        "br1530",                 # 4
        "br1530",                 # 5
        "br1530",                 # 6
        "br1530",                 # 7
        "クロスベル市方面",       # 8
        "ウルスラ医科大学方面",   # 9
    ))

    ATBonus("ATBonus_3D8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_16DE", 0,   0,   9,   2,   5,   0,   4)
    Sepith("Sepith_16EE", 0,   9,   2,   0,   3,   3,   3)
    Sepith("Sepith_16D6", 2,   8,   0,   6,   2,   0,   0)
    Sepith("Sepith_16E6", 9,   4,   0,   2,   0,   2,   3)
    Sepith("Sepith_171E", 28,  28,  28,  28,  28,  28,  28)
    Sepith("Sepith_1726", 9,   7,   18,  6,   7,   6,   3)

    MonsterBattlePostion("MonsterBattlePostion_438", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_49C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_418", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 2, 13, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_554", 0x0000, 12, 6, 45, 10, 1, 40, 0, "br1530", "Sepith_16DE", 30, 40, 20, 10,
        (
            ("ms65700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms65700.dat", "ms65700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms65700.dat", "ms65700.dat", "ms65700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms65700.dat", "ms65700.dat", "ms62100.dat", "ms65700.dat", 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
        )
    )

    BattleInfo(
        "BattleInfo_7AC", 0x0000, 6, 6, 45, 10, 1, 65, 0, "br1530", "Sepith_16EE", 85, 5, 5, 5,
        (
            ("ms70800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms70800.dat", "ms70800.dat", "ms70800.dat", "ms61400.dat", 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms70800.dat", "ms70700.dat", "ms70800.dat", "ms70800.dat", 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms70800.dat", "ms70700.dat", "ms70800.dat", "ms61400.dat", 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
        )
    )

    BattleInfo(
        "BattleInfo_6E4", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1530", "Sepith_16D6", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
        )
    )

    BattleInfo(
        "BattleInfo_61C", 0x0000, 12, 6, 45, 10, 1, 40, 0, "br1530", "Sepith_16E6", 30, 40, 20, 10,
        (
            ("ms61100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms61100.dat", "ms61100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
        )
    )

    BattleInfo(
        "BattleInfo_874", 0x0000, 12, 6, 90, 8, 1, 50, 0, "br1530", "Sepith_171E", 30, 40, 20, 10,
        (
            ("ms66401.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms66401.dat", "ms66401.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms66401.dat", "ms66401.dat", "ms66401.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms66401.dat", "ms66401.dat", "ms66401.dat", "ms66401.dat", 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
        )
    )

    BattleInfo(
        "BattleInfo_4B8", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br1530", "Sepith_1726", 40, 35, 25, 0,
        (
            ("ms70201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_438", "MonsterBattlePostion_498", "ed7400", "ed7403", "ATBonus_3D8"),
            (),
        )
    )

    AddCharChip((
        "chr/ch20500.itc",                   # 00
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
        "monster/ch70250.itc",               # 10
        "monster/ch70251.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "monster/ch65750.itc",               # 14
        "monster/ch65751.itc",               # 15
        "monster/ch61150.itc",               # 16
        "monster/ch61150.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "monster/ch70850.itc",               # 1A
        "monster/ch70851.itc",               # 1B
        "monster/ch66450.itc",               # 1C
        "monster/ch66450.itc",               # 1D
    ))

    DeclNpc(-64129,  6300,    18979,   356,  385,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)

    DeclMonster(-16149,  -15050,  0,       0x1010000,    "BattleInfo_554", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-29300,  -27360,  0,       0x1010000,    "BattleInfo_7AC", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(-27960,  -49820,  0,       0x1010000,    "BattleInfo_6E4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(-50100,  -41380,  0,       0x1010000,    "BattleInfo_61C", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-62780,  15730,   6300,    0x1010000,    "BattleInfo_554", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-70810,  -52410,  -2100,   0x1010000,    "BattleInfo_61C", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-83770,  -55240,  -2100,   0x1010000,    "BattleInfo_61C", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-55500,  -81280,  -870,    0x1010000,    "BattleInfo_7AC", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(-37250,  -65390,  -690,    0x1010000,    "BattleInfo_554", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-20030,  -84440,  -700,    0x1010000,    "BattleInfo_6E4", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(-70270,  -36330,  0,       0x1010000,    "BattleInfo_874", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-28180,  -13440,  0,       0x1010000,    "BattleInfo_4B8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-77050,  -65440,  -2100,   0x1010000,    "BattleInfo_4B8", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-47100,  0,       -53310,  1200,    -47100,  1000,    -53310,  0x007C, 0,  3,  0x0000)
    DeclActor(-55000,  6350,    17270,   1200,    -55000,  7350,    17270,   0x007C, 0,  4,  0x0000)
    DeclActor(-36900,  -700,    -67700,  1200,    -36900,  300,     -67700,  0x007C, 0,  5,  0x0000)
    DeclActor(-66140,  -2100,   -72180,  1200,    -63990,  -3500,   -65970,  0x007C, 0,  9,  0x0000)
    DeclActor(-59460,  0,       -27710,  1200,    -59460,  0,       -27710,  0x007C, 0,  6,  0x0000)
    DeclActor(-2450,   -700,    -92010,  1500,    -2450,   1000,    -92010,  0x007C, 0,  10, 0x0000)

    PlaceName(27.450000762939453, 0.0, 1.25, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(26.0, 0.0, -92.0, 0x0000, 0x0000, "ウルスラ医科大学方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 11

    ScpFunction((
        "Function_0_9F8",          # 00, 0
        "Function_1_AB0",          # 01, 1
        "Function_2_D4F",          # 02, 2
        "Function_3_103A",         # 03, 3
        "Function_4_1187",         # 04, 4
        "Function_5_12D4",         # 05, 5
        "Function_6_1437",         # 06, 6
        "Function_7_144B",         # 07, 7
        "Function_8_147A",         # 08, 8
        "Function_9_1536",         # 09, 9
        "Function_10_160A",        # 0A, 10
    ))


    def Function_0_9F8(): pass

    label("Function_0_9F8")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_A38"),
        (1, "loc_A44"),
        (2, "loc_A50"),
        (3, "loc_A5C"),
        (4, "loc_A68"),
        (5, "loc_A74"),
        (6, "loc_A80"),
        (SWITCH_DEFAULT, "loc_A8C"),
    )


    label("loc_A38")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_A44")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_A50")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_A5C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_A68")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_A74")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_A80")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_A8C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_A98")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AAF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_A98")

    label("loc_AAF")

    Return()

    # Function_0_9F8 end

    def Function_1_AB0(): pass

    label("Function_1_AB0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_ACD")
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)

    label("loc_ACD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_D4B")
    ClearScenarioFlags(0x7A, 0)
    ClearScenarioFlags(0x7A, 1)
    ClearScenarioFlags(0x7A, 2)
    ClearScenarioFlags(0x7A, 3)
    ClearScenarioFlags(0x7A, 4)
    ClearScenarioFlags(0x7A, 5)
    ClearScenarioFlags(0x7A, 6)
    ClearScenarioFlags(0x7A, 7)
    ClearScenarioFlags(0x7B, 0)
    ClearScenarioFlags(0x7B, 1)
    ClearScenarioFlags(0x7B, 2)
    ClearScenarioFlags(0x7B, 3)
    ClearScenarioFlags(0x7B, 4)
    ClearScenarioFlags(0x7B, 5)
    ClearScenarioFlags(0x7B, 6)
    ClearScenarioFlags(0x7B, 7)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B2A")
    SetScenarioFlags(0x7A, 0)

    label("loc_B2A")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B40")
    SetScenarioFlags(0x7A, 1)

    label("loc_B40")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B56")
    SetScenarioFlags(0x7A, 2)

    label("loc_B56")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B6C")
    SetScenarioFlags(0x7A, 3)

    label("loc_B6C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B82")
    SetScenarioFlags(0x7A, 4)

    label("loc_B82")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B98")
    SetScenarioFlags(0x7A, 5)

    label("loc_B98")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BAE")
    SetScenarioFlags(0x7A, 6)

    label("loc_BAE")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BC4")
    SetScenarioFlags(0x7A, 7)

    label("loc_BC4")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BDA")
    SetScenarioFlags(0x7B, 0)

    label("loc_BDA")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BF0")
    SetScenarioFlags(0x7B, 1)

    label("loc_BF0")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C06")
    SetScenarioFlags(0x7B, 2)

    label("loc_C06")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C1C")
    SetScenarioFlags(0x7B, 3)

    label("loc_C1C")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C32")
    SetScenarioFlags(0x7B, 4)

    label("loc_C32")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C48")
    SetScenarioFlags(0x7B, 5)

    label("loc_C48")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C5E")
    SetScenarioFlags(0x7B, 6)

    label("loc_C5E")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C74")
    SetScenarioFlags(0x7B, 7)

    label("loc_C74")

    ClearScenarioFlags(0x7C, 0)
    ClearScenarioFlags(0x7C, 1)
    ClearScenarioFlags(0x7C, 2)
    ClearScenarioFlags(0x7C, 3)
    ClearScenarioFlags(0x7C, 4)
    ClearScenarioFlags(0x7C, 5)
    ClearScenarioFlags(0x7C, 6)
    ClearScenarioFlags(0x7C, 7)
    RunExpression(0x3, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CAF")
    SetScenarioFlags(0x7C, 0)
    Jump("loc_D4B")

    label("loc_CAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CC6")
    SetScenarioFlags(0x7C, 1)
    Jump("loc_D4B")

    label("loc_CC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDD")
    SetScenarioFlags(0x7C, 2)
    Jump("loc_D4B")

    label("loc_CDD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CF4")
    SetScenarioFlags(0x7C, 3)
    Jump("loc_D4B")

    label("loc_CF4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D0B")
    SetScenarioFlags(0x7C, 4)
    Jump("loc_D4B")

    label("loc_D0B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D22")
    SetScenarioFlags(0x7C, 5)
    Jump("loc_D4B")

    label("loc_D22")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D39")
    SetScenarioFlags(0x7C, 6)
    Jump("loc_D4B")

    label("loc_D39")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D4B")
    SetScenarioFlags(0x7C, 7)

    label("loc_D4B")

    Call(0, 7)
    Return()

    # Function_1_AB0 end

    def Function_2_D4F(): pass

    label("Function_2_D4F")

    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEE")
    OP_70(0x0, 0x0)
    Jump("loc_EF2")

    label("loc_EEE")

    OP_70(0x0, 0x1E)

    label("loc_EF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F05")
    OP_70(0x1, 0x0)
    Jump("loc_F09")

    label("loc_F05")

    OP_70(0x1, 0x1E)

    label("loc_F09")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1C")
    OP_70(0x2, 0x0)
    Jump("loc_F20")

    label("loc_F1C")

    OP_70(0x2, 0x1E)

    label("loc_F20")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 7)), scpexpr(EXPR_END)), "loc_F7D")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -59460, 0, -27710, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_F7D")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -63990, -3500, -65970, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1003")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xDE, 0xB7, 0xA7, 0xA, 0xC8, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "allback", 0x2, "red")

    label("loc_1003")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1017")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)
    Jump("loc_101D")

    label("loc_1017")

    OP_10(0x1, 0x1)
    OP_10(0x2, 0x0)

    label("loc_101D")

    SoundDistance(0x7B, 0xFFFF4174, 0xFFFFFACE, 0xFFFEFDA4, 0x1770, 0xC350, 0x64, 0x0)
    Return()

    # Function_2_D4F end

    def Function_3_103A(): pass

    label("Function_3_103A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1136")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x43, 1)"), scpexpr(EXPR_END)), "loc_10BF")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x43),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1131")

    label("loc_10BF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x43),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x43),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1131")

    Jump("loc_117B")

    label("loc_1136")

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

    label("loc_117B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_103A end

    def Function_4_1187(): pass

    label("Function_4_1187")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1283")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_120C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_127E")

    label("loc_120C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_127E")

    Jump("loc_12C8")

    label("loc_1283")

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

    label("loc_12C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1187 end

    def Function_5_12D4(): pass

    label("Function_5_12D4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1400")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 20)
    AddSepith(0x1, 20)
    AddSepith(0x2, 20)
    AddSepith(0x3, 20)
    AddSepith(0x4, 20)
    AddSepith(0x5, 20)
    AddSepith(0x6, 20)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×２０\x01\x07\x02",

            "#57I水のセピス×２０\x01\x07\x02",

            "#58I火のセピス×２０\x01\x07\x02",

            "#59I風のセピス×２０\x01\x07\x02",

            "#60I時のセピス×２０\x01\x07\x02",

            "#61I空のセピス×２０\x01\x07\x02",

            "#62I幻のセピス×２０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x116, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_1425")

    label("loc_1400")


    #A0008
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

    label("loc_1425")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12D4 end

    def Function_6_1437(): pass

    label("Function_6_1437")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 7)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_1437 end

    def Function_7_144B(): pass

    label("Function_7_144B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1463")
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)

    label("loc_1463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7C, 0)), scpexpr(EXPR_END)), "loc_1474")
    ClearScenarioFlags(0x7C, 0)
    Jump("loc_1479")

    label("loc_1474")

    SetChrFlags(0x13, 0x80)

    label("loc_1479")

    Return()

    # Function_7_144B end

    def Function_8_147A(): pass

    label("Function_8_147A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EB")

    #C0009
    ChrTalk(
        0xFE,
        "見晴らしがいい……\x02",
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "今日はここでお昼にしよう。\x02",
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        "そして周辺の森を探索するのだ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1532")

    label("loc_14EB")


    #C0012
    ChrTalk(
        0xFE,
        "お昼はここで食べよう。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "夜はウルスラ病院の\x01",
            "宿に泊まろうかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1532")

    TalkEnd(0xFE)
    Return()

    # Function_8_147A end

    def Function_9_1536(): pass

    label("Function_9_1536")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0014
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-65660, -1500, -69990, 1500)
    MoveCamera(45, 38, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(20500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0015
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1605")
    OP_E0(0x2)
    MiniGame(0x6, 0xD, 0xFFFEFC64, 0xFFFFF7CC, 0xFFFEE198, 0x0, 0xFFFF060A, 0xFFFFF254, 0xFFFEFE4E)

    label("loc_1605")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_9_1536 end

    def Function_10_160A(): pass

    label("Function_10_160A")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "東・聖ウルスラ医科大学\x01",
            "北・クロスベル市　１５３セルジュ\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_10_160A end

    SaveToFile()

Try(main)
