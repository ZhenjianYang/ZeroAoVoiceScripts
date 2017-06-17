from ZeroScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m3030.bin",                # FileName
        "m3030",                    # MapName
        "m3030",                    # Location
        0x007E,                     # MapIndex
        "ed7305",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 2500, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 126, 0, 0, 0, 1],
    )

    BuildStringList((
        "m3030",                  # 0
        "bm3030",                 # 1
        "bm3030",                 # 2
    ))

    ATBonus("ATBonus_158", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_B23", 9,   9,   9,   9,   10,  10,  10)
    Sepith("Sepith_B3B", 7,   7,   14,  7,   9,   12,  12)

    MonsterBattlePostion("MonsterBattlePostion_1B8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_1BC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_1C0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1C4", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1C8", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1CC", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1D4", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_218", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_21C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_220", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_224", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_228", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_22C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_230", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_234", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_198", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_19C", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_1A8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_1AC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1B0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_1B4", 2, 13, 180)

    # monster count: 2

    BattleInfo(
        "BattleInfo_238", 0x0000, 43, 6, 60, 4, 1, 30, 0, "bm3030", "Sepith_B23", 60, 25, 10, 5,
        (
            ("ms61500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1B8", "MonsterBattlePostion_218", "ed7402", "ed7403", "ATBonus_158"),
            ("ms61500.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_198", "MonsterBattlePostion_218", "ed7402", "ed7403", "ATBonus_158"),
            ("ms61500.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1B8", "MonsterBattlePostion_218", "ed7402", "ed7403", "ATBonus_158"),
            ("ms61500.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_198", "MonsterBattlePostion_218", "ed7402", "ed7403", "ATBonus_158"),
        )
    )

    BattleInfo(
        "BattleInfo_300", 0x0000, 43, 6, 60, 4, 1, 60, 0, "bm3030", "Sepith_B3B", 60, 25, 10, 5,
        (
            ("ms72500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1B8", "MonsterBattlePostion_218", "ed7402", "ed7403", "ATBonus_158"),
            ("ms72500.dat", "ms77300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_198", "MonsterBattlePostion_218", "ed7402", "ed7403", "ATBonus_158"),
            ("ms72500.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1B8", "MonsterBattlePostion_218", "ed7402", "ed7403", "ATBonus_158"),
            ("ms72500.dat", "ms77300.dat", "ms77300.dat", "ms77300.dat", 0, 0, 0, 0, "MonsterBattlePostion_198", "MonsterBattlePostion_218", "ed7402", "ed7403", "ATBonus_158"),
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
        "monster/ch61550.itc",               # 10
        "monster/ch61550.itc",               # 11
        "monster/ch72550.itc",               # 12
        "monster/ch72551.itc",               # 13
    ))

    DeclMonster(-23130,  -60,     -6000,   0x1010000,    "BattleInfo_238", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-300200, 8750,    -6000,   0x1010000,    "BattleInfo_300", 0,   18,  0xFFFF, 2,  3)

    DeclActor(-49500,  -4960,   3200,    2500,    -49500,  -3960,   3200,    0x007C, 0,  2,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 2
    ChipFrameInfo(1000, 0, [0, 1, 2, 3])                         # 3

    ScpFunction((
        "Function_0_404",          # 00, 0
        "Function_1_405",          # 01, 1
        "Function_2_723",          # 02, 2
    ))


    def Function_0_404(): pass

    label("Function_0_404")

    Return()

    # Function_0_404 end

    def Function_1_405(): pass

    label("Function_1_405")

    ClearMapObjFlags(0x4, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 6)), scpexpr(EXPR_END)), "loc_41D")
    OP_70(0x4, 0x1E)
    Jump("loc_421")

    label("loc_41D")

    OP_70(0x4, 0x0)

    label("loc_421")

    SetBarrier(0x0, 0x0, 0x1, 0x0, -34500, -7000, -6000, 5000, 2000, 0)
    SetBarrier(0x0, 0x1, 0x1, 0x0, -34500, -7000, -10500, 5000, 2000, 0)
    SetBarrier(0x0, 0x2, 0x1, 0x0, -40500, -7000, 0, 5000, 2000, 90000)
    SetBarrier(0x0, 0x3, 0x1, 0x0, -45000, -7000, 0, 5000, 2000, 90000)
    SetBarrier(0x0, 0x4, 0x1, 0x0, -34500, -7000, 6000, 5000, 2000, 0)
    SetBarrier(0x0, 0x5, 0x1, 0x0, -34500, -7000, 10500, 5000, 2000, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_503")
    OP_70(0x5, 0x0)
    OP_70(0x6, 0x0)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_596")

    label("loc_503")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_536")
    OP_70(0x5, 0x1E)
    OP_70(0x6, 0x32)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_596")

    label("loc_536")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_569")
    OP_70(0x5, 0x3C)
    OP_70(0x6, 0x64)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    Jump("loc_596")

    label("loc_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_596")
    OP_70(0x5, 0x5A)
    OP_70(0x6, 0x96)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)

    label("loc_596")

    OP_52(0x8, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xE4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_405 end

    def Function_2_723(): pass

    label("Function_2_723")

    EventBegin(0x1)
    SetMapFlags(0x8000000)

    #A0001
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "レバーがある。\x01",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A8B")
    Fade(500)
    SetChrPos(0x0, -50000, -6000, 2029, 0)
    SetChrPos(0x1, -49180, -6000, 500, 0)
    SetChrPos(0x2, -51180, -6000, 500, 0)
    SetChrPos(0x3, -50000, -6000, -770, 0)
    OP_68(-49500, -6000, 3480, 0)
    MoveCamera(45, 38, 0, 0)
    OP_6E(360, 0)
    SetCameraDistance(32000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_89F")
    Sound(143, 0, 100, 0)
    OP_71(0x5, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x5)
    Fade(500)
    OP_68(-35880, -6000, -1780, 0)
    MoveCamera(45, 55, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(37000, 0)
    OP_0D()
    Sleep(500)
    Sound(158, 0, 100, 0)
    OP_71(0x6, 0x0, 0x32, 0x0, 0x0)
    OP_79(0x6)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    ClearScenarioFlags(0xF5, 3)
    SetScenarioFlags(0xF5, 4)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_A8B")

    label("loc_89F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_945")
    Sound(143, 0, 100, 0)
    OP_71(0x5, 0x1E, 0x3C, 0x0, 0x0)
    OP_79(0x5)
    Fade(500)
    OP_68(-35880, -6000, -1780, 0)
    MoveCamera(45, 55, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(37000, 0)
    OP_0D()
    Sleep(500)
    Sound(158, 0, 100, 0)
    OP_71(0x6, 0x32, 0x64, 0x0, 0x0)
    OP_79(0x6)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0xF5, 3)
    ClearScenarioFlags(0xF5, 4)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x2, 0x4, 0x1)
    SetBarrier(0x2, 0x5, 0x1)
    Jump("loc_A8B")

    label("loc_945")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_9EB")
    Sound(143, 0, 100, 0)
    OP_71(0x5, 0x3C, 0x5A, 0x0, 0x0)
    OP_79(0x5)
    Fade(500)
    OP_68(-35880, -6000, -1780, 0)
    MoveCamera(45, 55, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(37000, 0)
    OP_0D()
    Sleep(500)
    Sound(158, 0, 100, 0)
    OP_71(0x6, 0x64, 0x96, 0x0, 0x0)
    OP_79(0x6)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    SetScenarioFlags(0xF5, 3)
    SetScenarioFlags(0xF5, 4)
    SetBarrier(0x3, 0x0, 0x1)
    SetBarrier(0x3, 0x1, 0x1)
    SetBarrier(0x2, 0x2, 0x1)
    SetBarrier(0x2, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)
    Jump("loc_A8B")

    label("loc_9EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xF5, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_A8B")
    Sound(143, 0, 100, 0)
    OP_71(0x5, 0x5A, 0x78, 0x0, 0x0)
    OP_79(0x5)
    Fade(500)
    OP_68(-35880, -6000, -1780, 0)
    MoveCamera(45, 55, 0, 0)
    OP_6E(580, 0)
    SetCameraDistance(37000, 0)
    OP_0D()
    Sleep(500)
    Sound(158, 0, 100, 0)
    OP_71(0x6, 0x96, 0xC8, 0x0, 0x0)
    OP_79(0x6)
    OP_82(0x0, 0x12C, 0xBB8, 0xC8)
    Sleep(1000)
    ClearScenarioFlags(0xF5, 3)
    ClearScenarioFlags(0xF5, 4)
    SetBarrier(0x2, 0x0, 0x1)
    SetBarrier(0x2, 0x1, 0x1)
    SetBarrier(0x3, 0x2, 0x1)
    SetBarrier(0x3, 0x3, 0x1)
    SetBarrier(0x3, 0x4, 0x1)
    SetBarrier(0x3, 0x5, 0x1)

    label("loc_A8B")

    ClearMapFlags(0x8000000)
    EventEnd(0x5)
    Return()

    # Function_2_723 end

    SaveToFile()

Try(main)
