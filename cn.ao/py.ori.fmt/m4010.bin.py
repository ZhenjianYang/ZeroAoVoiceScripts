from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4010.bin",                # FileName
        "m4010",                    # MapName
        "m4010",                    # Location
        0x007B,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("m4010", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x2B,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 123, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4010",                  # 0
        "达德利搜查官",           # 1
        "亚里欧斯",               # 2
        "暴龙",                   # 3
        "bm4010",                 # 4
        "bm4010",                 # 5
        "bm4010",                 # 6
        "bm4010",                 # 7
    ))

    ATBonus("ATBonus_460", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_470", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_414C", 2,   2,   0,   2,   2,   2,   1)
    Sepith("Sepith_4144", 0,   4,   0,   4,   1,   1,   1)
    Sepith("Sepith_413C", 3,   4,   5,   2,   0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_490", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_494", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_498", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_49C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_510", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_514", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_518", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_51C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_520", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_524", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_528", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_52C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4CC", 8, 14, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_610", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_414C", 60, 25, 10, 0,
        (
            ("ms83800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83800.dat", "ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_574", 0x0000, 46, 6, 60, 6, 1, 20, 0, "bm4010", "Sepith_4144", 60, 25, 10, 0,
        (
            ("ms83600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83600.dat", "ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_530", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_413C", 100, 0, 0, 0,
        (
            ("ms86200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
            (),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_6AC", 0x0000, 50, 6, 45, 0, 1, 0, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86200.dat", "ms86200.dat", "ms86200.dat", "ms86200.dat", 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7451", "ed7453", "ATBonus_470"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch00900.itc",                   # 00
        "chr/ch02400.itc",                   # 01
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
        "monster/ch86250.itc",               # 10
        "monster/ch86251.itc",               # 11
        "monster/ch83650.itc",               # 12
        "monster/ch83650.itc",               # 13
        "monster/ch83850.itc",               # 14
        "monster/ch83851.itc",               # 15
    ))

    DeclNpc(0,       -8000,   -1500,   90,   389,  0x0, 0,   0,   0,   0,   0,   0,   10,  255,  0)
    DeclNpc(0,       -8000,   -2500,   90,   389,  0x0, 0,   1,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(39580,   9550,    221570,  0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(15760,   72320,   0,       0x101008C,    "BattleInfo_610", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(13220,   87760,   0,       0x101008C,    "BattleInfo_574", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(45940,   109370,  -5000,   0x10100B9,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(253530,  97490,   -5000,   0x10100E6,    "BattleInfo_610", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(152730,  20290,   -5000,   0x10100E6,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-100860, 90780,   0,       0x101008C,    "BattleInfo_574", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-107780, 100190,  0,       0x10100B9,    "BattleInfo_574", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-115160, 88000,   0,       0x101005F,    "BattleInfo_610", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-110120, 126890,  3500,    0x10100E6,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-123150, 151900,  9000,    0x10100B9,    "BattleInfo_574", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-139110, 159700,  9000,    0x101005F,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(31000,   219940,  9000,    0x10100A0,    "BattleInfo_530", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 19,  2.7699999809265137,    7.920000076293945,     -9.0,                  2304.0,                [0.03125,              -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.08656249940395355,  -2.640000104904175,    1.8000001907348633,    1.0])

    DeclActor(-1100,   0,       78900,   2000,    -1100,   1500,    78900,   0x007C, 0,  16, 0x0000)
    DeclActor(36110,   3200,    223690,  2000,    36110,   4700,    223690,  0x007C, 0,  17, 0x0000)
    DeclActor(147320,  -5000,   22180,   1200,    147320,  -4000,   22180,   0x007C, 0,  4,  0x0000)
    DeclActor(39580,   9050,    221570,  1200,    39580,   10050,   221570,  0x007C, 0,  5,  0x0000)
    DeclActor(259510,  -4950,   97890,   1200,    259510,  -3950,   97890,   0x007C, 0,  6,  0x0000)
    DeclActor(-142180, 9000,    178130,  1200,    -142180, 10000,   178130,  0x007C, 0,  7,  0x0000)
    DeclActor(247980,  9000,    234020,  1200,    247980,  10000,   234020,  0x007C, 0,  8,  0x0000)
    DeclActor(-4270,   -7900,   2580,    1200,    -4270,   -6400,   2580,    0x007C, 0,  12, 0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5, 6])                 # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6])                # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_788",          # 00, 0
        "Function_1_838",          # 01, 1
        "Function_2_857",          # 02, 2
        "Function_3_89F",          # 03, 3
        "Function_4_DDD",          # 04, 4
        "Function_5_F18",          # 05, 5
        "Function_6_1116",         # 06, 6
        "Function_7_126F",         # 07, 7
        "Function_8_13AA",         # 08, 8
        "Function_9_14E5",         # 09, 9
        "Function_10_14E9",        # 0A, 10
        "Function_11_1570",        # 0B, 11
        "Function_12_1603",        # 0C, 12
        "Function_13_16E7",        # 0D, 13
        "Function_14_28C5",        # 0E, 14
        "Function_15_33CC",        # 0F, 15
        "Function_16_3B16",        # 10, 16
        "Function_17_3DA7",        # 11, 17
        "Function_18_3F36",        # 12, 18
        "Function_19_407D",        # 13, 19
    ))


    def Function_0_788(): pass

    label("Function_0_788")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_7C0"),
        (1, "loc_7CC"),
        (2, "loc_7D8"),
        (3, "loc_7E4"),
        (4, "loc_7F0"),
        (5, "loc_7FC"),
        (6, "loc_808"),
        (SWITCH_DEFAULT, "loc_814"),
    )


    label("loc_7C0")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7CC")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7D8")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7E4")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7F0")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_7FC")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_808")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_814")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_820")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_837")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_820")

    label("loc_837")

    Return()

    # Function_0_788 end

    def Function_1_838(): pass

    label("Function_1_838")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_856")
    OP_A1(0xFE, 0x2BC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_838")

    label("loc_856")

    Return()

    # Function_1_838 end

    def Function_2_857(): pass

    label("Function_2_857")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86F")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_86F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_884")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    SetScenarioFlags(0x0, 1)
    Event(0, 13)

    label("loc_884")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89E")
    Event(0, 15)

    label("loc_89E")

    Return()

    # Function_2_857 end

    def Function_3_89F(): pass

    label("Function_3_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_8B4")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_8B4")

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
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x16, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDB")
    OP_66(0x0, 0x1)

    label("loc_CDB")

    OP_1B(0x0, 0x0, 0x12)
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CF4")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_CF4")

    ClearMapObjFlags(0x5, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D11")
    OP_70(0x5, 0x0)
    OP_70(0x6, 0x0)
    Jump("loc_D19")

    label("loc_D11")

    OP_70(0x5, 0x14)
    OP_70(0x6, 0x14)

    label("loc_D19")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2C")
    OP_70(0x0, 0x0)
    Jump("loc_D30")

    label("loc_D2C")

    OP_70(0x0, 0x1E)

    label("loc_D30")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D43")
    OP_70(0x1, 0x0)
    Jump("loc_D47")

    label("loc_D43")

    OP_70(0x1, 0x1E)

    label("loc_D47")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D5A")
    OP_70(0x2, 0x0)
    Jump("loc_D5E")

    label("loc_D5A")

    OP_70(0x2, 0x1E)

    label("loc_D5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D71")
    OP_70(0x3, 0x0)
    Jump("loc_D75")

    label("loc_D71")

    OP_70(0x3, 0x1E)

    label("loc_D75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D88")
    OP_70(0x4, 0x0)
    Jump("loc_D8C")

    label("loc_D88")

    OP_70(0x4, 0x1E)

    label("loc_D8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_DA0")
    OP_24(0x81)
    ClearScenarioFlags(0x0, 1)
    Jump("loc_DA6")

    label("loc_DA0")

    Sound(129, 1, 100, 0)

    label("loc_DA6")

    OP_1C(0x0, 0x8, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    OP_1C(0x0, 0x9, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    OP_1C(0x0, 0xA, 0x0, 0x32, 0x0, 0x9, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_3_89F end

    def Function_4_DDD(): pass

    label("Function_4_DDD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ECF")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('复苏药', 1)"), scpexpr(EXPR_END)), "loc_E60")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_ECA")

    label("loc_E60")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_ECA")

    Jump("loc_F0C")

    label("loc_ECF")

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

    label("loc_F0C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_DDD end

    def Function_5_F18(): pass

    label("Function_5_F18")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10D8")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1015")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F75():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F75)

    def lambda_F8F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_F8F)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

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
    WaitChrThread(0xA, 1)
    Battle("BattleInfo_6AC", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_FF6"),
        (2, "loc_1005"),
        (1, "loc_1012"),
        (SWITCH_DEFAULT, "loc_1015"),
    )


    label("loc_FF6")

    SetScenarioFlags(0x21A, 6)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1015")

    label("loc_1005")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_1012")

    OP_B9(0x0)
    Return()

    label("loc_1015")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＨＰ１', 1)"), scpexpr(EXPR_END)), "loc_106C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_10D3")

    label("loc_106C")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10D3")

    Jump("loc_110A")

    label("loc_10D8")

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

    label("loc_110A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F18 end

    def Function_6_1116(): pass

    label("Function_6_1116")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1240")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x2, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 30)
    AddSepith(0x1, 30)
    AddSepith(0x2, 30)
    AddSepith(0x3, 30)
    AddSepith(0x4, 30)
    AddSepith(0x5, 30)
    AddSepith(0x6, 30)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×３０\x01\x07\x02",

            "#57I水之耀晶片×３０\x01\x07\x02",

            "#58I火之耀晶片×３０\x01\x07\x02",

            "#59I风之耀晶片×３０\x01\x07\x02",

            "#60I时之耀晶片×３０\x01\x07\x02",

            "#61I空之耀晶片×３０\x01\x07\x02",

            "#62I幻之耀晶片×３０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E0, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_125D")

    label("loc_1240")


    #A0009
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

    label("loc_125D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1116 end

    def Function_7_126F(): pass

    label("Function_7_126F")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1361")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('打火机', 1)"), scpexpr(EXPR_END)), "loc_12F2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_135C")

    label("loc_12F2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_135C")

    Jump("loc_139E")

    label("loc_1361")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0012
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

    label("loc_139E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_126F end

    def Function_8_13AA(): pass

    label("Function_8_13AA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_149C")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_142D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_1497")

    label("loc_142D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1497")

    Jump("loc_14D9")

    label("loc_149C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
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

    label("loc_14D9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_13AA end

    def Function_9_14E5(): pass

    label("Function_9_14E5")

    Call(1, 6)
    Return()

    # Function_9_14E5 end

    def Function_10_14E9(): pass

    label("Function_10_14E9")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1516")
    FadeToDark(500, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_E2(0x3)
    Call(0, 14)
    Return()

    label("loc_1516")


    #C0016
    ChrTalk(
        0x8,
        (
            "#00603F把刚才交给你们的\x01",
            "核心回路镶嵌到\x01",
            "『艾尼格玛Ⅱ』里。\x02\x03",

            "#00600F先做好这个吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_14E9 end

    def Function_11_1570(): pass

    label("Function_11_1570")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_159D")
    FadeToDark(500, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_E2(0x3)
    Call(0, 14)
    Return()

    label("loc_159D")


    #C0017
    ChrTalk(
        0x9,
        (
            "#01403F真没想到，我会再次\x01",
            "来到这个地方……\x02\x03",

            "#01400F总之，一定要争分夺秒，\x01",
            "尽快将那两人逮捕。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1570 end

    def Function_12_1603(): pass

    label("Function_12_1603")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0018
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16D8")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x7, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x7, 0x0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x7)
    OP_71(0x7, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x7, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_16D8")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_12_1603 end

    def Function_13_16E7(): pass

    label("Function_13_16E7")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis090.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    CreatePortrait(2, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "c_vis230.itp")
    OP_68(3000, -7900, -6000, 0)
    MoveCamera(317, 36, 0, 0)
    OP_6E(800, 0)
    SetCameraDistance(21500, 0)
    SetChrPos(0x101, 3000, -8000, -17200, 0)
    SetChrPos(0x10A, 4700, -8000, -18400, 0)
    SetChrPos(0x108, 1600, -8000, -18200, 0)
    SetChrPos(0x109, 3300, -8000, -19100, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0019
    AnonymousTalk(
        0xFF,
        (
            "#30W我们前来此地，\x01",
            "是由于接到了帝国政府的联络。\x02\x03",

            "在教团事件结束之后，又过了几个月……\x02\x03",

            "趁乱逃亡到帝国的前议长哈尔特曼\x01",
            "和前市长秘书阿奈斯特\x01",
            "遭到了帝国的驱逐。\x02\x03",

            "不知出于什么原因，这两人将位于共和国\x01",
            "最西端的阿尔泰尔市选定为新的潜伏地点……\x02\x03",

            "新市长立刻与共和国政府\x01",
            "达成了秘密协议，\x01",
            "派人前往境外逮捕他们。\x02\x03",

            "不过，由于这是很特殊的政治问题，\x01",
            "因此将逮捕任务交给了处于正规指挥系统\x01",
            "之外的『特别任务支援科』……\x02\x03",

            "另外，搜查一科、警备队与游击士协会也\x01",
            "提供了协助，破例组建成史无前例的调查体制。\x02\x03",

            "在阿尔泰尔市调查了数日之后……\x02\x03",

            "我们终于发现了哈尔特曼和阿奈斯特\x01",
            "逃向了教团据点旧址。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)

    def lambda_1A57():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1A57)
    Sleep(100)

    def lambda_1A74():
        OP_97(0x108, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1A74)
    Sleep(100)

    def lambda_1A91():
        OP_97(0x10A, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1A91)
    Sleep(100)

    def lambda_1AAE():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1AAE)
    OP_68(3000, -7900, 6000, 7000)
    SetCameraDistance(35500, 7000)
    PlayBGM("ed7350", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sound(129, 1, 100, 0)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(500)
    PlaceName2(340, 200, "c_plac50", 0x0, 0)
    OP_6F(0x79)
    Fade(500)
    OP_68(3000, -7000, 2500, 0)
    MoveCamera(323, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(17000, 0)
    SetCameraDistance(15000, 3000)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_93(0x101, 0x2D, 0x190)
    Sleep(500)
    OP_93(0x101, 0x13B, 0x190)
    Sleep(750)
    OP_93(0x101, 0x0, 0x190)
    Sleep(300)
    OP_6F(0x79)
    #Sound(2079, 255, 100, 0)    #voice#Lloyd

    #C0020
    ChrTalk(
        0x101,
        "#00005F#30W这里是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x109, 0)
    Sleep(150)

    #C0021
    ChrTalk(
        0x109,
        (
            "#6P#10108F钟乳洞吗……\x01",
            "不过好像经过人为修整。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x108,
        (
            "#01403F似乎是数百年前使用过的\x01",
            "石窟寺院遗迹。\x02\x03",

            "之后经过『Ｄ∴Ｇ教团』的改造修建，\x01",
            "被其作为举行『仪式』的场所。\x02\x03",

            "#01401F一直持续到六年前的那一天。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x0, 0x0, 0x0)
    Sleep(500)

    #A0023
    AnonymousTalk(
        0x101,
        (
            "#00006F……也就是科长、亚里欧斯先生\x01",
            "还有大哥前来镇压的那一天吧。\x02\x03",

            "#00001F大哥当时救出了\x01",
            "此地唯一的幸存者缇欧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0024
    AnonymousTalk(
        0x108,
        (
            "#01403F嗯，老实说，\x01",
            "在如同地狱般的惨状下，\x01",
            "那可以算是唯一的安慰了。\x02\x03",

            "#01400F如今，当初的那些痕迹\x01",
            "几乎都已经消失了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0025
    AnonymousTalk(
        0x101,
        "#00008F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)

    #C0026
    ChrTalk(
        0x109,
        (
            "#6P#10106F真是让人难以相信啊……\x01",
            "竟然发生过那样的事情。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x10A,
        (
            "#6P#00603F哼，实在是一群\x01",
            "毫无人性的家伙啊。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x108, 500)
    Sleep(300)

    #C0028
    ChrTalk(
        0x10A,
        (
            "#12P#00600F听说共和国军当时没有出动，\x01",
            "是因为军中的部分军官\x01",
            "被教团抓住了把柄……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x10A, 500)

    #C0029
    ChrTalk(
        0x108,
        (
            "#01402F#5P嗯，所以才会任命赛尔盖班\x01",
            "来捣毁这里。\x02\x03",

            "#01404F如今想想，当时那种\x01",
            "强行介入的做法真是相当莽撞，\x01",
            "连游击士协会都震惊得瞠目结舌。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x10A,
        (
            "#12P#00602F哼，真不愧是\x01",
            "『恶名昭著』的赛尔盖班啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    #C0031
    ChrTalk(
        0x101,
        (
            "#11P#00004F哈哈……当时的景象\x01",
            "好像已经浮现在我的眼前了。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 500)
    Sleep(300)

    #C0032
    ChrTalk(
        0x101,
        (
            "#11P#00001F亚里欧斯先生，\x01",
            "那两人大概会前往\x01",
            "据点中的什么地方？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_201E():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_201E)
    Sleep(100)

    #C0033
    ChrTalk(
        0x108,
        (
            "#01403F#5P可能性最高的地方，\x01",
            "应该就是最深处的『仪式之间』。\x02\x03",

            "那里残留着神秘的祭坛，\x01",
            "与『太阳堡垒』中的那个很相似。\x02\x03",

            "#01401F哈尔特曼姑且不说……\x01",
            "阿奈斯特将那里视为目的地\x01",
            "并不奇怪。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#11P#00003F……确实。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x109,
        (
            "#12P#10113F莫非那个地方\x01",
            "与那种名为『真知』的药物\x01",
            "存在着某些关系？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x10A,
        (
            "#12P#00606F不能否认这种可能性。\x02\x03",

            "据我所知，阿奈斯特\x01",
            "似乎已从约亚西姆那里\x01",
            "得到了『真知』。\x02\x03",

            "#00601F而且并非蓝色，而是红色那种。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    TurnDirection(0x109, 0x10A, 600)

    #C0037
    ChrTalk(
        0x109,
        (
            "#5P#10107F那、那是……\x01",
            "能把人变成怪物的那种药！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0038
    ChrTalk(
        0x101,
        (
            "#11P#00003F嗯，与他同行的\x01",
            "哈尔特曼说不定\x01",
            "也会有危险呢。\x02\x03",

            "#00001F在无法挽回的情况发生之前，\x01",
            "我们无论如何也要将他们两人拘捕。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0039
    ChrTalk(
        0x109,
        (
            "#6P#10101F嗯！\x02\x03",

            "#10106F……不过还真是伤脑筋啊。\x02\x03",

            "艾尼格玛偏偏在\x01",
            "这种特别时期\x01",
            "升级版本……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#11P#00006F唉，是啊。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sleep(500)

    #C0041
    ChrTalk(
        0x101,
        "#11P#00001F『艾尼格玛Ⅱ』……\x02",
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0xFFFFD8F0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    Sleep(300)

    #A0042
    AnonymousTalk(
        0x109,
        (
            "#10108F可以在导力器中心\x01",
            "镶嵌新型的『核心回路』……\x02\x03",

            "但因为时间仓促，我们没能等到配送，\x01",
            "结果现在连魔法都不能使用。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0043
    AnonymousTalk(
        0x101,
        (
            "#00006F爱普斯泰恩财团每次\x01",
            "升级机型都很突然呢。\x02\x03",

            "我并不想批评缇欧\x01",
            "所在的财团，可是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0044
    AnonymousTalk(
        0x10A,
        (
            "#00603F哼，虽说时机的确很不巧，\x01",
            "但也不用发这种牢骚。\x02\x03",

            "#00600F如果用心做好准备工作，\x01",
            "这点东西总应该预备好吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    def lambda_2521():
        OP_9A(0xFE, 0x101, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_2521)
    WaitChrThread(0x10A, 1)
    ClearChrFlags(0x101, 0x20)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    TurnDirection(0x101, 0x10A, 500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xDC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('力量', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0046
    ChrTalk(
        0x101,
        "#00005F哎……\x02",
    )

    CloseMessageWindow()

    def lambda_25AC():
        OP_96(0xFE, 0x125C, 0xFFFFE0C0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_25AC)

    #C0047
    ChrTalk(
        0x108,
        (
            "#01404F#5P呵呵，既然如此，\x01",
            "那我也提供一枚备用品吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_25FF():
        OP_9A(0xFE, 0x109, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_25FF)
    WaitChrThread(0x108, 1)
    TurnDirection(0x109, 0x108, 500)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetChrName("")

    #A0048
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xDD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "收下了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber('盾牌', 1)
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_2665():
        OP_96(0xFE, 0x640, 0xFFFFE0C0, 0x708, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2665)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x10A, 1)

    #C0049
    ChrTalk(
        0x109,
        (
            "#12P#10105F这就是……\x01",
            "核心回路吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00005F要把这两个给我们吗……？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x10A,
        (
            "#12P#00601F哼，只是怕你们碍手碍脚，\x01",
            "给我们拖后腿而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x108,
        (
            "#01402F#5P把自己喜欢的核心回路\x01",
            "镶嵌在『艾尼格玛Ⅱ』的中心吧。\x02\x03",

            "无论镶嵌哪个，\x01",
            "都可以使用多种魔法。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 600)

    #C0053
    ChrTalk(
        0x101,
        "#11P#00002F是！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x109,
        "#12P#10102F明白了！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※在新型战术导力器『艾尼格玛Ⅱ』\x01",
            "  的中央结晶孔中，\x01",
            "  可以镶嵌核心回路。\x02\x03",

            "※在主菜单中打开[ORBMENT]选项，\x01",
            "  并选择[QUARTZ]，\x01",
            "  即可镶嵌核心回路。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(100)
    OP_D7(0x1E)
    OP_37()
    OP_CC(0x1, 0xFF, 0x0)
    OP_32(0xFF, 0xF9, 0x0)
    RemoveParty(0x9, 0x0)
    RemoveParty(0x7, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x0, 2460, -8000, -200, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 0)
    OP_29(0xA0, 0x4, 0x2)
    OP_29(0xA0, 0x1, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28BD")
    SetScenarioFlags(0x21, 0)

    label("loc_28BD")

    OP_E2(0x2)
    Sleep(400)
    EventEnd(0x5)
    Return()

    # Function_13_16E7 end

    def Function_14_28C5(): pass

    label("Function_14_28C5")

    AddParty(0x9, 0xFF, 0xFF)
    AddParty(0x7, 0xFF, 0xFF)
    OP_37()
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    OP_68(3000, -7000, 2500, 0)
    MoveCamera(323, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15000, 0)
    SetChrPos(0x101, 3000, -8000, 2800, 180)
    SetChrPos(0x10A, 4700, -8000, 1600, 270)
    SetChrPos(0x108, 1600, -8000, 1800, 90)
    SetChrPos(0x109, 3300, -8000, 900, 0)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00001.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10100.itp")
    CreatePortrait(2, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00600.itp")
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01400.itp")
    FadeToBright(1000, 0)
    OP_0D()

    #C0056
    ChrTalk(
        0x10A,
        "#12P#00600F好，你们已经准备完毕了吧？\x02",
    )

    CloseMessageWindow()

    def lambda_2A30():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2A30)
    Sleep(100)

    def lambda_2A40():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2A40)
    WaitChrThread(0x101, 2)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00000F是的，久等了。\x02\x03",

            "#00002F那个……\x01",
            "多谢二位特意为我们准备，\x01",
            "真是帮大忙了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2558, 255, 100, 0)    #voice#Dudley
    Sleep(100)
    OP_63(0x10A, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(800)

    #C0058
    ChrTalk(
        0x10A,
        (
            "#12P#00605F并、并不是特意\x01",
            "为你们准备的。\x02\x03",

            "#00606F言归正传，班宁斯，\x01",
            "我想你应该明白吧？\x02\x03",

            "#00601F对你来说，这项任务也是\x01",
            "在一科研修的最后一个环节。\x02\x03",

            "#00607F万一你无所作为，丑态百出，\x01",
            "就要从头再来了，做好心理准备吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(3317, 255, 100, 0)    #voice#Lloyd

    #C0059
    ChrTalk(
        0x101,
        "#00000F#30W……是！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        (
            "#6P#10112F#6P（啊哈哈……\x01",
            "  真是个不坦率的人呢。）\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x108,
        (
            "#01404F#5P（呵，这个男人的内心\x01",
            "  远比外表炽热。）\x02\x03",

            "#01402F（……真不愧是在一科和盖伊\x01",
            "  一争高下的人啊。）\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0062
    AnonymousTalk(
        0x101,
        "好，那我们就开始行动吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    def lambda_2CFA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2CFA)
    Sleep(50)

    def lambda_2D0A():

        label("loc_2D0A")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2D0A")

    QueueWorkItem2(0x10A, 2, lambda_2D0A)
    Sleep(50)

    def lambda_2D1F():

        label("loc_2D1F")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_2D1F")

    QueueWorkItem2(0x108, 2, lambda_2D1F)
    WaitChrThread(0x109, 2)
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_2D3C():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2D3C)
    Sleep(500)
    Fade(500)
    OP_68(3000, -7100, 3900, 0)
    MoveCamera(0, 19, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(15500, 1500)
    SetChrPos(0x10A, 4500, -8000, 1600, 270)
    SetChrPos(0x108, 1500, -8000, 1600, 90)
    SetChrPos(0x109, 3000, -8000, 900, 0)
    OP_0D()
    WaitChrThread(0x101, 1)
    EndChrThread(0x10A, 0x2)
    EndChrThread(0x108, 0x2)
    OP_93(0x101, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sleep(150)

    #C0063
    ChrTalk(
        0x101,
        (
            "#00003F克洛斯贝尔警察局·搜查一科，\x01",
            "阿雷克斯·达德利主任搜查官。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)
    #Sound(4115, 255, 100, 0)    #voice#Dudley

    #A0064
    AnonymousTalk(
        0x10A,
        "#30W嗯。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    #C0065
    ChrTalk(
        0x101,
        (
            "#00000F克洛斯贝尔警备队，\x01",
            "诺艾尔·希卡上士。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)
    #Sound(3514, 255, 100, 0)    #voice#Noel

    #A0066
    AnonymousTalk(
        0x109,
        "#30W是！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0067
    ChrTalk(
        0x101,
        (
            "#00004F以及特别协助人员，\x01",
            "游击士协会·克洛斯贝尔分部的\x01",
            "亚里欧斯·马克莱因先生。\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(150)
    #Sound(4022, 255, 100, 0)    #voice#Arios

    #A0068
    AnonymousTalk(
        0x108,
        "#30W嗯。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x3, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    OP_CC(0x0, 0x3, 0x0)

    #C0069
    ChrTalk(
        0x101,
        (
            "#00003F接下来，克洛斯贝尔警察局·\x01",
            "特别任务支援科将要执行强制搜查\x01",
            "以及逮捕任务。\x02\x03",

            "#00013F对象为前议长哈尔特曼\x01",
            "与前市长秘书阿奈斯特，共计二人。\x02\x03",

            "#00007F期限为本日１７：００，\x01",
            "请大家全力以赴！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(2506, 255, 100, 0)    #voice#Dudley

    #C0070
    ChrTalk(
        0x10A,
        "#00607F#12P好！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(4024, 255, 100, 1)    #voice#Arios

    #C0071
    ChrTalk(
        0x108,
        "#01407F#6P明白……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(2481, 255, 100, 2)    #voice#Noel

    #C0072
    ChrTalk(
        0x109,
        "#6P#10107F#6P明白了……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※关于『调查手册』。\x02\x03",

            "※在游戏中发生的\x01",
            "  各种事件会自动\x01",
            "  记录到『调查手册』中。\x02\x03",

            "※在主菜单中打开［ITEMS］项目，\x01",
            "  在其中使用『调查手册』，\x01",
            "  或在场景中按下『△键＋左方向键』，\x01",
            "  即可查阅其内容。\x02\x03",

            "※各类资料与指南也可在手册中查阅，\x01",
            "  请多加利用。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Sound(814, 0, 100, 0)

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※关于『战斗手册』。\x02\x03",

            "※在战斗中遇到敌人时，\x01",
            "  其情报会自动记录到\x01",
            "  『战斗手册』中。\x02\x03",

            "※与调查手册相同，\x01",
            "  使用道具栏中的『战斗手册』，\x01",
            "  或按下『△键＋右方向键』，\x01",
            "  即可查阅其内容。 \x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 3000, -8000, 0, 0)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 1)
    OP_29(0xA0, 0x1, 0x1)
    ModifyEventFlags(0, 0, 0x80)
    OP_CC(0x1, 0xFF, 0x0)
    OP_E2(0x2)
    OP_E0(0x19, 0x0)
    Sleep(300)
    OP_E0(0x80, 0x0)
    EventEnd(0x5)
    Return()

    # Function_14_28C5 end

    def Function_15_33CC(): pass

    label("Function_15_33CC")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SoundLoad(814)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis091.itp")
    OP_68(164900, -3800, -2200, 0)
    MoveCamera(325, 24, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x101, 169900, -5000, -2200, 270)
    SetChrPos(0x109, 172300, -5000, -2200, 270)
    SetChrFlags(0x109, 0x40)
    SetChrPos(0x10A, 171300, -5000, -1100, 270)
    SetChrPos(0x108, 171300, -5000, -3300, 270)

    def lambda_3485():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3485)
    Sleep(50)

    def lambda_34A2():
        OP_97(0x108, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_34A2)
    Sleep(50)

    def lambda_34BF():
        OP_97(0x10A, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_34BF)
    Sleep(50)

    def lambda_34DC():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_34DC)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x10A, 0)
    OP_63(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    WaitChrThread(0x109, 0)
    ClearChrFlags(0x109, 0x40)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0075
    ChrTalk(
        0x109,
        "#12P#10105F这、这是……\x02",
    )

    CloseMessageWindow()
    OP_68(147900, -2800, -2200, 3500)
    MoveCamera(303, 17, 0, 3500)
    SetCameraDistance(25000, 3500)
    Sleep(500)

    def lambda_358F():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_358F)
    Sleep(100)

    def lambda_35AC():
        OP_97(0x108, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_35AC)
    Sleep(100)

    def lambda_35C9():
        OP_97(0x10A, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_35C9)
    Sleep(100)

    def lambda_35E6():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_35E6)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(154400, -3700, -2200, 0)
    MoveCamera(325, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18500, 0)
    SetCameraDistance(17500, 1500)
    OP_0D()
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    TurnDirection(0x101, 0x108, 500)

    #C0076
    ChrTalk(
        0x101,
        "#00010F#5P亚里欧斯先生，这是……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x108,
        (
            "#6P#01403F嗯……\x01",
            "『感应力强化实验』设备的残骸。\x02\x03",

            "#01401F教团成员给孩子们喂食『真知』，并在这里\x01",
            "用尽一切方法来提升他们的五感与感应力，\x01",
            "孩子们就这样成为了实验的牺牲品。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x10A,
        "#00608F啧……这群邪教徒。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        (
            "#12P#10110FＤ∴Ｇ教团……\x02\x03",

            "#10103F虽然早已被消灭了，\x01",
            "但仍然无法原谅他们啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0x10E, 0x1F4)
    Sleep(300)

    #C0080
    ChrTalk(
        0x101,
        "#00008F#11P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(1000)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    #C0081
    ChrTalk(
        0x101,
        (
            "#00003F#11P……不知阿奈斯特和哈尔特曼\x01",
            "特意来到这种地方\x01",
            "想做什么……\x02\x03",

            "#00001F总之，我们绝不能让任何人\x01",
            "再度利用这个场所。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x108,
        "#6P#01403F嗯，那当然。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x109,
        "#4P#10107F全力阻止他们吧！\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x10A,
        "#00607F好，赶快行动！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "关于魔兽的情报解析\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0086
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※除了镶嵌着「情报」回路的达德利之外，\x01",
            "  其他角色无法查看魔兽的情报。\x02\x03",

            "※不过，只需使用「战斗探测器」\x01",
            "  或幻属性的辅助魔法「情报解析」，\x01",
            "  就可以获得魔兽或敌人的情报。\x02\x03",

            "※从魔兽情报中可以了解到它的\x01",
            "  弱点属性，以及不能免疫的异常状态，\x01",
            "  从而使战斗效率得到提高。\x02\x03",

            "※另外，取得魔兽或敌人的情报之后，\x01",
            "  再遇到同类魔兽或敌人时，只要将光标移动\x01",
            "  到其所在处，并按下『□键』，即可随时查看。\x02\x03",

            "※在当前阶段，只有达德利可以使用\x01",
            "  幻属性的辅助魔法「情报解析」。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(100)
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 155000, -5000, -2200, 270)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x120, 2)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_15_33CC end

    def Function_16_3B16(): pass

    label("Function_16_3B16")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 3)), scpexpr(EXPR_END)), "loc_3B86")
    TalkBegin(0xFF)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "石门牢固地关闭着。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)

    #C0088
    ChrTalk(
        0x108,
        (
            "#01400F右手边的深处有开关，\x01",
            "我们赶快过去操作吧。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_3B86")

    EventBegin(0x0)
    OP_E2(0x3)
    Fade(500)
    OP_68(1100, 1300, 77900, 0)
    MoveCamera(320, 24, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19500, 0)
    SetChrPos(0x101, 1100, 0, 77900, 270)
    SetChrPos(0x109, 2800, 0, 76300, 270)
    SetChrPos(0x10A, 3400, 0, 77400, 270)
    SetChrPos(0x108, 3300, 0, 78900, 230)
    OP_0D()

    #C0089
    ChrTalk(
        0x101,
        "#11P#00005F这是……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        "#12P#10105F岩石制的大门吗？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x108,
        (
            "#01401F#4P这是通向深处的入口大门，\x01",
            "我们在六年前已经把它打开了……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x10A,
        (
            "#12P#00603F哼，看来是阿奈斯特\x01",
            "重新开启了机关。\x02\x03",

            "#00600F有没有解除方法？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(2500, 1300, 79260, 1000)
    OP_93(0x108, 0x5A, 0x190)
    OP_6F(0x1)

    #C0093
    ChrTalk(
        0x108,
        (
            "#5P#01400F右手边的深处有开关，\x01",
            "操作那个就可以把门打开。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3D2C():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3D2C)
    Sleep(50)

    def lambda_3D3C():
        OP_93(0x10A, 0x32, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_3D3C)
    Sleep(50)

    def lambda_3D4C():
        OP_93(0x109, 0x32, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3D4C)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 1)

    #C0094
    ChrTalk(
        0x101,
        "#00001F#5P好，我们赶快去看看吧。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x120, 3)
    SetChrPos(0x0, 2100, 0, 77900, 90)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_16_3B16 end

    def Function_17_3DA7(): pass

    label("Function_17_3DA7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 4)), scpexpr(EXPR_END)), "loc_3DE3")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0095
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "已经不能动了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    EventEnd(0x3)
    Jump("loc_3F35")

    label("loc_3DE3")

    EventBegin(0x1)

    #A0096
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个开关。\x01",
            "要操作吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F2E")
    Fade(500)
    OP_68(36110, 4130, 221300, 0)
    MoveCamera(0, 38, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x0, 36200, 2830, 221010, 360)
    SetChrPos(0x1, 37050, 2320, 219590, 360)
    SetChrPos(0x2, 35320, 2330, 219560, 360)
    SetChrPos(0x3, 36200, 2009, 218660, 360)
    OP_0D()
    Sleep(500)
    Sound(143, 0, 100, 0)
    OP_71(0x6, 0x0, 0x14, 0x0, 0x0)
    Sleep(1000)
    Fade(500)
    OP_68(-1090, 1360, 78640, 0)
    MoveCamera(291, 30, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(19000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    OP_74(0x5, 0xF)
    OP_71(0x5, 0x0, 0x14, 0x0, 0x0)
    Sleep(1300)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x64, 0x0, 0x3E8, 0x64)
    Sleep(1000)
    SetScenarioFlags(0x120, 4)
    OP_65(0x0, 0x1)

    label("loc_3F2E")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_3F35")

    Return()

    # Function_17_3DA7 end

    def Function_18_3F36(): pass

    label("Function_18_3F36")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9A")

    #C0097
    ChrTalk(
        0x101,
        (
            "#00003F我们不能在此时回头。\x02\x03",

            "#00001F无论如何也要抓到\x01",
            "阿奈斯特和哈尔特曼。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4069")

    label("loc_3F9A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FEA")

    #C0098
    ChrTalk(
        0x109,
        (
            "#10101F我们不能在这种地方\x01",
            "磨磨蹭蹭，\x01",
            "尽快向深处前进吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4069")

    label("loc_3FEA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4033")

    #C0099
    ChrTalk(
        0x10A,
        (
            "#00603F阿奈斯特和哈尔特曼在里面，\x01",
            "赶快追上去吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4069")

    label("loc_4033")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4069")

    #C0100
    ChrTalk(
        0x108,
        (
            "#01401F没时间回头了，\x01",
            "赶快追上去。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4069")

    SetChrPos(0x0, 2860, -8000, -8020, 0)
    EventEnd(0x4)
    Return()

    # Function_18_3F36 end

    def Function_19_407D(): pass

    label("Function_19_407D")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0101
    ChrTalk(
        0x8,
        (
            "#00603F班宁斯，\x01",
            "你想去哪里？\x02\x03",

            "#00601F禁止擅自行动。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0102
    ChrTalk(
        0x101,
        "#00003F对不起，我马上就准备好。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2430, -8000, 3380, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_19_407D end

    SaveToFile()

Try(main)
