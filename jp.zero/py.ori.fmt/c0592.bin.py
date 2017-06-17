from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "c0592.bin",                # FileName
        "c0592",                    # MapName
        "c0592",                    # Location
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
        "c0592",                  # 0
        "トライアタッカーＲ",     # 1
        "MapThread",              # 2
        "bc0520",                 # 3
        "bc0520",                 # 4
        "bc0520",                 # 5
        "bc0520",                 # 6
        "bc0520",                 # 7
    ))

    ATBonus("ATBonus_2B0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_170E", 9,   9,   9,   9,   0,   19,  0)
    Sepith("Sepith_1706", 9,   9,   9,   9,   19,  0,   0)
    Sepith("Sepith_171E", 0,   0,   0,   0,   15,  20,  20)
    Sepith("Sepith_1716", 9,   9,   9,   9,   0,   0,   19)

    MonsterBattlePostion("MonsterBattlePostion_310", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_370", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_374", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_378", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_37C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_380", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_384", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_388", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_38C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_390", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_394", 12, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_398", 4, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_39C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 0, 0, 180)

    # monster count: 6

    BattleInfo(
        "BattleInfo_478", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_170E", 40, 30, 20, 10,
        (
            ("ms67700.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67700.dat", "ms67700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67700.dat", "ms67900.dat", "ms67700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67700.dat", "ms67700.dat", "ms67900.dat", "ms67700.dat", 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
        )
    )

    BattleInfo(
        "BattleInfo_3B0", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1706", 40, 30, 20, 10,
        (
            ("ms67600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67600.dat", "ms67600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67600.dat", "ms67900.dat", "ms67600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67600.dat", "ms67600.dat", "ms67900.dat", "ms67600.dat", 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
        )
    )

    BattleInfo(
        "BattleInfo_608", 0x0000, 33, 6, 90, 0, 1, 0, 0, "bc0520", "Sepith_171E", 40, 30, 20, 10,
        (
            ("ms67900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67900.dat", "ms67900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2F0", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67900.dat", "ms67900.dat", "ms67900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67900.dat", "ms67900.dat", "ms67900.dat", "ms67900.dat", 0, 0, 0, 0, "MonsterBattlePostion_2F0", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
        )
    )

    BattleInfo(
        "BattleInfo_540", 0x0000, 33, 6, 45, 4, 1, 30, 0, "bc0520", "Sepith_1716", 40, 30, 20, 10,
        (
            ("ms67800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67800.dat", "ms67800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67800.dat", "ms67900.dat", "ms67800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
            ("ms67800.dat", "ms67800.dat", "ms67900.dat", "ms67800.dat", 0, 0, 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_370", "ed7400", "ed7403", "ATBonus_2B0"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_6D0", 0x0000, 33, 6, 45, 0, 1, 0, 0, "bc0520", 0x00000000, 100, 0, 0, 0,
        (
            ("ms67600.dat", "ms67700.dat", "ms67800.dat", "ms67900.dat", 0, 0, 0, 0, "MonsterBattlePostion_390", "MonsterBattlePostion_370", "ed7401", "ed7403", "ATBonus_2B0"),
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

    DeclNpc(28000,   500,     -5500,   0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    456,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(9870,    -56200,  30,      0x1010000,    "BattleInfo_478", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-9000,   -73080,  20,      0x1010000,    "BattleInfo_3B0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(13500,   -64000,  0,       0x1010000,    "BattleInfo_608", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(11640,   1610,    500,     0x1010000,    "BattleInfo_540", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-12000,  -50500,  0,       0x1010000,    "BattleInfo_608", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(-51830,  -23680,  0,       0x1010000,    "BattleInfo_478", 0,   18,  0xFFFF, 2,  3)

    DeclActor(28000,   0,       -2500,   1200,    28000,   1000,    -2500,   0x007C, 0,  5,  0x0000)
    DeclActor(28000,   0,       -5500,   1200,    28000,   1000,    -5500,   0x007C, 0,  6,  0x0000)
    DeclActor(-28000,  0,       -30000,  1200,    -28000,  1000,    -30000,  0x007C, 0,  7,  0x0000)
    DeclActor(8000,    0,       3000,    1200,    8000,    1000,    3000,    0x007C, 0,  8,  0x0000)
    DeclActor(-24000,  0,       -29000,  1200,    -24000,  1000,    -29000,  0x007C, 0,  9,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 6
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 7

    ScpFunction((
        "Function_0_79C",          # 00, 0
        "Function_1_7B8",          # 01, 1
        "Function_2_7E3",          # 02, 2
        "Function_3_7E4",          # 03, 3
        "Function_4_D30",          # 04, 4
        "Function_5_E09",          # 05, 5
        "Function_6_F56",          # 06, 6
        "Function_7_1169",         # 07, 7
        "Function_8_12B6",         # 08, 8
        "Function_9_14B6",         # 09, 9
    ))


    def Function_0_79C(): pass

    label("Function_0_79C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7B7")
    OP_A1(0xFE, 0x7D0, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_79C")

    label("loc_7B7")

    Return()

    # Function_0_79C end

    def Function_1_7B8(): pass

    label("Function_1_7B8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_7DA")
    Sound(154, 0, 100, 0)
    Sleep(900)
    Jump("loc_7DD")

    label("loc_7DA")

    Sleep(30)

    label("loc_7DD")

    Jump("Function_1_7B8")

    label("loc_7E2")

    Return()

    # Function_1_7B8 end

    def Function_2_7E3(): pass

    label("Function_2_7E3")

    Return()

    # Function_2_7E3 end

    def Function_3_7E4(): pass

    label("Function_3_7E4")

    ClearScenarioFlags(0x0, 0)
    BeginChrThread(0x9, 0, 0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 6)), scpexpr(EXPR_END)), "loc_85B")
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari20_add", 0x0, 0x1)
    Jump("loc_900")

    label("loc_85B")

    OP_C1(0x0, 0x1, 0x3, 0x1F4, 0x0, 0x2, 10000, -500, 0, 30000, 1000, -8000)
    SetMapObjFrame(0xFF, "lgt1_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari00_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari01_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari02_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari20_add", 0x1, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_900")
    SetScenarioFlags(0x0, 0)

    label("loc_900")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 7)), scpexpr(EXPR_END)), "loc_96E")
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari21_add", 0x0, 0x1)
    Jump("loc_A13")

    label("loc_96E")

    OP_C1(0x1, 0x1, 0x3, 0x1F4, 0x0, 0x2, -38000, -500, -28000, -26000, 1000, -32000)
    SetMapObjFrame(0xFF, "lgt2_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari10_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hikari21_add", 0x1, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_A13")
    SetScenarioFlags(0x0, 0)

    label("loc_A13")

    LoadEffect(0xC, "eff\\\\trapdmg0.eff")
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xB3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CFA")
    OP_70(0x0, 0x0)
    Jump("loc_CFE")

    label("loc_CFA")

    OP_70(0x0, 0x1E)

    label("loc_CFE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D11")
    OP_70(0x1, 0x0)
    Jump("loc_D15")

    label("loc_D11")

    OP_70(0x1, 0x1E)

    label("loc_D15")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D28")
    OP_70(0x2, 0x0)
    Jump("loc_D2C")

    label("loc_D28")

    OP_70(0x2, 0x1E)

    label("loc_D2C")

    Call(0, 4)
    Return()

    # Function_3_7E4 end

    def Function_4_D30(): pass

    label("Function_4_D30")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D66")
    SetChrFlags(0xD, 0x8)
    SetMapObjFlags(0x0, 0x4)
    SetMapObjFlags(0x1, 0x4)
    Jump("loc_D77")

    label("loc_D66")

    ClearChrFlags(0xD, 0x8)
    ClearMapObjFlags(0x0, 0x4)
    ClearMapObjFlags(0x1, 0x4)

    label("loc_D77")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DB9")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    SetChrFlags(0xC, 0x8)
    SetChrFlags(0xE, 0x8)
    Jump("loc_DCD")

    label("loc_DB9")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xE, 0x8)

    label("loc_DCD")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DFD")
    SetChrFlags(0xF, 0x8)
    SetMapObjFlags(0x2, 0x4)
    Jump("loc_E08")

    label("loc_DFD")

    ClearChrFlags(0xF, 0x8)
    ClearMapObjFlags(0x2, 0x4)

    label("loc_E08")

    Return()

    # Function_4_D30 end

    def Function_5_E09(): pass

    label("Function_5_E09")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F05")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x55, 1)"), scpexpr(EXPR_END)), "loc_E8E")
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
    SetScenarioFlags(0x112, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_F00")

    label("loc_E8E")

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
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_F00")

    Jump("loc_F4A")

    label("loc_F05")

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

    label("loc_F4A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_E09 end

    def Function_6_F56(): pass

    label("Function_6_F56")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1123")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x76, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1051")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_FAF():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_FAF)

    def lambda_FC9():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_FC9)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

    #A0004
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
    Battle("BattleInfo_6D0", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1032"),
        (2, "loc_1041"),
        (1, "loc_104E"),
        (SWITCH_DEFAULT, "loc_1051"),
    )


    label("loc_1032")

    SetScenarioFlags(0x76, 0)
    OP_70(0x1, 0x1E)
    Sleep(500)
    Jump("loc_1051")

    label("loc_1041")

    OP_70(0x1, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_104E")

    OP_B7(0x0)
    Return()

    label("loc_1051")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5EC, 1)"), scpexpr(EXPR_END)), "loc_10AE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5EC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x112, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_111E")

    label("loc_10AE")

    FadeToDark(300, 0, 100)

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5EC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5EC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_111E")

    Jump("loc_115D")

    label("loc_1123")

    FadeToDark(300, 0, 100)

    #A0007
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

    label("loc_115D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_F56 end

    def Function_7_1169(): pass

    label("Function_7_1169")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x112, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1265")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x650, 1)"), scpexpr(EXPR_END)), "loc_11EE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x650),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x112, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_1260")

    label("loc_11EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x650),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x650),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1260")

    Jump("loc_12AA")

    label("loc_1265")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_12AA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1169 end

    def Function_8_12B6(): pass

    label("Function_8_12B6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 6)), scpexpr(EXPR_END)), "loc_12FF")
    TalkBegin(0xFF)
    SetChrName("")

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは切られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_14B5")

    label("loc_12FF")

    EventBegin(0x1)

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14AE")
    Fade(500)
    SetChrPos(0x0, 7710, 500, 1950, 0)
    SetChrPos(0x1, 10000, 500, 2680, 270)
    SetChrPos(0x2, 10000, 500, 1260, 270)
    SetChrPos(0x3, 11180, 500, 2440, 270)
    OP_68(7280, 1000, 1930, 0)
    MoveCamera(45, 41, 0, 0)
    OP_6E(440, 0)
    SetCameraDistance(21500, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt1_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(16460, 500, -4830, 0)
    MoveCamera(45, 33, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(23000, 0)
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
    OP_C1(0x0, 0x1, 0x0, 0x5, 0x0, 0x2, 10000, 0, 0, 30000, 1000, -8000)
    SetScenarioFlags(0xD4, 6)

    label("loc_14AE")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_14B5")

    Return()

    # Function_8_12B6 end

    def Function_9_14B6(): pass

    label("Function_9_14B6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xD4, 7)), scpexpr(EXPR_END)), "loc_14FF")
    TalkBegin(0xFF)
    SetChrName("")

    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは切られている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_16B5")

    label("loc_14FF")

    EventBegin(0x1)

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "スイッチがある。\x01",
            "操作しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16AE")
    Fade(500)
    SetChrPos(0x0, -24260, 500, -30000, 0)
    SetChrPos(0x1, -23900, 500, -31000, 0)
    SetChrPos(0x2, -24750, 500, -31000, 0)
    SetChrPos(0x3, -24530, 500, -31910, 0)
    OP_68(-24490, 990, -30060, 0)
    MoveCamera(45, 41, 0, 0)
    OP_6E(400, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    Sound(140, 0, 100, 0)
    SetMapObjFrame(0xFF, "lgt2_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    Fade(500)
    OP_68(-32119, 500, -30700, 0)
    MoveCamera(45, 27, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(23000, 0)
    OP_0D()
    Sleep(500)
    Fade(500)
    ClearScenarioFlags(0x0, 0)
    Sound(161, 0, 100, 0)
    SetMapObjFrame(0xFF, "hikari10_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari11_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari12_add", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hikari21_add", 0x0, 0x1)
    OP_0D()
    Sleep(1000)
    OP_C1(0x1, 0x1, 0x0, 0x5, 0x0, 0x2, -38000, 0, -28000, -28000, 1000, -32000)
    SetScenarioFlags(0xD4, 7)

    label("loc_16AE")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_16B5")

    Return()

    # Function_9_14B6 end

    SaveToFile()

Try(main)
