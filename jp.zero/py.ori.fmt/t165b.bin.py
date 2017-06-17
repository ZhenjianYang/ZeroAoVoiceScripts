from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "アーネスト",             # 1
        "殲滅天使レン",           # 2
        "パテルマテル",           # 3
        "アーネストお供",         # 4
        "アーネストお供",         # 5
        "SE制御",                 # 6
        "bt162b",                 # 7
        "bt162b",                 # 8
        "bt163b",                 # 9
    ))

    ATBonus("ATBonus_28C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_2AC", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_5F1E", 13,  13,  24,  10,  0,   0,   0)
    Sepith("Sepith_5F26", 3,   14,  4,   4,   12,  12,  12)

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
        "BattleInfo_38C", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_5F1E", 30, 45, 20, 5,
        (
            ("ms67501.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2EC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2EC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, "MonsterBattlePostion_2CC", "MonsterBattlePostion_34C", "ed7402", "ed7403", "ATBonus_28C"),
        )
    )

    BattleInfo(
        "BattleInfo_454", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_5F26", 30, 45, 20, 5,
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
        "Function_5_9B6",          # 05, 5
        "Function_6_B03",          # 06, 6
        "Function_7_C50",          # 07, 7
        "Function_8_C6C",          # 08, 8
        "Function_9_C8B",          # 09, 9
        "Function_10_1DE9",        # 0A, 10
        "Function_11_1E32",        # 0B, 11
        "Function_12_1E7B",        # 0C, 12
        "Function_13_290C",        # 0D, 13
        "Function_14_294F",        # 0E, 14
        "Function_15_2C5B",        # 0F, 15
        "Function_16_2EE5",        # 10, 16
        "Function_17_56A7",        # 11, 17
        "Function_18_56CC",        # 12, 18
        "Function_19_571F",        # 13, 19
        "Function_20_5762",        # 14, 20
        "Function_21_5E85",        # 15, 21
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_965")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x4A, 1)"), scpexpr(EXPR_END)), "loc_8EE")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_960")

    label("loc_8EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x4A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_960")

    Jump("loc_9AA")

    label("loc_965")

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

    label("loc_9AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_869 end

    def Function_5_9B6(): pass

    label("Function_5_9B6")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AB2")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x87, 1)"), scpexpr(EXPR_END)), "loc_A3B")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_AAD")

    label("loc_A3B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x87),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x87),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_AAD")

    Jump("loc_AF7")

    label("loc_AB2")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0006
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

    label("loc_AF7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_9B6 end

    def Function_6_B03(): pass

    label("Function_6_B03")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BFF")
    Sound(14, 0, 100, 0)
    OP_71(0xA, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_B88")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_BFA")

    label("loc_B88")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F9),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0xA, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BFA")

    Jump("loc_C44")

    label("loc_BFF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_C44")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B03 end

    def Function_7_C50(): pass

    label("Function_7_C50")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C6B")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_7_C50")

    label("loc_C6B")

    Return()

    # Function_7_C50 end

    def Function_8_C6C(): pass

    label("Function_8_C6C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C8A")
    OP_A1(0xFE, 0x5DC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_8_C6C")

    label("loc_C8A")

    Return()

    # Function_8_C6C end

    def Function_9_C8B(): pass

    label("Function_9_C8B")

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

    def lambda_F4D():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F4D)
    Sleep(50)

    def lambda_F65():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F65)
    Sleep(50)

    def lambda_F7D():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_F7D)
    Sleep(50)

    def lambda_F95():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_F95)
    Sleep(50)

    def lambda_FAD():
        OP_9B(0x0, 0xFE, 0x0, 0xDAC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_FAD)
    Sleep(200)

    def lambda_FC5():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_FC5)
    Sleep(50)

    def lambda_FD9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_FD9)
    Sleep(500)

    def lambda_FED():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_FED)
    Sleep(50)

    def lambda_1001():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1001)
    Sleep(500)

    def lambda_1015():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 2, lambda_1015)
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
        "青年の声",
        "#3Pクク、存外早かったものだ。\x02",
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
        "#0007Fあなたは……！\x02",
    )

    CloseMessageWindow()

    #C0012
    ChrTalk(
        0x102,
        "#0101Fア、アーネストさん！？\x02",
    )

    CloseMessageWindow()
    Sound(1899, 255, 100, 0)    #voice#Earnest
    OP_93(0x8, 0x10E, 0x190)
    Sleep(600)
    OP_68(109660, 1100, 50060, 2500)
    MoveCamera(50, 19, 0, 2500)
    SetCameraDistance(20420, 2500)

    def lambda_119F():
        OP_9B(0x0, 0xFE, 0x0, 0x7D0, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_119F)
    Sleep(500)

    def lambda_11B7():
        OP_95(0xFE, 108000, 0, 50650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11B7)
    Sleep(50)

    def lambda_11D4():
        OP_95(0xFE, 108000, 0, 49350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11D4)
    Sleep(50)

    def lambda_11F1():
        OP_95(0xFE, 106750, 0, 49350, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11F1)
    Sleep(50)

    def lambda_120E():
        OP_95(0xFE, 106750, 0, 50650, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_120E)
    Sleep(50)

    def lambda_122B():
        OP_95(0xFE, 105500, 0, 50000, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_122B)
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
            "#30Wやあ、エリィ……\x01",
            "２ヶ月ぶりになるかな？\x02\x03",

            "まだ宵の口だが、\x01",
            "月の綺麗な晩じゃないか。\x02",
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
            "#0101F#6Pアーネストさん……\x01",
            "その瞳の色は……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6Pフン……どうやら\x01",
            "魔性に堕ちたらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6610F#11Pほう、これは……\x01",
            "噂の《銀#2Rイン#》殿もご一緒だったか。\x02\x03",

            "#6613F君が余計な事を吹き込まなければ\x01",
            "私の立場も安泰だったろうに……\x02\x03",

            "#6611Fどうやらお礼をする機会が\x01",
            "巡ってきてくれたようだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#6P我が存在は影……\x01",
            "人の身で騙#2Rかた#るは叶わぬと知れ。\x02\x03",

            "たとえ魔性に堕ちようともな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#6610F#11Pクク……言ってくれる。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#0201F#6P……どうやらあなたが、\x01",
            "魔獣を率いていたようですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#0010F#6Pそれ以前に、どうして\x01",
            "あなたがこんな場所にいる！？\x02\x03",

            "#0007F拘置所にいるはずのあなたが！？\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x8,
        (
            "#6613F#11Pクク、拘置所か……\x02\x03",

            "#6610Fあの建物なら、この病院と同じく\x01",
            "既に“我ら”の手に落ちている。\x02",
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
        "#0005F#6Pなに……！？\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x104,
        (
            "#0310F#6P拘置所の警備は\x01",
            "ベルガード門の警備隊が\x01",
            "担当しているはずだ……\x02\x03",

            "そんな場所を\x01",
            "マフィアが襲ったってのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x8,
        (
            "#6613F#11Pフフ……\x01",
            "そういう訳ではないんだが。\x02\x03",

            "#6610Fちなみにルバーチェごときを\x01",
            "我らと同じに見ないでくれたまえ。\x02\x03",

            "彼らは単なる傀儡#4Rくぐつ#さ。\x01",
            "我らの計画を成就するためのね。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#0006F#6Pやはりそうか……\x02\x03",

            "#0013F《グノーシス》を服用した者を\x01",
            "何らかの方法で操っているんだな？\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x8,
        (
            "#6600F#11Pフフ、その通り……\x02\x03",

            "#6604F……全ては偉大なる\x01",
            "我らが“同志”の計画によるもの。\x02\x03",

            "#6610F大いなる儀式を遂行するための\x01",
            "“駒”に過ぎないというわけさ！\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x102,
        "#0101F#6P偉大なる“同志”……\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x101,
        (
            "#0003F#6P《Ｄ∴Ｇ教団》の残党にして\x01",
            "マフィアの背後に潜んでいた人物……\x02\x03",

            "#0013Fつまり──\x01",
            "この部屋の主というわけか。\x02",
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
        "#4S#11P#20Aハハハハハハハッ……！！\x02",
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

    def lambda_1BAF():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_1BAF)
    Sleep(50)

    def lambda_1BC7():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1BC7)
    Sleep(50)

    def lambda_1BDF():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BDF)
    Sleep(50)

    def lambda_1BF7():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_1BF7)
    Sleep(50)

    def lambda_1C0F():
        OP_9B(0x1, 0xFE, 0xB4, 0x1F4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C0F)
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
        "#0007F#6Pなっ……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0707F#6P#Nこの鬼気は……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0032
    ChrTalk(
        0x103,
        "#0207F#6P#N上位三属性の気配……！？\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0033
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F#11P#30W──それを確かめたければ\x01",
            "私を退けてみるがいい……\x02\x03",

            "#6610F#30W“同志”の導きによって\x01",
            "《真なる叡智#10Rグ ノ ー シ ス#》に至った私をなァ……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x102,
        "#0101F#6P……っ……！！\x02",
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x104,
        "#0307F#6P来るぞ……！\x02",
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

    # Function_9_C8B end

    def Function_10_1DE9(): pass

    label("Function_10_1DE9")

    PlayEffect(0x0, 0x5, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x5, 0x2)
    Return()

    # Function_10_1DE9 end

    def Function_11_1E32(): pass

    label("Function_11_1E32")

    PlayEffect(0x0, 0x6, 0xFE, 0x40, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    StopEffect(0x6, 0x2)
    Return()

    # Function_11_1E32 end

    def Function_12_1E7B(): pass

    label("Function_12_1E7B")

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
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xB), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xC), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0xD), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_214E")

    #C0036
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F#11P#30Wクク……\x01",
            "さすがは《銀#2Rイン#》……\x02\x03",

            "#6610F今の私を退けるとは\x01",
            "噂以上の化物だったようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P……フン…………\x02",
        )
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6600F#11P#30Wそれ以外の者どもも\x01",
            "ここまで食い下がるとは。\x02\x03",

            "#6604F正直、予想外だったぞ。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21A3")

    label("loc_214E")


    #C0039
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F#11P#30Wクク……\x01",
            "ここまで食い下がるとは。\x02\x03",

            "#6600F正直、予想外だったぞ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_21A3")


    #C0040
    ChrTalk(
        0x102,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0108F#6Pアーネストさん……！\x01",
            "……どうしてそんな……！\x02\x03",

            "#0103Fおじいさまを裏切って\x01",
            "邪悪な教団の走狗となって……\x02\x03",

            "#0107Fどうしてそこまで\x01",
            "堕ちてしまったんですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6605F#11P堕ちた……？\x01",
            "いや、真実に目覚めただけさ。\x02\x03",

            "#6613Fそう……今なら判る。\x02\x03",

            "このクロスベルという地が\x01",
            "どんな意味を持っているのか……\x02\x03",

            "#6610F理屈抜きで“判る”んだよ！\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x102,
        "#0101F#6Pな……\x02",
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x103,
        "#0206F#6P#N……意味不明です……\x02",
    )

    CloseMessageWindow()
    OP_5A()

    #C0044
    ChrTalk(
        0x104,
        "#0301F#6P#N完全にイッちまってるな……\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    #C0045
    ChrTalk(
        0x101,
        (
            "#0003F#6P──戯言は\x01",
            "そのくらいにしてもらおう。\x02\x03",

            "#0013F元市長秘書、アーネスト・ライズ。\x02\x03",

            "自治州法に基づき、傷害、騒乱、\x01",
            "不法占拠、薬物使用、拘置所脱走などの\x01",
            "容疑で現行犯逮捕する。\x02\x03",

            "#0007F大人しく捕まってもらうぞ！\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x8,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#6613F#11Pクク……\x01",
            "そう焦ることはない。\x02\x03",

            "まだ夜は始まったばかり……\x01",
            "“同志”の趣向はこれからだ。\x02\x03",

            "#6610Fそちらに招待状があるから\x01",
            "せいぜい目を通しておくといい。\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0011F#6Pなに……\x02",
        )
    )

    CloseMessageWindow()
    OP_68(111440, 400, 58730, 2000)
    MoveCamera(45, 16, 0, 2000)
    SetCameraDistance(17580, 2000)

    def lambda_252E():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_252E)

    def lambda_253B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_253B)
    Sleep(100)

    def lambda_254B():
        OP_93(0xFE, 0x0, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_254B)

    def lambda_2558():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2558)
    Sleep(100)

    def lambda_2568():
        OP_93(0xFE, 0x2D, 0x12C)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2568)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x106, 1)
    OP_6F(0x79)

    #C0048
    ChrTalk(
        0x102,
        "#0105F#1Pあれは……\x02",
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
            "#6610F#11Pはは……\x01",
            "それではまた会おう……！\x02\x03",

            "君たちがこの先の死地を\x01",
            "見事切り抜けられたらな……！\x02",
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

    def lambda_26DC():
        OP_93(0xFE, 0x5A, 0x320)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_26DC)

    def lambda_26E9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26E9)
    Sleep(50)

    def lambda_26F9():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_26F9)
    Sleep(50)

    def lambda_2709():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2709)
    Sleep(50)

    def lambda_2719():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2719)
    Sleep(50)

    def lambda_2729():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2729)
    WaitChrThread(0x8, 1)
    OP_68(115300, 1200, 50000, 1000)
    MoveCamera(65, 13, 0, 1000)
    SetCameraDistance(15500, 1000)
    SetChrChipByIndex(0x8, 0x2A)
    SetChrChip(0x0, 0x8, 0x1E, 0x12C)

    def lambda_276B():
        OP_9B(0x0, 0xFE, 0x0, 0x8FC, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_276B)
    WaitChrThread(0x8, 1)
    SetChrSubChip(0x8, 0x1)
    Sound(814, 0, 100, 0)

    def lambda_278E():
        OP_9D(0xFE, 0x1C138, 0x2EE, 0xC350, 0x3E8, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_278E)
    WaitChrThread(0x8, 1)
    Sound(854, 0, 100, 0)

    def lambda_27B5():
        OP_9D(0xFE, 0x1F338, 0xFFFFD8F0, 0xC350, 0x5DC, 0x1F40)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_27B5)
    WaitChrThread(0x8, 1)
    SetChrChip(0x1, 0x8, 0x0, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)

    #C0050
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010Fくっ……\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0707F逃がすか……！\x02",
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

    def lambda_2867():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2867)

    def lambda_287C():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_287C)

    def lambda_2891():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2891)

    def lambda_28A6():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_28A6)

    def lambda_28BB():
        OP_9B(0x0, 0xFE, 0x0, 0x157C, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_28BB)
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

    # Function_12_1E7B end

    def Function_13_290C(): pass

    label("Function_13_290C")

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

    # Function_13_290C end

    def Function_14_294F(): pass

    label("Function_14_294F")

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
        "#0011F#5P……な………\x02",
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#0101F#5Pい、今のは……\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x79, 3)), scpexpr(EXPR_END)), "loc_2A85")

    #C0054
    ChrTalk(
        0x103,
        (
            "#0206F#6P《星見の塔》にもいた\x01",
            "太古の翼竜……\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2AB7")

    label("loc_2A85")


    #C0055
    ChrTalk(
        0x103,
        (
            "#0206F#6P太古の翼竜……\x01",
            "みたいでしたけど……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2AB7")


    #C0056
    ChrTalk(
        0x104,
        (
            "#0307Fおいおい……\x01",
            "メチャクチャすぎんだろ。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6Pフン……\x01",
            "さすがに追うのは無理か。\x02",
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
            "#0700F#11P──時が惜しい。\x01",
            "とっとと目を通すとしよう。\x02\x03",

            "その“同志”とやらが\x01",
            "用意した招待状とやらをな。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B97():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2B97)

    def lambda_2BA4():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2BA4)
    Sleep(100)

    def lambda_2BB4():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_2BB4)

    def lambda_2BC1():
        TurnDirection(0xFE, 0x106, 300)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_2BC1)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)

    #C0059
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#11Pあ……\x02\x03",

            "#0013F──ああ、そうだな。\x02",
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

    # Function_14_294F end

    def Function_15_2C5B(): pass

    label("Function_15_2C5B")

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
            "黒と白のファイルが\x01",
            "デスクの上に置かれている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E5A")

    #A0061
    AnonymousTalk(
        0x101,
        "#0005F……この紋章は……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0062
    AnonymousTalk(
        0x103,
        (
            "#0201F……もしかして\x01",
            "これが《Ｄ∴Ｇ教団》の……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0063
    AnonymousTalk(
        0x102,
        (
            "#0101Fそ、それにあの《僧院》に\x01",
            "あったのと似ているような……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0064
    AnonymousTalk(
        0x104,
        (
            "#0301Fあの薄気味悪い\x01",
            "悪魔が現れやがった場所か……\x02",
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
            "#0700Fほう……\x01",
            "そんな場所があるのか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0066
    AnonymousTalk(
        0x101,
        (
            "#0006F……あんたが待ち受けていた\x01",
            "《塔》と似たような場所でね。\x02\x03",

            "#0013Fそれはともかく──\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetScenarioFlags(0xE3, 6)

    label("loc_2E5A")


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【ファイルに目を通す】\x01",      # 0
            "【やめておく】\x01",              # 1
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
        (0, "loc_2EC6"),
        (1, "loc_2EDD"),
        (SWITCH_DEFAULT, "loc_2EE2"),
    )


    label("loc_2EC6")

    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_65(0x0, 0x1)
    Call(0, 16)
    Jump("loc_2EE2")

    label("loc_2EDD")

    Jump("loc_2EE2")

    label("loc_2EE2")

    EventEnd(0x3)
    Return()

    # Function_15_2C5B end

    def Function_16_2EE5(): pass

    label("Function_16_2EE5")

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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4294")
    Sound(18, 0, 100, 0)
    OP_C9(0x0, 0x3, 0xFFFFFFFF, 0x3E8, 0x0)
    OP_CA(0x0, 0x0, 0x3)
    Sleep(500)

    #A0067
    AnonymousTalk(
        0x102,
        "#0108Fまさか……こんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0068
    AnonymousTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F……クク、世も末だな。\x02\x03",

            "まさかハルトマン議長さえも\x01",
            "取り込まれていたとは……\x02",
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
            "#0303Fどうやら何かの弱味を握られて\x01",
            "協力させられてたみてぇだが……\x02\x03",

            "#0301Fこの《楽園》ってのは何なんだ？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0070
    AnonymousTalk(
        0x103,
        (
            "#0208F……分かりません。\x02\x03",

            "ひょっとしたら教団の拠点#4Rロッジ#の\x01",
            "一つかもしれませんが……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0071
    AnonymousTalk(
        0x101,
        (
            "#0003Fいずれにせよ、ハルトマン議長は\x01",
            "《彼》に弱味を握られていた。\x02\x03",

            "#0013Fそして《彼》がクロスベルに潜伏するのを\x01",
            "ルバーチェに手伝わせたのか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0072
    AnonymousTalk(
        0x102,
        (
            "#0110F……許せない……\x01",
            "自治州代表の一人でありながら\x01",
            "何という愚劣なことを……\x02\x03",

            "#0108Fこんな人のために\x01",
            "おじいさまは長年苦労をして、\x01",
            "お父さまはクロスベルを捨てて……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0073
    AnonymousTalk(
        0x101,
        "#0008Fエリィ……\x02",
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
            "#0700F#11P……感慨に浸るのは早い。\x02\x03",

            "この黒いファイルによれば\x01",
            "グノーシスを製造している場所は\x01",
            "病院ではなく別の場所のようだ。\x02\x03",

            "そして出荷リストによれば……\x01",
            "マフィア以外にもかなりの量が\x01",
            "どこかに流れているらしい。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#5P……ああ。\x01",
            "どうやら“彼”はここ以外にも\x01",
            "拠点を持っていることになる……\x02\x03",

            "#0013Fひょっとして\x01",
            "行方不明の人たちはそこに……？\x02",
        )
    )

    CloseMessageWindow()

    #C0077
    ChrTalk(
        0x103,
        (
            "#0203F#12P……あり得そうですね。\x02\x03",

            "#0201F一体どこにあるんでしょう……？\x02",
        )
    )

    CloseMessageWindow()

    #C0078
    ChrTalk(
        0x104,
        (
            "#0306F#1Pその、マフィア以外の\x01",
            "卸し先ってのも気になるな。\x02\x03",

            "#0301Fおい、まさか《黒月》とかいう\x01",
            "オチじゃねえだろうな……？\x02",
        )
    )

    CloseMessageWindow()

    #C0079
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#11Pフッ、あのツァオがそんな物に\x01",
            "手を出すほど可愛気があるものか。\x02\x03",

            "#0700F可能性があるとすれば、\x01",
            "どこぞの野心的な製薬会社……\x02\x03",

            "もしくはテロリストや猟兵団、\x01",
            "各国の諜報機関もあり得るだろう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        "#0303F#1Pフン、確かにな……\x02",
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        (
            "#0106F#6Pつくづくクロスベルという地の\x01",
            "特異性が恨めしくなるわね……\x02",
        )
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x101,
        (
            "#0006F#6P……ああ……\x02\x03",

            "#0001F──こちらの白いファイルも\x01",
            "確かめてみよう。\x02",
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
        "#0208F……っ……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0084
    AnonymousTalk(
        0x102,
        "#0110Fこ、これは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0085
    AnonymousTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700Fふむ……\x01",
            "６年前の“儀式”の被害者たちか。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0086
    AnonymousTalk(
        0x104,
        (
            "#0311F……外道が……\x01",
            "こんなものを……\x02",
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

            "#0008F……ごめん、ティオ。\x01",
            "中を確認していくぞ……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0088
    AnonymousTalk(
        0x103,
        (
            "#0204F#30W……謝らないでください。\x02\x03",

            "#0202Fどうか……\x01",
            "そのまま確認して下さい。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0089
    AnonymousTalk(
        0x101,
        "#0003Fああ……\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_39A9")
    OP_C9(0x2, 0x0, 0xFA00, 0x7D00, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)

    label("loc_39A9")

    OP_C9(0x2, 0x1, 0x2EE, 0x2EE, 0x0)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x1F4)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)

    #A0090
    AnonymousTalk(
        0x101,
        "#0013F……っ………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0091
    AnonymousTalk(
        0x103,
        (
            "#0213F#30W……あはは…………\x02\x03",

            "#0212Fこの頃の表情に比べたら……\x01",
            "少しはマシになりましたよね？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0092
    AnonymousTalk(
        0x101,
        "#0008Fティオ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0093
    AnonymousTalk(
        0x102,
        "#0102F……言うまでもないわ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0094
    AnonymousTalk(
        0x104,
        (
            "#0304Fはは……見違えるほど\x01",
            "可愛くなったと思うぜ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0095
    AnonymousTalk(
        0x103,
        (
            "#0212F……お世辞でも嬉しいです。\x02\x03",

            "#0213Fロイドさん──どうか確認を。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0096
    AnonymousTalk(
        0x101,
        "#0003F……わかった。\x02",
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
    Jc((scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_END)), "loc_3C12")
    OP_C9(0x2, 0x0, 0xFA00, 0x7D00, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)
    Jump("loc_3C30")

    label("loc_3C12")

    OP_C9(0x2, 0x0, 0x1F400, 0x0, 0x0)
    OP_C9(0x2, 0x0, 0x0, 0x0, 0x1F4)

    label("loc_3C30")

    OP_C9(0x2, 0x1, 0x2EE, 0x2EE, 0x0)
    OP_C9(0x2, 0x1, 0x3E8, 0x3E8, 0x1F4)
    OP_C9(0x2, 0x3, 0xFFFFFFFF, 0x1F4, 0x0)
    OP_CA(0x0, 0x2, 0x3)
    Sleep(500)

    #A0097
    AnonymousTalk(
        0x101,
        "#0005Fあ……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0098
    AnonymousTalk(
        0x104,
        "#0301Fこいつは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0099
    AnonymousTalk(
        0x103,
        "#0208F……レンさん……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0100
    AnonymousTalk(
        0x102,
        (
            "#0103Fそう……\x01",
            "やはりそう繋がるのね……\x02",
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
            "#0700Fふむ……\x01",
            "その娘もお前たちの知り合いか。\x02\x03",

            "──当時、共和国の東方人街でも\x01",
            "拉致事件の噂は耳にしたが……\x02\x03",

            "しかし、よくもまあ、\x01",
            "これだけの事をしでかしたものだ。\x07\x00\x02",
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
            "ファイルの間に写真が挟まっている。\x07\x00\x02",
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
        "#0013F……ッ……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0105
    AnonymousTalk(
        0x102,
        "#0107Fキーアちゃん……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0106
    AnonymousTalk(
        0x103,
        "#0201F……そんな……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #A0107
    AnonymousTalk(
        0x104,
        (
            "#0310F野郎……\x01",
            "まさかとは思ったが……！\x02",
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
            "#0700F例の競売会で\x01",
            "お前たちが保護した少女か。\x02\x03",

            "この写真だけ新しいようだが、\x01",
            "最近撮ったものということか……？\x02",
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
            "#0006Fああ、多分そうだろう……\x02\x03",

            "#0010F……クソッ……！\x01",
            "最初から知っていたのか……！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 4)), scpexpr(EXPR_END)), "loc_40F3")

    #A0110
    AnonymousTalk(
        0x102,
        (
            "#0108F私たちがキーアちゃんを\x01",
            "ここに連れて来た時……\x02\x03",

            "#0101F“彼”は何喰わぬ顔で\x01",
            "検査入院を勧めてきたのね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_41F4")

    label("loc_40F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 5)), scpexpr(EXPR_END)), "loc_4178")

    #A0111
    AnonymousTalk(
        0x103,
        (
            "#0203Fわたしたちがキーアを\x01",
            "ここに連れて来た時……\x02\x03",

            "#0201F“彼”は何喰わぬ顔で\x01",
            "検査入院を勧めてきたんですね……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Jump("loc_41F4")

    label("loc_4178")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA9, 6)), scpexpr(EXPR_END)), "loc_41F4")

    #A0112
    AnonymousTalk(
        0x104,
        (
            "#0303F俺たちがキー坊を\x01",
            "ここに連れて来た時……\x02\x03",

            "#0310F“ヤツ”は何喰わぬ顔で\x01",
            "検査入院を勧めてきたわけか……\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_41F4")

    StopBGM(0xFA0)
    Sleep(300)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    SetChrName("少女の声")

    #A0113
    AnonymousTalk(
        0xFF,
        (
            "#3Pふふっ……\x01",
            "おそらくそうでしょうね。\x02",
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

    label("loc_4294")

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
            "#0707F#11Pなに……！？\x02",
        )
    )

    CloseMessageWindow()

    #C0115
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0005F#5Pこの声は……\x02",
        )
    )

    CloseMessageWindow()
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7304", 0)
    OP_68(115330, 1000, 50270, 2500)
    MoveCamera(67, 17, 0, 2500)

    def lambda_4383():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4383)
    Sleep(50)

    def lambda_4393():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4393)
    Sleep(50)

    def lambda_43A3():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_43A3)
    Sleep(50)

    def lambda_43B3():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_43B3)
    Sleep(50)

    def lambda_43C3():
        TurnDirection(0xFE, 0x9, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_43C3)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    OP_6F(0x79)

    #C0116
    ChrTalk(
        0x103,
        "#0205Fあ……\x02",
    )

    CloseMessageWindow()

    #C0117
    ChrTalk(
        0x102,
        "#0105Fレンちゃん……！？\x02",
    )

    CloseMessageWindow()

    #C0118
    ChrTalk(
        0x104,
        "#0301Fおいおい……マジかよ！？\x02",
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

    def lambda_44ED():
        OP_95(0xFE, 109970, 0, 51460, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_44ED)

    def lambda_4507():
        OP_95(0xFE, 109180, 0, 50270, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4507)

    def lambda_4521():
        OP_95(0xFE, 108860, 0, 52330, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4521)

    def lambda_453B():
        OP_95(0xFE, 107860, 0, 51050, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_453B)

    def lambda_4555():
        OP_95(0xFE, 107760, 0, 52680, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_4555)
    WaitChrThread(0x102, 1)

    def lambda_4573():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4573)
    WaitChrThread(0x101, 1)

    def lambda_4584():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_4584)
    WaitChrThread(0x103, 1)

    def lambda_4595():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_4595)
    WaitChrThread(0x104, 1)

    def lambda_45A6():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_45A6)
    WaitChrThread(0x106, 1)

    def lambda_45B7():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_45B7)
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
            "#0001F#6P君は……\x01",
            "いつからそこに……？\x02",
        )
    )

    CloseMessageWindow()

    #C0120
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P……気配を感じなかった……\x02\x03",

            "どうやら只者ではなさそうだな？\x02",
        )
    )

    CloseMessageWindow()

    #N0121
    NpcTalk(
        0x9,
        "レン",
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304F#11Pうふふ……\x01",
            "あなたと同じくらいにはね。\x02",
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
            "──改めて自己紹介を。\x02\x03",

            "《身喰らう蛇#10Rウ ロ ボ ロ ス#》の執行者、\x01",
            "Ｎｏ．ⅩⅤ──《殲滅天使》レンよ。\x02\x03",

            "うふふ、お見知りおきを。\x02",
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
        "#0006F#6Pエステルたちから聞いた通りか……\x02",
    )

    CloseMessageWindow()

    #C0124
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P《身喰らう蛇》……\x01",
            "なるほど《痩せ狼》の同類か。\x02",
        )
    )

    CloseMessageWindow()

    #C0125
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3305F#11Pあら……\x01",
            "ヴァルターの事を知っているの？\x02",
        )
    )

    CloseMessageWindow()

    #C0126
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#6P前に一度、やり合った事がある。\x02\x03",

            "結局、決着が付かずに\x01",
            "取り逃がしてしまったがな。\x02",
        )
    )

    CloseMessageWindow()

    #C0127
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3304F#11Pうふふ、彼も同じように\x01",
            "思っているでしょうね。\x02\x03",

            "#3302Fレンが《結社》に戻っていれば\x01",
            "一緒に誘っても良かったけど……\x02\x03",

            "#3309Fそれともブルブランあたりを\x01",
            "誘った方が喜んでくれたかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0128
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0702F#6Pクク……\x01",
            "かの怪盗の名まで出てくるか。\x02\x03",

            "《身喰らう蛇》……\x01",
            "なかなか興味深い連中だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0129
    ChrTalk(
        0x9,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#3302F#11Pうふふ、あなたみたいな人が\x01",
            "今までスカウトされていないのは\x01",
            "むしろ不思議な気もするけど……\x02\x03",

            "#3309Fクスクス……\x01",
            "何か理由でもあるのかしら？\x02",
        )
    )

    CloseMessageWindow()

    #C0130
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P戯言を……\x02",
        )
    )

    CloseMessageWindow()

    #C0131
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0003F#6Pレン……ひょっとして\x01",
            "《結社》も関与しているのか？\x02\x03",

            "#0013Fこの研究室の主が\x01",
            "起こそうとしている企みに？\x02",
        )
    )

    CloseMessageWindow()

    #C0132
    ChrTalk(
        0x9,
        (
            "#3304F#11Pうふふ……それは無いわ。\x02\x03",

            "レンはあくまで個人的な理由で\x01",
            "この地に留まっているというだけ。\x02",
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
            "#3308F#11P──ヨアヒム・ギュンター。\x02\x03",

            "聖ウルスラ医科大学准教授にして\x01",
            "《Ｄ∴Ｇ教団》幹部司祭……\x02\x03",

            "#3303F全ての《儀式》の成果を集めて\x01",
            "闇に消えた《グノーシス》の開発者。\x02\x03",

            "#3300F……これでやっと\x01",
            "レンの知りたい全てが揃ったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0134
    ChrTalk(
        0x101,
        "#0008F#6P……そうか、君は……\x02",
    )

    CloseMessageWindow()

    #C0135
    ChrTalk(
        0x103,
        "#0208F#6Pあの白いファイル、ですか……\x02",
    )

    CloseMessageWindow()

    #C0136
    ChrTalk(
        0x9,
        (
            "#3304F#11Pふふっ、アタリは付いていたけど\x01",
            "決定的な証拠は無かったから……\x02\x03",

            "#3300F──“彼”のケガも治ったし、\x01",
            "お兄さんたちにも助けてもらった。\x02\x03",

            "#3309Fこれでやっと……この地に\x01",
            "留まる理由は一つだけになったわ。\x02",
        )
    )

    CloseMessageWindow()

    #C0137
    ChrTalk(
        0x101,
        "#0005F#6Pえ……\x02",
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
            "#3300F#11P──エステルたちに会ったら\x01",
            "伝えておいてちょうだい。\x02\x03",

            "レンを捕まえられる\x01",
            "最後のチャンスをあげるって。\x02\x03",

            "#3304Fうふふ……\x01",
            "無駄な努力だとは思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0139
    ChrTalk(
        0x101,
        (
            "#0013F#6P君は……\x01",
            "一体何をするつもりなんだ？\x02",
        )
    )

    CloseMessageWindow()

    #C0140
    ChrTalk(
        0x9,
        (
            "#3300F#11Pこの地のレンは《仔猫》……\x01",
            "気まぐれに観察するだけの存在。\x02\x03",

            "お兄さんたちを助けるつもりも\x01",
            "あえて邪魔するつもりもないわ。\x02\x03",

            "#3303Fでもまあ……\x01",
            "一つだけ忠告してあげる。\x02\x03",

            "#3301Fあの子は多分、全ての《鍵》。\x01",
            "くれぐれも奪われないことね。\x02\x03",

            "#3302Fクスクス……\x01",
            "言われるまでもないと思うけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0141
    ChrTalk(
        0x101,
        "#0005F#6P……全ての《鍵》……\x02",
    )

    CloseMessageWindow()

    #C0142
    ChrTalk(
        0x102,
        (
            "#0101F#6P#Nひょっとして\x01",
            "キーアちゃんの事……！？\x02",
        )
    )

    CloseMessageWindow()
    OP_5A()

    #C0143
    ChrTalk(
        0x9,
        (
            "#3309F#11Pうふふ……\x01",
            "そろそろレンは行くわね。\x02",
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
        "#3304F#11Pそれでは皆様──良き夜を#8Rグーテン・アーベント#。\x02",
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

    def lambda_5132():
        OP_9D(0xFE, 0x1D45C, 0xFFFFD8F0, 0xC350, 0x3E8, 0x9C4)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5132)
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
        "#0007F#6Pな……！？\x02",
    )

    CloseMessageWindow()

    #C0146
    ChrTalk(
        0x104,
        "#0307F#6P#Nおいっ……！？\x02",
    )

    CloseMessageWindow()
    OP_68(114250, 1000, 51350, 1500)

    def lambda_5232():
        OP_95(0xFE, 113120, 0, 50450, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5232)
    Sleep(50)

    def lambda_524F():
        OP_95(0xFE, 112260, 0, 49260, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_524F)
    Sleep(50)

    def lambda_526C():
        OP_95(0xFE, 112030, 0, 51400, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_526C)
    Sleep(50)

    def lambda_5289():
        OP_95(0xFE, 110940, 0, 49890, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5289)
    Sleep(50)

    def lambda_52A6():
        OP_95(0xFE, 110470, 0, 51110, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_52A6)
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

    def lambda_558F():
        OP_96(0xFE, 0x1CEE4, 0xFFFFF704, 0xB8C4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_558F)
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

    def lambda_565C():
        OP_96(0xFE, 0x1CEE4, 0x10CC, 0xB8C4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_565C)
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

    # Function_16_2EE5 end

    def Function_17_56A7(): pass

    label("Function_17_56A7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_56CB")
    OP_82(0x46, 0x46, 0x3E8, 0x3E8)
    Sleep(1000)
    Jump("Function_17_56A7")

    label("loc_56CB")

    Return()

    # Function_17_56A7 end

    def Function_18_56CC(): pass

    label("Function_18_56CC")

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

    # Function_18_56CC end

    def Function_19_571F(): pass

    label("Function_19_571F")

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

    # Function_19_571F end

    def Function_20_5762(): pass

    label("Function_20_5762")

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
            "#0106F#5Pわ、わたしたち……\x01",
            "夢でも見ているの……？\x02",
        )
    )

    CloseMessageWindow()

    #C0148
    ChrTalk(
        0x103,
        (
            "#0201F#6P《身喰らう蛇》……\x01",
            "あそこまでの技術力だなんて……\x02",
        )
    )

    CloseMessageWindow()

    #C0149
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6Pフン……どうやら認識を\x01",
            "改める必要があるようだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0150
    ChrTalk(
        0x104,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0306F#5Pったく、あの秘書野郎といい、\x01",
            "常識外れすぎんだろ……\x02",
        )
    )

    CloseMessageWindow()

    #C0151
    ChrTalk(
        0x101,
        (
            "#0006F#5P……ああ……\x02\x03",

            "#0008Fだが、どうやら彼女#4Rレ ン#は\x01",
            "事件には関わってないようだ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5A21():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_5A21)
    Sleep(50)

    def lambda_5A31():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_5A31)
    Sleep(50)

    def lambda_5A41():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_5A41)
    Sleep(50)

    def lambda_5A51():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_5A51)
    Sleep(50)

    def lambda_5A61():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_5A61)
    Sleep(500)

    #C0152
    ChrTalk(
        0x101,
        (
            "#0003F#11P……黒幕の正体も判明して\x01",
            "その狙いも朧#2Rおぼろ#げだが見えてきた。\x02\x03",

            "#0013Fこうなったら急いで\x01",
            "クロスベル市に戻って──\x02",
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
        "#0005F#11Pあ……\x02",
    )

    CloseMessageWindow()

    #C0154
    ChrTalk(
        0x102,
        "#0101F#11Pすごいタイミングね……\x02",
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
            "#0013Fはい、特務支援課、\x01",
            "ロイド・バニングスです！\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("女性の声")

    #A0156
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "良かった、無事だったのね。\x02\x03",

            "──私よ。\x01",
            "警備隊のソーニャ・ベルツ。\x02",
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
            "#0005Fソーニャ副司令……！\x02\x03",

            "#0000F今、どちらにいるんですか！？\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ソーニャの声")

    #A0158
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ちょうど病院に到着した所よ。\x02\x03",

            "これから部隊を突入させるけど\x01",
            "問題ないかしら？\x02",
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
            "#0004Fそ、そうですか……\x02\x03",

            "#0000F──マフィアたちは\x01",
            "一通り制圧している状態です。\x02\x03",

            "病院内の人たちに声をかけて\x01",
            "保護してあげてください。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(170, 50, -1, -1)
    SetChrName("ソーニャの声")

    #A0160
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "分かったわ。\x01",
            "また後で合流しましょう。\x07\x00\x02",
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

    # Function_20_5762 end

    def Function_21_5E85(): pass

    label("Function_21_5E85")

    EventBegin(0x1)

    #C0161
    ChrTalk(
        0x101,
        (
            "#0008F……いや、今は時間が惜しい……\x01",
            "先に招待状とやらに\x01",
            "目を通してみよう。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(50)
    SetChrPos(0x0, 100500, 0, 50000, 90)
    EventEnd(0x4)
    Return()

    # Function_21_5E85 end

    SaveToFile()

Try(main)
