from ScenarioHelper import *

def main():
    CreateScenaFile(
        "m4220.bin",                # FileName
        "m4220",                    # MapName
        "m4220",                    # Location
        0x007F,                     # MapIndex
        "ed7573",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x29,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 127, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4220",                  # 0
        "诺艾尔",                 # 1
        "瓦吉",                   # 2
        "游击士艾欧莉娅",         # 3
        "游击士林",               # 4
        "狂暴花",                 # 5
        "bm4200",                 # 6
        "bm4200",                 # 7
        "bm4200",                 # 8
        "bm4200",                 # 9
    ))

    ATBonus("ATBonus_3A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_3541", 4,   2,   10,  4,   8,   2,   10)
    Sepith("Sepith_3539", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_3529", 8,   8,   6,   6,   6,   8,   6)

    MonsterBattlePostion("MonsterBattlePostion_3D4", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3EC", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_454", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_458", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_45C", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_460", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_464", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_468", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_46C", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_40C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_410", 8, 14, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_5AC", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_3541", 40, 30, 20, 0,
        (
            ("ms86800.dat", "ms82700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_510", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_3539", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_474", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_3529", 50, 25, 25, 0,
        (
            ("ms78200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms78200.dat", "ms78200.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms78200.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_648", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm4200", 0x00000000, 100, 0, 0, 0,
        (
            ("ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "ms86800.dat", "ms82700.dat", "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7451", "ed7453", "ATBonus_3B4"),
            (),
            (),
            (),
        )
    )

    AddCharChip((
        "chr/ch02900.itc",                   # 00
        "chr/ch03000.itc",                   # 01
        "apl/ch51406.itc",                   # 02
        "apl/ch51407.itc",                   # 03
        "chr/ch32053.itc",                   # 04
        "apl/ch51447.itc",                   # 05
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
        "monster/ch78250.itc",               # 10
        "monster/ch78251.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "monster/ch83350.itc",               # 16
        "monster/ch83351.itc",               # 17
        "monster/ch86850.itc",               # 18
        "monster/ch86850.itc",               # 19
    ))

    DeclNpc(44360,   0,       -7019,   270,  389,  0x0, 0,   0,   0,   0,   0,   0,   11,  255,  0)
    DeclNpc(44360,   0,       -7019,   270,  389,  0x0, 0,   1,   0,   0,   0,   0,   12,  255,  0)
    DeclNpc(43279,   0,       -5500,   180,  389,  0x0, 0,   2,   0,   255, 255, 0,   13,  255,  0)
    DeclNpc(42290,   0,       -5570,   180,  389,  0x0, 0,   3,   0,   255, 255, 0,   14,  255,  0)
    DeclNpc(-43500,  500,     -28000,  0,    484,  0x0, 0,   24,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(-600,    -17390,  0,       0x101002D,    "BattleInfo_5AC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-44230,  -6120,   0,       0x1010087,    "BattleInfo_510", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(-33410,  8380,    0,       0x1010087,    "BattleInfo_510", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(-73170,  -4920,   0,       0x1010046,    "BattleInfo_5AC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-51030,  -33110,  0,       0x10100FE,    "BattleInfo_510", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(-81580,  -31370,  0,       0x10100D2,    "BattleInfo_474", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-113720, -45730,  0,       0x1010062,    "BattleInfo_5AC", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-123610, -6900,   0,       0x1010094,    "BattleInfo_474", 0,   16,  0xFFFF, 0,  1)

    DeclActor(-6000,   0,       -39000,  1200,    -6000,   1000,    -39000,  0x007C, 0,  5,  0x0000)
    DeclActor(-33000,  0,       15000,   1200,    -33000,  1000,    15000,   0x007C, 0,  6,  0x0000)
    DeclActor(-43500,  0,       -28000,  1200,    -43500,  1000,    -28000,  0x007C, 0,  7,  0x0000)
    DeclActor(-44000,  0,       1000,    1200,    -44000,  1000,    1000,    0x007C, 0,  8,  0x0000)
    DeclActor(-77500,  0,       0,       1200,    -77500,  1000,    0,       0x007C, 0,  9,  0x0000)
    DeclActor(-132500, 0,       -20500,  1200,    -132500, 1000,    -20500,  0x007C, 0,  10, 0x0000)
    DeclActor(-130000, 0,       19000,   1200,    -130000, 1000,    19000,   0x007C, 0,  15, 0x0000)

    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 5])                   # 5

    ScpFunction((
        "Function_0_734",          # 00, 0
        "Function_1_7E4",          # 01, 1
        "Function_2_801",          # 02, 2
        "Function_3_850",          # 03, 3
        "Function_4_FD8",          # 04, 4
        "Function_5_100D",         # 05, 5
        "Function_6_1148",         # 06, 6
        "Function_7_1283",         # 07, 7
        "Function_8_1481",         # 08, 8
        "Function_9_15DA",         # 09, 9
        "Function_10_1715",        # 0A, 10
        "Function_11_1850",        # 0B, 11
        "Function_12_1AB9",        # 0C, 12
        "Function_13_1D02",        # 0D, 13
        "Function_14_1DE4",        # 0E, 14
        "Function_15_1F69",        # 0F, 15
        "Function_16_204D",        # 10, 16
        "Function_17_2088",        # 11, 17
        "Function_18_20C0",        # 12, 18
        "Function_19_2116",        # 13, 19
        "Function_20_2173",        # 14, 20
        "Function_21_21CF",        # 15, 21
        "Function_22_2225",        # 16, 22
        "Function_23_34E4",        # 17, 23
    ))


    def Function_0_734(): pass

    label("Function_0_734")

    Switch(
        (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_END)),
        (0, "loc_76C"),
        (1, "loc_778"),
        (2, "loc_784"),
        (3, "loc_790"),
        (4, "loc_79C"),
        (5, "loc_7A8"),
        (6, "loc_7B4"),
        (SWITCH_DEFAULT, "loc_7C0"),
    )


    label("loc_76C")

    OP_A0(0xFE, 1450, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_778")

    OP_A0(0xFE, 1550, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_784")

    OP_A0(0xFE, 1600, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_790")

    OP_A0(0xFE, 1400, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_79C")

    OP_A0(0xFE, 1650, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7A8")

    OP_A0(0xFE, 1350, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7B4")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7C0")

    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7CC")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_7E3")
    OP_A0(0xFE, 1500, 0x0, 0xFB)
    Jump("loc_7CC")

    label("loc_7E3")

    Return()

    # Function_0_734 end

    def Function_1_7E4(): pass

    label("Function_1_7E4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_800")
    OP_A1(0xFE, 0x320, 0x6, 0x0, 0x1, 0x2, 0x3, 0x4, 0x5)
    Jump("Function_1_7E4")

    label("loc_800")

    Return()

    # Function_1_7E4 end

    def Function_2_801(): pass

    label("Function_2_801")

    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_834")
    Event(0, 22)

    label("loc_834")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_84F")
    Call(0, 4)
    ClearChrFlags(0xA, 0x80)
    ClearChrFlags(0xB, 0x80)

    label("loc_84F")

    Return()

    # Function_2_801 end

    def Function_3_850(): pass

    label("Function_3_850")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x165, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_872")
    LoadEffect(0x9, "event/ev14011.eff")

    label("loc_872")

    OP_52(0x12, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD9), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x11, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x12, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x14, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x13, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F5A")
    OP_70(0x0, 0x0)
    Jump("loc_F5E")

    label("loc_F5A")

    OP_70(0x0, 0x1E)

    label("loc_F5E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F71")
    OP_70(0x1, 0x0)
    Jump("loc_F75")

    label("loc_F71")

    OP_70(0x1, 0x1E)

    label("loc_F75")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F88")
    OP_70(0x2, 0x0)
    Jump("loc_F8C")

    label("loc_F88")

    OP_70(0x2, 0x1E)

    label("loc_F8C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F9F")
    OP_70(0x3, 0x0)
    Jump("loc_FA3")

    label("loc_F9F")

    OP_70(0x3, 0x1E)

    label("loc_FA3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FB6")
    OP_70(0x4, 0x0)
    Jump("loc_FBA")

    label("loc_FB6")

    OP_70(0x4, 0x1E)

    label("loc_FBA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FCD")
    OP_70(0x5, 0x0)
    Jump("loc_FD1")

    label("loc_FCD")

    OP_70(0x5, 0x1E)

    label("loc_FD1")

    Sound(123, 1, 80, 0)
    Return()

    # Function_3_850 end

    def Function_4_FD8(): pass

    label("Function_4_FD8")

    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_FF7")
    ClearChrFlags(0x8, 0x80)

    label("loc_FF7")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_LEQ), scpexpr(EXPR_END)), "loc_100C")
    ClearChrFlags(0x9, 0x80)

    label("loc_100C")

    Return()

    # Function_4_FD8 end

    def Function_5_100D(): pass

    label("Function_5_100D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10FF")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA1, 1)"), scpexpr(EXPR_END)), "loc_1090")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_10FA")

    label("loc_1090")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10FA")

    Jump("loc_113C")

    label("loc_10FF")

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

    label("loc_113C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_100D end

    def Function_6_1148(): pass

    label("Function_6_1148")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_123A")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E8, 1)"), scpexpr(EXPR_END)), "loc_11CB")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1235")

    label("loc_11CB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1235")

    Jump("loc_1277")

    label("loc_123A")

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

    label("loc_1277")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1148 end

    def Function_7_1283(): pass

    label("Function_7_1283")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1443")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1380")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_12E0():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_12E0)

    def lambda_12FA():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_12FA)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

    #A0007
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "出现了魔兽！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_648", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_1361"),
        (2, "loc_1370"),
        (1, "loc_137D"),
        (SWITCH_DEFAULT, "loc_1380"),
    )


    label("loc_1361")

    SetScenarioFlags(0x217, 4)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_1380")

    label("loc_1370")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_137D")

    OP_B9(0x0)
    Return()

    label("loc_1380")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x72, 1)"), scpexpr(EXPR_END)), "loc_13D7")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_143E")

    label("loc_13D7")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_143E")

    Jump("loc_1475")

    label("loc_1443")

    FadeToDark(300, 0, 100)

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

    label("loc_1475")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1283 end

    def Function_8_1481(): pass

    label("Function_8_1481")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15AB")
    Sound(14, 0, 100, 0)
    OP_74(0x3, 0x1E)
    OP_71(0x3, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    OP_70(0x3, 0x1E)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 80)
    AddSepith(0x1, 80)
    AddSepith(0x2, 80)
    AddSepith(0x3, 80)
    AddSepith(0x4, 80)
    AddSepith(0x5, 80)
    AddSepith(0x6, 80)

    #A0011
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x2),
            "#56I地之耀晶片×８０\x01\x07\x02",

            "#57I水之耀晶片×８０\x01\x07\x02",

            "#58I火之耀晶片×８０\x01\x07\x02",

            "#59I风之耀晶片×８０\x01\x07\x02",

            "#60I时之耀晶片×８０\x01\x07\x02",

            "#61I空之耀晶片×８０\x01\x07\x02",

            "#62I幻之耀晶片×８０\x01\x07\x00",
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F3, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_15C8")

    label("loc_15AB")


    #A0012
    AnonymousTalk(
        0x3E7,
        (
            scpstr(0x6),
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "宝箱里什么也没有。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)

    label("loc_15C8")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1481 end

    def Function_9_15DA(): pass

    label("Function_9_15DA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16CC")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_165D")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0013
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
    SetScenarioFlags(0x1F3, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_16C7")

    label("loc_165D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_16C7")

    Jump("loc_1709")

    label("loc_16CC")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
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

    label("loc_1709")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_15DA end

    def Function_10_1715(): pass

    label("Function_10_1715")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1807")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1798")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0016
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1802")

    label("loc_1798")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1802")

    Jump("loc_1844")

    label("loc_1807")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0018
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

    label("loc_1844")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1715 end

    def Function_11_1850(): pass

    label("Function_11_1850")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_185D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB5")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",            # 0
            "与瓦吉换班\x01",      # 1
            "放弃\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1928")

    #C0019
    ChrTalk(
        0x105,
        "#10300F接下来就拜托你啦。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "#10100F嗯，交给我吧！\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0x4, 0xF9, 0x0)
    OP_32(0x8, 0xF9, 0x0)
    RemoveParty(0x4, 0xFF)
    ClearChrFlags(0x9, 0x80)
    RemoveParty(0x8, 0xFF)
    AddParty(0x8, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x8)
    OP_37()
    Call(0, 4)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_1AB0")

    label("loc_1928")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_193C")
    Jump("loc_1AB0")

    label("loc_193C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1AB0")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A34")

    #C0021
    ChrTalk(
        0x8,
        (
            "#10101F约鲁古大师所说的那名\x01",
            "被冠以『钢』之别称的达人……\x01",
            "似乎真的不是寻常之辈。\x02\x03",

            "#10103F……亚里欧斯先生他们\x01",
            "再过不久就能到达了。\x02\x03",

            "#10101F我们也已经确保了两位游击士的平安，\x01",
            "接下来请一定不要太过勉强。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1AB0")

    label("loc_1A34")


    #C0022
    ChrTalk(
        0x8,
        (
            "#10103F……亚里欧斯先生他们\x01",
            "再过不久就能到达了。\x02\x03",

            "#10101F我们也已经确保了两位游击士的平安，\x01",
            "接下来请一定不要太过勉强。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1AB0")

    Jump("loc_185D")

    label("loc_1AB5")

    TalkEnd(0xFE)
    Return()

    # Function_11_1850 end

    def Function_12_1AB9(): pass

    label("Function_12_1AB9")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1AC6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CFE")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "对话\x01",              # 0
            "与诺艾尔换班\x01",      # 1
            "放弃\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B99")

    #C0023
    ChrTalk(
        0x109,
        "#10100F瓦吉，接下来就交给你啦！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        "#10300F呵呵，知道了。\x02",
    )

    CloseMessageWindow()
    FadeToDark(500, 0, -1)
    OP_0D()
    OP_32(0x4, 0xF9, 0x0)
    OP_32(0x8, 0xF9, 0x0)
    RemoveParty(0x8, 0xFF)
    ClearChrFlags(0x8, 0x80)
    RemoveParty(0x4, 0xFF)
    AddParty(0x4, 0xF4, 0xFF)
    OP_CF(0x1, 0xF4, 0x4)
    OP_37()
    Call(0, 4)
    FadeToBright(500, 0)
    OP_0D()
    Jump("loc_1CF9")

    label("loc_1B99")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BAD")
    Jump("loc_1CF9")

    label("loc_1BAD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CF9")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C91")

    #C0025
    ChrTalk(
        0x9,
        (
            "#10301F似乎正如约鲁古老人所说，\x01",
            "来到这里的尽是些在『结社』中\x01",
            "也算是最危险的人物啊。\x02\x03",

            "#10304F如果就这样返回克洛斯贝尔市，\x01",
            "实在是有些于心不甘……\x02\x03",

            "#10300F我们至少要探明\x01",
            "他们的企图。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1CF9")

    label("loc_1C91")


    #C0026
    ChrTalk(
        0x9,
        (
            "#10303F如果就这样返回克洛斯贝尔市，\x01",
            "实在是有些于心不甘……\x02\x03",

            "#10300F我们至少要探明\x01",
            "『结社』的企图。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1CF9")

    Jump("loc_1AC6")

    label("loc_1CFE")

    TalkEnd(0xFE)
    Return()

    # Function_12_1AB9 end

    def Function_13_1D02(): pass

    label("Function_13_1D02")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D91")

    #C0027
    ChrTalk(
        0xFE,
        "呼……幸好林平安无事。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "『结社』的那些家伙\x01",
            "恐怕并没有拿出全力呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "……不过，他们在这种地方\x01",
            "究竟要做什么……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1DE0")

    label("loc_1D91")


    #C0030
    ChrTalk(
        0xFE,
        "不管怎么说，林没事就好……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "不过，『结社』的那些家伙\x01",
            "究竟要做什么……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1DE0")

    TalkEnd(0xFE)
    Return()

    # Function_13_1D02 end

    def Function_14_1DE4(): pass

    label("Function_14_1DE4")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EEE")

    #C0032
    ChrTalk(
        0xFE,
        (
            "『小丑』和那些骑士装扮\x01",
            "的女孩固然很难对付……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "但那个戴着诡异面具的家伙\x01",
            "更是远非他们可比。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "老实说，即使是传说中的刺客，\x01",
            "恐怕也非其敌……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F……阻吾路者，下场唯有灭亡。\x02\x03",

            "与其担心这种多余之事，\x01",
            "不如专心治疗自身的伤势。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_1F65")

    label("loc_1EEE")


    #C0036
    ChrTalk(
        0xFE,
        (
            "那个戴着诡异面具的家伙\x01",
            "实在是太强大了。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "老实说，即使是传说中的刺客，\x01",
            "恐怕也非其敌……\x01",
            "各位千万要多加小心啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F65")

    TalkEnd(0xFE)
    Return()

    # Function_14_1DE4 end

    def Function_15_1F69(): pass

    label("Function_15_1F69")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0038
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有恢复导力的装置。\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "在这里休息\x01",      # 0
            "放弃\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_203E")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x6, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x6, 0x0)
    OP_71(0x6, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x6)
    OP_71(0x6, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x6, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_203E")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_15_1F69 end

    def Function_16_204D(): pass

    label("Function_16_204D")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x258, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x0)
    Sleep(100)
    Return()

    # Function_16_204D end

    def Function_17_2088(): pass

    label("Function_17_2088")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x320, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x320, 0xFA0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(400)
    Return()

    # Function_17_2088 end

    def Function_18_20C0(): pass

    label("Function_18_20C0")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    Sleep(100)
    OP_9B(0x0, 0xFE, 0x159, 0x4B0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_18_20C0 end

    def Function_19_2116(): pass

    label("Function_19_2116")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x5DC, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xDAC, 0xFA0, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_19_2116 end

    def Function_20_2173(): pass

    label("Function_20_2173")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
    Sleep(100)
    OP_9B(0x0, 0xFE, 0x2D, 0x6D6, 0xFA0, 0x0)
    Sleep(50)
    OP_9B(0x0, 0xFE, 0x15E, 0x9C4, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x154, 0x5DC, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x3E8, 0x7D0, 0x0)
    Sleep(250)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_20_2173 end

    def Function_21_21CF(): pass

    label("Function_21_21CF")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x0)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0xA, 0x41A, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0x15E, 0x41A, 0x7D0, 0x0)
    OP_93(0xFE, 0x10E, 0x1F4)
    Sleep(400)
    OP_93(0xFE, 0x13B, 0x1F4)
    OP_93(0xFE, 0x2D, 0x1F4)
    Sleep(400)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(400)
    Return()

    # Function_21_21CF end

    def Function_22_2225(): pass

    label("Function_22_2225")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51448.itc", 0x1E)
    LoadEffect(0x2, "event/ev17017.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_225F")
    OP_CF(0x1, 0xF4, 0x8)

    label("loc_225F")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2273")
    OP_CF(0x1, 0xF4, 0x4)

    label("loc_2273")

    OP_68(40820, 1000, -18740, 0)
    MoveCamera(36, 19, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(18000, 0)
    SetChrPos(0x101, 40750, 0, -21250, 0)
    SetChrPos(0x102, 42250, 0, -21250, 0)
    SetChrPos(0x103, 40150, 0, -22500, 0)
    SetChrPos(0x104, 42850, 0, -22500, 0)
    SetChrPos(0x106, 40750, 0, -23750, 0)
    SetChrPos(0xF4, 42250, 0, -23750, 0)
    ClearChrFlags(0x4, 0x80)
    ClearChrBattleFlags(0x4, 0x8000)
    ClearChrFlags(0x5, 0x80)
    ClearChrBattleFlags(0x5, 0x8000)
    SetChrPos(0xB, 37500, 0, -6000, 180)
    ClearChrFlags(0xB, 0x80)
    SetChrFlags(0xB, 0x8000)
    SetChrChipByIndex(0xB, 0x4)
    SetChrSubChip(0xB, 0x3)
    ClearChrBattleFlags(0xA, 0x4)
    SetChrFlags(0xA, 0x80)
    PlayEffect(0x9, 0x7, 0xB, 0x5, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 1000)
    OP_68(40430, 1000, -16630, 1500)
    FadeToBright(1000, 0)

    def lambda_239E():
        OP_9B(0x0, 0x101, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_239E)
    Sleep(30)

    def lambda_23B6():
        OP_9B(0x0, 0x102, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_23B6)
    Sleep(30)

    def lambda_23CE():
        OP_9B(0x0, 0x103, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_23CE)
    Sleep(30)

    def lambda_23E6():
        OP_9B(0x0, 0x104, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_23E6)
    Sleep(30)

    def lambda_23FE():
        OP_9B(0x0, 0xF4, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_23FE)
    Sleep(30)

    def lambda_2416():
        OP_9B(0x0, 0x106, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_2416)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x102, 0)
    WaitChrThread(0x103, 0)
    WaitChrThread(0x104, 0)
    WaitChrThread(0xF4, 0)
    WaitChrThread(0x106, 0)
    OP_0D()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)

    #C0039
    ChrTalk(
        0x101,
        "#00013F#11P……！\x02",
    )

    CloseMessageWindow()

    #C0040
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P在这里。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(37480, 1000, -6000, 3000)
    MoveCamera(45, 18, 0, 3000)
    OP_6E(650, 3000)
    SetCameraDistance(15500, 3000)
    BeginChrThread(0x101, 3, 0, 16)
    Sleep(50)
    BeginChrThread(0x102, 3, 0, 17)
    Sleep(50)
    BeginChrThread(0x103, 3, 0, 18)
    Sleep(50)
    BeginChrThread(0x104, 3, 0, 19)
    Sleep(50)
    BeginChrThread(0x106, 3, 0, 21)
    Sleep(50)
    BeginChrThread(0xF4, 3, 0, 20)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x103, 3)
    WaitChrThread(0x104, 3)
    WaitChrThread(0xF4, 3)
    WaitChrThread(0x106, 3)

    #C0041
    ChrTalk(
        0x101,
        (
            "#00010F#12P唔……\x01",
            "林小姐！你不要紧吧！？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        (
            "#00208F#6P……看起来，\x01",
            "性命并无大碍……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P大概是耗尽了全部力量，\x01",
            "最后不支倒地吧。\x02\x03",

            "#00702F闪开，我来为她注入气力。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2644():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2644)
    Sleep(50)

    def lambda_2654():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2654)
    Sleep(50)

    def lambda_2664():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2664)
    Sleep(50)

    def lambda_2674():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2674)
    Sleep(50)

    def lambda_2684():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2684)
    Sleep(50)
    Sleep(300)

    #C0044
    ChrTalk(
        0x101,
        "#00011F#5P啊……嗯，拜托了。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 2)

    def lambda_26BD():
        OP_96(0xFE, 0x8930, 0x0, 0xFFFFE4BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26BD)
    Sleep(350)

    def lambda_26DA():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_26DA)
    Sleep(300)

    def lambda_26F2():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_26F2)
    Sleep(50)

    def lambda_2702():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2702)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x106, 1)
    WaitChrThread(0x101, 2)
    WaitChrThread(0x102, 2)
    Sleep(300)
    SetCameraDistance(14660, 2000)
    Sound(2580, 255, 100, 0)    #voice#Yin

    #C0045
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#60W#10A#00700F………噢噢噢噢………\x07\x00\x02",
        )
    )
    #Auto

    CloseMessageWindow()
    OP_6F(0x79)
    Sleep(500)
    BlurSwitch(0x1F4, 0xBBFFFFFF, 0x0, 0x1, 0xA)
    OP_82(0xC8, 0x0, 0xBB8, 0x12C)
    Sound(253, 0, 60, 0)
    Sound(2590, 255, 100, 0)    #voice#Yin

    #C0046
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#11P#4S#00707F……喝！#12A\x07\x00\x02",
        )
    )
    #Auto

    Sleep(300)
    PlayEffect(0x2, 0xFF, 0xB, 0x1, 0, 350, 0, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(200)
    StopEffect(0x7, 0x2)
    Sound(833, 0, 30, 0)
    CancelBlur(500)
    CloseMessageWindow()

    def lambda_27FF():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_27FF)
    Sleep(50)

    def lambda_280F():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_280F)
    Sleep(50)

    def lambda_281F():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_281F)
    Sleep(500)

    def lambda_282F():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_282F)
    WaitChrThread(0xB, 2)
    Sleep(500)

    #C0047
    ChrTalk(
        0xB,
        "#5P#50W呜……\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_9B(0x0, 0x104, 0x159, 0x2BC, 0x7D0, 0x0)
    SetChrChipByIndex(0x104, 0x1E)
    SetChrSubChip(0x104, 0x0)
    SetChrFlags(0x104, 0x1000)
    SetChrFlags(0x104, 0x20)
    SetChrFlags(0x104, 0x2)
    SetChrChipByIndex(0xB, 0x5)
    SetChrSubChip(0xB, 0x0)
    SetChrFlags(0xB, 0x1000)
    SetChrFlags(0xB, 0x20)
    SetChrFlags(0xB, 0x2)
    SetChrPos(0xB, 37500, -70, -6000, 180)
    Sleep(300)
    SetCameraDistance(13500, 0)
    FadeToBright(1000, 0)
    SetCameraDistance(14000, 2000)
    Sleep(1000)
    BeginChrThread(0xB, 0, 0, 23)
    Sleep(1000)

    def lambda_28E5():
        OP_9B(0x1, 0xFE, 0xF, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_28E5)
    WaitChrThread(0x106, 1)

    #C0048
    ChrTalk(
        0xB,
        "#5P#30W……唔………\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "#5P#30W这样啊……原来我当时\x01",
            "就那么晕过去了……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00000F#6P林小姐……你好像已经\x01",
            "理解了如今的状况啊。\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        "#5P#30W嗯……真丢脸……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        (
            "#5P#30W……对了……\x01",
            "艾欧莉娅没事吧……？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#00104F#12P是的，不必担心。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "罗伊德等人向林说明了\x01",
            "至今为止的事情经过。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0055
    ChrTalk(
        0xB,
        (
            "#5P#30W……这样啊……\x01",
            "真是太感谢你们了……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "#5P#30W唔……\x01",
            "看来我的修行还远远不足……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "#5P#30W竟然会被对方\x01",
            "像小孩子一样戏耍……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2AF0")

    #C0058
    ChrTalk(
        0x109,
        (
            "#10101F#11P是指那些骑士打扮\x01",
            "的女孩吗？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B1C")

    label("loc_2AF0")


    #C0059
    ChrTalk(
        0x105,
        (
            "#10301F#11P是指那些骑士打扮\x01",
            "的女孩吗？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B1C")


    #C0060
    ChrTalk(
        0xB,
        (
            "#5P#30W……不……\x01",
            "她们虽然也很强，\x01",
            "但还有个远在她们之上的家伙……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "#5P#30W单用强字，根本不足以形容……\x01",
            "……彼此间的差距简直有如云泥之别……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xB,
        (
            "#5P#30W恐怕连亚里欧斯先生\x01",
            "都不是那个人的对手……\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x103, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0x104, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(50)
    OP_63(0x106, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    OP_63(0xF4, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_82(0x64, 0x0, 0xBB8, 0x12C)

    #C0063
    ChrTalk(
        0x101,
        "#00007F#6P什、什么……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00307F#5P喂喂……\x01",
            "这怎么可能？！\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#00108F#12P莫非是约鲁古大师\x01",
            "所说的『使徒』之一……？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00201F#6P恐怕正是那个被冠以『钢』\x01",
            "之别称的武术达人……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xB,
        "#5P#30W……多半如此吧。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "#5P#30W另外，一名叫做『小丑』的少年\x01",
            "与一名白衣中年男性也在一起……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            "#5P#30W就算有传说中的刺客与你们同行……\x01",
            "恐怕也不是他们的对手……\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#00008F#6P这……\x02",
    )

    CloseMessageWindow()

    #C0071
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P…………………………………\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_68(37280, 1000, -6640, 1500)
    OP_96(0x106, 0x8D18, 0x0, 0xFFFFDFBC, 0x7D0, 0x1)
    OP_93(0x106, 0xE1, 0x190)

    def lambda_2E6C():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2E6C)
    Sleep(50)

    def lambda_2E7C():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2E7C)
    Sleep(50)

    def lambda_2E8C():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2E8C)
    Sleep(50)

    def lambda_2E9C():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2E9C)
    Sleep(50)

    def lambda_2EAC():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2EAC)
    Sleep(250)

    #C0072
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P吾既为『银』，\x01",
            "无论对手是何方神圣，\x01",
            "在情势需要下，也都会将其灭杀。\x02\x03",

            "#00702F你们要是害怕了，\x01",
            "我们就在此别过。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#00013F#5P等、等一下！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#00107F#11P就算是你，独自一人\x01",
            "前去也太过莽撞了！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FE2")

    #C0075
    ChrTalk(
        0x109,
        (
            "#10101F#11P总、总之，我们先联络瓦吉，\x01",
            "把林小姐交给他来照料吧。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3026")

    label("loc_2FE2")


    #C0076
    ChrTalk(
        0x105,
        (
            "#10306F#11P总之，我们先联络诺艾尔，\x01",
            "把这位姐姐交给她来照料吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3026")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3065")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 40670, 0, -5530, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    Jump("loc_3084")

    label("loc_3065")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 40670, 0, -5530, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    label("loc_3084")

    ClearChrFlags(0xA, 0x80)
    SetChrPos(0xA, 43280, 0, -5500, 180)
    ClearChrFlags(0xA, 0x1000)
    ClearChrFlags(0xA, 0x20)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 0x2)
    SetChrSubChip(0xA, 0x0)
    EndChrThread(0xA, 0x0)
    SetChrBattleFlags(0xA, 0x4)
    SetChrSubChip(0xA, 0x2)
    SetChrPos(0xB, 42290, 0, -5570, 180)
    ClearChrFlags(0xB, 0x1000)
    ClearChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x2)
    SetChrChipByIndex(0xB, 0x3)
    SetChrSubChip(0xB, 0x0)
    EndChrThread(0xB, 0x0)
    SetChrBattleFlags(0xB, 0x4)
    SetChrSubChip(0xB, 0x2)
    SetChrChipByIndex(0x104, 0xFF)
    SetChrSubChip(0x104, 0x0)
    ClearChrFlags(0x104, 0x1000)
    ClearChrFlags(0x104, 0x20)
    ClearChrFlags(0x104, 0x2)
    SetChrPos(0x101, 39800, 0, -7300, 0)
    SetChrPos(0x102, 41200, 0, -7300, 0)
    SetChrPos(0x103, 39500, 0, -8500, 0)
    SetChrPos(0x104, 41500, 0, -8500, 0)
    SetChrPos(0x106, 39800, 0, -9700, 0)
    SetChrPos(0xF4, 41200, 0, -9700, 0)
    OP_68(41100, 1200, -7240, 0)
    MoveCamera(60, 27, 0, 0)
    OP_6E(650, 0)
    SetCameraDistance(15620, 0)
    Sleep(500)
    SetCameraDistance(14620, 2000)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x79)
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_31FE")

    #C0077
    ChrTalk(
        0x9,
        (
            "#10301F#5P……没问题吗？\x01",
            "对手似乎相当可怕啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3231")

    label("loc_31FE")


    #C0078
    ChrTalk(
        0x8,
        (
            "#10101F#5P没、没问题吗？\x01",
            "听说对手非同寻常啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3231")


    #C0079
    ChrTalk(
        0x101,
        (
            "#00000F#12P嗯……\x01",
            "不管怎么说，先过去看看吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00306F#12P总之，我们就多加小心，\x01",
            "尽量避免和那个叫『钢』\x01",
            "的家伙正面交锋吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#00108F#12P……是啊……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P……………哼。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "#5P#30W嗯，最好如此……\x02\x03",

            "#5P#30W……那个人穿着铠甲，还披着\x01",
            "很长的披风，应该很好辨认……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "#11P亚里欧斯先生他们就快赶到了，\x01",
            "你们一定不要太过逞强。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3393():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3393)
    Sleep(50)

    def lambda_33A3():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_33A3)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    #C0085
    ChrTalk(
        0x101,
        "#00000F#6P嗯，知道了。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#00201F#6P……明白了。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_341E")

    #C0087
    ChrTalk(
        0x109,
        "#10107F#12P我们走吧！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3439")

    label("loc_341E")


    #C0088
    ChrTalk(
        0x105,
        "#10301F#12P我们走吧。\x02",
    )

    CloseMessageWindow()

    label("loc_3439")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_346E")
    SetChrPos(0x9, 44360, 0, -7020, 270)
    OP_4C(0x9, 0xFF)
    Jump("loc_3483")

    label("loc_346E")

    SetChrPos(0x8, 44360, 0, -7020, 270)
    OP_4C(0x8, 0xFF)

    label("loc_3483")

    ClearChrFlags(0xB, 0x8000)
    SetChrPos(0x0, 38980, 0, -8290, 270)
    SetChrFlags(0x4, 0x80)
    SetChrBattleFlags(0x4, 0x8000)
    SetChrFlags(0x5, 0x80)
    SetChrBattleFlags(0x5, 0x8000)
    SetChrPos(0x101, 38980, 0, -8290, 270)
    OP_93(0xB, 0xB4, 0x0)
    OP_93(0xA, 0xB4, 0x0)
    SetChrSubChip(0xB, 0x0)
    SetChrSubChip(0xA, 0x0)
    SetScenarioFlags(0x165, 4)
    OP_29(0xA9, 0x1, 0x6)
    OP_37()
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_22_2225 end

    def Function_23_34E4(): pass

    label("Function_23_34E4")

    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    Return()

    # Function_23_34E4 end

    SaveToFile()

Try(main)
