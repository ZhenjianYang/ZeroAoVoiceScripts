from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ゲイリー教授",           # 1
        "アーシュラ主任",         # 2
        "ラゴー教授",             # 3
        "bt162b",                 # 4
        "bt162b",                 # 5
    ))

    ATBonus("ATBonus_20C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_19BC", 3,   14,  4,   4,   12,  12,  12)
    Sepith("Sepith_19B4", 13,  13,  24,  10,  0,   0,   0)

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
        "BattleInfo_3B4", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_19BC", 30, 45, 20, 5,
        (
            ("ms75701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_24C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, "MonsterBattlePostion_24C", "MonsterBattlePostion_2CC", "ed7402", "ed7403", "ATBonus_20C"),
        )
    )

    BattleInfo(
        "BattleInfo_2EC", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_19B4", 30, 45, 20, 5,
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
        "Function_4_994",          # 04, 4
        "Function_5_C31",          # 05, 5
        "Function_6_179D",         # 06, 6
        "Function_7_17E1",         # 07, 7
        "Function_8_1825",         # 08, 8
        "Function_9_1869",         # 09, 9
        "Function_10_18C7",        # 0A, 10
        "Function_11_1928",        # 0B, 11
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_943")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_8CC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
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
    SetScenarioFlags(0x10F, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_93E")

    label("loc_8CC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
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
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_93E")

    Jump("loc_988")

    label("loc_943")

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

    label("loc_988")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_847 end

    def Function_4_994(): pass

    label("Function_4_994")

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
    SetChrName("声")

    #A0004
    AnonymousTalk(
        0xFF,
        "#1S……こうなったら……\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 30, -1, -1)
    SetChrName("声")

    #A0005
    AnonymousTalk(
        0xFF,
        "#1S………ああ……くれる………\x02",
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

    def lambda_B2A():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_B2A)

    def lambda_B37():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_B37)
    Sleep(100)

    def lambda_B47():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_B47)

    def lambda_B54():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_B54)
    Sleep(100)

    def lambda_B64():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_B64)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    #C0006
    ChrTalk(
        0x103,
        "#0201F#6Pそこの部屋からです。\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0301F#6P逃げ遅れたっていう\x01",
            "教授たちか、それとも……\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x101,
        "#0013F#6P……とにかく調べてみよう。\x02",
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

    # Function_4_994 end

    def Function_5_C31(): pass

    label("Function_5_C31")

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

    def lambda_DB2():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_DB2)
    Sleep(50)

    def lambda_DCA():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_DCA)
    Sleep(50)

    def lambda_DE2():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_DE2)
    Sleep(50)

    def lambda_DFA():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_DFA)
    Sleep(50)

    def lambda_E12():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_E12)
    Sleep(200)

    def lambda_E2A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_E2A)
    Sleep(50)

    def lambda_E3E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_E3E)
    Sleep(500)

    def lambda_E52():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_E52)
    Sleep(50)

    def lambda_E66():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_E66)
    Sleep(500)

    def lambda_E7A():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_E7A)
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
        "女性の声",
        "#5P#2Sき、来ました～！\x02",
    )

    CloseMessageWindow()
    OP_68(49400, 1200, 55460, 1000)
    OP_6F(0x1)

    #N0010
    NpcTalk(
        0x8,
        "男性の声",
        "#5Pええい、これでも喰らえ！\x02",
    )

    CloseMessageWindow()

    #N0011
    NpcTalk(
        0xA,
        "老人の声",
        "#5Pくたばれ、化物があっ！\x02",
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
        "#0005F#11Pえ……\x02",
    )

    CloseMessageWindow()
    BeginChrThread(0x8, 3, 0, 9)
    BeginChrThread(0xA, 3, 0, 10)
    OP_68(49400, 1200, 54460, 2000)
    Sleep(1500)
    Sound(949, 0, 100, 0)

    def lambda_FFD():
        OP_9D(0xFE, 0xBEF0, 0x0, 0xCF12, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FFD)

    def lambda_101A():
        OP_9D(0xFE, 0xC878, 0x0, 0xCF58, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_101A)

    def lambda_1037():
        OP_9D(0xFE, 0xBE32, 0x32, 0xC8DC, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1037)

    def lambda_1054():
        OP_9D(0xFE, 0xC88C, 0x32, 0xC832, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1054)

    def lambda_1071():
        OP_98(0xFE, 0x0, 0x0, 0xFFFFFED4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1071)

    def lambda_108B():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_108B)

    def lambda_1098():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1098)

    def lambda_10A5():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_10A5)

    def lambda_10B2():
        OP_93(0xFE, 0x13B, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_10B2)
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
        "#0305F#11Pうおっ……！？\x02",
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x102,
        "#0101F#11Pあ、危な……\x02",
    )

    CloseMessageWindow()
    OP_68(49400, 1200, 54960, 1500)

    def lambda_1134():
        TurnDirection(0xFE, 0xA, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1134)

    def lambda_1141():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1141)
    Sleep(100)

    def lambda_1151():
        TurnDirection(0xFE, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1151)

    def lambda_115E():
        TurnDirection(0xFE, 0xA, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_115E)
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
        "老人の声",
        "#11P馬鹿者、何を外しておるか！\x02",
    )

    CloseMessageWindow()

    #N0016
    NpcTalk(
        0xA,
        "老人の声",
        (
            "#11Pまったくこれだから\x01",
            "無能な外科医師はっ……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x8, 0xA, 500)

    #N0017
    NpcTalk(
        0x8,
        "男性の声",
        (
            "#1Pそういうアンタこそ\x01",
            "思いっきり外しただろうが！\x02",
        )
    )

    CloseMessageWindow()

    #N0018
    NpcTalk(
        0x8,
        "男性の声",
        (
            "#1Pこれだから内科医師は\x01",
            "口先ばかりで使えんのだ！\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0xA, 500)

    #N0019
    NpcTalk(
        0x9,
        "女性の声",
        "#11Pあのぉ……先生方。\x02",
    )

    CloseMessageWindow()

    #N0020
    NpcTalk(
        0x9,
        "女性の声",
        (
            "#11Pなんか魔獣じゃ\x01",
            "なかったみたいですけど。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0xA, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1334():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_1334)

    def lambda_1341():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1341)
    Sleep(100)

    def lambda_1351():
        TurnDirection(0xFE, 0x101, 300)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1351)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)
    Sleep(1000)
    OP_68(48480, 1200, 54180, 3500)

    def lambda_137E():

        label("loc_137E")

        TurnDirection(0x101, 0xA, 500)
        Yield()
        Jump("loc_137E")

    QueueWorkItem2(0x101, 1, lambda_137E)

    def lambda_1390():

        label("loc_1390")

        TurnDirection(0x102, 0xA, 500)
        Yield()
        Jump("loc_1390")

    QueueWorkItem2(0x102, 1, lambda_1390)

    def lambda_13A2():

        label("loc_13A2")

        TurnDirection(0x103, 0xA, 500)
        Yield()
        Jump("loc_13A2")

    QueueWorkItem2(0x103, 1, lambda_13A2)

    def lambda_13B4():

        label("loc_13B4")

        TurnDirection(0x104, 0xA, 500)
        Yield()
        Jump("loc_13B4")

    QueueWorkItem2(0x104, 1, lambda_13B4)

    def lambda_13C6():

        label("loc_13C6")

        TurnDirection(0x106, 0xA, 500)
        Yield()
        Jump("loc_13C6")

    QueueWorkItem2(0x106, 1, lambda_13C6)
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
        "#5Pおお、君たちは……！？\x02",
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x8,
        "#5Pたしかクロスベル警察の……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x101,
        (
            "#0012F#11P……特務支援課の者です。\x01",
            "皆さん、ご無事みたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x104,
        (
            "#0300F#11Pやれやれ……\x01",
            "まさか薬品を投げられるとは\x01",
            "思いもしなかったぜ。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x103,
        "#0211F#11Pこれ、酸か何かですか？\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0xA,
        (
            "#5Pす、すまん……\x01",
            "実験用の酸化液なんだが。\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x8,
        (
            "#5Pた、多少刺激は強いが\x01",
            "毒性はないから安心してくれ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x9, 0xE1, 0x1F4)

    #C0028
    ChrTalk(
        0x9,
        (
            "#5Pまったくお２人とも。\x01",
            "軽はずみはいけませんよ～。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x8, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    OP_63(0xA, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    def lambda_15E7():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_15E7)
    Sleep(50)

    def lambda_15F7():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_15F7)
    WaitChrThread(0xA, 1)
    WaitChrThread(0x8, 1)

    #C0029
    ChrTalk(
        0x8,
        (
            "#6P『来ました』と言ったのは\x01",
            "アーシュラ君じゃないか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0xA,
        (
            "#12P酸化液のビンを見つけたのも\x01",
            "君だったと思うが……？\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x9,
        "#5Pあれれ、そうでしたっけ？\x02",
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
            "#0001F#11Pと、とにかく内部は\x01",
            "まだ魔獣が徘徊しています。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x102,
        (
            "#0100F#11P護衛しますので\x01",
            "いったんここから出ましょう。\x02",
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

    # Function_5_C31 end

    def Function_6_179D(): pass

    label("Function_6_179D")


    def lambda_17A2():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17A2)
    WaitChrThread(0xFE, 1)

    def lambda_17C0():
        OP_95(0xFE, 45910, 0, 54880, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17C0)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_6_179D end

    def Function_7_17E1(): pass

    label("Function_7_17E1")


    def lambda_17E6():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17E6)
    WaitChrThread(0xFE, 1)

    def lambda_1804():
        OP_95(0xFE, 44750, 0, 55520, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1804)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_7_17E1 end

    def Function_8_1825(): pass

    label("Function_8_1825")


    def lambda_182A():
        OP_95(0xFE, 45000, 0, 57020, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_182A)
    WaitChrThread(0xFE, 1)

    def lambda_1848():
        OP_95(0xFE, 45790, 0, 56050, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1848)
    WaitChrThread(0xFE, 1)
    TurnDirection(0xFE, 0x101, 500)
    Return()

    # Function_8_1825 end

    def Function_9_1869(): pass

    label("Function_9_1869")


    def lambda_186E():
        OP_9D(0xFE, 0xB9F0, 0x0, 0xDEA8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_186E)
    Sleep(150)
    Sound(814, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 0, 52500, 330, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_9_1869 end

    def Function_10_18C7(): pass

    label("Function_10_18C7")

    Sleep(100)

    def lambda_18CF():
        OP_9D(0xFE, 0xBEA0, 0x0, 0xDEA8, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18CF)
    Sleep(150)
    Sound(541, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xFF, 0x0, 50000, 0, 52500, 345, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Return()

    # Function_10_18C7 end

    def Function_11_1928(): pass

    label("Function_11_1928")

    EventBegin(0x1)

    #C0034
    ChrTalk(
        0x101,
        (
            "#0001Fさっきの人の声が気になる……\x01",
            "先にそっちを調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 41500, 0, 18000, 90)
    EventEnd(0x4)
    Return()

    # Function_11_1928 end

    SaveToFile()

Try(main)
