from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r0100.bin",                # FileName
        "r0100",                    # MapName
        "r0100",                    # Location
        0x0061,                     # MapIndex
        "ed7201",
        0x00000000,                 # Flags
        ("r0100", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x0E,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 97, 0, 3, 0, 4],
    )

    BuildStringList((
        "r0100",                  # 0
        "ゴールデンアクス",       # 1
        "ゴールデンアクス",       # 2
        "ブレードファング",       # 3
        "ブレードファング",       # 4
        "キラーポポ",             # 5
        "幻獣",                   # 6
        "人形",                   # 7
        "br0100",                 # 8
        "br0100",                 # 9
        "br0100",                 # 10
        "br0100",                 # 11
        "br0100",                 # 12
        "br0100",                 # 13
        "br0100",                 # 14
        "br0100",                 # 15
        "br0100",                 # 16
        "br0100",                 # 17
        "クロスベル市・タングラム門方面",# 18
        "アルモリカ村方面",       # 19
    ))

    ATBonus("ATBonus_55C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_57C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_2C44", 0,   6,   0,   9,   4,   6,   0)
    Sepith("Sepith_2C3C", 5,   0,   9,   0,   3,   2,   5)
    Sepith("Sepith_2C34", 7,   5,   0,   0,   4,   5,   4)
    Sepith("Sepith_2C54", 3,   0,   10,  2,   4,   3,   2)
    Sepith("Sepith_2C5C", 11,  0,   0,   13,  6,   0,   0)
    Sepith("Sepith_2C64", 21,  8,   16,  3,   0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_5BC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_61C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_620", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_624", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_628", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_62C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_630", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_634", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_638", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_59C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_640", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_65C", 0x0000, 60, 6, 45, 6, 1, 40, 0, "br0100", "Sepith_2C44", 30, 45, 25, 0,
        (
            ("ms63900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms63900.dat", "ms63900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms63900.dat", "ms62600.dat", "ms63900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6F8", 0x0000, 60, 6, 45, 6, 1, 50, 0, "br0100", "Sepith_2C3C", 30, 45, 25, 0,
        (
            ("ms62600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms62600.dat", "ms62600.dat", "ms62600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_794", 0x0000, 60, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_2C34", 30, 45, 25, 0,
        (
            ("ms62200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms62200.dat", "ms62200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms62200.dat", "ms69800.dat", "ms62200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_830", 0x0000, 60, 6, 45, 6, 1, 25, 0, "br0100", "Sepith_2C54", 30, 45, 25, 0,
        (
            ("ms69800.dat", "ms69800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms69800.dat", "ms63900.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms69800.dat", "ms69900.dat", "ms62600.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_8CC", 0x0000, 60, 6, 45, 6, 1, 30, 0, "br0100", "Sepith_2C5C", 35, 35, 30, 0,
        (
            ("ms68900.dat", "ms68900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms68900.dat", "ms68900.dat", "ms68900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms68900.dat", "ms68900.dat", "ms68900.dat", "ms68900.dat", 0, 0, 0, 0, "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_968", 0x0000, 82, 6, 60, 8, 1, 40, 0, "br0100", "Sepith_2C64", 40, 35, 25, 0,
        (
            ("ms76201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7450", "ed7453", "ATBonus_55C"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_AD0", 0x0000, 50, 6, 45, 0, 1, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms62200.dat", "ms62200.dat", "ms62200.dat", "ms62200.dat", "ms62200.dat", "ms62200.dat", "ms62200.dat", "ms62200.dat", "MonsterBattlePostion_59C", "MonsterBattlePostion_61C", "ed7451", "ed7453", "ATBonus_55C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A04", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63900.dat", "ms63900.dat", "ms63900.dat", "ms63900.dat", "ms63900.dat", "ms63900.dat", "ms63900.dat", "ms63900.dat", "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7453", "ed7453", "ATBonus_55C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A48", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms76201.dat", "ms76201.dat", "ms76201.dat", "ms76201.dat", 0, 0, 0, 0, "MonsterBattlePostion_5BC", "MonsterBattlePostion_61C", "ed7453", "ed7453", "ATBonus_55C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_A8C", 0x0040, 255, 6, 45, 10, 1, 30, 0, "br0100", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_63C", "MonsterBattlePostion_61C", "ed7454", "ed7453", "ATBonus_57C"),
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
        "monster/ch63950.itc",               # 10
        "monster/ch63951.itc",               # 11
        "monster/ch62650.itc",               # 12
        "monster/ch62651.itc",               # 13
        "monster/ch62250.itc",               # 14
        "monster/ch62250.itc",               # 15
        "monster/ch69850.itc",               # 16
        "monster/ch69850.itc",               # 17
        "monster/ch68950.itc",               # 18
        "monster/ch68951.itc",               # 19
        "monster/ch76250.itc",               # 1A
        "monster/ch76251.itc",               # 1B
    ))

    DeclNpc(-27239,  0,       21010,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-83319,  0,       85529,   270,  484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-27239,  0,       21010,   270,  484,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-83319,  0,       85529,   270,  484,  0x0, 0,   26,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-28000,  500,     97000,   0,    484,  0x0, 0,   20,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    502,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(7430,    10740,   0,       0x1010000,    "BattleInfo_65C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-26680,  23160,   0,       0x1010000,    "BattleInfo_6F8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-47820,  49480,   0,       0x1010000,    "BattleInfo_794", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-82330,  83810,   0,       0x1010000,    "BattleInfo_830", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-68630,  134320,  2000,    0x1010000,    "BattleInfo_65C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-88070,  136430,  2000,    0x1010000,    "BattleInfo_6F8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-28450,  88010,   0,       0x1010000,    "BattleInfo_8CC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(10730,   40540,   -1000,   0x1010000,    "BattleInfo_8CC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(740,     78220,   -1000,   0x1010000,    "BattleInfo_8CC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-16390,  76670,   -1000,   0x1010000,    "BattleInfo_8CC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-11580,  63140,   -1000,   0x1010000,    "BattleInfo_8CC", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-20900,  36230,   0,       0x1010000,    "BattleInfo_968", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-75890,  91810,   0,       0x1010000,    "BattleInfo_968", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0040, 0, 12,  -14.460000038146973,   73.9800033569336,      -2.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   1.8075000047683716,    -9.2475004196167,      0.5,                   1.0])
    DeclEvent(0x0000, 0, 13,  -27.459999084472656,   68.41999816894531,     -0.07000000029802322,  144.0,                 [0.08838831633329391,  0.23570233583450317,   -0.0,                  0.0,                   -0.08838837593793869,  0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.2499999850988388,    0.0,                   8.474675178527832,     -9.654356956481934,    0.017499998211860657,  1.0])

    DeclActor(-84150,  2000,    144490,  1200,    -84150,  3000,    144490,  0x007C, 0,  5,  0x0000)
    DeclActor(3220,    -1000,   92260,   1200,    3220,    0,       92260,   0x007C, 0,  6,  0x0000)
    DeclActor(-28000,  0,       97000,   1200,    -28000,  1000,    97000,   0x007C, 0,  7,  0x0000)
    DeclActor(-27240,  0,       21010,   1200,    -27240,  0,       21010,   0x007C, 0,  8,  0x0000)
    DeclActor(-83320,  0,       85530,   1200,    -83320,  0,       85530,   0x007C, 0,  9,  0x0000)
    DeclActor(2350,    -1000,   40530,   1200,    2350,    -500,    40530,   0x007C, 0,  14, 0x0000)
    DeclActor(-29400,  0,       66620,   2000,    -29400,  1500,    66620,   0x007C, 0,  15, 0x0000)

    PlaceName(-5.0, 0.0, -45.0, 0x0000, 0x0000, "クロスベル市・タングラム門方面")
    PlaceName(-50.0, 0.0, 172.0, 0x0000, 0x0000, "アルモリカ村方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1299, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1250, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 8
    ChipFrameInfo(2500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 11

    ScpFunction((
        "Function_0_BE4",          # 00, 0
        "Function_1_C03",          # 01, 1
        "Function_2_C20",          # 02, 2
        "Function_3_C3C",          # 03, 3
        "Function_4_C40",          # 04, 4
        "Function_5_1723",         # 05, 5
        "Function_6_1874",         # 06, 6
        "Function_7_19C5",         # 07, 7
        "Function_8_1BDC",         # 08, 8
        "Function_9_1F3A",         # 09, 9
        "Function_10_2298",        # 0A, 10
        "Function_11_22B1",        # 0B, 11
        "Function_12_22B5",        # 0C, 12
        "Function_13_2331",        # 0D, 13
        "Function_14_257F",        # 0E, 14
        "Function_15_2BCC",        # 0F, 15
    ))


    def Function_0_BE4(): pass

    label("Function_0_BE4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C02")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_BE4")

    label("loc_C02")

    Return()

    # Function_0_BE4 end

    def Function_1_C03(): pass

    label("Function_1_C03")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C1F")
    OP_A1(0xFE, 0x3E8, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_C03")

    label("loc_C1F")

    Return()

    # Function_1_C03 end

    def Function_2_C20(): pass

    label("Function_2_C20")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C3B")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_2_C20")

    label("loc_C3B")

    Return()

    # Function_2_C20 end

    def Function_3_C3C(): pass

    label("Function_3_C3C")

    Call(0, 10)
    Return()

    # Function_3_C3C end

    def Function_4_C40(): pass

    label("Function_4_C40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_C52")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C52")

    SoundDistance(0x7B, 0x57DA, 0xFFFFFC22, 0xB0AE, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E3(0xD8E, 0xFFFFFC22, 0xD4B2)
    OP_E3(0xFFFFF678, 0xFFFFFC22, 0xFF50)
    OP_E3(0x4EC, 0xFFFFFC22, 0x109C8)
    OP_E3(0xFFFFED5E, 0xFFFFFC18, 0x1195E)
    OP_E3(0xFFFFE700, 0xFFFFFDF8, 0x1451E)
    OP_E3(0xFFFFFE02, 0xFFFFFDF8, 0x1C7B4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_CE3")
    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_D4C")

    label("loc_CE3")

    OP_78(0x3, 0xD)
    ClearMapObjFlags(0x3, 0x4)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8)
    SetChrFlags(0xD, 0x8000)
    SetChrFlags(0xD, 0x1)
    SetChrPos(0xD, -14460, -1000, 73980, 270)
    OP_93(0xD, 0x10E, 0x0)
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1F40), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x1, 0x2, 0x0, -14460, -2000, 73980, 3000, 3000, 90000)

    label("loc_D4C")

    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1316")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0x8C, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_1316")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_140A")
    SetMapObjFrame(0xFF, "obj_shadow0", 0x0, 0x1)
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0x8C, 0x0)
    ClearMapObjFlags(0x7, 0x4)
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
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    ClearMapObjFlags(0x1E, 0x4)
    ClearMapObjFlags(0x1F, 0x4)
    ClearMapObjFlags(0x20, 0x4)
    ClearMapObjFlags(0x21, 0x4)
    ClearMapObjFlags(0x22, 0x4)
    ClearMapObjFlags(0x23, 0x4)
    ClearMapObjFlags(0x24, 0x4)
    ClearMapObjFlags(0x25, 0x4)
    Jump("loc_14C4")

    label("loc_140A")

    SetMapObjFlags(0x7, 0x4)
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
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)
    SetMapObjFlags(0x1E, 0x4)
    SetMapObjFlags(0x1F, 0x4)
    SetMapObjFlags(0x20, 0x4)
    SetMapObjFlags(0x21, 0x4)
    SetMapObjFlags(0x22, 0x4)
    SetMapObjFlags(0x23, 0x4)
    SetMapObjFlags(0x24, 0x4)
    SetMapObjFlags(0x25, 0x4)

    label("loc_14C4")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -29410, 0, 66630, 10000, 2000, 45000)
    SetMapObjFrame(0xFF, "Null_door", 0x2, "close")
    SetBarrier(0x3, 0x0, 0x1)
    OP_66(0x6, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1536")
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x6, 0x1)

    label("loc_1536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_1559")
    SetMapObjFrame(0xFF, "Null_door", 0x2, "open")
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x6, 0x1)

    label("loc_1559")

    SoundDistance(0x7B, 0x57DA, 0xFFFFFC22, 0xB0AE, 0x1388, 0x4E20, 0x64, 0x0)
    OP_E3(0xD8E, 0xFFFFFC22, 0xD4B2)
    OP_E3(0xFFFFF678, 0xFFFFFC22, 0xFF50)
    OP_E3(0x4EC, 0xFFFFFC22, 0x109C8)
    OP_E3(0xFFFFED5E, 0xFFFFFC18, 0x1195E)
    OP_E3(0xFFFFE700, 0xFFFFFDF8, 0x1451E)
    OP_E3(0xFFFFFE02, 0xFFFFFDF8, 0x1C7B4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15D6")
    OP_70(0x0, 0x0)
    Jump("loc_15DA")

    label("loc_15D6")

    OP_70(0x0, 0x1E)

    label("loc_15DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15ED")
    OP_70(0x1, 0x0)
    Jump("loc_15F1")

    label("loc_15ED")

    OP_70(0x1, 0x1E)

    label("loc_15F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1604")
    OP_70(0x2, 0x0)
    Jump("loc_1608")

    label("loc_1604")

    OP_70(0x2, 0x1E)

    label("loc_1608")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1669")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -27240, 0, 21010, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_1669")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_16B5")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -83320, 0, 85530, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_16B5")

    OP_1C(0x0, 0x4, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x5, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    OP_1C(0x0, 0x6, 0x0, 0x32, 0x0, 0xB, 0x0, 0x0)
    ModifyEventFlags(0, 1, 0x80)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x7A, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1722")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C6, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_170E")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_170E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x157, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1722")
    ClearMapObjFlags(0x26, 0x4)
    OP_66(0x5, 0x1)

    label("loc_1722")

    Return()

    # Function_4_C40 end

    def Function_5_1723(): pass

    label("Function_5_1723")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1823")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x40, 1)"), scpexpr(EXPR_END)), "loc_17AC")
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
    SetScenarioFlags(0x1EA, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_181E")

    label("loc_17AC")

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

    label("loc_181E")

    Jump("loc_1868")

    label("loc_1823")

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

    label("loc_1868")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1723 end

    def Function_6_1874(): pass

    label("Function_6_1874")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1974")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_18FD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x1EA, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_196F")

    label("loc_18FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_196F")

    Jump("loc_19B9")

    label("loc_1974")

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

    label("loc_19B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1874 end

    def Function_7_19C5(): pass

    label("Function_7_19C5")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EA, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B96")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AC4")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1A22():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_1A22)

    def lambda_1A3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1A3C)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    #A0007
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
    Battle("BattleInfo_AD0", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1AA5"),
        (2, "loc_1AB4"),
        (1, "loc_1AC1"),
        (SWITCH_DEFAULT, "loc_1AC4"),
    )


    label("loc_1AA5")

    SetScenarioFlags(0x21B, 3)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1AC4")

    label("loc_1AB4")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1AC1")

    OP_B9(0x0)
    Return()

    label("loc_1AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xAC, 1)"), scpexpr(EXPR_END)), "loc_1B21")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xAC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EA, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1B91")

    label("loc_1B21")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xAC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xAC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1B91")

    Jump("loc_1BD0")

    label("loc_1B96")

    FadeToDark(300, 0, 100)

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

    label("loc_1BD0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_19C5 end

    def Function_8_1BDC(): pass

    label("Function_8_1BDC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1D94")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_1D75")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D70")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_1D6D")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1C96():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1C96)
    TurnDirection(0x8, 0x0, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    PlayEffect(0x7, 0x1, 0x8, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_A04", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D68")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D4F")
    Call(1, 5)
    Jump("loc_1D68")

    label("loc_1D4F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1D65")
    Call(1, 4)
    Jump("loc_1D68")

    label("loc_1D65")

    Call(1, 3)

    label("loc_1D68")

    Jump("loc_1D70")

    label("loc_1D6D")

    Call(1, 1)

    label("loc_1D70")

    Jump("loc_1D8B")

    label("loc_1D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_1D8B")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1D8B")

    TalkEnd(0xFF)
    Return()

    label("loc_1D94")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 1)), scpexpr(EXPR_END)), "loc_1F1F")
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F1A")
    ClearScenarioFlags(0x3B, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_1F17")
    ClearScenarioFlags(0x39, 1)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1E40():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1E40)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
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
    Battle("BattleInfo_A48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F12")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1EF9")
    Call(1, 5)
    Jump("loc_1F12")

    label("loc_1EF9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F0F")
    Call(1, 4)
    Jump("loc_1F12")

    label("loc_1F0F")

    Call(1, 3)

    label("loc_1F12")

    Jump("loc_1F1A")

    label("loc_1F17")

    Call(1, 1)

    label("loc_1F1A")

    Jump("loc_1F35")

    label("loc_1F1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 1)), scpexpr(EXPR_END)), "loc_1F35")
    ClearScenarioFlags(0x39, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1F35")

    TalkEnd(0xFF)
    Return()

    # Function_8_1BDC end

    def Function_9_1F3A(): pass

    label("Function_9_1F3A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_20F2")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_20D3")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0015
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20CE")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_20CB")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1FF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1FF4)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0016
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
    Battle("BattleInfo_A04", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_20C6")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20AD")
    Call(1, 5)
    Jump("loc_20C6")

    label("loc_20AD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_20C3")
    Call(1, 4)
    Jump("loc_20C6")

    label("loc_20C3")

    Call(1, 3)

    label("loc_20C6")

    Jump("loc_20CE")

    label("loc_20CB")

    Call(1, 1)

    label("loc_20CE")

    Jump("loc_20E9")

    label("loc_20D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_20E9")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_20E9")

    TalkEnd(0xFF)
    Return()

    label("loc_20F2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3B, 2)), scpexpr(EXPR_END)), "loc_227D")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0017
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2278")
    ClearScenarioFlags(0x3B, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_2275")
    ClearScenarioFlags(0x39, 2)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_219E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_219E)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0018
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
    Battle("BattleInfo_A48", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2270")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2257")
    Call(1, 5)
    Jump("loc_2270")

    label("loc_2257")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_226D")
    Call(1, 4)
    Jump("loc_2270")

    label("loc_226D")

    Call(1, 3)

    label("loc_2270")

    Jump("loc_2278")

    label("loc_2275")

    Call(1, 1)

    label("loc_2278")

    Jump("loc_2293")

    label("loc_227D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x39, 2)), scpexpr(EXPR_END)), "loc_2293")
    ClearScenarioFlags(0x39, 2)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2293")

    TalkEnd(0xFF)
    Return()

    # Function_9_1F3A end

    def Function_10_2298(): pass

    label("Function_10_2298")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22B0")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    label("loc_22B0")

    Return()

    # Function_10_2298 end

    def Function_11_22B1(): pass

    label("Function_11_22B1")

    Call(1, 6)
    Return()

    # Function_11_22B1 end

    def Function_12_22B5(): pass

    label("Function_12_22B5")

    Battle("BattleInfo_A8C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    OP_E2(0x2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22FC")
    OP_90(0x0, -24270, -440, 70780, 270)
    EventEnd(0x5)
    SetChrFlags(0xD, 0x8000)
    Jump("loc_2330")

    label("loc_22FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230F")
    Jump("loc_2330")

    label("loc_230F")

    ModifyEventFlags(0, 0, 0x80)
    SetMapObjFlags(0x3, 0x4)
    SetBarrier(0x2, 0x1, 0x1)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8)
    SetScenarioFlags(0x0, 0)
    ClearScenarioFlags(0x3C, 3)
    EventEnd(0x5)

    label("loc_2330")

    Return()

    # Function_12_22B5 end

    def Function_13_2331(): pass

    label("Function_13_2331")

    EventBegin(0x0)
    Fade(500)
    OP_68(-28370, 1800, 65660, 0)
    MoveCamera(20, 17, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14520, 0)
    SetChrPos(0x101, -29860, 0, 67810, 45)
    SetChrPos(0x102, -28830, 0, 66970, 45)
    SetChrPos(0x103, -27840, -10, 65990, 45)
    SetChrPos(0x104, -30710, 0, 67020, 45)
    SetChrPos(0x109, -29780, 0, 66090, 45)
    SetChrPos(0x105, -28760, 0, 65069, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()

    #C0019
    ChrTalk(
        0x101,
        "#6P#00005F私有地の扉が開いてる……！？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#6P#00105Fこの場所は確か、\x01",
            "アルモリカ村で管理されていて\x01",
            "普段は入れなかったはずじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        "#12P#00200F何者かが鍵を開けたんでしょうか。\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x109,
        "#6P#10103Fでも、何の目的で……？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#6P#00303F……ともかく、また中に魔獣が\x01",
            "入り込んじまってるみてえだ。\x02\x03",

            "#00301F調べるなら気をつけねえとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        "#12P#10302Fフフ、了解。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, -29130, 0, 66400, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_66(0x5, 0x1)
    SetScenarioFlags(0x1C6, 4)
    ModifyEventFlags(0, 1, 0x80)
    EventEnd(0x5)
    Return()

    # Function_13_2331 end

    def Function_14_257F(): pass

    label("Function_14_257F")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_E2(0x2)
    OP_68(2570, -190, 38680, 0)
    MoveCamera(28, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(15480, 0)
    SetChrPos(0x101, 2330, -1000, 38240, 0)
    SetChrPos(0x102, 1000, -1000, 38170, 45)
    SetChrPos(0x103, 3630, -1000, 38170, 0)
    SetChrPos(0x104, 1110, -1000, 36780, 45)
    SetChrPos(0x109, 2290, -1000, 36780, 0)
    SetChrPos(0x105, 3780, -1000, 36780, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    LoadChrToIndex("apl/ch51099.itc", 0x1E)
    SetChrChipByIndex(0xE, 0x1E)
    SetChrSubChip(0xE, 0xA)
    SetChrPos(0xE, 2340, -850, 40020, 0)
    OP_52(0xE, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x1C2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x2)
    SetChrFlags(0xE, 0x10)
    SetChrFlags(0xE, 0x20)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis348.itp")
    FadeToBright(500, 0)
    OP_0D()

    #C0025
    ChrTalk(
        0x101,
        (
            "#12P#00000F２つ目の人形のトランク……\x01",
            "こんなところにあったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#6P#00103F『古の道にて里人が受け継ぎし場所』……\x02\x03",

            "#00100Fアルモリカ村が古道で\x01",
            "代々所有しているこの私有地なら、\x01",
            "確かに当てはまりそうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x105,
        (
            "#12P#10300Fそれじゃあ、ここの扉を\x01",
            "勝手に開けたのは\x01",
            "怪盗Ｂの仕業ってことになるワケか。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x109,
        (
            "#12P#10106Fはあ……\x01",
            "かなり迷惑な人物みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x101,
        "#12P#00000Fとにかく、確認してみよう。\x02",
    )

    CloseMessageWindow()
    Sound(1024, 0, 100, 0)
    OP_74(0x26, 0x1E)
    OP_71(0x26, 0x1, 0x14, 0x1, 0x8)
    OP_A7(0xE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    OP_79(0x26)
    Sleep(1000)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "トランクの裏側には\x01",
            "カードが貼り付けてあった。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    Sleep(500)
    SetMessageWindowPos(-1, 140, -1, -1)
    SetChrName("")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "第三の檻は市外に。\x01",
            "『最も大いなる女神の光を\x01",
            "  その背に浴びし者』を探せ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0032
    ChrTalk(
        0x102,
        (
            "#6P#00105Fこれは、ベルが\x01",
            "『リエーテ』って呼んでいる人形ね。\x02\x03",

            "#00104Fうん、本物に間違いないと思う。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#6P#00306Fカードの方も、\x01",
            "またワケのわかんねえ\x01",
            "謎かけが出てきやがったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x103,
        (
            "#12P#00203F『最も大いなる女神の光』……\x01",
            "この言葉がポイントでしょう。\x02\x03",

            "#00200F『最も大いなる』ということは、\x01",
            "大きさを比べる対象が\x01",
            "いくつか存在するのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#00001Fとにかく探してみるしかないか……\x01",
            "行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#16Iローゼンベルク人形・Ｒ\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x336, 1)
    SetMapObjFlags(0x26, 0x4)
    SetChrFlags(0xE, 0x80)
    OP_D7(0x1E)
    SetChrPos(0x0, 2330, -1000, 38240, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_29(0x7A, 0x1, 0x3)
    SetScenarioFlags(0x157, 2)
    OP_65(0x5, 0x1)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_14_257F end

    def Function_15_2BCC(): pass

    label("Function_15_2BCC")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    Sound(807, 0, 100, 0)
    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "鍵がかかっているようだ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x3)
    Return()

    # Function_15_2BCC end

    SaveToFile()

Try(main)
