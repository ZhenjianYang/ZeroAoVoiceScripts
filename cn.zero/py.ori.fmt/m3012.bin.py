from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m3012.bin",                # FileName
        "m3012",                    # MapName
        "m3012",                    # Location
        0x007C,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 124, 0, 2, 0, 3],
    )

    BuildStringList((
        "m3012",                  # 0
        "黑手党",                 # 1
        "黑手党",                 # 2
        "魔人·黑手党成员",       # 3
        "魔人·黑手党成员",       # 4
        "地狱犬",                 # 5
        "bm3010",                 # 6
        "bm3010",                 # 7
        "bm3010",                 # 8
    ))

    ATBonus("ATBonus_290", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_2B0", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_3CBC", 9,   12,  6,   16,  2,   13,  4)

    MonsterBattlePostion("MonsterBattlePostion_2D0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_354", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_358", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_35C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_360", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_364", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_368", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_390", 0x0000, 38, 6, 60, 4, 1, 40, 0, "bm3010", "Sepith_3CBC", 60, 25, 10, 5,
        (
            ("ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_350", "ed7402", "ed7403", "ATBonus_290"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F0", "MonsterBattlePostion_350", "ed7402", "ed7403", "ATBonus_290"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_350", "ed7402", "ed7403", "ATBonus_290"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, "MonsterBattlePostion_2F0", "MonsterBattlePostion_350", "ed7402", "ed7403", "ATBonus_290"),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_458", 0x0010, 38, 6, 60, 0, 1, 0, 0, "bm3010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67200.dat", "ms67200.dat", "ms67200.dat", "ms67200.dat", 0, 0, "ms72100.dat", 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_350", "ed7402", "ed7403", "ATBonus_290"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_49C", 0x0040, 38, 6, 45, 0, 1, 0, 0, "bm3010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67300.dat", "ms67300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_370", "MonsterBattlePostion_350", "ed7405", "ed7000", "ATBonus_2B0"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "apl/ch50362.itc",                   # 00
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
        "monster/ch67250.itc",               # 10
        "monster/ch67251.itc",               # 11
        "monster/ch72150.itc",               # 12
        "monster/ch72151.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    389,  0x0, 0,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    389,  0x0, 1,   0,   0,   255, 255, 0,   6,   255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-111000, -23000,  5500,    0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-236920, -4059,   -24000,  0x1010000,    "BattleInfo_390", 0,   18,  0xFFFF, 0,  1)

    DeclEvent(0x0000, 0, 7,   0.0,                   22.0,                  -25.0,                 225.0,                 [0.10000000149011612,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333432674408,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -7.333333492279053,    5.0,                   1.0])

    DeclActor(-108700, -24000,  0,       1500,    -108700, -23000,  0,       0x007C, 0,  10, 0x0000)
    DeclActor(8000,    -24000,  -118400, 1500,    8000,    -23000,  -118400, 0x007C, 0,  11, 0x0000)
    DeclActor(-111000, -24000,  5500,    1200,    -111000, -24000,  5500,    0x007C, 0,  4,  0x0000)
    DeclActor(6250,    -24000,  -108250, 1200,    6250,    -24000,  -108250, 0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1

    ScpFunction((
        "Function_0_52C",          # 00, 0
        "Function_1_54B",          # 01, 1
        "Function_2_56A",          # 02, 2
        "Function_3_5F6",          # 03, 3
        "Function_4_865",          # 04, 4
        "Function_5_A5F",          # 05, 5
        "Function_6_B95",          # 06, 6
        "Function_7_BC1",          # 07, 7
        "Function_8_18D7",         # 08, 8
        "Function_9_193B",         # 09, 9
        "Function_10_249F",        # 0A, 10
        "Function_11_3072",        # 0B, 11
        "Function_12_3AE0",        # 0C, 12
    ))


    def Function_0_52C(): pass

    label("Function_0_52C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54A")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_52C")

    label("loc_54A")

    Return()

    # Function_0_52C end

    def Function_1_54B(): pass

    label("Function_1_54B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_569")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_54B")

    label("loc_569")

    Return()

    # Function_1_54B end

    def Function_2_56A(): pass

    label("Function_2_56A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 0)), scpexpr(EXPR_END)), "loc_5F5")
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 3600, -24000, 31500, 135)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 3800, -24000, 29600, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)

    label("loc_5F5")

    Return()

    # Function_2_56A end

    def Function_3_5F6(): pass

    label("Function_3_5F6")

    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE4, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60E")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_60E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 5)), scpexpr(EXPR_END)), "loc_623")
    OP_71(0x7, 0x96, 0xD2, 0x0, 0x20)

    label("loc_623")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 6)), scpexpr(EXPR_END)), "loc_638")
    OP_71(0x6, 0x96, 0xD2, 0x0, 0x20)

    label("loc_638")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_659")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_659")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_670")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_670")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_687")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_687")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6B9")
    OP_70(0x3, 0x5A)
    OP_70(0x4, 0x5A)
    OP_70(0x5, 0x5A)
    ClearMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jump("loc_73B")

    label("loc_6B9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6EB")
    OP_70(0x3, 0x14)
    OP_70(0x4, 0x14)
    OP_70(0x5, 0x14)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_73B")

    label("loc_6EB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_71D")
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0xA)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_73B")

    label("loc_71D")

    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    OP_70(0x5, 0x0)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)

    label("loc_73B")

    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 0)), scpexpr(EXPR_END)), "loc_836")
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_849")
    OP_70(0x1, 0x0)
    Jump("loc_84D")

    label("loc_849")

    OP_70(0x1, 0x1E)

    label("loc_84D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_860")
    OP_70(0x2, 0x0)
    Jump("loc_864")

    label("loc_860")

    OP_70(0x2, 0x1E)

    label("loc_864")

    Return()

    # Function_3_5F6 end

    def Function_4_865(): pass

    label("Function_4_865")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A21")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_95E")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_8BE():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_8BE)

    def lambda_8D8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_8D8)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_458", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_93F"),
        (2, "loc_94E"),
        (1, "loc_95B"),
        (SWITCH_DEFAULT, "loc_95E"),
    )


    label("loc_93F")

    SetScenarioFlags(0x76, 4)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_95E")

    label("loc_94E")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_95B")

    OP_B7(0x0)
    Return()

    label("loc_95E")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x652, 1)"), scpexpr(EXPR_END)), "loc_9B5")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x652),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11F, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_A1C")

    label("loc_9B5")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x652),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x652),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A1C")

    Jump("loc_A53")

    label("loc_A21")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_A53")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_865 end

    def Function_5_A5F(): pass

    label("Function_5_A5F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B4C")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_ADE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x108, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_B47")

    label("loc_ADE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B47")

    Jump("loc_B89")

    label("loc_B4C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_B89")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A5F end

    def Function_6_B95(): pass

    label("Function_6_B95")

    TalkBegin(0xFE)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "黑手党成员失去了意识。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_6_B95 end

    def Function_7_BC1(): pass

    label("Function_7_BC1")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("chr/ch36000.itc", 0x24)
    LoadChrToIndex("chr/ch36100.itc", 0x25)
    LoadChrToIndex("monster/ch67350.itc", 0x26)
    LoadChrToIndex("monster/ch67352.itc", 0x27)
    LoadChrToIndex("monster/ch67353.itc", 0x28)
    LoadChrToIndex("apl/ch50522.itc", 0x29)
    LoadChrToIndex("apl/ch50522.itc", 0x2A)
    SoundLoad(861)
    OP_68(0, -22900, 25000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, -1300, -24000, 22100, 0)
    SetChrPos(0x102, -300, -24000, 21800, 0)
    SetChrPos(0x103, -1800, -24000, 20500, 0)
    SetChrPos(0x104, -800, -24000, 20200, 0)
    SetChrPos(0x107, 1500, -24000, 21900, 0)
    SetChrPos(0x108, 1900, -24000, 20900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrPos(0x8, -700, -24000, 40600, 180)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xA, 0x0)
    SetChrPos(0xA, -1200, -24000, 30900, 180)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x9, 0x25)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrPos(0x9, 700, -24000, 40600, 180)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x1)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EndChrThread(0xB, 0x0)
    SetChrPos(0xB, 1200, -24000, 31200, 180)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_11(0x0, 0x80, 0x80, 0x14, 0x32, 0x0)
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x1, "event\\ev602_02.eff")

    def lambda_DE9():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DE9)
    Sleep(50)

    def lambda_E06():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E06)

    def lambda_E20():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_E20)
    Sleep(50)

    def lambda_E3D():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E3D)

    def lambda_E57():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_E57)
    Sleep(50)

    def lambda_E74():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_E74)
    SetCameraDistance(20500, 2000)
    FadeToBright(1000, 0)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x107, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)
    WaitChrThread(0x104, 1)
    OP_93(0x102, 0x13B, 0x1F4)
    Sleep(750)
    OP_93(0x102, 0x2D, 0x1F4)
    Sleep(750)
    OP_93(0x102, 0x0, 0x1F4)
    Sleep(500)
    OP_6F(0x10)

    #C0009
    ChrTalk(
        0x102,
        (
            "#0108F#12P这一带存放着\x01",
            "不少近代化设备啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)
    Sleep(300)

    #C0010
    ChrTalk(
        0x107,
        (
            "#11P#0801F大概是那个叫约亚西姆\x01",
            "的人改造的吧？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F46():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F46)
    Sleep(50)

    def lambda_F56():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F56)

    def lambda_F63():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_F63)
    Sleep(50)

    def lambda_F73():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_F73)

    def lambda_F80():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_F80)
    WaitChrThread(0x101, 2)

    #C0011
    ChrTalk(
        0x101,
        (
            "#6P#0003F……多半如此吧。\x02\x03",

            "#0001F或许是为了完成『真知』\x01",
            "而建立的研究设备。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x108,
        (
            "#0903F#11P原来如此……\x02\x03",

            "#0900F在医院中并没有相关的设备，\x01",
            "所以这种可能性相当高呢──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1070():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1070)

    def lambda_107D():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_107D)
    WaitChrThread(0x108, 2)
    Fade(250)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    OP_0D()

    #C0013
    ChrTalk(
        0x108,
        "#0901F#12P……唔……！\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#12P#0201F有人来了……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -23100, 38000, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    OP_68(0, -23100, 28000, 5000)
    SetCameraDistance(22000, 5000)

    def lambda_1142():
        OP_96(0xFE, 0xFFFFFB50, 0xFFFFA240, 0x78B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1142)
    Sleep(50)

    def lambda_115F():
        OP_96(0xFE, 0x4B0, 0xFFFFA240, 0x79E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_115F)

    def lambda_1179():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1179)

    def lambda_1186():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1186)

    def lambda_1193():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1193)

    def lambda_11A0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_11A0)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sound(540, 0, 80, 0)
    OP_0D()

    #C0015
    ChrTalk(
        0x101,
        "#12P#0013F你们……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#12P#0301F嘁……\x01",
            "在这种地方也有啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x107,
        (
            "#0807F你们几个！\x01",
            "老老实实地投降吧！\x02\x03",

            "就算靠药物得到了强化，\x01",
            "也无法同我们这么多人──\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#12P#0205F请、请等一下……！\x02\x03",

            "#0201F#40W他们的样子……好像很奇怪……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x107,
        "#0805F哎……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(340, -23100, 28730, 3000)
    SetCameraDistance(20900, 3000)

    def lambda_1308():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1308)
    Fade(500)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    Sound(861, 2, 100, 0)

    #C0020
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#100W#18A……啊啊啊啊啊………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x8, 2)

    def lambda_13A1():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_13A1)
    Fade(500)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x1)
    OP_0D()
    PlayEffect(0x0, 0x1, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)

    #C0021
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#100W#18A……嘻嘻嘻嘻嘻………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x9, 2)
    OP_6F(0x79)
    Sleep(300)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)

    #C0022
    ChrTalk(
        0x102,
        "#0105F怎、怎么回事……！？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x108,
        "#0905F这、这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    OP_68(0, -23000, 30600, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(22000, 0)
    SetCameraDistance(17000, 2000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)

    def lambda_14CC():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_14CC)

    def lambda_14E5():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_14E5)

    def lambda_14FE():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_14FE)

    def lambda_1517():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1517)
    Sleep(500)

    def lambda_1533():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1533)

    def lambda_1544():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1544)

    def lambda_1555():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1555)

    def lambda_1566():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1566)
    Sound(202, 0, 100, 0)
    WaitChrThread(0xA, 2)
    WaitChrThread(0xB, 2)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    Sleep(500)
    OP_6F(0x10)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(22000, 500)
    SetChrChipByIndex(0xA, 0x27)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xB, 0x27)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1, 0xFF, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(315, 0, 100, 0)
    OP_24(0x35D)
    Sound(965, 0, 100, 0)
    Sound(948, 0, 100, 0)
    OP_82(0x1F4, 0x1F4, 0xBB8, 0x3E8)

    def lambda_1683():
        OP_A6(0xFE, 0x0, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1683)

    def lambda_169C():
        OP_A6(0xFE, 0x0, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_169C)

    #C0024
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#5S#15A嘎啊啊啊啊啊啊啊啊啊！\x02",
        )
    )
    #Auto


    #C0025
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#5S#15A嗷嗷嗷嗷嗷嗷嗷嗷嗷嗷！\x02",
        )
    )
    #Auto

    OP_5A()
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sleep(1000)
    CancelBlur(0)
    Fade(250)
    SetChrChipByIndex(0xA, 0x26)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xA, 0, 0, 1)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    BeginChrThread(0xB, 0, 0, 1)
    OP_68(0, -23100, 28000, 1500)
    OP_6F(0x1)
    OP_0D()

    #C0026
    ChrTalk(
        0x107,
        "#0813F#4S这是什么啊……！？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#12P#0207F这就是肉体变异吗……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#12P#0007F没时间犹豫了……！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        "#12P#0307F总之快点把他们打倒！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(18000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sound(814, 0, 100, 0)
    BeginChrThread(0xA, 3, 0, 8)
    Sleep(50)
    BeginChrThread(0xB, 3, 0, 8)
    Sleep(450)
    OP_24(0x35D)
    Battle("BattleInfo_49C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    Call(0, 9)
    Return()

    # Function_7_BC1 end

    def Function_8_18D7(): pass

    label("Function_8_18D7")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_190C():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFF060, 0x320, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_190C)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    SetChrSubChip(0xFE, 0x2)
    Sleep(130)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_8_18D7 end

    def Function_9_193B(): pass

    label("Function_9_193B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00650.itc", 0x22)
    LoadChrToIndex("chr/ch00750.itc", 0x23)
    LoadChrToIndex("apl/ch50546.itc", 0x24)
    LoadChrToIndex("monster/ch67350.itc", 0x26)
    LoadChrToIndex("monster/ch67352.itc", 0x27)
    LoadChrToIndex("monster/ch67353.itc", 0x28)
    LoadChrToIndex("chr/ch00056.itc", 0x29)
    SoundLoad(861)
    OP_68(-20, -23100, 30300, 0)
    MoveCamera(55, 19, 0, 0)
    OP_6E(450, 0)
    SetCameraDistance(21000, 0)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0x22)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0x23)
    SetChrSubChip(0x108, 0x0)
    SetChrPos(0x101, -1300, -24000, 26100, 0)
    SetChrPos(0x102, -300, -24000, 25800, 0)
    SetChrPos(0x103, -1800, -24000, 24500, 0)
    SetChrPos(0x104, -800, -24000, 24200, 0)
    SetChrPos(0x107, 1500, -24000, 25900, 0)
    SetChrPos(0x108, 1900, -24000, 24900, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -1200, -24000, 30900, 180)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x8, 0x800)
    OP_4B(0xA, 0xFF)
    SetChrChipByIndex(0xA, 0x28)
    SetChrSubChip(0xA, 0x1)
    OP_52(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xA, -1200, -24000, 30900, 180)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrChipByIndex(0x9, 0x24)
    SetChrSubChip(0x9, 0x1)
    SetChrPos(0x9, 1200, -24000, 31200, 180)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0x9, 0x800)
    OP_4B(0xB, 0xFF)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x1)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 1200, -24000, 31200, 180)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    OP_11(0x0, 0x80, 0x80, 0x14, 0x32, 0x0)
    LoadEffect(0x0, "event\\ev602_00.eff")
    LoadEffect(0x1, "event\\ev602_03.eff")
    PlayEffect(0x0, 0x0, 0x8, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x1, 0x9, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 100, 0)
    SetCameraDistance(20000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x10)
    Sound(965, 0, 100, 0)

    def lambda_1C2A():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1C2A)

    #C0030
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#15A#50W嘎啊啊……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_5A()
    Sleep(500)
    Sound(965, 0, 100, 0)

    def lambda_1C6C():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1C6C)

    #C0031
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#15A#50W嗷嗷嗷……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_5A()
    Sound(202, 0, 100, 0)

    def lambda_1CAB():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CAB)

    def lambda_1CC4():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CC4)

    def lambda_1CDD():
        OP_A6(0xFE, 0x0, 0x1E, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1CDD)

    def lambda_1CF6():
        OP_A6(0xFE, 0x0, 0x1E, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1CF6)

    def lambda_1D0F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1D0F)

    def lambda_1D20():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1D20)

    def lambda_1D31():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1D31)

    def lambda_1D42():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1D42)
    WaitChrThread(0x8, 2)
    WaitChrThread(0x9, 2)
    PlayEffect(0x1, 0xFF, 0xA, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0xB, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(868, 0, 100, 0)
    OP_24(0x35D)
    Sleep(1000)
    StopEffect(0x0, 0x2)
    StopEffect(0x1, 0x2)
    OP_68(0, -23100, 28000, 3000)
    MoveCamera(55, 19, 0, 3000)
    OP_6E(450, 3000)
    SetCameraDistance(23000, 3000)
    Fade(1000)
    SetChrChipByIndex(0x8, 0x0)
    SetChrSubChip(0x8, 0x0)
    OP_93(0x8, 0x87, 0x0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x0)
    SetChrSubChip(0x9, 0x1)
    Sound(514, 0, 100, 0)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    ClearChrFlags(0x8, 0x800)
    ClearChrFlags(0x9, 0x800)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x107, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x108, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x107)
    OP_64(0x108)
    OP_6F(0x79)

    #C0032
    ChrTalk(
        0x107,
        "#0808F这、这简直……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#0106F就像是一场噩梦啊……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x108,
        (
            "#0903F这就是魔人化……\x02\x03",

            "#0908F……之前也听说过这种现象\x01",
            "的存在，但没想到……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(808, 0, 80, 0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_68(540, -23100, 28800, 1500)

    def lambda_1FB9():
        OP_96(0xFE, 0xFFFFFCE0, 0xFFFFA240, 0x73A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1FB9)
    WaitChrThread(0x101, 1)
    Sleep(300)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x29)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_63(0x101, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_64(0x101)

    #C0035
    ChrTalk(
        0x101,
        (
            "#0006F#11P──已经晕过去了。\x02\x03",

            "#0008F虽然已经相当衰弱，\x01",
            "但似乎并没有性命之忧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x108, 0xFF)
    SetChrSubChip(0x108, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0036
    ChrTalk(
        0x107,
        "#0806F呼……太好了。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21800, 1500)
    OP_68(410, -23100, 29290, 1500)

    def lambda_20CF():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_20CF)
    Sleep(50)

    def lambda_20EC():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_20EC)
    Sleep(50)

    def lambda_2109():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2109)
    Sleep(50)

    def lambda_2126():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_2126)
    Sleep(50)

    def lambda_2143():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2143)
    WaitChrThread(0x107, 1)

    def lambda_2161():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2161)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)

    def lambda_217A():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_217A)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0037
    ChrTalk(
        0x103,
        (
            "#12P#0203F……恐怕，这也是\x01",
            "『真知』的力量吧……\x02\x03",

            "#0201F精神的异变，是有可能会\x01",
            "影响到肉体的。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#12P#0306F喂喂……\x01",
            "这也太夸张了吧？\x02\x03",

            "#0310F虽说只是些没用的小杂鱼，\x01",
            "但落得如此下场，也未免太……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x107,
        (
            "#0807F绝对不能原谅\x01",
            "那个叫约亚西姆的家伙……！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0003F#11P没错……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    OP_0D()
    OP_93(0x101, 0xB4, 0x1F4)
    Sleep(300)

    #C0041
    ChrTalk(
        0x101,
        (
            "#0013F#5P──总之，我们先在\x01",
            "这一带调查一下吧。\x02\x03",

            "说不定能得到什么\x01",
            "和教团相关的情报呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0101F#12P嗯……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x108,
        "#0901F#11P明白了……！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x8, 3800, -24000, 31500, 135)
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xAB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0x9, 3800, -24000, 29600, 180)
    SetChrFlags(0x8, 0x10)
    SetChrFlags(0x9, 0x10)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_D5(0x23)
    OP_D5(0x24)
    OP_D5(0x26)
    OP_D5(0x27)
    OP_D5(0x28)
    OP_D5(0x29)
    OP_37()
    OP_68(0, -23000, 28600, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(30000, 0)
    SetChrPos(0x0, 0, -24000, 28600, 0)
    SetChrPos(0x1, 0, -24000, 28600, 0)
    SetChrPos(0x2, 0, -24000, 28600, 0)
    SetChrPos(0x3, 0, -24000, 28600, 0)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_11(0x0, 0x80, 0x80, 0x19, 0x3C, 0x0)
    ModifyEventFlags(0, 0, 0x80)
    SetScenarioFlags(0xE5, 0)
    OP_29(0x4F, 0x1, 0x2)
    Sleep(500)
    OP_24(0x35D)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_9_193B end

    def Function_10_249F(): pass

    label("Function_10_249F")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_68(-109170, -23000, -760, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21950, 0)
    SetChrPos(0x101, -111000, -24000, -1500, 90)
    SetChrPos(0x102, -111000, -24000, -500, 90)
    SetChrPos(0x103, -109500, -24000, -1000, 90)
    SetChrPos(0x104, -112100, -24000, -1000, 90)
    SetChrPos(0x107, -110400, -24000, 1500, 135)
    SetChrPos(0x108, -111300, -24000, 1600, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_25A0")
    OP_71(0x7, 0x0, 0x96, 0x0, 0x0)
    Sound(72, 0, 100, 0)
    Sleep(2000)
    Sound(967, 0, 100, 0)
    Sleep(900)
    Sound(967, 0, 100, 0)
    Sleep(1400)
    Sound(967, 0, 100, 0)
    OP_79(0x7)
    OP_71(0x7, 0x96, 0xD2, 0x0, 0x20)
    Sleep(500)
    SetScenarioFlags(0xF4, 5)

    label("loc_25A0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_279F")

    #C0044
    ChrTalk(
        0x107,
        "#5P#0800F启动了……！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#0203F#5P是数年前，由财团开发出的\x01",
            "情报处理系统呢。\x02\x03",

            "#0201F虽然现在已经属于旧型号了，\x01",
            "但当时应该是相当昂贵的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0106F#6P采购这些东西所花销的米拉，\x01",
            "多半是由哈尔特曼议长提供的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯……总有一天，也有必要\x01",
            "彻底调查一下他那边呢。\x02\x03",

            "#0001F缇欧，还有别的发现吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#5P#0201F是的……\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x103,
        (
            "#5P#0205F──操作这个终端似乎可以\x01",
            "解除附近的锁，\x01",
            "还可以浏览情报。\x02\x03",

            "#0206F不过，情报好像\x01",
            "只剩下了一部分……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#6P#0000F足够了……\x01",
            "赶快调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_279F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_27A9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3045")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K情报终端０２\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【阅览情报】\x01",        # 0
            "【解锁】\x01",            # 1
            "【什么都不做】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_284D"),
        (1, "loc_2F85"),
        (2, "loc_3022"),
        (SWITCH_DEFAULT, "loc_3031"),
    )


    label("loc_284D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于真知』\x01\x01",
            "『真知』……是一种被称为\x01",
            "■■■■■■■■，以■■■■■\x01",
            "和『灵智之草』为原料制成的秘药。\x01\x01",
            "它的调配方法是■■■■■■■■■，\x01",
            "服用之后，可以提高身体能力与感应力，\x01",
            "更拥有激发出人体潜在能力的效果。\x01",
            "■■■■■■■■■■■■■■■■■。\x01",
            "■■■■■■■■■■■■■■■。\x01",
            "『真知』是可以将■■■的■■\x01",
            "■■■■■■■为『■』的■■的药物。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『■』拥有通过将■■■的■■进行■■，\x01",
            "将■■储存，并加以■■的性质。\x01",
            "当那■■达到『■■』的境界之时，\x01",
            "『■』就会■■。\x01\x01",
            "另外，『真知』\x01",
            "尚有改良的余地。\x01",
            "■■■■■■■■■■■■■■■■■，\x01",
            "将■■■■■■■在『■』■■■■■。\x01\x01",
            "随后■■■■■■■，我们教团一直\x01",
            "在对更具效果的『真知』进行研究……\x01",
            "并不断举行各种『仪式』。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S如此，■■■■■的■■■，\x01",
            "■■■■■■■■■■■■，\x01",
            "虽然『真知』已经接近完成，\x01",
            "但就在只差一步的关头，出现了差错。\x01\x01",
            "由于实验规模太过庞大，\x01",
            "所以被游击士及其它势力所察觉，\x01",
            "各据点，以及整个教团，\x01",
            "因此步入毁灭。\x01\x01",
            "不得不说，这确实太过愚蠢了。\x01",
            "但为了『■■■■』的■■，\x01",
            "这点牺牲还是必要的……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S我从已经覆灭的据点中\x01",
            "秘密回收了实验资料，\x01",
            "并来到了克洛斯贝尔这个■■之地。\x01\x01",
            "由于『真知』的材料\x01",
            "『灵智之草』生长在■■■■■■■\x01",
            "的■■■，所以■■\x01",
            "■■■■■并没有任何困难。\x01",
            "此外，在这『太阳堡垒』的深层地带，\x01",
            "有着■■的■■■■的■■■研究设施，\x01",
            "备有众多先进设备。\x01",
            "如此一来，我拥有了完美的研究环境，\x01",
            "最后终于将秘药彻底完成──\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F80")

    #C0056
    ChrTalk(
        0x101,
        "#0013F#6P相当多的情报都被删除了呢……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0101F#6P是啊……不过关于这药物的情报，\x01",
            "似乎已经算是比较详尽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x108,
        (
            "#0908F#5P看起来，『真知』确实是利用这里的\x01",
            "研究设施而完成的啊。\x02\x03",

            "#0903F仅仅用了数年时间，\x01",
            "就能进展到量产阶段吗……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x107,
        (
            "#0801F#5P这个『灵智之草』\x01",
            "到底是什么呢？\x02\x03",

            "似乎是药物的原材料……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0301F#6P『灵智之草』……\x01",
            "从没听过这个名字啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#0206F#5P……我也从没听说过。\x02\x03",

            "#0201F回去之后，似乎有必要\x01",
            "再到资料库中好好调查一下呢。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 2)

    label("loc_2F80")

    Jump("loc_3040")

    label("loc_2F85")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2FC7")
    SetChrName("")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进行了解锁操作。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE5, 3)
    OP_29(0x4F, 0x1, 0x4)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_301D")

    label("loc_2FC7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2FFA")
    SetChrName("")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "附近的门锁被打开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_301D")

    label("loc_2FFA")

    SetChrName("")

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "对应的门锁已经解除了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_301D")

    Jump("loc_3040")

    label("loc_3022")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3040")

    label("loc_3031")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3040")

    label("loc_3040")

    Jump("loc_27A9")

    label("loc_3045")

    SetChrPos(0x0, -111400, -24000, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_249F end

    def Function_11_3072(): pass

    label("Function_11_3072")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_68(7660, -23000, -119310, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(22110, 0)
    SetChrPos(0x101, 6000, -24000, -120000, 90)
    SetChrPos(0x102, 6000, -24000, -119000, 90)
    SetChrPos(0x103, 7500, -24000, -119500, 90)
    SetChrPos(0x104, 4900, -24000, -119500, 90)
    SetChrPos(0x107, 6600, -24000, -117000, 135)
    SetChrPos(0x108, 5700, -24000, -116900, 135)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3173")
    OP_71(0x6, 0x0, 0x96, 0x0, 0x0)
    Sound(72, 0, 100, 0)
    Sleep(2000)
    Sound(967, 0, 100, 0)
    Sleep(900)
    Sound(967, 0, 100, 0)
    Sleep(1400)
    Sound(967, 0, 100, 0)
    OP_79(0x6)
    OP_71(0x6, 0x96, 0xD2, 0x0, 0x20)
    Sleep(500)
    SetScenarioFlags(0xF4, 6)

    label("loc_3173")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3372")

    #C0065
    ChrTalk(
        0x107,
        "#5P#0800F启动了……！\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#0203F#5P是数年前，由财团开发出的\x01",
            "情报处理系统呢。\x02\x03",

            "#0201F虽然现在已经属于旧型号了，\x01",
            "但当时应该是相当昂贵的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#0106F#6P采购这些东西所花销的米拉，\x01",
            "多半是由哈尔特曼议长提供的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#6P#0003F嗯……总有一天，也有必要\x01",
            "彻底调查一下他那边呢。\x02\x03",

            "#0001F缇欧，还有别的发现吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        "#5P#0201F是的……\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x103,
        (
            "#5P#0205F──操作这个终端似乎可以\x01",
            "解除附近的锁，\x01",
            "还可以浏览情报。\x02\x03",

            "#0206F不过，情报好像\x01",
            "只剩下了一部分……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#6P#0000F足够了……\x01",
            "赶快调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_3372")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_337C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3AB3")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K情报终端０３\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【阅览情报】\x01",        # 0
            "【解锁】\x01",            # 1
            "【什么都不做】\x01",      # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_0D()
    SetMessageWindowPos(14, 280, 60, 3)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3420"),
        (1, "loc_39F3"),
        (2, "loc_3A90"),
        (SWITCH_DEFAULT, "loc_3A9F"),
    )


    label("loc_3420")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于圣子』\x01\x01",
            "克洛斯贝尔不仅是我们『Ｄ∴Ｇ教团』\x01",
            "的■■■，而且也是■■■■。\x01",
            "这是因为，■■『圣子』\x01",
            "■■■■■■■■■■■■■。\x01\x01",
            "所谓『圣子』，是『■■■■』■■■■■\x01",
            "■■『Ｄ∴Ｇ教团』■■■■■■■■■■。\x01",
            "『太阳堡垒』■■■■■■■■■■■■，\x01",
            "■■■■■■■■■■■■■■■■■，\x01",
            "■■■■■■■『太阳堡垒』■■■■\x01",
            "■■■■■■■■■■■■■■。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S然而将如此的■■进行■■等事，\x01",
            "对凡夫俗子而言，也许难以置信吧。\x01\x01",
            "但是，我确实曾经亲眼见证过。\x01",
            "在被称作『■■■■■』的■■的■，\x01",
            "■■■■■■■■■■■■■■──\x01",
            "将神圣的■■。\x01\x01",
            "『■■■■■』将『古代遗物』\x01",
            "进行■■，以■■■■的■■为基础，\x01",
            "从而■■■■■■■■■■■■■■■。\x01",
            "既然如此，这■■■■■■■■■■\x01",
            "也并不足为奇吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『圣子』是从■■■■■■，\x01",
            "将『真知』■■■，■■■■■■■\x01",
            "■■■■■■■■■■■■■。\x01\x01",
            "──『■■』■■■『圣子』将■■，\x01",
            "■■■■『■』■■■吧。\x01",
            "接下来，■■的■■和■■\x01",
            "将归于『■』，并得到■■，\x01",
            "并将人类从『■■』的咒缚中解放。\x01\x01",
            "那正是我们『Ｄ∴Ｇ教团』的前人们\x01",
            "留下的预言，终将实现的伟大愿望──\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39EE")

    #C0076
    ChrTalk(
        0x104,
        (
            "#0305F#6P这什么乱七八糟的……\x01",
            "就像被虫子啃过一样嘛。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x108,
        (
            "#0901F#5P……对教团来说，\x01",
            "这些情报似乎算是最高机密了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x107,
        (
            "#0808F#5P那个，这里说的『圣子』，\x01",
            "就是指小琪雅吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#0106F#6P嗯……\x02\x03",

            "#0101F现身于ＩＢＣ大厦的约亚西姆医生\x01",
            "就是这么称呼她的。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        (
            "#0211F#6P但说实话，从他的口气来判断，\x01",
            "只能认为那是妄想者的一派胡言呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0003F#6P……不管怎么说，关于这些情报，\x01",
            "还是要直接询问他本人啊。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 3)

    label("loc_39EE")

    Jump("loc_3AAE")

    label("loc_39F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A35")
    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "进行了解锁操作。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE5, 4)
    OP_29(0x4F, 0x1, 0x5)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3A8B")

    label("loc_3A35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3A68")
    SetChrName("")

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "附近的门锁被打开了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3A8B")

    label("loc_3A68")

    SetChrName("")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "对应的门锁已经解除了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3A8B")

    Jump("loc_3AAE")

    label("loc_3A90")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AAE")

    label("loc_3A9F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3AAE")

    label("loc_3AAE")

    Jump("loc_337C")

    label("loc_3AB3")

    SetChrPos(0x0, 6000, -24000, -118400, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_3072 end

    def Function_12_3AE0(): pass

    label("Function_12_3AE0")

    Fade(500)
    OP_68(0, -23000, 218000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_3B38")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B38")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_3B4F")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B4F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_3B66")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3B66")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3BBC")
    OP_71(0x5, 0x14, 0x5A, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    Sleep(700)
    Sound(135, 0, 100, 0)
    OP_79(0x5)
    Sound(116, 0, 100, 0)
    OP_70(0x3, 0x5A)
    OP_70(0x4, 0x5A)
    OP_70(0x5, 0x5A)
    ClearMapObjFlags(0x3, 0x2)
    ClearMapObjFlags(0x4, 0x2)
    ClearMapObjFlags(0x5, 0x2)
    Jump("loc_3C68")

    label("loc_3BBC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C03")
    OP_71(0x5, 0xA, 0x14, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x5)
    OP_70(0x3, 0x14)
    OP_70(0x4, 0x14)
    OP_70(0x5, 0x14)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_3C68")

    label("loc_3C03")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C4A")
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x5)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0xA)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_3C68")

    label("loc_3C4A")

    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    OP_70(0x5, 0x0)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)

    label("loc_3C68")

    Sleep(1000)
    Return()

    # Function_12_3AE0 end

    SaveToFile()

Try(main)
