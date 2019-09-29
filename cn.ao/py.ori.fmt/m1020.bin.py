from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m1020.bin",                # FileName
        "m1020",                    # MapName
        "m1020",                    # Location
        0x006C,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 108, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1020",                  # 0
        "bm1020",                 # 1
        "bm1020",                 # 2
    ))

    ATBonus("ATBonus_194", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_E8B", 0,   0,   21,  7,   5,   11,  8)
    Sepith("Sepith_E93", 0,   21,  0,   9,   6,   8,   8)

    MonsterBattlePostion("MonsterBattlePostion_1E4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_244", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_248", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_24C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_250", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_254", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_258", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_25C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_260", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_1C4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1C8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1CC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_32C", 0x0000, 90, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_E8B", 40, 30, 20, 10,
        (
            ("ms64600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_244", "ed7450", "ed7453", "ATBonus_194"),
            ("ms64600.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1C4", "MonsterBattlePostion_244", "ed7450", "ed7453", "ATBonus_194"),
            ("ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_244", "ed7450", "ed7453", "ATBonus_194"),
            ("ms64600.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_1C4", "MonsterBattlePostion_244", "ed7450", "ed7453", "ATBonus_194"),
        )
    )

    BattleInfo(
        "BattleInfo_264", 0x0000, 90, 6, 60, 4, 1, 30, 0, "bm1020", "Sepith_E93", 40, 30, 20, 10,
        (
            ("ms62800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_244", "ed7450", "ed7453", "ATBonus_194"),
            ("ms62800.dat", "ms62800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1C4", "MonsterBattlePostion_244", "ed7450", "ed7453", "ATBonus_194"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_244", "ed7450", "ed7453", "ATBonus_194"),
            ("ms62800.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_1C4", "MonsterBattlePostion_244", "ed7450", "ed7453", "ATBonus_194"),
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

    DeclMonster(-31440,  3550,    0,       0x1010000,    "BattleInfo_32C", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-620,    25220,   0,       0x1010000,    "BattleInfo_264", 0,   18,  0xFFFF, 2,  3)

    DeclActor(-5650,   0,       30610,   1200,    -5650,   1000,    30610,   0x007C, 0,  2,  0x0000)
    DeclActor(14870,   0,       -18100,  1200,    14870,   1000,    -18100,  0x007C, 0,  3,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5

    ScpFunction((
        "Function_0_450",          # 00, 0
        "Function_1_47E",          # 01, 1
        "Function_2_666",          # 02, 2
        "Function_3_7A1",          # 03, 3
        "Function_4_908",          # 04, 4
    ))


    def Function_0_450(): pass

    label("Function_0_450")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x2)"), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x71, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x153, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_47D")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_47D")

    Return()

    # Function_0_450 end

    def Function_1_47E(): pass

    label("Function_1_47E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_495")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_495")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_4C1")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    OP_65(0x0, 0x1)
    OP_65(0x1, 0x1)

    label("loc_4C1")

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
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_64A")
    OP_70(0x0, 0x0)
    Jump("loc_64E")

    label("loc_64A")

    OP_70(0x0, 0x1E)

    label("loc_64E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_661")
    OP_70(0x1, 0x0)
    Jump("loc_665")

    label("loc_661")

    OP_70(0x1, 0x1E)

    label("loc_665")

    Return()

    # Function_1_47E end

    def Function_2_666(): pass

    label("Function_2_666")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F6, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_758")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x654, 1)"), scpexpr(EXPR_END)), "loc_6E9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x654),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F6, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_753")

    label("loc_6E9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x654),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x654),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_753")

    Jump("loc_795")

    label("loc_758")

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

    label("loc_795")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_666 end

    def Function_3_7A1(): pass

    label("Function_3_7A1")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F7, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8D9")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x1, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 200)
    AddSepith(0x1, 200)
    AddSepith(0x2, 200)
    AddSepith(0x3, 200)
    AddSepith(0x4, 200)
    AddSepith(0x5, 200)
    AddSepith(0x6, 200)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×２００\x01\x07\x02",

            "#57I水之耀晶片×２００\x01\x07\x02",

            "#58I火之耀晶片×２００\x01\x07\x02",

            "#59I风之耀晶片×２００\x01\x07\x02",

            "#60I时之耀晶片×２００\x01\x07\x02",

            "#61I空之耀晶片×２００\x01\x07\x02",

            "#62I幻之耀晶片×２００\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F7, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_8F6")

    label("loc_8D9")


    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_8F6")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_7A1 end

    def Function_4_908(): pass

    label("Function_4_908")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(-800, 3200, -27100, 0)
    MoveCamera(355, -8, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(13600, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_A14")
    SetChrPos(0x101, 200, 0, -33600, 0)
    SetChrPos(0x102, -1560, 0, -33880, 0)
    SetChrPos(0x103, 1560, 0, -33880, 0)
    SetChrPos(0x104, -1560, 0, -35050, 0)
    SetChrPos(0x109, -200, 0, -35050, 0)
    SetChrPos(0x105, 1560, 0, -35050, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    Jump("loc_AAA")

    label("loc_A14")

    SetChrPos(0x101, -970, 0, -33880, 0)
    SetChrPos(0x102, 570, 0, -33880, 0)
    SetChrPos(0x104, -1560, 0, -35050, 0)
    SetChrPos(0x109, -200, 0, -35050, 0)
    SetChrPos(0x105, 1560, 0, -35050, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)

    label("loc_AAA")

    FadeToBright(1000, 0)
    OP_0D()
    OP_68(-800, 3200, -27100, 7000)
    MoveCamera(47, -8, 0, 7000)
    OP_6E(550, 7000)
    SetCameraDistance(13600, 7000)
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(-1030, 3900, -2690, 0)
    MoveCamera(23, 14, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(55250, 0)
    OP_0D()
    OP_68(-1030, 3900, -2690, 7000)
    MoveCamera(23, 14, 0, 7000)
    OP_6E(550, 7000)
    SetCameraDistance(79120, 7000)
    PlaceName2(340, 200, "c_plac28", 0x0, 3000)
    OP_6F(0x79)
    Sleep(3000)
    Fade(1000)
    OP_68(-5050, 4000, -37070, 0)
    MoveCamera(44, 21, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(13920, 0)
    OP_A7(0x101, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x102, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x104, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x109, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    OP_A7(0x105, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_BE4")
    OP_A7(0x103, 0xFF, 0xFF, 0xFF, 0xFF, 0x0)

    label("loc_BE4")

    OP_0D()

    #C0006
    ChrTalk(
        0x101,
        "#00003F……好安静啊……\x02",
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x109,
        (
            "#10104F据报告称，自教团事件结束之后，\x01",
            "此地的魔兽便消失了踪影。\x02\x03",

            "#10100F正因如此，\x01",
            "才允许民间人士\x01",
            "来这里调查。\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x102,
        (
            "#00108F看来和『僧院』相同，\x01",
            "魔兽的消失应该与最上层的那口『钟』\x01",
            "存在着某些关系吧……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_D3D")

    #C0009
    ChrTalk(
        0x103,
        (
            "#00203F那口『钟』吗……\x01",
            "的确有可能。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x105,
        (
            "#10305F说起来，我也听说过\x01",
            "这里有那种东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D7A")

    label("loc_D3D")


    #C0011
    ChrTalk(
        0x105,
        (
            "#10303F『钟』吗……\x01",
            "说起来，我也听说过\x01",
            "这里有那种东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D7A")


    #C0012
    ChrTalk(
        0x104,
        (
            "#00302F这里已经没有敌人了，\x01",
            "从某种意义上说，也算是幸运吧？\x02\x03",

            "#00309F我们就加快脚步前进吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        (
            "#00000F嗯……\x01",
            "但还是不能\x01",
            "放松警惕。\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_E2B")
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    Jump("loc_E35")

    label("loc_E2B")

    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)

    label("loc_E35")

    SetChrPos(0x0, 100, 0, -34300, 0)
    OP_69(0xFF, 0x0)
    OP_29(0x71, 0x1, 0x3)
    SetScenarioFlags(0x153, 2)
    ClearMapFlags(0x10000000)
    EventEnd(0x5)
    Return()

    # Function_4_908 end

    SaveToFile()

Try(main)
