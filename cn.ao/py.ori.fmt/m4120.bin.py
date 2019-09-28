from ScenarioHelper import *

def main():
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

    Sepith("Sepith_1947", 3,   3,   0,   4,   4,   3,   0)
    Sepith("Sepith_192F", 2,   7,   2,   2,   0,   3,   0)
    Sepith("Sepith_194F", 2,   2,   6,   2,   0,   2,   6)

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
        "BattleInfo_3F8", 0x0000, 54, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_1947", 40, 30, 20, 0,
        (
            ("ms79400.dat", "ms79400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms79400.dat", "ms79400.dat", "ms79400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2DC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms79400.dat", "ms79400.dat", "ms79400.dat", "ms79400.dat", 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_35C", 0x0000, 54, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_192F", 40, 30, 20, 0,
        (
            ("ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2DC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            ("ms83400.dat", "ms83400.dat", "ms83400.dat", "ms83400.dat", 0, 0, 0, 0, "MonsterBattlePostion_2BC", "MonsterBattlePostion_33C", "ed7450", "ed7453", "ATBonus_27C"),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_494", 0x0000, 55, 6, 45, 10, 1, 30, 0, "bm4110", "Sepith_194F", 40, 30, 20, 0,
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
        "Function_4_A05",          # 04, 4
        "Function_5_B40",          # 05, 5
        "Function_6_D3E",          # 06, 6
        "Function_7_E22",          # 07, 7
        "Function_8_EA9",          # 08, 8
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9BC")
    Sound(14, 0, 100, 0)
    OP_74(0x0, 0x1E)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('爆灵宝玉', 1)"), scpexpr(EXPR_END)), "loc_94D")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 4)
    OP_E0(0x5, 0x0)
    Jump("loc_9B7")

    label("loc_94D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x20C),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_9B7")

    Jump("loc_9F9")

    label("loc_9BC")

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

    label("loc_9F9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_8CA end

    def Function_4_A05(): pass

    label("Function_4_A05")

    OP_F4(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AF7")
    Sound(14, 0, 100, 0)
    OP_74(0x1, 0x1E)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('结晶碎片', 1)"), scpexpr(EXPR_END)), "loc_A88")
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
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 5)
    OP_E0(0x5, 0x0)
    Jump("loc_AF2")

    label("loc_A88")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多，",
            scpstr(SCPSTR_CODE_ITEM, 0x334),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_AF2")

    Jump("loc_B34")

    label("loc_AF7")

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

    label("loc_B34")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_A05 end

    def Function_5_B40(): pass

    label("Function_5_B40")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1FA, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D00")
    Sound(14, 0, 100, 0)
    OP_74(0x2, 0x1E)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x216, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3D")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_B9D():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_B9D)

    def lambda_BB7():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_BB7)
    ClearChrFlags(0x8, 0x80)
    SetChrFlags(0x8, 0x8000)

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
    WaitChrThread(0x8, 1)
    Battle("BattleInfo_530", 0x0, 0x0, 0x0, 0xB, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_C1E"),
        (2, "loc_C2D"),
        (1, "loc_C3A"),
        (SWITCH_DEFAULT, "loc_C3D"),
    )


    label("loc_C1E")

    SetScenarioFlags(0x216, 3)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_C3D")

    label("loc_C2D")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_C3A")

    OP_B9(0x0)
    Return()

    label("loc_C3D")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('必胜扎头巾', 1)"), scpexpr(EXPR_END)), "loc_C94")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 0x4F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x1FA, 6)
    OP_E0(0x5, 0x0)
    Jump("loc_CFB")

    label("loc_C94")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 0x4F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 0x4F),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_CFB")

    Jump("loc_D32")

    label("loc_D00")

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

    label("loc_D32")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_B40 end

    def Function_6_D3E(): pass

    label("Function_6_D3E")

    OP_F4(0x2)
    FadeToDark(300, 0, 100)

    #A0011
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
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E13")
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

    label("loc_E13")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_6_D3E end

    def Function_7_E22(): pass

    label("Function_7_E22")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x140, 0)), scpexpr(EXPR_END)), "loc_E8B")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个梯子。\x01",
            "要上去吗？\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "是\x01",      # 0
            "否\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E86")
    FadeToDark(500, 0, -1)
    OP_0D()
    EventEnd(0x5)
    NewScene("m4160", 106, 0, 0)
    IdleLoop()

    label("loc_E86")

    Jump("loc_EA6")

    label("loc_E8B")


    #A0013
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "有个坏掉的梯子。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    OP_5A()

    label("loc_EA6")

    EventEnd(0x5)
    Return()

    # Function_7_E22 end

    def Function_8_EA9(): pass

    label("Function_8_EA9")

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

    def lambda_F57():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F57)
    Sleep(50)

    def lambda_F6F():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_F6F)
    Sleep(50)

    def lambda_F87():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F87)
    Sleep(50)

    def lambda_F9F():
        OP_9B(0x0, 0xFE, 0x0, 0x2328, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_F9F)
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
            "#00008F#6P仔细一看……\x01",
            "这些散发着紫色光芒的东西似乎是种植物呢。\x02\x03",

            "#00001F看起来，大多是些苔藓与菇类。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x109,
        (
            "#10106F#12P不管怎么看，这个地方也不像是\x01",
            "普通的废弃矿山啊……\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x102, 0xE1, 0x1F4)
    Sleep(300)

    #C0016
    ChrTalk(
        0x102,
        (
            "#00103F#5P我过去曾听说过\x01",
            "一种会发光的苔藓。\x02\x03",

            "#00101F名字叫做『塞姆里亚苔藓』，\x01",
            "似乎还是一种药用植物……\x02",
        )
    )

    CloseMessageWindow()

    def lambda_10EF():
        OP_93(0xFE, 0x2D, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10EF)
    Sleep(100)
    OP_93(0x101, 0x5A, 0x1F4)

    #C0017
    ChrTalk(
        0x101,
        "#00005F#6P哦？还有那种东西吗？\x02",
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x102,
        (
            "#00106F#5P不过，这颜色和我\x01",
            "所听说的完全不同……\x02\x03",

            "#00100F也许是其它种类吧。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x13B, 0x1F4)
    Sleep(200)

    #C0019
    ChrTalk(
        0x105,
        (
            "#10302F#11P不……\x01",
            "这的确是『塞姆里亚苔藓』。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_11B6():
        OP_93(0xFE, 0xB4, 0x1F4)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_11B6)
    Sleep(50)

    def lambda_11C6():
        OP_93(0xFE, 0x87, 0x1F4)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_11C6)
    Sleep(50)

    def lambda_11D6():
        OP_93(0xFE, 0x5A, 0x1F4)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11D6)
    Sleep(100)

    #C0020
    ChrTalk(
        0x102,
        "#00105F#5P哎？\x02",
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x105,
        (
            "#10304F#11P塞姆里亚苔藓原本\x01",
            "散发着金色光芒……\x02\x03",

            "#10300F但有时也会受到七耀脉的影响，\x01",
            "导致颜色发生变化。\x02",
        )
    )

    CloseMessageWindow()

    #C0022
    ChrTalk(
        0x102,
        "#00100F#5P原来如此……\x02",
    )

    CloseMessageWindow()

    #C0023
    ChrTalk(
        0x105,
        (
            "#10303F#11P顺便一说，这些菇类是\x01",
            "名为『荧光菇』的品种。\x02\x03",

            "#10308F这种蘑菇本应散发绿光，\x01",
            "而且不可能生长得如此巨大……\x02\x03",

            "#10301F看样子，七耀脉的流动\x01",
            "似乎出现了某种异常呢。\x02",
        )
    )

    CloseMessageWindow()

    #C0024
    ChrTalk(
        0x102,
        "#00101F#5P七耀脉的流动出现异常……\x02",
    )

    CloseMessageWindow()

    #C0025
    ChrTalk(
        0x101,
        (
            "#00003F#6P也就是说，这和布置陷阱的\x01",
            "犯人应该没什么关系吧？\x02\x03",

            "#00008F破坏入口大门的时间是昨天……\x02\x03",

            "#00001F在短短一天的时间里，绝不可能\x01",
            "使这些东西大量繁殖到这种程度。\x02",
        )
    )

    CloseMessageWindow()

    #C0026
    ChrTalk(
        0x105,
        "#10300F#11P嗯，说的没错。\x02",
    )

    CloseMessageWindow()

    #C0027
    ChrTalk(
        0x109,
        (
            "#10102F#6P瓦吉，你还真是博识啊。\x02\x03",

            "那些知识是从哪里学来的？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_93(0x105, 0x10E, 0x1F4)

    #C0028
    ChrTalk(
        0x105,
        (
            "#10305F#11P哦，最近认识了一位\x01",
            "对药草类的知识相当熟悉的客人。\x02\x03",

            "#10309F在店里你一杯我一杯地对饮时，\x01",
            "对方顺便教给我不少东西呢⊥\x02",
        )
    )

    CloseMessageWindow()

    #C0029
    ChrTalk(
        0x109,
        "#10106F#6P……就当我没问吧。\x02",
    )

    CloseMessageWindow()

    #C0030
    ChrTalk(
        0x101,
        (
            "#00012F#6P呼……\x01",
            "我就知道是这样。\x02",
        )
    )

    CloseMessageWindow()

    #C0031
    ChrTalk(
        0x102,
        (
            "#00111F#5P虽说那属于公关的工作，\x01",
            "但我还是觉得未成年人不该喝酒。\x02",
        )
    )

    CloseMessageWindow()
    OP_93(0x105, 0x0, 0x1F4)
    Sleep(150)

    #C0032
    ChrTalk(
        0x105,
        (
            "#10304F#11P呵呵，别这么严厉嘛。\x02\x03",

            "#10302F反正只是不含酒精的\x01",
            "鸡尾酒而已。\x02",
        )
    )

    CloseMessageWindow()

    #C0033
    ChrTalk(
        0x101,
        "#00006F#6P（真的吗……）\x02",
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
            "※关于爆灵的灵活运用\x07\x00\x02",
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
            "※在剧情的进展过程中，\x01",
            "　仅在某些特定的时段才能使用爆灵系统，\x01",
            "　只要巧妙运用，就可在战斗中使我方获得惊人优势。\x02",
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
            "#2C①攻击力增加２０％，ＣＰ也会自动上升，\x01",
            "　攻击类战技会更加强大，更容易发动。\x02",
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
            "#2C②发动爆灵时，我方全员的异常状态都将恢复，\x01",
            "　同时强行终止敌人驱动中的所有战技与魔法。\x01",
            "　当陷入危机时，使用爆灵可以一举扭转局势。\x02",
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
            "#2C③原本需要消耗大量驱动时间的大范围\x01",
            "　高级魔法，在爆灵状态下可以即时发动，\x01",
            "　只要ＥＰ充足，甚至可以一口气歼灭所有敌人。\x02",
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
            "#5C※魔法能够针对敌人的弱点属性进行攻击，\x01",
            "　更能让人感受到爆灵状态的强大之处。\x02\x03",

            "※当面对棘手的BOSS级敌人或宝箱魔兽时，\x01",
            "　请体会爆灵强悍效果的乐趣吧。\x07\x00\x02",
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

    # Function_8_EA9 end

    SaveToFile()

Try(main)
