from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3010.bin",                # FileName
        "M3010",                    # MapName
        "M3010",                    # Location
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
        "m3010",                  # 0
        "ザン・スー",             # 1
        "bm3000",                 # 2
        "bm3000",                 # 3
        "bm3000",                 # 4
        "bm3000",                 # 5
        "bm3000",                 # 6
    ))

    ATBonus("ATBonus_22C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_E04", 3,   0,   3,   23,  9,   9,   13)
    Sepith("Sepith_DEC", 4,   4,   20,  0,   16,  12,  7)
    Sepith("Sepith_DF4", 0,   29,  0,   0,   9,   3,   19)
    Sepith("Sepith_DFC", 24,  0,   0,   2,   8,   14,  14)

    MonsterBattlePostion("MonsterBattlePostion_28C", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_304", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_26C", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_270", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_274", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 2, 13, 180)

    # monster count: 5

    BattleInfo(
        "BattleInfo_30C", 0x0010, 37, 6, 60, 4, 1, 30, 0, "bm3000", "Sepith_E04", 100, 0, 0, 0,
        (
            ("ms64700.dat", 0, 0, 0, 0, 0, "ms60600.dat", 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_418", 0x0000, 37, 6, 60, 4, 1, 30, 0, "bm3000", "Sepith_DEC", 60, 25, 10, 5,
        (
            ("ms60600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms60600.dat", "ms60600.dat", "ms68600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
        )
    )

    BattleInfo(
        "BattleInfo_350", 0x0000, 37, 6, 60, 4, 1, 40, 0, "bm3000", "Sepith_DF4", 60, 25, 10, 5,
        (
            ("ms68600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms68600.dat", "ms68600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms68600.dat", "ms68600.dat", "ms60600.dat", "ms68600.dat", 0, 0, 0, 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
        )
    )

    BattleInfo(
        "BattleInfo_4E0", 0x0000, 37, 6, 60, 4, 1, 35, 0, "bm3000", "Sepith_DFC", 60, 25, 10, 5,
        (
            ("ms70900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms70900.dat", "ms60600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms70900.dat", "ms60600.dat", "ms60600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
            ("ms70900.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", 0, 0, 0, 0, "MonsterBattlePostion_28C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_5A8", 0x0010, 37, 6, 60, 0, 1, 0, 0, "bm3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64700.dat", "ms64700.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", "ms60600.dat", 0, "MonsterBattlePostion_26C", "MonsterBattlePostion_2EC", "ed7402", "ed7403", "ATBonus_22C"),
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

    DeclNpc(28500,   108500,  52500,   0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-1930,   44230,   -21000,  0x1010000,    "BattleInfo_30C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(144660,  29740,   -18000,  0x1010000,    "BattleInfo_418", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(43300,   22510,   107000,  0x1010000,    "BattleInfo_30C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(42820,   52130,   107000,  0x1010000,    "BattleInfo_350", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(169370,  35920,   107000,  0x1010000,    "BattleInfo_4E0", 0,   22,  0xFFFF, 6,  7)

    DeclActor(-1500,   -21000,  48750,   1200,    -1500,   -20000,  48750,   0x007C, 0,  3,  0x0000)
    DeclActor(43500,   107000,  19500,   1200,    43500,   108000,  19500,   0x007C, 0,  4,  0x0000)
    DeclActor(28500,   107000,  52500,   1200,    28500,   108000,  52500,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 7

    ScpFunction((
        "Function_0_664",          # 00, 0
        "Function_1_683",          # 01, 1
        "Function_2_684",          # 02, 2
        "Function_3_917",          # 03, 3
        "Function_4_A64",          # 04, 4
        "Function_5_BB1",          # 05, 5
    ))


    def Function_0_664(): pass

    label("Function_0_664")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_682")
    OP_A1(0xFE, 0x7D0, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_664")

    label("loc_682")

    Return()

    # Function_0_664 end

    def Function_1_683(): pass

    label("Function_1_683")

    Return()

    # Function_1_683 end

    def Function_2_684(): pass

    label("Function_2_684")

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
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8DE")
    OP_70(0x2, 0x0)
    Jump("loc_8E2")

    label("loc_8DE")

    OP_70(0x2, 0x1E)

    label("loc_8E2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8F5")
    OP_70(0x7, 0x0)
    Jump("loc_8F9")

    label("loc_8F5")

    OP_70(0x7, 0x1E)

    label("loc_8F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_90C")
    OP_70(0x8, 0x0)
    Jump("loc_910")

    label("loc_90C")

    OP_70(0x8, 0x1E)

    label("loc_910")

    Sound(129, 1, 100, 0)
    Return()

    # Function_2_684 end

    def Function_3_917(): pass

    label("Function_3_917")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A13")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F9, 1)"), scpexpr(EXPR_END)), "loc_99C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
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
    SetScenarioFlags(0x11F, 0)
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B60")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20A, 1)"), scpexpr(EXPR_END)), "loc_AE9")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11F, 1)
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
            scpstr(SCPSTR_CODE_ITEM, 0x20A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20A),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D7E")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CAC")
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
    Battle("BattleInfo_5A8", 0x0, 0x0, 0x0, 0x0, 0xFF)
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

    SetScenarioFlags(0x76, 2)
    OP_70(0x8, 0x1E)
    Sleep(500)
    Jump("loc_CAC")

    label("loc_C9C")

    OP_70(0x8, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_CA9")

    OP_B7(0x0)
    Return()

    label("loc_CAC")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x651, 1)"), scpexpr(EXPR_END)), "loc_D09")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x651),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11F, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_D79")

    label("loc_D09")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x651),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x651),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

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

    SaveToFile()

Try(main)
