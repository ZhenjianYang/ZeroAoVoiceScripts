from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1520.bin",                # FileName
        "r1520",                    # MapName
        "r1520",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1520", "r0000_1", "", "", "", ""),   # include
        0x03,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 12500, 0, 0, 1, 96, 0, 2, 0, 3],
    )

    BuildStringList((
        "r1520",                  # 0
        "バス",                   # 1
        "運転手",                 # 2
        "エステル",               # 3
        "ヨシュア",               # 4
        "ボス１",                 # 5
        "ボス２",                 # 6
        "ボス３",                 # 7
        "br1500",                 # 8
        "br1500",                 # 9
        "br1500",                 # 10
        "br1500",                 # 11
        "br1500",                 # 12
        "br1500",                 # 13
        "br1500",                 # 14
        "br1500",                 # 15
        "クロスベル市方面",       # 16
        "ウルスラ医科大学方面",   # 17
        "星見の塔方面",           # 18
    ))

    ATBonus("ATBonus_530", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_557C", 8,   2,   0,   0,   3,   0,   5)
    Sepith("Sepith_559C", 2,   8,   0,   6,   2,   0,   0)
    Sepith("Sepith_556C", 8,   0,   5,   2,   0,   0,   4)
    Sepith("Sepith_5574", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_5564", 4,   2,   0,   8,   0,   3,   2)
    Sepith("Sepith_55EC", 9,   7,   18,  6,   7,   6,   3)

    MonsterBattlePostion("MonsterBattlePostion_590", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5F0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_5F4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_5F8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_5FC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_600", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_604", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_608", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_60C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_570", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_57C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_610", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_614", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_618", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_61C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_620", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_628", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_62C", 0, 0, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_888", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_557C", 30, 45, 20, 5,
        (
            ("ms65800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms65800.dat", "ms65800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms65800.dat", "ms63600.dat", "ms65800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms65800.dat", "ms65800.dat", "ms66600.dat", "ms65800.dat", 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_950", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_559C", 30, 45, 20, 5,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_6F8", 0x0000, 12, 6, 45, 10, 1, 45, 0, "br1500", "Sepith_556C", 30, 45, 20, 5,
        (
            ("ms66600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms66600.dat", "ms66600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms66600.dat", "ms62100.dat", "ms66600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms66600.dat", "ms66600.dat", "ms69700.dat", "ms66600.dat", 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_7C0", 0x0010, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_5574", 60, 25, 10, 5,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms63600.dat", "ms66600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "ms63600.dat", 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms63600.dat", "ms63600.dat", "ms62100.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_630", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_5564", 30, 45, 20, 5,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_AA0", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br1500", "Sepith_55EC", 40, 35, 25, 0,
        (
            ("ms70201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_A18", 0x0012, 12, 6, 45, 0, 1, 0, 0, "br1500", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68501.dat", "ms68501.dat", 0, 0, 0, 0, "ms66600.dat", 0, "MonsterBattlePostion_610", "MonsterBattlePostion_5F0", "ed7401", "ed7403", "ATBonus_530"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch28300.itc",                   # 00
        "chr/ch00600.itc",                   # 01
        "chr/ch00700.itc",                   # 02
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
        "monster/ch62150.itc",               # 10
        "monster/ch62151.itc",               # 11
        "monster/ch66650.itc",               # 12
        "monster/ch66651.itc",               # 13
        "monster/ch63650.itc",               # 14
        "monster/ch63650.itc",               # 15
        "monster/ch65850.itc",               # 16
        "monster/ch65851.itc",               # 17
        "monster/ch69750.itc",               # 18
        "monster/ch69750.itc",               # 19
        "chr/ch00000.itc",                   # 1A
        "chr/ch00000.itc",                   # 1B
        "monster/ch70250.itc",               # 1C
        "monster/ch70251.itc",               # 1D
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   1,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   2,   0,   0,   0,   0,   14,  255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(60,      -21740,  0,       0x1010000,    "BattleInfo_888", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(13280,   -29310,  0,       0x1010000,    "BattleInfo_950", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-14000,  -53580,  0,       0x1010000,    "BattleInfo_6F8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-17670,  -78600,  0,       0x1010000,    "BattleInfo_7C0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-41730,  -84600,  0,       0x1010000,    "BattleInfo_630", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-41630,  -87100,  0,       0x1010000,    "BattleInfo_630", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-56290,  -101340, 0,       0x1010000,    "BattleInfo_6F8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-44280,  -104010, 0,       0x1010000,    "BattleInfo_888", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-2950,   -34030,  0,       0x1010000,    "BattleInfo_AA0", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-42660,  -94360,  10,      0x1010000,    "BattleInfo_AA0", 0,   28,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 17,  -28.0,                 -82.0,                 -1.0,                  625.0,                 [0.07071065902709961,  0.14142140746116638,   -0.0,                  0.0,                   -0.07071070373058319,  0.14142131805419922,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -3.8183791637420654,   15.556347846984863,    0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 27,  -2.5,                  9.0,                   -1.0,                  506.25,                [0.06666667014360428,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   0.1666666716337204,    -3.0,                  0.20000000298023224,   1.0])
    DeclEvent(0x0000, 0, 28,  0.0,                   -1.5,                  -1.0,                  506.25,                [0.04714055731892586,  -0.23570173978805542,  0.0,                   0.0,                   0.047140348702669144,  0.23570279777050018,   -0.0,                  0.0,                   -0.0,                  -0.0,                  0.20000000298023224,   0.0,                   0.07071052491664886,   0.3535541892051697,    0.20000000298023224,   1.0])

    DeclActor(-14600,  -1400,   -10500,  1200,    -14600,  -400,    -10500,  0x007C, 0,  4,  0x0000)
    DeclActor(-33050,  0,       -69250,  1200,    -33050,  1000,    -69250,  0x007C, 0,  5,  0x0000)
    DeclActor(4920,    0,       -11820,  1200,    4920,    0,       -11820,  0x007C, 0,  6,  0x0000)
    DeclActor(-1270,   0,       -59940,  1200,    -1270,   0,       -59940,  0x007C, 0,  7,  0x0000)
    DeclActor(-57680,  0,       -116430, 1200,    -57680,  0,       -116430, 0x007C, 0,  8,  0x0000)

    PlaceName(2.0, 0.4300000071525574, 40.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(-59.900001525878906, 0.0, -142.27999877929688, 0x0000, 0x0000, "ウルスラ医科大学方面")
    PlaceName(-51.7400016784668, -1.399999976158142, -3.7799999713897705, 0x0000, 0x0000, "星見の塔方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5, 6, 7])              # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11

    ScpFunction((
        "Function_0_C44",          # 00, 0
        "Function_1_CFC",          # 01, 1
        "Function_2_D1B",          # 02, 2
        "Function_3_DA4",          # 03, 3
        "Function_4_116E",         # 04, 4
        "Function_5_12BB",         # 05, 5
        "Function_6_1408",         # 06, 6
        "Function_7_141C",         # 07, 7
        "Function_8_1430",         # 08, 8
        "Function_9_1444",         # 09, 9
        "Function_10_145D",        # 0A, 10
        "Function_11_1486",        # 0B, 11
        "Function_12_15F0",        # 0C, 12
        "Function_13_16F3",        # 0D, 13
        "Function_14_182C",        # 0E, 14
        "Function_15_1917",        # 0F, 15
        "Function_16_1CFE",        # 10, 16
        "Function_17_1D63",        # 11, 17
        "Function_18_237C",        # 12, 18
        "Function_19_352C",        # 13, 19
        "Function_20_4984",        # 14, 20
        "Function_21_49A9",        # 15, 21
        "Function_22_4AA8",        # 16, 22
        "Function_23_4AC3",        # 17, 23
        "Function_24_4B2C",        # 18, 24
        "Function_25_4B50",        # 19, 25
        "Function_26_4BC4",        # 1A, 26
        "Function_27_5017",        # 1B, 27
        "Function_28_542A",        # 1C, 28
        "Function_29_5438",        # 1D, 29
    ))


    def Function_0_C44(): pass

    label("Function_0_C44")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_C84"),
        (1, "loc_C90"),
        (2, "loc_C9C"),
        (3, "loc_CA8"),
        (4, "loc_CB4"),
        (5, "loc_CC0"),
        (6, "loc_CCC"),
        (SWITCH_DEFAULT, "loc_CD8"),
    )


    label("loc_C84")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_C90")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_C9C")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_CA8")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_CB4")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_CC0")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_CCC")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_CD8")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_CE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CFB")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_CE4")

    label("loc_CFB")

    Return()

    # Function_0_C44 end

    def Function_1_CFC(): pass

    label("Function_1_CFC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D1A")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_1_CFC")

    label("loc_D1A")

    Return()

    # Function_1_CFC end

    def Function_2_D1B(): pass

    label("Function_2_D1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_D2A")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 18)

    label("loc_D2A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D96")
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, -51450, 0, -96010, 315)
    SetChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrPos(0xB, -52810, 0, -95050, 45)
    SetChrFlags(0xB, 0x10)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, -53470, 0, -94190, 45)
    Call(0, 10)

    label("loc_D96")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 9)
    Return()

    # Function_2_D1B end

    def Function_3_DA4(): pass

    label("Function_3_DA4")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC6")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_DC6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x84, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DDE")
    ModifyEventFlags(1, 1, 0x80)
    ModifyEventFlags(1, 2, 0x80)

    label("loc_DDE")

    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F7D")
    OP_70(0x1, 0x0)
    Jump("loc_F81")

    label("loc_F7D")

    OP_70(0x1, 0x1E)

    label("loc_F81")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F94")
    OP_70(0x2, 0x0)
    Jump("loc_F98")

    label("loc_F94")

    OP_70(0x2, 0x1E)

    label("loc_F98")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 1)), scpexpr(EXPR_END)), "loc_1002")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 4920, 0, -11820, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)
    Jump("loc_10B9")

    label("loc_1002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 2)), scpexpr(EXPR_END)), "loc_1060")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -1270, 0, -59940, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_10B9")

    label("loc_1060")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 3)), scpexpr(EXPR_END)), "loc_10B9")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -57680, 0, -116430, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_10B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1104")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF1, 0xC2, 0xB1, 0x0, 0x1AE, 0x0)
    SetMapObjFrame(0xFF, "sky", 0x2, "red")
    SetMapObjFrame(0xFF, "water00", 0x2, "red")
    SetMapObjFrame(0xFF, "water01", 0x2, "red")

    label("loc_1104")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1115")
    Call(0, 16)

    label("loc_1115")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1128")
    OP_1B(0x2, 0x0, 0x1D)

    label("loc_1128")

    SoundDistance(0x7D, 0xFFFFAD4E, 0x0, 0xFFFDDD7A, 0x15F90, 0x11170, 0x64, 0x0)
    OP_E1(0xB50E, 0x0, 0xFFFEEE0E)
    OP_E1(0xBA86, 0x0, 0xD0D4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_116D")
    OP_16(0x3, 0x2, 0x1, 0x0)

    label("loc_116D")

    Return()

    # Function_3_DA4 end

    def Function_4_116E(): pass

    label("Function_4_116E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_126A")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_11F3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1265")

    label("loc_11F3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1265")

    Jump("loc_12AF")

    label("loc_126A")

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

    label("loc_12AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_116E end

    def Function_5_12BB(): pass

    label("Function_5_12BB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B7")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_1340")
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
    SetScenarioFlags(0x116, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_13B2")

    label("loc_1340")

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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13B2")

    Jump("loc_13FC")

    label("loc_13B7")

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

    label("loc_13FC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12BB end

    def Function_6_1408(): pass

    label("Function_6_1408")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_1408 end

    def Function_7_141C(): pass

    label("Function_7_141C")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_141C end

    def Function_8_1430(): pass

    label("Function_8_1430")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 3)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1430 end

    def Function_9_1444(): pass

    label("Function_9_1444")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_145C")
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)

    label("loc_145C")

    Return()

    # Function_9_1444 end

    def Function_10_145D(): pass

    label("Function_10_145D")

    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    Return()

    # Function_10_145D end

    def Function_11_1486(): pass

    label("Function_11_1486")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15B4")

    #C0007
    ChrTalk(
        0xFE,
        (
            "やあ警察の人たち、\x01",
            "さっきはありがとうな。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "遊撃士さんたちも\x01",
            "確かに凄かったけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "君たちが来てくれなかったら\x01",
            "やっぱり危なかったと思うんだ。\x01",
            "礼を言わせて貰うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "そうだ……良かったら\x01",
            "バスの中で休んでいくかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "空いてる座席なら\x01",
            "好きに使っちゃってくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    SetScenarioFlags(0x70, 7)
    Jump("loc_15EC")

    label("loc_15B4")


    #C0012
    ChrTalk(
        0xFE,
        (
            "どうだい、良かったら\x01",
            "バスの中で休んでいくかい？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)

    label("loc_15EC")

    TalkEnd(0xFE)
    Return()

    # Function_11_1486 end

    def Function_12_15F0(): pass

    label("Function_12_15F0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "バスの中で休んでいく\x01",      # 0
            "やめておく\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167B")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    Jump("loc_16F2")

    label("loc_167B")

    FadeToBright(300, 0)

    #C0013
    ChrTalk(
        0x9,
        (
            "そうかい、休みたくなったら\x01",
            "いつでも言ってくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "このザマじゃ、どうせ\x01",
            "しばらくは動けないだろうしさ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_16F2")

    Return()

    # Function_12_15F0 end

    def Function_13_16F3(): pass

    label("Function_13_16F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1709")
    Call(0, 26)
    Jump("loc_182B")

    label("loc_1709")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_171E")
    Call(0, 15)
    Jump("loc_1828")

    label("loc_171E")


    #C0015
    ChrTalk(
        0xA,
        (
            "#0800Fあ、ロイド君たち。\x02\x03",

            "大丈夫、こっちは任せといて。\x02\x03",

            "#0804F魔獣の見張りと\x01",
            "乗客の人たちへの説明、\x01",
            "あとは市庁舎に報告ってとこよね。\x02\x03",

            "#0800Fばっちりやっておくから、\x01",
            "ロイド君たちは仕事の方に\x01",
            "全力を注いでくれると嬉しいかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0000Fすまない、よろしく頼むよ。\x02",
    )

    CloseMessageWindow()

    label("loc_1828")

    TalkEnd(0xA)

    label("loc_182B")

    Return()

    # Function_13_16F3 end

    def Function_14_182C(): pass

    label("Function_14_182C")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1841")
    Call(0, 15)
    Jump("loc_1913")

    label("loc_1841")


    #C0017
    ChrTalk(
        0xB,
        (
            "#0904F特務支援課のことは\x01",
            "聞いていたけど……こんなに早く\x01",
            "会えるとは思わなかったな。\x02\x03",

            "#0900Fエンジンの修理には\x01",
            "少し時間が掛かりそうだ。\x01",
            "君たちは気にせず先に進んでくれ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        "#0300Fスマン、こっちは任せたぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_1913")

    TalkEnd(0xB)
    Return()

    # Function_14_182C end

    def Function_15_1917(): pass

    label("Function_15_1917")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0019
    ChrTalk(
        0xA,
        (
            "#0804F#11Pしっかし、導力車といい\x01",
            "何とかネットワークってのといい、\x01",
            "クロスベルは進んでるわねぇ。\x02\x03",

            "#0800Fてっきりあたし、リベールが一番\x01",
            "導力技術が進んでると思ってたけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0020
    ChrTalk(
        0xB,
        (
            "#0904F#5Pまあリベールも技術先進国だけど\x01",
            "伝統を大事にする傾向があるからね。\x02\x03",

            "#0900Fそれに導力ネットワークに関しては\x01",
            "エプスタイン財団の肝煎りみたいだ。\x02\x03",

            "その意味では……\x01",
            "今、一番導力化が進んでいる場所は\x01",
            "このクロスベルかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "#0805F#11Pなるほど……\x02\x03",

            "#0809Fティータとか連れて来たら\x01",
            "飛び上がって喜んじゃいそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "#0909F#5Pはは……そうだね。\x02\x03",

            "#0902Fエステル……寂しい？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xA,
        (
            "#0802F#11Pあ、あはは……\x02\x03",

            "#0804Fあんな形だったけど\x01",
            "ちゃんと再会できたしね。\x02\x03",

            "#0808Fあれから３ヶ月か……\x01",
            "みんな元気にしてるのかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "#0904F#5P大丈夫……\x01",
            "きっとみんな元気でいるさ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C49")

    #C0025
    ChrTalk(
        0x101,
        "#0005F（誰の話だろう……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE1")

    label("loc_1C49")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7E")

    #C0026
    ChrTalk(
        0x102,
        "#0105F（誰の話かしら……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE1")

    label("loc_1C7E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB1")

    #C0027
    ChrTalk(
        0x103,
        "#0200F（……誰の話……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1CE1")

    label("loc_1CB1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CE1")

    #C0028
    ChrTalk(
        0x104,
        "#0300F（誰の話かねぇ……？）\x02",
    )

    CloseMessageWindow()

    label("loc_1CE1")

    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x2D, 0x0)
    Return()

    # Function_15_1917 end

    def Function_16_1CFE(): pass

    label("Function_16_1CFE")

    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x0, 0x2)
    SetMapObjFlags(0x0, 0x400)
    SetChrFlags(0x8, 0x8000)
    OP_78(0x0, 0x8)
    SetMapObjFlags(0x0, 0x1000)
    SetMapObjFrame(0x0, "light", 0x0, 0x1)
    SetChrPos(0x8, -49600, 0, -91600, 230)
    OP_D3(0x8, 0x0, 0x38270, 0x0, 0x0)
    OP_74(0x0, 0x1E)
    OP_70(0x0, 0x14A)
    Return()

    # Function_16_1CFE end

    def Function_17_1D63(): pass

    label("Function_17_1D63")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    AddParty(0x9D, 0xFF, 0xFF)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("monster/ch68550.itc", 0x26)
    LoadChrToIndex("monster/ch68551.itc", 0x27)
    SetChrFlags(0x19E, 0x80)
    SetChrBattleFlags(0x19E, 0x8000)
    OP_68(-30410, 600, -82830, 0)
    MoveCamera(15, 18, 0, 0)
    OP_6E(410, 0)
    SetCameraDistance(25080, 0)
    SetChrPos(0x101, -32800, 0, -85500, 225)
    SetChrPos(0x102, -31800, 0, -86500, 225)
    SetChrPos(0x103, -30800, 0, -85500, 225)
    SetChrPos(0x104, -31800, 0, -84500, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -48090, 300, -93440, 135)
    BeginChrThread(0x9, 3, 0, 20)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrPos(0xC, -44270, 0, -94740, 315)
    SetChrPos(0xD, -47430, 0, -98660, 0)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 1)
    BeginChrThread(0xD, 3, 0, 1)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 16)
    OP_70(0x0, 0x1E)
    SetMapObjFlags(0x2, 0x4)
    StopBGM(0x7D0)
    FadeToBright(1000, 0)
    OP_68(-32830, 600, -84230, 1500)
    OP_6F(0x1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0029
    ChrTalk(
        0x101,
        "#0013F#11Pあれは……！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0307F#11Pチッ……\x01",
            "やっぱり予想通りか！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1FF7():
        OP_A6(0xFE, 0x0, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1FF7)
    OP_68(-45100, 600, -91970, 0)
    MoveCamera(340, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21660, 0)
    OP_68(-48150, 600, -93080, 1500)
    OP_6F(0x1)
    OP_0D()
    Sound(835, 0, 100, 0)
    Sleep(1000)

    #C0031
    ChrTalk(
        0x9,
        (
            "#5Pひっ、ひいっ！\x01",
            "何でこんな時に魔獣が……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "#5Pああ、女神#4Rエイドス#よ！\x01",
            "どうかお守りください～！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0007F#1P大丈夫ですか……！\x02",
    )

    CloseMessageWindow()
    OP_64(0x9)
    EndChrThread(0x9, 0x1)
    EndChrThread(0x9, 0x3)
    OP_93(0x9, 0x5A, 0x1F4)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Fade(1000)
    OP_68(-44300, 1100, -93460, 0)
    MoveCamera(359, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23150, 0)
    SetCameraDistance(19150, 1500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -34490, 0, -89160, 225)
    SetChrPos(0x102, -33270, 0, -86290, 225)
    SetChrPos(0x103, -33260, 0, -89550, 225)
    SetChrPos(0x104, -31970, 0, -87360, 225)

    def lambda_21C7():
        OP_95(0xFE, -41650, 0, -93000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_21C7)

    def lambda_21E1():
        OP_95(0xFE, -40590, 0, -90960, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_21E1)

    def lambda_21FB():
        OP_95(0xFE, -40140, 0, -93680, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21FB)

    def lambda_2215():
        OP_95(0xFE, -39140, 0, -91570, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2215)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    def lambda_2241():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2241)

    def lambda_224E():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_224E)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)

    #C0034
    ChrTalk(
        0x9,
        "#5Pあ、あんたらは……！？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#0013F#11P警察の者です！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#0307F#2P撃退すっから\x01",
            "中に入っててくれや！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)
    OP_68(-43010, 1100, -92990, 1500)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_22EB():
        OP_95(0xFE, -48840, 500, -92450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_22EB)
    Sleep(300)

    def lambda_2308():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_2308)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_71(0x0, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x0)
    OP_6F(0x1)
    Battle("BattleInfo_A18", 0x30200011, 0x0, 0x0, 0xC, 0xFF)
    FadeToDark(0, 0, -1)
    RemoveParty(0x9D, 0xFF)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 18)
    Return()

    # Function_17_1D63 end

    def Function_18_237C(): pass

    label("Function_18_237C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("monster/ch68550.itc", 0x26)
    LoadChrToIndex("monster/ch68551.itc", 0x27)
    LoadChrToIndex("chr/ch00651.itc", 0x29)
    LoadChrToIndex("chr/ch00652.itc", 0x2A)
    LoadChrToIndex("chr/ch00751.itc", 0x2B)
    LoadChrToIndex("chr/ch00650.itc", 0x2C)
    LoadChrToIndex("chr/ch00750.itc", 0x2D)
    LoadEffect(0x0, "battle\\cr006201.eff")
    OP_68(-47720, 200, -93920, 0)
    MoveCamera(335, 19, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22500, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -45410, 0, -97050, 135)
    SetChrPos(0x102, -46960, 0, -96830, 135)
    SetChrPos(0x103, -48540, 0, -96760, 180)
    SetChrPos(0x104, -45330, 0, -94950, 90)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -48840, 500, -92450, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xC, -58010, 0, -97980, 45)
    SetChrPos(0xD, -55680, 0, -100660, 45)
    SetChrPos(0xE, -55780, 0, -104760, 45)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 1)
    BeginChrThread(0xD, 3, 0, 1)
    BeginChrThread(0xE, 3, 0, 1)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    Call(0, 16)
    OP_70(0x0, 0x0)
    SetMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -41590, 0, -97730, 225)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -43200, 0, -98240, 225)
    SetChrFlags(0xB, 0x8000)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(21400, 1500)
    OP_6F(0x10)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(100)
    OP_93(0x101, 0x10E, 0x12C)
    Sleep(300)

    #C0037
    ChrTalk(
        0x101,
        (
            "#0006F#12Pふう……\x01",
            "かなり手強かったな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2697():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2697)

    def lambda_26A4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26A4)
    Sleep(100)

    def lambda_26B4():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26B4)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0038
    ChrTalk(
        0x102,
        (
            "#0106F#5Pそうね……\x02\x03",

            "#0101Fずいぶん大きかったけれど\x01",
            "どこから現れたのかしら。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        (
            "#0206F#5P……どうやら森林地帯に\x01",
            "棲息する種のようですが……\x02\x03",

            "#0200F何かのきっかけで\x01",
            "街道に出てしまったのでしょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#0305F#11Pふぅん……？\x01",
            "珍しいこともあるもんだな。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-48290, 200, -93170, 3000)
    MoveCamera(320, 19, 0, 3000)
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x0)

    def lambda_2801():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2801)

    def lambda_280E():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_280E)

    def lambda_281B():
        TurnDirection(0xFE, 0x9, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_281B)

    def lambda_2828():
        TurnDirection(0xFE, 0x9, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2828)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_2845():
        OP_95(0xFE, -48090, 300, -93440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2845)

    def lambda_285F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_285F)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    #C0041
    ChrTalk(
        0x9,
        "#5Pあんたら、よくやってくれた！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "#5Pいや～、助かったよ！\x01",
            "一時はどうなることかと……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0004F#6Pいえ、無事でよかったです。\x02\x03",

            "#0000F今の魔獣のせいで\x01",
            "足止めをくらってたんですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        "#5Pああ、そうだけど……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#5Pその前に、導力エンジンが\x01",
            "故障を起こしちまったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "#5P仕方ないから一旦停車して\x01",
            "調べてみようとしたんだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0300F#12Pそこに今の魔獣が現れて\x01",
            "立ち往生する羽目になったのか。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        (
            "#0200F#6P通信器の調子が悪かったのも\x01",
            "エンジントラブルが原因ですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#5Pああ、バスに搭載してる通信器は\x01",
            "エンジンから導力を取ってるからな。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "#5Pおっと、こうしちゃいられない。\x01",
            "何とか直せないか確かめないと……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-49330, 200, -94050, 3000)

    def lambda_2AFC():

        label("loc_2AFC")

        TurnDirection(0x101, 0x9, 500)
        Yield()
        Jump("loc_2AFC")

    QueueWorkItem2(0x101, 1, lambda_2AFC)

    def lambda_2B0E():

        label("loc_2B0E")

        TurnDirection(0x102, 0x9, 500)
        Yield()
        Jump("loc_2B0E")

    QueueWorkItem2(0x102, 1, lambda_2B0E)

    def lambda_2B20():

        label("loc_2B20")

        TurnDirection(0x103, 0x9, 500)
        Yield()
        Jump("loc_2B20")

    QueueWorkItem2(0x103, 1, lambda_2B20)

    def lambda_2B32():

        label("loc_2B32")

        TurnDirection(0x104, 0x9, 500)
        Yield()
        Jump("loc_2B32")

    QueueWorkItem2(0x104, 1, lambda_2B32)
    BeginChrThread(0x9, 3, 0, 21)
    Sleep(10000)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    OP_6F(0x1)
    Sleep(2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x104)
    OP_64(0x103)

    def lambda_2BB9():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BB9)
    Sleep(50)

    def lambda_2BC9():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BC9)

    def lambda_2BD6():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BD6)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0051
    ChrTalk(
        0x102,
        (
            "#0103F#5P……この様子だと\x01",
            "復旧にはまだかかりそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0001F#12Pうーん、いったん街に戻って\x01",
            "交通課の人に報告した方がいいか。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#0206F#5Pはぁ……これも運命ですか。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#0306F#11Pま、面倒だけど、\x01",
            "そうするしかねぇかもな──\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_93(0x104, 0xE1, 0x1F4)

    #C0055
    ChrTalk(
        0x104,
        "#0307F#11P……おい！\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    EndChrThread(0x9, 0x3)

    def lambda_2D68():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D68)

    def lambda_2D75():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2D75)
    Sleep(100)

    def lambda_2D85():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2D85)

    def lambda_2D92():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2D92)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x9, 1)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(500)
    OP_68(-50900, 1600, -98850, 0)
    MoveCamera(7, 15, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22200, 0)
    OP_68(-51930, 1600, -99720, 1500)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_6F(0x79)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0056
    ChrTalk(
        0x9,
        "#5Pひ、ひいいいっ！？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0005F#2Pなっ……！？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#0201F#11Pそんな……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        "#0107F#2Pまだいたの……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0303F#11Pさすがにマズイな……\x02\x03",

            "#0307Fおい、ロイド！\x01",
            "各個撃破に持ってくぞ！\x02\x03",

            "さすがに全部は\x01",
            "相手にしてらんねぇ！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#0007F#11Pいや……駄目だ！\x02\x03",

            "それだとバスが\x01",
            "襲われる可能性がある！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#0310F#11Pちっ、それもそうか……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#0101F#2Pとにかく\x01",
            "すぐに対処しないと……！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20000, 1500)
    EndChrThread(0xC, 0x3)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(835, 0, 100, 0)
    BeginChrThread(0xC, 3, 0, 22)

    def lambda_306D():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_306D)
    Sleep(300)
    EndChrThread(0xD, 0x3)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 3, 0, 22)

    def lambda_30A7():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_30A7)
    Sleep(200)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 3, 0, 22)

    def lambda_30E1():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_30E1)
    WaitChrThread(0xC, 1)
    EndChrThread(0xC, 0x3)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 1)
    WaitChrThread(0xD, 1)
    EndChrThread(0xD, 0x3)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 3, 0, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 3, 0, 1)
    OP_6F(0x79)

    #C0064
    ChrTalk(
        0x103,
        "#0207F#2P……来ます……！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0010F#2P（………くっ…………！？）\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Sound(1701, 255, 100, 0)    #voice#Estelle
    StopBGM(0x4B0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7402", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x192), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetCameraDistance(22500, 1250)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    BeginChrThread(0xA, 3, 0, 23)
    BeginChrThread(0xB, 3, 0, 24)

    def lambda_31F5():
        OP_95(0xFE, -50690, 0, -99150, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_31F5)
    Sleep(750)
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_82(0x96, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x0, 0xFF, 0xA, 0x140, 0, -300, 1250, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    Sound(834, 0, 100, 0)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xC, 0x27)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 22)
    BeginChrThread(0xD, 3, 0, 22)
    BeginChrThread(0xE, 3, 0, 22)

    def lambda_32C9():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_32C9)

    def lambda_32E3():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_32E3)

    def lambda_32FD():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_32FD)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x26)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x26)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xC, 3, 0, 1)
    BeginChrThread(0xD, 3, 0, 1)
    BeginChrThread(0xE, 3, 0, 1)
    WaitChrThread(0xB, 1)
    EndChrThread(0xB, 0x3)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    TurnDirection(0xB, 0xD, 500)
    WaitChrThread(0xA, 3)
    OP_6F(0x10)
    CancelBlur(0)
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

    #C0066
    ChrTalk(
        0x101,
        "#0005F#2Pえ……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#0305F#2Pな……\x02",
    )

    CloseMessageWindow()

    #N0068
    NpcTalk(
        0xA,
        "ツインテールの娘",
        "#0807F#5Pヨシュア！\x02",
    )

    CloseMessageWindow()

    #N0069
    NpcTalk(
        0xB,
        "黒髪の青年",
        "#0903F#11P──ああ！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(19000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)
    Battle(0xFFFFFFFF, 0x30200003, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30068501, 0x30068501, 0x30068501, 0x0, 0x0, 0x0, 0x0, 0x0, 0x192, 0x8)
    FadeToDark(0, 0, -1)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    Call(0, 19)
    Return()

    # Function_18_237C end

    def Function_19_352C(): pass

    label("Function_19_352C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("monster/ch68553.itc", 0x28)
    LoadChrToIndex("chr/ch00650.itc", 0x2C)
    LoadChrToIndex("chr/ch00750.itc", 0x2D)
    LoadEffect(0x0, "battle\\ms00001.eff")
    OP_68(-53870, 800, -99910, 0)
    MoveCamera(6, 14, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(24120, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrPos(0x101, -48420, 0, -95970, 225)
    SetChrPos(0x102, -47190, 0, -95080, 225)
    SetChrPos(0x103, -45450, 0, -95570, 225)
    SetChrPos(0x104, -46730, 0, -96390, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_4B(0x9, 0xFF)
    SetChrPos(0x9, -53630, 0, -94960, 180)
    Call(0, 16)
    SetMapObjFlags(0x2, 0x4)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -51980, 0, -98210, 225)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xA, 0x2C)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_4B(0xB, 0xFF)
    SetChrPos(0xB, -50720, 0, -98630, 225)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x2D)
    SetChrSubChip(0xB, 0x0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00800.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu00900.itp")
    EndChrThread(0xC, 0x3)
    EndChrThread(0xD, 0x3)
    EndChrThread(0xE, 0x3)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    ClearChrFlags(0xD, 0x80)
    ClearChrBattleFlags(0xD, 0x8000)
    ClearChrFlags(0xE, 0x80)
    ClearChrBattleFlags(0xE, 0x8000)
    SetChrChipByIndex(0xC, 0x28)
    SetChrSubChip(0xC, 0x0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrChipByIndex(0xE, 0x28)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x8000)
    SetChrPos(0xC, -58010, 0, -97980, 45)
    SetChrPos(0xD, -55680, 0, -100660, 45)
    SetChrPos(0xE, -55780, 0, -104760, 45)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xC, 0x0)
    EndChrThread(0xD, 0x0)
    EndChrThread(0xE, 0x0)
    FadeToBright(1000, 0)
    SetCameraDistance(22620, 1500)
    OP_6F(0x79)
    OP_0D()
    OP_82(0x0, 0x96, 0x1770, 0x3E8)
    BeginChrThread(0xC, 3, 0, 25)
    Sound(502, 0, 100, 0)
    Sleep(300)
    BeginChrThread(0xD, 3, 0, 25)
    Sound(502, 0, 100, 0)
    Sleep(200)
    BeginChrThread(0xE, 3, 0, 25)
    Sound(502, 0, 100, 0)
    Sound(816, 0, 100, 0)
    WaitChrThread(0xC, 3)
    WaitChrThread(0xD, 3)
    WaitChrThread(0xE, 3)
    Sleep(500)
    OP_68(-51040, 800, -95930, 2500)
    OP_6F(0x79)
    StopBGM(0x1770)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(100)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0070
    ChrTalk(
        0x101,
        "#0005F#11P……あ………\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        "#0105F#11Pす、凄い……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        "#0205F#11P……とんでもないです。\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0xA, 0x1)
    SetChrSubChip(0xA, 0x0)
    SetChrChipByIndex(0xB, 0x2)
    SetChrSubChip(0xB, 0x0)
    Sound(808, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    Sleep(500)

    #N0073
    NpcTalk(
        0xB,
        "黒髪の青年",
        (
            "#0903F#11P……ふう。\x01",
            "何とか間に合ったかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    Sleep(300)

    #N0074
    NpcTalk(
        0xB,
        "黒髪の青年",
        "#0900F#11Pエステル、大丈夫かい？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)
    Sleep(300)

    #N0075
    NpcTalk(
        0xA,
        "ツインテールの娘",
        (
            "#0804F#5Pうん、あたしは別に。\x02\x03",

            "#0800F何とかヨシュアの切り込みの\x01",
            "タイミングを作れてよかったわ。\x02\x03",

            "#0805Fそれはそうと……\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7519", 0)
    OP_68(-49690, 800, -95970, 2000)

    def lambda_3A37():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3A37)
    TurnDirection(0xB, 0x101, 500)
    OP_93(0x9, 0x87, 0x1F4)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    #N0076
    NpcTalk(
        0xA,
        "ツインテールの娘",
        (
            "#0800F#6Pえっと、もしかして\x01",
            "クロスベル警察の人かしら？\x02\x03",

            "南口のところで、交通課の人から\x01",
            "話を聞いたんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#0011F#11Pあ、ああ……\x02\x03",

            "#0001Fその、君たちは……\x02",
        )
    )

    CloseMessageWindow()

    #N0078
    NpcTalk(
        0xA,
        "ツインテールの娘",
        (
            "#0809F#6Pあ、いきなり現れて\x01",
            "混乱させちゃったみたいね。\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(300)
    #Sound(1702, 255, 100, 0)    #voice#Estelle
    SetChrName("ツインテールの娘")

    #A0079
    AnonymousTalk(
        0xFF,
        (
            "初めまして！\x02\x03",

            "あたしはエステル。\x01",
            "エステル・ブライトよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    Sleep(500)
    #Sound(1770, 255, 100, 0)    #voice#Joshua
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    SetChrName("黒髪の青年")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            "僕はヨシュアと言います。\x02\x03",

            "遊撃士協会・クロスベル支部に\x01",
            "正式配属になったばかりです。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x1, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x1, 0x3)
    OP_CA(0x0, 0x1, 0x0)

    #C0081
    ChrTalk(
        0x101,
        "#0006F#11P（やっぱり遊撃士か……）\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-49950, 800, -96090, 800)
    OP_9B(0x0, 0x101, 0x0, 0x3E8, 0x3E8, 0x0)
    Sleep(300)

    #C0082
    ChrTalk(
        0x101,
        (
            "#0003F#11P自分たちはクロスベル警察、\x01",
            "特務支援課に所属する者です。\x02\x03",

            "#0000F危ないところをありがとう。\x01",
            "本当に助かったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#0809F#6Pあはは、いいって。\x02\x03",

            "#0800Fあなたたちも結構やりそうだし、\x01",
            "余計なお世話かなって\x01",
            "ちょっと思ったんだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#0006F#11Pいや……\x01",
            "正直、危ない所だったよ。\x02\x03",

            "#0000F──俺はロイド。\x01",
            "ロイド・バニングスだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#0100F#11P初めまして。\x01",
            "エリィ・マクダエルです。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#0302F#11Pうっす。\x01",
            "ランディ・オルランドだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#0203F#11Pティオ・プラトーです。\x01",
            "……よろしく。（ペコリ）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "#0800F#6Pロイドさんに、エリィさんに、\x01",
            "ランディさんに、ティオちゃん……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0089
    ChrTalk(
        0xA,
        "#0805F#6Pあれ、ティオにロイドって……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        (
            "#0909F#6Pはは……\x01",
            "ちょっと面白い偶然だね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)

    #C0091
    ChrTalk(
        0x101,
        "#0005F#11Pえっと……？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#0205F#11P……わたしたちの名前が何か？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#0809F#6Pあはは、ゴメンゴメン。\x02\x03",

            "#0802Fちょうど知り合いに\x01",
            "ティオとロイドさんがいたから\x01",
            "面白い偶然だなぁって思って。\x02\x03",

            "もちろん全然似てないけどね。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#0000F#11Pは、はあ……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x9, 500)

    #C0095
    ChrTalk(
        0xB,
        (
            "#0901F#12Pそういえば……\x01",
            "導力バスの方はどうですか？\x02\x03",

            "どうやらエンジントラブルを\x01",
            "起こしているみたいですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x9, 500)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x9,
        "#5Pあ、ああ……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "#5P結晶回路#8Rク オ ー ツ#の接続不良が\x01",
            "原因なのは確かみたいだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "#5P困ったな、こんな事なら\x01",
            "もう少しちゃんと\x01",
            "整備研修を受けとくんだったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xB,
        (
            "#0903F#12Pその、よかったら\x01",
            "少し見せてもらえますか？\x02\x03",

            "#0900Fひょっとしたら何とか\x01",
            "修理できるかもしれません。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x9,
        "#5Pお、本当か！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0101
    ChrTalk(
        0xA,
        (
            "#0802F#5Pそういえばヨシュア、\x01",
            "飛行船の操縦とか出来るもんね。\x02\x03",

            "簡単な整備ならお手のものか。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "#5Pいや～、さすが遊撃士！\x01",
            "いざっていう時は頼りになるなぁ！\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        "#0904F#12Pいえ、たまたまですから。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)

    #C0104
    ChrTalk(
        0x104,
        (
            "#0301F#11P（なあティオすけ……\x01",
            "  お前、エンジン修理とかは？）\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        (
            "#0206F#11P（いえ……門外漢です。）\x02\x03",

            "（導力ネットの関連機器なら\x01",
            "  そこそこ分かりますけど……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 500)

    def lambda_44F7():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_44F7)
    Sleep(300)

    #C0106
    ChrTalk(
        0xA,
        (
            "#0805F#6Pそういえば……\x01",
            "あなた達はどうしてここに？\x02\x03",

            "#0800Fあたしたちみたいに\x01",
            "手配魔獣を捜しに来たとか？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#0011F#11Pい、いや……\x01",
            "そういうわけじゃないけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#0103F#11P警察の任務で、この先にある\x01",
            "病院に向かう所だったんです。\x02\x03",

            "#0100Fそこで丁度、\x01",
            "この騒ぎに出くわしてしまって。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "#0900F#6Pこの先の病院……\x01",
            "《聖ウルスラ医科大学》でしたか。\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "#0805F#6Pへ～、そんな場所があるんだ。\x02\x03",

            "#0800Fあ、それじゃあこの場は\x01",
            "あたしたちが引き受けるわよ。\x02\x03",

            "用事があるんだったら\x01",
            "先に行った方がいいんじゃない？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#0105F#11Pそ、それは……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0112
    ChrTalk(
        0x101,
        (
            "#0003F#11P……折角だからお願いしよう。\x02\x03",

            "#0000Fえっと……エステルさんに\x01",
            "ヨシュア君だったかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "#0809F#6Pあ、呼び捨てでいいわよ。\x02\x03",

            "#0802F見たところ同い年くらいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "#0902F#6Pそうだね……\x01",
            "できればお近づきの印に。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#0005F#11Pあ、ああ……\x02\x03",

            "#0004F──それじゃあ、\x01",
            "エステル、ヨシュア。\x02\x03",

            "#0000F導力バスのこと、\x01",
            "よろしくお願いするよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        "#0809F#6Pうん！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        "#0900F#6P君たちの方も気をつけて。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Sound(1775, 255, 90, 0)    #voice#Joshua
    SetCameraDistance(23120, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0xBB8)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7200", 0)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x25)
    OP_D5(0x28)
    OP_D5(0x2C)
    OP_D5(0x2D)
    OP_37()
    OP_4C(0xA, 0xFF)
    SetChrPos(0xA, -51350, 0, -96010, 315)
    SetChrFlags(0xA, 0x10)
    OP_4C(0xB, 0xFF)
    SetChrPos(0xB, -52810, 0, -95050, 45)
    SetChrFlags(0xB, 0x10)
    OP_4C(0x9, 0xFF)
    SetChrPos(0x9, -53470, 0, -94190, 45)
    ClearMapObjFlags(0x2, 0x4)
    SetChrPos(0x0, -47400, 0, -96310, 225)
    SetScenarioFlags(0x61, 3)
    OP_29(0x3F, 0x1, 0x7)
    ModifyEventFlags(0, 0, 0x80)
    OP_E0(0x0)
    Call(0, 9)
    Call(0, 10)
    EventEnd(0x5)
    Return()

    # Function_19_352C end

    def Function_20_4984(): pass

    label("Function_20_4984")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_49A8")
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    Jump("Function_20_4984")

    label("loc_49A8")

    Return()

    # Function_20_4984 end

    def Function_21_49A9(): pass

    label("Function_21_49A9")

    OP_95(0xFE, -47450, 0, -94270, 2000, 0x0)
    OP_95(0xFE, -48230, 0, -94830, 2000, 0x0)
    OP_95(0xFE, -50330, 0, -94830, 2000, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    Sound(822, 0, 100, 0)
    Sleep(1000)
    OP_71(0x0, 0x1F, 0x3C, 0x0, 0x0)
    Sound(463, 0, 100, 0)
    OP_79(0x0)
    Sleep(1000)
    OP_71(0x0, 0x12D, 0x14A, 0x0, 0x0)
    Sound(454, 0, 100, 0)
    OP_79(0x0)
    Sleep(1000)
    OP_95(0xFE, -51890, 0, -96080, 2000, 0x0)
    OP_95(0xFE, -53450, 0, -94190, 2000, 0x0)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sound(833, 0, 100, 0)
    Sleep(2000)

    label("loc_4A5D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AA7")
    OP_96(0xFE, 0xFFFF3152, 0x0, 0xFFFE8D74, 0x7D0, 0x0)
    Sound(833, 0, 100, 0)
    Sleep(2000)
    OP_96(0xFE, 0xFFFF2F36, 0x0, 0xFFFE9012, 0x7D0, 0x0)
    Sound(833, 0, 100, 0)
    Sleep(2000)
    Jump("loc_4A5D")

    label("loc_4AA7")

    Return()

    # Function_21_49A9 end

    def Function_22_4AA8(): pass

    label("Function_22_4AA8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4AC2")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_22_4AA8")

    label("loc_4AC2")

    Return()

    # Function_22_4AA8 end

    def Function_23_4AC3(): pass

    label("Function_23_4AC3")


    def lambda_4AC8():
        OP_9D(0xFE, 0xFFFF35A8, 0x0, 0xFFFE8018, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4AC8)
    Sound(814, 0, 100, 0)
    SetChrChip(0x0, 0xFE, 0x32, 0x1F4)
    SetChrChipByIndex(0xFE, 0x29)
    SetChrSubChip(0xFE, 0x2)
    ClearChrFlags(0xFE, 0x1)
    Sleep(600)
    SetChrChipByIndex(0xFE, 0x2A)
    SetChrSubChip(0xFE, 0x2)
    OP_A1(0xFE, 0x3E8, 0x6, 0x2, 0x3, 0x4, 0x5, 0x6, 0x7)
    SetChrFlags(0xFE, 0x1)
    SetChrChip(0x1, 0xFE, 0x0, 0x0)
    SetChrChipByIndex(0xFE, 0x2C)
    SetChrSubChip(0xFE, 0x0)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_23_4AC3 end

    def Function_24_4B2C(): pass

    label("Function_24_4B2C")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    label("loc_4B34")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4B4F")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_4B34")

    label("loc_4B4F")

    Return()

    # Function_24_4B2C end

    def Function_25_4B50(): pass

    label("Function_25_4B50")

    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 1500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_4B8C():
        OP_A6(0xFE, 0x96, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4B8C)

    def lambda_4BA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4BA5)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_25_4B50 end

    def Function_26_4BC4(): pass

    label("Function_26_4BC4")

    EventBegin(0x0)
    OP_E0(0x3)
    Fade(1000)
    OP_68(-50910, 800, -96660, 0)
    MoveCamera(0, 17, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18850, 0)
    SetCameraDistance(17850, 2500)
    OP_4B(0xA, 0xFF)
    SetChrPos(0xA, -51450, 0, -96010, 135)
    SetChrPos(0x101, -50470, 0, -97180, 315)
    SetChrPos(0x102, -49360, 0, -97230, 315)
    SetChrPos(0x103, -50060, 0, -99050, 315)
    SetChrPos(0x104, -48830, 0, -98720, 315)
    OP_6F(0x10)
    OP_0D()

    #C0118
    ChrTalk(
        0xA,
        (
            "#0805F#5Pそういえば……\x01",
            "《特務支援課》だったっけ？\x02\x03",

            "#0800Fたしか遊撃士と似たような\x01",
            "仕事をする部署って聞いたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#0011F#11Pうっ……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#0108F#11Pえっと、その……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#0206F#12P……まあ、あながち\x01",
            "間違いではありませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "#0809F#5Pそっか～……\x01",
            "へへ、何だか嬉しいわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0123
    ChrTalk(
        0x101,
        "#0005F#11Pえ……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0305F#12P嬉しいって……\x01",
            "そりゃまたどうしてだい？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "#0802F#5Pだって似たような志で\x01",
            "仕事をしてくれてるんでしょ？\x02\x03",

            "それって要するに\x01",
            "お仲間みたいなもんじゃない。\x02\x03",

            "#0809Fえへへ……今後ともよろしくね！\x02",
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
    Sleep(1000)

    #C0126
    ChrTalk(
        0x104,
        "#0302F#12P（こりゃまた……）\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x103,
        (
            "#0204F#12P（お人好しさでは\x01",
            "  ロイドさん以上ですか……）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        "#0102F#11P（何だか眩しいくらいね……）\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0012F#11Pははっ……\x02\x03",

            "#0002F──ああ。\x01",
            "こちらこそよろしく頼むよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_4C(0xA, 0xFF)
    SetChrPos(0xA, -51450, 0, -96010, 315)
    SetChrPos(0x0, -50600, 0, -97410, 225)
    SetScenarioFlags(0x61, 4)
    OP_E0(0x2)
    Call(0, 9)
    Call(0, 10)
    EventEnd(0x5)
    Return()

    # Function_26_4BC4 end

    def Function_27_5017(): pass

    label("Function_27_5017")

    EventBegin(0x0)
    OP_E0(0x3)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Fade(1000)
    OP_68(-5760, 1000, 3900, 0)
    MoveCamera(36, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_50AB")
    SetChrPos(0x101, -2660, 0, 8920, 210)
    SetChrPos(0x102, -1580, 0, 8109, 210)
    SetChrPos(0x103, -80, 0, 9090, 210)
    SetChrPos(0x104, -1280, 0, 9660, 210)
    Jump("loc_50EF")

    label("loc_50AB")

    SetChrPos(0x101, -310, 0, -500, 315)
    SetChrPos(0x102, -70, 0, -1700, 315)
    SetChrPos(0x103, 1340, 0, -1430, 315)
    SetChrPos(0x104, 1070, 0, -350, 315)

    label("loc_50EF")


    def lambda_50F4():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_50F4)

    def lambda_5109():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5109)

    def lambda_511E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_511E)

    def lambda_5133():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5133)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetCameraDistance(19500, 2500)

    def lambda_51AD():
        OP_95(0xFE, -5470, 0, 4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_51AD)

    def lambda_51C7():
        OP_95(0xFE, -4680, 0, 3270, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_51C7)

    def lambda_51E1():
        OP_95(0xFE, -3230, 0, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_51E1)

    def lambda_51FB():
        OP_95(0xFE, -4160, 0, 5120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_51FB)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5273")
    WaitChrThread(0x104, 1)

    def lambda_5223():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5223)
    WaitChrThread(0x101, 1)

    def lambda_5234():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5234)
    WaitChrThread(0x103, 1)

    def lambda_5245():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5245)
    WaitChrThread(0x102, 1)

    def lambda_5256():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5256)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_52C7")

    label("loc_5273")

    WaitChrThread(0x102, 1)

    def lambda_527C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_527C)
    WaitChrThread(0x101, 1)

    def lambda_528D():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_528D)
    WaitChrThread(0x104, 1)

    def lambda_529E():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_529E)
    WaitChrThread(0x103, 1)

    def lambda_52AF():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_52AF)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    label("loc_52C7")

    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_534D")

    #C0130
    ChrTalk(
        0x101,
        (
            "#0001F#11P確か……\x01",
            "《星見の塔》はこの先だったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#0101F#11Pええ、警備隊のフェンスで\x01",
            "封鎖されていたけど……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_53C7")

    label("loc_534D")


    #C0132
    ChrTalk(
        0x101,
        (
            "#0001F#11P《星見の塔》……\x01",
            "ひょっとしてこっちの方か？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#0101F#11P前に見た位置を考えると\x01",
            "その可能性はありそうね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_53C7")


    #C0134
    ChrTalk(
        0x104,
        "#0300F#11Pま、とにかく行ってみようぜ。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        "#0202F#11Pですね。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, -6520, 0, 4300, 270)
    SetScenarioFlags(0x84, 0)
    OP_E0(0x2)
    Call(0, 9)
    EventEnd(0x5)
    Return()

    # Function_27_5017 end

    def Function_28_542A(): pass

    label("Function_28_542A")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 27)
    Return()

    # Function_28_542A end

    def Function_29_5438(): pass

    label("Function_29_5438")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_54E5")

    #C0136
    ChrTalk(
        0x104,
        (
            "#0300Fこの道は森の中に\x01",
            "入るみたいだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0000Fああ、森の奥に\x01",
            "遺跡があるって聞いた事がある。\x02\x03",

            "でも今は用事もないし……\x01",
            "立ち入らないでおこうか。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5525")

    label("loc_54E5")

    SetChrName("")

    #A0138
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "道は森の中へと続いている。\x01",
            "……今は特に用事はない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5525")

    Sleep(50)
    SetChrPos(0x0, -39950, -1400, -1490, 90)
    EventEnd(0x4)
    Return()

    # Function_29_5438 end

    SaveToFile()

Try(main)
