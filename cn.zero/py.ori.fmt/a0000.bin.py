from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "a0000.bin",                # FileName
        "a0000",                    # MapName
        "a0000",                    # Location
        0x0001,                     # MapIndex
        "ed7000",
        0x00000000,                 # Flags
        ("a0000", "a0000_1", "a0000_2", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 45, 1, 1, 0, 0, 0, 1],
    )

    BuildStringList((
        "a0000",                  # 0
        "Npl03",                  # 1
        "ランディ",               # 2
        "br2000",                 # 3
        "bm0113",                 # 4
        "br2000",                 # 5
        "bt3000",                 # 6
        "bm0112",                 # 7
        "br2000",                 # 8
        "br2000",                 # 9
        "bm3060",                 # 10
        "bm3070",                 # 11
        "地名１",                 # 12
        "地名３",                 # 13
    ))

    ATBonus("ATBonus_1C0", 100, 20, 20, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
    ATBonus("ATBonus_1A0", 100, 5, 0, 5, 0, 5, 0, 5, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_180", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_4C74", 100, 1,   2,   3,   70,  89,  99)

    MonsterBattlePostion("MonsterBattlePostion_1D0", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D8", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1DC", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E0", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1E8", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1EC", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_250", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_254", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_258", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_25C", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_260", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_264", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_268", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_26C", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_330", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_344", 14, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 10, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 11, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 12, 16, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 5, 16, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 2, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 14, 15, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 6, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 10, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_318", 6, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_31C", 10, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_320", 4, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_324", 12, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 8, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 11, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 8, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_364", 14, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_368", 9, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_36C", 6, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B0", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2B4", 14, 8, 225)
    MonsterBattlePostion("MonsterBattlePostion_2B8", 2, 8, 135)
    MonsterBattlePostion("MonsterBattlePostion_2BC", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 0, 0, 180)

    # monster count: 1

    BattleInfo(
        "BattleInfo_370", 0x0010, 3, 6, 45, 3, 3, 30, 0, "br2000", "Sepith_4C74", 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, "ms65000.dat", 0, "MonsterBattlePostion_1D0", "MonsterBattlePostion_250", "ed7400", "ed7403", "ATBonus_1C0"),
            (),
            (),
            (),
        )
    )

    # event battle count: 9

    BattleInfo(
        "BattleInfo_3B4", 0x0042, 50, 6, 0, 0, 1, 0, 0, "bm0113", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60001.dat", "ms60001.dat", "ms60001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_330", "MonsterBattlePostion_250", "ed7405", "ed7403", "ATBonus_1A0"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_3F8", 0x0000, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms02000.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2D0", "MonsterBattlePostion_2D0", "ed7400", "ed7403", "ATBonus_180"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_43C", 0x0062, 40, 6, 60, 0, 0, 0, 0, "bt3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms75400.dat", "ms75400.dat", "ms76300.dat", "ms76300.dat", "ms76300.dat", "ms76300.dat", 0, 0, "MonsterBattlePostion_310", "MonsterBattlePostion_250", "ed7405", "ed7000", "ATBonus_180"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_480", 0x0042, 50, 6, 0, 0, 1, 0, 0, "bm0112", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "ms60100.dat", "MonsterBattlePostion_350", "MonsterBattlePostion_250", "ed7405", "ed7403", "ATBonus_180"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_4C4", 0x0000, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "ms74600.dat", "MonsterBattlePostion_1D0", "MonsterBattlePostion_250", "ed7400", "ed7403", "ATBonus_180"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_508", 0x0010, 3, 6, 45, 3, 1, 30, 0, "br2000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms60000.dat", "ms60000.dat", "ms60000.dat", 0, 0, 0, "ms65000.dat", 0, "MonsterBattlePostion_1D0", "MonsterBattlePostion_250", "ed7400", "ed7403", "ATBonus_180"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_54C", 0x0010, 3, 6, 45, 3, 1, 30, 0, "bm3060", 0x00000000, 100, 0, 0, 0,
        (
            ("ms89900.dat", "ms61600.dat", "ms69600.dat", 0, 0, 0, 0, "ms70100.dat", "MonsterBattlePostion_2B0", "MonsterBattlePostion_2B0", "ed7001", "ed7403", "ATBonus_180"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch40000.itc",                   # 00
        "chr/ch20000.itc",                   # 01
        "chr/ch20100.itc",                   # 02
        "chr/ch20200.itc",                   # 03
        "chr/ch20300.itc",                   # 04
        "chr/ch20400.itc",                   # 05
        "chr/ch20500.itc",                   # 06
        "chr/ch20600.itc",                   # 07
        "chr/ch00000.itc",                   # 08
        "chr/ch00000.itc",                   # 09
        "chr/ch00000.itc",                   # 0A
        "chr/ch00000.itc",                   # 0B
        "chr/ch00000.itc",                   # 0C
        "chr/ch20700.itc",                   # 0D
    ))

    DeclNpc(-4000,   2000,    0,       135,  261,  0x0, 0,   3,   0,   0,   11,  0,   14,  255,  0)
    DeclNpc(-17989,  0,       -22840,  135,  261,  0x0, 0,   13,  0,   0,   11,  0,   14,  255,  0)

    DeclMonster(10000,   -14000,  0,       0x1010000,    "BattleInfo_370", 4,   5,   0xFFFF, 0,  1)

    DeclActor(2000,    0,       400000,  2000,    2000,    1000,    400000,  0x007C, 0,  2,  0x0000)

    PlaceName(10.0, 1.0, 2.0, 0x0000, 0x0000, "地名１")
    PlaceName(-10.0, 1.0, 2.0, 0x0000, 0x0000, "地名３")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 0
    ChipFrameInfo(5000, 0, [0, 1, 2, 3])                         # 1

    ScpFunction((
        "Function_0_688",          # 00, 0
        "Function_1_69C",          # 01, 1
        "Function_2_6FE",          # 02, 2
        "Function_3_B7D",          # 03, 3
        "Function_4_C08",          # 04, 4
        "Function_5_C2D",          # 05, 5
        "Function_6_C4B",          # 06, 6
        "Function_7_184A",         # 07, 7
        "Function_8_1A76",         # 08, 8
        "Function_9_1F0F",         # 09, 9
        "Function_10_1FBF",        # 0A, 10
        "Function_11_2077",        # 0B, 11
        "Function_12_212F",        # 0C, 12
        "Function_13_2140",        # 0D, 13
        "Function_14_217F",        # 0E, 14
        "Function_15_2426",        # 0F, 15
        "Function_16_244E",        # 10, 16
        "Function_17_2463",        # 11, 17
        "Function_18_25DA",        # 12, 18
        "Function_19_25DD",        # 13, 19
        "Function_20_25E0",        # 14, 20
        "Function_21_25E3",        # 15, 21
        "Function_22_25E6",        # 16, 22
        "Function_23_25E9",        # 17, 23
        "Function_24_25EC",        # 18, 24
        "Function_25_25EF",        # 19, 25
        "Function_26_25F2",        # 1A, 26
        "Function_27_26BC",        # 1B, 27
        "Function_28_276F",        # 1C, 28
        "Function_29_28CD",        # 1D, 29
        "Function_30_2C3F",        # 1E, 30
        "Function_31_30B2",        # 1F, 31
        "Function_32_3426",        # 20, 32
        "Function_33_377C",        # 21, 33
        "Function_34_41E2",        # 22, 34
        "Function_35_42B5",        # 23, 35
        "Function_36_4525",        # 24, 36
        "Function_37_475D",        # 25, 37
        "Function_38_4BE6",        # 26, 38
    ))


    def Function_0_688(): pass

    label("Function_0_688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_695")
    Call(0, 2)

    label("loc_695")

    SetScenarioFlags(0x5A, 0)
    Event(0, 6)
    Return()

    # Function_0_688 end

    def Function_1_69C(): pass

    label("Function_1_69C")

    SetBarrier(0x0, 0x0, 0x1, 0x0, 5000, 0, 9000, 4000, 2000, 30000)
    SetBarrier(0x0, 0x1, 0x1, 0x0, 4000, 0, 8000, 4000, 2000, 30000)
    SetBarrier(0x2, 0x0, 0x1)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    SetChrFlags(0x9, 0x8)
    OP_63(0x9, 0x0, 2000, 0x1C, 0x21, 0xFA, 0x0)
    Return()

    # Function_1_69C end

    def Function_2_6FE(): pass

    label("Function_2_6FE")

    ClearMapFlags(0x80)
    ClearParty()
    AddParty(0x0, 0xFF, 0xFF)
    AddParty(0x1, 0xFF, 0xFF)
    AddParty(0x2, 0xFF, 0xFF)
    AddParty(0x3, 0xFF, 0xFF)
    OP_32(0x0, 0xFB, 0x0)
    OP_32(0x1, 0xFB, 0x0)
    OP_32(0x2, 0xFB, 0x0)
    OP_32(0x3, 0xFB, 0x0)
    OP_32(0x4, 0xFB, 0x0)
    OP_32(0x4, 0xFB, 0x0)
    OP_32(0x5, 0xFB, 0x0)
    OP_32(0x6, 0xFB, 0x0)
    OP_32(0x7, 0xFB, 0x0)
    OP_32(0x8, 0xFB, 0x0)
    OP_32(0x9, 0xFB, 0x0)
    OP_DE(0x0, 0x0)
    AddMira(2000)
    AddSepith(0xFF, 100)
    AddItemNumber(0x3E8, 1)
    AddItemNumber(0x3E9, 1)
    AddItemNumber(0x3EA, 1)
    AddItemNumber(0x3ED, 1)
    AddItemNumber(0x1, 1)
    AddItemNumber(0x2, 1)
    AddItemNumber(0x3, 1)
    AddItemNumber(0x4, 1)
    AddItemNumber(0x5, 1)
    AddItemNumber(0x6, 1)
    AddItemNumber(0x1F4, 10)
    AddItemNumber(0x1F5, 10)
    AddItemNumber(0x1F6, 10)
    AddItemNumber(0x1F8, 10)
    AddItemNumber(0x1F9, 10)
    AddItemNumber(0x1FB, 10)
    AddItemNumber(0x1FC, 10)
    AddItemNumber(0x20B, 10)
    AddItemNumber(0x32, 10)
    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    OP_42(0x0, 0x640, 0xFF)
    OP_42(0x1, 0x640, 0xFF)
    OP_42(0x2, 0x640, 0xFF)
    OP_42(0x3, 0x640, 0xFF)
    OP_42(0x8, 0x640, 0xFF)
    OP_42(0x9, 0x640, 0xFF)
    OP_42(0x6, 0x640, 0xFF)
    OP_42(0x7, 0x640, 0xFF)
    OP_42(0x0, 0x5DC, 0xFF)
    OP_42(0x1, 0x5DC, 0xFF)
    OP_42(0x2, 0x5DC, 0xFF)
    OP_42(0x3, 0x5DC, 0xFF)
    OP_42(0x8, 0x5DC, 0xFF)
    OP_42(0x9, 0x5DC, 0xFF)
    OP_42(0x6, 0x5DC, 0xFF)
    OP_42(0x7, 0x5DC, 0xFF)
    OP_42(0x0, 0x3E8, 0xFF)
    OP_42(0x1, 0x3FC, 0xFF)
    OP_42(0x2, 0x410, 0xFF)
    OP_42(0x3, 0x424, 0xFF)
    OP_42(0x9, 0x451, 0xFF)
    OP_42(0x8, 0x44C, 0xFF)
    AddCraft(0x0, 0x14A)
    AddCraft(0x1, 0x14A)
    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    AddCraft(0x0, 0x14B)
    AddCraft(0x2, 0x14B)
    AddCraft(0x0, 0x14C)
    AddCraft(0x3, 0x14C)
    AddCraft(0x1, 0x14D)
    AddCraft(0x2, 0x14D)
    AddCraft(0x1, 0x14E)
    AddCraft(0x3, 0x14E)
    AddCraft(0x2, 0x14F)
    AddCraft(0x3, 0x14F)
    AddCraft(0x6, 0x150)
    AddCraft(0x7, 0x150)
    AddCraft(0x0, 0x154)
    AddCraft(0x0, 0x155)
    AddCraft(0x0, 0x156)
    AddCraft(0x0, 0x96)
    AddCraft(0x0, 0x97)
    AddCraft(0x0, 0x98)
    AddCraft(0x0, 0x99)
    AddCraft(0x0, 0x9A)
    AddCraft(0x0, 0xFA)
    AddCraft(0x0, 0xFB)
    AddCraft(0x0, 0x12C)
    AddCraft(0x1, 0xA0)
    AddCraft(0x1, 0xA1)
    AddCraft(0x1, 0xA2)
    AddCraft(0x1, 0xA3)
    AddCraft(0x1, 0xA4)
    AddCraft(0x1, 0xFF)
    AddCraft(0x1, 0x100)
    AddCraft(0x1, 0x12F)
    AddCraft(0x2, 0xAA)
    AddCraft(0x2, 0xAB)
    AddCraft(0x2, 0xAC)
    AddCraft(0x2, 0xAD)
    AddCraft(0x2, 0xAE)
    AddCraft(0x2, 0x104)
    AddCraft(0x2, 0x105)
    AddCraft(0x2, 0x132)
    SetScenarioFlags(0x5A, 2)
    AddCraft(0x3, 0xB4)
    AddCraft(0x3, 0xB5)
    AddCraft(0x3, 0xB6)
    AddCraft(0x3, 0xB7)
    AddCraft(0x3, 0xB8)
    AddCraft(0x3, 0x109)
    AddCraft(0x3, 0x10A)
    AddCraft(0x3, 0x135)
    AddCraft(0x4, 0xBE)
    AddCraft(0x4, 0xBF)
    AddCraft(0x4, 0xC0)
    AddCraft(0x4, 0x10E)
    AddCraft(0x4, 0x138)
    AddCraft(0x5, 0xC8)
    AddCraft(0x5, 0xC9)
    AddCraft(0x5, 0xCA)
    AddCraft(0x5, 0xCB)
    AddCraft(0x5, 0x113)
    AddCraft(0x5, 0x13B)
    AddCraft(0x6, 0xD2)
    AddCraft(0x6, 0xD3)
    AddCraft(0x6, 0xD4)
    AddCraft(0x6, 0xD5)
    AddCraft(0x6, 0xD6)
    AddCraft(0x6, 0x118)
    AddCraft(0x6, 0x13E)
    AddCraft(0x7, 0xDC)
    AddCraft(0x7, 0xDD)
    AddCraft(0x7, 0xDE)
    AddCraft(0x7, 0xDF)
    AddCraft(0x7, 0xE0)
    AddCraft(0x7, 0x11D)
    AddCraft(0x7, 0x141)
    AddCraft(0x8, 0xE6)
    AddCraft(0x8, 0xE7)
    AddCraft(0x8, 0xE8)
    AddCraft(0x8, 0x122)
    AddCraft(0x8, 0x144)
    AddCraft(0x9, 0xF0)
    AddCraft(0x9, 0xF1)
    AddCraft(0x9, 0xF2)
    AddCraft(0x9, 0xF3)
    AddCraft(0x9, 0x127)
    AddCraft(0x9, 0x147)
    SetChrChipPat(0x0, 0x6, 0xFA)
    SetChrChipPat(0x2, 0x6, 0x104)
    SetChrChipPat(0x1, 0x6, 0xFF)
    SetChrChipPat(0x3, 0x6, 0x109)
    SetChrChipPat(0x6, 0x6, 0x118)
    OP_38(0x0, 0x80, 0x2)
    OP_38(0x0, 0x81, 0x2)
    OP_38(0x0, 0x82, 0x2)
    OP_38(0x0, 0x83, 0x2)
    OP_38(0x0, 0x84, 0x2)
    OP_38(0x0, 0x85, 0x2)
    OP_38(0x0, 0x86, 0x2)
    AddItemNumber(0x6A, 1)
    AddItemNumber(0x6D, 1)
    AddItemNumber(0x70, 1)
    AddItemNumber(0x73, 1)
    AddItemNumber(0x76, 1)
    AddItemNumber(0x79, 1)
    RemoveCraft(0x0, 0xA)
    RemoveCraft(0x0, 0xB)
    RemoveCraft(0x0, 0xC)
    RemoveCraft(0x0, 0xD)
    RemoveCraft(0x0, 0xE)
    RemoveCraft(0x0, 0x14)
    RemoveCraft(0x0, 0x15)
    RemoveCraft(0x0, 0x16)
    RemoveCraft(0x0, 0x17)
    RemoveCraft(0x0, 0x18)
    RemoveCraft(0x0, 0x19)
    RemoveCraft(0x0, 0x1E)
    RemoveCraft(0x0, 0x1F)
    RemoveCraft(0x0, 0x20)
    RemoveCraft(0x0, 0x21)
    RemoveCraft(0x0, 0x22)
    RemoveCraft(0x0, 0x28)
    RemoveCraft(0x0, 0x29)
    RemoveCraft(0x0, 0x2A)
    RemoveCraft(0x0, 0x2B)
    RemoveCraft(0x0, 0x2C)
    RemoveCraft(0x0, 0x32)
    RemoveCraft(0x0, 0x33)
    RemoveCraft(0x0, 0x34)
    RemoveCraft(0x0, 0x3C)
    RemoveCraft(0x0, 0x48)
    RemoveCraft(0x0, 0x3E)
    RemoveCraft(0x0, 0x46)
    RemoveCraft(0x0, 0x47)
    RemoveCraft(0x0, 0x50)
    RemoveCraft(0x0, 0x51)
    RemoveCraft(0x0, 0x52)
    RemoveCraft(0x0, 0x53)
    RemoveCraft(0x0, 0x58)
    RemoveCraft(0x0, 0x59)
    RemoveCraft(0x0, 0x5A)
    RemoveCraft(0x0, 0x60)
    RemoveCraft(0x0, 0x61)
    RemoveCraft(0x0, 0x62)
    RemoveCraft(0x0, 0x63)
    RemoveCraft(0x0, 0x64)
    RemoveCraft(0x0, 0x68)
    RemoveCraft(0x0, 0x69)
    RemoveCraft(0x0, 0x6A)
    RemoveCraft(0x0, 0x70)
    RemoveCraft(0x0, 0x71)
    RemoveCraft(0x0, 0x72)
    RemoveCraft(0x0, 0x78)
    RemoveCraft(0x0, 0x79)
    RemoveCraft(0x0, 0x7A)
    RemoveCraft(0x0, 0x73)
    RemoveCraft(0x0, 0x80)
    RemoveCraft(0x0, 0x81)
    RemoveCraft(0x0, 0x82)
    RemoveCraft(0x0, 0x83)
    RemoveCraft(0x0, 0x84)
    RemoveCraft(0x0, 0x85)
    RemoveCraft(0x1, 0x50)
    RemoveCraft(0x1, 0x51)
    RemoveCraft(0x1, 0x52)
    RemoveCraft(0x1, 0x53)
    RemoveCraft(0x1, 0x58)
    RemoveCraft(0x1, 0x59)
    RemoveCraft(0x1, 0x5A)
    RemoveCraft(0x1, 0x60)
    RemoveCraft(0x1, 0x61)
    RemoveCraft(0x1, 0x62)
    RemoveCraft(0x1, 0x63)
    RemoveCraft(0x1, 0x64)
    RemoveCraft(0x1, 0x68)
    RemoveCraft(0x1, 0x69)
    RemoveCraft(0x1, 0x6A)
    RemoveCraft(0x1, 0x70)
    RemoveCraft(0x1, 0x71)
    RemoveCraft(0x1, 0x72)
    RemoveCraft(0x1, 0x78)
    RemoveCraft(0x1, 0x79)
    RemoveCraft(0x1, 0x7A)
    RemoveCraft(0x1, 0x73)
    RemoveCraft(0x1, 0x80)
    RemoveCraft(0x1, 0x81)
    RemoveCraft(0x1, 0x82)
    RemoveCraft(0x1, 0x83)
    RemoveCraft(0x1, 0x84)
    RemoveCraft(0x1, 0x85)
    RemoveCraft(0x2, 0x1E)
    RemoveCraft(0x2, 0x1F)
    RemoveCraft(0x2, 0x20)
    RemoveCraft(0x2, 0x21)
    RemoveCraft(0x3, 0x28)
    RemoveCraft(0x3, 0x29)
    RemoveCraft(0x3, 0x2A)
    RemoveCraft(0x3, 0x2B)
    RemoveCraft(0x6, 0x32)
    RemoveCraft(0x6, 0x33)
    RemoveCraft(0x6, 0x34)
    RemoveCraft(0x6, 0x3C)
    RemoveCraft(0x7, 0x48)
    RemoveCraft(0x7, 0x3E)
    RemoveCraft(0x7, 0x46)
    RemoveCraft(0x7, 0x47)
    Return()

    # Function_2_6FE end

    def Function_3_B7D(): pass

    label("Function_3_B7D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C07")

    label("loc_B88")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_BC9")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_BC1")
    SetMapObjFrame(0x5, "light", 0x1, 0x1)
    OP_71(0x5, 0x79, 0xB4, 0x0, 0x20)
    Jump("loc_BC9")

    label("loc_BC1")

    Sleep(100)
    Jump("loc_B88")

    label("loc_BC9")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C02")
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0x0, 0xB), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BFA")
    SetMapObjFrame(0x5, "light", 0x0, 0x1)
    OP_70(0x5, 0x78)
    Jump("loc_C02")

    label("loc_BFA")

    Sleep(1)
    Jump("loc_BC9")

    label("loc_C02")

    Jump("Function_3_B7D")

    label("loc_C07")

    Return()

    # Function_3_B7D end

    def Function_4_C08(): pass

    label("Function_4_C08")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C2C")
    SetMapObjFrame(0x3, "motest06", 0x2, "play")
    Sleep(1000)
    Jump("Function_4_C08")

    label("loc_C2C")

    Return()

    # Function_4_C08 end

    def Function_5_C2D(): pass

    label("Function_5_C2D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_C4A")
    OP_A1(0xFE, 0x3E8, 0x4, 0x0, 0x0, 0x0, 0x0)
    Sleep(1000)
    Jump("Function_5_C2D")

    label("loc_C4A")

    Return()

    # Function_5_C2D end

    def Function_6_C4B(): pass

    label("Function_6_C4B")

    SetMapFlags(0x80)

    #A0001
    AnonymousTalk(
        0x101,
        (
            "ああああ\x01",
            "012345678901234567890123456789012345678901234567890123456789\x01",
            "ううううう\x02",
        )
    )

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_CAF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_183E")

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "マップ選択\x01",                # 0
            "キャラ閲覧\x01",                # 1
            "戦闘テスト\x01",                # 2
            "ミニゲーム\x01",                # 3
            "ムービー\x01",                  # 4
            "クエスト関連テスト\x01",        # 5
            "徘徊テスト\x01",                # 6
            "お店テスト\x01",                # 7
            "キーア、イヌ、２週目\x01",      # 8
            "イベントジャンプ１\x01",        # 9
            "イベントジャンプ２\x01",        # 10
            "イベントジャンプ３\x01",        # 11
            "一般会話用フラグ管理\x01",      # 12
            "クエスト用フラグ管理\x01",      # 13
            "各種取得、リセット\x01",        # 14
            "テスト\x01",                    # 15
        )
    )

    MenuCmd(4, 0, 0x3)
    MenuEnd(0x0)
    MenuCmd(4, 0, 0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E2C"),
        (1, "loc_E34"),
        (2, "loc_E3C"),
        (3, "loc_E44"),
        (4, "loc_E4C"),
        (5, "loc_FD6"),
        (6, "loc_1558"),
        (7, "loc_1566"),
        (8, "loc_1573"),
        (9, "loc_16BA"),
        (10, "loc_16C5"),
        (11, "loc_16D0"),
        (12, "loc_16DB"),
        (13, "loc_16E3"),
        (14, "loc_16EB"),
        (15, "loc_16F3"),
        (SWITCH_DEFAULT, "loc_182F"),
    )


    label("loc_E2C")

    Call(1, 0)
    Jump("loc_1839")

    label("loc_E34")

    Call(0, 9)
    Jump("loc_1839")

    label("loc_E3C")

    Call(0, 8)
    Jump("loc_1839")

    label("loc_E44")

    Call(0, 7)
    Jump("loc_1839")

    label("loc_E4C")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "ed7_ev01\x01",      # 0
            "欠番    \x01",      # 1
            "ed7_ev03\x01",      # 2
            "ed7_ev04\x01",      # 3
            "ed7_ev05\x01",      # 4
            "ed7_ev06\x01",      # 5
            "ed7_ev07\x01",      # 6
            "ed7_op\x01",        # 7
            "ed7_ed\x01",        # 8
        )
    )

    MenuEnd(0x0)
    OP_57(0x0)
    OP_60(0x0)
    OP_60(0x1)
    OP_C7(0x0, 0x10)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EF3"),
        (1, "loc_F0B"),
        (2, "loc_F15"),
        (3, "loc_F2D"),
        (4, "loc_F45"),
        (5, "loc_F5D"),
        (6, "loc_F75"),
        (7, "loc_F8D"),
        (8, "loc_FA3"),
        (SWITCH_DEFAULT, "loc_FB9"),
    )


    label("loc_EF3")

    PlayMovie(0x0, "ed7_ev01.pmf", 0x2, 0x0)
    Jump("loc_FB9")

    label("loc_F0B")

    UseItem(0x2D6, 0xFF)
    Jump("loc_FB9")

    label("loc_F15")

    PlayMovie(0x0, "ed7_ev03.pmf", 0x2, 0x0)
    Jump("loc_FB9")

    label("loc_F2D")

    PlayMovie(0x0, "ed7_ev04.pmf", 0x2, 0x0)
    Jump("loc_FB9")

    label("loc_F45")

    PlayMovie(0x0, "ed7_ev05.pmf", 0x2, 0x0)
    Jump("loc_FB9")

    label("loc_F5D")

    PlayMovie(0x0, "ed7_ev06.pmf", 0x2, 0x0)
    Jump("loc_FB9")

    label("loc_F75")

    PlayMovie(0x0, "ed7_ev07.pmf", 0x2, 0x0)
    Jump("loc_FB9")

    label("loc_F8D")

    PlayMovie(0x0, "ed7_op.pmf", 0x2, 0x0)
    Jump("loc_FB9")

    label("loc_FA3")

    PlayMovie(0x0, "ed7_ed.pmf", 0x2, 0x0)
    Jump("loc_FB9")

    label("loc_FB9")

    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C7(0x1, 0x10)
    FadeToBright(10, 0)
    Jump("loc_1839")

    label("loc_FD6")


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "端末\x01",                                  # 0
            "報告\x01",                                  # 1
            "??? 序章メイン二つ     情報1登録\x01",      # 2
            "??? ジオフロントの探索      達成\x01",      # 3
            "??? 紛失物の捜索願い   情報1登録\x01",      # 4
            "??? 紛失物の捜索願い        達成\x01",      # 5
            "??  支援要請の補足説明 情報1登録\x01",      # 6
            "??  支援要請の補足説明      達成\x01",      # 7
            "get_note_fish\x01",                         # 8
            "DPくれ\x01",                                # 9
        )
    )

    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1110"),
        (1, "loc_13DD"),
        (2, "loc_1405"),
        (3, "loc_1429"),
        (4, "loc_1445"),
        (5, "loc_148C"),
        (6, "loc_149C"),
        (7, "loc_14AC"),
        (8, "loc_14BC"),
        (9, "loc_1549"),
        (SWITCH_DEFAULT, "loc_1553"),
    )


    label("loc_1110")

    OP_57(0x0)
    OP_E3(0xA)
    OP_E3(0x5)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1120")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CA")
    RunExpression(0x3, (scpexpr(EXPR_EXEC_OP, "OP_E3(0x0)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1153"),
        (1, "loc_1165"),
        (2, "loc_1396"),
        (SWITCH_DEFAULT, "loc_13C5"),
    )


    label("loc_1153")

    OP_2B(0x0, 0x1, 0x2, 0x3, 0xB, 0xFFFF)
    Jump("loc_13C5")

    label("loc_1165")

    OP_E3(0x7)
    Sleep(500)
    Sound(2061, 255, 100, 0)    #voice#Fran
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E3(0x4)"), scpexpr(EXPR_END)), "loc_130D")
    OutputDebugInt(0xDE)
    SetChrName("フラン")

    #A0002
    AnonymousTalk(
        0xFF,
        (
            "それでは達成した依頼の\x01",
            "報告を承りますね～。\x02",
        )
    )

    CloseMessageWindow()
    RunExpression(0x6, (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_E3(0xC)
    Jc((scpexpr(EXPR_GET_RESULT, 0x6), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12AF")
    SetMapFlags(0x40000000)
    SetChrName("フラン")

    #A0003
    AnonymousTalk(
        0xFF,
        "ランクアップおめでとうございます。\x02",
    )

    CloseMessageWindow()
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2F), scpexpr(EXPR_END)),
        (1, "loc_120D"),
        (SWITCH_DEFAULT, "loc_1241"),
    )


    label("loc_120D")


    #A0004
    AnonymousTalk(
        0xFF,
        (
            "クラス１４ｔｈ－－\x01",
            "ロイドさん、すごいです\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1241")

    label("loc_1241")

    ClearMapFlags(0x40000000)

    #A0005
    AnonymousTalk(
        0xFF,
        (
            "特典の品もすぐに\x01",
            "そちらにお届けしますね～！\x02\x03",

            "お疲れさまでした～！\x01",
            "またよろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1308")

    label("loc_12AF")

    SetChrName("フラン")

    #A0006
    AnonymousTalk(
        0xFF,
        (
            "これで以上ですね～。\x02\x03",

            "では、また依頼を達成したら\x01",
            "よろしくお願いしますー。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1308")

    Jump("loc_136C")

    label("loc_130D")

    OutputDebugInt(0x6F)
    SetChrName("フラン")

    #A0007
    AnonymousTalk(
        0xFF,
        (
            "あれっ、報告可能な\x01",
            "依頼は無いみたいですね～。\x02\x03",

            "またよろしくお願いしますね～。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_136C")

    OP_E3(0x8)
    SetChrName("フラン")

    #A0008
    AnonymousTalk(
        0xFF,
        (
            "テストです\x01",
            "テストです\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_13C5")

    label("loc_1396")

    SetChrName("フラン")

    #A0009
    AnonymousTalk(
        0xFF,
        "まだ支援要請を見てないですよ\x02",
    )

    CloseMessageWindow()
    Jump("loc_13C5")

    label("loc_13C5")

    Jump("loc_1120")

    label("loc_13CA")

    OP_E3(0x6)
    OP_E3(0xB)
    FadeToBright(1000, 0)
    OP_0D()
    Jump("loc_1553")

    label("loc_13DD")

    OP_57(0x0)
    FadeToDark(300, 0, -1)
    OP_0D()
    OP_29(0x2, 0x4, 0x10)
    OP_29(0x5, 0x4, 0x10)
    OP_E3(0x3)
    FadeToBright(300, 0)
    OP_0D()
    Jump("loc_1553")

    label("loc_1405")

    PlayBGM("ed7400", 0)
    OP_29(0x3C, 0x4, 0x2)
    OP_29(0x3C, 0x4, 0x80)
    OP_29(0x3C, 0x1, 0x0)
    OP_29(0x3D, 0x4, 0x2)
    OP_29(0x3D, 0x1, 0x0)
    Jump("loc_1553")

    label("loc_1429")

    StopBGM(0x2710)
    Sleep(3000)
    PlayBGM("ed7205", 0)
    OP_29(0x3C, 0x1, 0x1)
    OP_29(0x3C, 0x4, 0x10)
    Jump("loc_1553")

    label("loc_1445")

    StopBGM(0xFA0)
    Sound(844, 0, 100, 0)
    Sleep(1000)
    Sound(844, 0, 100, 0)
    Sleep(1000)
    Sound(844, 0, 100, 0)
    Sleep(1000)
    Sound(844, 0, 100, 0)
    Sleep(1000)
    WaitBGM()
    Sleep(10)
    Sound(901, 0, 100, 0)
    PlayBGM("ed7205", 0)
    OP_29(0x2, 0x4, 0x2)
    OP_29(0x2, 0x1, 0x0)
    Jump("loc_1553")

    label("loc_148C")

    OP_29(0x2, 0x1, 0x1)
    OP_29(0x2, 0x4, 0x10)
    Jump("loc_1553")

    label("loc_149C")

    OP_29(0x1, 0x4, 0x2)
    OP_29(0x1, 0x1, 0x0)
    Jump("loc_1553")

    label("loc_14AC")

    OP_29(0x1, 0x1, 0x1)
    OP_29(0x1, 0x4, 0x10)
    Jump("loc_1553")

    label("loc_14BC")

    Sound(3, 1, 100, 0)
    Sleep(5000)
    OP_24(0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_14ED")

    #C0010
    ChrTalk(
        0x0,
        "FISH_COUNT > 0\x02",
    )

    CloseMessageWindow()

    label("loc_14ED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x4, 0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1515")

    #C0011
    ChrTalk(
        0x0,
        "FISH_MAXSIZE > 30\x02",
    )

    CloseMessageWindow()

    label("loc_1515")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x1, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_1544")

    #C0012
    ChrTalk(
        0x0,
        "BATTLE_NOTE_MONSCOUNT > 2\x02",
    )

    CloseMessageWindow()

    label("loc_1544")

    Jump("loc_1553")

    label("loc_1549")

    OP_2C(0x1, 0x5A)
    Jump("loc_1553")

    label("loc_1553")

    Jump("loc_1839")

    label("loc_1558")

    NewScene("a0004", 0, 0, 0)
    IdleLoop()
    Jump("loc_1839")

    label("loc_1566")

    OP_60(0x0)
    OP_57(0x0)
    Call(0, 17)
    Jump("loc_1839")

    label("loc_1573")

    MenuCmd(0, 1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A5")
    MenuCmd(1, 1, "???を?????として仲間に加える")
    Jump("loc_15C7")

    label("loc_15A5")

    MenuCmd(1, 1, "???を護衛???として仲間に加える")

    label("loc_15C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F0")
    MenuCmd(1, 1, "ツァイト使用可能にする")
    Jump("loc_160A")

    label("loc_15F0")

    MenuCmd(1, 1, "ツァイト使用不能にする")

    label("loc_160A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162A")
    MenuCmd(1, 1, "周回数?２週目")
    Jump("loc_1639")

    label("loc_162A")

    MenuCmd(1, 1, "周回数?初回")

    label("loc_1639")

    MenuCmd(2, 1, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x1)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1663"),
        (1, "loc_1681"),
        (2, "loc_169B"),
        (SWITCH_DEFAULT, "loc_16B5"),
    )


    label("loc_1663")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1675")
    SetScenarioFlags(0x5A, 3)
    Jump("loc_1678")

    label("loc_1675")

    ClearScenarioFlags(0x5A, 3)

    label("loc_1678")

    AddParty(0x32, 0xFF, 0xFF)
    Jump("loc_16B5")

    label("loc_1681")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1693")
    SetScenarioFlags(0x5A, 2)
    Jump("loc_1696")

    label("loc_1693")

    ClearScenarioFlags(0x5A, 2)

    label("loc_1696")

    Jump("loc_16B5")

    label("loc_169B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5A, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16AD")
    SetScenarioFlags(0x5A, 4)
    Jump("loc_16B0")

    label("loc_16AD")

    ClearScenarioFlags(0x5A, 4)

    label("loc_16B0")

    Jump("loc_16B5")

    label("loc_16B5")

    Jump("loc_1839")

    label("loc_16BA")

    ClearScenarioFlags(0x5F, 7)
    Call(2, 0)
    Jump("loc_1839")

    label("loc_16C5")

    ClearScenarioFlags(0x5F, 7)
    Call(2, 1)
    Jump("loc_1839")

    label("loc_16D0")

    ClearScenarioFlags(0x5F, 7)
    Call(2, 2)
    Jump("loc_1839")

    label("loc_16DB")

    Call(2, 3)
    Jump("loc_1839")

    label("loc_16E3")

    Call(2, 54)
    Jump("loc_1839")

    label("loc_16EB")

    Call(0, 28)
    Jump("loc_1839")

    label("loc_16F3")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x2C, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_END)), "loc_1734")

    #C0013
    ChrTalk(
        0x0,
        "エクストラある\x02",
    )

    Jump("loc_1747")

    label("loc_1734")


    #C0014
    ChrTalk(
        0x0,
        "エクストラない\x02",
    )


    label("loc_1747")

    Jump("loc_1839")

    label("loc_182F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1839")

    Jump("loc_CAF")

    label("loc_183E")

    OP_60(0x0)
    OP_57(0x0)
    OP_DB()
    ClearMapFlags(0x80)
    Return()

    # Function_6_C4B end

    def Function_7_184A(): pass

    label("Function_7_184A")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1854")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A68")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "パチスロ\x01",                        # 0
            "釣り\x01",                            # 1
            "ルーレット\x01",                      # 2
            "ポーカー(メダル式)\x01",              # 3
            "ポーカー(対戦式)\x01",                # 4
            "ブラックジャック(メダル式)\x01",      # 5
            "ブラックジャック(対戦式)\x01",        # 6
            "メダル取得\x01",                      # 7
            "キャンセル\x01",                      # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1930"),
        (1, "loc_1957"),
        (2, "loc_197E"),
        (3, "loc_19A5"),
        (4, "loc_19CC"),
        (5, "loc_19F3"),
        (6, "loc_1A1A"),
        (7, "loc_1A41"),
        (SWITCH_DEFAULT, "loc_1A4F"),
    )


    label("loc_1930")

    MiniGame(0x11, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1A59")

    label("loc_1957")

    MiniGame(0x6, 0x1, 0x0, 0x0, 0x0, 0x0, 0xFFFFFF38, 0x0, 0xFFFFF768)
    Jump("loc_1A59")

    label("loc_197E")

    MiniGame(0x12, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1A59")

    label("loc_19A5")

    MiniGame(0xB, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1A59")

    label("loc_19CC")

    MiniGame(0xD, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1A59")

    label("loc_19F3")

    MiniGame(0xC, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1A59")

    label("loc_1A1A")

    MiniGame(0xE, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Jump("loc_1A59")

    label("loc_1A41")

    OP_50(0x4B, (scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_1A59")

    label("loc_1A4F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A59")

    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_1854")

    label("loc_1A68")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_7_184A end

    def Function_8_1A76(): pass

    label("Function_8_1A76")

    PlayBGM("ed7001", 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1A84")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F01")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "BTL_TEST_01 テスト\x01",         # 0
            "BTL_TEST_02 状態異常\x01",       # 1
            "BTL_TEST_03 屋外\x01",           # 2
            "BTL_TEST_04 俺専用\x01",         # 3
            "BTL_TEST_05 誰か専用\x01",       # 4
            "BTL_TEST_06 誰か専用2\x01",      # 5
            "BTL_MONSSET 相手選択\x01",       # 6
            "BTL_TEST_07 ラスボス\x01",       # 7
            "自 ロ&ラ VS ワ&ヴ ①\x01",       # 8
            "自 ロ&ラ VS ワ&ヴ ②\x01",       # 9
            "自 ロ&ラ VS エ&ヨ ①\x01",       # 10
            "自 ロ&ラ VS エ&ヨ ②\x01",       # 11
            "自 エ&ヨ VS ワ&ヴ\x01",          # 12
            "自 エ&ヨ VS 魔獣\x01",           # 13
            "自 イン  VS マフィア\x01",       # 14
            "キーアといっしょ\x01",           # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1C47"),
        (1, "loc_1C5C"),
        (2, "loc_1C71"),
        (3, "loc_1C86"),
        (4, "loc_1C9B"),
        (5, "loc_1CB0"),
        (6, "loc_1CC5"),
        (7, "loc_1CDA"),
        (8, "loc_1CEF"),
        (9, "loc_1D38"),
        (10, "loc_1D81"),
        (11, "loc_1DC7"),
        (12, "loc_1E10"),
        (13, "loc_1E53"),
        (14, "loc_1E96"),
        (15, "loc_1ED9"),
        (SWITCH_DEFAULT, "loc_1EF2"),
    )


    label("loc_1C47")

    Battle("BattleInfo_370", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EF2")

    label("loc_1C5C")

    Battle("BattleInfo_3B4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EF2")

    label("loc_1C71")

    Battle("BattleInfo_3F8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EF2")

    label("loc_1C86")

    Battle("BattleInfo_43C", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EF2")

    label("loc_1C9B")

    Battle("BattleInfo_480", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EF2")

    label("loc_1CB0")

    Battle("BattleInfo_4C4", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EF2")

    label("loc_1CC5")

    Battle("BattleInfo_508", 0x0, 0x0, 0x0, 0x1, 0xFF)
    Jump("loc_1EF2")

    label("loc_1CDA")

    Battle("BattleInfo_54C", 0x30200010, 0x0, 0x4, 0xA, 0xFF)
    Jump("loc_1EF2")

    label("loc_1CEF")

    ClearScenarioFlags(0x5C, 0)
    Sleep(1000)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1EF2")

    label("loc_1D38")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200001, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x190, 0x0)
    ClearScenarioFlags(0x5C, 0)
    Jump("loc_1EF2")

    label("loc_1D81")

    ClearScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1EF2")

    label("loc_1DC7")

    SetScenarioFlags(0x5C, 0)
    Battle(0xFFFFFFFF, 0x30200000, "", 0x30000000, 0x30000300, 0x0, 0x0, 0x30000600, 0x30000700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x190, 0x0)
    ClearScenarioFlags(0x5C, 0)
    Jump("loc_1EF2")

    label("loc_1E10")

    Battle(0xFFFFFFFF, 0x30200002, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30000400, 0x30002100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1EF2")

    label("loc_1E53")

    Battle(0xFFFFFFFF, 0x30200003, "", 0x30000600, 0x30000700, 0x0, 0x0, 0x30063700, 0x30063700, 0x30063700, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1EF2")

    label("loc_1E96")

    Battle(0xFFFFFFFF, 0x30200004, "", 0x30000500, 0x0, 0x0, 0x0, 0x30031900, 0x30031100, 0x30031100, 0x0, 0x0, 0x0, 0x0, 0x0, 0x1, 0x8)
    Jump("loc_1EF2")

    label("loc_1ED9")

    AddParty(0x52, 0xFF, 0xFF)
    Battle("BattleInfo_370", 0x0, 0x0, 0x0, 0x0, 0xFF)
    Jump("loc_1EF2")

    label("loc_1EF2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_1A84")

    label("loc_1F01")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_8_1A76 end

    def Function_9_1F0F(): pass

    label("Function_9_1F0F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1F19")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FB1")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "ＮＰＣ\x01",          # 0
            "戦闘キャラ\x01",      # 1
            "モンスター\x01",      # 2
            "キャンセル\x01",      # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F78"),
        (1, "loc_1F86"),
        (2, "loc_1F94"),
        (SWITCH_DEFAULT, "loc_1FA2"),
    )


    label("loc_1F78")

    NewScene("a0002", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F86")

    NewScene("a0001", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1F94")

    NewScene("a0003", 0, 0, 0)
    IdleLoop()
    Jump("loc_1FAC")

    label("loc_1FA2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1FAC")

    Jump("loc_1F19")

    label("loc_1FB1")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_9_1F0F end

    def Function_10_1FBF(): pass

    label("Function_10_1FBF")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_1FFF"),
        (1, "loc_200B"),
        (2, "loc_2017"),
        (3, "loc_2023"),
        (4, "loc_202F"),
        (5, "loc_203B"),
        (6, "loc_2047"),
        (SWITCH_DEFAULT, "loc_2053"),
    )


    label("loc_1FFF")

    OP_A0(0xFE, 1450, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_200B")

    OP_A0(0xFE, 1550, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_2017")

    OP_A0(0xFE, 1600, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_2023")

    OP_A0(0xFE, 1400, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_202F")

    OP_A0(0xFE, 1650, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_203B")

    OP_A0(0xFE, 1350, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_2047")

    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_2053")

    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_205F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2076")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_205F")

    label("loc_2076")

    Return()

    # Function_10_1FBF end

    def Function_11_2077(): pass

    label("Function_11_2077")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_20B7"),
        (1, "loc_20C3"),
        (2, "loc_20CF"),
        (3, "loc_20DB"),
        (4, "loc_20E7"),
        (5, "loc_20F3"),
        (6, "loc_20FF"),
        (SWITCH_DEFAULT, "loc_210B"),
    )


    label("loc_20B7")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_20C3")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_20CF")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_20DB")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_20E7")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_20F3")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_20FF")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_210B")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_2117")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_212E")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_2117")

    label("loc_212E")

    Return()

    # Function_11_2077 end

    def Function_12_212F(): pass

    label("Function_12_212F")

    TalkBegin(0xFF)

    #C0015
    ChrTalk(
        0x0,
        "おい\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_12_212F end

    def Function_13_2140(): pass

    label("Function_13_2140")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_217E")
    OP_9D(0xFE, 0x2BC, 0x0, 0x2AF8, 0x1F4, 0x3E8)
    OP_9D(0xFE, 0x12C0, 0x0, 0x2AF8, 0x1F4, 0x3E8)
    Jump("Function_13_2140")

    label("loc_217E")

    Return()

    # Function_13_2140 end

    def Function_14_217F(): pass

    label("Function_14_217F")

    TalkBegin(0xFE)
    PlayBGM("ed7001", 0)
    VolumeBGM(0x1E, 0x0)
    RemoveParty(0x8, 0xFF)
    AddParty(0x37, 0xFF, 0xFF)
    TurnDirection(0xFE, 0x102, 500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_BD(0x0, 0x63)"), scpexpr(EXPR_END)), "loc_2255")

    #C0016
    ChrTalk(
        0x101,
        (
            "#0000F#Nいや、気にしないでよ。\x02\x03",

            "手紙で色々と聞いて#4Rクロスベル#いるし……\x01",
            "それにどんなに変わったとしても#4Rクロスベル#\x01",
            "故郷#4Rクロスベル#は故郷#4Rクロスベル#だから。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_226F")

    label("loc_2255")


    #C0017
    ChrTalk(
        0x138,
        "#0000Fマリアベルです\x02",
    )

    CloseMessageWindow()

    label("loc_226F")


    #C0018
    ChrTalk(
        0xFE,
        "おやエリーさま\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x0,
        "パーティ０のメッセージ\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x1,
        "パーティ１のメッセージ\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        (
            "ノエルがサポートメンバーでいればメッセージでる？\x01",
            "トゲなしウィンドウなんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0xFE,
        (
            "#00Fでも先生#4Rせんせい#は先生先生……\x01",
            "レナさんの死#2Rし#を乗り越えて#12Rをのりこえて#\x01",
            "遊撃士としての道を歩き始めた。\x02\x03",

            "#10F決して立ち止まることなく\x01",
            "大切なものを守り続けてきた。\x02\x03",

            "王国軍に戻った今も\x01",
            "それは変わっていないと思う。\x02\x03",

            "#00Fエステル……\x01",
            "あんたは、どうしたいの？\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFF)
    Return()

    # Function_14_217F end

    def Function_15_2426(): pass

    label("Function_15_2426")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_244D")
    OP_94(0xFE, 0xFFFFD8F0, 0xFFFFD8F0, 0x2710, 0x2710, 0x157C)
    Jump("Function_15_2426")

    label("loc_244D")

    Return()

    # Function_15_2426 end

    def Function_16_244E(): pass

    label("Function_16_244E")

    OP_95(0x0, -2000, 0, 22400, 4000, 0x0)
    Return()

    # Function_16_244E end

    def Function_17_2463(): pass

    label("Function_17_2463")

    SetChrName("ショップちゃん")

    #A0023
    AnonymousTalk(
        0xFF,
        (
            scpstr(0x6),
            "どのお店？\x02",
        )
    )


    Menu(
        1,
        -1,
        -1,
        1,
        (
            "武器屋\x01",                      # 0
            "道具屋\x01",                      # 1
            "工房\x01",                        # 2
            "宿屋\x01",                        # 3
            "食材屋\x01",                      # 4
            "カジノ\x01",                      # 5
            "交換屋\x01",                      # 6
            "改造屋\x01",                      # 7
            "こっそりムービーテスト\x01",      # 8
            "こっそりメニューテスト\x01",      # 9
            "キャンセル\x01",                  # 10
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_60(0x1)
    OP_57(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_254A"),
        (1, "loc_2552"),
        (2, "loc_255A"),
        (3, "loc_2562"),
        (4, "loc_256A"),
        (5, "loc_2572"),
        (6, "loc_257A"),
        (7, "loc_2582"),
        (8, "loc_258A"),
        (9, "loc_25C2"),
        (SWITCH_DEFAULT, "loc_25CA"),
    )


    label("loc_254A")

    Call(0, 18)
    Jump("loc_25CF")

    label("loc_2552")

    Call(0, 19)
    Jump("loc_25CF")

    label("loc_255A")

    Call(0, 20)
    Jump("loc_25CF")

    label("loc_2562")

    Call(0, 21)
    Jump("loc_25CF")

    label("loc_256A")

    Call(0, 22)
    Jump("loc_25CF")

    label("loc_2572")

    Call(0, 23)
    Jump("loc_25CF")

    label("loc_257A")

    Call(0, 24)
    Jump("loc_25CF")

    label("loc_2582")

    Call(0, 25)
    Jump("loc_25CF")

    label("loc_258A")

    OP_C7(0x0, 0x10)
    PlayMovie(0x0, "ed7_op.pmf", 0x2, 0x1)
    Sleep(1000)
    OP_57(0x2)
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C7(0x1, 0x10)
    FadeToBright(10, 0)
    OP_0D()
    Jump("loc_25CF")

    label("loc_25C2")

    Call(0, 26)
    Jump("loc_25CF")

    label("loc_25CA")

    Jump("loc_25CF")

    label("loc_25CF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_17_2463 end

    def Function_18_25DA(): pass

    label("Function_18_25DA")

    OP_AF(0x0)
    Return()

    # Function_18_25DA end

    def Function_19_25DD(): pass

    label("Function_19_25DD")

    OP_AF(0x14)
    Return()

    # Function_19_25DD end

    def Function_20_25E0(): pass

    label("Function_20_25E0")

    OP_AF(0xA)
    Return()

    # Function_20_25E0 end

    def Function_21_25E3(): pass

    label("Function_21_25E3")

    OP_AF(0x32)
    Return()

    # Function_21_25E3 end

    def Function_22_25E6(): pass

    label("Function_22_25E6")

    OP_AF(0x81)
    Return()

    # Function_22_25E6 end

    def Function_23_25E9(): pass

    label("Function_23_25E9")

    OP_AF(0x3E)
    Return()

    # Function_23_25E9 end

    def Function_24_25EC(): pass

    label("Function_24_25EC")

    OP_AF(0xA4)
    Return()

    # Function_24_25EC end

    def Function_25_25EF(): pass

    label("Function_25_25EF")

    OP_AF(0xAE)
    Return()

    # Function_25_25EF end

    def Function_26_25F2(): pass

    label("Function_26_25F2")

    MenuCmd(0, 2)
    MenuCmd(1, 2, "項目01")
    MenuCmd(1, 2, "項目02")
    MenuCmd(1, 2, "項目03")
    MenuCmd(1, 2, "項目04")
    MenuCmd(1, 2, "項目05")
    MenuCmd(1, 2, "項目06")
    MenuCmd(1, 2, "項目07")
    MenuCmd(1, 2, "項目08")
    MenuCmd(1, 2, "項目09")
    MenuCmd(1, 2, "項目10")
    MenuCmd(1, 2, "項目11")
    MenuCmd(1, 2, "項目12")
    MenuCmd(1, 2, "項目13")
    MenuCmd(1, 2, "項目14")
    MenuCmd(1, 2, "項目15")
    MenuCmd(1, 2, "項目16")
    MenuCmd(3, 2, 0x1)
    MenuCmd(3, 2, 0x8)
    MenuCmd(3, 2, 0x5)
    MenuCmd(3, 2, 0xE)
    MenuCmd(3, 2, 0xF)
    MenuCmd(3, 2, 0x9)
    MenuCmd(2, 2, -1, -1, 1)
    MenuEnd(0x0)
    OP_60(0x2)
    Return()

    # Function_26_25F2 end

    def Function_27_26BC(): pass

    label("Function_27_26BC")

    EventBegin(0x1)

    #C0024
    ChrTalk(
        0x0,
        "#1001Fここなら何か釣れそうね。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        10,
        32,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    WaitChrThread(0x0, 1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_275D")
    MiniGame(0x6, 0x1, 0x4B834, 0xFFFFFFBA, 0x4BB4, 0x5A, 0xFFFFFF38, 0x0, 0xFFFFF768)
    OP_0D()
    EventEnd(0x1)
    Jump("loc_276E")

    label("loc_275D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_276E")
    EventEnd(0x1)

    label("loc_276E")

    Return()

    # Function_27_26BC end

    def Function_28_276F(): pass

    label("Function_28_276F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2779")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28BF")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "基本装備\x01",                # 0
            "魔法?クラフト\x01",           # 1
            "捜査手帳／戦闘手帳\x01",      # 2
            "レシピ手帳／料理\x01",        # 3
            "釣り\x01",                    # 4
            "改造関係\x01",                # 5
            "イベントアイテム\x01",        # 6
            "ＤＰセット\x01",              # 7
            "その他\x01",                  # 8
            "ランダムテスト\x01",          # 9
            "キャンセル\x01",              # 10
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2860"),
        (1, "loc_2868"),
        (2, "loc_2870"),
        (3, "loc_2878"),
        (4, "loc_2880"),
        (5, "loc_2888"),
        (6, "loc_2890"),
        (7, "loc_2898"),
        (8, "loc_28A0"),
        (9, "loc_28A8"),
        (SWITCH_DEFAULT, "loc_28B0"),
    )


    label("loc_2860")

    Call(0, 29)
    Jump("loc_28BA")

    label("loc_2868")

    Call(0, 30)
    Jump("loc_28BA")

    label("loc_2870")

    Call(0, 31)
    Jump("loc_28BA")

    label("loc_2878")

    Call(0, 32)
    Jump("loc_28BA")

    label("loc_2880")

    Call(0, 33)
    Jump("loc_28BA")

    label("loc_2888")

    Call(0, 34)
    Jump("loc_28BA")

    label("loc_2890")

    Call(0, 35)
    Jump("loc_28BA")

    label("loc_2898")

    Call(0, 36)
    Jump("loc_28BA")

    label("loc_28A0")

    Call(0, 37)
    Jump("loc_28BA")

    label("loc_28A8")

    Call(0, 38)
    Jump("loc_28BA")

    label("loc_28B0")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28BA")

    Jump("loc_2779")

    label("loc_28BF")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x1)
    Return()

    # Function_28_276F end

    def Function_29_28CD(): pass

    label("Function_29_28CD")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_28D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C31")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "序章基本装備(レベル 3)\x01",        # 0
            "１章基本装備(レベル 7)\x01",        # 1
            "２章基本装備(レベル16)\x01",        # 2
            "３章基本装備(レベル22)\x01",        # 3
            "４章基本装備(レベル29)\x01",        # 4
            "終章基本装備(レベル34)\x01",        # 5
            "ラスボス戦装備(レベル44)\x01",      # 6
            "キャンセル\x01",                    # 7
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29D4"),
        (1, "loc_2A01"),
        (2, "loc_2A2E"),
        (3, "loc_2A5B"),
        (4, "loc_2A88"),
        (5, "loc_2AB5"),
        (6, "loc_2AE2"),
        (SWITCH_DEFAULT, "loc_2C22"),
    )


    label("loc_29D4")

    Call(1, 46)
    SetChrName("")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "序章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2C2C")

    label("loc_2A01")

    Call(1, 49)
    SetChrName("")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "１章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2C2C")

    label("loc_2A2E")

    Call(1, 52)
    SetChrName("")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "２章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2C2C")

    label("loc_2A5B")

    Call(1, 55)
    SetChrName("")

    #A0029
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "３章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2C2C")

    label("loc_2A88")

    Call(1, 60)
    SetChrName("")

    #A0030
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "４章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2C2C")

    label("loc_2AB5")

    Call(1, 63)
    SetChrName("")

    #A0031
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "終章開始時の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2C2C")

    label("loc_2AE2")

    AddItemNumber(0x1F5, 5)
    AddItemNumber(0x1F5, 30)
    AddItemNumber(0x1F6, 10)
    AddItemNumber(0x1F9, 20)
    AddItemNumber(0x1FB, 5)
    AddItemNumber(0x1FC, 10)
    AddItemNumber(0x1FE, 2)
    AddItemNumber(0x200, 5)
    AddItemNumber(0x201, 30)
    AddItemNumber(0x203, 30)
    AddItemNumber(0x204, 30)
    AddItemNumber(0x205, 30)
    AddItemNumber(0x190, 20)
    AddItemNumber(0x192, 20)
    AddItemNumber(0x195, 20)
    AddItemNumber(0x1C8, 20)
    AddItemNumber(0x1C9, 20)
    OP_42(0x0, 0x51, 0x3)
    OP_42(0x0, 0x50, 0x4)
    OP_42(0x1, 0x49, 0x3)
    OP_42(0x1, 0x58, 0x4)
    OP_42(0x2, 0x42, 0x3)
    OP_42(0x2, 0x56, 0x4)
    OP_42(0x3, 0x4F, 0x3)
    OP_42(0x3, 0x57, 0x4)
    OP_42(0x0, 0x81, 0x0)
    OP_42(0x0, 0x6C, 0x2)
    OP_42(0x0, 0x99, 0x1)
    OP_42(0x0, 0xAA, 0x6)
    OP_42(0x0, 0x75, 0x4)
    OP_42(0x0, 0x66, 0x5)
    OP_42(0x0, 0x7E, 0x3)
    OP_42(0x1, 0xA2, 0x0)
    OP_42(0x1, 0x6C, 0x4)
    OP_42(0x1, 0xA1, 0x5)
    OP_42(0x1, 0xAE, 0x6)
    OP_42(0x1, 0xA0, 0x1)
    OP_42(0x1, 0x66, 0x2)
    OP_42(0x1, 0x78, 0x3)
    OP_42(0x2, 0x66, 0x0)
    OP_42(0x2, 0xA6, 0x3)
    OP_42(0x2, 0x98, 0x2)
    OP_42(0x2, 0x87, 0x1)
    OP_42(0x2, 0x97, 0x6)
    OP_42(0x2, 0xA5, 0x5)
    OP_42(0x2, 0xA3, 0x4)
    OP_42(0x3, 0x9B, 0x0)
    OP_42(0x3, 0x9C, 0x4)
    OP_42(0x3, 0x6C, 0x3)
    OP_42(0x3, 0x75, 0x1)
    OP_42(0x3, 0x93, 0x2)
    OP_42(0x3, 0xB0, 0x6)
    OP_42(0x3, 0x7E, 0x5)
    OP_42(0x6, 0x6B, 0x0)
    OP_42(0x7, 0x6B, 0x0)
    Call(1, 68)
    SetChrName("")

    #A0032
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ラスボス戦の装備です。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_2C2C")

    label("loc_2C22")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C2C")

    Jump("loc_28D7")

    label("loc_2C31")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_29_28CD end

    def Function_30_2C3F(): pass

    label("Function_30_2C3F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2C49")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30A4")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "オーブメント開放最小\x01",          # 0
            "オーブメント開放ＡＬＬ１\x01",      # 1
            "オーブメント開放ＡＬＬ２\x01",      # 2
            "全員魔法無し\x01",                  # 3
            "魔法コンプ４人分\x01",              # 4
            "全クオーツ入手\x01",                # 5
            "クラフト初期化\x01",                # 6
            "クラフトコンプ10人分\x01",          # 7
            "コンビ２取得\x01",                  # 8
            "キャンセル\x01",                    # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2D54"),
        (1, "loc_2DA8"),
        (2, "loc_2E0E"),
        (3, "loc_2E74"),
        (4, "loc_2EF4"),
        (5, "loc_2F86"),
        (6, "loc_2FBB"),
        (7, "loc_2FF0"),
        (8, "loc_3043"),
        (SWITCH_DEFAULT, "loc_3095"),
    )


    label("loc_2D54")

    Call(1, 29)
    OP_38(0x0, 0x80, 0x1)
    OP_38(0x1, 0x80, 0x1)
    OP_38(0x2, 0x80, 0x1)
    OP_38(0x3, 0x80, 0x1)
    OP_38(0x4, 0x80, 0x1)
    OP_38(0x5, 0x80, 0x1)
    OP_38(0x6, 0x80, 0x1)
    OP_38(0x7, 0x80, 0x1)
    OP_38(0x8, 0x80, 0x1)
    OP_38(0x9, 0x80, 0x1)
    SetChrName("")

    #A0033
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "中央のみ開いています。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_2DA8")

    Call(1, 29)
    OP_38(0x0, 0x7F, 0x1)
    OP_38(0x1, 0x7F, 0x1)
    OP_38(0x2, 0x7F, 0x1)
    OP_38(0x3, 0x7F, 0x1)
    OP_38(0x4, 0x7F, 0x1)
    OP_38(0x5, 0x7F, 0x1)
    OP_38(0x6, 0x7F, 0x1)
    OP_38(0x7, 0x7F, 0x1)
    OP_38(0x8, 0x7F, 0x1)
    OP_38(0x9, 0x7F, 0x1)
    SetChrName("")

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメント盤を全てレベル１にしました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_2E0E")

    Call(1, 29)
    OP_38(0x0, 0x7F, 0x2)
    OP_38(0x1, 0x7F, 0x2)
    OP_38(0x2, 0x7F, 0x2)
    OP_38(0x3, 0x7F, 0x2)
    OP_38(0x4, 0x7F, 0x2)
    OP_38(0x5, 0x7F, 0x2)
    OP_38(0x6, 0x7F, 0x2)
    OP_38(0x7, 0x7F, 0x2)
    OP_38(0x8, 0x7F, 0x2)
    OP_38(0x9, 0x7F, 0x2)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オーブメント盤を全てレベル２にしました。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_2E74")

    Call(1, 30)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての魔法を消去しました。\x01",
            "クオーツを装備しなおすと、\x01",
            "装備しているクオーツに合わせて再取得してしまいます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_2EF4")

    Call(1, 30)
    Call(1, 31)
    Call(1, 32)
    Call(1, 33)
    Call(1, 34)
    SetChrName("")

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての魔法を４人が取得しました。\x01",
            "クオーツを装備しなおすと、\x01",
            "装備しているクオーツに合わせて再取得してしまいます。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_2F86")

    Call(1, 86)
    SetChrName("")

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのクオーツを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_2FBB")

    Call(1, 35)
    SetChrName("")

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのクラフトを消去しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_2FF0")

    Call(1, 35)
    Call(1, 36)
    Call(1, 37)
    Call(1, 38)
    Call(1, 39)
    Call(1, 40)
    Call(1, 41)
    Call(1, 42)
    Call(1, 43)
    Call(1, 44)
    Call(1, 45)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのクラフトを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_3043")

    AddCraft(0x0, 0x154)
    AddCraft(0x1, 0x154)
    AddCraft(0x0, 0x155)
    AddCraft(0x2, 0x155)
    AddCraft(0x0, 0x156)
    AddCraft(0x3, 0x156)
    SetChrName("")

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのコンビクラフト２を入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_309F")

    label("loc_3095")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_309F")

    Jump("loc_2C49")

    label("loc_30A4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_30_2C3F end

    def Function_31_30B2(): pass

    label("Function_31_30B2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_30BC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3418")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "捜査手帳情報初期化\x01",          # 0
            "捜査手帳ＡＬＬコンプ\x01",        # 1
            "捜査手帳メインコンプ\x01",        # 2
            "捜査手帳サブコンプ\x01",          # 3
            "捜査手帳サブ受付のみ\x01",        # 4
            "捜査手帳サブ失敗\x01",            # 5
            "戦闘手帳情報初期化\x01",          # 6
            "戦闘手帳コンプ(全魔獣)\x01",      # 7
            "キャンセル\x01",                  # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_31BC"),
        (1, "loc_31F0"),
        (2, "loc_322E"),
        (3, "loc_3275"),
        (4, "loc_32BA"),
        (5, "loc_32FE"),
        (6, "loc_3347"),
        (7, "loc_33A5"),
        (SWITCH_DEFAULT, "loc_3409"),
    )


    label("loc_31BC")

    Call(1, 69)
    Call(1, 70)
    SetChrName("")

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳を初期化しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3413")

    label("loc_31F0")

    Call(1, 71)
    Call(1, 72)
    SetChrName("")

    #A0043
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳を全てコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3413")

    label("loc_322E")

    Call(1, 71)
    SetChrName("")

    #A0044
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳のメインクエストをコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3413")

    label("loc_3275")

    Call(1, 72)
    SetChrName("")

    #A0045
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳のサブクエストをコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3413")

    label("loc_32BA")

    Call(1, 70)
    Call(1, 73)
    SetChrName("")

    #A0046
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳のサブクエストを受付だけしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3413")

    label("loc_32FE")

    Call(1, 70)
    Call(1, 73)
    Call(1, 74)
    SetChrName("")

    #A0047
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "捜査手帳のサブクエストを全て失敗にしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3413")

    label("loc_3347")

    SetChrName("")

    #A0048
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "戦闘手帳の初期化は、\x01",
            "[F5]メニューの6ページの MonsNote を使用してください。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3413")

    label("loc_33A5")

    SetChrName("")

    #A0049
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "戦闘手帳のコンプリートは、\x01",
            "[F5]メニューの6ページの MonsNote を使用してください。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3413")

    label("loc_3409")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3413")

    Jump("loc_30BC")

    label("loc_3418")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_31_30B2 end

    def Function_32_3426(): pass

    label("Function_32_3426")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3430")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_376E")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "レシピ情報初期化\x01",                    # 0
            "レシピ全てコンプリート\x01",              # 1
            "レシピ成功料理のみコンプリート\x01",      # 2
            "レシピ大成功のみコンプリート\x01",        # 3
            "レシピ予想外のみコンプリート\x01",        # 4
            "食材いっぱい入手(50個)\x01",              # 5
            "全料理アイテム入手(10個)\x01",            # 6
            "全予想外料理アイテム入手(1個)\x01",       # 7
            "キャンセル\x01",                          # 8
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_355F"),
        (1, "loc_3594"),
        (2, "loc_35DF"),
        (3, "loc_3626"),
        (4, "loc_366F"),
        (5, "loc_36B8"),
        (6, "loc_36F0"),
        (7, "loc_3728"),
        (SWITCH_DEFAULT, "loc_375F"),
    )


    label("loc_355F")

    OP_B0(0x0)
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳を全て消去しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3769")

    label("loc_3594")

    Call(1, 75)
    Call(1, 76)
    Call(1, 77)
    SetChrName("")

    #A0051
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳の全ての料理をコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3769")

    label("loc_35DF")

    Call(1, 75)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳の「成功料理」をコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3769")

    label("loc_3626")

    Call(1, 76)
    SetChrName("")

    #A0053
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳の「大成功料理」をコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3769")

    label("loc_366F")

    Call(1, 77)
    SetChrName("")

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レシピ手帳の「予想外料理」をコンプリートしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3769")

    label("loc_36B8")

    Call(1, 78)
    SetChrName("")

    #A0055
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての食材を 50ずつ入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3769")

    label("loc_36F0")

    Call(1, 79)
    SetChrName("")

    #A0056
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての料理を 50ずつ入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3769")

    label("loc_3728")

    Call(1, 80)
    SetChrName("")

    #A0057
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "予想外料理を 1ずつ入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_3769")

    label("loc_375F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3769")

    Jump("loc_3430")

    label("loc_376E")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_32_3426 end

    def Function_33_377C(): pass

    label("Function_33_377C")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_3786")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_41D4")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "釣り情報初期化\x01",            # 0
            "釣り情報コンプ(全魚)\x01",      # 1
            "釣り竿全部入手\x01",            # 2
            "釣りエサ全部入手\x01",          # 3
            "釣り魚全部入手\x01",            # 4
            "釣り魚個別入手\x01",            # 5
            "釣り魚個別入手×５\x01",        # 6
            "釣り魚全破棄\x01",              # 7
            "オロショチェック\x01",          # 8
            "キャンセル\x01",                # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_387F"),
        (1, "loc_38DD"),
        (2, "loc_3941"),
        (3, "loc_3984"),
        (4, "loc_3A23"),
        (5, "loc_3AC3"),
        (6, "loc_3DC4"),
        (7, "loc_40C5"),
        (8, "loc_4142"),
        (SWITCH_DEFAULT, "loc_41C5"),
    )


    label("loc_387F")

    SetChrName("")

    #A0058
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣り手帳の初期化は、\x01",
            "[F5]メニューの6ページの FishNote を使用してください。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_41CF")

    label("loc_38DD")

    SetChrName("")

    #A0059
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣り手帳のコンプリートは、\x01",
            "[F5]メニューの6ページの FishNote を使用してください。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_41CF")

    label("loc_3941")

    AddItemNumber(0x32, 1)
    AddItemNumber(0x33, 1)
    AddItemNumber(0x34, 1)
    AddItemNumber(0x35, 1)
    AddItemNumber(0x37, 1)
    SetChrName("")

    #A0060
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての釣竿を入手した。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_41CF")

    label("loc_3984")

    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    AddItemNumber(0x188, 10)
    AddItemNumber(0x189, 10)
    AddItemNumber(0x18A, 10)
    AddItemNumber(0x18B, 10)
    AddItemNumber(0x18C, 10)
    AddItemNumber(0x18D, 10)
    AddItemNumber(0x15E, 10)
    AddItemNumber(0x162, 10)
    AddItemNumber(0x165, 10)
    AddItemNumber(0x167, 10)
    AddItemNumber(0x168, 10)
    AddItemNumber(0x169, 10)
    AddItemNumber(0x16C, 10)
    AddItemNumber(0x16D, 10)
    SetChrName("")

    #A0061
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのエサを入手した。\x01",
            "エサとして使用できる魚も入手します。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_41CF")

    label("loc_3A23")

    AddItemNumber(0x15E, 10)
    AddItemNumber(0x15F, 10)
    AddItemNumber(0x160, 10)
    AddItemNumber(0x161, 10)
    AddItemNumber(0x162, 10)
    AddItemNumber(0x163, 10)
    AddItemNumber(0x164, 10)
    AddItemNumber(0x165, 10)
    AddItemNumber(0x166, 10)
    AddItemNumber(0x167, 10)
    AddItemNumber(0x168, 10)
    AddItemNumber(0x169, 10)
    AddItemNumber(0x16A, 10)
    AddItemNumber(0x16B, 10)
    AddItemNumber(0x16C, 10)
    AddItemNumber(0x16D, 10)
    AddItemNumber(0x16E, 10)
    AddItemNumber(0x16F, 10)
    AddItemNumber(0x170, 10)
    AddItemNumber(0x171, 10)
    AddItemNumber(0x172, 10)
    AddItemNumber(0x173, 10)
    AddItemNumber(0x174, 10)
    AddItemNumber(0x175, 10)
    SetChrName("")

    #A0062
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての魚を入手した。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_41CF")

    label("loc_3AC3")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "スノーシュラブ\x01",      # 0
            "アルモリカブナ\x01",      # 1
            "オロショ\x01",            # 2
            "ロック\x01",              # 3
            "カルプ\x01",              # 4
            "レイニー\x01",            # 5
            "エーゼル\x01",            # 6
            "カサギン\x01",            # 7
            "レインボウ\x01",          # 8
            "トラード\x01",            # 9
            "サモーナ\x01",            # 10
            "イール\x01",              # 11
            "【→次へ】\x01",          # 12
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3BB0"),
        (1, "loc_3BBA"),
        (2, "loc_3BC4"),
        (3, "loc_3BCE"),
        (4, "loc_3BD8"),
        (5, "loc_3BE2"),
        (6, "loc_3BEC"),
        (7, "loc_3BF6"),
        (8, "loc_3C00"),
        (9, "loc_3C0A"),
        (10, "loc_3C14"),
        (11, "loc_3C1E"),
        (12, "loc_3C28"),
        (SWITCH_DEFAULT, "loc_3DB5"),
    )


    label("loc_3BB0")

    AddItemNumber(0x15E, 1)
    Jump("loc_3DB5")

    label("loc_3BBA")

    AddItemNumber(0x15F, 1)
    Jump("loc_3DB5")

    label("loc_3BC4")

    AddItemNumber(0x160, 1)
    Jump("loc_3DB5")

    label("loc_3BCE")

    AddItemNumber(0x161, 1)
    Jump("loc_3DB5")

    label("loc_3BD8")

    AddItemNumber(0x162, 1)
    Jump("loc_3DB5")

    label("loc_3BE2")

    AddItemNumber(0x163, 1)
    Jump("loc_3DB5")

    label("loc_3BEC")

    AddItemNumber(0x164, 1)
    Jump("loc_3DB5")

    label("loc_3BF6")

    AddItemNumber(0x165, 1)
    Jump("loc_3DB5")

    label("loc_3C00")

    AddItemNumber(0x166, 1)
    Jump("loc_3DB5")

    label("loc_3C0A")

    AddItemNumber(0x167, 1)
    Jump("loc_3DB5")

    label("loc_3C14")

    AddItemNumber(0x168, 1)
    Jump("loc_3DB5")

    label("loc_3C1E")

    AddItemNumber(0x169, 1)
    Jump("loc_3DB5")

    label("loc_3C28")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "パールグラス\x01",          # 0
            "グラトンバス\x01",          # 1
            "バイパーヘッド\x01",        # 2
            "パイソンヘッド\x01",        # 3
            "タイタン\x01",              # 4
            "クインシザー\x01",          # 5
            "エレキイール\x01",          # 6
            "デモンタイタン\x01",        # 7
            "アークシュラブ\x01",        # 8
            "ゴルドサモーナ\x01",        # 9
            "ノーブルカルプ\x01",        # 10
            "サーペントヘッド\x01",      # 11
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3D38"),
        (1, "loc_3D42"),
        (2, "loc_3D4C"),
        (3, "loc_3D56"),
        (4, "loc_3D60"),
        (5, "loc_3D6A"),
        (6, "loc_3D74"),
        (7, "loc_3D7E"),
        (8, "loc_3D88"),
        (9, "loc_3D92"),
        (10, "loc_3D9C"),
        (11, "loc_3DA6"),
        (SWITCH_DEFAULT, "loc_3DB0"),
    )


    label("loc_3D38")

    AddItemNumber(0x16A, 1)
    Jump("loc_3DB0")

    label("loc_3D42")

    AddItemNumber(0x16B, 1)
    Jump("loc_3DB0")

    label("loc_3D4C")

    AddItemNumber(0x16C, 1)
    Jump("loc_3DB0")

    label("loc_3D56")

    AddItemNumber(0x16D, 1)
    Jump("loc_3DB0")

    label("loc_3D60")

    AddItemNumber(0x16E, 1)
    Jump("loc_3DB0")

    label("loc_3D6A")

    AddItemNumber(0x16F, 1)
    Jump("loc_3DB0")

    label("loc_3D74")

    AddItemNumber(0x170, 1)
    Jump("loc_3DB0")

    label("loc_3D7E")

    AddItemNumber(0x171, 1)
    Jump("loc_3DB0")

    label("loc_3D88")

    AddItemNumber(0x172, 1)
    Jump("loc_3DB0")

    label("loc_3D92")

    AddItemNumber(0x173, 1)
    Jump("loc_3DB0")

    label("loc_3D9C")

    AddItemNumber(0x174, 1)
    Jump("loc_3DB0")

    label("loc_3DA6")

    AddItemNumber(0x175, 1)
    Jump("loc_3DB0")

    label("loc_3DB0")

    Jump("loc_3DB5")

    label("loc_3DB5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41CF")

    label("loc_3DC4")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "スノーシュラブ\x01",      # 0
            "アルモリカブナ\x01",      # 1
            "オロショ\x01",            # 2
            "ロック\x01",              # 3
            "カルプ\x01",              # 4
            "レイニー\x01",            # 5
            "エーゼル\x01",            # 6
            "カサギン\x01",            # 7
            "レインボウ\x01",          # 8
            "トラード\x01",            # 9
            "サモーナ\x01",            # 10
            "イール\x01",              # 11
            "【→次へ】\x01",          # 12
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_3EB1"),
        (1, "loc_3EBB"),
        (2, "loc_3EC5"),
        (3, "loc_3ECF"),
        (4, "loc_3ED9"),
        (5, "loc_3EE3"),
        (6, "loc_3EED"),
        (7, "loc_3EF7"),
        (8, "loc_3F01"),
        (9, "loc_3F0B"),
        (10, "loc_3F15"),
        (11, "loc_3F1F"),
        (12, "loc_3F29"),
        (SWITCH_DEFAULT, "loc_40B6"),
    )


    label("loc_3EB1")

    AddItemNumber(0x15E, 5)
    Jump("loc_40B6")

    label("loc_3EBB")

    AddItemNumber(0x15F, 5)
    Jump("loc_40B6")

    label("loc_3EC5")

    AddItemNumber(0x160, 5)
    Jump("loc_40B6")

    label("loc_3ECF")

    AddItemNumber(0x161, 5)
    Jump("loc_40B6")

    label("loc_3ED9")

    AddItemNumber(0x162, 5)
    Jump("loc_40B6")

    label("loc_3EE3")

    AddItemNumber(0x163, 5)
    Jump("loc_40B6")

    label("loc_3EED")

    AddItemNumber(0x164, 5)
    Jump("loc_40B6")

    label("loc_3EF7")

    AddItemNumber(0x165, 5)
    Jump("loc_40B6")

    label("loc_3F01")

    AddItemNumber(0x166, 5)
    Jump("loc_40B6")

    label("loc_3F0B")

    AddItemNumber(0x167, 5)
    Jump("loc_40B6")

    label("loc_3F15")

    AddItemNumber(0x168, 5)
    Jump("loc_40B6")

    label("loc_3F1F")

    AddItemNumber(0x169, 5)
    Jump("loc_40B6")

    label("loc_3F29")

    RunExpression(0x5, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "パールグラス\x01",          # 0
            "グラトンバス\x01",          # 1
            "バイパーヘッド\x01",        # 2
            "パイソンヘッド\x01",        # 3
            "タイタン\x01",              # 4
            "クインシザー\x01",          # 5
            "エレキイール\x01",          # 6
            "デモンタイタン\x01",        # 7
            "アークシュラブ\x01",        # 8
            "ゴルドサモーナ\x01",        # 9
            "ノーブルカルプ\x01",        # 10
            "サーペントヘッド\x01",      # 11
        )
    )

    MenuEnd(0x5)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x5), scpexpr(EXPR_END)),
        (0, "loc_4039"),
        (1, "loc_4043"),
        (2, "loc_404D"),
        (3, "loc_4057"),
        (4, "loc_4061"),
        (5, "loc_406B"),
        (6, "loc_4075"),
        (7, "loc_407F"),
        (8, "loc_4089"),
        (9, "loc_4093"),
        (10, "loc_409D"),
        (11, "loc_40A7"),
        (SWITCH_DEFAULT, "loc_40B1"),
    )


    label("loc_4039")

    AddItemNumber(0x16A, 5)
    Jump("loc_40B1")

    label("loc_4043")

    AddItemNumber(0x16B, 5)
    Jump("loc_40B1")

    label("loc_404D")

    AddItemNumber(0x16C, 5)
    Jump("loc_40B1")

    label("loc_4057")

    AddItemNumber(0x16D, 5)
    Jump("loc_40B1")

    label("loc_4061")

    AddItemNumber(0x16E, 5)
    Jump("loc_40B1")

    label("loc_406B")

    AddItemNumber(0x16F, 5)
    Jump("loc_40B1")

    label("loc_4075")

    AddItemNumber(0x170, 5)
    Jump("loc_40B1")

    label("loc_407F")

    AddItemNumber(0x171, 5)
    Jump("loc_40B1")

    label("loc_4089")

    AddItemNumber(0x172, 5)
    Jump("loc_40B1")

    label("loc_4093")

    AddItemNumber(0x173, 5)
    Jump("loc_40B1")

    label("loc_409D")

    AddItemNumber(0x174, 5)
    Jump("loc_40B1")

    label("loc_40A7")

    AddItemNumber(0x175, 5)
    Jump("loc_40B1")

    label("loc_40B1")

    Jump("loc_40B6")

    label("loc_40B6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_41CF")

    label("loc_40C5")

    SubItemNumber(0x15E, 1)
    SubItemNumber(0x15F, 1)
    SubItemNumber(0x160, 1)
    SubItemNumber(0x161, 1)
    SubItemNumber(0x162, 1)
    SubItemNumber(0x163, 1)
    SubItemNumber(0x164, 1)
    SubItemNumber(0x165, 1)
    SubItemNumber(0x166, 1)
    SubItemNumber(0x167, 1)
    SubItemNumber(0x168, 1)
    SubItemNumber(0x169, 1)
    SubItemNumber(0x16A, 1)
    SubItemNumber(0x16B, 1)
    SubItemNumber(0x16C, 1)
    SubItemNumber(0x16D, 1)
    SubItemNumber(0x16E, 1)
    SubItemNumber(0x16F, 1)
    SubItemNumber(0x170, 1)
    SubItemNumber(0x171, 1)
    SubItemNumber(0x172, 1)
    SubItemNumber(0x173, 1)
    SubItemNumber(0x174, 1)
    SubItemNumber(0x175, 1)
    Jump("loc_41CF")

    label("loc_4142")

    Jc((scpexpr(EXPR_EXEC_OP, "MiniGame(0x15, 0x2, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_419D")
    SetChrName("")

    #A0063
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オロショ１回以上釣った。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_41C0")

    label("loc_419D")

    SetChrName("")

    #A0064
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "オロショ釣ってない。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_41C0")

    Jump("loc_41CF")

    label("loc_41C5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41CF")

    Jump("loc_3786")

    label("loc_41D4")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_33_377C end

    def Function_34_41E2(): pass

    label("Function_34_41E2")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41EC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_42A7")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "Ｕマテリアル\x01",          # 0
            "デヴァインクロス\x01",      # 1
            "ゼムリアストーン\x01",      # 2
            "Ｔマテリアル\x01",          # 3
            "キャンセル\x01",            # 4
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4270"),
        (1, "loc_427A"),
        (2, "loc_4284"),
        (3, "loc_428E"),
        (SWITCH_DEFAULT, "loc_4298"),
    )


    label("loc_4270")

    AddItemNumber(0x38E, 10)
    Jump("loc_42A2")

    label("loc_427A")

    AddItemNumber(0x395, 10)
    Jump("loc_42A2")

    label("loc_4284")

    AddItemNumber(0x396, 10)
    Jump("loc_42A2")

    label("loc_428E")

    AddItemNumber(0x397, 10)
    Jump("loc_42A2")

    label("loc_4298")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42A2")

    Jump("loc_41EC")

    label("loc_42A7")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_34_41E2 end

    def Function_35_42B5(): pass

    label("Function_35_42B5")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_42BF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4517")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "研究棟認証カード\x01",        # 0
            "自室家具一式\x01",            # 1
            "小説全巻\x01",                # 2
            "小説?１巻抜き\x01",           # 3
            "自治州の地図\x01",            # 4
            "クロスベル市の地図\x01",      # 5
            "街区ジャンプＯＮ\x01",        # 6
            "街区ジャンプＯＦＦ\x01",      # 7
            "GAMESTART_ON\x01",            # 8
            "キャンセル\x01",              # 9
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_43AB"),
        (1, "loc_43B5"),
        (2, "loc_43E2"),
        (3, "loc_442D"),
        (4, "loc_4478"),
        (5, "loc_4482"),
        (6, "loc_44AA"),
        (7, "loc_44B5"),
        (8, "loc_44C0"),
        (SWITCH_DEFAULT, "loc_44C8"),
    )


    label("loc_43AB")

    AddItemNumber(0x335, 1)
    Jump("loc_44D2")

    label("loc_43B5")

    AddItemNumber(0x350, 1)
    AddItemNumber(0x351, 1)
    AddItemNumber(0x352, 1)
    AddItemNumber(0x353, 1)
    AddItemNumber(0x354, 1)
    AddItemNumber(0x355, 1)
    AddItemNumber(0x356, 1)
    AddItemNumber(0x357, 1)
    Jump("loc_44D2")

    label("loc_43E2")

    AddItemNumber(0x2C6, 1)
    AddItemNumber(0x2C7, 1)
    AddItemNumber(0x2C8, 1)
    AddItemNumber(0x2C9, 1)
    AddItemNumber(0x2CA, 1)
    AddItemNumber(0x2CB, 1)
    AddItemNumber(0x2CC, 1)
    AddItemNumber(0x2CD, 1)
    AddItemNumber(0x2CE, 1)
    AddItemNumber(0x2CF, 1)
    AddItemNumber(0x2D0, 1)
    AddItemNumber(0x2D1, 1)
    AddItemNumber(0x2D2, 1)
    AddItemNumber(0x2D3, 1)
    Jump("loc_44D2")

    label("loc_442D")

    SubItemNumber(0x2C6, 99)
    AddItemNumber(0x2C7, 1)
    AddItemNumber(0x2C8, 1)
    AddItemNumber(0x2C9, 1)
    AddItemNumber(0x2CA, 1)
    AddItemNumber(0x2CB, 1)
    AddItemNumber(0x2CC, 1)
    AddItemNumber(0x2CD, 1)
    AddItemNumber(0x2CE, 1)
    AddItemNumber(0x2CF, 1)
    AddItemNumber(0x2D0, 1)
    AddItemNumber(0x2D1, 1)
    AddItemNumber(0x2D2, 1)
    AddItemNumber(0x2D3, 1)
    Jump("loc_44D2")

    label("loc_4478")

    AddItemNumber(0x5, 1)
    Jump("loc_44D2")

    label("loc_4482")

    SetChrName("")

    #A0065
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "そんな物はないです。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_44D2")

    label("loc_44AA")

    OP_C7(0x0, 0x1000)
    Jump("loc_44D2")

    label("loc_44B5")

    OP_C7(0x1, 0x1000)
    Jump("loc_44D2")

    label("loc_44C0")

    SetScenarioFlags(0x5A, 0)
    Jump("loc_44D2")

    label("loc_44C8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_44D2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4512")
    SetChrName("")

    #A0066
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "アイテムを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_4512")

    Jump("loc_42BF")

    label("loc_4517")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_35_42B5 end

    def Function_36_4525(): pass

    label("Function_36_4525")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_452F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_474F")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "ＤＰ　０\x01",          # 0
            "ＤＰ　１５\x01",        # 1
            "ＤＰ　３０\x01",        # 2
            "ＤＰ　５５\x01",        # 3
            "ＤＰ　７０\x01",        # 4
            "ＤＰ　９０\x01",        # 5
            "ＤＰ　１１０\x01",      # 6
            "ＤＰ　１３０\x01",      # 7
            "ＤＰ　１５０\x01",      # 8
            "ＤＰ　１９５\x01",      # 9
            "ＤＰ　２２４\x01",      # 10
            "ＤＰ　２６５\x01",      # 11
            "ＤＰ　２９４\x01",      # 12
            "ＤＰ　３２４\x01",      # 13
            "ＤＰ　３８０\x01",      # 14
            "キャンセル\x01",        # 15
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_466E"),
        (1, "loc_467C"),
        (2, "loc_468A"),
        (3, "loc_4698"),
        (4, "loc_46A6"),
        (5, "loc_46B4"),
        (6, "loc_46C2"),
        (7, "loc_46D0"),
        (8, "loc_46DE"),
        (9, "loc_46EC"),
        (10, "loc_46FA"),
        (11, "loc_4708"),
        (12, "loc_4716"),
        (13, "loc_4724"),
        (14, "loc_4732"),
        (SWITCH_DEFAULT, "loc_4740"),
    )


    label("loc_466E")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_467C")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_468A")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_4698")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x37), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_46A6")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x46), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_46B4")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_46C2")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_46D0")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x82), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_46DE")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x96), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_46EC")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_46FA")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0xE0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_4708")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x109), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_4716")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x126), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_4724")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x144), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_4732")

    OP_50(0x14, (scpexpr(EXPR_PUSH_LONG, 0x17C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_474A")

    label("loc_4740")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_474A")

    Jump("loc_452F")

    label("loc_474F")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_36_4525 end

    def Function_37_475D(): pass

    label("Function_37_475D")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4767")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4BD8")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "全アイテム消去\x01",          # 0
            "基本アイテム入手\x01",        # 1
            "全装備品入手\x01",            # 2
            "全アクセサリ入手\x01",        # 3
            "全消費アイテム入手\x01",      # 4
            "セピス大量入手\x01",          # 5
            "セピスを０に\x01",            # 6
            "クオーツ大量入手\x01",        # 7
            "全員瀕死\x01",                # 8
            "実績全部初期化\x01",          # 9
            "実績全部入手\x01",            # 10
            "クロスベル全部\x01",          # 11
            "キャンセル\x01",              # 12
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_488B"),
        (1, "loc_48C6"),
        (2, "loc_4946"),
        (3, "loc_4989"),
        (4, "loc_49C2"),
        (5, "loc_4A05"),
        (6, "loc_4A3F"),
        (7, "loc_4A73"),
        (8, "loc_4AA8"),
        (9, "loc_4B08"),
        (11, "loc_4B35"),
        (SWITCH_DEFAULT, "loc_4BC9"),
    )


    label("loc_488B")

    SubItemNumber(0x270F, 99)
    SetChrName("")

    #A0067
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての所持アイテムを削除しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_48C6")

    AddItemNumber(0x1, 1)
    AddItemNumber(0x2, 1)
    AddItemNumber(0x3, 1)
    AddItemNumber(0x4, 1)
    AddItemNumber(0x5, 1)
    AddItemNumber(0x1F4, 10)
    AddItemNumber(0x1F5, 10)
    AddItemNumber(0x1F6, 10)
    AddItemNumber(0x1F8, 10)
    AddItemNumber(0x1F9, 10)
    AddItemNumber(0x1FB, 10)
    AddItemNumber(0x1FC, 10)
    AddItemNumber(0x20B, 10)
    AddItemNumber(0x32, 10)
    AddItemNumber(0x186, 10)
    AddItemNumber(0x187, 10)
    SetChrName("")

    #A0068
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "基本アイテムを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4946")

    Call(1, 81)
    Call(1, 82)
    Call(1, 83)
    SetChrName("")

    #A0069
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての装備品(武器防具)を入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4989")

    Call(1, 84)
    SetChrName("")

    #A0070
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのアクセサリーを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_49C2")

    Call(1, 85)
    SetChrName("")

    #A0071
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全ての消費アイテム(薬、道具)を入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4A05")

    AddSepith(0xFF, 5000)
    SetChrName("")

    #A0072
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのセピスを大量に入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4A3F")

    SubSepith(0xFF, 9999)
    SetChrName("")

    #A0073
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのセピスを消去しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4A73")

    Call(1, 86)
    SetChrName("")

    #A0074
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全てのクオーツを入手しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4AA8")

    OP_32(0x0, 0x2, 0x1)
    OP_32(0x1, 0x2, 0x1)
    OP_32(0x2, 0x2, 0x1)
    OP_32(0x3, 0x2, 0x1)
    OP_32(0x4, 0x2, 0x1)
    OP_32(0x5, 0x2, 0x1)
    OP_32(0x6, 0x2, 0x1)
    OP_32(0x7, 0x2, 0x1)
    OP_32(0x8, 0x2, 0x1)
    OP_32(0x9, 0x2, 0x1)
    SetChrName("")

    #A0075
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "全員のＨＰを１にしました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4B08")

    OP_DE(0x0, 0x0)
    SetChrName("")

    #A0076
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "実績を初期化しました。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4B35")

    SetScenarioFlags(0xF8, 0)
    SetScenarioFlags(0xF8, 1)
    SetScenarioFlags(0xF8, 2)
    SetScenarioFlags(0xF8, 3)
    SetScenarioFlags(0xF8, 4)
    SetScenarioFlags(0xF8, 5)
    SetScenarioFlags(0xF8, 6)
    SetScenarioFlags(0xF8, 7)
    SetScenarioFlags(0xF9, 0)
    SetScenarioFlags(0xF9, 1)
    SetScenarioFlags(0xF9, 2)
    SetScenarioFlags(0xF9, 3)
    SetScenarioFlags(0xF9, 4)
    SetScenarioFlags(0xF9, 5)
    SetScenarioFlags(0xF9, 6)
    SetScenarioFlags(0xF9, 7)
    SetScenarioFlags(0xFA, 0)
    SetScenarioFlags(0xFA, 1)
    SetScenarioFlags(0xFA, 2)
    SetScenarioFlags(0xFA, 3)
    SetScenarioFlags(0xFA, 4)
    SetScenarioFlags(0xFA, 5)
    SetScenarioFlags(0xFA, 6)
    SetScenarioFlags(0xFA, 7)
    SetScenarioFlags(0xFB, 0)
    SetScenarioFlags(0xFB, 1)
    SetScenarioFlags(0xFB, 2)
    SetScenarioFlags(0xFB, 3)
    SetScenarioFlags(0xFB, 4)
    SetScenarioFlags(0xFB, 5)
    SetScenarioFlags(0xFB, 6)
    SetScenarioFlags(0xFB, 7)
    SetChrName("")

    #A0077
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "クロスベルジャンプ使用できます。\x01\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    Jump("loc_4BD3")

    label("loc_4BC9")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BD3")

    Jump("loc_4767")

    label("loc_4BD8")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_37_475D end

    def Function_38_4BE6(): pass

    label("Function_38_4BE6")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4BF0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_4C66")

    Menu(
        2,
        -1,
        -1,
        1,
        (
            "波音ループ再生\x01",      # 0
            "波音停止\x01",            # 1
            "キャンセル\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_4C44"),
        (1, "loc_4C4F"),
        (SWITCH_DEFAULT, "loc_4C57"),
    )


    label("loc_4C44")

    Sound(479, 1, 100, 0)
    Jump("loc_4C61")

    label("loc_4C4F")

    OP_24(0x1DF)
    Jump("loc_4C61")

    label("loc_4C57")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_4C61")

    Jump("loc_4BF0")

    label("loc_4C66")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_60(0x2)
    Return()

    # Function_38_4BE6 end

    SaveToFile()

Try(main)
