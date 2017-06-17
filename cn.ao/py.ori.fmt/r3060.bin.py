from ScenarioHelper import *

def main():
    CreateScenaFile(
        "r3060.bin",                # FileName
        "r3060",                    # MapName
        "r3060",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("r3060", "r0000_1", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x17,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 101, 0, 1, 0, 2],
    )

    BuildStringList((
        "r3060",                  # 0
        "曹",                     # 1
        "刘",                     # 2
        "黑月成员",               # 3
        "黑月成员",               # 4
        "黑月成员",               # 5
        "黑月成员",               # 6
        "黑月成员",               # 7
        "黑月成员",               # 8
        "黑月成员",               # 9
        "莉夏",                   # 10
        "看到请回馈",             # 11
        "br3000",                 # 12
        "br3000",                 # 13
        "br3000",                 # 14
        "br3000",                 # 15
        "br3000",                 # 16
        "br3000",                 # 17
        "阿尔摩利卡古道方向",     # 18
    ))

    ATBonus("ATBonus_540", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_46C7", 8,   14,  0,   10,  4,   2,   0)
    Sepith("Sepith_46CF", 0,   0,   6,   14,  6,   6,   6)
    Sepith("Sepith_46DF", 8,   8,   8,   8,   8,   8,   8)
    Sepith("Sepith_46D7", 8,   6,   3,   0,   7,   7,   7)
    Sepith("Sepith_46EF", 10,  10,  10,  10,  3,   3,   3)

    MonsterBattlePostion("MonsterBattlePostion_5A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_5A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_5AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_5B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_5BC", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_600", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_604", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_608", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_60C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_610", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_614", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_618", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_61C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_580", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_590", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_594", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_598", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_59C", 2, 13, 180)

    # monster count: 20

    BattleInfo(
        "BattleInfo_878", 0x0000, 73, 6, 60, 8, 1, 20, 0, "br3000", "Sepith_46C7", 30, 30, 20, 20,
        (
            ("ms69500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms69500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms63400.dat", "ms69500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms69500.dat", "ms64100.dat", "ms64100.dat", "ms64100.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_7B0", 0x0000, 73, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_46CF", 30, 40, 20, 10,
        (
            ("ms63400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_620", 0x0000, 73, 6, 60, 8, 1, 40, 0, "br3000", "Sepith_46DF", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms66800.dat", "ms69500.dat", "ms66800.dat", "ms69500.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_6E8", 0x0000, 73, 6, 60, 8, 1, 10, 0, "br3000", "Sepith_46D7", 30, 40, 20, 10,
        (
            ("ms63500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms63500.dat", "ms63500.dat", "ms63400.dat", "ms63500.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    BattleInfo(
        "BattleInfo_940", 0x0000, 73, 6, 60, 8, 1, 60, 0, "br3000", "Sepith_46EF", 30, 40, 20, 10,
        (
            ("ms75600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms75600.dat", "ms75600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
            ("ms75600.dat", "ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, 0, "MonsterBattlePostion_580", "MonsterBattlePostion_600", "ed7450", "ed7453", "ATBonus_540"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_A08", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "ms63400.dat", "MonsterBattlePostion_5A0", "MonsterBattlePostion_600", "ed7451", "ed7453", "ATBonus_540"),
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
        "monster/ch66850.itc",               # 10
        "monster/ch66851.itc",               # 11
        "monster/ch63550.itc",               # 12
        "monster/ch63550.itc",               # 13
        "monster/ch63450.itc",               # 14
        "monster/ch63450.itc",               # 15
        "monster/ch69550.itc",               # 16
        "monster/ch69550.itc",               # 17
        "monster/ch75650.itc",               # 18
        "monster/ch75651.itc",               # 19
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-33919,  -1399,   2369,    0,    484,  0x0, 0,   20,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-48580,  33400,   -2000,   0x1010000,    "BattleInfo_878", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-61000,  11790,   -2000,   0x1010000,    "BattleInfo_7B0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-9170,   -11260,  6000,    0x1010000,    "BattleInfo_620", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(990,     -1770,   6000,    0x1010000,    "BattleInfo_6E8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(12630,   -29610,  6000,    0x1010000,    "BattleInfo_7B0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(24750,   -32600,  6000,    0x1010000,    "BattleInfo_878", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(46240,   -12720,  6000,    0x1010000,    "BattleInfo_620", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-11670,  20490,   6000,    0x1010000,    "BattleInfo_7B0", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(25610,   11790,   14000,   0x1010000,    "BattleInfo_6E8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(51790,   19370,   14000,   0x1010000,    "BattleInfo_878", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-48580,  33400,   -2000,   0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-61000,  11790,   -2000,   0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-9170,   -11260,  6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(990,     -1770,   6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(12630,   -29610,  6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(24750,   -32600,  6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(46240,   -12720,  6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-11670,  20490,   6000,    0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(25610,   11790,   14000,   0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(51790,   19370,   14000,   0x1010000,    "BattleInfo_940", 0,   24,  0xFFFF, 8,  9)

    DeclActor(39430,   14100,   1210,    1200,    39430,   15100,   1210,    0x007C, 0,  3,  0x0000)
    DeclActor(-33920,  -1900,   2370,    1200,    -33920,  -900,    2370,    0x007C, 0,  4,  0x0000)
    DeclActor(50000,   6100,    -10000,  1200,    50000,   7100,    -10000,  0x007C, 0,  5,  0x0000)

    PlaceName(-84.0, 0.0, 48.0, 0x0000, 0x0000, "阿尔摩利卡古道方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 9

    ScpFunction((
        "Function_0_B08",          # 00, 0
        "Function_1_B27",          # 01, 1
        "Function_2_BDC",          # 02, 2
        "Function_3_1935",         # 03, 3
        "Function_4_1A70",         # 04, 4
        "Function_5_1C6E",         # 05, 5
        "Function_6_1DA9",         # 06, 6
        "Function_7_1DAD",         # 07, 7
        "Function_8_3F82",         # 08, 8
        "Function_9_3FC1",         # 09, 9
        "Function_10_4000",        # 0A, 10
        "Function_11_403F",        # 0B, 11
        "Function_12_407E",        # 0C, 12
        "Function_13_40BD",        # 0D, 13
        "Function_14_40FC",        # 0E, 14
        "Function_15_413B",        # 0F, 15
        "Function_16_465B",        # 10, 16
    ))


    def Function_0_B08(): pass

    label("Function_0_B08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_B26")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_B08")

    label("loc_B26")

    Return()

    # Function_0_B08 end

    def Function_1_B27(): pass

    label("Function_1_B27")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_B3E")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 7)
    Jump("loc_B4D")

    label("loc_B3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_B4D")
    ClearScenarioFlags(0x22, 1)
    Event(0, 15)

    label("loc_B4D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA9")
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    Jump("loc_BDB")

    label("loc_BA9")

    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)

    label("loc_BDB")

    Return()

    # Function_1_B27 end

    def Function_2_BDC(): pass

    label("Function_2_BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_BF1")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_BF1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_CD8")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x190, 0x0)
    ClearMapObjFlags(0x4, 0x4)
    ClearMapObjFlags(0x5, 0x4)
    ClearMapObjFlags(0x6, 0x4)
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
    Jump("loc_D98")

    label("loc_CD8")

    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x6, 0x4)
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

    label("loc_D98")

    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1C, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1A, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1B, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CC")
    OP_70(0x0, 0x0)
    Jump("loc_18D0")

    label("loc_18CC")

    OP_70(0x0, 0x1E)

    label("loc_18D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18E3")
    OP_70(0x1, 0x0)
    Jump("loc_18E7")

    label("loc_18E3")

    OP_70(0x1, 0x1E)

    label("loc_18E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18FA")
    OP_70(0x2, 0x0)
    Jump("loc_18FE")

    label("loc_18FA")

    OP_70(0x2, 0x1E)

    label("loc_18FE")

    OP_1C(0x0, 0x24, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x25, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x26, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_2_BDC end

    def Function_3_1935(): pass

    label("Function_3_1935")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A27")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅲ', 1)"), scpexpr(EXPR_END)), "loc_19B8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F4, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1A22")

    label("loc_19B8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅲ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1A22")

    Jump("loc_1A64")

    label("loc_1A27")

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

    label("loc_1A64")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1935 end

    def Function_4_1A70(): pass

    label("Function_4_1A70")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C30")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B6D")
    OP_A7(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x12, 0x0, 0)
    OP_98(0x12, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1ACD():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1ACD)

    def lambda_1AE7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x12, 2, lambda_1AE7)
    ClearChrFlags(0x12, 0x80)
    SetChrFlags(0x12, 0x8000)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x12, 1)
    Battle("BattleInfo_A08", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x12, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1B4E"),
        (2, "loc_1B5D"),
        (1, "loc_1B6A"),
        (SWITCH_DEFAULT, "loc_1B6D"),
    )


    label("loc_1B4E")

    SetScenarioFlags(0x217, 5)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1B6D")

    label("loc_1B5D")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1B6A")

    OP_B9(0x0)
    Return()

    label("loc_1B6D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ３', 1)"), scpexpr(EXPR_END)), "loc_1BC4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F4, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1C2B")

    label("loc_1BC4")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ３'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1C2B")

    Jump("loc_1C62")

    label("loc_1C30")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_1C62")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1A70 end

    def Function_5_1C6E(): pass

    label("Function_5_1C6E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D60")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('骑士护腿', 1)"), scpexpr(EXPR_END)), "loc_1CF1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '骑士护腿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F4, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1D5B")

    label("loc_1CF1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '骑士护腿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, '骑士护腿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1D5B")

    Jump("loc_1D9D")

    label("loc_1D60")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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

    label("loc_1D9D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1C6E end

    def Function_6_1DA9(): pass

    label("Function_6_1DA9")

    Call(1, 6)
    Return()

    # Function_6_1DA9 end

    def Function_7_1DAD(): pass

    label("Function_7_1DAD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch31400.itc", 0x1F)
    LoadChrToIndex("chr/ch31500.itc", 0x20)
    LoadChrToIndex("chr/ch12500.itc", 0x21)
    LoadChrToIndex("apl/ch51705.itc", 0x22)
    LoadChrToIndex("apl/ch50237.itc", 0x23)
    SoundLoad(3272)
    SoundLoad(3273)
    SoundLoad(3274)
    SoundLoad(3256)
    SoundLoad(3257)
    SoundLoad(3258)
    SoundLoad(3259)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis283.itp")
    SetChrSubChip(0x107, 0x5)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x21)
    SetChrSubChip(0xB, 0x0)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x20)
    SetChrSubChip(0xC, 0x0)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x21)
    SetChrSubChip(0xD, 0x0)
    ClearChrFlags(0xD, 0x80)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x20)
    SetChrSubChip(0xE, 0x0)
    ClearChrFlags(0xE, 0x80)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x21)
    SetChrSubChip(0xF, 0x0)
    ClearChrFlags(0xF, 0x80)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x20)
    SetChrSubChip(0x10, 0x0)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x8000)
    SetMapObjFlags(0x26, 0x4)
    SetChrPos(0xA, 64000, 14000, 7400, 90)
    SetChrPos(0xB, 61500, 14000, 6900, 90)
    SetChrPos(0xC, 61000, 14000, 7900, 90)
    SetChrPos(0xD, 59000, 14000, 7400, 90)
    SetChrPos(0xE, 57000, 14000, 7900, 90)
    SetChrPos(0xF, 56000, 14000, 6900, 90)
    SetChrPos(0x10, 54500, 14000, 7200, 90)
    OP_68(90290, 21000, 26800, 0)
    MoveCamera(78, 8, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20000, 0)
    OP_68(68650, 16250, 7000, 10000)
    MoveCamera(90, 20, 0, 10000)
    OP_6E(510, 10000)
    SetCameraDistance(30000, 10000)
    PlayBGM("ed7563", 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(4000)
    BeginChrThread(0xA, 1, 0, 8)
    BeginChrThread(0xB, 1, 0, 9)
    BeginChrThread(0xC, 1, 0, 10)
    BeginChrThread(0xD, 1, 0, 11)
    BeginChrThread(0xE, 1, 0, 12)
    BeginChrThread(0xF, 1, 0, 13)
    BeginChrThread(0x10, 1, 0, 14)
    OP_6F(0x79)
    Fade(500)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    EndChrThread(0xD, 0x1)
    EndChrThread(0xE, 0x1)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x10, 0x1)
    SetChrPos(0x101, 48000, 14000, 20000, 45)
    SetChrPos(0x103, 47250, 14000, 19000, 45)
    SetChrPos(0x105, 48750, 14000, 19000, 0)
    SetChrPos(0x107, 48000, 14000, 17500, 0)
    SetChrPos(0x106, 48000, 14000, 23300, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x8, 50000, 14000, 22100, 225)
    SetChrPos(0x9, 51000, 14000, 21100, 225)
    OP_52(0x101, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x101, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x103, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x105, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x107, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x106, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x106, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x106, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x41A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(48550, 15000, 21800, 0)
    MoveCamera(50, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20760, 0)
    SetCameraDistance(19760, 1500)
    OP_0D()
    OP_6F(0x79)

    #C0011
    ChrTalk(
        0x101,
        (
            "#00006F#6P原来如此……\x02\x03",

            "#00001F自那起袭击事件之后，\x01",
            "你们一直都潜伏在这一带啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x8,
        (
            "#03204F#5P嗯，教团旧址就在此地，\x01",
            "这里是个很好的藏身之处。\x02\x03",

            "#03210F我们还看到『蛇』的人员\x01",
            "在这里安置了一口巨大的钟。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        "#00201F#6P那个博士所在的现场吗……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(500)
    SetMessageWindowPos(0, 170, -1, -1)

    #A0014
    AnonymousTalk(
        0x105,
        (
            "#10403F就是原本放置在中央广场，\x01",
            "在完成『零之至宝』的仪式中\x01",
            "所使用的那口大钟吧。\x02\x03",

            "#10401F我想那肯定是\x01",
            "某种古代遗物。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    #C0015
    ChrTalk(
        0x9,
        (
            "#11P顺便一说，那口钟已经被撤走，\x01",
            "好像运送回克洛斯贝尔市了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x9,
        (
            "#11P如今仍然留在此地的，\x01",
            "只剩下我们『黑月』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        "#11P当然还有『银』大人。\x02",
    )

    CloseMessageWindow()

    def lambda_23E3():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_23E3)
    Sleep(50)

    def lambda_23F3():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_23F3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    def lambda_240B():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_240B)
    Sleep(50)

    def lambda_241B():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_241B)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    #C0018
    ChrTalk(
        0x106,
        "#10708F#11P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x101,
        "#00008F#12P莉夏……\x02",
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x106)
    TurnDirection(0x106, 0x101, 500)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x3)
    OP_0D()
    Sleep(150)

    #C0020
    ChrTalk(
        0x106,
        (
            "#10706F#5P……罗伊德警官，\x01",
            "这次请你放过我吧。\x02\x03",

            "#10708F我曾在此地做出过\x01",
            "很多违法行为……\x02\x03",

            "#10711F我并不想遭到逮捕，\x01",
            "不过为了不再给你们造成更多的麻烦，\x01",
            "我打算返回卡尔瓦德。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A0(0x106, 1500, 0x3, 0x5)
    Sleep(300)

    #C0021
    ChrTalk(
        0x106,
        "#10703F#5P……但在那之前，我一定要把该了结的事情做个了结。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0022
    ChrTalk(
        0x103,
        "#00208F#12P这是指……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        "#00006F#12P……是指复仇吧。\x02",
    )

    CloseMessageWindow()
    Sleep(50)
    OP_A0(0x106, 1300, 0x5, 0x3)
    Sleep(100)

    #C0024
    ChrTalk(
        0x106,
        "#10708F#5P#30W……………………………………\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x106, 0x2)
    OP_93(0x106, 0x0, 0x1F4)
    Sleep(300)

    #C0025
    ChrTalk(
        0x106,
        (
            "#10703F#11P#30W那些人……\x01",
            "夺去了我最重要的东西。\x02\x03",

            "把大家的太阳……\x01",
            "把那无可替代的希望……\x02\x03",

            "#10708F我绝对……\x01",
            "绝对不能饶恕他们。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0xE1, 0x1F4)
    Sleep(300)

    #C0026
    ChrTalk(
        0x8,
        (
            "#03204F#5P呵呵，『银』大人和我们重新签署了\x01",
            "之前已经撕毁的契约。\x02\x03",

            "#03210F这都是为了协力对抗\x01",
            "共同的强敌『赤色星座』。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x101,
        "#00006F#6P……你就别插嘴了。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0028
    ChrTalk(
        0x101,
        (
            "#00003F#12P莉夏。\x02\x03",

            "#00001F你知道吗？\x01",
            "伊莉娅小姐已经醒过来了。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x106, 0x101, 500)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 0x22)
    OP_A0(0x106, 1500, 0x7, 0x8)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0029
    ChrTalk(
        0x106,
        (
            "#10712F#5P#4S！！？\x02\x03",

            "#10707F#3S真、真的吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#00204F#12P是的，在异变发生之后不久，\x01",
            "她就恢复了意识。\x02\x03",

            "#00202F虽然还没有彻底痊愈……\x01",
            "但看起来很有精神。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A0(0x106, 1200, 0x1B, 0x1C)
    Sleep(200)

    #C0031
    ChrTalk(
        0x106,
        (
            "#10704F#5P#40W……啊啊，女神爱德丝……\x02\x03",

            "#10710F#40W………谢谢您………\x01",
            "感谢您的慈悲……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    #C0032
    ChrTalk(
        0x8,
        (
            "#03204F#11P呵呵，这真是个好消息啊。\x02\x03",

            "#03210F但据我所知，她的下半身失去了知觉，\x01",
            "恐怕已经没希望重回舞台了。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    OP_A1(0x106, 0x5DC, 0x3, 0x1C, 0x1B, 0x3)
    Sleep(100)

    #C0033
    ChrTalk(
        0x106,
        "#10708F#5P唔……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#00013F#6P你……\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x105,
        (
            "#10401F#12P你似乎早就掌握到了\x01",
            "这个情报啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x8,
        (
            "#03204F#11P嗯，『银』大人自己说过，\x01",
            "不想知道那方面的消息。\x02\x03",

            "#03210F所以我便斗胆隐瞒了下来。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    SetChrSubChip(0x106, 0xA)
    Sleep(150)

    #C0037
    ChrTalk(
        0x106,
        "#10701F#5P………………（瞪）\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x9,
        "#11P曹先生……何必这样说呢。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x9,
        (
            "#11P『银』大人，\x01",
            "请不要误解。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x9,
        (
            "#11P曹先生只是不想让您消沉，\x01",
            "所以才会……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    SetChrSubChip(0x106, 0x3)
    Sleep(300)

    #C0041
    ChrTalk(
        0x106,
        (
            "#10703F#5P……不必辩解了。\x02\x03",

            "#10708F还有，无论听到什么，\x01",
            "我的决心也不会改变。\x02\x03",

            "#10711F将事情彻底了结之后……\x01",
            "我才会离开克洛斯贝尔。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x9,
        "#11P…………………………\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x8,
        (
            "#03204F#11P呵呵，对我们来说，\x01",
            "真是值得庆幸啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0044
    ChrTalk(
        0x8,
        (
            "#03200F#5P罗伊德警官，\x01",
            "虽然我们的目的有所不同，\x01",
            "但需要面对的敌人却是一样的。\x02\x03",

            "#03209F因此我希望各位务必与我们\x01",
            "缔结合作关系。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x2D, 0x1F4)
    Sleep(300)

    #C0045
    ChrTalk(
        0x101,
        "#00001F#6P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x101)

    #C0046
    ChrTalk(
        0x101,
        (
            "#00006F#6P嗯，我没有异议。\x02\x03",

            "#00000F不过，\x01",
            "我要带走莉夏。\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xFA0)
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2DCE():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2DCE)
    Sleep(0)

    def lambda_2DDE():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2DDE)
    Sleep(0)

    def lambda_2DEE():
        TurnDirection(0x107, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2DEE)
    Sleep(0)

    def lambda_2DFE():
        TurnDirection(0x8, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2DFE)
    Sleep(0)

    def lambda_2E0E():
        TurnDirection(0x9, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2E0E)
    Sleep(0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    #C0047
    ChrTalk(
        0x106,
        "#10705F#5P……！？\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#00205F#6P罗伊德前辈……\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x8,
        "#03201F#5P………哦？\x02",
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    OP_68(48580, 15000, 22190, 60000)
    MoveCamera(46, 21, 0, 60000)
    SetCameraDistance(18740, 60000)
    PlayBGM("ed7568", 0)
    OP_93(0x101, 0x0, 0x1F4)
    Sleep(300)

    #C0050
    ChrTalk(
        0x101,
        (
            "#00001F#12P莉夏，伊莉娅小姐\x01",
            "让我们传话给你。\x02\x03",

            "#00003F『对你来说，\x01",
            "  什么才是最重要的？』\x02\x03",

            "『面对那重要之物，\x01",
            "  你能不为之努力吗？』\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0051
    ChrTalk(
        0x106,
        "#10712F#5P#30W…………啊……………\x02",
    )

    CloseMessageWindow()

    def lambda_2F85():
        TurnDirection(0x101, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2F85)
    Sleep(0)

    def lambda_2F95():
        TurnDirection(0x103, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2F95)
    Sleep(0)

    def lambda_2FA5():
        TurnDirection(0x105, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_2FA5)
    Sleep(0)

    def lambda_2FB5():
        TurnDirection(0x107, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_2FB5)
    Sleep(0)

    def lambda_2FC5():
        TurnDirection(0x106, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2FC5)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    WaitChrThread(0x106, 0)

    def lambda_2FE9():
        OP_93(0x8, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 0, lambda_2FE9)
    Sleep(50)

    def lambda_2FF9():
        OP_93(0x9, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_2FF9)
    Sleep(50)
    WaitChrThread(0x8, 0)
    WaitChrThread(0x9, 0)

    #C0052
    ChrTalk(
        0x101,
        (
            "#00003F#12P伊莉娅小姐她……\x01",
            "完全没有消沉。\x02\x03",

            "#00008F一开始，我本以为\x01",
            "她只是在拼命逞强，\x01",
            "内心其实非常不安……\x02\x03",

            "#00000F但随后却发现……她好像真的\x01",
            "坚信自己一定能重登舞台。\x02\x03",

            "#00004F而且，她完全了解\x01",
            "那有多么困难。\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x106,
        "#10708F#5P#30W………………………………\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x105,
        (
            "#10406F#12P老实说，能如此坚定地贯彻\x01",
            "自己的信念，实在是一件很不容易的事……\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x103,
        (
            "#00204F#12P仅仅是听了她的一番话，\x01",
            "我们便感到勇气倍增。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x8,
        "#03201F#11P………………………………\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x101,
        (
            "#00003F#12P伊莉娅小姐以重返舞台为目标，\x01",
            "正在拼命努力……\x02\x03",

            "#00001F对你来说，\x01",
            "最重要的又是什么呢？\x02\x03",

            "是向『赤色星座』复仇？\x02\x03",

            "继承『银』的道路？\x02\x03",

            "还是……\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x106, 0x2)
    OP_0D()
    OP_93(0x106, 0x0, 0x190)

    def lambda_3280():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_3280)
    WaitChrThread(0x106, 2)
    Sleep(500)

    def lambda_32A0():
        OP_A6(0xFE, 0x0, 0x1E, 0x190, 0x7D0)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_32A0)
    WaitChrThread(0x106, 2)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #C0058
    ChrTalk(
        0x106,
        (
            "#10708F#3272V#11P#40W#20A………这种问题…………\x02\x03",

            "#3273V#48A我又怎有……\x01",
            "我又怎有资格回答。\x02\x03",

            "#10706F#3274V#52A……双手染满鲜血……\x01",
            "成长在黑暗中的我……\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    Sleep(300)

    #C0059
    ChrTalk(
        0x101,
        (
            "#00006F#12P不要转移话题，莉夏。\x02\x03",

            "#00013F我在问你，对你来说，\x01",
            "什么才是最重要的？\x02\x03",

            "你发自内心地渴求……\x01",
            "不惜一切代价也要去\x01",
            "争取的重要之物究竟是什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0060
    ChrTalk(
        0x106,
        "#10708F#11P呜……！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 500)
    Fade(250)
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 0x22)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x0, 0xA)
    SetCameraDistance(16740, 500)
    OP_A0(0x106, 2000, 0xC, 0xE)
    Sleep(300)
    OP_C9(0x0, 0x80000000)

    #C0061
    ChrTalk(
        0x106,
        (
            "#10713F#3256V#4S#5P#30A那……\x01",
            "那当然是彩虹剧团！\x02",
        )
    )
    #Auto

    OP_6F(0x10)
    OP_82(0xC8, 0x0, 0xBB8, 0x320)
    CloseMessageWindow()
    MoveCamera(42, 21, 0, 12000)
    OP_A0(0x106, 1200, 0xE, 0x13)
    OP_A0(0x106, 1200, 0x13, 0x11)
    Sleep(300)

    #C0062
    ChrTalk(
        0x106,
        (
            "#10714F#3257V#5P#40A我还……\x01",
            "我还想站在那舞台上跳舞！\x02\x03",

            "#3258V#40A和伊莉娅小姐、修利，\x01",
            "还有剧团的各位一起！\x02\x03",

            "#10713F#3259V#30A我的愿望……只有这个而已！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    SetCameraDistance(17690, 800)
    OP_6F(0x79)
    CancelBlur(0)
    Sleep(300)

    #C0063
    ChrTalk(
        0x103,
        "#00214F#12P啊……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x105,
        "#10404F#12P……呵呵…………\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x101,
        "#00002F#12P……是吗。\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x8,
        "#03201F#11P………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x8)

    #C0067
    ChrTalk(
        0x9,
        "#11P……曹先生。\x02",
    )

    CloseMessageWindow()

    def lambda_361F():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_361F)
    Sleep(50)

    def lambda_362F():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_362F)
    Sleep(50)

    def lambda_363F():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_363F)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    OP_A0(0x106, 1500, 0x14, 0x15)
    Sleep(150)

    #C0068
    ChrTalk(
        0x106,
        "#10708F#5P…………啊……………\x02",
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x101,
        "#00013F#6P………………………………\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A0(0x106, 1500, 0x15, 0x17)
    Sleep(150)

    #C0070
    ChrTalk(
        0x8,
        "#03204F#60W#2S#11P#32A……哼哼……哈哈哈……\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    SetCameraDistance(18690, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)

    #C0071
    ChrTalk(
        0x8,
        "#03209F#4S#11P#50A啊哈哈哈哈哈哈哈哈哈！！\x02",
    )
    #Auto

    CloseMessageWindow()
    Sleep(150)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0072
    ChrTalk(
        0x8,
        (
            "#03210F#5P呵呵……真不愧是罗伊德警官。\x02\x03",

            "三言两语就把我的计划\x01",
            "彻底打乱了。\x02\x03",

            "#03203F不，应该说是伊莉娅小姐\x01",
            "的胜利才对吧……\x02\x03",

            "#03202F是我输了……\x01",
            "嗯，彻底输了！\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x106,
        "#10708F#5P曹先生……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        "#00006F#6P……你不想再说什么了吗？\x02",
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x8,
        (
            "#03202F#5P呵呵，老实说，\x01",
            "我从来没有如此恼火过……\x02\x03",

            "#03204F不过今后还要继续协作，\x01",
            "这次我就退让一步吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x8, 0x10E, 0x1F4)
    Sleep(300)

    #C0076
    ChrTalk(
        0x8,
        (
            "#03204F#11P『银』大人……\x01",
            "不，莉夏·毛小姐。\x02\x03",

            "你与『黑月』签署的契约\x01",
            "就此作废。\x02\x03",

            "#03200F今后要去什么地方，都是你的自由了。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x106,
        (
            "#10712F#5P啊……\x02\x03",

            "#10710F……曹先生，\x01",
            "谢谢你。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x8,
        (
            "#03210F#11P我只是放弃了\x01",
            "这次的契约而已。\x02\x03",

            "#03203F但我……\x01",
            "我们『黑月』要想进一步发展，\x01",
            "还是需要借助你的力量。\x02\x03",

            "#03210F总之你就先\x01",
            "努力重返舞台吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_A0(0x106, 1200, 0x17, 0x19)
    Sleep(300)

    #C0079
    ChrTalk(
        0x106,
        (
            "#10704F#5P……嗯，\x01",
            "我一定不会放弃的。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(48720, 15000, 21530, 2000)
    MoveCamera(51, 21, 0, 2000)
    OP_6E(510, 2000)
    SetCameraDistance(19710, 2000)
    StopBGM(0x1770)
    Sleep(500)
    OP_A0(0x106, 1000, 0x19, 0x17)
    OP_6F(0x79)
    Sleep(300)

    #C0080
    ChrTalk(
        0x101,
        "#00006F#5P呼……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x103,
        (
            "#00204F#6P……罗伊德前辈，\x01",
            "你辛苦了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 500)
    Sleep(100)

    #C0082
    ChrTalk(
        0x105,
        (
            "#10402F#11P呵呵，你竟然能在\x01",
            "这种局面下成功挖角。\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x107,
        (
            "#01203F#12P#3C嗯……真不愧是\x01",
            "能让身为至宝的圣子牵挂的人啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x107, 500)
    Sleep(100)

    #C0084
    ChrTalk(
        0x101,
        (
            "#00012F#5P哪、哪里哪里，\x01",
            "我只不过是传句话而已。\x02\x03",

            "#00002F能顺利转达……\x01",
            "真是太好了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x23)
    OP_A1(0x8, 0x514, 0x4, 0x0, 0x1, 0x2, 0x3)
    Sound(318, 0, 100, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7114", 0)
    Sleep(500)

    #C0085
    ChrTalk(
        0x8,
        (
            "#03203F#11P话说回来，罗伊德警官。\x02\x03",

            "#03201F我的满腔愤懑\x01",
            "又该向何处发泄呢？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3C19():
        TurnDirection(0x101, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3C19)
    Sleep(0)

    def lambda_3C29():
        TurnDirection(0x103, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_3C29)
    Sleep(0)

    def lambda_3C39():
        TurnDirection(0x105, 0x8, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_3C39)
    Sleep(0)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)

    #C0086
    ChrTalk(
        0x101,
        "#00005F#6P哎哎……？\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_A1(0x8, 0x5DC, 0x3, 0x2, 0x1, 0x0)
    Sleep(50)
    SetChrChipByIndex(0x8, 0x1E)
    Sleep(300)
    TurnDirection(0x8, 0x101, 500)
    Sleep(150)

    #C0087
    ChrTalk(
        0x8,
        (
            "#03204F#5P唔，有了。\x02\x03",

            "#03202F作为抢走莉夏小姐的补偿，\x01",
            "你就加入我们『黑月』吧。\x02\x03",

            "#03209F你似乎很有潜质，努力锻炼后，\x01",
            "相信一定能成为很出色的战力。\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0x101,
        "#00011F#6P咦咦！？\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x106,
        "#10705F#5P曹、曹先生！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 500)
    Sleep(100)

    #C0090
    ChrTalk(
        0x9,
        "#11P嗯，确实。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x9,
        (
            "#11P如果用心修炼我们的拳法，\x01",
            "你的旋棍技术应该也能\x01",
            "提升到更高的境界。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x101,
        (
            "#00012F#6P不、不用了！\x01",
            "好意还是心领了！\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0x105,
        (
            "#10402F#12P呵呵，你很受欢迎嘛。\x02\x03",

            "#10409F既然如此，我也不该落于人后，\x01",
            "不然就邀请你加入骑士团好了。\x02",
        )
    )

    CloseMessageWindow()

    #C0094
    ChrTalk(
        0x103,
        (
            "#00211F#6P……瓦吉先生，\x01",
            "不要开玩笑了。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(21210, 2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "就这样，罗伊德等人与『黑月』\x01",
            "结成了暂时性的合作关系……\x02\x03",

            "双方约定，在遇到情况时\x01",
            "会互相协助，在获得新情报时\x01",
            "也会通知对方。\x02\x03",

            "而『银』──莉夏·毛……\x02\x03",

            "为了达成自己新的目的，\x01",
            "决定协助罗伊德等人。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 4)
    NewScene("e4300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1DAD end

    def Function_8_3F82(): pass

    label("Function_8_3F82")

    OP_95(0xFE, 69000, 14000, 7400, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3FA0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FA0)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_8_3F82 end

    def Function_9_3FC1(): pass

    label("Function_9_3FC1")

    OP_95(0xFE, 69000, 14000, 6900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_3FDF():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_3FDF)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_9_3FC1 end

    def Function_10_4000(): pass

    label("Function_10_4000")

    OP_95(0xFE, 69000, 14000, 7900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_401E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_401E)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_10_4000 end

    def Function_11_403F(): pass

    label("Function_11_403F")

    OP_95(0xFE, 69000, 14000, 7400, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_405D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_405D)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_11_403F end

    def Function_12_407E(): pass

    label("Function_12_407E")

    OP_95(0xFE, 69000, 14000, 7900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_409C():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_409C)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_12_407E end

    def Function_13_40BD(): pass

    label("Function_13_40BD")

    OP_95(0xFE, 69000, 14000, 6900, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_40DB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_40DB)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_13_40BD end

    def Function_14_40FC(): pass

    label("Function_14_40FC")

    OP_95(0xFE, 69000, 14000, 7200, 2000, 0x0)
    ClearChrFlags(0xFE, 0x4)

    def lambda_411A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_411A)
    OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x4)
    Return()

    # Function_14_40FC end

    def Function_15_413B(): pass

    label("Function_15_413B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch06300.itc", 0x1E)
    LoadChrToIndex("chr/ch03200.itc", 0x1F)
    LoadChrToIndex("chr/ch31400.itc", 0x20)
    SoundLoad(3254)
    SoundLoad(3255)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10700.itp")
    OP_68(72390, 24300, 23330, 0)
    MoveCamera(80, 14, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(15240, 0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, 72600, 18000, 21400, 90)
    ClearChrFlags(0x8, 0x80)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrPos(0x11, 80270, 18000, 21350, 40)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 71580, 18000, 20440, 90)
    ClearChrFlags(0x9, 0x80)
    OP_68(72390, 22500, 23330, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)

    #C0096
    ChrTalk(
        0x11,
        "#10708F……………………………………\x02",
    )

    CloseMessageWindow()

    #N0097
    NpcTalk(
        0x8,
        "青年的声音",
        (
            "#1P呵呵，看到了\x01",
            "很有趣的场面呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(69460, 22600, 20450, 3000)
    MoveCamera(83, 18, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(11200, 3000)

    def lambda_430A():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_430A)
    Sleep(50)

    def lambda_4322():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4322)
    WaitChrThread(0x9, 1)
    OP_6F(0x79)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0098
    AnonymousTalk(
        0x8,
        (
            "多亏他们，我们就不用\x01",
            "费力气做扫除了。\x02\x03",

            "真该好好感谢他们啊。\x02",
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

    #C0099
    ChrTalk(
        0x11,
        "#10703F……………………………………\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x11, 500)
    Sleep(300)

    #C0100
    ChrTalk(
        0x8,
        (
            "#03204F#6P怎么了？\x01",
            "莉夏小姐……不，『银』大人。\x02\x03",

            "#03200F再次与我们签署契约……\x01",
            "你开始后悔了吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x11, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x11)
    TurnDirection(0x11, 0x8, 500)
    Sleep(300)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)
    OP_C9(0x0, 0x80000000)

    #A0101
    AnonymousTalk(
        0x11,
        (
            "#3254V#30W……没有的事。\x02\x03",

            "#3255V#30W现在需要静待时机……\x01",
            "我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_24(0xCB7)
    OP_C9(0x1, 0x80000000)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0102
    ChrTalk(
        0x9,
        "#12P『银』大人……\x02",
    )

    CloseMessageWindow()

    #C0103
    ChrTalk(
        0x8,
        (
            "#03209F#6P呵呵……很好。\x02\x03",

            "#03204F为了对抗『他们』，\x01",
            "我们需要你的力量。\x02\x03",

            "#03210F今后就请\x01",
            "继续关照了。\x02",
        )
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 16)
    Sleep(1500)
    BeginChrThread(0x9, 3, 0, 16)
    Sleep(100)
    BeginChrThread(0x11, 3, 0, 16)
    Sleep(500)
    OP_68(69460, 23700, 20450, 5000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    Sleep(1000)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetScenarioFlags(0x22, 1)
    NewScene("t2520", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_15_413B end

    def Function_16_465B(): pass

    label("Function_16_465B")

    OP_93(0xFE, 0x10E, 0x1F4)
    OP_95(0xFE, 72030, 18000, 20890, 2000, 0x0)
    OP_95(0xFE, 71490, 18000, 16230, 2000, 0x0)
    OP_95(0xFE, 67840, 16920, 16270, 2000, 0x0)
    Return()

    # Function_16_465B end

    SaveToFile()

Try(main)
