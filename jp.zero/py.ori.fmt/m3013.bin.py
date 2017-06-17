from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

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

    Sepith("Sepith_1815", 9,   12,  6,   16,  2,   13,  4)
    Sepith("Sepith_180D", 12,  6,   17,  9,   12,  4,   2)
    Sepith("Sepith_181D", 15,  9,   14,  5,   3,   0,   14)

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
        "BattleInfo_34C", 0x0000, 38, 6, 60, 4, 1, 40, 0, "bm3010", "Sepith_1815", 60, 25, 10, 5,
        (
            ("ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
        )
    )

    BattleInfo(
        "BattleInfo_284", 0x0010, 38, 6, 60, 4, 1, 50, 0, "bm3010", "Sepith_180D", 60, 25, 10, 5,
        (
            ("ms67200.dat", 0, 0, 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67200.dat", "ms72100.dat", 0, 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67200.dat", "ms72100.dat", "ms72100.dat", 0, 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_204", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
            ("ms67200.dat", "ms72100.dat", "ms72100.dat", "ms72100.dat", 0, 0, "ms67200.dat", 0, "MonsterBattlePostion_1E4", "MonsterBattlePostion_264", "ed7402", "ed7403", "ATBonus_1A4"),
        )
    )

    BattleInfo(
        "BattleInfo_414", 0x0000, 38, 6, 60, 4, 1, 30, 0, "bm3010", "Sepith_181D", 60, 25, 10, 5,
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
        "Function_3_8F8",          # 03, 3
        "Function_4_1689",         # 04, 4
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x108, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8A7")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x58, 1)"), scpexpr(EXPR_END)), "loc_830")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x58),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x108, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_8A2")

    label("loc_830")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x58),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x58),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_8A2")

    Jump("loc_8EC")

    label("loc_8A7")

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

    label("loc_8EC")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_7AB end

    def Function_3_8F8(): pass

    label("Function_3_8F8")

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9F9")
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

    label("loc_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C32")

    #C0004
    ChrTalk(
        0x107,
        "#6P#0800F動いた……！\x02",
    )

    CloseMessageWindow()

    #C0005
    ChrTalk(
        0x103,
        (
            "#11P#0203F数年前に財団が開発した\x01",
            "情報処理システムですね。\x02\x03",

            "#0201F今となっては旧式ですが\x01",
            "当時は相当高価だったはずです。\x02",
        )
    )

    CloseMessageWindow()

    #C0006
    ChrTalk(
        0x102,
        (
            "#0106F#12P多分ミラは、ハルトマン議長が\x01",
            "用意したんでしょうね……\x02",
        )
    )

    CloseMessageWindow()

    #C0007
    ChrTalk(
        0x101,
        (
            "#12P#0003Fああ……いずれその辺りも\x01",
            "徹底的に洗う必要がありそうだな。\x02\x03",

            "#0001Fティオ、他に何か分かるか？\x02",
        )
    )

    CloseMessageWindow()

    #C0008
    ChrTalk(
        0x103,
        "#11P#0201Fはい……\x02",
    )

    CloseMessageWindow()
    Sound(849, 0, 100, 0)
    Sleep(1000)

    #C0009
    ChrTalk(
        0x103,
        (
            "#11P#0205F──どうやらこの端末では\x01",
            "隔壁のロックの解除と\x01",
            "情報の閲覧が出来るようです。\x02\x03",

            "#0206Fもっとも情報は一部しか\x01",
            "残っていないようですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x101,
        (
            "#12P#0000F十分だ……\x01",
            "さっそく調べてみよう。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xE5, 1)

    label("loc_C32")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_C3C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_165C")
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
            "#1K第０１情報端末\x07\x00\x02",
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
        (0, "loc_CF4"),
        (1, "loc_1574"),
        (2, "loc_1639"),
        (SWITCH_DEFAULT, "loc_1648"),
    )


    label("loc_CF4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, 34, -1)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#2S『教団について』\x01\x01",
            "──私の名はヨアヒム・ギュンター。\x01",
            "《Ｄ∴Ｇ教団》に属する幹部司祭である。\x01",
            "６年前、遊撃士を含む多くの勢力の手で\x01",
            "我が教団は壊滅状態に陥ってしまった。\x01",
            "しかし、私だけは故あって難を逃れ、\x01",
            "この■■の地へと落ち延びる事ができた。\x01",
            "大いなる《■》の導きによって\x01",
            "教団の大望を成すべく私は永らえたのだ。\x01",
            "いずれ来るその時──\x01",
            "新たな聖典を記すための資料として\x01",
            "各端末にデータを記録しておく事とする。\x07\x00\x02",
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
            "#2Sまず、我が教団の成り立ちについて語ろう。\x01",
            "そのためには、このゼムリア大陸が辿った\x01",
            "忌々しい歴史を振り返る必要がある。\x01\x01",
            "──約１２００年前の《大崩壊》によって\x01",
            "大陸は高度な文明と秩序を失い、\x01",
            "戦と貧困の支配する《暗黒時代》が訪れた。\x01",
            "そして、疲れ果てた人々は\x01",
            "大いなる間違いを犯してしまった。\x01\x01",
            "突如現れた愚か者どもの甘言に惑わされ、\x01",
            "彼らの作りだした身勝手な秩序を\x01",
            "受け入れてしまったのだ。\x07\x00\x02",
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
            "#2Sすなわち──愚かなる■■■■と\x01",
            "信仰の象徴たる《■の■■》である。\x01",
            "彼らの秩序によって《暗黒時代》は終焉し、\x01",
            "その信仰はたちまち大陸中に広まったが……\x01\x01",
            "よく考えてみてほしい。\x01",
            "もし真に《■■》が存在するというのならば\x01",
            "誰もが等しく救いを受けるべきではないか？\x01",
            "しかし、未だに格差の概念は無くならず、\x01",
            "災厄や不幸で命を落とす者も後を絶たない。\x01\x01",
            "《■■》は救う人間を選ぶというのか？\x01",
            "あまりに馬鹿馬鹿しい話ではないか。\x07\x00\x02",
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
            "#2S所詮は■■■■が権威を得るため\x01",
            "作りだした虚像に過ぎないのである。\x01",
            "《■■》など、存在するわけがないのだ。\x01\x01",
            "真理に辿りついた我々の先人たちは、\x01",
            "《■■■■》に邂逅すべく長き旅路に出た。\x01\x01",
            "そして時代が中世に移り変わる頃、\x01",
            "ついに彼らは見出したのである。\x01",
            "この地の奥深くで■■■■■■■■■■\x01",
            "■■■■■■■■■■■■■■■……\x01\x01",
            "《■》──それはそう呼ばれていた。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_156F")

    #C0016
    ChrTalk(
        0x101,
        (
            "#0008F#11Pこれは……\x01",
            "ヨアヒム先生が残したものか。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#0108F#12P教団についての概要が\x01",
            "残されているみたいだけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x104,
        "#0301F#12Pしかし所々、読めなくなってるな。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x103,
        (
            "#0203F#5P恐らく意図的に\x01",
            "削除したのだと思います。\x02\x03",

            "#0201Fデータの復旧は\x01",
            "難しいかもしれませんね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x107,
        (
            "#0801F#6Pでも、ここで消されてるのって\x01",
            "『七耀教会』とか『空の女神』よね？\x02\x03",

            "#0806F女神の存在を否定するって\x01",
            "公言してたみたいだし……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x108,
        (
            "#0903F#6Pああ、間違いないだろうね。\x02\x03",

            "#0901Fそれ以外にも、気になる単語が\x01",
            "削除されているみたいだけど……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0xF1, 1)

    label("loc_156F")

    Jump("loc_1657")

    label("loc_1574")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15CA")
    SetChrName("")

    #A0022
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
    SetScenarioFlags(0xE5, 2)
    OP_29(0x4F, 0x1, 0x3)
    Call(0, 4)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1634")

    label("loc_15CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1603")
    SetChrName("")

    #A0023
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
    Jump("loc_1634")

    label("loc_1603")

    SetChrName("")

    #A0024
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

    label("loc_1634")

    Jump("loc_1657")

    label("loc_1639")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1657")

    label("loc_1648")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1657")

    label("loc_1657")

    Jump("loc_C3C")

    label("loc_165C")

    SetChrPos(0x0, -45000, -27000, 136400, 180)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_3_8F8 end

    def Function_4_1689(): pass

    label("Function_4_1689")

    Fade(500)
    OP_68(0, -23000, 18000, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(25000, 0)
    OP_0D()
    Sleep(500)
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 2)), scpexpr(EXPR_END)), "loc_16E1")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16E1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 3)), scpexpr(EXPR_END)), "loc_16F8")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_16F8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xE5, 4)), scpexpr(EXPR_END)), "loc_170F")
    RunExpression(0x2, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_170F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1751")
    OP_71(0x1, 0x14, 0x5A, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    Sleep(700)
    Sound(135, 0, 100, 0)
    OP_79(0x1)
    Sound(116, 0, 100, 0)
    OP_70(0x1, 0x5A)
    ClearMapObjFlags(0x1, 0x2)
    Jump("loc_17C1")

    label("loc_1751")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1784")
    OP_71(0x1, 0xA, 0x14, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x1)
    OP_70(0x1, 0x14)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_17C1")

    label("loc_1784")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17B7")
    OP_71(0x1, 0x0, 0xA, 0x0, 0x0)
    Sound(140, 0, 100, 0)
    OP_79(0x1)
    OP_70(0x1, 0xA)
    SetMapObjFlags(0x1, 0x2)
    Jump("loc_17C1")

    label("loc_17B7")

    OP_70(0x1, 0x0)
    SetMapObjFlags(0x1, 0x2)

    label("loc_17C1")

    Sleep(1000)
    Return()

    # Function_4_1689 end

    SaveToFile()

Try(main)
