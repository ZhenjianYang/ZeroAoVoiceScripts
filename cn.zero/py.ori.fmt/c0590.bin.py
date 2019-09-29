from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "c0590.bin",                # FileName
        "c0590",                    # MapName
        "c0590",                    # Location
        0x0029,                     # MapIndex
        "ed7122",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 41, 0, 2, 0, 3],
    )

    BuildStringList((
        "c0590",                  # 0
        "事件用魔兽",             # 1
        "事件用魔兽",             # 2
        "事件用魔兽",             # 3
        "MapThread",              # 4
        "bc0520",                 # 5
        "bc0520",                 # 6
        "bc0520",                 # 7
        "bc0520",                 # 8
        "bc0520",                 # 9
    ))

    ATBonus("ATBonus_2E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_1FCC", 9,   9,   9,   9,   19,  0,   0)
    Sepith("Sepith_1FE4", 0,   0,   0,   0,   15,  20,  20)
    Sepith("Sepith_1FD4", 9,   9,   9,   9,   0,   19,  0)
    Sepith("Sepith_1FDC", 9,   9,   9,   9,   0,   0,   19)

    MonsterBattlePostion("MonsterBattlePostion_340", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 2, 13, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_3C0", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1FCC", 50, 30, 15, 5,
        (
            ("ms67600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67600.dat", "ms67600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67600.dat", "ms67900.dat", "ms67600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67600.dat", "ms67600.dat", "ms67900.dat", "ms67600.dat", 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
        )
    )

    BattleInfo(
        "BattleInfo_618", 0x0000, 33, 6, 90, 0, 1, 0, 0, "bc0520", "Sepith_1FE4", 50, 30, 15, 5,
        (
            ("ms67900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67900.dat", "ms67900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_320", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67900.dat", "ms67900.dat", "ms67900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67900.dat", "ms67900.dat", "ms67900.dat", "ms67900.dat", 0, 0, 0, 0, "MonsterBattlePostion_320", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
        )
    )

    BattleInfo(
        "BattleInfo_488", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1FD4", 50, 30, 15, 5,
        (
            ("ms67700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67700.dat", "ms67700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67700.dat", "ms67900.dat", "ms67700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67700.dat", "ms67700.dat", "ms67900.dat", "ms67700.dat", 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
        )
    )

    BattleInfo(
        "BattleInfo_550", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1FDC", 50, 30, 15, 5,
        (
            ("ms67800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67800.dat", "ms67800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67800.dat", "ms67900.dat", "ms67800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
            ("ms67800.dat", "ms67800.dat", "ms67900.dat", "ms67800.dat", 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7400", "ed7403", "ATBonus_2E0"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_6E0", 0x0002, 33, 6, 45, 0, 1, 0, 0, "bc0520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67700.dat", "ms67700.dat", "ms67700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_340", "MonsterBattlePostion_3A0", "ed7401", "ed7403", "ATBonus_2E0"),
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
        "monster/ch67650.itc",               # 10
        "monster/ch67650.itc",               # 11
        "monster/ch67750.itc",               # 12
        "monster/ch67750.itc",               # 13
        "monster/ch67850.itc",               # 14
        "monster/ch67850.itc",               # 15
        "monster/ch67950.itc",               # 16
        "monster/ch67950.itc",               # 17
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(9930,    57840,   30,      0x1010000,    "BattleInfo_3C0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(21500,   64000,   0,       0x1010000,    "BattleInfo_618", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(57820,   35800,   30,      0x1010000,    "BattleInfo_488", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(61580,   27680,   20,      0x1010000,    "BattleInfo_550", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(58500,   18000,   0,       0x1010000,    "BattleInfo_618", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(24500,   -32000,  0,       0x1010000,    "BattleInfo_618", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-58180,  -2300,   30,      0x1010000,    "BattleInfo_3C0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-56250,  22540,   0,       0x1010000,    "BattleInfo_488", 0,   18,  0xFFFF, 2,  3)

    DeclActor(34000,   500,     -33000,  1200,    34000,   1500,    -33000,  0x007C, 0,  5,  0x0000)
    DeclActor(60000,   0,       54000,   1200,    60000,   1000,    54000,   0x007C, 0,  6,  0x0000)
    DeclActor(34320,   500,     -3780,   1200,    34320,   1500,    -3780,   0x007C, 0,  7,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_7B8",          # 00, 0
        "Function_1_7D4",          # 01, 1
        "Function_2_7FF",          # 02, 2
        "Function_3_811",          # 03, 3
        "Function_4_CE3",          # 04, 4
        "Function_5_DCE",          # 05, 5
        "Function_6_F04",          # 06, 6
        "Function_7_103A",         # 07, 7
        "Function_8_121E",         # 08, 8
        "Function_9_17E6",         # 09, 9
        "Function_10_1834",        # 0A, 10
        "Function_11_1882",        # 0B, 11
        "Function_12_18D0",        # 0C, 12
    ))


    def Function_0_7B8(): pass

    label("Function_0_7B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7D3")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_7B8")

    label("loc_7D3")

    Return()

    # Function_0_7B8 end

    def Function_1_7D4(): pass

    label("Function_1_7D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7FE")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7F6")
    Sound(154, 0, 100, 0)
    Sleep(900)
    Jump("loc_7F9")

    label("loc_7F6")

    Sleep(30)

    label("loc_7F9")

    Jump("Function_1_7D4")

    label("loc_7FE")

    Return()

    # Function_1_7D4 end

    def Function_2_7FF(): pass

    label("Function_2_7FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC4, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC5, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_810")
    Event(0, 8)

    label("loc_810")

    Return()

    # Function_2_7FF end

    def Function_3_811(): pass

    label("Function_3_811")

    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0xB, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 3)), scpexpr(EXPR_END)), "loc_888")
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari20_add", 0x0, 0x1)
    Jump("loc_92D")

    label("loc_888")

    OP_C1(0x0, 0x1, 0x3, 0x1F4, 0x0, 0x2, 24000, -500, -2000, 32000, 1000, -26000)
    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari20_add", 0x1, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_92D")
    SetScenarioFlags(0x0, 0)

    label("loc_92D")

    LoadEffect(0xC, "eff\\\\trapdmg0.eff")
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CC4")
    OP_70(0x0, 0x0)
    Jump("loc_CC8")

    label("loc_CC4")

    OP_70(0x0, 0x1E)

    label("loc_CC8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CDB")
    OP_70(0x1, 0x0)
    Jump("loc_CDF")

    label("loc_CDB")

    OP_70(0x1, 0x1E)

    label("loc_CDF")

    Call(0, 4)
    Return()

    # Function_3_811 end

    def Function_4_CE3(): pass

    label("Function_4_CE3")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D1C")
    SetChrFlags(0x11, 0x8)
    SetMapObjFlags(0x0, 0x4)
    Jump("loc_D27")

    label("loc_D1C")

    ClearChrFlags(0x11, 0x8)
    ClearMapObjFlags(0x0, 0x4)

    label("loc_D27")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D4D")
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xD, 0x8)
    Jump("loc_D57")

    label("loc_D4D")

    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xD, 0x8)

    label("loc_D57")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D88")
    SetChrFlags(0xE, 0x8)
    SetChrFlags(0xF, 0x8)
    SetChrFlags(0x10, 0x8)
    SetMapObjFlags(0x1, 0x4)
    Jump("loc_D9D")

    label("loc_D88")

    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xF, 0x8)
    ClearChrFlags(0x10, 0x8)
    ClearMapObjFlags(0x1, 0x4)

    label("loc_D9D")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DC3")
    SetChrFlags(0x12, 0x8)
    SetChrFlags(0x13, 0x8)
    Jump("loc_DCD")

    label("loc_DC3")

    ClearChrFlags(0x12, 0x8)
    ClearChrFlags(0x13, 0x8)

    label("loc_DCD")

    Return()

    # Function_4_CE3 end

    def Function_5_DCE(): pass

    label("Function_5_DCE")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EBB")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x395, 1)"), scpexpr(EXPR_END)), "loc_E4D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x112, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_EB6")

    label("loc_E4D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x395),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EB6")

    Jump("loc_EF8")

    label("loc_EBB")

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

    label("loc_EF8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_DCE end

    def Function_6_F04(): pass

    label("Function_6_F04")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FF1")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_F83")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x112, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_FEC")

    label("loc_F83")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_FEC")

    Jump("loc_102E")

    label("loc_FF1")

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

    label("loc_102E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_F04 end

    def Function_7_103A(): pass

    label("Function_7_103A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 3)), scpexpr(EXPR_END)), "loc_1077")
    TalkBegin(0xFF)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "开关已经被关闭了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_121D")

    label("loc_1077")

    EventBegin(0x1)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有一个开关。\x01",
            "要操作吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1216")
    Fade(500)
    SetChrPos(0x0, 34000, 500, -4350, 0)
    SetChrPos(0x1, 34500, 500, -5700, 0)
    SetChrPos(0x2, 33500, 500, -5700, 0)
    SetChrPos(0x3, 34000, 500, -6850, 0)
    OP_68(33420, 1000, -4340, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(28430, 500, -12090, 0)
    MoveCamera(45, 22, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(28000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    ClearScenarioFlags(0x0, 0)
    Sound(161, 0, 100, 0)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari20_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    OP_C1(0x0, 0x1, 0x0, 0x5, 0x0, 0x2, 24000, 0, -2000, 32000, 1000, -26000)
    SetScenarioFlags(0xD4, 3)

    label("loc_1216")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_121D")

    Return()

    # Function_7_103A end

    def Function_8_121E(): pass

    label("Function_8_121E")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    SoundLoad(865)
    OP_68(28000, 1000, -15500, 0)
    MoveCamera(48, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    SetChrPos(0x101, 3600, 30, 900, 90)
    SetChrPos(0x102, 2100, 30, 1400, 90)
    SetChrPos(0x103, 2200, 30, 300, 90)
    SetChrPos(0x104, 2000, 30, 2500, 90)
    SetChrPos(0x10A, 3500, 30, 2100, 90)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    SetChrChipByIndex(0x8, 0x12)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x8, 22000, 0, 7500, 180)
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x9, 0x12)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x9, 22000, 0, 7500, 180)
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0xA, 0x12)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    OP_A7(0xA, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0xA, 22000, 0, 7500, 180)
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x6A4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_68(28000, 1000, -5500, 5000)
    FadeToBright(2000, 0)
    OP_6F(0x1)
    Fade(1000)
    OP_68(9600, 1000, 1400, 0)
    MoveCamera(48, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(22500, 0)
    OP_68(4600, 1000, 1400, 3000)
    SetCameraDistance(21500, 3000)
    OP_6F(0x11)

    #C0009
    ChrTalk(
        0x101,
        (
            "#0008F#5P这里……好像是由旧建筑\x01",
            "翻修改建而来的啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0010
    ChrTalk(
        0x10A,
        (
            "#0603F#5P根据一科的推测，\x01",
            "这里应该是那些家伙们的\x01",
            "武器库。\x02\x03",

            "#0601F当然啦，我也是头一次\x01",
            "实际进入此区域……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0011
    ChrTalk(
        0x103,
        "#6P#0205F……这种机械运转的声音……\x02",
    )

    CloseMessageWindow()
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0012
    ChrTalk(
        0x103,
        (
            "#6P#0207F有东西过来了……！\x01",
            "大家小心！\x02",
        )
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#0013F#5P什么……！？\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sound(865, 2, 100, 0)
    Fade(250)
    OP_68(21000, 1000, 1400, 0)
    MoveCamera(48, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21000, 0)
    ClearChrFlags(0x8, 0x80)
    ClearChrBattleFlags(0x8, 0x8000)
    ClearChrFlags(0x9, 0x80)
    ClearChrBattleFlags(0x9, 0x8000)
    ClearChrFlags(0xA, 0x80)
    ClearChrBattleFlags(0xA, 0x8000)
    BeginChrThread(0x8, 0, 0, 0)
    BeginChrThread(0x8, 3, 0, 9)
    Sleep(300)
    BeginChrThread(0x9, 0, 0, 0)
    BeginChrThread(0x9, 3, 0, 10)
    Sleep(300)
    BeginChrThread(0xA, 0, 0, 0)
    BeginChrThread(0xA, 3, 0, 11)
    OP_68(5600, 1000, 1400, 3000)
    SetCameraDistance(20500, 3000)
    Sleep(2500)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(200)
    OP_24(0x361)
    Sleep(800)
    WaitChrThread(0x8, 3)
    WaitChrThread(0x9, 3)
    WaitChrThread(0xA, 3)
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0x1F)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0x20)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0x21)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()

    #C0014
    ChrTalk(
        0x101,
        "#0011F#6P这、这是什么……！？\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x104,
        "#0301F#6P甲壳类魔兽吗，不对……\x02",
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x102,
        (
            "#6P#0105F好、好像是用机械\x01",
            "制造的呢……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x10A,
        "#0607F#6P稍后再研究这些──它们过来了！\x02",
    )

    CloseMessageWindow()
    BlurSwitch(0x12C, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    SetCameraDistance(20000, 300)
    Sound(865, 2, 100, 0)

    def lambda_176A():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_176A)

    def lambda_1784():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_1784)

    def lambda_179E():
        OP_98(0xFE, 0xFFFFF448, 0x0, 0x0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_179E)
    Sleep(300)
    OP_24(0x361)
    Battle("BattleInfo_6E0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x8, 0x1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    OP_24(0x361)
    Call(0, 12)
    Return()

    # Function_8_121E end

    def Function_9_17E6(): pass

    label("Function_9_17E6")


    def lambda_17EB():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_17EB)

    def lambda_17FC():
        OP_95(0xFE, 22000, 0, 1900, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_17FC)
    WaitChrThread(0xFE, 1)

    def lambda_181A():
        OP_95(0xFE, 7500, 0, 1400, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_181A)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_9_17E6 end

    def Function_10_1834(): pass

    label("Function_10_1834")


    def lambda_1839():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1839)

    def lambda_184A():
        OP_95(0xFE, 22000, 0, 1900, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_184A)
    WaitChrThread(0xFE, 1)

    def lambda_1868():
        OP_95(0xFE, 9100, 30, 2900, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1868)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_10_1834 end

    def Function_11_1882(): pass

    label("Function_11_1882")


    def lambda_1887():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x12C)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_1887)

    def lambda_1898():
        OP_95(0xFE, 22000, 0, 1900, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_1898)
    WaitChrThread(0xFE, 1)

    def lambda_18B6():
        OP_95(0xFE, 10700, 0, 1400, 6000, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_18B6)
    WaitChrThread(0xFE, 1)
    Return()

    # Function_11_1882 end

    def Function_12_18D0(): pass

    label("Function_12_18D0")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch00150.itc", 0x1F)
    LoadChrToIndex("chr/ch00250.itc", 0x20)
    LoadChrToIndex("chr/ch00350.itc", 0x21)
    LoadChrToIndex("chr/ch00950.itc", 0x22)
    OP_68(5290, 1000, 1520, 0)
    MoveCamera(48, 20, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 3600, 30, 900, 90)
    SetChrPos(0x102, 2100, 30, 1400, 90)
    SetChrPos(0x103, 2200, 30, 300, 90)
    SetChrPos(0x104, 2000, 30, 2500, 90)
    SetChrPos(0x10A, 3500, 30, 2100, 90)
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
    SetChrChipByIndex(0x10A, 0x22)
    SetChrSubChip(0x10A, 0x0)
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    OP_68(4290, 1000, 1520, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1)
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x102, 0xFF)
    SetChrSubChip(0x102, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    SetChrChipByIndex(0x10A, 0xFF)
    SetChrSubChip(0x10A, 0x0)
    Sound(808, 0, 100, 0)
    Sound(531, 0, 100, 0)
    OP_0D()
    Sleep(300)

    #C0018
    ChrTalk(
        0x102,
        (
            "#6P#0106F果、果然是用机械\x01",
            "制造的啊……\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 500)

    #C0019
    ChrTalk(
        0x104,
        (
            "#0303F#5P而且相当棘手啊……\x02\x03",

            "#0301F这些家伙，到底是什么东西啊？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1AA6():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_1AA6)
    Sleep(50)

    def lambda_1AB6():
        TurnDirection(0xFE, 0x102, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1AB6)
    Sleep(100)
    TurnDirection(0x10A, 0x103, 500)
    Sleep(100)

    #C0020
    ChrTalk(
        0x103,
        (
            "#6P#0203F自律式人偶兵器……\x02\x03",

            "虽然财团也在对它进行研究，\x01",
            "但还没有实用化。\x02\x03",

            "#0201F据传闻说，『结社』的那些家伙\x01",
            "好像已经把这种东西投入使用了……\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x101,
        (
            "#11P#0006F结社……就是艾丝蒂尔他们所说的\x01",
            "那个神秘犯罪组织吗……\x02\x03",

            "#0001F可是……\x01",
            "他们的兵器为什么会在这种地方出现呢？\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x10A,
        (
            "#5P#0604F呵，没想到你们\x01",
            "竟然知道『结社』的存在啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x102, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x103, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(30)
    OP_63(0x104, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    def lambda_1C6B():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1C6B)
    Sleep(50)

    def lambda_1C7B():
        TurnDirection(0xFE, 0x10A, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_1C7B)
    Sleep(50)
    TurnDirection(0x102, 0x10A, 500)

    #C0023
    ChrTalk(
        0x101,
        (
            "#12P#0005F这么说来，达德利警官\x01",
            "也知道吗？\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x10A,
        (
            "#5P#0600F当然。\x01",
            "关于利贝尔发生的异变，\x01",
            "是由一科独家收集情报的。\x02\x03",

            "#0603F而且，据说在半年前左右……\x01",
            "『结社』制造的那些兵器\x01",
            "已经流向黑市了。\x02\x03",

            "#0601F虽然无法辨别真伪……\x01",
            "但真是没想到，竟然被鲁巴彻搞到手了啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        "#12P#0001F还有这种事吗……\x02",
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x102,
        (
            "#6P#0101F难道马尔克尼会长是因为\x01",
            "个人兴趣才把这些东西弄到手的吗……？\x02",
        )
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x10A,
        (
            "#5P#0606F嗯，这些破铜烂铁想必\x01",
            "很符合他的口味吧。\x02\x03",

            "#0601F不过，说到战斗力的话，\x01",
            "倒是不容小觑的……\x02",
        )
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0x103,
        (
            "#6P#0201F而且，看起来……\x01",
            "那种东西应该还有不少。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x104,
        (
            "#0306F#6P哎呀呀……也就是说，我们\x01",
            "前进的道路似乎没有那么平坦呢。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_49()
    OP_D5(0x1E)
    OP_D5(0x1F)
    OP_D5(0x20)
    OP_D5(0x21)
    OP_D5(0x22)
    OP_37()
    OP_68(3000, 530, 1400, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(23000, 0)
    SetChrPos(0x0, 3000, 30, 1400, 90)
    SetChrPos(0x1, 3000, 30, 1400, 90)
    SetChrPos(0x2, 3000, 30, 1400, 90)
    SetChrPos(0x3, 3000, 30, 1400, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetScenarioFlags(0xC5, 5)
    OP_29(0x4C, 0x1, 0x15)
    OP_E0(0x0)
    EventEnd(0x5)
    Return()

    # Function_12_18D0 end

    SaveToFile()

Try(main)
