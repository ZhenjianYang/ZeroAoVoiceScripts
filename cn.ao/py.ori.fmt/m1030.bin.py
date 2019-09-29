from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m1030.bin",                # FileName
        "m1030",                    # MapName
        "m1030",                    # Location
        0x006D,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 109, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1030",                  # 0
        "bm1000",                 # 1
        "bm1020",                 # 2
        "bm1020",                 # 3
    ))

    ATBonus("ATBonus_1B4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_A99", 0,   0,   21,  7,   5,   11,  8)
    Sepith("Sepith_A91", 19,  0,   0,   10,  10,  8,   8)
    Sepith("Sepith_AA1", 0,   21,  0,   9,   6,   8,   8)

    MonsterBattlePostion("MonsterBattlePostion_204", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_268", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_26C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_270", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_274", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_278", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_414", 0x0000, 90, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_A99", 40, 30, 20, 10,
        (
            ("ms64600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms64600.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms64600.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
        )
    )

    BattleInfo(
        "BattleInfo_284", 0x0000, 90, 6, 60, 4, 1, 25, 0, "bm1000", "Sepith_A91", 40, 30, 20, 10,
        (
            ("ms63300.dat", "ms63300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms63300.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
        )
    )

    BattleInfo(
        "BattleInfo_34C", 0x0000, 90, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_AA1", 40, 30, 20, 10,
        (
            ("ms62800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms62800.dat", "ms62800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7450", "ed7453", "ATBonus_1B4"),
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
        "monster/ch63350.itc",               # 10
        "monster/ch63351.itc",               # 11
        "monster/ch62850.itc",               # 12
        "monster/ch62850.itc",               # 13
        "monster/ch64650.itc",               # 14
        "monster/ch64650.itc",               # 15
    ))

    DeclMonster(7670,    -24260,  0,       0x1010000,    "BattleInfo_414", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-5830,   160,     0,       0x1010000,    "BattleInfo_284", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-24680,  -7250,   0,       0x1010000,    "BattleInfo_34C", 0,   18,  0xFFFF, 2,  3)

    DeclActor(2380,    0,       -18220,  1200,    2380,    1000,    -18220,  0x007C, 0,  2,  0x0000)
    DeclActor(-25500,  0,       0,       1200,    -25500,  1000,    0,       0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5

    ScpFunction((
        "Function_0_534",          # 00, 0
        "Function_1_535",          # 01, 1
        "Function_2_7F3",          # 02, 2
        "Function_3_92E",          # 03, 3
    ))


    def Function_0_534(): pass

    label("Function_0_534")

    Return()

    # Function_0_534 end

    def Function_1_535(): pass

    label("Function_1_535")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_54C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_54C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_57D")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_57D")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D7")
    OP_70(0x0, 0x0)
    Jump("loc_7DB")

    label("loc_7D7")

    OP_70(0x0, 0x1E)

    label("loc_7DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7EE")
    OP_70(0x1, 0x0)
    Jump("loc_7F2")

    label("loc_7EE")

    OP_70(0x1, 0x1E)

    label("loc_7F2")

    Return()

    # Function_1_535 end

    def Function_2_7F3(): pass

    label("Function_2_7F3")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8E5")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x406, 1)"), scpexpr(EXPR_END)), "loc_876")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x406),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F7, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_8E0")

    label("loc_876")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x406),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x406),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8E0")

    Jump("loc_922")

    label("loc_8E5")

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

    label("loc_922")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_7F3 end

    def Function_3_92E(): pass

    label("Function_3_92E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A20")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_9B1")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F7, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_A1B")

    label("loc_9B1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A1B")

    Jump("loc_A5D")

    label("loc_A20")

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

    label("loc_A5D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_92E end

    SaveToFile()

Try(main)
