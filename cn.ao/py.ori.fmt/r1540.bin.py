from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r1540.bin",                # FileName
        "r1540",                    # MapName
        "r1540",                    # Location
        0x0060,                     # MapIndex
        "ed7200",
        0x00000000,                 # Flags
        ("r1540", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x0D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 96, 0, 4, 0, 5],
    )

    BuildStringList((
        "r1540",                  # 0
        "『海刃』沙克曼",         # 1
        "火焰甲壳虫",             # 2
        "火焰甲壳虫",             # 3
        "强壮巨骨猩",             # 4
        "强壮巨骨猩",             # 5
        "栗子双壳兽",             # 6
        "幻兽",                   # 7
        "br1530",                 # 8
        "br1530",                 # 9
        "br1530",                 # 10
        "br1530",                 # 11
        "br1530",                 # 12
        "br1530",                 # 13
        "br1530",                 # 14
        "br1530",                 # 15
        "br1530",                 # 16
        "br1530",                 # 17
        "克洛斯贝尔市方向",       # 18
        "乌尔斯拉医科大学方向",   # 19
    ))

    ATBonus("ATBonus_94", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_A4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_B4", 0,   0,   18,  2,   2,   0,   2)
    Sepith("Sepith_C4", 0,   9,   3,   0,   4,   4,   4)
    Sepith("Sepith_D4", 3,   10,  0,   8,   3,   0,   0)
    Sepith("Sepith_E4", 9,   5,   0,   3,   0,   3,   4)
    Sepith("Sepith_F4", 23,  23,  23,  23,  23,  23,  23)
    Sepith("Sepith_104", 9,   7,   18,  6,   7,   6,   3)

    MonsterBattlePostion("MonsterBattlePostion_114", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_118", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_11C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_120", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_124", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_128", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_12C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_130", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_134", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_138", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_13C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_140", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_144", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_148", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_14C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_150", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_154", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_158", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_15C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_160", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_164", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_168", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_16C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_170", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_174", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_178", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_17C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_180", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_184", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_188", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_18C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_190", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_194", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1530", "Sepith_B4", 30, 40, 20, 10,
        (
            ("ms65700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65700.dat", "ms65700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65700.dat", "ms65700.dat", "ms65700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms65700.dat", "ms65700.dat", "ms62100.dat", "ms65700.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_25C", 0x0000, 58, 6, 45, 10, 1, 65, 0, "br1530", "Sepith_C4", 45, 20, 20, 15,
        (
            ("ms70800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms70800.dat", "ms70800.dat", "ms70800.dat", "ms61400.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms70800.dat", "ms70700.dat", "ms70800.dat", "ms70800.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms70800.dat", "ms70700.dat", "ms70800.dat", "ms61400.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_324", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1530", "Sepith_D4", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_3EC", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1530", "Sepith_E4", 30, 40, 20, 10,
        (
            ("ms61100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms61100.dat", "ms61100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_4B4", 0x0000, 58, 6, 90, 8, 1, 50, 0, "br1530", "Sepith_F4", 30, 40, 20, 10,
        (
            ("ms66401.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms66401.dat", "ms66401.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms66401.dat", "ms66401.dat", "ms66401.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms66401.dat", "ms66401.dat", "ms66401.dat", "ms66401.dat", 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
        )
    )

    BattleInfo(
        "BattleInfo_57C", 0x0000, 81, 6, 45, 6, 1, 40, 0, "br1530", "Sepith_104", 40, 35, 25, 0,
        (
            ("ms70201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_154", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7450", "ed7453", "ATBonus_94"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_618", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7451", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_65C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6A0", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_114", "MonsterBattlePostion_134", "ed7453", "ed7453", "ATBonus_94"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6E4", 0x0040, 255, 6, 45, 3, 3, 30, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_174", "MonsterBattlePostion_134", "ed7454", "ed7453", "ATBonus_A4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch46000.itc",                   # 00
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

    DeclNpc(-37270,  -449,    -80489,  270,  277,  0x0, 0,   0,   0,   0,   0,   0,   13,  255,  0)
    DeclNpc(-11420,  0,       -14380,  270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-65269,  6300,    17739,   270,  484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(-11420,  0,       -14380,  270,  484,  0x0, 0,   16,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(-65269,  6300,    17739,   270,  484,  0x0, 0,   16,  0,   0,   2,   255, 255, 255,  0)
    DeclNpc(-63069,  6849,    15500,   0,    484,  0x0, 0,   22,  0,   0,   3,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-16149,  -15050,  0,       0x1010000,    "BattleInfo_194", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-29300,  -27360,  0,       0x1010000,    "BattleInfo_25C", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(-27960,  -49820,  0,       0x1010000,    "BattleInfo_324", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(-50100,  -41380,  0,       0x1010000,    "BattleInfo_3EC", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-61400,  7360,    6300,    0x1010000,    "BattleInfo_194", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-70810,  -52410,  -2100,   0x1010000,    "BattleInfo_3EC", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-83770,  -55240,  -2100,   0x1010000,    "BattleInfo_3EC", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-55500,  -81280,  -870,    0x1010000,    "BattleInfo_25C", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(-39400,  -65319,  -700,    0x1010000,    "BattleInfo_194", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-20030,  -84440,  -700,    0x1010000,    "BattleInfo_324", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(-70270,  -36330,  0,       0x1010000,    "BattleInfo_4B4", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-28180,  -13440,  0,       0x1010000,    "BattleInfo_57C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-77050,  -65440,  -2100,   0x1010000,    "BattleInfo_57C", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 16,  -74.0,                 -45.0,                 -2.5,                  441.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.285714626312256,     15.0,                  0.5,                   1.0])
    DeclEvent(0x0000, 0, 18,  2.9100000858306885,    -95.0,                 -1.7000000476837158,   324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.9700000286102295,   7.9166669845581055,    0.3400000035762787,    1.0])

    DeclActor(-27130,  0,       -52750,  1200,    -27130,  1000,    -52750,  0x007C, 0,  6,  0x0000)
    DeclActor(-63070,  6350,    15500,   1200,    -63070,  7350,    15500,   0x007C, 0,  7,  0x0000)
    DeclActor(-36340,  -700,    -65120,  1200,    -36340,  300,     -65120,  0x007C, 0,  8,  0x0000)
    DeclActor(-11420,  0,       -14380,  1200,    -11420,  0,       -14380,  0x007C, 0,  9,  0x0000)
    DeclActor(-65269,  6300,    17740,   1200,    -65269,  6300,    17740,   0x007C, 0,  10, 0x0000)
    DeclActor(-37240,  -410,    -79670,  1200,    -42890,  -2800,   -78670,  0x007C, 0,  15, 0x0000)
    DeclActor(-2450,   -700,    -92010,  1500,    -2450,   1000,    -92010,  0x007C, 0,  24, 0x0000)

    PlaceName(27.450000762939453, 0.0, 1.25, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(26.0, 0.0, -92.0, 0x0000, 0x0000, "乌尔斯拉医科大学方向")

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
        "Function_0_CDC",          # 00, 0
        "Function_1_D94",          # 01, 1
        "Function_2_DB3",          # 02, 2
        "Function_3_DD2",          # 03, 3
        "Function_4_DF1",          # 04, 4
        "Function_5_1378",         # 05, 5
        "Function_6_19A3",         # 06, 6
        "Function_7_1AFC",         # 07, 7
        "Function_8_1CFA",         # 08, 8
        "Function_9_1E35",         # 09, 9
        "Function_10_2159",        # 0A, 10
        "Function_11_247D",        # 0B, 11
        "Function_12_24AC",        # 0C, 12
        "Function_13_24B0",        # 0D, 13
        "Function_14_2F99",        # 0E, 14
        "Function_15_3046",        # 0F, 15
        "Function_16_32FA",        # 10, 16
        "Function_17_36D5",        # 11, 17
        "Function_18_3BD6",        # 12, 18
        "Function_19_3D1B",        # 13, 19
        "Function_20_42A5",        # 14, 20
        "Function_21_432E",        # 15, 21
        "Function_22_4524",        # 16, 22
        "Function_23_458B",        # 17, 23
        "Function_24_45CD",        # 18, 24
    ))


    def Function_0_CDC(): pass

    label("Function_0_CDC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_D1C"),
        (1, "loc_D28"),
        (2, "loc_D34"),
        (3, "loc_D40"),
        (4, "loc_D4C"),
        (5, "loc_D58"),
        (6, "loc_D64"),
        (SWITCH_DEFAULT, "loc_D70"),
    )


    label("loc_D1C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D28")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D34")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D40")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D4C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D58")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D64")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D70")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D7C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_D93")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D7C")

    label("loc_D93")

    Return()

    # Function_0_CDC end

    def Function_1_D94(): pass

    label("Function_1_D94")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DB2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_D94")

    label("loc_DB2")

    Return()

    # Function_1_D94 end

    def Function_2_DB3(): pass

    label("Function_2_DB3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DD1")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_DB3")

    label("loc_DD1")

    Return()

    # Function_2_DB3 end

    def Function_3_DD2(): pass

    label("Function_3_DD2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DF0")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_DD2")

    label("loc_DF0")

    Return()

    # Function_3_DD2 end

    def Function_4_DF1(): pass

    label("Function_4_DF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_E0B")
    SetChrPos(0x8, -37300, -440, -76070, 270)

    label("loc_E0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E1E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_EB8")

    label("loc_E1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E3A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_E35")
    SetChrFlags(0x8, 0x80)

    label("loc_E35")

    Jump("loc_EB8")

    label("loc_E3A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E48")
    Jump("loc_EB8")

    label("loc_E48")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E56")
    Jump("loc_EB8")

    label("loc_E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E64")
    Jump("loc_EB8")

    label("loc_E64")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E72")
    Jump("loc_EB8")

    label("loc_E72")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E80")
    Jump("loc_EB8")

    label("loc_E80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E8E")
    Jump("loc_EB8")

    label("loc_E8E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_E9C")
    Jump("loc_EB8")

    label("loc_E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EAA")
    Jump("loc_EB8")

    label("loc_EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_EB8")
    SetChrFlags(0x8, 0x80)

    label("loc_EB8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_EC7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)

    label("loc_EC7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1374")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F5D")
    SetScenarioFlags(0x38, 0)

    label("loc_F5D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F73")
    SetScenarioFlags(0x38, 1)

    label("loc_F73")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F89")
    SetScenarioFlags(0x38, 2)

    label("loc_F89")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F9F")
    SetScenarioFlags(0x38, 3)

    label("loc_F9F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FB5")
    SetScenarioFlags(0x38, 4)

    label("loc_FB5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FCB")
    SetScenarioFlags(0x38, 5)

    label("loc_FCB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FE1")
    SetScenarioFlags(0x38, 6)

    label("loc_FE1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF7")
    SetScenarioFlags(0x38, 7)

    label("loc_FF7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_100D")
    SetScenarioFlags(0x39, 0)

    label("loc_100D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1023")
    SetScenarioFlags(0x39, 1)

    label("loc_1023")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1039")
    SetScenarioFlags(0x39, 2)

    label("loc_1039")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_104F")
    SetScenarioFlags(0x39, 3)

    label("loc_104F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1065")
    SetScenarioFlags(0x39, 4)

    label("loc_1065")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_107B")
    SetScenarioFlags(0x39, 5)

    label("loc_107B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1091")
    SetScenarioFlags(0x39, 6)

    label("loc_1091")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A7")
    SetScenarioFlags(0x39, 7)

    label("loc_10A7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10BD")
    SetScenarioFlags(0x3A, 0)

    label("loc_10BD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D3")
    SetScenarioFlags(0x3A, 1)

    label("loc_10D3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E9")
    SetScenarioFlags(0x3A, 2)

    label("loc_10E9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10FF")
    SetScenarioFlags(0x3A, 3)

    label("loc_10FF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1115")
    SetScenarioFlags(0x3A, 4)

    label("loc_1115")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_112B")
    SetScenarioFlags(0x3A, 5)

    label("loc_112B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1141")
    SetScenarioFlags(0x3A, 6)

    label("loc_1141")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1157")
    SetScenarioFlags(0x3A, 7)

    label("loc_1157")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116D")
    SetScenarioFlags(0x3B, 0)

    label("loc_116D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1183")
    SetScenarioFlags(0x3B, 1)

    label("loc_1183")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1199")
    SetScenarioFlags(0x3B, 2)

    label("loc_1199")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11AF")
    SetScenarioFlags(0x3B, 3)

    label("loc_11AF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11C5")
    SetScenarioFlags(0x3B, 4)

    label("loc_11C5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11DB")
    SetScenarioFlags(0x3B, 5)

    label("loc_11DB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11F1")
    SetScenarioFlags(0x3B, 6)

    label("loc_11F1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1207")
    SetScenarioFlags(0x3B, 7)

    label("loc_1207")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_121D")
    SetScenarioFlags(0x3D, 5)

    label("loc_121D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1233")
    SetScenarioFlags(0x3D, 6)

    label("loc_1233")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1249")
    SetScenarioFlags(0x3D, 7)

    label("loc_1249")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1284")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1374")

    label("loc_1284")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12A7")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1374")

    label("loc_12A7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12CA")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1374")

    label("loc_12CA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12ED")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1374")

    label("loc_12ED")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1310")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1374")

    label("loc_1310")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1333")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1374")

    label("loc_1333")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1356")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1374")

    label("loc_1356")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1374")
    SetScenarioFlags(0x3C, 7)

    label("loc_1374")

    Call(0, 11)
    Return()

    # Function_4_DF1 end

    def Function_5_1378(): pass

    label("Function_5_1378")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_138A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_138A")

    SoundDistance(0x7B, 0xFFFF4174, 0xFFFFFACE, 0xFFFEFDA4, 0x1770, 0xC350, 0x64, 0x0)
    OP_52(0x1A, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_172C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xBE, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_172C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_1793")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xBE, 0x0)
    SetMapObjFrame(0xFF, "allback", 0x2, "gray")
    ClearMapObjFlags(0x3, 0x4)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    Jump("loc_17C3")

    label("loc_1793")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)

    label("loc_17C3")

    SetMapObjFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17DD")
    ClearMapObjFlags(0x10, 0x4)

    label("loc_17DD")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -42890, -2800, -78670, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1841")
    OP_66(0x5, 0x1)

    label("loc_1841")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1854")
    OP_70(0x0, 0x0)
    Jump("loc_1858")

    label("loc_1854")

    OP_70(0x0, 0x1E)

    label("loc_1858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_186B")
    OP_70(0x1, 0x0)
    Jump("loc_186F")

    label("loc_186B")

    OP_70(0x1, 0x1E)

    label("loc_186F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1882")
    OP_70(0x2, 0x0)
    Jump("loc_1886")

    label("loc_1882")

    OP_70(0x2, 0x1E)

    label("loc_1886")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18E7")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -11420, 0, -14380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_18E7")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1933")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -65269, 6300, 17740, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1933")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_194B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_194B")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1963")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1963")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1976")
    OP_1B(0x1, 0x0, 0x14)

    label("loc_1976")

    OP_1C(0x0, 0xB, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xC, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xD, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xE, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    Return()

    # Function_5_1378 end

    def Function_6_19A3(): pass

    label("Function_6_19A3")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ACD")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 60)
    AddSepith(0x1, 60)
    AddSepith(0x2, 60)
    AddSepith(0x3, 60)
    AddSepith(0x4, 60)
    AddSepith(0x5, 60)
    AddSepith(0x6, 60)

    #A0001
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
    SetScenarioFlags(0x1EC, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1AEA")

    label("loc_1ACD")


    #A0002
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

    label("loc_1AEA")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_19A3 end

    def Function_7_1AFC(): pass

    label("Function_7_1AFC")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CBC")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BF9")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1B59():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B59)

    def lambda_1B73():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1B73)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    #A0003
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
    Battle("BattleInfo_618", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1BDA"),
        (2, "loc_1BE9"),
        (1, "loc_1BF6"),
        (SWITCH_DEFAULT, "loc_1BF9"),
    )


    label("loc_1BDA")

    SetScenarioFlags(0x216, 6)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1BF9")

    label("loc_1BE9")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1BF6")

    OP_B9(0x0)
    Return()

    label("loc_1BF9")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('幸运', 1)"), scpexpr(EXPR_END)), "loc_1C50")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1CB7")

    label("loc_1C50")

    FadeToDark(300, 0, 100)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1CB7")

    Jump("loc_1CEE")

    label("loc_1CBC")

    FadeToDark(300, 0, 100)

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

    label("loc_1CEE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1AFC end

    def Function_8_1CFA(): pass

    label("Function_8_1CFA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DEC")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药', 1)"), scpexpr(EXPR_END)), "loc_1D7D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1DE7")

    label("loc_1D7D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1DE7")

    Jump("loc_1E29")

    label("loc_1DEC")

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

    label("loc_1E29")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1CFA end

    def Function_9_1E35(): pass

    label("Function_9_1E35")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1FCE")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_1FB4")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FAF")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_1FAC")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1ED7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1ED7)
    TurnDirection(0x9, 0x0, 0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    PlayEffect(0x7, 0x1, 0x9, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_65C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FA7")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1F8E")
    Call(1, 5)
    Jump("loc_1FA7")

    label("loc_1F8E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FA4")
    Call(1, 4)
    Jump("loc_1FA7")

    label("loc_1FA4")

    Call(1, 3)

    label("loc_1FA7")

    Jump("loc_1FAF")

    label("loc_1FAC")

    Call(1, 1)

    label("loc_1FAF")

    Jump("loc_1FCA")

    label("loc_1FB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_1FCA")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_1FCA")

    TalkEnd(0xFF)
    Return()

    label("loc_1FCE")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_213F")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_213A")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2137")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2062():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2062)
    TurnDirection(0xB, 0x0, 0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    PlayEffect(0x7, 0x1, 0xB, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_6A0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2132")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2119")
    Call(1, 5)
    Jump("loc_2132")

    label("loc_2119")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_212F")
    Call(1, 4)
    Jump("loc_2132")

    label("loc_212F")

    Call(1, 3)

    label("loc_2132")

    Jump("loc_213A")

    label("loc_2137")

    Call(1, 1)

    label("loc_213A")

    Jump("loc_2155")

    label("loc_213F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2155")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2155")

    TalkEnd(0xFF)
    Return()

    # Function_9_1E35 end

    def Function_10_2159(): pass

    label("Function_10_2159")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_22F2")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_22D8")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22D3")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_22D0")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_21FB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_21FB)
    TurnDirection(0xA, 0x0, 0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    PlayEffect(0x7, 0x1, 0xA, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_65C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22CB")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22B2")
    Call(1, 5)
    Jump("loc_22CB")

    label("loc_22B2")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_22C8")
    Call(1, 4)
    Jump("loc_22CB")

    label("loc_22C8")

    Call(1, 3)

    label("loc_22CB")

    Jump("loc_22D3")

    label("loc_22D0")

    Call(1, 1)

    label("loc_22D3")

    Jump("loc_22EE")

    label("loc_22D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_22EE")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_22EE")

    TalkEnd(0xFF)
    Return()

    label("loc_22F2")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_2463")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "似乎埋藏着什么。\x01",
            "要挖掘吗？\x07\x00\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_245E")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_245B")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2386():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2386)
    TurnDirection(0xC, 0x0, 0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    PlayEffect(0x7, 0x1, 0xC, 0x1, 0, 0, 0, 0, 0, 0, 300, 300, 300, 0xFF, 0, 0, 0, 0)
    Sound(601, 0, 100, 0)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_6A0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2456")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_243D")
    Call(1, 5)
    Jump("loc_2456")

    label("loc_243D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2453")
    Call(1, 4)
    Jump("loc_2456")

    label("loc_2453")

    Call(1, 3)

    label("loc_2456")

    Jump("loc_245E")

    label("loc_245B")

    Call(1, 1)

    label("loc_245E")

    Jump("loc_2479")

    label("loc_2463")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_2479")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2479")

    TalkEnd(0xFF)
    Return()

    # Function_10_2159 end

    def Function_11_247D(): pass

    label("Function_11_247D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2495")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    label("loc_2495")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 0)), scpexpr(EXPR_END)), "loc_24A6")
    ClearScenarioFlags(0x3C, 0)
    Jump("loc_24AB")

    label("loc_24A6")

    SetChrFlags(0x19, 0x80)

    label("loc_24AB")

    Return()

    # Function_11_247D end

    def Function_12_24AC(): pass

    label("Function_12_24AC")

    Call(1, 6)
    Return()

    # Function_12_24AC end

    def Function_13_24B0(): pass

    label("Function_13_24B0")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24C8")
    SetScenarioFlags(0x0, 1)

    label("loc_24C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_24D4")
    SetScenarioFlags(0x0, 1)

    label("loc_24D4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_26FE")
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0018
    ChrTalk(
        0x8,
        (
            "哇哈哈，\x01",
            "你是钓公师团的人吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "我是沙克曼，\x01",
            "『海刃』沙克曼。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00005F害人……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0021
    ChrTalk(
        0x8,
        (
            "不对！是海刃！海刃！！\x01",
            "海中的利刃！海刃！！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "记住了吧？那我们就以\x01",
            "『突然死亡制』为规则开始爆钓比赛吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00006F好、好的……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x8,
        (
            "哦，差点忘了。\x01",
            "在那之前，还有个条件。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "从外表也许看不出，但我可是\x01",
            "四天王之中技巧最高超的一人。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "要想挑战我，\x01",
            "你必须先钓到几种\x01",
            "指定的鱼类。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "如果想知道具体种类，\x01",
            "就去市里问塞拉姆吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00012F明、明白了……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 5)
    OP_93(0x8, 0x10E, 0x0)

    label("loc_26FE")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2708")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F95")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_274C")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "进行爆钓比赛\x01",      # 1
            "放弃\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_2756")

    label("loc_274C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2756")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D4B")
    TurnDirection(0x8, 0x0, 0)
    Call(0, 14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2BE8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28A5")

    #C0029
    ChrTalk(
        0x8,
        (
            "哦，那就给我看看\x01",
            "你的钓鱼手册吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0030
    ChrTalk(
        0x8,
        (
            "哇哈哈，有点本事啊。\x01",
            "完全满足条件了！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "好，那我们就\x01",
            "赶快开始比赛吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "之前就说过了，\x01",
            "爆钓比赛规则为\x01",
            "『突然死亡制』！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "我们轮流下竿，\x01\x07\x02",

            "先出现失误的一方\x07\x00",
            "就是失败者。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 6)
    Jump("loc_290D")

    label("loc_28A5")


    #C0034
    ChrTalk(
        0x8,
        (
            "哇哈哈，要以『突然死亡制』\x01",
            "为规则和我比赛吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "我们轮流下竿，\x01\x07\x02",

            "先出现失误的一方\x07\x00",
            "就是失败者。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_290D")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要以『突然死亡制』为规则\x01",
            "向『海刃』沙克曼挑战吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "挑战\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2998"),
        (1, "loc_2B9C"),
        (SWITCH_DEFAULT, "loc_2BE3"),
    )


    label("loc_2998")


    #C0037
    ChrTalk(
        0x8,
        (
            "哇哈哈，\x01",
            "那就赶快开始吧！\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_E2(0x2)
    ClearMapFlags(0x1)
    OP_68(-40100, -1120, -77350, 0)
    MoveCamera(29, 40, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x0, -38000, -700, -95000, 182)
    OP_31(0x1)
    SetChrPos(0x101, -37300, -440, -76070, 270)
    OP_93(0x8, 0x10E, 0x1F4)
    FadeToBright(300, 0)
    OP_0D()
    OP_DE("apl/ch51003.itc")
    MiniGame(0x7, 0x1, 0x8, 0xFFFF5F92, 0xFFFFF510, 0xFFFED0EA, 0xFFFF5EFC, 0xFFFFF510, 0xFFFEC370)
    SetChrPos(0x0, -53410, 0, 15290, 226)
    OP_31(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AD8")
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_68(-34670, -440, -78930, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetChrPos(0x101, -35530, -450, -80410, 270)
    OP_93(0xFE, 0x5A, 0x0)
    Sleep(500)
    Call(0, 21)
    Return()

    label("loc_2AD8")

    OP_68(-36530, -1120, -76470, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -37300, -440, -76070, 180)
    OP_93(0xFE, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B37")
    Call(0, 22)
    Jump("loc_2B5B")

    label("loc_2B37")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B4A")
    Jump("loc_2B5B")

    label("loc_2B4A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5B")
    Call(0, 23)

    label("loc_2B5B")

    FadeToDark(300, 0, -1)
    OP_0D()
    OP_93(0x8, 0x10E, 0x1F4)
    OP_4C(0x8, 0xFF)
    SetChrPos(0x0, -37300, -440, -76070, 180)
    OP_31(0x1)
    SetMapFlags(0x1)
    OP_69(0xFF, 0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_2BE3")

    label("loc_2B9C")


    #C0038
    ChrTalk(
        0x8,
        "嗯？这样啊……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "算了，既然你不想比，\x01",
            "那也没办法。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    Jump("loc_2BE3")

    label("loc_2BE3")

    Jump("loc_2D46")

    label("loc_2BE8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2CA9")

    #C0040
    ChrTalk(
        0x8,
        (
            "哦，那就给我看看\x01",
            "你的钓鱼手册吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0041
    ChrTalk(
        0x8,
        (
            "嗯……我承认你努力过了，\x01",
            "但还是有些不足啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "把我特别喜欢的几种\x01",
            "指定鱼类全部钓到\x01",
            "之后再来吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    Jump("loc_2D46")

    label("loc_2CA9")


    #C0043
    ChrTalk(
        0x8,
        (
            "哦，那就给我看看\x01",
            "你的钓鱼手册吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x8)

    #C0044
    ChrTalk(
        0x8,
        (
            "这算什么？\x01",
            "根本没有成果啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "把我特别喜欢的几种\x01",
            "指定鱼类全部钓到\x01",
            "之后再来吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)

    label("loc_2D46")

    Jump("loc_2F90")

    label("loc_2D4B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F90")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D6E")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2D6E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2D7C")
    Jump("loc_2F90")

    label("loc_2D7C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2DB1")

    #C0046
    ChrTalk(
        0x8,
        (
            "我是沙克曼～\x01",
            "热爱大海～技术高超～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2DB1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_2DE6")

    #C0047
    ChrTalk(
        0x8,
        (
            "在雨水的击打下，\x01",
            "男人会变得更强～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2DE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_2E1D")

    #C0048
    ChrTalk(
        0x8,
        (
            "所有人类～都是诞生于\x01",
            "大海的兄弟们～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2E1D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_2E5A")

    #C0049
    ChrTalk(
        0x8,
        (
            "大海男儿啊～\x01",
            "沉默～只用背影来述说一切吧～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2E5A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_2EAA")

    #C0050
    ChrTalk(
        0x8,
        (
            "扬帆起航～\x01",
            "追逐梦想～\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "我是把整个人生\x01",
            "献给梦想的男子汉～\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2EAA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_2EF3")

    #C0052
    ChrTalk(
        0x8,
        (
            "我是沙克曼～\x01",
            "扬帆起航～\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "去征服这名为世界的巨浪～\x02",
    )

    CloseMessageWindow()
    Jump("loc_2F90")

    label("loc_2EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_2F79")

    #C0054
    ChrTalk(
        0x8,
        (
            "我是沙克曼～\x01",
            "大海男儿～\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2F74")

    #C0055
    ChrTalk(
        0x101,
        (
            "#00003F（在这里似乎可以钓到鱼……\x01",
            "  但已经有别人先来了，还是算了吧。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2F74")

    Jump("loc_2F90")

    label("loc_2F79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_2F87")
    Jump("loc_2F90")

    label("loc_2F87")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_2F90")

    label("loc_2F90")

    Jump("loc_2708")

    label("loc_2F95")

    TalkEnd(0xFE)
    Return()

    # Function_13_24B0 end

    def Function_14_2F99(): pass

    label("Function_14_2F99")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FBE")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FBE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FD9")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FF4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_300F")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_300F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_302A")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_302A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3045")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3045")

    Return()

    # Function_14_2F99 end

    def Function_15_3046(): pass

    label("Function_15_3046")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0056
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(-42270, 170, -79360, 1500)
    MoveCamera(45, 28, 0, 1500)
    OP_6E(510, 1500)
    SetCameraDistance(19500, 1500)
    Sleep(1000)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F5")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_3120")
    MiniGame(0x6, 0xF, 0xFFFF6E88, 0xFFFFFE66, 0xFFFEC8CA, 0x10E, 0xFFFF5876, 0xFFFFF510, 0xFFFECCB2)
    Jump("loc_32F5")

    label("loc_3120")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    MiniGame(0x6, 0x10, 0xFFFF6E88, 0xFFFFFE66, 0xFFFEC8CA, 0x10E, 0xFFFF5876, 0xFFFFF510, 0xFFFECCB2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32F5")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_32F5")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(-36950, 170, -79060, 0)
    MoveCamera(29, 26, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(16720, 0)
    LoadChrToIndex("apl/ch50163.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, -37240, -410, -79670, 270)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    OP_0D()
    FadeToBright(1000, 0)
    OP_0D()

    #N0058
    NpcTalk(
        0x0,
        "罗伊德",
        (
            "#00011F哇、哇哇……\x01",
            "这条鱼好像很凶猛啊。\x02\x03",

            "#00003F看上去和食人鱼很相似……\x01",
            "莫非是一种\x01",
            "特别的鱼类吗？\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, -37240, -410, -79670, 270)
    SetChrPos(0x2, -37240, -410, -79670, 270)
    SetChrPos(0x3, -37240, -410, -79670, 270)
    SetChrPos(0x4, -37240, -410, -79670, 270)
    SetChrPos(0x5, -37240, -410, -79670, 270)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D7(0x1E)
    OP_37()
    SetScenarioFlags(0x18B, 2)

    label("loc_32F5")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_3046 end

    def Function_16_32FA(): pass

    label("Function_16_32FA")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch03150.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    LoadEffect(0x0, "battle\\cr036301.eff")
    ClearChrFlags(0xE, 0x80)
    OP_78(0xF, 0xE)
    OP_49()
    ClearMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0xF, 0x1000)
    OP_71(0xF, 0xA, 0x32, 0x1, 0x20)
    OP_75(0xF, 0x1, 0x0)
    SetMapObjFrame(0xFF, "tree", 0x0, 0x1)
    SetMapObjFrame(0xFF, "wood01", 0x0, 0x1)
    SetMapObjFrame(0xFF, "sunlight", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35C4")
    SetChrPos(0x101, -77200, -2100, -46800, 180)
    SetChrPos(0x105, -75950, -2100, -46300, 180)
    SetChrPos(0x107, -77650, -2100, -45600, 180)
    SetChrPos(0xE, -76750, -2100, -56600, 0)
    OP_68(-77200, -1500, -51000, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30500, 0)
    OP_68(-77200, -1500, -52150, 3000)
    MoveCamera(45, 30, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(28000, 3000)

    def lambda_3446():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3446)
    Sleep(50)

    def lambda_345E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_345E)
    Sleep(50)

    def lambda_3476():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3476)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    Sound(919, 0, 100, 0)
    BlurSwitch(0x3E8, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    PlayEffect(0x0, 0xFF, 0xE, 0x0, 0, 1500, 0, 0, 0, 0, 3000, 3000, 3000, 0xFF, 0, 0, 0, 1000)
    Sleep(100)
    SetChrSubChip(0x107, 0x5)
    Sleep(900)
    OP_75(0xF, 0x2, 0x3E8)
    CancelBlur(1000)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x20)
    SetChrSubChip(0x107, 0x0)
    OP_0D()
    OP_71(0xF, 0x48, 0x5B, 0x1, 0x8)
    OP_79(0xF)

    def lambda_357C():
        OP_9B(0x1, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_357C)
    OP_74(0xF, 0xA)
    Sound(842, 0, 100, 0)
    OP_71(0xF, 0x5B, 0x5F, 0x1, 0x8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetCameraDistance(23500, 200)
    Sleep(200)
    Jump("loc_365F")

    label("loc_35C4")

    SetChrPos(0x101, -77200, -2100, -49800, 180)
    SetChrPos(0x105, -75950, -2100, -49300, 180)
    SetChrPos(0x107, -77650, -2100, -48600, 180)
    SetChrPos(0xE, -76750, -2100, -56600, 0)
    OP_75(0xF, 0x2, 0x0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x20)
    SetChrSubChip(0x107, 0x0)
    OP_68(-77200, -1500, -52150, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(28000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_365F")

    Battle("BattleInfo_6E4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    SetMapObjFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_36D1")
    SetScenarioFlags(0x1A9, 7)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    OP_49()
    OP_37()
    SetChrPos(0x0, -73500, -600, -40000, 0)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Jump("loc_36D4")

    label("loc_36D1")

    Call(0, 17)

    label("loc_36D4")

    Return()

    # Function_16_32FA end

    def Function_17_36D5(): pass

    label("Function_17_36D5")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch03150.itc", 0x1F)
    LoadChrToIndex("chr/ch02750.itc", 0x20)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0x1F)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x20)
    SetChrSubChip(0x107, 0x0)
    SetChrPos(0x101, -76500, -2100, -55450, 180)
    SetChrPos(0x105, -75050, -2100, -53150, 180)
    SetChrPos(0x107, -77050, -2100, -52500, 180)
    OP_68(-76500, -1100, -56000, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20500, 0)
    OP_68(-76450, -1100, -54000, 3000)
    SetCameraDistance(19500, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x5)
    OP_0D()

    def lambda_37BD():
        OP_92(0x101, 0xFFFED55E, 0xFFFF2D10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_37BD)
    Sleep(50)

    def lambda_37D3():
        OP_92(0x105, 0xFFFED55E, 0xFFFF2D10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_37D3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    SetChrSubChip(0x107, 0x5)

    #C0059
    ChrTalk(
        0x101,
        (
            "#00006F#12P呼……好突然啊。\x02\x03",

            "#00013F话说回来，在这种状况下，\x01",
            "往来于城市和医院之间\x01",
            "的巴士还能正常运行吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x105,
        (
            "#10403F#5P恐怕很难吧。\x02\x03",

            "#10408F如果是国防军的装甲车，\x01",
            "倒还有硬冲过去的可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00006F#12P这就是说，\x01",
            "如今的状况也许已经对\x01",
            "市民的身体健康造成威胁了……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C嗯，真是不幸。\x02\x03",

            "乌尔斯拉要是看到如今这样的情景，\x01",
            "想必会叹息不已吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3982():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3982)
    Sleep(0)

    def lambda_3992():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3992)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    #C0063
    ChrTalk(
        0x101,
        (
            "#00005F#12P乌尔斯拉……\x01",
            "就是《圣女与白狼》中的那位……？\x02\x03",

            "#00011F哎！白狼……\x01",
            "难道那头白狼就是蔡特吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        (
            "#10404F#11P乌尔斯拉是存在于中世纪的真实人物，\x01",
            "曾向领主进谏过的女性医师。\x02\x03",

            "#10400F教会也将其\x01",
            "认定为圣人。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C嗯，是个很温柔的女孩。\x02\x03",

            "#01200F顺便一说，虽然小说中的她不幸丧生，\x01",
            "但实际上她却侥幸保住了性命……\x02\x03",

            "之后，乌尔斯拉与骑士结为夫妻，\x01",
            "他们的后世子孙至今仍然生活在这片大地。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00012F#12P是、是这样啊……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10409F#11P哈哈，现实往往比\x01",
            "小说中的情节更加离奇呢。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19750, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_37()
    SetChrPos(0x0, -76500, -2100, -55450, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A0, 3)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_17_36D5 end

    def Function_18_3BD6(): pass

    label("Function_18_3BD6")

    EventBegin(0x0)
    OP_E2(0x3)
    OP_68(3370, -100, -96510, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x101, -840, -700, -98050, 90)
    SetChrPos(0x105, -1380, -700, -96700, 90)
    SetChrPos(0x107, -3500, -700, -97500, 90)
    Fade(500)

    def lambda_3C45():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C45)
    Sleep(50)

    def lambda_3C5D():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C5D)
    Sleep(50)

    def lambda_3C75():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3C75)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0068
    ChrTalk(
        0x101,
        "#00007F#5P（那是……！）\x02",
    )

    CloseMessageWindow()
    OP_68(9880, -100, -96020, 2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 0)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_18_3BD6 end

    def Function_19_3D1B(): pass

    label("Function_19_3D1B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    OP_68(3370, -100, -96510, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21210, 0)
    SetChrPos(0x101, 2590, -700, -94990, 90)
    SetChrPos(0x105, 1520, -700, -94950, 90)
    SetChrPos(0x107, 880, -700, -93770, 90)
    SetChrSubChip(0x107, 0x5)
    OP_68(3140, -500, -93460, 0)
    MoveCamera(56, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21000, 0)
    SetCameraDistance(20000, 1500)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0069
    ChrTalk(
        0x101,
        (
            "#00006F#5P……我们绝不能在这种地方\x01",
            "被国防军发现。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x105,
        (
            "#10403F#6P嗯，还是避开他们为好。\x02\x03",

            "#10408F但不知道他们\x01",
            "什么时候才会离开。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x107, 0x1C2, 2100, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x107)
    Sleep(500)

    #C0071
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C……嗯。\x02\x03",

            "#01200F缇欧似乎在\x01",
            "这间医院中。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3EE7():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3EE7)
    Sleep(50)

    def lambda_3EF7():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_3EF7)

    #C0072
    ChrTalk(
        0x101,
        "#00007F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x105,
        "#10401F#12P真的吗……？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3C嗯，我隐隐嗅到了她的味道。\x02\x03",

            "#01201F但支援科的其他成员\x01",
            "似乎都不在。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#00006F#11P难、难道缇欧……\x02\x03",

            "#00010F在当时受了伤，\x01",
            "然后一直在住院治疗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x107,
        (
            "#01200F#5P#3C唔……这种事情\x01",
            "就不能凭我的鼻子来判断了……\x02\x03",

            "#01203F实在是有些担心呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00008F#11P啧，到底该怎么办才好……\x02",
    )

    CloseMessageWindow()
    OP_63(0x105, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x105)
    TurnDirection(0x105, 0x101, 500)

    #C0078
    ChrTalk(
        0x105,
        (
            "#10403F#6P……虽然可能是有点犯规。\x02\x03",

            "#10400F但就算过去与那些士兵对峙，\x01",
            "说不定也能让他们无法呼叫增援。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x1B8, 2100, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_411C():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_411C)
    Sleep(50)
    SetChrFlags(0x107, 0x20)
    OP_93(0x107, 0xB4, 0x1F4)
    ClearChrFlags(0x107, 0x20)

    #C0079
    ChrTalk(
        0x101,
        "#00005F#11P真、真的吗……！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x107,
        (
            "#01200F#5P#3C嗯？你好像\x01",
            "有什么办法啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10404F#6P呵呵，算是吧。\x02\x03",

            "#10402F如何？罗伊德。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00003F#11P……这还用问吗，\x01",
            "立刻开始行动吧。\x02\x03",

            "#00013F无论如何也要\x01",
            "确认缇欧的情况……！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x107,
        "#01201F#5P#3C嗯，上吧。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x105,
        (
            "#10404F#6P那就以电光石火般\x01",
            "的速度将他们解决掉。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 960, -700, -97990, 90)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A0, 4)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x1, 0x0, 0x14)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_19_3D1B end

    def Function_20_42A5(): pass

    label("Function_20_42A5")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "直接突入\x01",      # 0
            "继续准备\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_42F3"),
        (1, "loc_4315"),
        (SWITCH_DEFAULT, "loc_432D"),
    )


    label("loc_42F3")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_432D")

    label("loc_4315")

    SetChrPos(0x0, 2500, -700, -97500, 270)
    EventEnd(0x5)
    Jump("loc_432D")

    label("loc_432D")

    Return()

    # Function_20_42A5 end

    def Function_21_432E(): pass

    label("Function_21_432E")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0085
    ChrTalk(
        0x8,
        (
            "没想到我竟然\x01",
            "会输给你这种\x01",
            "弱不禁风的小男孩……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "给，把它拿去吧，\x01",
            "这是战胜我的证明。\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x28),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('海刃奖牌', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0088
    ChrTalk(
        0x101,
        "#00012F谢、谢谢……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "从今以后，你就是\x01",
            "『超级海刃』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "但是……不要因此\x01",
            "而得意忘形哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "我是『海刃』沙克曼，\x01",
            "换言之，就是海之男儿。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "如果是在海边比赛钓鱼，\x01",
            "绝对不可能输给你这种家伙……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x101,
        "#00006F知、知道了……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x8, -37300, -440, -76070, 270)
    OP_66(0x5, 0x1)
    OP_4C(0x8, 0xFF)
    SetScenarioFlags(0x1C0, 6)
    SetChrPos(0x0, -35530, -450, -80410, 315)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)
    Return()

    # Function_21_432E end

    def Function_22_4524(): pass

    label("Function_22_4524")


    #C0094
    ChrTalk(
        0x8,
        (
            "哇哈哈，\x01",
            "你虽然输给了我，\x01",
            "但也没必要沮丧。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "因为你并不差，\x01",
            "只是我太强了而已。\x01",
            "哇哈哈哈哈哈！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_22_4524 end

    def Function_23_458B(): pass

    label("Function_23_458B")


    #C0096
    ChrTalk(
        0x8,
        "喂喂，要放弃比赛吗？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "啧，算了，\x01",
            "但下次可不能再这样啦。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_23_458B end

    def Function_24_45CD(): pass

    label("Function_24_45CD")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0098
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "东·圣乌尔斯拉医科大学\x01",
            "北·克洛斯贝尔市　１５３赛尔矩\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_24_45CD end

    SaveToFile()

Try(main)
