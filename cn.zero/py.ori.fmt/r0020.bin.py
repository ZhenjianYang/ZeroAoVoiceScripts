from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r0020.bin",                # FileName
        "r0020",                    # MapName
        "r0020",                    # Location
        0x005E,                     # MapIndex
        "ed7204",
        0x00000000,                 # Flags
        ("r0020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 94, 0, 1, 0, 2],
    )

    BuildStringList((
        "r0020",                  # 0
        "br0000",                 # 1
        "br0000",                 # 2
        "br0000",                 # 3
        "br0000",                 # 4
        "br0000",                 # 5
        "br0000",                 # 6
        "克洛斯贝尔市方向",       # 7
        "阿尔摩利卡村·唐古拉姆门方向",# 8
    ))

    ATBonus("ATBonus_490", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_15B4", 4,   4,   4,   4,   0,   0,   0)
    Sepith("Sepith_15A4", 5,   2,   3,   0,   0,   3,   0)
    Sepith("Sepith_15AC", 1,   6,   0,   3,   2,   1,   1)
    Sepith("Sepith_15BC", 3,   0,   2,   6,   0,   0,   2)
    Sepith("Sepith_15E4", 12,  20,  10,  28,  11,  2,   5)

    MonsterBattlePostion("MonsterBattlePostion_4F0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_500", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_504", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_508", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_50C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_550", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_554", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_558", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_55C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_560", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_564", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_568", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_56C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_4D0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4D8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4DC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4E8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4EC", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_570", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_574", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_578", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_57C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_580", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_584", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_588", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_58C", 0, 0, 180)

    # monster count: 18

    BattleInfo(
        "BattleInfo_62C", 0x0000, 8, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_15B4", 30, 45, 25, 0,
        (
            ("ms63000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms63000.dat", "ms63000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms63000.dat", "ms61000.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_590", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_15A4", 30, 45, 25, 0,
        (
            ("ms66500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms66500.dat", "ms66500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms66500.dat", "ms63000.dat", "ms66500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_764", 0x0000, 8, 6, 45, 6, 1, 25, 0, "br0000", "Sepith_15AC", 30, 45, 25, 0,
        (
            ("ms69900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms69900.dat", "ms69900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms69900.dat", "ms63000.dat", "ms69900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6C8", 0x0000, 8, 6, 45, 6, 1, 75, 0, "br0000", "Sepith_15BC", 30, 45, 25, 0,
        (
            ("ms61000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms61000.dat", "ms61000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms61000.dat", "ms61000.dat", "ms63000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_800", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br0000", "Sepith_15E4", 40, 35, 25, 0,
        (
            ("ms63701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4D0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            ("ms63701.dat", "ms63701.dat", "ms63701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4F0", "MonsterBattlePostion_550", "ed7400", "ed7403", "ATBonus_490"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_89C", 0x0C00, 255, 6, 0, 0, 0, 0, 0, "br0000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms77500.dat", "ms77500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_570", "MonsterBattlePostion_550", "ed7401", "ed7403", "ATBonus_490"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

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
        "monster/ch66550.itc",               # 10
        "monster/ch66551.itc",               # 11
        "monster/ch63050.itc",               # 12
        "monster/ch63050.itc",               # 13
        "monster/ch61050.itc",               # 14
        "monster/ch61050.itc",               # 15
        "monster/ch69950.itc",               # 16
        "monster/ch69950.itc",               # 17
        "monster/ch77550.itc",               # 18
        "monster/ch77550.itc",               # 19
        "monster/ch63750.itc",               # 1A
        "monster/ch63751.itc",               # 1B
    ))

    DeclMonster(6590,    11560,   0,       0x1010000,    "BattleInfo_62C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(19770,   -540,    -1790,   0x1010000,    "BattleInfo_590", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(32340,   -13180,  -2000,   0x1010000,    "BattleInfo_764", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(34430,   22750,   0,       0x1010000,    "BattleInfo_62C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(59270,   42550,   0,       0x1010000,    "BattleInfo_590", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(16120,   34420,   0,       0x1010000,    "BattleInfo_6C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(60950,   19410,   -4000,   0x1010000,    "BattleInfo_6C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(62620,   -1500,   -3610,   0x1010000,    "BattleInfo_590", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(86970,   1440,    -4000,   0x1010000,    "BattleInfo_764", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(60450,   -360,    3000,    0x1010000,    "BattleInfo_6C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(38070,   48570,   1130,    0x1010000,    "BattleInfo_62C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(131240,  60350,   4000,    0x1010000,    "BattleInfo_590", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(147670,  22420,   1000,    0x1010000,    "BattleInfo_764", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(145080,  62620,   3860,    0x1010000,    "BattleInfo_6C8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(106730,  12830,   -3080,   0x1010000,    "BattleInfo_62C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(33820,   32880,   10,      0x1010000,    "BattleInfo_800", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(110030,  47740,   1000,    0x1010000,    "BattleInfo_800", 0,   26,  0xFFFF, 8,  9)
    DeclMonster(83470,   -2040,   -3000,   0x185010E,    "BattleInfo_89C", 0,   24,  0xFFFF, 4,  5)

    DeclEvent(0x0040, 0, 7,   83.47000122070312,     -2.0399999618530273,   -5.0,                  16.0,                  [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.125,                 -0.0,                  0.0,                   0.0,                   -0.0,                  0.25,                  0.0,                   -10.43375015258789,    0.2549999952316284,    1.25,                  1.0])

    DeclActor(65950,   3000,    61070,   1200,    65950,   4000,    61070,   0x007C, 0,  3,  0x0000)
    DeclActor(151530,  1000,    22610,   1200,    151530,  2000,    22610,   0x007C, 0,  4,  0x0000)
    DeclActor(92870,   -5000,   34660,   1200,    90050,   -7000,   39730,   0x007C, 0,  9,  0x0000)
    DeclActor(72570,   0,       29130,   1200,    72570,   0,       29130,   0x007C, 0,  5,  0x0000)
    DeclActor(142060,  1500,    63090,   1200,    142060,  1500,    63090,   0x007C, 0,  6,  0x0000)

    PlaceName(-19.5, 0.0, -18.5, 0x0000, 0x0000, "克洛斯贝尔市方向")
    PlaceName(187.0, 0.0, 39.0, 0x0000, 0x0000, "阿尔摩利卡村·唐古拉姆门方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 9

    ScpFunction((
        "Function_0_980",          # 00, 0
        "Function_1_99C",          # 01, 1
        "Function_2_9A0",          # 02, 2
        "Function_3_FC6",          # 03, 3
        "Function_4_10FC",         # 04, 4
        "Function_5_1251",         # 05, 5
        "Function_6_1265",         # 06, 6
        "Function_7_1279",         # 07, 7
        "Function_8_149B",         # 08, 8
        "Function_9_14B4",         # 09, 9
    ))


    def Function_0_980(): pass

    label("Function_0_980")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_99B")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_980")

    label("loc_99B")

    Return()

    # Function_0_980 end

    def Function_1_99C(): pass

    label("Function_1_99C")

    Call(0, 8)
    Return()

    # Function_1_99C end

    def Function_2_9A0(): pass

    label("Function_2_9A0")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x18, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_NEQ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_E0E")
    SetChrFlags(0x19, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    Jump("loc_E22")

    label("loc_E0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E22")
    ClearChrFlags(0x19, 0x80)
    ModifyEventFlags(1, 0, 0x80)

    label("loc_E22")

    OP_52(0x19, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrBattleFlags(0x19, 0x100)
    OP_52(0x19, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('咪雪缎带', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "GetItemNumber('进击刻印', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('超·必胜扎头巾', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('超·斗魂腰带', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('正义徽章', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "GetItemNumber('幸运刻印', 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_E8E")
    OP_65(0x2, 0x1)

    label("loc_E8E")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 90050, -7000, 39730, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EEB")
    OP_70(0x0, 0x0)
    Jump("loc_EEF")

    label("loc_EEB")

    OP_70(0x0, 0x1E)

    label("loc_EEF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F02")
    OP_70(0x1, 0x0)
    Jump("loc_F06")

    label("loc_F02")

    OP_70(0x1, 0x1E)

    label("loc_F06")

    OP_65(0x3, 0x1)
    OP_65(0x4, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 1)), scpexpr(EXPR_END)), "loc_F6C")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 72570, 0, 29130, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)
    Jump("loc_FC5")

    label("loc_F6C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 2)), scpexpr(EXPR_END)), "loc_FC5")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 142060, 1500, 63090, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)

    label("loc_FC5")

    Return()

    # Function_2_9A0 end

    def Function_3_FC6(): pass

    label("Function_3_FC6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10B3")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('银胸针', 1)"), scpexpr(EXPR_END)), "loc_1045")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x100, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_10AE")

    label("loc_1045")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x3C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10AE")

    Jump("loc_10F0")

    label("loc_10B3")

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

    label("loc_10F0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_FC6 end

    def Function_4_10FC(): pass

    label("Function_4_10FC")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x100, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1222")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 20)
    AddSepith(0x1, 20)
    AddSepith(0x2, 20)
    AddSepith(0x3, 20)
    AddSepith(0x4, 20)
    AddSepith(0x5, 20)
    AddSepith(0x6, 20)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２０\x01\x07\x02",

            "#57I水之耀晶片×２０\x01\x07\x02",

            "#58I火之耀晶片×２０\x01\x07\x02",

            "#59I风之耀晶片×２０\x01\x07\x02",

            "#60I时之耀晶片×２０\x01\x07\x02",

            "#61I空之耀晶片×２０\x01\x07\x02",

            "#62I幻之耀晶片×２０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x100, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_123F")

    label("loc_1222")


    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么都没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_123F")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_10FC end

    def Function_5_1251(): pass

    label("Function_5_1251")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 1)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_1251 end

    def Function_6_1265(): pass

    label("Function_6_1265")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 2)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_1265 end

    def Function_7_1279(): pass

    label("Function_7_1279")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x78, 6)), scpexpr(EXPR_END)), "loc_1283")
    Return()

    label("loc_1283")

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

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "大型魔兽正在四处游荡。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【消灭】\x01",      # 0
            "【放弃】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_134F"),
        (SWITCH_DEFAULT, "loc_1366"),
    )


    label("loc_134F")

    Sleep(500)
    OP_90(0x0, 76760, -4000, 920, 135)
    EventEnd(0x5)
    Return()

    label("loc_1366")

    Battle("BattleInfo_89C", 0x0, 0x0, 0x100, 0x0, 0xFF)
    OP_E0(0x2)
    EventBegin(0x1)
    OP_68(76760, -3000, 920, 0)
    OP_90(0x0, 76760, -4000, 920, 135)
    OP_90(0x1, 76760, -4000, 920, 135)
    OP_90(0x2, 76760, -4000, 920, 135)
    OP_90(0x3, 76760, -4000, 920, 135)
    OP_90(0x4, 76760, -4000, 920, 135)
    OP_90(0x5, 76760, -4000, 920, 135)
    OP_90(0x6, 76760, -4000, 920, 135)
    OP_90(0x7, 76760, -4000, 920, 135)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_1428"),
        (1, "loc_142B"),
        (SWITCH_DEFAULT, "loc_142E"),
    )


    label("loc_1428")

    EventEnd(0x5)
    Return()

    label("loc_142B")

    OP_B7(0x0)
    Return()

    label("loc_142E")

    EventBegin(0x1)
    SetChrFlags(0x19, 0x80)
    ModifyEventFlags(0, 0, 0x80)
    OP_0D()
    Sleep(400)
    Sound(9, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "消灭了通缉魔兽！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetScenarioFlags(0x78, 6)
    OP_29(0x21, 0x4, 0x10)
    OP_29(0x21, 0x4, 0x2)
    OP_29(0x21, 0x1, 0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    EventEnd(0x5)
    Return()

    # Function_7_1279 end

    def Function_8_149B(): pass

    label("Function_8_149B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_14B3")
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)

    label("loc_14B3")

    Return()

    # Function_8_149B end

    def Function_9_14B4(): pass

    label("Function_9_14B4")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0008
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
    )

    CloseMessageWindow()
    OP_68(90520, -4400, 36960, 1500)
    MoveCamera(26, 41, 0, 1500)
    OP_6E(470, 1500)
    SetCameraDistance(23000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0009
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1577")
    OP_E0(0x2)
    MiniGame(0x6, 0x14, 0x16A8A, 0xFFFFEC78, 0x8214, 0x0, 0x15FC2, 0xFFFFE4A8, 0x9B32)

    label("loc_1577")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_9_14B4 end

    SaveToFile()

Try(main)
