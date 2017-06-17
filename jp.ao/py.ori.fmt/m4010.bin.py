from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ダドリー捜査官",         # 1
        "アリオス",               # 2
        "ダイナソゥ",             # 3
        "bm4010",                 # 4
        "bm4010",                 # 5
        "bm4010",                 # 6
        "bm4010",                 # 7
    ))

    ATBonus("ATBonus_460", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_470", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_46A6", 2,   2,   0,   2,   2,   2,   1)
    Sepith("Sepith_469E", 0,   4,   0,   4,   1,   1,   1)
    Sepith("Sepith_4696", 3,   4,   5,   2,   0,   0,   0)

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
        "BattleInfo_610", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_46A6", 60, 25, 10, 0,
        (
            ("ms83800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83800.dat", "ms83800.dat", "ms83800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_574", 0x0000, 46, 6, 60, 6, 1, 20, 0, "bm4010", "Sepith_469E", 60, 25, 10, 0,
        (
            ("ms83600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_490", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            ("ms83600.dat", "ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_4B0", "MonsterBattlePostion_510", "ed7450", "ed7453", "ATBonus_460"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_530", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_4696", 100, 0, 0, 0,
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
        "Function_5_F2E",          # 05, 5
        "Function_6_1145",         # 06, 6
        "Function_7_12AC",         # 07, 7
        "Function_8_13FD",         # 08, 8
        "Function_9_154E",         # 09, 9
        "Function_10_1552",        # 0A, 10
        "Function_11_15EF",        # 0B, 11
        "Function_12_169A",        # 0C, 12
        "Function_13_1796",        # 0D, 13
        "Function_14_2BEA",        # 0E, 14
        "Function_15_37F8",        # 0F, 15
        "Function_16_3FC4",        # 10, 16
        "Function_17_4287",        # 11, 17
        "Function_18_442C",        # 12, 18
        "Function_19_45B9",        # 13, 19
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EDD")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_E66")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_ED8")

    label("loc_E66")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_ED8")

    Jump("loc_F22")

    label("loc_EDD")

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

    label("loc_F22")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_DDD end

    def Function_5_F2E(): pass

    label("Function_5_F2E")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FF")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21A, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102D")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F8B():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_F8B)

    def lambda_FA5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_FA5)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_100E"),
        (2, "loc_101D"),
        (1, "loc_102A"),
        (SWITCH_DEFAULT, "loc_102D"),
    )


    label("loc_100E")

    SetScenarioFlags(0x21A, 6)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_102D")

    label("loc_101D")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_102A")

    OP_B9(0x0)
    Return()

    label("loc_102D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x64, 1)"), scpexpr(EXPR_END)), "loc_108A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_10FA")

    label("loc_108A")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x64),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10FA")

    Jump("loc_1139")

    label("loc_10FF")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_1139")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F2E end

    def Function_6_1145(): pass

    label("Function_6_1145")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1275")
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
            "#56I地のセピス×３０\x01\x07\x02",

            "#57I水のセピス×３０\x01\x07\x02",

            "#58I火のセピス×３０\x01\x07\x02",

            "#59I風のセピス×３０\x01\x07\x02",

            "#60I時のセピス×３０\x01\x07\x02",

            "#61I空のセピス×３０\x01\x07\x02",

            "#62I幻のセピス×３０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1E0, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_129A")

    label("loc_1275")


    #A0009
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

    label("loc_129A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1145 end

    def Function_7_12AC(): pass

    label("Function_7_12AC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AC")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x41, 1)"), scpexpr(EXPR_END)), "loc_1335")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_13A7")

    label("loc_1335")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x41),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13A7")

    Jump("loc_13F1")

    label("loc_13AC")

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

    label("loc_13F1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12AC end

    def Function_8_13FD(): pass

    label("Function_8_13FD")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14FD")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_1486")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E0, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_14F8")

    label("loc_1486")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
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
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_14F8")

    Jump("loc_1542")

    label("loc_14FD")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
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

    label("loc_1542")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_13FD end

    def Function_9_154E(): pass

    label("Function_9_154E")

    Call(1, 6)
    Return()

    # Function_9_154E end

    def Function_10_1552(): pass

    label("Function_10_1552")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_157F")
    FadeToDark(500, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_E2(0x3)
    Call(0, 14)
    Return()

    label("loc_157F")


    #C0016
    ChrTalk(
        0x8,
        (
            "#00603F各々の《エニグマⅡ》に\x01",
            "今渡したマスタークオーツを\x01",
            "セットするがいい。\x02\x03",

            "#00600Fまずはそれからだ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_10_1552 end

    def Function_11_15EF(): pass

    label("Function_11_15EF")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BF(0x0, 0x63)"), scpexpr(EXPR_EXEC_OP, "OP_BF(0x8, 0x63)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_161C")
    FadeToDark(500, 0, -1)
    OP_0D()
    TalkEnd(0xFE)
    EventBegin(0x0)
    OP_E2(0x3)
    Call(0, 14)
    Return()

    label("loc_161C")


    #C0017
    ChrTalk(
        0x9,
        (
            "#01403Fそれにしても、またこの場所に\x01",
            "踏み込むことになろうとはな……\x02\x03",

            "#01400Fとにかく――\x01",
            "一刻も早く２人を拘束するぞ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_15EF end

    def Function_12_169A(): pass

    label("Function_12_169A")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0018
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1787")
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

    label("loc_1787")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_12_169A end

    def Function_13_1796(): pass

    label("Function_13_1796")

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
            "#30W──俺たちがこの地を訪れたのは\x01",
            "帝国政府からの連絡がきっかけだった。\x02\x03",

            "あの教団事件から数ヶ月後──\x02\x03",

            "どさくさに紛れて、帝国へ亡命していた\x01",
            "ハルトマン元議長と元市長秘書アーネストが\x01",
            "帝国からの追放処分を受けたのである。\x02\x03",

            "何故か、２人は新たな潜伏先として\x01",
            "共和国最西端のアルタイル市を選び……\x02\x03",

            "急遽#4Rきゅうきょ#、新市長によって\x01",
            "共和国政府との協議が秘密裏に行われ、\x01",
            "２人の国外逮捕が執行される事となった。\x02\x03",

            "しかし、極めて政治的な問題を持つため、\x01",
            "逮捕は正規の指揮系統から外れている\x01",
            "『特務支援課』に任される形となり……\x02\x03",

            "さらに捜査一課、警備隊、ギルドが協力する\x01",
            "異例の捜査体制が整えられたのだった。\x02\x03",

            "そしてアルタイル市での捜査から数日──\x02\x03",

            "俺たちはハルトマン、アーネスト両名が\x01",
            "教団の旧ロッジ跡に向かった事を突き止めた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)

    def lambda_1B96():
        OP_97(0x101, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1B96)
    Sleep(100)

    def lambda_1BB3():
        OP_97(0x108, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_1BB3)
    Sleep(100)

    def lambda_1BD0():
        OP_97(0x10A, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_1BD0)
    Sleep(100)

    def lambda_1BED():
        OP_97(0x109, 0x0, 0x0, 0x4E20, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1BED)
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
        "#00005F#30Wここは……\x02",
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
            "#6P#10108F鍾乳洞ですか……\x01",
            "でも、人の手が入っていますね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x108,
        (
            "#01403F元々は数百年前に使われていた\x01",
            "石窟寺院跡だったようだ。\x02\x03",

            "それを《Ｄ∴Ｇ教団》が改修し、\x01",
            "《儀式》を行うロッジとして利用した。\x02\x03",

            "#01401F６年前のあの日までな。\x02",
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
            "#00006F……課長とアリオスさん、\x01",
            "それに兄貴が制圧した時ですね。\x02\x03",

            "#00001Fそして兄貴はここで、ただ一人\x01",
            "生き残ったティオを救出した……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0024
    AnonymousTalk(
        0x108,
        (
            "#01403Fああ、正直それだけが\x01",
            "あの地獄のような惨状における\x01",
            "唯一の慰めだった。\x02\x03",

            "#01400F今となってはその痕跡も\x01",
            "ほとんど無くなっているがな。\x02",
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
            "#6P#10106F何だか信じられませんね……\x01",
            "そんな事があったなんて。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x10A,
        (
            "#6P#00603Fフン、どこまでも\x01",
            "最悪な連中だったようだな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x108, 500)
    Sleep(300)

    #C0028
    ChrTalk(
        0x10A,
        (
            "#12P#00600F当時、共和国軍が動けなかったのは\x01",
            "一部の将校が教団に弱味を\x01",
            "握られていたからだそうだが……？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x108, 0x10A, 500)

    #C0029
    ChrTalk(
        0x108,
        (
            "#01402F#5Pああ、だからこそセルゲイ班に\x01",
            "ここの制圧が任されたわけだ。\x02\x03",

            "#01404F今にしてみれば、\x01",
            "ギルドも真っ青と言うくらいの\x01",
            "強引な介入の仕方だったが。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x10A,
        (
            "#12P#00602Fフン、さすがは悪名高き\x01",
            "セルゲイ班といったところか。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(150)

    #C0031
    ChrTalk(
        0x101,
        (
            "#11P#00004Fはは……何だか当時の光景が\x01",
            "目に浮かぶ気がしますね。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 500)
    Sleep(300)

    #C0032
    ChrTalk(
        0x101,
        (
            "#11P#00001F──アリオスさん。\x01",
            "２人が向かっているとしたら\x01",
            "ロッジのどの辺りでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_21FB():
        TurnDirection(0xFE, 0x108, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_21FB)
    Sleep(100)

    #C0033
    ChrTalk(
        0x108,
        (
            "#01403F#5Pやはり最奥にある\x01",
            "《儀式の間》の可能性が高い。\x02\x03",

            "《太陽の砦》にあったような\x01",
            "不思議な祭壇が残されている。\x02\x03",

            "#01401Fハルトマンはともかく……\x01",
            "アーネストがそこを目指しても\x01",
            "不思議ではないだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x101,
        "#11P#00003F……確かに。\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x109,
        (
            "#12P#10113Fひょっとして、\x01",
            "あの《グノーシス》という薬も\x01",
            "関係しているんでしょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x10A,
        (
            "#12P#00606Fその可能性は否定できんな。\x02\x03",

            "どうやらアーネストは\x01",
            "ヨアヒムから《グノーシス》を\x01",
            "それなりに受け取っていたようだ。\x02\x03",

            "#00601Fそれも蒼色のではなく、紅色の。\x02",
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
            "#5P#10107Fそ、それって……\x01",
            "人を化物に変えるっていう！？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)

    #C0038
    ChrTalk(
        0x101,
        (
            "#11P#00003Fああ、場合によっては\x01",
            "同行しているハルトマンの身が\x01",
            "危ないかもしれない。\x02\x03",

            "#00001F取り返しが付かなくなる前に\x01",
            "何としても２人を拘束しよう。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)

    #C0039
    ChrTalk(
        0x109,
        (
            "#6P#10101Fええ！\x02\x03",

            "#10106Fはあ……でも参ったなぁ。\x02\x03",

            "こんなタイミングで\x01",
            "エニグマのバージョンアップが\x01",
            "行われちゃうなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#11P#00006Fふう、そうなんだよな。\x02",
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
        "#11P#00001F『エニグマⅡ』か……\x02",
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
            "#10108F中心に嵌めるっていう\x01",
            "新型の『マスタークオーツ』……\x02\x03",

            "それが間に合わなかったから\x01",
            "結局、アーツは使えない状態ですし。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0043
    AnonymousTalk(
        0x101,
        (
            "#00006F毎度ながらエプスタイン財団も\x01",
            "切り替えが突然すぎるんだよな。\x02\x03",

            "ティオの所属している場所を\x01",
            "悪く言いたくはないんだけど……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0044
    AnonymousTalk(
        0x10A,
        (
            "#00603Fフン、いくらタイミングが\x01",
            "悪いとはいえ泣き言を抜かすな。\x02\x03",

            "#00600Fきちんと準備していれば\x01",
            "これくらいは用意できるだろう。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x2, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CC(0x0, 0x2, 0x0)

    def lambda_27CE():
        OP_9A(0xFE, 0x101, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_27CE)
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xDC, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    #C0046
    ChrTalk(
        0x101,
        "#00005Fえ……\x02",
    )

    CloseMessageWindow()

    def lambda_285F():
        OP_96(0xFE, 0x125C, 0xFFFFE0C0, 0x640, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_285F)

    #C0047
    ChrTalk(
        0x108,
        (
            "#01404F#5Pフフ、ならば俺の方からも\x01",
            "予備を一つ提供しよう。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_28B8():
        OP_9A(0xFE, 0x109, 0x384, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_28B8)
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
            "を受け取った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    AddItemNumber(0xDD, 1)
    SetMessageWindowPos(14, 280, 60, 3)

    def lambda_2924():
        OP_96(0xFE, 0x640, 0xFFFFE0C0, 0x708, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2924)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x10A, 1)

    #C0049
    ChrTalk(
        0x109,
        (
            "#12P#10105Fこれ……\x01",
            "マスタークオーツですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#00005Fこれを俺たちに……？\x02",
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x10A,
        (
            "#12P#00601Fフン、足手まといに\x01",
            "なられても困るというだけだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x108,
        (
            "#01402F#5P《エニグマⅡ》の中心に\x01",
            "好きな方をセットするといい。\x02\x03",

            "どちらも、付けたらすぐに\x01",
            "複数のアーツが使えるはずだ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 600)

    #C0053
    ChrTalk(
        0x101,
        "#11P#00002Fはい！\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x109,
        "#12P#10102F分かりました！\x02",
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
            "※新型オーブメント《エニグマⅡ》は、\x01",
            "  中央のスロットにマスタークオーツを\x01",
            "  セットすることができます。\x02\x03",

            "※キャンプメニューから[ORBMENT]を開き、\x01",
            "  [QUARTZ]を選択することで、\x01",
            "  マスタークオーツのセットが行えます。\x07\x00\x02",
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2BE2")
    SetScenarioFlags(0x21, 0)

    label("loc_2BE2")

    OP_E2(0x2)
    Sleep(400)
    EventEnd(0x5)
    Return()

    # Function_13_1796 end

    def Function_14_2BEA(): pass

    label("Function_14_2BEA")

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
        "#12P#00600Fよし、準備は済んだな。\x02",
    )

    CloseMessageWindow()

    def lambda_2D51():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2D51)
    Sleep(100)

    def lambda_2D61():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_2D61)
    WaitChrThread(0x101, 2)

    #C0057
    ChrTalk(
        0x101,
        (
            "#00000Fはい、お待たせしました。\x02\x03",

            "#00002Fその……\x01",
            "わざわざ用意してもらって\x01",
            "本当に助かりました。\x02",
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
            "#12P#00605Fべ、別にお前たちのために\x01",
            "用意したわけじゃない。\x02\x03",

            "#00606F──それよりバニングス。\x01",
            "分かっているんだろうな？\x02\x03",

            "#00601Fこの任務は、お前にとって\x01",
            "一課での研修の仕上げでもある。\x02\x03",

            "#00607F万が一、無様を晒#2Rさら#したら\x01",
            "やり直しにするから心しておけ！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    #Sound(3317, 255, 100, 0)    #voice#Lloyd

    #C0059
    ChrTalk(
        0x101,
        "#00000F#30W……はい！\x02",
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x109,
        (
            "#6P#10112F#6P（あはは……\x01",
            "  素直じゃない人ですねぇ。）\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x108,
        (
            "#01404F#5P（フッ、見た目よりも\x01",
            "  はるかに熱くタフな男だ。）\x02\x03",

            "#01402F（……さすが一課でガイと\x01",
            "  張り合ったけはあるようだな。）\x02",
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
        "よし──それでは始めましょう。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)

    def lambda_3071():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_3071)
    Sleep(50)

    def lambda_3081():

        label("loc_3081")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3081")

    QueueWorkItem2(0x10A, 2, lambda_3081)
    Sleep(50)

    def lambda_3096():

        label("loc_3096")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3096")

    QueueWorkItem2(0x108, 2, lambda_3096)
    WaitChrThread(0x109, 2)
    OP_93(0x101, 0x0, 0x1F4)

    def lambda_30B3():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_30B3)
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
            "#00003Fクロスベル警察、捜査一課所属、\x01",
            "アレックス・ダドリー主任捜査官。\x02",
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
        "#30Wああ。\x02",
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
            "#00000Fクロスベル警備隊所属、\x01",
            "ノエル・シーカー曹長。\x02",
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
        "#30Wはいっ！\x02",
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
            "#00004Fそして特別補佐として\x01",
            "遊撃士協会クロスベル支部所属、\x01",
            "アリオス・マクレインどの。\x02",
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
        "#30Wああ。\x02",
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
            "#00003Fこれよりクロスベル警察、\x01",
            "特務支援課による強制捜索、\x01",
            "および逮捕任務を執行します。\x02\x03",

            "#00013F逮捕対象は、ハルトマン元議長、\x01",
            "およびアーネスト元市長秘書の２名。\x02\x03",

            "#00007F期限は本日１７：００──\x01",
            "各自全力を尽くしてください！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(2506, 255, 100, 0)    #voice#Dudley

    #C0070
    ChrTalk(
        0x10A,
        "#00607F#12Pいいだろう！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(4024, 255, 100, 1)    #voice#Arios

    #C0071
    ChrTalk(
        0x108,
        "#01407F#6P承知……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    #Sound(2481, 255, 100, 2)    #voice#Noel

    #C0072
    ChrTalk(
        0x109,
        "#6P#10107F#6P了解です……！\x02",
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
            "※『捜査手帳』について。\x02\x03",

            "※『捜査手帳』には、\x01",
            "  ゲーム中で起こった様々な出来事が\x01",
            "  自動的に記録されていきます。\x02\x03",

            "※キャンプメニューから[ITEMS]を開いて\x01",
            "  『捜査手帳』を使用するか、\x01",
            "  フィールド上で『△ボタン＋方向キー左』で\x01",
            "  内容を見ることが出来ます。 \x02\x03",

            "※マニュアルなども確認できるので、\x01",
            "  活用してください。\x07\x00\x02",
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
            "※『戦闘手帳』について。\x02\x03",

            "※『戦闘手帳』には、\x01",
            "  戦闘で戦った相手の情報が\x01",
            "  自動的に記録されていきます。\x02\x03",

            "※捜査手帳と同じく、\x01",
            "  アイテムの『戦闘手帳』を使用する、\x01",
            "  もしくは『△ボタン＋方向キー右』で\x01",
            "  内容を見ることが出来ます。 \x07\x00\x02",
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

    # Function_14_2BEA end

    def Function_15_37F8(): pass

    label("Function_15_37F8")

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

    def lambda_38B1():
        OP_97(0x101, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_38B1)
    Sleep(50)

    def lambda_38CE():
        OP_97(0x108, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_38CE)
    Sleep(50)

    def lambda_38EB():
        OP_97(0x10A, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_38EB)
    Sleep(50)

    def lambda_3908():
        OP_97(0x109, 0xFFFFEC78, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3908)
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
        "#12P#10105Fこ、これって……\x02",
    )

    CloseMessageWindow()
    OP_68(147900, -2800, -2200, 3500)
    MoveCamera(303, 17, 0, 3500)
    SetCameraDistance(25000, 3500)
    Sleep(500)

    def lambda_39BF():
        OP_97(0x101, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_39BF)
    Sleep(100)

    def lambda_39DC():
        OP_97(0x108, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 0, lambda_39DC)
    Sleep(100)

    def lambda_39F9():
        OP_97(0x10A, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_39F9)
    Sleep(100)

    def lambda_3A16():
        OP_97(0x109, 0xFFFFD8F0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_3A16)
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
        "#00010F#5Pアリオスさん、これが……\x02",
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x108,
        (
            "#6P#01403Fああ……\x01",
            "『感応#4Rかんのう#力強化実験』の名残だ。\x02\x03",

            "#01401Fグノーシスを投与された子供たちが\x01",
            "ありとあらゆる方法で五感と霊感を\x01",
            "高める実験の犠牲となった。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x10A,
        "#00608Fチッ……外道どもが。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x109,
        (
            "#12P#10110FＤ∴Ｇ教団……\x02\x03",

            "#10103Fとっくに潰れたんでしょうけど\x01",
            "正直、許せないです……\x02",
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
            "#00003F#11P……アーネストたちが\x01",
            "何をしようとしているのか\x01",
            "分かりませんが……\x02\x03",

            "#00001F二度と、この場所を利用される\x01",
            "わけにはいきませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x108,
        "#6P#01403Fああ、勿論だ。\x02",
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0x109,
        "#4P#10107F全力で阻止しましょう！\x02",
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0x10A,
        "#00607Fよし、先を急ぐぞ！\x02",
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
            "魔獣のアナライズについて\x07\x00\x02",
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
            "※クオーツ「情報」を付けているダドリー以外の\x01",
            "  キャラクターは、魔獣の情報を見る事ができません。\x02\x03",

            "※ただしアイテムの「バトルスコープ」や\x01",
            "  幻属性の補助アーツ「アナライズ」を使うと\x01",
            "  魔獣や敵の情報を取得する事ができます。\x02\x03",

            "※その魔獣が苦手とするアーツの属性や\x01",
            "  どんな状態異常が効くかなどが判るため\x01",
            "  効率的に戦闘することが可能になります。\x02\x03",

            "※なお、取得した魔獣や敵の情報は\x01",
            "  同じ種類であればカーソルを合わせて\x01",
            "  『□ボタン』を押せばいつでも確認できます。\x02\x03",

            "※ちなみに補助アーツ「アナライズ」は\x01",
            "  現状ではダドリーが使用することが可能です。\x07\x00\x02",
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

    # Function_15_37F8 end

    def Function_16_3FC4(): pass

    label("Function_16_3FC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 3)), scpexpr(EXPR_END)), "loc_404A")
    TalkBegin(0xFF)
    SetChrName("")

    #A0087
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "岩の扉は固く閉ざされている。\x07\x00\x02",
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
            "#01400F――右手の奥にスイッチがある。\x01",
            "急いで解除に向かうぞ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    label("loc_404A")

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
        "#11P#00005Fこれは……\x02",
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0x109,
        "#12P#10105F岩の扉、でしょうか？\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0x108,
        (
            "#01401F#4P奥に続いているゲートだ。\x01",
            "６年前に解除したはずだが……\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x10A,
        (
            "#12P#00603Fフン、アーネストあたりが\x01",
            "仕掛け直したのかもしれんな。\x02\x03",

            "#00600F解除方法はあるのか？\x02",
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
            "#5P#01400F右手の奥にスイッチがある。\x01",
            "それで開くはずだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_420A():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_420A)
    Sleep(50)

    def lambda_421A():
        OP_93(0x10A, 0x32, 0x1F4)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_421A)
    Sleep(50)

    def lambda_422A():
        OP_93(0x109, 0x32, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_422A)
    Sleep(50)
    WaitChrThread(0x10A, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x101, 1)

    #C0094
    ChrTalk(
        0x101,
        "#00001F#5Pよし、行ってみましょう。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    SetScenarioFlags(0x120, 3)
    SetChrPos(0x0, 2100, 0, 77900, 90)
    OP_69(0xFF, 0x0)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_16_3FC4 end

    def Function_17_4287(): pass

    label("Function_17_4287")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 4)), scpexpr(EXPR_END)), "loc_42C9")
    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0095
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
    EventEnd(0x3)
    Jump("loc_442B")

    label("loc_42C9")

    EventBegin(0x1)

    #A0096
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4424")
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

    label("loc_4424")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_442B")

    Return()

    # Function_17_4287 end

    def Function_18_442C(): pass

    label("Function_18_442C")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_449E")

    #C0097
    ChrTalk(
        0x101,
        (
            "#00003F引き返すわけにはいかない。\x02\x03",

            "#00001F何としても、アーネストたちを\x01",
            "捕まえないとな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A5")

    label("loc_449E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_44FC")

    #C0098
    ChrTalk(
        0x109,
        (
            "#10101Fこんな所で\x01",
            "もたもたしていられない――\x01",
            "急いで奥を目指さないと。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A5")

    label("loc_44FC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4559")

    #C0099
    ChrTalk(
        0x10A,
        (
            "#00603Fアーネストとハルトマンは奥だ。\x01",
            "――さっさと後を追いかけるぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_45A5")

    label("loc_4559")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45A5")

    #C0100
    ChrTalk(
        0x108,
        (
            "#01401F引き返している時間はない。\x01",
            "――急いで後を追うぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_45A5")

    SetChrPos(0x0, 2860, -8000, -8020, 0)
    EventEnd(0x4)
    Return()

    # Function_18_442C end

    def Function_19_45B9(): pass

    label("Function_19_45B9")

    EventBegin(0x1)
    OP_4B(0x8, 0xFF)
    TurnDirection(0x8, 0x101, 500)
    Sleep(300)

    #C0101
    ChrTalk(
        0x8,
        (
            "#00603Fバニングス、\x01",
            "一体どこに行くつもりだ。\x02\x03",

            "#00601F勝手な行動は許さんぞ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x8, 500)
    Sleep(300)

    #C0102
    ChrTalk(
        0x101,
        "#00003Fすみません、すぐに準備します。\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x0, 2430, -8000, 3380, 180)
    OP_93(0x8, 0x5A, 0x0)
    OP_4C(0x8, 0xFF)
    EventEnd(0x4)
    Return()

    # Function_19_45B9 end

    SaveToFile()

Try(main)
