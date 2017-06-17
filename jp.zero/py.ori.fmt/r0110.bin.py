from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0110.bin",                # FileName
        "r0110",                    # MapName
        "r0110",                    # Location
        0x0061,                     # MapIndex
        "ed7201",
        0x00000000,                 # Flags
        ("r0110", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 97, 0, 4, 0, 5],
    )

    BuildStringList((
        "r0110",                  # 0
        "観光ガイド",             # 1
        "観光客シュウラン",       # 2
        "観光客ウォルト",         # 3
        "観光客サイファー",       # 4
        "観光客アリュート",       # 5
        "観光客ティーニー",       # 6
        "バス",                   # 7
        "飲み物",                 # 8
        "飲み物",                 # 9
        "飲み物",                 # 10
        "飲み物",                 # 11
        "SE制御",                 # 12
        "br0100",                 # 13
        "br0100",                 # 14
        "br0100",                 # 15
        "br0100",                 # 16
        "br0100",                 # 17
        "br0100",                 # 18
        "br0100",                 # 19
        "クロスベル市・タングラム門方面",# 20
        "アルモリカ村方面",       # 21
    ))

    ATBonus("ATBonus_638", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3FE9", 1,   7,   0,   3,   0,   1,   5)
    Sepith("Sepith_3FF1", 2,   0,   7,   1,   4,   2,   1)
    Sepith("Sepith_3FD1", 6,   3,   0,   0,   4,   3,   1)
    Sepith("Sepith_3FD9", 3,   0,   7,   0,   2,   1,   4)
    Sepith("Sepith_3FE1", 0,   2,   0,   7,   3,   5,   0)
    Sepith("Sepith_3FF9", 34,  15,  25,  15,  0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_698", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_69C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6F8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6FC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_700", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_704", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_708", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_70C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_710", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_714", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_678", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_67C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_680", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_684", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_688", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_68C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_690", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_694", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_718", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_71C", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_720", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_724", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_728", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_72C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_730", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_734", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_9D4", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_3FE9", 30, 45, 20, 5,
        (
            ("ms64500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms64500.dat", "ms64500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms64500.dat", "ms62600.dat", "ms64500.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
        )
    )

    BattleInfo(
        "BattleInfo_938", 0x0000, 10, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_3FF1", 30, 45, 25, 0,
        (
            ("ms69800.dat", "ms69800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_678", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms69800.dat", "ms63900.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms69800.dat", "ms69900.dat", "ms62600.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_678", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_870", 0x0000, 10, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_3FD1", 30, 45, 20, 5,
        (
            ("ms62200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms62200.dat", "ms62200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_678", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms62200.dat", "ms69800.dat", "ms62200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms62200.dat", "ms61800.dat", "ms62200.dat", "ms61800.dat", 0, 0, 0, 0, "MonsterBattlePostion_678", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
        )
    )

    BattleInfo(
        "BattleInfo_7D4", 0x0000, 10, 6, 45, 6, 1, 50, 0, "br0100", "Sepith_3FD9", 30, 45, 25, 0,
        (
            ("ms62600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_678", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms62600.dat", "ms66200.dat", "ms62600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_738", 0x0000, 10, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_3FE1", 30, 45, 25, 0,
        (
            ("ms63900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms63900.dat", "ms63900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_678", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms63900.dat", "ms62600.dat", "ms63900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AE0", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_3FF9", 40, 35, 25, 0,
        (
            ("ms76201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_678", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_698", "MonsterBattlePostion_6F8", "ed7400", "ed7403", "ATBonus_638"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A9C", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms66801.dat", "ms66801.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_718", "MonsterBattlePostion_6F8", "ed7401", "ed7403", "ATBonus_638"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

    AddCharChip((
        "chr/ch26600.itc",                   # 00
        "chr/ch32500.itc",                   # 01
        "chr/ch23000.itc",                   # 02
        "chr/ch33102.itc",                   # 03
        "chr/ch32300.itc",                   # 04
        "chr/ch23900.itc",                   # 05
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
        "monster/ch63950.itc",               # 10
        "monster/ch63951.itc",               # 11
        "monster/ch62650.itc",               # 12
        "monster/ch62651.itc",               # 13
        "monster/ch62250.itc",               # 14
        "monster/ch62250.itc",               # 15
        "monster/ch69850.itc",               # 16
        "monster/ch69850.itc",               # 17
        "monster/ch64550.itc",               # 18
        "monster/ch64551.itc",               # 19
        "monster/ch66850.itc",               # 1A
        "monster/ch66851.itc",               # 1B
        "monster/ch76250.itc",               # 1C
        "monster/ch76251.itc",               # 1D
    ))

    DeclNpc(-43049,  3000,    72669,   270,  385,  0x0, 0,   0,   0,   0,   1,   0,   13,  255,  0)
    DeclNpc(-27329,  5000,    98910,   315,  385,  0x0, 0,   1,   0,   0,   2,   0,   14,  255,  0)
    DeclNpc(-34709,  5000,    83029,   270,  385,  0x0, 0,   2,   0,   0,   1,   0,   15,  255,  0)
    DeclNpc(-25319,  5199,    86550,   180,  405,  0x0, 0,   3,   0,   255, 255, 0,   16,  255,  0)
    DeclNpc(-29319,  5000,    79690,   225,  385,  0x0, 0,   4,   0,   0,   3,   0,   17,  255,  0)
    DeclNpc(-16520,  5000,    87919,   45,   385,  0x0, 0,   5,   0,   0,   1,   0,   18,  255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-16030,  21390,   1050,    0x1010000,    "BattleInfo_9D4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-650,    34640,   2009,    0x1010000,    "BattleInfo_938", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-43390,  58440,   3000,    0x1010000,    "BattleInfo_870", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-33100,  91170,   3000,    0x1010000,    "BattleInfo_7D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-50950,  128690,  1800,    0x1010000,    "BattleInfo_738", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-62740,  137000,  -410,    0x1010000,    "BattleInfo_9D4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-67430,  109860,  40,      0x1010000,    "BattleInfo_938", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-90980,  120410,  -1000,   0x1010000,    "BattleInfo_870", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-97230,  131570,  -1000,   0x1010000,    "BattleInfo_7D4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-13090,  34470,   2009,    0x1010000,    "BattleInfo_AE0", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-57690,  66190,   3000,    0x1010000,    "BattleInfo_AE0", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-58220,  121570,  860,     0x1010000,    "BattleInfo_AE0", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-66530,  110660,  840,     0x1850000,    "BattleInfo_A9C", 0,   26,  0xFFFF, 8,  9)

    DeclEvent(0x0000, 0, 20,  -56.0,                 67.5,                  2.0,                   1406.25,               [0.06666666269302368,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   3.733333110809326,     -13.5,                 -0.4000000059604645,   1.0])
    DeclEvent(0x0040, 0, 9,   -66.52999877929688,    110.66000366210938,    0.03999999910593033,   16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   8.31624984741211,      -13.832500457763672,   -0.009999999776482582, 1.0])

    DeclActor(-35330,  3000,    58260,   1200,    -35330,  4000,    58260,   0x007C, 0,  6,  0x0000)
    DeclActor(-96800,  -1000,   121110,  1200,    -96800,  0,       121110,  0x007C, 0,  7,  0x0000)
    DeclActor(-98580,  1000,    157750,  1200,    -98580,  2000,    157750,  0x007C, 0,  8,  0x0000)
    DeclActor(-15380,  5000,    78030,   1200,    -11760,  1000,    74380,   0x007C, 0,  19, 0x0000)
    DeclActor(-30440,  5000,    73410,   1200,    -30440,  6500,    73410,   0x007C, 0,  22, 0x0000)
    DeclActor(-47130,  2040,    113100,  1200,    -47130,  2040,    113100,  0x007C, 0,  10, 0x0000)
    DeclActor(-12680,  10,      9680,    1200,    -12680,  10,      9680,    0x007C, 0,  11, 0x0000)
    DeclActor(-16850,  5000,    89750,   1000,    -16850,  6500,    89750,   0x007C, 0,  23, 0x0000)
    DeclActor(-15850,  5000,    88750,   1000,    -15850,  6500,    88750,   0x007C, 0,  23, 0x0000)

    PlaceName(-1.3899999856948853, 0.0, -33.0, 0x0000, 0x0000, "クロスベル市・タングラム門方面")
    PlaceName(-88.0, 0.0, 178.0, 0x0000, 0x0000, "アルモリカ村方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11

    ScpFunction((
        "Function_0_C6C",          # 00, 0
        "Function_1_C8B",          # 01, 1
        "Function_2_D43",          # 02, 2
        "Function_3_D6E",          # 03, 3
        "Function_4_D99",          # 04, 4
        "Function_5_DEE",          # 05, 5
        "Function_6_154C",         # 06, 6
        "Function_7_1699",         # 07, 7
        "Function_8_17E6",         # 08, 8
        "Function_9_1933",         # 09, 9
        "Function_10_1B74",        # 0A, 10
        "Function_11_1B88",        # 0B, 11
        "Function_12_1B9C",        # 0C, 12
        "Function_13_1BBA",        # 0D, 13
        "Function_14_1C9D",        # 0E, 14
        "Function_15_1DE2",        # 0F, 15
        "Function_16_1ECE",        # 10, 16
        "Function_17_20EF",        # 11, 17
        "Function_18_21E7",        # 12, 18
        "Function_19_22F5",        # 13, 19
        "Function_20_258B",        # 14, 20
        "Function_21_38BF",        # 15, 21
        "Function_22_38D8",        # 16, 22
        "Function_23_3957",        # 17, 23
    ))


    def Function_0_C6C(): pass

    label("Function_0_C6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C8A")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_C6C")

    label("loc_C8A")

    Return()

    # Function_0_C6C end

    def Function_1_C8B(): pass

    label("Function_1_C8B")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_CCB"),
        (1, "loc_CD7"),
        (2, "loc_CE3"),
        (3, "loc_CEF"),
        (4, "loc_CFB"),
        (5, "loc_D07"),
        (6, "loc_D13"),
        (SWITCH_DEFAULT, "loc_D1F"),
    )


    label("loc_CCB")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_CD7")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_CE3")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_CEF")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_CFB")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_D07")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_D13")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_D1F")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_D2B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D42")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D2B")

    label("loc_D42")

    Return()

    # Function_1_C8B end

    def Function_2_D43(): pass

    label("Function_2_D43")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D6D")
    OP_94(0xFE, 0xFFFF9598, 0x18DB2, 0xFFFF9372, 0x175CA, 0x3E8)
    Sleep(300)
    Jump("Function_2_D43")

    label("loc_D6D")

    Return()

    # Function_2_D43 end

    def Function_3_D6E(): pass

    label("Function_3_D6E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D98")
    OP_94(0xFE, 0xFFFF8D82, 0x12A52, 0xFFFF8BC0, 0x14546, 0x3E8)
    Sleep(300)
    Jump("Function_3_D6E")

    label("loc_D98")

    Return()

    # Function_3_D6E end

    def Function_4_D99(): pass

    label("Function_4_D99")

    Call(0, 12)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1E, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB7")
    SetChrFlags(0x1A, 0x8)

    label("loc_DB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DED")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_DED")

    Return()

    # Function_4_D99 end

    def Function_5_DEE(): pass

    label("Function_5_DEE")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x60, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E06")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E06")

    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_133A")
    SetChrFlags(0x20, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jump("loc_134E")

    label("loc_133A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_134E")
    ClearChrFlags(0x20, 0x80)
    ModifyEventFlags(1, 1, 0x80)

    label("loc_134E")

    OP_52(0x20, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x20, 0x100)
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x32, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x34, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x35, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x36, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x37, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_13BA")
    OP_65(0x3, 0x1)

    label("loc_13BA")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -11760, 1000, 74380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1417")
    OP_70(0x0, 0x0)
    Jump("loc_141B")

    label("loc_1417")

    OP_70(0x0, 0x1E)

    label("loc_141B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_142E")
    OP_70(0x1, 0x0)
    Jump("loc_1432")

    label("loc_142E")

    OP_70(0x1, 0x1E)

    label("loc_1432")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1445")
    OP_70(0x2, 0x0)
    Jump("loc_1449")

    label("loc_1445")

    OP_70(0x2, 0x1E)

    label("loc_1449")

    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 2)), scpexpr(EXPR_END)), "loc_14AF")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -47130, 2040, 113100, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)
    Jump("loc_1508")

    label("loc_14AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 3)), scpexpr(EXPR_END)), "loc_1508")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -12680, 10, 9680, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_1508")

    SoundDistance(0x7B, 0xFFFFCD1A, 0x1388, 0x10946, 0x3A98, 0xC350, 0x64, 0x0)
    OP_E1(0xFFFFDE0E, 0x1388, 0x14712)
    OP_E1(0xFFFFEBBA, 0x1388, 0x25B48)
    OP_E1(0xFFFE3EDC, 0x1388, 0x28EC4)
    Return()

    # Function_5_DEE end

    def Function_6_154C(): pass

    label("Function_6_154C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1648")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x40, 1)"), scpexpr(EXPR_END)), "loc_15D1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x40),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1643")

    label("loc_15D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x40),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x40),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1643")

    Jump("loc_168D")

    label("loc_1648")

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

    label("loc_168D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_154C end

    def Function_7_1699(): pass

    label("Function_7_1699")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1795")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x38E, 1)"), scpexpr(EXPR_END)), "loc_171E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1790")

    label("loc_171E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x38E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1790")

    Jump("loc_17DA")

    label("loc_1795")

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

    label("loc_17DA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1699 end

    def Function_8_17E6(): pass

    label("Function_8_17E6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x102, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E2")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x8A, 1)"), scpexpr(EXPR_END)), "loc_186B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x102, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_18DD")

    label("loc_186B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x8A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18DD")

    Jump("loc_1927")

    label("loc_18E2")

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

    label("loc_1927")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_17E6 end

    def Function_9_1933(): pass

    label("Function_9_1933")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 5)), scpexpr(EXPR_END)), "loc_193D")
    Return()

    label("loc_193D")

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

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型の魔獣が徘徊#4Rはいかい#している。\x02",
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
        (1, "loc_1A1F"),
        (SWITCH_DEFAULT, "loc_1A36"),
    )


    label("loc_1A1F")

    Sleep(500)
    OP_90(0x0, -63920, 350, 114420, 45)
    EventEnd(0x5)
    Return()

    label("loc_1A36")

    Battle("BattleInfo_A9C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(-63920, 1350, 114420, 0)
    OP_90(0x0, -63920, 350, 114420, 45)
    OP_90(0x1, -63920, 350, 114420, 45)
    OP_90(0x2, -63920, 350, 114420, 45)
    OP_90(0x3, -63920, 350, 114420, 45)
    OP_90(0x4, -63920, 350, 114420, 45)
    OP_90(0x5, -63920, 350, 114420, 45)
    OP_90(0x6, -63920, 350, 114420, 45)
    OP_90(0x7, -63920, 350, 114420, 45)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1AF8"),
        (1, "loc_1AFB"),
        (SWITCH_DEFAULT, "loc_1AFE"),
    )


    label("loc_1AF8")

    EventEnd(0x5)
    Return()

    label("loc_1AFB")

    OP_B7(0x0)
    Return()

    label("loc_1AFE")

    SetChrFlags(0x1A, 0x8)
    EventBegin(0x1)
    SetChrFlags(0x20, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "手配魔獣を退治した！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x78, 5)
    OP_29(0x1E, 0x4, 0x10)
    OP_29(0x1E, 0x4, 0x2)
    OP_29(0x1E, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_9_1933 end

    def Function_10_1B74(): pass

    label("Function_10_1B74")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 2)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_10_1B74 end

    def Function_11_1B88(): pass

    label("Function_11_1B88")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 3)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_11_1B88 end

    def Function_12_1B9C(): pass

    label("Function_12_1B9C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1BB9")
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)

    label("loc_1BB9")

    Return()

    # Function_12_1B9C end

    def Function_13_1BBA(): pass

    label("Function_13_1BBA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C31")

    #C0012
    ChrTalk(
        0xFE,
        (
            "クロスベル観光ツアーで\x01",
            "こちらにやってきました。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0xFE,
        (
            "皆さんに楽しんで頂けて\x01",
            "私も嬉しいです。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1C99")

    label("loc_1C31")


    #C0014
    ChrTalk(
        0xFE,
        (
            "クロスベルは観光地として\x01",
            "有名な場所ですからね。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0xFE,
        (
            "皆さんも以前から楽しみに\x01",
            "されていたようです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C99")

    TalkEnd(0xFE)
    Return()

    # Function_13_1BBA end

    def Function_14_1C9D(): pass

    label("Function_14_1C9D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D74")

    #C0016
    ChrTalk(
        0xFE,
        (
            "このあたりは\x01",
            "自然が豊かでいいネー。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "近代都市とばかり聞いてたから、\x01",
            "自然はあまりないのかと思ってたヨ。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xFE,
        (
            "そうと知ってれば\x01",
            "奮発#4Rふんぱつ#してオーバルカメラを\x01",
            "買っておいたのにナー。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1DDE")

    label("loc_1D74")


    #C0019
    ChrTalk(
        0xFE,
        (
            "あちこち景色がキレイで、\x01",
            "目移りしちゃうヨ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0xFE,
        (
            "奮発してオーバルカメラを\x01",
            "買っておけばよかったネー。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DDE")

    TalkEnd(0xFE)
    Return()

    # Function_14_1C9D end

    def Function_15_1DE2(): pass

    label("Function_15_1DE2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E71")

    #C0021
    ChrTalk(
        0xFE,
        (
            "向こうに畑があるけど、\x01",
            "何を育ててるのかな？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "くだものかな？\x01",
            "それとも、お野菜かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0xFE,
        "……くだものがいいなー。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1ECA")

    label("loc_1E71")


    #C0024
    ChrTalk(
        0xFE,
        (
            "向こうの畑で育ててるのは、\x01",
            "くだものかな、お野菜かな？\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        "……くだものがいいなー。\x02",
    )

    CloseMessageWindow()

    label("loc_1ECA")

    TalkEnd(0xFE)
    Return()

    # Function_15_1DE2 end

    def Function_16_1ECE(): pass

    label("Function_16_1ECE")

    OP_52(0x0, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    TalkBegin(0xFE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x168), scpexpr(EXPR_ADD), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0xB4), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2D), scpexpr(EXPR_LEQ), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x13B), scpexpr(EXPR_GE), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x195), scpexpr(EXPR_LEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x2A3), scpexpr(EXPR_GE), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1F62")
    Jump("loc_1FAC")

    label("loc_1F62")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1F82")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FAC")

    label("loc_1F82")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1FA2")
    OP_52(0xFE, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1FAC")

    label("loc_1FA2")

    OP_52(0xFE, 0x8, (scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FAC")

    OP_52(0xFE, 0x4, (scpexpr(EXPR_GET_CHR_WORK, 0x0, 0x5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x0, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2070")

    #C0026
    ChrTalk(
        0xFE,
        (
            "……はっ、いかんいかん。\x01",
            "あまりに昼寝に適した陽気に\x01",
            "つい、うとうとしてしまったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "しかし心地いいな。\x01",
            "このまま、寝てしまおうか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_20E7")

    label("loc_2070")


    #C0028
    ChrTalk(
        0xFE,
        (
            "いかんいかん、\x01",
            "せっかくの旅行を\x01",
            "昼寝で潰すわけには……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "しかし、このポカポカ陽気に\x01",
            "逆らえる者など、いまい……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_20E7")

    SetChrSubChip(0xFE, 0x0)
    TalkEnd(0xFE)
    Return()

    # Function_16_1ECE end

    def Function_17_20EF(): pass

    label("Function_17_20EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2166")

    #C0030
    ChrTalk(
        0xFE,
        (
            "きれいに整備された\x01",
            "休憩所だよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "旅慣れてない人にとって\x01",
            "こういうのはありがたいよね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_21E3")

    label("loc_2166")


    #C0032
    ChrTalk(
        0xFE,
        (
            "街道に休憩所があるのは\x01",
            "やっぱりありがたいよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "クロスベル市がきちんと\x01",
            "管理してるんだろうな。\x01",
            "感心するばかりだよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21E3")

    TalkEnd(0xFE)
    Return()

    # Function_17_20EF end

    def Function_18_21E7(): pass

    label("Function_18_21E7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229C")

    #C0034
    ChrTalk(
        0xFE,
        (
            "この箱……\x01",
            "じどうはんばいきって\x01",
            "言うんだって。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "ミラをいれてボタンを押したら\x01",
            "飲み物がでてきたんだよ。\x01",
            "すごいよね～。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xFE,
        "……中に誰か入ってるのかな？\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 5)
    Jump("loc_22F1")

    label("loc_229C")


    #C0037
    ChrTalk(
        0xFE,
        (
            "じどうはんばいきって……\x01",
            "中に誰か入ってるのかなぁ？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0xFE,
        "だったらすごいよね～。\x02",
    )

    CloseMessageWindow()

    label("loc_22F1")

    TalkEnd(0xFE)
    Return()

    # Function_18_21E7 end

    def Function_19_22F5(): pass

    label("Function_19_22F5")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0039
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-14450, 3800, 76450, 1500)
    MoveCamera(12, 27, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(23000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0040
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2586")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 3)), scpexpr(EXPR_END)), "loc_23D2")
    MiniGame(0x6, 0x15, 0xFFFFBFFA, 0x1388, 0x134B6, 0x87, 0xFFFFD210, 0x3E8, 0x1228C)
    Jump("loc_2586")

    label("loc_23D2")

    MiniGame(0x6, 0x16, 0xFFFFBFFA, 0x1388, 0x134B6, 0x87, 0xFFFFD210, 0x3E8, 0x1228C)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2586")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x16, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2586")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-16390, 6500, 79030, 0)
    MoveCamera(25, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21000, 0)
    LoadChrToIndex("apl/ch50162.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -16390, 5000, 79030, 135)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #N0041
    NpcTalk(
        0x0,
        "ロイド",
        (
            "#0011Fな、なんだこりゃ……\x02\x03",

            "#0003F凄い綺麗な魚が釣れたけど……\x01",
            "もしかして特別な魚だったり\x01",
            "するのかな。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -16390, 5000, 79030, 135)
    SetChrPos(0x2, -16390, 5000, 79030, 135)
    SetChrPos(0x3, -16390, 5000, 79030, 135)
    SetChrPos(0x4, -16390, 5000, 79030, 135)
    SetChrPos(0x5, -16390, 5000, 79030, 135)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_37()
    SetScenarioFlags(0x69, 3)

    label("loc_2586")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_19_22F5 end

    def Function_20_258B(): pass

    label("Function_20_258B")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0x14, 0x8)
    SetChrFlags(0x15, 0x8)
    SetChrFlags(0x16, 0x8)
    SetChrFlags(0x17, 0x8)
    SetChrFlags(0x18, 0x8)
    SetChrFlags(0x19, 0x8)
    SetChrFlags(0x1A, 0x8)
    SetChrFlags(0x1B, 0x8)
    SetChrFlags(0x1C, 0x8)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    OP_78(0x3, 0xE)
    SetMapObjFrame(0x3, "light", 0x0, 0x1)
    OP_49()
    SetChrPos(0xE, -41000, 3000, 100200, 190)
    OP_D3(0xE, 0x0, 0xBE, 0x0, 0x0)
    SetMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x3, 0x4)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x79, 0xB4, 0x0, 0x20)
    OP_68(-37910, 7300, 75370, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(30840, 0)
    SetChrPos(0x101, -51380, 3000, 66930, 45)
    SetChrPos(0x104, -53080, 3000, 67090, 45)
    SetChrPos(0x102, -52120, 3000, 66570, 45)
    SetChrPos(0x103, -53840, 3000, 67420, 45)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(-37910, 2400, 75370, 5000)
    Sleep(1500)

    def lambda_26E5():
        OP_95(0xFE, -45660, 3000, 71330, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26E5)

    def lambda_26FF():
        OP_95(0xFE, -47170, 3000, 71910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26FF)
    OP_6F(0x1)
    OP_0D()
    WaitChrThread(0x101, 1)
    Sleep(50)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x104, 1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    Fade(1000)
    OP_68(-40710, 2400, 74790, 0)
    MoveCamera(59, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30460, 0)
    OP_0D()
    Sleep(300)

    #C0042
    ChrTalk(
        0x101,
        "#0005F#5Pここは……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x104,
        "#0300F#5P休憩所、みたいだな。\x02",
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x102,
        "#5P#50Wきゅ、休憩所……？\x02",
    )

    CloseMessageWindow()
    OP_68(-43440, 2400, 73320, 3000)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    def lambda_2807():
        OP_95(0xFE, -48700, 3000, 69060, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2807)
    Sleep(500)

    def lambda_2824():
        OP_95(0xFE, -49800, 3000, 69800, 1000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2824)

    def lambda_283E():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_283E)

    def lambda_284B():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_284B)
    Sound(1176, 255, 100, 0)    #voice#Elie
    Sleep(1000)
    Sound(1272, 255, 100, 1)    #voice#Tio
    WaitChrThread(0x101, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    OP_6F(0x1)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0045
    ChrTalk(
        0x101,
        (
            "#0002F#5P……２人とも、\x01",
            "そこで少し休んで行こうか？\x02\x03",

            "景色も良さそうだし、\x01",
            "一息つくには丁度よさそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        "#0106F#12P#40Wう、うん……そうね。\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#0206F#6P#40W……正直……助かります。\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        "#0300F#5Pそんじゃ、一休みとするかね。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    LoadChrToIndex("chr/ch00002.itc", 0x1E)
    LoadChrToIndex("chr/ch00102.itc", 0x1F)
    LoadChrToIndex("chr/ch00202.itc", 0x20)
    LoadChrToIndex("chr/ch00302.itc", 0x21)
    LoadChrToIndex("apl/ch50092.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0x103, 0x4)
    SetChrFlags(0x104, 0x4)
    SetChrPos(0x101, -19300, 5200, 86600, 180)
    SetChrPos(0x102, -17800, 5200, 83300, 0)
    SetChrPos(0x103, -19300, 5200, 83300, 0)
    SetChrPos(0x104, -17800, 5200, 86600, 180)
    SetChrChipByIndex(0xF, 0x22)
    SetChrSubChip(0xF, 0x3)
    SetChrChipByIndex(0x10, 0x22)
    SetChrSubChip(0x10, 0x3)
    SetChrChipByIndex(0x11, 0x22)
    SetChrSubChip(0x11, 0x3)
    SetChrChipByIndex(0x12, 0x22)
    SetChrSubChip(0x12, 0x3)
    SetChrFlags(0xF, 0x2)
    SetChrFlags(0x10, 0x2)
    SetChrFlags(0x11, 0x2)
    SetChrFlags(0x12, 0x2)
    SetChrFlags(0xF, 0x10)
    SetChrFlags(0x10, 0x10)
    SetChrFlags(0x11, 0x10)
    SetChrFlags(0x12, 0x10)
    ClearChrFlags(0xF, 0x80)
    ClearChrBattleFlags(0xF, 0x8000)
    ClearChrFlags(0x10, 0x80)
    ClearChrBattleFlags(0x10, 0x8000)
    ClearChrFlags(0x11, 0x80)
    ClearChrBattleFlags(0x11, 0x8000)
    ClearChrFlags(0x12, 0x80)
    ClearChrBattleFlags(0x12, 0x8000)
    SetChrPos(0xF, -19300, 5700, 85400, 0)
    SetChrPos(0x10, -17800, 5700, 84500, 0)
    SetChrPos(0x11, -19300, 5700, 84500, 0)
    SetChrPos(0x12, -17800, 5700, 85400, 0)
    FadeToBright(1000, 0)
    OP_68(-73140, 5600, 97250, 0)
    MoveCamera(48, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(43060, 0)
    OP_68(-75530, 5600, 71880, 12000)
    Sleep(10000)
    OP_0D()
    Fade(1000)
    OP_68(-16760, 5300, 86730, 0)
    MoveCamera(49, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(21780, 0)
    SetCameraDistance(20280, 3000)
    OP_6F(0x10)
    OP_0D()

    #C0049
    ChrTalk(
        0x102,
        (
            "#0104F#4P#40W……いい風……\x02\x03",

            "#0102F#30Wふう……\x01",
            "やっと人心地ついた気分ね。\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x103,
        (
            "#0202F#12P#40W……そうですね……\x02\x03",

            "#0203F#30Wなんだかこのまま\x01",
            "寝てしまいそうな感じです……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6C, 7)), scpexpr(EXPR_END)), "loc_2D09")

    #C0051
    ChrTalk(
        0x101,
        (
            "#0009F#5Pはは、お疲れさま。\x02\x03",

            "#0000Fそれにしても……\x01",
            "レモネードを貰ってよかったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x104,
        (
            "#0309F#5Pはは、氷も溶けて\x01",
            "ちょうど飲み頃だったしな。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        (
            "#0204F#12Pはい……\x01",
            "冷え冷えで最高でした。\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#0102F#4Pふふ……\x01",
            "お婆さんには感謝しなくちゃね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D2A")

    label("loc_2D09")


    #C0055
    ChrTalk(
        0x101,
        "#0009F#5Pはは、お疲れさま。\x02",
    )

    CloseMessageWindow()

    label("loc_2D2A")

    OP_57(0x0)
    OP_5A()
    Sleep(100)
    SetChrSubChip(0x101, 0x2)
    Sleep(300)

    #C0056
    ChrTalk(
        0x101,
        (
            "#0000F#5Pそれにしても……\x01",
            "綺麗な田園風景だな……\x02\x03",

            "まるでお伽話に\x01",
            "出てきそうな風景っていうか。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x104, 0x2)
    Sleep(50)
    SetChrSubChip(0x102, 0x1)
    Sleep(50)
    SetChrSubChip(0x103, 0x1)
    Sleep(300)

    #C0057
    ChrTalk(
        0x104,
        (
            "#0305F#5Pそういや……\x01",
            "古い建物跡みたいなのが\x01",
            "あちこちに点在してんだな。\x02\x03",

            "ちょっと珍しい風景だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x102,
        (
            "#0100F#11P朽ちた中世の建物跡が\x01",
            "そのまま残されているみたいね。\x02\x03",

            "#0103F確か……このあたりは昔、\x01",
            "戦場になったという話だけど。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x103, 0x2)
    Sleep(50)
    SetChrSubChip(0x101, 0x0)
    Sleep(50)
    SetChrSubChip(0x104, 0x0)
    Sleep(200)

    #C0059
    ChrTalk(
        0x103,
        "#0205F#6P戦場、ですか？\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x102,
        (
            "#0108F#11Pええ……\x01",
            "エレボニアとカルバードのね。\x02\x03",

            "#0101Fここからすぐ近くに\x01",
            "古戦場跡があるとも聞いたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#0001F#5P古戦場跡……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x104,
        (
            "#0300F#5Pへえ、面白そうじゃねえか。\x02\x03",

            "せっかくだから\x01",
            "ちょっと見に行ってみるか？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)
    SetChrSubChip(0x101, 0x1)
    Sleep(50)
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    #C0063
    ChrTalk(
        0x101,
        "#0006F#6Pいや、それはさすがに……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#0106F#4Pうーん……\x01",
            "ちょっと遠慮したいわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x103,
        (
            "#0211F#12P……ランディさん。\x01",
            "少し空気を読んでください。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x104,
        (
            "#0306F#5Pなんだなんだ。\x01",
            "若いモンがだらしねーな。\x02\x03",

            "#0300F#5Pしかし、クロスベル育ちってのは\x01",
            "そんなに街から出ないもんなのか？\x02\x03",

            "普通、街道くらいは\x01",
            "たまに出歩いたりするだろう？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x101,
        (
            "#0006F#6Pいや……\x01",
            "それが滅多に出ないんだよ。\x02\x03",

            "#0000F基本的には市内だけでも\x01",
            "全ての物が揃っちゃうしなぁ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x102,
        (
            "#0103F#4P元々貿易都市だから\x01",
            "自治州内で自給できなくても\x01",
            "成り立ってきたのよね……\x02\x03",

            "#0100F大抵の移動は鉄道か飛行船……\x02\x03",

            "最近は車やバスもあるから\x01",
            "自分の足でここまで歩くのは\x01",
            "正直、久しぶりかもしれないわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        (
            "#0203F#12P……わたしは、\x01",
            "クロスベル育ちではありませんが……\x02\x03",

            "#0200Fしばらく財団の研究所にいたので\x01",
            "こんなに歩いたのは久しぶりです。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x104,
        (
            "#0303F#5Pなるほどねぇ。\x01",
            "いわゆる文明病ってやつか。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x104, 0x2)
    Sleep(200)

    #C0071
    ChrTalk(
        0x104,
        (
            "#0305F#5Pその割には、ロイドは\x01",
            "あんまり疲れてなさそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x101,
        (
            "#0012F#6P俺は一応、警察学校で\x01",
            "サバイバル訓練を受けてるから……\x02\x03",

            "#0000Fそういうランディこそ\x01",
            "元警備隊なだけはあるみたいだな。\x02\x03",

            "汗一つ、かいてなさそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x104,
        (
            "#0304F#5Pハハッ……\x01",
            "歩き回るのは慣れてるからな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x104, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0074
    ChrTalk(
        0x104,
        "#0305F#5Pおっと、戻ってきたみたいだぜ。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 1700, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    SetChrSubChip(0x101, 0x2)
    SetChrSubChip(0x102, 0x1)
    SetChrSubChip(0x103, 0x1)
    Fade(1000)
    OP_68(-46500, 5000, 80300, 0)
    MoveCamera(45, 17, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(24000, 0)
    OP_68(-46500, 2800, 80300, 7000)
    BeginChrThread(0x13, 1, 0, 21)
    ClearMapObjFlags(0x3, 0x4)

    def lambda_3541():
        OP_95(0xFE, -52200, 3000, 59200, 5000, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3541)
    WaitChrThread(0xE, 1)
    SetChrPos(0xE, -93540, 3000, 51290, 0)
    SetChrFlags(0xE, 0x80)
    ClearChrFlags(0xE, 0x8000)
    ClearMapObjFlags(0x3, 0x1000)
    SetMapObjFlags(0x3, 0x4)
    OP_6F(0x1)
    OP_0D()
    Fade(500)
    OP_68(-16760, 5300, 86730, 0)
    MoveCamera(49, 17, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20280, 0)
    OP_0D()

    #C0075
    ChrTalk(
        0x102,
        "#0108F#2Pクロスベルに戻るバスね……\x02",
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x103,
        (
            "#0208F#11P……一瞬、手を上げて\x01",
            "乗せてもらいそうになりました。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 1700, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)
    SetChrSubChip(0x101, 0x0)
    Sleep(200)

    #C0077
    ChrTalk(
        0x101,
        (
            "#0006F#5Pあれに乗ったら、せっかくここまで\x01",
            "歩いた甲斐が無いってば……\x02\x03",

            "#0000F──とにかく、もう一頑張りだ。\x02\x03",

            "多分、ここから村までは\x01",
            "もうそんなに歩かないと思う。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 0x0)
    Sleep(50)
    SetChrSubChip(0x103, 0x0)
    Sleep(200)

    #C0078
    ChrTalk(
        0x102,
        "#0102F#4Pええ、そうね。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x103,
        "#0203F#12Pふう……了解です。\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#0302F#5Pよーし。\x01",
            "そんじゃあ行くとすっか！\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(20780, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    ClearChrFlags(0x101, 0x4)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    ClearChrFlags(0x102, 0x4)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    ClearChrFlags(0x103, 0x4)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x4)
    SetChrFlags(0xF, 0x80)
    SetChrBattleFlags(0xF, 0x8000)
    SetChrFlags(0x10, 0x80)
    SetChrBattleFlags(0x10, 0x8000)
    SetChrFlags(0x11, 0x80)
    SetChrBattleFlags(0x11, 0x8000)
    SetChrFlags(0x12, 0x80)
    SetChrBattleFlags(0x12, 0x8000)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    OP_68(-22900, 5600, 82800, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(22000, 0)
    SetChrPos(0x0, -21900, 5000, 82800, 225)
    SetChrPos(0x1, -21900, 5000, 82800, 225)
    SetChrPos(0x2, -21900, 5000, 82800, 225)
    SetChrPos(0x3, -21900, 5000, 82800, 225)
    ModifyEventFlags(0, 0, 0x80)
    MiniGame(0x18, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    SetScenarioFlags(0x60, 3)
    EndChrThread(0x13, 0x1)
    ClearMapFlags(0x8000000)
    ClearChrFlags(0x14, 0x8)
    ClearChrFlags(0x15, 0x8)
    ClearChrFlags(0x16, 0x8)
    ClearChrFlags(0x17, 0x8)
    ClearChrFlags(0x18, 0x8)
    ClearChrFlags(0x19, 0x8)
    ClearChrFlags(0x1A, 0x8)
    ClearChrFlags(0x1B, 0x8)
    ClearChrFlags(0x1C, 0x8)
    Call(0, 12)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_20_258B end

    def Function_21_38BF(): pass

    label("Function_21_38BF")

    Sound(465, 0, 100, 0)
    Sleep(3000)
    Sound(467, 0, 100, 0)
    Sleep(2000)
    Sound(470, 0, 100, 0)
    Return()

    # Function_21_38BF end

    def Function_22_38D8(): pass

    label("Function_22_38D8")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0081
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《アルモリカ古道・休憩所》\x01",
            "  ※公共の場では\x01",
            "    マナーを守りましょう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_22_38D8 end

    def Function_23_3957(): pass

    label("Function_23_3957")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x95, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F8E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D14")

    #C0082
    ChrTalk(
        0x101,
        (
            "#0005Fそういえば……\x01",
            "さっきから気になってたんだけど。\x02\x03",

            "#0001Fこれって何だ？\x01",
            "確か警察本部にも\x01",
            "似た物があった気がするけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x104,
        (
            "#0305Fおお、俺も気になってたぜ。\x02\x03",

            "#0300Fいくつかジュースやらコーヒーやらが\x01",
            "並んでるみたいだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x103,
        (
            "#0202Fこれは『導力式自動販売機』です。\x01",
            "お２人は見るのは初めてですか？\x02\x03",

            "#0204Fミラ硬貨を入れると、\x01",
            "その金額に応じた飲料を\x01",
            "買うことが出来ます。\x02\x03",

            "元々エプスタイン財団で開発されたので\x01",
            "あちらの研究施設には\x01",
            "時々置かれているのですが……\x02\x03",

            "#0202Fクロスベルにも実験的に\x01",
            "設置しているようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0085
    ChrTalk(
        0x101,
        "#0000Fへー、そうなんだ……\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x104,
        "#0305Fお嬢は知ってたかよ？\x02",
    )

    CloseMessageWindow()

    #C0087
    ChrTalk(
        0x102,
        (
            "#0104Fううん、私も見るのは初めてね。\x02\x03",

            "#0100Fそれにしても、こんな所まで\x01",
            "エプスタイン財団の装置が\x01",
            "設置されているのね……\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x103,
        (
            "#0203F何でも、有力なスポンサーが\x01",
            "いると聞いていますが……\x02\x03",

            "#0200F……皆さん、利用するときは\x01",
            "硬貨を使ってください。\x01",
            "紙幣には対応していませんから。\x02",
        )
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#0000Fりょ、了解。\x01",
            "（物珍しいし……\x01",
            "  一度くらい使ってみるか。）\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F86")

    label("loc_3D14")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0090
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "導力式の自動販売機がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()

    #C0091
    ChrTalk(
        0x101,
        (
            "#0005Fこれは……確か、硬貨を入れると\x01",
            "飲料が買えるんだったな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3E12")

    #C0092
    ChrTalk(
        0x103,
        (
            "#0200Fええ、エプスタイン財団が開発した\x01",
            "自動販売機です。\x02\x03",

            "クロスベルにも実験的に\x01",
            "設置している物ですね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F4F")

    label("loc_3E12")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3EB4")

    #C0093
    ChrTalk(
        0x102,
        (
            "#0100Fエプスタイン財団が開発した\x01",
            "自動販売機……だったかしら。\x02\x03",

            "ティオちゃんによれば、\x01",
            "財団が実験的に\x01",
            "クロスベルにも設置しているそうね。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3F4F")

    label("loc_3EB4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3F4F")

    #C0094
    ChrTalk(
        0x104,
        (
            "#0300Fエプスタイン財団が開発した\x01",
            "自動販売機……だったか。\x02\x03",

            "ティオすけによりゃあ、\x01",
            "財団が実験的に\x01",
            "クロスベルにも設置しているそうだな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F4F")


    #C0095
    ChrTalk(
        0x101,
        (
            "#0000Fさすがクロスベル……\x01",
            "色んな物があるよなぁ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3F86")

    SetScenarioFlags(0x95, 3)
    Jump("loc_3FA5")

    label("loc_3F8E")

    FadeToDark(300, 0, 100)
    OP_0D()
    OP_AF(0xFA)
    FadeToBright(300, 0)
    OP_0D()

    label("loc_3FA5")

    TalkEnd(0xFF)
    Return()

    # Function_23_3957 end

    SaveToFile()

Try(main)
