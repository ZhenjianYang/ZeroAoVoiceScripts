from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t163b.bin",                # FileName
        "t163b",                    # MapName
        "t163b",                    # Location
        0x0056,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 86, 0, 0, 0, 1],
    )

    BuildStringList((
        "t163b",                  # 0
        "盖里教授",               # 1
        "阿修拉主任",             # 2
        "拉格教授",               # 3
        "bt162b",                 # 4
        "bt162b",                 # 5
    ))

    ATBonus("ATBonus_20C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1903", 3,   14,  4,   4,   12,  12,  12)
    Sepith("Sepith_18FB", 13,  13,  24,  10,  0,   0,   0)

    MonsterBattlePostion("MonsterBattlePostion_26C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_24C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_268", 2, 13, 180)

    # monster count: 5

    BattleInfo(
        "BattleInfo_3B4", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_1903", 30, 45, 20, 5,
        (
            ("ms75701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_24C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, "MonsterBattlePostion_24C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
        )
    )

    BattleInfo(
        "BattleInfo_2EC", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_18FB", 30, 45, 20, 5,
        (
            ("ms67501.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_24C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, "MonsterBattlePostion_24C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
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
        "monster/ch67550.itc",               # 10
        "monster/ch67551.itc",               # 11
        "monster/ch75750.itc",               # 12
        "monster/ch75750.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(110030,  -1160,   0,       0x1010000,    "BattleInfo_3B4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-6640,   34720,   0,       0x1010000,    "BattleInfo_2EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-63640,  51560,   0,       0x1010000,    "BattleInfo_3B4", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-72820,  59500,   0,       0x1010000,    "BattleInfo_2EC", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-54530,  42350,   0,       0x1010000,    "BattleInfo_3B4", 0,   18,  0xFFFF, 2,  3)

    DeclActor(110480,  0,       5410,    1200,    110480,  1000,    5410,    0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_4DC",          # 00, 0
        "Function_1_4F7",          # 01, 1
        "Function_2_7AB",          # 02, 2
        "Function_3_847",          # 03, 3
        "Function_4_97D",          # 04, 4
        "Function_5_C0E",          # 05, 5
        "Function_6_16F0",         # 06, 6
        "Function_7_1734",         # 07, 7
        "Function_8_1778",         # 08, 8
        "Function_9_17BC",         # 09, 9
        "Function_10_181A",        # 0A, 10
        "Function_11_187B",        # 0B, 11
    ))


    def Function_0_4DC(): pass

    label("Function_0_4DC")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x74), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4F6")
    Event(0, 5)

    label("loc_4F6")

    Return()

    # Function_0_4DC end

    def Function_1_4F7(): pass

    label("Function_1_4F7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_54C")
    LoadEffect(0x7, "event\\ev617_00.eff")
    PlayEffect(0x7, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_54C")

    OP_1B(0x3, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_569")
    OP_1B(0x3, 0x0, 0x4)

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_580")
    OP_1B(0x3, 0x0, 0xB)

    label("loc_580")

    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A3")
    OP_70(0x5, 0x0)
    Jump("loc_7A7")

    label("loc_7A3")

    OP_70(0x5, 0x1E)

    label("loc_7A7")

    Call(0, 2)
    Return()

    # Function_1_4F7 end

    def Function_2_7AB(): pass

    label("Function_2_7AB")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7C9")
    SetChrFlags(0xB, 0x8)
    SetMapObjFlags(0x5, 0x4)
    Jump("loc_7D4")

    label("loc_7C9")

    ClearChrFlags(0xB, 0x8)
    ClearMapObjFlags(0x5, 0x4)

    label("loc_7D4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_807")
    SetChrFlags(0xC, 0x8)
    Jump("loc_80C")

    label("loc_807")

    ClearChrFlags(0xC, 0x8)

    label("loc_80C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_837")
    SetChrFlags(0xD, 0x8)
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    Jump("loc_846")

    label("loc_837")

    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)

    label("loc_846")

    Return()

    # Function_2_7AB end

    def Function_3_847(): pass

    label("Function_3_847")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_934")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('痊愈之药', 1)"), scpexpr(EXPR_END)), "loc_8C6")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x10F, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_92F")

    label("loc_8C6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '痊愈之药'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_92F")

    Jump("loc_971")

    label("loc_934")

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

    label("loc_971")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_847 end

    def Function_4_97D(): pass

    label("Function_4_97D")

    EventBegin(0x0)
    Fade(1000)
    OP_E0(0x1)
    OP_68(44510, 900, 18470, 0)
    MoveCamera(40, 18, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22760, 0)
    OP_68(46010, 900, 18470, 2500)
    SetChrPos(0x101, 42280, 0, 18600, 270)
    SetChrPos(0x102, 42280, 0, 17300, 270)
    SetChrPos(0x103, 43580, 0, 17300, 270)
    SetChrPos(0x104, 43580, 0, 18600, 270)
    SetChrPos(0x106, 44880, 0, 17950, 270)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_6F(0x1)
    OP_0D()
    SetMessageWindowPos(230, 40, -1, -1)
    SetChrName("声音")

    #A0004
    AnonymousTalk(
        0xFF,
        "#1S……既然如此……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 30, -1, -1)
    SetChrName("声音")

    #A0005
    AnonymousTalk(
        0xFF,
        "#1S………啊啊……给我………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
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
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_B11():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B11)

    def lambda_B1E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B1E)
    Sleep(100)

    def lambda_B2E():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B2E)

    def lambda_B3B():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B3B)
    Sleep(100)

    def lambda_B4B():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B4B)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    #C0006
    ChrTalk(
        0x103,
        "#0201F#6P是从那个房间里传出来的。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0301F#6P是来不及逃走的\x01",
            "教授们，还是……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#0013F#6P……总之，去调查一下吧。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetChrPos(0x0, 43500, 0, 17800, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_1B(0x3, 0x0, 0xB)
    SetScenarioFlags(0xE3, 1)
    OP_E0(0x1)
    EventEnd(0x5)
    Return()

    # Function_4_97D end

    def Function_5_C0E(): pass

    label("Function_5_C0E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch32700.itc", 0x1E)
    LoadChrToIndex("chr/ch32900.itc", 0x1F)
    LoadChrToIndex("chr/ch29200.itc", 0x20)
    LoadEffect(0x0, "event\\ev604_00.eff")
    OP_68(49400, 1200, 53960, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, 49400, 0, 49000, 0)
    SetChrPos(0x102, 50600, 0, 49000, 0)
    SetChrPos(0x103, 49400, 0, 47800, 0)
    SetChrPos(0x104, 50600, 0, 47800, 0)
    SetChrPos(0x106, 50000, 0, 46600, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrPos(0x8, 47600, 0, 57000, 180)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrPos(0x9, 50000, 0, 57000, 180)
    SetChrChipByIndex(0xA, 0x20)
    SetChrSubChip(0xA, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrPos(0xA, 48800, 0, 57000, 180)
    FadeToBright(1000, 0)
    OP_68(49400, 1200, 54960, 2500)

    def lambda_D8F():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_D8F)
    Sleep(50)

    def lambda_DA7():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DA7)
    Sleep(50)

    def lambda_DBF():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DBF)
    Sleep(50)

    def lambda_DD7():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DD7)
    Sleep(50)

    def lambda_DEF():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_DEF)
    Sleep(200)

    def lambda_E07():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E07)
    Sleep(50)

    def lambda_E1B():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E1B)
    Sleep(500)

    def lambda_E2F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E2F)
    Sleep(50)

    def lambda_E43():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E43)
    Sleep(500)

    def lambda_E57():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_E57)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x106, 2)
    OP_6F(0x1)
    OP_0D()

    #N0009
    NpcTalk(
        0x9,
        "女性的声音",
        "#5P#2S过、过来了～！\x02",
    )

    CloseMessageWindow()
    OP_68(49400, 1200, 55460, 1000)
    OP_6F(0x1)

    #N0010
    NpcTalk(
        0x8,
        "男性的声音",
        "#5P哼，吃我一招！\x02",
    )

    CloseMessageWindow()

    #N0011
    NpcTalk(
        0xA,
        "老人的声音",
        "#5P去死吧，可恶的怪物！\x02",
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
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x101,
        "#0005F#11P哎……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 9)
    BeginChrThread(0xA, 3, 0, 10)
    OP_68(49400, 1200, 54460, 2000)
    Sleep(1500)
    Sound(949, 0, 100, 0)

    def lambda_FD2():
        OP_9D(0xFE, 0xBEF0, 0x0, 0xCF12, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FD2)

    def lambda_FEF():
        OP_9D(0xFE, 0xC878, 0x0, 0xCF58, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FEF)

    def lambda_100C():
        OP_9D(0xFE, 0xBE32, 0x32, 0xC8DC, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_100C)

    def lambda_1029():
        OP_9D(0xFE, 0xC88C, 0x32, 0xC832, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1029)

    def lambda_1046():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1046)

    def lambda_1060():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1060)

    def lambda_106D():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_106D)

    def lambda_107A():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_107A)

    def lambda_1087():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1087)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    WaitChrThread(0x103, 2)
    WaitChrThread(0x104, 2)
    WaitChrThread(0x8, 1)
    OP_6F(0x1)

    #C0013
    ChrTalk(
        0x104,
        "#0305F#11P哇……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0101F#11P啊，危险……\x02",
    )

    CloseMessageWindow()
    OP_68(49400, 1200, 54960, 1500)

    def lambda_1105():
        TurnDirection(0xFE, 0xA, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1105)

    def lambda_1112():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1112)
    Sleep(100)

    def lambda_1122():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1122)

    def lambda_112F():
        TurnDirection(0xFE, 0xA, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_112F)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x1)
    OP_63(0xA, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xA, 0x8, 500)

    #N0015
    NpcTalk(
        0xA,
        "老人的声音",
        "#11P笨蛋，你往哪里扔啊！\x02",
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0xA,
        "老人的声音",
        (
            "#11P真是受不了，\x01",
            "你这无能的外科医生……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0xA, 500)

    #N0017
    NpcTalk(
        0x8,
        "男性的声音",
        (
            "#1P你怎么不说自己啊，\x01",
            "你不是也扔偏了吗！\x02",
        )
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x8,
        "男性的声音",
        (
            "#1P所以说，你们内科医生\x01",
            "只会耍嘴皮子罢了！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    #N0019
    NpcTalk(
        0x9,
        "女性的声音",
        "#11P那个……两位医生。\x02",
    )

    CloseMessageWindow()

    #N0020
    NpcTalk(
        0x9,
        "女性的声音",
        (
            "#11P他们好像\x01",
            "不是魔兽哦。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_12E5():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_12E5)

    def lambda_12F2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_12F2)
    Sleep(100)

    def lambda_1302():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1302)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    Sleep(1000)
    OP_68(48480, 1200, 54180, 3500)

    def lambda_132F():

        label("loc_132F")

        TurnDirection(0x101, 0xA, 500)
        Yield()
        Jump("loc_132F")

    QueueWorkItem2(0x101, 1, lambda_132F)

    def lambda_1341():

        label("loc_1341")

        TurnDirection(0x102, 0xA, 500)
        Yield()
        Jump("loc_1341")

    QueueWorkItem2(0x102, 1, lambda_1341)

    def lambda_1353():

        label("loc_1353")

        TurnDirection(0x103, 0xA, 500)
        Yield()
        Jump("loc_1353")

    QueueWorkItem2(0x103, 1, lambda_1353)

    def lambda_1365():

        label("loc_1365")

        TurnDirection(0x104, 0xA, 500)
        Yield()
        Jump("loc_1365")

    QueueWorkItem2(0x104, 1, lambda_1365)

    def lambda_1377():

        label("loc_1377")

        TurnDirection(0x106, 0xA, 500)
        Yield()
        Jump("loc_1377")

    QueueWorkItem2(0x106, 1, lambda_1377)
    BeginChrThread(0x8, 3, 0, 7)
    Sleep(100)
    BeginChrThread(0xA, 3, 0, 6)
    Sleep(100)
    BeginChrThread(0x9, 3, 0, 8)
    WaitChrThread(0xA, 3)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    EndChrThread(0x101, 0x1)
    EndChrThread(0x102, 0x1)
    EndChrThread(0x103, 0x1)
    EndChrThread(0x104, 0x1)
    EndChrThread(0x106, 0x1)
    OP_6F(0x1)

    #C0021
    ChrTalk(
        0xA,
        "#5P哦哦，你们是……！？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "#5P没记错的话，是克洛斯贝尔警察局的……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0012F#11P……我们是特别任务支援科的人，\x01",
            "大家好像平安无事呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#0300F#11P哎呀呀……\x01",
            "没想到竟然把\x01",
            "药品扔了过来。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#0211F#11P这个，是某种强酸吗？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "#5P对、对不起……\x01",
            "是试验用的酸化液。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#5P虽、虽然刺激性有些强，\x01",
            "但是没有毒性，还请放心。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    #C0028
    ChrTalk(
        0x9,
        (
            "#5P两位可真是的，\x01",
            "以后可不能再这么鲁莽了啊～\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_1578():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1578)
    Sleep(50)

    def lambda_1588():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1588)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x8, 1)

    #C0029
    ChrTalk(
        0x8,
        (
            "#6P是阿修拉狂喊着\x01",
            "『过来了』吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "#12P而且发现酸化瓶的人\x01",
            "也是你吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        "#5P咦？是这样吗？\x02",
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1200)

    #C0032
    ChrTalk(
        0x101,
        (
            "#0001F#11P总、总之，还有魔兽\x01",
            "在医院内部游荡。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0100F#11P我们会担任护卫，\x01",
            "大家先从这里出去吧。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(23000, 2000)
    OP_6F(0x79)
    OP_0D()
    SetScenarioFlags(0x5C, 2)
    NewScene("t160B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_5_C0E end

    def Function_6_16F0(): pass

    label("Function_6_16F0")


    def lambda_16F5():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_16F5)
    WaitChrThread(0xFE, 1)

    def lambda_1713():
        OP_95(0xFE, 45910, 0, 54880, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1713)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_6_16F0 end

    def Function_7_1734(): pass

    label("Function_7_1734")


    def lambda_1739():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1739)
    WaitChrThread(0xFE, 1)

    def lambda_1757():
        OP_95(0xFE, 44750, 0, 55520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1757)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_7_1734 end

    def Function_8_1778(): pass

    label("Function_8_1778")


    def lambda_177D():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_177D)
    WaitChrThread(0xFE, 1)

    def lambda_179B():
        OP_95(0xFE, 45790, 0, 56050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_179B)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_8_1778 end

    def Function_9_17BC(): pass

    label("Function_9_17BC")


    def lambda_17C1():
        OP_9D(0xFE, 0xB9F0, 0x0, 0xDEA8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17C1)
    Sleep(150)
    Sound(814, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 0, 52500, 330, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_9_17BC end

    def Function_10_181A(): pass

    label("Function_10_181A")

    Sleep(100)

    def lambda_1822():
        OP_9D(0xFE, 0xBEA0, 0x0, 0xDEA8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1822)
    Sleep(150)
    Sound(541, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 0, 52500, 345, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_10_181A end

    def Function_11_187B(): pass

    label("Function_11_187B")

    EventBegin(0x1)

    #C0034
    ChrTalk(
        0x101,
        (
            "#0001F很在意刚才的说话声……\x01",
            "先去那边调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 41500, 0, 18000, 90)
    EventEnd(0x4)
    Return()

    # Function_11_187B end

    SaveToFile()

Try(main)
