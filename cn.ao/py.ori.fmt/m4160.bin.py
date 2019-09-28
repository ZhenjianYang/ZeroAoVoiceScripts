from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4160.bin",                # FileName
        "m4160",                    # MapName
        "m4160",                    # Location
        0x00C9,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x28,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 201, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4160",                  # 0
        "剧情用魔兽",             # 1
        "剧情用魔兽",             # 2
        "苍蓝毒蜘蛛",             # 3
        "妖虫兽",                 # 4
        "SE控制",                 # 5
        "bm4150",                 # 6
        "bm4150",                 # 7
        "bm4150",                 # 8
        "bm4160",                 # 9
        "bm4160",                 # 10
        "bm4160",                 # 11
    ))

    ATBonus("ATBonus_340", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_360", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_2541", 6,   6,   8,   8,   8,   6,   6)
    Sepith("Sepith_2531", 4,   4,   6,   6,   4,   6,   6)
    Sepith("Sepith_2539", 12,  12,  4,   4,   4,   2,   2)

    MonsterBattlePostion("MonsterBattlePostion_380", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_404", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_408", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_40C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_410", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_414", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_418", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_41C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 8, 14, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_558", 0x0000, 72, 6, 60, 10, 1, 30, 0, "bm4150", "Sepith_2541", 50, 50, 0, 0,
        (
            ("ms82500.dat", "ms82500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms82500.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_420", 0x0000, 72, 6, 60, 10, 1, 40, 0, "bm4150", "Sepith_2531", 40, 30, 20, 0,
        (
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", "ms86900.dat", 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4BC", 0x0000, 72, 6, 60, 10, 1, 20, 0, "bm4150", "Sepith_2539", 40, 30, 20, 0,
        (
            ("ms83700.dat", "ms83700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms83700.dat", "ms83700.dat", "ms83700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3A0", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            ("ms83700.dat", "ms83700.dat", "ms83700.dat", "ms83700.dat", 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7450", "ed7453", "ATBonus_340"),
            (),
        )
    )

    # event battle count: 4

    BattleInfo(
        "BattleInfo_60C", 0x0000, 85, 6, 0, 0, 1, 0, 0, "bm4160", 0x00000000, 100, 0, 0, 0,
        (
            ("ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "ms68600.dat", "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7451", "ed7453", "ATBonus_360"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_650", 0x0000, 50, 6, 45, 0, 1, 0, 0, "bm4160", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82500.dat", "ms82500.dat", "ms82500.dat", "ms82500.dat", 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7451", "ed7453", "ATBonus_340"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5C8", 0x0002, 3, 6, 45, 3, 3, 30, 0, "bm4160", 0x00000000, 100, 0, 0, 0,
        (
            ("ms82000.dat", "ms82000.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_380", "MonsterBattlePostion_400", "ed7453", "ed7453", "ATBonus_340"),
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
        "monster/ch86950.itc",               # 10
        "monster/ch86951.itc",               # 11
        "monster/ch83750.itc",               # 12
        "monster/ch83751.itc",               # 13
        "monster/ch82550.itc",               # 14
        "monster/ch82551.itc",               # 15
        "monster/ch68650.itc",               # 16
        "monster/ch68651.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-28319,  4500,    603030,  180,  484,  0x0, 0,   22,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(-8000,   500,     2500,    0,    484,  0x0, 0,   20,  0,   0,   1,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(5340,    2500,    0,       0x1010107,    "BattleInfo_558", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-850,    29010,   0,       0x10100C6,    "BattleInfo_420", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(3410,    50790,   0,       0x10100E1,    "BattleInfo_4BC", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 8,   0.0,                   290.0,                 -1.0,                  144.0,                 [0.125,                -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000001788139343,   0.0,                   -0.0,                  -96.66667175292969,    0.20000001788139343,   1.0])
    DeclEvent(0x0000, 0, 11,  2.0199999809265137,    611.0,                 3.0,                   225.0,                 [0.3333333432674408,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.10000000149011612,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.6733333468437195,   -61.10000228881836,    -0.6000000238418579,   1.0])

    DeclActor(-28320,  4000,    603030,  1200,    -28320,  5000,    603030,  0x007C, 0,  4,  0x0000)
    DeclActor(-8000,   0,       2500,    1200,    -8000,   1000,    2500,    0x007C, 0,  5,  0x0000)
    DeclActor(7250,    0,       52500,   1200,    7250,    1000,    52500,   0x007C, 0,  6,  0x0000)
    DeclActor(-28310,  4000,    619750,  1200,    -28310,  4000,    619750,  0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_710",          # 00, 0
        "Function_1_72F",          # 01, 1
        "Function_2_74B",          # 02, 2
        "Function_3_75B",          # 03, 3
        "Function_4_C98",          # 04, 4
        "Function_5_F25",          # 05, 5
        "Function_6_1330",         # 06, 6
        "Function_7_146B",         # 07, 7
        "Function_8_14EE",         # 08, 8
        "Function_9_1AF6",         # 09, 9
        "Function_10_1B24",        # 0A, 10
        "Function_11_200D",        # 0B, 11
        "Function_12_249A",        # 0C, 12
    ))


    def Function_0_710(): pass

    label("Function_0_710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_72E")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_710")

    label("loc_72E")

    Return()

    # Function_0_710 end

    def Function_1_72F(): pass

    label("Function_1_72F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74A")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_1_72F")

    label("loc_74A")

    Return()

    # Function_1_72F end

    def Function_2_74B(): pass

    label("Function_2_74B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_75A")
    ClearScenarioFlags(0x22, 0)
    Event(0, 10)

    label("loc_75A")

    Return()

    # Function_2_74B end

    def Function_3_75B(): pass

    label("Function_3_75B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_792")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x12D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_79B")

    label("loc_792")

    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_79B")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 5)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7B3")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_7B3")

    ModifyEventFlags(0, 1, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7CB")
    ModifyEventFlags(1, 1, 0x80)

    label("loc_7CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7DE")
    OP_1B(0x5, 0x0, 0xC)

    label("loc_7DE")

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
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF3")
    OP_70(0x0, 0x0)
    Jump("loc_AF7")

    label("loc_AF3")

    OP_70(0x0, 0x1E)

    label("loc_AF7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B0A")
    OP_70(0x1, 0x0)
    Jump("loc_B0E")

    label("loc_B0A")

    OP_70(0x1, 0x1E)

    label("loc_B0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B21")
    OP_70(0x2, 0x0)
    Jump("loc_B25")

    label("loc_B21")

    OP_70(0x2, 0x1E)

    label("loc_B25")

    LoadEffect(0x9, "map/mpcave2.eff")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BA9")
    PlayEffect(0x9, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_E6(0x0, 0x7, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    OP_11(0x0, 0x0, 0x0, 0x19, 0x28, 0x0)

    label("loc_BA9")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -4380, 4140, 611170, 8000, 5000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_END)), "loc_BE6")
    SetMapObjFrame(0xFF, "gate00", 0x0, 0x1)
    SetBarrier(0x2, 0x0, 0x1)
    Jump("loc_BF4")

    label("loc_BE6")

    SetMapObjFrame(0xFF, "gate00", 0x1, 0x1)

    label("loc_BF4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_C22")
    SetMapObjFrame(0xFF, "hasigo_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasigo_b", 0x1, 0x1)
    Jump("loc_C42")

    label("loc_C22")

    SetMapObjFrame(0xFF, "hasigo_a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasigo_b", 0x0, 0x1)

    label("loc_C42")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x180, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C54")
    OP_65(0x3, 0x1)

    label("loc_C54")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x166, 7)), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_C97")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_C91")
    Sound(120, 1, 80, 0)
    Jump("loc_C97")

    label("loc_C91")

    Sound(120, 1, 50, 0)

    label("loc_C97")

    Return()

    # Function_3_75B end

    def Function_4_C98(): pass

    label("Function_4_C98")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D27")
    TalkBegin(0xFF)
    SetMapFlags(0x8000000)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "从宝箱中感觉到了强大魔兽的气息。\x01",
            "【推测魔兽等级８５】\x01",
            "要打开宝箱吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D27")
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Return()

    label("loc_D27")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FB, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE7")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E24")
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xA, 0x0, 0)
    OP_98(0xA, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D84():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_D84)

    def lambda_D9E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_D9E)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x8000)

    #A0002
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
    Battle("BattleInfo_60C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xA, 0x80)
    ClearChrFlags(0xA, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E05"),
        (2, "loc_E14"),
        (1, "loc_E21"),
        (SWITCH_DEFAULT, "loc_E24"),
    )


    label("loc_E05")

    SetScenarioFlags(0x214, 3)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_E24")

    label("loc_E14")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_E21")

    OP_B9(0x0)
    Return()

    label("loc_E24")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('岁星铃', 1)"), scpexpr(EXPR_END)), "loc_E7B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FB, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_EE2")

    label("loc_E7B")

    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xA8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xA8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EE2")

    Jump("loc_F19")

    label("loc_EE7")

    FadeToDark(300, 0, 100)

    #A0005
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

    label("loc_F19")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C98 end

    def Function_5_F25(): pass

    label("Function_5_F25")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber('无限', 0x4)"), scpexpr(EXPR_END)), "loc_1132")
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F0")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_102D")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_F8D():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_F8D)

    def lambda_FA7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_FA7)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_650", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_100E"),
        (2, "loc_101D"),
        (1, "loc_102A"),
        (SWITCH_DEFAULT, "loc_102D"),
    )


    label("loc_100E")

    SetScenarioFlags(0x21B, 7)
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

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('光耀珠', 1)"), scpexpr(EXPR_END)), "loc_1084")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_10EB")

    label("loc_1084")

    FadeToDark(300, 0, 100)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x7F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10EB")

    Jump("loc_1122")

    label("loc_10F0")

    FadeToDark(300, 0, 100)

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

    label("loc_1122")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Jump("loc_132F")

    label("loc_1132")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12F2")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_122F")
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xB, 0x0, 0)
    OP_98(0xB, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_118F():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_118F)

    def lambda_11A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_11A9)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)

    #A0010
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xB, 1)
    Battle("BattleInfo_650", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xB, 0x80)
    ClearChrFlags(0xB, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1210"),
        (2, "loc_121F"),
        (1, "loc_122C"),
        (SWITCH_DEFAULT, "loc_122F"),
    )


    label("loc_1210")

    SetScenarioFlags(0x21B, 7)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_122F")

    label("loc_121F")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_122C")

    OP_B9(0x0)
    Return()

    label("loc_122F")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('无限', 1)"), scpexpr(EXPR_END)), "loc_1286")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xE9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_12ED")

    label("loc_1286")

    FadeToDark(300, 0, 100)

    #A0012
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xE9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0xE9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_12ED")

    Jump("loc_1324")

    label("loc_12F2")

    FadeToDark(300, 0, 100)

    #A0013
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

    label("loc_1324")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)

    label("loc_132F")

    Return()

    # Function_5_F25 end

    def Function_6_1330(): pass

    label("Function_6_1330")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1422")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('全回复药', 1)"), scpexpr(EXPR_END)), "loc_13B3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F1, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_141D")

    label("loc_13B3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1F7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_141D")

    Jump("loc_145F")

    label("loc_1422")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0016
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

    label("loc_145F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1330 end

    def Function_7_146B(): pass

    label("Function_7_146B")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_14D2")

    #A0017
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有梯子。\x01",
            "要下去吗？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14CD")
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("m4120", 112, 0, 0)
    IdleLoop()

    label("loc_14CD")

    Jump("loc_14EB")

    label("loc_14D2")


    #A0018
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "是坏掉的梯子。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_14EB")

    EventEnd(0x5)
    Return()

    # Function_7_146B end

    def Function_8_14EE(): pass

    label("Function_8_14EE")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("chr/ch00050.itc", 0x20)
    LoadChrToIndex("chr/ch00150.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch02950.itc", 0x23)
    LoadChrToIndex("chr/ch03050.itc", 0x24)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x6)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x6)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x101, 0, 0, 293000, 0)
    SetChrPos(0x102, -1250, 0, 292500, 0)
    SetChrPos(0x103, 750, 0, 292000, 0)
    SetChrPos(0x109, -750, 0, 291250, 0)
    SetChrPos(0x105, 0, 0, 290500, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrPos(0x8, 0, 7000, 289000, 0)
    SetChrPos(0x9, 0, 7000, 305000, 180)

    def lambda_1626():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1626)
    Sleep(50)

    def lambda_163E():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_163E)
    Sleep(50)

    def lambda_1656():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1656)
    Sleep(50)

    def lambda_166E():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_166E)
    Sleep(50)

    def lambda_1686():
        OP_9B(0x0, 0xFE, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1686)
    OP_68(0, 800, 292000, 0)
    MoveCamera(45, 30, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    OP_68(0, 800, 296000, 3000)
    SetCameraDistance(20000, 3000)
    FadeToBright(1000, 0)
    OP_0D()
    Sound(948, 0, 30, 0)
    Sound(911, 0, 70, 0)
    Sleep(300)
    WaitChrThread(0x101, 1)
    OP_63(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(50)
    OP_63(0x109, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    OP_63(0x105, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    Sound(29, 0, 100, 0)
    Sleep(1000)
    StopBGM(0xBB8)
    OP_6F(0x79)

    #C0019
    ChrTalk(
        0x101,
        "#00005F#11P……？\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x109,
        "#10108F#12P上面……？\x02",
    )

    CloseMessageWindow()
    OP_68(0, 800, 296000, 8000)
    MoveCamera(64, 23, 0, 8000)
    OP_6E(600, 8000)
    SetCameraDistance(18050, 8000)
    Sound(844, 0, 50, 0)
    Sound(809, 0, 60, 0)

    def lambda_17F4():
        OP_9D(0xFE, 0x0, 0x0, 0x493E0, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_17F4)
    Sleep(300)

    def lambda_1814():
        OP_9D(0xFE, 0x0, 0x0, 0x474A0, 0x1F4, 0x1770)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1814)
    WaitChrThread(0x9, 1)
    Sound(845, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x1E)
    BeginChrThread(0x9, 3, 0, 9)
    WaitChrThread(0x8, 1)
    Sound(845, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1E)
    BeginChrThread(0x8, 3, 0, 9)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7453", 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_18E2():
        OP_92(0x109, 0x0, 0x474A0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_18E2)
    Sleep(50)

    def lambda_18F8():
        OP_92(0x105, 0x0, 0x474A0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_18F8)
    Sleep(50)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x20)
    SetChrChipByIndex(0x102, 0x21)
    SetChrChipByIndex(0x103, 0x22)
    SetChrChipByIndex(0x109, 0x23)
    SetChrChipByIndex(0x105, 0x24)
    SetChrSubChip(0x101, 0x0)
    SetChrSubChip(0x102, 0x0)
    SetChrSubChip(0x103, 0x0)
    SetChrSubChip(0x109, 0x0)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_199E")

    #C0021
    ChrTalk(
        0x101,
        "#00007F#11P什么……！\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#00101F#11P是那时曾经见过的……！\x02",
    )

    CloseMessageWindow()
    Jump("loc_19E8")

    label("loc_199E")


    #C0023
    ChrTalk(
        0x101,
        "#00010F#11P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x103,
        "#00201F#11P似乎与普通的魔兽有所不同……\x02",
    )

    CloseMessageWindow()

    label("loc_19E8")


    #C0025
    ChrTalk(
        0x105,
        "#10307F#5P我们被夹击了……它们过来了！\x02",
    )

    CloseMessageWindow()
    EndChrThread(0x9, 0x3)
    EndChrThread(0x8, 0x3)
    Sound(809, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x1F)
    SetChrSubChip(0x8, 0x6)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x6)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1A63():
        OP_9D(0xFE, 0x0, 0x320, 0x48440, 0x320, 0x1F4)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1A63)

    def lambda_1A80():
        OP_9D(0xFE, 0x0, 0x320, 0x48440, 0x320, 0x1F4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1A80)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    OP_68(0, 600, 296000, 200)
    SetCameraDistance(18000, 200)
    Sleep(200)
    CancelBlur(200)
    Battle("BattleInfo_5C8", 0x30200011, 0x1, 0x0, 0x26, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Call(0, 10)
    Return()

    # Function_8_14EE end

    def Function_9_1AF6(): pass

    label("Function_9_1AF6")

    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B0C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1B23")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_1B0C")

    label("loc_1B23")

    Return()

    # Function_9_1AF6 end

    def Function_10_1B24(): pass

    label("Function_10_1B24")

    EventBegin(0x0)
    OP_E2(0x3)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch03050.itc", 0x22)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0x22)
    SetChrSubChip(0x105, 0x0)
    SetChrPos(0x101, 0, 0, 297000, 0)
    SetChrPos(0x102, -1250, 0, 296500, 0)
    SetChrPos(0x103, 750, 0, 296000, 0)
    SetChrPos(0x109, -1000, 0, 295250, 180)
    SetChrPos(0x105, 0, 0, 294500, 180)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(230, 800, 296330, 0)
    MoveCamera(41, 26, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16800, 0)
    SetCameraDistance(17800, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    Fade(250)
    Sound(805, 0, 100, 0)
    Sound(531, 0, 100, 0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    OP_0D()
    Sleep(300)

    def lambda_1C5A():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C5A)

    def lambda_1C67():
        TurnDirection(0x102, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1C67)
    Sleep(50)

    def lambda_1C77():
        TurnDirection(0x103, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1C77)
    Sleep(50)

    def lambda_1C87():
        TurnDirection(0x109, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1C87)
    Sleep(50)

    def lambda_1C97():
        TurnDirection(0x105, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1C97)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)
    OP_6F(0x79)

    #C0026
    ChrTalk(
        0x101,
        (
            "#00006F#5P啧……真是强得可怕啊。\x02\x03",

            "#00013F看样子，与当时的军犬有些相似，\x01",
            "是经受过训练的魔兽……\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        (
            "#00106F#6P嗯，不过并非犬科，\x01",
            "好像是猫科的魔兽……\x02\x03",

            "#00108F是『赤色星座』驯养的吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x109,
        (
            "#10106F#6P多半如此……\x01",
            "我听说猎兵团驯养\x01",
            "军用魔兽是很普遍的。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x105,
        (
            "#10306F#12P它们的实力远不是\x01",
            "黑手党的军犬可以相比的。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x103,
        (
            "#00211F#11P嗯……而且竟然还\x01",
            "懂得两面夹击。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x87, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1F4F")

    #C0031
    ChrTalk(
        0x102,
        (
            "#00103F#6P说起来，那个名叫敏涅斯的男人\x01",
            "也曾放出过刚才那种魔兽……\x02\x03",

            "#00101F也许他和『赤色星座』\x01",
            "存在着什么关联。\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0x101,
        (
            "#00006F#5P嗯，可能是专门为猎兵团\x01",
            "服务的商人，或者是负责周转资金的人吧。\x02\x03",

            "#00003F总之，\x01",
            "我们总算把那些魔兽击退了。\x02\x03",

            "#00013F离出口好像也已经不远了，\x01",
            "我们抓紧时间吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FB2")

    label("loc_1F4F")


    #C0033
    ChrTalk(
        0x101,
        (
            "#00003F#5P总之，\x01",
            "我们总算把那些魔兽击退了。\x02\x03",

            "#00013F离出口好像也已经不远了，\x01",
            "我们抓紧时间吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1FB2")


    #C0034
    ChrTalk(
        0x109,
        "#10101F#6P是……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_D7(0x20)
    OP_D7(0x21)
    OP_D7(0x22)
    OP_37()
    SetChrPos(0x0, 0, 0, 297000, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 6)
    ModifyEventFlags(0, 0, 0x80)
    ModifyEventFlags(1, 1, 0x80)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_1B24 end

    def Function_11_200D(): pass

    label("Function_11_200D")

    EventBegin(0x0)
    OP_E2(0x3)
    OP_63(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_68(-3750, 6800, 611400, 2000)
    MoveCamera(50, 20, 0, 2000)
    OP_6E(600, 2000)
    SetCameraDistance(18650, 2000)

    def lambda_205F():
        OP_93(0x0, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x0, 0, lambda_205F)
    Sleep(50)

    def lambda_206F():
        OP_93(0x1, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x1, 0, lambda_206F)
    Sleep(50)

    def lambda_207F():
        OP_93(0x2, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x2, 0, lambda_207F)
    Sleep(50)

    def lambda_208F():
        OP_93(0x3, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x3, 0, lambda_208F)
    Sleep(50)
    WaitChrThread(0x0, 0)
    WaitChrThread(0x1, 0)
    WaitChrThread(0x2, 0)
    WaitChrThread(0x3, 0)
    OP_6F(0x79)
    Sleep(500)
    Fade(500)
    OP_68(-28450, 4500, 619250, 0)
    MoveCamera(25, 25, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(20000, 0)
    OP_68(-15450, 8000, 617750, 5000)
    MoveCamera(45, 0, 0, 5000)
    OP_6E(600, 5000)
    SetCameraDistance(22000, 5000)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(1000, 5000, 611000, 0)
    MoveCamera(35, 20, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, -500, 4000, 611000, 270)
    SetChrPos(0x102, 750, 4000, 610500, 270)
    SetChrPos(0x103, 1000, 4000, 611950, 270)
    SetChrPos(0x109, 2000, 4000, 610900, 270)
    SetChrPos(0x105, 2500, 4000, 612750, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_0D()

    #C0035
    ChrTalk(
        0x101,
        (
            "#00002F#11P这里是……\x01",
            "旧矿山的入口附近！\x02",
        )
    )

    CloseMessageWindow()

    #C0036
    ChrTalk(
        0x102,
        (
            "#00106F#11P太好了……\x01",
            "顺利抵达了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x109,
        (
            "#10108F#11P不过……\x01",
            "兰迪前辈在哪里呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x105,
        (
            "#10301F#11P如果他还没动手，\x01",
            "我们应该来得及与他会合……\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0x7D0)
    OP_82(0x64, 0x0, 0xBB8, 0x3E8)
    Sound(196, 0, 30, 0)
    Sound(833, 0, 40, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7586", 0)
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x24A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ReplaceBGM("ed7301", "ed7586")
    ReplaceBGM("ed7351", "ed7586")

    #C0039
    ChrTalk(
        0x103,
        (
            "#00205F#11P从外面传来了爆炸声……！\x02\x03",

            "#00207F而且还听到了枪击的声音！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x102,
        "#00107F#11P兰迪……！\x02",
    )

    CloseMessageWindow()
    OP_93(0x101, 0x5A, 0x2EE)

    def lambda_23A2():
        TurnDirection(0x102, 0x101, 750)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23A2)
    Sleep(50)

    def lambda_23B2():
        TurnDirection(0x103, 0x101, 750)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_23B2)
    Sleep(50)

    def lambda_23C2():
        TurnDirection(0x109, 0x101, 750)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_23C2)
    Sleep(50)

    def lambda_23D2():
        TurnDirection(0x105, 0x101, 750)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_23D2)
    Sleep(50)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x109, 0)
    WaitChrThread(0x105, 0)

    #C0041
    ChrTalk(
        0x101,
        "#00010F#6P啧，我们也出去吧！\x02",
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x109,
        "#10107F#11P是！队长！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x105,
        "#10308F#11P（……不知是否还来得及。）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SoundLoad(120)
    Sound(120, 2, 80, 0)
    SetChrPos(0x0, -500, 4000, 611000, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0x166, 7)
    ModifyEventFlags(0, 1, 0x80)
    OP_1B(0x5, 0x0, 0xC)
    OP_65(0x3, 0x1)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_11_200D end

    def Function_12_249A(): pass

    label("Function_12_249A")

    EventBegin(0x1)

    #C0044
    ChrTalk(
        0x101,
        (
            "#00001F已经没时间了——\x01",
            "赶快从出口出去吧！\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()
    SetChrPos(0x0, 12800, 0, 573040, 0)
    EventEnd(0x4)
    Return()

    # Function_12_249A end

    SaveToFile()

Try(main)
