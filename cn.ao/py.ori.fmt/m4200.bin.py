from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4200.bin",                # FileName
        "m4200",                    # MapName
        "m4200",                    # Location
        0x007F,                     # MapIndex
        "ed7573",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x29,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 127, 0, 1, 0, 2],
    )

    BuildStringList((
        "m4200",                  # 0
        "诺艾尔",                 # 1
        "瓦吉",                   # 2
        "银",                     # 3
        "小船",                   # 4
        "SE控制",                 # 5
        "bm4200",                 # 6
        "bm4200",                 # 7
        "bm4200",                 # 8
    ))

    ATBonus("ATBonus_3C4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_3E3F", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_3E2F", 8,   8,   6,   6,   6,   8,   6)
    Sepith("Sepith_3E47", 4,   2,   10,  4,   8,   2,   10)

    MonsterBattlePostion("MonsterBattlePostion_414", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_418", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_420", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_424", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_428", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_42C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_430", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_478", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_47C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_480", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_484", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_488", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_48C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_490", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 2, 13, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_530", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_3E3F", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_3E2F", 50, 25, 25, 0,
        (
            ("ms78200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms78200.dat", "ms78200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms78200.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5CC", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_3E47", 40, 30, 20, 0,
        (
            ("ms86800.dat", "ms82700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_414", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_474", "ed7450", "ed7453", "ATBonus_3C4"),
            (),
        )
    )

    AddCharChip((
        "chr/ch02900.itc",                   # 00
        "chr/ch03000.itc",                   # 01
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
        "monster/ch78250.itc",               # 10
        "monster/ch78251.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "monster/ch83350.itc",               # 16
        "monster/ch83351.itc",               # 17
        "monster/ch86850.itc",               # 18
        "monster/ch86850.itc",               # 19
    ))

    DeclNpc(16000,   0,       31000,   225,  389,  0x0, 0,   0,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(16000,   0,       31000,   225,  389,  0x0, 0,   1,   0,   0,   0,   0,   9,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    196,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-20830,  12140,   -490,    0x1010087,    "BattleInfo_530", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(6310,    -31880,  0,       0x1010141,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-8250,   -44810,  0,       0x1010154,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-32820,  -46290,  0,       0x1010154,    "BattleInfo_530", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(21150,   -42670,  -500,    0x10100D1,    "BattleInfo_5CC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-23420,  -73150,  0,       0x1010065,    "BattleInfo_5CC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-7480,   -86230,  0,       0x101013B,    "BattleInfo_494", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-26130,  -98330,  -10,     0x1010098,    "BattleInfo_530", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(-11650,  -115380, -10,     0x101014C,    "BattleInfo_5CC", 0,   24,  0xFFFF, 4,  5)

    DeclActor(-22000,  -500,    19000,   1200,    -22000,  500,     19000,   0x007C, 0,  4,  0x0000)
    DeclActor(-7000,   0,       -48500,  1200,    -7000,   1000,    -48500,  0x007C, 0,  5,  0x0000)
    DeclActor(22000,   500,     -36000,  1200,    22000,   1500,    -36000,  0x007C, 0,  6,  0x0000)
    DeclActor(-27000,  0,       -94000,  1200,    -27000,  1000,    -94000,  0x007C, 0,  7,  0x0000)
    DeclActor(-6780,   0,       32820,   1200,    -6780,   2000,    32820,   0x007C, 0,  11, 0x0000)
    DeclActor(13100,   -500,    -7310,   1200,    14390,   -500,    -14360,  0x007C, 0,  10, 0x0000)
    DeclActor(5410,    0,       44030,   3200,    5410,    0,       44030,   0x007C, 0,  23, 0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_710",          # 00, 0
        "Function_1_7C0",          # 01, 1
        "Function_2_852",          # 02, 2
        "Function_3_104E",         # 03, 3
        "Function_4_1083",         # 04, 4
        "Function_5_11BE",         # 05, 5
        "Function_6_12F9",         # 06, 6
        "Function_7_1434",         # 07, 7
        "Function_8_158D",         # 08, 8
        "Function_9_17DA",         # 09, 9
        "Function_10_1A12",        # 0A, 10
        "Function_11_1ADA",        # 0B, 11
        "Function_12_1E07",        # 0C, 12
        "Function_13_1E1F",        # 0D, 13
        "Function_14_1E37",        # 0E, 14
        "Function_15_1E4F",        # 0F, 15
        "Function_16_1E67",        # 10, 16
        "Function_17_1E7F",        # 11, 17
        "Function_18_1ECA",        # 12, 18
        "Function_19_1F15",        # 13, 19
        "Function_20_1F78",        # 14, 20
        "Function_21_1FDB",        # 15, 21
        "Function_22_202F",        # 16, 22
        "Function_23_3D77",        # 17, 23
    ))


    def Function_0_710(): pass

    label("Function_0_710")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_748"),
        (1, "loc_754"),
        (2, "loc_760"),
        (3, "loc_76C"),
        (4, "loc_778"),
        (5, "loc_784"),
        (6, "loc_790"),
        (SWITCH_DEFAULT, "loc_79C"),
    )


    label("loc_748")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_754")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_760")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_76C")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_778")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_784")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_790")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_79C")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_7A8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7BF")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7A8")

    label("loc_7BF")

    Return()

    # Function_0_710 end

    def Function_1_7C0(): pass

    label("Function_1_7C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7D1")
    Call(0, 3)

    label("loc_7D1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_808")
    ClearScenarioFlags(0x22, 0)
    OP_78(0x5, 0xB)
    SetChrPos(0xB, 21000, -500, 29720, 225)
    OP_D5(0xB, 0x0, 0x36EE8, 0x0, 0x0)
    Event(0, 22)

    label("loc_808")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_81E")
    OP_50(0x1E, (scpexpr(EXPR_PUSH_LONG, 0x29), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_81E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_851")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_851")
    SetChrPos(0x0, -6780, 0, 32820, 180)
    OP_31(0x1)
    OP_69(0xFF, 0x0)
    ClearMapFlags(0x8000000)

    label("loc_851")

    Return()

    # Function_1_7C0 end

    def Function_2_852(): pass

    label("Function_2_852")

    SetMapObjFlags(0x4, 0x4)
    OP_65(0x6, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_86E")
    OP_66(0x6, 0x1)

    label("loc_86E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_889")
    SetMapObjFlags(0x5, 0x4)
    SetMapObjFlags(0x4, 0x4)
    SetMapObjFlags(0x6, 0x4)

    label("loc_889")

    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x15, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    LoadEffect(0xF, "eff\\mgm03_02.eff")
    PlayEffect(0xF, 0x8, 0xFF, 0x0, 14390, -500, -14360, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    MiniGame(0x2F, 0xFFFFFFFF, 0x4, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FFE")
    OP_70(0x0, 0x0)
    Jump("loc_1002")

    label("loc_FFE")

    OP_70(0x0, 0x1E)

    label("loc_1002")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1015")
    OP_70(0x1, 0x0)
    Jump("loc_1019")

    label("loc_1015")

    OP_70(0x1, 0x1E)

    label("loc_1019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102C")
    OP_70(0x2, 0x0)
    Jump("loc_1030")

    label("loc_102C")

    OP_70(0x2, 0x1E)

    label("loc_1030")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1043")
    OP_70(0x3, 0x0)
    Jump("loc_1047")

    label("loc_1043")

    OP_70(0x3, 0x1E)

    label("loc_1047")

    Sound(123, 1, 80, 0)
    Return()

    # Function_2_852 end

    def Function_3_104E(): pass

    label("Function_3_104E")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_106D")
    ClearChrFlags(0x8, 0x80)

    label("loc_106D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_1082")
    ClearChrFlags(0x9, 0x80)

    label("loc_1082")

    Return()

    # Function_3_104E end

    def Function_4_1083(): pass

    label("Function_4_1083")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1175")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1B9, 1)"), scpexpr(EXPR_END)), "loc_1106")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_1170")

    label("loc_1106")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1B9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1170")

    Jump("loc_11B2")

    label("loc_1175")

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

    label("loc_11B2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_1083 end

    def Function_5_11BE(): pass

    label("Function_5_11BE")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B0")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_1241")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_12AB")

    label("loc_1241")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12AB")

    Jump("loc_12ED")

    label("loc_12B0")

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

    label("loc_12ED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_11BE end

    def Function_6_12F9(): pass

    label("Function_6_12F9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13EB")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x64A, 1)"), scpexpr(EXPR_END)), "loc_137C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x64A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F2, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_13E6")

    label("loc_137C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x64A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x64A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_13E6")

    Jump("loc_1428")

    label("loc_13EB")

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

    label("loc_1428")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_12F9 end

    def Function_7_1434(): pass

    label("Function_7_1434")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155E")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×８０\x01\x07\x02",

            "#57I水之耀晶片×８０\x01\x07\x02",

            "#58I火之耀晶片×８０\x01\x07\x02",

            "#59I风之耀晶片×８０\x01\x07\x02",

            "#60I时之耀晶片×８０\x01\x07\x02",

            "#61I空之耀晶片×８０\x01\x07\x02",

            "#62I幻之耀晶片×８０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F2, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_157B")

    label("loc_155E")


    #A0011
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

    label("loc_157B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1434 end

    def Function_8_158D(): pass

    label("Function_8_158D")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_159A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D6")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "与瓦吉换班\x01",      # 1
            "放弃\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1665")

    #C0012
    ChrTalk(
        0x105,
        "#10300F接下来就拜托你啦。\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x8,
        "#10100F嗯！交给我吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0x4, 0xF9, 0x0)
    OP_32(0x8, 0xF9, 0x0)
    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x9, 0x80)
    RemoveParty(0x8, 0xFF)
    AddParty(0x8, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x8)
    OP_37()
    Call(0, 3)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_17D1")

    label("loc_1665")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1679")
    Jump("loc_17D1")

    label("loc_1679")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17D1")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_175C")

    #C0014
    ChrTalk(
        0x8,
        (
            "#10103F这里是约亚西姆·琼塔\x01",
            "当初采集『真知』\x01",
            "原料的地方……\x02\x03",

            "#10108F艾欧莉娅小姐她们在这种地方\x01",
            "究竟遇到了什么事呢……\x02\x03",

            "#10101F此地出现『幻兽』\x01",
            "的危险性恐怕很高。\x01",
            "大家千万要小心！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_17D1")

    label("loc_175C")


    #C0015
    ChrTalk(
        0x8,
        (
            "#10108F艾欧莉娅小姐她们\x01",
            "在这里究竟发生了什么事……\x02\x03",

            "#10101F此地出现『幻兽』\x01",
            "的危险性恐怕很高。\x01",
            "大家千万要小心！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_17D1")

    Jump("loc_159A")

    label("loc_17D6")

    TalkEnd(0xFE)
    Return()

    # Function_8_158D end

    def Function_9_17DA(): pass

    label("Function_9_17DA")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_17E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A0E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "与诺艾尔换班\x01",      # 1
            "放弃\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18BA")

    #C0016
    ChrTalk(
        0x109,
        "#10100F瓦吉，接下来就交给你啦！\x02",
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x9,
        "#10300F呵呵，明白了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0x4, 0xF9, 0x0)
    OP_32(0x8, 0xF9, 0x0)
    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x4)
    OP_37()
    Call(0, 3)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_1A09")

    label("loc_18BA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_18CE")
    Jump("loc_1A09")

    label("loc_18CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A09")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1991")

    #C0018
    ChrTalk(
        0x9,
        (
            "#10303F这个地方盛开着\x01",
            "『灵智之草』。\x02\x03",

            "#10302F笼罩在这一带的奇异雾气，\x01",
            "莫非也与这种花有关吗……？\x02\x03",

            "#10304F总之，如果要继续前进，\x01",
            "还是慎重一些为好。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1A09")

    label("loc_1991")


    #C0019
    ChrTalk(
        0x9,
        (
            "#10302F笼罩在这一带的奇异雾气，\x01",
            "莫非也与『灵智之草』有关吗……？\x02\x03",

            "#10304F总之，如果要继续前进，\x01",
            "还是慎重一些为好。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A09")

    Jump("loc_17E7")

    label("loc_1A0E")

    TalkEnd(0xFE)
    Return()

    # Function_9_17DA end

    def Function_10_1A12(): pass

    label("Function_10_1A12")

    EventBegin(0x1)
    #Sound(2094, 255, 100, 0)    #voice#Lloyd

    #C0020
    ChrTalk(
        0x101,
        "#0000F在这里似乎可以钓到鱼呢。\x02",
    )

    CloseMessageWindow()
    OP_68(14080, 500, -10820, 1500)
    MoveCamera(53, 46, 0, 1500)
    OP_6E(650, 1500)
    SetCameraDistance(16290, 1500)
    Sleep(1000)
    SetChrName("")

    #A0021
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AD5")
    OP_E2(0x2)
    MiniGame(0x6, 0x6, 0x328C, 0xFFFFFE0C, 0xFFFFE322, 0xB4, 0x3836, 0xFFFFFE0C, 0xFFFFC7E8)

    label("loc_1AD5")

    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_1A12 end

    def Function_11_1ADA(): pass

    label("Function_11_1ADA")

    SetMapFlags(0x80)
    SetMapFlags(0x8000000)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x31, 2)
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x182, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1B0C")
    SetScenarioFlags(0x31, 2)

    label("loc_1B0C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B52")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 2)), scpexpr(EXPR_END)), "loc_1B4C")
    Jc((scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_IMOD), scpexpr(EXPR_PUSH_LONG, 0x32), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_1B41")
    Sound(2499, 255, 100, 0)    #voice#Noel
    Jump("loc_1B47")

    label("loc_1B41")

    Sound(3537, 255, 100, 0)    #voice#Noel

    label("loc_1B47")

    Jump("loc_1B52")

    label("loc_1B4C")

    Sound(3344, 255, 100, 0)    #voice#Lloyd

    label("loc_1B52")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1DF9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 5)), scpexpr(EXPR_END)), "loc_1BC3")
    MenuCmd(0, 0)
    MenuCmd(1, 0, "登上梅尔卡瓦")
    MenuCmd(1, 0, "放弃")
    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1BA3"),
        (SWITCH_DEFAULT, "loc_1BB4"),
    )


    label("loc_1BA3")

    SetScenarioFlags(0x22, 0)
    NewScene("e3020", 0, 0, 0)
    IdleLoop()
    Jump("loc_1BBE")

    label("loc_1BB4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1BBE")

    Jump("loc_1DF4")

    label("loc_1BC3")

    MenuCmd(0, 0)
    MenuCmd(1, 0, "驾驶导力车移动")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1BF3")
    MenuCmd(1, 0, "在导力车中休息")

    label("loc_1BF3")

    MenuCmd(2, 0, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C1D"),
        (1, "loc_1D21"),
        (2, "loc_1DB2"),
        (SWITCH_DEFAULT, "loc_1DEA"),
    )


    label("loc_1C1D")

    SetMapObjFrame(0x7, "light", 0x0, 0x1)
    OP_74(0x7, 0x1E)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1C4E")
    OP_70(0x7, 0x12C)
    OP_71(0x7, 0x12C, 0x14A, 0x0, 0x0)
    Jump("loc_1C5E")

    label("loc_1C4E")

    OP_70(0x7, 0xF0)
    OP_71(0x7, 0xF0, 0x10E, 0x0, 0x0)

    label("loc_1C5E")

    Sound(462, 0, 100, 0)
    SoundLoad(2500)
    SoundLoad(3538)
    SoundLoad(3345)
    Sleep(700)
    FadeToDark(300, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2E, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB4")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1CB4")

    FadeToDark(0, 0, -1)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1D4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CD7")
    Sound(461, 0, 100, 0)

    label("loc_1CD7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1CF7")
    OP_70(0x7, 0x14A)
    OP_71(0x7, 0x14A, 0x12C, 0x0, 0x0)
    Jump("loc_1D07")

    label("loc_1CF7")

    OP_70(0x7, 0x10E)
    OP_71(0x7, 0x10E, 0xF0, 0x0, 0x0)

    label("loc_1D07")

    Sleep(1000)
    OP_0D()
    SetMapObjFrame(0x7, "light", 0x1, 0x1)
    OP_70(0x7, 0x0)
    Jump("loc_1B52")

    label("loc_1D21")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_END)), "loc_1D93")
    OP_57(0x0)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_5A()
    Sound(13, 0, 100, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x31, 0)), scpexpr(EXPR_END)), "loc_1D56")
    OP_32(0xFF, 0xFF, 0x0)
    Jump("loc_1D6E")

    label("loc_1D56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1D69")
    OP_32(0xFF, 0xFE, 0x0)
    Jump("loc_1D6E")

    label("loc_1D69")

    OP_32(0xFF, 0xFA, 0x0)

    label("loc_1D6E")

    OP_6A(0x0, 0x0)
    Sleep(3500)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DAD")

    label("loc_1D93")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1DA3")
    OP_AF(0xFB)
    Jump("loc_1DAD")

    label("loc_1DA3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DAD")

    Jump("loc_1DF4")

    label("loc_1DB2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1DCB")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1DE5")

    label("loc_1DCB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x30, 7)), scpexpr(EXPR_END)), "loc_1DDB")
    OP_AF(0xFB)
    Jump("loc_1DE5")

    label("loc_1DDB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DE5")

    Jump("loc_1DF4")

    label("loc_1DEA")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1DF4")

    Jump("loc_1B52")

    label("loc_1DF9")

    ClearMapFlags(0x8000000)
    OP_60(0x0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    # Function_11_1ADA end

    def Function_12_1E07(): pass

    label("Function_12_1E07")

    OP_9C(0xFE, 0xFFFFAC04, 0x0, 0xFFFFAC04, 0x32, 0x3)
    Return()

    # Function_12_1E07 end

    def Function_13_1E1F(): pass

    label("Function_13_1E1F")

    OP_9C(0xFE, 0xFFFFE4A8, 0x0, 0xFFFFE4A8, 0x32, 0x5)
    Return()

    # Function_13_1E1F end

    def Function_14_1E37(): pass

    label("Function_14_1E37")

    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0xFFFFFA24, 0x32, 0xA)
    Return()

    # Function_14_1E37 end

    def Function_15_1E4F(): pass

    label("Function_15_1E4F")

    OP_9C(0xFE, 0xFFFFEE6C, 0x0, 0x0, 0x32, 0xA)
    Return()

    # Function_15_1E4F end

    def Function_16_1E67(): pass

    label("Function_16_1E67")

    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0x0, 0x32, 0xA)
    Return()

    # Function_16_1E67 end

    def Function_17_1E7F(): pass

    label("Function_17_1E7F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1EC9")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -500, -5000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(233)
    Jump("Function_17_1E7F")

    label("loc_1EC9")

    Return()

    # Function_17_1E7F end

    def Function_18_1ECA(): pass

    label("Function_18_1ECA")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1F14")
    PlayEffect(0x0, 0xFF, 0xFE, 0x4, 0, -750, -5000, 0, 0, 0, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    Sleep(333)
    Jump("Function_18_1ECA")

    label("loc_1F14")

    Return()

    # Function_18_1ECA end

    def Function_19_1F15(): pass

    label("Function_19_1F15")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xFFFFF542, 0x0, 0x5DC, 0xFA, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(39, 0, 80, 0)
    Sound(30, 0, 50, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_19_1F15 end

    def Function_20_1F78(): pass

    label("Function_20_1F78")

    SetChrFlags(0xFE, 0x20)
    SetChrFlags(0xFE, 0x1000)
    SetChrSubChip(0xFE, 0x0)
    SetChrFlags(0xFE, 0x40)
    ClearChrFlags(0xFE, 0x4)
    ClearChrBattleFlags(0xFE, 0x20)
    SetChrSubChip(0xFE, 0x1)
    Sleep(150)
    SetChrSubChip(0xFE, 0x2)
    OP_9C(0xFE, 0xFFFFFA24, 0x0, 0x5DC, 0xFA, 0x9C4)
    ClearChrFlags(0xFE, 0x20)
    ClearChrFlags(0xFE, 0x1000)
    SetChrChipByIndex(0xFE, 0xFF)
    SetChrSubChip(0xFE, 0x0)
    Sound(39, 0, 80, 0)
    Sound(30, 0, 50, 0)
    ClearChrFlags(0xFE, 0x40)
    Return()

    # Function_20_1F78 end

    def Function_21_1FDB(): pass

    label("Function_21_1FDB")

    Sound(483, 2, 50, 0)
    Sleep(200)
    OP_25(0x1E3, 0x3C)
    Sleep(200)
    OP_25(0x1E3, 0x46)
    Sleep(200)
    OP_25(0x1E3, 0x50)
    Sleep(200)
    OP_25(0x1E3, 0x5A)
    Sleep(200)
    OP_25(0x1E3, 0x64)
    Sleep(2000)
    StopSound(483, 500, 100)
    Sound(481, 0, 100, 0)
    Sleep(2500)
    Sound(484, 0, 50, 0)
    Sleep(500)
    Sound(477, 0, 60, 0)
    Sleep(6500)
    Sound(478, 0, 40, 0)
    Return()

    # Function_21_1FDB end

    def Function_22_202F(): pass

    label("Function_22_202F")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00500.itc", 0x1E)
    LoadChrToIndex("chr/ch02902.itc", 0x1F)
    LoadChrToIndex("chr/ch00201.itc", 0x20)
    LoadChrToIndex("chr/ch00301.itc", 0x21)
    LoadChrToIndex("chr/ch02901.itc", 0x22)
    LoadChrToIndex("chr/ch03001.itc", 0x23)
    LoadEffect(0x0, "event/ev315_00.eff")
    LoadEffect(0x1, "event/ev202_00.eff")
    SoundLoad(483)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_20CB")
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis263.itp")
    Jump("loc_20F7")

    label("loc_20CB")

    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis264.itp")

    label("loc_20F7")

    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu00700.itp")
    SetChrPos(0xB, 57000, -500, 59720, 225)
    SetChrPos(0x101, 56350, -150, 57870, 225)
    SetChrPos(0x109, 55800, -150, 58520, 225)
    SetChrPos(0x102, 55150, -150, 59270, 270)
    SetChrPos(0x105, 57400, 280, 61720, 270)
    SetChrPos(0x103, 56900, 280, 59620, 225)
    SetChrPos(0x104, 58300, 280, 59620, 225)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetChrFlags(0x109, 0x4)
    SetChrBattleFlags(0x101, 0x20)
    SetChrBattleFlags(0x102, 0x20)
    SetChrBattleFlags(0x103, 0x20)
    SetChrBattleFlags(0x104, 0x20)
    SetChrBattleFlags(0x105, 0x20)
    ClearChrFlags(0x102, 0x1)
    SetChrChipByIndex(0xA, 0x1E)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrPos(0xA, 10000, 0, 20000, 45)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_7D(0x90, 0xB0, 0xC0, 0x0, 0x0)
    OP_11(0xA0, 0xB8, 0xD0, 0x1, 0x28, 0x0)
    OP_68(52530, 1000, 55230, 0)
    MoveCamera(29, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(26420, 0)
    BeginChrThread(0xC, 1, 0, 21)
    FadeToBright(1000, 0)
    OP_68(25540, 1000, 30950, 7000)
    BeginChrThread(0xB, 1, 0, 12)
    BeginChrThread(0x109, 1, 0, 12)
    BeginChrThread(0x109, 3, 0, 17)
    Sleep(1500)
    MoveCamera(329, 20, 0, 3500)
    OP_6E(650, 3500)
    SetCameraDistance(26420, 3500)
    OP_7D(0xFF, 0xFF, 0xFF, 0x0, 0x1194)
    OP_11(0xB4, 0xE6, 0xFA, 0x19, 0x5A, 0x157C)
    Sleep(1000)
    EndChrThread(0x109, 0x3)
    BeginChrThread(0x109, 3, 0, 18)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xB, 1, 0, 13)
    BeginChrThread(0x109, 1, 0, 13)
    Sleep(1000)

    def lambda_22E4():
        OP_93(0xFE, 0x10E, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_22E4)

    def lambda_22F1():
        OP_93(0xFE, 0x10E, 0x64)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_22F1)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xB, 1, 0, 14)
    BeginChrThread(0x109, 1, 0, 14)
    WaitChrThread(0xB, 1)

    def lambda_2312():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_2312)

    def lambda_231F():
        OP_93(0xFE, 0x13B, 0xC8)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_231F)
    SetChrFlags(0x102, 0x1)
    BeginChrThread(0xB, 1, 0, 15)
    BeginChrThread(0x109, 1, 0, 15)
    SetChrSubChip(0x109, 0x2)
    OP_68(21520, 1000, 29780, 0)
    MoveCamera(282, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(24330, 0)
    Fade(500)
    OP_68(21520, 1000, 29780, 2000)
    MoveCamera(291, 23, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(19110, 2000)
    Sleep(1000)

    def lambda_23A5():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_23A5)
    WaitChrThread(0xB, 1)
    BeginChrThread(0xB, 1, 0, 16)
    BeginChrThread(0x109, 1, 0, 16)
    Sleep(300)

    def lambda_23C5():
        OP_9B(0x1, 0xFE, 0x159, 0x8CA, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23C5)
    Sleep(200)
    EndChrThread(0x109, 0x3)
    Sleep(200)

    def lambda_23E4():
        OP_93(0xFE, 0xE1, 0x12C)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_23E4)
    WaitChrThread(0x105, 2)
    Sleep(400)
    WaitChrThread(0xB, 1)
    OP_71(0x5, 0x5B, 0x78, 0x0, 0x0)
    WaitChrThread(0x104, 1)
    SetChrChipByIndex(0x104, 0x21)
    BeginChrThread(0x104, 1, 0, 19)
    Sleep(200)

    def lambda_2419():
        OP_9B(0x1, 0xFE, 0x1E, 0x3E8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2419)
    Sleep(200)
    WaitChrThread(0x105, 2)
    SetChrChipByIndex(0x105, 0x23)
    BeginChrThread(0x105, 1, 0, 19)
    WaitChrThread(0x104, 1)

    def lambda_2443():
        OP_9B(0x0, 0xFE, 0x14A, 0x1F4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2443)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x103, 1)

    def lambda_2460():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2460)
    WaitChrThread(0x103, 2)
    SetChrChipByIndex(0x103, 0x20)
    BeginChrThread(0x103, 1, 0, 19)
    Sleep(300)
    WaitChrThread(0x103, 1)
    SetChrPos(0x105, 14800, 0, 26800, 180)
    SetChrPos(0x103, 13500, 0, 28800, 180)
    SetChrPos(0x101, 12300, 0, 27000, 180)
    SetChrPos(0x102, 17000, 0, 32500, 225)
    SetChrPos(0x104, 12750, 0, 29500, 225)
    SetChrPos(0x109, 20500, 400, 30700, 225)
    ClearChrFlags(0x101, 0x4)
    ClearChrFlags(0x102, 0x4)
    ClearChrFlags(0x109, 0x4)
    ClearChrFlags(0x103, 0x4)
    ClearChrFlags(0x104, 0x4)
    ClearChrFlags(0x105, 0x4)
    ClearChrBattleFlags(0x101, 0x20)
    ClearChrBattleFlags(0x102, 0x20)
    ClearChrBattleFlags(0x109, 0x20)
    ClearChrBattleFlags(0x103, 0x20)
    ClearChrBattleFlags(0x104, 0x20)
    ClearChrBattleFlags(0x105, 0x20)
    SetChrChipByIndex(0x109, 0x0)
    SetChrSubChip(0x109, 0x0)
    OP_68(13480, 1000, 28250, 0)
    MoveCamera(12, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(20690, 0)
    Fade(500)

    def lambda_255F():
        OP_9B(0x0, 0xFE, 0x0, 0x1450, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_255F)

    def lambda_2574():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2574)

    def lambda_2589():
        OP_9B(0x0, 0xFE, 0xB, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_2589)

    def lambda_259E():
        OP_9B(0x0, 0xFE, 0x5, 0x7D0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_259E)

    def lambda_25B3():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_25B3)
    Sleep(850)
    SetChrChipByIndex(0x109, 0x22)
    BeginChrThread(0x109, 1, 0, 20)
    WaitChrThread(0x109, 1)

    def lambda_25D9():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_25D9)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    Sleep(150)

    def lambda_25F9():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_25F9)
    Sleep(250)

    def lambda_2609():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2609)
    WaitChrThread(0x109, 2)

    def lambda_261A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_261A)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x109, 2)
    Sleep(250)

    #C0022
    ChrTalk(
        0x101,
        "#00007F#5P这、这是……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x102,
        (
            "#00106F#5P林小姐她们\x01",
            "应该就是乘坐\x01",
            "那艘小船来这里的……\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x105,
        (
            "#10310F#11P……竟然……\x01",
            "会有这种事。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(11980, 1000, 24000, 0)
    MoveCamera(197, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16030, 0)
    OP_68(-6620, 1000, -43200, 9000)
    MoveCamera(228, 27, 0, 9000)
    OP_6E(650, 9000)
    SetCameraDistance(27620, 9000)
    SetChrPos(0x101, 8930, 0, 17730, 180)
    SetChrPos(0x102, 7930, 0, 18730, 180)
    SetChrPos(0x103, 10030, 0, 18430, 180)
    SetChrPos(0x109, 8530, 0, 19830, 180)
    SetChrPos(0x104, 9730, 0, 20530, 180)
    SetChrPos(0x105, 10730, 0, 19530, 180)
    SetChrPos(0xA, 750, 0, 10500, 45)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-7670, 1000, -44840, 0)
    MoveCamera(37, 36, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(41480, 0)
    OP_68(4910, 1000, 14450, 10000)
    MoveCamera(76, 35, 0, 10000)
    OP_6E(550, 10000)
    SetCameraDistance(27520, 10000)
    SetChrPos(0x101, 8930, 0, 17730, 225)
    SetChrPos(0x102, 7930, 0, 18730, 225)
    SetChrPos(0x103, 10030, 0, 18430, 225)
    SetChrPos(0x109, 8530, 0, 19830, 225)
    SetChrPos(0x104, 9730, 0, 20530, 225)
    SetChrPos(0x105, 10730, 0, 19530, 225)
    Sleep(3000)
    PlaceName2(340, 200, "c_plac51", 0x0, 0)

    def lambda_287E():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_287E)
    Sleep(100)

    def lambda_2896():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2896)
    Sleep(100)

    def lambda_28AE():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_28AE)
    Sleep(50)

    def lambda_28C6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_28C6)
    Sleep(50)

    def lambda_28DE():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28DE)
    Sleep(100)

    def lambda_28F6():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_28F6)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x109, 1)
    WaitChrThread(0x105, 1)
    Sleep(750)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(4460, 1000, 14170, 0)
    MoveCamera(224, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(16000, 0)
    OP_0D()
    Sleep(300)

    #C0025
    ChrTalk(
        0x104,
        (
            "#00301F#12P喂喂……\x01",
            "我们难道是在做梦吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x109,
        (
            "#10106F#12P就像身处\x01",
            "童话世界中一样……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        (
            "#00208F#6P难、难以置信……\x02\x03",

            "#00201F似乎连空间自身的结构\x01",
            "都与现实中有所不同……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#00010F#6P灵智之草……究竟是在何时\x01",
            "生长得如此繁盛的？\x02\x03",

            "#00003F原来如此……\x01",
            "约亚西姆采集『真知』原料的\x01",
            "地方恐怕就是……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2628, 255, 100, 0)    #voice#Yin
    Sleep(500)
    ClearChrFlags(0xA, 0x80)

    #N0029
    NpcTalk(
        0xA,
        "声音",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#N#5P嗯，应该就是\x01",
            "这里了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(4260, 1000, 13700, 2000)
    MoveCamera(166, 18, 0, 2000)
    OP_6E(650, 2000)
    SetCameraDistance(13900, 2000)
    PlayEffect(0x1, 0xFF, 0xA, 0x1, 0, 1000, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(341, 0, 100, 0)
    ClearChrFlags(0xA, 0x8)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)

    def lambda_2BDE():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2BDE)

    def lambda_2BF3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2BF3)
    Sleep(300)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xA, 2)
    OP_6F(0x79)
    Sleep(300)

    #C0030
    ChrTalk(
        0x102,
        "#00105F#6P什么……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x109,
        "#10107F#6P那、那个时候的……！\x02",
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00011F#5P『银』……\x01",
            "你为何会在这里！？\x02",
        )
    )

    CloseMessageWindow()
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sound(2627, 255, 100, 0)    #voice#Yin
    Sleep(500)

    #A0033
    AnonymousTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "那是我想说的话。\x02\x03",

            "『蛇』在蠢蠢欲动，\x01",
            "不良团伙的头领化为魔人……\x02\x03",

            "各地同时出现了蓝花\x01",
            "与不可思议的『幻兽』……\x02\x03",

            "我循着这些线索来此调查，\x01",
            "竟然会偶遇你们……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0034
    ChrTalk(
        0x105,
        "#10305F#6P哎……？\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        (
            "#00301F#6P也就是说，\x01",
            "你察觉到这个地方很可疑，\x01",
            "所以特意来此调查？\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11P正是。\x02\x03",

            "#00702F嗯，看来你们来此的目的\x01",
            "与我有些不同吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x102,
        "#00106F#6P嗯……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x101,
        (
            "#00008F#5P情况特殊，\x01",
            "就把事情经过告诉你吧……\x02",
        )
    )

    CloseMessageWindow()
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "将林和艾欧莉娅下落不明\x01",
            "一事的整个过程做了说明。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0040
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11P原来那艘小船\x01",
            "是那两个游击士开来的。\x02\x03",

            "#00702F呵呵，原来如此……\x01",
            "由此看来，我似乎已经\x01",
            "接近事态的核心了。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x109,
        "#10101F#6P核心……\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x105,
        (
            "#10303F#6P也就是那些蓝花──『灵智之草』\x01",
            "为何会盛开在克洛斯贝尔各地，\x01",
            "『幻兽』为何会出现……\x02\x03",

            "#10301F以及……这些状况对克洛斯贝尔\x01",
            "而言『究竟有何含义』，没错吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P呵呵，不错。\x02\x03",

            "#00700F调查此事，也是我与『黑月』\x01",
            "签署的契约中所包含的内容。\x02\x03",

            "那两个游击士就由你们去寻找吧，\x01",
            "我就先——\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0x101,
        (
            "#00006F#5P……不。\x02\x03",

            "#00000F『银』……\x01",
            "我们一起行动如何？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xA, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_3149():

        label("loc_3149")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3149")

    QueueWorkItem2(0x102, 2, lambda_3149)
    Sleep(100)

    def lambda_315E():

        label("loc_315E")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_315E")

    QueueWorkItem2(0x104, 2, lambda_315E)
    Sleep(100)

    def lambda_3173():

        label("loc_3173")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3173")

    QueueWorkItem2(0x103, 2, lambda_3173)
    Sleep(50)

    def lambda_3188():

        label("loc_3188")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_3188")

    QueueWorkItem2(0x109, 2, lambda_3188)
    Sleep(50)

    def lambda_319D():

        label("loc_319D")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_319D")

    QueueWorkItem2(0x105, 2, lambda_319D)
    Sleep(200)

    #C0045
    ChrTalk(
        0x109,
        "#10111F#6P罗、罗伊德警官！？\x02",
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x105,
        "#10305F#6P喂喂，你是认真的吗？\x02",
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x102,
        (
            "#00111F#12P呼，我就猜到\x01",
            "你会说出这种话……\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#00204F#5P果然不出所料。\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x104,
        (
            "#00302F#6P真是的，你好像只有在\x01",
            "这种情况下会变得十分通融。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(2629, 255, 100, 0)    #voice#Yin
    Sleep(500)

    def lambda_3291():

        label("loc_3291")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_3291")

    QueueWorkItem2(0x102, 2, lambda_3291)
    Sleep(100)

    def lambda_32A6():

        label("loc_32A6")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_32A6")

    QueueWorkItem2(0x104, 2, lambda_32A6)
    Sleep(150)

    def lambda_32BB():

        label("loc_32BB")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_32BB")

    QueueWorkItem2(0x103, 2, lambda_32BB)
    Sleep(100)

    def lambda_32D0():

        label("loc_32D0")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_32D0")

    QueueWorkItem2(0x109, 2, lambda_32D0)
    Sleep(50)

    def lambda_32E5():

        label("loc_32E5")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_32E5")

    QueueWorkItem2(0x105, 2, lambda_32E5)
    Sleep(200)

    #C0050
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P……班宁斯，你是不是\x01",
            "没有搞清现在的状况？\x02\x03",

            "我与你们的立场相异，\x01",
            "也没有共通的利害关系。\x02\x03",

            "和当初在医院时不同，如今与你们合作，\x01",
            "我完全没有任何好处可言——\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x101,
        (
            "#00003F#5P完全没有？这样说未免过于武断了吧？\x02\x03",

            "#00001F林小姐和艾欧莉娅小姐\x01",
            "都有着接近Ａ级的高超实力。\x02\x03",

            "如果那两人联手，\x01",
            "恐怕可以与亚里欧斯\x01",
            "先生匹敌。\x02\x03",

            "#00006F前方的危险之高，甚至可以令\x01",
            "她们二人音讯全无……\x02\x03",

            "#00013F单凭你一个人，\x01",
            "真的可以断言毫无问题吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#11P……………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x103,
        "#00200F#5P嗯，毕竟是紧急事态。\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0x104,
        (
            "#00304F#6P如能顺利找到林小姐她们，\x01",
            "肯定可以得到一些重要情报。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0x102,
        (
            "#00100F#6P从效率角度来考虑，\x01",
            "我们确实应该合作呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P……哼哼…………\x02\x03",

            "『特别任务支援科』……\x01",
            "你们几个似乎都受到了\x01",
            "队长的影响。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        "#00112F#6P有、有那种事吗？\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x104,
        "#00309F#6P呼，好像也无法否定。\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x103,
        "#00211F#5P……虽然不是我的本意。\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_3652():

        label("loc_3652")

        OP_93(0xFE, 0x159, 0x1F4)
        Yield()
        Jump("loc_3652")

    QueueWorkItem2(0x101, 2, lambda_3652)
    Sleep(500)

    #C0060
    ChrTalk(
        0x101,
        (
            "#00011F#5P那个……为什么\x01",
            "要把责任归在我身上……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x109,
        "#10112F#6P啊、啊哈哈……\x02",
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0x105,
        (
            "#10309F#6P呵呵……\x01",
            "这也算是某种人格魅力吧。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_36EB():

        label("loc_36EB")

        OP_93(0xFE, 0xE1, 0x1F4)
        Yield()
        Jump("loc_36EB")

    QueueWorkItem2(0x101, 2, lambda_36EB)
    Sleep(100)
    Sleep(250)

    #C0063
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00702F#11P好吧，\x01",
            "我这次就暂时与你们同行。\x02\x03",

            "#00700F但如果『风之剑圣』赶到，\x01",
            "我就会立刻离开。\x02\x03",

            "没有意见吧？\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x101,
        "#00000F#5P嗯，明白了。\x02",
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x104,
        (
            "#00303F#6P话说回来，我们现在的人数有点多，\x01",
            "实在是不利于灵活行动啊。\x02\x03",

            "#00301F如果有魔兽突然袭来，\x01",
            "说不定会乱作一团。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_380C():

        label("loc_380C")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_380C")

    QueueWorkItem2(0x101, 2, lambda_380C)
    Sleep(50)

    def lambda_3821():

        label("loc_3821")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3821")

    QueueWorkItem2(0x102, 2, lambda_3821)
    Sleep(50)

    def lambda_3836():

        label("loc_3836")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3836")

    QueueWorkItem2(0x103, 2, lambda_3836)
    Sleep(50)

    def lambda_384B():

        label("loc_384B")

        TurnDirection(0xFE, 0x101, 500)
        Yield()
        Jump("loc_384B")

    QueueWorkItem2(0x109, 2, lambda_384B)
    Sleep(50)

    def lambda_3860():

        label("loc_3860")

        TurnDirection(0xFE, 0x104, 500)
        Yield()
        Jump("loc_3860")

    QueueWorkItem2(0x105, 2, lambda_3860)
    Sleep(200)

    #C0066
    ChrTalk(
        0x109,
        (
            "#10103F#12P既然如此，那就选派\x01",
            "一个人留在这里吧。\x02\x03",

            "#10101F毕竟小船也\x01",
            "需要看守。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x105,
        (
            "#10302F#5P这主意不错。\x01",
            "等『风之剑圣』赶到以后，\x01",
            "还可以起到联络作用。\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        "#00001F#11P明白了，那就来编组队伍吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_68(-2600, 1500, 2120, 3000)
    MoveCamera(182, 16, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(18630, 3000)

    def lambda_396F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_396F)
    Sleep(50)

    def lambda_397F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_397F)
    Sleep(50)

    def lambda_398F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_398F)
    Sleep(50)

    def lambda_399F():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_399F)
    Sleep(50)

    def lambda_39AF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 2, lambda_39AF)
    Sleep(50)

    def lambda_39BF():
        OP_93(0xFE, 0xE1, 0x1F4)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_39BF)
    OP_6F(0x79)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x75, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3A9A")
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    FadeToDark(0, 0, -1)

    #A0069
    AnonymousTalk(
        0x101,
        (
            "#00003F#1P（林小姐当时教我学会那招战技\x01",
            "  的恩情，我至今都没能回报……）\x02\x03",

            "#00013F（无论如何也要探寻到\x01",
            "  她们的下落……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Jump("loc_3B5F")

    label("loc_3A9A")

    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    FadeToDark(0, 0, -1)

    #A0070
    AnonymousTalk(
        0x101,
        (
            "#00006F#1P（林小姐她们在相识之初对我们很严厉，\x01",
            "  但最近已经建立了良好关系……）\x02\x03",

            "#00001F（无论如何也要探寻到\x01",
            "  她们的下落……！）\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)

    label("loc_3B5F")

    Sleep(1000)
    OP_32(0xFF, 0xF9, 0x0)
    SetMessageWindowPos(-1, 30, -1, -1)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K选择谁担当待命成员？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【瓦吉】\x01",        # 0
            "【诺艾尔】\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_3BD8"),
        (0, "loc_3BF0"),
        (SWITCH_DEFAULT, "loc_3C08"),
    )


    label("loc_3BD8")

    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x4)
    Jump("loc_3C08")

    label("loc_3BF0")

    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x9, 0x80)
    RemoveParty(0x8, 0xFF)
    AddParty(0x8, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x8)
    Jump("loc_3C08")

    label("loc_3C08")

    AddParty(0x5, 0xFF, 0xFF)
    SetChrFlags(0xA, 0x80)
    OP_49()
    OP_32(0x5, 0x0, 0x49)
    OP_32(0x5, 0x5, 0xC8)
    OP_42(0x5, 0x460, 0xFF)
    OP_42(0x5, 0x5E8, 0xFF)
    OP_42(0x5, 0x649, 0xFF)
    OP_42(0x5, 0x4A, 0x3)
    OP_42(0x5, 0x22, 0x4)
    RemoveCraft(0x5, 0xFFFF)
    OP_38(0x5, 0x80, 0x2)
    OP_38(0x5, 0x81, 0x1)
    OP_38(0x5, 0x82, 0x1)
    OP_38(0x5, 0x83, 0x1)
    OP_38(0x5, 0x84, 0x2)
    OP_38(0x5, 0x85, 0x2)
    OP_38(0x5, 0x86, 0x1)
    OP_42(0x5, 0xE7, 0x0)
    OP_42(0x5, 0xBA, 0x1)
    OP_42(0x5, 0x9E, 0x2)
    OP_42(0x5, 0x6D, 0x3)
    OP_42(0x5, 0x76, 0x4)
    OP_42(0x5, 0x69, 0x5)
    OP_42(0x5, 0x90, 0x6)
    AddCraft(0x5, 0xC8)
    AddCraft(0x5, 0xC9)
    AddCraft(0x5, 0xCA)
    AddCraft(0x5, 0xCB)
    AddCraft(0x5, 0xCC)
    AddCraft(0x5, 0x131)
    SetChrChipPat(0x5, 0x6, 0x131)
    AddCraft(0x5, 0x16D)
    OP_CC(0x1, 0xFF, 0x0)
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    SetChrPos(0x0, 11000, 0, 26000, 225)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetScenarioFlags(0x165, 2)
    OP_29(0xA9, 0x1, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x80, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CE3")
    Jump("loc_3CE8")

    label("loc_3CE3")

    OP_29(0x80, 0x4, 0x40)

    label("loc_3CE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x83, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3CF9")
    Jump("loc_3CFE")

    label("loc_3CF9")

    OP_29(0x83, 0x4, 0x40)

    label("loc_3CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x88, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D0F")
    Jump("loc_3D14")

    label("loc_3D0F")

    OP_29(0x88, 0x4, 0x40)

    label("loc_3D14")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8B, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D25")
    Jump("loc_3D2A")

    label("loc_3D25")

    OP_29(0x8B, 0x4, 0x40)

    label("loc_3D2A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8C, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D3B")
    Jump("loc_3D40")

    label("loc_3D3B")

    OP_29(0x8C, 0x4, 0x40)

    label("loc_3D40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x8D, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_3D51")
    Jump("loc_3D56")

    label("loc_3D51")

    OP_29(0x8D, 0x4, 0x40)

    label("loc_3D56")

    OP_C9(0x1, 0x10000)
    OP_50(0x52, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x21, 5)
    OP_66(0x6, 0x1)
    OP_24(0x1E3)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_202F end

    def Function_23_3D77(): pass

    label("Function_23_3D77")

    EventBegin(0x2)
    ClearMapFlags(0x20)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "停靠着一艘小船。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E04")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E04")

    #C0073
    ChrTalk(
        0x101,
        (
            "#00001F这是一艘可供双人乘坐的小船。\x02\x03",

            "好了，我们赶快向深处前进吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_3E04")

    EventEnd(0x3)
    Return()

    # Function_23_3D77 end

    SaveToFile()

Try(main)
