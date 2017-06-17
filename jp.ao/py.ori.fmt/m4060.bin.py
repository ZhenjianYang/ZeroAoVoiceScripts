from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4060.bin",                # FileName
        "m4060",                    # MapName
        "m4060",                    # Location
        0x007D,                     # MapIndex
        "ed7350",
        0x00000000,                 # Flags
        ("m4060", "r0000_1", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x27,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 125, 0, 2, 0, 3],
    )

    BuildStringList((
        "m4060",                  # 0
        "イベント用モンスター",   # 1
        "ロックドミナ",           # 2
        "bm4010",                 # 3
        "bm4010",                 # 4
        "bm4010",                 # 5
        "bm4010",                 # 6
        "bm4010",                 # 7
        "bm4010",                 # 8
        "bm4010",                 # 9
    ))

    ATBonus("ATBonus_3AC", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)
    ATBonus("ATBonus_39C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_29EC", 4,   4,   2,   0,   2,   2,   4)
    Sepith("Sepith_29DC", 0,   3,   3,   3,   0,   0,   1)
    Sepith("Sepith_29C4", 0,   4,   0,   4,   1,   1,   1)
    Sepith("Sepith_29E4", 3,   0,   4,   3,   3,   5,   0)

    MonsterBattlePostion("MonsterBattlePostion_3EC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3F8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3FC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_400", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_404", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_408", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_44C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_450", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_454", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_458", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_45C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_460", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_464", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_468", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_3CC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_3D8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_3DC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3E8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_46C", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_470", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_474", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_478", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_47C", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_480", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_484", 0, 0, 180)
    MonsterBattlePostion("MonsterBattlePostion_488", 0, 0, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_6A4", 0x0010, 48, 6, 45, 6, 1, 30, 0, "bm4010", "Sepith_29EC", 100, 0, 0, 0,
        (
            ("ms80700.dat", "ms84600.dat", 0, 0, 0, 0, "ms84600.dat", 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_3AC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_5C4", 0x0000, 47, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_29DC", 60, 25, 10, 0,
        (
            ("ms83900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            ("ms83900.dat", "ms83900.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            ("ms83900.dat", "ms83900.dat", "ms83900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_528", 0x0000, 46, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_29C4", 60, 25, 10, 0,
        (
            ("ms83600.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            ("ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3CC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            ("ms83600.dat", "ms83600.dat", "ms83600.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_660", 0x0000, 47, 6, 45, 6, 1, 40, 0, "bm4010", "Sepith_29E4", 100, 0, 0, 0,
        (
            ("ms82900.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7450", "ed7453", "ATBonus_39C"),
            (),
            (),
            (),
        )
    )

    # event battle count: 2

    BattleInfo(
        "BattleInfo_72C", 0x0000, 255, 6, 45, 0, 1, 0, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80700.dat", "ms80700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_46C", "MonsterBattlePostion_44C", "ed7451", "ed7453", "ATBonus_3AC"),
            (),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_6E8", 0x0012, 48, 6, 45, 3, 3, 30, 0, "bm4010", 0x00000000, 100, 0, 0, 0,
        (
            ("ms80700.dat", "ms84600.dat", "ms84600.dat", 0, 0, 0, "ms84600.dat", 0, "MonsterBattlePostion_3EC", "MonsterBattlePostion_44C", "ed7452", "ed7453", "ATBonus_3AC"),
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
        "monster/ch80750.itc",               # 10
        "monster/ch80750.itc",               # 11
        "monster/ch83650.itc",               # 12
        "monster/ch83650.itc",               # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "chr/ch00000.itc",                   # 16
        "chr/ch00000.itc",                   # 17
        "monster/ch83950.itc",               # 18
        "monster/ch83951.itc",               # 19
        "monster/ch82950.itc",               # 1A
        "monster/ch82950.itc",               # 1B
        "chr/ch00000.itc",                   # 1C
        "chr/ch00000.itc",                   # 1D
    ))

    DeclNpc(0,       0,       0,       0,    453,  0x0, 0,   0,   0,   255, 255, 255, 255, 255,  0)
    DeclNpc(-239,    10500,   32380,   0,    484,  0x0, 0,   16,  0,   0,   1,   255, 255, 255,  0)

    DeclMonster(-166630, 161730,  5000,    0x10100B9,    "BattleInfo_6A4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-164430, 188750,  5000,    0x10100B9,    "BattleInfo_5C4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-298920, 165910,  5000,    0x10100B9,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(168220,  172490,  5000,    0x10100E6,    "BattleInfo_5C4", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(154890,  187560,  5000,    0x101005F,    "BattleInfo_660", 0,   26,  0xFFFF, 6,  7)
    DeclMonster(299310,  190630,  5000,    0x10100E8,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(302640,  192150,  5000,    0x10100E8,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(302320,  185940,  5000,    0x10100E8,    "BattleInfo_528", 0,   18,  0xFFFF, 2,  3)

    DeclEvent(0x0000, 0, 9,   0.0,                   14.0,                  -1.0,                  182.25,                [0.1111111119389534,   -0.0,                  0.0,                   0.0,                   -0.0,                  0.3333333134651184,    -0.0,                  0.0,                   0.0,                   -0.0,                  0.20000000298023224,   0.0,                   -0.0,                  -4.666666507720947,    0.20000000298023224,   1.0])

    DeclActor(-240,    10000,   32870,   1200,    -240,    11000,   32870,   0x007C, 0,  4,  0x0000)
    DeclActor(296180,  5000,    193510,  1200,    296180,  6000,    193510,  0x007C, 0,  5,  0x0000)
    DeclActor(-299630, 5000,    160570,  1200,    -299630, 6000,    160570,  0x007C, 0,  6,  0x0000)
    DeclActor(220,     5250,    324370,  2000,    220,     6750,    324370,  0x007C, 0,  12, 0x0000)
    DeclActor(-1850,   200,     -1430,   1200,    -1850,   1700,    -1430,   0x007C, 0,  8,  0x0000)
    DeclActor(190,     160,     31000,   2000,    190,     2160,    31000,   0x007C, 0,  13, 0x0000)

    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 3, 2, 1])              # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(699, 0, [0, 1, 2, 3, 4, 5, 6])                 # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5, 6])                # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 5
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 7

    ScpFunction((
        "Function_0_808",          # 00, 0
        "Function_1_85F",          # 01, 1
        "Function_2_87E",          # 02, 2
        "Function_3_89D",          # 03, 3
        "Function_4_C91",          # 04, 4
        "Function_5_EA8",          # 05, 5
        "Function_6_FF9",          # 06, 6
        "Function_7_114A",         # 07, 7
        "Function_8_114E",         # 08, 8
        "Function_9_124A",         # 09, 9
        "Function_10_1CA2",        # 0A, 10
        "Function_11_1EC2",        # 0B, 11
        "Function_12_27D9",        # 0C, 12
        "Function_13_2959",        # 0D, 13
    ))


    def Function_0_808(): pass

    label("Function_0_808")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_85E")
    SetChrSubChip(0xFE, 0x0)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x5)
    Sleep(100)
    SetChrSubChip(0xFE, 0x4)
    Sleep(100)
    SetChrSubChip(0xFE, 0x3)
    Sleep(100)
    SetChrSubChip(0xFE, 0x2)
    Sleep(100)
    SetChrSubChip(0xFE, 0x1)
    Sleep(100)
    Jump("Function_0_808")

    label("loc_85E")

    Return()

    # Function_0_808 end

    def Function_1_85F(): pass

    label("Function_1_85F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_87D")
    OP_A1(0xFE, 0x2BC, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_1_85F")

    label("loc_87D")

    Return()

    # Function_1_85F end

    def Function_2_87E(): pass

    label("Function_2_87E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6E), scpexpr(EXPR_EQU), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x125, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89C")
    Event(0, 10)

    label("loc_89C")

    Return()

    # Function_2_87E end

    def Function_3_89D(): pass

    label("Function_3_89D")

    OP_52(0xA, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xC3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x4B0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xA, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xE, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xB, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ModifyEventFlags(0, 0, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x120, 7)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x121, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_BD8")
    ModifyEventFlags(1, 0, 0x80)

    label("loc_BD8")

    OP_65(0x5, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x125, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BEA")
    OP_66(0x5, 0x1)

    label("loc_BEA")

    ClearMapObjFlags(0x3, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x125, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C07")
    OP_70(0x3, 0x0)
    OP_70(0x4, 0x0)
    Jump("loc_C0F")

    label("loc_C07")

    OP_70(0x3, 0x14)
    OP_70(0x4, 0x14)

    label("loc_C0F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C22")
    OP_70(0x0, 0x0)
    Jump("loc_C26")

    label("loc_C22")

    OP_70(0x0, 0x1E)

    label("loc_C26")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C39")
    OP_70(0x1, 0x0)
    Jump("loc_C3D")

    label("loc_C39")

    OP_70(0x1, 0x1E)

    label("loc_C3D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C50")
    OP_70(0x2, 0x0)
    Jump("loc_C54")

    label("loc_C50")

    OP_70(0x2, 0x1E)

    label("loc_C54")

    Sound(129, 1, 100, 0)
    OP_1C(0x0, 0x6, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x7, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    OP_1C(0x0, 0x8, 0x0, 0x32, 0x0, 0x7, 0x0, 0x0)
    LoadEffect(0x10, "event\\eva00_00.eff")
    Return()

    # Function_3_89D end

    def Function_4_C91(): pass

    label("Function_4_C91")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E62")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21B, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D90")
    OP_A7(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_98(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_CEE():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_CEE)

    def lambda_D08():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_D08)
    ClearChrFlags(0x9, 0x80)
    SetChrFlags(0x9, 0x8000)

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "魔獣が現れた！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    WaitChrThread(0x9, 1)
    Battle("BattleInfo_72C", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_D71"),
        (2, "loc_D80"),
        (1, "loc_D8D"),
        (SWITCH_DEFAULT, "loc_D90"),
    )


    label("loc_D71")

    SetScenarioFlags(0x21B, 0)
    OP_70(0x0, 0x1E)
    Sleep(500)
    Jump("loc_D90")

    label("loc_D80")

    OP_70(0x0, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_D8D")

    OP_B9(0x0)
    Return()

    label("loc_D90")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x96, 1)"), scpexpr(EXPR_END)), "loc_DED")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x96),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E1, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_E5D")

    label("loc_DED")

    FadeToDark(300, 0, 100)

    #A0003
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x96),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x96),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_E5D")

    Jump("loc_E9C")

    label("loc_E62")

    FadeToDark(300, 0, 100)

    #A0004
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

    label("loc_E9C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_C91 end

    def Function_5_EA8(): pass

    label("Function_5_EA8")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FA8")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F5, 1)"), scpexpr(EXPR_END)), "loc_F31")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E1, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_FA3")

    label("loc_F31")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0006
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F5),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_FA3")

    Jump("loc_FED")

    label("loc_FA8")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

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

    label("loc_FED")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_EA8 end

    def Function_6_FF9(): pass

    label("Function_6_FF9")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1E1, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10F9")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x1F8, 1)"), scpexpr(EXPR_END)), "loc_1082")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1E1, 7)
    OP_E0(0x5, 0x0)
    Jump("loc_10F4")

    label("loc_1082")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x1F8),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_10F4")

    Jump("loc_113E")

    label("loc_10F9")

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

    label("loc_113E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_FF9 end

    def Function_7_114A(): pass

    label("Function_7_114A")

    Call(1, 6)
    Return()

    # Function_7_114A end

    def Function_8_114E(): pass

    label("Function_8_114E")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_123B")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x5, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x5, 0x0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x5)
    OP_71(0x5, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x5, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_123B")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_8_114E end

    def Function_9_124A(): pass

    label("Function_9_124A")

    EventBegin(0x0)
    FadeToDark(0, -1, 0)
    FadeToDark(500, 0, -1)
    OP_0D()
    FadeToBright(0, -1)
    OP_E2(0x3)
    CreatePortrait(0, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01903.itp")
    CreatePortrait(1, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01001.itp")
    CreatePortrait(2, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01201.itp")
    CreatePortrait(3, 224, 0, 480, 256, 0, 16, 256, 256, 0, 0, 256, 256, 0xFFFFFF, 0x0, "bu01105.itp")
    SoundLoad(2707)
    SoundLoad(4125)
    SoundLoad(3593)
    SoundLoad(3594)
    OP_68(0, 1000, 18350, 0)
    MoveCamera(317, 22, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 500, 0, 13500, 0)
    SetChrPos(0x109, -800, 0, 13200, 0)

    def lambda_1379():
        OP_97(0x101, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1379)
    Sleep(100)

    def lambda_1396():
        OP_97(0x109, 0x0, 0x0, 0x1388, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1396)
    SetCameraDistance(17000, 2500)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0x109, 0)
    OP_6F(0x79)

    #C0012
    ChrTalk(
        0x109,
        "#10111F#6Pこれは……\x02",
    )

    CloseMessageWindow()

    #C0013
    ChrTalk(
        0x101,
        "#00013F#6Pまた扉か……\x02",
    )

    CloseMessageWindow()
    OP_68(-710, 1000, 28570, 5000)

    def lambda_1410():
        OP_97(0x101, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1410)
    Sleep(100)

    def lambda_142D():
        OP_97(0x109, 0x0, 0x0, 0x2710, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_142D)
    WaitChrThread(0x109, 0)
    OP_6F(0x79)
    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0014
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "岩の扉は固く閉ざされている。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    FadeToBright(300, 0)
    OP_0D()

    #C0015
    ChrTalk(
        0x101,
        (
            "#6P#00003F駄目か……\x02\x03",

            "#00008F多分、入口近くの扉と同じように\x01",
            "解除する装置があるんだろう。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x109,
        "#10101F#6Pええ、探してみましょう。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x109, 0x101, 500)
    Sleep(300)

    #C0017
    ChrTalk(
        0x109,
        (
            "#10113F#5Pそれにしても……\x01",
            "ダドリーさんたちの方は\x01",
            "どうなっているんでしょうか？\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x109, 500)
    Sleep(100)

    #C0018
    ChrTalk(
        0x101,
        (
            "#12P#00006Fあの２人なら滅多な事じゃ\x01",
            "遅れを取ることはなさそうだけど……\x02\x03",

            "#00008F敵はグノーシスを使っている上に\x01",
            "あんな危険な人形も呼び出せる。\x02\x03",

            "#00001F楽観は出来ないかもしれないな。\x02",
        )
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x109,
        (
            "#10108F#5Pですよね……\x02\x03",

            "#10106Fふう、こんな時にエニグマで\x01",
            "連絡が取り合えたらいいんですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0020
    ChrTalk(
        0x101,
        (
            "#12P#00006Fうーん、通信機能が使えるのは\x01",
            "クロスベルと、財団の本拠地がある\x01",
            "レマン自治州だけみたいだからな。\x02\x03",

            "#00000Fでも確かに、改めて考えると\x01",
            "物凄く便利な機能だったんだよな。\x02\x03",

            "フランのサポートも受けられたし。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x109,
        (
            "#10112F#5Pあはは……ちゃんとお役に\x01",
            "立っていればいいんですけど。\x02\x03",

            "#10100Fあの調子で、ちゃんとお仕事が\x01",
            "勤まっているか心配なんですよね。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x101,
        (
            "#12P#00009Fはは、アルタイル市へ出発する前、\x01",
            "キーアと駅まで見送りにきた時か。\x02\x03",

            "#00002Fあれくらいいいじゃないか。\x01",
            "君を心配してのことだろうし。\x02",
        )
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x109,
        (
            "#10106F#5Pだからといって、勤務時間中に\x01",
            "サボって来るのはダメですよ……\x02\x03",

            "#10101Fキーアちゃんと一緒に\x01",
            "列車に乗り込もうとするし。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x101,
        (
            "#12P#00004Fはは、今回はキーアも\x01",
            "珍しくダダをこねてたからな。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetMessageWindowPos(14, 280, 35, 3)
    SetChrName("フラン")

    #A0025
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#2707V#30Wお姉ちゃん、ロイドさん！\x01",
            "くれぐれも気をつけてくださいね！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_C9(0x1, 0x80000000)
    OP_24(0xA93)
    OP_57(0x0)
    OP_5A()
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    Sleep(300)
    SetChrName("セルゲイ課長")

    #A0026
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#30Wま、気を抜くんじゃねえぞ。\x02\x03",

            "後ろ盾を失った逃亡者とはいえ、\x01",
            "あの教団に関わっていた連中だ。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    OP_CB(0x2, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    Sleep(300)
    OP_C9(0x0, 0x80000000)
    SetChrName("ツァイト")

    #A0027
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#4125V#30Wウォン。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0x101D)
    OP_57(0x0)
    OP_5A()
    OP_CB(0x2, 0x3, 0xFFFFFF, 0x1F4, 0x0, 0x0)
    OP_CC(0x0, 0x2, 0x3)
    OP_CB(0x3, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    Sleep(500)
    SetChrName("キーア")

    #A0028
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xC),
            "#3593V#30Wロイド……\x01",
            "ゼッタイに無事に戻ってきてね。\x02\x03",

            "#3594Vキーア、いい子で待ってるから……！\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_24(0xE0A)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x80000000)
    FadeToBright(800, 0)
    OP_CB(0x3, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x3, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(300)

    #C0029
    ChrTalk(
        0x101,
        (
            "#12P#00004F大切な人たちがクロスベルで\x01",
            "俺たちのことを待っている……\x02\x03",

            "#00000F何としても任務を達成して\x01",
            "無事な顔を見せてやらないとな。\x02",
        )
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x109,
        "#10102F#5P……はい！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 530, 0, 27590, 180)
    OP_69(0xFF, 0x0)
    SetScenarioFlags(0x121, 0)
    ModifyEventFlags(0, 0, 0x80)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_9_124A end

    def Function_10_1CA2(): pass

    label("Function_10_1CA2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("monster/ch80750.itc", 0x1E)
    LoadChrToIndex("chr/ch00050.itc", 0x1F)
    LoadChrToIndex("chr/ch00051.itc", 0x20)
    LoadChrToIndex("chr/ch02950.itc", 0x21)
    LoadChrToIndex("chr/ch02951.itc", 0x22)
    OP_68(0, 6000, 201500, 0)
    MoveCamera(323, 23, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(19000, 0)
    SetChrPos(0x101, 800, 5000, 205100, 180)
    SetChrPos(0x109, -600, 5000, 205500, 180)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x20)
    SetChrFlags(0x8, 0x8000)
    SetChrChipByIndex(0x8, 0x1E)
    SetChrSubChip(0x8, 0x0)
    SetChrPos(0x8, 0, 5000, 191500, 0)
    OP_52(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xC7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x34, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1D6C():
        OP_97(0x101, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_1D6C)
    Sleep(50)

    def lambda_1D89():
        OP_97(0x109, 0x0, 0x0, 0xFFFFE4A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1D89)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x101, 0)
    OP_63(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    WaitChrThread(0x109, 0)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)
    OP_6F(0x79)
    Fade(250)
    SetChrChipByIndex(0x101, 0x1F)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0x21)
    SetChrSubChip(0x109, 0x0)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_0D()
    BeginChrThread(0x8, 0, 0, 0)
    OP_68(0, 6100, 195000, 2000)
    MoveCamera(311, 21, 0, 2000)
    SetCameraDistance(17500, 2000)
    OP_6F(0x79)
    Sleep(800)
    BlurSwitch(0x258, 0xBBFFFFFF, 0x0, 0x0, 0x0)
    OP_68(0, 6300, 193700, 600)
    SetCameraDistance(15000, 600)

    def lambda_1E62():
        OP_96(0xFE, 0x320, 0x0, 0x2E824, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1E62)
    Sleep(50)

    def lambda_1E7F():
        OP_96(0xFE, 0xFFFFFDA8, 0x0, 0x2E824, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E7F)
    Sleep(550)
    EndChrThread(0x101, 0xFF)
    EndChrThread(0x109, 0xFF)
    Battle("BattleInfo_6E8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x8, 0x80)
    Call(0, 11)
    Return()

    # Function_10_1CA2 end

    def Function_11_1EC2(): pass

    label("Function_11_1EC2")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    LoadChrToIndex("chr/ch00050.itc", 0x1E)
    LoadChrToIndex("chr/ch02950.itc", 0x1F)
    CreatePortrait(0, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis221.itp")
    CreatePortrait(1, 0, 8, 480, 264, 0, 0, 512, 256, 0, 0, 480, 256, 0xFFFFFF, 0x0, "c_vis222.itp")
    OP_68(150, 6100, 196150, 0)
    MoveCamera(320, 21, 0, 0)
    OP_6E(600, 0)
    SetCameraDistance(16000, 0)
    OP_F0(0x0, 0x1)
    SetChrPos(0x101, 800, 5000, 196000, 180)
    SetChrChipByIndex(0x101, 0x1E)
    SetChrSubChip(0x101, 0x0)
    SetChrPos(0x109, -700, 5000, 196300, 180)
    SetChrChipByIndex(0x109, 0x1F)
    SetChrSubChip(0x109, 0x0)
    SetCameraDistance(15000, 2000)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6F(0x79)

    #C0031
    ChrTalk(
        0x101,
        "#11P#00000Fよし……！\x02",
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Fade(250)
    SetChrChipByIndex(0x101, 0xFF)
    SetChrSubChip(0x101, 0x0)
    SetChrChipByIndex(0x109, 0xFF)
    SetChrSubChip(0x109, 0x0)
    Sound(531, 0, 100, 0)
    Sound(805, 0, 100, 0)
    OP_0D()

    def lambda_1FF2():
        TurnDirection(0xFE, 0x101, 500)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1FF2)
    Sleep(100)
    TurnDirection(0x101, 0x109, 500)
    Sleep(150)

    #C0032
    ChrTalk(
        0x109,
        (
            "#10109F#5Pふふっ、お疲れ様でした。\x02\x03",

            "#10106Fそれにしても……\x01",
            "あのアーネストという男、\x01",
            "本当に何が狙いなんでしょうか？\x02\x03",

            "#10101Fどうやら元議長の方は無理矢理\x01",
            "つき合わされてるみたいですけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        (
            "#12P#00003F……分からない。\x02\x03",

            "#00001Fただ、ヨアヒムと同じ力を\x01",
            "手に入れようとしているのは\x01",
            "確かみたいだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0034
    ChrTalk(
        0x109,
        (
            "#10105F#5P教団事件の黒幕と同じ力……\x02\x03",

            "#10101Fマフィアやベルガード門の部隊を\x01",
            "意のままに操ったアレですか？\x02",
        )
    )

    CloseMessageWindow()

    #C0035
    ChrTalk(
        0x101,
        (
            "#12P#00006Fああ、それも危険だったけど\x01",
            "さらにタチが悪い力がある。\x02\x03",

            "#00013F人の心や背景を“視#2Rみ#る”力だ。\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    OP_CB(0x0, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_CB(0x0, 0x3, 0xAAFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x0, 0x3)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(30, 60, -1, -1)
    SetChrName("")

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30Wこいつ……\x01",
            "あたしたちの記憶を！？\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(100, 110, -1, -1)

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xD),
            "#30Wまさか……\x01",
            "そこから再現したのか！？\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    FadeToBright(800, 0)
    OP_CB(0x0, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    Sleep(500)
    VolumeBGM(0x64, 0x3E8)
    OP_63(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    Sound(28, 0, 100, 0)
    Sleep(1000)

    #C0038
    ChrTalk(
        0x109,
        (
            "#10107F#5Pそ、それって……\x01",
            "色々とまずくありませんか？\x02",
        )
    )

    CloseMessageWindow()

    #C0039
    ChrTalk(
        0x101,
        (
            "#12P#00003Fああ、ある意味どんな風にも\x01",
            "悪用できてしまう能力だろう。\x02\x03",

            "#00008Fそれどころか──\x02",
        )
    )

    CloseMessageWindow()
    VolumeBGM(0x46, 0x3E8)
    Sound(824, 0, 100, 0)
    OP_CB(0x1, 0x3, 0xFFFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToDark(0, 0, -1)
    Sleep(500)
    OP_CB(0x1, 0x3, 0xAAFFFFFF, 0x12C, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    FadeToDark(0, 0, -1)
    Sound(1005, 0, 80, 0)
    OP_C9(0x0, 0x800)
    SetMessageWindowPos(-1, 120, -1, -1)
    SetChrName("")

    #A0040
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60W我ニハ総テガ視エルノダ……\x02",
        )
    )

    CloseMessageWindow()

    #A0041
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60Wきーあ様ノ失踪ノカラクリ……\x01",
            "ソシテ貴様ノ兄ノ死ノ真相モ……\x02",
        )
    )

    CloseMessageWindow()

    #A0042
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0xB),
            "#60Wくろすべるノ地ニ課セラレタ\x01",
            "避ケラレヌ運命モ……\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    OP_C9(0x1, 0x800)
    OP_63(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    FadeToBright(800, 0)
    OP_CB(0x1, 0x3, 0xFFFFFF, 0x320, 0x0, 0x0)
    OP_CC(0x0, 0x1, 0x3)
    VolumeBGM(0x64, 0x3E8)
    Sleep(1000)

    #C0043
    ChrTalk(
        0x109,
        "#10105F#5Pロイドさん……？\x02",
    )

    CloseMessageWindow()
    OP_64(0x101)
    Sleep(500)

    #C0044
    ChrTalk(
        0x101,
        (
            "#12P#00003F……いや、何でもない。\x02\x03",

            "#00008Fいずれにせよ、アーネストに\x01",
            "ヨアヒムと同じ末路を\x01",
            "歩ませるわけにはいかない。\x02\x03",

            "#00013F絶対に……\x01",
            "生かして捕まえないとな。\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x109, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    #C0045
    ChrTalk(
        0x109,
        (
            "#10113F#5Pロイドさん……\x02\x03",

            "#10106Fその、例の首謀者が死んだのは\x01",
            "別にロイドさんのせいじゃ……\x02",
        )
    )

    CloseMessageWindow()

    #C0046
    ChrTalk(
        0x101,
        (
            "#12P#00006Fそれでも……\x01",
            "死なせずに捕まえることは\x01",
            "出来たんじゃないかと思ってさ。\x02\x03",

            "#00008F今更なのは百も承知だけど……\x02",
        )
    )

    CloseMessageWindow()

    #C0047
    ChrTalk(
        0x109,
        "#10108F#5P……………………………………\x02",
    )

    CloseMessageWindow()

    #C0048
    ChrTalk(
        0x101,
        (
            "#12P#00004Fはは、ウジウジしてると\x01",
            "ランディにまたどやされるかな。\x02\x03",

            "#00000F──先を急ごう。\x01",
            "アリオスさんたちと合流しないと。\x02",
        )
    )

    CloseMessageWindow()

    #C0049
    ChrTalk(
        0x109,
        "#10100F#5Pええ……！\x02",
    )

    CloseMessageWindow()
    SetCameraDistance(15250, 1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_D7(0x1E)
    OP_D7(0x1F)
    OP_37()
    OP_CC(0x1, 0xFF, 0x0)
    SetChrPos(0x0, 0, 5000, 196600, 180)
    OP_69(0xFF, 0x0)
    OP_F0(0x0, 0xA)
    SetScenarioFlags(0x121, 1)
    OP_E2(0x2)
    Sleep(500)
    EventEnd(0x5)
    Return()

    # Function_11_1EC2 end

    def Function_12_27D9(): pass

    label("Function_12_27D9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x125, 1)), scpexpr(EXPR_END)), "loc_2818")
    TalkBegin(0xFF)
    SetChrName("")

    #A0050
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "もう動かないようだ。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    ClearMapFlags(0x8000000)
    TalkEnd(0xFF)
    Jump("loc_2958")

    label("loc_2818")

    EventBegin(0x1)

    #A0051
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2951")
    Fade(500)
    OP_68(290, 6300, 321960, 0)
    MoveCamera(330, 35, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(17000, 0)
    SetChrPos(0x0, 910, 5000, 322080, 1)
    SetChrPos(0x1, -220, 5000, 322120, 1)
    OP_0D()
    Sleep(500)
    Sound(143, 0, 100, 0)
    OP_71(0x4, 0x0, 0x14, 0x0, 0x0)
    Sleep(1000)
    Fade(500)
    OP_68(-1250, 1300, 28830, 0)
    MoveCamera(336, 28, 0, 0)
    OP_6E(550, 0)
    SetCameraDistance(20000, 0)
    OP_0D()
    Sleep(500)
    Sound(155, 2, 100, 0)
    OP_74(0x3, 0xF)
    OP_71(0x3, 0x0, 0x14, 0x0, 0x0)
    Sleep(1300)
    OP_24(0x9B)
    Sound(149, 0, 100, 0)
    OP_82(0x64, 0x0, 0x3E8, 0x64)
    Sleep(1000)
    SetScenarioFlags(0x125, 1)
    OP_65(0x5, 0x1)

    label("loc_2951")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)

    label("loc_2958")

    Return()

    # Function_12_27D9 end

    def Function_13_2959(): pass

    label("Function_13_2959")

    TalkBegin(0xFF)
    SetChrName("")

    #A0052
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "岩の扉は固く閉ざされている。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    TalkEnd(0xFF)
    Return()

    # Function_13_2959 end

    SaveToFile()

Try(main)
