from ZeroScenarioHelper import *

def main():
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
        "巴士",                   # 1
        "驾驶员",                 # 2
        "艾丝蒂尔",               # 3
        "约修亚",                 # 4
        "ＢＯＳＳ１",             # 5
        "ＢＯＳＳ２",             # 6
        "ＢＯＳＳ３",             # 7
        "br1500",                 # 8
        "br1500",                 # 9
        "br1500",                 # 10
        "br1500",                 # 11
        "br1500",                 # 12
        "br1500",                 # 13
        "br1500",                 # 14
        "br1500",                 # 15
        "克洛斯贝尔市方向",       # 16
        "乌尔斯拉医科大学方向",   # 17
        "星见之塔方向",           # 18
    ))

    ATBonus("ATBonus_530", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_5089", 8,   2,   0,   0,   3,   0,   5)
    Sepith("Sepith_50A9", 2,   8,   0,   6,   2,   0,   0)
    Sepith("Sepith_5079", 8,   0,   5,   2,   0,   0,   4)
    Sepith("Sepith_5081", 0,   8,   0,   4,   4,   2,   0)
    Sepith("Sepith_5071", 4,   2,   0,   8,   0,   3,   2)
    Sepith("Sepith_50F9", 9,   7,   18,  6,   7,   6,   3)

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
        "BattleInfo_888", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_5089", 30, 45, 20, 5,
        (
            ("ms65800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms65800.dat", "ms65800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms65800.dat", "ms63600.dat", "ms65800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms65800.dat", "ms65800.dat", "ms66600.dat", "ms65800.dat", 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_950", 0x0000, 12, 6, 45, 10, 1, 25, 0, "br1500", "Sepith_50A9", 30, 45, 20, 5,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms69700.dat", "ms69700.dat", "ms69900.dat", "ms69800.dat", 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_6F8", 0x0000, 12, 6, 45, 10, 1, 45, 0, "br1500", "Sepith_5079", 30, 45, 20, 5,
        (
            ("ms66600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms66600.dat", "ms66600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms66600.dat", "ms62100.dat", "ms66600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms66600.dat", "ms66600.dat", "ms69700.dat", "ms66600.dat", 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_7C0", 0x0010, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_5081", 60, 25, 10, 5,
        (
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, 0, "ms63600.dat", 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms63600.dat", "ms66600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "ms63600.dat", 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms63600.dat", "ms63600.dat", "ms62100.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", "ms63600.dat", 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_630", 0x0000, 12, 6, 45, 10, 1, 30, 0, "br1500", "Sepith_5071", 30, 45, 20, 5,
        (
            ("ms62100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms62100.dat", "ms62100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms62100.dat", "ms69700.dat", "ms62100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_590", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
            ("ms62100.dat", "ms62100.dat", "ms65800.dat", "ms62100.dat", 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_5F0", "ed7400", "ed7403", "ATBonus_530"),
        )
    )

    BattleInfo(
        "BattleInfo_AA0", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br1500", "Sepith_50F9", 40, 35, 25, 0,
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

    PlaceName(2.0, 0.4300000071525574, 40.0, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(-59.900001525878906, 0.0, -142.27999877929688, 0x0000, 0x0000, "乌尔斯拉医科大学方向")
    PlaceName(-51.7400016784668, -1.399999976158142, -3.7799999713897705, 0x0000, 0x0000, "星见之塔方向")

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
        "Function_5_12A4",         # 05, 5
        "Function_6_13DA",         # 06, 6
        "Function_7_13EE",         # 07, 7
        "Function_8_1402",         # 08, 8
        "Function_9_1416",         # 09, 9
        "Function_10_142F",        # 0A, 10
        "Function_11_1458",        # 0B, 11
        "Function_12_157C",        # 0C, 12
        "Function_13_164F",        # 0D, 13
        "Function_14_176E",        # 0E, 14
        "Function_15_1849",        # 0F, 15
        "Function_16_1BBC",        # 10, 16
        "Function_17_1C21",        # 11, 17
        "Function_18_2210",        # 12, 18
        "Function_19_32EE",        # 13, 19
        "Function_20_4547",        # 14, 20
        "Function_21_456C",        # 15, 21
        "Function_22_466B",        # 16, 22
        "Function_23_4686",        # 17, 23
        "Function_24_46EF",        # 18, 24
        "Function_25_4713",        # 19, 25
        "Function_26_4787",        # 1A, 26
        "Function_27_4B6E",        # 1B, 27
        "Function_28_4F57",        # 1C, 28
        "Function_29_4F65",        # 1D, 29
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125B")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3D, 1)"), scpexpr(EXPR_END)), "loc_11ED")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_1256")

    label("loc_11ED")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x3D),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1256")

    Jump("loc_1298")

    label("loc_125B")

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

    label("loc_1298")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_116E end

    def Function_5_12A4(): pass

    label("Function_5_12A4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x116, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1391")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_1323")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x116, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_138C")

    label("loc_1323")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_138C")

    Jump("loc_13CE")

    label("loc_1391")

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

    label("loc_13CE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_12A4 end

    def Function_6_13DA(): pass

    label("Function_6_13DA")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_13DA end

    def Function_7_13EE(): pass

    label("Function_7_13EE")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_13EE end

    def Function_8_1402(): pass

    label("Function_8_1402")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 3)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1402 end

    def Function_9_1416(): pass

    label("Function_9_1416")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_142E")
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)

    label("loc_142E")

    Return()

    # Function_9_1416 end

    def Function_10_142F(): pass

    label("Function_10_142F")

    SetChrFlags(0x13, 0x80)
    SetChrBattleFlags(0x13, 0x8000)
    SetChrFlags(0x14, 0x80)
    SetChrBattleFlags(0x14, 0x8000)
    SetChrFlags(0x15, 0x80)
    SetChrBattleFlags(0x15, 0x8000)
    SetChrFlags(0x16, 0x80)
    SetChrBattleFlags(0x16, 0x8000)
    Return()

    # Function_10_142F end

    def Function_11_1458(): pass

    label("Function_11_1458")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x70, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1544")

    #C0007
    ChrTalk(
        0xFE,
        (
            "哎呀，各位警察，\x01",
            "刚才谢谢了。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0xFE,
        (
            "虽然游击士\x01",
            "的确也很厉害……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "但如果你们没来，\x01",
            "恐怕就真的有危险了。\x01",
            "请容我表示谢意。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        (
            "对了……不嫌弃的话，\x01",
            "要不要在巴士里休息一下？\x02",
        )
    )

    CloseMessageWindow()

    #C0011
    ChrTalk(
        0xFE,
        (
            "那些空座位\x01",
            "你们可以随便坐。\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)
    SetScenarioFlags(0x70, 7)
    Jump("loc_1578")

    label("loc_1544")


    #C0012
    ChrTalk(
        0xFE,
        (
            "怎样，不嫌弃的话，\x01",
            "要不要在巴士里休息一下？\x02",
        )
    )

    CloseMessageWindow()
    Call(0, 12)

    label("loc_1578")

    TalkEnd(0xFE)
    Return()

    # Function_11_1458 end

    def Function_12_157C(): pass

    label("Function_12_157C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在巴士中休息\x01",      # 0
            "放弃\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F9")
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
    Jump("loc_164E")

    label("loc_15F9")

    FadeToBright(300, 0)

    #C0013
    ChrTalk(
        0x9,
        (
            "是吗，想休息的时候\x01",
            "就随时跟我说吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x9,
        (
            "看这样子，\x01",
            "暂时也发动不了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_164E")

    Return()

    # Function_12_157C end

    def Function_13_164F(): pass

    label("Function_13_164F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x61, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1665")
    Call(0, 26)
    Jump("loc_176D")

    label("loc_1665")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_167A")
    Call(0, 15)
    Jump("loc_176A")

    label("loc_167A")


    #C0015
    ChrTalk(
        0xA,
        (
            "#0800F啊，罗伊德，还有大家。\x02\x03",

            "没问题，这边就交给我们吧。\x02\x03",

            "#0804F防范魔兽，\x01",
            "向乘客们进行说明，\x01",
            "还有向市政厅报告对吧。\x02\x03",

            "#0800F我们会把这些事情处理好的，\x01",
            "希望你们也能免于分心，\x01",
            "全力专注于自己的工作。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x101,
        "#0000F不好意思，那就拜托你们了。\x02",
    )

    CloseMessageWindow()

    label("loc_176A")

    TalkEnd(0xA)

    label("loc_176D")

    Return()

    # Function_13_164F end

    def Function_14_176E(): pass

    label("Function_14_176E")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1783")
    Call(0, 15)
    Jump("loc_1845")

    label("loc_1783")


    #C0017
    ChrTalk(
        0xB,
        (
            "#0904F特别任务支援科的事情，\x01",
            "我们已经有所耳闻……\x01",
            "不过，真没想到这么快就能见面啊。\x02\x03",

            "#0900F引擎的修理\x01",
            "似乎还要花一点时间。\x01",
            "你们不必介意，继续赶路吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        "#0300F不好意思，这边就拜托你们啦。\x02",
    )

    CloseMessageWindow()

    label("loc_1845")

    TalkEnd(0xB)
    Return()

    # Function_14_176E end

    def Function_15_1849(): pass

    label("Function_15_1849")

    OP_4B(0xA, 0xFF)
    OP_4B(0xB, 0xFF)

    #C0019
    ChrTalk(
        0xA,
        (
            "#0804F#11P不过，导力车也好，\x01",
            "什么网络也好，\x01",
            "克洛斯贝尔还真是先进呢。\x02\x03",

            "#0800F我原本还以为利贝尔的\x01",
            "导力技术才是最先进的。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)

    #C0020
    ChrTalk(
        0xB,
        (
            "#0904F#5P利贝尔虽然技术先进，\x01",
            "但毕竟民风比较传统嘛。\x02\x03",

            "#0900F而且，导力网络方面\x01",
            "似乎也是由爱普斯泰恩财团推进的。\x02\x03",

            "从这个意义上来说……\x01",
            "目前，导力化最为完善的地方\x01",
            "或许还是克洛斯贝尔吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xA,
        (
            "#0805F#11P原来如此……\x02\x03",

            "#0809F要是带提妲来这里的话，\x01",
            "她一定会开心得跳起来呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xB,
        (
            "#0909F#5P哈哈……是啊。\x02\x03",

            "#0902F艾丝蒂尔……你感到寂寞了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xA,
        (
            "#0802F#11P啊哈哈……\x02\x03",

            "#0804F虽然是以那种形式，\x01",
            "但我们毕竟还是重逢过了呢。\x02\x03",

            "#0808F自那之后，已经过去了三个月……\x01",
            "不知大家现在都还好吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xB,
        (
            "#0904F#5P没问题……\x01",
            "大家一定都很好的。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B0F")

    #C0025
    ChrTalk(
        0x101,
        "#0005F（在说谁啊……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1B0F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B40")

    #C0026
    ChrTalk(
        0x102,
        "#0105F（在说谁呢……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1B40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B75")

    #C0027
    ChrTalk(
        0x103,
        "#0200F（……说的是谁……？）\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B9F")

    label("loc_1B75")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B9F")

    #C0028
    ChrTalk(
        0x104,
        "#0300F（说谁呢……？）\x02",
    )

    CloseMessageWindow()

    label("loc_1B9F")

    SetScenarioFlags(0x0, 1)
    ClearChrFlags(0xA, 0x10)
    ClearChrFlags(0xB, 0x10)
    OP_4C(0xA, 0xFF)
    OP_4C(0xB, 0xFF)
    OP_93(0xB, 0x2D, 0x0)
    Return()

    # Function_15_1849 end

    def Function_16_1BBC(): pass

    label("Function_16_1BBC")

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

    # Function_16_1BBC end

    def Function_17_1C21(): pass

    label("Function_17_1C21")

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
        "#0013F#11P那是……！\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x104,
        (
            "#0307F#11P嘁……\x01",
            "果然料中了吗！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7511", 0)
    Fade(1000)
    OP_63(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)

    def lambda_1EAB():
        OP_A6(0xFE, 0x0, 0x32, 0x5DC, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1EAB)
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
            "#5P呜、呜啊！\x01",
            "为什么这种时候会有魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x9,
        (
            "#5P啊啊，女神啊！\x01",
            "求您保佑我吧～！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#0007F#1P不要紧吧……！\x02",
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

    def lambda_2061():
        OP_95(0xFE, -41650, 0, -93000, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2061)

    def lambda_207B():
        OP_95(0xFE, -40590, 0, -90960, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_207B)

    def lambda_2095():
        OP_95(0xFE, -40140, 0, -93680, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2095)

    def lambda_20AF():
        OP_95(0xFE, -39140, 0, -91570, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_20AF)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x10)

    def lambda_20DB():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20DB)

    def lambda_20E8():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_20E8)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)

    #C0034
    ChrTalk(
        0x9,
        "#5P你、你们是……！？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        "#0013F#11P我们是警察！\x02",
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x104,
        (
            "#0307F#2P快到车里去，\x01",
            "我们立刻就击退它们！\x02",
        )
    )

    CloseMessageWindow()
    OP_64(0x9)
    OP_68(-43010, 1100, -92990, 1500)
    OP_93(0x9, 0x0, 0x1F4)

    def lambda_217F():
        OP_95(0xFE, -48840, 500, -92450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_217F)
    Sleep(300)

    def lambda_219C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_219C)
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

    # Function_17_1C21 end

    def Function_18_2210(): pass

    label("Function_18_2210")

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
            "#0006F#12P呼……\x01",
            "还真难对付呢。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2523():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2523)

    def lambda_2530():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2530)
    Sleep(100)

    def lambda_2540():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2540)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0038
    ChrTalk(
        0x102,
        (
            "#0106F#5P是呀……\x02\x03",

            "#0101F这种魔兽的体型很大，\x01",
            "是从哪里出现的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x103,
        (
            "#0206F#5P……看起来，似乎是\x01",
            "栖息在森林地带的种类……\x02\x03",

            "#0200F是出于某种契机\x01",
            "而来到了这里吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x104,
        (
            "#0305F#11P哦……？\x01",
            "还有这种稀奇事啊。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_68(-48290, 200, -93170, 3000)
    MoveCamera(320, 19, 0, 3000)
    OP_71(0x0, 0x1, 0x1E, 0x0, 0x0)
    Sound(464, 0, 100, 0)
    OP_79(0x0)

    def lambda_2661():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2661)

    def lambda_266E():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_266E)

    def lambda_267B():
        TurnDirection(0xFE, 0x9, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_267B)

    def lambda_2688():
        TurnDirection(0xFE, 0x9, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2688)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    def lambda_26A5():
        OP_95(0xFE, -48090, 300, -93440, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_26A5)

    def lambda_26BF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_26BF)
    WaitChrThread(0x9, 1)
    WaitChrThread(0x9, 2)
    OP_6F(0x79)

    #C0041
    ChrTalk(
        0x9,
        "#5P你们几个，干得好！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        (
            "#5P哎呀～得救了！\x01",
            "刚才一时还真不知该如何是好呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x101,
        (
            "#0004F#6P哪里，您平安无事就好。\x02\x03",

            "#0000F您是因为刚才的魔兽\x01",
            "才把车停在这里的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x9,
        "#5P啊，其实……\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x9,
        (
            "#5P导力引擎在此之前就\x01",
            "出现了故障。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x9,
        (
            "#5P无奈之下，我只能临时停车，\x01",
            "下来检查……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x104,
        (
            "#0300F#12P结果，刚才的魔兽就在那时突然出现，\x01",
            "使你陷入了进退两难的绝境吗。\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        (
            "#0200F#6P通讯器的信号不好，\x01",
            "也是因为引擎故障吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x9,
        (
            "#5P嗯，因为巴士上的通讯器\x01",
            "是从引擎获取导力的。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x9,
        (
            "#5P哦，现在可顾不上聊天了。\x01",
            "得赶快确认一下，看看能不能想办法修好……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-49330, 200, -94050, 3000)

    def lambda_2902():

        label("loc_2902")

        TurnDirection(0x101, 0x9, 500)
        Yield()
        Jump("loc_2902")

    QueueWorkItem2(0x101, 1, lambda_2902)

    def lambda_2914():

        label("loc_2914")

        TurnDirection(0x102, 0x9, 500)
        Yield()
        Jump("loc_2914")

    QueueWorkItem2(0x102, 1, lambda_2914)

    def lambda_2926():

        label("loc_2926")

        TurnDirection(0x103, 0x9, 500)
        Yield()
        Jump("loc_2926")

    QueueWorkItem2(0x103, 1, lambda_2926)

    def lambda_2938():

        label("loc_2938")

        TurnDirection(0x104, 0x9, 500)
        Yield()
        Jump("loc_2938")

    QueueWorkItem2(0x104, 1, lambda_2938)
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

    def lambda_29BF():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29BF)
    Sleep(50)

    def lambda_29CF():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29CF)

    def lambda_29DC():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29DC)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0051
    ChrTalk(
        0x102,
        (
            "#0103F#5P……看起来，\x01",
            "要想修好，似乎得花点时间呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        (
            "#0001F#12P嗯～我们还是先回市里一趟，\x01",
            "向交通科的人报告为好吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#0206F#5P呼……这也是命运吗？\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#0306F#11P唉，虽然麻烦，\x01",
            "但好像也只能这么做了──\x02",
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
        "#0307F#11P……喂！\x02",
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

    def lambda_2B58():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B58)

    def lambda_2B65():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2B65)
    Sleep(100)

    def lambda_2B75():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2B75)

    def lambda_2B82():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B82)
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
        "#5P呜、呜咿咿咿！？\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        "#0005F#2P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x103,
        "#0201F#11P怎么会……\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x102,
        "#0107F#2P竟然还有吗……！？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0303F#11P这下可真有点不妙啊……\x02\x03",

            "#0307F喂，罗伊德！\x01",
            "准备各个击破！\x02\x03",

            "同时对付全部\x01",
            "是行不通的！\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#0007F#11P不……不行！\x02\x03",

            "那样的话，\x01",
            "巴士可能会遭到袭击！\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        "#0310F#11P嘁，那倒也是啊……\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x102,
        (
            "#0101F#2P总之，\x01",
            "必须要立刻采取措施……！\x02",
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

    def lambda_2E39():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_2E39)
    Sleep(300)
    EndChrThread(0xD, 0x3)
    SetChrChipByIndex(0xD, 0x27)
    SetChrSubChip(0xD, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xD, 3, 0, 22)

    def lambda_2E73():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2E73)
    Sleep(200)
    EndChrThread(0xE, 0x3)
    SetChrChipByIndex(0xE, 0x27)
    SetChrSubChip(0xE, 0x0)
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xE, 3, 0, 22)

    def lambda_2EAD():
        OP_98(0xFE, 0x3E8, 0x0, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2EAD)
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
        "#0207F#2P……来了……！\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#0010F#2P（………呜…………！？）\x02",
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

    def lambda_2FBD():
        OP_95(0xFE, -50690, 0, -99150, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2FBD)
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

    def lambda_3091():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3091)

    def lambda_30AB():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_30AB)

    def lambda_30C5():
        OP_98(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFF06, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_30C5)
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
        "#0005F#2P哎……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x104,
        "#0305F#2P什么……\x02",
    )

    CloseMessageWindow()

    #N0068
    NpcTalk(
        0xA,
        "双马尾的女孩",
        "#0807F#5P约修亚！\x02",
    )

    CloseMessageWindow()

    #N0069
    NpcTalk(
        0xB,
        "黑发的青年",
        "#0903F#11P──嗯！\x02",
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

    # Function_18_2210 end

    def Function_19_32EE(): pass

    label("Function_19_32EE")

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
        "#0005F#11P……啊………\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x102,
        "#0105F#11P厉、厉害……\x02",
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x103,
        "#0205F#11P……叹为观止。\x02",
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
        "黑发的青年",
        (
            "#0903F#11P……呼，\x01",
            "总算赶上了啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xA, 500)
    Sleep(300)

    #N0074
    NpcTalk(
        0xB,
        "黑发的青年",
        "#0900F#11P艾丝蒂尔，你没事吧？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)
    Sleep(300)

    #N0075
    NpcTalk(
        0xA,
        "双马尾的女孩",
        (
            "#0804F#5P嗯，我没什么。\x02\x03",

            "#0800F总算成功给约修亚创造了\x01",
            "杀入敌阵的时机，真是太好了。\x02\x03",

            "#0805F话说回来……\x02",
        )
    )

    CloseMessageWindow()
    PlayBGM("ed7519", 0)
    OP_68(-49690, 800, -95970, 2000)

    def lambda_37D1():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_37D1)
    TurnDirection(0xB, 0x101, 500)
    OP_93(0x9, 0x87, 0x1F4)
    WaitChrThread(0xA, 1)
    OP_6F(0x1)

    #N0076
    NpcTalk(
        0xA,
        "双马尾的女孩",
        (
            "#0800F#6P嗯，难不成，\x01",
            "你们是克洛斯贝尔警察局的人吗？\x02\x03",

            "我们在南出口听交通科的人\x01",
            "说了这里的情况。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        (
            "#0011F#11P啊，是的……\x02\x03",

            "#0001F那个，你们是……\x02",
        )
    )

    CloseMessageWindow()

    #N0078
    NpcTalk(
        0xA,
        "双马尾的女孩",
        (
            "#0809F#6P啊，突然出现，\x01",
            "好像把你们搞糊涂了吧。\x02",
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
    SetChrName("双马尾的女孩")

    #A0079
    AnonymousTalk(
        0xFF,
        (
            "初次见面！\x02\x03",

            "我是艾丝蒂尔，\x01",
            "艾丝蒂尔·布莱特。\x02",
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
    SetChrName("黑发的青年")

    #A0080
    AnonymousTalk(
        0xFF,
        (
            "我叫约修亚。\x02\x03",

            "我们刚刚被正式调配到\x01",
            "游击士协会克洛斯贝尔分部。\x02",
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
        "#0006F#11P（果然是游击士吗……）\x02",
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
            "#0003F#11P我们是克洛斯贝尔警察局·特别\x01",
            "任务支援科的成员。\x02\x03",

            "#0000F多谢你们在危机时刻出手相救，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xA,
        (
            "#0809F#6P啊哈哈，不客气。\x02\x03",

            "#0800F你们好像也挺厉害的，\x01",
            "我还怕是我们\x01",
            "多管闲事了呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x101,
        (
            "#0006F#11P不……\x01",
            "说实话，真是千钧一发啊。\x02\x03",

            "#0000F──我是罗伊德，\x01",
            "罗伊德·班宁斯。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x102,
        (
            "#0100F#11P幸会，\x01",
            "我是艾莉·麦克道尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        (
            "#0302F#11P你们好啊，\x01",
            "我是兰迪·奥兰多。\x02",
        )
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x103,
        (
            "#0203F#11P我是缇欧·普拉托。\x01",
            "……请多关照。（点头行礼）\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xA,
        (
            "#0800F#6P罗伊德先生、艾莉小姐、\x01",
            "兰迪先生和小缇欧……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0089
    ChrTalk(
        0xA,
        "#0805F#6P咦，缇欧和罗伊德……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xB,
        (
            "#0909F#6P哈哈……\x01",
            "真是有趣的巧合呢。\x02",
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
        "#0005F#11P那个……？\x02",
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        "#0205F#11P……我们的名字有什么问题吗？\x02",
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xA,
        (
            "#0809F#6P啊哈哈，抱歉抱歉。\x02\x03",

            "#0802F我们认识的人里正好\x01",
            "也有人叫缇欧和罗伊德，\x01",
            "所以觉得这个巧合挺有趣的。\x02\x03",

            "当然，你们长得完全不像啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x101,
        "#0000F#11P这、这样啊……\x02",
    )

    CloseMessageWindow()
    OP_63(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xB, 0x9, 500)

    #C0095
    ChrTalk(
        0xB,
        (
            "#0901F#12P说起来……\x01",
            "导力巴士怎么样了？\x02\x03",

            "看起来，好像是\x01",
            "引擎出了故障吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xA, 0x9, 500)
    Sleep(1000)

    #C0096
    ChrTalk(
        0x9,
        "#5P啊，是的……\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x9,
        (
            "#5P原因应该就是\x01",
            "结晶回路的接触不良……\x02",
        )
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0x9,
        (
            "#5P伤脑筋啊，早知道会遇到这种事的话，\x01",
            "我多少也应该参加几次\x01",
            "那个维修培训的。\x02",
        )
    )

    CloseMessageWindow()

    #C0099
    ChrTalk(
        0xB,
        (
            "#0903F#12P那个，不介意的话，\x01",
            "能让我看看吗？\x02\x03",

            "#0900F说不定可以想办法\x01",
            "修理一下。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0100
    ChrTalk(
        0x9,
        "#5P哦，真的吗！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0xB, 500)

    #C0101
    ChrTalk(
        0xA,
        (
            "#0802F#5P说起来，约修亚，\x01",
            "你还会操纵飞行船呢。\x02\x03",

            "简单的维修应该是小菜一碟吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0102
    ChrTalk(
        0x9,
        (
            "#5P哎呀～真不愧是游击士！\x01",
            "出事的时候真是可靠啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0xB,
        "#0904F#12P不，我还差得远呢。\x02",
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
            "#0301F#11P（我说阿缇……\x01",
            "  你会修引擎吗？）\x02",
        )
    )

    CloseMessageWindow()

    #C0105
    ChrTalk(
        0x103,
        (
            "#0206F#11P（不……完全不懂。）\x02\x03",

            "（和导力网络相关的机器\x01",
            "  倒是还懂一些……）\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xA, 0x101, 500)

    def lambda_4142():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_4142)
    Sleep(300)

    #C0106
    ChrTalk(
        0xA,
        (
            "#0805F#6P话说回来……\x01",
            "你们为什么会来这里？\x02\x03",

            "#0800F是和我们一样，\x01",
            "来搜寻通缉魔兽的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0107
    ChrTalk(
        0x101,
        (
            "#0011F#11P不……\x01",
            "倒不是那样的。\x02",
        )
    )

    CloseMessageWindow()

    #C0108
    ChrTalk(
        0x102,
        (
            "#0103F#11P我们在执行警察局的任务，\x01",
            "正要前往前方的医院。\x02\x03",

            "#0100F然后就正好\x01",
            "碰上了这场骚乱。\x02",
        )
    )

    CloseMessageWindow()

    #C0109
    ChrTalk(
        0xB,
        (
            "#0900F#6P前方的医院……\x01",
            "是『圣乌尔斯拉医科大学』吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0xA,
        (
            "#0805F#6P嘿～还有这样的地方啊。\x02\x03",

            "#0800F啊，既然如此，\x01",
            "这里就交给我们好了。\x02\x03",

            "你们如果有事要办，\x01",
            "还是立刻动身为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x102,
        "#0105F#11P这、这个……\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0112
    ChrTalk(
        0x101,
        (
            "#0003F#11P……承蒙好意，那就麻烦你们了。\x02\x03",

            "#0000F那个……是艾丝蒂尔小姐\x01",
            "和约修亚先生吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0113
    ChrTalk(
        0xA,
        (
            "#0809F#6P啊，直接叫名字就好啦。\x02\x03",

            "#0802F看上去，我们年纪应该差不多吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0114
    ChrTalk(
        0xB,
        (
            "#0902F#6P是啊……\x01",
            "可以的话，就当做是友好的证明。\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#0005F#11P啊，好的……\x02\x03",

            "#0004F──那么，\x01",
            "艾丝蒂尔、约修亚。\x02\x03",

            "#0000F导力巴士的事\x01",
            "就拜托你们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0116
    ChrTalk(
        0xA,
        "#0809F#6P嗯！\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0xB,
        "#0900F#6P你们也要多加小心。\x02",
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

    # Function_19_32EE end

    def Function_20_4547(): pass

    label("Function_20_4547")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_456B")
    OP_93(0xFE, 0xE1, 0x1F4)
    Sleep(1000)
    OP_93(0xFE, 0x87, 0x1F4)
    Sleep(1000)
    Jump("Function_20_4547")

    label("loc_456B")

    Return()

    # Function_20_4547 end

    def Function_21_456C(): pass

    label("Function_21_456C")

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

    label("loc_4620")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_466A")
    OP_96(0xFE, 0xFFFF3152, 0x0, 0xFFFE8D74, 0x7D0, 0x0)
    Sound(833, 0, 100, 0)
    Sleep(2000)
    OP_96(0xFE, 0xFFFF2F36, 0x0, 0xFFFE9012, 0x7D0, 0x0)
    Sound(833, 0, 100, 0)
    Sleep(2000)
    Jump("loc_4620")

    label("loc_466A")

    Return()

    # Function_21_456C end

    def Function_22_466B(): pass

    label("Function_22_466B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4685")
    OP_A1(0xFE, 0x5DC, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_22_466B")

    label("loc_4685")

    Return()

    # Function_22_466B end

    def Function_23_4686(): pass

    label("Function_23_4686")


    def lambda_468B():
        OP_9D(0xFE, 0xFFFF35A8, 0x0, 0xFFFE8018, 0x9C4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_468B)
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

    # Function_23_4686 end

    def Function_24_46EF(): pass

    label("Function_24_46EF")

    SetChrChipByIndex(0xFE, 0x2B)
    SetChrSubChip(0xFE, 0x0)

    label("loc_46F7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4712")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("loc_46F7")

    label("loc_4712")

    Return()

    # Function_24_46EF end

    def Function_25_4713(): pass

    label("Function_25_4713")

    PlayEffect(0x0, 0xFF, 0xFE, 0x140, 0, 1500, 0, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)

    def lambda_474F():
        OP_A6(0xFE, 0x96, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_474F)

    def lambda_4768():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_4768)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    SetChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x8000)
    Return()

    # Function_25_4713 end

    def Function_26_4787(): pass

    label("Function_26_4787")

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
            "#0805F#5P说起来……\x01",
            "是叫『特别任务支援科』吧？\x02\x03",

            "#0800F听说是工作性质与游击士\x01",
            "相似的部门。\x02",
        )
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x101,
        "#0011F#11P呜……\x02",
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x102,
        "#0108F#11P哎，这个……\x02",
    )

    CloseMessageWindow()

    #C0121
    ChrTalk(
        0x103,
        (
            "#0206F#12P……嗯，好像\x01",
            "也没说错吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0xA,
        (
            "#0809F#5P是吗～……\x01",
            "嘿嘿，好开心哦。\x02",
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
        "#0005F#11P哎……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x104,
        (
            "#0305F#12P开心……\x01",
            "这又是为什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0xA,
        (
            "#0802F#5P因为，你们是怀着与我们\x01",
            "相似的志向来工作的吧？\x02\x03",

            "坦白地说，\x01",
            "不就和同伴一样嘛。\x02\x03",

            "#0809F嘿嘿……今后也请多多关照哦！\x02",
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
        "#0302F#12P（这可真是……）\x02",
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x103,
        (
            "#0204F#12P（老好人的程度\x01",
            "  竟然在罗伊德前辈之上吗……）\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x102,
        "#0102F#11P（感觉都有点耀眼呢……）\x02",
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x101,
        (
            "#0012F#11P哈哈……\x02\x03",

            "#0002F──嗯。\x01",
            "彼此彼此，请多关照啦。\x02",
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

    # Function_26_4787 end

    def Function_27_4B6E(): pass

    label("Function_27_4B6E")

    EventBegin(0x0)
    OP_E0(0x3)
    ModifyEventFlags(0, 1, 0x80)
    ModifyEventFlags(0, 2, 0x80)
    Fade(1000)
    OP_68(-5760, 1000, 3900, 0)
    MoveCamera(36, 18, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21500, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4C02")
    SetChrPos(0x101, -2660, 0, 8920, 210)
    SetChrPos(0x102, -1580, 0, 8109, 210)
    SetChrPos(0x103, -80, 0, 9090, 210)
    SetChrPos(0x104, -1280, 0, 9660, 210)
    Jump("loc_4C46")

    label("loc_4C02")

    SetChrPos(0x101, -310, 0, -500, 315)
    SetChrPos(0x102, -70, 0, -1700, 315)
    SetChrPos(0x103, 1340, 0, -1430, 315)
    SetChrPos(0x104, 1070, 0, -350, 315)

    label("loc_4C46")


    def lambda_4C4B():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4C4B)

    def lambda_4C60():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4C60)

    def lambda_4C75():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4C75)

    def lambda_4C8A():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4C8A)
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

    def lambda_4D04():
        OP_95(0xFE, -5470, 0, 4250, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D04)

    def lambda_4D1E():
        OP_95(0xFE, -4680, 0, 3270, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D1E)

    def lambda_4D38():
        OP_95(0xFE, -3230, 0, 4400, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D38)

    def lambda_4D52():
        OP_95(0xFE, -4160, 0, 5120, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4D52)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4DCA")
    WaitChrThread(0x104, 1)

    def lambda_4D7A():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4D7A)
    WaitChrThread(0x101, 1)

    def lambda_4D8B():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4D8B)
    WaitChrThread(0x103, 1)

    def lambda_4D9C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D9C)
    WaitChrThread(0x102, 1)

    def lambda_4DAD():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DAD)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Jump("loc_4E1E")

    label("loc_4DCA")

    WaitChrThread(0x102, 1)

    def lambda_4DD3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4DD3)
    WaitChrThread(0x101, 1)

    def lambda_4DE4():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4DE4)
    WaitChrThread(0x104, 1)

    def lambda_4DF5():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4DF5)
    WaitChrThread(0x103, 1)

    def lambda_4E06():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4E06)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    label("loc_4E1E")

    OP_6F(0x79)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 6)), scpexpr(EXPR_END)), "loc_4E96")

    #C0130
    ChrTalk(
        0x101,
        (
            "#0001F#11P我记得……\x01",
            "『星见之塔』就在这前面吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x102,
        (
            "#0101F#11P嗯，虽然被\x01",
            "警备队用防护栏封锁了……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4EFC")

    label("loc_4E96")


    #C0132
    ChrTalk(
        0x101,
        (
            "#0001F#11P『星见之塔』……\x01",
            "莫非是这边吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0133
    ChrTalk(
        0x102,
        (
            "#0101F#11P从之前见过的位置来推测，\x01",
            "似乎有可能呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4EFC")


    #C0134
    ChrTalk(
        0x104,
        "#0300F#11P嗯，总之，过去看看吧。\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        "#0202F#11P是呀。\x02",
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

    # Function_27_4B6E end

    def Function_28_4F57(): pass

    label("Function_28_4F57")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Call(0, 27)
    Return()

    # Function_28_4F57 end

    def Function_29_4F65(): pass

    label("Function_29_4F65")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FFC")

    #C0136
    ChrTalk(
        0x104,
        (
            "#0300F这条路似乎是\x01",
            "通向森林的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        (
            "#0000F嗯，我听说\x01",
            "森林深处好像有个遗迹。\x02\x03",

            "不过现在也没什么事要去……\x01",
            "还是不要进去了吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_5032")

    label("loc_4FFC")

    SetChrName("")

    #A0138
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "道路通往森林深处。\x01",
            "……现在没什么事要去。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_5032")

    Sleep(50)
    SetChrPos(0x0, -39950, -1400, -1490, 90)
    EventEnd(0x4)
    Return()

    # Function_29_4F65 end

    SaveToFile()

Try(main)
