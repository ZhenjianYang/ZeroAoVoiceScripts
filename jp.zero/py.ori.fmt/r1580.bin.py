from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r1580.bin",                # FileName
        "r1580",                    # MapName
        "r1580",                    # Location
        0x0060,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r1580", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 1000, -2400, 6000, 0, 0, 1, 96, 0, 1, 0, 2],
    )

    BuildStringList((
        "r1580",                  # 0
        "ゴーディ・オッサー",     # 1
        "br1510",                 # 2
        "br1510",                 # 3
        "br1510",                 # 4
        "br1510",                 # 5
        "br1510",                 # 6
        "br1510",                 # 7
        "br1530",                 # 8
        "ウルスラ間道方面",       # 9
        "星見の塔方面",           # 10
    ))

    ATBonus("ATBonus_434", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_19EA", 0,   1,   1,   15,  9,   4,   5)
    Sepith("Sepith_19F2", 0,   0,   8,   14,  2,   4,   7)
    Sepith("Sepith_1A02", 9,   9,   0,   13,  0,   4,   1)
    Sepith("Sepith_19FA", 0,   14,  3,   4,   4,   9,   2)
    Sepith("Sepith_1A0A", 15,  0,   8,   0,   7,   2,   5)
    Sepith("Sepith_1A1A", 9,   7,   18,  6,   7,   6,   3)

    MonsterBattlePostion("MonsterBattlePostion_494", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_500", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_504", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_508", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_50C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_48C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_514", 5, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_518", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_51C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_520", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_524", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_528", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_52C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_530", 0, 0, 180)

    # monster count: 15

    BattleInfo(
        "BattleInfo_5FC", 0x0000, 19, 6, 60, 8, 1, 45, 0, "br1510", "Sepith_19EA", 30, 40, 20, 10,
        (
            ("ms65600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms65600.dat", "ms65600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms65600.dat", "ms72700.dat", "ms65600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms65600.dat", "ms65600.dat", "ms72700.dat", "ms65600.dat", 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_6C4", 0x0000, 19, 6, 60, 8, 1, 40, 0, "br1510", "Sepith_19F2", 30, 40, 20, 10,
        (
            ("ms72300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms72300.dat", "ms72300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms72300.dat", "ms72700.dat", "ms72300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms72300.dat", "ms72300.dat", "ms72700.dat", "ms72300.dat", 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_78C", 0x0000, 19, 6, 60, 8, 1, 25, 0, "br1510", "Sepith_1A02", 30, 40, 20, 10,
        (
            ("ms72700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms72700.dat", "ms72700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms72700.dat", "ms62400.dat", "ms72700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms72700.dat", "ms72700.dat", "ms62400.dat", "ms72700.dat", 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_854", 0x0000, 19, 6, 60, 8, 1, 40, 0, "br1510", "Sepith_19FA", 30, 40, 20, 10,
        (
            ("ms62400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms62400.dat", "ms62400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms62400.dat", "ms62400.dat", "ms62400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms62400.dat", "ms62400.dat", "ms62400.dat", "ms62400.dat", 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_534", 0x0000, 19, 6, 60, 8, 1, 30, 0, "br1510", "Sepith_1A0A", 30, 30, 30, 10,
        (
            ("ms68500.dat", "ms65600.dat", "ms65600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms68500.dat", "ms72700.dat", "ms72700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms68500.dat", "ms62400.dat", "ms62400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms68500.dat", "ms68500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
        )
    )

    BattleInfo(
        "BattleInfo_960", 0x0000, 35, 6, 45, 6, 1, 40, 0, "br1530", "Sepith_1A1A", 40, 35, 25, 0,
        (
            ("ms70201.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_474", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            ("ms70201.dat", "ms70201.dat", "ms70201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_494", "MonsterBattlePostion_4F4", "ed7400", "ed7403", "ATBonus_434"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_91C", 0x0000, 25, 6, 0, 0, 1, 0, 0, "br1510", 0x00000000, 100, 0, 0, 0,
        (
            ("ms70200.dat", "ms70200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_514", "MonsterBattlePostion_4F4", "ed7401", "ed7403", "ATBonus_434"),
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
        "monster/ch68550.itc",               # 10
        "monster/ch68551.itc",               # 11
        "monster/ch65650.itc",               # 12
        "monster/ch65651.itc",               # 13
        "monster/ch72350.itc",               # 14
        "monster/ch72351.itc",               # 15
        "monster/ch72750.itc",               # 16
        "monster/ch72750.itc",               # 17
        "monster/ch62450.itc",               # 18
        "monster/ch62450.itc",               # 19
        "monster/ch70250.itc",               # 1A
        "monster/ch70251.itc",               # 1B
    ))

    DeclNpc(-91150,  -1750,   -9770,   180,  484,  0x0, 0,   26,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-23890,  14070,   -3000,   0x1010000,    "BattleInfo_5FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-76780,  7060,    -3000,   0x1010000,    "BattleInfo_6C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-89700,  -8380,   -3000,   0x1010000,    "BattleInfo_78C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-61540,  -6870,   -3000,   0x1010000,    "BattleInfo_854", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-63680,  -42920,  -6000,   0x1010000,    "BattleInfo_534", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-64680,  -41920,  -6000,   0x1010000,    "BattleInfo_5FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-26440,  -40790,  -5990,   0x1010000,    "BattleInfo_6C4", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-15180,  -19080,  -6000,   0x1010000,    "BattleInfo_534", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(5510,    -16030,  -5990,   0x1010000,    "BattleInfo_78C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-7370,   -56890,  -5990,   0x1010000,    "BattleInfo_854", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(-58340,  -67070,  -5990,   0x1010000,    "BattleInfo_5FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-93340,  -63620,  -6000,   0x1010000,    "BattleInfo_534", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-141380, -63350,  -9000,   0x1010000,    "BattleInfo_78C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-32759,  3490,    -3000,   0x1010000,    "BattleInfo_960", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(-33040,  -63970,  -6000,   0x1010000,    "BattleInfo_960", 0,   26,  0xFFFF, 10, 11)

    DeclActor(10020,   -6000,   -12950,  1200,    10020,   -5000,   -12950,  0x007C, 0,  3,  0x0000)
    DeclActor(-4019,   -6000,   -62740,  1200,    -4019,   -5000,   -62740,  0x007C, 0,  4,  0x0000)
    DeclActor(-60180,  -3000,   -8380,   1200,    -60180,  -2000,   -8380,   0x007C, 0,  5,  0x0000)
    DeclActor(-91150,  -3000,   -9770,   1200,    -91150,  -2000,   -9770,   0x007C, 0,  6,  0x0000)
    DeclActor(-2530,   -3000,   12390,   1200,    -2530,   -3000,   12390,   0x007C, 0,  7,  0x0000)
    DeclActor(-27260,  -6000,   -57930,  1200,    -27260,  -6000,   -57930,  0x007C, 0,  8,  0x0000)
    DeclActor(-134190, -9000,   -74190,  1200,    -134190, -9000,   -74190,  0x007C, 0,  9,  0x0000)

    PlaceName(35.220001220703125, 0.0, 7.400000095367432, 0x0000, 0x0000, "ウルスラ間道方面")
    PlaceName(-128.0, 0.0, -20.0, 0x0000, 0x0000, "星見の塔方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11

    ScpFunction((
        "Function_0_AB8",          # 00, 0
        "Function_1_AD7",          # 01, 1
        "Function_2_ADB",          # 02, 2
        "Function_3_1278",         # 03, 3
        "Function_4_13C5",         # 04, 4
        "Function_5_1512",         # 05, 5
        "Function_6_165F",         # 06, 6
        "Function_7_1915",         # 07, 7
        "Function_8_1929",         # 08, 8
        "Function_9_193D",         # 09, 9
        "Function_10_1951",        # 0A, 10
    ))


    def Function_0_AB8(): pass

    label("Function_0_AB8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_AD6")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_AB8")

    label("loc_AD6")

    Return()

    # Function_0_AB8 end

    def Function_1_AD7(): pass

    label("Function_1_AD7")

    Call(0, 10)
    Return()

    # Function_1_AD7 end

    def Function_2_ADB(): pass

    label("Function_2_ADB")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x17, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x117, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10DC")
    OP_70(0x0, 0x0)
    Jump("loc_10E0")

    label("loc_10DC")

    OP_70(0x0, 0x1E)

    label("loc_10E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x117, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F3")
    OP_70(0x1, 0x0)
    Jump("loc_10F7")

    label("loc_10F3")

    OP_70(0x1, 0x1E)

    label("loc_10F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x117, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110A")
    OP_70(0x2, 0x0)
    Jump("loc_110E")

    label("loc_110A")

    OP_70(0x2, 0x1E)

    label("loc_110E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x117, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1121")
    OP_70(0x3, 0x0)
    Jump("loc_1125")

    label("loc_1121")

    OP_70(0x3, 0x1E)

    label("loc_1125")

    OP_65(0x4, 0x1)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 0)), scpexpr(EXPR_END)), "loc_118F")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -2530, -3000, 12390, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x4, 0x1)
    Jump("loc_1246")

    label("loc_118F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 1)), scpexpr(EXPR_END)), "loc_11ED")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -27260, -6000, -57930, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)
    Jump("loc_1246")

    label("loc_11ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 2)), scpexpr(EXPR_END)), "loc_1246")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -134190, -9000, -74190, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x6, 0x1)

    label("loc_1246")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_END)), "loc_1268")
    OP_7D(0xFF, 0xBE, 0xB4, 0x0, 0x0)
    OP_11(0xF4, 0xBF, 0xA6, 0x14, 0x78, 0x0)

    label("loc_1268")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x83, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1277")
    OP_16(0x3, 0x1, 0x1, 0x0)

    label("loc_1277")

    Return()

    # Function_2_ADB end

    def Function_3_1278(): pass

    label("Function_3_1278")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x117, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1374")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA3, 1)"), scpexpr(EXPR_END)), "loc_12FD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x117, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_136F")

    label("loc_12FD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xA3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xA3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_136F")

    Jump("loc_13B9")

    label("loc_1374")

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

    label("loc_13B9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1278 end

    def Function_4_13C5(): pass

    label("Function_4_13C5")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x117, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14C1")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_144A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x117, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_14BC")

    label("loc_144A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14BC")

    Jump("loc_1506")

    label("loc_14C1")

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

    label("loc_1506")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_13C5 end

    def Function_5_1512(): pass

    label("Function_5_1512")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x117, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_160E")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1597")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x117, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_1609")

    label("loc_1597")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1609")

    Jump("loc_1653")

    label("loc_160E")

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

    label("loc_1653")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1512 end

    def Function_6_165F(): pass

    label("Function_6_165F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1702")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱の中から強力な魔獣の気配を感じる。\x01",
            "【推定魔獣レベル２５】\x01",
            "宝箱を開きますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1702")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_1702")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x117, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CF")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x72, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FD")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_175B():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_175B)

    def lambda_1775():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1775)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_91C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_17DE"),
        (2, "loc_17ED"),
        (1, "loc_17FA"),
        (SWITCH_DEFAULT, "loc_17FD"),
    )


    label("loc_17DE")

    SetScenarioFlags(0x72, 2)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_17FD")

    label("loc_17ED")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_17FA")

    OP_B7(0x0)
    Return()

    label("loc_17FD")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x94, 1)"), scpexpr(EXPR_END)), "loc_185A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x94),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x117, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_18CA")

    label("loc_185A")

    FadeToDark(300, 0, 100)

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x94),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x94),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18CA")

    Jump("loc_1909")

    label("loc_18CF")

    FadeToDark(300, 0, 100)

    #A0014
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

    label("loc_1909")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_165F end

    def Function_7_1915(): pass

    label("Function_7_1915")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 0)
    OP_65(0x4, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_7_1915 end

    def Function_8_1929(): pass

    label("Function_8_1929")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 1)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_8_1929 end

    def Function_9_193D(): pass

    label("Function_9_193D")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 2)
    OP_65(0x6, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_9_193D end

    def Function_10_1951(): pass

    label("Function_10_1951")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1969")
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)

    label("loc_1969")

    Return()

    # Function_10_1951 end

    SaveToFile()

Try(main)
