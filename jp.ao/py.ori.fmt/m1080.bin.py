from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m1080.bin",                # FileName
        "m1080",                    # MapName
        "m1080",                    # Location
        0x0071,                     # MapIndex
        "ed7304",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x21,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 24000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 113, 0, 0, 0, 1],
    )

    BuildStringList((
        "m1080",                  # 0
        "bm1020",                 # 1
        "bm1020",                 # 2
    ))

    ATBonus("ATBonus_168", 100, 5, 1, 5, 1, 5, 1, 5, 5, 5, 5, 5, 5, 0, 0, 0)

    Sepith("Sepith_705", 19,  0,   0,   10,  10,  8,   8)
    Sepith("Sepith_72D", 9,   9,   9,   21,  4,   4,   4)

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
        "BattleInfo_238", 0x0000, 90, 6, 60, 6, 1, 25, 0, "bm1020", "Sepith_705", 40, 30, 20, 10,
        (
            ("ms63300.dat", "ms63300.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1B8", "MonsterBattlePostion_218", "ed7450", "ed7453", "ATBonus_168"),
            ("ms63300.dat", "ms64600.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_198", "MonsterBattlePostion_218", "ed7450", "ed7453", "ATBonus_168"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_1B8", "MonsterBattlePostion_218", "ed7450", "ed7453", "ATBonus_168"),
            ("ms63300.dat", "ms64600.dat", "ms62800.dat", "ms64600.dat", 0, 0, 0, 0, "MonsterBattlePostion_198", "MonsterBattlePostion_218", "ed7450", "ed7453", "ATBonus_168"),
        )
    )

    BattleInfo(
        "BattleInfo_300", 0x0000, 90, 6, 60, 6, 1, 30, 0, "bm1020", "Sepith_72D", 40, 30, 20, 10,
        (
            ("ms75200.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_1B8", "MonsterBattlePostion_218", "ed7450", "ed7453", "ATBonus_168"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_198", "MonsterBattlePostion_218", "ed7450", "ed7453", "ATBonus_168"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, 0, "MonsterBattlePostion_1B8", "MonsterBattlePostion_218", "ed7450", "ed7453", "ATBonus_168"),
            ("ms75200.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", "ms62700.dat", 0, 0, 0, "MonsterBattlePostion_198", "MonsterBattlePostion_218", "ed7450", "ed7453", "ATBonus_168"),
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
        "monster/ch63350.itc",               # 10
        "monster/ch63351.itc",               # 11
        "monster/ch75250.itc",               # 12
        "monster/ch75250.itc",               # 13
    ))

    DeclMonster(-19230,  70,      0,       0x1010000,    "BattleInfo_238", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(22310,   -8980,   1990,    0x1010000,    "BattleInfo_300", 0,   18,  0xFFFF, 2,  3)

    DeclActor(-3730,   2000,    -24060,  1200,    -3730,   3500,    -24060,  0x007C, 0,  2,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4, 5])                    # 1
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 2
    ChipFrameInfo(2000, 0, [0, 1, 2, 3, 4])                      # 3

    ScpFunction((
        "Function_0_404",          # 00, 0
        "Function_1_405",          # 01, 1
        "Function_2_5E1",          # 02, 2
    ))


    def Function_0_404(): pass

    label("Function_0_404")

    Return()

    # Function_0_404 end

    def Function_1_405(): pass

    label("Function_1_405")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_41C")
    OP_50(0x1, (scpexpr(EXPR_PUSH_LONG, 0x15F), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_41C")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_43E")
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetMapObjFlags(0x0, 0x4)
    OP_65(0x0, 0x1)

    label("loc_43E")

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
    OP_52(0x9, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xD7), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x14), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x37, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x320), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x8, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_405 end

    def Function_2_5E1(): pass

    label("Function_2_5E1")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6CE")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x0, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x0, 0x0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x0)
    OP_71(0x0, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x0, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_6CE")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_2_5E1 end

    SaveToFile()

Try(main)
