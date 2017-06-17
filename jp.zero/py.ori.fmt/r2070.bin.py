from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "SE制御",                 # 1
        "br2070",                 # 2
        "br2070",                 # 3
        "マインツ山道方面",       # 4
    ))

    ATBonus("ATBonus_3E4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3476", 12,  0,   9,   1,   7,   3,   6)
    Sepith("Sepith_347E", 0,   7,   3,   12,  6,   7,   1)

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
        "BattleInfo_4C4", 0x0000, 23, 6, 60, 6, 1, 25, 0, "br2070", "Sepith_3476", 30, 40, 20, 10,
        (
            ("ms76100.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms76100.dat", "ms76100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_444", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
            ("ms76100.dat", "ms76100.dat", "ms66300.dat", "ms76100.dat", 0, 0, 0, 0, "MonsterBattlePostion_424", "MonsterBattlePostion_4A4", "ed7400", "ed7403", "ATBonus_3E4"),
        )
    )

    BattleInfo(
        "BattleInfo_58C", 0x0000, 23, 6, 60, 6, 1, 40, 0, "br2070", "Sepith_347E", 30, 45, 20, 5,
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

    PlaceName(16.25, 0.0, 5.0, 0x0000, 0x0000, "マインツ山道方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_6C4",          # 00, 0
        "Function_1_6E5",          # 01, 1
        "Function_2_B89",          # 02, 2
        "Function_3_CD6",          # 03, 3
        "Function_4_E23",          # 04, 4
        "Function_5_F70",          # 05, 5
        "Function_6_10BD",         # 06, 6
        "Function_7_10D1",         # 07, 7
        "Function_8_10FD",         # 08, 8
        "Function_9_1106",         # 09, 9
        "Function_10_12AF",        # 0A, 10
        "Function_11_1E0E",        # 0B, 11
        "Function_12_1E1E",        # 0C, 12
        "Function_13_24D8",        # 0D, 13
        "Function_14_250C",        # 0E, 14
        "Function_15_3158",        # 0F, 15
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C85")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E3, 1)"), scpexpr(EXPR_END)), "loc_C0E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_C80")

    label("loc_C0E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E3),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C80")

    Jump("loc_CCA")

    label("loc_C85")

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

    label("loc_CCA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_B89 end

    def Function_3_CD6(): pass

    label("Function_3_CD6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DD2")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_D5B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x105, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_DCD")

    label("loc_D5B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_DCD")

    Jump("loc_E17")

    label("loc_DD2")

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

    label("loc_E17")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_CD6 end

    def Function_4_E23(): pass

    label("Function_4_E23")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F1F")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x81, 1)"), scpexpr(EXPR_END)), "loc_EA8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x105, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_F1A")

    label("loc_EA8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x81),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F1A")

    Jump("loc_F64")

    label("loc_F1F")

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

    label("loc_F64")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_E23 end

    def Function_5_F70(): pass

    label("Function_5_F70")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x105, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_106C")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_FF5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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
    SetScenarioFlags(0x105, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_1067")

    label("loc_FF5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0011
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
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1067")

    Jump("loc_10B1")

    label("loc_106C")

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

    label("loc_10B1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_F70 end

    def Function_6_10BD(): pass

    label("Function_6_10BD")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7B, 4)
    OP_65(0x5, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_6_10BD end

    def Function_7_10D1(): pass

    label("Function_7_10D1")

    TalkBegin(0xFF)
    SetChrName("")

    #A0013
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
    TalkEnd(0xFF)
    Return()

    # Function_7_10D1 end

    def Function_8_10FD(): pass

    label("Function_8_10FD")

    SetScenarioFlags(0x87, 7)
    ModifyEventFlags(0, 1, 0x80)
    Return()

    # Function_8_10FD end

    def Function_9_1106(): pass

    label("Function_9_1106")

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
        "#0005Fこっちの方は……\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        (
            "#0301F何か抜け道っぽいが\x01",
            "鉱山町方面じゃねえよな？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#0101Fええ……\x01",
            "地図にも何もないわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x103,
        (
            "#0203Fとりあえず、聞こえてきたのは\x01",
            "こっちの方ではないです。\x02\x03",

            "#0200F引き返した方がいいのでは？\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#0003F分かった……そうするか。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetScenarioFlags(0x64, 7)
    EventEnd(0x5)
    NewScene("r2050", 102, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1106 end

    def Function_10_12AF(): pass

    label("Function_10_12AF")

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

    def lambda_1371():
        OP_95(0xFE, -88160, 19750, 181910, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1371)

    def lambda_138B():
        OP_95(0xFE, -87720, 19750, 179610, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_138B)

    def lambda_13A5():
        OP_95(0xFE, -89820, 19750, 181730, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_13A5)

    def lambda_13BF():
        OP_95(0xFE, -89380, 19750, 178450, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_13BF)

    def lambda_13D9():
        OP_95(0xFE, -90830, 19750, 178970, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_13D9)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_1501")

    #C0019
    ChrTalk(
        0x101,
        (
            "#0006F#5Pふう、やっと着いたか。\x02\x03",

            "#0005Fしかし、前に来た時に比べると\x01",
            "やたらと薄暗い感じだな……\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        (
            "#0108F#6Pええ……前に来た時は\x01",
            "こんなモヤは出てなかったのに。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1591")

    label("loc_1501")


    #C0021
    ChrTalk(
        0x101,
        (
            "#0005F#5Pこれは……\x01",
            "中世の遺跡みたいだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        (
            "#0106F#6Pこんなものが\x01",
            "山道の外れにあったなんて……\x02\x03",

            "#0108F……何だかモヤが出て肌寒いし……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1591")


    #C0023
    ChrTalk(
        0x104,
        (
            "#0301F#6Pで、この遺跡の中に\x01",
            "幽霊が出るってわけだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x109,
        (
            "#0506F#6Pええ……幽霊というか\x01",
            "得体の知れない魔獣ですけど。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x103, 500)
    Sleep(300)

    #C0025
    ChrTalk(
        0x109,
        "#0501F#6Pティオちゃん……何か感じる？\x02",
    )

    CloseMessageWindow()

    def lambda_1645():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1645)
    Sleep(50)

    def lambda_1655():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1655)
    Sleep(50)

    def lambda_1665():
        TurnDirection(0xFE, 0x103, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1665)
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
            "#0203F#5P……何か不思議な\x01",
            "波動のようなものを感じます。\x02\x03",

            "#0208Fただの空気振動……？\x01",
            "……それとも霊的なもの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x109,
        "#0505F#6P不思議な波動……？\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x87, 7)), scpexpr(EXPR_END)), "loc_17DB")

    #C0029
    ChrTalk(
        0x103,
        (
            "#0206F#5Pええ、前に来た時には\x01",
            "感じなかったんですけど……\x02\x03",

            "#0201Fどうやら屋上に見えている\x01",
            "鐘のあたりから感じられます。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_181F")

    label("loc_17DB")


    #C0030
    ChrTalk(
        0x103,
        (
            "#0201F#5Pええ……屋上に見えている\x01",
            "鐘のあたりから感じられます。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_181F")

    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_186F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_186F)
    Sleep(50)

    def lambda_187F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_187F)
    Sleep(50)

    def lambda_188F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_188F)
    Sleep(50)

    def lambda_189F():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_189F)
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
            "#0105F#11Pそういえば……\x02\x03",

            "#0101Fこの遺跡も、星見の塔みたいに\x01",
            "屋上に鐘楼があるみたいね……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#0013F#5Pああ、そうみたいだな。\x02\x03",

            "クロスベルの中央広場にあるのと\x01",
            "同じような鐘みたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x104,
        (
            "#0301F#11Pふむ……\x01",
            "なんか関係あんのかねぇ。\x02",
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
            "#0503F#6P今回は、一通り内部を\x01",
            "探索するのが目的ですが……\x02\x03",

            "#0501Fとりあえずの目標地点として\x01",
            "あの鐘楼まで行ってみませんか？\x02\x03",

            "ティオちゃんの言ってたことも\x01",
            "確認してみたいですし。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1B1A():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1B1A)
    Sleep(50)

    def lambda_1B2A():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1B2A)
    Sleep(50)

    def lambda_1B3A():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1B3A)
    Sleep(50)

    def lambda_1B4A():
        TurnDirection(0xFE, 0x109, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1B4A)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0036
    ChrTalk(
        0x101,
        (
            "#0004F#11Pああ、異存はないよ。\x02\x03",

            "#0000Fそれじゃあ……\x01",
            "さっそく中に入るとしようか。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#0106F#11Pふう……分かったわ。\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x103,
        "#0202F#5P了解です。\x02",
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x104,
        (
            "#0304F#12Pそんじゃま、幽霊ってのに\x01",
            "ご対面といきますかね。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x102, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    #C0040
    ChrTalk(
        0x102,
        (
            "#0112F#11Pだ、だから幽霊じゃなくて\x01",
            "得体の知れない魔獣だってば！\x02\x03",

            "#0109Fね、ねえノエルさん！？\x02",
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

    def lambda_1D15():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1D15)
    Sleep(50)

    def lambda_1D25():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1D25)
    Sleep(50)

    def lambda_1D35():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1D35)
    Sleep(50)

    def lambda_1D45():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1D45)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)

    #C0041
    ChrTalk(
        0x109,
        "#0509F#6Pえ、ええまあ……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x101,
        (
            "#0012F#5P（そんなに怖いんだったら\x01",
            "  無理しなきゃいいのに……）\x02",
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

    # Function_10_12AF end

    def Function_11_1E0E(): pass

    label("Function_11_1E0E")

    Sound(866, 0, 100, 0)
    Sleep(3500)
    Sound(933, 0, 100, 0)
    Return()

    # Function_11_1E0E end

    def Function_12_1E1E(): pass

    label("Function_12_1E1E")

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
            "#0106F#11Pはあ……\x01",
            "ちゃんと出られたわね。\x02\x03",

            "#0102F正直、生きた心地がしなかったわ。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x102, 500)
    TurnDirection(0x103, 0x102, 500)

    #C0044
    ChrTalk(
        0x109,
        (
            "#0509F#5Pふふ、お疲れさまでした。\x02\x03",

            "#0506Fそれにしても……\x01",
            "あの鐘、一体何なんでしょうね。\x02\x03",

            "#0501Fそれにあの化物たちも一体……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_20FA():
        TurnDirection(0xFE, 0x109, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20FA)
    TurnDirection(0x102, 0x109, 500)
    WaitChrThread(0x101, 1)

    #C0045
    ChrTalk(
        0x101,
        (
            "#0003F#6P《塔》も不思議な場所だったけど\x01",
            "この《僧院》はそれ以上だったな。\x02\x03",

            "#0001Fそれと礼拝堂の裏にあった\x01",
            "あの不気味な《儀式の間》か……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0106F#12Pええ……\x01",
            "正直、教会の遺跡にしては\x01",
            "あまりにも禍々しすぎると思う。\x02\x03",

            "#0108F５００年前……\x01",
            "一体、何があったのかしら？\x02",
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
            "#0304F#11Pま、そのあたりは専門家に任せて\x01",
            "俺たちはとっとと帰ろうぜ。\x02\x03",

            "#0300Fテーマパークにあるホラーハウスを\x01",
            "１０回くらいハシゴした気分だぜ。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_23, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2366")

    #C0049
    ChrTalk(
        0x109,
        (
            "#0509F#5Pふふ、そうですね。\x02\x03",

            "#0502Fそれじゃあ停車している\x01",
            "車両の所まで戻りましょうか？\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        "#0002F#6Pああ、そうしよう。\x02",
    )

    CloseMessageWindow()
    Jump("loc_2422")

    label("loc_2366")


    #C0051
    ChrTalk(
        0x109,
        (
            "#0509F#5Pふふ、そうですね。\x02\x03",

            "#0505Fそういえば……\x01",
            "車、別の場所に停めてましたね。\x02\x03",

            "#0502F部隊に連絡して、トンネルの\x01",
            "途中まで届けてもらいましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0x101,
        "#0002F#6Pああ、それは助かるな。\x02",
    )

    CloseMessageWindow()

    label("loc_2422")

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

    # Function_12_1E1E end

    def Function_13_24D8(): pass

    label("Function_13_24D8")


    def lambda_24DD():
        OP_97(0xFE, 0xFFFFD8F0, 0x0, 0xFFFFD8F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_24DD)

    def lambda_24F7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x7D0)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_24F7)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)
    Return()

    # Function_13_24D8 end

    def Function_14_250C(): pass

    label("Function_14_250C")

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
            "#6P#0205Fあの建物……何なんでしょう。\x01",
            "随分古い遺跡のようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x102,
        (
            "#12P#0100F中世に建てられたらしい\x01",
            "寺院の遺跡だったと思うわ。\x02\x03",

            "#0103F詳しくは知らないけど……\x01",
            "今は警備隊によって\x01",
            "バリケードが張られてるみたい。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x104,
        "#6P#0300F《星見の塔》と一緒だな。\x02",
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0x101,
        (
            "#12P#0000F今のところ用はなさそうだけど……\x01",
            "眺める分には珍しくてよさそうだ。\x02\x03",

            "グレイスさんに依頼された写真、\x01",
            "ここならいいものが撮れそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D99")
    TurnDirection(0x101, 0x102, 500)

    #C0057
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれじゃあエリィ、\x01",
            "撮影をお願いできるかな。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 500)

    #C0058
    ChrTalk(
        0x102,
        (
            "#12P#0108Fえ、ええ。\x01",
            "ちょっと自信はないけど……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x102, 500)

    #C0059
    ChrTalk(
        0x104,
        (
            "#6P#0300Fいやいや、大丈夫だろ。\x02\x03",

            "ちょっとレンズを覗いて\x01",
            "パチリと撮っちまえば\x01",
            "終わりじゃねぇか。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x104, 500)

    #C0060
    ChrTalk(
        0x102,
        (
            "#12P#0103Fあのねぇ……\x01",
            "いい写真を撮るのは\x01",
            "そんな簡単なことじゃないのよ。\x02\x03",

            "#0100Fフレームの中に\x01",
            "対象物をどう収めるか、\x01",
            "構成を練らなきゃいけないし……\x02\x03",

            "天気や風の影響で\x01",
            "写真の印象もガラリと変わってしまう。\x02\x03",

            "ある一瞬を逃したら\x01",
            "二度と撮れないことだって\x01",
            "あるんだから。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#6P#0200F素人とプロの写真を見比べると\x01",
            "一目で違いが分かりますからね。\x02\x03",

            "#0203F粗雑な人には、その繊細さが\x01",
            "理解できないかも知れませんが。\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0062
    ChrTalk(
        0x104,
        (
            "#6P#0306Fぐっ……\x01",
            "誰のことを言ってんだ、誰の。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0x101,
        (
            "#12P#0000Fま、まぁまぁ。\x01",
            "ここはエリィに任せてみよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x102,
        (
            "#12P#0100Fそれじゃあ……\x01",
            "やってみるわね。\x02",
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
            "#12P#0103F……ふぅ。\x01",
            "念のため何枚か撮っておいたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x101,
        (
            "#12P#0000Fどうやら撮れたみたいだな。\x02\x03",

            "出来栄えはどんな感じだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#12P#0100F実際に現像してみないと\x01",
            "分からないけど……\x02\x03",

            "少なくとも、\x01",
            "悪い写真ではないとは思うわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x103,
        (
            "#6P#0200Fエリィさんも\x01",
            "カンを取り戻せたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x104,
        (
            "#6P#0300Fふーん……\x01",
            "俺にはさっぱりだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        (
            "#12P#0000Fまたこういう場所を見つけたら\x01",
            "写真に収めていこう。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30EA")

    label("loc_2D99")

    TurnDirection(0x101, 0x102, 500)

    #C0071
    ChrTalk(
        0x101,
        (
            "#12P#0000Fそれじゃあ……\x01",
            "エリィ、撮影を頼むよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0072
    ChrTalk(
        0x102,
        "#12P#0100Fええ、分かったわ。\x02",
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
            "#12P#0103F……ふぅ。\x01",
            "こんなところかしら。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x2)"), scpexpr(EXPR_END)), "loc_2F32")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F32")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x3)"), scpexpr(EXPR_END)), "loc_2F49")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x4)"), scpexpr(EXPR_END)), "loc_2F60")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F60")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x5)"), scpexpr(EXPR_END)), "loc_2F77")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F77")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x6)"), scpexpr(EXPR_END)), "loc_2F8E")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2F8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x7)"), scpexpr(EXPR_END)), "loc_2FA5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x8)"), scpexpr(EXPR_END)), "loc_2FBC")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0x9)"), scpexpr(EXPR_END)), "loc_2FD3")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x18, 0x1, 0xA)"), scpexpr(EXPR_END)), "loc_2FEA")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    label("loc_2FEA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3095")

    #C0074
    ChrTalk(
        0x101,
        (
            "#12P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "これでグレイスさんに提示された\x01",
            "５枚ってノルマは達成できた。\x01",
            "これでいつでも提出できそうだな。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_30EA")

    label("loc_3095")


    #C0075
    ChrTalk(
        0x101,
        (
            "#12P#0000Fご苦労さん。\x01",
            "無事に撮影出来たみたいだな。\x02\x03",

            "それじゃ、行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_30EA")

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

    # Function_14_250C end

    def Function_15_3158(): pass

    label("Function_15_3158")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3208")
    SetChrPos(0x10A, -111890, 2000, 29150, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_3208")

    OP_0D()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x34A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x34A, 1)

    #C0077
    ChrTalk(
        0x101,
        (
            "#6P#0000F青い花……\x01",
            "これがリクエムの花だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x103,
        "#12P#0206F……とんだひと手間でしたね。\x02",
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x104,
        (
            "#11P#0306F……だな。\x01",
            "これでもし花が無かったら\x01",
            "完全に骨折り損だしよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x102,
        (
            "#5P#0100Fまぁまぁ。\x01",
            "花はあったんだし、\x01",
            "よかったじゃない。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3382")

    #C0081
    ChrTalk(
        0x10A,
        "#6P#0603F（いいワケないだろう、全く……）\x02",
    )

    CloseMessageWindow()
    Jump("loc_33BD")

    label("loc_3382")


    #C0082
    ChrTalk(
        0x101,
        (
            "#0000Fああ、その通りだ。\x01",
            "……そろそろ行くとしようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_33BD")

    OP_65(0x7, 0x1)
    OP_29(0x2E, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x4)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x2E, 0x1, 0x5)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_33EA")
    OP_29(0x2E, 0x1, 0x6)

    label("loc_33EA")

    ClearMapFlags(0x8000000)
    OP_37()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_340A")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_340A")

    SetChrPos(0x0, -110330, 2000, 28710, 90)
    EventEnd(0x5)
    Return()

    # Function_15_3158 end

    SaveToFile()

Try(main)
