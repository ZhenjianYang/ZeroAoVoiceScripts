from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m9061.bin",                # FileName
        "m9061",                    # MapName
        "m9061",                    # Location
        0x00C1,                     # MapIndex
        "ed7354",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2A,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 193, 0, 1, 0, 2],
    )

    BuildStringList((
        "m9061",                  # 0
        "测试用",                 # 1
        "bm9041",                 # 2
        "bm9041",                 # 3
        "bm9041",                 # 4
    ))

    ATBonus("ATBonus_2F8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_308", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_1022", 13,  8,   11,  6,   3,   5,   12)
    Sepith("Sepith_101A", 17,  9,   7,   6,   13,  9,   9)

    MonsterBattlePostion("MonsterBattlePostion_328", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_348", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 8, 14, 180)

    # monster count: 10

    BattleInfo(
        "BattleInfo_490", 0x0000, 103, 6, 60, 6, 1, 30, 0, "bm9041", "Sepith_1022", 40, 30, 20, 10,
        (
            ("ms85800.dat", "ms85800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_328", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_2F8"),
            ("ms85800.dat", "ms85800.dat", "ms85800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_348", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_2F8"),
            ("ms85800.dat", "ms85800.dat", "ms85800.dat", "ms85800.dat", 0, 0, 0, 0, "MonsterBattlePostion_328", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_2F8"),
            ("ms85800.dat", "ms85800.dat", "ms85800.dat", "ms85800.dat", "ms85800.dat", 0, 0, 0, "MonsterBattlePostion_348", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_2F8"),
        )
    )

    BattleInfo(
        "BattleInfo_3C8", 0x0000, 103, 6, 60, 6, 1, 30, 0, "bm9041", "Sepith_101A", 40, 30, 20, 10,
        (
            ("ms80400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_348", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_2F8"),
            ("ms80400.dat", "ms85800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_328", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_2F8"),
            ("ms80400.dat", "ms85800.dat", "ms85800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_348", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_2F8"),
            ("ms80400.dat", "ms85800.dat", "ms80400.dat", "ms85800.dat", 0, 0, 0, 0, "MonsterBattlePostion_328", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_2F8"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_558", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm9041", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80400.dat", "ms85800.dat", "ms80400.dat", "ms85800.dat", "ms80400.dat", "ms85800.dat", "ms85800.dat", "ms80400.dat", "MonsterBattlePostion_328", "MonsterBattlePostion_3A8", "ed7452", "ed7453", "ATBonus_308"),
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
        "chr/ch00000.itc",                   # 10
        "chr/ch00000.itc",                   # 11
        "monster/ch80450.itc",               # 12
        "monster/ch80451.itc",               # 13
        "monster/ch85850.itc",               # 14
        "monster/ch85851.itc",               # 15
    ))

    DeclNpc(188000,  500,     37000,   0,    484,  0x0, 0,   18,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(13030,   29020,   0,       0x10100B4,    "BattleInfo_490", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(12060,   19830,   0,       0x10100B4,    "BattleInfo_490", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(23500,   16120,   0,       0x101010E,    "BattleInfo_490", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(27910,   -1670,   0,       0x1010168,    "BattleInfo_490", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(41000,   17310,   0,       0x10100AD,    "BattleInfo_490", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(36720,   23310,   0,       0x1010081,    "BattleInfo_490", 0,   20,  0xFFFF, 2,  3)
    DeclMonster(46540,   2460,    0,       0x1010168,    "BattleInfo_3C8", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(166170,  16400,   0,       0x10100FC,    "BattleInfo_3C8", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(180690,  3300,    0,       0x1010168,    "BattleInfo_3C8", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(192130,  19550,   0,       0x10100EB,    "BattleInfo_3C8", 0,   18,  0xFFFF, 0,  1)

    DeclActor(52000,   0,       7000,    1200,    52000,   1000,    7000,    0x007C, 0,  3,  0x0000)
    DeclActor(188000,  0,       37000,   1200,    188000,  1000,    37000,   0x007C, 0,  4,  0x0000)
    DeclActor(34000,   0,       25000,   1200,    34000,   1000,    25000,   0x007C, 0,  5,  0x0000)
    DeclActor(-124000, 0,       32000,   1200,    -124000, 1000,    32000,   0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_5E8",          # 00, 0
        "Function_1_603",          # 01, 1
        "Function_2_604",          # 02, 2
        "Function_3_A16",          # 03, 3
        "Function_4_B7D",          # 04, 4
        "Function_5_D7B",          # 05, 5
        "Function_6_EB6",          # 06, 6
    ))


    def Function_0_5E8(): pass

    label("Function_0_5E8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_602")
    OP_A1(0xFE, 0x4B0, 0x4, 0x0, 0x1, 0x2, 0x3)
    Jump("Function_0_5E8")

    label("loc_602")

    Return()

    # Function_0_5E8 end

    def Function_1_603(): pass

    label("Function_1_603")

    Return()

    # Function_1_603 end

    def Function_2_604(): pass

    label("Function_2_604")

    OP_F0(0x1, 0x320)
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0xFA0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E3")
    OP_70(0x0, 0x0)
    Jump("loc_9E7")

    label("loc_9E3")

    OP_70(0x0, 0x1E)

    label("loc_9E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9FA")
    OP_70(0x1, 0x0)
    Jump("loc_9FE")

    label("loc_9FA")

    OP_70(0x1, 0x1E)

    label("loc_9FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A11")
    OP_70(0x2, 0x0)
    Jump("loc_A15")

    label("loc_A11")

    OP_70(0x2, 0x1E)

    label("loc_A15")

    Return()

    # Function_2_604 end

    def Function_3_A16(): pass

    label("Function_3_A16")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x204, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4E")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２００\x01\x07\x02",

            "#57I水之耀晶片×２００\x01\x07\x02",

            "#58I火之耀晶片×２００\x01\x07\x02",

            "#59I风之耀晶片×２００\x01\x07\x02",

            "#60I时之耀晶片×２００\x01\x07\x02",

            "#61I空之耀晶片×２００\x01\x07\x02",

            "#62I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x204, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_B6B")

    label("loc_B4E")


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

    label("loc_B6B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_A16 end

    def Function_4_B7D(): pass

    label("Function_4_B7D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3D")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x219, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7A")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_BDA():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BDA)

    def lambda_BF4():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BF4)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

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
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_558", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C5B"),
        (2, "loc_C6A"),
        (1, "loc_C77"),
        (SWITCH_DEFAULT, "loc_C7A"),
    )


    label("loc_C5B")

    SetScenarioFlags(0x219, 1)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_C7A")

    label("loc_C6A")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_C77")

    OP_B9(0x0)
    Return()

    label("loc_C7A")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x468, 1)"), scpexpr(EXPR_END)), "loc_CD1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x468),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x205, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_D38")

    label("loc_CD1")

    FadeToDark(300, 0, 100)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x468),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x468),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D38")

    Jump("loc_D6F")

    label("loc_D3D")

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

    label("loc_D6F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_B7D end

    def Function_5_D7B(): pass

    label("Function_5_D7B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x205, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6D")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xBF, 1)"), scpexpr(EXPR_END)), "loc_DFE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xBF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x205, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_E68")

    label("loc_DFE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xBF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0xBF),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E68")

    Jump("loc_EAA")

    label("loc_E6D")

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

    label("loc_EAA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_D7B end

    def Function_6_EB6(): pass

    label("Function_6_EB6")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F8B")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x3, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x3, 0x0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x3)
    OP_71(0x3, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x3, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_F8B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_6_EB6 end

    SaveToFile()

Try(main)
