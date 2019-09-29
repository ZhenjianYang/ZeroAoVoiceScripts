from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "m3032.bin",                # FileName
        "m3032",                    # MapName
        "m3032",                    # Location
        0x007E,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 5000, 0, 0, 0, 1, 126, 0, 1, 0, 2],
    )

    BuildStringList((
        "m3032",                  # 0
        "黄金雕像",               # 1
        "bm3040",                 # 2
        "bm3040",                 # 3
        "bm3030",                 # 4
        "bm3030",                 # 5
        "bm3040",                 # 6
    ))

    ATBonus("ATBonus_234", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_107B", 12,  0,   0,   8,   18,  10,  16)
    Sepith("Sepith_10A3", 5,   18,  5,   5,   12,  12,  12)
    Sepith("Sepith_109B", 7,   7,   14,  7,   9,   12,  12)

    MonsterBattlePostion("MonsterBattlePostion_294", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_300", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_304", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_308", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_30C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_274", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_278", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_27C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_280", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 10, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 0, 0, 180)

    # monster count: 5

    BattleInfo(
        "BattleInfo_334", 0x0000, 43, 6, 60, 4, 1, 30, 0, "bm3040", "Sepith_107B", 60, 25, 10, 5,
        (
            ("ms60700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_294", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms60700.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_274", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms60700.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_294", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms60700.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_274", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
        )
    )

    BattleInfo(
        "BattleInfo_3FC", 0x0000, 43, 6, 60, 4, 1, 30, 0, "bm3040", "Sepith_10A3", 60, 25, 10, 5,
        (
            ("ms75300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_294", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms75300.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_274", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms75300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_294", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms75300.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_274", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
        )
    )

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 43, 6, 60, 4, 1, 60, 0, "bm3030", "Sepith_109B", 60, 25, 10, 5,
        (
            ("ms72500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_294", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms72500.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_274", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms72500.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_294", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
            ("ms72500.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_274", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_654", 0x0010, 43, 6, 60, 0, 1, 0, 0, "bm3040", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74200.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, "ms77300.dat", 0, "MonsterBattlePostion_314", "MonsterBattlePostion_2F4", "ed7402", "ed7403", "ATBonus_234"),
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
        "monster/ch60750.itc",               # 10
        "monster/ch60750.itc",               # 11
        "monster/ch75350.itc",               # 12
        "monster/ch75350.itc",               # 13
        "monster/ch72550.itc",               # 14
        "monster/ch72551.itc",               # 15
        "monster/ch61550.itc",               # 16
        "monster/ch61550.itc",               # 17
        "monster/ch74250.itc",               # 18
        "monster/ch74250.itc",               # 19
    ))

    DeclNpc(-145000, 2000,    26500,   0,    484,  0x0, 0,   24,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-6170,   30610,   0,       0x1010000,    "BattleInfo_334", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-24520,  36630,   0,       0x1010000,    "BattleInfo_3FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-170240, 31380,   -2500,   0x1010000,    "BattleInfo_334", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-171140, 43790,   0,       0x1010000,    "BattleInfo_3FC", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-343090, 235290,  0,       0x1010000,    "BattleInfo_4C4", 0,   20,  0xFFFF, 4,  5)

    DeclActor(-1500,   0,       35250,   1200,    -1500,   1000,    35250,   0x007C, 0,  3,  0x0000)
    DeclActor(-145000, 0,       26500,   1200,    -145000, 1000,    26500,   0x007C, 0,  4,  0x0000)
    DeclActor(-176000, -2500,   32750,   1200,    -176000, -1500,   32750,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 6
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 7

    ScpFunction((
        "Function_0_710",          # 00, 0
        "Function_1_728",          # 01, 1
        "Function_2_729",          # 02, 2
        "Function_3_B8D",          # 03, 3
        "Function_4_CC3",          # 04, 4
        "Function_5_EBD",          # 05, 5
    ))


    def Function_0_710(): pass

    label("Function_0_710")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_727")
    OP_A1(0xFE, 0x3E8, 0x1, 0x0)
    Jump("Function_0_710")

    label("loc_727")

    Return()

    # Function_0_710 end

    def Function_1_728(): pass

    label("Function_1_728")

    Return()

    # Function_1_728 end

    def Function_2_729(): pass

    label("Function_2_729")

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
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1A")
    OP_70(0x2, 0x0)
    Jump("loc_B1E")

    label("loc_B1A")

    OP_70(0x2, 0x1E)

    label("loc_B1E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B31")
    OP_70(0x3, 0x0)
    Jump("loc_B35")

    label("loc_B31")

    OP_70(0x3, 0x1E)

    label("loc_B35")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B48")
    OP_70(0x4, 0x0)
    Jump("loc_B4C")

    label("loc_B48")

    OP_70(0x4, 0x1E)

    label("loc_B4C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B89")
    Sound(130, 1, 100, 0)
    Jump("loc_B8C")

    label("loc_B89")

    OP_24(0x82)

    label("loc_B8C")

    Return()

    # Function_2_729 end

    def Function_3_B8D(): pass

    label("Function_3_B8D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C7A")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_C0C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x101, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_C75")

    label("loc_C0C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C75")

    Jump("loc_CB7")

    label("loc_C7A")

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

    label("loc_CB7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B8D end

    def Function_4_CC3(): pass

    label("Function_4_CC3")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x101, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E7F")
    Sound(14, 0, 100, 0)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x77, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_DBC")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_D1C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_D1C)

    def lambda_D36():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_D36)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_654", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D9D"),
        (2, "loc_DAC"),
        (1, "loc_DB9"),
        (SWITCH_DEFAULT, "loc_DBC"),
    )


    label("loc_D9D")

    SetScenarioFlags(0x77, 3)
    OP_70(0x3, 0x1E)
    Sleep(500)
    Jump("loc_DBC")

    label("loc_DAC")

    OP_70(0x3, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_DB9")

    OP_B7(0x0)
    Return()

    label("loc_DBC")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5ED, 1)"), scpexpr(EXPR_END)), "loc_E13")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5ED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x101, 7)
    OP_DE(0x6, 0x0)
    Jump("loc_E7A")

    label("loc_E13")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5ED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x5ED),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E7A")

    Jump("loc_EB1")

    label("loc_E7F")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_EB1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_CC3 end

    def Function_5_EBD(): pass

    label("Function_5_EBD")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x119, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FAA")
    Sound(14, 0, 100, 0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20B, 1)"), scpexpr(EXPR_END)), "loc_F3C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x119, 6)
    OP_DE(0x6, 0x0)
    Jump("loc_FA5")

    label("loc_F3C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x20B),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_FA5")

    Jump("loc_FE7")

    label("loc_FAA")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0010
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

    label("loc_FE7")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_EBD end

    SaveToFile()

Try(main)
