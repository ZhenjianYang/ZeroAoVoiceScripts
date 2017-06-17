from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c1581.bin",                # FileName
        "c1581",                    # MapName
        "c1581",                    # Location
        0x00B4,                     # MapIndex
        "ed7352",
        0x00000000,                 # Flags
        ("c1581", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 180, 0, 0, 0, 1],
    )

    BuildStringList((
        "c1581",                  # 0
        " ",                      # 1
        "フラッグトルーパー",     # 2
        "フラッグトルーパー",     # 3
        "フラッグトルーパー",     # 4
        "フラッグトルーパー",     # 5
        "bc1520",                 # 6
        "bc1520",                 # 7
        "bc1520",                 # 8
        "bc1540",                 # 9
    ))

    ATBonus("ATBonus_3C8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_2B86", 8,   8,   8,   8,   11,  11,  11)
    Sepith("Sepith_2B9E", 16,  4,   16,  4,   12,  4,   4)
    Sepith("Sepith_2B8E", 10,  9,   10,  9,   0,   8,   8)

    MonsterBattlePostion("MonsterBattlePostion_418", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_47C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_480", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_484", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_488", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_48C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_490", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 2, 13, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_498", 0x0000, 95, 6, 60, 4, 1, 25, 0, "bc1520", "Sepith_2B86", 60, 30, 10, 0,
        (
            ("ms85101.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            ("ms85101.dat", "ms82600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            ("ms85101.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5D0", 0x0010, 95, 6, 60, 4, 1, 20, 0, "bc1520", "Sepith_2B9E", 60, 30, 10, 0,
        (
            ("ms79200.dat", 0, 0, 0, 0, 0, "ms82600.dat", 0, "MonsterBattlePostion_418", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            ("ms79200.dat", "ms82600.dat", 0, 0, 0, 0, "ms82600.dat", 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            ("ms79200.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, "ms82600.dat", 0, "MonsterBattlePostion_418", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_534", 0x0000, 95, 6, 60, 4, 1, 30, 0, "bc1520", "Sepith_2B8E", 60, 30, 10, 0,
        (
            ("ms82600.dat", "ms82600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            ("ms82600.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_418", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            ("ms82600.dat", "ms82600.dat", "ms82600.dat", "ms82600.dat", 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_478", "ed7450", "ed7453", "ATBonus_3C8"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_66C", 0x0042, 255, 6, 45, 3, 3, 30, 0, "bc1540", 0x00000000, 100, 0, 0, 0,
        (
            ("ms85101.dat", "ms85101.dat", "ms85101.dat", "ms85101.dat", 0, 0, 0, 0, "MonsterBattlePostion_3F8", "MonsterBattlePostion_478", "ed7451", "ed7453", "ATBonus_3C8"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch51759.itc",                   # 00
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
        "monster/ch85150.itc",               # 10
        "monster/ch85151.itc",               # 11
        "monster/ch82650.itc",               # 12
        "monster/ch82651.itc",               # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "monster/ch79250.itc",               # 16
        "monster/ch79250.itc",               # 17
        "chr/ch00000.itc",                   # 18
        "chr/ch00000.itc",                   # 19
    ))

    DeclNpc(-69940,  1500,    -197000, 0,    324,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(680,     -15520,  0,       0x101013B,    "BattleInfo_498", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(100170,  -180,    0,       0x101010E,    "BattleInfo_5D0", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(-8420,   -100730, 0,       0x101010E,    "BattleInfo_534", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-21800,  -99170,  0,       0x1010059,    "BattleInfo_498", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(2220,    -200790, 0,       0x101010E,    "BattleInfo_5D0", 0,   22,  0xFFFF, 4,  5)
    DeclMonster(181950,  -107120, 0,       0x101002D,    "BattleInfo_534", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(168700,  -98110,  0,       0x10100B4,    "BattleInfo_498", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-148650, -96880,  0,       0x10100B4,    "BattleInfo_534", 0,   18,  0xFFFF, 2,  3)

    DeclActor(102620,  0,       120,     1200,    102620,  1000,    120,     0x007C, 0,  2,  0x0000)
    DeclActor(10,      0,       -202320, 1200,    10,      1000,    -202320, 0x007C, 0,  3,  0x0000)
    DeclActor(-148500, 0,       -198000, 1200,    -148500, 1000,    -198000, 0x007C, 0,  4,  0x0000)
    DeclActor(-151500, 0,       -198000, 1200,    -151500, 1000,    -198000, 0x007C, 0,  5,  0x0000)
    DeclActor(-150020, 0,       88750,   1200,    -150020, 1000,    88750,   0x007C, 0,  8,  0x0000)
    DeclActor(-143370, 0,       2510,    1200,    -143370, 1000,    2510,    0x007C, 0,  7,  0x0000)
    DeclActor(-26050,  0,       -92710,  1200,    -26050,  2000,    -92710,  0x007C, 0,  9,  0x0000)
    DeclActor(-70100,  0,       -199170, 1200,    -70100,  1000,    -199170, 0x007C, 0,  10, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_72C",          # 00, 0
        "Function_1_743",          # 01, 1
        "Function_2_CF6",          # 02, 2
        "Function_3_E47",          # 03, 3
        "Function_4_F98",          # 04, 4
        "Function_5_10E9",         # 05, 5
        "Function_6_123A",         # 06, 6
        "Function_7_123E",         # 07, 7
        "Function_8_133A",         # 08, 8
        "Function_9_148F",         # 09, 9
        "Function_10_15CA",        # 0A, 10
        "Function_11_212B",        # 0B, 11
        "Function_12_2B3F",        # 0C, 12
    ))


    def Function_0_72C(): pass

    label("Function_0_72C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x77), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1CF, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_742")
    Event(0, 11)

    label("loc_742")

    Return()

    # Function_0_72C end

    def Function_1_743(): pass

    label("Function_1_743")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A6, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_757")
    OP_C9(0x0, 0x8)

    label("loc_757")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 1)), scpexpr(EXPR_END)), "loc_BA8")
    SetMapObjFrame(0xFF, "monita_add", 0x1, 0x1)
    SetMapObjFrame(0x5, "03_add", 0x1, 0x1)
    SetMapObjFrame(0x5, "04_add", 0x0, 0x1)
    Jump("loc_BDC")

    label("loc_BA8")

    SetMapObjFrame(0xFF, "monita_add", 0x0, 0x1)
    SetMapObjFrame(0x5, "03_add", 0x0, 0x1)
    SetMapObjFrame(0x5, "04_add", 0x1, 0x1)
    ClearMapObjFlags(0x5, 0x10)

    label("loc_BDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEF")
    OP_70(0x9, 0x0)
    Jump("loc_BF3")

    label("loc_BEF")

    OP_70(0x9, 0x1E)

    label("loc_BF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C06")
    OP_70(0xA, 0x0)
    Jump("loc_C0A")

    label("loc_C06")

    OP_70(0xA, 0x1E)

    label("loc_C0A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C1D")
    OP_70(0xB, 0x0)
    Jump("loc_C21")

    label("loc_C1D")

    OP_70(0xB, 0x1E)

    label("loc_C21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C34")
    OP_70(0xC, 0x0)
    Jump("loc_C38")

    label("loc_C34")

    OP_70(0xC, 0x1E)

    label("loc_C38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 6)), scpexpr(EXPR_END)), "loc_C6A")
    SetMapObjFlags(0x2, 0x10)
    SetMapObjFrame(0x2, "g_add", 0x1, 0x1)
    SetMapObjFrame(0x2, "r_add", 0x0, 0x1)
    OP_65(0x6, 0x1)
    Jump("loc_C8A")

    label("loc_C6A")

    ClearMapObjFlags(0x2, 0x10)
    SetMapObjFrame(0x2, "g_add", 0x0, 0x1)
    SetMapObjFrame(0x2, "r_add", 0x1, 0x1)

    label("loc_C8A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 7)), scpexpr(EXPR_END)), "loc_CA5")
    SetChrFlags(0x8, 0x80)
    OP_65(0x7, 0x1)
    OP_70(0x11, 0x33)
    Jump("loc_CAE")

    label("loc_CA5")

    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x2)

    label("loc_CAE")

    OP_1C(0x0, 0xD, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0xE, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0xF, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x10, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Sound(927, 1, 100, 0)
    Return()

    # Function_1_743 end

    def Function_2_CF6(): pass

    label("Function_2_CF6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DF6")
    Sound(14, 0, 100, 0)
    OP_74(0x9, 0x1E)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_D7F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F8, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_DF1")

    label("loc_D7F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_DF1")

    Jump("loc_E3B")

    label("loc_DF6")

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

    label("loc_E3B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_CF6 end

    def Function_3_E47(): pass

    label("Function_3_E47")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F47")
    Sound(14, 0, 100, 0)
    OP_74(0xA, 0x1E)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xC6, 1)"), scpexpr(EXPR_END)), "loc_ED0")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xC6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F8, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_F42")

    label("loc_ED0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xC6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xC6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F42")

    Jump("loc_F8C")

    label("loc_F47")

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

    label("loc_F8C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_E47 end

    def Function_4_F98(): pass

    label("Function_4_F98")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1098")
    Sound(14, 0, 100, 0)
    OP_74(0xB, 0x1E)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FA, 1)"), scpexpr(EXPR_END)), "loc_1021")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F8, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1093")

    label("loc_1021")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xB, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1093")

    Jump("loc_10DD")

    label("loc_1098")

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

    label("loc_10DD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_F98 end

    def Function_5_10E9(): pass

    label("Function_5_10E9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F8, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11E9")
    Sound(14, 0, 100, 0)
    OP_74(0xC, 0x1E)
    OP_71(0xC, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x379, 1)"), scpexpr(EXPR_END)), "loc_1172")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x379),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F8, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_11E4")

    label("loc_1172")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x379),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x379),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xC, 0x1E, 0x0, 0x0, 0x0)

    label("loc_11E4")

    Jump("loc_122E")

    label("loc_11E9")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
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

    label("loc_122E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_10E9 end

    def Function_6_123A(): pass

    label("Function_6_123A")

    Call(1, 6)
    Return()

    # Function_6_123A end

    def Function_7_123E(): pass

    label("Function_7_123E")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_132B")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x8, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x8, 0x0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x8)
    OP_71(0x8, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x8, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_132B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_7_123E end

    def Function_8_133A(): pass

    label("Function_8_133A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B6, 1)), scpexpr(EXPR_END)), "loc_1379")
    TalkBegin(0xFF)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_148E")

    label("loc_1379")

    EventBegin(0x1)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1487")
    Fade(500)
    OP_68(-150430, 1500, 87820, 0)
    MoveCamera(33, 32, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14220, 0)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "monita_add", 0x1, 0x1)
    Sleep(1000)
    Fade(500)
    OP_68(-142270, 1350, -2320, 0)
    MoveCamera(60, 23, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(23500, 0)
    OP_0D()
    Sleep(500)
    Sound(164, 0, 100, 0)
    SetMapObjFrame(0x5, "03_add", 0x1, 0x1)
    SetMapObjFrame(0x5, "04_add", 0x0, 0x1)
    Sleep(1000)
    SetMapObjFlags(0x5, 0x10)
    SetScenarioFlags(0x1B6, 1)

    label("loc_1487")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_148E")

    Return()

    # Function_8_133A end

    def Function_9_148F(): pass

    label("Function_9_148F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x379, 0x0)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D3")
    TalkBegin(0xFF)
    Sleep(500)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_15C9")

    label("loc_14D3")

    SetMapFlags(0x8000000)
    EventBegin(0x1)

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "セキュリティーでロックされている扉がある。\x01",
            "赤いカードキーを使いますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15BE")
    Fade(500)
    OP_68(-25830, 1350, -92440, 0)
    MoveCamera(47, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(14770, 0)
    OP_0D()
    Sleep(500)
    Sound(140, 0, 100, 0)
    SetMapObjFlags(0x2, 0x10)
    SetMapObjFrame(0x2, "g_add", 0x1, 0x1)
    SetMapObjFrame(0x2, "r_add", 0x0, 0x1)
    Sleep(1000)
    OP_65(0x6, 0x1)
    SetScenarioFlags(0x1B6, 6)

    label("loc_15BE")

    ClearMapFlags(0x8000000)
    OP_69(0xFF, 0x0)
    EventEnd(0x5)

    label("loc_15C9")

    Return()

    # Function_9_148F end

    def Function_10_15CA(): pass

    label("Function_10_15CA")

    EventBegin(0x0)
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_68(-70820, 4400, -200680, 0)
    MoveCamera(33, 18, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(15400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, -70340, 0, -200560, 0)
    SetChrPos(0x103, -68720, 0, -200370, 315)
    SetChrPos(0x102, -71780, 0, -200170, 45)
    SetChrPos(0x104, -72190, 0, -202720, 45)
    SetChrPos(0xF4, -68740, 0, -202230, 315)
    SetChrPos(0xF5, -70340, 0, -202260, 0)
    OP_68(-70820, 1500, -200680, 4000)
    FadeToBright(500, 0)
    OP_0D()
    OP_6F(0x79)

    #C0018
    ChrTalk(
        0x101,
        "#12P#00011Fな、なんだこれ……！？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_172D")

    #C0019
    ChrTalk(
        0x106,
        (
            "#12P#10712F人形兵器……でしょうか。\x02\x03",

            "#10701F動き出す気配は\x01",
            "感じられませんが……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FE")

    label("loc_172D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1797")

    #C0020
    ChrTalk(
        0x105,
        (
            "#12P#10405F人形兵器……かな？\x02\x03",

            "#10401Fどうも、動き出す気配は\x01",
            "ないみたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_17FE")

    label("loc_1797")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_17FE")

    #C0021
    ChrTalk(
        0x109,
        (
            "#12P#10111Fに、人形兵器でしょうか？\x02\x03",

            "#10106F動き出す気配は\x01",
            "ないみたいですけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17FE")

    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0022
    ChrTalk(
        0x103,
        (
            "#00208F#11Pこれは……間違いありません。\x02\x03",

            "#00201Fエプスタイン財団で開発されていた\x01",
            "《エイドロンギア》です。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_190B():
        TurnDirection(0x101, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_190B)
    Sleep(30)

    def lambda_191B():
        TurnDirection(0x104, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_191B)
    Sleep(30)

    def lambda_192B():
        TurnDirection(0x102, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_192B)
    Sleep(30)

    def lambda_193B():
        TurnDirection(0xF4, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_193B)
    Sleep(30)

    def lambda_194B():
        TurnDirection(0xF5, 0x103, 500)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_194B)
    Sleep(30)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)

    #C0023
    ChrTalk(
        0x104,
        "#00305F#6Pなんだと……！？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00101F#6Pそ、それって……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        (
            "#00203F#11P……リベールの異変の後、\x01",
            "《結社》の人形兵器に対抗するべく\x01",
            "ある計画が立ち上がりました。\x02\x03",

            "#00201F《オーバルギア計画》……\x02\x03",

            "リベールのＺＣＦで着手され、\x01",
            "財団がソフト面で協力することで\x01",
            "本格始動したプロジェクトです。\x02\x03",

            "#00204Fこれは、高名なＡ・ラッセル博士を\x01",
            "レマン自治州にお招きして共同開発した\x01",
            "最新鋭のテスト機体になります。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x101,
        (
            "#00005F#6Pそんな計画が……\x02\x03",

            "#00001Fでも、どうしてそのテスト機体が\x01",
            "こんな場所に？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00208F#11Pそれが……\x02\x03",

            "#00201F……半年ほど前、完成間際に\x01",
            "何者かによって盗まれてしまって……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x102,
        (
            "#00106F#6P……ベルの仕業かもしれないわ。\x02\x03",

            "#00108F彼女は財団で学んだ経験もあるし、\x01",
            "導力ネット事業で、レマン自治州には\x01",
            "頻繁に出張していたから……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1C8C")

    #C0029
    ChrTalk(
        0x10A,
        (
            "#00601F#12Pなるほど……\x01",
            "いかにも怪しいな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D0E")

    label("loc_1C8C")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1CC4")

    #C0030
    ChrTalk(
        0x109,
        "#10106F#12P……怪しいですね。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1D0E")

    label("loc_1CC4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1D0E")

    #C0031
    ChrTalk(
        0x105,
        (
            "#10402F#12Pフフ、確かにそれは\x01",
            "真っ黒かもしれないね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D0E")


    #C0032
    ChrTalk(
        0x104,
        (
            "#00306F#6P気に入ったものを手に入れるためなら\x01",
            "何でもしそうなタイプだしなぁ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x103)

    #C0033
    ChrTalk(
        0x103,
        (
            "#11P#00203F…………ふむ…………\x02\x03",

            "#00202Fどうやら、制御を司る部分に\x01",
            "マトリクス化されたシステムが\x01",
            "用いられているようですね。\x02\x03",

            "エイオンシステムに連動させれば、\x01",
            "わたしでも操ることができそうです。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF5, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0034
    ChrTalk(
        0x104,
        "#6P#00307F……マ、マジか！？\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 500)
    Sleep(150)

    #C0035
    ChrTalk(
        0x103,
        (
            "#11P#00204Fええ、おそらく問題ないかと。\x02\x03",

            "#00202Fせっかく見つけたんですし、\x01",
            "ありがたく回収していきましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x101,
        (
            "#6P#00012Fま、まあ、元々財団の機体なら\x01",
            "回収しても問題ないか……\x02\x03",

            "#00004Fこれから戦いも激しくなるだろうし、\x01",
            "活用できるなら確かに心強いな。\x02\x03",

            "#00000F……ティオ、任せてもいいか？\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        "#11P#00202Fええ、了解しました。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15650, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "『エイドロンギア』を手に入れた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrFlags(0x8, 0x80)
    OP_70(0x11, 0x33)
    Sleep(500)
    Sound(517, 0, 100, 0)
    AddCraft(0x2, 0x124)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ティオがＳクラフト\x01\x07\x02",

            "『エイドロンギア』\x07\x05",
            "を修得しました。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, -70340, 0, -200560, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x1B6, 7)
    OP_65(0x7, 0x1)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_15CA end

    def Function_11_212B(): pass

    label("Function_11_212B")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x1CF, 1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2153")
    LoadChrToIndex("chr/ch00050.itc", 0x1F)

    label("loc_2153")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_216B")
    LoadChrToIndex("chr/ch00150.itc", 0x1F)

    label("loc_216B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2183")
    LoadChrToIndex("chr/ch00250.itc", 0x1F)

    label("loc_2183")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_219B")
    LoadChrToIndex("chr/ch00350.itc", 0x1F)

    label("loc_219B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21B3")
    LoadChrToIndex("chr/ch02950.itc", 0x1F)

    label("loc_21B3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21CB")
    LoadChrToIndex("chr/ch03150.itc", 0x1F)

    label("loc_21CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21E3")
    LoadChrToIndex("chr/ch03250.itc", 0x1F)

    label("loc_21E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_21FB")
    LoadChrToIndex("chr/ch00950.itc", 0x1F)

    label("loc_21FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2213")
    LoadChrToIndex("chr/ch00050.itc", 0x20)

    label("loc_2213")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_222B")
    LoadChrToIndex("chr/ch00150.itc", 0x20)

    label("loc_222B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2243")
    LoadChrToIndex("chr/ch00250.itc", 0x20)

    label("loc_2243")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_225B")
    LoadChrToIndex("chr/ch00350.itc", 0x20)

    label("loc_225B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2273")
    LoadChrToIndex("chr/ch02950.itc", 0x20)

    label("loc_2273")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_228B")
    LoadChrToIndex("chr/ch03150.itc", 0x20)

    label("loc_228B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22A3")
    LoadChrToIndex("chr/ch03250.itc", 0x20)

    label("loc_22A3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22BB")
    LoadChrToIndex("chr/ch00950.itc", 0x20)

    label("loc_22BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22D3")
    LoadChrToIndex("chr/ch00050.itc", 0x21)

    label("loc_22D3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_22EB")
    LoadChrToIndex("chr/ch00150.itc", 0x21)

    label("loc_22EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2303")
    LoadChrToIndex("chr/ch00250.itc", 0x21)

    label("loc_2303")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_231B")
    LoadChrToIndex("chr/ch00350.itc", 0x21)

    label("loc_231B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2333")
    LoadChrToIndex("chr/ch02950.itc", 0x21)

    label("loc_2333")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_234B")
    LoadChrToIndex("chr/ch03150.itc", 0x21)

    label("loc_234B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2363")
    LoadChrToIndex("chr/ch03250.itc", 0x21)

    label("loc_2363")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_237B")
    LoadChrToIndex("chr/ch00950.itc", 0x21)

    label("loc_237B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2393")
    LoadChrToIndex("chr/ch00050.itc", 0x22)

    label("loc_2393")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23AB")
    LoadChrToIndex("chr/ch00150.itc", 0x22)

    label("loc_23AB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23C3")
    LoadChrToIndex("chr/ch00250.itc", 0x22)

    label("loc_23C3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23DB")
    LoadChrToIndex("chr/ch00350.itc", 0x22)

    label("loc_23DB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_23F3")
    LoadChrToIndex("chr/ch02950.itc", 0x22)

    label("loc_23F3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_240B")
    LoadChrToIndex("chr/ch03150.itc", 0x22)

    label("loc_240B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2423")
    LoadChrToIndex("chr/ch03250.itc", 0x22)

    label("loc_2423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_243B")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_243B")

    OP_68(-151770, 1500, 59940, 0)
    MoveCamera(50, 27, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20800, 0)
    SetChrPos(0x0, -150800, 0, 60700, 0)
    SetChrPos(0x1, -149120, 0, 59980, 0)
    SetChrPos(0x2, -150890, 0, 58680, 0)
    SetChrPos(0x3, -149220, 0, 58050, 0)
    SetChrChipByIndex(0x9, 0x10)
    SetChrChipByIndex(0xA, 0x10)
    SetChrChipByIndex(0xB, 0x10)
    SetChrChipByIndex(0xC, 0x10)
    SetChrSubChip(0x9, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xC, 0x0)
    SetChrPos(0x9, -155170, 0, 73000, 135)
    SetChrPos(0xA, -152200, 0, 76210, 180)
    SetChrPos(0xB, -148020, 0, 76160, 180)
    SetChrPos(0xC, -145340, 0, 73000, 225)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x8000)
    OP_52(0x9, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0x9, 3, 0, 12)
    Sleep(50)
    BeginChrThread(0xA, 3, 0, 12)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 12)
    Sleep(50)
    BeginChrThread(0xC, 3, 0, 12)
    OP_68(-150620, 1500, 63320, 3000)

    def lambda_28B4():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_28B4)
    Sleep(50)

    def lambda_28D1():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_28D1)
    Sleep(50)

    def lambda_28EE():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_28EE)
    Sleep(50)

    def lambda_290B():
        OP_97(0xFE, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_290B)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    WaitChrThread(0x3, 1)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-149490, 1500, 73520, 2000)
    MoveCamera(29, 13, 0, 2000)
    OP_6E(550, 2000)
    SetCameraDistance(25000, 2000)

    def lambda_29CF():
        OP_95(0xFE, -151070, 0, 70510, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_29CF)
    Sleep(50)

    def lambda_29EC():
        OP_95(0xFE, -149100, 0, 69990, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_29EC)
    Sleep(50)

    def lambda_2A09():
        OP_95(0xFE, -150750, 0, 64730, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2A09)
    Sleep(50)

    def lambda_2A26():
        OP_95(0xFE, -149130, 0, 64690, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2A26)
    WaitChrThread(0x2, 1)

    def lambda_2A44():
        OP_95(0xFE, -152610, 0, 68770, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2A44)
    WaitChrThread(0x3, 1)

    def lambda_2A62():
        OP_95(0xFE, -147970, 0, 68580, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2A62)
    OP_6F(0x79)
    Fade(500)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_FB(0x0, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x1, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x2, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_FB(0x3, 0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AC9")
    Sound(540, 0, 50, 0)

    label("loc_2AC9")

    SetChrChipByIndex(0x0, 0x1F)
    SetChrChipByIndex(0x1, 0x20)
    SetChrChipByIndex(0x2, 0x21)
    SetChrChipByIndex(0x3, 0x22)
    SetChrSubChip(0x0, 0x0)
    SetChrSubChip(0x1, 0x0)
    SetChrSubChip(0x2, 0x0)
    SetChrSubChip(0x3, 0x0)
    OP_0D()
    Sleep(1000)
    Battle("BattleInfo_66C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrChipByIndex(0x1, 0xFF)
    SetChrChipByIndex(0x2, 0xFF)
    SetChrChipByIndex(0x3, 0xFF)
    Sleep(100)
    OP_69(0xFF, 0x0)
    FadeToBright(500, 0)
    OP_0D()
    EventEnd(0x5)
    Return()

    # Function_11_212B end

    def Function_12_2B3F(): pass

    label("Function_12_2B3F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2B5D")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_12_2B3F")

    label("loc_2B5D")

    Return()

    # Function_12_2B3F end

    SaveToFile()

Try(main)
