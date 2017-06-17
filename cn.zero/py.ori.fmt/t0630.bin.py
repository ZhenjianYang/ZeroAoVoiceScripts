from ZeroScenarioHelper import *

def main():
    CreateScenaFile(
        "t0630.bin",                # FileName
        "t0630",                    # MapName
        "t0630",                    # Location
        0x006A,                     # MapIndex
        "ed7301",
        0x00000000,                 # Flags
        ("", "", "", "", "", ""),   # include
        0x00,                       # PlaceNameNumber
        0x00,                       # PreInitFunctionIndex
        b'\x00\xff\xff',            # Unknown_51

        # Information
        [0, 0, -1000, 0, 0, 0, 34000, 262, 30, 45, 0, 360, 0, 0, 0, 0, 0, 1, 106, 0, 1, 0, 2],
    )

    BuildStringList((
        "t0630",                  # 0
        "温古德安特",             # 1
        "bt0610",                 # 2
        "bt0610",                 # 3
        "bt0610",                 # 4
    ))

    ATBonus("ATBonus_298", 100, 5, 1, 5, 1, 5, 1, 5, 5, 0, 0, 0, 1, 0, 0, 0)

    Sepith("Sepith_10E3", 10,  7,   0,   7,   9,   6,   9)

    MonsterBattlePostion("MonsterBattlePostion_2F8", 8, 8, 180)
    MonsterBattlePostion("MonsterBattlePostion_2FC", 5, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_300", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_304", 6, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_308", 10, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_30C", 13, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_310", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_314", 8, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_358", 7, 4, 0)
    MonsterBattlePostion("MonsterBattlePostion_35C", 10, 11, 225)
    MonsterBattlePostion("MonsterBattlePostion_360", 4, 7, 90)
    MonsterBattlePostion("MonsterBattlePostion_364", 12, 7, 270)
    MonsterBattlePostion("MonsterBattlePostion_368", 4, 11, 135)
    MonsterBattlePostion("MonsterBattlePostion_36C", 11, 4, 315)
    MonsterBattlePostion("MonsterBattlePostion_370", 7, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_374", 5, 5, 45)
    MonsterBattlePostion("MonsterBattlePostion_2D8", 7, 9, 180)
    MonsterBattlePostion("MonsterBattlePostion_2DC", 11, 10, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E0", 10, 13, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E4", 5, 11, 180)
    MonsterBattlePostion("MonsterBattlePostion_2E8", 12, 12, 180)
    MonsterBattlePostion("MonsterBattlePostion_2EC", 4, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F0", 14, 14, 180)
    MonsterBattlePostion("MonsterBattlePostion_2F4", 2, 13, 180)

    # monster count: 8

    BattleInfo(
        "BattleInfo_378", 0x0000, 23, 6, 60, 6, 1, 40, 0, "bt0610", "Sepith_10E3", 75, 25, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7400", "ed7403", "ATBonus_298"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, "MonsterBattlePostion_2D8", "MonsterBattlePostion_358", "ed7400", "ed7403", "ATBonus_298"),
            (),
            (),
        )
    )

    BattleInfo(
        "BattleInfo_42C", 0x0400, 23, 6, 60, 6, 1, 40, 0, "bt0610", "Sepith_10E3", 75, 25, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, 0, "MonsterBattlePostion_2F8", "MonsterBattlePostion_358", "ed7400", "ed7403", "ATBonus_298"),
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", 0, 0, 0, 0, "MonsterBattlePostion_2D8", "MonsterBattlePostion_358", "ed7400", "ed7403", "ATBonus_298"),
            (),
            (),
        )
    )

    # event battle count: 1

    BattleInfo(
        "BattleInfo_3E8", 0x0000, 23, 6, 45, 0, 1, 0, 0, "bt0610", 0x00000000, 100, 0, 0, 0,
        (
            ("ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "ms64800.dat", "MonsterBattlePostion_2D8", "MonsterBattlePostion_358", "ed7401", "ed7403", "ATBonus_298"),
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
        "monster/ch64850.itc",               # 10
        "monster/ch64851.itc",               # 11
    ))

    DeclNpc(20110,   1500,    -32299,  0,    484,  0x0, 0,   16,  0,   0,   0,   255, 255, 255,  0)

    DeclMonster(100120,  29150,   8050,    0x1010000,    "BattleInfo_378", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(58300,   29340,   3550,    0x1010000,    "BattleInfo_378", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(71140,   -970,    800,     0x1010000,    "BattleInfo_378", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(47150,   -13350,  -3950,   0x10100B4,    "BattleInfo_378", 0,   16,  0xFFFF, 0,  1)
    DeclMonster(100120,  29150,   8050,    0x1810000,    "BattleInfo_42C", 1504, 16,  0xFFFF, 0,  1)
    DeclMonster(58300,   29340,   3550,    0x1810000,    "BattleInfo_42C", 1505, 16,  0xFFFF, 0,  1)
    DeclMonster(71140,   -970,    800,     0x1810000,    "BattleInfo_42C", 1506, 16,  0xFFFF, 0,  1)
    DeclMonster(47150,   -13350,  -3950,   0x18100B4,    "BattleInfo_42C", 1507, 16,  0xFFFF, 0,  1)

    DeclActor(105900,  8000,    24800,   1200,    105900,  9000,    24800,   0x007C, 0,  3,  0x0000)
    DeclActor(42580,   -1250,   580,     1200,    42580,   -250,    580,     0x007C, 0,  4,  0x0000)
    DeclActor(20110,   1000,    -32299,  1200,    20110,   2000,    -32299,  0x007C, 0,  5,  0x0000)
    DeclActor(55680,   -1750,   -41900,  1200,    52000,   -6150,   -45150,  0x007C, 0,  6,  0x0000)

    ChipFrameInfo(1000, 0, [0, 1, 2, 3, 4, 3, 2, 1])             # 0
    ChipFrameInfo(1500, 0, [0, 1, 2, 1, 0, 3, 4, 3])             # 1

    ScpFunction((
        "Function_0_4D4",          # 00, 0
        "Function_1_4F3",          # 01, 1
        "Function_2_560",          # 02, 2
        "Function_3_64F",          # 03, 3
        "Function_4_785",          # 04, 4
        "Function_5_8BB",          # 05, 5
        "Function_6_AB5",          # 06, 6
        "Function_7_D80",          # 07, 7
    ))


    def Function_0_4D4(): pass

    label("Function_0_4D4")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4F2")
    OP_A1(0xFE, 0x3E8, 0x8, 0x0, 0x1, 0x2, 0x3, 0x4, 0x3, 0x2, 0x1)
    Jump("Function_0_4D4")

    label("loc_4F2")

    Return()

    # Function_0_4D4 end

    def Function_1_4F3(): pass

    label("Function_1_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xC0, 0)), scpexpr(EXPR_END)), "loc_501")
    Jump("loc_55F")

    label("loc_501")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xA7, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_55F")
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xC, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_532")
    ClearChrFlags(0xD, 0x80)

    label("loc_532")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_541")
    ClearChrFlags(0xE, 0x80)

    label("loc_541")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_550")
    ClearChrFlags(0xF, 0x80)

    label("loc_550")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_55F")
    ClearChrFlags(0x10, 0x80)

    label("loc_55F")

    Return()

    # Function_1_4F3 end

    def Function_2_560(): pass

    label("Function_2_560")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_573")
    OP_70(0x0, 0x0)
    Jump("loc_577")

    label("loc_573")

    OP_70(0x0, 0x1E)

    label("loc_577")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_58A")
    OP_70(0x1, 0x0)
    Jump("loc_58E")

    label("loc_58A")

    OP_70(0x1, 0x1E)

    label("loc_58E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A1")
    OP_70(0x2, 0x0)
    Jump("loc_5A5")

    label("loc_5A1")

    OP_70(0x2, 0x1E)

    label("loc_5A5")

    Sound(124, 1, 100, 0)
    LoadEffect(0x8, "eff\\mgm03_02.eff")
    PlayEffect(0x8, 0x8, 0xFF, 0x0, 52000, -6150, -45150, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBA, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBB, 7)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 0)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0xBC, 3)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_2A(0x1C, 0x1, 0x4)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_64E")
    Event(0, 7)

    label("loc_64E")

    Return()

    # Function_2_560 end

    def Function_3_64F(): pass

    label("Function_3_64F")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_73C")
    Sound(14, 0, 100, 0)
    OP_71(0x0, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('ＥＰ填充剂Ⅰ', 1)"), scpexpr(EXPR_END)), "loc_6CE")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0001
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 1)
    OP_DE(0x6, 0x0)
    Jump("loc_737")

    label("loc_6CE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0002
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, 'ＥＰ填充剂Ⅰ'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x0, 0x1E, 0x0, 0x0, 0x0)

    label("loc_737")

    Jump("loc_779")

    label("loc_73C")

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

    label("loc_779")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_64F end

    def Function_4_785(): pass

    label("Function_4_785")

    OP_F2(0x1)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_872")
    Sound(14, 0, 100, 0)
    OP_71(0x1, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('必胜扎头巾', 1)"), scpexpr(EXPR_END)), "loc_804")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    #A0004
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '必胜扎头巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 2)
    OP_DE(0x6, 0x0)
    Jump("loc_86D")

    label("loc_804")

    FadeToDark(300, 0, 100)
    SetChrName("")

    #A0005
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '必胜扎头巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '必胜扎头巾'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x1, 0x1E, 0x0, 0x0, 0x0)

    label("loc_86D")

    Jump("loc_8AF")

    label("loc_872")

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

    label("loc_8AF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_785 end

    def Function_5_8BB(): pass

    label("Function_5_8BB")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x115, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A77")
    Sound(14, 0, 100, 0)
    OP_71(0x2, 0x0, 0x1E, 0x0, 0x0)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x75, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9B4")
    OP_A7(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_98(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_914():
        OP_98(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_914)

    def lambda_92E():
        OP_A7(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x3E8)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_92E)
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
    Battle("BattleInfo_3E8", 0x0, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x8000)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_995"),
        (2, "loc_9A4"),
        (1, "loc_9B1"),
        (SWITCH_DEFAULT, "loc_9B4"),
    )


    label("loc_995")

    SetScenarioFlags(0x75, 3)
    OP_70(0x2, 0x1E)
    Sleep(500)
    Jump("loc_9B4")

    label("loc_9A4")

    OP_70(0x2, 0x0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_9B1")

    OP_B7(0x0)
    Return()

    label("loc_9B4")

    Jc((scpexpr(EXPR_EXEC_OP, "AddItemNumber('黑靴', 1)"), scpexpr(EXPR_END)), "loc_A0B")
    FadeToDark(300, 0, 100)
    Sound(17, 0, 100, 0)
    SetMessageWindowPos(-1, -1, -1, -1)

    #A0008
    AnonymousTalk(
        0x3E7,
        (
            scpstr(SCPSTR_CODE_ITEM, '黑靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "获得了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    SetMessageWindowPos(14, 280, 60, 3)
    FadeToBright(300, 0)
    SetScenarioFlags(0x115, 3)
    OP_DE(0x6, 0x0)
    Jump("loc_A72")

    label("loc_A0B")

    FadeToDark(300, 0, 100)

    #A0009
    AnonymousTalk(
        0x3E7,
        (
            "宝箱里装有",
            scpstr(SCPSTR_CODE_ITEM, '黑靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "。\x01",
            "不过现有的数量太多,",
            scpstr(SCPSTR_CODE_ITEM, '黑靴'),
            scpstr(SCPSTR_CODE_COLOR, 0x0),
            "不能再拿更多了。\x02",
        )
    )

    CloseMessageWindow()
    OP_57(0x0)
    FadeToBright(300, 0)
    Sound(15, 0, 100, 0)
    OP_71(0x2, 0x1E, 0x0, 0x0, 0x0)

    label("loc_A72")

    Jump("loc_AA9")

    label("loc_A77")

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

    label("loc_AA9")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_8BB end

    def Function_6_AB5(): pass

    label("Function_6_AB5")

    EventBegin(0x1)
    Sound(1094, 255, 100, 0)    #voice#Lloyd

    #C0011
    ChrTalk(
        0x101,
        "#0000F这里的话似乎可以钓到鱼。\x02",
    )

    CloseMessageWindow()
    OP_68(52750, -2850, -44000, 1500)
    MoveCamera(90, 27, 0, 1500)
    OP_6E(500, 1500)
    SetCameraDistance(26000, 1500)
    Sleep(1000)
    SetChrName("")

    #A0012
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "要钓鱼吗？\x07\x00\x02",
        )
    )


    Menu(
        0,
        -1,
        -1,
        1,
        (
            "钓鱼\x01",      # 0
            "放弃\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    OP_6F(0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7B")
    OP_E0(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_END)), "loc_B86")
    MiniGame(0x6, 0x7, 0xD6D8, 0xFFFFF92A, 0xFFFF5AF6, 0xE1, 0xCB20, 0xFFFFE7FA, 0xFFFF4FA2)
    Jump("loc_D7B")

    label("loc_B86")

    MiniGame(0x6, 0x8, 0xD6D8, 0xFFFFF92A, 0xFFFF5AF6, 0xE1, 0xCB20, 0xFFFFE7FA, 0xFFFF4FA2)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x45), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D7B")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_E2(0x0, 0x15, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x69, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_D7B")
    FadeToDark(0, 0, -1)
    EventBegin(0x0)
    OP_68(55000, -250, -42250, 0)
    MoveCamera(90, 24, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(20500, 0)
    LoadChrToIndex("apl/ch50162.itc", 0x1E)
    SetChrFlags(0x0, 0x2)
    SetChrChipByIndex(0x0, 0x1E)
    SetChrSubChip(0x0, 0x12)
    SetChrPos(0x0, 55000, -1750, -42250, 225)
    SetChrFlags(0x1, 0x8)
    SetChrFlags(0x2, 0x8)
    SetChrFlags(0x3, 0x8)
    FadeToBright(1000, 0)
    OP_0D()

    #N0013
    NpcTalk(
        0x0,
        "罗伊德",
        (
            "#0005F这、这是什么……\x02\x03",

            "#0003F钓上了很漂亮的鱼呢……\x01",
            "难道这是一条十分稀有的\x01",
            "特别鱼类吗。\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_68(55000, -250, -42250, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(27000, 0)
    ClearChrFlags(0x1, 0x8)
    ClearChrFlags(0x2, 0x8)
    ClearChrFlags(0x3, 0x8)
    SetChrPos(0x1, 55000, -1750, -42250, 225)
    SetChrPos(0x2, 55000, -1750, -42250, 225)
    SetChrPos(0x3, 55000, -1750, -42250, 225)
    SetChrPos(0x4, 55000, -1750, -42250, 225)
    SetChrPos(0x5, 55000, -1750, -42250, 225)
    SetChrPos(0x6, 55000, -1750, -42250, 225)
    SetChrPos(0x7, 55000, -1750, -42250, 225)
    SetChrChipByIndex(0x0, 0xFF)
    SetChrSubChip(0x0, 0x0)
    ClearChrFlags(0x0, 0x2)
    OP_49()
    OP_D5(0x1E)
    OP_37()
    SetScenarioFlags(0x69, 2)

    label("loc_D7B")

    OP_E0(0x2)
    EventEnd(0x4)
    Return()

    # Function_6_AB5 end

    def Function_7_D80(): pass

    label("Function_7_D80")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_E0(0x1)
    OP_68(63530, -200, -37770, 0)
    MoveCamera(45, 23, 0, 0)
    OP_6E(500, 0)
    SetCameraDistance(18690, 0)
    SetChrPos(0x101, 62960, -1700, -37310, 90)
    SetChrPos(0x102, 64590, -1700, -38050, 0)
    SetChrPos(0x103, 63900, -1700, -35830, 180)
    SetChrPos(0x104, 65170, -1700, -36660, 270)
    SetCameraDistance(17690, 3000)
    FadeToBright(1000, 0)
    OP_0D()

    #C0014
    ChrTalk(
        0x101,
        (
            "#6P#0000F……看来，刚才那个应该就是\x01",
            "最后一只魔兽了。\x02",
        )
    )

    CloseMessageWindow()

    #C0015
    ChrTalk(
        0x103,
        (
            "#5P#0203F嗯，应该是的。\x02\x03",

            "#0200F废坑内已经\x01",
            "感觉不到魔兽的气息了。\x02",
        )
    )

    CloseMessageWindow()

    #C0016
    ChrTalk(
        0x104,
        (
            "#11P#0306F呼～终于搞定了啊。\x02\x03",

            "在这么大的一个废坑里走来走去，\x01",
            "实在累死人啦。\x02",
        )
    )

    CloseMessageWindow()

    #C0017
    ChrTalk(
        0x102,
        (
            "#12P#0100F呵呵，辛苦了。\x02\x03",

            "那么，罗伊德……\x01",
            "我们快回去\x01",
            "向镇长报告吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0018
    ChrTalk(
        0x101,
        "#6P#0000F嗯，好的。\x02",
    )

    CloseMessageWindow()

    #C0019
    ChrTalk(
        0x104,
        (
            "#11P#0306F呜……我已经走不动啦。\x02\x03",

            "#0309F……罗伊德。\x01",
            "背我到出口吧⊥\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    Sound(23, 0, 100, 0)
    Sleep(1000)

    #C0020
    ChrTalk(
        0x101,
        (
            "#6P#0003F我拒绝。\x02\x03",

            "#0000F别闹了，\x01",
            "快点走吧。\x02",
        )
    )

    CloseMessageWindow()

    #C0021
    ChrTalk(
        0x104,
        "#11P#0306F哼，薄情鬼。\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_29(0x1C, 0x1, 0x4)
    SetChrName("")
    SetMessageWindowPos(-1, 40, -1, -1)

    #A0022
    AnonymousTalk(
        0xFF,
        (
            scpstr(SCPSTR_CODE_COLOR, 0x5),
            "自动返回镇长家吗？\x07\x00",
            scpstr(0x18),
            scpstr(SCPSTR_CODE_ENTER),
        )
    )


    Menu(
        0,
        -1,
        -1,
        0,
        (
            "【返回镇长家】\x01",      # 0
            "【放弃】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_60(0x0)
    OP_57(0x0)
    OP_5A()
    SetMessageWindowPos(14, 280, 60, 3)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1087")
    StopBGM(0xFA0)
    WaitBGM()
    NewScene("t0510", 0, 0, 0)
    IdleLoop()
    Jump("loc_109A")

    label("loc_1087")

    SetChrPos(0x0, 63730, -1700, -33940, 180)
    EventEnd(0x5)

    label("loc_109A")

    Return()

    # Function_7_D80 end

    SaveToFile()

Try(main)
