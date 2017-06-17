from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m2000.bin",                # FileName
        "m2000",                    # MapName
        "m2000",                    # Location
        0x0077,                     # MapIndex
        "ed7303",
        0x00080000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x23,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 119, 0, 0, 0, 1],
    )

    BuildStringList((
        "m2000",                  # 0
        "bm2000",                 # 1
    ))

    ATBonus("ATBonus_258", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_1CAF", 0,   0,   12,  0,   8,   8,   0)

    MonsterBattlePostion("MonsterBattlePostion_2A8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2AC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_30C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_310", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_314", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_318", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_31C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_320", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_288", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_28C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_290", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_294", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_298", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_29C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2A4", 2, 13, 180)

    # monster count: 3

    BattleInfo(
        "BattleInfo_328", 0x0000, 63, 6, 60, 6, 1, 30, 0, "bm2000", "Sepith_1CAF", 40, 30, 20, 10,
        (
            ("ms73400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2A8", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
            ("ms73400.dat", "ms73400.dat", "ms73400.dat", "ms73400.dat", 0, 0, 0, 0, "MonsterBattlePostion_288", "MonsterBattlePostion_308", "ed7450", "ed7453", "ATBonus_258"),
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
        "monster/ch73450.itc",               # 10
        "monster/ch73450.itc",               # 11
    ))

    DeclMonster(112650,  -360,    0,       0x1010000,    "BattleInfo_328", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(111370,  -16710,  0,       0x1010000,    "BattleInfo_328", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(110950,  10260,   0,       0x1010000,    "BattleInfo_328", 0,   16,  0xFFFF, 0,  1)

    DeclActor(113500,  9630,    8130,    1200,    113500,  10630,   8130,    0x007C, 0,  6,  0x0000)
    DeclActor(113500,  9650,    -8160,   1200,    113500,  10650,   -8160,   0x007C, 0,  7,  0x0000)
    DeclActor(34000,   0,       4000,    1200,    34000,   1500,    4000,    0x007C, 0,  2,  0x0000)
    DeclActor(-3500,   0,       0,       1200,    -3500,   1000,    0,       0x007C, 0,  8,  0x0000)
    DeclActor(132500,  0,       16000,   1200,    132500,  1000,    16000,   0x007C, 0,  9,  0x0000)
    DeclActor(130300,  500,     -1900,   1200,    130300,  1500,    -1900,   0x007C, 0,  3,  0x0000)
    DeclActor(130300,  500,     1900,    1200,    130300,  1500,    1900,    0x007C, 0,  4,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 0
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5, 6, 7])             # 1

    ScpFunction((
        "Function_0_43C",          # 00, 0
        "Function_1_498",          # 01, 1
        "Function_2_BF8",          # 02, 2
        "Function_3_CF4",          # 03, 3
        "Function_4_EDB",          # 04, 4
        "Function_5_10C2",         # 05, 5
        "Function_6_1132",         # 06, 6
        "Function_7_1313",         # 07, 7
        "Function_8_14F1",         # 08, 8
        "Function_9_15F5",         # 09, 9
        "Function_10_1621",        # 0A, 10
        "Function_11_1B7B",        # 0B, 11
        "Function_12_1C01",        # 0C, 12
    ))


    def Function_0_43C(): pass

    label("Function_0_43C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_44F")
    Jump("loc_44F")

    label("loc_44F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_46E")
    SetMapFlags(0x10000000)
    Event(0, 10)

    label("loc_46E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_482")
    ClearScenarioFlags(0x22, 0)
    Event(0, 12)
    Jump("loc_491")

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 1)), scpexpr(EXPR_END)), "loc_491")
    ClearScenarioFlags(0x22, 1)
    Event(0, 11)

    label("loc_491")

    SetScenarioFlags(0x150, 4)
    SetScenarioFlags(0x150, 5)
    Return()

    # Function_0_43C end

    def Function_1_498(): pass

    label("Function_1_498")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A4, 5)), scpexpr(EXPR_END)), "loc_4AA")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x130), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4AA")

    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    PlayEffect(0x2F, 0x0, 0x8, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x1, 0x9, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x2F, 0x2, 0xA, 0x41, 0, 0, 0, 0, 0, 0, 1250, 750, 1250, 0xFF, 0, 0, 0, 0)
    SetMapObjFrame(0xFF, "glow02", 0x0, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_7C2")
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    OP_65(0x5, 0x1)
    OP_65(0x6, 0x1)

    label("loc_7C2")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 120500, 9000, 9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 115000, 9000, 9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, 132500, 9000, 5000, 2000, 2000, 90000)
    SetBarrier(0x0, 0x5, 0x1, 0x0, 132500, 9000, -5000, 2000, 2000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 4)), scpexpr(EXPR_END)), "loc_897")
    SetMapObjFrame(0x6, "root", 0x2, "on")
    SetMapObjFrame(0x4, "root", 0x2, "on")
    SetMapObjFrame(0x9, "root", 0x2, "on")
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_892")
    SetMapObjFrame(0x9, "root", 0x2, "off")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)

    label("loc_892")

    Jump("loc_8CB")

    label("loc_897")

    SetMapObjFrame(0x6, "root", 0x2, "off")
    SetMapObjFrame(0x4, "root", 0x2, "off")
    SetMapObjFrame(0x9, "root", 0x2, "off")
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)

    label("loc_8CB")

    SetBarrier(0x0, 0x2, 0x1, 0x0, 120500, 9000, -9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, 115000, 9000, -9800, 3000, 2000, 90000)
    SetBarrier(0x0, 0x6, 0x1, 0x0, 136950, 9000, 2160, 3000, 2000, 150000)
    SetBarrier(0x0, 0x7, 0x1, 0x0, 136950, 9000, -2160, 3000, 2000, 30000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 5)), scpexpr(EXPR_END)), "loc_9A0")
    SetMapObjFrame(0x7, "root", 0x2, "on")
    SetMapObjFrame(0x5, "root", 0x2, "on")
    SetMapObjFrame(0xA, "root", 0x2, "on")
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_99B")
    SetMapObjFrame(0xA, "root", 0x2, "off")
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)

    label("loc_99B")

    Jump("loc_9D4")

    label("loc_9A0")

    SetMapObjFrame(0x7, "root", 0x2, "off")
    SetMapObjFrame(0x5, "root", 0x2, "off")
    SetMapObjFrame(0xA, "root", 0x2, "off")
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x6, 0x1)
    SetBarrier(0x3, 0x7, 0x1)

    label("loc_9D4")

    SetBarrier(0x0, 0x8, 0x1, 0x0, -3000, 0, 0, 6000, 3000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 6)), scpexpr(EXPR_END)), "loc_A18")
    SetMapObjFrame(0xC, "root", 0x2, "on")
    ClearMapObjFlags(0xC, 0x2)
    SetBarrier(0x2, 0x8, 0x1)
    OP_65(0x3, 0x1)
    Jump("loc_A2E")

    label("loc_A18")

    SetMapObjFrame(0xC, "root", 0x2, "off")
    SetMapObjFlags(0xC, 0x2)
    SetBarrier(0x3, 0x8, 0x1)

    label("loc_A2E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_A47")
    ClearMapObjFlags(0x1, 0x10)
    Jump("loc_A4B")

    label("loc_A47")

    OP_65(0x4, 0x1)

    label("loc_A4B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_BF1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 0)), scpexpr(EXPR_END)), "loc_A7B")
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0x10, "b_bace", 0x0, 0x1)
    Jump("loc_ACC")

    label("loc_A7B")

    SetMapObjFrame(0x10, "b_bace", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_in", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_in2", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_out", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_out2", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_light", 0x0, 0x1)

    label("loc_ACC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 1)), scpexpr(EXPR_END)), "loc_AEE")
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "b_bace", 0x0, 0x1)
    Jump("loc_B3F")

    label("loc_AEE")

    SetMapObjFrame(0x11, "b_bace", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_in", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_in2", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_out", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_out2", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_light", 0x0, 0x1)

    label("loc_B3F")

    SetBarrier(0x0, 0x9, 0x1, 0x0, 138100, 9000, 0, 8000, 3000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_B73")
    SetMapObjFlags(0xF, 0x4)
    SetBarrier(0x2, 0x9, 0x1)

    label("loc_B73")

    SetBarrier(0x0, 0xA, 0x1, 0x0, 131000, 0, -15500, 6000, 3000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 2)), scpexpr(EXPR_END)), "loc_BA8")
    SetMapObjFlags(0xD, 0x4)
    SetBarrier(0x2, 0xA, 0x1)
    Jump("loc_BB2")

    label("loc_BA8")

    ClearMapObjFlags(0xD, 0x4)
    SetBarrier(0x3, 0xA, 0x1)

    label("loc_BB2")

    SetBarrier(0x0, 0xB, 0x1, 0x0, 131000, 0, 15500, 6000, 3000, 90000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 3)), scpexpr(EXPR_END)), "loc_BE7")
    SetMapObjFlags(0xE, 0x4)
    SetBarrier(0x2, 0xB, 0x1)
    Jump("loc_BF1")

    label("loc_BE7")

    ClearMapObjFlags(0xE, 0x4)
    SetBarrier(0x3, 0xB, 0x1)

    label("loc_BF1")

    Sound(129, 1, 100, 0)
    Return()

    # Function_1_498 end

    def Function_2_BF8(): pass

    label("Function_2_BF8")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメントを回復できる装置がある。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "ここで休憩する\x01",      # 0
            "やめる\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CE5")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0xB, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0xB, 0x0)
    OP_71(0xB, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0xB)
    OP_71(0xB, 0x1F, 0x186, 0x0, 0x20)
    Sleep(1000)
    StopBGM(0xBB8)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    Sound(13, 0, 100, 0)
    OP_0D()
    OP_32(0xFF, 0xFE, 0x0)
    OP_6A(0x0, 0x0)
    OP_31(0x1)
    Sleep(3500)
    OP_70(0xB, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_CE5")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_BF8 end

    def Function_3_CF4(): pass

    label("Function_3_CF4")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 0)), scpexpr(EXPR_END)), "loc_D3D")
    TalkBegin(0xFF)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座の上に宝珠が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_EDA")

    label("loc_D3D")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33E, 0x0)"), scpexpr(EXPR_END)), "loc_EB6")
    EventBegin(0x1)

    #A0003
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座がある。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "宝珠を置く\x01",      # 0
            "やめておく\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EAA")
    Fade(500)
    SetChrPos(0x0, 128500, 0, -1900, 90)
    SetChrPos(0x1, 127500, 0, -2700, 90)
    SetChrPos(0x2, 127500, 0, -1100, 90)
    SetChrPos(0x3, 126500, 0, -1900, 90)
    OP_68(128889, 2500, -2580, 0)
    MoveCamera(59, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15390, 0)
    OP_E2(0x3)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(200)
    ClearMapObjFlags(0x10, 0x4)
    SetMapObjFrame(0x10, "b_bace", 0x0, 0x1)
    SetMapObjFrame(0x10, "b_in", 0x1, 0x1)
    SetMapObjFrame(0x10, "b_in2", 0x1, 0x1)
    SetMapObjFrame(0x10, "b_out", 0x1, 0x1)
    SetMapObjFrame(0x10, "b_out2", 0x1, 0x1)
    SetMapObjFrame(0x10, "b_light", 0x1, 0x1)
    OP_0D()
    Sleep(500)

    #A0004
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座の上に宝珠を置いた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x33E, 1)
    SetScenarioFlags(0x1B7, 0)
    Call(0, 5)
    OP_E2(0x2)

    label("loc_EAA")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_EDA")

    label("loc_EB6")

    TalkBegin(0xFF)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_EDA")

    Return()

    # Function_3_CF4 end

    def Function_4_EDB(): pass

    label("Function_4_EDB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 1)), scpexpr(EXPR_END)), "loc_F24")
    TalkBegin(0xFF)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座の上に宝珠が置かれている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_10C1")

    label("loc_F24")

    Jc((scpexpr(EXPR_EXEC_OP, "GetItemNumber(0x33E, 0x0)"), scpexpr(EXPR_END)), "loc_109D")
    EventBegin(0x1)

    #A0007
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座がある。\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "宝珠を置く\x01",      # 0
            "やめておく\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1091")
    Fade(500)
    SetChrPos(0x0, 128500, 0, 1900, 90)
    SetChrPos(0x1, 127500, 0, 2700, 90)
    SetChrPos(0x2, 127500, 0, 1100, 90)
    SetChrPos(0x3, 126500, 0, 1900, 90)
    OP_68(127770, 2550, 720, 0)
    MoveCamera(48, 28, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14620, 0)
    OP_E2(0x3)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(802, 0, 100, 0)
    Fade(200)
    ClearMapObjFlags(0x11, 0x4)
    SetMapObjFrame(0x11, "b_bace", 0x0, 0x1)
    SetMapObjFrame(0x11, "b_in", 0x1, 0x1)
    SetMapObjFrame(0x11, "b_in2", 0x1, 0x1)
    SetMapObjFrame(0x11, "b_out", 0x1, 0x1)
    SetMapObjFrame(0x11, "b_out2", 0x1, 0x1)
    SetMapObjFrame(0x11, "b_light", 0x1, 0x1)
    OP_0D()
    Sleep(500)

    #A0008
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座の上に宝珠を置いた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SubItemNumber(0x33E, 1)
    SetScenarioFlags(0x1B7, 1)
    Call(0, 5)
    OP_E2(0x2)

    label("loc_1091")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Jump("loc_10C1")

    label("loc_109D")

    TalkBegin(0xFF)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "台座がある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)

    label("loc_10C1")

    Return()

    # Function_4_EDB end

    def Function_5_10C2(): pass

    label("Function_5_10C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1B7, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1131")
    Fade(500)
    OP_68(139400, 10850, 780, 0)
    MoveCamera(69, 7, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(21990, 0)
    OP_0D()
    Sleep(500)
    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Fade(1000)
    SetMapObjFlags(0xF, 0x4)
    SetBarrier(0x2, 0x9, 0x1)
    SetCameraDistance(20990, 1000)
    OP_0D()
    Sleep(3000)

    label("loc_1131")

    Return()

    # Function_5_10C2 end

    def Function_6_1132(): pass

    label("Function_6_1132")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 4)), scpexpr(EXPR_END)), "loc_117B")
    TalkBegin(0xFF)
    SetChrName("")

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは押されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_1312")

    label("loc_117B")

    EventBegin(0x1)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_130B")
    Fade(500)
    SetChrPos(0x0, 113260, 9000, 9260, 180)
    SetChrPos(0x1, 110400, 9000, 9300, 90)
    SetChrPos(0x2, 108400, 9000, 9300, 90)
    SetChrPos(0x3, 106400, 9000, 9300, 90)
    OP_68(113920, 11500, 9260, 0)
    MoveCamera(35, 27, 0, 0)
    OP_6E(570, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    SetMapObjFrame(0x6, "root", 0x2, "on")
    Sleep(1200)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x9, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(500)
    Fade(500)
    OP_68(133890, 11500, -180, 0)
    MoveCamera(64, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x4, "root", 0x2, "move")
    Sleep(1000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    SetScenarioFlags(0x150, 4)

    label("loc_130B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_1312")

    Return()

    # Function_6_1132 end

    def Function_7_1313(): pass

    label("Function_7_1313")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 5)), scpexpr(EXPR_END)), "loc_135C")
    TalkBegin(0xFF)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでにスイッチは押されている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_14F0")

    label("loc_135C")

    EventBegin(0x1)

    #A0013
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_14E9")
    Fade(500)
    SetChrPos(0x0, 113660, 9000, -9380, 0)
    SetChrPos(0x1, 110400, 9000, -10100, 90)
    SetChrPos(0x2, 108400, 9000, -10100, 90)
    SetChrPos(0x3, 106400, 9000, -10100, 90)
    OP_68(114150, 11500, -10180, 0)
    MoveCamera(50, 31, 0, 0)
    OP_6E(630, 0)
    SetCameraDistance(15500, 0)
    OP_0D()
    SetMapObjFrame(0x7, "root", 0x2, "on")
    Sleep(1200)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0xA, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(500)
    Fade(500)
    OP_68(133890, 11500, -180, 0)
    MoveCamera(64, 21, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    SetMapObjFrame(0x5, "root", 0x2, "move")
    Sleep(2000)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x0, 0x64, 0x3E8, 0x64)
    Sleep(1000)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x2, 0x6, 0x1)
    SetBarrier(0x2, 0x7, 0x1)
    SetScenarioFlags(0x150, 5)

    label("loc_14E9")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_14F0")

    Return()

    # Function_7_1313 end

    def Function_8_14F1(): pass

    label("Function_8_14F1")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x150, 6)), scpexpr(EXPR_END)), "loc_1532")
    TalkBegin(0xFF)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "すでに鍵は外されてる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_15F4")

    label("loc_1532")

    EventBegin(0x1)

    #A0015
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉に鍵が掛けられている。\x01",
            "外しますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15ED")
    Fade(500)
    OP_68(-3250, 600, 40, 0)
    MoveCamera(55, 27, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(18000, 0)
    OP_0D()
    Sleep(1000)
    Sound(119, 0, 100, 0)
    SetMapObjFrame(0xC, "root", 0x2, "move")
    Sleep(1500)
    ClearMapObjFlags(0xC, 0x2)
    SetBarrier(0x2, 0x8, 0x1)
    OP_65(0x3, 0x1)
    SetScenarioFlags(0x150, 6)

    label("loc_15ED")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_15F4")

    Return()

    # Function_8_14F1 end

    def Function_9_15F5(): pass

    label("Function_9_15F5")

    TalkBegin(0xFF)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    TalkEnd(0xFF)
    Return()

    # Function_9_15F5 end

    def Function_10_1621(): pass

    label("Function_10_1621")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    ClearMapFlags(0x10000000)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 104000, 0, 0, 90)
    SetChrPos(0x102, 103000, 0, 600, 90)
    SetChrPos(0x103, 103000, 0, -600, 90)
    SetChrPos(0x104, 102000, 0, -100, 90)
    SetChrPos(0xF4, 101300, 0, 600, 90)
    SetChrPos(0xF5, 100700, 0, -600, 90)
    OP_68(100000, 6700, -3000, 0)
    MoveCamera(67, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    PlaceName2(340, 200, "c_plac29", 0x0, 1500)
    FadeToBright(1000, 0)
    OP_68(100000, 4700, -3000, 5000)

    def lambda_170C():
        OP_9B(0x0, 0x101, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_170C)
    Sleep(50)

    def lambda_1724():
        OP_9B(0x0, 0x102, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_1724)
    Sleep(50)

    def lambda_173C():
        OP_9B(0x0, 0x103, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_173C)
    Sleep(50)

    def lambda_1754():
        OP_9B(0x0, 0x104, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_1754)
    Sleep(50)

    def lambda_176C():
        OP_9B(0x0, 0xF4, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_176C)
    Sleep(50)

    def lambda_1784():
        OP_9B(0x0, 0xF5, 0x0, 0x1B58, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF5, 0, lambda_1784)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0xF5, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(110000, 1400, 0, 0)
    MoveCamera(67, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(14500, 0)
    SetCameraDistance(13500, 2500)
    OP_6F(0x79)
    OP_0D()

    #C0017
    ChrTalk(
        0x101,
        "#00005F#6Pあれは……\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(1000)
    OP_68(131500, 3000, 16000, 0)
    MoveCamera(60, 13, 0, 0)
    MoveCamera(45, 6, 0, 5000)
    OP_6E(700, 0)
    SetCameraDistance(29500, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(131500, 2000, -3000, 0)
    OP_68(131500, 2000, -8300, 5000)
    MoveCamera(65, 12, 0, 0)
    MoveCamera(55, 12, 0, 5000)
    OP_6E(700, 0)
    SetCameraDistance(29500, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(125000, 11200, 0, 0)
    OP_68(135500, 11200, 0, 7500)
    MoveCamera(67, 6, 0, 0)
    MoveCamera(67, 13, 0, 7500)
    OP_6E(700, 0)
    SetCameraDistance(20000, 0)
    OP_6F(0x79)
    OP_0D()
    Fade(1000)
    OP_68(110000, 2100, 0, 0)
    OP_68(110000, 1400, 0, 2000)
    MoveCamera(67, 26, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(13500, 0)
    OP_6F(0x79)
    OP_0D()

    #C0018
    ChrTalk(
        0x103,
        (
            "#00208F#6Pやはり何らかの術によって\x01",
            "封印されているようですが……\x02\x03",

            "#00201F幾つか種類があるみたいですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x102,
        (
            "#00108F#6P両脇の扉を封じているのは\x01",
            "《結社》のものみたいだけど……\x02\x03",

            "#00101F隠し扉を封じているのは\x01",
            "《教団》の目の紋章みたいね。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#00013F#6Pああ……\x01",
            "一体どういうつもりだ？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1AA5")

    #C0021
    ChrTalk(
        0x109,
        (
            "#10101F#6Pとにかく探索を始めるしか\x01",
            "ありませんね……！\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1ADC")

    label("loc_1AA5")


    #C0022
    ChrTalk(
        0x106,
        (
            "#10701F#6Pとにかく探索を\x01",
            "始めるしかなさそうです。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1ADC")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1B15")

    #C0023
    ChrTalk(
        0x105,
        "#10400F#6Pそれじゃあ行こうか。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B39")

    label("loc_1B15")


    #C0024
    ChrTalk(
        0x106,
        "#10701F#6Pええ、行きましょう。\x02",
    )

    CloseMessageWindow()

    label("loc_1B39")

    FadeToDark(1000, 0, -1)
    OP_0D()
    SetChrPos(0x0, 105500, 0, 0, 90)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x1A4, 4)
    OP_29(0xB0, 0x1, 0x2)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_10_1621 end

    def Function_11_1B7B(): pass

    label("Function_11_1B7B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(130310, 2500, -16730, 0)
    MoveCamera(50, 13, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15530, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Fade(1000)
    SetMapObjFlags(0xD, 0x4)
    SetCameraDistance(16990, 1000)
    OP_0D()
    Sleep(3000)
    SetScenarioFlags(0x1B7, 2)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m2050", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_1B7B end

    def Function_12_1C01(): pass

    label("Function_12_1C01")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_68(129740, 2500, 12880, 0)
    MoveCamera(41, 17, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15530, 0)
    FadeToBright(500, 0)
    OP_0D()
    Sleep(1000)
    Sound(202, 0, 100, 0)
    Sound(223, 0, 100, 0)
    Fade(1000)
    SetMapObjFlags(0xE, 0x4)
    SetCameraDistance(16990, 1000)
    OP_0D()
    Sleep(3000)
    SetScenarioFlags(0x1B7, 3)
    FadeToDark(500, 0, -1)
    OP_0D()
    SetScenarioFlags(0x22, 0)
    NewScene("m2020", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1C01 end

    SaveToFile()

Try(main)
