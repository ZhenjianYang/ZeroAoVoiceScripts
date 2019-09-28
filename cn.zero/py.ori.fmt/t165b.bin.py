from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t165b.bin",                # FileName
        "t165b",                    # MapName
        "t165b",                    # Location
        0x0058,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 88, 0, 0, 0, 2],
    )

    BuildStringList((
        "t165b",                  # 0
        "阿奈斯特",               # 1
        "歼灭天使玲",             # 2
        "帕蒂尔·玛蒂尔",         # 3
        "阿奈斯特随员",           # 4
        "阿奈斯特随员",           # 5
        "SE控制",                 # 6
        "bt162b",                 # 7
        "bt162b",                 # 8
        "bt163b",                 # 9
    ))

    ATBonus("ATBonus_28C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_2AC", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_5947", 13,  13,  24,  10,  0,   0,   0)
    Sepith("Sepith_594F", 3,   14,  4,   4,   12,  12,  12)

    MonsterBattlePostion("MonsterBattlePostion_2EC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_350", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_354", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_358", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_35C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_360", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_364", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 4, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_378", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_37C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_380", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_384", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_388", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_38C", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_5947", 30, 45, 20, 5,
        (
            ("ms67501.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2EC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2EC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
        )
    )

    BattleInfo(
        "BattleInfo_454", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_594F", 30, 45, 20, 5,
        (
            ("ms75701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2EC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2EC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_51C", 0x0042, 34, 6, 0, 0, 0, 0, 0, "bt163b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02300.dat", "ms67201.dat", "ms67201.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_36C", "MonsterBattlePostion_34C", "ed7405", "ed7000", "ATBonus_2AC"),
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
        "monster/ch67550.itc",               # 10
        "monster/ch67551.itc",               # 11
        "monster/ch75750.itc",               # 12
        "monster/ch75750.itc",               # 13
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(-50170,  39240,   0,       0x1010000,    "BattleInfo_38C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-60420,  106890,  0,       0x1010000,    "BattleInfo_454", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(95760,   109010,  0,       0x1010000,    "BattleInfo_38C", 0,   16,  0xFFFF, 0,  1)

    DeclActor(109500,  0,       56500,   1500,    109500,  900,     56500,   0x007C, 0,  15, 0x0000)
    DeclActor(95000,   0,       113500,  1200,    95000,   1000,    113500,  0x007C, 0,  4,  0x0000)
    DeclActor(-50000,  0,       36500,   1200,    -50000,  1000,    36500,   0x007C, 0,  5,  0x0000)
    DeclActor(-62000,  0,       110000,  1200,    -62000,  1000,    110000,  0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_5E8",          # 00, 0
        "Function_1_655",          # 01, 1
        "Function_2_65C",          # 02, 2
        "Function_3_7ED",          # 03, 3
        "Function_4_869",          # 04, 4
        "Function_5_99F",          # 05, 5
        "Function_6_AD5",          # 06, 6
        "Function_7_C0B",          # 07, 7
        "Function_8_C27",          # 08, 8
        "Function_9_C46",          # 09, 9
        "Function_10_1CB7",        # 0A, 10
        "Function_11_1D00",        # 0B, 11
        "Function_12_1D49",        # 0C, 12
        "Function_13_2752",        # 0D, 13
        "Function_14_2795",        # 0E, 14
        "Function_15_2A6B",        # 0F, 15
        "Function_16_2CAF",        # 10, 16
        "Function_17_5169",        # 11, 17
        "Function_18_518E",        # 12, 18
        "Function_19_51E1",        # 13, 19
        "Function_20_5224",        # 14, 20
        "Function_21_58B8",        # 15, 21
    ))


    def Function_0_5E8(): pass

    label("Function_0_5E8")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_600")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 1)

    label("loc_600")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_61A")
    Event(0, 9)

    label("loc_61A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_62E")
    ClearScenarioFlags(0x5C, 0)
    Event(0, 12)
    Jump("loc_654")

    label("loc_62E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 1)), scpexpr(EXPR_END)), "loc_645")
    ClearScenarioFlags(0x5C, 1)
    SetScenarioFlags(0x0, 0)
    Event(0, 14)
    Jump("loc_654")

    label("loc_645")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 2)), scpexpr(EXPR_END)), "loc_654")
    ClearScenarioFlags(0x5C, 2)
    Event(0, 20)

    label("loc_654")

    Return()

    # Function_0_5E8 end

    def Function_1_655(): pass

    label("Function_1_655")

    Sound(160, 0, 100, 0)
    Return()

    # Function_1_655 end

    def Function_2_65C(): pass

    label("Function_2_65C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_671")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_671")

    OP_65(0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_END)), "loc_682")
    OP_66(0x0, 0x1)

    label("loc_682")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6DC")
    LoadEffect(0x7, "event\\ev617_00.eff")
    PlayEffect(0x7, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_6DC")

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
    OP_1B(0x1, 0xFF, 0xFFFF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7A4")
    OP_1B(0x1, 0x0, 0x15)

    label("loc_7A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7B7")
    OP_70(0x8, 0x0)
    Jump("loc_7BB")

    label("loc_7B7")

    OP_70(0x8, 0x1E)

    label("loc_7BB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7CE")
    OP_70(0x9, 0x0)
    Jump("loc_7D2")

    label("loc_7CE")

    OP_70(0x9, 0x1E)

    label("loc_7D2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7E5")
    OP_70(0xA, 0x0)
    Jump("loc_7E9")

    label("loc_7E5")

    OP_70(0xA, 0x1E)

    label("loc_7E9")

    Call(0, 3)
    Return()

    # Function_2_65C end

    def Function_3_7ED(): pass

    label("Function_3_7ED")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_80B")
    SetChrFlags(0xF, 0x8)
    SetMapObjFlags(0xA, 0x4)
    Jump("loc_816")

    label("loc_80B")

    ClearChrFlags(0xF, 0x8)
    ClearMapObjFlags(0xA, 0x4)

    label("loc_816")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_834")
    SetChrFlags(0x10, 0x8)
    SetMapObjFlags(0x8, 0x4)
    Jump("loc_83F")

    label("loc_834")

    ClearChrFlags(0x10, 0x8)
    ClearMapObjFlags(0x8, 0x4)

    label("loc_83F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_85D")
    SetChrFlags(0xE, 0x8)
    SetMapObjFlags(0x9, 0x4)
    Jump("loc_868")

    label("loc_85D")

    ClearChrFlags(0xE, 0x8)
    ClearMapObjFlags(0x9, 0x4)

    label("loc_868")

    Return()

    # Function_3_7ED end

    def Function_4_869(): pass

    label("Function_4_869")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_956")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('星辰灵摆', 1)"), scpexpr(EXPR_END)), "loc_8E8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_951")

    label("loc_8E8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_951")

    Jump("loc_993")

    label("loc_956")

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

    label("loc_993")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_869 end

    def Function_5_99F(): pass

    label("Function_5_99F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A8C")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x87, 1)"), scpexpr(EXPR_END)), "loc_A1E")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x87),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_A87")

    label("loc_A1E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x87),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x87),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A87")

    Jump("loc_AC9")

    label("loc_A8C")

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

    label("loc_AC9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_99F end

    def Function_6_AD5(): pass

    label("Function_6_AD5")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC2")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅱ', 1)"), scpexpr(EXPR_END)), "loc_B54")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
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
    SetScenarioFlags(0x115, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_BBD")

    label("loc_B54")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BBD")

    Jump("loc_BFF")

    label("loc_BC2")

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

    label("loc_BFF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_AD5 end

    def Function_7_C0B(): pass

    label("Function_7_C0B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C26")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_7_C0B")

    label("loc_C26")

    Return()

    # Function_7_C0B end

    def Function_8_C27(): pass

    label("Function_8_C27")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C45")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_C27")

    label("loc_C45")

    Return()

    # Function_8_C27 end

    def Function_9_C46(): pass

    label("Function_9_C46")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("chr/ch02300.itc", 0x23)
    LoadChrToIndex("chr/ch02350.itc", 0x24)
    LoadChrToIndex("chr/ch02351.itc", 0x25)
    LoadChrToIndex("monster/ch67250.itc", 0x26)
    LoadChrToIndex("monster/ch67251.itc", 0x27)
    LoadChrToIndex("chr/ch00051.itc", 0x28)
    LoadChrToIndex("chr/ch00151.itc", 0x29)
    LoadChrToIndex("chr/ch00251.itc", 0x2A)
    LoadChrToIndex("chr/ch00351.itc", 0x2B)
    LoadChrToIndex("chr/ch00551.itc", 0x2C)
    SoundLoad(861)
    OP_68(110910, 400, 58340, 0)
    OP_6E(440, 0)
    MoveCamera(38, 26, 0, 0)
    SetCameraDistance(23750, 0)
    SetChrPos(0x101, 99000, 0, 50600, 90)
    SetChrPos(0x102, 99000, 0, 49400, 90)
    SetChrPos(0x103, 97800, 0, 49400, 90)
    SetChrPos(0x104, 97800, 0, 50600, 90)
    SetChrPos(0x106, 96600, 0, 50000, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 113800, 0, 50000, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetChrChipByIndex(0xB, 0x26)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x20)
    OP_52(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xB, 112500, 0, 51300, 270)
    OP_A7(0xB, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xB, 0x80)
    ClearChrBattleFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x26)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x20)
    OP_52(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xD8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2D, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2E, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x2F, (scpexpr(EXPR_PUSH_LONG, 0x384), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrPos(0xC, 112500, 0, 48700, 270)
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0xC, 0x80)
    ClearChrBattleFlags(0xC, 0x8000)
    BeginChrThread(0xB, 0, 0, 8)
    BeginChrThread(0xC, 0, 0, 8)
    SetMapFlags(0x2000)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu06600.itp")
    LoadEffect(0x0, "event\\ev602_01.eff")
    LoadEffect(0x2, "event\\ev605_00.eff")
    FadeToBright(1000, 0)
    OP_68(102940, 400, 51730, 4000)
    MoveCamera(38, 26, 0, 4000)
    SetCameraDistance(23750, 4000)
    Sleep(2000)

    def lambda_F08():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F08)
    Sleep(50)

    def lambda_F20():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F20)
    Sleep(50)

    def lambda_F38():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F38)
    Sleep(50)

    def lambda_F50():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F50)
    Sleep(50)

    def lambda_F68():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_F68)
    Sleep(200)

    def lambda_F80():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F80)
    Sleep(50)

    def lambda_F94():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_F94)
    Sleep(500)

    def lambda_FA8():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FA8)
    Sleep(50)

    def lambda_FBC():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_FBC)
    Sleep(500)

    def lambda_FD0():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_FD0)
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
    OP_6F(0x79)
    OP_0D()
    #Sound(1902, 255, 100, 0)    #voice#Earnest
    Sleep(800)

    #N0010
    NpcTalk(
        0x8,
        "青年的声音",
        "#3P哼哼，来得很快啊，还真是出乎意料。\x02",
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
    OP_68(111800, 1200, 50000, 2500)
    MoveCamera(60, 16, 0, 2500)
    SetCameraDistance(19500, 2500)
    OP_6F(0x79)

    #C0011
    ChrTalk(
        0x101,
        "#0007F你是……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#0101F阿、阿奈斯特先生！？\x02",
    )

    CloseMessageWindow()
    Sound(1899, 255, 100, 0)    #voice#Earnest
    OP_93(0x8, 0x10E, 0x190)
    Sleep(600)
    OP_68(109660, 1100, 50060, 2500)
    MoveCamera(50, 19, 0, 2500)
    SetCameraDistance(20420, 2500)

    def lambda_115E():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_115E)
    Sleep(500)

    def lambda_1176():
        OP_95(0xFE, 108000, 0, 50650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1176)
    Sleep(50)

    def lambda_1193():
        OP_95(0xFE, 108000, 0, 49350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1193)
    Sleep(50)

    def lambda_11B0():
        OP_95(0xFE, 106750, 0, 49350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11B0)
    Sleep(50)

    def lambda_11CD():
        OP_95(0xFE, 106750, 0, 50650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_11CD)
    Sleep(50)

    def lambda_11EA():
        OP_95(0xFE, 105500, 0, 50000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_11EA)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x10)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0013
    AnonymousTalk(
        0x8,
        (
            "#30W你好啊，艾莉……\x01",
            "两个月没见了吧？\x02\x03",

            "虽然夜幕才刚刚降临，\x01",
            "但今晚的月色可真美啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x0, 0x0, 0x0)

    #C0014
    ChrTalk(
        0x102,
        (
            "#0101F#6P阿奈斯特先生…\x01",
            "你眼睛的颜色是……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P哼……似乎已\x01",
            "堕入魔道了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6610F#11P呵，这位是……\x01",
            "传说中的『银』大人竟然也在一起啊。\x02\x03",

            "#6613F要不是你多余生事的话，\x01",
            "我的立场本是坚如磐石……\x02\x03",

            "#6611F看样子，向你回礼的好机会\x01",
            "已经到来了呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#6P吾为影……\x01",
            "不会为人类所欺骗利用。\x02\x03",

            "即使是堕入魔道者亦不例外。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6610F#11P哼哼……真敢说大话。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#0201F#6P……看来，就是你\x01",
            "统领着那些魔兽吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0010F#6P更重要的是，你怎么\x01",
            "会在这种地方！？\x02\x03",

            "#0007F你不是应该在拘留所才对吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#6613F#11P哼哼，拘留所吗……\x02\x03",

            "#6610F那栋建筑物已经同这座医院一样，\x01",
            "落入『我们』的手中了。\x02",
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
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0022
    ChrTalk(
        0x101,
        "#0005F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0310F#6P拘留所的警备工作\x01",
            "应该是由贝尔加德门的\x01",
            "警备队负责的……\x02\x03",

            "黑手党竟然\x01",
            "袭击了那里吗！？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#6613F#11P呵呵……\x01",
            "那倒不是。\x02\x03",

            "#6610F顺便一提，不要把区区鲁巴彻\x01",
            "与我们混为一谈。\x02\x03",

            "他们只不过是傀儡罢了，\x01",
            "我们为了达成计划而操纵的傀儡。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#0006F#6P果然是这样吗……\x02\x03",

            "#0013F你们利用某种方法，操纵了\x01",
            "服用过『真知』的人，对吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#6600F#11P呵呵，没错……\x02\x03",

            "#6604F……一切都在我们那位\x01",
            "伟大『同志』的计划之中。\x02\x03",

            "#6610F他们不过就是一些我们为了完成\x01",
            "伟大仪式而利用的『棋子』而已！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#0101F#6P伟大的『同志』……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0003F#6P『Ｄ∴Ｇ教团』的残党，\x01",
            "潜藏在黑手党背后的人物……\x02\x03",

            "#0013F也就是──\x01",
            "这个房间的主人吗？\x02",
        )
    )

    CloseMessageWindow()
    OP_68(111600, 1000, 50000, 2500)
    MoveCamera(60, 26, 0, 2500)
    SetCameraDistance(19500, 2500)
    Sleep(300)
    Sound(1903, 255, 100, 0)    #voice#Earnest
    OP_6F(0x79)
    Sleep(500)
    OP_82(0xC8, 0x0, 0xBB8, 0x3E8)
    #Sound(1904, 255, 100, 0)    #voice#Earnest

    #C0029
    ChrTalk(
        0x8,
        "#4S#11P#20A哈哈哈哈哈哈哈……！！\x02",
    )
    #Auto

    Sleep(2400)
    StopBGM(0xFA0)
    Fade(500)
    Sound(868, 0, 100, 0)
    Sound(861, 2, 100, 0)
    OP_82(0x0, 0x258, 0x1770, 0x1F4)
    PlayEffect(0x0, 0x0, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2, 0x2, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(540, 0, 80, 0)
    Sound(531, 0, 100, 0)
    SetCameraDistance(21500, 800)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    OP_0D()
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(202, 0, 100, 0)
    BeginChrThread(0xB, 3, 0, 10)
    BeginChrThread(0xC, 3, 0, 11)
    WaitChrThread(0xB, 3)
    WaitChrThread(0xC, 3)
    OP_68(109660, 1100, 50060, 2500)
    MoveCamera(50, 19, 0, 2500)
    SetCameraDistance(20420, 2500)
    StopBGM(0x1F4)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7405", 0)
    Sleep(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    Sleep(200)
    SetChrChipByIndex(0x101, 0x28)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x29)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x2A)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x2B)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x2C)
    SetChrSubChip(0x106, 0x0)

    def lambda_1A94():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1A94)
    Sleep(50)

    def lambda_1AAC():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1AAC)
    Sleep(50)

    def lambda_1AC4():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1AC4)
    Sleep(50)

    def lambda_1ADC():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1ADC)
    Sleep(50)

    def lambda_1AF4():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1AF4)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x22)
    SetChrSubChip(0x106, 0x0)
    OP_6F(0x79)

    #C0030
    ChrTalk(
        0x101,
        "#0007F#6P什么……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0707F#6P#N这种阴森之气是……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0032
    ChrTalk(
        0x103,
        "#0207F#6P#N上级三属性的气息……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0033
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F#11P#30W──如想确认这点，\x01",
            "只需击退我即可……\x02\x03",

            "#6610F#30W击退这个在『同志』的引导下，\x01",
            "到达『真之睿智（真知）』境界的我……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0101F#6P…………！！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#0307F#6P来了……！\x02",
    )

    CloseMessageWindow()
    OP_5A()
    OP_24(0x35D)
    Battle("BattleInfo_51C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0xB, 0x0)
    EndChrThread(0xC, 0x0)
    EndChrThread(0xB, 0x1)
    EndChrThread(0xC, 0x1)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    Call(0, 12)
    Return()

    # Function_9_C46 end

    def Function_10_1CB7(): pass

    label("Function_10_1CB7")

    PlayEffect(0x0, 0x5, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_10_1CB7 end

    def Function_11_1D00(): pass

    label("Function_11_1D00")

    PlayEffect(0x0, 0x6, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_11_1D00 end

    def Function_12_1D49(): pass

    label("Function_12_1D49")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00051.itc", 0x1F)
    LoadChrToIndex("chr/ch00150.itc", 0x20)
    LoadChrToIndex("chr/ch00151.itc", 0x21)
    LoadChrToIndex("chr/ch00250.itc", 0x22)
    LoadChrToIndex("chr/ch00251.itc", 0x23)
    LoadChrToIndex("chr/ch00350.itc", 0x24)
    LoadChrToIndex("chr/ch00351.itc", 0x25)
    LoadChrToIndex("chr/ch00550.itc", 0x26)
    LoadChrToIndex("chr/ch00551.itc", 0x27)
    LoadChrToIndex("chr/ch02300.itc", 0x28)
    LoadChrToIndex("chr/ch02350.itc", 0x29)
    LoadChrToIndex("chr/ch02351.itc", 0x2A)
    LoadChrToIndex("chr/ch02353.itc", 0x2B)
    LoadChrToIndex("chr/ch02352.itc", 0x2C)
    SoundLoad(861)
    OP_68(109660, 1100, 50060, 0)
    MoveCamera(50, 19, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(18420, 0)
    SetChrPos(0x101, 107540, 0, 50360, 90)
    SetChrPos(0x102, 106840, 0, 48670, 90)
    SetChrPos(0x103, 105610, 0, 49480, 90)
    SetChrPos(0x104, 104460, 0, 50510, 90)
    SetChrPos(0x106, 105970, 0, 51390, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x26)
    SetChrSubChip(0x106, 0x0)
    SetChrChipByIndex(0x8, 0x2B)
    SetChrSubChip(0x8, 0x3)
    SetChrPos(0x8, 111000, 0, 50000, 270)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    SetMapFlags(0x2000)
    StopEffect(0x7, 0x0)
    LoadEffect(0x0, "event\\ev602_00.eff")
    PlayEffect(0x0, 0x0, 0x8, 0x140, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(861, 2, 100, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(20420, 2000)
    OP_6F(0x10)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2010")

    #C0036
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F#11P#30W哼哼……\x01",
            "不愧是『银』……\x02\x03",

            "#6610F竟能击退如今的我，\x01",
            "你似乎是比传闻中更加可怕的怪物啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P……哼…………\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6600F#11P#30W其他人竟然\x01",
            "也能纠缠到如此地步。\x02\x03",

            "#6604F老实说，这真是在预料之外啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2069")

    label("loc_2010")


    #C0039
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F#11P#30W哼哼……\x01",
            "竟然能纠缠到如此地步。\x02\x03",

            "#6600F老实说，这真是在预料之外啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2069")


    #C0040
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0108F#6P阿奈斯特先生……！\x01",
            "……你为什么要这样做……！\x02\x03",

            "#0103F背叛外公，\x01",
            "沦为邪恶教团的走狗……\x02\x03",

            "#0107F你为什么会\x01",
            "堕落至此啊！？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6605F#11P堕落……？\x01",
            "不，我只是察觉了真相而已。\x02\x03",

            "#6613F没错……如今我已明白。\x02\x03",

            "这片名为克洛斯贝尔的土地\x01",
            "究竟拥有何种意义……\x02\x03",

            "#6610F无需任何解释，我全都『明白』了啊！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0101F#6P什么……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#0206F#6P#N……莫名其妙……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0044
    ChrTalk(
        0x104,
        "#0301F#6P#N完全疯掉了啊……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0045
    ChrTalk(
        0x101,
        (
            "#0003F#6P──胡话就说到\x01",
            "这里为止吧。\x02\x03",

            "#0013F原市长秘书阿奈斯特·莱兹。\x02\x03",

            "根据自治州法，以人身伤害、扰乱治安、\x01",
            "非法侵占、使用违禁药物、越狱等嫌疑，\x01",
            "在此将你逮捕。\x02\x03",

            "#0007F老老实实束手就擒吧！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F#11P哼哼……\x01",
            "不必那么着急。\x02\x03",

            "夜晚才刚刚开始……\x01",
            "『同志』的好戏还在后面呢。\x02\x03",

            "#6610F那边有邀请函，\x01",
            "好好看个仔细吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F#6P什么……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(111440, 400, 58730, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17580, 2000)

    def lambda_2382():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2382)

    def lambda_238F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_238F)
    Sleep(100)

    def lambda_239F():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_239F)

    def lambda_23AC():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_23AC)
    Sleep(100)

    def lambda_23BC():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_23BC)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    #C0048
    ChrTalk(
        0x102,
        "#0105F#1P那是……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_68(109660, 1100, 50060, 0)
    MoveCamera(50, 19, 0, 0)
    SetCameraDistance(20420, 0)
    OP_6F(0x79)
    BeginChrThread(0xD, 1, 0, 13)
    StopEffect(0x0, 0x0)
    SetChrChipByIndex(0x8, 0x29)
    SetChrSubChip(0x8, 0x0)
    Sound(540, 0, 80, 0)
    Sound(531, 0, 100, 0)
    Sound(804, 0, 100, 0)
    OP_0D()

    #C0049
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6610F#11P哈哈……\x01",
            "那么，后会有期了……！\x02\x03",

            "前提是，你们能顺利跨越\x01",
            "位于前方的绝境……！\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_2524():
        OP_93(0xFE, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_2524)

    def lambda_2531():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2531)
    Sleep(50)

    def lambda_2541():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2541)
    Sleep(50)

    def lambda_2551():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2551)
    Sleep(50)

    def lambda_2561():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2561)
    Sleep(50)

    def lambda_2571():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2571)
    WaitChrThread(0x8, 1)
    OP_68(115300, 1200, 50000, 1000)
    MoveCamera(65, 13, 0, 1000)
    SetCameraDistance(15500, 1000)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_25B3():
        OP_9B(0x0, 0xFE, 0x0, 0x8FC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25B3)
    WaitChrThread(0x8, 1)
    SetChrSubChip(0x8, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_25D6():
        OP_9D(0xFE, 0x1C138, 0x2EE, 0xC350, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25D6)
    WaitChrThread(0x8, 1)
    Sound(854, 0, 100, 0)

    def lambda_25FD():
        OP_9D(0xFE, 0x1F338, 0xFFFFD8F0, 0xC350, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_25FD)
    WaitChrThread(0x8, 1)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)

    #C0050
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010F呜……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0707F休想逃跑……！\x02",
        )
    )

    CloseMessageWindow()
    OP_68(113000, 1200, 50000, 1500)
    MoveCamera(60, 26, 0, 1500)
    SetCameraDistance(21420, 1500)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x20)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x22)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x24)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0x26)
    SetChrSubChip(0x106, 0x0)

    def lambda_26AD():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26AD)

    def lambda_26C2():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26C2)

    def lambda_26D7():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_26D7)

    def lambda_26EC():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_26EC)

    def lambda_2701():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2701)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)
    OP_0D()
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x1FE), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x35D)
    SetScenarioFlags(0x5C, 0)
    NewScene("e3300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1D49 end

    def Function_13_2752(): pass

    label("Function_13_2752")

    OP_25(0x35D, 0x5A)
    Sleep(100)
    OP_25(0x35D, 0x50)
    Sleep(100)
    OP_25(0x35D, 0x46)
    Sleep(100)
    OP_25(0x35D, 0x3C)
    Sleep(100)
    OP_25(0x35D, 0x32)
    Sleep(100)
    OP_25(0x35D, 0x28)
    Sleep(100)
    OP_25(0x35D, 0x1E)
    Sleep(100)
    OP_25(0x35D, 0x14)
    Sleep(100)
    OP_25(0x35D, 0xA)
    Sleep(100)
    OP_24(0x35D)
    Return()

    # Function_13_2752 end

    def Function_14_2795(): pass

    label("Function_14_2795")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(114540, 900, 50290, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24200, 0)
    SetChrPos(0x101, 112980, 0, 50210, 90)
    SetChrPos(0x102, 112670, 0, 48780, 90)
    SetChrPos(0x103, 111040, 0, 48560, 90)
    SetChrPos(0x104, 111900, 0, 50560, 90)
    SetChrPos(0x106, 109870, 0, 49310, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapFlags(0x2000)
    StopEffect(0x7, 0x0)
    FadeToBright(1000, 0)
    OP_68(113040, 900, 50290, 3000)
    OP_6F(0x1)
    OP_0D()

    #C0052
    ChrTalk(
        0x101,
        "#0011F#5P……什么………\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#0101F#5P刚、刚才那是……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 3)), scpexpr(EXPR_END)), "loc_28CF")

    #C0054
    ChrTalk(
        0x103,
        (
            "#0206F#6P在『星见之塔』出现过的\x01",
            "太古翼龙……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_28F5")

    label("loc_28CF")


    #C0055
    ChrTalk(
        0x103,
        (
            "#0206F#6P好像是……\x01",
            "太古翼龙……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_28F5")


    #C0056
    ChrTalk(
        0x104,
        (
            "#0307F喂喂……\x01",
            "这也太夸张了吧？\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P哼……\x01",
            "看来是追不上了。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x106, 0x10E, 0x1F4)
    Sleep(300)

    #C0058
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#11P──时间宝贵，\x01",
            "立刻过目吧……\x02\x03",

            "看看那个所谓的『同志』\x01",
            "准备的什么邀请函。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29AB():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_29AB)

    def lambda_29B8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_29B8)
    Sleep(100)

    def lambda_29C8():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_29C8)

    def lambda_29D5():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_29D5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0059
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#11P啊……\x02\x03",

            "#0013F──嗯，说得对。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    SetCameraDistance(24700, 2000)
    Sleep(2000)
    SetChrPos(0x0, 106500, 0, 50000, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    OP_66(0x0, 0x1)
    SetScenarioFlags(0xE3, 5)
    OP_29(0x4D, 0x1, 0xE)
    PlayBGM("ed7526", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x20E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    EventEnd(0x5)
    Return()

    # Function_14_2795 end

    def Function_15_2A6B(): pass

    label("Function_15_2A6B")

    EventBegin(0x2)
    FadeToDark(300, 0, 100)
    CreatePortrait(0, 112, 8, 368, 264, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis176.itp")
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    SetChrName("")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "桌上放着黑色和\x01",
            "白色封皮的文件。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2C34")

    #A0061
    AnonymousTalk(
        0x101,
        "#0005F……这个标志是……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0062
    AnonymousTalk(
        0x103,
        (
            "#0201F……莫非这就是\x01",
            "『Ｄ∴Ｇ教团』的……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0063
    AnonymousTalk(
        0x102,
        (
            "#0101F而、而且好像和那个『僧院』\x01",
            "里的标志很像……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0064
    AnonymousTalk(
        0x104,
        (
            "#0301F是那个出现了\x01",
            "诡异恶魔的地方吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0065
    AnonymousTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F哦……\x01",
            "还有那种地方吗？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0066
    AnonymousTalk(
        0x101,
        (
            "#0006F……嗯，那个地方与之前\x01",
            "和你会面的那座『塔』很相似。\x02\x03",

            "#0013F先不提这些了──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE3, 6)

    label("loc_2C34")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【阅读文件】\x01",      # 0
            "【放弃】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0xFF, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C90"),
        (1, "loc_2CA7"),
        (SWITCH_DEFAULT, "loc_2CAC"),
    )


    label("loc_2C90")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x0, 0x1)
    Call(0, 16)
    Jump("loc_2CAC")

    label("loc_2CA7")

    Jump("loc_2CAC")

    label("loc_2CAC")

    EventEnd(0x3)
    Return()

    # Function_15_2A6B end

    def Function_16_2CAF(): pass

    label("Function_16_2CAF")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("chr/ch09500.itc", 0x1E)
    LoadChrToIndex("apl/ch50505.itc", 0x1F)
    LoadChrToIndex("chr/ch09501.itc", 0x20)
    LoadChrToIndex("apl/ch50115.itc", 0x21)
    SoundLoad(953)
    OP_68(109250, 1000, 56760, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25250, 0)
    SetChrPos(0x101, 107800, 0, 56800, 90)
    SetChrPos(0x102, 106700, 0, 56800, 90)
    SetChrPos(0x103, 107800, 0, 55700, 45)
    SetChrPos(0x104, 106700, 0, 58000, 135)
    SetChrPos(0x106, 108800, 0, 54400, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 0x1F)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x9, 114900, 600, 50000, 270)
    ClearChrFlags(0x9, 0x1)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis100.itp")
    LoadEffect(0x0, "event\\ev600_01.eff")
    LoadEffect(0x1, "event\\ev601_01.eff")
    FadeToBright(1000, 0)
    SetCameraDistance(24250, 4000)
    OP_6F(0x10)
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3EBC")
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    #A0067
    AnonymousTalk(
        0x102,
        "#0108F怎么会……这样……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0068
    AnonymousTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F……哼哼，真是世道中落啊。\x02\x03",

            "没想到竟连哈尔特曼议长\x01",
            "都被笼络了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0069
    AnonymousTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0303F看样子，似乎是被人握住了什么把柄，\x01",
            "被迫协助他们的……\x02\x03",

            "#0301F这个『乐园』是指什么？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0070
    AnonymousTalk(
        0x103,
        (
            "#0208F……不清楚。\x02\x03",

            "说不定是教团的\x01",
            "据点之一吧……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0071
    AnonymousTalk(
        0x101,
        (
            "#0003F总而言之，哈尔特曼议长\x01",
            "被『他』握住了把柄。\x02\x03",

            "#0013F所以指示鲁巴彻协助『他』\x01",
            "潜伏在克洛斯贝尔吗……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0072
    AnonymousTalk(
        0x102,
        (
            "#0110F……不可饶恕……\x01",
            "身为自治州的代表之一，\x01",
            "竟做出这等愚行……\x02\x03",

            "#0108F就因为这种人，\x01",
            "使外公长年辛苦操劳，\x01",
            "害得父亲舍弃了克洛斯贝尔……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0073
    AnonymousTalk(
        0x101,
        "#0008F艾莉……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0074
    AnonymousTalk(
        0x103,
        "#0208F……………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0x0, 0x0)

    #C0075
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#11P……要沉浸在感慨中，还为时尚早。\x02\x03",

            "根据这本黑皮文件的资料，\x01",
            "『真知』的制造场所似乎\x01",
            "并非医院，而是其它地方。\x02\x03",

            "而且，从其出货清单看来……\x01",
            "除了供给黑手党以外，\x01",
            "好像还有相当多的流出量。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#5P……嗯。\x01",
            "看样子，除了这里之外，\x01",
            "『他』还拥有其它据点……\x02\x03",

            "#0013F莫非行踪不明\x01",
            "的人们就在那里……？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#0203F#12P……很有可能呢。\x02\x03",

            "#0201F到底会在哪里呢……？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#0306F#1P鲁巴彻以外的\x01",
            "其他出货对象也很令人在意啊。\x02\x03",

            "#0301F喂，该不会是\x01",
            "『黑月』之类的吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11P哼，曹怎么可能会\x01",
            "天真单纯到染指那种东西……\x02\x03",

            "#0700F若要说可能性，\x01",
            "也许是某个野心勃勃的制药公司……\x02\x03",

            "或者就是恐怖分子、猎兵团，\x01",
            "以及各国的谍报机关吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        "#0303F#1P哼，的确如此……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#0106F#6P越来越痛恨克洛斯贝尔\x01",
            "这个地区的特异性了……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0006F#6P……嗯……\x02\x03",

            "#0001F──也确认一下\x01",
            "这边的白皮文件吧。\x02",
        )
    )

    CloseMessageWindow()
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis101.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis115.itp")
    CreatePortrait(3, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis127.itp")
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    #A0083
    AnonymousTalk(
        0x103,
        "#0208F…………！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0084
    AnonymousTalk(
        0x102,
        "#0110F这、这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0085
    AnonymousTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F唔……\x01",
            "是六年前那些『仪式』的受害者们啊。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0086
    AnonymousTalk(
        0x104,
        (
            "#0311F……禽兽……\x01",
            "竟然做出这种勾当……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0087
    AnonymousTalk(
        0x101,
        (
            "#0003F………………………………\x02\x03",

            "#0008F……抱歉，缇欧。\x01",
            "我要确认里面的内容了……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0088
    AnonymousTalk(
        0x103,
        (
            "#0204F#30W……不需要道歉。\x02\x03",

            "#0202F请大家……\x01",
            "继续查看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0089
    AnonymousTalk(
        0x101,
        "#0003F嗯……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    CreatePortrait(2, 112, 65520, 368, 240, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis102.itp")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3645")
    OP_C9(0x2, 0x0, 0xFA00, 0x7D00, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)

    label("loc_3645")

    OP_C9(0x2, 0x1, 0x2EE, 0x2EE, 0x0)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x1F4)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)

    #A0090
    AnonymousTalk(
        0x101,
        "#0013F……！………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0091
    AnonymousTalk(
        0x103,
        (
            "#0213F#30W……啊哈哈…………\x02\x03",

            "#0212F和当时那副表情比起来……\x01",
            "我现在应该是好点了吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0092
    AnonymousTalk(
        0x101,
        "#0008F缇欧……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0093
    AnonymousTalk(
        0x102,
        "#0102F……那还用说吗……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0094
    AnonymousTalk(
        0x104,
        (
            "#0304F哈哈……你现在可爱得\x01",
            "简直判若两人呢。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0095
    AnonymousTalk(
        0x103,
        (
            "#0212F……就算是客套话，我也很开心。\x02\x03",

            "#0213F罗伊德前辈──请继续看吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0096
    AnonymousTalk(
        0x101,
        "#0003F……明白了。\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x1, 0x2, 0x0)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    OP_C9(0x1, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(1000)
    CreatePortrait(2, 112, 65520, 368, 240, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis103.itp")
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3898")
    OP_C9(0x2, 0x0, 0xFA00, 0x7D00, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    Jump("loc_38B6")

    label("loc_3898")

    OP_C9(0x2, 0x0, 0x1F400, 0x0, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)

    label("loc_38B6")

    OP_C9(0x2, 0x1, 0x2EE, 0x2EE, 0x0)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x1F4)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)

    #A0097
    AnonymousTalk(
        0x101,
        "#0005F啊……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0098
    AnonymousTalk(
        0x104,
        "#0301F这是……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0099
    AnonymousTalk(
        0x103,
        "#0208F……小玲……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0100
    AnonymousTalk(
        0x102,
        (
            "#0103F是吗……\x01",
            "果然有这层联系呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0101
    AnonymousTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F唔……\x01",
            "这个女孩也是你们认识的人吗？\x02\x03",

            "──当时，我在共和国的东方人街\x01",
            "也曾听过绑架事件的传闻……\x02\x03",

            "然而，没想到他们竟做出了\x01",
            "如此多的残酷之事。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0102
    AnonymousTalk(
        0x101,
        "#0003F………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x1, 0x2, 0x0)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_C9(0x1, 0x3, 0xFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x1, 0x3)
    Sleep(1000)
    Sound(18, 0, 100, 0)
    CreatePortrait(2, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x1, "c_vis104.itp")
    OP_C9(0x2, 0x1, 0x190, 0x190, 0x0)
    OP_C9(0x2, 0x0, 0x36B00, 0xBB80, 0x0)
    OP_C9(0x2, 0x2, 0xFFFF9E58, 0x0, 0x0)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x5DC, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x0, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)
    SetChrName("")

    #A0103
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "文件里夹着一张照片。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sound(18, 0, 100, 0)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x3E8)
    OP_C9(0x2, 0x0, 0x0, 0xFFFF5420, 0x3E8)
    OP_C9(0x2, 0x2, 0x0, 0x3E8, 0x0)
    OP_CA(0x0, 0x2, 0x1)
    Sleep(500)

    #A0104
    AnonymousTalk(
        0x101,
        "#0013F……唔……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0105
    AnonymousTalk(
        0x102,
        "#0107F小琪雅……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0106
    AnonymousTalk(
        0x103,
        "#0201F……怎么会……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0107
    AnonymousTalk(
        0x104,
        (
            "#0310F混账……\x01",
            "虽然已经有了心理准备……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0108
    AnonymousTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F是你们从那场竞拍会中\x01",
            "救出来的少女吧？\x02\x03",

            "似乎只有这张照片是新的，\x01",
            "也就是说，应该是在最近拍的吧……？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0109
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0006F嗯，多半如此……\x02\x03",

            "#0010F……可恶……！\x01",
            "原来从一开始就知道了吗……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_3D2D")

    #A0110
    AnonymousTalk(
        0x102,
        (
            "#0108F我们不久前带小琪雅\x01",
            "来这里的时候……\x02\x03",

            "#0101F『他』还装作毫不知情地\x01",
            "建议她住院检查呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3E20")

    label("loc_3D2D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_3DAC")

    #A0111
    AnonymousTalk(
        0x103,
        (
            "#0203F我们当时带琪雅\x01",
            "来这里的时候……\x02\x03",

            "#0201F『他』还摆出一副毫不知情的表情，\x01",
            "建议琪雅留下住院检查呢……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_3E20")

    label("loc_3DAC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_3E20")

    #A0112
    AnonymousTalk(
        0x104,
        (
            "#0303F在我们带阿琪\x01",
            "来这里的时候……\x02\x03",

            "#0310F『那家伙』还装出一副毫不知情的表情，\x01",
            "推荐她住院检查……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_3E20")

    StopBGM(0xFA0)
    Sleep(300)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrName("少女的声音")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            "#3P呵呵……\x01",
            "恐怕正是有所企图吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_68(109250, 1000, 56760, 0)
    MoveCamera(60, 17, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21890, 0)
    OP_C9(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    OP_CA(0x0, 0x0, 0x3)
    OP_CA(0x1, 0x2, 0x0)

    label("loc_3EBC")

    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
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

    #C0114
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0707F#11P什么……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#5P这声音是……\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    OP_68(115330, 1000, 50270, 2500)
    MoveCamera(67, 17, 0, 2500)

    def lambda_3FAB():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_3FAB)
    Sleep(50)

    def lambda_3FBB():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FBB)
    Sleep(50)

    def lambda_3FCB():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3FCB)
    Sleep(50)

    def lambda_3FDB():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3FDB)
    Sleep(50)

    def lambda_3FEB():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_3FEB)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0116
    ChrTalk(
        0x103,
        "#0205F啊……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        "#0105F小玲……！？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        "#0301F喂喂……真的假的！？\x02",
    )

    CloseMessageWindow()
    OP_5A()
    Fade(500)
    OP_68(112510, 1000, 51940, 0)
    MoveCamera(65, 15, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(26200, 0)
    SetChrPos(0x101, 108890, 0, 53750, 90)
    SetChrPos(0x102, 108080, 0, 52250, 90)
    SetChrPos(0x103, 107910, 0, 54870, 90)
    SetChrPos(0x104, 107150, 0, 53720, 90)
    SetChrPos(0x106, 107240, 0, 56080, 90)
    OP_68(112890, 1000, 51950, 2500)
    MoveCamera(57, 15, 0, 2500)
    OP_6E(400, 2500)
    SetCameraDistance(23650, 2500)

    def lambda_410B():
        OP_95(0xFE, 109970, 0, 51460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_410B)

    def lambda_4125():
        OP_95(0xFE, 109180, 0, 50270, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4125)

    def lambda_413F():
        OP_95(0xFE, 108860, 0, 52330, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_413F)

    def lambda_4159():
        OP_95(0xFE, 107860, 0, 51050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4159)

    def lambda_4173():
        OP_95(0xFE, 107760, 0, 52680, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4173)
    WaitChrThread(0x102, 1)

    def lambda_4191():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4191)
    WaitChrThread(0x101, 1)

    def lambda_41A2():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_41A2)
    WaitChrThread(0x103, 1)

    def lambda_41B3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_41B3)
    WaitChrThread(0x104, 1)

    def lambda_41C4():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_41C4)
    WaitChrThread(0x106, 1)

    def lambda_41D5():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_41D5)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)
    SetCameraDistance(23150, 80000)

    #C0119
    ChrTalk(
        0x101,
        (
            "#0001F#6P你……\x01",
            "从什么时候开始在那里的……？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P……完全没有感觉到气息……\x02\x03",

            "看来你并非等闲之辈呢。\x02",
        )
    )

    CloseMessageWindow()

    #N0121
    NpcTalk(
        0x9,
        "玲",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304F#11P呵呵……\x01",
            "和你差不多吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_CA(0x1, 0x3, 0x0)
    CreatePortrait(3, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "bu03300.itp")
    OP_C9(0x3, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0xFFFFD8F0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0122
    AnonymousTalk(
        0x9,
        (
            "──重新自我介绍一下。\x02\x03",

            "我是『噬身之蛇』的执行者，\x01",
            "Ｎｏ．ⅩⅤ──『歼灭天使』玲。\x02\x03",

            "呵呵，请多关照。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x3, 0x3, 0xFFFFFF, 0x1F4, 0x0)
    OP_C9(0x3, 0x0, 0x0, 0x0, 0x1F4)
    OP_CA(0x0, 0x3, 0x3)
    OP_CA(0x0, 0x3, 0x0)

    #C0123
    ChrTalk(
        0x101,
        "#0006F#6P正如艾丝蒂尔他们所说吗……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P『噬身之蛇』……\x01",
            "原来如此，是『瘦狼』的同类吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3305F#11P哎呀……\x01",
            "你认识瓦鲁特吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#6P之前曾经与他交过一次手。\x02\x03",

            "但最后并没有分出胜负，\x01",
            "让他逃掉了。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304F#11P呵呵，他大概\x01",
            "也是这样想的吧。\x02\x03",

            "#3302F玲要是回到『结社』的话，\x01",
            "也可以邀请他一起过来……\x02\x03",

            "#3309F还是说，邀请布卢布兰来\x01",
            "会让你更加开心呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#6P哼哼……\x01",
            "连那个怪盗的名字都出来了啊。\x02\x03",

            "『噬身之蛇』……\x01",
            "真是一群有趣的家伙啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3302F#11P呵呵，像你这样的人\x01",
            "至今都没有被挖角，\x01",
            "玲还觉得不可思议呢……\x02\x03",

            "#3309F嘻嘻……\x01",
            "难道是有什么特殊原因吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P蠢话……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#6P玲……莫非\x01",
            "『结社』也与此事有所关联吗？\x02\x03",

            "#0013F与这间研究室的主人\x01",
            "企图实行的计划有所关联？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "#3304F#11P呵呵……那倒没有哦。\x02\x03",

            "玲只是出于个人原因\x01",
            "而留在此地的。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x9, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1200)
    OP_64(0xFFFF)
    Sleep(500)

    #C0133
    ChrTalk(
        0x9,
        (
            "#3308F#11P──约亚西姆·琼塔。\x02\x03",

            "圣乌尔斯拉医科大学的副教授，\x01",
            "『Ｄ∴Ｇ教团』的干部祭司……\x02\x03",

            "#3303F收集了所有『仪式』的结果数据，\x01",
            "消失于黑暗中，也是『真知』的开发者。\x02\x03",

            "#3300F……这下，玲想知道的情报\x01",
            "终于全部收集到了。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#0008F#6P……是吗，你是指……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        "#0208F#6P那个白皮文件……吗……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "#3304F#11P呵呵，虽然早有头绪，\x01",
            "但之前一直缺乏决定性的证据……\x02\x03",

            "#3300F──『他』的伤也已经治好了，\x01",
            "又承蒙大哥哥你们相助。\x02\x03",

            "#3309F这样一来……玲留在这里的原因\x01",
            "终于只剩下一个了。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#0005F#6P哎……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_68(112890, 1200, 51950, 800)
    Fade(500)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x10)
    SetChrPos(0x9, 114900, 800, 50000, 270)
    Sound(820, 0, 100, 0)
    OP_0D()
    OP_6F(0x1)
    Sleep(300)

    #C0138
    ChrTalk(
        0x9,
        (
            "#3300F#11P──如果见到了艾丝蒂尔他们，\x01",
            "请转达一声。\x02\x03",

            "就说给他们最后一个\x01",
            "抓住玲的机会。\x02\x03",

            "#3304F呵呵……\x01",
            "虽然我觉得那只是无谓的努力。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0013F#6P你……\x01",
            "到底有什么打算？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        (
            "#3300F#11P在此地，玲只是『小猫』……\x01",
            "随心所欲，只负责在旁观察的存在。\x02\x03",

            "不打算帮助大哥哥你们，\x01",
            "但也不打算妨碍。\x02\x03",

            "#3303F不过呢……\x01",
            "就给你们一个忠告吧。\x02\x03",

            "#3301F那个孩子大概是一切的『钥匙』。\x01",
            "千万要小心，别让她被人抢走哦。\x02\x03",

            "#3302F嘻嘻……\x01",
            "不过这话也许根本就没必要再说。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#0005F#6P……一切的『钥匙』……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#0101F#6P#N莫非\x01",
            "是指小琪雅……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0143
    ChrTalk(
        0x9,
        (
            "#3309F#11P呵呵……\x01",
            "玲差不多也该走了。\x02",
        )
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x4)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    Sound(820, 0, 100, 0)
    OP_A1(0x9, 0x384, 0x4, 0x4, 0x5, 0x6, 0x7)
    Sleep(300)

    #C0144
    ChrTalk(
        0x9,
        "#3304F#11P那么，各位──Guten Abend（晚安）。\x02",
    )

    CloseMessageWindow()
    OP_A1(0x9, 0x384, 0x3, 0x6, 0x5, 0x4)
    Sleep(300)
    StopBGM(0x1770)
    ClearChrFlags(0x9, 0x2)
    ClearChrFlags(0x9, 0x10)
    SetChrChipByIndex(0x9, 0x20)
    SetChrSubChip(0x9, 0x4)
    Sound(854, 0, 100, 0)
    Fade(500)
    OP_68(113940, 1000, 51950, 1000)
    MoveCamera(57, 15, 0, 1000)
    SetCameraDistance(22130, 1000)
    SetChrChip(0x0, 0x9, 0x1E, 0x12C)

    def lambda_4BF6():
        OP_9D(0xFE, 0x1D45C, 0xFFFFD8F0, 0xC350, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_4BF6)
    Sleep(800)
    SetChrChip(0x1, 0x9, 0x0, 0x0)
    EndChrThread(0x9, 0x1)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0145
    ChrTalk(
        0x101,
        "#0007F#6P什么……！？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x104,
        "#0307F#6P#N喂……！？\x02",
    )

    CloseMessageWindow()
    OP_68(114250, 1000, 51350, 1500)

    def lambda_4CF4():
        OP_95(0xFE, 113120, 0, 50450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4CF4)
    Sleep(50)

    def lambda_4D11():
        OP_95(0xFE, 112260, 0, 49260, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4D11)
    Sleep(50)

    def lambda_4D2E():
        OP_95(0xFE, 112030, 0, 51400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4D2E)
    Sleep(50)

    def lambda_4D4B():
        OP_95(0xFE, 110940, 0, 49890, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_4D4B)
    Sleep(50)

    def lambda_4D68():
        OP_95(0xFE, 110470, 0, 51110, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4D68)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x11)
    BeginChrThread(0xD, 1, 0, 18)
    BeginChrThread(0xA, 3, 0, 17)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)
    OP_50(0x4C, (scpexpr(EXPR_PUSH_LONG, 0x200), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMapObjFlags(0x7, 0x1000)
    OP_78(0x7, 0xA)
    OP_49()
    OP_74(0x7, 0xF)
    OP_71(0x7, 0xF1, 0x104, 0x0, 0x20)
    SetChrPos(0xA, 118500, -8150, 47300, 0)
    OP_D3(0xA, 0x0, 0x41EB0, 0x0, 0x0)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrChipByIndex(0x9, 0x1E)
    SetChrSubChip(0x9, 0x0)
    OP_93(0x9, 0x0, 0x0)
    OP_D1(0x9, 0x7, "Null_ren(52)")
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xA5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x8000)
    OP_87(0x1, 0xFF, 0x7, "Null_S_jet_r0(63)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0x7, "Null_S_jet_r2(64)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0x7, "Null_S_jet_l0(66)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x1, 0xFF, 0x7, "Null_S_jet_l2(65)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0x7, "Null_S_jet_r1(61)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0x7, "Null_S_jet_l1(62)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0x7, "Null_kata_jet_r(53)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    OP_87(0x0, 0xFF, 0x7, "Null_kata_jet_l(54)", 0x1C0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x3E8, 0x3E8, 0x3E8, 0x0)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xA, 0x1)
    SetChrFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x8000)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x40), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xEA60), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_5051():
        OP_96(0xFE, 0x1CEE4, 0xFFFFF704, 0xB8C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_5051)
    Sleep(2000)
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
    WaitChrThread(0xA, 1)
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x9, 0x21)
    SetChrSubChip(0x9, 0x4)
    SetChrFlags(0x9, 0x2)
    SetChrFlags(0x9, 0x10)
    OP_0D()
    OP_A1(0x9, 0x384, 0x7, 0x4, 0x5, 0x6, 0x7, 0x6, 0x5, 0x4)
    Sleep(500)
    Sleep(500)

    def lambda_511E():
        OP_96(0xFE, 0x1CEE4, 0x10CC, 0xB8C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_511E)
    WaitChrThread(0xA, 1)
    FadeToDark(1000, 0, -1)
    OP_0D()
    BeginChrThread(0xD, 2, 0, 19)
    EndChrThread(0xD, 0x1)
    WaitChrThread(0xD, 2)
    EndChrThread(0xA, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x3B9)
    SetScenarioFlags(0x5C, 1)
    NewScene("e3300", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_16_2CAF end

    def Function_17_5169(): pass

    label("Function_17_5169")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_518D")
    OP_82(0x46, 0x46, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_17_5169")

    label("loc_518D")

    Return()

    # Function_17_5169 end

    def Function_18_518E(): pass

    label("Function_18_518E")

    Sound(954, 0, 70, 0)
    Sound(953, 2, 0, 0)
    Sleep(80)
    OP_25(0x3B9, 0xA)
    Sleep(80)
    OP_25(0x3B9, 0x14)
    Sleep(80)
    OP_25(0x3B9, 0x1E)
    Sleep(80)
    OP_25(0x3B9, 0x28)
    Sleep(80)
    OP_25(0x3B9, 0x32)
    Sleep(80)
    OP_25(0x3B9, 0x3C)
    Sleep(80)
    OP_25(0x3B9, 0x46)
    Sleep(80)
    OP_25(0x3B9, 0x50)
    Sleep(80)
    OP_25(0x3B9, 0x5A)
    Sleep(80)
    OP_25(0x3B9, 0x64)
    Return()

    # Function_18_518E end

    def Function_19_51E1(): pass

    label("Function_19_51E1")

    OP_25(0x3B9, 0x5A)
    Sleep(150)
    OP_25(0x3B9, 0x50)
    Sleep(150)
    OP_25(0x3B9, 0x46)
    Sleep(150)
    OP_25(0x3B9, 0x3C)
    Sleep(150)
    OP_25(0x3B9, 0x32)
    Sleep(150)
    OP_25(0x3B9, 0x28)
    Sleep(150)
    OP_25(0x3B9, 0x1E)
    Sleep(150)
    OP_25(0x3B9, 0x14)
    Sleep(150)
    OP_25(0x3B9, 0xA)
    Sleep(150)
    OP_24(0x3B9)
    Return()

    # Function_19_51E1 end

    def Function_20_5224(): pass

    label("Function_20_5224")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch50011.itc", 0x1E)
    SoundLoad(806)
    CreatePortrait(0, 180, 0, 436, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x1, "c_vis007.itp")
    OP_68(114540, 900, 50290, 0)
    MoveCamera(50, 18, 0, 0)
    OP_6E(350, 0)
    SetCameraDistance(24200, 0)
    SetChrPos(0x101, 113630, 0, 49990, 90)
    SetChrPos(0x102, 112940, 0, 48520, 90)
    SetChrPos(0x103, 111480, 0, 48550, 90)
    SetChrPos(0x104, 112430, 0, 50730, 90)
    SetChrPos(0x106, 110760, 0, 49390, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetMapFlags(0x2000)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x103, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x104, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    OP_63(0x106, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(1000, 0)
    OP_68(113040, 900, 50290, 3000)
    OP_6F(0x1)
    OP_0D()
    Sleep(500)
    OP_64(0x101)
    OP_64(0x102)
    OP_64(0x103)
    OP_64(0x104)
    OP_64(0x106)
    Sleep(500)

    #C0147
    ChrTalk(
        0x102,
        (
            "#0106F#5P我、我们……\x01",
            "是在做梦吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        (
            "#0201F#6P『噬身之蛇』……\x01",
            "竟然拥有这等技术实力……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P哼……看来有必要\x01",
            "重新认识一下他们了。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0306F#5P真是的，那个混账秘书也是，\x01",
            "也太超乎常识了吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#0006F#5P……嗯……\x02\x03",

            "#0008F不过，看起来，玲和\x01",
            "这次的事件是无关的。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_54AA():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_54AA)
    Sleep(50)

    def lambda_54BA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_54BA)
    Sleep(50)

    def lambda_54CA():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_54CA)
    Sleep(50)

    def lambda_54DA():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_54DA)
    Sleep(50)

    def lambda_54EA():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_54EA)
    Sleep(500)

    #C0152
    ChrTalk(
        0x101,
        (
            "#0003F#11P……幕后黑手的真实身份已经水落石出，\x01",
            "其目的虽然朦胧，但也已开始显现。\x02\x03",

            "#0013F既然如此，那就赶快\x01",
            "返回克洛斯贝尔市──\x02",
        )
    )

    CloseMessageWindow()
    Sound(806, 2, 100, 0)
    Sleep(500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0153
    ChrTalk(
        0x101,
        "#0005F#11P啊……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#0101F#11P还真会挑时候呢……\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    Sound(804, 0, 100, 0)
    Sleep(500)
    SetChrSubChip(0x101, 0x1)
    OP_24(0x326)
    Sound(807, 0, 100, 0)
    Sleep(300)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    FadeToDark(500, 0, 100)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    SetMessageWindowPos(90, 130, -1, -1)

    #A0155
    AnonymousTalk(
        0x101,
        (
            "#0013F您好，我是特别任务支援科的\x01",
            "罗伊德·班宁斯！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("女性的声音")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "你们都平安无事吧，太好了。\x02\x03",

            "──是我，\x01",
            "警备队的索妮亚·贝尔茨。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0157
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F索妮亚副司令……！\x02\x03",

            "#0000F您现在在哪里！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("索妮亚的声音")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "刚刚到达医院。\x02\x03",

            "打算现在就让部队突击进去，\x01",
            "没问题吧？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(90, 130, -1, -1)

    #A0159
    AnonymousTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0004F是、是吗……\x02\x03",

            "#0000F──那些黑手党\x01",
            "都已经被我们制服了。\x02\x03",

            "请召集医院里的人，\x01",
            "将他们保护起来吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("索妮亚的声音")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "明白了，\x01",
            "稍后再会合吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x0, 0x3, 0xFFFFFF, 0x3E8, 0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CA(0x0, 0x0, 0x3)
    OP_49()
    OP_CA(0x1, 0xFF, 0x0)
    OP_24(0x326)
    SetScenarioFlags(0x5C, 2)
    NewScene("t150B", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_20_5224 end

    def Function_21_58B8(): pass

    label("Function_21_58B8")

    EventBegin(0x1)

    #C0161
    ChrTalk(
        0x101,
        (
            "#0008F……不行，现在时间宝贵……\x01",
            "还是快点看看\x01",
            "那封什么邀请函吧。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x4)
    Return()

    # Function_21_58B8 end

    SaveToFile()

Try(main)
