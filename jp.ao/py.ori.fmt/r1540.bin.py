from ScenarioHelper import *

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
        0x0D,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 96, 0, 4, 0, 5],
    )

    BuildStringList((
        "r1540",                  # 0
        "海刃シャークマン",       # 1
        "ファイヤービートル",     # 2
        "ファイヤービートル",     # 3
        "ゴーディ・オッサー",     # 4
        "ゴーディ・オッサー",     # 5
        "クリドゥヴァー",         # 6
        "幻獣",                   # 7
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
        "クロスベル市方面",       # 18
        "ウルスラ医科大学方面",   # 19
    ))

    ATBonus("ATBonus_564", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_584", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4A92", 0,   0,   18,  2,   2,   0,   2)
    Sepith("Sepith_4AA2", 0,   9,   3,   0,   4,   4,   4)
    Sepith("Sepith_4A8A", 3,   10,  0,   8,   3,   0,   0)
    Sepith("Sepith_4A9A", 9,   5,   0,   3,   0,   3,   4)
    Sepith("Sepith_4AD2", 23,  23,  23,  23,  23,  23,  23)
    Sepith("Sepith_4ADA", 9,   7,   18,  6,   7,   6,   3)

    MonsterBattlePostion("MonsterBattlePostion_5C4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5CC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5D8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5DC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5E0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_628", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_62C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_630", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_634", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_638", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_63C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_640", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5C0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_660", 0, 0, 180)

    # monster count: 13

    BattleInfo(
        "BattleInfo_700", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1530", "Sepith_4A92", 30, 40, 20, 10,
        (
            ("ms65700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms65700.dat", "ms65700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms65700.dat", "ms65700.dat", "ms65700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms65700.dat", "ms65700.dat", "ms62100.dat", "ms65700.dat", 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_958", 0x0000, 58, 6, 45, 10, 1, 65, 0, "br1530", "Sepith_4AA2", 45, 20, 20, 15,
        (
            ("ms70800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70800.dat", "ms70800.dat", "ms70800.dat", "ms61400.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70800.dat", "ms70700.dat", "ms70800.dat", "ms70800.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70800.dat", "ms70700.dat", "ms70800.dat", "ms61400.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_890", 0x0000, 58, 6, 45, 10, 1, 25, 0, "br1530", "Sepith_4A8A", 30, 40, 20, 10,
        (
            ("ms69700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms69700.dat", "ms69700.dat", "ms69700.dat", "ms69700.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_7C8", 0x0000, 58, 6, 45, 10, 1, 40, 0, "br1530", "Sepith_4A9A", 30, 40, 20, 10,
        (
            ("ms61100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms61100.dat", "ms61100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_A20", 0x0000, 58, 6, 90, 8, 1, 50, 0, "br1530", "Sepith_4AD2", 30, 40, 20, 10,
        (
            ("ms66401.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms66401.dat", "ms66401.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms66401.dat", "ms66401.dat", "ms66401.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms66401.dat", "ms66401.dat", "ms66401.dat", "ms66401.dat", 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
        )
    )

    BattleInfo(
        "BattleInfo_664", 0x0000, 81, 6, 45, 6, 1, 40, 0, "br1530", "Sepith_4ADA", 40, 35, 25, 0,
        (
            ("ms70201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7450", "ed7453", "ATBonus_564"),
            (),
        )
    )

    # event battle count: 6

    BattleInfo(
        "BattleInfo_B70", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "ms61100.dat", "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7451", "ed7453", "ATBonus_564"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_AE8", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "ms65700.dat", "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7453", "ed7453", "ATBonus_564"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_B2C", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "ms70201.dat", "MonsterBattlePostion_5C4", "MonsterBattlePostion_624", "ed7453", "ed7453", "ATBonus_564"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_BB4", 0x0040, 255, 6, 45, 3, 3, 30, 0, "br1530", 0x00000000, 100, 0, 0, 0,
        (
            ("ms88901.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_644", "MonsterBattlePostion_624", "ed7454", "ed7453", "ATBonus_584"),
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

    DeclMonster(-16149,  -15050,  0,       0x1010000,    "BattleInfo_700", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-29300,  -27360,  0,       0x1010000,    "BattleInfo_958", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(-27960,  -49820,  0,       0x1010000,    "BattleInfo_890", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(-50100,  -41380,  0,       0x1010000,    "BattleInfo_7C8", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-61400,  7360,    6300,    0x1010000,    "BattleInfo_700", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-70810,  -52410,  -2100,   0x1010000,    "BattleInfo_7C8", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-83770,  -55240,  -2100,   0x1010000,    "BattleInfo_7C8", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-55500,  -81280,  -870,    0x1010000,    "BattleInfo_958", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(-39400,  -65319,  -700,    0x1010000,    "BattleInfo_700", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(-20030,  -84440,  -700,    0x1010000,    "BattleInfo_890", 0,   24,  0xFFFF, 6,  7)
    DeclMonster(-70270,  -36330,  0,       0x1010000,    "BattleInfo_A20", 0,   28,  0xFFFF, 10, 11)
    DeclMonster(-28180,  -13440,  0,       0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-77050,  -65440,  -2100,   0x1010000,    "BattleInfo_664", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 16,  -74.0,                 -45.0,                 -2.5,                  441.0,                 [0.0714285746216774,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   5.285714626312256,     15.0,                  0.5,                   1.0])
    DeclEvent(0x0000, 0, 18,  2.9100000858306885,    -95.0,                 -1.7000000476837158,   324.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.0833333358168602,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.9700000286102295,   7.9166669845581055,    0.3400000035762787,    1.0])

    DeclActor(-27130,  0,       -52750,  1200,    -27130,  1000,    -52750,  0x007C, 0,  6,  0x0000)
    DeclActor(-63070,  6350,    15500,   1200,    -63070,  7350,    15500,   0x007C, 0,  7,  0x0000)
    DeclActor(-36340,  -700,    -65120,  1200,    -36340,  300,     -65120,  0x007C, 0,  8,  0x0000)
    DeclActor(-11420,  0,       -14380,  1200,    -11420,  0,       -14380,  0x007C, 0,  9,  0x0000)
    DeclActor(-65269,  6300,    17740,   1200,    -65269,  6300,    17740,   0x007C, 0,  10, 0x0000)
    DeclActor(-37240,  -410,    -79670,  1200,    -42890,  -2800,   -78670,  0x007C, 0,  15, 0x0000)
    DeclActor(-2450,   -700,    -92010,  1500,    -2450,   1000,    -92010,  0x007C, 0,  24, 0x0000)

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
        "Function_0_CEC",          # 00, 0
        "Function_1_DA4",          # 01, 1
        "Function_2_DC3",          # 02, 2
        "Function_3_DE2",          # 03, 3
        "Function_4_E01",          # 04, 4
        "Function_5_1388",         # 05, 5
        "Function_6_19B3",         # 06, 6
        "Function_7_1B1A",         # 07, 7
        "Function_8_1D31",         # 08, 8
        "Function_9_1E82",         # 09, 9
        "Function_10_21E0",        # 0A, 10
        "Function_11_253E",        # 0B, 11
        "Function_12_256D",        # 0C, 12
        "Function_13_2571",        # 0D, 13
        "Function_14_3249",        # 0E, 14
        "Function_15_32F6",        # 0F, 15
        "Function_16_35AA",        # 10, 16
        "Function_17_3985",        # 11, 17
        "Function_18_3EA5",        # 12, 18
        "Function_19_3FEC",        # 13, 19
        "Function_20_4600",        # 14, 20
        "Function_21_469D",        # 15, 21
        "Function_22_48E3",        # 16, 22
        "Function_23_496E",        # 17, 23
        "Function_24_49BE",        # 18, 24
    ))


    def Function_0_CEC(): pass

    label("Function_0_CEC")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_D2C"),
        (1, "loc_D38"),
        (2, "loc_D44"),
        (3, "loc_D50"),
        (4, "loc_D5C"),
        (5, "loc_D68"),
        (6, "loc_D74"),
        (SWITCH_DEFAULT, "loc_D80"),
    )


    label("loc_D2C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D38")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D44")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D50")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D5C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D68")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D74")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D80")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_D8C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DA3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_D8C")

    label("loc_DA3")

    Return()

    # Function_0_CEC end

    def Function_1_DA4(): pass

    label("Function_1_DA4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DC2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_DA4")

    label("loc_DC2")

    Return()

    # Function_1_DA4 end

    def Function_2_DC3(): pass

    label("Function_2_DC3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_DE1")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_2_DC3")

    label("loc_DE1")

    Return()

    # Function_2_DC3 end

    def Function_3_DE2(): pass

    label("Function_3_DE2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_E00")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_3_DE2")

    label("loc_E00")

    Return()

    # Function_3_DE2 end

    def Function_4_E01(): pass

    label("Function_4_E01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_E1B")
    SetChrPos(0x8, -37300, -440, -76070, 270)

    label("loc_E1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_E2E")
    SetChrFlags(0x8, 0x80)
    Jump("loc_EC8")

    label("loc_E2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_E4A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x191, 1)), scpexpr(EXPR_END)), "loc_E45")
    SetChrFlags(0x8, 0x80)

    label("loc_E45")

    Jump("loc_EC8")

    label("loc_E4A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_E58")
    Jump("loc_EC8")

    label("loc_E58")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_E66")
    Jump("loc_EC8")

    label("loc_E66")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 5)), scpexpr(EXPR_END)), "loc_E74")
    Jump("loc_EC8")

    label("loc_E74")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_E82")
    Jump("loc_EC8")

    label("loc_E82")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_E90")
    Jump("loc_EC8")

    label("loc_E90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_E9E")
    Jump("loc_EC8")

    label("loc_E9E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_EAC")
    Jump("loc_EC8")

    label("loc_EAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EBA")
    Jump("loc_EC8")

    label("loc_EBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_EC8")
    SetChrFlags(0x8, 0x80)

    label("loc_EC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_ED7")
    ClearScenarioFlags(0x22, 0)
    Event(0, 19)

    label("loc_ED7")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1384")
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
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F6D")
    SetScenarioFlags(0x38, 0)

    label("loc_F6D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F83")
    SetScenarioFlags(0x38, 1)

    label("loc_F83")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F99")
    SetScenarioFlags(0x38, 2)

    label("loc_F99")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FAF")
    SetScenarioFlags(0x38, 3)

    label("loc_FAF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FC5")
    SetScenarioFlags(0x38, 4)

    label("loc_FC5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FDB")
    SetScenarioFlags(0x38, 5)

    label("loc_FDB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF1")
    SetScenarioFlags(0x38, 6)

    label("loc_FF1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1007")
    SetScenarioFlags(0x38, 7)

    label("loc_1007")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101D")
    SetScenarioFlags(0x39, 0)

    label("loc_101D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1033")
    SetScenarioFlags(0x39, 1)

    label("loc_1033")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1049")
    SetScenarioFlags(0x39, 2)

    label("loc_1049")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_105F")
    SetScenarioFlags(0x39, 3)

    label("loc_105F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1075")
    SetScenarioFlags(0x39, 4)

    label("loc_1075")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_108B")
    SetScenarioFlags(0x39, 5)

    label("loc_108B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10A1")
    SetScenarioFlags(0x39, 6)

    label("loc_10A1")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B7")
    SetScenarioFlags(0x39, 7)

    label("loc_10B7")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10CD")
    SetScenarioFlags(0x3A, 0)

    label("loc_10CD")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10E3")
    SetScenarioFlags(0x3A, 1)

    label("loc_10E3")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10F9")
    SetScenarioFlags(0x3A, 2)

    label("loc_10F9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_110F")
    SetScenarioFlags(0x3A, 3)

    label("loc_110F")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1125")
    SetScenarioFlags(0x3A, 4)

    label("loc_1125")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113B")
    SetScenarioFlags(0x3A, 5)

    label("loc_113B")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1151")
    SetScenarioFlags(0x3A, 6)

    label("loc_1151")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1167")
    SetScenarioFlags(0x3A, 7)

    label("loc_1167")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_117D")
    SetScenarioFlags(0x3B, 0)

    label("loc_117D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1193")
    SetScenarioFlags(0x3B, 1)

    label("loc_1193")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11A9")
    SetScenarioFlags(0x3B, 2)

    label("loc_11A9")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11BF")
    SetScenarioFlags(0x3B, 3)

    label("loc_11BF")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11D5")
    SetScenarioFlags(0x3B, 4)

    label("loc_11D5")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_11EB")
    SetScenarioFlags(0x3B, 5)

    label("loc_11EB")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1201")
    SetScenarioFlags(0x3B, 6)

    label("loc_1201")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1217")
    SetScenarioFlags(0x3B, 7)

    label("loc_1217")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_122D")
    SetScenarioFlags(0x3D, 5)

    label("loc_122D")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1243")
    SetScenarioFlags(0x3D, 6)

    label("loc_1243")

    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1259")
    SetScenarioFlags(0x3D, 7)

    label("loc_1259")

    ClearScenarioFlags(0x3C, 0)
    ClearScenarioFlags(0x3C, 1)
    ClearScenarioFlags(0x3C, 2)
    ClearScenarioFlags(0x3C, 3)
    ClearScenarioFlags(0x3C, 4)
    ClearScenarioFlags(0x3C, 5)
    ClearScenarioFlags(0x3C, 6)
    ClearScenarioFlags(0x3C, 7)
    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1294")
    SetScenarioFlags(0x3C, 0)
    Jump("loc_1384")

    label("loc_1294")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12B7")
    SetScenarioFlags(0x3C, 1)
    Jump("loc_1384")

    label("loc_12B7")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12DA")
    SetScenarioFlags(0x3C, 2)
    Jump("loc_1384")

    label("loc_12DA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FD")
    SetScenarioFlags(0x3C, 3)
    Jump("loc_1384")

    label("loc_12FD")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1320")
    SetScenarioFlags(0x3C, 4)
    Jump("loc_1384")

    label("loc_1320")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1343")
    SetScenarioFlags(0x3C, 5)
    Jump("loc_1384")

    label("loc_1343")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1366")
    SetScenarioFlags(0x3C, 6)
    Jump("loc_1384")

    label("loc_1366")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1384")
    SetScenarioFlags(0x3C, 7)

    label("loc_1384")

    Call(0, 11)
    Return()

    # Function_4_E01 end

    def Function_5_1388(): pass

    label("Function_5_1388")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_139A")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0xFB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_139A")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_173C")
    LoadEffect(0x9, "map/mprain00.eff")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_7D(0xB4, 0xB4, 0xB4, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0x0, 0xBE, 0x0)
    Sound(128, 1, 100, 0)

    label("loc_173C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_17A3")
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
    Jump("loc_17D3")

    label("loc_17A3")

    SetMapObjFlags(0x3, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)

    label("loc_17D3")

    SetMapObjFlags(0x10, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_17ED")
    ClearMapObjFlags(0x10, 0x4)

    label("loc_17ED")

    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, -42890, -2800, -78670, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1851")
    OP_66(0x5, 0x1)

    label("loc_1851")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1864")
    OP_70(0x0, 0x0)
    Jump("loc_1868")

    label("loc_1864")

    OP_70(0x0, 0x1E)

    label("loc_1868")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187B")
    OP_70(0x1, 0x0)
    Jump("loc_187F")

    label("loc_187B")

    OP_70(0x1, 0x1E)

    label("loc_187F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1892")
    OP_70(0x2, 0x0)
    Jump("loc_1896")

    label("loc_1892")

    OP_70(0x2, 0x1E)

    label("loc_1896")

    LoadEffect(0x10, "event\\eva00_00.eff")
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_18F7")
    PlayEffect(0x10, 0x9, 0xFF, 0x0, -11420, 0, -14380, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_18F7")

    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_1943")
    PlayEffect(0x10, 0xA, 0xFF, 0x0, -65269, 6300, 17740, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_1943")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_195B")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_195B")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1973")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_1973")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1986")
    OP_1B(0x1, 0x0, 0x14)

    label("loc_1986")

    OP_1C(0x0, 0xB, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xC, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xD, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    OP_1C(0x0, 0xE, 0x0, 0x32, 0x0, 0xC, 0x0, 0x0)
    Return()

    # Function_5_1388 end

    def Function_6_19B3(): pass

    label("Function_6_19B3")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AE3")
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
    SetScenarioFlags(0x1EC, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1B08")

    label("loc_1AE3")


    #A0002
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

    label("loc_1B08")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_19B3 end

    def Function_7_1B1A(): pass

    label("Function_7_1B1A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CEB")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C19")
    OP_A7(0xD, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xD, 0x0, 0)
    OP_98(0xD, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1B77():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_1B77)

    def lambda_1B91():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_1B91)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)

    #A0003
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
    Battle("BattleInfo_B70", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xD, 0x80)
    ClearChrFlags(0xD, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1BFA"),
        (2, "loc_1C09"),
        (1, "loc_1C16"),
        (SWITCH_DEFAULT, "loc_1C19"),
    )


    label("loc_1BFA")

    SetScenarioFlags(0x216, 6)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1C19")

    label("loc_1C09")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1C16")

    OP_B9(0x0)
    Return()

    label("loc_1C19")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xB6, 1)"), scpexpr(EXPR_END)), "loc_1C76")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1CE6")

    label("loc_1C76")

    FadeToDark(300, 0, 100)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xB6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1CE6")

    Jump("loc_1D25")

    label("loc_1CEB")

    FadeToDark(300, 0, 100)

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

    label("loc_1D25")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1B1A end

    def Function_8_1D31(): pass

    label("Function_8_1D31")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1EC, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E31")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1DBA")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1EC, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1E2C")

    label("loc_1DBA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1E2C")

    Jump("loc_1E76")

    label("loc_1E31")

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

    label("loc_1E76")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1D31 end

    def Function_9_1E82(): pass

    label("Function_9_1E82")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_203A")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_201B")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0010
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2016")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2013")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_1F3C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1F3C)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_AE8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200E")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_1FF5")
    Call(1, 5)
    Jump("loc_200E")

    label("loc_1FF5")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_200B")
    Call(1, 4)
    Jump("loc_200E")

    label("loc_200B")

    Call(1, 3)

    label("loc_200E")

    Jump("loc_2016")

    label("loc_2013")

    Call(1, 1)

    label("loc_2016")

    Jump("loc_2031")

    label("loc_201B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_2031")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_2031")

    TalkEnd(0xFF)
    Return()

    label("loc_203A")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 6)), scpexpr(EXPR_END)), "loc_21C5")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0012
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21C0")
    ClearScenarioFlags(0x3A, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_21BD")
    ClearScenarioFlags(0x38, 6)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_20E6():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_20E6)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_B2C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21B8")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_219F")
    Call(1, 5)
    Jump("loc_21B8")

    label("loc_219F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_21B5")
    Call(1, 4)
    Jump("loc_21B8")

    label("loc_21B5")

    Call(1, 3)

    label("loc_21B8")

    Jump("loc_21C0")

    label("loc_21BD")

    Call(1, 1)

    label("loc_21C0")

    Jump("loc_21DB")

    label("loc_21C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 6)), scpexpr(EXPR_END)), "loc_21DB")
    ClearScenarioFlags(0x38, 6)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    Call(1, 0)

    label("loc_21DB")

    TalkEnd(0xFF)
    Return()

    # Function_9_1E82 end

    def Function_10_21E0(): pass

    label("Function_10_21E0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2398")
    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_2379")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0014
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2374")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_2371")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_229A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_229A)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_AE8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_236C")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2353")
    Call(1, 5)
    Jump("loc_236C")

    label("loc_2353")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2369")
    Call(1, 4)
    Jump("loc_236C")

    label("loc_2369")

    Call(1, 3)

    label("loc_236C")

    Jump("loc_2374")

    label("loc_2371")

    Call(1, 1)

    label("loc_2374")

    Jump("loc_238F")

    label("loc_2379")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_238F")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_238F")

    TalkEnd(0xFF)
    Return()

    label("loc_2398")

    TalkBegin(0xFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A, 7)), scpexpr(EXPR_END)), "loc_2523")
    LoadEffect(0x7, "event\\eva07_00.eff")

    #A0016
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251E")
    ClearScenarioFlags(0x3A, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_251B")
    ClearScenarioFlags(0x38, 7)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2444():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_2444)
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
            "魔獣が現れた！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Battle("BattleInfo_B2C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2516")
    RunExpression(0x0, (scpexpr(EXPR_RAND), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_24FD")
    Call(1, 5)
    Jump("loc_2516")

    label("loc_24FD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2513")
    Call(1, 4)
    Jump("loc_2516")

    label("loc_2513")

    Call(1, 3)

    label("loc_2516")

    Jump("loc_251E")

    label("loc_251B")

    Call(1, 1)

    label("loc_251E")

    Jump("loc_2539")

    label("loc_2523")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x38, 7)), scpexpr(EXPR_END)), "loc_2539")
    ClearScenarioFlags(0x38, 7)
    OP_65(0x4, 0x1)
    StopEffect(0xA, 0x2)
    Call(1, 0)

    label("loc_2539")

    TalkEnd(0xFF)
    Return()

    # Function_10_21E0 end

    def Function_11_253E(): pass

    label("Function_11_253E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2556")
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)

    label("loc_2556")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C, 0)), scpexpr(EXPR_END)), "loc_2567")
    ClearScenarioFlags(0x3C, 0)
    Jump("loc_256C")

    label("loc_2567")

    SetChrFlags(0x19, 0x80)

    label("loc_256C")

    Return()

    # Function_11_253E end

    def Function_12_256D(): pass

    label("Function_12_256D")

    Call(1, 6)
    Return()

    # Function_12_256D end

    def Function_13_2571(): pass

    label("Function_13_2571")

    TalkBegin(0xFE)
    ClearScenarioFlags(0x0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2589")
    SetScenarioFlags(0x0, 1)

    label("loc_2589")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 6)), scpexpr(EXPR_END)), "loc_2595")
    SetScenarioFlags(0x0, 1)

    label("loc_2595")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2831")
    TurnDirection(0x8, 0x101, 0)
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0018
    ChrTalk(
        0x8,
        (
            "がはは、\x01",
            "アンタは釣公師団のモンだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x8,
        (
            "オレッちはシャークマン。\x01",
            "《海刃》シャークマンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00005Fか、怪人……？\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x0)
    Sleep(1000)
    OP_64(0x8)

    #C0021
    ChrTalk(
        0x8,
        (
            "ちがーう！　海刃だ、海刃！！\x01",
            "海の刃で海刃んんっ！\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        (
            "というわけで、オレッちと\x01",
            "『爆釣サドンデス』で勝負だ！\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00006Fは、はあ……\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0024
    ChrTalk(
        0x8,
        (
            "おっと、いけねえ。\x01",
            "その前に条件があるんだった。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x8,
        (
            "俺はこう見えて、四天王随一の\x01",
            "テクニシャンと呼ばれていてな。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "俺と戦うにはいわゆる\x01",
            "ゲームフィッシュと言われる魚を\x01",
            "いくつか釣って来てもらうぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "ま、詳しい種類が知りたい場合は\x01",
            "街にいるセイラームに聞いてくんな。\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#00012Fりょ、了解です……\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 5)
    OP_93(0x8, 0x10E, 0x0)

    label("loc_2831")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_283B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3245")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2887")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "爆釣勝負を挑む\x01",      # 1
            "やめる\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    Jump("loc_2891")

    label("loc_2887")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2891")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F61")
    TurnDirection(0x8, 0x0, 0)
    Call(0, 14)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2DA2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x15F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A1E")

    #C0029
    ChrTalk(
        0x8,
        (
            "おう、そんじゃ釣り手帳を\x01",
            "見させてもらうぜ！\x02",
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
            "がはは、やるじぇねえか。\x01",
            "見事条件を満たしてやがる！\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x8,
        (
            "よしっ、そんじゃ\x01",
            "さっそく勝負と行こうぜ！\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x8,
        (
            "前にも言ったが、\x01",
            "オレッちとの勝負は\x01",
            "『爆釣サドンデス』！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x8,
        (
            "ひたすら交互に竿を振り、\x01\x07\x02",

            "先に釣り損ねた方の負け\x07\x00",
            "ってわけだ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x15F, 6)
    Jump("loc_2A9C")

    label("loc_2A1E")


    #C0034
    ChrTalk(
        0x8,
        (
            "がはは、『爆釣サドンデス』で\x01",
            "オレッちと勝負するかい？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x8,
        (
            "ひたすら交互に竿を振り、\x01\x07\x02",

            "先に釣れなく方の負け\x07\x00",
            "ってわけだ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A9C")

    FadeToDark(300, 0, 100)
    OP_0D()
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "《海刃》シャークマンに、\x01",
            "『爆釣サドンデス』を挑みますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "勝負を挑む\x01",      # 0
            "やめておく\x01",      # 1
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
        (0, "loc_2B3B"),
        (1, "loc_2D4E"),
        (SWITCH_DEFAULT, "loc_2D9D"),
    )


    label("loc_2B3B")


    #C0037
    ChrTalk(
        0x8,
        (
            "がはは、\x01",
            "そんじゃさっそく始めるか！\x02",
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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C8A")
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

    label("loc_2C8A")

    OP_68(-36530, -1120, -76470, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, -37300, -440, -76070, 180)
    OP_93(0xFE, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE9")
    Call(0, 22)
    Jump("loc_2D0D")

    label("loc_2CE9")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CFC")
    Jump("loc_2D0D")

    label("loc_2CFC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D0D")
    Call(0, 23)

    label("loc_2D0D")

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
    Jump("loc_2D9D")

    label("loc_2D4E")


    #C0038
    ChrTalk(
        0x8,
        "んあ？　そうか……\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x8,
        (
            "まあやりたくなけりゃあ\x01",
            "仕方ねえやな。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    Jump("loc_2D9D")

    label("loc_2D9D")

    Jump("loc_2F5C")

    label("loc_2DA2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_2E8D")

    #C0040
    ChrTalk(
        0x8,
        (
            "おう、そんじゃ釣り手帳を\x01",
            "見させてもらうぜ！\x02",
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
            "まあ、努力は認めるがよ。\x01",
            "まだちょっち足りねえな。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x8,
        (
            "オレッちがこよなく愛する\x01",
            "ゲームフィッシュ……\x01",
            "見事全部揃えて来いってんだ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)
    Jump("loc_2F5C")

    label("loc_2E8D")


    #C0043
    ChrTalk(
        0x8,
        (
            "おう、そんじゃ釣り手帳を\x01",
            "見させてもらうぜ！\x02",
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
            "なんじゃこりゃ？\x01",
            "まだまだ全然じゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x8,
        (
            "オレッちがこよなく愛する\x01",
            "ゲームフィッシュ……\x01",
            "さっさと釣って来いってんだ！\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x0)

    label("loc_2F5C")

    Jump("loc_3240")

    label("loc_2F61")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3240")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F84")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2F84")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_END)), "loc_2F92")
    Jump("loc_3240")

    label("loc_2F92")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 2)), scpexpr(EXPR_END)), "loc_2FE3")

    #C0046
    ChrTalk(
        0x8,
        (
            "オレぇはシャークマン～っ。\x01",
            "海ぃに惚れた～テクニシャン～～っ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3240")

    label("loc_2FE3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x164, 0)), scpexpr(EXPR_END)), "loc_301E")

    #C0047
    ChrTalk(
        0x8,
        (
            "雨に打たれてぇ、\x01",
            "漢ぉは強くなるぅ～っ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3240")

    label("loc_301E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x162, 0)), scpexpr(EXPR_END)), "loc_3069")

    #C0048
    ChrTalk(
        0x8,
        (
            "人間ん～、みんなぁあ、\x01",
            "海から生まれた兄弟だものぉ～っ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3240")

    label("loc_3069")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x160, 0)), scpexpr(EXPR_END)), "loc_30B0")

    #C0049
    ChrTalk(
        0x8,
        (
            "海のぉ漢はよぉ～、\x01",
            "黙ってぇ背中で語りゃあいい～っ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3240")

    label("loc_30B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x141, 5)), scpexpr(EXPR_END)), "loc_3122")

    #C0050
    ChrTalk(
        0x8,
        (
            "面舵ぃいっぱい～、\x01",
            "夢ぇいっぱい～～っ。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x8,
        (
            "オレぇは夢にぃ～、\x01",
            "人生を売った漢ぉ～だぜぇ～っ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3240")

    label("loc_3122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 4)), scpexpr(EXPR_END)), "loc_3187")

    #C0052
    ChrTalk(
        0x8,
        (
            "オレぇはシャークマン～っ。\x01",
            "船を出すぅ～っ。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x8,
        "世間と言う名のぉ、荒波にぃ～っ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_3240")

    label("loc_3187")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_3229")

    #C0054
    ChrTalk(
        0x8,
        (
            "オレぇはシャークマン～っ。\x01",
            "海ぃの～漢ぉお～～っ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1C0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3224")

    #C0055
    ChrTalk(
        0x101,
        (
            "#00003F（ここなら何か釣れそうだけど……\x01",
            "  先客がいるなら止めておくか。）\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3224")

    Jump("loc_3240")

    label("loc_3229")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x128, 1)), scpexpr(EXPR_END)), "loc_3237")
    Jump("loc_3240")

    label("loc_3237")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x126, 1)), scpexpr(EXPR_END)), "loc_3240")

    label("loc_3240")

    Jump("loc_283B")

    label("loc_3245")

    TalkEnd(0xFE)
    Return()

    # Function_13_2571 end

    def Function_14_3249(): pass

    label("Function_14_3249")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0xB, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_326E")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_326E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x7, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3289")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_3289")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32A4")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32A4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x9, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32BF")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32BF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x11, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32DA")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32F5")
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_32F5")

    Return()

    # Function_14_3249 end

    def Function_15_32F6(): pass

    label("Function_15_32F6")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0056
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A5")
    OP_E2(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_OR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33DC")
    MiniGame(0x6, 0xF, 0xFFFF6E88, 0xFFFFFE66, 0xFFFEC8CA, 0x10E, 0xFFFF5876, 0xFFFFF510, 0xFFFECCB2)
    Jump("loc_35A5")

    label("loc_33DC")

    MiniGame(0x6, 0x10, 0xFFFF6E88, 0xFFFFFE66, 0xFFFEC8CA, 0x10E, 0xFFFF5876, 0xFFFFF510, 0xFFFECCB2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35A5")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E4(0x0, 0x1C, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x18B, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_35A5")
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
        "ロイド",
        (
            "#00011Fう、うわ……\x01",
            "何だか凄く凶暴そうな魚だな。\x02\x03",

            "#00003Fピラーニャに似てるけど……\x01",
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

    label("loc_35A5")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_32F6 end

    def Function_16_35AA(): pass

    label("Function_16_35AA")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A9, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3874")
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

    def lambda_36F6():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_36F6)
    Sleep(50)

    def lambda_370E():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_370E)
    Sleep(50)

    def lambda_3726():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3726)
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

    def lambda_382C():
        OP_9B(0x1, 0xFE, 0x0, 0x2710, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_382C)
    OP_74(0xF, 0xA)
    Sound(842, 0, 100, 0)
    OP_71(0xF, 0x5B, 0x5F, 0x1, 0x8)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    SetCameraDistance(23500, 200)
    Sleep(200)
    Jump("loc_390F")

    label("loc_3874")

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

    label("loc_390F")

    Battle("BattleInfo_BB4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0xE, 0x1)
    SetChrFlags(0xE, 0x80)
    SetMapObjFlags(0xF, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3981")
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
    Jump("loc_3984")

    label("loc_3981")

    Call(0, 17)

    label("loc_3984")

    Return()

    # Function_16_35AA end

    def Function_17_3985(): pass

    label("Function_17_3985")

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

    def lambda_3A6D():
        OP_92(0x101, 0xFFFED55E, 0xFFFF2D10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3A6D)
    Sleep(50)

    def lambda_3A83():
        OP_92(0x105, 0xFFFED55E, 0xFFFF2D10, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3A83)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)
    SetChrSubChip(0x107, 0x5)

    #C0059
    ChrTalk(
        0x101,
        (
            "#00006F#12Pふう……いきなりだったな。\x02\x03",

            "#00013Fしかしあんなのがいる状況で、\x01",
            "街から病院へのバスなんて\x01",
            "ちゃんと運行できているのか？\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x105,
        (
            "#10403F#5P難しいかもしれないね。\x02\x03",

            "#10408F国防軍の装甲車とかなら\x01",
            "何とか行き来できそうだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        (
            "#00006F#12Pということは、\x01",
            "市民の健康が損なわれている\x01",
            "可能性もありそうだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3Cふむ、因果なものだ。\x02\x03",

            "ウルスラが見たら\x01",
            "さぞ嘆くかもしれんな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_3C5A():
        TurnDirection(0x101, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C5A)
    Sleep(0)

    def lambda_3C6A():
        TurnDirection(0x105, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C6A)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x105, 0)

    #C0063
    ChrTalk(
        0x101,
        (
            "#00005F#12Pウルスラって……\x01",
            "『聖女と白い狼』の？\x02\x03",

            "#00011Fって、白い狼って\x01",
            "やっぱりツァイトなのか！\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        (
            "#10404F#11P中世の時代に実在した\x01",
            "領主を諌#2Rいさ#めた治療師の娘だね。\x02\x03",

            "#10400F教会でも一応、\x01",
            "聖人認定されているけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3Cうむ、心優しき娘だった。\x02\x03",

            "#01200Fちなみに物語では命を落としたが、\x01",
            "実は一命を取り留めてな……\x02\x03",

            "後に騎士と添い遂げて\x01",
            "末裔#4Rす え#もこの地に残っているぞ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        "#00012F#12Pそ、そうだったのか……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10409F#11Pあはは。\x01",
            "事実は小説より奇なりだね。\x02",
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

    # Function_17_3985 end

    def Function_18_3EA5(): pass

    label("Function_18_3EA5")

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

    def lambda_3F14():
        OP_9B(0x0, 0x101, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3F14)
    Sleep(50)

    def lambda_3F2C():
        OP_9B(0x0, 0x105, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3F2C)
    Sleep(50)

    def lambda_3F44():
        OP_9B(0x0, 0x107, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_3F44)
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
        "#00007F#5P（あれは……！）\x02",
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

    # Function_18_3EA5 end

    def Function_19_3FEC(): pass

    label("Function_19_3FEC")

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
            "#00006F#5P……さすがにここで国防軍に\x01",
            "見つかるわけにはいかないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x105,
        (
            "#10403F#6Pまあ、避けた方が無難だろうね。\x02\x03",

            "#10408Fもっともいつになったら\x01",
            "居なくなるかは判らないけど。\x02",
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
            "#01203F#5P#3C……ふむ。\x02\x03",

            "#01200Fどうやらこの病院内に\x01",
            "ティオがいるようだな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_41FA():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_41FA)
    Sleep(50)

    def lambda_420A():
        TurnDirection(0xFE, 0x107, 500)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_420A)

    #C0072
    ChrTalk(
        0x101,
        "#00007F#11Pな……！？\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x105,
        "#10401F#12Pマジかい……？\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x107,
        (
            "#01203F#5P#3Cうむ、微かに匂いを感じる。\x02\x03",

            "#01201Fそれ以外の支援課のメンバーは\x01",
            "居ないようだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x101,
        (
            "#00006F#11Pま、まさかティオ……\x02\x03",

            "#00010Fあれからどこかで\x01",
            "ケガを負って入院を……？\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x107,
        (
            "#01200F#5P#3Cふむ、そこまでは\x01",
            "私の鼻でも分からぬが……\x02\x03",

            "#01203Fさすがに少々心配だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x101,
        "#00008F#11Pくっ、一体どうしたら……\x02",
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
            "#10403F#6P……少し裏技になるけど。\x02\x03",

            "#10400Fここで兵士たちと交戦しても\x01",
            "増援を呼ばれずに済むかもしれない。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x107, 0x1B8, 2100, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_4449():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4449)
    Sleep(50)
    SetChrFlags(0x107, 0x20)
    OP_93(0x107, 0xB4, 0x1F4)
    ClearChrFlags(0x107, 0x20)

    #C0079
    ChrTalk(
        0x101,
        "#00005F#11Pほ、本当か……！？\x02",
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x107,
        (
            "#01200F#5P#3Cふむ、何やら\x01",
            "手立てがあるようだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x105,
        (
            "#10404F#6Pフフ、まあね。\x02\x03",

            "#10402Fどうする、ロイド？\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#00003F#11P……言うまでもない。\x01",
            "すぐにでも仕掛けよう。\x02\x03",

            "#00013F何としてもティオの様子を\x01",
            "確かめないと……！\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x107,
        "#01201F#5P#3Cうむ、やるか。\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x105,
        (
            "#10404F#6Pそれじゃあ電光石火で\x01",
            "ケリを付けるとしようか。\x02",
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

    # Function_19_3FEC end

    def Function_20_4600(): pass

    label("Function_20_4600")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    OP_0D()

    Menu(
        0,
        -1,
        -1,
        0,
        (
            "このまま突入する\x01",          # 0
            "いったん準備を整える\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4662"),
        (1, "loc_4684"),
        (SWITCH_DEFAULT, "loc_469C"),
    )


    label("loc_4662")

    FadeToDark(1000, 0, -1)
    OP_0D()
    StopBGM(0x7D0)
    WaitBGM()
    SetScenarioFlags(0x22, 1)
    NewScene("t1500", 0, 0, 0)
    IdleLoop()
    Jump("loc_469C")

    label("loc_4684")

    SetChrPos(0x0, 2500, -700, -97500, 270)
    EventEnd(0x5)
    Jump("loc_469C")

    label("loc_469C")

    Return()

    # Function_20_4600 end

    def Function_21_469D(): pass

    label("Function_21_469D")

    EventBegin(0x0)
    FadeToBright(1000, 0)
    OP_0D()

    #C0085
    ChrTalk(
        0x8,
        (
            "まさか、このオレッちが\x01",
            "アンタみたいな\x01",
            "優男に負けちまうとはな……\x02",
        )
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x8,
        (
            "ほらよ、コイツを受け取りな。\x01",
            "オレッちに勝った証だ。\x02",
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0x28, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0088
    ChrTalk(
        0x101,
        "#00012Fど、どうも……\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x8,
        (
            "さてと、これでアンタは\x01",
            "これから『海刃バスター』だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x8,
        (
            "だが……あんまし\x01",
            "調子に乗るんじゃねえぞ？\x02",
        )
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x8,
        (
            "オレッちは《海刃》シャークマン。\x01",
            "すなわち、海の漢なんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x8,
        (
            "これが海釣りだったら、\x01",
            "アンタなんかにゃ絶対に……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0093
    ChrTalk(
        0x101,
        "#00006Fは、はあ……\x02",
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

    # Function_21_469D end

    def Function_22_48E3(): pass

    label("Function_22_48E3")


    #C0094
    ChrTalk(
        0x8,
        (
            "がはは、ってことで\x01",
            "勝負はオレッちの勝ちだが、\x01",
            "気に病むことはないぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0x8,
        (
            "ただオレッちが\x01",
            "強すぎるってだけだからな。\x01",
            "ぐわははははっ！\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_22_48E3 end

    def Function_23_496E(): pass

    label("Function_23_496E")


    #C0096
    ChrTalk(
        0x8,
        "おいおい、試合放棄かよ？\x02",
    )

    CloseMessageWindow()

    #C0097
    ChrTalk(
        0x8,
        (
            "ちっ、まあいい。\x01",
            "次はこうはいかねえからな。\x02",
        )
    )

    CloseMessageWindow()
    Return()

    # Function_23_496E end

    def Function_24_49BE(): pass

    label("Function_24_49BE")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0098
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

    # Function_24_49BE end

    SaveToFile()

Try(main)
