from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2020.bin",                # FileName
        "r2020",                    # MapName
        "r2020",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2020", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r2020",                  # 0
        "SE制御",                 # 1
        "br2000",                 # 2
        "br2000",                 # 3
        "br2000",                 # 4
        "br2000",                 # 5
        "br2000",                 # 6
        "br2000",                 # 7
        "クロスベル市方面",       # 8
        "鉱山町マインツ方面",     # 9
    ))

    ATBonus("ATBonus_3C8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1B24", 4,   0,   1,   10,  5,   3,   0)
    Sepith("Sepith_1B2C", 0,   10,  3,   0,   2,   0,   5)
    Sepith("Sepith_1B3C", 10,  2,   0,   4,   0,   5,   2)
    Sepith("Sepith_1B1C", 10,  0,   0,   4,   3,   5,   0)
    Sepith("Sepith_1B34", 9,   0,   4,   0,   2,   0,   7)
    Sepith("Sepith_1B64", 14,  4,   9,   5,   7,   12,  9)

    MonsterBattlePostion("MonsterBattlePostion_428", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_48C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_490", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_494", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_498", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_49C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_408", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_414", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 2, 13, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_638", 0x0000, 14, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_1B24", 30, 40, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
        )
    )

    BattleInfo(
        "BattleInfo_570", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_1B2C", 30, 40, 20, 10,
        (
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
        )
    )

    BattleInfo(
        "BattleInfo_700", 0x0010, 14, 6, 90, 0, 1, 5, 0, "br2000", "Sepith_1B3C", 30, 40, 20, 10,
        (
            ("ms77400.dat", 0, 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms77400.dat", "ms77400.dat", 0, 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms77400.dat", "ms77400.dat", "ms65500.dat", 0, 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms77400.dat", "ms77400.dat", "ms77400.dat", "ms65500.dat", 0, 0, "ms77400.dat", 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
        )
    )

    BattleInfo(
        "BattleInfo_4A8", 0x0000, 14, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_1B1C", 30, 40, 20, 10,
        (
            ("ms62500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
        )
    )

    BattleInfo(
        "BattleInfo_7C8", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_1B34", 30, 40, 20, 10,
        (
            ("ms69400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms69400.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms69400.dat", "ms69700.dat", "ms69400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms69400.dat", "ms69400.dat", "ms69700.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
        )
    )

    BattleInfo(
        "BattleInfo_890", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br2000", "Sepith_1B64", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_408", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_428", "MonsterBattlePostion_488", "ed7400", "ed7403", "ATBonus_3C8"),
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
        "monster/ch62550.itc",               # 10
        "monster/ch62551.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch65550.itc",               # 14
        "monster/ch65551.itc",               # 15
        "monster/ch77450.itc",               # 16
        "monster/ch77450.itc",               # 17
        "monster/ch69450.itc",               # 18
        "monster/ch69450.itc",               # 19
        "monster/ch76050.itc",               # 1A
        "monster/ch76051.itc",               # 1B
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(24830,   -5000,   0,       0x1010000,    "BattleInfo_638", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(53230,   -1940,   2000,    0x1010000,    "BattleInfo_570", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(35920,   6210,    1990,    0x1010000,    "BattleInfo_570", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(52150,   13400,   1990,    0x1010000,    "BattleInfo_570", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(24100,   10020,   1990,    0x1010000,    "BattleInfo_700", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(91270,   -25850,  6180,    0x1010000,    "BattleInfo_4A8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(94500,   21310,   11990,   0x1010000,    "BattleInfo_638", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(46950,   51270,   6000,    0x1010000,    "BattleInfo_7C8", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(27720,   28230,   4000,    0x1010000,    "BattleInfo_570", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(44450,   -18520,  1990,    0x1010000,    "BattleInfo_890", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(108560,  -8460,   10220,   0x1010000,    "BattleInfo_890", 0,   26,  0xFFFF, 10, 11)
    DeclMonster(59010,   31760,   6000,    0x1010000,    "BattleInfo_890", 0,   26,  0xFFFF, 10, 11)

    DeclEvent(0x0000, 0, 8,   104.0,                 -16.5,                 8.5,                   506.25,                [0.04714043438434601,  0.23570235073566437,   -0.0,                  0.0,                   -0.047140467911958694, 0.23570218682289124,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -5.680422782897949,    -20.623958587646484,   -1.7000000476837158,   1.0])

    DeclActor(43840,   2000,    17080,   1200,    43840,   3000,    17080,   0x007C, 0,  2,  0x0000)
    DeclActor(22000,   4000,    26000,   1200,    22000,   5000,    26000,   0x007C, 0,  3,  0x0000)
    DeclActor(40200,   1760,    -18240,  1200,    40200,   1760,    -18240,  0x007C, 0,  4,  0x0000)
    DeclActor(103960,  12000,   7570,    1200,    103960,  12000,   7570,    0x007C, 0,  5,  0x0000)

    PlaceName(-17.0, 0.0, -5.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(37.0, 0.0, 94.0, 0x0000, 0x0000, "鉱山町マインツ方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 9
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 10
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 11

    ScpFunction((
        "Function_0_9F8",          # 00, 0
        "Function_1_9FC",          # 01, 1
        "Function_2_C77",          # 02, 2
        "Function_3_D6E",          # 03, 3
        "Function_4_EBB",          # 04, 4
        "Function_5_ECF",          # 05, 5
        "Function_6_EE3",          # 06, 6
        "Function_7_F01",          # 07, 7
        "Function_8_FC1",          # 08, 8
        "Function_9_19F2",         # 09, 9
        "Function_10_1A18",        # 0A, 10
        "Function_11_1A3E",        # 0B, 11
        "Function_12_1A64",        # 0C, 12
        "Function_13_1A8A",        # 0D, 13
        "Function_14_1ACD",        # 0E, 14
    ))


    def Function_0_9F8(): pass

    label("Function_0_9F8")

    Call(0, 6)
    Return()

    # Function_0_9F8 end

    def Function_1_9FC(): pass

    label("Function_1_9FC")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A14")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_A14")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C58")
    OP_70(0x0, 0x0)
    Jump("loc_C5C")

    label("loc_C58")

    OP_70(0x0, 0x1E)

    label("loc_C5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6F")
    OP_70(0x1, 0x0)
    Jump("loc_C73")

    label("loc_C6F")

    OP_70(0x1, 0x1E)

    label("loc_C73")

    Call(0, 7)
    Return()

    # Function_1_9FC end

    def Function_2_C77(): pass

    label("Function_2_C77")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D37")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x0, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x4, 50)
    AddSepith(0x5, 50)
    AddSepith(0x6, 50)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#60I時のセピス×５０\x01\x07\x02",

            "#61I空のセピス×５０\x01\x07\x02",

            "#62I幻のセピス×５０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x104, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_D5C")

    label("loc_D37")


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

    label("loc_D5C")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_C77 end

    def Function_3_D6E(): pass

    label("Function_3_D6E")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E6A")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x3F, 1)"), scpexpr(EXPR_END)), "loc_DF3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x104, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_E65")

    label("loc_DF3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x3F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E65")

    Jump("loc_EAF")

    label("loc_E6A")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
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

    label("loc_EAF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_D6E end

    def Function_4_EBB(): pass

    label("Function_4_EBB")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 3)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_4_EBB end

    def Function_5_ECF(): pass

    label("Function_5_ECF")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 4)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_5_ECF end

    def Function_6_EE3(): pass

    label("Function_6_EE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_F00")
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)

    label("loc_F00")

    Return()

    # Function_6_EE3 end

    def Function_7_F01(): pass

    label("Function_7_F01")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 3)), scpexpr(EXPR_END)), "loc_F67")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 40200, 1760, -18240, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)
    Jump("loc_FC0")

    label("loc_F67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 4)), scpexpr(EXPR_END)), "loc_FC0")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 103960, 12000, 7570, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_FC0")

    Return()

    # Function_7_F01 end

    def Function_8_FC1(): pass

    label("Function_8_FC1")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x3)
    LoadChrToIndex("chr/ch00250.itc", 0x1E)
    LoadChrToIndex("chr/ch00254.itc", 0x1F)
    LoadEffect(0x0, "battle\\mgaria0.eff")
    LoadEffect(0x1, "event\\eva06_00.eff")
    SoundLoad(132)
    SoundLoad(840)
    StopEffect(0x9, 0x0)
    OP_68(123600, 8080, 2110, 0)
    MoveCamera(45, 10, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(55360, 0)
    SetChrPos(0x101, 108410, 10000, -12040, 45)
    SetChrPos(0x102, 108970, 10000, -13370, 45)
    SetChrPos(0x103, 107370, 9980, -13780, 45)
    SetChrPos(0x104, 108120, 9910, -15230, 45)
    Sound(132, 2, 60, 0)
    FadeToBright(1000, 0)
    OP_68(130690, 8080, 23940, 10000)
    BeginChrThread(0x101, 3, 0, 9)
    BeginChrThread(0x102, 3, 0, 10)
    BeginChrThread(0x103, 3, 0, 11)
    BeginChrThread(0x104, 3, 0, 12)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    SetCameraDistance(48420, 0)
    OP_0D()
    Sleep(300)

    #C0006
    ChrTalk(
        0x101,
        "#0002F#6P凄いな……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x102,
        (
            "#0104F#6P……絶景ね……\x02\x03",

            "#0102F私たちの住むクロスベルって\x01",
            "こんなにも美しかったのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#0202F#6P……ここまで歩いた疲れも\x01",
            "吹き飛んでしまう気がします。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x104,
        (
            "#0302F#12Pしかし、大都市から少し離れると\x01",
            "こんな自然が広がってるとはなぁ。\x02\x03",

            "#0304Fなんつーか、変な自治州だよな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    Sleep(500)
    TurnDirection(0x104, 0x101, 500)

    #C0010
    ChrTalk(
        0x104,
        (
            "#0305F#12Pおっと、悪ぃ。\x01",
            "けなすつもりじゃなかったが。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1299():
        TurnDirection(0xFE, 0x104, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1299)
    TurnDirection(0x102, 0x104, 500)
    WaitChrThread(0x101, 1)

    #C0011
    ChrTalk(
        0x101,
        (
            "#0006F#5Pいや……\x01",
            "言いたいことは判る気がする。\x02\x03",

            "#0001F外国の町で\x01",
            "２年くらい暮らしたけど……\x02\x03",

            "そこと比べると、クロスベルは\x01",
            "確かにアンバランスかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        (
            "#0106F#5Pそうね、私も留学とかで\x01",
            "あちこちの国を回ったけど……\x02\x03",

            "どこも伝統と自然の美しさを\x01",
            "大事にしている国ばかりだったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x103,
        (
            "#0203F#6Pでも……\x01",
            "わたしはクロスベルが\x01",
            "決して嫌いではありません。\x02\x03",

            "#0202F良い所も悪い所も含めて……\x01",
            "惹き付けられる感じがします。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_147D():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_147D)
    Sleep(50)
    TurnDirection(0x102, 0x103, 500)

    #C0014
    ChrTalk(
        0x101,
        "#0000F#5Pティオ……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x102,
        "#0102F#11P……ありがとう。\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#0304F#12Pま、色々と\x01",
            "刺激的な場所だとは思うぜ。\x02\x03",

            "#0302F俺たちみたいな\x01",
            "縁もゆかりもない連中が\x01",
            "何故か集まっちまうくらいだし。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        "#0204F#6P……そうですね。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        (
            "#0004F#5P確かに、クロスベルあっての\x01",
            "特務支援課#10Rオ レ た ち#なんだよな……\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#0109F#11Pふふ、そう考えると\x01",
            "悪い所ばかりじゃないわね。\x02",
        )
    )

    CloseMessageWindow()
    Sound(841, 0, 100, 0)
    Sleep(1000)
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

    def lambda_1671():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1671)
    Sleep(50)

    def lambda_1681():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1681)
    Sleep(50)

    def lambda_1691():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1691)
    Sleep(50)

    def lambda_16A1():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_16A1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    Sleep(500)

    #C0020
    ChrTalk(
        0x101,
        "#0013F#11Pまた……！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x102,
        (
            "#0101F#11P今度はずいぶん、\x01",
            "はっきりと聞こえたわね……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1716():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1716)
    WaitChrThread(0x104, 1)

    #C0022
    ChrTalk(
        0x104,
        "#0301F#11Pどっから聞こえたか判るか？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x103,
        "#0201F#11P待ってください……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    def lambda_1774():
        TurnDirection(0xFE, 0x103, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1774)

    def lambda_1781():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1781)
    Sleep(300)
    VolumeBGM(0x3C, 0x3E8)
    Sound(1278, 255, 100, 0)    #voice#Tio
    Fade(250)
    SetChrChipByIndex(0x103, 0x1E)
    SetChrSubChip(0x103, 0x0)
    Sound(820, 0, 100, 0)
    OP_0D()
    SetChrChipByIndex(0x103, 0x1F)
    SetChrSubChip(0x103, 0x0)
    Sound(831, 0, 100, 0)
    Sound(840, 2, 100, 0)
    PlayEffect(0x0, 0x0, 0x103, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0x1, 0x103, 0x140, 0, 1450, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    OP_A1(0x103, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x1, 0x2, 0x1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sound(820, 0, 100, 0)
    BeginChrThread(0x8, 1, 0, 13)
    Fade(250)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    OP_0D()
    VolumeBGM(0x64, 0x3E8)
    Sleep(500)

    #C0024
    ChrTalk(
        0x103,
        (
            "#0203F#11P……１０セルジュ北西です。\x02\x03",

            "#0201F地図と照らし合わせると……\x01",
            "ちょうど山道の分岐点ですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#0001F#5P分かった、行ってみよう。\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 2, 0, 14)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_37()
    OP_69(0x1, 0x0)
    OP_68(107100, 14500, 5500, 0)
    MoveCamera(45, 8, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    SetChrPos(0x0, 107100, 12000, 5500, 45)
    SetChrPos(0x1, 107100, 12000, 5500, 45)
    SetChrPos(0x2, 107100, 12000, 5500, 45)
    SetChrPos(0x3, 107100, 12000, 5500, 45)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0x64, 3)
    OP_29(0x40, 0x1, 0x2)
    OP_E0(0x2)
    Call(0, 6)
    Call(0, 7)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x8, 0x2)
    OP_24(0x84)
    OP_24(0x348)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_8_FC1 end

    def Function_9_19F2(): pass

    label("Function_9_19F2")


    def lambda_19F7():
        OP_95(0xFE, 109100, 12000, 3500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_19F7)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_9_19F2 end

    def Function_10_1A18(): pass

    label("Function_10_1A18")


    def lambda_1A1D():
        OP_95(0xFE, 110100, 12000, 2500, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A1D)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_10_1A18 end

    def Function_11_1A3E(): pass

    label("Function_11_1A3E")


    def lambda_1A43():
        OP_95(0xFE, 108050, 12000, 1860, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A43)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_11_1A3E end

    def Function_12_1A64(): pass

    label("Function_12_1A64")


    def lambda_1A69():
        OP_95(0xFE, 109030, 11960, 870, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1A69)
    WaitChrThread(0xFE, 1)
    OP_93(0xFE, 0x2D, 0x1F4)
    Return()

    # Function_12_1A64 end

    def Function_13_1A8A(): pass

    label("Function_13_1A8A")

    OP_25(0x348, 0x5A)
    Sleep(50)
    OP_25(0x348, 0x50)
    Sleep(50)
    OP_25(0x348, 0x46)
    Sleep(50)
    OP_25(0x348, 0x3C)
    Sleep(50)
    OP_25(0x348, 0x32)
    Sleep(50)
    OP_25(0x348, 0x28)
    Sleep(50)
    OP_25(0x348, 0x1E)
    Sleep(50)
    OP_25(0x348, 0x14)
    Sleep(50)
    OP_25(0x348, 0xA)
    Sleep(50)
    OP_24(0x348)
    Return()

    # Function_13_1A8A end

    def Function_14_1ACD(): pass

    label("Function_14_1ACD")

    OP_25(0x84, 0x32)
    Sleep(50)
    OP_25(0x84, 0x28)
    Sleep(50)
    OP_25(0x84, 0x1E)
    Sleep(50)
    OP_25(0x84, 0x14)
    Sleep(50)
    OP_25(0x84, 0xA)
    Sleep(50)
    OP_24(0x84)
    Return()

    # Function_14_1ACD end

    SaveToFile()

Try(main)
