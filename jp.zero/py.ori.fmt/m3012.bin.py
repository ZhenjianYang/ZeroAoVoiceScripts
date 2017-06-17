from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "マフィア",               # 1
        "マフィア",               # 2
        "魔人マフィア",           # 3
        "魔人マフィア",           # 4
        "ヘルハウンド",           # 5
        "bm3010",                 # 6
        "bm3010",                 # 7
        "bm3010",                 # 8
    ))

    ATBonus("ATBonus_290", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_2B0", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_4046", 9,   12,  6,   16,  2,   13,  4)

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
        "BattleInfo_390", 0x0000, 38, 6, 60, 4, 1, 40, 0, "bm3010", "Sepith_4046", 60, 25, 10, 5,
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
        "Function_5_A78",          # 05, 5
        "Function_6_BC5",          # 06, 6
        "Function_7_BF5",          # 07, 7
        "Function_8_195B",         # 08, 8
        "Function_9_19BF",         # 09, 9
        "Function_10_2577",        # 0A, 10
        "Function_11_32E2",        # 0B, 11
        "Function_12_3E6A",        # 0C, 12
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_960")
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
            "魔獣が現れた！\x07\x00\x02",
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
        (0, "loc_941"),
        (2, "loc_950"),
        (1, "loc_95D"),
        (SWITCH_DEFAULT, "loc_960"),
    )


    label("loc_941")

    SetScenarioFlags(0x76, 4)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_960")

    label("loc_950")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_95D")

    OP_B7(0x0)
    Return()

    label("loc_960")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x652, 1)"), scpexpr(EXPR_END)), "loc_9BD")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x652),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11F, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_A2D")

    label("loc_9BD")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x652),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x652),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A2D")

    Jump("loc_A6C")

    label("loc_A32")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_A6C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_865 end

    def Function_5_A78(): pass

    label("Function_5_A78")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B74")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_AFD")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x108, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_B6F")

    label("loc_AFD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
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
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B6F")

    Jump("loc_BB9")

    label("loc_B74")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_BB9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A78 end

    def Function_6_BC5(): pass

    label("Function_6_BC5")

    TalkBegin(0xFE)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "マフィアは気を失っている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFE)
    Return()

    # Function_6_BC5 end

    def Function_7_BF5(): pass

    label("Function_7_BF5")

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

    def lambda_E1D():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_E1D)
    Sleep(50)

    def lambda_E3A():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_E3A)

    def lambda_E54():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_E54)
    Sleep(50)

    def lambda_E71():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_E71)

    def lambda_E8B():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_E8B)
    Sleep(50)

    def lambda_EA8():
        OP_98(0xFE, 0x0, 0x0, 0xFA0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_EA8)
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
            "#0108F#12Pこのあたりは近代的な\x01",
            "設備が入っているわね……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x107, 0x101, 500)
    Sleep(300)

    #C0010
    ChrTalk(
        0x107,
        (
            "#11P#0801Fそのヨアヒムって人が\x01",
            "改築させたのかしら？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_F8C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F8C)
    Sleep(50)

    def lambda_F9C():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F9C)

    def lambda_FA9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FA9)
    Sleep(50)

    def lambda_FB9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FB9)

    def lambda_FC6():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_FC6)
    WaitChrThread(0x101, 2)

    #C0011
    ChrTalk(
        0x101,
        (
            "#6P#0003F……多分そうだろう。\x02\x03",

            "#0001F《グノーシス》を完成させるための\x01",
            "研究設備かもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x108,
        (
            "#0903F#11Pなるほど……\x02\x03",

            "#0900F病院にその設備が無かった以上、\x01",
            "可能性は高いかもしれないね──\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x108, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_10D0():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10D0)

    def lambda_10DD():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_10DD)
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
        "#0901F#12P……っ……！\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        "#12P#0201F誰か来ます……！\x02",
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

    def lambda_11A4():
        OP_96(0xFE, 0xFFFFFB50, 0xFFFFA240, 0x78B4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_11A4)
    Sleep(50)

    def lambda_11C1():
        OP_96(0xFE, 0x4B0, 0xFFFFA240, 0x79E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_11C1)

    def lambda_11DB():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_11DB)

    def lambda_11E8():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_11E8)

    def lambda_11F5():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_11F5)

    def lambda_1202():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1202)
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
        "#12P#0013Fあんたたち……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#12P#0301Fチッ……\x01",
            "ここにもいやがったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x107,
        (
            "#0807Fあなたたち！\x01",
            "大人しく投降しなさい！\x02\x03",

            "いくら薬で強くなったって\x01",
            "この人数相手に──\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x103,
        (
            "#12P#0205Fま、待ってください……！\x02\x03",

            "#0201F#40W様子が……何か変です……！\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x107,
        "#0805Fえっ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    StopBGM(0xFA0)
    OP_68(340, -23100, 28730, 3000)
    SetCameraDistance(20900, 3000)

    def lambda_137C():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_137C)
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
            "#5P#100W#18A……ァァアアア………\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    WaitChrThread(0x8, 2)

    def lambda_1415():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1415)
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
            "#5P#100W#18A……ギギギギギ………\x02",
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
        "#0105Fな、なんなの……！？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x108,
        "#0905Fこ、これは……\x02",
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

    def lambda_1542():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1542)

    def lambda_155B():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_155B)

    def lambda_1574():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1574)

    def lambda_158D():
        OP_A6(0xFE, 0x0, 0x1E, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_158D)
    Sleep(500)

    def lambda_15A9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_15A9)

    def lambda_15BA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_15BA)

    def lambda_15CB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_15CB)

    def lambda_15DC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_15DC)
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

    def lambda_16F9():
        OP_A6(0xFE, 0x0, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_16F9)

    def lambda_1712():
        OP_A6(0xFE, 0x0, 0x0, 0x7D0, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1712)

    #C0024
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6P#5S#15Aガアアアアアアアアッ！\x02",
        )
    )
    #Auto


    #C0025
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#5S#15Aオオオオオオオオオッ！\x02",
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
        "#0813F#4Sなああっ……！？\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x103,
        "#12P#0207F肉体変異#8Rメタモルフォーゼ#……！？\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        "#12P#0007F迷ってる暇はない……！\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        "#12P#0307Fとにかくブチ倒すぞ！\x02",
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

    # Function_7_BF5 end

    def Function_8_195B(): pass

    label("Function_8_195B")

    EndChrThread(0xFE, 0x0)
    SetChrChipByIndex(0xFE, 0x27)
    SetChrSubChip(0xFE, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_52(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1990():
        OP_9C(0xFE, 0x0, 0x0, 0xFFFFF060, 0x320, 0x5DC)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1990)
    SetChrSubChip(0xFE, 0x1)
    Sleep(130)
    SetChrSubChip(0xFE, 0x2)
    Sleep(130)
    SetChrSubChip(0xFE, 0x3)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_8_195B end

    def Function_9_19BF(): pass

    label("Function_9_19BF")

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

    def lambda_1CAE():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1CAE)

    #C0030
    ChrTalk(
        0xA,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#15A#50Wガアアッ……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_5A()
    Sleep(500)
    Sound(965, 0, 100, 0)

    def lambda_1CF2():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1CF2)

    #C0031
    ChrTalk(
        0xB,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#5P#15A#50Wオオオッ……！\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_5A()
    Sound(202, 0, 100, 0)

    def lambda_1D33():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1D33)

    def lambda_1D4C():
        OP_A6(0xFE, 0x0, 0x32, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1D4C)

    def lambda_1D65():
        OP_A6(0xFE, 0x0, 0x1E, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1D65)

    def lambda_1D7E():
        OP_A6(0xFE, 0x0, 0x1E, 0xBB8, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1D7E)

    def lambda_1D97():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1D97)

    def lambda_1DA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_1DA8)

    def lambda_1DB9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_1DB9)

    def lambda_1DCA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x5DC)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_1DCA)
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
        "#0808Fこ、これって……\x02",
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        "#0106F悪夢でも見てるみたい……\x02",
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x108,
        (
            "#0903F魔人化#6Rデモナイズ#……\x02\x03",

            "#0908F……そんな現象があるのは\x01",
            "聞いたことがあるけれど……\x02",
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

    def lambda_2055():
        OP_96(0xFE, 0xFFFFFCE0, 0xFFFFA240, 0x73A0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2055)
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
            "#0006F#11P──気絶している。\x02\x03",

            "#0008Fかなり衰弱してるけど\x01",
            "命に別状はなさそうだな。\x02",
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
        "#0806Fほっ……良かった。\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(21800, 1500)
    OP_68(410, -23100, 29290, 1500)

    def lambda_2173():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_2173)
    Sleep(50)

    def lambda_2190():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2190)
    Sleep(50)

    def lambda_21AD():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_21AD)
    Sleep(50)

    def lambda_21CA():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x108, 1, lambda_21CA)
    Sleep(50)

    def lambda_21E7():
        OP_98(0xFE, 0x0, 0x0, 0x7D0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_21E7)
    WaitChrThread(0x107, 1)

    def lambda_2205():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_2205)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x108, 1)

    def lambda_221E():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x108, 2, lambda_221E)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)

    #C0037
    ChrTalk(
        0x103,
        (
            "#12P#0203F……恐らくこれも\x01",
            "《グノーシス》の力かと……\x02\x03",

            "#0201F精神の変容が肉体まで\x01",
            "影響したのかもしれません。\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x104,
        (
            "#12P#0306Fおいおい……\x01",
            "メチャクチャすぎんだろ。\x02\x03",

            "#0310Fいくらロクデナシどもとはいえ、\x01",
            "こんな目に遭わせるたぁ……\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x107,
        (
            "#0807Fそのヨアヒムってヤツ、\x01",
            "絶対に許せないわね……！\x02",
        )
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x101,
        "#0003F#11Pああ……\x02",
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
            "#0013F#5P──とりあえず、\x01",
            "この一帯を調べてみよう。\x02\x03",

            "教団に関する情報が\x01",
            "手に入るかもしれない。\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0101F#12Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x108,
        "#0901F#11P分かった……！\x02",
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

    # Function_9_19BF end

    def Function_10_2577(): pass

    label("Function_10_2577")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2678")
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

    label("loc_2678")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_28AB")

    #C0044
    ChrTalk(
        0x107,
        "#5P#0800F動いた……！\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0x103,
        (
            "#0203F#5P数年前に財団が開発した\x01",
            "情報処理システムですね。\x02\x03",

            "#0201F今となっては旧式ですが\x01",
            "当時は相当高価だったはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x102,
        (
            "#0106F#6P多分ミラは、ハルトマン議長が\x01",
            "用意したんでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ……いずれその辺りも\x01",
            "徹底的に洗う必要がありそうだな。\x02\x03",

            "#0001Fティオ、他に何か分かるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x103,
        "#5P#0201Fはい……\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    #C0049
    ChrTalk(
        0x103,
        (
            "#5P#0205F──どうやらこの端末では\x01",
            "隔壁のロックの解除と\x01",
            "情報の閲覧が出来るようです。\x02\x03",

            "#0206Fもっとも情報は一部しか\x01",
            "残っていないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#6P#0000F十分だ……\x01",
            "さっそく調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_28AB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B5")
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
            "#1K第０２情報端末\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【情報を閲覧する】\x01",        # 0
            "【ロックを解除する】\x01",      # 1
            "【何もしない】\x01",            # 2
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
        (0, "loc_296D"),
        (1, "loc_31CD"),
        (2, "loc_3292"),
        (SWITCH_DEFAULT, "loc_32A1"),
    )


    label("loc_296D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『グノーシスについて』\x01\x01",
            "《グノーシス》……それは、\x01",
            "■■■■■■■■という■■■■■、\x01",
            "《プレロマ草》を原料とした秘薬である。\x01\x01",
            "その調合方法は■■■■■■■■■、\x01",
            "服用することで身体能力と感応力を高め、\x01",
            "さらには潜在能力すら引き出す効能を持つ。\x01",
            "■■■■■■■■■■■■■■■■■。\x01",
            "■■■■■■■■■■■■■■■。\x01",
            "《グノーシス》は、■■■の■■を\x01",
            "《■》の■■に■■■■■■■薬なのだ。\x07\x00\x02",
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
            "#2S《■》は■■■の■■を■■することで\x01",
            "■■を蓄え、■■する性質を持つ。\x01",
            "いずれその■■が《■■》に至ったとき、\x01",
            "《■》は■■するのである。\x01\x01",
            "さらに、《グノーシス》には\x01",
            "改良の余地が残されていた。\x01",
            "■■■■■■■■■■■■■■■■■、\x01",
            "■■■■■■■を《■》に■■■■■のだ。\x01\x01",
            "それから■■■■■■■、我が教団は\x01",
            "より効果の高い《グノーシス》の研究……\x01",
            "いわゆる“儀式”を繰り返してきた。\x07\x00\x02",
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
            "#2Sそうして、■■■■■の■■■とは\x01",
            "■■■■■■■■■■■■\x01",
            "《グノーシス》は完成へと近づいたが、\x01",
            "今一歩のところで誤算が生じてしまう。\x01\x01",
            "実験の規模を大きくしたことで\x01",
            "遊撃士やその他の勢力に存在を感づかれ、\x01",
            "各ロッジ、及び教団そのものの壊滅に\x01",
            "繋がってしまったのである。\x01\x01",
            "誠に愚かな事であると言わざるを得ない。\x01",
            "《■■■■》の■■のためには\x01",
            "多少の犠牲は付き物だというのに……\x07\x00\x02",
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
            "#2S私は、壊滅したロッジから\x01",
            "実験のデータを秘密裏に回収し、\x01",
            "この■■の地クロスベルへと至った。\x01\x01",
            "《グノーシス》の材料である\x01",
            "《プレロマ草》は■■■■■■■の\x01",
            "■■■に■■しているため、\x01",
            "■■■■■に困ることはなかった。\x01",
            "また、この《太陽の砦》の深層は\x01",
            "■■の■■■■の■■■研究施設であり、\x01",
            "数々の高度な設備を備えている。\x01",
            "こうして私は恵まれた研究環境を手に入れ\x01",
            "遂にこの秘薬を完成させたのである──。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_31C8")

    #C0056
    ChrTalk(
        0x101,
        "#0013F#6Pかなりの情報が削除されてるな……\x02",
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x102,
        (
            "#0101F#6Pええ……例の薬についての情報が\x01",
            "まとめられているみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0x108,
        (
            "#0908F#5Pでも、ここの研究施設を使って\x01",
            "完成させたのは確かみたいだね。\x02\x03",

            "#0903Fたった数年で、量産段階まで\x01",
            "漕ぎつけたのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x107,
        (
            "#0801F#5Pこの《プレロマ草》ってのは\x01",
            "何なのかしら？\x02\x03",

            "薬の原材料っぽいけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x104,
        (
            "#0301F#6P《プレロマ草》……\x01",
            "聞いたことのない名前だな。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x103,
        (
            "#0206F#5P……わたしも聞き覚えがありません。\x02\x03",

            "#0201F戻ったらデータベースで\x01",
            "調べてみる必要がありそうですね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 2)

    label("loc_31C8")

    Jump("loc_32B0")

    label("loc_31CD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3223")
    SetChrName("")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロックを解除するための操作を行った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE5, 3)
    OP_29(0x4F, 0x1, 0x4)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_328D")

    label("loc_3223")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_325C")
    SetChrName("")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "隔壁は既に開放されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_328D")

    label("loc_325C")

    SetChrName("")

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "対応するロックは既に解除されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_328D")

    Jump("loc_32B0")

    label("loc_3292")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32B0")

    label("loc_32A1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_32B0")

    label("loc_32B0")

    Jump("loc_28B5")

    label("loc_32B5")

    SetChrPos(0x0, -111400, -24000, 0, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_10_2577 end

    def Function_11_32E2(): pass

    label("Function_11_32E2")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_33E3")
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

    label("loc_33E3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3616")

    #C0065
    ChrTalk(
        0x107,
        "#5P#0800F動いた……！\x02",
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#0203F#5P数年前に財団が開発した\x01",
            "情報処理システムですね。\x02\x03",

            "#0201F今となっては旧式ですが\x01",
            "当時は相当高価だったはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x102,
        (
            "#0106F#6P多分ミラは、ハルトマン議長が\x01",
            "用意したんでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x101,
        (
            "#6P#0003Fああ……いずれその辺りも\x01",
            "徹底的に洗う必要がありそうだな。\x02\x03",

            "#0001Fティオ、他に何か分かるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x103,
        "#5P#0201Fはい……\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    #C0070
    ChrTalk(
        0x103,
        (
            "#5P#0205F──どうやらこの端末では\x01",
            "隔壁のロックの解除と\x01",
            "情報の閲覧が出来るようです。\x02\x03",

            "#0206Fもっとも情報は一部しか\x01",
            "残っていないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x101,
        (
            "#6P#0000F十分だ……\x01",
            "さっそく調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_3616")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3620")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3E3D")
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
            "#1K第０３情報端末\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【情報を閲覧する】\x01",        # 0
            "【ロックを解除する】\x01",      # 1
            "【何もしない】\x01",            # 2
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
        (0, "loc_36D8"),
        (1, "loc_3D55"),
        (2, "loc_3E1A"),
        (SWITCH_DEFAULT, "loc_3E29"),
    )


    label("loc_36D8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『御子について』\x01\x01",
            "このクロスベルは我々《Ｄ∴Ｇ教団》の\x01",
            "■■■であるとともに、■■■■とされる。\x01",
            "その■■は、《御子》たるものが\x01",
            "■■■■■■■■■■■■■だからである。\x01\x01",
            "《御子》とは、《■■■■》■■■■■■■\x01",
            "■■《Ｄ∴Ｇ教団》■■■■■■■■■■。\x01",
            "《太陽の砦》■■■■■■■■■■■■、\x01",
            "■■■■■■■■■■■■■■■■■、\x01",
            "■■■■■■■《太陽の砦》■■■■\x01",
            "■■■■■■■■■■■■■■のだ。\x07\x00\x02",
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
            "#2S■■がそれほどの■■を■■■など、\x01",
            "俗世の者には信じ難い話であろう。\x01\x01",
            "だが、私は確かにこの目で見たのだ。\x01",
            "『■■■■■』と呼ばれる■■の■で\x01",
            "■■■■■■■■■■■■■■──\x01",
            "その神々しき■■を。\x01\x01",
            "『■■■■■』は、《古代遺物》を\x01",
            "■■していた■■■■■■の■■を元に\x01",
            "■■■■■■■■■■■■■■■である。\x01",
            "ならば、この■■■■■■■■■■にも\x01",
            "何ら不思議はないだろう。\x07\x00\x02",
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
            "#2S《御子》は■■■■■■から\x01",
            "《グノーシス》を■■■、■■■■■■■\x01",
            "■■■■■■■■■■■■■。\x01\x01",
            "──《■■》■■■■■《御子》は■■■、\x01",
            "■■■■《■》■■■であろう。\x01",
            "そして、■■の■■の■■と■■は\x01",
            "《■》のもとに■■され、\x01",
            "人々を《■■》の呪縛から解き放つのだ。\x01\x01",
            "それが我が《Ｄ∴Ｇ教団》の先人が残した\x01",
            "預言であり、成すべき大望なのである──。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D50")

    #C0076
    ChrTalk(
        0x104,
        (
            "#0305F#6P何だこりゃ……\x01",
            "虫食いだらけじゃねえか。\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x108,
        (
            "#0901F#5P……どうやら教団にとって\x01",
            "最高機密にあたる情報みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x107,
        (
            "#0808F#5Pえっと、この《御子》っていうのは\x01",
            "キーアちゃんの事なのよね？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x102,
        (
            "#0106F#6Pえ、ええ……\x02\x03",

            "#0101FＩＢＣビルに現れたヨアヒム先生が\x01",
            "彼女のことをそう呼んでたわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x103,
        (
            "#0211F#6P正直、妄想のたぐいとしか\x01",
            "思えないような口ぶりでしたけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x101,
        (
            "#0003F#6P……いずれにせよ、この情報は\x01",
            "直接本人から聞くしかなさそうだな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 3)

    label("loc_3D50")

    Jump("loc_3E38")

    label("loc_3D55")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3DAB")
    SetChrName("")

    #A0082
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロックを解除するための操作を行った。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE5, 4)
    OP_29(0x4F, 0x1, 0x5)
    Call(0, 12)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E15")

    label("loc_3DAB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3DE4")
    SetChrName("")

    #A0083
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "隔壁は既に開放されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3E15")

    label("loc_3DE4")

    SetChrName("")

    #A0084
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "対応するロックは既に解除されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3E15")

    Jump("loc_3E38")

    label("loc_3E1A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E38")

    label("loc_3E29")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3E38")

    label("loc_3E38")

    Jump("loc_3620")

    label("loc_3E3D")

    SetChrPos(0x0, 6000, -24000, -118400, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_11_32E2 end

    def Function_12_3E6A(): pass

    label("Function_12_3E6A")

    Fade(500)
    OP_68(0, -23000, 218000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_3EC2")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EC2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_3ED9")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3ED9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_3EF0")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3EF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F46")
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
    Jump("loc_3FF2")

    label("loc_3F46")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F8D")
    OP_71(0x5, 0xA, 0x14, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x5)
    OP_70(0x3, 0x14)
    OP_70(0x4, 0x14)
    OP_70(0x5, 0x14)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_3FF2")

    label("loc_3F8D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FD4")
    OP_71(0x5, 0x0, 0xA, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x5)
    OP_70(0x3, 0xA)
    OP_70(0x4, 0xA)
    OP_70(0x5, 0xA)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)
    Jump("loc_3FF2")

    label("loc_3FD4")

    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    OP_70(0x5, 0x0)
    SetMapObjFlags(0x3, 0x2)
    SetMapObjFlags(0x4, 0x2)
    SetMapObjFlags(0x5, 0x2)

    label("loc_3FF2")

    Sleep(1000)
    Return()

    # Function_12_3E6A end

    SaveToFile()

Try(main)
