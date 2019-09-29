from ZeroScenarioHelper import *

def main():
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
        "霍夫曼矿山长",           # 1
        "矿工马库斯",             # 2
        "矿工玛尔罗",             # 3
        "矿工冈兹",               # 4
        "矿工罗基",               # 5
        "魔兽",                   # 6
        "魔兽",                   # 7
        "魔兽",                   # 8
        "魔兽",                   # 9
        "魔兽",                   # 10
        "bt0600",                 # 11
        "bt0600",                 # 12
    ))

    ATBonus("ATBonus_384", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_35CF", 3,   3,   9,   3,   5,   4,   4)

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
        "BattleInfo_464", 0x0000, 15, 6, 45, 6, 1, 30, 0, "bt0600", "Sepith_35CF", 40, 30, 20, 10,
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
        "Function_5_131C",         # 05, 5
        "Function_6_15D4",         # 06, 6
        "Function_7_18A8",         # 07, 7
        "Function_8_1B0D",         # 08, 8
        "Function_9_1F1C",         # 09, 9
        "Function_10_2052",        # 0A, 10
        "Function_11_2188",        # 0B, 11
        "Function_12_22BE",        # 0C, 12
        "Function_13_23F4",        # 0D, 13
        "Function_14_2AE5",        # 0E, 14
        "Function_15_30C5",        # 0F, 15
        "Function_16_348E",        # 10, 16
        "Function_17_34AD",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_F7D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EED")

    #C0001
    ChrTalk(
        0xFE,
        "我已从镇长夫人那里听说了事情的经过……\x02",
    )

    CloseMessageWindow()

    #C0002
    ChrTalk(
        0xFE,
        (
            "这下也就可以理解\x01",
            "镇长为什么没能马上带冈兹回来了。\x02",
        )
    )

    CloseMessageWindow()

    #C0003
    ChrTalk(
        0xFE,
        (
            "……虽然不想相信有什么奇怪的药……\x01",
            "不过，竟敢引诱我重要的部下，\x01",
            "绝对不可原谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0004
    ChrTalk(
        0xFE,
        (
            "竟然会被那种东西诱惑，\x01",
            "冈兹那小子也得\x01",
            "好好吃我一顿拳头才行。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_F78")

    label("loc_EED")


    #C0005
    ChrTalk(
        0xFE,
        (
            "引诱冈兹的家伙\x01",
            "绝对不可原谅。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0xFE,
        (
            "但是，冈兹竟然那么轻易就上钩，\x01",
            "也真是个丢人的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0xFE,
        (
            "等那小子回来之后，\x01",
            "少不了要挨我一顿揍。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_F78")

    Jump("loc_1318")

    label("loc_F7D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1019")

    #C0008
    ChrTalk(
        0xFE,
        (
            "冈兹那小子，好像在\x01",
            "『巴鲁卡』连续赢了大量米拉啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0xFE,
        (
            "嘁，所以就被金钱冲昏头脑，\x01",
            "玩起失踪了吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0xFE,
        "回来之后，一定要狠狠骂他一顿才行。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1318")

    label("loc_1019")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1027")
    Jump("loc_1318")

    label("loc_1027")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1093")

    #C0011
    ChrTalk(
        0xFE,
        (
            "老婆刚才给我送来了饭，\x01",
            "我又精神百倍了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0xFE,
        (
            "好～今天只剩下最后的冲刺了，\x01",
            "鼓足干劲吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1318")

    label("loc_1093")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_10ED")

    #C0013
    ChrTalk(
        0xFE,
        (
            "冈兹那家伙……\x01",
            "到底上哪里晃悠去了。\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0xFE,
        (
            "哼，算了，\x01",
            "我们只管挖洞就是。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1318")

    label("loc_10ED")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1222")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_11A2")

    #C0015
    ChrTalk(
        0xFE,
        (
            "话说，现在这时代\x01",
            "还真是方便啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xFE,
        (
            "上代矿山长在任的时候，\x01",
            "连导力灯都没有呢。\x01",
            "往深处走一点就有生命危险。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xFE,
        (
            "矿工的工作和以前比起来\x01",
            "也安全多了啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_121D")

    label("loc_11A2")


    #C0018
    ChrTalk(
        0xFE,
        (
            "矿工的工作和以前比起来\x01",
            "也安全多了。\x01",
            "今后也会继续发展导力化吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xFE,
        (
            "不过，我也不知道这座矿山\x01",
            "能不能一直存续到将来呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_121D")

    Jump("loc_1318")

    label("loc_1222")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_12F3")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12B6")

    #C0020
    ChrTalk(
        0xFE,
        (
            "马库斯的伤终于治好了。\x01",
            "我马上让他回来工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0xFE,
        (
            "这下终于\x01",
            "能恢复原来的步调了。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "好，今天也要\x01",
            "鼓足干劲挖矿啊！\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_12EE")

    label("loc_12B6")


    #C0023
    ChrTalk(
        0xFE,
        (
            "马库斯那家伙\x01",
            "也回来了……\x01",
            "今天也要鼓足干劲挖矿啊！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_12EE")

    Jump("loc_1318")

    label("loc_12F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1301")
    Jump("loc_1318")

    label("loc_1301")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_130F")
    Jump("loc_1318")

    label("loc_130F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1318")

    label("loc_1318")

    TalkEnd(0xFE)
    Return()

    # Function_4_DD6 end

    def Function_5_131C(): pass

    label("Function_5_131C")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_139D")

    #C0024
    ChrTalk(
        0xFE,
        (
            "在我被魔兽袭击受伤期间，\x01",
            "大家都很照顾我。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xFE,
        (
            "就当作是对那时的报恩吧。\x01",
            "……要让大家看看我身为矿工的潜力！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D0")

    label("loc_139D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_141A")

    #C0026
    ChrTalk(
        0xFE,
        (
            "听说冈兹那家伙\x01",
            "好像赚了很多米拉嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0xFE,
        (
            "作为让大家担心的惩罚，\x01",
            "他至少也得出钱办一场宴会才行啊，\x01",
            "哈哈哈。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D0")

    label("loc_141A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1428")
    Jump("loc_15D0")

    label("loc_1428")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1477")

    #C0028
    ChrTalk(
        0xFE,
        (
            "哦……管子上有个洞啊，\x01",
            "是被老鼠咬了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        "趁早堵上吧。\x02",
    )

    CloseMessageWindow()
    Jump("loc_15D0")

    label("loc_1477")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_14E0")

    #C0030
    ChrTalk(
        0xFE,
        "都过了两个星期了吗……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "嗯嗯，虽说那家伙已经是个成年人了，\x01",
            "但终究还是令人担心啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D0")

    label("loc_14E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1539")

    #C0032
    ChrTalk(
        0xFE,
        (
            "吃了我老婆做的便当，\x01",
            "肚子饱饱，精神满满啦！\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        "噢噢，拼命干活吧～！\x02",
    )

    CloseMessageWindow()
    Jump("loc_15D0")

    label("loc_1539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_15AB")

    #C0034
    ChrTalk(
        0xFE,
        (
            "被魔兽袭击时受的伤已经治好了，\x01",
            "终于能回来工作了。\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xFE,
        (
            "啊啊～力量多得要溢出来啦！\x01",
            "赶紧开工吧！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15D0")

    label("loc_15AB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_15B9")
    Jump("loc_15D0")

    label("loc_15B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_15C7")
    Jump("loc_15D0")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_15D0")

    label("loc_15D0")

    TalkEnd(0xFE)
    Return()

    # Function_5_131C end

    def Function_6_15D4(): pass

    label("Function_6_15D4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_15E5")
    Jump("loc_18A4")

    label("loc_15E5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_15F3")
    Jump("loc_18A4")

    label("loc_15F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1601")
    Jump("loc_18A4")

    label("loc_1601")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1648")

    #C0036
    ChrTalk(
        0xFE,
        "……呼。\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "冈兹那家伙不在，\x01",
            "还真有点提不起劲啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A4")

    label("loc_1648")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1656")
    Jump("loc_18A4")

    label("loc_1656")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1782")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1718")

    #C0038
    ChrTalk(
        0xFE,
        (
            "冈兹那家伙，\x01",
            "好像有点浮躁啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0xFE,
        (
            "那小子自从以前玩老虎机时\x01",
            "偶然中了一次之后，\x01",
            "就完全迷上『巴鲁卡』了。\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xFE,
        (
            "玩玩倒是可以，\x01",
            "但要到几时才能\x01",
            "把我借他的米拉还来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_177D")

    label("loc_1718")


    #C0041
    ChrTalk(
        0xFE,
        (
            "冈兹虽然迷上了『巴鲁卡』，\x01",
            "但几乎从没赢过。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0xFE,
        (
            "真是的，要到几时才能\x01",
            "把我借他的米拉还来啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)

    label("loc_177D")

    Jump("loc_18A4")

    label("loc_1782")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_187F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1823")

    #C0043
    ChrTalk(
        0xFE,
        (
            "哦，你们是之前\x01",
            "救了我们的……\x02",
        )
    )

    CloseMessageWindow()

    #C0044
    ChrTalk(
        0xFE,
        "那个……特别任务支援科的人，对吧？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xFE,
        (
            "那时真是谢谢了。\x01",
            "多亏了你们，我和冈兹才免于身受重伤。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_187A")

    label("loc_1823")


    #C0046
    ChrTalk(
        0xFE,
        (
            "那时真是谢谢了。\x01",
            "多亏你们，我们才没有受重伤。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0xFE,
        "特别任务支援科，我支持你们哦。\x02",
    )

    CloseMessageWindow()

    label("loc_187A")

    Jump("loc_18A4")

    label("loc_187F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_188D")
    Jump("loc_18A4")

    label("loc_188D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_189B")
    Jump("loc_18A4")

    label("loc_189B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_18A4")

    label("loc_18A4")

    TalkEnd(0xFE)
    Return()

    # Function_6_15D4 end

    def Function_7_18A8(): pass

    label("Function_7_18A8")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_18B9")
    Jump("loc_1B09")

    label("loc_18B9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_18C7")
    Jump("loc_1B09")

    label("loc_18C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_18D5")
    Jump("loc_1B09")

    label("loc_18D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_18E3")
    Jump("loc_1B09")

    label("loc_18E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_18F1")
    Jump("loc_1B09")

    label("loc_18F1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_19F9")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1994")

    #C0048
    ChrTalk(
        0xFE,
        (
            "下个月的纪念庆典期间，\x01",
            "我们矿工也要放假。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xFE,
        (
            "趁这次放假，我要去『巴鲁卡』\x01",
            "把以前输的全都赢回来！\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0xFE,
        "嘿嘿嘿，现在就开始期待了。\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_19F4")

    label("loc_1994")


    #C0051
    ChrTalk(
        0xFE,
        (
            "下个月的纪念庆典期间，\x01",
            "我们矿工也要放假。\x02",
        )
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xFE,
        (
            "那是久违的长假，\x01",
            "要去『巴鲁卡』好好玩一番！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_19F4")

    Jump("loc_1B09")

    label("loc_19F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1AE4")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A94")

    #C0053
    ChrTalk(
        0xFE,
        "嘿哟……\x02",
    )

    CloseMessageWindow()

    #C0054
    ChrTalk(
        0xFE,
        (
            "……啊～可恶！\x01",
            "想起昨天\x01",
            "在『巴鲁卡』输掉的事了。\x02",
        )
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xFE,
        (
            "可恶，要尽快\x01",
            "赢回来才行啊。\x01",
            "还要再去找玛尔罗借钱吗……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1ADF")

    label("loc_1A94")


    #C0056
    ChrTalk(
        0xFE,
        "啊啊，怎么还不快点到周末啊。\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xFE,
        (
            "最近输多赢少，\x01",
            "得赶紧赢回来才行……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADF")

    Jump("loc_1B09")

    label("loc_1AE4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1AF2")
    Jump("loc_1B09")

    label("loc_1AF2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1B00")
    Jump("loc_1B09")

    label("loc_1B00")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1B09")

    label("loc_1B09")

    TalkEnd(0xFE)
    Return()

    # Function_7_18A8 end

    def Function_8_1B0D(): pass

    label("Function_8_1B0D")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C49")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BE0")

    #C0058
    ChrTalk(
        0xFE,
        (
            "哦，有魔兽出现了？\x01",
            "那是你们运气不好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0xFE,
        (
            "嗯，这种时候\x01",
            "偶尔也是会有的啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0xFE,
        (
            "反正也把书找到了，\x01",
            "总之，算是皆大欢喜吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x101,
        "#0006F（说得好像事不关己一样……）\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 4)
    Jump("loc_1C40")

    label("loc_1BE0")


    #C0062
    ChrTalk(
        0xFE,
        (
            "竟然会碰到魔兽，\x01",
            "你们的运气真不好啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xFE,
        (
            "哈，不过好在把书找到了，\x01",
            "总之，算是皆大欢喜吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1C40")

    TalkEnd(0xFE)
    Return()

    label("loc_1C49")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x6)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D09")

    #C0064
    ChrTalk(
        0xFE,
        (
            "我把书忘在\x01",
            "矿山里面了。\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0xFE,
        (
            "不好意思，我现在\x01",
            "工作很忙，实在抽不开身，\x01",
            "你们能不能自己过去拿啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0xFE,
        (
            "从那边的梯子下去，\x01",
            "就在坑道深处，\x01",
            "我想应该很容易找到。\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    label("loc_1D09")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x1)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x6)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1D26")
    Call(0, 13)
    TalkEnd(0xFE)
    Return()

    label("loc_1D26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC3, 6)), scpexpr(EXPR_END)), "loc_1DC3")

    #C0067
    ChrTalk(
        0xFE,
        (
            "冈兹～……\x01",
            "你快回来吧～……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xFE,
        (
            "话说回来，镇长都亲自去接他了，\x01",
            "却还是没有回来，这到底是怎么回事？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xFE,
        (
            "该不会是两个人\x01",
            "一起去游玩了吧……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F18")

    label("loc_1DC3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC2, 2)), scpexpr(EXPR_END)), "loc_1E43")

    #C0070
    ChrTalk(
        0xFE,
        (
            "嘿哟……\x01",
            "大概是因为以前总偷懒，\x01",
            "昨天一努力，肌肉就酸痛得厉害。\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0xFE,
        "可恶，只好努力工作，尽快适应这种痛感了！\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F18")

    label("loc_1E43")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 3)), scpexpr(EXPR_END)), "loc_1E51")
    Jump("loc_1F18")

    label("loc_1E51")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC1, 0)), scpexpr(EXPR_END)), "loc_1E9C")

    #C0072
    ChrTalk(
        0xFE,
        (
            "冈兹不在，\x01",
            "完全没法偷懒……\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0xFE,
        "他怎么还不快点回来啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1F18")

    label("loc_1E9C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_1ED7")

    #C0074
    ChrTalk(
        0xFE,
        (
            "因为人数太少，\x01",
            "都找不到偷懒的空闲啊……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F18")

    label("loc_1ED7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x82, 0)), scpexpr(EXPR_END)), "loc_1EE5")
    Jump("loc_1F18")

    label("loc_1EE5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x80, 0)), scpexpr(EXPR_END)), "loc_1EF3")
    Jump("loc_1F18")

    label("loc_1EF3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 5)), scpexpr(EXPR_END)), "loc_1F01")
    Jump("loc_1F18")

    label("loc_1F01")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x65, 4)), scpexpr(EXPR_END)), "loc_1F0F")
    Jump("loc_1F18")

    label("loc_1F0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x64, 1)), scpexpr(EXPR_END)), "loc_1F18")

    label("loc_1F18")

    TalkEnd(0xFE)
    Return()

    # Function_8_1B0D end

    def Function_9_1F1C(): pass

    label("Function_9_1F1C")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2009")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_1F9B")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_2004")

    label("loc_1F9B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0076
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2004")

    Jump("loc_2046")

    label("loc_2009")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0077
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

    label("loc_2046")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_1F1C end

    def Function_10_2052(): pass

    label("Function_10_2052")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_213F")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_20D1")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_213A")

    label("loc_20D1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0079
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1FB),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_213A")

    Jump("loc_217C")

    label("loc_213F")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0080
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

    label("loc_217C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_2052 end

    def Function_11_2188(): pass

    label("Function_11_2188")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2275")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E8, 1)"), scpexpr(EXPR_END)), "loc_2207")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_2270")

    label("loc_2207")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0082
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_2270")

    Jump("loc_22B2")

    label("loc_2275")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0083
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

    label("loc_22B2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_2188 end

    def Function_12_22BE(): pass

    label("Function_12_22BE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x114, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_23AB")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x65, 1)"), scpexpr(EXPR_END)), "loc_233D")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x114, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_23A6")

    label("loc_233D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0085
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x65),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x65),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_23A6")

    Jump("loc_23E8")

    label("loc_23AB")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0086
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

    label("loc_23E8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_22BE end

    def Function_13_23F4(): pass

    label("Function_13_23F4")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24A8")
    SetChrPos(0x109, -21300, 50, 19600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_24D3")

    label("loc_24A8")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_24D3")
    SetChrPos(0x10A, -21300, 50, 19600, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_24D3")

    OP_0D()

    #C0087
    ChrTalk(
        0x101,
        (
            "#6P#0000F那个……\x01",
            "您是矿工罗基先生吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0088
    ChrTalk(
        0xC,
        "#11P嗯？你们是什么人？\x02",
    )

    CloseMessageWindow()

    #C0089
    ChrTalk(
        0x101,
        (
            "#6P#0000F我们今天是接到图书馆的\x01",
            "委托而来的。\x02\x03",

            "罗基先生，您是不是借了\x01",
            "图书馆的书，然后就忘记还了？\x02",
        )
    )

    CloseMessageWindow()

    #C0090
    ChrTalk(
        0xC,
        "#11P……啊～原来是说那个啊。\x02",
    )

    CloseMessageWindow()

    #C0091
    ChrTalk(
        0xC,
        (
            "#11P嗯，的确是\x01",
            "借了还没还呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0092
    ChrTalk(
        0x103,
        (
            "#6P#0200F还书日期已经\x01",
            "过了很久了……\x01",
            "为什么还没还呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0093
    ChrTalk(
        0xC,
        (
            "#11P因为去克洛斯贝尔市\x01",
            "很麻烦啦。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_26B2")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_26B2")

    Sleep(1000)

    #C0094
    ChrTalk(
        0x104,
        "#6P#0306F（真直白啊……）\x02",
    )

    CloseMessageWindow()

    #C0095
    ChrTalk(
        0xC,
        (
            "#11P不过，你们肯上门来回收，\x01",
            "还真是求之不得。\x02",
        )
    )

    CloseMessageWindow()

    #C0096
    ChrTalk(
        0xC,
        (
            "#11P我刚才休息时\x01",
            "正好还在看呢……嗯？\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_64(0xC)

    #C0097
    ChrTalk(
        0x102,
        "#5P#0105F……您怎么了？\x02",
    )

    CloseMessageWindow()

    #C0098
    ChrTalk(
        0xC,
        (
            "#11P……我把书扔在矿山里面，\x01",
            "忘记拿出来了。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2820")
    OP_63(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)

    label("loc_2820")

    Sleep(1000)

    #C0099
    ChrTalk(
        0xC,
        (
            "#11P不好意思，我现在\x01",
            "工作很忙，实在抽不开身，\x01",
            "你们能不能自己过去拿啊？\x02",
        )
    )

    CloseMessageWindow()

    #C0100
    ChrTalk(
        0xC,
        (
            "#11P从那边的梯子下去，\x01",
            "就在坑道深处，\x01",
            "我想应该很容易找到。\x02",
        )
    )

    CloseMessageWindow()

    #C0101
    ChrTalk(
        0x103,
        (
            "#6P#0206F还真是个超级\x01",
            "怕麻烦的人呢……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_291B")

    #C0102
    ChrTalk(
        0x109,
        (
            "#12P#0503F和司令是不同类型的\x01",
            "懒惰……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2953")

    label("loc_291B")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2953")

    #C0103
    ChrTalk(
        0x10A,
        "#12P#0603F………………………………\x02",
    )

    CloseMessageWindow()

    label("loc_2953")


    #C0104
    ChrTalk(
        0x101,
        (
            "#6P#0006F嗯，没办法，\x01",
            "我们去拿吧。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 4)), scpexpr(EXPR_END)), "loc_29D3")

    #C0105
    ChrTalk(
        0xC,
        (
            "#11P啊，保险起见，我先告诉你们，\x01",
            "可不是左边深处的废矿哦。\x01",
            "注意点啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A34")

    label("loc_29D3")


    #C0106
    ChrTalk(
        0xC,
        (
            "#11P啊，可不是左边深处的废矿哦。虽然那边的门锁着，\x01",
            "应该不会搞错，不过以防万一还是提醒一下。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A34")


    #C0107
    ChrTalk(
        0x101,
        "#6P#0001F明、明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A74")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_2A74")

    SetChrPos(0x0, -20750, 50, 20860, 90)
    OP_93(0xC, 0x5A, 0x0)
    OP_66(0x5, 0x1)
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, 117500, -8750, -15770, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_29(0x28, 0x1, 0x6)
    EventEnd(0x5)
    Return()

    # Function_13_23F4 end

    def Function_14_2AE5(): pass

    label("Function_14_2AE5")

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
            "获得了。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B6F")
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    Jump("loc_2B85")

    label("loc_2B6F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2B85")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_2B85")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C45")
    SetChrPos(0x109, 115020, -8950, -16730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    Jump("loc_2C70")

    label("loc_2C45")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2C70")
    SetChrPos(0x10A, 115020, -8950, -16730, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_2C70")

    OP_0D()

    #C0109
    ChrTalk(
        0x101,
        "#5P#0000F找到了……是这本吧。\x02",
    )

    CloseMessageWindow()

    #C0110
    ChrTalk(
        0x102,
        "#5P#0105F这书名还真是煞有介事呢……\x02",
    )

    CloseMessageWindow()

    #C0111
    ChrTalk(
        0x103,
        (
            "#11P#0200F这本书写的都是发生在克洛斯贝尔\x01",
            "各地的怪异现象吧。\x02\x03",

            "#0203F是否如副标题所说，是真实\x01",
            "存在的事件，似乎还未可知。\x02",
        )
    )

    CloseMessageWindow()

    #C0112
    ChrTalk(
        0x104,
        (
            "#12P#0300F不过，\x01",
            "感觉还真是完全为了\x01",
            "消磨时间而借的书啊。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2DE8")

    #C0113
    ChrTalk(
        0x109,
        (
            "#6P#0500F我记得里面好像还写着\x01",
            "警备队的什么经历……\x02\x03",

            "但在正式记录中并没有\x01",
            "那么恐怖的事件呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DE8")


    #C0114
    ChrTalk(
        0x102,
        "#5P#0103F（无论如何都绝对不想看呢……）\x02",
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            "#5P#0000F嗯，不管怎么说，\x01",
            "已经顺利拿回了图书。\x01",
            "接下来──\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2E9F")
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0116
    ChrTalk(
        0x10A,
        "#6P#0605F唔……！？\x02",
    )

    CloseMessageWindow()
    OP_93(0x10A, 0x13B, 0x1F4)

    label("loc_2E9F")

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

    def lambda_2F33():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2F33)

    def lambda_2F40():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F40)

    def lambda_2F4D():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2F4D)

    def lambda_2F5A():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2F5A)
    OP_68(115510, -8000, -13560, 4000)
    MoveCamera(16, 17, 0, 4000)
    OP_6E(440, 4000)
    SetCameraDistance(20790, 4000)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2FC5")
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)

    def lambda_2FBD():
        OP_93(0xFE, 0x13B, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_2FBD)

    label("loc_2FC5")

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
        "#12P#0005F魔、魔兽！？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        "#12P#0301F嘁，去路被堵住了啊。\x02",
    )

    CloseMessageWindow()

    #C0119
    ChrTalk(
        0x103,
        "#12P#0201F……来了！\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_308E")
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_30A6")

    label("loc_308E")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_30A6")
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)

    label("loc_30A6")

    OP_0D()
    Battle("BattleInfo_52C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 15)
    Return()

    # Function_14_2AE5 end

    def Function_15_30C5(): pass

    label("Function_15_30C5")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3127")
    LoadChrToIndex("chr/ch00850.itc", 0x22)
    Jump("loc_313D")

    label("loc_3127")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_313D")
    LoadChrToIndex("chr/ch00950.itc", 0x22)

    label("loc_313D")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3207")
    SetChrPos(0x109, 115020, -8950, -16730, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x109, 0x22)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_323A")

    label("loc_3207")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_323A")
    SetChrPos(0x10A, 115020, -8950, -16730, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)

    label("loc_323A")

    FadeToBright(1000, 0)
    OP_0D()

    #C0120
    ChrTalk(
        0x101,
        "#11P#0006F呼……吓了一跳。\x02",
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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32B2")
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Jump("loc_32CA")

    label("loc_32B2")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_32CA")
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)

    label("loc_32CA")

    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_331C")

    #C0121
    ChrTalk(
        0x10A,
        "#6P#0603F真是的，不可大意！\x02",
    )

    CloseMessageWindow()

    #C0122
    ChrTalk(
        0x101,
        "#11P#0012F哈哈，对不起……\x02",
    )

    CloseMessageWindow()

    label("loc_331C")


    #C0123
    ChrTalk(
        0x104,
        (
            "#12P#0300F哈，但根本不是\x01",
            "我们的对手嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x103,
        (
            "#12P#0200F路上也有不少魔兽在徘徊，\x01",
            "我们似乎是刚好赶上了\x01",
            "魔兽狂暴的时刻。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x102,
        (
            "#11P#0100F还好没有\x01",
            "损毁图书啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x101,
        "#12P#0000F好，那我们走吧。\x02",
    )

    CloseMessageWindow()
    OP_29(0x28, 0x1, 0x7)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x5)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0x7)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x28, 0x1, 0xA)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3405")
    OP_29(0x28, 0x1, 0x1F)

    label("loc_3405")

    SetChrPos(0x0, 115910, -8950, -14740, 315)
    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3431")
    OP_D5(0x22)
    Jump("loc_3443")

    label("loc_3431")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3443")
    OP_D5(0x22)

    label("loc_3443")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_3462")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    Jump("loc_347C")

    label("loc_3462")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_347C")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_347C")

    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    ClearMapFlags(0x8000000)
    OP_37()
    EventEnd(0x5)
    Return()

    # Function_15_30C5 end

    def Function_16_348E(): pass

    label("Function_16_348E")


    def lambda_3493():
        OP_98(0xFE, 0xFA0, 0x0, 0xFFFFF830, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3493)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_16_348E end

    def Function_17_34AD(): pass

    label("Function_17_34AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x1)"), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBF, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_356C")
    TalkBegin(0xFF)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "【使用废坑的钥匙】\x01",      # 0
            "【放弃】\x01",                # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3564")
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
            "打开了废矿大门的锁。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3553")
    OP_29(0x1C, 0x1, 0x2)

    label("loc_3553")

    SetScenarioFlags(0xBF, 4)
    SetMapObjFlags(0x15, 0x10)
    SetBarrier(0x2, 0x0, 0x1)
    OP_65(0x4, 0x1)

    label("loc_3564")

    TalkEnd(0xFF)
    Jump("loc_35A6")

    label("loc_356C")

    TalkBegin(0xFF)
    Sound(810, 0, 100, 0)
    SetChrName("")

    #A0128
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "门被紧紧锁住了。\x01",
            "里面好像是废坑。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)

    label("loc_35A6")

    Return()

    # Function_17_34AD end

    SaveToFile()

Try(main)
