from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m3013.bin",                # FileName
        "M3013",                    # MapName
        "M3013",                    # Location
        0x007C,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 124, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3013",                  # 0
        "bm3010",                 # 1
        "bm3010",                 # 2
        "bm3010",                 # 3
    ))

    ATBonus("ATBonus_1A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1652", 9,   12,  6,   16,  2,   13,  4)
    Sepith("Sepith_164A", 12,  6,   17,  9,   12,  4,   2)
    Sepith("Sepith_165A", 15,  9,   14,  5,   3,   0,   14)

    MonsterBattlePostion("MonsterBattlePostion_1E4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1F8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1FC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_200", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_264", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_268", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_26C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_270", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_274", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_278", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_27C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_204", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_208", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_20C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_210", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_214", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_21C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_220", 8, 14, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_34C", 0x0000, 38, 6, 60, 4, 1, 40, 0, "bm3010", "Sepith_1652", 60, 25, 10, 5,
        (
            ("ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
        )
    )

    BattleInfo(
        "BattleInfo_284", 0x0010, 38, 6, 60, 4, 1, 50, 0, "bm3010", "Sepith_164A", 60, 25, 10, 5,
        (
            ("ms67200.dat", 0, 0, 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67200.dat", "ms72100.dat", 0, 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67200.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67200.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
        )
    )

    BattleInfo(
        "BattleInfo_414", 0x0000, 38, 6, 60, 4, 1, 30, 0, "bm3010", "Sepith_165A", 60, 25, 10, 5,
        (
            ("ms67500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67500.dat", "ms67500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67500.dat", "ms67500.dat", "ms67500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67500.dat", "ms67500.dat", "ms67500.dat", "ms67500.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
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
        "monster/ch67250.itc",               # 10
        "monster/ch67251.itc",               # 11
        "monster/ch72150.itc",               # 12
        "monster/ch72151.itc",               # 13
        "monster/ch67550.itc",               # 14
        "monster/ch67551.itc",               # 15
    ))

    DeclMonster(-260,    14750,   -24000,  0x1010000,    "BattleInfo_34C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-33270,  14410,   -27000,  0x1010000,    "BattleInfo_284", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-54090,  -113940, -27000,  0x1010000,    "BattleInfo_414", 0,   20,  0xFFFF, 4,  5)

    DeclActor(-45000,  -27000,  139000,  1500,    -45000,  -26000,  139000,  0x007C, 0,  3,  0x0000)
    DeclActor(-51000,  -27000,  -114000, 1200,    -51000,  -26000,  -114000, 0x007C, 0,  2,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_538",          # 00, 0
        "Function_1_539",          # 01, 1
        "Function_2_7AB",          # 02, 2
        "Function_3_8E1",          # 03, 3
        "Function_4_14C6",         # 04, 4
    ))


    def Function_0_538(): pass

    label("Function_0_538")

    Return()

    # Function_0_538 end

    def Function_1_539(): pass

    label("Function_1_539")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 4)), scpexpr(EXPR_END)), "loc_54E")
    OP_71(0x2, 0x96, 0xD2, 0x0, 0x20)

    label("loc_54E")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_56F")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_56F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_586")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_586")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_59D")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_59D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5BB")
    OP_70(0x1, 0x5A)
    ClearMapObjFlags(0x1, 0x2)
    Jump("loc_601")

    label("loc_5BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D9")
    OP_70(0x1, 0x14)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_601")

    label("loc_5D9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F7")
    OP_70(0x1, 0xA)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_601")

    label("loc_5F7")

    OP_70(0x1, 0x0)
    SetMapObjFlags(0x1, 0x2)

    label("loc_601")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78A")
    OP_70(0x0, 0x0)
    Jump("loc_78E")

    label("loc_78A")

    OP_70(0x0, 0x1E)

    label("loc_78E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7A4")
    OP_24(0x85)
    Jump("loc_7AA")

    label("loc_7A4")

    Sound(133, 1, 100, 0)

    label("loc_7AA")

    Return()

    # Function_1_539 end

    def Function_2_7AB(): pass

    label("Function_2_7AB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_898")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('常青之绿', 1)"), scpexpr(EXPR_END)), "loc_82A")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '常青之绿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x108, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_893")

    label("loc_82A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '常青之绿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '常青之绿'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_893")

    Jump("loc_8D5")

    label("loc_898")

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

    label("loc_8D5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_7AB end

    def Function_3_8E1(): pass

    label("Function_3_8E1")

    EventBegin(0x0)
    SetMapFlags(0x8000000)
    Fade(1000)
    OP_68(-44520, -26000, 137730, 0)
    MoveCamera(40, 23, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(21520, 0)
    SetChrPos(0x101, -44800, -27000, 136500, 0)
    SetChrPos(0x102, -43800, -27000, 136500, 0)
    SetChrPos(0x103, -44300, -27000, 138000, 0)
    SetChrPos(0x104, -44300, -27000, 135400, 0)
    SetChrPos(0x107, -46400, -27000, 137300, 45)
    SetChrPos(0x108, -46300, -27000, 136400, 45)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9E2")
    OP_71(0x2, 0x0, 0x96, 0x0, 0x0)
    Sound(72, 0, 100, 0)
    Sleep(2000)
    Sound(967, 0, 100, 0)
    Sleep(900)
    Sound(967, 0, 100, 0)
    Sleep(1400)
    Sound(967, 0, 100, 0)
    OP_79(0x2)
    OP_71(0x2, 0x96, 0xD2, 0x0, 0x20)
    Sleep(500)
    SetScenarioFlags(0xF4, 4)

    label("loc_9E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BE7")

    #C0004
    ChrTalk(
        0x107,
        "#6P#0800F启动了……！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        (
            "#11P#0203F是数年前，由财团开发出的\x01",
            "情报处理系统呢。\x02\x03",

            "#0201F虽然现在已经属于旧型号了，\x01",
            "但当时应该是相当昂贵的东西。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#0106F#12P采购这些东西所花销的米拉，\x01",
            "多半是由哈尔特曼议长提供的吧……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#12P#0003F嗯……总有一天，也有必要\x01",
            "彻底调查一下他那边呢。\x02\x03",

            "#0001F缇欧，还有别的发现吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#11P#0201F是的……\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    #C0009
    ChrTalk(
        0x103,
        (
            "#11P#0205F──操作这个终端似乎可以\x01",
            "解除附近的锁，\x01",
            "还可以浏览情报。\x02\x03",

            "#0206F不过，情报好像\x01",
            "只剩下了一部分……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#12P#0000F足够了……\x01",
            "赶快调查一下吧。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_BE7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_BF1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1499")
    FadeToDark(300, 0, 100)
    OP_0D()
    SetMessageWindowPos(173, 40, -1, -1)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            scpstr(0x6),
            scpstr(0x18),
            "#1K情报终端０１\x07\x00\x02",
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
        (0, "loc_C95"),
        (1, "loc_13D9"),
        (2, "loc_1476"),
        (SWITCH_DEFAULT, "loc_1485"),
    )


    label("loc_C95")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『关于教团』\x01\x01",
            "──我的名字是约亚西姆·琼塔。\x01",
            "隶属于『Ｄ∴Ｇ教团』的干部祭司。\x01",
            "六年前，在众多势力与游击士共同联手之下，\x01",
            "我们的教团被毁灭了。\x01",
            "但是，唯有我逃了出来，\x01",
            "并来到了这片■■之地。\x01",
            "在伟大的『■』的引导下，\x01",
            "为了完成教团的伟业，我努力坚持了下来。\x01",
            "那一刻终将到来──\x01",
            "为了留下书写新时代圣典所用的资料，\x01",
            "我决定把这些数据保存在各个终端之上。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S首先，从我们教团的成立说起吧。\x01",
            "关于这件事，有必要回顾一下\x01",
            "塞姆里亚大陆那段骇人听闻的历史。\x01\x01",
            "──经历了大约在一千两百年前发生的\x01",
            "『大崩坏』，大陆失去了高度的文明与秩序，\x01",
            "迎来了被战争与贫困支配的『黑暗时代』。\x01",
            "最终，精疲力尽的人们\x01",
            "犯下了巨大的错误。\x01\x01",
            "被突然出现的愚蠢之人的花言巧语迷惑，\x01",
            "接受了那些人创造的，\x01",
            "毫无道理的秩序。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S即──愚蠢的■■■■\x01",
            "与象征着其信仰的『■之■■』。\x01",
            "他们创造的秩序使『黑暗时代』终结，\x01",
            "但这种信仰也散播到了大陆各处……\x01\x01",
            "可是，请仔细想一想。\x01",
            "如果『■■』真的存在，\x01",
            "每个人不是应该都能得到平等的救赎吗？\x01",
            "然而，差距这种概念并没有消失，\x01",
            "依然不断有人因为灾难与不幸而丧命。\x01\x01",
            "『■■』在赐予救赎时，难道是有选择性的吗？\x01",
            "这未免也太过愚蠢可笑了吧。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetChrName("")

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S其实，那不过就是■■■■为了得到权势，\x01",
            "而人为创造出来的虚幻存在罢了。\x01",
            "『■■』这种东西，是不可能存在的。\x01\x01",
            "我们那些终于寻得真理的前辈们，\x01",
            "为了与『■■■■』相遇，踏上了漫长的旅途。\x01\x01",
            "时代不断变迁，当中世纪来临时，\x01",
            "他们终于发现了……\x01",
            "在这地底深处，■■■■■■■■■■\x01",
            "■■■■■■■■■■■■■■■……\x01\x01",
            "『■』──便是其名字。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13D4")

    #C0016
    ChrTalk(
        0x101,
        (
            "#0008F#11P这是……\x01",
            "约亚西姆医生留下的吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0108F#12P好像留下了一些\x01",
            "关于教团的概要……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        "#0301F#12P但是有的地方无法阅读。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#0203F#5P恐怕是故意\x01",
            "删除掉的。\x02\x03",

            "#0201F想恢复数据\x01",
            "也许很困难。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x107,
        (
            "#0801F#6P不过，那些被删除的部分，\x01",
            "应该都是『七耀教会』或『空之女神』之类的字眼吧？\x02\x03",

            "#0806F好像是在堂堂正正地\x01",
            "否定女神的存在呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x108,
        (
            "#0903F#6P嗯，应该没错。\x02\x03",

            "#0901F除此之外，敏感的词语\x01",
            "好像也被删除了……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 1)

    label("loc_13D4")

    Jump("loc_1494")

    label("loc_13D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_141B")
    SetChrName("")

    #A0022
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
    SetScenarioFlags(0xE5, 2)
    OP_29(0x4F, 0x1, 0x3)
    Call(0, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1471")

    label("loc_141B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_144E")
    SetChrName("")

    #A0023
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
    Jump("loc_1471")

    label("loc_144E")

    SetChrName("")

    #A0024
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

    label("loc_1471")

    Jump("loc_1494")

    label("loc_1476")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1494")

    label("loc_1485")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1494")

    label("loc_1494")

    Jump("loc_BF1")

    label("loc_1499")

    SetChrPos(0x0, -45000, -27000, 136400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_8E1 end

    def Function_4_14C6(): pass

    label("Function_4_14C6")

    Fade(500)
    OP_68(0, -23000, 18000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_151E")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_151E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_1535")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1535")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_154C")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_154C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158E")
    OP_71(0x1, 0x14, 0x5A, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    Sleep(700)
    Sound(135, 0, 100, 0)
    OP_79(0x1)
    Sound(116, 0, 100, 0)
    OP_70(0x1, 0x5A)
    ClearMapObjFlags(0x1, 0x2)
    Jump("loc_15FE")

    label("loc_158E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15C1")
    OP_71(0x1, 0xA, 0x14, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x1)
    OP_70(0x1, 0x14)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_15FE")

    label("loc_15C1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15F4")
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x1)
    OP_70(0x1, 0xA)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_15FE")

    label("loc_15F4")

    OP_70(0x1, 0x0)
    SetMapObjFlags(0x1, 0x2)

    label("loc_15FE")

    Sleep(1000)
    Return()

    # Function_4_14C6 end

    SaveToFile()

Try(main)
