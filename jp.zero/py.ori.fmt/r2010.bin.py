from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "r2010.bin",                # FileName
        "r2010",                    # MapName
        "r2010",                    # Location
        0x0062,                     # MapIndex
        "ed7202",
        0x00000000,                 # Flags
        ("r2010", "r0000_1", "", "", "", ""),   # include
        0x02,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 98, 0, 0, 0, 1],
    )

    BuildStringList((
        "r2010",                  # 0
        "br2000",                 # 1
        "br2000",                 # 2
        "br2000",                 # 3
        "br2000",                 # 4
        "br2000",                 # 5
        "クロスベル市方面",       # 6
        "鉱山町マインツ方面",     # 7
    ))

    ATBonus("ATBonus_2E4", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_D55", 10,  0,   0,   4,   3,   5,   0)
    Sepith("Sepith_D5D", 4,   0,   1,   10,  5,   3,   0)
    Sepith("Sepith_D6D", 9,   0,   4,   0,   2,   0,   7)
    Sepith("Sepith_D65", 0,   10,  3,   0,   2,   0,   5)
    Sepith("Sepith_D9D", 14,  4,   9,   5,   7,   12,  9)

    MonsterBattlePostion("MonsterBattlePostion_344", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_348", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_34C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_350", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_354", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_35C", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_360", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_3A4", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_3A8", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_3AC", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_3B0", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_3B4", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_3B8", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_3BC", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_3C0", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_324", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_328", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_32C", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_330", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_334", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_338", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_340", 2, 13, 180)

    # monster count: 9

    BattleInfo(
        "BattleInfo_3C4", 0x0000, 14, 6, 45, 10, 1, 30, 0, "br2000", "Sepith_D55", 40, 30, 20, 10,
        (
            ("ms62500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms62500.dat", "ms62500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_324", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms62500.dat", "ms65900.dat", "ms62500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms62500.dat", "ms62500.dat", "ms65500.dat", "ms62500.dat", 0, 0, 0, 0, "MonsterBattlePostion_324", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
        )
    )

    BattleInfo(
        "BattleInfo_554", 0x0000, 14, 6, 45, 10, 1, 40, 0, "br2000", "Sepith_D5D", 40, 30, 20, 10,
        (
            ("ms65500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms65500.dat", "ms65500.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_324", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms65500.dat", "ms62500.dat", "ms65500.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms65500.dat", "ms65500.dat", "ms69400.dat", "ms65500.dat", 0, 0, 0, 0, "MonsterBattlePostion_324", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
        )
    )

    BattleInfo(
        "BattleInfo_61C", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_D6D", 40, 30, 20, 10,
        (
            ("ms69400.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms69400.dat", "ms69700.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms69400.dat", "ms69700.dat", "ms69800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms69400.dat", "ms69700.dat", "ms69800.dat", "ms69900.dat", 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
        )
    )

    BattleInfo(
        "BattleInfo_48C", 0x0000, 14, 6, 45, 10, 1, 25, 0, "br2000", "Sepith_D65", 40, 30, 20, 10,
        (
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, 0, "MonsterBattlePostion_324", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", "ms65900.dat", 0, 0, "MonsterBattlePostion_324", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
        )
    )

    BattleInfo(
        "BattleInfo_6E4", 0x0000, 35, 6, 45, 6, 1, 30, 0, "br2000", "Sepith_D9D", 40, 35, 25, 0,
        (
            ("ms76001.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_324", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
            ("ms76001.dat", "ms76001.dat", "ms76001.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_344", "MonsterBattlePostion_3A4", "ed7400", "ed7403", "ATBonus_2E4"),
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
        "monster/ch62550.itc",               # 10
        "monster/ch62551.itc",               # 11
        "monster/ch65950.itc",               # 12
        "monster/ch65951.itc",               # 13
        "monster/ch65550.itc",               # 14
        "monster/ch65551.itc",               # 15
        "monster/ch69450.itc",               # 16
        "monster/ch69450.itc",               # 17
        "monster/ch76050.itc",               # 18
        "monster/ch76051.itc",               # 19
    ))

    DeclMonster(-31720,  15370,   0,       0x1010000,    "BattleInfo_3C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-64090,  36330,   0,       0x1010000,    "BattleInfo_554", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(-41420,  86260,   8000,    0x1010000,    "BattleInfo_61C", 0,   22,  0xFFFF, 6,  7)
    DeclMonster(8029,    99200,   18000,   0x1010000,    "BattleInfo_48C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(27930,   93470,   18000,   0x1010000,    "BattleInfo_3C4", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(30600,   53520,   8000,    0x1010000,    "BattleInfo_554", 0,   20,  0xFFFF, 4,  5)
    DeclMonster(17410,   30550,   8000,    0x1010000,    "BattleInfo_48C", 0,   18,  0xFFFF, 2,  3)
    DeclMonster(-52720,  42390,   0,       0x1010000,    "BattleInfo_6E4", 0,   24,  0xFFFF, 8,  9)
    DeclMonster(19680,   94830,   18000,   0x1010000,    "BattleInfo_6E4", 0,   24,  0xFFFF, 8,  9)

    DeclActor(-87000,  0,       35750,   1200,    -87000,  1000,    35750,   0x007C, 0,  2,  0x0000)
    DeclActor(-13600,  5370,    58650,   1200,    -15420,  370,     63420,   0x007C, 0,  6,  0x0000)
    DeclActor(-28830,  0,       15790,   1200,    -28830,  0,       15790,   0x007C, 0,  3,  0x0000)
    DeclActor(-29010,  8000,    92960,   1200,    -29010,  8000,    92960,   0x007C, 0,  4,  0x0000)

    PlaceName(26.0, 0.0, -28.0, 0x0000, 0x0000, "クロスベル市方面")
    PlaceName(61.0, 18.0, 112.0, 0x0000, 0x0000, "鉱山町マインツ方面")

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 3
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 4
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 5
    ChipFrameInfo(500, 0, [0, 1, 2, 3, 4, 5])                    # 6
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 5])                   # 7
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 8
    ChipFrameInfo(1000, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 9

    ScpFunction((
        "Function_0_814",          # 00, 0
        "Function_1_818",          # 01, 1
        "Function_2_ACB",          # 02, 2
        "Function_3_C18",          # 03, 3
        "Function_4_C2C",          # 04, 4
        "Function_5_C40",          # 05, 5
        "Function_6_C59",          # 06, 6
    ))


    def Function_0_814(): pass

    label("Function_0_814")

    Call(0, 5)
    Return()

    # Function_0_814 end

    def Function_1_818(): pass

    label("Function_1_818")

    OP_52(0xF, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xF, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x10, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9A1")
    OP_70(0x0, 0x0)
    Jump("loc_9A5")

    label("loc_9A1")

    OP_70(0x0, 0x1E)

    label("loc_9A5")

    OP_65(0x2, 0x1)
    OP_65(0x3, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 1)), scpexpr(EXPR_END)), "loc_A0B")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -28830, 0, 15790, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x2, 0x1)
    Jump("loc_A64")

    label("loc_A0B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x7A, 2)), scpexpr(EXPR_END)), "loc_A64")
    LoadEffect(0x9, "event\\eva00_00.eff")
    PlayEffect(0x9, 0x9, 0xFF, 0x0, -29010, 8000, 92960, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_66(0x3, 0x1)

    label("loc_A64")

    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, -15420, 370, 63420, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    SoundDistance(0x7C, 0xFFFFCE6E, 0x1504, 0x1205C, 0x7530, 0x249F0, 0x64, 0x0)
    Return()

    # Function_1_818 end

    def Function_2_ACB(): pass

    label("Function_2_ACB")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x104, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BC7")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x8E, 1)"), scpexpr(EXPR_END)), "loc_B50")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x104, 0)
    OP_DE(0x6, 0x0)
    Jump("loc_BC2")

    label("loc_B50")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x8E),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_BC2")

    Jump("loc_C0C")

    label("loc_BC7")

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

    label("loc_C0C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_ACB end

    def Function_3_C18(): pass

    label("Function_3_C18")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 1)
    OP_65(0x2, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_3_C18 end

    def Function_4_C2C(): pass

    label("Function_4_C2C")

    TalkBegin(0xFF)
    Call(1, 0)
    ClearScenarioFlags(0x7A, 2)
    OP_65(0x3, 0x1)
    StopEffect(0x9, 0x2)
    TalkEnd(0xFF)
    Return()

    # Function_4_C2C end

    def Function_5_C40(): pass

    label("Function_5_C40")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_C58")
    SetChrFlags(0xF, 0x80)
    SetChrFlags(0x10, 0x80)

    label("loc_C58")

    Return()

    # Function_5_C40 end

    def Function_6_C59(): pass

    label("Function_6_C59")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0004
    ChrTalk(
        0x101,
        "#0000Fここなら釣れそうだな。\x02",
    )

    CloseMessageWindow()
    OP_68(-14980, 4370, 60900, 1500)
    MoveCamera(19, 50, 0, 1500)
    OP_6E(370, 1500)
    SetCameraDistance(30000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "釣りをしますか？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "釣りをする\x01",      # 0
            "やめる\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D28")
    OP_E0(0x2)
    MiniGame(0x6, 0x5, 0xFFFFCFD6, 0x14FA, 0xE45C, 0x14E, 0xFFFFC3C4, 0x172, 0xF7BC)

    label("loc_D28")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_6_C59 end

    SaveToFile()

Try(main)
