from ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        "m4120.bin",                # FileName
        "m4120",                    # MapName
        "m4120",                    # Location
        0x00C8,                     # MapIndex
        "ed7351",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x28,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 28000, 500, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 200, 0, 1, 0, 2],
    )

    BuildStringList((
        "m4120",                  # 0
        "フリーザーマッシュ",     # 1
        "bm4110",                 # 2
        "bm4110",                 # 3
        "bm4110",                 # 4
        "bm4110",                 # 5
    ))

    ATBonus("ATBonus_27C", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)
    ATBonus("ATBonus_29C", 100, 5, 0, 5, 0, 5, 0, 2, 5, 0, 0, 0, 2, 0, 0, 0)

    Sepith("Sepith_1A9E", 3,   3,   0,   4,   4,   3,   0)
    Sepith("Sepith_1A86", 2,   7,   2,   2,   0,   3,   0)
    Sepith("Sepith_1AA6", 2,   2,   6,   2,   0,   2,   6)

    MonsterBattlePostion("MonsterBattlePostion_2BC", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C0", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C4", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2C8", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2CC", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D0", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D4", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 2, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_33C", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_340", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_344", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_348", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_34C", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_350", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_354", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F8", 8, 14, 180)

    # monster count: 5

    BattleInfo(
        "BattleInfo_3F8", 0x0000, 54, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_1A9E", 40, 30, 20, 0,
        (
            ("ms79400.dat", "ms79400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms79400.dat", "ms79400.dat", "ms79400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2DC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms79400.dat", "ms79400.dat", "ms79400.dat", "ms79400.dat", 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_35C", 0x0000, 54, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_1A86", 40, 30, 20, 0,
        (
            ("ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2DC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 55, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_1AA6", 40, 30, 20, 0,
        (
            ("ms79500.dat", 0, 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2DC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms79500.dat", "ms79400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms79500.dat", "ms79400.dat", "ms79400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2DC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_530", 0x0C00, 255, 6, 0, 0, 3, 0, 0, "bm4110", 0x00000000, 100, 0, 0, 0,
        (
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", "MonsterBattlePostion_2DC", "MonsterBattlePostion_33C", "ed7451", "ed7453", "ATBonus_29C"),
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
        "monster/ch83450.itc",               # 10
        "monster/ch83451.itc",               # 11
        "chr/ch00000.itc",                   # 12
        "chr/ch00000.itc",                   # 13
        "chr/ch00000.itc",                   # 14
        "chr/ch00000.itc",                   # 15
        "monster/ch79450.itc",               # 16
        "monster/ch79451.itc",               # 17
        "monster/ch79550.itc",               # 18
        "monster/ch79551.itc",               # 19
    ))

    DeclNpc(-12699,  -39500,  213160,  0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(-13190,  211110,  -20000,  0x101002D,    "BattleInfo_3F8", 0,   22,  0xFFFF, 2,  3)
    DeclMonster(-199670, -1030,   4000,    0x101013B,    "BattleInfo_35C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(-210110, -1260,   0,       0x101005A,    "BattleInfo_35C", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(1960,    185270,  -40000,  0x101015E,    "BattleInfo_494", 0,   24,  0xFFFF, 4,  5)
    DeclMonster(-12030,  202770,  -40000,  0x1010082,    "BattleInfo_494", 0,   24,  0xFFFF, 4,  5)

    DeclActor(18600,   -20000,  205190,  1200,    18600,   -19000,  205190,  0x007C, 0,  3,  0x0000)
    DeclActor(7830,    0,       23910,   1200,    7830,    1000,    23910,   0x007C, 0,  4,  0x0000)
    DeclActor(-12700,  -40000,  213160,  1200,    -12700,  -39000,  213160,  0x007C, 0,  5,  0x0000)
    DeclActor(-193760, 4000,    9300,    1200,    -193760, 6000,    9300,    0x007C, 0,  7,  0x0000)
    DeclActor(4710,    0,       425160,  1200,    4710,    1500,    425160,  0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4])                      # 0
    ChipFrameInfo(1200, 0, [0, 1, 2, 3, 4])                      # 1
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 2
    ChipFrameInfo(1500, 0, [0, 1, 2, 3, 4])                      # 3
    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 2, 1])                   # 4
    ChipFrameInfo(800, 0, [0, 1, 2, 3, 4])                       # 5

    ScpFunction((
        "Function_0_5E0",          # 00, 0
        "Function_1_5FC",          # 01, 1
        "Function_2_60E",          # 02, 2
        "Function_3_8CA",          # 03, 3
        "Function_4_A1B",          # 04, 4
        "Function_5_B6C",          # 05, 5
        "Function_6_D83",          # 06, 6
        "Function_7_E7F",          # 07, 7
        "Function_8_F18",          # 08, 8
    ))


    def Function_0_5E0(): pass

    label("Function_0_5E0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5FB")
    OP_A1(0xFE, 0x3E8, 0x5, 0x0, 0x1, 0x2, 0x3, 0x4)
    Jump("Function_0_5E0")

    label("loc_5FB")

    Return()

    # Function_0_5E0 end

    def Function_1_5FC(): pass

    label("Function_1_5FC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x12A, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_60D")
    Event(0, 8)

    label("loc_60D")

    Return()

    # Function_1_5FC end

    def Function_2_60E(): pass

    label("Function_2_60E")

    OP_52(0xC, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xC, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x14, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xD, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x15, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xE, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x16, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0xF, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x17, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x10, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x18, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x11, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x19, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x12, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1A, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x13, (scpexpr(EXPR_PUSH_LONG, 0x80), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x1B, (scpexpr(EXPR_PUSH_LONG, 0xDB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x37, (scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x33, (scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xC, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_52(0xD, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetBarrier(0x0, 0x0, 0x1, 0x0, 16500, 3000, 205000, 8000, 5000, 15000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7FD")
    SetMapObjFrame(0xFF, "extra", 0x0, 0x1)
    SetMapObjFrame(0xFF, "kinoko", 0x1, 0x1)
    SetMapObjFlags(0x3, 0x4)
    Jump("loc_836")

    label("loc_7FD")

    SetMapObjFrame(0xFF, "extra", 0x1, 0x1)
    SetMapObjFrame(0xFF, "kinoko", 0x0, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1A0, 0)), scpexpr(EXPR_END)), "loc_830")
    SetMapObjFlags(0x3, 0x4)
    SetBarrier(0x2, 0x0, 0x1)
    Jump("loc_836")

    label("loc_830")

    ClearMapObjFlags(0x3, 0x4)

    label("loc_836")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_864")
    SetMapObjFrame(0xFF, "hasigo_a", 0x0, 0x1)
    SetMapObjFrame(0xFF, "hasigo_b", 0x1, 0x1)
    Jump("loc_884")

    label("loc_864")

    SetMapObjFrame(0xFF, "hasigo_a", 0x1, 0x1)
    SetMapObjFrame(0xFF, "hasigo_b", 0x0, 0x1)

    label("loc_884")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_897")
    OP_70(0x0, 0x0)
    Jump("loc_89B")

    label("loc_897")

    OP_70(0x0, 0x1E)

    label("loc_89B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8AE")
    OP_70(0x1, 0x0)
    Jump("loc_8B2")

    label("loc_8AE")

    OP_70(0x1, 0x1E)

    label("loc_8B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_8C5")
    OP_70(0x2, 0x0)
    Jump("loc_8C9")

    label("loc_8C5")

    OP_70(0x2, 0x1E)

    label("loc_8C9")

    Return()

    # Function_2_60E end

    def Function_3_8CA(): pass

    label("Function_3_8CA")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9CA")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x20C, 1)"), scpexpr(EXPR_END)), "loc_953")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_9C5")

    label("loc_953")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_9C5")

    Jump("loc_A0F")

    label("loc_9CA")

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

    label("loc_A0F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_8CA end

    def Function_4_A1B(): pass

    label("Function_4_A1B")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B1B")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x334, 1)"), scpexpr(EXPR_END)), "loc_AA4")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
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
    SetScenarioFlags(0x1FA, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_B16")

    label("loc_AA4")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
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
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_B16")

    Jump("loc_B60")

    label("loc_B1B")

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

    label("loc_B60")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A1B end

    def Function_5_B6C(): pass

    label("Function_5_B6C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D3D")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C6B")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_BC9():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_BC9)

    def lambda_BE3():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BE3)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

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
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_530", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C4C"),
        (2, "loc_C5B"),
        (1, "loc_C68"),
        (SWITCH_DEFAULT, "loc_C6B"),
    )


    label("loc_C4C")

    SetScenarioFlags(0x216, 3)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_C6B")

    label("loc_C5B")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_C68")

    OP_B9(0x0)
    Return()

    label("loc_C6B")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber(0x4F, 1)"), scpexpr(EXPR_END)), "loc_CC8")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "を手に入れた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_D38")

    label("loc_CC8")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱には",
            scpstr(SCPSTR_CODE_ITEM, 0x4F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "が入っている。\x01",
            "持ち物が一杯なので、",
            scpstr(SCPSTR_CODE_ITEM, 0x4F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "をあきらめた。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_D38")

    Jump("loc_D77")

    label("loc_D3D")

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

    label("loc_D77")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B6C end

    def Function_6_D83(): pass

    label("Function_6_D83")

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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E70")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_74(0x4, 0x1E)
    Sound(7, 0, 100, 0)
    OP_70(0x4, 0x0)
    OP_71(0x4, 0x0, 0x1E, 0x0, 0x0)
    OP_79(0x4)
    OP_71(0x4, 0x1F, 0x186, 0x0, 0x20)
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
    OP_70(0x4, 0x0)
    OP_1F()
    FadeToBright(1000, 0)
    OP_57(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_E70")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_6_D83 end

    def Function_7_E7F(): pass

    label("Function_7_E7F")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_EF6")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "ハシゴがある。\x01",
            "登りますか？\x02",
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EF1")
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("m4160", 106, 0, 0)
    IdleLoop()

    label("loc_EF1")

    Jump("loc_F15")

    label("loc_EF6")


    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "壊れたハシゴがある。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_F15")

    EventEnd(0x5)
    Return()

    # Function_7_E7F end

    def Function_8_F18(): pass

    label("Function_8_F18")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E2(0x3)
    SoundLoad(814)
    OP_68(-10, 3330, -15780, 0)
    MoveCamera(65, 25, 0, 0)
    OP_6E(700, 0)
    SetCameraDistance(16910, 0)
    SetChrPos(0x101, -800, 2330, -15700, 0)
    SetChrPos(0x102, 800, 2330, -15700, 0)
    SetChrPos(0x109, -800, 2330, -17300, 0)
    SetChrPos(0x105, 800, 3330, -17300, 0)
    FadeToBright(1000, 0)
    OP_68(0, 1160, -7500, 5000)
    SetCameraDistance(14430, 5000)
    Sleep(50)

    def lambda_FC6():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_FC6)
    Sleep(50)

    def lambda_FDE():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_FDE)
    Sleep(50)

    def lambda_FF6():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_FF6)
    Sleep(50)

    def lambda_100E():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_100E)
    Sleep(50)
    WaitChrThread(0x101, 3)
    WaitChrThread(0x102, 3)
    WaitChrThread(0x109, 3)
    WaitChrThread(0x105, 3)
    OP_6F(0x79)
    Sleep(300)

    #C0014
    ChrTalk(
        0x101,
        (
            "#00008F#6Pこうして見ると……\x01",
            "この紫の光は植物のものみたいだな。\x02\x03",

            "#00001F苔にキノコが多いみたいだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        (
            "#10106F#12Pどう考えても、ただの鉱山跡とは\x01",
            "思えないような場所ですよね……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)
    Sleep(300)

    #C0016
    ChrTalk(
        0x102,
        (
            "#00103F#5P光る苔というのは\x01",
            "どこかで聞いたことがあるわ。\x02\x03",

            "#00101F《ゼムリア苔》という名前で\x01",
            "薬にも使われるそうだけど……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_117C():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_117C)
    Sleep(100)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0017
    ChrTalk(
        0x101,
        "#00005F#6Pへぇ、そんなものがあるのか。\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#00106F#5Pでも、聞いていた色とは\x01",
            "ぜんぜん違うのよね……\x02\x03",

            "#00100F別の種類かもしれないわ。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)
    Sleep(200)

    #C0019
    ChrTalk(
        0x105,
        (
            "#10302F#11Pいや……\x01",
            "《ゼムリア苔》で合ってるよ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_125D():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_125D)
    Sleep(50)

    def lambda_126D():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_126D)
    Sleep(50)

    def lambda_127D():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_127D)
    Sleep(100)

    #C0020
    ChrTalk(
        0x102,
        "#00105F#5Pえ。\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        (
            "#10304F#11P本来、ゼムリア苔は\x01",
            "金色の光を放つんだけど……\x02\x03",

            "#10300Fたまに七耀脈の影響を受けて\x01",
            "色を変化させることがあるんだ。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#00100F#5Pそうだったの……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x105,
        (
            "#10303F#11Pちなみにキノコの方は\x01",
            "《ホタル茸》って種類だね。\x02\x03",

            "#10308Fこちらは本来、緑色の光を放つし、\x01",
            "ここまで巨大化する事はない……\x02\x03",

            "#10301Fどうやら、七耀脈の流れに\x01",
            "何らかの異常があるみたいだね。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00101F#5P七耀脈の流れの異常……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00003F#6Pという事は、トラップを仕掛けた\x01",
            "犯人とは関係なさそうだな。\x02\x03",

            "#00008F入口の扉が壊されたのは昨日……\x02\x03",

            "#00001F一日やそこらで、こんな風に\x01",
            "大量に繁殖するとは思えないし。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        "#10300F#11Pまあ、そうだね。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x109,
        (
            "#10102F#6Pでもワジ君、すごく博識だね。\x02\x03",

            "どこで仕入れた知識なの？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_93(0x105, 0x10E, 0x1F4)

    #C0028
    ChrTalk(
        0x105,
        (
            "#10305F#11Pああ、最近知り合った客に\x01",
            "薬草とか詳しいヒトがいてさ。\x02\x03",

            "#10309F店で差しつ差されつしてる時に\x01",
            "色々教えてもらったってワケ㈱\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        "#10106F#6P……聞くんじゃなかった。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00012F#6Pはあ……\x01",
            "そんな事だろうと思ったよ。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#00111F#5Pいくらホストの仕事とはいえ、\x01",
            "未成年でお酒は感心しないわね。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(150)

    #C0032
    ChrTalk(
        0x105,
        (
            "#10304F#11Pフフ、人聞きが悪いなぁ。\x02\x03",

            "#10302Fあくまでノンアルコールの\x01",
            "カクテルなんだけど。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00006F#6P（ホントかよ……）\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    Sound(814, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0034
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※バーストの活用法について\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0035
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "※バーストはストーリー中、\x01",
            "　限定されたタイミングでしか使えませんが\x01",
            "　工夫しだいで驚くほど有利な使い方ができます。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0036
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2C①攻撃力が２０％上昇し、ＣＰも自動上昇するので\x01",
            "　攻撃クラフトがさらに使いやすく強力になる。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    #A0037
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2C②発動時に、味方全員の状態異常が回復し、\x01",
            "　敵の技やアーツも全てキャンセルできるため、\x01",
            "　ピンチを一気にひっくり返すことが出来る。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    Sleep(150)

    #A0038
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#2C③本来、発動にかなりの時間を必要とする\x01",
            "　範囲系の上位アーツも即座に発動できるので\x01",
            "　ＥＰさえあれば一気に敵集団を殲滅することも…。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0039
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "#5C※特にアーツは、敵の弱点属性を狙い撃てるので\x01",
            "　バーストの醍醐味を気軽に味わう事ができます。\x02\x03",

            "※手強いボス戦や、宝箱魔獣の攻略などに\x01",
            "　積極的に役立ててみてください。\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    SetChrPos(0x0, 0, 30, -7150, 0)
    SetScenarioFlags(0x12A, 3)
    OP_29(0xA2, 0x1, 0x3)
    Sleep(500)
    OP_E2(0x2)
    EventEnd(0x5)
    Return()

    # Function_8_F18 end

    SaveToFile()

Try(main)
