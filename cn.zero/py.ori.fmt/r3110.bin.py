from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "r3110.bin",                # FileName
        "r3110",                    # MapName
        "r3110",                    # Location
        0x0066,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 6000, 0, -61500, 0, 0, 1, 102, 0, 0, 0, 1],
    )

    BuildStringList((
        "r3110",                  # 0
        "br3100",                 # 1
        "br3100",                 # 2
        "br3100",                 # 3
    ))

    ATBonus("ATBonus_1E8", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_ABB", 0,   2,   16,  10,  4,   3,   5)
    Sepith("Sepith_ACB", 8,   15,  9,   10,  0,   0,   0)
    Sepith("Sepith_AC3", 8,   6,   0,   12,  5,   5,   5)

    MonsterBattlePostion("MonsterBattlePostion_248", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_24C", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_254", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_258", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_25C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_228", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_22C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_230", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_234", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_238", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_23C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_240", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_244", 2, 13, 180)

    # monster count: 4

    BattleInfo(
        "BattleInfo_2C8", 0x0000, 25, 6, 60, 6, 1, 30, 0, "br3100", "Sepith_ABB", 50, 50, 0, 0,
        (
            ("ms69200.dat", "ms69200.dat", "ms69200.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_248", "MonsterBattlePostion_2A8", "ed7400", "ed7403", "ATBonus_1E8"),
            ("ms69200.dat", "ms69200.dat", "ms69200.dat", "ms69200.dat", 0, 0, 0, 0, "MonsterBattlePostion_228", "MonsterBattlePostion_2A8", "ed7400", "ed7403", "ATBonus_1E8"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3A8", 0x0000, 25, 6, 60, 6, 1, 30, 0, "br3100", "Sepith_ACB", 50, 50, 0, 0,
        (
            ("ms77000.dat", "ms71400.dat", "ms77000.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_248", "MonsterBattlePostion_2A8", "ed7400", "ed7403", "ATBonus_1E8"),
            ("ms77000.dat", "ms77000.dat", "ms71400.dat", "ms77000.dat", 0, 0, 0, 0, "MonsterBattlePostion_228", "MonsterBattlePostion_2A8", "ed7400", "ed7403", "ATBonus_1E8"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_338", 0x0000, 25, 6, 60, 6, 1, 30, 0, "br3100", "Sepith_AC3", 50, 50, 0, 0,
        (
            ("ms71400.dat", "ms71400.dat", "ms71400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_248", "MonsterBattlePostion_2A8", "ed7400", "ed7403", "ATBonus_1E8"),
            ("ms71400.dat", "ms71400.dat", "ms71400.dat", "ms71400.dat", 0, 0, 0, 0, "MonsterBattlePostion_228", "MonsterBattlePostion_2A8", "ed7400", "ed7403", "ATBonus_1E8"),
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
        "monster/ch69250.itc",               # 10
        "monster/ch69250.itc",               # 11
        "monster/ch71450.itc",               # 12
        "monster/ch71450.itc",               # 13
        "monster/ch77050.itc",               # 14
        "monster/ch77051.itc",               # 15
    ))

    DeclMonster(6040,    -34790,  0,       0x1010000,    "BattleInfo_2C8", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-6390,   -11530,  0,       0x1010000,    "BattleInfo_3A8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-6570,   25080,   0,       0x1010000,    "BattleInfo_338", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(5920,    980,     0,       0x1010000,    "BattleInfo_2C8", 0,   16,  0xFFFF, 0,  1)

    DeclActor(6000,    100,     -10500,  1200,    6000,    1100,    -10500,  0x007C, 0,  2,  0x0000)
    DeclActor(-6000,   100,     28500,   1200,    -6000,   1100,    28500,   0x007C, 0,  3,  0x0000)
    DeclActor(6000,    100,     -22500,  1200,    6000,    1100,    -22500,  0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_474",          # 00, 0
        "Function_1_475",          # 01, 1
        "Function_2_6D1",          # 02, 2
        "Function_3_807",          # 03, 3
        "Function_4_93D",          # 04, 4
    ))


    def Function_0_474(): pass

    label("Function_0_474")

    Return()

    # Function_0_474 end

    def Function_1_475(): pass

    label("Function_1_475")

    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_698")
    OP_70(0x0, 0x0)
    Jump("loc_69C")

    label("loc_698")

    OP_70(0x0, 0x1E)

    label("loc_69C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AF")
    OP_70(0x1, 0x0)
    Jump("loc_6B3")

    label("loc_6AF")

    OP_70(0x1, 0x1E)

    label("loc_6B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6C6")
    OP_70(0x2, 0x0)
    Jump("loc_6CA")

    label("loc_6C6")

    OP_70(0x2, 0x1E)

    label("loc_6CA")

    Sound(127, 1, 100, 0)
    Return()

    # Function_1_475 end

    def Function_2_6D1(): pass

    label("Function_2_6D1")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7BE")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_750")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
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
    SetScenarioFlags(0x108, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_7B9")

    label("loc_750")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
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

    label("loc_7B9")

    Jump("loc_7FB")

    label("loc_7BE")

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

    label("loc_7FB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_6D1 end

    def Function_3_807(): pass

    label("Function_3_807")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F4")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x35, 1)"), scpexpr(EXPR_END)), "loc_886")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x35),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x108, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_8EF")

    label("loc_886")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x35),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x35),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8EF")

    Jump("loc_931")

    label("loc_8F4")

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

    label("loc_931")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_807 end

    def Function_4_93D(): pass

    label("Function_4_93D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A2A")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_9BC")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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
    SetScenarioFlags(0x108, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_A25")

    label("loc_9BC")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
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

    label("loc_A25")

    Jump("loc_A67")

    label("loc_A2A")

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

    label("loc_A67")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_93D end

    SaveToFile()

Try(main)
