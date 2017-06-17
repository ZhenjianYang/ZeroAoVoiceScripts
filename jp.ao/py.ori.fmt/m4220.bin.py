from ScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "ノエル",                 # 1
        "ワジ",                   # 2
        "遊撃士エオリア",         # 3
        "遊撃士リン",             # 4
        "マッドブルーム",         # 5
        "bm4200",                 # 6
        "bm4200",                 # 7
        "bm4200",                 # 8
        "bm4200",                 # 9
    ))

    ATBonus("ATBonus_3A4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)
    ATBonus("ATBonus_3B4", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_383A", 4,   2,   10,  4,   8,   2,   10)
    Sepith("Sepith_3832", 5,   2,   8,   8,   2,   8,   2)
    Sepith("Sepith_3822", 8,   8,   6,   6,   6,   8,   6)

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
        "BattleInfo_5AC", 0x0000, 71, 6, 60, 10, 1, 20, 0, "bm4200", "Sepith_383A", 40, 30, 20, 0,
        (
            ("ms86800.dat", "ms82700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms86800.dat", "ms82700.dat", "ms82700.dat", "ms82700.dat", 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_510", 0x0000, 71, 6, 60, 10, 1, 30, 0, "bm4200", "Sepith_3832", 40, 30, 20, 0,
        (
            ("ms83300.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3D4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            ("ms83300.dat", "ms83300.dat", "ms83300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3F4", "MonsterBattlePostion_454", "ed7450", "ed7453", "ATBonus_3A4"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_474", 0x0000, 71, 6, 60, 10, 1, 40, 0, "bm4200", "Sepith_3822", 50, 25, 25, 0,
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
        "Function_6_115E",         # 06, 6
        "Function_7_12AF",         # 07, 7
        "Function_8_14C6",         # 08, 8
        "Function_9_162D",         # 09, 9
        "Function_10_177E",        # 0A, 10
        "Function_11_18CF",        # 0B, 11
        "Function_12_1B92",        # 0C, 12
        "Function_13_1E2B",        # 0D, 13
        "Function_14_1F51",        # 0E, 14
        "Function_15_2106",        # 0F, 15
        "Function_16_2202",        # 10, 16
        "Function_17_223D",        # 11, 17
        "Function_18_2275",        # 12, 18
        "Function_19_22CB",        # 13, 19
        "Function_20_2328",        # 14, 20
        "Function_21_2384",        # 15, 21
        "Function_22_23DA",        # 16, 22
        "Function_23_37DD",        # 17, 23
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110D")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0xA1, 1)"), scpexpr(EXPR_END)), "loc_1096")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 1)
    OP_E0(0x5, 0x0)
    Jump("loc_1108")

    label("loc_1096")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0xA1),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1108")

    Jump("loc_1152")

    label("loc_110D")

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

    label("loc_1152")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_100D end

    def Function_6_115E(): pass

    label("Function_6_115E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_125E")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x5E8, 1)"), scpexpr(EXPR_END)), "loc_11E7")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 2)
    OP_E0(0x5, 0x0)
    Jump("loc_1259")

    label("loc_11E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x5E8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1259")

    Jump("loc_12A3")

    label("loc_125E")

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

    label("loc_12A3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_115E end

    def Function_7_12AF(): pass

    label("Function_7_12AF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1480")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_13AE")
    OP_A7(0xC, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0xC, 0x0, 0)
    OP_98(0xC, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_130C():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_130C)

    def lambda_1326():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0xC, 2, lambda_1326)
    ClearChrFlags(0xC, 0x80)
    SetChrFlags(0xC, 0x8000)

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
    WaitChrThread(0xC, 1)
    Battle("BattleInfo_648", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0xC, 0x80)
    ClearChrFlags(0xC, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_138F"),
        (2, "loc_139E"),
        (1, "loc_13AB"),
        (SWITCH_DEFAULT, "loc_13AE"),
    )


    label("loc_138F")

    SetScenarioFlags(0x217, 4)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_13AE")

    label("loc_139E")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_13AB")

    OP_B9(0x0)
    Return()

    label("loc_13AE")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x72, 1)"), scpexpr(EXPR_END)), "loc_140B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 3)
    OP_E0(0x5, 0x0)
    Jump("loc_147B")

    label("loc_140B")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x72),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_147B")

    Jump("loc_14BA")

    label("loc_1480")

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

    label("loc_14BA")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_12AF end

    def Function_8_14C6(): pass

    label("Function_8_14C6")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15F6")
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
            "#56I地のセピス×８０\x01\x07\x02",

            "#57I水のセピス×８０\x01\x07\x02",

            "#58I火のセピス×８０\x01\x07\x02",

            "#59I風のセピス×８０\x01\x07\x02",

            "#60I時のセピス×８０\x01\x07\x02",

            "#61I空のセピス×８０\x01\x07\x02",

            "#62I幻のセピス×８０\x01\x07\x00",
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    SetScenarioFlags(0x1F3, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_161B")

    label("loc_15F6")


    #A0012
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

    label("loc_161B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_14C6 end

    def Function_9_162D(): pass

    label("Function_9_162D")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172D")
    Sound(14, 0, 100, 0)
    OP_74(0x4, 0x1E)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_16B6")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_1728")

    label("loc_16B6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F6),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x4, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1728")

    Jump("loc_1772")

    label("loc_172D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0015
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

    label("loc_1772")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_162D end

    def Function_10_177E(): pass

    label("Function_10_177E")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1F3, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_187E")
    Sound(14, 0, 100, 0)
    OP_74(0x5, 0x1E)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_1807")
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
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1F3, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_1879")

    label("loc_1807")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0017
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1FD),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x0, 0x0, 0x0)

    label("loc_1879")

    Jump("loc_18C3")

    label("loc_187E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0018
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

    label("loc_18C3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_177E end

    def Function_11_18CF(): pass

    label("Function_11_18CF")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_18DC")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B8E")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",            # 0
            "ワジと交代する\x01",      # 1
            "やめる\x01",              # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19B5")

    #C0019
    ChrTalk(
        0x105,
        "#10300Fそれじゃ、後は頼むよ。\x02",
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x8,
        "#10100Fうん、任せて！\x02",
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
    Jump("loc_1B89")

    label("loc_19B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19C9")
    Jump("loc_1B89")

    label("loc_19C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B89")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1AF5")

    #C0021
    ChrTalk(
        0x8,
        (
            "#10101Fヨルグ・マイスターが言っていた\x01",
            "《鋼》の異名を冠する達人……\x01",
            "本当に尋常じゃない相手みたいですね。\x02\x03",

            "#10103F……アリオスさんたちも\x01",
            "もう少ししたら到着すると思います。\x02\x03",

            "#10101F遊撃士さんたちの保護は出来たんですし、\x01",
            "くれぐれも無理はしないで下さいね。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 0)
    Jump("loc_1B89")

    label("loc_1AF5")


    #C0022
    ChrTalk(
        0x8,
        (
            "#10103Fアリオスさんたちも\x01",
            "もう少ししたら到着すると思います。\x02\x03",

            "#10101F遊撃士さんたちの保護は出来たんですし、\x01",
            "くれぐれも無理はしないで下さいね。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1B89")

    Jump("loc_18DC")

    label("loc_1B8E")

    TalkEnd(0xFE)
    Return()

    # Function_11_18CF end

    def Function_12_1B92(): pass

    label("Function_12_1B92")

    TalkBegin(0xFE)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_1B9F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E27")
    FadeToDark(300, 0, 100)

    Menu(
        0,
        -1,
        -1,
        1,
        (
            "話をする\x01",              # 0
            "ノエルと交代する\x01",      # 1
            "やめる\x01",                # 2
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C7A")

    #C0023
    ChrTalk(
        0x109,
        "#10100Fワジ君、後は任せたよ！\x02",
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x9,
        "#10300Fフフ、了解だ。\x02",
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
    Jump("loc_1E22")

    label("loc_1C7A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C8E")
    Jump("loc_1E22")

    label("loc_1C8E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E22")
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x63), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D98")

    #C0025
    ChrTalk(
        0x9,
        (
            "#10301Fヨルグ老人の言うとおり、\x01",
            "《結社》でもヤバそうな人物ばかりが\x01",
            "来ているみたいだね。\x02\x03",

            "#10304Fこのままクロスベル市に戻るのも\x01",
            "どうにも後味が悪いし……\x02\x03",

            "#10300Fせめて、彼らの企みくらいは\x01",
            "突き止めておきたいところかな。\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 1)
    Jump("loc_1E22")

    label("loc_1D98")


    #C0026
    ChrTalk(
        0x9,
        (
            "#10303Fこのままクロスベル市に戻るのも\x01",
            "どうにも後味が悪いし……\x02\x03",

            "#10300Fせめて、《結社》の企みくらいは\x01",
            "突き止めておきたいところかな。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E22")

    Jump("loc_1B9F")

    label("loc_1E27")

    TalkEnd(0xFE)
    Return()

    # Function_12_1B92 end

    def Function_13_1E2B(): pass

    label("Function_13_1E2B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1EE4")

    #C0027
    ChrTalk(
        0xFE,
        "ふう……リンが無事でよかったわ。\x02",
    )

    CloseMessageWindow()

    #C0028
    ChrTalk(
        0xFE,
        (
            "多分、《結社》の連中も\x01",
            "本気じゃ無かったんでしょうね。\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0xFE,
        (
            "……でも、こんな場所で一体、\x01",
            "何をしようとしているのかしら……\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 2)
    Jump("loc_1F4D")

    label("loc_1EE4")


    #C0030
    ChrTalk(
        0xFE,
        "ともかく、リンが無事でよかったけど……\x02",
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0xFE,
        (
            "《結社》の連中は一体、\x01",
            "何をしようとしているのかしら……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F4D")

    TalkEnd(0xFE)
    Return()

    # Function_13_1E2B end

    def Function_14_1F51(): pass

    label("Function_14_1F51")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_207F")

    #C0032
    ChrTalk(
        0xFE,
        (
            "《道化師》や騎士の格好をした\x01",
            "娘たちも厄介だったが……\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0xFE,
        (
            "あの不気味な仮面の奴は\x01",
            "あまりにも格が違っていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0xFE,
        (
            "正直、伝説の凶手がいても\x01",
            "分が悪いかもしれない……\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F……立ち塞がるなら滅するのみだ。\x02\x03",

            "無用な気を回す余裕があるなら\x01",
            "その身を癒すのに専念するんだな。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    SetScenarioFlags(0x0, 3)
    Jump("loc_2102")

    label("loc_207F")


    #C0036
    ChrTalk(
        0xFE,
        (
            "あの不気味な仮面の奴は\x01",
            "あまりにも格が違っていた。\x02",
        )
    )

    CloseMessageWindow()

    #C0037
    ChrTalk(
        0xFE,
        (
            "正直、伝説の凶手がいても\x01",
            "分が悪いかもしれない……\x01",
            "充分に気をつけなよ。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2102")

    TalkEnd(0xFE)
    Return()

    # Function_14_1F51 end

    def Function_15_2106(): pass

    label("Function_15_2106")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0038
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F3")
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

    label("loc_21F3")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_15_2106 end

    def Function_16_2202(): pass

    label("Function_16_2202")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x258, 0xFA0, 0x0)
    OP_93(0xFE, 0x0, 0x12C)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x320, 0x7D0, 0x0)
    Sleep(100)
    Return()

    # Function_16_2202 end

    def Function_17_223D(): pass

    label("Function_17_223D")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x320, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x159, 0x320, 0xFA0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(400)
    Return()

    # Function_17_223D end

    def Function_18_2275(): pass

    label("Function_18_2275")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    Sleep(100)
    OP_9B(0x0, 0xFE, 0x159, 0x4B0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x1E, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x1)
    OP_9B(0x0, 0xFE, 0xF, 0x4E2, 0x7D0, 0x0)
    TurnDirection(0xFE, 0xB, 500)
    Return()

    # Function_18_2275 end

    def Function_19_22CB(): pass

    label("Function_19_22CB")

    OP_9B(0x0, 0xFE, 0x0, 0x2328, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0xA, 0x5DC, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14, 0x7D0, 0xFA0, 0x1)
    OP_9B(0x0, 0xFE, 0x14A, 0xDAC, 0xFA0, 0x0)
    OP_93(0xFE, 0x13B, 0x1F4)
    TurnDirection(0xFE, 0xB, 500)
    Sleep(250)
    OP_9B(0x0, 0xFE, 0x0, 0x1F4, 0x7D0, 0x0)
    Return()

    # Function_19_22CB end

    def Function_20_2328(): pass

    label("Function_20_2328")

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

    # Function_20_2328 end

    def Function_21_2384(): pass

    label("Function_21_2384")

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

    # Function_21_2384 end

    def Function_22_23DA(): pass

    label("Function_22_23DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadChrToIndex("apl/ch51448.itc", 0x1E)
    LoadEffect(0x2, "event/ev17017.eff")
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2414")
    OP_CF(0x1, 0xF4, 0x8)

    label("loc_2414")

    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2428")
    OP_CF(0x1, 0xF4, 0x4)

    label("loc_2428")

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

    def lambda_2553():
        OP_9B(0x0, 0x101, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_2553)
    Sleep(30)

    def lambda_256B():
        OP_9B(0x0, 0x102, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_256B)
    Sleep(30)

    def lambda_2583():
        OP_9B(0x0, 0x103, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_2583)
    Sleep(30)

    def lambda_259B():
        OP_9B(0x0, 0x104, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x104, 0, lambda_259B)
    Sleep(30)

    def lambda_25B3():
        OP_9B(0x0, 0xF4, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0xF4, 0, lambda_25B3)
    Sleep(30)

    def lambda_25CB():
        OP_9B(0x0, 0x106, 0x154, 0xDAC, 0x898, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 0, lambda_25CB)
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
            "#00700F#12Pいたか。\x07\x00\x02",
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
            "#00010F#12Pくっ……\x01",
            "リンさん、大丈夫ですか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0042
    ChrTalk(
        0x103,
        (
            "#00208F#6P……どうやら命に\x01",
            "別状はなさそうですけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0043
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12Pおそらく力を使い果たして\x01",
            "落ちてしまったのだろう。\x02\x03",

            "#00702Fどけ──活を入れてみる。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2817():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2817)
    Sleep(50)

    def lambda_2827():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2827)
    Sleep(50)

    def lambda_2837():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_2837)
    Sleep(50)

    def lambda_2847():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_2847)
    Sleep(50)

    def lambda_2857():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_2857)
    Sleep(50)
    Sleep(300)

    #C0044
    ChrTalk(
        0x101,
        "#00011F#5Pあ、ああ、頼む。\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 2)

    def lambda_288E():
        OP_96(0xFE, 0x8930, 0x0, 0xFFFFE4BC, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_288E)
    Sleep(350)

    def lambda_28AB():
        OP_9B(0x1, 0xFE, 0x0, 0xBB8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_28AB)
    Sleep(300)

    def lambda_28C3():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_28C3)
    Sleep(50)

    def lambda_28D3():
        OP_93(0xFE, 0x10E, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_28D3)
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
            "#11P#60W#10A#00700F………おおおおっ………\x07\x00\x02",
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
            "#11P#4S#00707F──活#2Rかつ#！#12A\x07\x00\x02",
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

    def lambda_29DA():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_29DA)
    Sleep(50)

    def lambda_29EA():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_29EA)
    Sleep(50)

    def lambda_29FA():
        TurnDirection(0xFE, 0xB, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_29FA)
    Sleep(500)

    def lambda_2A0A():
        OP_A6(0xFE, 0x0, 0x32, 0x1F4, 0xBB8)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_2A0A)
    WaitChrThread(0xB, 2)
    Sleep(500)

    #C0047
    ChrTalk(
        0xB,
        "#5P#50Wう……\x02",
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

    def lambda_2AC0():
        OP_9B(0x1, 0xFE, 0xF, 0xFFFFFE70, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x106, 1, lambda_2AC0)
    WaitChrThread(0x106, 1)

    #C0048
    ChrTalk(
        0xB,
        "#5P#30W……くっ………\x02",
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0xB,
        (
            "#5P#30Wそうか……あのまま\x01",
            "落ちてしまったのか……\x02",
        )
    )

    CloseMessageWindow()

    #C0050
    ChrTalk(
        0x101,
        (
            "#00000F#6Pリンさん……どうやら\x01",
            "状況は掴めてるみたいですね？\x02",
        )
    )

    CloseMessageWindow()

    #C0051
    ChrTalk(
        0xB,
        "#5P#30Wああ……面目ない……\x02",
    )

    CloseMessageWindow()

    #C0052
    ChrTalk(
        0xB,
        (
            "#5P#30W……そうだ……\x01",
            "エオリアは無事なのか……？\x02",
        )
    )

    CloseMessageWindow()

    #C0053
    ChrTalk(
        0x102,
        "#00104F#12Pはい、心配いりません。\x02",
    )

    CloseMessageWindow()
    SetChrName("")

    #A0054
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ロイドたちはリンに\x01",
            "それまでの経緯を説明した。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    #C0055
    ChrTalk(
        0xB,
        (
            "#5P#30W……そうか……\x01",
            "本当に済まなかったな……\x02",
        )
    )

    CloseMessageWindow()

    #C0056
    ChrTalk(
        0xB,
        (
            "#5P#30Wくっ……\x01",
            "まだまだ私も修行不足か……\x02",
        )
    )

    CloseMessageWindow()

    #C0057
    ChrTalk(
        0xB,
        (
            "#5P#30Wまさかああまで\x01",
            "子供扱いされるなんて……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D09")

    #C0058
    ChrTalk(
        0x109,
        (
            "#10101F#11P騎士の格好をしたという\x01",
            "娘たちのことですか？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2D43")

    label("loc_2D09")


    #C0059
    ChrTalk(
        0x105,
        (
            "#10301F#11P騎士の格好をしたという\x01",
            "娘たちのことかい？\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2D43")


    #C0060
    ChrTalk(
        0xB,
        (
            "#5P#30W……いや……\x01",
            "あいつらも手強かったが\x01",
            "一人別格なヤツがいてね……\x02",
        )
    )

    CloseMessageWindow()

    #C0061
    ChrTalk(
        0xB,
        (
            "#5P#30W強いなんてモンじゃない……\x01",
            "……次元が違うと言うべきか……\x02",
        )
    )

    CloseMessageWindow()

    #C0062
    ChrTalk(
        0xB,
        (
            "#5P#30Wひょっとしたらアリオスさんでも\x01",
            "敵わないかもしれない……\x02",
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
        "#00007F#6Pなっ……\x02",
    )

    CloseMessageWindow()

    #C0064
    ChrTalk(
        0x104,
        (
            "#00307F#5Pおいおい……\x01",
            "そんなのあり得んのか！？\x02",
        )
    )

    CloseMessageWindow()

    #C0065
    ChrTalk(
        0x102,
        (
            "#00108F#12Pヨルグさんが言っていた\x01",
            "《使徒》の一人かしら……？\x02",
        )
    )

    CloseMessageWindow()

    #C0066
    ChrTalk(
        0x103,
        (
            "#00201F#6P《鋼#2Rはがね#》の異名を冠した\x01",
            "恐るべき達人らしいですが……\x02",
        )
    )

    CloseMessageWindow()

    #C0067
    ChrTalk(
        0xB,
        "#5P#30W……多分そいつの事だろう。\x02",
    )

    CloseMessageWindow()

    #C0068
    ChrTalk(
        0xB,
        (
            "#5P#30Wそれと《道化師》とかいう少年と\x01",
            "白衣の中年男を見かけた……\x02",
        )
    )

    CloseMessageWindow()

    #C0069
    ChrTalk(
        0xB,
        (
            "#5P#30Wいくら伝説の凶手#4Rきょうしゅ#を連れていても\x01",
            "……分が悪いかもしれないよ……？\x02",
        )
    )

    CloseMessageWindow()

    #C0070
    ChrTalk(
        0x101,
        "#00008F#6Pそれは……\x02",
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

    def lambda_30DD():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_30DD)
    Sleep(50)

    def lambda_30ED():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_30ED)
    Sleep(50)

    def lambda_30FD():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x103, 2, lambda_30FD)
    Sleep(50)

    def lambda_310D():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0x104, 2, lambda_310D)
    Sleep(50)

    def lambda_311D():
        TurnDirection(0xFE, 0x106, 500)
        ExitThread()

    QueueWorkItem(0xF4, 2, lambda_311D)
    Sleep(250)

    #C0072
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#5P──我が名は《銀#2Rイン#》。\x01",
            "どのような相手であろうと\x01",
            "必要とあらば滅するのみだ。\x02\x03",

            "#00702Fお前たちが怖気づくなら\x01",
            "同行はここまでとしよう。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0073
    ChrTalk(
        0x101,
        "#00013F#5Pちょ、ちょっと待った！\x02",
    )

    CloseMessageWindow()

    #C0074
    ChrTalk(
        0x102,
        (
            "#00107F#11Pいくら貴方でも\x01",
            "一人で行くのは無茶だわ！\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_327F")

    #C0075
    ChrTalk(
        0x109,
        (
            "#10101F#11Pと、とりあえずワジ君に連絡して\x01",
            "リンさんを任せましょう。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_32C5")

    label("loc_327F")


    #C0076
    ChrTalk(
        0x105,
        (
            "#10306F#11Pとりあえずノエルに連絡して\x01",
            "このお姉さんを任せようか。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_32C5")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3304")
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 40670, 0, -5530, 180)
    ClearChrFlags(0x9, 0x80)
    OP_4B(0x9, 0xFF)
    Jump("loc_3323")

    label("loc_3304")

    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 40670, 0, -5530, 180)
    ClearChrFlags(0x8, 0x80)
    OP_4B(0x8, 0xFF)

    label("loc_3323")

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
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AB")

    #C0077
    ChrTalk(
        0x9,
        (
            "#10301F#5P……大丈夫かい？\x01",
            "随分ヤバそうな相手みたいだけど。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_34EE")

    label("loc_34AB")


    #C0078
    ChrTalk(
        0x8,
        (
            "#10101F#5Pだ、大丈夫ですか？\x01",
            "尋常ではない相手みたいですけど。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34EE")


    #C0079
    ChrTalk(
        0x101,
        (
            "#00000F#12Pああ……\x01",
            "とにかく様子を伺ってくる。\x02",
        )
    )

    CloseMessageWindow()

    #C0080
    ChrTalk(
        0x104,
        (
            "#00306F#12Pま、《鋼》ってヤツと\x01",
            "やり合うことにならねぇよう、\x01",
            "気をつけておくか。\x02",
        )
    )

    CloseMessageWindow()

    #C0081
    ChrTalk(
        0x102,
        "#00108F#12P……そうね……\x02",
    )

    CloseMessageWindow()

    #C0082
    ChrTalk(
        0x106,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x3),
            "#00700F#12P……………フン。\x07\x00\x02",
        )
    )

    CloseMessageWindow()

    #C0083
    ChrTalk(
        0xB,
        (
            "#5P#30Wああ、それがいいだろう……\x02\x03",

            "#5P#30W……ゴツイ鎧と長いマントを\x01",
            "付けていたから判るはずだ……\x02",
        )
    )

    CloseMessageWindow()

    #C0084
    ChrTalk(
        0xA,
        (
            "#11Pアリオスさんたちも来るんだし、\x01",
            "くれぐれも無茶はしないでね？\x02",
        )
    )

    CloseMessageWindow()

    def lambda_366C():
        TurnDirection(0x101, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_366C)
    Sleep(50)

    def lambda_367C():
        TurnDirection(0x103, 0xA, 500)
        ExitThread()

    QueueWorkItem(0x103, 0, lambda_367C)
    Sleep(50)
    WaitChrThread(0x101, 0)
    WaitChrThread(0x103, 0)

    #C0085
    ChrTalk(
        0x101,
        "#00000F#6Pええ、分かりました。\x02",
    )

    CloseMessageWindow()

    #C0086
    ChrTalk(
        0x103,
        "#00201F#6P……了解です。\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_370D")

    #C0087
    ChrTalk(
        0x109,
        "#10107F#12Pそれでは行きましょう！\x02",
    )

    CloseMessageWindow()
    Jump("loc_3732")

    label("loc_370D")


    #C0088
    ChrTalk(
        0x105,
        "#10301F#12Pそれじゃあ行こうか。\x02",
    )

    CloseMessageWindow()

    label("loc_3732")

    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "GetPartyIndex(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3767")
    SetChrPos(0x9, 44360, 0, -7020, 270)
    OP_4C(0x9, 0xFF)
    Jump("loc_377C")

    label("loc_3767")

    SetChrPos(0x8, 44360, 0, -7020, 270)
    OP_4C(0x8, 0xFF)

    label("loc_377C")

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

    # Function_22_23DA end

    def Function_23_37DD(): pass

    label("Function_23_37DD")

    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    SetChrSubChip(0xB, 0x0)
    Sleep(100)
    SetChrSubChip(0xB, 0x1)
    Sleep(100)
    Return()

    # Function_23_37DD end

    SaveToFile()

Try(main)
