from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "t162b.bin",                # FileName
        "t162b",                    # MapName
        "t162b",                    # Location
        0x0055,                     # MapIndex
        "ed7123",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 85, 0, 0, 0, 2],
    )

    BuildStringList((
        "t162b",                  # 0
        "イベント用モンスター",   # 1
        "イベント用モンスター",   # 2
        "bt162b",                 # 3
        "bt162b",                 # 4
        "bt162b",                 # 5
    ))

    ATBonus("ATBonus_1D4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_15BD", 13,  13,  24,  10,  0,   0,   0)
    Sepith("Sepith_15C5", 3,   14,  4,   4,   12,  12,  12)

    MonsterBattlePostion("MonsterBattlePostion_234", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_238", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_23C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_240", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_244", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_248", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_24C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_298", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_29C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_214", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_224", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_228", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_22C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_230", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 4, 12, 45)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 12, 12, 315)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 0, 0, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_2D4", 0x0000, 34, 6, 60, 4, 1, 30, 0, "bt162b", "Sepith_15BD", 30, 45, 20, 5,
        (
            ("ms67501.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
            ("ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_214", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
            ("ms67501.dat", "ms67501.dat", "ms67501.dat", "ms67501.dat", 0, 0, 0, 0, "MonsterBattlePostion_214", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
        )
    )

    BattleInfo(
        "BattleInfo_39C", 0x0000, 34, 6, 60, 4, 1, 40, 0, "bt162b", "Sepith_15C5", 30, 45, 20, 5,
        (
            ("ms75701.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_214", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_234", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
            ("ms75701.dat", "ms75701.dat", "ms75701.dat", "ms75701.dat", 0, 0, 0, 0, "MonsterBattlePostion_214", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_464", 0x0002, 34, 6, 0, 0, 0, 0, 0, "bt162b", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75701.dat", "ms75701.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2B4", "MonsterBattlePostion_294", "ed7402", "ed7403", "ATBonus_1D4"),
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

    DeclMonster(-3610,   62420,   0,       0x1010000,    "BattleInfo_2D4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(9070,    61620,   0,       0x1010000,    "BattleInfo_39C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(6590,    -63750,  0,       0x1010000,    "BattleInfo_39C", 0,   18,  0xFFFF, 2,  3)

    DeclActor(9500,    0,       -63750,  1200,    9500,    1000,    -63750,  0x007C, 0,  4,  0x0000)
    DeclActor(7600,    0,       3000,    1200,    7600,    1500,    3000,    0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_510",          # 00, 0
        "Function_1_58F",          # 01, 1
        "Function_2_596",          # 02, 2
        "Function_3_766",          # 03, 3
        "Function_4_7B7",          # 04, 4
        "Function_5_904",          # 05, 5
        "Function_6_A0F",          # 06, 6
        "Function_7_F29",          # 07, 7
        "Function_8_F41",          # 08, 8
        "Function_9_13B7",         # 09, 9
        "Function_10_1415",        # 0A, 10
        "Function_11_1473",        # 0B, 11
        "Function_12_14D1",        # 0C, 12
        "Function_13_152F",        # 0D, 13
    ))


    def Function_0_510(): pass

    label("Function_0_510")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x75), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_528")
    ClearScenarioFlags(0x5F, 1)
    Call(0, 1)

    label("loc_528")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE3, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_53E")
    SetMapFlags(0x10000000)
    Event(0, 6)

    label("loc_53E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5C, 0)), scpexpr(EXPR_END)), "loc_58E")
    ClearScenarioFlags(0x5C, 0)
    SetChrPos(0x0, 7190, 0, -90, 270)
    SetChrPos(0x1, 7190, 0, -90, 270)
    SetChrPos(0x2, 7190, 0, -90, 270)
    SetChrPos(0x3, 7190, 0, -90, 270)

    label("loc_58E")

    Return()

    # Function_0_510 end

    def Function_1_58F(): pass

    label("Function_1_58F")

    Sound(160, 0, 100, 0)
    Return()

    # Function_1_58F end

    def Function_2_596(): pass

    label("Function_2_596")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE2, 7)), scpexpr(EXPR_END)), "loc_5EB")
    LoadEffect(0x7, "event\\ev617_00.eff")
    PlayEffect(0x7, 0x7, 0xFF, 0x0, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)

    label("loc_5EB")

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
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xBF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75E")
    OP_70(0x3, 0x0)
    Jump("loc_762")

    label("loc_75E")

    OP_70(0x3, 0x1E)

    label("loc_762")

    Call(0, 3)
    Return()

    # Function_2_596 end

    def Function_3_766(): pass

    label("Function_3_766")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x72), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_783")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    Jump("loc_78D")

    label("loc_783")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)

    label("loc_78D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x70), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7AB")
    SetChrFlags(0xC, 0x8)
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_7B6")

    label("loc_7AB")

    ClearChrFlags(0xC, 0x8)
    ClearMapObjFlags(0x3, 0x4)

    label("loc_7B6")

    Return()

    # Function_3_766 end

    def Function_4_7B7(): pass

    label("Function_4_7B7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x10B, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8B3")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_83C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
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
    SetScenarioFlags(0x10B, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_8AE")

    label("loc_83C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
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
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8AE")

    Jump("loc_8F8")

    label("loc_8B3")

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

    label("loc_8F8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_7B7 end

    def Function_5_904(): pass

    label("Function_5_904")

    OP_F2(0x2)
    FadeToDark(300, 0, 100)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F1")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x4, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x4, 0x0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0x4, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_9F1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A0D")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_A0D")

    Return()

    # Function_5_904 end

    def Function_6_A0F(): pass

    label("Function_6_A0F")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    LoadChrToIndex("monster/ch75750.itc", 0x23)
    LoadChrToIndex("monster/ch75750.itc", 0x24)
    OP_68(12250, 500, -7480, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(24500, 0)
    SetChrPos(0x101, -1000, 0, 0, 90)
    SetChrPos(0x102, -1000, 0, 0, 90)
    SetChrPos(0x103, -1000, 0, 0, 90)
    SetChrPos(0x104, -1000, 0, 0, 90)
    SetChrPos(0x106, -1000, 0, 0, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x106, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrChipByIndex(0x9, 0x23)
    SetChrSubChip(0x9, 0x0)
    SetChrPos(0x8, 7880, 0, 8370, 0)
    SetChrPos(0x9, 9020, 0, -7350, 0)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x9, 0x20)
    BeginChrThread(0x8, 0, 0, 7)
    BeginChrThread(0x9, 0, 0, 7)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_68(4190, 500, 580, 7000)
    SetCameraDistance(23500, 7000)
    Sleep(2000)
    BeginChrThread(0x101, 3, 0, 9)
    Sleep(750)
    BeginChrThread(0x102, 3, 0, 10)
    Sleep(750)
    BeginChrThread(0x103, 3, 0, 11)
    Sleep(750)
    BeginChrThread(0x104, 3, 0, 12)
    Sleep(750)
    BeginChrThread(0x106, 3, 0, 13)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0x106, 3)
    OP_6F(0x1)
    OP_0D()

    #C0005
    ChrTalk(
        0x101,
        "#0011F#6Pなんだ、このモヤは……\x02",
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#0108F#6Pな、なんだか\x01",
            "空気が淀んでるような……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x104,
        (
            "#0301F#6Pおいおい、まさか危険な\x01",
            "ガスとかじゃねえだろうな？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        (
            "#0203F#6Pいえ……人体に影響する\x01",
            "ものではなさそうですが……\x02\x03",

            "#0208F精神には影響がありそうですね……\x02",
        )
    )

    CloseMessageWindow()

    #C0009
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P恐らく邪気や瘴気の類だろう。\x02\x03",

            "#0702Fクク、どうやら思っていた以上に\x01",
            "厄介な相手がいるらしいな。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0010F#6Pくっ、いったい誰が……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Sound(835, 0, 100, 0)
    Fade(1000)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)

    def lambda_DA5():
        OP_95(0xFE, 3970, 0, 4370, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DA5)

    def lambda_DBF():
        OP_95(0xFE, 4000, 0, -4140, 4500, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_DBF)
    OP_93(0x101, 0x2D, 0x0)
    SetChrPos(0x102, 2230, 0, -960, 90)
    SetChrPos(0x106, 1010, 0, 260, 45)
    OP_68(3930, 800, 30, 0)
    MoveCamera(65, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(27000, 0)
    SetCameraDistance(25000, 1500)
    OP_6F(0x10)
    OP_0D()
    WaitChrThread(0x8, 1)
    WaitChrThread(0x9, 1)

    #C0011
    ChrTalk(
        0x102,
        "#0101F#6Pま、また……！\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
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
    OP_0D()
    Sleep(300)

    #C0012
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#6P片付けるぞ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_EC0():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_EC0)

    def lambda_ED5():
        OP_9B(0x0, 0xFE, 0x0, 0xBB8, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_ED5)
    SetCameraDistance(20000, 500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    Sleep(400)
    Battle("BattleInfo_464", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    Call(0, 8)
    Return()

    # Function_6_A0F end

    def Function_7_F29(): pass

    label("Function_7_F29")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_F40")
    OP_A0(0xFE, 1250, 0x0, 0xFB)
    Jump("Function_7_F29")

    label("loc_F40")

    Return()

    # Function_7_F29 end

    def Function_8_F41(): pass

    label("Function_8_F41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00550.itc", 0x22)
    OP_68(4000, 1800, 120, 0)
    MoveCamera(65, 22, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22060, 0)
    SetChrPos(0x101, 4790, 0, 1050, 45)
    SetChrPos(0x102, 4090, 0, -350, 135)
    SetChrPos(0x103, 3780, 0, 1890, 0)
    SetChrPos(0x104, 2880, 0, -1690, 180)
    SetChrPos(0x106, 2020, 0, 280, 315)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
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
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    FadeToBright(1000, 0)
    OP_68(4000, 1000, 120, 2000)
    OP_6F(0x1)
    OP_0D()

    #C0013
    ChrTalk(
        0x101,
        (
            "#0003F#5Pやはり普通の魔獣とは違う……\x02\x03",

            "#0008F《塔》や《僧院》で戦ったのと\x01",
            "似ているような……\x02",
        )
    )

    CloseMessageWindow()

    #C0014
    ChrTalk(
        0x103,
        (
            "#0208F#5P上位三属性は働いていませんが\x01",
            "わたしも同感です……\x02\x03",

            "#0201F……ひょっとしたら……\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#0700F#12Pマフィアたちと同じく\x01",
            "例の《グノーシス》なる魔薬が\x01",
            "投与された可能性がある……\x02\x03",

            "#0702Fつまり、そういう事だな？\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x103,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "#0206F#5P……はい。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x104,
        "#0303F#5Pチッ、そういう事かよ。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        "#0101F#5P手強いのも頷けるわね……\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    def lambda_123D():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_123D)
    Sleep(50)

    def lambda_124D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_124D)
    Sleep(50)

    def lambda_125D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_125D)
    Sleep(50)

    def lambda_126D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_126D)
    Sleep(50)

    def lambda_127D():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_127D)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x102, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x104, 1)
    WaitChrThread(0x106, 1)

    #C0019
    ChrTalk(
        0x101,
        (
            "#0003F#5P……とにかく探索を始めよう。\x02\x03",

            "#0013Fセシル姉によれば、まだ教授たちが\x01",
            "取り残されている可能性が高い。\x02\x03",

            "ヨアヒム先生共々、見つけ出すんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x102,
        "#0101F#2Pええ……！\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        (
            "#0301F#12P手遅れになる前に\x01",
            "急ぐ必要がありそうだな……！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    SetChrPos(0x0, 4500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xE3, 0)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_8_F41 end

    def Function_9_13B7(): pass

    label("Function_9_13B7")


    def lambda_13BC():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13BC)

    def lambda_13D1():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_13D1)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_13EA():
        OP_95(0xFE, 2600, 0, 580, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_13EA)
    WaitChrThread(0x101, 1)

    def lambda_1408():
        OP_93(0xFE, 0x5A, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1408)
    WaitChrThread(0x101, 1)
    Return()

    # Function_9_13B7 end

    def Function_10_1415(): pass

    label("Function_10_1415")


    def lambda_141A():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_141A)

    def lambda_142F():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_142F)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1448():
        OP_95(0xFE, 2700, 0, -1220, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1448)
    WaitChrThread(0xFE, 1)

    def lambda_1466():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1466)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_1415 end

    def Function_11_1473(): pass

    label("Function_11_1473")


    def lambda_1478():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1478)

    def lambda_148D():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_148D)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_14A6():
        OP_95(0xFE, 1380, 0, -1820, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14A6)
    WaitChrThread(0xFE, 1)

    def lambda_14C4():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14C4)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_1473 end

    def Function_12_14D1(): pass

    label("Function_12_14D1")


    def lambda_14D6():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_14D6)

    def lambda_14EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_14EB)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1504():
        OP_95(0xFE, 1420, 0, 1670, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1504)
    WaitChrThread(0xFE, 1)

    def lambda_1522():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1522)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_12_14D1 end

    def Function_13_152F(): pass

    label("Function_13_152F")


    def lambda_1534():
        OP_9B(0x0, 0xFE, 0x0, 0x5DC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1534)

    def lambda_1549():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1549)
    WaitChrThread(0xFE, 1)
    WaitChrThread(0xFE, 2)

    def lambda_1562():
        OP_95(0xFE, 950, 0, 40, 2000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1562)
    WaitChrThread(0xFE, 1)

    def lambda_1580():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1580)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_13_152F end

    SaveToFile()

Try(main)
