from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m2030.bin",                # FileName
        "M2030",                    # MapName
        "M2030",                    # Location
        0x0075,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 117, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2030",                  # 0
        "bm2000",                 # 1
        "bm2000",                 # 2
    ))

    ATBonus("ATBonus_250", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_F8C", 11,  10,  0,   7,   12,  0,   11)
    Sepith("Sepith_F84", 16,  12,  3,   9,   5,   0,   5)

    MonsterBattlePostion("MonsterBattlePostion_280", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_284", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_288", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_304", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_308", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_30C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_310", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_314", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_318", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 8, 14, 180)

    # monster count: 7

    BattleInfo(
        "BattleInfo_3E8", 0x0000, 30, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_F8C", 40, 30, 20, 10,
        (
            ("ms74400.dat", "ms74400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_280", "MonsterBattlePostion_300", "ed7400", "ed7403", "ATBonus_250"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2A0", "MonsterBattlePostion_300", "ed7400", "ed7403", "ATBonus_250"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, 0, "MonsterBattlePostion_280", "MonsterBattlePostion_300", "ed7400", "ed7403", "ATBonus_250"),
            ("ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", "ms74400.dat", 0, 0, 0, "MonsterBattlePostion_2A0", "MonsterBattlePostion_300", "ed7400", "ed7403", "ATBonus_250"),
        )
    )

    BattleInfo(
        "BattleInfo_320", 0x0000, 30, 6, 45, 4, 1, 30, 0, "bm2000", "Sepith_F84", 40, 30, 20, 10,
        (
            ("ms74300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2A0", "MonsterBattlePostion_300", "ed7400", "ed7403", "ATBonus_250"),
            ("ms74300.dat", "ms74300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_280", "MonsterBattlePostion_300", "ed7400", "ed7403", "ATBonus_250"),
            ("ms74300.dat", "ms74300.dat", "ms74300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2A0", "MonsterBattlePostion_300", "ed7400", "ed7403", "ATBonus_250"),
            ("ms74300.dat", "ms74300.dat", "ms74300.dat", "ms74300.dat", 0, 0, 0, 0, "MonsterBattlePostion_280", "MonsterBattlePostion_300", "ed7400", "ed7403", "ATBonus_250"),
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
        "monster/ch74350.itc",               # 10
        "monster/ch74350.itc",               # 11
        "monster/ch74450.itc",               # 12
        "monster/ch74450.itc",               # 13
    ))

    DeclMonster(19660,   -630,    -4000,   0x1010000,    "BattleInfo_3E8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(10620,   -7410,   -12000,  0x1010000,    "BattleInfo_320", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-109200, -490,    0,       0x1010000,    "BattleInfo_3E8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-110220, 3280,    0,       0x1010000,    "BattleInfo_3E8", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(170,     -83910,  0,       0x1010000,    "BattleInfo_320", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-100880, 85630,   0,       0x1010000,    "BattleInfo_320", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-200310, -84960,  0,       0x1010000,    "BattleInfo_320", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-100000, 0,       89000,   1200,    -100000, 1000,    89000,   0x007C, 0,  3,  0x0000)
    DeclActor(-200000, 0,       -87000,  1200,    -200000, 1000,    -87000,  0x007C, 0,  4,  0x0000)
    DeclActor(14000,   -12000,  -9500,   1200,    14000,   -11000,  -9500,   0x007C, 0,  5,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 2
    ChipFrameInfo(3000, 0, [0, 1, 2, 3, 4, 5])                   # 3

    ScpFunction((
        "Function_0_4F8",          # 00, 0
        "Function_1_4F9",          # 01, 1
        "Function_2_A64",          # 02, 2
        "Function_3_B4D",          # 03, 3
        "Function_4_C9A",          # 04, 4
        "Function_5_DE7",          # 05, 5
    ))


    def Function_0_4F8(): pass

    label("Function_0_4F8")

    Return()

    # Function_0_4F8 end

    def Function_1_4F9(): pass

    label("Function_1_4F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_50B")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_50B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_51A")
    StopEffect(0x80, 0x0)
    StopEffect(0x81, 0x0)

    label("loc_51A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_57B")
    SetMapObjFrame(0xFF, "object02_smoke", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_particle", 0x0, 0x1)
    SetMapObjFrame(0xFF, "object02_fire", 0x0, 0x1)
    SetMapObjFrame(0xFF, "model04_glow", 0x0, 0x1)

    label("loc_57B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_END)), "loc_5CA")
    SetChrFlags(0x8, 0x80)
    SetChrBattleFlags(0x8, 0x8000)
    SetChrFlags(0x9, 0x80)
    SetChrBattleFlags(0x9, 0x8000)
    SetChrFlags(0xA, 0x80)
    SetChrBattleFlags(0xA, 0x8000)
    SetChrFlags(0xB, 0x80)
    SetChrBattleFlags(0xB, 0x8000)
    SetChrFlags(0xC, 0x80)
    SetChrBattleFlags(0xC, 0x8000)
    SetChrFlags(0xD, 0x80)
    SetChrBattleFlags(0xD, 0x8000)
    SetChrFlags(0xE, 0x80)
    SetChrBattleFlags(0xE, 0x8000)

    label("loc_5CA")

    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xA7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x1D, 0x0, 0x8, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x1, 0x9, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x2, 0xA, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x3, 0xB, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x4, 0xC, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x5, 0xD, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1D, 0x6, 0xE, 0x40, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A1E")
    OP_70(0x7, 0x0)
    Jump("loc_A22")

    label("loc_A1E")

    OP_70(0x7, 0x1E)

    label("loc_A22")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A35")
    OP_70(0x8, 0x0)
    Jump("loc_A39")

    label("loc_A35")

    OP_70(0x8, 0x1E)

    label("loc_A39")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A4C")
    OP_70(0x9, 0x0)
    Jump("loc_A50")

    label("loc_A4C")

    OP_70(0x9, 0x1E)

    label("loc_A50")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A60")
    Sound(129, 1, 100, 0)

    label("loc_A60")

    Call(0, 2)
    Return()

    # Function_1_4F9 end

    def Function_2_A64(): pass

    label("Function_2_A64")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A90")
    SetChrFlags(0x8, 0x8)
    SetChrFlags(0x9, 0x8)
    SetMapObjFlags(0x9, 0x4)
    Jump("loc_AA0")

    label("loc_A90")

    ClearChrFlags(0x8, 0x8)
    ClearChrFlags(0x9, 0x8)
    ClearMapObjFlags(0x9, 0x4)

    label("loc_AA0")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_NEQ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6A), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6B), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_AFC")
    SetChrFlags(0xA, 0x8)
    SetChrFlags(0xB, 0x8)
    Jump("loc_B06")

    label("loc_AFC")

    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xB, 0x8)

    label("loc_B06")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B24")
    SetChrFlags(0xD, 0x8)
    SetMapObjFlags(0x7, 0x4)
    Jump("loc_B2F")

    label("loc_B24")

    ClearChrFlags(0xD, 0x8)
    ClearMapObjFlags(0x7, 0x4)

    label("loc_B2F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x71), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B47")
    SetChrFlags(0xC, 0x8)
    Jump("loc_B4C")

    label("loc_B47")

    ClearChrFlags(0xC, 0x8)

    label("loc_B4C")

    Return()

    # Function_2_A64 end

    def Function_3_B4D(): pass

    label("Function_3_B4D")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C49")
    Sound(14, 0, 100, 0)
    OP_71(0x7, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1A1, 1)"), scpexpr(EXPR_END)), "loc_BD2")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11C, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_C44")

    label("loc_BD2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1A1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1A1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x7, 0x1E, 0x0, 0x0, 0x0)

    label("loc_C44")

    Jump("loc_C8E")

    label("loc_C49")

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

    label("loc_C8E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_B4D end

    def Function_4_C9A(): pass

    label("Function_4_C9A")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D96")
    Sound(14, 0, 100, 0)
    OP_71(0x8, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1AA, 1)"), scpexpr(EXPR_END)), "loc_D1F")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11C, 4)
    OP_DE(0x6, 0x0)
    Jump("loc_D91")

    label("loc_D1F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1AA),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x8, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D91")

    Jump("loc_DDB")

    label("loc_D96")

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

    label("loc_DDB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C9A end

    def Function_5_DE7(): pass

    label("Function_5_DE7")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x11C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EE3")
    Sound(14, 0, 100, 0)
    OP_71(0x9, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1A7, 1)"), scpexpr(EXPR_END)), "loc_E6C")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x11C, 5)
    OP_DE(0x6, 0x0)
    Jump("loc_EDE")

    label("loc_E6C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1A7),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x9, 0x1E, 0x0, 0x0, 0x0)

    label("loc_EDE")

    Jump("loc_F28")

    label("loc_EE3")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0009
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

    label("loc_F28")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_DE7 end

    SaveToFile()

Try(main)
