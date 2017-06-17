from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r2070.bin",                # FileName
        "R2070",                    # MapName
        "R2070",                    # Location
        0x0074,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2070", "r0000_1", "", "", "", ""),   # include
        0x01,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 116, 0, 0, 0, 1],
    )

    BuildStringList((
        "r2070",                  # 0
        "SE控制",                 # 1
        "br2070",                 # 2
        "br2070",                 # 3
        "玛因兹山道方向",         # 4
    ))

    ATBonus("ATBonus_3E4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3154", 12,  0,   9,   1,   7,   3,   6)
    Sepith("Sepith_315C", 0,   7,   3,   12,  6,   7,   1)

    MonsterBattlePostion("MonsterBattlePostion_444", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_448", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_450", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_458", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_45C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_4A4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_4A8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_4AC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_4B0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_4B4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_4B8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_4BC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_4C0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_424", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_434", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_438", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_43C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_440", 2, 13, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 23, 6, 60, 6, 1, 25, 0, "br2070", "Sepith_3154", 30, 40, 20, 10,
        (
            ("ms76100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms76100.dat", "ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
        )
    )

    BattleInfo(
        "BattleInfo_58C", 0x0000, 23, 6, 60, 6, 1, 40, 0, "br2070", "Sepith_315C", 30, 45, 20, 5,
        (
            ("ms64300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms64300.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms64300.dat", "ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms64300.dat", "ms66300.dat", "ms66300.dat", "ms66300.dat", 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
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
        "monster/ch76150.itc",               # 10
        "monster/ch76150.itc",               # 11
        "monster/ch64350.itc",               # 12
        "monster/ch64350.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-27230,  5960,    0,       0x1010000,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-68500,  36190,   10000,   0x1010000,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-107980, 55130,   6000,    0x1010000,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-111460, 28450,   2000,    0x1010000,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-108740, 75420,   20000,   0x1010000,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-137070, 87090,   20000,   0x1010000,    "BattleInfo_58C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-134470, 133220,  20000,   0x1010000,    "BattleInfo_4C4", 0,   16,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 10,  -96.0,                 175.0,                 18.75,                 1406.25,               [0.04714043438434601,  0.14142140746116638,   -0.0,                  0.0,                   -0.047140467911958694, 0.14142130315303802,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   12.775063514709473,    -11.172272682189941,   -3.75,                 1.0])
    DeclEvent(0x0000, 0, 8,   -136.0,                99.0,                  18.75,                 2500.0,                [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   13.600000381469727,    -9.90000057220459,     -3.75,                 1.0])

    DeclActor(-108720, 2000,    22560,   1200,    -108720, 3000,    22560,   0x007C, 0,  2,  0x0000)
    DeclActor(-116200, 2000,    29390,   1200,    -116200, 3000,    29390,   0x007C, 0,  3,  0x0000)
    DeclActor(-77840,  3750,    170050,  1200,    -77840,  4750,    170050,  0x007C, 0,  4,  0x0000)
    DeclActor(-99540,  7750,    191810,  1200,    -99540,  8750,    191810,  0x007C, 0,  5,  0x0000)
    DeclActor(-62380,  11750,   159630,  1200,    -62380,  12750,   159630,  0x007C, 0,  7,  0x0000)
    DeclActor(-94450,  20000,   67770,   1200,    -94450,  20000,   67770,   0x007C, 0,  6,  0x0000)
    DeclActor(-132900, 20000,   122090,  5000,    -132900, 20000,   122090,  0x007C, 0,  14, 0x0000)
    DeclActor(-108800, 2000,    28500,   1200,    -108800, 3000,    28500,   0x007C, 0,  15, 0x0000)

    PlaceName(16.25, 0.0, 5.0, 0x0000, 0x0000, "玛因兹山道方向")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_6C4",          # 00, 0
        "Function_1_6E5",          # 01, 1
        "Function_2_B89",          # 02, 2
        "Function_3_CBF",          # 03, 3
        "Function_4_DF5",          # 04, 4
        "Function_5_F2B",          # 05, 5
        "Function_6_1061",         # 06, 6
        "Function_7_1075",         # 07, 7
        "Function_8_1095",         # 08, 8
        "Function_9_109E",         # 09, 9
        "Function_10_121F",        # 0A, 10
        "Function_11_1CAA",        # 0B, 11
        "Function_12_1CBA",        # 0C, 12
        "Function_13_22EA",        # 0D, 13
        "Function_14_231E",        # 0E, 14
        "Function_15_2E4E",        # 0F, 15
    ))


    def Function_0_6C4(): pass

    label("Function_0_6C4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6D5")
    Event(0, 9)

    label("loc_6D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_6E4")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 12)

    label("loc_6E4")

    Return()

    # Function_0_6C4 end

    def Function_1_6E5(): pass

    label("Function_1_6E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_701")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_737")

    label("loc_701")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_737")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_737")

    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_754")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_754")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_768")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_768")

    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_END)), "loc_77A")
    Jump("loc_7B7")

    label("loc_77A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_7B7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_794")
    Jump("loc_7B7")

    label("loc_794")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_7A6")
    Jump("loc_7B7")

    label("loc_7A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x1)"), scpexpr(EXPR_END)), "loc_7B7")
    OP_66(0x6, 0x1)

    label("loc_7B7")

    OP_65(0x7, 0x1)
    SetMapObjFlags(0xD, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x3)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DB")
    OP_66(0x7, 0x1)

    label("loc_7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7EA")
    ClearMapObjFlags(0xD, 0x4)

    label("loc_7EA")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -62550, 11750, 159550, 5000, 3000, 45000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_820")
    SetBarrier(0x3, 0x0, 0x1)
    ClearMapObjFlags(0x4, 0x10)
    Jump("loc_828")

    label("loc_820")

    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_828")

    SetBarrier(0x0, 0x1, 0x1, 0x0, -133980, 20000, 135680, 20000, 2000, 45000)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_86E")
    SetBarrier(0x3, 0x1, 0x1)
    ClearMapObjFlags(0xB, 0x4)
    Jump("loc_872")

    label("loc_86E")

    SetBarrier(0x2, 0x1, 0x1)

    label("loc_872")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_895")
    OP_11(0x28, 0x32, 0x1E, 0x1E, 0xC8, 0x0)
    Jump("loc_8B9")

    label("loc_895")

    SetMapObjFrame(0xFF, "panorama05", 0x0, 0x1)
    SetMapObjFrame(0xFF, "panorama06", 0x0, 0x1)

    label("loc_8B9")

    SetMapObjFlags(0x0, 0x4)
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE2")
    OP_70(0x7, 0x0)
    Jump("loc_AE6")

    label("loc_AE2")

    OP_70(0x7, 0x1E)

    label("loc_AE6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF9")
    OP_70(0x8, 0x0)
    Jump("loc_AFD")

    label("loc_AF9")

    OP_70(0x8, 0x1E)

    label("loc_AFD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B10")
    OP_70(0x9, 0x0)
    Jump("loc_B14")

    label("loc_B10")

    OP_70(0x9, 0x1E)

    label("loc_B14")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B27")
    OP_70(0xA, 0x0)
    Jump("loc_B2B")

    label("loc_B27")

    OP_70(0xA, 0x1E)

    label("loc_B2B")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7B, 4)), scpexpr(EXPR_END)), "loc_B88")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -94450, 20000, 67770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x5, 0x1)

    label("loc_B88")

    Return()

    # Function_1_6E5 end

    def Function_2_B89(): pass

    label("Function_2_B89")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C76")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('野战套装', 1)"), scpexpr(EXPR_END)), "loc_C08")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '野战套装'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_C71")

    label("loc_C08")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '野战套装'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '野战套装'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C71")

    Jump("loc_CB3")

    label("loc_C76")

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

    label("loc_CB3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_B89 end

    def Function_3_CBF(): pass

    label("Function_3_CBF")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DAC")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('中回复药', 1)"), scpexpr(EXPR_END)), "loc_D3E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_DA7")

    label("loc_D3E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '中回复药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_DA7")

    Jump("loc_DE9")

    label("loc_DAC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_DE9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_CBF end

    def Function_4_DF5(): pass

    label("Function_4_DF5")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE2")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('回避２', 1)"), scpexpr(EXPR_END)), "loc_E74")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '回避２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_EDD")

    label("loc_E74")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '回避２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '回避２'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EDD")

    Jump("loc_F1F")

    label("loc_EE2")

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

    label("loc_F1F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_DF5 end

    def Function_5_F2B(): pass

    label("Function_5_F2B")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1018")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('圣灵药', 1)"), scpexpr(EXPR_END)), "loc_FAA")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1013")

    label("loc_FAA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '圣灵药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1013")

    Jump("loc_1055")

    label("loc_1018")

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

    label("loc_1055")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F2B end

    def Function_6_1061(): pass

    label("Function_6_1061")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 4)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_1061 end

    def Function_7_1075(): pass

    label("Function_7_1075")

    TalkBegin(0xFF)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门紧紧关着。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_7_1075 end

    def Function_8_1095(): pass

    label("Function_8_1095")

    SetScenarioFlags(0x87, 7)
    ModifyEventFlags(0, 1, 0x80)
    Return()

    # Function_8_1095 end

    def Function_9_109E(): pass

    label("Function_9_109E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(2800, 600, -400, 0)
    MoveCamera(45, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23500, 0)
    SetChrPos(0x101, 2200, 0, -1000, 270)
    SetChrPos(0x102, 2200, 0, 300, 270)
    SetChrPos(0x103, 3500, 0, -1000, 270)
    SetChrPos(0x104, 3500, 0, 300, 270)
    FadeToBright(1000, 0)
    OP_0D()

    #C0014
    ChrTalk(
        0x101,
        "#0005F这边是……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0301F好像是条小道，\x01",
            "似乎不是通往矿山镇的吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0101F嗯……\x01",
            "地图上也没有任何标注呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#0203F总之，声音\x01",
            "并不是从这边传来的。\x02\x03",

            "#0200F还是原路回去为好吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0003F明白了……原路返回吧。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x64, 7)
    EventEnd(0x5)
    NewScene("r2050", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_9_109E end

    def Function_10_121F(): pass

    label("Function_10_121F")

    EventBegin(0x0)
    OP_E0(0x1)
    Fade(1000)
    OP_11(0x28, 0x32, 0x1E, 0x37, 0x64, 0x0)
    OP_68(-62530, 30850, 175200, 0)
    MoveCamera(31, -2, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(81900, 0)
    BeginChrThread(0x8, 1, 0, 11)
    OP_68(-83430, 30850, 189890, 12000)
    SetChrPos(0x101, -96040, 19750, 173960, 45)
    SetChrPos(0x102, -96170, 19750, 171980, 45)
    SetChrPos(0x103, -98380, 19750, 173760, 45)
    SetChrPos(0x104, -97620, 19750, 170810, 45)
    SetChrPos(0x109, -99220, 19750, 171180, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    def lambda_12E1():
        OP_95(0xFE, -88160, 19750, 181910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_12E1)

    def lambda_12FB():
        OP_95(0xFE, -87720, 19750, 179610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_12FB)

    def lambda_1315():
        OP_95(0xFE, -89820, 19750, 181730, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1315)

    def lambda_132F():
        OP_95(0xFE, -89380, 19750, 178450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_132F)

    def lambda_1349():
        OP_95(0xFE, -90830, 19750, 178970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1349)
    PlaceName2(340, 40, "c_plac29", 0x0, 6000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-88220, 22750, 181360, 0)
    MoveCamera(12, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21720, 0)
    OP_68(-88220, 20750, 181360, 3000)
    OP_6F(0x1)
    OP_0D()
    EndChrThread(0x8, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_1453")

    #C0019
    ChrTalk(
        0x101,
        (
            "#0006F#5P呼，终于到了。\x02\x03",

            "#0005F和以前来的时候相比，\x01",
            "感觉好像变得很昏暗呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#0108F#6P嗯……之前来的时候，\x01",
            "并没有这些雾气的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_14D1")

    label("loc_1453")


    #C0021
    ChrTalk(
        0x101,
        (
            "#0005F#5P这个……\x01",
            "好像是中世纪的遗迹呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0106F#6P山道的尽头竟然\x01",
            "有这种东西……\x02\x03",

            "#0108F……好像有一股寒冷的雾气……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_14D1")


    #C0023
    ChrTalk(
        0x104,
        (
            "#0301F#6P那么，就是这个遗迹里\x01",
            "有幽灵出没吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x109,
        (
            "#0506F#6P嗯……与其说是幽灵，\x01",
            "倒不如说是不明根底的魔兽。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x103, 500)
    Sleep(300)

    #C0025
    ChrTalk(
        0x109,
        "#0501F#6P缇欧……你有没有感觉到什么？\x02",
    )

    CloseMessageWindow()

    def lambda_157B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_157B)
    Sleep(50)

    def lambda_158B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_158B)
    Sleep(50)

    def lambda_159B():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_159B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x104, 1)

    #C0026
    ChrTalk(
        0x103,
        "#0205F#5P……………………………………\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x103)

    #C0027
    ChrTalk(
        0x103,
        (
            "#0203F#5P……我感觉到了，\x01",
            "似乎有种不可思议的波动。\x02\x03",

            "#0208F只是空气震动吗……？\x01",
            "……还是灵气的波动……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x109,
        "#0505F#6P不可思议的波动……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_16F9")

    #C0029
    ChrTalk(
        0x103,
        (
            "#0206F#5P嗯，之前来的时候\x01",
            "并没有感觉到……\x02\x03",

            "#0201F看起来，这种波动似乎是从\x01",
            "顶上那口钟的附近传来的。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1733")

    label("loc_16F9")


    #C0030
    ChrTalk(
        0x103,
        (
            "#0201F#5P嗯……波动似乎是从顶上的\x01",
            "那口钟附近传来的。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1733")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1783():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1783)
    Sleep(50)

    def lambda_1793():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1793)
    Sleep(50)

    def lambda_17A3():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_17A3)
    Sleep(50)

    def lambda_17B3():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17B3)
    Sleep(300)
    Fade(1000)
    Sound(866, 0, 100, 0)
    OP_68(-65349, 29450, 204690, 0)
    OP_68(-65349, 33950, 204690, 4000)
    MoveCamera(45, -8, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(57870, 0)
    OP_0D()
    OP_6F(0x79)

    #C0031
    ChrTalk(
        0x102,
        (
            "#0105F#11P如此说来……\x02\x03",

            "#0101F这个遗迹好像也和星见之塔一样，\x01",
            "在顶部建有钟楼呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0013F#5P嗯，看来是呢。\x02\x03",

            "而且它们好像和克洛斯贝尔中央广场\x01",
            "的那口大钟很相似……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0301F#11P唔……\x01",
            "彼此之间莫非有什么关系吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        "#0501F#5P…………………………………\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_6F(0x79)
    Fade(1000)
    OP_68(-88220, 20750, 181360, 0)
    MoveCamera(12, 16, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(21720, 0)
    OP_0D()
    OP_63(0x109, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_64(0x109)

    #C0035
    ChrTalk(
        0x109,
        (
            "#0503F#6P虽然这次行动的目的是\x01",
            "探索建筑的内部……\x02\x03",

            "#0501F不过，我们就将那个钟楼作为目标地点，\x01",
            "上去看一看如何？\x02\x03",

            "我也想确认一下\x01",
            "缇欧所说的那个波动。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_19FC():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_19FC)
    Sleep(50)

    def lambda_1A0C():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1A0C)
    Sleep(50)

    def lambda_1A1C():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1A1C)
    Sleep(50)

    def lambda_1A2C():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1A2C)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0036
    ChrTalk(
        0x101,
        (
            "#0004F#11P嗯，没有异议。\x02\x03",

            "#0000F那么……\x01",
            "就赶快进去吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#0106F#11P唉……明白了。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#0202F#5P明白。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#0304F#12P那么，就去跟幽灵\x01",
            "见个面吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0040
    ChrTalk(
        0x102,
        (
            "#0112F#11P都、都说过那不是幽灵，\x01",
            "而是不明根底的魔兽啦！\x02\x03",

            "#0109F对、对吧？诺艾尔上士！？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1BB9():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1BB9)
    Sleep(50)

    def lambda_1BC9():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BC9)
    Sleep(50)

    def lambda_1BD9():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BD9)
    Sleep(50)

    def lambda_1BE9():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BE9)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0041
    ChrTalk(
        0x109,
        "#0509F#6P嗯，是、是啊……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0012F#5P（既然那么害怕的话，\x01",
            "  就不要勉强过来啊……）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, -95800, 19750, 175000, 45)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xC0, 3)
    OP_29(0x49, 0x1, 0x1)
    OP_11(0x28, 0x32, 0x1E, 0x1E, 0xC8, 0x0)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_10_121F end

    def Function_11_1CAA(): pass

    label("Function_11_1CAA")

    Sound(866, 0, 100, 0)
    Sleep(3500)
    Sound(933, 0, 100, 0)
    Return()

    # Function_11_1CAA end

    def Function_12_1CBA(): pass

    label("Function_12_1CBA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(-62740, 30450, 191600, 0)
    MoveCamera(31, -2, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(81900, 0)
    SetChrPos(0x101, -77900, 19750, 191710, 225)
    SetChrPos(0x102, -76730, 19750, 191680, 225)
    SetChrPos(0x103, -76660, 19750, 195030, 225)
    SetChrPos(0x104, -75280, 19750, 194580, 225)
    SetChrPos(0x109, -78160, 19750, 193870, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    FadeToBright(1000, 0)
    OP_68(-76410, 30450, 204910, 11000)
    OP_6F(0x1)
    OP_0D()
    Fade(1000)
    OP_68(-83880, 25000, 186180, 0)
    MoveCamera(15, 21, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(34120, 0)
    OP_68(-83880, 22850, 186180, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(750)
    OP_82(0x64, 0x64, 0x1388, 0x708)
    OP_74(0x1, 0x6)
    Sound(938, 0, 100, 0)
    ClearMapObjFlags(0x1, 0x10)
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    OP_79(0x1)
    OP_74(0x1, 0x1E)
    Sleep(1000)
    BeginChrThread(0x101, 3, 0, 13)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 13)
    Sleep(50)
    BeginChrThread(0x109, 3, 0, 13)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 13)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 13)
    Sleep(4500)
    Fade(500)
    OP_68(-87810, 21250, 182120, 0)
    MoveCamera(12, 12, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(20120, 0)
    SetCameraDistance(17380, 3000)
    OP_6F(0x10)
    OP_0D()
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x109, 3)

    #C0043
    ChrTalk(
        0x102,
        (
            "#0106F#11P呼……\x01",
            "总算活着出来了。\x02\x03",

            "#0102F说实话，真是感觉差点就要死掉了呢。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    TurnDirection(0x103, 0x102, 500)

    #C0044
    ChrTalk(
        0x109,
        (
            "#0509F#5P呵呵，辛苦了。\x02\x03",

            "#0506F话说回来……\x01",
            "那口钟究竟是什么东西呢？\x02\x03",

            "#0501F还有那些怪物们，到底是……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1F7A():
        TurnDirection(0xFE, 0x109, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1F7A)
    TurnDirection(0x102, 0x109, 500)
    WaitChrThread(0x101, 1)

    #C0045
    ChrTalk(
        0x101,
        (
            "#0003F#6P『塔』虽然也是个不可思议的地方，\x01",
            "但这座『僧院』实在是有过之而无不及啊。\x02\x03",

            "#0001F另外，礼拜堂后面的\x01",
            "那个诡异的『仪式堂』……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0106F#12P嗯……\x01",
            "老实说，作为教会的遗迹，\x01",
            "感觉未免也太不祥了。\x02\x03",

            "#0108F五百年前……\x01",
            "究竟发生过什么呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x103,
        "#0208F#5P…………………………………\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x104,
        (
            "#0304F#11P算啦，那些就交给历史专家去研究，\x01",
            "我们还是快点回去吧。\x02\x03",

            "#0300F感觉真像是在主题公园\x01",
            "连续逛了十次鬼屋一样啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2196")

    #C0049
    ChrTalk(
        0x109,
        (
            "#0509F#5P呵呵，是呀。\x02\x03",

            "#0502F那么，我们就先回\x01",
            "停车的地方吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0002F#6P嗯，就这么办。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2234")

    label("loc_2196")


    #C0051
    ChrTalk(
        0x109,
        (
            "#0509F#5P呵呵，是呀。\x02\x03",

            "#0505F说起来……\x01",
            "车子好像停在别的地方了呢。\x02\x03",

            "#0502F我来联络部队，\x01",
            "让他们帮忙把车开到隧道途中吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#0002F#6P嗯，那就帮大忙啦。\x02",
    )

    CloseMessageWindow()

    label("loc_2234")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D0(0x1, (scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x1, 0x0, 0x0, 0x0, 0x0)
    OP_79(0x1)
    SetMapObjFlags(0x1, 0x10)
    OP_68(-95800, 21250, 175000, 0)
    MoveCamera(10, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(27000, 0)
    SetChrPos(0x0, -95800, 19750, 175000, 225)
    SetChrPos(0x1, -95800, 19750, 175000, 225)
    SetChrPos(0x2, -95800, 19750, 175000, 225)
    SetChrPos(0x3, -95800, 19750, 175000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC0, 7)
    OP_29(0x49, 0x1, 0x5)
    OP_E0(0x0)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_12_1CBA end

    def Function_13_22EA(): pass

    label("Function_13_22EA")


    def lambda_22EF():
        OP_97(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_22EF)

    def lambda_2309():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_2309)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_22EA end

    def Function_14_231E(): pass

    label("Function_14_231E")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_68(-131760, 25590, 131440, 0)
    MoveCamera(43, -2, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(26840, 0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0xF, 0x80)
    LoadChrToIndex("apl/ch50387.itc", 0x32)
    LoadEffect(0x0, "event\\eva02_00.eff")
    SetChrPos(0x101, -133660, 20000, 121680, 0)
    SetChrPos(0x102, -133200, 20000, 123580, 0)
    SetChrPos(0x103, -134930, 20000, 123500, 0)
    SetChrPos(0x104, -135130, 20000, 125140, 0)
    OP_68(-131760, 20990, 131440, 4000)
    MoveCamera(46, 6, 0, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0053
    ChrTalk(
        0x103,
        (
            "#6P#0205F那栋建筑物……到底是什么呢？\x01",
            "好像是很古老的遗迹……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#12P#0100F我想，应该是中世纪建造的\x01",
            "寺院遗迹吧。\x02\x03",

            "#0103F虽然不知道详情……\x01",
            "但现在好像有警备队\x01",
            "设置的防护栏。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        "#6P#0300F和『星见之塔』一样啊。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#12P#0000F现在似乎不需要进去……\x01",
            "不过这里风景好像挺特别的。\x02\x03",

            "格蕾丝小姐委托我们拍摄的照片，\x01",
            "在这里似乎能拍到很不错的呢。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2AD1")
    TurnDirection(0x101, 0x102, 500)

    #C0057
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么艾莉，\x01",
            "可以拜托你来拍照吗？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0058
    ChrTalk(
        0x102,
        (
            "#12P#0108F哎，好的。\x01",
            "虽然我没什么自信……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0059
    ChrTalk(
        0x104,
        (
            "#6P#0300F哪里哪里，应该没问题吧。\x02\x03",

            "只要看看镜头，\x01",
            "然后咔嚓一下拍下来\x01",
            "不就搞定了嘛。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0060
    ChrTalk(
        0x102,
        (
            "#12P#0103F我说你啊……\x01",
            "要拍出好照片，\x01",
            "可没有那么简单哦。\x02\x03",

            "#0100F要注意确认\x01",
            "拍摄对象有没有被收入取景框中，\x01",
            "还要构思摄影角度……\x02\x03",

            "而且受到天气和风的影响，\x01",
            "照片所呈现出的感觉也会有很大不同。\x02\x03",

            "有时只要错过那一瞬的时机，\x01",
            "就再也拍不到\x01",
            "那么好的风景了。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#6P#0200F外行和专家所拍出的照片，\x01",
            "差别可是一目了然的。\x02\x03",

            "#0203F不过，某些粗神经的人\x01",
            "大概无法理解这种细致的工作吧。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0062
    ChrTalk(
        0x104,
        (
            "#6P#0306F唔……\x01",
            "你在说谁啊，说谁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0000F好啦好啦，\x01",
            "总之就交给艾莉吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#12P#0100F那么……\x01",
            "我来试试看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x0, 0x1F4)
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0x103, 0x0, 0x1F4)
    OP_93(0x104, 0x0, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0065
    ChrTalk(
        0x102,
        (
            "#12P#0103F……呼，\x01",
            "为了保险起见，我多拍了几张。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#12P#0000F看样子，似乎已经拍好了呢。\x02\x03",

            "感觉怎么样啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#12P#0100F在没有实际显像出来之前，\x01",
            "还无法确定……\x02\x03",

            "不过，我觉得至少\x01",
            "不会很差吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#6P#0200F艾莉前辈似乎\x01",
            "找回感觉了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#6P#0300F哼……\x01",
            "反正只有我完全搞不懂。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#12P#0000F如果发现了这种风景漂亮的地方，\x01",
            "就再拍些照片吧。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE0")

    label("loc_2AD1")

    TurnDirection(0x101, 0x102, 500)

    #C0071
    ChrTalk(
        0x101,
        (
            "#12P#0000F那么……\x01",
            "艾莉，麻烦你拍照了哦。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        "#12P#0100F嗯，知道了。\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_93(0x102, 0x0, 0x1F4)
    OP_93(0x101, 0x0, 0x1F4)
    OP_93(0x103, 0x0, 0x1F4)
    OP_93(0x104, 0x0, 0x1F4)
    Fade(1000)
    SetChrChipByIndex(0x102, 0x32)
    SetChrSubChip(0x102, 0x0)
    OP_0D()
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Sound(817, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0x102, 0xC0, 0, 1200, 400, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    #C0073
    ChrTalk(
        0x102,
        (
            "#12P#0103F……呼，\x01",
            "大概就这样吧。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2C56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C56")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2C6D")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2C84")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C84")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2C9B")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2C9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2CB2")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CB2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2CC9")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CC9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2CE0")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CE0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2CF7")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2CF7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2D0E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2D0E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D9F")

    #C0074
    ChrTalk(
        0x101,
        (
            "#12P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "这样一来，就拍完了格蕾丝小姐\x01",
            "所要求的五张照片了。\x01",
            "现在随时都可以去交付了啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE0")

    label("loc_2D9F")


    #C0075
    ChrTalk(
        0x101,
        (
            "#12P#0000F辛苦了，\x01",
            "看来已经顺利拍好了啊。\x02\x03",

            "那么，我们走吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE0")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-132900, 23500, 122090, 0)
    MoveCamera(45, 0, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(25000, 0)
    OP_69(0x1, 0x0)
    SetChrPos(0x0, -132900, 20000, 122090, 45)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    OP_D5(0x32)
    OP_29(0x18, 0x1, 0x9)
    Sleep(500)
    ClearMapFlags(0x8000000)
    OP_37()
    OP_65(0x6, 0x1)
    EventEnd(0x5)
    Return()

    # Function_14_231E end

    def Function_15_2E4E(): pass

    label("Function_15_2E4E")

    EventBegin(0x0)
    Fade(500)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    SetChrFlags(0xC, 0x80)
    OP_68(-107910, 2600, 29060, 0)
    MoveCamera(60, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18900, 0)
    SetChrPos(0x101, -110330, 2000, 28710, 90)
    SetChrPos(0x102, -110100, 2000, 30100, 135)
    SetChrPos(0x103, -109030, 2000, 26830, 0)
    SetChrPos(0x104, -107190, 2000, 26870, 315)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2EFE")
    SetChrPos(0x10A, -111890, 2000, 29150, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2EFE")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, '优雅衣镜'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber('优雅衣镜', 1)

    #C0077
    ChrTalk(
        0x101,
        (
            "#6P#0000F蓝色的花……\x01",
            "这就是利奎姆之花吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        "#12P#0206F……真是大费周章呢。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#11P#0306F……是啊。\x01",
            "要是连这里也没有花的话，\x01",
            "可就真是要白跑一趟了。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#5P#0100F好啦好啦。\x01",
            "反正已经摘到了花，\x01",
            "这不是很好嘛。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_306C")

    #C0081
    ChrTalk(
        0x10A,
        "#6P#0603F（哪里好了，真是的，浪费那么多时间……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_309B")

    label("loc_306C")


    #C0082
    ChrTalk(
        0x101,
        (
            "#0000F嗯，说得对。\x01",
            "……差不多也该走了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_309B")

    OP_65(0x7, 0x1)
    OP_29(0x2E, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_30C8")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_30C8")

    ClearMapFlags(0x8000000)
    OP_37()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30E8")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_30E8")

    SetChrPos(0x0, -110330, 2000, 28710, 90)
    EventEnd(0x5)
    Return()

    # Function_15_2E4E end

    SaveToFile()

Try(main)
