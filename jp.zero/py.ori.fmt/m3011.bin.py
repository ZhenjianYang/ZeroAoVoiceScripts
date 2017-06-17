from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3011.bin",                # FileName
        "M3011",                    # MapName
        "M3011",                    # Location
        0x007B,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 123, 0, 1, 0, 2],
    )

    BuildStringList((
        "m3011",                  # 0
        "ザン・スー",             # 1
        "bm3000",                 # 2
        "bm3000",                 # 3
        "bm3000",                 # 4
        "bm3000",                 # 5
        "bm3000",                 # 6
    ))

    ATBonus("ATBonus_294", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_10EF", 0,   29,  0,   0,   9,   3,   19)
    Sepith("Sepith_10F7", 24,  0,   0,   2,   8,   14,  14)
    Sepith("Sepith_10FF", 3,   0,   3,   23,  9,   9,   13)
    Sepith("Sepith_10E7", 4,   4,   20,  0,   16,  12,  7)

    MonsterBattlePostion("MonsterBattlePostion_2F4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_358", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_35C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_360", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_364", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_368", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_36C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 2, 13, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_3B8", 0x0000, 37, 6, 60, 4, 1, 40, 0, "bm3000", "Sepith_10EF", 60, 25, 10, 5,
        (
            ("ms68600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms68600.dat", "ms68600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms68600.dat", "ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
        )
    )

    BattleInfo(
        "BattleInfo_548", 0x0000, 37, 6, 60, 4, 1, 35, 0, "bm3000", "Sepith_10F7", 60, 25, 10, 5,
        (
            ("ms70900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms70900.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms70900.dat", "ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms70900.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
        )
    )

    BattleInfo(
        "BattleInfo_374", 0x0010, 37, 6, 60, 4, 1, 30, 0, "bm3000", "Sepith_10FF", 100, 0, 0, 0,
        (
            ("ms64700.dat", 0, 0, 0, 0, 0, "ms60600.dat", 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_480", 0x0000, 37, 6, 60, 4, 1, 30, 0, "bm3000", "Sepith_10E7", 60, 25, 10, 5,
        (
            ("ms60600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
            ("ms60600.dat", "ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_2F4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_610", 0x0010, 37, 6, 60, 0, 1, 0, 0, "bm3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64700.dat", "ms64700.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", 0, "MonsterBattlePostion_2D4", "MonsterBattlePostion_354", "ed7402", "ed7403", "ATBonus_294"),
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
        "monster/ch64750.itc",               # 10
        "monster/ch64750.itc",               # 11
        "monster/ch68650.itc",               # 12
        "monster/ch68651.itc",               # 13
        "monster/ch60650.itc",               # 14
        "monster/ch60650.itc",               # 15
        "monster/ch70950.itc",               # 16
        "monster/ch70951.itc",               # 17
    ))

    DeclNpc(165000,  -22500,  -48750,  0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(193990,  -24550,  106000,  0x1010000,    "BattleInfo_3B8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(168860,  -29810,  106000,  0x1010000,    "BattleInfo_548", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(155810,  -21710,  -18000,  0x1010000,    "BattleInfo_3B8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(25060,   -48350,  -18000,  0x1010000,    "BattleInfo_374", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(1510,    -20720,  -21000,  0x1010000,    "BattleInfo_3B8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(1100,    18990,   -21000,  0x1010000,    "BattleInfo_480", 0,   20,  0xFFFF, 4,  5)

    DeclActor(1370,    -21000,  21880,   1200,    1370,    -20000,  21880,   0x007C, 0,  3,  0x0000)
    DeclActor(25500,   -18000,  -51750,  1200,    25500,   -17000,  -51750,  0x007C, 0,  4,  0x0000)
    DeclActor(165000,  -24000,  -48750,  1200,    165000,  -23000,  -48750,  0x007C, 0,  5,  0x0000)
    DeclActor(168750,  -24000,  -45000,  1200,    168750,  -23000,  -45000,  0x007C, 0,  6,  0x0000)
    DeclActor(165000,  -17500,  -38750,  1200,    165000,  -16500,  -38750,  0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_6D4",          # 00, 0
        "Function_1_6F3",          # 01, 1
        "Function_2_6F4",          # 02, 2
        "Function_3_917",          # 03, 3
        "Function_4_A64",          # 04, 4
        "Function_5_BB1",          # 05, 5
        "Function_6_DC4",          # 06, 6
        "Function_7_F11",          # 07, 7
    ))


    def Function_0_6D4(): pass

    label("Function_0_6D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6F2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x1, 0x0, 0x3, 0x4, 0x3)
    Jump("Function_0_6D4")

    label("loc_6F2")

    Return()

    # Function_0_6D4 end

    def Function_1_6F3(): pass

    label("Function_1_6F3")

    Return()

    # Function_1_6F3 end

    def Function_2_6F4(): pass

    label("Function_2_6F4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 1)), scpexpr(EXPR_END)), "loc_70A")
    OP_70(0xC, 0x64)
    OP_70(0xD, 0x3C)
    Jump("loc_712")

    label("loc_70A")

    OP_70(0xC, 0x0)
    OP_70(0xD, 0x0)

    label("loc_712")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C7")
    OP_70(0x2, 0x0)
    Jump("loc_8CB")

    label("loc_8C7")

    OP_70(0x2, 0x1E)

    label("loc_8CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DE")
    OP_70(0x5, 0x0)
    Jump("loc_8E2")

    label("loc_8DE")

    OP_70(0x5, 0x1E)

    label("loc_8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F5")
    OP_70(0x6, 0x0)
    Jump("loc_8F9")

    label("loc_8F5")

    OP_70(0x6, 0x1E)

    label("loc_8F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90C")
    OP_70(0x7, 0x0)
    Jump("loc_910")

    label("loc_90C")

    OP_70(0x7, 0x1E)

    label("loc_910")

    Sound(129, 1, 100, 0)
    Return()

    # Function_2_6F4 end

    def Function_3_917(): pass

    label("Function_3_917")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A13")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x55, 1)"), scpexpr(EXPR_END)), "loc_99C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11F, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_A0E")

    label("loc_99C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x55),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A0E")

    Jump("loc_A58")

    label("loc_A13")

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

    label("loc_A58")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_917 end

    def Function_4_A64(): pass

    label("Function_4_A64")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B60")
    Sound(14, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_AE9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x11F, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_B5B")

    label("loc_AE9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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

    label("loc_B5B")

    Jump("loc_BA5")

    label("loc_B60")

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

    label("loc_BA5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A64 end

    def Function_5_BB1(): pass

    label("Function_5_BB1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7E")
    Sound(14, 0, 100, 0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAC")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_C0A():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_C0A)

    def lambda_C24():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_C24)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_610", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C8D"),
        (2, "loc_C9C"),
        (1, "loc_CA9"),
        (SWITCH_DEFAULT, "loc_CAC"),
    )


    label("loc_C8D")

    SetScenarioFlags(0x76, 3)
    OP_70(0x6, 0x1E)
    Sleep(500)
    Jump("loc_CAC")

    label("loc_C9C")

    OP_70(0x6, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_CA9")

    OP_B7(0x0)
    Return()

    label("loc_CAC")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x407, 1)"), scpexpr(EXPR_END)), "loc_D09")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x407),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11F, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_D79")

    label("loc_D09")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x407),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x407),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x6, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D79")

    Jump("loc_DB8")

    label("loc_D7E")

    FadeToDark(300, 0, 100)

    #A0010
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

    label("loc_DB8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_BB1 end

    def Function_6_DC4(): pass

    label("Function_6_DC4")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC0")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_E49")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0011
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
    SetScenarioFlags(0x11F, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_EBB")

    label("loc_E49")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0012
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
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EBB")

    Jump("loc_F05")

    label("loc_EC0")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0013
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

    label("loc_F05")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_DC4 end

    def Function_7_F11(): pass

    label("Function_7_F11")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF4, 1)), scpexpr(EXPR_END)), "loc_F58")
    TalkBegin(0xFF)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もうレバーは動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_10BE")

    label("loc_F58")

    EventBegin(0x1)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レバーが取り付けられている。\x01",
            "動かしますか？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "は　い\x01",      # 0
            "いいえ\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B7")
    Fade(500)
    SetChrPos(0x0, 165540, -18000, -37690, 180)
    SetChrPos(0x1, 166750, -18000, -36030, 180)
    SetChrPos(0x2, 165390, -18000, -35830, 180)
    SetChrPos(0x3, 166270, -18000, -35080, 180)
    OP_68(165160, -17000, -37720, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(340, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sound(142, 0, 100, 0)
    OP_71(0xC, 0x0, 0x64, 0x0, 0x0)
    OP_79(0xC)
    Sleep(500)
    Fade(500)
    OP_68(167000, -23000, -36890, 0)
    MoveCamera(45, 44, 0, 0)
    OP_6E(560, 0)
    SetCameraDistance(30000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    OP_71(0xD, 0x0, 0x3C, 0x0, 0x0)
    OP_79(0xD)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0xF4, 1)

    label("loc_10B7")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_10BE")

    Return()

    # Function_7_F11 end

    SaveToFile()

Try(main)
