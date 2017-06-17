from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t0600.bin",                # FileName
        "t0600",                    # MapName
        "t0600",                    # Location
        0x0069,                     # MapIndex
        "ed7301",
        0x00002000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 105, 0, 2, 0, 3],
    )

    BuildStringList((
        "t0600",                  # 0
        "鉱山長ホフマン",         # 1
        "鉱員マックス",           # 2
        "鉱員マルロ",             # 3
        "鉱員ガンツ",             # 4
        "鉱員ロージー",           # 5
        "魔獣",                   # 6
        "魔獣",                   # 7
        "魔獣",                   # 8
        "魔獣",                   # 9
        "魔獣",                   # 10
        "bt0600",                 # 11
        "bt0600",                 # 12
    ))

    ATBonus("ATBonus_384", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_3A51", 3,   3,   9,   3,   5,   4,   4)

    MonsterBattlePostion("MonsterBattlePostion_3E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_444", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_448", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_44C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_450", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_454", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_458", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_45C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_460", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3C4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 2, 13, 180)

    # monster count: 5

    BattleInfo(
        "BattleInfo_464", 0x0000, 15, 6, 45, 6, 1, 30, 0, "bt0600", "Sepith_3A51", 40, 30, 20, 10,
        (
            ("ms76400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3E4", "MonsterBattlePostion_444", "ed7400", "ed7403", "ATBonus_384"),
            ("ms76400.dat", "ms76400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3C4", "MonsterBattlePostion_444", "ed7400", "ed7403", "ATBonus_384"),
            ("ms76400.dat", "ms76400.dat", "ms76400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3E4", "MonsterBattlePostion_444", "ed7400", "ed7403", "ATBonus_384"),
            ("ms76400.dat", "ms76400.dat", "ms76400.dat", "ms76400.dat", 0, 0, 0, 0, "MonsterBattlePostion_3C4", "MonsterBattlePostion_444", "ed7400", "ed7403", "ATBonus_384"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_52C", 0x0002, 30, 6, 0, 0, 1, 40, 0, "bt0600", 0x00000000, 100, 0, 0, 0,
        (
            ("ms65101.dat", "ms65101.dat", "ms65101.dat", "ms65101.dat", "ms65101.dat", 0, 0, 0, "MonsterBattlePostion_3E4", "MonsterBattlePostion_444", "ed7401", "ed7403", "ATBonus_384"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch26300.itc",                   # 00
        "chr/ch26200.itc",                   # 01
        "chr/ch30700.itc",                   # 02
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
        "monster/ch65150.itc",               # 10
        "monster/ch65150.itc",               # 11
        "monster/ch76450.itc",               # 12
        "monster/ch76451.itc",               # 13
    ))

    DeclNpc(-31850,  0,       32080,   270,  385,  0x0, 0,   0,   0,   0,   0,   0,   4,   255,  0)
    DeclNpc(-28860,  0,       56150,   0,    385,  0x0, 0,   1,   0,   0,   0,   0,   5,   255,  0)
    DeclNpc(4139,    0,       6690,    90,   385,  0x0, 0,   1,   0,   0,   0,   0,   6,   255,  0)
    DeclNpc(-11470,  0,       15090,   19,   385,  0x0, 0,   2,   0,   0,   0,   0,   7,   255,  0)
    DeclNpc(-17250,  50,      30370,   180,  385,  0x0, 0,   1,   0,   0,   0,   0,   8,   255,  0)
    DeclNpc(109209,  -8949,   -9039,   135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(110739,  -8949,   -6610,   135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(106959,  -9000,   -9560,   135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(109220,  -8949,   -5909,   135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(107290,  -9000,   -11909,  135,  449,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-22150,  25270,   0,       0x1010000,    "BattleInfo_464", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(6200,    35950,   0,       0x1010000,    "BattleInfo_464", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(124120,  6350,    0,       0x1010000,    "BattleInfo_464", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(111590,  34990,   0,       0x1010000,    "BattleInfo_464", 0,   18,  0xFFFF, 0,  1)
    DeclMonster(129789,  -23000,  -1950,   0x1010000,    "BattleInfo_464", 0,   18,  0xFFFF, 0,  1)

    DeclActor(129000,  0,       15000,   1200,    129000,  1000,    15000,   0x007C, 0,  9,  0x0000)
    DeclActor(130810,  0,       19250,   1200,    130810,  1000,    19250,   0x007C, 0,  10, 0x0000)
    DeclActor(119000,  -9000,   -26500,  1200,    119000,  -8000,   -26500,  0x007C, 0,  11, 0x0000)
    DeclActor(134600,  -2000,   -34220,  1200,    134600,  -1000,   -34220,  0x007C, 0,  12, 0x0000)
    DeclActor(-22540,  0,       54760,   1200,    -22540,  1500,    54760,   0x007C, 0,  17, 0x0000)
    DeclActor(117500,  -8950,   -15770,  1200,    117500,  -8000,   -15770,  0x007C, 0,  14, 0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 1

    ScpFunction((
        "Function_0_5D0",          # 00, 0
        "Function_1_688",          # 01, 1
        "Function_2_6B3",          # 02, 2
        "Function_3_8A4",          # 03, 3
        "Function_4_DD6",          # 04, 4
        "Function_5_1428",         # 05, 5
        "Function_6_1770",         # 06, 6
        "Function_7_1ABA",         # 07, 7
        "Function_8_1D69",         # 08, 8
        "Function_9_21F2",         # 09, 9
        "Function_10_233F",        # 0A, 10
        "Function_11_248C",        # 0B, 11
        "Function_12_25D9",        # 0C, 12
        "Function_13_2726",        # 0D, 13
        "Function_14_2E9D",        # 0E, 14
        "Function_15_34CD",        # 0F, 15
        "Function_16_38F0",        # 10, 16
        "Function_17_390F",        # 11, 17
    ))


    def Function_0_5D0(): pass

    label("Function_0_5D0")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_610"),
        (1, "loc_61C"),
        (2, "loc_628"),
        (3, "loc_634"),
        (4, "loc_640"),
        (5, "loc_64C"),
        (6, "loc_658"),
        (SWITCH_DEFAULT, "loc_664"),
    )


    label("loc_610")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_61C")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_628")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_634")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_640")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_64C")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_658")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_664")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_670")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_687")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_670")

    label("loc_687")

    Return()

    # Function_0_5D0 end

    def Function_1_688(): pass

    label("Function_1_688")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6B2")
    OP_94(0xFE, 0xFFFFA7FE, 0x7F4E, 0xFFFFC3B0, 0x6AA4, 0x3E8)
    Sleep(300)
    Jump("Function_1_688")

    label("loc_6B2")

    Return()

    # Function_1_688 end

    def Function_2_6B3(): pass

    label("Function_2_6B3")

    BeginChrThread(0xC, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_703")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6FE")
    SetChrPos(0xC, -18590, 0, 21420, 90)
    BeginChrThread(0xC, 0, 0, 0)

    label("loc_6FE")

    Jump("loc_8A3")

    label("loc_703")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_74D")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_748")
    SetChrPos(0xC, -18590, 0, 21420, 90)
    BeginChrThread(0xC, 0, 0, 0)

    label("loc_748")

    Jump("loc_8A3")

    label("loc_74D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_75B")
    Jump("loc_8A3")

    label("loc_75B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_7AA")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A5")
    SetChrPos(0xC, -18590, 0, 21420, 90)
    BeginChrThread(0xC, 0, 0, 0)

    label("loc_7A5")

    Jump("loc_8A3")

    label("loc_7AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_7F4")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7EF")
    SetChrPos(0xC, -18590, 0, 21420, 90)
    BeginChrThread(0xC, 0, 0, 0)

    label("loc_7EF")

    Jump("loc_8A3")

    label("loc_7F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_802")
    Jump("loc_8A3")

    label("loc_802")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA1, 4)), scpexpr(EXPR_END)), "loc_810")
    Jump("loc_8A3")

    label("loc_810")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_END)), "loc_81E")
    Jump("loc_8A3")

    label("loc_81E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 0)), scpexpr(EXPR_END)), "loc_82C")
    Jump("loc_8A3")

    label("loc_82C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA3, 3)), scpexpr(EXPR_END)), "loc_83A")
    Jump("loc_8A3")

    label("loc_83A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_85C")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8A3")

    label("loc_85C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_87E")
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    Jump("loc_8A3")

    label("loc_87E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_88C")
    Jump("loc_8A3")

    label("loc_88C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_89A")
    Jump("loc_8A3")

    label("loc_89A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_8A3")

    label("loc_8A3")

    Return()

    # Function_2_6B3 end

    def Function_3_8A4(): pass

    label("Function_3_8A4")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C9A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C7B")
    ClearMapFlags(0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C70")
    OP_E0(0x0)
    SetScenarioFlags(0x0, 5)

    label("loc_C70")

    OP_10(0x0, 0x0)
    OP_10(0x4, 0x1)
    Jump("loc_C95")

    label("loc_C7B")

    SetMapFlags(0x2000)
    OP_E0(0x1)
    ClearScenarioFlags(0x0, 5)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    OP_10(0x0, 0x1)
    OP_10(0x4, 0x0)

    label("loc_C95")

    Jump("loc_CAE")

    label("loc_C9A")

    ClearMapFlags(0x2000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAE")
    OP_E0(0x0)
    SetScenarioFlags(0x0, 5)

    label("loc_CAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC1")
    OP_70(0x0, 0x0)
    Jump("loc_CC5")

    label("loc_CC1")

    OP_70(0x0, 0x1E)

    label("loc_CC5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CD8")
    OP_70(0x1, 0x0)
    Jump("loc_CDC")

    label("loc_CD8")

    OP_70(0x1, 0x1E)

    label("loc_CDC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CEF")
    OP_70(0x2, 0x0)
    Jump("loc_CF3")

    label("loc_CEF")

    OP_70(0x2, 0x1E)

    label("loc_CF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D06")
    OP_70(0x3, 0x0)
    Jump("loc_D0A")

    label("loc_D06")

    OP_70(0x3, 0x1E)

    label("loc_D0A")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -22700, 0, 54850, 10000, 2000, 45000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 4)), scpexpr(EXPR_END)), "loc_D50")
    SetMapObjFrame(0xFF, "key00", 0x0, 0x1)
    SetMapObjFlags(0x15, 0x10)
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)
    Jump("loc_D6B")

    label("loc_D50")

    SetMapObjFrame(0xFF, "key00", 0x1, 0x1)
    ClearMapObjFlags(0x15, 0x10)
    SetBarrier(0x3, 0x0, 0x1)
    OP_66(0x4, 0x1)

    label("loc_D6B")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DD5")
    OP_66(0x5, 0x1)
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 117500, -8750, -15770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_DD5")

    Return()

    # Function_3_8A4 end

    def Function_4_DD6(): pass

    label("Function_4_DD6")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_FBB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F09")

    #C0001
    ChrTalk(
        0xFE,
        "俺は町長夫人から話を聞いた……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "町長がガンツをすぐに\x01",
            "連れて帰らないのも納得がいったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "……妙な薬なんて信じたくはねぇが……\x01",
            "俺の大切な部下を惑わしやがった奴は\x01",
            "絶対に許せねぇぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "そんなのに引っかかっちまった\x01",
            "ガンツにも特大の拳骨を\x01",
            "くれてやりてぇ気分だがな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_FB6")

    label("loc_F09")


    #C0005
    ChrTalk(
        0xFE,
        (
            "ガンツを惑わしやがった奴は\x01",
            "絶対に許せねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "だが、ホイホイとそんな誘惑に乗った\x01",
            "ガンツの野郎も情けねぇ。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "あいつが帰ってきたら\x01",
            "特大の拳骨をくれてやらなきゃな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_FB6")

    Jump("loc_1424")

    label("loc_FBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_106F")

    #C0008
    ChrTalk(
        0xFE,
        (
            "ガンツめ、ギャンブルで\x01",
            "大当たりを連発していたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "チッ、それで金に眼が眩んで\x01",
            "行方をくらましてたってとこか。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "帰ってきたら喝をいれてやんねぇとな。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1424")

    label("loc_106F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_107D")
    Jump("loc_1424")

    label("loc_107D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_10FF")

    #C0011
    ChrTalk(
        0xFE,
        (
            "ガンツの野郎……\x01",
            "一体どこをほっつき歩いてやがるんだか。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "へっ、まぁいい。\x01",
            "俺たちはひたすら穴を掘るだけさ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1424")

    label("loc_10FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1185")

    #C0013
    ChrTalk(
        0xFE,
        (
            "さっき妻から弁当の差し入れがあってな。\x01",
            "元気百万倍だぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "よーし、今日のラストスパートだ。\x01",
            "気合入れていくぜぇ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1424")

    label("loc_1185")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_12EC")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1258")

    #C0015
    ChrTalk(
        0xFE,
        (
            "しかし、今の時代は\x01",
            "便利になったモンだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "先代の鉱山長の頃は、\x01",
            "導力灯すら無かったからな。\x01",
            "奥へ進むのすら命がけだったんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "昔に比べりゃ、\x01",
            "鉱員の仕事も安全になった方だぜ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12E7")

    label("loc_1258")


    #C0018
    ChrTalk(
        0xFE,
        (
            "昔に比べりゃ、\x01",
            "鉱員の仕事も安全になった方だ。\x01",
            "これからも導力化していくだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "ま、将来この鉱山が残ってるかは\x01",
            "俺にもわからねぇがな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12E7")

    Jump("loc_1424")

    label("loc_12EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_13FF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13B0")

    #C0020
    ChrTalk(
        0xFE,
        (
            "マックスの怪我がやっと治ってな。\x01",
            "早速仕事に復帰してもらった。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "これでようやく、\x01",
            "元のペースを取り戻せるってもんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "うっし、今日も\x01",
            "気合入れて掘るとすっか！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_13FA")

    label("loc_13B0")


    #C0023
    ChrTalk(
        0xFE,
        (
            "マックスのヤツも\x01",
            "復帰したことだし……\x01",
            "今日も気合入れて掘るとすっか！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    Jump("loc_1424")

    label("loc_13FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_140D")
    Jump("loc_1424")

    label("loc_140D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_141B")
    Jump("loc_1424")

    label("loc_141B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1424")

    label("loc_1424")

    TalkEnd(0xFE)
    Return()

    # Function_4_DD6 end

    def Function_5_1428(): pass

    label("Function_5_1428")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_14C5")

    #C0024
    ChrTalk(
        0xFE,
        (
            "俺が魔獣に襲われて怪我している間も、\x01",
            "皆がフォローしてくれてたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "あの時の恩返しみたいなもんさ。\x01",
            "……鉱員の底力を見せてやらぁ！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176C")

    label("loc_14C5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1564")

    #C0026
    ChrTalk(
        0xFE,
        (
            "聞いた話だとガンツのやつ\x01",
            "随分儲かってたそうじゃないか。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "みんなに心配かけたバツとして\x01",
            "宴会１回分くらいは支払わせなきゃな。\x01",
            "はっはっは。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176C")

    label("loc_1564")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1572")
    Jump("loc_176C")

    label("loc_1572")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_15E7")

    #C0028
    ChrTalk(
        0xFE,
        (
            "おっと……パイプに穴があいてるな。\x01",
            "ネズミにでもかじられたか……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "早いとこ塞いじまうとするか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_176C")

    label("loc_15E7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1648")

    #C0030
    ChrTalk(
        0xFE,
        "もう２週間になるか……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "んん、あいつもいい大人とはいえ\x01",
            "流石に心配だなぁ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176C")

    label("loc_1648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_16B9")

    #C0032
    ChrTalk(
        0xFE,
        (
            "うちの奥さんの弁当のおかげで\x01",
            "腹いっぱい、元気いっぱいだ！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "うぉお、ガンガン仕事するぜ～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_176C")

    label("loc_16B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1747")

    #C0034
    ChrTalk(
        0xFE,
        (
            "魔獣に襲われた怪我が治ってな。\x01",
            "やっと仕事に復帰できたんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "あぁ～力が有り余ってやがるぜ！\x01",
            "早速、取り掛かるとすっか！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_176C")

    label("loc_1747")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1755")
    Jump("loc_176C")

    label("loc_1755")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1763")
    Jump("loc_176C")

    label("loc_1763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_176C")

    label("loc_176C")

    TalkEnd(0xFE)
    Return()

    # Function_5_1428 end

    def Function_6_1770(): pass

    label("Function_6_1770")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1781")
    Jump("loc_1AB6")

    label("loc_1781")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_178F")
    Jump("loc_1AB6")

    label("loc_178F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_179D")
    Jump("loc_1AB6")

    label("loc_179D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_17F0")

    #C0036
    ChrTalk(
        0xFE,
        "……ふぅ。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "ガンツのやつがいないと\x01",
            "いまいち気が乗らないよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1AB6")

    label("loc_17F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_17FE")
    Jump("loc_1AB6")

    label("loc_17FE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1980")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18F2")

    #C0038
    ChrTalk(
        0xFE,
        (
            "ガンツのヤツ、\x01",
            "何だか浮かれてやがるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "あいつ、前にスロットで\x01",
            "一度だけまぐれ当たりしたときから\x01",
            "すっかりカジノにはまってるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "別に楽しむのはいいけど、\x01",
            "いつになったら貸したミラを\x01",
            "返してくれんのかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_197B")

    label("loc_18F2")


    #C0041
    ChrTalk(
        0xFE,
        (
            "ガンツはカジノにはまってるが、\x01",
            "勝ったことなんてほとんどないんだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "ったく、いつになったら貸したミラを\x01",
            "返してくれんのかね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_197B")

    Jump("loc_1AB6")

    label("loc_1980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A35")

    #C0043
    ChrTalk(
        0xFE,
        (
            "お、あんたらはこないだ、\x01",
            "俺たちを助けてくれた……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "えっと……特務支援課、だっけか？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "あの時はありがとな。\x01",
            "俺もガンツも大怪我せずに済んだよ。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1A8C")

    label("loc_1A35")


    #C0046
    ChrTalk(
        0xFE,
        (
            "あの時はありがとな。\x01",
            "お陰で大怪我せずに済んだよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "特務支援課、応援してるぜ。\x02",
    )

    CloseMessageWindow()

    label("loc_1A8C")

    Jump("loc_1AB6")

    label("loc_1A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1A9F")
    Jump("loc_1AB6")

    label("loc_1A9F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1AAD")
    Jump("loc_1AB6")

    label("loc_1AAD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1AB6")

    label("loc_1AB6")

    TalkEnd(0xFE)
    Return()

    # Function_6_1770 end

    def Function_7_1ABA(): pass

    label("Function_7_1ABA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1ACB")
    Jump("loc_1D65")

    label("loc_1ACB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1AD9")
    Jump("loc_1D65")

    label("loc_1AD9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1AE7")
    Jump("loc_1D65")

    label("loc_1AE7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1AF5")
    Jump("loc_1D65")

    label("loc_1AF5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1B03")
    Jump("loc_1D65")

    label("loc_1B03")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1C1F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BAC")

    #C0048
    ChrTalk(
        0xFE,
        (
            "来月の記念祭中は\x01",
            "俺ら鉱員も休みなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "この休みを使って、カジノでの\x01",
            "今までの負け分を全部取り返す！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "へへへ、今から楽しみだぜ。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1C1A")

    label("loc_1BAC")


    #C0051
    ChrTalk(
        0xFE,
        (
            "来月の記念祭中は\x01",
            "俺ら鉱員も休みなんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "久しぶりのまとまった休みだ、\x01",
            "カジノでパーッと遊ぶとするぜ！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C1A")

    Jump("loc_1D65")

    label("loc_1C1F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1D40")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE0")

    #C0053
    ChrTalk(
        0xFE,
        "よっこいせっと……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "……あー、くそっ！\x01",
            "昨日カジノで負けたのを\x01",
            "思い出しちまった。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "ちくしょう、早いとこ\x01",
            "取り戻さねぇとな。\x01",
            "またマルロにミラを借りるか……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1D3B")

    label("loc_1CE0")


    #C0056
    ChrTalk(
        0xFE,
        "ああ、はやく週末にならねぇかな。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "最近負け越してるから\x01",
            "ここらで取り戻さねぇと……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D3B")

    Jump("loc_1D65")

    label("loc_1D40")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1D4E")
    Jump("loc_1D65")

    label("loc_1D4E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1D5C")
    Jump("loc_1D65")

    label("loc_1D5C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1D65")

    label("loc_1D65")

    TalkEnd(0xFE)
    Return()

    # Function_7_1ABA end

    def Function_8_1D69(): pass

    label("Function_8_1D69")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1ED5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E5E")

    #C0058
    ChrTalk(
        0xFE,
        (
            "へ、魔獣が出たって？\x01",
            "そりゃアンタ、運が悪かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "ま、そういう日も\x01",
            "たまにはあるよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "本は回収できたみたいだし、\x01",
            "とりあえず良かったってことで。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#0006F（他人事みたいに言ってるな……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1ECC")

    label("loc_1E5E")


    #C0062
    ChrTalk(
        0xFE,
        (
            "魔獣と出くわすなんて\x01",
            "運が悪かったな。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "ま、本は回収できたみたいだし、\x01",
            "とりあえず良かったってことで。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ECC")

    TalkEnd(0xFE)
    Return()

    label("loc_1ED5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FA1")

    #C0064
    ChrTalk(
        0xFE,
        (
            "本は鉱山の奥に\x01",
            "忘れてきちゃった。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "悪いけどさ、今は\x01",
            "仕事で手が離せないから\x01",
            "回収してきてくんない？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "そこの階段から降りた\x01",
            "坑道の奥だから、\x01",
            "すぐ見つかると思うよ。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_1FA1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1FBE")
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    label("loc_1FBE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_2081")

    #C0067
    ChrTalk(
        0xFE,
        (
            "ガンツぅ～……\x01",
            "いい加減戻って来いよ～……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "だいたい、町長が迎えに行ったはずなのに\x01",
            "まだ戻ってこねぇのはどういうこった？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "まさか、２人して遊んでるんじゃ\x01",
            "ないだろうな……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_2081")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_2103")

    #C0070
    ChrTalk(
        0xFE,
        (
            "ヒィ、ヒィ……\x01",
            "いままでサボってきたせいか\x01",
            "昨日の分の筋肉痛がヒドい。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "くっそぉ、仕事して忘れるしかねぇや！\x02",
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_2103")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_2111")
    Jump("loc_21EE")

    label("loc_2111")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_216A")

    #C0072
    ChrTalk(
        0xFE,
        (
            "ガンツがいないせいで\x01",
            "全然サボれねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "早く帰ってこねぇかなぁ。\x02",
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_216A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_21AD")

    #C0074
    ChrTalk(
        0xFE,
        (
            "人数が少ないせいで\x01",
            "サボる暇が見つかんないぜ……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21EE")

    label("loc_21AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_21BB")
    Jump("loc_21EE")

    label("loc_21BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_21C9")
    Jump("loc_21EE")

    label("loc_21C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_21D7")
    Jump("loc_21EE")

    label("loc_21D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_21E5")
    Jump("loc_21EE")

    label("loc_21E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_21EE")

    label("loc_21EE")

    TalkEnd(0xFE)
    Return()

    # Function_8_1D69 end

    def Function_9_21F2(): pass

    label("Function_9_21F2")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_22EE")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_2277")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0075
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
    SetScenarioFlags(0x114, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_22E9")

    label("loc_2277")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0076
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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_22E9")

    Jump("loc_2333")

    label("loc_22EE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0077
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

    label("loc_2333")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_21F2 end

    def Function_10_233F(): pass

    label("Function_10_233F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_243B")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_23C4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0078
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
    SetScenarioFlags(0x114, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_2436")

    label("loc_23C4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0079
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2436")

    Jump("loc_2480")

    label("loc_243B")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0080
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

    label("loc_2480")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_233F end

    def Function_11_248C(): pass

    label("Function_11_248C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2588")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E8, 1)"), scpexpr(EXPR_END)), "loc_2511")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0081
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_2583")

    label("loc_2511")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2583")

    Jump("loc_25CD")

    label("loc_2588")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0083
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

    label("loc_25CD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_248C end

    def Function_12_25D9(): pass

    label("Function_12_25D9")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D5")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x65, 1)"), scpexpr(EXPR_END)), "loc_265E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0084
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x65),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_26D0")

    label("loc_265E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x65),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x65),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_26D0")

    Jump("loc_271A")

    label("loc_26D5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0086
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

    label("loc_271A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_25D9 end

    def Function_13_2726(): pass

    label("Function_13_2726")

    EventBegin(0x0)
    Fade(500)
    OP_68(-19490, 1000, 21500, 0)
    MoveCamera(43, 21, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(20050, 0)
    SetChrPos(0x101, -20700, 50, 20900, 90)
    SetChrPos(0x102, -20700, 50, 22100, 90)
    SetChrPos(0x103, -21900, 50, 20900, 90)
    SetChrPos(0x104, -21900, 50, 22100, 90)
    OP_93(0xC, 0x10E, 0x0)
    SetChrSubChip(0xC, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_27DA")
    SetChrPos(0x109, -21300, 50, 19600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_2805")

    label("loc_27DA")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2805")
    SetChrPos(0x10A, -21300, 50, 19600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2805")

    OP_0D()

    #C0087
    ChrTalk(
        0x101,
        (
            "#6P#0000Fあの……\x01",
            "鉱員のロージーさんですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xC,
        "#11Pあん？　何、あんたら。\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#6P#0000F今日は図書館の方から\x01",
            "依頼があって訪ねました。\x02\x03",

            "ロージーさん、図書館の本を\x01",
            "借りたままにしていませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        "#11P……あー、そのことか。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "#11Pうん、確かに\x01",
            "借りっぱなしにしてるな。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        (
            "#6P#0200F結構な日数を延滞\x01",
            "しているようですが……\x01",
            "なぜ返却しないのですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "#11Pクロスベル市までいくの\x01",
            "めんどいから。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2A22")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2A22")

    Sleep(1000)

    #C0094
    ChrTalk(
        0x104,
        "#6P#0306F（身も蓋もねぇな……）\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xC,
        (
            "#11Pま、回収しにきてくれたなら\x01",
            "願ったり叶ったりだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xC,
        (
            "#11P丁度さっきまで、\x01",
            "休憩中に読んでたから……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0097
    ChrTalk(
        0x102,
        "#5P#0105F……どうされました？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xC,
        (
            "#11P……忘れてきちゃった。\x01",
            "鉱山の奥に。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2BA6")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2BA6")

    Sleep(1000)

    #C0099
    ChrTalk(
        0xC,
        (
            "#11P悪いけどさ、今は\x01",
            "仕事で手が離せないから\x01",
            "自分で回収してきてくんない？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xC,
        (
            "#11Pそこの階段から降りた\x01",
            "坑道の奥だから、\x01",
            "すぐ見つかると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#6P#0206Fとことん面倒くさがり\x01",
            "なんですね……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CB9")

    #C0102
    ChrTalk(
        0x109,
        (
            "#12P#0503F司令とは違うベクトルの\x01",
            "怠けっぷり……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2CF1")

    label("loc_2CB9")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2CF1")

    #C0103
    ChrTalk(
        0x10A,
        "#12P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2CF1")


    #C0104
    ChrTalk(
        0x101,
        (
            "#6P#0006Fま、まぁ仕方ない。\x01",
            "回収しに行くとしよう。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 4)), scpexpr(EXPR_END)), "loc_2D8D")

    #C0105
    ChrTalk(
        0xC,
        (
            "#11Pああ、念の為言っとくけど\x01",
            "左奥の廃坑のほうじゃないからな。\x01",
            "気を付けてくれよ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DE8")

    label("loc_2D8D")


    #C0106
    ChrTalk(
        0xC,
        (
            "#11Pああ、左奥の廃坑のほうじゃないからな。\x01",
            "閉じてるから間違えないと思うけど、念の為。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE8")


    #C0107
    ChrTalk(
        0x101,
        "#6P#0001Fりょ、了解です。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E2C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2E2C")

    SetChrPos(0x0, -20750, 50, 20860, 90)
    OP_93(0xC, 0x5A, 0x0)
    OP_66(0x5, 0x1)
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 117500, -8750, -15770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_29(0x28, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_13_2726 end

    def Function_14_2E9D(): pass

    label("Function_14_2E9D")

    TalkBegin(0xFF)
    StopEffect(0x9, 0x2)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    Sound(17, 0, 100, 0)

    #A0108
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x2D9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(14, 280, 60, 3)
    OP_5A()
    AddItemNumber(0x2D9, 1)
    EventBegin(0x0)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F2D")
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    Jump("loc_2F43")

    label("loc_2F2D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2F43")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_2F43")

    Fade(500)
    OP_68(116640, -7650, -15740, 0)
    MoveCamera(45, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19950, 0)
    SetChrPos(0x101, 115910, -8950, -14740, 135)
    SetChrPos(0x102, 117900, -8950, -14060, 180)
    SetChrPos(0x103, 118710, -8950, -15820, 270)
    SetChrPos(0x104, 116830, -8950, -17480, 0)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3003")
    SetChrPos(0x109, 115020, -8950, -16730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_302E")

    label("loc_3003")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_302E")
    SetChrPos(0x10A, 115020, -8950, -16730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_302E")

    OP_0D()

    #C0109
    ChrTalk(
        0x101,
        "#5P#0000Fあった……これだな。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        "#5P#0105Fなんだか物々しいタイトルの本ね……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        (
            "#11P#0200Fクロスベルで起こった\x01",
            "怪現象を乗せた本ですね。\x02\x03",

            "#0203F題名どおり本当にあったかどうかは\x01",
            "確かではないそうですが。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#12P#0300Fなんかもう、\x01",
            "まんまヒマつぶしに借りたって\x01",
            "感じの本だな。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_31DC")

    #C0113
    ChrTalk(
        0x109,
        (
            "#6P#0500F確か、警備隊がどうこうした\x01",
            "とかいう話が載ってるんですが……\x02\x03",

            "そんな怖い事件があったなんて\x01",
            "正式な記録はないんですよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_31DC")


    #C0114
    ChrTalk(
        0x102,
        "#5P#0103F（何にせよ絶対読みたくないわね……）\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#5P#0000Fまぁ、とりあえず\x01",
            "無事に本も回収できたし、\x01",
            "次は──\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_329B")
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x10A,
        "#6P#0605Fム……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x13B, 0x1F4)

    label("loc_329B")

    StopBGM(0xBB8)
    Sleep(200)
    Sound(835, 0, 100, 0)
    Sleep(700)
    BeginChrThread(0xD, 3, 0, 16)
    BeginChrThread(0xE, 3, 0, 16)
    BeginChrThread(0xF, 3, 0, 16)
    BeginChrThread(0x10, 3, 0, 16)
    BeginChrThread(0x11, 3, 0, 16)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_332F():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_332F)

    def lambda_333C():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_333C)

    def lambda_3349():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3349)

    def lambda_3356():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3356)
    OP_68(115510, -8000, -13560, 4000)
    MoveCamera(16, 17, 0, 4000)
    OP_6E(440, 4000)
    SetCameraDistance(20790, 4000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_33C1")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_33B9():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_33B9)

    label("loc_33C1")

    Sleep(1000)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x11, 3)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7401", 0)

    #C0117
    ChrTalk(
        0x101,
        "#12P#0005Fま、魔獣！？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        "#12P#0301Fチッ、道をふさがれちまったな。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        "#12P#0201F……来ます！\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3496")
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_34AE")

    label("loc_3496")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_34AE")
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)

    label("loc_34AE")

    OP_0D()
    Battle("BattleInfo_52C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    Return()

    # Function_14_2E9D end

    def Function_15_34CD(): pass

    label("Function_15_34CD")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x2)
    SetMapFlags(0x8000000)
    StopEffect(0x9, 0x2)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_352F")
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    Jump("loc_3545")

    label("loc_352F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3545")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_3545")

    OP_68(115910, -8000, -14990, 0)
    MoveCamera(12, 27, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21830, 0)
    SetChrPos(0x101, 115910, -8950, -14740, 315)
    SetChrPos(0x102, 117900, -8950, -14060, 315)
    SetChrPos(0x103, 118710, -8950, -15820, 315)
    SetChrPos(0x104, 116830, -8950, -17480, 315)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_360F")
    SetChrPos(0x109, 115020, -8950, -16730, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_3642")

    label("loc_360F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3642")
    SetChrPos(0x10A, 115020, -8950, -16730, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)

    label("loc_3642")

    FadeToBright(1000, 0)
    OP_0D()

    #C0120
    ChrTalk(
        0x101,
        "#11P#0006Fふぅ……驚いたな。\x02",
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36BC")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_36D4")

    label("loc_36BC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_36D4")
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    label("loc_36D4")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3730")

    #C0121
    ChrTalk(
        0x10A,
        "#6P#0603Fまったく、油断をするな！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#11P#0012Fはは、すみません……\x02",
    )

    CloseMessageWindow()

    label("loc_3730")


    #C0123
    ChrTalk(
        0x104,
        (
            "#12P#0300Fま、でも俺たちの敵じゃ\x01",
            "なかったようだがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#12P#0200F道中にも魔獣はウロウロしてましたし、\x01",
            "丁度魔獣が沸いてくる瞬間に\x01",
            "出くわしてしまったようです。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#11P#0100F本を傷つけられずにすんで\x01",
            "良かったわね。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#12P#0000Fよし、それじゃあ行くとしようか。\x02",
    )

    CloseMessageWindow()
    OP_29(0x28, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3867")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_3867")

    SetChrPos(0x0, 115910, -8950, -14740, 315)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3893")
    OP_D5(0x22)
    Jump("loc_38A5")

    label("loc_3893")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38A5")
    OP_D5(0x22)

    label("loc_38A5")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38C4")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_38DE")

    label("loc_38C4")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_38DE")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_38DE")

    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_15_34CD end

    def Function_16_38F0(): pass

    label("Function_16_38F0")


    def lambda_38F5():
        OP_98(0xFE, 0xFA0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38F5)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_38F0 end

    def Function_17_390F(): pass

    label("Function_17_390F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_39D2")
    TalkBegin(0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【廃坑の鍵を使う】\x01",      # 0
            "【やめる】\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_39CA")
    Fade(500)
    SetMapObjFrame(0xFF, "key00", 0x0, 0x1)
    OP_0D()
    Sound(809, 0, 100, 0)
    SetChrName("")

    #A0127
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "廃坑の扉の鍵を開けた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39B9")
    OP_29(0x1C, 0x1, 0x2)

    label("loc_39B9")

    SetScenarioFlags(0xBF, 4)
    SetMapObjFlags(0x15, 0x10)
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_39CA")

    TalkEnd(0xFF)
    Jump("loc_3A28")

    label("loc_39D2")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は頑丈な鎖で閉じられている。\x01",
            "どうやら向こうは廃坑のようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_3A28")

    Return()

    # Function_17_390F end

    SaveToFile()

Try(main)
