from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r3070.bin",                # FileName
        "r3070",                    # MapName
        "r3070",                    # Location
        0x0065,                     # MapIndex
        "ed7203",
        0x00000000,                 # Flags
        ("r3070", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x17,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 101, 0, 0, 0, 1],
    )

    BuildStringList((
        "r3070",                  # 0
        "猟兵",                   # 1
        "猟兵",                   # 2
        "猟兵",                   # 3
        "猟兵",                   # 4
        "猟兵",                   # 5
        "猟兵",                   # 6
        "猟兵",                   # 7
        "クーガー",               # 8
        "クーガー",               # 9
        "クーガー",               # 10
        "クーガー",               # 11
        "ツァオ",                 # 12
        "ラウ",                   # 13
        "黒月構成員",             # 14
        "黒月構成員",             # 15
        "黒月構成員",             # 16
        "黒月構成員",             # 17
        "黒月構成員",             # 18
        "黒月構成員",             # 19
        "黒月構成員",             # 20
        "SE制御",                 # 21
        "br3000",                 # 22
        "br3000",                 # 23
        "br3000",                 # 24
        "br3000",                 # 25
        "アルモリカ古道方面",     # 26
        "太陽の砦方面",           # 27
    ))

    ATBonus("ATBonus_5E0", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_600", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_475F", 15,  0,   0,   15,  5,   5,   2)
    Sepith("Sepith_4757", 8,   8,   8,   8,   8,   8,   8)
    Sepith("Sepith_4767", 10,  10,  10,  10,  3,   3,   3)

    MonsterBattlePostion("MonsterBattlePostion_640", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_644", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_648", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_64C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_650", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_654", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_658", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_65C", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_6A0", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_6A4", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_6A8", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_6AC", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_6B0", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_6B4", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_6B8", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_6BC", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_620", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_624", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_628", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_62C", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_630", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_634", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_638", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_63C", 2, 13, 180)

    # monster count: 12

    BattleInfo(
        "BattleInfo_6C0", 0x0000, 73, 6, 45, 10, 1, 40, 0, "br3000", "Sepith_475F", 75, 25, 0, 0,
        (
            ("ms71600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_640", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
            ("ms71600.dat", "ms71600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_730", 0x0000, 73, 6, 45, 10, 1, 30, 0, "br3000", "Sepith_4757", 30, 40, 20, 10,
        (
            ("ms66800.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_640", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
            ("ms66800.dat", "ms66800.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
            ("ms66800.dat", "ms63400.dat", "ms66800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_640", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
            ("ms66800.dat", "ms63400.dat", "ms66800.dat", "ms63400.dat", 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
        )
    )

    BattleInfo(
        "BattleInfo_7F8", 0x0000, 73, 6, 60, 8, 1, 60, 0, "br3000", "Sepith_4767", 30, 40, 20, 10,
        (
            ("ms75600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_640", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
            ("ms75600.dat", "ms75600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
            ("ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_640", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
            ("ms75600.dat", "ms75600.dat", "ms75600.dat", "ms75600.dat", 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7450", "ed7453", "ATBonus_5E0"),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_8C0", 0x0042, 3, 6, 45, 3, 3, 30, 0, "br3000", 0x00000000, 100, 0, 0, 0,
        (
            ("ms42000.dat", "ms41901.dat", "ms82001.dat", "ms82001.dat", 0, 0, 0, 0, "MonsterBattlePostion_620", "MonsterBattlePostion_6A0", "ed7455", "ed7453", "ATBonus_600"),
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
        "monster/ch71650.itc",               # 10
        "monster/ch71650.itc",               # 11
        "monster/ch66850.itc",               # 12
        "monster/ch66851.itc",               # 13
        "monster/ch75650.itc",               # 14
        "monster/ch75651.itc",               # 15
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    485,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(0,       0,       0,       0,    197,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)

    DeclMonster(50180,   44450,   7000,    0x1010000,    "BattleInfo_6C0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(4610,    43710,   3000,    0x1010000,    "BattleInfo_730", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-3480,   5030,    0,       0x1010000,    "BattleInfo_6C0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(9210,    -10880,  0,       0x1010000,    "BattleInfo_730", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-21260,  -25600,  3000,    0x1010000,    "BattleInfo_6C0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(40830,   4510,    0,       0x1010000,    "BattleInfo_6C0", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(50180,   44450,   7000,    0x1010000,    "BattleInfo_7F8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(4610,    43710,   3000,    0x1010000,    "BattleInfo_7F8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-3480,   5030,    0,       0x1010000,    "BattleInfo_7F8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(9210,    -10880,  0,       0x1010000,    "BattleInfo_7F8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-21260,  -25600,  3000,    0x1010000,    "BattleInfo_7F8", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(40830,   4510,    0,       0x1010000,    "BattleInfo_7F8", 0,   20,  0xFFFF, 4,  5)

    DeclEvent(0x0000, 0, 7,   -12.0,                 0.0,                   -1.0,                  1225.0,                [0.20000000298023224,  -0.0,                  0.0,                   0.0,                   -0.0,                  0.0714285671710968,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   2.4000000953674316,    -0.0,                  0.20000000298023224,   1.0])

    DeclActor(-22010,  3100,    19990,   1200,    -22010,  4100,    19990,   0x007C, 0,  2,  0x0000)
    DeclActor(27380,   3100,    24860,   1200,    27380,   4100,    24860,   0x007C, 0,  3,  0x0000)
    DeclActor(37500,   3100,    16000,   1200,    37500,   4100,    16000,   0x007C, 0,  4,  0x0000)
    DeclActor(62600,   7050,    21320,   1200,    62600,   8050,    21320,   0x007C, 0,  5,  0x0000)

    PlaceName(-95.0, 0.0, -6.0, 0x0000, 0x0000, "アルモリカ古道方面")
    PlaceName(82.0, 0.0, -34.0, 0x0000, 0x0000, "太陽の砦方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 5])                   # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 4
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 5

    ScpFunction((
        "Function_0_980",          # 00, 0
        "Function_1_9F9",          # 01, 1
        "Function_2_152A",         # 02, 2
        "Function_3_167B",         # 03, 3
        "Function_4_17CC",         # 04, 4
        "Function_5_191D",         # 05, 5
        "Function_6_1A92",         # 06, 6
        "Function_7_1A96",         # 07, 7
        "Function_8_2598",         # 08, 8
        "Function_9_25CA",         # 09, 9
        "Function_10_25FC",        # 0A, 10
        "Function_11_2616",        # 0B, 11
        "Function_12_46BF",        # 0C, 12
    ))


    def Function_0_980(): pass

    label("Function_0_980")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x22, 0)), scpexpr(EXPR_END)), "loc_992")
    ClearScenarioFlags(0x22, 0)
    SetScenarioFlags(0x0, 0)
    Event(0, 11)

    label("loc_992")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x2)"), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x91, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9DA")
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    Jump("loc_9F8")

    label("loc_9DA")

    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    SetChrFlags(0x28, 0x80)

    label("loc_9F8")

    Return()

    # Function_0_980 end

    def Function_1_9F9(): pass

    label("Function_1_9F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_A0E")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearScenarioFlags(0x0, 0)

    label("loc_A0E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x183, 4)), scpexpr(EXPR_END)), "loc_ABF")
    OP_7D(0xDC, 0xEB, 0xFF, 0x0, 0x0)
    OP_11(0x7B, 0xB4, 0xD5, 0xD, 0x78, 0x0)
    ClearMapObjFlags(0x7, 0x4)
    ClearMapObjFlags(0x8, 0x4)
    ClearMapObjFlags(0x9, 0x4)
    ClearMapObjFlags(0xA, 0x4)
    ClearMapObjFlags(0xB, 0x4)
    ClearMapObjFlags(0xC, 0x4)
    ClearMapObjFlags(0xD, 0x4)
    ClearMapObjFlags(0xE, 0x4)
    ClearMapObjFlags(0xF, 0x4)
    ClearMapObjFlags(0x10, 0x4)
    ClearMapObjFlags(0x11, 0x4)
    ClearMapObjFlags(0x12, 0x4)
    ClearMapObjFlags(0x13, 0x4)
    ClearMapObjFlags(0x14, 0x4)
    ClearMapObjFlags(0x15, 0x4)
    ClearMapObjFlags(0x16, 0x4)
    ClearMapObjFlags(0x17, 0x4)
    ClearMapObjFlags(0x18, 0x4)
    ClearMapObjFlags(0x19, 0x4)
    ClearMapObjFlags(0x1A, 0x4)
    ClearMapObjFlags(0x1B, 0x4)
    ClearMapObjFlags(0x1C, 0x4)
    ClearMapObjFlags(0x1D, 0x4)
    Jump("loc_B49")

    label("loc_ABF")

    SetMapObjFlags(0x7, 0x4)
    SetMapObjFlags(0x8, 0x4)
    SetMapObjFlags(0x9, 0x4)
    SetMapObjFlags(0xA, 0x4)
    SetMapObjFlags(0xB, 0x4)
    SetMapObjFlags(0xC, 0x4)
    SetMapObjFlags(0xD, 0x4)
    SetMapObjFlags(0xE, 0x4)
    SetMapObjFlags(0xF, 0x4)
    SetMapObjFlags(0x10, 0x4)
    SetMapObjFlags(0x11, 0x4)
    SetMapObjFlags(0x12, 0x4)
    SetMapObjFlags(0x13, 0x4)
    SetMapObjFlags(0x14, 0x4)
    SetMapObjFlags(0x15, 0x4)
    SetMapObjFlags(0x16, 0x4)
    SetMapObjFlags(0x17, 0x4)
    SetMapObjFlags(0x18, 0x4)
    SetMapObjFlags(0x19, 0x4)
    SetMapObjFlags(0x1A, 0x4)
    SetMapObjFlags(0x1B, 0x4)
    SetMapObjFlags(0x1C, 0x4)
    SetMapObjFlags(0x1D, 0x4)

    label("loc_B49")

    OP_52(0x1D, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE6), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1D, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1F, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x21, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x22, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x1E, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x20, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x23, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x24, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x25, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x26, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x27, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x28, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 6)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1493")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_1493")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14A6")
    OP_70(0x2, 0x0)
    Jump("loc_14AA")

    label("loc_14A6")

    OP_70(0x2, 0x1E)

    label("loc_14AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14BD")
    OP_70(0x3, 0x0)
    Jump("loc_14C1")

    label("loc_14BD")

    OP_70(0x3, 0x1E)

    label("loc_14C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14D4")
    OP_70(0x4, 0x0)
    Jump("loc_14D8")

    label("loc_14D4")

    OP_70(0x4, 0x1E)

    label("loc_14D8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_14EB")
    OP_70(0x5, 0x0)
    Jump("loc_14EF")

    label("loc_14EB")

    OP_70(0x5, 0x1E)

    label("loc_14EF")

    OP_70(0x0, 0x78)
    OP_1C(0x0, 0x1E, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x1F, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    OP_1C(0x0, 0x20, 0x0, 0x32, 0x0, 0x6, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_1_9F9 end

    def Function_2_152A(): pass

    label("Function_2_152A")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_162A")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x76, 1)"), scpexpr(EXPR_END)), "loc_15B3")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F4, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_1625")

    label("loc_15B3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x76),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1625")

    Jump("loc_166F")

    label("loc_162A")

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

    label("loc_166F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_152A end

    def Function_3_167B(): pass

    label("Function_3_167B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F5, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_177B")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_1704")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F5, 0)
    OP_E0(0x5, 0x0)
    Jump("loc_1776")

    label("loc_1704")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FC),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x3, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1776")

    Jump("loc_17C0")

    label("loc_177B")

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

    label("loc_17C0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_167B end

    def Function_4_17CC(): pass

    label("Function_4_17CC")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F5, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_18CC")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_1855")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F5, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_18C7")

    label("loc_1855")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_18C7")

    Jump("loc_1911")

    label("loc_18CC")

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

    label("loc_1911")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_17CC end

    def Function_5_191D(): pass

    label("Function_5_191D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F5, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A5B")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x5, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 150)
    AddSepith(0x1, 150)
    AddSepith(0x2, 150)
    AddSepith(0x3, 150)
    AddSepith(0x4, 150)
    AddSepith(0x5, 150)
    AddSepith(0x6, 150)

    #A0010
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地のセピス×１５０\x01\x07\x02",

            "#57I水のセピス×１５０\x01\x07\x02",

            "#58I火のセピス×１５０\x01\x07\x02",

            "#59I風のセピス×１５０\x01\x07\x02",

            "#60I時のセピス×１５０\x01\x07\x02",

            "#61I空のセピス×１５０\x01\x07\x02",

            "#62I幻のセピス×１５０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F5, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1A80")

    label("loc_1A5B")


    #A0011
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱には何も入っていない。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_1A80")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_191D end

    def Function_6_1A92(): pass

    label("Function_6_1A92")

    Call(1, 6)
    Return()

    # Function_6_1A92 end

    def Function_7_1A96(): pass

    label("Function_7_1A96")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("chr/ch41950.itc", 0x23)
    LoadChrToIndex("chr/ch41951.itc", 0x24)
    LoadChrToIndex("chr/ch41953.itc", 0x25)
    LoadChrToIndex("chr/ch41900.itc", 0x26)
    LoadChrToIndex("chr/ch42050.itc", 0x28)
    LoadChrToIndex("chr/ch42051.itc", 0x29)
    LoadChrToIndex("chr/ch42053.itc", 0x2A)
    LoadChrToIndex("chr/ch00050.itc", 0x2D)
    LoadChrToIndex("chr/ch00250.itc", 0x32)
    LoadChrToIndex("chr/ch03150.itc", 0x37)
    LoadChrToIndex("chr/ch02750.itc", 0x3C)
    SoundLoad(155)
    SetChrChipByIndex(0x8, 0x24)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x0)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x0)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x29)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x24)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x29)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x24)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x1F)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    SetChrChipByIndex(0x12, 0x1F)
    SetChrSubChip(0x12, 0x0)
    SetChrFlags(0x12, 0x8000)
    SetMapObjFlags(0x1E, 0x4)
    SetChrPos(0x101, -3250, 0, 0, 90)
    SetChrPos(0x103, -4400, 0, 1000, 90)
    SetChrPos(0x105, -5200, 0, -1000, 90)
    SetChrPos(0x107, -7000, 0, 0, 90)

    def lambda_1BE7():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1BE7)
    Sleep(50)

    def lambda_1BFF():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_1BFF)
    Sleep(50)

    def lambda_1C17():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C17)
    Sleep(50)

    def lambda_1C2F():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_1C2F)
    OP_68(-4500, 1000, 0, 0)
    MoveCamera(45, 28, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22000, 0)
    OP_68(-1500, 1000, 0, 2000)
    FadeToBright(1000, 0)
    Sleep(1500)
    OP_0D()
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(149, 0, 100, 0)
    Sleep(300)
    WaitChrThread(0x101, 1)
    WaitChrThread(0x103, 1)
    WaitChrThread(0x105, 1)
    WaitChrThread(0x107, 1)
    OP_6F(0x79)
    Fade(500)
    OP_68(-17500, 1500, 0, 0)
    MoveCamera(60, 22, 0, 0)
    OP_6E(610, 0)
    SetCameraDistance(19500, 0)
    Sound(155, 2, 100, 0)
    OP_71(0x0, 0x78, 0xA, 0x0, 0x8)
    StopBGM(0x1770)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x105, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x107, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    def lambda_1D72():
        OP_93(0x101, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D72)
    Sleep(50)

    def lambda_1D82():
        OP_93(0x103, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_1D82)
    Sleep(50)

    def lambda_1D92():
        OP_93(0x105, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_1D92)
    Sleep(50)

    def lambda_1DA2():
        OP_93(0x107, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_1DA2)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0012
    ChrTalk(
        0x101,
        "#00007Fしまった……！\x02",
    )

    OP_79(0x0)
    Sound(149, 0, 100, 0)
    OP_24(0x9B)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    OP_71(0x0, 0xA, 0x0, 0x0, 0x8)
    OP_79(0x0)
    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x105,
        "#10410F罠……だったみたいだね。\x02",
    )

    CloseMessageWindow()
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -21950, 3000, -9200, 0)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0xF, -20800, 3000, -11250, 60)
    ClearChrFlags(0xF, 0x80)
    BeginChrThread(0xF, 3, 0, 9)
    OP_68(-15500, 3000, -5000, 3000)
    MoveCamera(55, 25, 0, 3000)
    OP_6E(610, 3000)
    SetCameraDistance(27500, 3000)
    Sleep(2000)
    OP_93(0x8, 0x3C, 0x1F4)
    SetChrChipByIndex(0x8, 0x24)
    OP_96(0x8, 0xFFFFB3D4, 0xBB8, 0xFFFFDB7A, 0xBB8, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    Sound(531, 0, 50, 0)
    Sound(358, 0, 50, 0)
    Sleep(500)
    OP_6F(0x79)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7582", 0)
    Fade(500)
    EndChrThread(0xF, 0x3)
    SetChrPos(0x101, 3000, 0, 0, 90)
    SetChrPos(0x103, 2000, 0, 1000, 0)
    SetChrPos(0x105, 2000, 0, -1000, 180)
    SetChrPos(0x107, 1000, 0, 0, 270)
    SetChrPos(0x9, 13000, 0, 1000, 270)
    SetChrPos(0xA, 13500, 0, -1000, 270)
    SetChrPos(0xB, 2000, 0, 12000, 180)
    SetChrPos(0xC, 2000, 0, -12000, 0)
    SetChrPos(0xD, -9000, 0, 1000, 90)
    SetChrPos(0xE, -9500, 0, -1000, 90)
    SetChrPos(0xF, -6000, 0, -8000, 45)
    SetChrPos(0x10, 10000, 0, -8000, 315)
    SetChrPos(0x11, 10000, 0, 8000, 225)
    SetChrPos(0x12, -6000, 0, 8000, 135)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    OP_68(2000, 1000, 0, 0)
    MoveCamera(40, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(23000, 0)
    MoveCamera(50, 20, 0, 3000)
    SetCameraDistance(25000, 3000)

    def lambda_2054():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2054)

    def lambda_2069():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2069)
    Sleep(50)
    BeginChrThread(0xF, 3, 0, 8)
    BeginChrThread(0x1C, 1, 0, 10)

    def lambda_208D():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_208D)
    Sleep(50)

    def lambda_20A5():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_20A5)
    Sleep(50)
    BeginChrThread(0x10, 3, 0, 8)

    def lambda_20C3():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_20C3)
    Sleep(50)

    def lambda_20DB():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_20DB)

    def lambda_20F0():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_20F0)
    Sleep(50)
    BeginChrThread(0x11, 3, 0, 8)

    def lambda_210E():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_210E)
    Sleep(50)

    def lambda_2126():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_2126)
    BeginChrThread(0x12, 3, 0, 8)

    def lambda_2141():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2141)
    WaitChrThread(0xD, 1)
    Sound(540, 0, 50, 0)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    WaitChrThread(0xE, 1)
    Sound(531, 0, 50, 0)
    Sound(358, 0, 50, 0)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    WaitChrThread(0xF, 1)
    EndChrThread(0xF, 0x3)
    EndChrThread(0x1C, 0x1)
    BeginChrThread(0xF, 3, 0, 9)
    WaitChrThread(0xC, 1)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    WaitChrThread(0x10, 1)
    EndChrThread(0x10, 0x3)
    BeginChrThread(0x10, 3, 0, 9)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    WaitChrThread(0x11, 1)
    EndChrThread(0x11, 0x3)
    BeginChrThread(0x11, 3, 0, 9)
    WaitChrThread(0xB, 1)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    WaitChrThread(0x12, 1)
    EndChrThread(0x12, 0x3)
    BeginChrThread(0x12, 3, 0, 9)
    OP_0D()
    OP_6F(0x79)
    SetCameraDistance(21500, 20000)
    MoveCamera(60, 20, 0, 20000)

    #C0014
    ChrTalk(
        0x103,
        "#00201F#11P《赤い星座》……！\x02",
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x107,
        (
            "#01201F#12P#3C気配を消していたのは\x01",
            "こやつらだったか。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0xC,
        (
            "#12Pハハ、目当てに逃げられて\x01",
            "当てが外れた気分だったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0xC,
        (
            "#12P代わりの獲物が\x01",
            "飛び込んできてくれるとはな。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0xD,
        "#6Pランドルフ隊長の同僚か……\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0xD,
        (
            "#6P捕らえておけば大統領や\x01",
            "国防軍にも恩が売れそうだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        "#00010F#5Pくっ……\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x103,
        (
            "#00206F#11P総勢７名……\x01",
            "軍用魔獣多数の構成です。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x9,
        (
            "#11Pフフ、なかなか歯ごたえが\x01",
            "ありそうな獲物どもだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x9,
        (
            "#11Pじっくりと確実に\x01",
            "削ってくれるとしよう。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0xA,
        (
            "#11P《赤い星座#8Rわ れ わ れ#》の包囲から\x01",
            "どこまで持ちこたえられるか……\x02",
        )
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0xA,
        "#11P見せてもらうぞ、特務支援課！\x02",
    )

    CloseMessageWindow()
    Fade(250)
    Sound(805, 0, 100, 0)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x32)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0x37)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x3C)
    SetChrSubChip(0x107, 0x0)
    OP_0D()

    #C0026
    ChrTalk(
        0x101,
        "#00007F#5P望むところだ……！\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x105,
        "#10407F#6P全力で包囲を突破する！\x02",
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    SetChrChipByIndex(0x9, 0x29)

    def lambda_24D9():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_24D9)
    SetChrChipByIndex(0xA, 0x24)

    def lambda_24F2():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_24F2)
    BeginChrThread(0xF, 3, 0, 8)

    def lambda_250D():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_250D)
    BeginChrThread(0x12, 3, 0, 8)

    def lambda_2528():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_2528)
    OP_24(0x9B)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x5)
    SetCameraDistance(20000, 200)
    Sleep(200)
    CancelBlur(200)
    Battle("BattleInfo_8C0", 0x30200011, 0x0, 0x100, 0x1A, 0xFF)
    FadeToDark(0, 0, -1)
    EndChrThread(0x9, 0x1)
    EndChrThread(0xA, 0x1)
    EndChrThread(0xF, 0x3)
    EndChrThread(0xF, 0x1)
    EndChrThread(0x12, 0x3)
    EndChrThread(0x12, 0x1)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    Call(0, 11)
    Return()

    # Function_7_1A96 end

    def Function_8_2598(): pass

    label("Function_8_2598")

    SetChrChipByIndex(0xFE, 0x1F)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25C9")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_25B2")

    label("loc_25C9")

    Return()

    # Function_8_2598 end

    def Function_9_25CA(): pass

    label("Function_9_25CA")

    SetChrChipByIndex(0xFE, 0x1E)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_25E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25FB")
    OP_A0(0xFE, 1500, 0x0, 0x7)
    Jump("loc_25E4")

    label("loc_25FB")

    Return()

    # Function_9_25CA end

    def Function_10_25FC(): pass

    label("Function_10_25FC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2615")
    Sound(845, 0, 80, 0)
    Sleep(440)
    Jump("Function_10_25FC")

    label("loc_2615")

    Return()

    # Function_10_25FC end

    def Function_11_2616(): pass

    label("Function_11_2616")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SetChrChipPat(0x5, 0x1, 0x20)
    AddParty(0x5, 0xFF, 0xFF)
    LoadChrChipPat()
    OP_32(0x5, 0x0, 0x53)
    OP_32(0x5, 0x5, 0xC8)
    OP_42(0x5, 0x461, 0xFF)
    OP_42(0x5, 0x5ED, 0xFF)
    OP_42(0x5, 0x651, 0xFF)
    RemoveCraft(0x5, 0xFFFF)
    OP_38(0x5, 0x80, 0x2)
    OP_38(0x5, 0x81, 0x2)
    OP_38(0x5, 0x82, 0x1)
    OP_38(0x5, 0x83, 0x1)
    OP_38(0x5, 0x84, 0x2)
    OP_38(0x5, 0x85, 0x2)
    OP_38(0x5, 0x86, 0x2)
    OP_42(0x5, 0xBA, 0x1)
    OP_42(0x5, 0x7D, 0x2)
    OP_42(0x5, 0xA3, 0x3)
    OP_42(0x5, 0x76, 0x4)
    OP_42(0x5, 0x6A, 0x5)
    OP_42(0x5, 0xBB, 0x6)
    AddCraft(0x5, 0xCD)
    AddCraft(0x5, 0xCE)
    AddCraft(0x5, 0xD0)
    AddCraft(0x5, 0x134)
    SetChrChipPat(0x5, 0x6, 0x134)
    LoadChrToIndex("monster/ch82050.itc", 0x1E)
    LoadChrToIndex("monster/ch82051.itc", 0x1F)
    LoadChrToIndex("monster/ch82053.itc", 0x20)
    LoadChrToIndex("chr/ch41950.itc", 0x23)
    LoadChrToIndex("chr/ch41951.itc", 0x24)
    LoadChrToIndex("chr/ch41953.itc", 0x25)
    LoadChrToIndex("chr/ch41900.itc", 0x26)
    LoadChrToIndex("chr/ch42050.itc", 0x28)
    LoadChrToIndex("chr/ch42051.itc", 0x29)
    LoadChrToIndex("chr/ch42053.itc", 0x2A)
    LoadChrToIndex("chr/ch00050.itc", 0x2D)
    LoadChrToIndex("chr/ch00250.itc", 0x32)
    LoadChrToIndex("chr/ch03150.itc", 0x37)
    LoadChrToIndex("chr/ch02750.itc", 0x3C)
    LoadChrToIndex("apl/ch51705.itc", 0x41)
    LoadChrToIndex("chr/ch0325A.itc", 0x42)
    LoadChrToIndex("chr/ch06300.itc", 0x46)
    LoadChrToIndex("apl/ch51704.itc", 0x47)
    LoadChrToIndex("chr/ch31400.itc", 0x4B)
    LoadChrToIndex("chr/ch31452.itc", 0x4C)
    LoadChrToIndex("chr/ch31500.itc", 0x50)
    LoadChrToIndex("chr/ch12500.itc", 0x55)
    CreatePortrait(0, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu10700.itp")
    CreatePortrait(1, 234, 0, 490, 256, 0, 0, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu03200.itp")
    LoadEffect(0x0, "event/ev17028.eff")
    LoadEffect(0x1, "battle/cr320000.eff")
    LoadEffect(0x2, "battle/cr004000.eff")
    LoadEffect(0x3, "battle/ms00000.eff")
    SoundLoad(155)
    SetChrChipByIndex(0x101, 0x2D)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0x32)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0x37)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0x3C)
    SetChrSubChip(0x107, 0x0)
    SetChrChipByIndex(0x8, 0x23)
    SetChrSubChip(0x8, 0x0)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x3)
    SetChrFlags(0x9, 0x8000)
    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x3)
    SetChrFlags(0xA, 0x8000)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    SetChrFlags(0xC, 0x8000)
    SetChrChipByIndex(0xD, 0x28)
    SetChrSubChip(0xD, 0x0)
    SetChrFlags(0xD, 0x8000)
    SetChrChipByIndex(0xE, 0x23)
    SetChrSubChip(0xE, 0x0)
    SetChrFlags(0xE, 0x8000)
    SetChrChipByIndex(0x13, 0x46)
    SetChrSubChip(0x13, 0x0)
    SetChrFlags(0x13, 0x8000)
    SetChrChipByIndex(0x14, 0x4B)
    SetChrSubChip(0x14, 0x0)
    SetChrFlags(0x14, 0x8000)
    SetChrChipByIndex(0x15, 0x50)
    SetChrSubChip(0x15, 0x0)
    SetChrFlags(0x15, 0x8000)
    SetChrChipByIndex(0x16, 0x55)
    SetChrSubChip(0x16, 0x0)
    SetChrFlags(0x16, 0x8000)
    SetChrChipByIndex(0x17, 0x50)
    SetChrSubChip(0x17, 0x0)
    SetChrFlags(0x17, 0x8000)
    SetChrChipByIndex(0x18, 0x55)
    SetChrSubChip(0x18, 0x0)
    SetChrFlags(0x18, 0x8000)
    SetChrChipByIndex(0x19, 0x50)
    SetChrSubChip(0x19, 0x0)
    SetChrFlags(0x19, 0x8000)
    SetChrChipByIndex(0x1A, 0x55)
    SetChrSubChip(0x1A, 0x0)
    SetChrFlags(0x1A, 0x8000)
    SetChrChipByIndex(0x1B, 0x50)
    SetChrSubChip(0x1B, 0x0)
    SetChrFlags(0x1B, 0x8000)
    SetChrChipByIndex(0xF, 0x1E)
    SetChrSubChip(0xF, 0x0)
    SetChrFlags(0xF, 0x8000)
    SetChrChipByIndex(0x10, 0x1E)
    SetChrSubChip(0x10, 0x0)
    SetChrFlags(0x10, 0x8000)
    SetChrChipByIndex(0x11, 0x1E)
    SetChrSubChip(0x11, 0x0)
    SetChrFlags(0x11, 0x8000)
    BeginChrThread(0xF, 3, 0, 9)
    BeginChrThread(0x10, 3, 0, 9)
    SetMapObjFlags(0x1E, 0x4)
    OP_F3(100000)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)
    ClearChrFlags(0xC, 0x80)
    ClearChrFlags(0xD, 0x80)
    ClearChrFlags(0xE, 0x80)
    ClearChrFlags(0xF, 0x80)
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x101, 3000, 0, 0, 90)
    SetChrPos(0x103, 2000, 0, 1000, 0)
    SetChrPos(0x105, 2000, 0, -1000, 180)
    SetChrPos(0x107, 1000, 0, 0, 270)
    SetChrPos(0x8, -19500, 3000, -9350, 60)
    SetChrPos(0x9, 5500, 0, 1000, 270)
    SetChrPos(0xA, 6000, 0, -1000, 270)
    SetChrPos(0xB, 2000, 0, 6500, 180)
    SetChrPos(0xC, 2000, 0, -6500, 0)
    SetChrPos(0xD, -3500, 0, 1000, 135)
    SetChrPos(0xE, -4000, 0, -1000, 90)
    SetChrPos(0xF, 6450, 0, -4450, 315)
    SetChrPos(0x10, 6450, 0, 4450, 225)
    SetChrPos(0x11, -20800, 3000, -11250, 60)
    OP_68(1470, 1300, -990, 0)
    MoveCamera(60, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(22700, 0)
    PlayBGM("ed7582", 0)
    MoveCamera(33, 18, 0, 4000)
    SetCameraDistance(20500, 4000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2A8C():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_2A8C)
    Sleep(300)

    def lambda_2AA8():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2AA8)
    WaitChrThread(0x9, 3)
    Fade(250)
    Sound(802, 0, 100, 0)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    OP_52(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    WaitChrThread(0xA, 3)
    Fade(250)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    OP_52(0xA, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_0D()
    SetChrChipByIndex(0x9, 0x29)
    SetChrSubChip(0x9, 0x3)
    Sound(809, 0, 100, 0)

    def lambda_2B0F():
        OP_9D(0xFE, 0x1D4C, 0x0, 0x3E8, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_2B0F)
    Sleep(100)
    SetChrChipByIndex(0xA, 0x24)
    SetChrSubChip(0xA, 0x3)

    def lambda_2B37():
        OP_9D(0xFE, 0x1F40, 0x0, 0xFFFFFC18, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2B37)
    WaitChrThread(0x9, 1)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    WaitChrThread(0xA, 1)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    Sound(326, 0, 70, 0)
    Sleep(300)
    OP_6F(0x79)
    SetCameraDistance(19000, 20000)

    #C0028
    ChrTalk(
        0x9,
        "#11Pふむ……\x02",
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xA,
        "#11Pなかなかやる……\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        "#00015F#5Pくっ……はあはあ……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x105,
        (
            "#10410F#6Pさすがに国防軍とは\x01",
            "一味も二味も違うねぇ……\x02",
        )
    )

    CloseMessageWindow()

    #C0032
    ChrTalk(
        0xD,
        (
            "#6P当然だ──\x01",
            "我らは《赤い星座》。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xD,
        (
            "#6P大陸全土の戦場を駆け、\x01",
            "蹂躙してきた修羅の一党だ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xC,
        (
            "#11Pかの《身喰らう蛇》ですら\x01",
            "戦場では我らには及ばぬ……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0xC,
        (
            "#11Pたとえそちらの狼が\x01",
            "巨大な化物に変わっても\x01",
            "容赦なく狩るのみだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0036
    ChrTalk(
        0x107,
        "#01201F#12P#3Cほう……？\x02",
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0x103,
        "#00208F#11Pツァイトの事まで……\x02",
    )

    CloseMessageWindow()

    #C0038
    ChrTalk(
        0x105,
        (
            "#10406F#6P……アッバスに連絡を\x01",
            "入れておけば良かったかな。\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        "#00010F#5P……………………………\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0xB,
        (
            "#5Pお前たちがこの包囲を\x01",
            "突破できる可能性はゼロだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0041
    ChrTalk(
        0xB,
        (
            "#5Pこのまま嬲#2Rなぶ#られるか\x01",
            "投降するか、選ぶがいい。\x02",
        )
    )

    CloseMessageWindow()
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x13, 2000, 0, 9500, 180)
    ClearChrFlags(0x13, 0x80)

    #N0042
    NpcTalk(
        0x13,
        "青年の声",
        (
            "#5P#3C#N──やれやれ。\x01",
            "ゼロというのはさすがに\x01",
            "言いすぎではないですか？\x02",
        )
    )

    CloseMessageWindow()
    StopBGM(0xBB8)
    OP_63(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    OP_68(2000, 1000, 9500, 0)
    MoveCamera(45, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(12000, 0)

    def lambda_2EDA():
        OP_93(0xFE, 0x0, 0x12C)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2EDA)
    OP_0D()
    Sound(254, 0, 50, 0)
    SetChrPos(0x13, 2000, 5000, 9500, 180)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    SetChrFlags(0x13, 0x2)
    SetChrChipByIndex(0x13, 0x47)
    SetChrSubChip(0x13, 0x0)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x13, 0x4)
    SetChrFlags(0x13, 0x20)

    def lambda_2F32():
        OP_96(0xFE, 0x7D0, 0x0, 0x251C, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_2F32)
    OP_A7(0x13, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Sleep(100)
    WaitChrThread(0x13, 1)
    OP_52(0x13, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x13, 0x4)
    OP_68(2000, 1000, 7000, 500)
    SetCameraDistance(11000, 500)
    SetChrChip(0x0, 0x13, 0x32, 0xC8)
    Sound(250, 0, 100, 0)
    Sound(251, 0, 50, 0)
    OP_9A(0x13, 0xB, 0x2EE, 0x61A8, 0x0)
    ClearChrFlags(0x13, 0x20)
    SetChrChip(0x1, 0x13, 0x0, 0x0)
    Sleep(100)
    OP_A0(0x13, 2000, 0x0, 0x2)
    PlayEffect(0x1, 0xFF, 0x13, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(635, 0, 100, 0)
    Sound(815, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    Sound(833, 0, 30, 0)
    WaitChrThread(0xB, 2)

    #C0043
    ChrTalk(
        0xB,
        "#10Aがはっ……！\x02",
    )
    #Auto

    OP_68(3850, 1000, 730, 500)
    MoveCamera(40, 25, -5, 500)
    SetCameraDistance(18750, 500)
    PlayEffect(0x3, 0xFF, 0xB, 0x1, 0, 500, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xB, 0x2A)
    SetChrSubChip(0xB, 0x0)

    def lambda_30A9():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_30A9)
    Sound(809, 0, 100, 0)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xB, 0x1900, 0xFA, 0xFFFFEED0, 0x3E8, 0xBB8)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    Sound(501, 0, 100, 0)

    def lambda_3101():
        OP_9D(0xFE, 0x1770, 0x0, 0xFFFFF542, 0x3E8, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3101)

    def lambda_311E():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_311E)
    BeginChrThread(0xF, 1, 0, 12)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xB, 3)
    SetChrSubChip(0xB, 0x3)
    Sound(514, 0, 100, 0)
    OP_52(0xB, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(2000, 1000, 0, 0)
    MoveCamera(40, 20, 0, 0)
    SetCameraDistance(23000, 0)
    OP_0D()

    def lambda_318A():
        TurnDirection(0xFE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_318A)

    def lambda_3197():
        TurnDirection(0x9, 0x13, 500)
        ExitThread()

    QueueWorkItem(0x9, 0, lambda_3197)
    Sleep(50)

    def lambda_31A7():
        TurnDirection(0xA, 0x13, 500)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_31A7)
    Sleep(50)

    def lambda_31B7():
        TurnDirection(0xC, 0x13, 500)
        ExitThread()

    QueueWorkItem(0xC, 0, lambda_31B7)
    Sleep(50)

    def lambda_31C7():
        TurnDirection(0xD, 0x13, 500)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_31C7)
    Sleep(50)

    def lambda_31D7():
        TurnDirection(0xE, 0x13, 500)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_31D7)
    Sleep(50)
    WaitChrThread(0x9, 0)
    WaitChrThread(0xA, 0)
    WaitChrThread(0xC, 0)
    WaitChrThread(0xD, 0)
    WaitChrThread(0xE, 0)
    WaitBGM()
    Sleep(10)
    PlayBGM("ed7512", 0)

    #C0044
    ChrTalk(
        0xE,
        "#12Pツァオ・リー！？\x02",
    )

    CloseMessageWindow()

    #C0045
    ChrTalk(
        0xC,
        "#11Pここから逃げたはずでは！？\x02",
    )

    CloseMessageWindow()
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x14, 2000, 0, -9500, 0)
    ClearChrFlags(0x14, 0x80)

    #N0046
    NpcTalk(
        0x14,
        "男の声",
        (
            "それは貴様らが\x01",
            "我らを捉え損ねただけだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0xC, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    Fade(500)
    SetChrChipByIndex(0x13, 0x46)
    SetChrSubChip(0x13, 0x0)
    ClearChrFlags(0x13, 0x2)
    OP_93(0xA, 0xE1, 0x0)
    OP_93(0xE, 0x87, 0x0)
    OP_68(2000, 1000, -9500, 0)
    MoveCamera(50, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(13000, 0)

    def lambda_32FF():
        OP_93(0xFE, 0xB4, 0x12C)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_32FF)
    OP_0D()
    Sound(254, 0, 50, 0)
    SetChrPos(0x14, 2000, 5000, -9500, 0)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    CancelBlur(500)
    SetChrChipByIndex(0x14, 0x4C)
    SetChrSubChip(0x14, 0x0)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x14, 0x4)
    SetChrFlags(0x14, 0x20)

    def lambda_3352():
        OP_96(0xFE, 0x7D0, 0x0, 0xFFFFDAE4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_3352)
    OP_A7(0x14, 0xFF, 0xFF, 0xFF, 0xFF, 0x1F4)
    Sleep(100)
    WaitChrThread(0x14, 1)
    OP_52(0x14, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x14, 0x4)
    OP_68(2000, 1000, -7000, 300)
    SetCameraDistance(12000, 300)
    SetChrChip(0x0, 0x14, 0x32, 0xC8)
    Sound(250, 0, 100, 0)
    Sound(251, 0, 50, 0)
    SetChrFlags(0x14, 0x20)
    OP_96(0x14, 0x7D0, 0x0, 0xFFFFE37C, 0x61A8, 0x0)
    ClearChrFlags(0x14, 0x20)
    Sleep(100)
    SetChrChip(0x1, 0x14, 0x0, 0x0)
    OP_A0(0x14, 2000, 0x0, 0x1)
    PlayEffect(0x2, 0xFF, 0x14, 0x3, -500, 1000, 500, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sound(635, 0, 100, 0)
    Sound(815, 0, 100, 0)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    BlurSwitch(0x0, 0xBBFFFFFF, 0x0, 0x1, 0x1)
    CancelBlur(500)
    Sound(833, 0, 30, 0)
    OP_68(-70, 1000, -3470, 500)
    MoveCamera(44, 30, 5, 500)
    SetCameraDistance(18500, 500)

    #C0047
    ChrTalk(
        0xC,
        "#10Aぐおっ……！\x02",
    )
    #Auto

    OP_82(0x64, 0x0, 0xBB8, 0x12C)
    PlayEffect(0x3, 0xFF, 0xC, 0x1, 0, 500, 0, 0, 0, 0, 750, 750, 750, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0xC, 0x25)
    SetChrSubChip(0xC, 0x0)

    def lambda_34E1():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_34E1)
    Sound(809, 0, 100, 0)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_9D(0xC, 0xFFFFF92A, 0x0, 0x384, 0x3E8, 0xBB8)
    OP_52(0xC, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0xC, 0x3)
    Sound(514, 0, 100, 0)
    SetChrFlags(0xC, 0x20)
    OP_9B(0x1, 0xC, 0x0, 0xFFFFFC18, 0xBB8, 0x0)
    ClearChrFlags(0xC, 0x20)
    OP_0D()
    OP_6F(0x79)
    Sleep(1000)
    Fade(500)
    OP_68(5000, 1000, -400, 0)
    MoveCamera(45, 15, 5, 0)
    SetCameraDistance(21450, 0)
    OP_0D()

    #C0048
    ChrTalk(
        0x9,
        "#11P貴様らっ……！\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xA,
        (
            "#5P怯むな！\x01",
            "戦闘力ならこちらの方が──\x02",
        )
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x4)
    SetChrPos(0x106, 18350, 11600, 6200, 270)
    Sound(308, 0, 100, 0)
    PlayEffect(0x0, 0xFF, 0xA, 0x1, 0, 500, -500, 250, 40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(50)
    PlayEffect(0x0, 0xFF, 0x9, 0x1, 0, 500, -500, 260, 40, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(250)
    OP_82(0x0, 0x64, 0xBB8, 0x190)
    Sleep(400)
    Sound(196, 0, 100, 0)
    OP_82(0x0, 0x12C, 0xBB8, 0x3E8)

    #C0050
    ChrTalk(
        0xA,
        "#10A#5Pがっ……！\x02",
    )
    #Auto

    SetChrChipByIndex(0xA, 0x25)
    SetChrSubChip(0xA, 0x0)

    def lambda_369E():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_369E)

    def lambda_36B7():
        OP_9C(0xFE, 0xFFFFFE0C, 0x0, 0xFFFFFE0C, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_36B7)
    Sleep(50)

    #C0051
    ChrTalk(
        0x9,
        "#10A#6Pぐうっ……！\x02",
    )
    #Auto

    SetChrChipByIndex(0x9, 0x2A)
    SetChrSubChip(0x9, 0x0)

    def lambda_36F7():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_36F7)

    def lambda_3710():
        OP_9C(0xFE, 0xFFFFFE0C, 0x0, 0x1F4, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3710)
    WaitChrThread(0xA, 1)
    SetChrSubChip(0xA, 0x3)
    Sound(514, 0, 100, 0)
    WaitChrThread(0x9, 1)
    SetChrSubChip(0x9, 0x3)
    Sleep(1000)

    #C0052
    ChrTalk(
        0x101,
        "#00005Fあ……\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x106, 0x2)
    SetChrChipByIndex(0x106, 0x41)
    SetChrSubChip(0x106, 0x0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    OP_68(18350, 12500, 6200, 3000)
    MoveCamera(45, 25, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(17500, 3000)
    Sleep(2000)
    OP_6F(0x79)
    SetChrPos(0xD, 18150, 0, 3600, 45)
    SetChrPos(0xE, 16149, -130, 6450, 45)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0053
    AnonymousTalk(
        0x106,
        "…………………………………\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x0, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CC(0x0, 0x0, 0x0)

    #C0054
    ChrTalk(
        0xD,
        "#11P《銀#2Rイン#》……！\x02",
    )

    CloseMessageWindow()

    #C0055
    ChrTalk(
        0xE,
        (
            "#5P……やはりクロスベルに\x01",
            "まだ残っていたか……！\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrChipByIndex(0x14, 0x4B)
    SetChrSubChip(0x14, 0x0)
    SetChrPos(0x13, 2000, 0, 5000, 230)
    SetChrPos(0x14, 2000, 0, -5000, 320)
    SetChrPos(0x15, 14500, 0, 0, 270)
    SetChrPos(0x16, 15000, 0, 1000, 270)
    SetChrPos(0x17, 15500, 0, -1000, 270)
    SetChrPos(0x18, 3000, 0, 12000, 180)
    SetChrPos(0x19, 1000, 0, 11500, 180)
    SetChrPos(0x1A, 3000, 0, -11500, 0)
    SetChrPos(0x1B, 1000, 0, -12000, 0)
    SetChrPos(0xC, -1250, 0, 0, 180)
    SetChrPos(0xD, -3500, 0, 1000, 135)
    SetChrPos(0xE, -4000, 0, -1000, 90)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x19, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    OP_68(2000, 1000, 0, 0)
    MoveCamera(45, 20, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(27500, 0)
    MoveCamera(50, 18, 0, 2000)
    SetCameraDistance(25500, 2000)

    def lambda_39EB():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_39EB)
    Sleep(50)

    def lambda_3A03():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_3A03)
    Sleep(50)

    def lambda_3A1B():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_3A1B)
    Sleep(50)

    def lambda_3A33():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_3A33)
    Sleep(50)

    def lambda_3A4B():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_3A4B)
    Sleep(50)

    def lambda_3A63():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_3A63)
    Sleep(50)

    def lambda_3A7B():
        OP_9B(0x1, 0xFE, 0x0, 0x1388, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_3A7B)
    WaitChrThread(0x15, 1)
    WaitChrThread(0x16, 1)
    WaitChrThread(0x17, 1)
    WaitChrThread(0x18, 1)
    WaitChrThread(0x19, 1)
    WaitChrThread(0x1A, 1)
    WaitChrThread(0x1B, 1)
    OP_0D()
    OP_6F(0x79)

    #C0056
    ChrTalk(
        0x13,
        (
            "#03204F#5Pフフ、その程度の数で\x01",
            "私たちを狩ろうとは……\x02\x03",

            "#03210F《黒月#4Rヘイユエ#》も舐められたものですね。\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xD,
        "#6Pく……\x02",
    )

    CloseMessageWindow()

    #C0058
    ChrTalk(
        0xE,
        "#6P……どうする……？\x02",
    )

    CloseMessageWindow()

    #C0059
    ChrTalk(
        0x14,
        (
            "#11P──客人がいる故、\x01",
            "この場は見逃してやろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0060
    ChrTalk(
        0x14,
        (
            "#11P我らを狩るつもりならば\x01",
            "倍の数は連れてくるがいい。\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0x13,
        (
            "#03206F#5Pそれと《戦鬼》どのか\x01",
            "《血染めの#8Rブ ラ ッ デ ィ#シャーリィ》さんに\x01",
            "来て頂かなくては。\x02\x03",

            "#03202Fせっかくお持て成しをする\x01",
            "甲斐がないというものです。\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xD,
        "#6P……伝えておこう。\x02",
    )

    CloseMessageWindow()

    #C0063
    ChrTalk(
        0xE,
        "#6P後悔するなよ……？\x02",
    )

    CloseMessageWindow()

    def lambda_3C91():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 3, lambda_3C91)
    Sleep(100)

    def lambda_3CAD():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xC, 3, lambda_3CAD)
    Sleep(100)

    def lambda_3CC9():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0x9, 3, lambda_3CC9)
    Sleep(100)

    def lambda_3CE5():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3CE5)
    WaitChrThread(0xB, 3)
    Sound(802, 0, 100, 0)
    Sound(540, 0, 30, 0)
    Sound(531, 0, 30, 0)
    Sound(358, 0, 30, 0)
    SetChrChipByIndex(0xB, 0x28)
    SetChrSubChip(0xB, 0x0)
    WaitChrThread(0xC, 3)
    SetChrChipByIndex(0xC, 0x23)
    SetChrSubChip(0xC, 0x0)
    WaitChrThread(0x9, 3)
    SetChrChipByIndex(0x9, 0x28)
    SetChrSubChip(0x9, 0x0)
    WaitChrThread(0xA, 3)
    SetChrChipByIndex(0xA, 0x23)
    SetChrSubChip(0xA, 0x0)
    TurnDirection(0xE, 0x8, 500)
    Sleep(300)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0064
    ChrTalk(
        0xE,
        "#5P#4S──扉を開けろ！\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x9, 500)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0065
    ChrTalk(
        0xD,
        "#5P#4S撤退する……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(500)
    SetChrChipByIndex(0x8, 0x26)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, -21950, 3000, -9200, 0)
    SetChrChipByIndex(0x9, 0x29)
    SetChrChipByIndex(0xA, 0x24)
    SetChrChipByIndex(0xB, 0x29)
    SetChrChipByIndex(0xC, 0x24)
    SetChrChipByIndex(0xD, 0x29)
    SetChrChipByIndex(0xE, 0x24)
    OP_93(0x9, 0x10E, 0x0)
    OP_93(0xA, 0x10E, 0x0)
    OP_93(0xB, 0x10E, 0x0)
    OP_93(0xC, 0x10E, 0x0)
    OP_93(0xD, 0x10E, 0x0)
    OP_93(0xE, 0x10E, 0x0)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x0)
    OP_93(0x101, 0x10E, 0x0)
    OP_93(0x103, 0x10E, 0x0)
    OP_93(0x105, 0x10E, 0x0)
    OP_93(0x107, 0x10E, 0x0)
    SetChrChipByIndex(0xF, 0x1F)
    SetChrChipByIndex(0x10, 0x1F)
    SetChrPos(0xF, 2450, 0, -1450, 270)
    SetChrPos(0x10, 450, 0, 1450, 270)
    BeginChrThread(0xF, 3, 0, 8)
    BeginChrThread(0x10, 3, 0, 8)
    BeginChrThread(0x1C, 1, 0, 10)
    OP_68(-15000, 1000, 0, 0)
    MoveCamera(60, 25, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(30750, 0)
    OP_68(-20000, 1000, 0, 5000)
    MoveCamera(50, 30, 0, 0)

    def lambda_3ED4():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3ED4)

    def lambda_3EE9():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3EE9)

    def lambda_3EFE():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3EFE)

    def lambda_3F13():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3F13)

    def lambda_3F28():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F28)

    def lambda_3F3D():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3F3D)

    def lambda_3F52():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3F52)

    def lambda_3F67():
        OP_9B(0x1, 0xFE, 0x0, 0xC350, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3F67)
    Sound(155, 2, 100, 0)
    OP_71(0x0, 0x0, 0x78, 0x0, 0x0)
    Sleep(1200)

    def lambda_3F91():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x107, 1, lambda_3F91)
    Sleep(50)

    def lambda_3FA9():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3FA9)
    Sleep(50)

    def lambda_3FC1():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_3FC1)
    Sleep(50)

    def lambda_3FD9():
        OP_9B(0x1, 0xFE, 0x0, 0x1770, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3FD9)
    OP_79(0x0)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    SetChrChipByIndex(0x8, 0x24)

    def lambda_3FFE():
        OP_95(0xFE, -24450, 3000, -8800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3FFE)
    Sleep(100)
    BeginChrThread(0x11, 3, 0, 8)

    def lambda_4021():
        OP_95(0xFE, -24450, 3000, -8800, 4000, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_4021)
    WaitChrThread(0x8, 1)
    Sound(809, 0, 100, 0)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_4050():
        OP_9D(0xFE, 0xFFFF8EB8, 0x0, 0xFFFFE4A8, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_4050)
    WaitChrThread(0x11, 1)
    EndChrThread(0x11, 0x3)
    SetChrSubChip(0x11, 0x6)
    Sound(809, 0, 100, 0)
    OP_52(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_408A():
        OP_9D(0xFE, 0xFFFF8EB8, 0x0, 0xFFFFE4A8, 0x5DC, 0x2710)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_408A)
    Sleep(1000)
    EndChrThread(0x1C, 0x1)
    WaitChrThread(0x9, 1)
    WaitChrThread(0xA, 1)
    WaitChrThread(0xB, 1)
    WaitChrThread(0xC, 1)
    WaitChrThread(0xD, 1)
    WaitChrThread(0xE, 1)
    OP_52(0x8, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    SetChrFlags(0xE, 0x80)
    Fade(500)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x103, 0xFF)
    SetChrSubChip(0x103, 0x0)
    SetChrChipByIndex(0x105, 0xFF)
    SetChrSubChip(0x105, 0x0)
    SetChrChipByIndex(0x107, 0xFF)
    SetChrSubChip(0x107, 0x5)
    SetChrPos(0x101, -3000, 0, -2000, 270)
    SetChrPos(0x103, -4000, 0, -1000, 270)
    SetChrPos(0x105, -4000, 0, -3000, 270)
    SetChrPos(0x107, -5000, 0, -2000, 270)
    SetChrPos(0x13, 5250, 0, -2000, 270)
    SetChrPos(0x14, 5500, 0, -3000, 270)
    SetChrPos(0x15, 6750, 0, -1250, 270)
    SetChrPos(0x16, 7000, 0, -2750, 270)
    SetChrPos(0x17, 8750, 0, -1800, 270)
    SetChrPos(0x18, 8250, 0, -750, 270)
    SetChrPos(0x19, 8000, 0, -3200, 270)
    SetChrPos(0x1A, 10250, 0, -1550, 270)
    SetChrPos(0x1B, 10500, 0, -2800, 270)
    OP_68(-4000, 1000, -2000, 0)
    MoveCamera(28, 30, 0, 0)
    OP_6E(510, 0)
    SetCameraDistance(17500, 0)
    OP_0D()

    #C0066
    ChrTalk(
        0x101,
        "#00006F#11Pふう……\x02",
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0x103,
        "#00206F#11P……やれやれです。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0x105,
        (
            "#10403F#12Pさすがに結構、\x01",
            "ピンチだったかもね。\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0x13,
        (
            "#03209F#6Pフフ、お役に立てて\x01",
            "何よりですよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_42D1():
        OP_93(0x101, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_42D1)
    Sleep(50)

    def lambda_42E1():
        OP_93(0x103, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_42E1)
    Sleep(50)

    def lambda_42F1():
        OP_93(0x105, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x105, 0, lambda_42F1)
    Sleep(50)

    def lambda_4301():
        OP_93(0x107, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x107, 0, lambda_4301)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x105, 0)
    WaitChrThread(0x107, 0)
    SetChrSubChip(0x107, 0x5)
    OP_68(-1750, 1000, -2000, 3000)
    MoveCamera(40, 20, 0, 3000)
    OP_6E(510, 3000)
    SetCameraDistance(20000, 3000)

    def lambda_4353():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_4353)
    Sleep(50)

    def lambda_436B():
        OP_9B(0x0, 0xFE, 0x0, 0x1770, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_436B)
    Sleep(50)

    def lambda_4383():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_4383)
    Sleep(50)

    def lambda_439B():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 1, lambda_439B)
    Sleep(50)

    def lambda_43B3():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_43B3)
    Sleep(50)

    def lambda_43CB():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_43CB)
    Sleep(50)

    def lambda_43E3():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_43E3)
    Sleep(50)

    def lambda_43FB():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_43FB)
    Sleep(50)

    def lambda_4413():
        OP_9B(0x0, 0xFE, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4413)
    OP_6F(0x79)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0xFFFFD8F0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)
    SetMessageWindowPos(14, 280, 35, 3)
    Sleep(500)

    #A0070
    AnonymousTalk(
        0x13,
        (
            "お久しぶりですね。\x01",
            "ロイドさん、皆さん。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CB(0x1, 0x0, 0x0, 0x0, 0x1F4, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CC(0x0, 0x1, 0x0)

    #C0071
    ChrTalk(
        0x101,
        (
            "#00001F#6Pツァオさん……\x01",
            "それに──\x02",
        )
    )

    CloseMessageWindow()
    OP_68(-750, 1000, -500, 1500)
    SetCameraDistance(19000, 1500)
    SetChrChip(0x0, 0x106, 0x32, 0xC8)
    SetChrChipByIndex(0x106, 0x42)
    SetChrSubChip(0x106, 0x1)
    ClearChrFlags(0x106, 0x2)
    Sound(844, 0, 50, 0)
    Sound(809, 0, 50, 0)
    OP_9D(0x106, 0xFFFFFE0C, 0x0, 0x0, 0x3E8, 0x2710)
    SetChrSubChip(0x106, 0x0)
    Sound(326, 0, 50, 0)
    Sleep(500)
    SetChrChipByIndex(0x106, 0xFF)
    SetChrSubChip(0x106, 0x0)
    OP_93(0x106, 0xB4, 0x1F4)
    OP_6F(0x79)
    Sleep(300)
    SetChrChip(0x1, 0x106, 0x0, 0x0)

    #C0072
    ChrTalk(
        0x106,
        "#10708F#5P……………………………\x02",
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x103,
        "#00208F#6Pリーシャさん……\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x101,
        (
            "#00000F#6Pそうか……\x01",
            "彼らと一緒にいたんだな。\x02",
        )
    )

    CloseMessageWindow()

    #C0075
    ChrTalk(
        0x106,
        (
            "#10703F#5P……はい。\x02\x03",

            "#10711Fここでは何ですから\x01",
            "場所を移しましょう。\x02",
        )
    )

    CloseMessageWindow()

    #C0076
    ChrTalk(
        0x13,
        (
            "#03204F#11Pフフ、そうですね。\x02\x03",

            "#03210Fせっかくの再会ですし、\x01",
            "見晴らしのいい場所に行きましょうか。\x02",
        )
    )

    CloseMessageWindow()
    SetCameraDistance(19500, 1500)
    FadeToDark(1500, 0, -1)
    OP_0D()
    StopBGM(0xFA0)
    WaitBGM()
    OP_CC(0x1, 0xFF, 0x0)
    SetScenarioFlags(0x22, 0)
    NewScene("r3060", 0, 0, 0)
    IdleLoop()
    Return()

    # Function_11_2616 end

    def Function_12_46BF(): pass

    label("Function_12_46BF")

    TurnDirection(0xFE, 0xB, 0)
    EndChrThread(0xFE, 0x3)
    SetChrChipByIndex(0xF, 0x20)
    SetChrSubChip(0xF, 0x0)
    OP_52(0xFE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xFE, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_46ED():
        OP_A6(0xFE, 0x0, 0x32, 0x12C, 0xBB8)
        ExitThread()

    QueueWorkItem(0xF, 2, lambda_46ED)
    OP_9B(0x1, 0xFE, 0x0, 0xFFFFFE0C, 0x2710, 0x0)
    BeginChrThread(0xF, 3, 0, 9)
    Return()

    # Function_12_46BF end

    SaveToFile()

Try(main)
